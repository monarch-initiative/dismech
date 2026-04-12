---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T16:13:23.539098'
end_time: '2026-04-05T16:33:14.443804'
duration_seconds: 1190.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HPV-Negative Head and Neck Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 71
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HPV-Negative Head and Neck Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HPV-Negative Head and Neck Cancer** covering all of the
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
- **Disease Name:** HPV-Negative Head and Neck Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HPV-Negative Head and Neck Cancer** covering all of the
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


# HPV-Negative Head and Neck Cancer (HPV− HNSCC): Comprehensive Disease Characteristics Report

## Target disease
- **Disease name (preferred):** HPV-negative head and neck squamous cell carcinoma (HPV− HNSCC) (krsek2024theroleof pages 14-15, tasoulas2023geneticallyengineeredmouse pages 1-2)
- **Scope:** Squamous cell carcinomas arising in the **upper aerodigestive tract** (oral cavity, pharynx/oropharynx, larynx, hypopharynx) that are **HPV-independent** (tasoulas2023geneticallyengineeredmouse pages 1-2, xie2024immunelandscapein pages 1-2)
- **MONDO ID / MeSH / ICD:** **Not explicitly retrievable from the provided evidence** (placeholders recommended; see Artifact-00) (artifact-00)

| Field | Value |
|---|---|
| Preferred name | HPV-negative head and neck squamous cell carcinoma (HPV-negative HNSCC) (krsek2024theroleof pages 14-15, tasoulas2023geneticallyengineeredmouse pages 1-2) |
| Common synonyms | HPV− HNSCC; HPV-negative HNSCC; HPV-independent HNSCC; HPV-unrelated HNSCC; tobacco/alcohol-associated HNSCC (context-dependent); for oropharyngeal disease: HPV-negative OPSCC, p16-negative OPSCC, HPV-independent OPSCC (krsek2024theroleof pages 14-15, pakkanen2024simultaneousp53and pages 1-2, gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7) |
| Disease family | Head and neck squamous cell carcinoma (HNSCC), a squamous malignancy of the upper aerodigestive tract (tasoulas2023geneticallyengineeredmouse pages 1-2, xie2024immunelandscapein pages 1-2) |
| Typical anatomic subsites | Oral cavity, larynx, hypopharynx, and oropharynx; HNSCC arises from mucosal epithelium lining the oral cavity, pharynx, and larynx (tasoulas2023geneticallyengineeredmouse pages 1-2, xie2024immunelandscapein pages 1-2) |
| Oropharyngeal-specific terminology | In OPSCC, current classification distinguishes HPV-associated vs HPV-independent disease; p16 IHC is widely used as a surrogate marker, but p16-positive/HPV-negative discordance occurs, so confirmatory HPV nucleic-acid testing may be needed in selected cases (gallus2023accuracyofp16 pages 4-5, gallus2023accuracyofp16 pages 2-4, gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7) |
| Key classification note | WHO/AJCC framework separates HPV-associated OPSCC from HPV-independent/HPV-negative OPSCC because they are clinically and molecularly distinct entities with different prognosis (krsek2024theroleof pages 14-15, gallus2023accuracyofp16 pages 1-2) |
| p16 IHC note | p16 immunohistochemistry is an accepted practical surrogate for HPV-associated OPSCC, typically positive when >70% of tumor cells show strong nuclear and cytoplasmic staining; p16-negative OPSCC generally supports HPV-independent disease, but p16 alone is imperfect (pakkanen2024simultaneousp53and pages 1-2, gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7) |
| Distinguishing biology | HPV-negative disease is commonly linked to tobacco/alcohol exposure and frequently shows TP53 and CDKN2A alterations, unlike HPV-positive disease driven by viral E6/E7 biology (krsek2024theroleof pages 14-15, tasoulas2023geneticallyengineeredmouse pages 1-2) |
| MONDO ID | Not established from retrieved evidence; placeholder: MONDO: [not available from retrieved evidence] |
| MeSH | Placeholder: MeSH term for disease subset [not available from retrieved evidence]; broader family term HNSCC/head and neck neoplasms used in literature (tasoulas2023geneticallyengineeredmouse pages 1-2, xie2024immunelandscapein pages 1-2) |
| ICD-10 / ICD-11 | No single retrieved code specific to HPV-negative HNSCC subset; use site-specific head and neck SCC coding plus HPV-status modifiers where available; placeholder: ICD-10/11 [site-specific / not available from retrieved evidence] |
| Evidence source type | Aggregated disease-level literature and classification/guideline-style reviews, not individual EHR-derived records (krsek2024theroleof pages 14-15, tasoulas2023geneticallyengineeredmouse pages 1-2, gallus2023accuracyofp16 pages 1-2) |


*Table: This table summarizes practical names, synonyms, anatomic scope, and classification notes for HPV-negative head and neck squamous cell carcinoma. It is useful for harmonizing ontology mapping and terminology in a disease knowledge base when specific MONDO/MeSH/ICD identifiers are not directly available from the retrieved evidence.*

---

## 1. Disease information (concepts, definitions, identifiers)

### 1.1 Definition and current understanding
HPV− HNSCC refers to head and neck squamous cell carcinomas that are **not driven by transcriptionally active high-risk HPV** and are typically associated with carcinogen exposure (notably tobacco and alcohol), with a molecular landscape dominated by tumor-suppressor loss and high genomic instability (krsek2024theroleof pages 14-15, tasoulas2023geneticallyengineeredmouse pages 1-2, park2024advancedhumanpapillomavirus–negative pages 1-2).

In **oropharyngeal squamous cell carcinoma (OPSCC)**, HPV-associated and HPV-independent disease are now treated as clinically distinct entities because of differences in prognosis and biology; p16 immunohistochemistry (IHC) is widely used as a practical surrogate for HPV association but is imperfect (gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7).

### 1.2 Common synonyms / alternative names
- HPV− HNSCC; HPV-negative HNSCC; **HPV-independent** HNSCC; HPV-unrelated HNSCC (krsek2024theroleof pages 14-15, pakkanen2024simultaneousp53and pages 1-2)
- For OPSCC: HPV-negative OPSCC; p16-negative OPSCC; HPV-independent OPSCC (gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7)

### 1.3 Evidence source type
This report is based on aggregated disease-level resources (primary trials, registry studies, systematic reviews, translational studies), not individual EHR-only data (harrington2023pembrolizumabwithor pages 1-2, zhang2023causeofdeath pages 1-2, waas2024molecularcorrelatesfor pages 1-2).

---

## 2. Etiology

### 2.1 Primary causal factors and risk factors
**Carcinogen-associated etiology dominates HPV− disease.** Across HNSCC, tobacco and alcohol are repeatedly identified as major etiologic drivers, and HPV− tumors are enriched among patients with these exposures (krsek2024theroleof pages 14-15, xie2024immunelandscapein pages 1-2).

A 2023 review summarizing global burden states that **“at least 75% of HNSCCs are attributable to tobacco smoking and alcohol consumption”** and that combined heavy use confers a markedly increased risk (reported as **35-fold higher risk**) (huang2023circulatingtumourdna pages 1-2).

Other risk factors referenced in recent reviews include betel nut chewing and low socioeconomic status (tasoulas2023geneticallyengineeredmouse pages 1-2).

### 2.2 Protective factors
- **Risk-factor reduction:** tobacco and alcohol reduction are the most consistently supported protective measures for HPV− disease at the population level (huang2023circulatingtumourdna pages 1-2, gribb2023humanpapillomavirus pages 1-3).
- **HPV vaccination** prevents HPV-associated OPSCC (not HPV− tumors directly) but can change the population composition of OPSCC and is central for HPV+ prevention (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3, malagon2024epidemiologyofhpvassociated pages 1-4).

### 2.3 Gene–environment interactions
While the provided evidence does not include a formal G×E model, it links tobacco-associated carcinogenesis to:
- high mutational burden and copy-number alterations (CNAs) in HPV− tumors (park2024advancedhumanpapillomavirus–negative pages 1-2, huang2023circulatingtumourdna pages 4-6)
- loss of cell-cycle regulators and immunologic features consistent with an immunosuppressive/hypoxic tumor microenvironment (TME) (park2024advancedhumanpapillomavirus–negative pages 1-2).

---

## 3. Phenotypes (clinical manifestations) and quality of life

### 3.1 Anatomic distribution and staging (illustrative clinical cohorts)
A 2024 head and neck cancer survivor cohort (n=110) provides subsite and stage distributions: oral cavity 52.7%, oropharyngeal/nasopharyngeal 20.0%, pharyngeal 16.4%, larynx/hypopharynx 10.9%; stage III 32.7% and stage IV 27.3% (sharma2024dysphagiavoiceproblems pages 2-3). Although HPV status was not specified, these subsites and late-stage distributions are consistent with populations heavily enriched for HPV− disease in many settings.

### 3.2 Major symptom/survivorship phenotypes and suggested HPO terms
Post-treatment and survivorship phenotypes are prominent and clinically important:
- **Dysphagia** (HPO: **HP:0002015**) (sharma2024dysphagiavoiceproblems pages 1-2)
- **Voice impairment / hoarseness** (HPO: **HP:0001609** Dysphonia) (sharma2024dysphagiavoiceproblems pages 1-2)
- **Pain** (HPO: **HP:0012531**) (filippini2024healthrelatedqualityof pages 1-2)
- **Xerostomia** (HPO: **HP:0000217**) (filippini2024healthrelatedqualityof pages 1-2)
- **Weight loss / malnutrition** (HPO: **HP:0001824** Weight loss; **HP:0004395** Malnutrition) (filippini2024healthrelatedqualityof pages 1-2)

### 3.3 Quantitative QoL and symptom burden (recent data)
A 2024 survivor cohort reported very high prevalence of functional sequelae:
- Dysphagia in **85.5%** (94/110)
- Severe voice problems in **50%** (sharma2024dysphagiavoiceproblems pages 1-2, sharma2024dysphagiavoiceproblems pages 2-3)

In the same cohort, EORTC QLQ-C30 functional scores were relatively high for cognitive functioning (mean **80.76**) and role functioning (**80.30**), while symptoms included pain (mean **42.42**), fatigue (**42.22**), and financial difficulties (**41.21**) (sharma2024dysphagiavoiceproblems pages 1-2).

A 2024 systematic review of phase II/III trials emphasized dysphagia and speech problems as long-term burdens: dysphagia/dysarthria were described as affecting **~50% within the first year post-radiotherapy** with persistence in subsets for years, and treatment-associated weight loss (>5%) occurs in **66%** during therapy (filippini2024healthrelatedqualityof pages 1-2).

### 3.4 Suggested UBERON terms (anatomy)
- Oral cavity (UBERON:0000165)
- Oropharynx (UBERON:0001729)
- Larynx (UBERON:0001737)
- Hypopharynx (UBERON:0006562)

(UBERON IDs are standard ontology suggestions; not explicitly enumerated in the retrieved papers.)

---

## 4. Genetic / molecular information

### 4.1 Core somatic driver landscape (HPV−)
HPV− HNSCC is characterized by frequent tumor suppressor alterations and extensive CNAs (park2024advancedhumanpapillomavirus–negative pages 1-2, huang2023circulatingtumourdna pages 4-6).

A 2024 expert review focusing on advanced HPV− HNSCC reports mutation/alteration frequencies:
- **TP53 altered ~84%**
- **CDKN2A altered ~58%**
- **CCND1 altered ~31%**
- **PIK3CA altered ~34%**
and recurrent focal deletions including **NSD1, FAT1, NOTCH1, SMAD4** (park2024advancedhumanpapillomavirus–negative pages 1-2).

A ctDNA-focused 2023 review similarly emphasizes TP53 dominance and notes **TP53 mutations in 73–100%** of HPV− HNSCC in cited series, plus recurrent alterations impacting CCND1/CDKN2A, FAT1 (Wnt signaling activation), NOTCH pathway, EGFR CNV, and NRF2 pathway (smoking-associated) (huang2023circulatingtumourdna pages 4-6).

### 4.2 Copy number alterations and genomic subclasses
A 2024 Nature Communications study identifies a distinct HPV− oral cavity SCC subgroup with **no/few CNAs (“CNA-quiet”)** comprising **73/802 (9.1%)**, enriched for **wild-type TP53** and frequent **CASP8/HRAS** mutations, with a **less immunosuppressed TME (lower regulatory T-cell density)** and improved survival compared with CNA-other tumors (muijlwijk2024hallmarksofa pages 1-2).

### 4.3 Immune microenvironment and transcriptomic subtypes (2024)
A 2024 transcriptomic immune deconvolution analysis across >700 HPV− HNSCC cases assigns HPV− tumors into four molecular subtypes (classical, basal, mesenchymal, atypical) and reports:
- **Atypical and mesenchymal** subtypes show **greater immune enrichment** and **T-cell exhaustion phenotypes** relative to classical and basal
- distinct B-cell maturation/isotype patterns
- a hypothesis that treatments enhancing B-cell activity may benefit atypical subtypes (xie2024immunelandscapein pages 1-2, xie2024immunelandscapein pages 2-3).

### 4.4 Mechanistic pathways (GO term suggestions)
Key pathways and processes inferred from the evidence:
- **Cell-cycle dysregulation** (GO:0007049 cell cycle) via TP53/CDKN2A loss, CCND1 gain (park2024advancedhumanpapillomavirus–negative pages 1-2)
- **DNA damage response / genomic instability** (GO:0006974 cellular response to DNA damage stimulus) (huang2023circulatingtumourdna pages 4-6)
- **EGFR/PI3K/AKT signaling** (GO:0014066 regulation of phosphatidylinositol 3-kinase signaling; GO:0045744 negative regulation of G1/S transition) (park2024advancedhumanpapillomavirus–negative pages 1-2, huang2023circulatingtumourdna pages 4-6)
- **Hypoxia response** (GO:0001666 response to hypoxia) and immune suppression in tobacco-associated HPV− tumors (park2024advancedhumanpapillomavirus–negative pages 1-2)

### 4.5 Cell types (CL term suggestions)
- Squamous epithelial cells / keratinocytes (CL:0000312)
- Tumor-infiltrating CD8+ T cells (CL:0000625)
- Regulatory T cells (Treg) (CL:0000815)
- B cells (CL:0000236)

(Cell Ontology IDs are standard ontology suggestions; not explicitly enumerated in the retrieved papers.)

---

## 5. Environmental information

### 5.1 Lifestyle and environmental drivers
The strongest evidence-supported modifiable drivers for HPV− HNSCC remain:
- **Tobacco exposure**
- **Alcohol exposure**
with synergy increasing risk substantially (huang2023circulatingtumourdna pages 1-2).

---

## 6. Mechanism / pathophysiology (causal chain)

### 6.1 Upstream triggers to downstream disease
A consistent mechanistic model supported by recent reviews is:
1) **Carcinogen exposure** (tobacco/alcohol) → 2) **DNA damage and mutagenesis** → 3) **Loss of tumor suppressor control and cell-cycle checkpoint failure** (TP53, CDKN2A; CCND1 gains) → 4) **CNA accumulation and pathway rewiring** (EGFR/PI3K signaling; Wnt/NOTCH disruption; NRF2 oxidative stress response) → 5) **Immune evasion / hypoxic noninflamed TME** in many tumors → 6) **Invasion/metastasis and therapy resistance** (park2024advancedhumanpapillomavirus–negative pages 1-2, huang2023circulatingtumourdna pages 4-6).

### 6.2 HPV− immune escape and treatment resistance (expert analysis)
A 2024 HPV−-focused therapeutic review attributes worse outcomes partly to a **“noninflamed and hypoxic tumor microenvironment”** and reduced immune activation, including fewer CD8+ T cells and suppressed interferon pathway signals in tobacco-associated HPV− tumors (park2024advancedhumanpapillomavirus–negative pages 1-2).

---

## 7. Anatomical structures affected

Primary sites are the mucosal epithelium of the **oral cavity, pharynx (including oropharynx), larynx, and hypopharynx** (tasoulas2023geneticallyengineeredmouse pages 1-2, xie2024immunelandscapein pages 1-2). Complications and functional impacts reflect involvement of swallowing and voice structures in the upper aerodigestive tract (filippini2024healthrelatedqualityof pages 1-2, sharma2024dysphagiavoiceproblems pages 1-2).

---

## 8. Temporal development

### 8.1 Onset and course
HPV− HNSCC commonly presents in older patients and is frequently diagnosed at advanced stages in many settings (krsek2024theroleof pages 14-15, park2024advancedhumanpapillomavirus–negative pages 1-2). The clinical course varies by subsite and stage; survivorship can be characterized by prolonged functional impairment (dysphagia, xerostomia, speech/voice problems) especially after radiotherapy (filippini2024healthrelatedqualityof pages 1-2).

### 8.2 Staging frameworks
OPSCC staging has distinct HPV-associated vs HPV-independent rules under AJCC/UICC 8th edition; p16 status is incorporated into staging for OPSCC because of prognostic separation (gallus2023accuracyofp16 pages 1-2, tran2024advancesinhuman pages 6-7).

---

## 9. Inheritance and population

HPV− HNSCC is not typically a monogenic inherited disorder; it is best modeled as **multifactorial** (environmental carcinogens + somatic evolution). No germline inheritance pattern is supported by the provided evidence.

### Epidemiology highlights (recent quantitative data)
- **Global burden (GBD 2019 analysis, published 2024):** incidence **1,159,496** and deaths **554,146** for head and neck cancers in 2019, with ASIR **13.97** and ASDR **6.74** (zhou2024globalburdenof pages 1-2).
- **SEER OPSCC HPV testing trends (2010–2017):** testing increased from **21.95% (2010)** to **51.37% (2014)**; HPV-positive rates among tested OPSCC increased from **66.37% (2010)** to **79.32% (2016)** (kim2024aseerbasedanalysis pages 1-2).

---

## 10. Diagnostics

### 10.1 HPV testing and p16 IHC workflow (key concepts)
A guideline-aligned approach in the evidence base is:
1) **p16 IHC as initial screening** for OPSCC/selected HNSCC contexts, with **p16 positivity defined as >70% of tumor cells showing moderate-to-strong nuclear and cytoplasmic staining** (tran2024advancesinhuman pages 6-7).
2) **Confirmatory nucleic-acid testing** when clinical decisions depend on HPV-driven status (e.g., de-intensification or staging certainty), using DNA ISH/PCR or (preferably for transcriptional activity) **RNA ISH targeting E6/E7 mRNA** (tran2024advancesinhuman pages 6-7, gallus2023accuracyofp16 pages 2-4).

### 10.2 Discordance and false positives (quantitative)
p16 is sensitive but not fully specific. A 2024 review reported p16 overexpression in **93.2%** of HPV-positive OPSCC but also **18.8%** of HPV-negative patients; another cited series found **24%** p16 positivity in HPV16-negative tumors, suggesting non-HPV causes of p16 upregulation (e.g., inflammation/regeneration or p53-related biology) (tran2024advancesinhuman pages 6-6).

A 2023 analysis emphasizes that p16 false-positive rates depend on HPV prevalence in the tested population and warns that p16+/HPV− tumors can have prognosis similar to p16− tumors; thus confirmatory HPV nucleic-acid testing is recommended, especially in low-prevalence settings (gallus2023accuracyofp16 pages 1-2).

Table-based evidence of false-positive rates across populations and assays is shown in Table 1 from Gallus et al. (cropped table images) (gallus2023accuracyofp16 media 97554451, gallus2023accuracyofp16 media 6b48023a, gallus2023accuracyofp16 media 4f7617b0).

### 10.3 p16 + p53 immunostaining as a pragmatic classifier (2024)
A 2024 Head & Neck Pathology study proposes combined p16 and p53 IHC to classify HNSCC as:
- **HPV-associated (HPV-A): p16+/p53 wildtype**
- **HPV-independent (HPV-I): p16−/p53 abnormal (“mutant pattern”)**

In their cohort (n=31), 28/31 were straightforward; discordant cases were resolved with molecular testing. Adding p53 IHC increased the positive predictive value (PPV) of p16 positivity for HPV-A from **91.7% to 100%**; HPV-associated p53 patterns showed **specificity 100%** with **sensitivity 83%** (pakkanen2024simultaneousp53and pages 1-2, pakkanen2024simultaneousp53and pages 5-6).

### 10.4 Biomarkers beyond HPV status (liquid biopsy)
ctDNA is discussed as a biomarker for prognosis and surveillance in HNSCC due to tumor heterogeneity and sampling limitations; the cited review provides global burden and emphasizes the need for alternative sampling strategies, but does not provide HPV−-specific validated ctDNA thresholds in the excerpt (huang2023circulatingtumourdna pages 1-2).

---

## 11. Outcome / prognosis

HPV− OPSCC and HPV− HNSCC overall show substantially worse outcomes than HPV-associated disease, with strong population-level evidence.

| Evidence type/cohort | HPV-negative outcome metric | Comparator (if any) | Key quantitative results | Notes | URL/DOI |
|---|---|---|---|---|---|
| SEER OPSCC cohort, stage I-IVB, 2010-2015 (n=5,852) (zhang2023causeofdeath pages 1-2) | Cause-specific and competing mortality in HPV-negative OPSCC | HPV-positive OPSCC | 5-year head-and-neck cancer-specific mortality: **26.9%** vs **10.7%**; second primary cancer mortality: **12.4%** vs **4.6%**; non-cancer mortality: **13.7%** vs **5.8%**; HPV positivity associated with lower subdistribution hazards for HNCSM (**sHR 0.362**, 95% CI 0.315-0.417), SPCM (**0.400**, 0.321-0.496), NCCM (**0.460**, 0.378-0.560) (zhang2023causeofdeath pages 1-2) | Strong population-level evidence that HPV-negative OPSCC has substantially worse disease-specific and competing-cause outcomes than HPV-positive disease | https://doi.org/10.2196/47579 |
| General clinical prognosis in HPV-negative R/M HNSCC review (park2024advancedhumanpapillomavirus–negative pages 1-2) | Overall survival in advanced/recurrent disease | Not directly compared in same metric; contrasted conceptually with HPV-positive disease | Review states median OS for HPV-negative R/M HNSCC is approximately **1 year**, and approximately **6 months after progression** on PD-1/chemotherapy-based therapy (park2024advancedhumanpapillomavirus–negative pages 1-2) | Expert review frames HPV-negative disease as an unmet-need population with poorer outcomes partly related to tumor-suppressor loss and a noninflamed, hypoxic TME | https://doi.org/10.1158/1535-7163.MCT-24-0281 |
| Nature Communications biomarker study in HPV-negative HNSCC with PDX engraftment workflow; 273 resected specimens, molecular profiling subset n=88, validation cohort n=404 (waas2024molecularcorrelatesfor pages 1-2) | Prognostic biomarkers **LAMC2** and **TGM3** | Risk stratification beyond nodal status alone | Cohort disease-specific survival at 3 years was **71%** overall; engraftment correlated with worse outcomes and adverse features including N category (**p=0.022**), surgical margin (**p=0.037**), and nodal extracapsular extension (**p=0.038**); **LAMC2/TGM3 significantly improved prediction beyond nodal status alone** (waas2024molecularcorrelatesfor pages 1-2) | Biomarker-based prognostication may identify poor-risk HPV-negative patients even among node-negative cases; translational relevance from engraftment phenotype | https://doi.org/10.1038/s41467-024-55203-z |
| Nature Communications multicenter OCSCC cohort; HPV-negative oral cavity SCC, n=802 (muijlwijk2024hallmarksofa pages 1-2) | Prognosis of **CNA-quiet** HPV-negative subclass | CNA-other HPV-negative OCSCC | **73/802 (9.1%)** tumors were CNA-quiet; this subgroup had **better 5-year overall survival** than CNA-other tumors, with wild-type **TP53**, frequent **CASP8/HRAS** mutations, and **lower regulatory T-cell density** (muijlwijk2024hallmarksofa pages 1-2) | Identifies a favorable-prognosis biologic subset within otherwise generally poor-prognosis HPV-negative disease; also more common in older patients, women, and fewer current smokers | https://doi.org/10.1038/s41467-024-53390-3 |
| Molecular subtype immune-landscape analysis across >700 HPV-negative HNSCC patients (3 cohorts) (xie2024immunelandscapein pages 1-2, xie2024immunelandscapein pages 2-3) | Outcome heterogeneity within HPV-negative HNSCC | Internal comparison across HPV-negative molecular subtypes | Atypical and mesenchymal subtypes showed greater immune enrichment and T-cell exhaustion than classical/basal subtypes; study supports biologically distinct risk groups within HPV-negative disease, though no single pooled survival percentage is given in the excerpt (xie2024immunelandscapein pages 1-2, xie2024immunelandscapein pages 2-3) | Useful for prognosis refinement and future precision immunotherapy design in HPV-negative HNSCC | https://doi.org/10.1002/mc.23640 |
| Comparative prognosis statements from biomarker/review literature (krsek2024theroleof pages 14-15, xie2024immunelandscapein pages 1-2, tran2024advancesinhuman pages 2-3, tran2024advancesinhuman pages 2-2) | Overall and progression-free survival tendency in HPV-negative disease | HPV-positive HNSCC/OPSCC | Multiple reviews state HPV-positive tumors have higher OS/PFS and better radiosensitivity, whereas HPV-negative tumors are more heterogeneous and have worse outcomes; one cited comparison reported 3-year OS **57.1%** in HPV-negative vs **82.4%** in HPV-positive disease (tran2024advancesinhuman pages 2-3) | Broad consensus across recent literature that HPV-negative HNSCC/OPSCC carries inferior prognosis relative to HPV-positive disease | https://doi.org/10.1002/jmv.29746 |


*Table: This table summarizes key outcome evidence for HPV-negative HNSCC/OPSCC, including population-level mortality differences, prognostic biomarkers, and biologically distinct prognostic subgroups. It is useful for quickly identifying where HPV-negative disease has worse outcomes and which recent markers may refine risk stratification.*

Key quantitative evidence includes:
- SEER OPSCC 2010–2015: 5-year head-and-neck cancer-specific mortality **26.9% (HPV−)** vs **10.7% (HPV+)** (zhang2023causeofdeath pages 1-2).
- Translational prognostic biomarkers for HPV− HNSCC: **LAMC2 and TGM3** improved outcome prediction beyond nodal status in a validation cohort of **404** patients (waas2024molecularcorrelatesfor pages 1-2).
- A favorable HPV− oral cavity SCC subgroup (“CNA-quiet”, 9.1%) with lower Treg density and better survival (muijlwijk2024hallmarksofa pages 1-2).

---

## 12. Treatment

### 12.1 Standard-of-care (real-world implementation)
Across HPV status, core modalities remain **surgery, radiotherapy, and systemic therapy**, with immune checkpoint inhibitors now standard for recurrent/metastatic disease (krsek2024theroleof pages 14-15, harrington2023pembrolizumabwithor pages 1-2).

For recurrent/metastatic HNSCC, KEYNOTE-048 established pembrolizumab-based first-line therapy stratified by PD-L1 combined positive score (CPS). The updated JCO 2023 report concludes: **“With a 4-year follow-up, first-line pembrolizumab and pembrolizumab-chemotherapy continued to demonstrate survival benefit versus cetuximab-chemotherapy”** (harrington2023pembrolizumabwithor pages 1-2). This is particularly relevant to HPV− disease because HPV− tumors comprise a major proportion of R/M HNSCC.

| Study (year, journal) | Population | Comparator | Key efficacy results (OS/PFS/HR) | Notes re HPV-negative/p16 status | URL/DOI |
|---|---|---|---|---|---|
| Harrington et al. (2023, *J Clin Oncol*) | Phase III KEYNOTE-048; recurrent/metastatic HNSCC; n=882; median follow-up 45.0 months (IQR 41.0–49.2) (harrington2023pembrolizumabwithor pages 1-2, harrington2023pembrolizumabwithor pages 2-3) | Pembrolizumab alone or pembrolizumab + chemotherapy vs cetuximab-chemotherapy (EXTREME-like control) (harrington2023pembrolizumabwithor pages 1-2, harrington2023pembrolizumabwithor pages 2-3) | **Pembrolizumab monotherapy OS:** CPS ≥20: 14.9 vs 10.8 mo, HR 0.61 (95% CI 0.46–0.81); CPS ≥1: 12.3 vs 10.4 mo, HR 0.74 (0.61–0.89); total population: 11.5 vs 10.7 mo, HR 0.81 (0.68–0.97; noninferior). **Pembrolizumab + chemotherapy OS:** CPS ≥20 HR 0.62 (0.46–0.84); CPS ≥1 HR 0.64 (0.53–0.78); total population HR 0.71 (0.59–0.85). **PFS2:** improved in key PD-L1 groups; e.g., pembrolizumab CPS ≥20 HR 0.64, CPS ≥1 HR 0.79; pembrolizumab-chemo CPS ≥1 HR 0.66. 4-year follow-up continued to show survival benefit (harrington2023pembrolizumabwithor pages 1-2, harrington2023pembrolizumabwithor pages 2-3) | Trial stratified by p16 status for oropharyngeal cancers; subgroup analyses generally favored pembrolizumab in HPV-negative or smoking-associated disease, making results highly relevant to HPV-negative R/M HNSCC even though efficacy was reported primarily by PD-L1 CPS rather than HPV status (harrington2023pembrolizumabwithor pages 1-2) | https://doi.org/10.1200/JCO.21.02508 |
| Oridate et al. (2024, *Int J Clin Oncol*) | Japanese KEYNOTE-048 cohort; R/M HNSCC; n=67; pembrolizumab n=23, pembrolizumab-chemo n=25, EXTREME n=19; median follow-up 71.0 months (range 61.2–81.5) (oridate2024firstlinepembrolizumabwith pages 1-2) | Pembrolizumab or pembrolizumab + chemotherapy vs EXTREME (oridate2024firstlinepembrolizumabwith pages 1-2) | **5-year OS, pembrolizumab vs EXTREME:** CPS ≥20: 35.7% vs 12.5%, HR 0.38 (95% CI 0.13–1.05); CPS ≥1: 23.8% vs 12.5%, HR 0.70 (0.34–1.45); total: 30.4% vs 10.5%, HR 0.54 (0.27–1.07). **Pembrolizumab-chemo vs EXTREME:** CPS ≥20: 20.0% vs 14.3%, HR 0.79 (0.27–2.33); CPS ≥1: 10.5% vs 14.3%, HR 1.18 (0.56–2.48); total: 8.0% vs 12.5%, HR 1.11 (0.57–2.16). Earlier analysis cited median OS in CPS ≥20: 28.2 vs 13.3 mo, HR 0.29 (0.09–0.89) (oridate2024firstlinepembrolizumabwith pages 1-2) | Stratified by p16/HPV status for oropharyngeal cancers and PD-L1 22C3 CPS. Small subgroup study, but useful for long-term survivorship benchmarks in HPV-negative–relevant clinical populations (oridate2024firstlinepembrolizumabwith pages 1-2) | https://doi.org/10.1007/s10147-024-02632-x |
| Black et al. (2023, *Front Oncol*) | Real-world US 1L pembrolizumab in R/M HNSCC; n=646 analyzed (431 pembrolizumab monotherapy; 215 pembrolizumab + chemotherapy); median follow-up 8.3 mo (range 0.0–35.1) (black2023realworldtreatmentpatterns pages 1-2, black2023realworldtreatmentpatterns pages 8-9, black2023realworldtreatmentpatterns pages 3-5, black2023realworldtreatmentpatterns pages 5-6) | Observational comparison of pembrolizumab monotherapy vs pembrolizumab + chemotherapy; no randomized control arm (black2023realworldtreatmentpatterns pages 1-2, black2023realworldtreatmentpatterns pages 3-5) | **Pembrolizumab monotherapy:** rwOS 12.1 mo (95% CI 9.2–15.1), rwToT 4.2 mo (3.5–4.6), rwTTNT 6.5 mo (5.4–7.4). **Pembrolizumab + chemotherapy:** rwOS 11.9 mo (9.0–16.0), rwToT 4.9 mo (3.8–5.6), rwTTNT 6.6 mo (5.8–8.3). Survival rates overall: 6 mo 68.0%, 12 mo 50.3%, 24 mo 33.5% (black2023realworldtreatmentpatterns pages 1-2, black2023realworldtreatmentpatterns pages 8-9, black2023realworldtreatmentpatterns pages 3-5) | HPV-positive status and lower ECOG PS were associated with longer rwOS; monotherapy was less likely in HPV-negative tumors. Thus, HPV-negative patients likely represent a poorer-prognosis fraction of the real-world cohort, supporting use of these data as pragmatic context for HPV-negative disease (black2023realworldtreatmentpatterns pages 1-2, black2023realworldtreatmentpatterns pages 3-5, black2023realworldtreatmentpatterns pages 5-6) | https://doi.org/10.3389/fonc.2023.1160144 |
| Cirillo et al. (2024, *BMC Cancer*) | Single-center retrospective real-world cohort; PD-L1-positive R/M HNSCC treated Feb 2021–Mar 2023; n=92 received pembrolizumab-based 1L therapy (cirillo2024pembrolizumabbasedfirstlinetreatment pages 1-2) | Pembrolizumab monotherapy vs pembrolizumab-based chemoimmunotherapy in routine practice (cirillo2024pembrolizumabbasedfirstlinetreatment pages 1-2) | Median PFS 4 mo; median OS 8 mo overall. Pembrolizumab monotherapy had worse OS than chemoimmunotherapy (log-rank p=.001; HR 2.7). Outcomes improved with CPS ≥20: PFS HR 0.50 (p=.005); OS HR 0.57 (p=.04). ECOG PS2 independently associated with worse PFS and OS. Authors note that, unlike KEYNOTE-048, pembrolizumab regimens did not show statistically significant PFS/ORR improvement in trial reports and that OS curves plateaued in ~20–30% by 4 years (cirillo2024pembrolizumabbasedfirstlinetreatment pages 1-2) | HPV status incorporated in disease framing but not the primary analytic stratifier. Findings are relevant to HPV-negative disease because frailer real-world patients often include poorer-risk HPV-negative tumors and because PD-L1-positive R/M HNSCC practice decisions often mirror those in HPV-negative populations (cirillo2024pembrolizumabbasedfirstlinetreatment pages 1-2) | https://doi.org/10.1186/s12885-024-12155-3 |


*Table: This table summarizes pivotal trial and real-world evidence for first-line systemic therapy in recurrent/metastatic HNSCC, emphasizing findings most relevant to HPV-negative disease. It highlights long-term KEYNOTE-048 results, Japanese 5-year follow-up, and real-world pembrolizumab outcomes for practical comparison.*

### 12.2 Real-world evidence (2023–2024)
A large US real-world cohort (published 22 May 2023) evaluated first-line pembrolizumab in R/M HNSCC and reported median real-world OS (rwOS) ~12 months in both pembrolizumab monotherapy and pembrolizumab+chemotherapy groups; HPV-positive status was associated with longer rwOS, implying HPV− patients are an adverse-risk subset in practice (black2023realworldtreatmentpatterns pages 1-2, black2023realworldtreatmentpatterns pages 3-5).

### 12.3 HPV-negative-specific unmet need and emerging strategies (expert view)
A 2024 HPV−-focused therapeutic review emphasizes that durable responses to PD-1 blockade occur in only a subset, and cetuximab responses are “short-lived,” with resistance linked to **EGFR–c-MET pathway crosstalk**, motivating dual-targeting strategies in HPV− disease (park2024advancedhumanpapillomavirus–negative pages 1-2).

### 12.4 HPV−/p16− clinical trials (examples)
HPV−-restricted (or explicitly p16−/HPV-unrelated) trials in the retrieved ClinicalTrials.gov evidence include neoadjuvant immunoradiotherapy strategies and combined immunotherapy-RT regimens (NCT03624231 chunk 1, NCT03635164 chunk 2, NCT06161545 chunk 1).

| NCT | Population (HPV-/p16-) | Setting | Interventions | Phase | Status | Enrollment | Primary endpoint(s) | Notes |
|---|---|---|---|---|---|---:|---|---|
| NCT03624231 | Non-resectable, locally advanced HPV-negative/p16-negative HNSCC; central confirmation required; p16 negativity defined as ≤70% stained cells (NCT03624231 chunk 1, NCT03624231 chunk 2) | Definitive non-surgical local therapy | Arm 1: durvalumab + tremelimumab + radiotherapy; Arm 2: durvalumab + radiotherapy (NCT03624231 chunk 1, NCT03624231 chunk 2) | Phase II (NCT03624231 chunk 1) | Completed (NCT03624231 chunk 1) | 18 | Feasibility (treatment discontinuations due to toxicity) and efficacy including 1-year progression-free survival; also in-field PFS and 1-year distant metastasis-free survival (NCT03624231 chunk 1) | Arm 1 was stopped after interim analyses; QoL endpoints included EORTC QLQ-H&N35 and QLQ-C30 (NCT03624231 chunk 1) |
| NCT03635164 | Resectable HPV- and/or p16-negative intermediate/high-risk HNSCC; excludes p16-positive OPSCC (NCT03635164 chunk 2) | Neoadjuvant preoperative therapy before surgery | Radiotherapy/SBRT with durvalumab prior to surgical resection (NCT03635164 chunk 2) | Phase I/Ib suggested in record text (NCT03635164 chunk 2) | Completed (from trial search result) (NCT03635164 chunk 2) | 21 | Not explicitly reported in retrieved chunk; trial described as neoadjuvant RT + durvalumab with planned FACT H&N v4 QoL collection (NCT03635164 chunk 2) | University of Colorado study; window-style preoperative immunoradiotherapy approach (NCT03635164 chunk 2) |
| NCT03389477 | p16INK4a-negative, HPV-unrelated HNSCC (trial retrieval listing) | Multimodality treatment around chemoradiation | Neoadjuvant palbociclib monotherapy, concurrent chemoradiation, then adjuvant palbociclib monotherapy (trial retrieval listing) | Phase II (trial retrieval listing) | Active, not recruiting (trial retrieval listing) | 26 | Not available in retrieved evidence chunks | Explicitly designed for HPV-unrelated/p16-negative disease; detailed endpoints not available in retrieved chunks (trial retrieval listing) |
| NCT06935188 | HPV-negative, anti-PD-1-resistant recurrent/metastatic HNSCC (trial retrieval listing) | Recurrent/metastatic, post–PD-1 resistance | Dalpiciclib plus cetuximab vs cetuximab alone (trial retrieval listing) | Phase II (trial retrieval listing) | Recruiting (trial retrieval listing) | 98 | Not available in retrieved evidence chunks | Targets CDK4/6 + EGFR strategy in resistant HPV-negative disease; detailed endpoints not available in retrieved chunks (trial retrieval listing) |
| NCT05879484 | PD-L1-positive, HPV-negative recurrent/metastatic HNSCC in phase II; phase Ib included broader SCC populations including HPV-positive and HPV-negative patients (NCT05879484 chunk 1) | Front-line recurrent/metastatic systemic therapy | Pembrolizumab + valemetostat (EZH1/2 dual inhibitor) (NCT05879484 chunk 1) | Phase Ib/II (NCT05879484 chunk 1) | Withdrawn (NCT05879484 chunk 1) | 0 | Phase II disease control rate; Phase Ib safety/RP2D; secondary endpoints included PK, OS, and 6-month PFS (NCT05879484 chunk 1) | Study never opened because CRADA was never executed (NCT05879484 chunk 1) |
| NCT06161545 | Resectable HPV-unrelated HNSCC; for oropharyngeal tumors, p16-negative status specified (NCT06161545 chunk 1) | Neoadjuvant window-of-opportunity, resectable disease | Arm 1: pembrolizumab + N-803; Arm 2: pembrolizumab + N-803 + PD-L1 t-haNK cells (NCT06161545 chunk 1) | Phase II (NCT06161545 chunk 1) | Recruiting (NCT06161545 chunk 1) | 40 | Pathologic tumor response (≤50% viable tumor in resected primary tumor bed) (NCT06161545 chunk 1) | Secondary endpoints include safety, recurrence-free survival, and overall survival at 1 and 2 years (NCT06161545 chunk 1) |
| NCT02358031 | Reference trial in untreated recurrent/metastatic HNSCC; stratified by p16 status for oropharyngeal cancers rather than restricted to HPV-negative disease (harrington2023pembrolizumabwithor pages 1-2, oridate2024firstlinepembrolizumabwith pages 1-2) | First-line recurrent/metastatic benchmark | Pembrolizumab alone or pembrolizumab + chemotherapy vs cetuximab-chemotherapy (harrington2023pembrolizumabwithor pages 1-2, oridate2024firstlinepembrolizumabwith pages 1-2) | Phase III (harrington2023pembrolizumabwithor pages 1-2) | Completed/long-term follow-up reported (harrington2023pembrolizumabwithor pages 1-2, oridate2024firstlinepembrolizumabwith pages 1-2) | 882 overall; Japanese subgroup 67 (harrington2023pembrolizumabwithor pages 1-2, oridate2024firstlinepembrolizumabwith pages 1-2) | Overall survival and progression-free survival by PD-L1 CPS; updated analyses also reported PFS2 (harrington2023pembrolizumabwithor pages 1-2, harrington2023pembrolizumabwithor pages 2-3) | Practice-changing reference standard for R/M HNSCC; highly relevant comparator for HPV-negative populations though not HPV-negative-exclusive (harrington2023pembrolizumabwithor pages 1-2, oridate2024firstlinepembrolizumabwith pages 1-2) |


*Table: This table summarizes retrieved ClinicalTrials.gov studies and one pivotal reference trial relevant to HPV-negative or p16-negative HNSCC. It highlights populations, treatment settings, interventions, phases, endpoints, and key operational notes such as interim stopping or withdrawal.*

### 12.5 MAXO (treatment action ontology) suggestions
- Surgery (MAXO: surgical procedure)
- Radiotherapy (MAXO: radiation therapy)
- Platinum-based chemotherapy (MAXO: chemotherapy)
- Anti–PD-1 therapy (pembrolizumab/nivolumab) (MAXO: immunotherapy)
- Anti-EGFR therapy (cetuximab) (MAXO: targeted therapy)

(MAXO IDs are suggested categories; not explicitly enumerated in the retrieved evidence.)

---

## 13. Prevention

### 13.1 Primary prevention (HPV− relevance)
Because tobacco and alcohol account for a large proportion of HNSCC burden and are central in HPV− etiology, **risk-factor reduction is the most direct prevention strategy** for HPV− disease (huang2023circulatingtumourdna pages 1-2, gribb2023humanpapillomavirus pages 1-3).

A prevention-oriented review explicitly states: **“The main risk factors for oropharyngeal SCCa have been multi-factorial, including tobacco and alcohol use”** (published April 2023) (gribb2023humanpapillomavirus pages 1-3).

### 13.2 HPV vaccination (indirect relevance to HPV− burden)
HPV vaccination is the primary prevention strategy for HPV-associated OPSCC and may alter relative proportions of HPV− vs HPV+ OPSCC over time.

A 2023 public policy review reports vaccine efficacy against oral HPV infection of **88–93%**, and notes that as of 2022, **122/195 (63%)** WHO member states had national HPV vaccination programs, with **41/122 (34%)** gender-neutral coverage (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3). A 2024 Nature Reviews Clinical Oncology review notes HPV is attributed to **31% of oropharyngeal cancers worldwide** and that vaccination will likely prevent HPV-associated cancers beyond cervical cancer (malagon2024epidemiologyofhpvassociated pages 1-4).

---

## 14. Other species / natural disease

No naturally occurring HPV− HNSCC analogue in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms and experimental systems (HPV− translational research)

Preclinical work in HPV− HNSCC relies on complementary in vitro and in vivo model classes, with **4NQO carcinogen models**, **PDX**, and **GEMMs/transposon systems** being particularly prominent for carcinogen-associated biology.

| Model type | What it captures (strengths) | Key limitations | Typical use-cases |
|---|---|---|---|
| Cell lines / 2D cultures | Inexpensive, fast, easy to maintain and genetically manipulate; useful for mechanistic studies, pathway perturbation, and high-throughput drug screening; some patient-derived short-term cultures retain features of source tumors better than long-passaged lines (chaves2023preclinicalmodelsin pages 3-4, chaves2023preclinicalmodelsin pages 2-3, tinhofer2020preclinicalmodelsof pages 4-5) | Poorly recapitulate native histology and tumor microenvironment; prone to clonal selection, genomic instability, and drift from original tumors; limited immune/stromal context (chaves2023preclinicalmodelsin pages 3-4, chaves2023preclinicalmodelsin pages 2-3, tinhofer2020preclinicalmodelsof pages 4-5) | Rapid target validation, signaling studies, CRISPR/RNAi perturbation, initial drug sensitivity and resistance screens (chaves2023preclinicalmodelsin pages 3-4, tinhofer2020preclinicalmodelsof pages 4-5) |
| Spheroids / organoids (3D) | Better preserve 3D architecture, intratumoral heterogeneity, and diffusion barriers; can model slower proliferation, reduced drug penetration, and increased treatment resistance; patient-derived organoids can retain genomic and histologic characteristics of parent tumors (chaves2023preclinicalmodelsin pages 3-4, chaves2023preclinicalmodelsin pages 2-3, tinhofer2020preclinicalmodelsof pages 4-5) | Technically more complex; still being standardized; time- and cost-intensive; extracellular matrix dependence and incomplete immune/stromal representation unless specifically reconstituted (chaves2023preclinicalmodelsin pages 3-4, tinhofer2020preclinicalmodelsof pages 4-5) | Ex vivo drug testing, personalized therapy assessment, plasticity/EMT studies, modeling cisplatin resistance and heterogeneous treatment response (chaves2023preclinicalmodelsin pages 3-4, tinhofer2020preclinicalmodelsof pages 4-5) |
| Microfluidic / organotypic / host–microbe co-culture models | Preserve tissue architecture and enable study of epithelial-stromal-immune and microbiome interactions under controlled conditions; useful for dissecting host–bacterial interactions relevant to oral/HPV-negative carcinogenesis (chaves2023preclinicalmodelsin pages 3-4, chaves2023preclinicalmodelsin pages 2-3, tasoulas2023geneticallyengineeredmouse pages 5-7) | Expensive, labor-intensive, lower throughput; technical setup can limit widespread adoption; often lack full systemic physiology (chaves2023preclinicalmodelsin pages 3-4, chaves2023preclinicalmodelsin pages 2-3) | Tumor–microenvironment crosstalk, microbiome-cancer interaction studies, invasion assays, testing local immune or stromal modulation (chaves2023preclinicalmodelsin pages 3-4, tasoulas2023geneticallyengineeredmouse pages 5-7) |
| Patient-derived xenografts (PDX) | Retain tumor histology, genetics, and heterogeneity; often correlate with aggressiveness; useful bridge between patient tumors and in vivo therapeutic testing; can support derivation of secondary cultures/organoids (chaves2023preclinicalmodelsin pages 2-3, tinhofer2020preclinicalmodelsof pages 4-5, zohud2023towardssystemgenetics pages 2-3) | Time-consuming and expensive; mouse microenvironment replaces human stroma over time; standard PDX lack intact human immunity, limiting immunotherapy studies; prolonged passaging risks divergence (chaves2023preclinicalmodelsin pages 2-3, tinhofer2020preclinicalmodelsof pages 4-5, zohud2023towardssystemgenetics pages 2-3) | Biomarker discovery, in vivo efficacy testing, resistance modeling, translational validation of poor-prognosis molecular phenotypes in HPV-negative HNSCC (chaves2023preclinicalmodelsin pages 2-3, waas2024molecularcorrelatesfor pages 1-2, zohud2023towardssystemgenetics pages 2-3) |
| 4NQO carcinogen mouse model | Immunocompetent carcinogen-induced model that closely resembles multistep oral carcinogenesis and tobacco-associated disease; preserves genetic heterogeneity and native immune context; useful for initiation-to-progression studies and immunotherapy development (tinhofer2020preclinicalmodelsof pages 4-5, chaves2023preclinicalmodelsin pages 3-4, tasoulas2023geneticallyengineeredmouse pages 5-7) | Long latency (often many months, with metastasis studies taking longer); tumor onset can be variable; strongest for oral cavity/tongue rather than all head and neck subsites (tinhofer2020preclinicalmodelsof pages 4-5, chaves2023preclinicalmodelsin pages 3-4, tasoulas2023geneticallyengineeredmouse pages 5-7) | Studying carcinogenesis, premalignant-to-malignant transition, immune suppression, chemoprevention, and testing therapies in tobacco-mimetic HPV-negative settings (tinhofer2020preclinicalmodelsof pages 4-5, chaves2023preclinicalmodelsin pages 3-4) |
| GEMMs / transposon-based mouse models | Allow causal testing of specific drivers in controlled genetic backgrounds; can recapitulate stromal and immune microenvironments because tumors arise in situ; luciferase/reporters can enable longitudinal tracking; transposon systems accelerate identification of cooperating genes (tasoulas2023geneticallyengineeredmouse pages 5-7, tinhofer2020preclinicalmodelsof pages 4-5) | Often costly and slow; low incidence or incomplete penetrance in some models; some require added carcinogen (e.g., 4NQO) to produce frank malignancy; many available models are not fully representative of human HPV-negative oropharyngeal disease (tasoulas2023geneticallyengineeredmouse pages 5-7, tinhofer2020preclinicalmodelsof pages 4-5, zohud2023towardssystemgenetics pages 2-3) | Functional validation of TP53/CDKN2A/FAT1/PIK3CA-type drivers, lineage and progression studies, immune-oncology experiments, modeling initiation and metastatic spread in vivo (tasoulas2023geneticallyengineeredmouse pages 5-7, tinhofer2020preclinicalmodelsof pages 4-5) |


*Table: This table summarizes the main preclinical systems used to study HPV-negative head and neck squamous cell carcinoma, highlighting what each model captures, its limitations, and its best-fit applications. It is useful for matching a research question to the most appropriate model platform.*

Key expert consensus points:
- **4NQO**: immunocompetent and resembles multistep oral carcinogenesis but with long latency (tinhofer2020preclinicalmodelsof pages 4-5, chaves2023preclinicalmodelsin pages 3-4).
- **PDX**: preserves heterogeneity but lacks human immunity and is resource intensive (chaves2023preclinicalmodelsin pages 2-3, zohud2023towardssystemgenetics pages 2-3).
- **GEMMs**: enable causal tests of TP53/CDKN2A-type drivers; some need 4NQO to achieve frank malignancy (tasoulas2023geneticallyengineeredmouse pages 5-7).

---

# Recent developments (2023–2024 emphasis) and “expert opinions” (authoritative synthesis)

1) **HPV− molecular stratification is maturing**: HPV− HNSCC is not a single entity; transcriptomic subtype immune landscapes (classical/basal/mesenchymal/atypical) and CNA-quiet genomic subclasses support precision stratification and trial design (xie2024immunelandscapein pages 2-3, muijlwijk2024hallmarksofa pages 1-2).

2) **Immune checkpoint therapy is standard but insufficient**: KEYNOTE-048 continues to support pembrolizumab-based first-line R/M therapy with durable benefit in subsets, while HPV−-specific reviews emphasize a noninflamed/hypoxic TME and tumor suppressor loss contributing to resistance (harrington2023pembrolizumabwithor pages 1-2, park2024advancedhumanpapillomavirus–negative pages 1-2).

3) **Diagnostics are shifting toward multimodal confirmation**: Recognition of p16 discordance and false positives supports confirmatory HPV nucleic-acid testing and/or combined p16+p53 IHC approaches to classify HPV-associated vs HPV-independent tumors, especially where treatment decisions depend on HPV status (pakkanen2024simultaneousp53and pages 5-6, tran2024advancesinhuman pages 6-7, gallus2023accuracyofp16 media 97554451).

---

# Notes on evidence gaps (from retrieved sources)

- A single MONDO/ICD/MeSH identifier for “HPV-negative HNSCC” was not explicitly retrievable in the provided evidence; operationally, this entity is captured via **site-specific HNSCC diagnosis + HPV-negative/HPV-independent classification** (artifact-00).
- The provided phenotypic evidence is strongest for survivorship QoL and treatment sequelae; classic presenting symptoms (e.g., neck mass, odynophagia, hoarseness) are widely known clinically but were not explicitly enumerated in the retrieved excerpts.

---

## Embedded visual evidence
- p16 IHC false-positive rates across populations and assays (Table 1 cropped images) (gallus2023accuracyofp16 media 97554451, gallus2023accuracyofp16 media 6b48023a, gallus2023accuracyofp16 media 4f7617b0).

References

1. (krsek2024theroleof pages 14-15): Antea Krsek, Lara Baticic, Vlatka Sotosek, and Tamara Braut. The role of biomarkers in hpv-positive head and neck squamous cell carcinoma: towards precision medicine. Diagnostics, 14:1448, Jul 2024. URL: https://doi.org/10.3390/diagnostics14131448, doi:10.3390/diagnostics14131448. This article has 26 citations.

2. (tasoulas2023geneticallyengineeredmouse pages 1-2): Jason Tasoulas, Sonal Srivastava, Xiaonan Xu, Valentina Tarasova, Anastasios Maniakas, Florian A. Karreth, and Antonio L. Amelio. Genetically engineered mouse models of head and neck cancers. Oncogene, 42:2593-2609, Jul 2023. URL: https://doi.org/10.1038/s41388-023-02783-7, doi:10.1038/s41388-023-02783-7. This article has 15 citations and is from a domain leading peer-reviewed journal.

3. (xie2024immunelandscapein pages 1-2): Mengyu Xie, Ritu Chaudhary, Robbert J. C. Slebos, Kyubum Lee, Feifei Song, Maria I. Poole, Dirk S. Hoening, Leenil C. Noel, Juan C. Hernandez‐Prera, Jose R. Conejo‐Garcia, Christine H. Chung, and Aik Choon Tan. Immune landscape in molecular subtypes of human papillomavirus‐negative head and neck cancer. Molecular Carcinogenesis, 63:120-135, Sep 2024. URL: https://doi.org/10.1002/mc.23640, doi:10.1002/mc.23640. This article has 3 citations and is from a peer-reviewed journal.

4. (pakkanen2024simultaneousp53and pages 1-2): Pihla Pakkanen, Antti Silvoniemi, Katri Aro, Leif Bäck, Heikki Irjala, Leena-Maija Aaltonen, Jaana Hagström, Caj Haglund, Jukka Laine, Heikki Minn, and Jutta Huvila. Simultaneous p53 and p16 immunostaining for molecular subclassification of head and neck squamous cell carcinomas. Head and Neck Pathology, Aug 2024. URL: https://doi.org/10.1007/s12105-024-01680-z, doi:10.1007/s12105-024-01680-z. This article has 6 citations and is from a peer-reviewed journal.

5. (gallus2023accuracyofp16 pages 1-2): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

6. (tran2024advancesinhuman pages 6-7): Ngoc Ha Tran, Dayna Sais, and Nham Tran. Advances in human papillomavirus detection and molecular understanding in head and neck cancers: implications for clinical management. Journal of Medical Virology, Jun 2024. URL: https://doi.org/10.1002/jmv.29746, doi:10.1002/jmv.29746. This article has 27 citations and is from a peer-reviewed journal.

7. (gallus2023accuracyofp16 pages 4-5): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

8. (gallus2023accuracyofp16 pages 2-4): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

9. (park2024advancedhumanpapillomavirus–negative pages 1-2): Robin Park and Christine H. Chung. Advanced human papillomavirus–negative head and neck squamous cell carcinoma: unmet need and emerging therapies. Molecular Cancer Therapeutics, 23:1717-1730, Sep 2024. URL: https://doi.org/10.1158/1535-7163.mct-24-0281, doi:10.1158/1535-7163.mct-24-0281. This article has 9 citations and is from a peer-reviewed journal.

10. (harrington2023pembrolizumabwithor pages 1-2): Kevin J. Harrington, Barbara Burtness, Richard Greil, Denis Soulières, Makoto Tahara, Gilberto de Castro, Amanda Psyrri, Irene Brana, Neus Basté, Prakash Neupane, Åse Bratland, Thorsten Fuereder, Brett G.M. Hughes, Ricard Mesia, Nuttapong Ngamphaiboon, Tamara Rordorf, Wan Zamaniah Wan Ishak, Jianxin Lin, Burak Gumuscu, Ramona F. Swaby, and Danny Rischin. Pembrolizumab with or without chemotherapy in recurrent or metastatic head and neck squamous cell carcinoma: updated results of the phase iii keynote-048 study. Journal of Clinical Oncology, 41:790-802, Feb 2023. URL: https://doi.org/10.1200/jco.21.02508, doi:10.1200/jco.21.02508. This article has 541 citations and is from a highest quality peer-reviewed journal.

11. (zhang2023causeofdeath pages 1-2): Dong-Dong Zhang, Min Lei, Yue Wang, Pei-Ji Zeng, Yong-Jun Hong, and Cheng-Fu Cai. Cause of death in patients with oropharyngeal carcinoma by human papillomavirus status: comparative data analysis. JMIR Public Health and Surveillance, 9:e47579, Aug 2023. URL: https://doi.org/10.2196/47579, doi:10.2196/47579. This article has 6 citations and is from a peer-reviewed journal.

12. (waas2024molecularcorrelatesfor pages 1-2): Matthew Waas, Christina Karamboulas, Benson Z. Wu, Shahbaz Khan, Stephanie Poon, Jalna Meens, Meinusha Govindarajan, Amanda Khoo, Salvador Mejia-Guerrero, Annie Ha, Lydia Y. Liu, Kevin C. J. Nixon, Joseph Walton, Scott V. Bratman, Shao Hui Huang, David Goldstein, Federico Gaiti, Laurie Ailles, and Thomas Kislinger. Molecular correlates for hpv-negative head and neck cancer engraftment prognosticate patient outcomes. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55203-z, doi:10.1038/s41467-024-55203-z. This article has 12 citations and is from a highest quality peer-reviewed journal.

13. (huang2023circulatingtumourdna pages 1-2): Xiaomin Huang, Pascal H. G. Duijf, Sharath Sriram, Ganganath Perera, Sarju Vasani, Lizbeth Kenny, Paul Leo, and Chamindie Punyadeera. Circulating tumour dna alterations: emerging biomarker in head and neck squamous cell carcinoma. Journal of Biomedical Science, Aug 2023. URL: https://doi.org/10.1186/s12929-023-00953-z, doi:10.1186/s12929-023-00953-z. This article has 36 citations and is from a domain leading peer-reviewed journal.

14. (gribb2023humanpapillomavirus pages 1-3): Jacob P. Gribb, John H. Wheelock, and Etern S. Park. Human papilloma virus (hpv) and the current state of oropharyngeal cancer prevention and treatment. Delaware Journal of Public Health, 9:26-28, Apr 2023. URL: https://doi.org/10.32481/djph.2023.04.008, doi:10.32481/djph.2023.04.008. This article has 42 citations.

15. (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3): Sifon Ndon, Amritpal Singh, Patrick K. Ha, Joyce Aswani, Jason Ying-Kuen Chan, and Mary Jue Xu. Human papillomavirus-associated oropharyngeal cancer: global epidemiology and public policy implications. Cancers, 15:4080, Aug 2023. URL: https://doi.org/10.3390/cancers15164080, doi:10.3390/cancers15164080. This article has 58 citations.

16. (malagon2024epidemiologyofhpvassociated pages 1-4): Talía Malagón, Eduardo L. Franco, Romina Tejada, and Salvatore Vaccarella. Epidemiology of hpv-associated cancers past, present and future: towards prevention and elimination. Nature Reviews Clinical Oncology, 21:522-538, May 2024. URL: https://doi.org/10.1038/s41571-024-00904-z, doi:10.1038/s41571-024-00904-z. This article has 137 citations and is from a domain leading peer-reviewed journal.

17. (huang2023circulatingtumourdna pages 4-6): Xiaomin Huang, Pascal H. G. Duijf, Sharath Sriram, Ganganath Perera, Sarju Vasani, Lizbeth Kenny, Paul Leo, and Chamindie Punyadeera. Circulating tumour dna alterations: emerging biomarker in head and neck squamous cell carcinoma. Journal of Biomedical Science, Aug 2023. URL: https://doi.org/10.1186/s12929-023-00953-z, doi:10.1186/s12929-023-00953-z. This article has 36 citations and is from a domain leading peer-reviewed journal.

18. (sharma2024dysphagiavoiceproblems pages 2-3): Vaishali Sharma, Jisa George T, R Velmurugan, and Rajesh Pasricha. Dysphagia, voice problems and health related quality of life among head and neck cancer survivors. Journal of Caring Sciences, 13:207-213, Aug 2024. URL: https://doi.org/10.34172/jcs.33282, doi:10.34172/jcs.33282. This article has 2 citations.

19. (sharma2024dysphagiavoiceproblems pages 1-2): Vaishali Sharma, Jisa George T, R Velmurugan, and Rajesh Pasricha. Dysphagia, voice problems and health related quality of life among head and neck cancer survivors. Journal of Caring Sciences, 13:207-213, Aug 2024. URL: https://doi.org/10.34172/jcs.33282, doi:10.34172/jcs.33282. This article has 2 citations.

20. (filippini2024healthrelatedqualityof pages 1-2): Daria Maria Filippini, Francesca Carosi, Olimpia Panepinto, Giacomo Neri, Elisabetta Nobili, Nastassja Tober, Raffaele Giusti, and Massimo Di Maio. Health-related quality of life assessment in head and neck cancer: a systematic review of phase ii and iii clinical trials. Heliyon, 10:e40671, Dec 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e40671, doi:10.1016/j.heliyon.2024.e40671. This article has 3 citations.

21. (muijlwijk2024hallmarksofa pages 1-2): Tara Muijlwijk, Irene H. Nauta, Anabel van der Lee, Kari J. T. Grünewald, Arjen Brink, Sonja H. Ganzevles, Robert J. Baatenburg de Jong, Lilit Atanesyan, Suvi Savola, Mark A. van de Wiel, Laura A. N. Peferoen, Elisabeth Bloemena, Rieneke van de Ven, C. René Leemans, Jos B. Poell, and Ruud H. Brakenhoff. Hallmarks of a genomically distinct subclass of head and neck cancer. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53390-3, doi:10.1038/s41467-024-53390-3. This article has 18 citations and is from a highest quality peer-reviewed journal.

22. (xie2024immunelandscapein pages 2-3): Mengyu Xie, Ritu Chaudhary, Robbert J. C. Slebos, Kyubum Lee, Feifei Song, Maria I. Poole, Dirk S. Hoening, Leenil C. Noel, Juan C. Hernandez‐Prera, Jose R. Conejo‐Garcia, Christine H. Chung, and Aik Choon Tan. Immune landscape in molecular subtypes of human papillomavirus‐negative head and neck cancer. Molecular Carcinogenesis, 63:120-135, Sep 2024. URL: https://doi.org/10.1002/mc.23640, doi:10.1002/mc.23640. This article has 3 citations and is from a peer-reviewed journal.

23. (zhou2024globalburdenof pages 1-2): Tianjiao Zhou, Weijun Huang, Xiaoting Wang, Jingyu Zhang, Enhui Zhou, Yixing Tu, Jianyin Zou, Kaiming Su, Hongliang Yi, and Shankai Yin. Global burden of head and neck cancers from 1990 to 2019. iScience, 27:109282, Mar 2024. URL: https://doi.org/10.1016/j.isci.2024.109282, doi:10.1016/j.isci.2024.109282. This article has 63 citations and is from a peer-reviewed journal.

24. (kim2024aseerbasedanalysis pages 1-2): Su Il Kim, Jung Woo Lee, Young-Gyu Eun, and Young Chan Lee. A seer-based analysis of trends in hpv-associated oropharyngeal squamous cell carcinoma. Infectious Agents and Cancer, Jun 2024. URL: https://doi.org/10.1186/s13027-024-00592-5, doi:10.1186/s13027-024-00592-5. This article has 12 citations and is from a peer-reviewed journal.

25. (tran2024advancesinhuman pages 6-6): Ngoc Ha Tran, Dayna Sais, and Nham Tran. Advances in human papillomavirus detection and molecular understanding in head and neck cancers: implications for clinical management. Journal of Medical Virology, Jun 2024. URL: https://doi.org/10.1002/jmv.29746, doi:10.1002/jmv.29746. This article has 27 citations and is from a peer-reviewed journal.

26. (gallus2023accuracyofp16 media 97554451): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

27. (gallus2023accuracyofp16 media 6b48023a): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

28. (gallus2023accuracyofp16 media 4f7617b0): Roberto Gallus, Irene H Nauta, Linda Marklund, Davide Rizzo, Claudia Crescio, Luca Mureddu, Paolo Tropiano, Giovanni Delogu, and Francesco Bussu. Accuracy of p16 ihc in classifying hpv-driven opscc in different populations. Cancers, 15:656, Jan 2023. URL: https://doi.org/10.3390/cancers15030656, doi:10.3390/cancers15030656. This article has 35 citations.

29. (pakkanen2024simultaneousp53and pages 5-6): Pihla Pakkanen, Antti Silvoniemi, Katri Aro, Leif Bäck, Heikki Irjala, Leena-Maija Aaltonen, Jaana Hagström, Caj Haglund, Jukka Laine, Heikki Minn, and Jutta Huvila. Simultaneous p53 and p16 immunostaining for molecular subclassification of head and neck squamous cell carcinomas. Head and Neck Pathology, Aug 2024. URL: https://doi.org/10.1007/s12105-024-01680-z, doi:10.1007/s12105-024-01680-z. This article has 6 citations and is from a peer-reviewed journal.

30. (tran2024advancesinhuman pages 2-3): Ngoc Ha Tran, Dayna Sais, and Nham Tran. Advances in human papillomavirus detection and molecular understanding in head and neck cancers: implications for clinical management. Journal of Medical Virology, Jun 2024. URL: https://doi.org/10.1002/jmv.29746, doi:10.1002/jmv.29746. This article has 27 citations and is from a peer-reviewed journal.

31. (tran2024advancesinhuman pages 2-2): Ngoc Ha Tran, Dayna Sais, and Nham Tran. Advances in human papillomavirus detection and molecular understanding in head and neck cancers: implications for clinical management. Journal of Medical Virology, Jun 2024. URL: https://doi.org/10.1002/jmv.29746, doi:10.1002/jmv.29746. This article has 27 citations and is from a peer-reviewed journal.

32. (harrington2023pembrolizumabwithor pages 2-3): Kevin J. Harrington, Barbara Burtness, Richard Greil, Denis Soulières, Makoto Tahara, Gilberto de Castro, Amanda Psyrri, Irene Brana, Neus Basté, Prakash Neupane, Åse Bratland, Thorsten Fuereder, Brett G.M. Hughes, Ricard Mesia, Nuttapong Ngamphaiboon, Tamara Rordorf, Wan Zamaniah Wan Ishak, Jianxin Lin, Burak Gumuscu, Ramona F. Swaby, and Danny Rischin. Pembrolizumab with or without chemotherapy in recurrent or metastatic head and neck squamous cell carcinoma: updated results of the phase iii keynote-048 study. Journal of Clinical Oncology, 41:790-802, Feb 2023. URL: https://doi.org/10.1200/jco.21.02508, doi:10.1200/jco.21.02508. This article has 541 citations and is from a highest quality peer-reviewed journal.

33. (oridate2024firstlinepembrolizumabwith pages 1-2): Nobuhiko Oridate, Shunji Takahashi, Kaoru Tanaka, Yasushi Shimizu, Yasushi Fujimoto, Koji Matsumoto, Tomoya Yokota, Tomoko Yamazaki, Masanobu Takahashi, Tsutomu Ueda, Nobuhiro Hanai, Hironori Yamaguchi, Hiroki Hara, Tomokazu Yoshizaki, Ryuji Yasumatsu, Masahiro Nakayama, Kiyoto Shiga, Takashi Fujii, Kenji Mitsugi, Kenichi Takahashi, Nijiro Nohata, Burak Gumuscu, Nati Lerman, and Makoto Tahara. First-line pembrolizumab with or without chemotherapy for recurrent or metastatic head and neck squamous cell carcinoma: 5-year follow-up of the japanese population of keynote‑048. International Journal of Clinical Oncology, 29:1825-1839, Oct 2024. URL: https://doi.org/10.1007/s10147-024-02632-x, doi:10.1007/s10147-024-02632-x. This article has 9 citations and is from a peer-reviewed journal.

34. (black2023realworldtreatmentpatterns pages 1-2): Christopher M. Black, Glenn J. Hanna, Liya Wang, Karthik Ramakrishnan, Daisuke Goto, Vladimir Turzhitsky, and Gleicy M. Hair. Real-world treatment patterns and outcomes among individuals receiving first-line pembrolizumab therapy for recurrent/metastatic head and neck squamous cell carcinoma. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1160144, doi:10.3389/fonc.2023.1160144. This article has 22 citations.

35. (black2023realworldtreatmentpatterns pages 8-9): Christopher M. Black, Glenn J. Hanna, Liya Wang, Karthik Ramakrishnan, Daisuke Goto, Vladimir Turzhitsky, and Gleicy M. Hair. Real-world treatment patterns and outcomes among individuals receiving first-line pembrolizumab therapy for recurrent/metastatic head and neck squamous cell carcinoma. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1160144, doi:10.3389/fonc.2023.1160144. This article has 22 citations.

36. (black2023realworldtreatmentpatterns pages 3-5): Christopher M. Black, Glenn J. Hanna, Liya Wang, Karthik Ramakrishnan, Daisuke Goto, Vladimir Turzhitsky, and Gleicy M. Hair. Real-world treatment patterns and outcomes among individuals receiving first-line pembrolizumab therapy for recurrent/metastatic head and neck squamous cell carcinoma. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1160144, doi:10.3389/fonc.2023.1160144. This article has 22 citations.

37. (black2023realworldtreatmentpatterns pages 5-6): Christopher M. Black, Glenn J. Hanna, Liya Wang, Karthik Ramakrishnan, Daisuke Goto, Vladimir Turzhitsky, and Gleicy M. Hair. Real-world treatment patterns and outcomes among individuals receiving first-line pembrolizumab therapy for recurrent/metastatic head and neck squamous cell carcinoma. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1160144, doi:10.3389/fonc.2023.1160144. This article has 22 citations.

38. (cirillo2024pembrolizumabbasedfirstlinetreatment pages 1-2): Alessio Cirillo, Daniele Marinelli, Umberto Romeo, Daniela Messineo, Francesca De Felice, Marco De Vincentiis, Valentino Valentini, Silvia Mezi, Filippo Valentini, Luca Vivona, Antonella Chiavassa, Bruna Cerbelli, Daniele Santini, Paolo Bossi, Antonella Polimeni, Paolo Marchetti, and Andrea Botticelli. Pembrolizumab-based first-line treatment for pd-l1-positive, recurrent or metastatic head and neck squamous cell carcinoma: a retrospective analysis. BMC Cancer, Apr 2024. URL: https://doi.org/10.1186/s12885-024-12155-3, doi:10.1186/s12885-024-12155-3. This article has 11 citations and is from a peer-reviewed journal.

39. (NCT03624231 chunk 1): Ulrich Keilholz. Feasibility & Efficacy of Durvalumab+Tremelimumab+RT and Durvalumab+RT in Non-resect. Locally Advanced HPVnegativ HNSCC. Ulrich Keilholz. 2018. ClinicalTrials.gov Identifier: NCT03624231

40. (NCT03635164 chunk 2):  Radiotherapy With Durvalumab Prior to Surgical Resection for HPV Negative Squamous Cell Carcinoma. University of Colorado, Denver. 2018. ClinicalTrials.gov Identifier: NCT03635164

41. (NCT06161545 chunk 1):  Pembrolizumab + N-803 Alone or in Combination With PD-L1 t-haNK Cells for Resectable Head and Neck Squamous Cell Carcinoma. National Cancer Institute (NCI). 2025. ClinicalTrials.gov Identifier: NCT06161545

42. (NCT03624231 chunk 2): Ulrich Keilholz. Feasibility & Efficacy of Durvalumab+Tremelimumab+RT and Durvalumab+RT in Non-resect. Locally Advanced HPVnegativ HNSCC. Ulrich Keilholz. 2018. ClinicalTrials.gov Identifier: NCT03624231

43. (NCT05879484 chunk 1):  Study of Front Line Pembrolizumab and Valemetostat in PD-L1 Positive, HPV-Negative Recurrent/Metastatic Squamous Cell Carcinoma (SCC) of the Head and Neck: The PANTHERAS. National Cancer Institute (NCI). 2025. ClinicalTrials.gov Identifier: NCT05879484

44. (chaves2023preclinicalmodelsin pages 3-4): Patricia Chaves, María Garrido, Javier Oliver, Elisabeth Pérez-Ruiz, Isabel Barragan, and Antonio Rueda-Domínguez. Preclinical models in head and neck squamous cell carcinoma. British Journal of Cancer, 128:1819-1827, Feb 2023. URL: https://doi.org/10.1038/s41416-023-02186-1, doi:10.1038/s41416-023-02186-1. This article has 70 citations and is from a domain leading peer-reviewed journal.

45. (chaves2023preclinicalmodelsin pages 2-3): Patricia Chaves, María Garrido, Javier Oliver, Elisabeth Pérez-Ruiz, Isabel Barragan, and Antonio Rueda-Domínguez. Preclinical models in head and neck squamous cell carcinoma. British Journal of Cancer, 128:1819-1827, Feb 2023. URL: https://doi.org/10.1038/s41416-023-02186-1, doi:10.1038/s41416-023-02186-1. This article has 70 citations and is from a domain leading peer-reviewed journal.

46. (tinhofer2020preclinicalmodelsof pages 4-5): Ingeborg Tinhofer, Diana Braunholz, and Konrad Klinghammer. Preclinical models of head and neck squamous cell carcinoma for a basic understanding of cancer biology and its translation into efficient therapies. Cancers of the Head & Neck, Jul 2020. URL: https://doi.org/10.1186/s41199-020-00056-4, doi:10.1186/s41199-020-00056-4. This article has 67 citations.

47. (tasoulas2023geneticallyengineeredmouse pages 5-7): Jason Tasoulas, Sonal Srivastava, Xiaonan Xu, Valentina Tarasova, Anastasios Maniakas, Florian A. Karreth, and Antonio L. Amelio. Genetically engineered mouse models of head and neck cancers. Oncogene, 42:2593-2609, Jul 2023. URL: https://doi.org/10.1038/s41388-023-02783-7, doi:10.1038/s41388-023-02783-7. This article has 15 citations and is from a domain leading peer-reviewed journal.

48. (zohud2023towardssystemgenetics pages 2-3): Osayd Zohud, Iqbal M. Lone, Aysar Nashef, and Fuad A. Iraqi. Towards system genetics analysis of head and neck squamous cell carcinoma using the mouse model, cellular platform, and clinical human data. Animal Models and Experimental Medicine, 6:537-558, Dec 2023. URL: https://doi.org/10.1002/ame2.12367, doi:10.1002/ame2.12367. This article has 11 citations.
