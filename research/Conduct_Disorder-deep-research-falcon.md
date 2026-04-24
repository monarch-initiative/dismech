---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:53.743204'
end_time: '2026-04-24T17:16:26.109032'
duration_seconds: 932.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Conduct Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Conduct Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Conduct Disorder** covering all of the
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
- **Disease Name:** Conduct Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Conduct Disorder** covering all of the
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


# Conduct Disorder (CD): Disease Characteristics Research Report (Psychiatric)

## Target disease
- **Disease name:** Conduct Disorder (CD) (DSM-5/DSM-5-TR terminology) (masi2023contemporarydiagnosisand pages 1-5)
- **ICD-11 closest entity:** **Conduct-dissocial disorder** (ICD-11 code **6C91**) (ruotsalainen2022childhoodpsychopathyin pages 18-21)
- **MONDO ID:** Not identified from the retrieved sources in this run (no MONDO mapping document retrieved).

## Executive summary
Conduct disorder is a childhood/adolescent-onset psychiatric disorder defined by a persistent pattern of behaviors violating the rights of others and major societal norms/rules, spanning aggression, property destruction, deceit/theft, and serious rule violations (masi2023contemporarydiagnosisand pages 1-5, ruotsalainen2022childhoodpsychopathyin pages 38-43). Modern classification emphasizes clinically meaningful heterogeneity via specifiers for **age of onset** and **limited prosocial emotions (LPE)/callous-unemotional (CU)** traits, which are associated with more severe antisocial trajectories and may moderate treatment response (masi2023contemporarydiagnosisand pages 5-7, masi2023contemporarydiagnosisand pages 1-5). Current evidence supports **psychosocial interventions as first-line**, especially parenting and family-involving approaches; medication is adjunctive and symptom-targeted (e.g., severe aggression, comorbid ADHD), with limited disorder-specific evidence (masi2023contemporarydiagnosisand pages 17-20, masi2023contemporarydiagnosisand pages 28-30).

## Key structured facts (artifact)
| Item | Key details | Best supporting source (author year) | URL | Evidence citation ID |
|---|---|---|---|---|
| Nosology / identifiers | **DSM-5/DSM-5-TR:** Conduct Disorder (CD), in the chapter *Disruptive, Impulse-Control, and Conduct Disorders*. **ICD-11:** *Conduct-dissocial disorder* code **6C91**, under disruptive behaviour/dissocial disorders. ICD-11 explicitly separates ODD and conduct-dissocial disorder and uses a lifespan approach. | Masi et al. 2023; Reed et al. 2019 | https://doi.org/10.1080/14737175.2023.2271169 ; https://doi.org/10.1002/wps.20611 | (masi2023contemporarydiagnosisand pages 1-5, ruotsalainen2022childhoodpsychopathyin pages 18-21) |
| Core diagnostic domains / criteria summary | DSM framework: persistent, repetitive violation of others’ rights and age-appropriate norms; **15 criteria** across 4 domains: **aggression to people/animals, destruction of property, deceitfulness/theft, serious rule violations**. Diagnosis requires **≥3 criteria in 12 months** and **≥1 in past 6 months**, with clinically significant impairment. | Masi et al. 2023; Ruotsalainen 2022 | https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 1-5, ruotsalainen2022childhoodpsychopathyin pages 38-43) |
| ICD-11 diagnostic structure | ICD-11 conduct-dissocial disorder uses similar 4 behavioural groupings; evidence summarized in recent review notes ICD-11 requires a **persistent pattern over at least 12 months** and includes affective/interpersonal qualifiers. | Özbay et al. 2024 | https://doi.org/10.18863/pgy.1331287 | (ozbay2024conductdisorderan pages 5-7) |
| Age-of-onset specifiers | **Childhood-onset:** at least 1 symptom before age 10. **Adolescent-onset:** no symptoms before age 10. Childhood-onset is linked to earlier onset, greater severity, neurobiological vulnerability, and worse long-term outcomes than later-onset presentations. | Masi et al. 2023 | https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 5-7, masi2023contemporarydiagnosisand pages 1-5) |
| Limited prosocial emotions / callous-unemotional specifier | DSM-5 **with Limited Prosocial Emotions (LPE)** / CU traits: at least **2 of 4** traits for **12 months across settings**: lack of remorse/guilt, callous-lack of empathy, unconcern about performance, shallow/deficient affect. Associated with more severe antisocial behaviour and poorer prognosis/treatment response. | Masi et al. 2023 | https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 5-7, ruotsalainen2022childhoodpsychopathyin pages 38-43) |
| ICD-11 LPE-related qualifier | ICD-11 includes an LPE-related qualifier and, compared with DSM-5, adds an indicator related to **indifference to punishment**; recent summaries note qualifier use in conduct-dissocial disorder and ODD. | Masi et al. 2023; Ruotsalainen 2022 | https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 5-7, ruotsalainen2022childhoodpsychopathyin pages 47-48) |
| Recent epidemiology: community prevalence | Recent reviews cite **global prevalence ~1.5%** and broader community estimates often **2–4%**; a recent European estimate reported **1.5% overall**, **1.8% in males**, **1.0% in females**. | Masi et al. 2023; Özbay et al. 2024; Bachmann et al. 2024 | https://doi.org/10.1080/14737175.2023.2271169 ; https://doi.org/10.18863/pgy.1331287 ; https://doi.org/10.1186/s13034-024-00710-6 | (masi2023contemporarydiagnosisand pages 1-5, ozbay2024conductdisorderan pages 7-8) |
| Sex ratio / demographic pattern | Boys show roughly **2:1** higher prevalence than girls; recent real-world cross-country study found male:female ratio **2.0–2.5:1** for diagnosed CD. Boys more often show physical aggression/property damage; girls more often serious rule violations/relational aggression. | Bachmann et al. 2024; Masi et al. 2023 | https://doi.org/10.1186/s13034-024-00710-6 ; https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 1-5) |
| Real-world administrative prevalence variation | Among youths aged 0–19 years in 2018 health-system data, diagnosed CD prevalence differed **31-fold** across countries: **0.1% Denmark, 0.3% Norway, 1.1% USA, 3.1% Germany**; comorbidity was high (**69.7–86.1%**), ADHD most common. | Bachmann et al. 2024 | https://doi.org/10.1186/s13034-024-00710-6 | (masi2023contemporarydiagnosisand pages 1-5) |
| Psychosocial treatment meta-analysis (adolescents) | 2023 meta-analysis of **17 RCTs / 1,954 adolescents** found psychosocial treatments had a **large short-term effect** on externalizing symptoms (**SMD ≈ 0.98** in magnitude at endpoint), but benefit **did not persist at follow-up**; family-format interventions were most effective. | Boldrini et al. 2023 | https://doi.org/10.1016/j.jaac.2022.05.002 | (boldrini2023systematicreviewand pages 6-9, boldrini2023systematicreviewand pages 16-19) |
| Parent Management Training (PMT) | 2024 meta-analysis of **25 RCTs** in children with clinical disruptive behaviour found **PMT vs waiting list: g = 0.64 (95% CI 0.42–0.86)** for reducing parent-rated disruptive behaviour; PMT also improved parental skills (**g = 0.83**) and child social skills (**g = 0.49**). | Helander et al. 2024 | https://doi.org/10.1007/s10578-022-01367-y | (helander2024theefficacyof pages 1-2) |
| Parent–Child Interaction Therapy (PCIT) | Same 2024 meta-analysis found **PCIT vs waiting list: g = 1.22 (95% CI 0.75–1.69)**, larger than PMT for younger children with disruptive behaviour. | Helander et al. 2024 | https://doi.org/10.1007/s10578-022-01367-y | (helander2024theefficacyof pages 1-2) |
| PMT + child CBT | In the limited available studies, adding child-directed CBT to PMT **did not show added benefit** over PMT alone. | Helander et al. 2024 | https://doi.org/10.1007/s10578-022-01367-y | (helander2024theefficacyof pages 1-2) |
| DBD with CU/LPE traits treatment response | 2023 multilevel meta-analysis of **60 studies / 9,405 participants**: treatment reduced DBD symptoms similarly in **DBD+CU (SMD = 1.08)** and **DBD-only (SMD = 1.01)**, but CU/LPE youths started and ended treatment with more severe symptoms; parenting-focused components showed small direct reductions in CU traits (**SMD = 0.21**). | Perlstein et al. 2023 | https://doi.org/10.1111/jcpp.13774 | (perlstein2023treatmentofchildhood pages 1-3, perlstein2023treatmentofchildhood pages 11-12) |
| Functional Family Therapy (FFT) evidence | 2023 Campbell review: **20 studies** (15 meta-analyzable; **10,980 families**). Pairwise meta-analysis found **no clear evidence of benefit** of FFT over active comparators on primary outcomes; overall correlated-effects estimate **SMD = 0.19, SE = 0.09**, not significantly different from zero; certainty **very low**. | Littell et al. 2023 | https://doi.org/10.1002/cl2.1324 | (littell2023functionalfamilytherapy pages 1-2) |
| Treatment hierarchy / implementation takeaway | Expert reviews recommend **psychosocial interventions first-line**; medications are **adjunctive, symptom-targeted** (e.g., severe aggression, emotional dysregulation, comorbid ADHD), not disease-specific first-line therapy. | Masi et al. 2023 | https://doi.org/10.1080/14737175.2023.2271169 | (masi2023contemporarydiagnosisand pages 17-20, masi2023contemporarydiagnosisand pages 1-5, masi2023contemporarydiagnosisand pages 28-30) |


*Table: This table summarizes core nosology, diagnostic structure, specifiers, epidemiology, and treatment-effect evidence for Conduct Disorder / ICD-11 conduct-dissocial disorder. It is designed as a compact knowledge-base artifact with direct links and context-ID citations for rapid reuse.*

---

## 1. Disease information

### 1.1 Overview / definition
Conduct disorder (CD) is characterized by “persistent, repetitive behaviors that violate societal norms and others’ rights” (reviewed in contemporary clinical synthesis) (masi2023contemporarydiagnosisand pages 1-5). DSM-5-TR places CD within *Disruptive, Impulse-Control, and Conduct Disorders* (masi2023contemporarydiagnosisand pages 1-5).

**Core symptom domains (DSM framing):**
- Aggression toward people/animals
- Destruction of property
- Deceitfulness or theft
- Serious violations of rules (masi2023contemporarydiagnosisand pages 1-5, ruotsalainen2022childhoodpsychopathyin pages 38-43)

**DSM-5 diagnostic threshold (summary):** ≥3 of 15 criteria in the past 12 months, with ≥1 present in the last 6 months, plus clinically significant impairment (ruotsalainen2022childhoodpsychopathyin pages 38-43, ozbay2024conductdisorderan pages 2-3).

### 1.2 Key identifiers / terminologies
- **ICD-11:** conduct-dissocial disorder (**6C91**) (ruotsalainen2022childhoodpsychopathyin pages 18-21)
- **ICD-11 grouping:** described as under disruptive behaviour/dissocial disorders in secondary summaries (ozbay2024conductdisorderan pages 5-7)
- **MeSH / OMIM / Orphanet:** Not identified from retrieved sources in this run.

### 1.3 Synonyms / alternative names
- “Conduct-dissocial disorder” (ICD-11 naming) (ruotsalainen2022childhoodpsychopathyin pages 18-21)
- “Disruptive behavior disorders” (DBDs; an umbrella term often used in treatment evidence that includes CD and ODD) (boldrini2023systematicreviewand pages 6-9, perlstein2023treatmentofchildhood pages 1-3)

### 1.4 Evidence source type
This report is derived from **aggregated disease-level resources** (systematic reviews, meta-analyses, expert reviews) and selected **primary clinical/epidemiologic studies** (e.g., administrative prevalence comparisons; cohort/AI prediction studies) (boldrini2023systematicreviewand pages 6-9, helander2024theefficacyof pages 1-2, lacy2023selectivelypredictingthe pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
Recent expert synthesis emphasizes CD as etiologically heterogeneous and multifactorial, involving genetic, individual neurodevelopmental, and psychosocial factors (masi2023contemporarydiagnosisand pages 1-5).

### 2.2 Risk factors

#### 2.2.1 Genetic liability (polygenic)
Childhood aggression (closely related to conduct problems/CD phenotypes) is consistently reported as substantially heritable in modern synthesis.
- **Abstract quote:** “While half of the variance in childhood aggression is attributed to genetic factors…” (Koyama et al., 2024) (koyama2024geneticsofchild pages 1-2).
- Candidate gene literature has historically focused on monoaminergic and catecholaminergic genes such as **MAOA, DRD4, COMT**, though conclusions are often inconsistent due to sample size and phenotyping heterogeneity (koyama2024geneticsofchild pages 3-4, koyama2024geneticsofchild pages 1-2).

**Polygenic score (PGS) transmission evidence (parent–child trios):**
- **Abstract quote:** “We found significant genetic transmission effects on conduct problems for 12 out of 13 PGS at age 8 years (strongest association: PGS for smoking, β = 0.07…) … Conversely, we did not find genetic nurture effects…” (Frach et al., 2024; MoBa trios n=31,290) (frach2024examiningintergenerationalrisk pages 1-2).

#### 2.2.2 Environmental and social risk factors
A recent update review summarizes evidence that exposure to social violence is associated with markedly increased likelihood of CD (e.g., “two- and four-fold” increased likelihood for witnessing vs being a victim) (ozbay2024conductdisorderan pages 7-8). Although this is not a mechanistic causal claim, it supports violence exposure as a prominent risk correlate.

#### 2.2.3 Physiological correlates are not necessarily causal
A Mendelian randomization study testing low resting heart rate (RHR) as a potential causal risk factor for antisocial behavior (ASB; related to CD spectrum) found **no evidence of a causal association**, indicating some observed physiological associations may reflect confounding.
- **Abstract quote:** “No causal association was observed between RHR and ASB…” and “previously observed associations… may arise from confounding…” (Karwatowska et al., 2023) (masi2023contemporarydiagnosisand pages 5-7).

### 2.3 Protective factors
Direct protective-factor estimates specific to CD were not available from the retrieved sources. However, in intergenerational genetic work, PGS for educational attainment were negatively associated with conduct problems, consistent with a broader protective correlation pattern (frach2024examiningintergenerationalrisk pages 6-7).

### 2.4 Gene–environment interactions (GxE)
Modern genetic synthesis of childhood aggression notes the field increasingly studies GxE and reports examples (e.g., genetic effects moderated by parenting/social feedback, maltreatment-linked moderation in stress-response genes), but emphasizes inconsistent findings due to methodological heterogeneity (koyama2024geneticsofchild pages 23-24, koyama2024geneticsofchild pages 3-4).

---

## 3. Phenotypes

### 3.1 Core behavioral phenotype domains (DSM)
Phenotypes correspond to the DSM domains above (aggression; property destruction; deceit/theft; serious rule violations) (masi2023contemporarydiagnosisand pages 1-5, ruotsalainen2022childhoodpsychopathyin pages 38-43).

**Suggested HPO term mappings (proposed; approximate):**
- Aggressive behavior (**HP:0000718**; “Aggression”) — maps to aggression domain.
- Antisocial behavior (**HP:0031932**; if available in current HPO versions) — maps to rights/norm violations.
- Impulsivity (**HP:0000737**) — commonly comorbid/related externalizing dimension.
- Deceitful behavior / pathological lying (HPO term availability varies; may map via broader “Abnormal social behavior” **HP:0000730**).

*(Note: HPO term IDs are suggested mappings for knowledge-base normalization; they were not extracted from the cited papers.)*

### 3.2 Specifiers / clinical subtypes

#### 3.2.1 Age-of-onset specifiers
DSM subtyping includes:
- **Childhood-onset:** ≥1 symptom before age 10.
- **Adolescent-onset:** symptoms begin after age 10. (masi2023contemporarydiagnosisand pages 1-5)

Childhood-onset presentations are described as associated with earlier onset, greater severity, and worse long-term outcomes (including substance abuse and criminality) in expert synthesis (masi2023contemporarydiagnosisand pages 5-7).

#### 3.2.2 Limited prosocial emotions (LPE) / callous-unemotional (CU) traits
DSM-5 LPE specifier criteria (summary): at least **2 of 4 features** for **12 months** across relationships/settings—lack of remorse/guilt, callousness/lack of empathy, unconcern about performance, shallow/deficient affect (masi2023contemporarydiagnosisand pages 5-7, ruotsalainen2022childhoodpsychopathyin pages 38-43).

**Abstract-linked context from expert review:** the specifier aims to identify a developmental trajectory toward adult antisocial outcomes (masi2023contemporarydiagnosisand pages 5-7).

**Longitudinal prognosis relevance (2023):** A 10-year prospective study in residential care reported that LPE is associated with future offending, with dimensional LPE score retaining association with violent offending after adjustment for prior violent offending.
- **Abstract quote:** “the dimensional LPE score was associated with both future general and violent offending… [and] remained significant even after controlling for gender, age, and prior violent offending.” (Boonmann et al., 2023) (masi2023contemporarydiagnosisand pages 5-7).

### 3.3 Comorbidity patterns
High psychiatric comorbidity is typical in health-system cohorts.
- A cross-country administrative study reported comorbidity rates **69.7–86.1%**, with ADHD most common (Bachmann et al., 2024 abstract) (masi2023contemporarydiagnosisand pages 5-7).

---

## 4. Genetic / molecular information

### 4.1 Causal genes
Conduct disorder is not a Mendelian disorder; **no single causal gene** is established. Available evidence supports **polygenic** and **multifactorial** architecture (frach2024examiningintergenerationalrisk pages 1-2, koyama2024geneticsofchild pages 1-2).

### 4.2 Candidate genes / pathways studied
A recent systematic review of childhood aggression genetics (often used as an etiologic window into CD-spectrum behaviors) reports dominance of candidate gene research, particularly:
- **MAOA** (17 studies)
- **DRD4** (13 studies)
- **COMT** (12 studies) (koyama2024geneticsofchild pages 1-2)

However, the same review emphasizes inconsistent results and methodological limitations (moderate sample sizes, heterogeneous phenotyping) (koyama2024geneticsofchild pages 1-2).

### 4.3 Polygenic risk / PGS
Intergenerational trio analyses show measurable transmission effects across multiple parental-trait PGS with conduct problems at ages 8 and 14, with limited evidence of genetic nurture in the tested PGS set (frach2024examiningintergenerationalrisk pages 1-2).

### 4.4 Epigenetics / transcriptomics
Epigenetic and transcriptomic approaches are described as increasing in frequency in aggression genetics research, but no specific replicated biomarkers for CD were identified in the retrieved evidence (koyama2024geneticsofchild pages 1-2).

---

## 5. Environmental information
Direct toxin/pathogen associations were not identified in the retrieved sources. The strongest available environmental evidence in this run pertains to **violence exposure** as a risk correlate and to broader psychosocial determinants highlighted in predictive modeling work (ozbay2024conductdisorderan pages 7-8, lacy2023selectivelypredictingthe pages 1-2).

---

## 6. Mechanism / pathophysiology

### 6.1 Neurocognitive and neurocircuit mechanisms (current understanding)
Expert synthesis links CD/CU phenotypes to dysfunction in systems supporting empathy and social learning.
- Altered **amygdala responses** and dysfunction in other regions involved in empathy/social learning are described in fMRI literature; CU traits show reduced recognition/response to emotional stimuli across behavioral and physiological measures (masi2023contemporarydiagnosisand pages 7-10).

**Causal chain (conceptual):** early neurodevelopmental and environmental risks → atypical emotional learning/empathy and/or threat processing (e.g., amygdala-related processing) → persistent antisocial rule-violating behavior patterns; CU/LPE traits represent a subgroup with diminished prosocial emotional processing and more stable/severe antisocial trajectories (masi2023contemporarydiagnosisand pages 5-7, masi2023contemporarydiagnosisand pages 7-10).

### 6.2 Physiological arousal and aggression subtypes
Reactive aggression is described as associated with physiological overarousal and poor emotion regulation (masi2023contemporarydiagnosisand pages 7-10).

### 6.3 Biomarkers and molecular profiling: current limitations
A high-authority World Psychiatry systematic review assessed candidate diagnostic biomarkers (biochemical, neuroimaging, neurophysiological, etc.) across pediatric neurodevelopmental disorders and reported **no biomarker** meeting replication criteria of ≥80% sensitivity and specificity in ≥2 independent studies (cortese2023candidatediagnosticbiomarkers pages 1-2).
- **Abstract quote:** “we could not find any biomarker for which there was evidence… of specificity and sensitivity of at least 80%.” (Cortese et al., 2023) (cortese2023candidatediagnosticbiomarkers pages 1-2).

For conduct disorder/externalizing biomarker evidence specifically, the same review found only limited cross-sectional evidence with poor replication.
- “Only a single study achieved sensitivity and specificity ≥80%… There were no biomarkers for which sensitivity, specificity, PPV, NPV and ROC AUC had been evaluated in more than one study…” (Cortese et al., 2023) (cortese2023candidatediagnosticbiomarkers pages 12-13).

**Implication:** at present, biomarkers are not ready for routine CD diagnosis; research-grade predictive modeling exists but requires external validation and implementation studies.

### 6.4 Advanced technologies: AI prediction using multimodal features
A 2023 ABCD-based study used deep learning to predict future onset of CD/ODD/ADHD over 2 years using multimodal features including neuroimaging, physiology, and psychosocial measures.
- **Abstract quote:** “Multimodal models achieved ~86–97% accuracy, 0.919–0.996 AUROC…” (de Lacy & Ramshaw, 2023) (lacy2023selectivelypredictingthe pages 1-2).
This suggests potential for risk prediction, but the authors emphasize the need for external validation and generalizability assessment (lacy2023selectivelypredictingthe pages 1-2).

**Suggested GO biological process terms (conceptual mapping):**
- Social behavior (GO:0035176)
- Regulation of emotional behavior (GO:0046834)
- Learning (GO:0007612)

**Suggested Cell Ontology / UBERON mappings (conceptual):**
- Amygdala (UBERON:0001876)
- Prefrontal cortex (UBERON:0000451)
- Neurons (CL:0000540)
- Microglia (CL:0000129) *(note: microglia were not specifically evidenced for CD in retrieved sources; included only as a general CNS immune cell type)*

---

## 7. Anatomical structures affected
Primary involvement is neuropsychiatric/behavioral, implicating brain circuits for emotion regulation, empathy, and reward/threat learning.
- Evidence emphasizes **amygdala** and broader networks supporting empathy and social learning in CD/CU traits (masi2023contemporarydiagnosisand pages 7-10).

Suggested UBERON structures (conceptual mapping):
- Amygdala (UBERON:0001876)
- Prefrontal cortex (UBERON:0000451)

---

## 8. Temporal development

### 8.1 Onset
CD onset is typically during school years or early adolescence; DSM-5 uses onset before vs after age 10 for subtype specification (masi2023contemporarydiagnosisand pages 1-5).

### 8.2 Progression / course
Expert synthesis describes developmental shifts: aggressive behaviors tend to decline with age, while non-aggressive rule violations increase in adolescence (masi2023contemporarydiagnosisand pages 1-5).

### 8.3 Critical periods
The frequent developmental sequence from ODD to CD, with CD sometimes emerging before school age, supports early prevention and early treatment as critical (masi2023contemporarydiagnosisand pages 5-7).

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent estimates)
Recent expert review and update articles report community prevalence in the low single-digit percentages.
- Global prevalence around **~1.5%** (expert review summary) (masi2023contemporarydiagnosisand pages 1-5).
- Recent European estimate summarized as **1.5% overall; 1.8% males; 1.0% females** (secondary review citing Sacco et al. 2021) (ozbay2024conductdisorderan pages 7-8).

### 9.2 Sex ratio
Male prevalence is consistently higher than female prevalence, approximately ~2:1 in multiple sources.
- Boys 3–4% vs girls 0.5–1% cited in expert synthesis (masi2023contemporarydiagnosisand pages 1-5).

### 9.3 Administrative prevalence variation across countries (real-world data)
A 2024 real-world data study compared 2018 health-system data across Denmark, Norway, USA, and Germany.
- **Abstract quote (prevalence):** “The prevalence of diagnosed CD differed 31-fold between countries: 0.1% (Denmark), 0.3% (Norway), 1.1% (USA) and 3.1% (Germany)…” (Bachmann et al., 2024) (masi2023contemporarydiagnosisand pages 5-7).
- **Abstract quote (sex ratio):** “…with a male/female ratio of 2.0–2.5:1.” (Bachmann et al., 2024) (masi2023contemporarydiagnosisand pages 5-7).

---

## 10. Diagnostics

### 10.1 Clinical criteria (DSM-5 framing)
Diagnosis relies on clinical/behavioral criteria (no validated diagnostic biomarker).
- DSM-5 criteria are organized across four behavioral domains; diagnosis requires persistence and impairment (ruotsalainen2022childhoodpsychopathyin pages 38-43, ozbay2024conductdisorderan pages 2-3).

### 10.2 ICD-11 diagnostic framing
ICD-11 uses conduct-dissocial disorder (6C91) with similar behavioral groupings and an emphasized duration threshold (secondary summary indicates 12 months vs 6 months in ICD-10) (ozbay2024conductdisorderan pages 5-7).

### 10.3 Differential diagnosis / assessment considerations
High comorbidity with ADHD is common; comorbidity complicates specificity of candidate biomarkers and requires careful clinical assessment (cortese2023candidatediagnosticbiomarkers pages 2-3).

### 10.4 Biomarkers and omics-based diagnostics
Not clinically established.
- **Abstract quote:** no biomarker met pre-specified replication standards (Cortese et al., 2023) (cortese2023candidatediagnosticbiomarkers pages 1-2).

---

## 11. Outcome / prognosis

### 11.1 Prognosis by subtype
Childhood-onset CD and CU/LPE traits are linked to worse longitudinal outcomes in expert synthesis (e.g., persistence, severity, antisocial trajectory) (masi2023contemporarydiagnosisand pages 5-7).

### 11.2 Offending and long-term antisocial outcomes
Longitudinal evidence supports LPE/CU traits as relevant to future offending risk, but effect sizes are influenced by static risk factors (gender, prior offending).
- **Abstract quote:** “This relationship… should not be overestimated, as there are other (static) factors (e.g. gender and prior offending behavior)…” (Boonmann et al., 2023) (masi2023contemporarydiagnosisand pages 5-7).

---

## 12. Treatment

### 12.1 First-line: psychosocial interventions (evidence base)
The best-supported treatments are psychosocial, especially parenting and family-involving interventions.

**Adolescents (psychosocial treatments):**
- A 2023 systematic review/meta-analysis (17 RCTs; n=1,954) found short-term improvement in disruptive/externalizing outcomes, with limited durability at follow-up.
  - **Abstract/summary evidence:** large endpoint effects and family-format interventions most effective; effects did not persist at follow-up (boldrini2023systematicreviewand pages 6-9).

**Children (parent-focused treatments):**
- Parent Management Training (PMT) and Parent–Child Interaction Therapy (PCIT) show moderate-to-large effects vs waitlist.
  - **Abstract quote:** “PMT (g = 0.64…) and PCIT (g = 1.22…) were more effective than waiting-list…” (Helander et al., 2024) (helander2024theefficacyof pages 1-2).

**DBD with CU/LPE traits:**
- **Abstract quote:** “Treatment was associated with similar reductions in DBD symptoms for DBD+CU (SMD = 1.08…) and DBD-only (SMD = 1.01…)… [but] no overall direct effect… on CU traits (SMD = .09…).” (Perlstein et al., 2023) (perlstein2023treatmentofchildhood pages 1-3).

**MAXO suggestions (treatment actions; conceptual mapping):**
- Behavioral parent training / parenting intervention (MAXO: behavioral therapy / parent training; exact MAXO IDs not retrieved)
- Family therapy (FFT/MST modalities)
- Cognitive behavioral therapy (CBT) modules for anger, problem-solving, emotion regulation

### 12.2 Real-world implementation: variation in treatment patterns
Real-world administrative data show substantial between-country variation and notable psychopharmacology use.
- **Abstract quote:** “Between 4.0% (Germany) and 12.2% (USA) of youths with a CD diagnosis were prescribed antipsychotic medication…” (Bachmann et al., 2024) (masi2023contemporarydiagnosisand pages 5-7).

### 12.3 Pharmacotherapy (adjunctive, symptom-targeted)
Contemporary expert reviews emphasize medications are not first-line for CD itself, but can target severe aggression, irritability, emotional dysregulation, or comorbid ADHD.
- “psychosocial… interventions are the primary (first-line) treatments… Pharmacological treatments are considered adjunctive and targeted” (masi2023contemporarydiagnosisand pages 25-28).
- Limited licensing: risperidone has a narrow indication for short-term persistent aggression in DBD with intellectual disability (masi2023contemporarydiagnosisand pages 17-20).

**Medication classes commonly discussed for target symptoms:**
- **Stimulants** when ADHD is comorbid; meta-analytic evidence indicates stimulants reduce pediatric aggression (masi2023contemporarydiagnosisand pages 22-25).
- **Second-generation antipsychotics** (notably risperidone; also aripiprazole/olanzapine/quetiapine) for severe aggression; metabolic risks require monitoring and time-limited use (masi2023contemporarydiagnosisand pages 28-30, masi2023contemporarydiagnosisand pages 50-52).
- **Mood stabilizers** (e.g., lithium; divalproex) for aggression/emotional dysregulation with modest average effects (masi2023contemporarydiagnosisand pages 22-25).

**MAXO suggestions (pharmacologic actions; conceptual mapping):**
- Antipsychotic therapy
- Psychostimulant therapy
- Mood stabilizer therapy

---

## 13. Prevention
Evidence specific to CD prevention programs was not comprehensively retrieved in this run; however, the etiologic and course evidence indicates early intervention is important because CD may follow ODD and can emerge before school age (masi2023contemporarydiagnosisand pages 5-7).

Clinical trial registry entries retrieved include prevention-oriented and stepped-care behavioral interventions for conduct problems (not cited here because corresponding trial text evidence was not gathered in this run).

---

## 14. Other species / natural disease
No primary comparative psychiatry evidence for conduct disorder analogs in other species was retrieved in this run.

---

## 15. Model organisms
No conduct-disorder-specific model organism paper was retrieved in this run. Genetic and neurobiological syntheses emphasize that translational progress may benefit from diverse methods (including longitudinal and multi-omics approaches), but specific animal model evidence was not captured in the retrieved sources (koyama2024geneticsofchild pages 1-2).

---

## Expert opinion and analysis (authoritative synthesis)
A major recent expert review stresses that CD is heterogeneous and that careful subtyping (age of onset, CU/LPE traits, emotional dysregulation, comorbidity) is crucial for prognosis and treatment selection (masi2023contemporarydiagnosisand pages 1-5). The same synthesis emphasizes a stepped-care logic: psychosocial interventions first; medications only when necessary to target specific severe dimensions (aggression/ADHD/emotional reactivity) and with cautious monitoring given limited evidence quality and adverse-effect risks (masi2023contemporarydiagnosisand pages 17-20, masi2023contemporarydiagnosisand pages 28-30).

---

## URLs and publication dates (selected key sources used)
- Masi G. et al. **Oct 2023**. *Expert Review of Neurotherapeutics*. https://doi.org/10.1080/14737175.2023.2271169 (masi2023contemporarydiagnosisand pages 1-5)
- Özbay A. et al. **Mar 2024**. *Psikiyatride Güncel Yaklaşımlar*. https://doi.org/10.18863/pgy.1331287 (ozbay2024conductdisorderan pages 1-2)
- Frach L. et al. **Jan 2024**. *Molecular Psychiatry*. https://doi.org/10.1038/s41380-023-02383-7 (frach2024examiningintergenerationalrisk pages 1-2)
- Koyama E. et al. **Jun 2024**. *Translational Psychiatry*. https://doi.org/10.1038/s41398-024-02870-7 (koyama2024geneticsofchild pages 1-2)
- Cortese S. et al. **Jan 2023**. *World Psychiatry*. https://doi.org/10.1002/wps.21037 (cortese2023candidatediagnosticbiomarkers pages 1-2)
- Helander M. et al. **Jul 2024**. *Child Psychiatry & Human Development*. https://doi.org/10.1007/s10578-022-01367-y (helander2024theefficacyof pages 1-2)
- Perlstein S. et al. **Mar 2023**. *JCPP*. https://doi.org/10.1111/jcpp.13774 (perlstein2023treatmentofchildhood pages 1-3)
- Boldrini T. et al. **May 2023**. *JAACAP*. https://doi.org/10.1016/j.jaac.2022.05.002 (boldrini2023systematicreviewand pages 6-9)
- Bachmann C.J. et al. **Jan 2024**. *Child and Adolescent Psychiatry and Mental Health*. https://doi.org/10.1186/s13034-024-00710-6 (masi2023contemporarydiagnosisand pages 5-7)
- de Lacy N. & Ramshaw M.J. **Dec 2023**. *Frontiers in Psychiatry*. https://doi.org/10.3389/fpsyt.2023.1280326 (lacy2023selectivelypredictingthe pages 1-2)


References

1. (masi2023contemporarydiagnosisand pages 1-5): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

2. (ruotsalainen2022childhoodpsychopathyin pages 18-21): N Ruotsalainen. Childhood psychopathy in defining heterogeneity of conduct problems. Unknown journal, 2022.

3. (ruotsalainen2022childhoodpsychopathyin pages 38-43): N Ruotsalainen. Childhood psychopathy in defining heterogeneity of conduct problems. Unknown journal, 2022.

4. (masi2023contemporarydiagnosisand pages 5-7): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

5. (masi2023contemporarydiagnosisand pages 17-20): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

6. (masi2023contemporarydiagnosisand pages 28-30): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

7. (ozbay2024conductdisorderan pages 5-7): Ahmet ÖZBAY, Osman ÖZÇELİK, and Süleyman KAHRAMAN. Conduct disorder: an update. Psikiyatride Güncel Yaklaşımlar, 16:72-87, Mar 2024. URL: https://doi.org/10.18863/pgy.1331287, doi:10.18863/pgy.1331287. This article has 3 citations.

8. (ruotsalainen2022childhoodpsychopathyin pages 47-48): N Ruotsalainen. Childhood psychopathy in defining heterogeneity of conduct problems. Unknown journal, 2022.

9. (ozbay2024conductdisorderan pages 7-8): Ahmet ÖZBAY, Osman ÖZÇELİK, and Süleyman KAHRAMAN. Conduct disorder: an update. Psikiyatride Güncel Yaklaşımlar, 16:72-87, Mar 2024. URL: https://doi.org/10.18863/pgy.1331287, doi:10.18863/pgy.1331287. This article has 3 citations.

10. (boldrini2023systematicreviewand pages 6-9): Tommaso Boldrini, Viola Ghiandoni, Elisa Mancinelli, Silvia Salcuni, and Marco Solmi. Systematic review and meta-analysis: psychosocial treatments for disruptive behavior symptoms and disorders in adolescence. Journal of the American Academy of Child and Adolescent Psychiatry, May 2023. URL: https://doi.org/10.1016/j.jaac.2022.05.002, doi:10.1016/j.jaac.2022.05.002. This article has 17 citations and is from a highest quality peer-reviewed journal.

11. (boldrini2023systematicreviewand pages 16-19): Tommaso Boldrini, Viola Ghiandoni, Elisa Mancinelli, Silvia Salcuni, and Marco Solmi. Systematic review and meta-analysis: psychosocial treatments for disruptive behavior symptoms and disorders in adolescence. Journal of the American Academy of Child and Adolescent Psychiatry, May 2023. URL: https://doi.org/10.1016/j.jaac.2022.05.002, doi:10.1016/j.jaac.2022.05.002. This article has 17 citations and is from a highest quality peer-reviewed journal.

12. (helander2024theefficacyof pages 1-2): Maria Helander, Martin Asperholm, Dan Wetterborg, Lars-Göran Öst, Clara Hellner, Agneta Herlitz, and Pia Enebrink. The efficacy of parent management training with or without involving the child in the treatment among children with clinical levels of disruptive behavior: a meta-analysis. Child Psychiatry and Human Development, 55:164-181, Jul 2024. URL: https://doi.org/10.1007/s10578-022-01367-y, doi:10.1007/s10578-022-01367-y. This article has 69 citations and is from a peer-reviewed journal.

13. (perlstein2023treatmentofchildhood pages 1-3): Samantha Perlstein, Maddy Fair, Emily Hong, and Rebecca Waller. Treatment of childhood disruptive behavior disorders and callous-unemotional traits: a systematic review and two multilevel meta-analyses. Journal of child psychology and psychiatry, and allied disciplines, 64:1372-1387, Mar 2023. URL: https://doi.org/10.1111/jcpp.13774, doi:10.1111/jcpp.13774. This article has 121 citations.

14. (perlstein2023treatmentofchildhood pages 11-12): Samantha Perlstein, Maddy Fair, Emily Hong, and Rebecca Waller. Treatment of childhood disruptive behavior disorders and callous-unemotional traits: a systematic review and two multilevel meta-analyses. Journal of child psychology and psychiatry, and allied disciplines, 64:1372-1387, Mar 2023. URL: https://doi.org/10.1111/jcpp.13774, doi:10.1111/jcpp.13774. This article has 121 citations.

15. (littell2023functionalfamilytherapy pages 1-2): Julia H. Littell, Therese D. Pigott, Karianne H. Nilsen, Jennifer Roberts, and Travis K. Labrum. Functional family therapy for families of youth (age 11–18) with behaviour problems: a systematic review and meta‐analysis. Campbell Systematic Reviews, Jul 2023. URL: https://doi.org/10.1002/cl2.1324, doi:10.1002/cl2.1324. This article has 32 citations and is from a peer-reviewed journal.

16. (ozbay2024conductdisorderan pages 2-3): Ahmet ÖZBAY, Osman ÖZÇELİK, and Süleyman KAHRAMAN. Conduct disorder: an update. Psikiyatride Güncel Yaklaşımlar, 16:72-87, Mar 2024. URL: https://doi.org/10.18863/pgy.1331287, doi:10.18863/pgy.1331287. This article has 3 citations.

17. (lacy2023selectivelypredictingthe pages 1-2): Nina de Lacy and Michael J. Ramshaw. Selectively predicting the onset of adhd, oppositional defiant disorder, and conduct disorder in early adolescence with high accuracy. Frontiers in Psychiatry, Dec 2023. URL: https://doi.org/10.3389/fpsyt.2023.1280326, doi:10.3389/fpsyt.2023.1280326. This article has 11 citations.

18. (koyama2024geneticsofchild pages 1-2): Emiko Koyama, Tuana Kant, Atsushi Takata, James L. Kennedy, and Clement C. Zai. Genetics of child aggression, a systematic review. Translational Psychiatry, Jun 2024. URL: https://doi.org/10.1038/s41398-024-02870-7, doi:10.1038/s41398-024-02870-7. This article has 50 citations and is from a peer-reviewed journal.

19. (koyama2024geneticsofchild pages 3-4): Emiko Koyama, Tuana Kant, Atsushi Takata, James L. Kennedy, and Clement C. Zai. Genetics of child aggression, a systematic review. Translational Psychiatry, Jun 2024. URL: https://doi.org/10.1038/s41398-024-02870-7, doi:10.1038/s41398-024-02870-7. This article has 50 citations and is from a peer-reviewed journal.

20. (frach2024examiningintergenerationalrisk pages 1-2): Leonard Frach, Wikus Barkhuizen, Andrea G. Allegrini, Helga Ask, Laurie J. Hannigan, Elizabeth C. Corfield, Ole A. Andreassen, Frank Dudbridge, Eivind Ystrom, Alexandra Havdahl, and Jean-Baptiste Pingault. Examining intergenerational risk factors for conduct problems using polygenic scores in the norwegian mother, father and child cohort study. Molecular Psychiatry, 29:951-961, Jan 2024. URL: https://doi.org/10.1038/s41380-023-02383-7, doi:10.1038/s41380-023-02383-7. This article has 24 citations and is from a highest quality peer-reviewed journal.

21. (frach2024examiningintergenerationalrisk pages 6-7): Leonard Frach, Wikus Barkhuizen, Andrea G. Allegrini, Helga Ask, Laurie J. Hannigan, Elizabeth C. Corfield, Ole A. Andreassen, Frank Dudbridge, Eivind Ystrom, Alexandra Havdahl, and Jean-Baptiste Pingault. Examining intergenerational risk factors for conduct problems using polygenic scores in the norwegian mother, father and child cohort study. Molecular Psychiatry, 29:951-961, Jan 2024. URL: https://doi.org/10.1038/s41380-023-02383-7, doi:10.1038/s41380-023-02383-7. This article has 24 citations and is from a highest quality peer-reviewed journal.

22. (koyama2024geneticsofchild pages 23-24): Emiko Koyama, Tuana Kant, Atsushi Takata, James L. Kennedy, and Clement C. Zai. Genetics of child aggression, a systematic review. Translational Psychiatry, Jun 2024. URL: https://doi.org/10.1038/s41398-024-02870-7, doi:10.1038/s41398-024-02870-7. This article has 50 citations and is from a peer-reviewed journal.

23. (masi2023contemporarydiagnosisand pages 7-10): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

24. (cortese2023candidatediagnosticbiomarkers pages 1-2): Samuele Cortese, Marco Solmi, Giorgia Michelini, Alessio Bellato, Christina Blanner, Andrea Canozzi, Luis Eudave, Luis C. Farhat, Mikkel Højlund, Ole Köhler‐Forsberg, Douglas Teixeira Leffa, Christopher Rohde, Gonzalo Salazar de Pablo, Giovanni Vita, Rikke Wesselhoeft, Joanna Martin, Sarah Baumeister, Natali S. Bozhilova, Christina O. Carlisi, Virginia Carter Leno, Dorothea L. Floris, Nathalie E. Holz, Eline J. Kraaijenvanger, Seda Sacu, Isabella Vainieri, Giovanni Ostuzzi, Corrado Barbui, and Christoph U. Correll. Candidate diagnostic biomarkers for neurodevelopmental disorders in children and adolescents: a systematic review. World Psychiatry, 22:129-149, Jan 2023. URL: https://doi.org/10.1002/wps.21037, doi:10.1002/wps.21037. This article has 154 citations and is from a highest quality peer-reviewed journal.

25. (cortese2023candidatediagnosticbiomarkers pages 12-13): Samuele Cortese, Marco Solmi, Giorgia Michelini, Alessio Bellato, Christina Blanner, Andrea Canozzi, Luis Eudave, Luis C. Farhat, Mikkel Højlund, Ole Köhler‐Forsberg, Douglas Teixeira Leffa, Christopher Rohde, Gonzalo Salazar de Pablo, Giovanni Vita, Rikke Wesselhoeft, Joanna Martin, Sarah Baumeister, Natali S. Bozhilova, Christina O. Carlisi, Virginia Carter Leno, Dorothea L. Floris, Nathalie E. Holz, Eline J. Kraaijenvanger, Seda Sacu, Isabella Vainieri, Giovanni Ostuzzi, Corrado Barbui, and Christoph U. Correll. Candidate diagnostic biomarkers for neurodevelopmental disorders in children and adolescents: a systematic review. World Psychiatry, 22:129-149, Jan 2023. URL: https://doi.org/10.1002/wps.21037, doi:10.1002/wps.21037. This article has 154 citations and is from a highest quality peer-reviewed journal.

26. (cortese2023candidatediagnosticbiomarkers pages 2-3): Samuele Cortese, Marco Solmi, Giorgia Michelini, Alessio Bellato, Christina Blanner, Andrea Canozzi, Luis Eudave, Luis C. Farhat, Mikkel Højlund, Ole Köhler‐Forsberg, Douglas Teixeira Leffa, Christopher Rohde, Gonzalo Salazar de Pablo, Giovanni Vita, Rikke Wesselhoeft, Joanna Martin, Sarah Baumeister, Natali S. Bozhilova, Christina O. Carlisi, Virginia Carter Leno, Dorothea L. Floris, Nathalie E. Holz, Eline J. Kraaijenvanger, Seda Sacu, Isabella Vainieri, Giovanni Ostuzzi, Corrado Barbui, and Christoph U. Correll. Candidate diagnostic biomarkers for neurodevelopmental disorders in children and adolescents: a systematic review. World Psychiatry, 22:129-149, Jan 2023. URL: https://doi.org/10.1002/wps.21037, doi:10.1002/wps.21037. This article has 154 citations and is from a highest quality peer-reviewed journal.

27. (masi2023contemporarydiagnosisand pages 25-28): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

28. (masi2023contemporarydiagnosisand pages 22-25): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

29. (masi2023contemporarydiagnosisand pages 50-52): Gabriele Masi, Sara Carucci, Pietro Muratori, Carla Balia, Gianluca Sesso, and Annarita Milone. Contemporary diagnosis and treatment of conduct disorder in youth. Expert Review of Neurotherapeutics, 23:1277-1296, Oct 2023. URL: https://doi.org/10.1080/14737175.2023.2271169, doi:10.1080/14737175.2023.2271169. This article has 8 citations and is from a peer-reviewed journal.

30. (ozbay2024conductdisorderan pages 1-2): Ahmet ÖZBAY, Osman ÖZÇELİK, and Süleyman KAHRAMAN. Conduct disorder: an update. Psikiyatride Güncel Yaklaşımlar, 16:72-87, Mar 2024. URL: https://doi.org/10.18863/pgy.1331287, doi:10.18863/pgy.1331287. This article has 3 citations.