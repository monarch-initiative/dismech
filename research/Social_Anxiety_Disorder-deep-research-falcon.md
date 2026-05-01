---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:53.741742'
end_time: '2026-04-24T17:17:42.152720'
duration_seconds: 1008.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Social Anxiety Disorder
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
- **Disease Name:** Social Anxiety Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Social Anxiety Disorder** covering all of the
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
- **Disease Name:** Social Anxiety Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Social Anxiety Disorder** covering all of the
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


## Social Anxiety Disorder (SAD) / Social Phobia — Disease Characteristics Research Report (Psychiatric)

### Target disease
- **Disease name:** Social Anxiety Disorder (SAD) 
- **Category:** Psychiatric; anxiety and fear-related disorder
- **MONDO ID:** Not available in the retrieved sources (gap)

### Evidence base note
This report is based on full-text sources retrieved in-tool (peer‑reviewed clinical guidelines, RCTs, meta-analyses, registry-validation studies, and molecular studies) and ClinicalTrials.gov records. Where the template requests items not present in the retrieved corpus (e.g., ICD‑11 code number, OMIM/Orphanet entries, MONDO ID, SAD-specific GWAS lead loci, or extensive PMID-level extraction), these are explicitly noted as gaps.


## 1. Disease Information

### 1.1 What is the disease? (overview and current understanding)
Social Anxiety Disorder is characterized by persistent fear and avoidance of social situations driven by concerns about negative evaluation (e.g., humiliation, rejection), producing clinically significant impairment in daily functioning. A recent expert review defines SAD as “persistent anxiety or avoidance of social situations because of a fear of negative evaluation.” (wolitzkytaylor2023recentadvancesin pages 1-3)

### 1.2 Key identifiers and controlled vocabularies
- **ICD-10:** **F40.1** (Social phobia). This code is used operationally in Swedish national registry research and explicitly stated in a registry-validation study. (vilaplanaperez2020validityandreliability pages 2-5)
- **MeSH:** **Phobia, Social** (as used in PubMed search strategies in a QoL scoping review). (alnemr2024prevalenceofsocial pages 19-20)
- **ICD-11 / DSM-5-TR:** ICD‑11 criteria are referenced in the WFSBP guideline as a basis for treatment indication, but the retrieved excerpt does not provide a specific ICD‑11 code or full diagnostic text; DSM-IV diagnostic criteria are used in key RCTs. (bandelow2023worldfederationof pages 16-20, clark2023morethandoubling pages 2-4)
- **Synonyms/alternative names:** Social anxiety disorder; social phobia. (vilaplanaperez2020validityandreliability pages 1-2)

### 1.3 Evidence-source type (individual vs aggregated)
- **Aggregated disease-level resources:** WFSBP international guideline synthesis and meta-analytic evidence; Japanese society guideline; systematic reviews/meta-analyses. (asakura2023japanesesocietyof pages 1-2, bandelow2023worldfederationof pages 16-20, rejbrand2023standalonevirtualreality pages 1-2)
- **Patient-level/clinical files:** Swedish National Patient Register chart review validating SAD coding. (vilaplanaperez2020validityandreliability pages 1-2)
- **Molecular profiling in humans:** Peripheral blood RNA-seq and EWAS studies. (edelmann2023bloodtranscriptomeanalysis pages 1-2, wiegand2021dnamethylationdifferences pages 1-2)


## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
SAD is widely described as multifactorial, involving both genetic and environmental contributors. A transcriptome study states: “Multiple genetic as well as environmental factors contribute to the etiopathology of SAD.” (edelmann2023bloodtranscriptomeanalysis pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors (familial aggregation and heritability)
A 2024 genetics-focused chapter summarizes family and twin evidence indicating that SAD “runs in families,” including findings that risk increases with genetic relatedness and that partners of affected individuals are about **four times** more likely to have SAD—interpreted as consistent with assortative mating. (bashoogendam2024geneticvulnerabilityto pages 1-6)

Twin evidence summarized in the same chapter reports a meta-analytic estimate that genetic factors explain ~**0.41** of variance in social anxiety, while non-shared environmental factors explain ~**0.54** (shared environment less prominent). (bashoogendam2024geneticvulnerabilityto pages 1-6)

**Gap:** SAD-specific GWAS loci / polygenic risk scores were not available in the retrieved full texts.

#### Environmental risk factors
Early-life stress/adversity is repeatedly highlighted as a major environmental risk factor for later SAD. The blood transcriptome study states: “One of the main risk factors for SAD is stress, especially during early periods of life (early life adversity; ELA).” (edelmann2023bloodtranscriptomeanalysis pages 1-2)

### 2.3 Protective factors
Direct protective factors specific to SAD were not identified in the retrieved corpus. (gap)

### 2.4 Gene–environment interaction and epigenetics
#### Epigenome-wide association study (EWAS)
A 2021 EWAS identified SAD-associated differentially methylated regions (DMRs) in **SLC43A2** and **TNXB**, with mean methylation differences reported on the order of ~**9.3%** and **5.3%** across sites, respectively. (wiegand2021dnamethylationdifferences pages 3-6)

The same study identified ELA-associated DMRs in the **SLC17A3** promoter and **SIAH3**, with mean methylation differences ~**8.7%** and **10.6%**, and multiple DMRs associated with **SAD×ELA interaction**, including regions in **C2CD2L** and **MRPL28** showing among the largest methylation differences. (wiegand2021dnamethylationdifferences pages 3-6)


## 3. Phenotypes

### 3.1 Core symptom/behavioral phenotype spectrum
Commonly emphasized phenotypes include:
- fear of negative evaluation and humiliation;
- avoidance of social situations;
- performance/public-speaking anxiety;
- functional impairment in work and social life. (wolitzkytaylor2023recentadvancesin pages 1-3, clark2023morethandoubling pages 1-2, rejbrand2023standalonevirtualreality pages 1-2)

### 3.2 Suggested HPO terms (examples)
The retrieved sources do not provide canonical HPO mappings; below are suggested phenotype anchors consistent with the measures and constructs explicitly used:
- **Social withdrawal** (HPO: HP:0000726) (conceptual alignment with avoidance/withdrawal) (wolitzkytaylor2023recentadvancesin pages 1-3)
- **Anxiety** (HPO: HP:0000739) (clark2023morethandoubling pages 4-5)
- **Performance anxiety** (mapped to performance-only subtype discussed in DSM-5 context in VRET review) (rejbrand2023standalonevirtualreality pages 1-2)
- **Fear of negative evaluation** (anchored to FNE scale used in SAD trials) (clark2023morethandoubling pages 4-5)

(Additional phenotype/HPO suggestions are summarized in the structured table artifact.)

### 3.3 Quality of life and functional impact
SAD is associated with substantial impairment. In Swedish registry validation, reviewed cases were described as in the moderate range of severity and functional impairment using CGI-S and GAF in chart review. (vilaplanaperez2020validityandreliability pages 1-2)


## 4. Genetic/Molecular Information

### 4.1 Causal genes
No single causal gene is established in the retrieved sources; evidence supports polygenic/multifactorial liability. (bashoogendam2024geneticvulnerabilityto pages 1-6)

### 4.2 Molecular profiling evidence
#### Peripheral blood transcriptomics (RNA-seq)
A 2023 peripheral blood RNA-seq study found **13** differentially expressed genes (DEGs) associated with SAD, with **MAPK3** reported as the most significantly expressed gene (upregulated in SAD; p=0.003 in the abstract). Functional enrichment implicated “signal transduction pathways” and “inflammatory responses,” supporting immune-system involvement in the association between ELA and SAD, but concluded no direct transcriptional mediation of ELA→SAD. (edelmann2023bloodtranscriptomeanalysis pages 1-2)

Network enrichment and interactome analysis highlighted immune-related signal transduction and MAPK/STAT involvement, including **STAT3**, **RAF1**, and **PTPN7** as relevant to MAPK3-linked immune signaling. (edelmann2023bloodtranscriptomeanalysis pages 6-7)

#### Epigenetics (DNA methylation)
See Section 2.4 for EWAS results (SLC43A2, TNXB; and ELA-linked DMRs). (wiegand2021dnamethylationdifferences pages 3-6)


## 5. Environmental Information

The retrieved sources emphasize psychosocial stress/ELA as a major environmental factor and a mechanistic driver via immune dysregulation and long-lasting gene-expression regulation. (edelmann2023bloodtranscriptomeanalysis pages 1-2)


## 6. Mechanism / Pathophysiology

### 6.1 Psychological/cognitive mechanisms (core modern model)
A key contemporary mechanistic framing is the cognitive model of social phobia (Clark & Wells), operationalized in CT-SAD interventions; targeted maintenance processes include self-focused attention, safety behaviors, distorted self-imagery, and trauma-related social memories. The iCT-SAD RCT describes a protocol implementing these components (e.g., video feedback, behavioral experiments, discrimination training/memory rescripting for early socially traumatic memories). (clark2023morethandoubling pages 2-4)

### 6.2 Stress-immune-signal transduction mechanisms (molecular)
The blood transcriptome study frames ELA as producing “structural and regulatory alterations,” including immune dysregulation, and reports signal transduction and inflammatory enrichment; MAPK3 upregulation is highlighted, with network-level links to JAK–STAT/interleukin-related signaling modules in ELA. (edelmann2023bloodtranscriptomeanalysis pages 1-2, edelmann2023bloodtranscriptomeanalysis pages 6-7)

### 6.3 Biomarker status (expert consensus)
The WFSBP guideline notes that despite extensive neurobiology research, “no biomarker has to date proven sufficiently sensitive and specific.” (bandelow2023worldfederationof pages 16-20)

### 6.4 Suggested ontology terms for mechanisms (examples)
- **GO biological process (examples):** signal transduction; MAPK cascade; cytokine-mediated signaling; interleukin-21 production / regulation themes (immune regulation mentioned in transcriptome enrichment context) (edelmann2023bloodtranscriptomeanalysis pages 6-7)
- **CL cell types (examples):** CD4+ T cell / T-helper differentiation references appear in immune discussion of STAT3-related pathways (edelmann2023bloodtranscriptomeanalysis pages 6-7)
- **UBERON anatomical system:** brain (behavioral/cognitive model) and peripheral blood (molecular profiling sample source). (edelmann2023bloodtranscriptomeanalysis pages 1-2, clark2023morethandoubling pages 2-4)


## 7. Anatomical Structures Affected

Direct SAD-specific neuroimaging anatomical conclusions were not available in the retrieved corpus. Evidence for anxiety disorders more broadly (not SAD-specific) suggests brain structure/function involvement; however, this is not used here as a SAD-specific anatomical claim. (zanoaga2024brainwidemendelianrandomization pages 1-4)


## 8. Temporal Development

### Onset
Mean age of onset for SAD is reported as **14.3 years** in a guideline synthesis referencing a meta-analysis across representative surveys. (bandelow2023worldfederationof pages 16-20)

### Course
SAD is repeatedly described as persistent/chronic and impairing; an RCT background notes it is among the most persistent common mental health problems without treatment, and a 2023 review highlights early onset and persistent course. (wolitzkytaylor2023recentadvancesin pages 1-3, clark2023morethandoubling pages 1-2)


## 9. Inheritance and Population

### 9.1 Epidemiology
- **Lifetime prevalence:** worldwide average lifetime prevalence reported as ~**4%** (also echoed in molecular study intro and BMC registry-validation intro). (vilaplanaperez2020validityandreliability pages 1-2, edelmann2023bloodtranscriptomeanalysis pages 1-2)
- **12-month prevalence:** a mouse-model introduction citing epidemiology reports 12‑month prevalence **6.8%** and lifetime prevalence **12.1%** from NCS-R-era sources, while a more recent expert review reports U.S. 12‑month prevalence ~**8%**. (toth2012socialfearconditioning pages 1-2, wolitzkytaylor2023recentadvancesin pages 1-3)
- **Sex ratio:** female-to-male ratio **1.2–2.1** for SAD in a guideline synthesis. (bandelow2023worldfederationof pages 16-20)

### 9.2 Registry-based population statistics (implementation/data provenance)
Swedish NPR context: **31,975** SAD cases were recorded from 1997–2013; annual incidence increased sharply after 2001 due to outpatient data inclusion. (vilaplanaperez2020validityandreliability pages 2-5)

### 9.3 Inheritance model
Evidence supports **polygenic/multifactorial** inheritance (familial aggregation + heritability), rather than Mendelian inheritance. (bashoogendam2024geneticvulnerabilityto pages 1-6)


## 10. Diagnostics

### 10.1 Diagnostic criteria and structured interviews
In the iCT-SAD RCT, diagnostic assessment used structured clinical interviews including the SAD module of the **ADIS** and screening modules of **SCID-I** and **SCID-II** (with additional modules as indicated). (clark2023morethandoubling pages 2-4)

### 10.2 Validated symptom severity instruments (clinical and research)
- **LSAS** (Liebowitz Social Anxiety Scale)
- **SPIN** (Social Phobia Inventory)
- **SPS** (Social Phobia Scale)
- **SIAS** (Social Interaction Anxiety Scale)
- **FNE** (Fear of Negative Evaluation)
These were core measures in SAD RCT outcome composites. (clark2023morethandoubling pages 4-5)

### 10.3 Registry diagnostic validity
Swedish NPR ICD-10 SAD coding validation: among 95 analyzable medical files, 77 were true positives, PPV **0.81** (95% CI **0.72–0.88**), with substantial inter-rater agreement (κ **0.72**). (vilaplanaperez2020validityandreliability pages 1-2)

### 10.4 Screening / monitoring tools in trials
Trials also used general measures such as **GAD-7** and **PHQ-9** to track anxious/depressed mood and risk. (clark2023morethandoubling pages 4-5)


## 11. Outcome/Prognosis

SAD is associated with substantial functional impairment and persistence; additionally, suicidality links in youth are supported by a 2023 systematic review/meta-analysis showing cross-sectional associations between social anxiety and suicide attempt (r=0.10), suicidal ideation (r=0.22), and suicide risk (r=0.24). (leigh2023socialanxietyand pages 1-2)


## 12. Treatment

### 12.1 Psychotherapy (first-line)
#### CT-SAD / CBT
A 2023 adult guideline for SAD in Japan suggests disorder-specific **CBT** (Clark & Wells or Heimberg models) delivered individually by a skilled therapist (weak recommendation; low certainty), and suggests supported CBT self-help when face-to-face CBT is declined. (asakura2023japanesesocietyof pages 1-2)

#### Internet cognitive therapy (iCT-SAD): real-world implementation evidence
A randomized controlled trial compared face-to-face CT-SAD vs internet-delivered CT-SAD with remote therapist support.
- **Sample:** 102 patients randomized.
- **Efficacy:** iCT-SAD did not differ from CT-SAD on the primary outcome at post-treatment or follow-up.
- **Efficiency:** Total therapist time was **6.45 h** for iCT-SAD vs **15.8 h** for CT-SAD for the same reduction in social anxiety.
- **Mechanistic mediation:** change in process variables specified in cognitive models accounted for **60%** of improvements.
This supports scalable implementation (increasing benefit per therapist-hour). (clark2023morethandoubling pages 1-2)

### 12.2 Technology-enabled exposure: Virtual Reality Exposure Therapy (VRET)
A 2023 systematic review/meta-analysis of **stand-alone** VRET for social anxiety symptoms (PROSPERO CRD42022361900; published 14 Sep 2023) reported:
- **Included studies:** 5 studies in the primary meta-analysis
- **Effect:** standardized mean difference **SMD −0.82** (95% CI −1.52 to −0.13) vs controls
- **Caveat:** few studies, small samples, and high risk of bias. (rejbrand2023standalonevirtualreality pages 1-2, rejbrand2023standalonevirtualreality pages 4-6)

Forest-plot visual evidence for the VRET effect is provided in the extracted figure images. (rejbrand2023standalonevirtualreality media f192a911, rejbrand2023standalonevirtualreality media 5bbbb219)

### 12.3 Pharmacotherapy
#### Guideline recommendations (adults)
Japanese guideline suggests:
- **SSRIs** (weak; low certainty)
- **Venlafaxine (SNRI)** (weak; low certainty)
and does not recommend for/against monotherapy vs combination due to insufficient evidence. (asakura2023japanesesocietyof pages 1-2)

#### Broader quantitative medication response (anxiety disorders)
A 2024 Bayesian hierarchical meta-analysis across anxiety disorders (122 trials; N=15,760) found SSRIs, SNRIs, and benzodiazepines all produced significant improvement vs placebo; benzodiazepines produced faster improvement by week 1, but by week 8 outcomes did not differ significantly between classes; placebo response plateaued by week 4 and social anxiety disorder trials had lower placebo response at week 8 than other anxiety disorders. (mendez2024trajectoryandmagnitude pages 1-2)

### 12.4 MAXO term suggestions (examples)
- **Cognitive behavioral therapy** (CT-SAD; iCT-SAD) (MAXO concept)
- **Exposure therapy** (including VRET)
- **Selective serotonin reuptake inhibitor therapy**
- **Serotonin-norepinephrine reuptake inhibitor therapy**


## 13. Prevention

Direct SAD-specific prevention trials were not retrieved; however, multiple sources emphasize early onset, chronicity, and under-recognition/access barriers, supporting:
- **Secondary prevention:** early detection/screening and early intervention (especially youth), consistent with guideline emphasis on treatment indication and scalability via internet delivery. (bandelow2023worldfederationof pages 16-20, clark2023morethandoubling pages 1-2)
- **Tertiary prevention:** relapse/nonresponse monitoring; comorbidity management (depression, suicidality), consistent with youth suicidality association evidence. (leigh2023socialanxietyand pages 1-2)


## 14. Other Species / Natural Disease

No naturally occurring SAD-equivalent diagnosis in non-human species was retrieved; however, translational fear/avoidance phenotypes are modeled experimentally in rodents (see below). (toth2012socialfearconditioning pages 1-2)


## 15. Model Organisms

### 15.1 Mouse model: Social Fear Conditioning (SFC)
A 2012 Neuropsychopharmacology study developed a **social fear conditioning** mouse paradigm as a “novel and specific animal model to study social anxiety disorder,” in which electric foot shocks are paired with investigation of a conspecific, reducing investigation of unfamiliar conspecifics both short- and long-term and producing social-stimulus-specific fear without generalized anxiety/depression/locomotor impairment. (toth2012socialfearconditioning pages 1-2)

The induced social fear was reversed by **acute diazepam** (dose-dependent) and by **chronic paroxetine**, supporting predictive validity for medications used clinically in SAD. (toth2012socialfearconditioning pages 1-2, toth2012socialfearconditioning pages 9-10)

### 15.2 Translational relevance and limitations
The SFC paradigm supports studying extinction-like processes analogous to exposure-based CBT (repeated social stimulus exposure reduces fear) and enables testing fast-acting vs delayed-onset medications. Limitations include model specificity to conditioned social fear and historical rather than 2023–2024 development. (toth2012socialfearconditioning pages 9-10)


## Recent developments and latest research emphasis (2023–2024)
Key 2023–2024 advancements captured in the retrieved evidence include: 
1) guideline updates emphasizing CBT and SSRI/SNRI first-line approaches (Japan guideline 2023; WFSBP guideline 2023), (asakura2023japanesesocietyof pages 1-2, bandelow2023worldfederationof pages 16-20)
2) scalable digital implementation evidence (iCT-SAD RCT, published 2023), (clark2023morethandoubling pages 1-2)
3) synthesis of stand-alone VRET outcomes (meta-analysis published 2023) with supporting forest-plot evidence, (rejbrand2023standalonevirtualreality pages 1-2, rejbrand2023standalonevirtualreality media f192a911)
4) quantitative meta-analytic modeling of pharmacotherapy response trajectories across anxiety disorders (2024). (mendez2024trajectoryandmagnitude pages 1-2)


## Visual evidence (figures)
- Forest plot(s) for stand-alone VRET meta-analysis: extracted figures showing effect sizes for social anxiety outcomes. (rejbrand2023standalonevirtualreality media f192a911, rejbrand2023standalonevirtualreality media 5bbbb219)


## Structured summary table
The following artifact consolidates identifiers, definitions, epidemiology, risk factors, phenotypes/HPO suggestions, diagnostics, mechanisms, and treatments with quantitative data and direct URLs.

| Claim/Item | Key quantitative data | Evidence type | Source (journal/year) | DOI/URL | Context citation |
|---|---:|---|---|---|---|
| Disease name and synonym | Social anxiety disorder (SAD), also called social phobia | Disease definition / registry validation | BMC Psychiatry / 2020 | https://doi.org/10.1186/s12888-020-02644-7 | (vilaplanaperez2020validityandreliability pages 1-2, vilaplanaperez2020validityandreliability pages 2-5) |
| Core definition | “Persistent anxiety or avoidance of social situations because of a fear of negative evaluation” | Expert review | Faculty Reviews / 2023 | https://doi.org/10.12703/r/12-8 | (wolitzkytaylor2023recentadvancesin pages 1-3) |
| ICD-10 identifier | ICD-10 code **F40.1**; ICD-10 uses the term “social phobia” | Administrative coding / diagnostic validity study | BMC Psychiatry / 2020 | https://doi.org/10.1186/s12888-020-02644-7 | (vilaplanaperez2020validityandreliability pages 2-5) |
| MeSH identifier | MeSH term used in the literature: **“Phobia, Social”** | Literature indexing evidence | Clinical Practice & Epidemiology in Mental Health / 2021 | https://doi.org/10.2174/1745017902117010224 | (alnemr2024prevalenceofsocial pages 19-20) |
| 12-month prevalence | Estimated U.S. 12-month prevalence about **8%** | Expert review / epidemiology synthesis | Faculty Reviews / 2023 | https://doi.org/10.12703/r/12-8 | (wolitzkytaylor2023recentadvancesin pages 1-3) |
| Lifetime prevalence | Average worldwide lifetime prevalence about **4%**; youth-oriented review cites lifetime prevalence about **11%** | Epidemiology review / systematic review | BMC Psychiatry / 2020; Research on Child and Adolescent Psychopathology / 2023 | https://doi.org/10.1186/s12888-020-02644-7; https://doi.org/10.1007/s10802-022-00996-0 | (vilaplanaperez2020validityandreliability pages 1-2, leigh2023socialanxietyand pages 1-2) |
| Typical age of onset | Mean age of onset for SAD **14.3 years** | Guideline evidence synthesis | World Journal of Biological Psychiatry / 2023 | https://doi.org/10.1080/15622975.2022.2086295 | (bandelow2023worldfederationof pages 16-20) |
| Sex ratio | Female:male ratio for SAD about **1.2–2.1** | Guideline evidence synthesis | World Journal of Biological Psychiatry / 2023 | https://doi.org/10.1080/15622975.2022.2086295 | (bandelow2023worldfederationof pages 16-20) |
| Typical clinical cohort age | Mean age of SAD participants in clinical studies **35.2 years** | Guideline evidence synthesis | World Journal of Biological Psychiatry / 2023 | https://doi.org/10.1080/15622975.2022.2086295 | (bandelow2023worldfederationof pages 16-20) |
| Chronicity / course | Described as **early onset**, **persistent/chronic**, and highly impairing if untreated | Expert review / RCT background | Faculty Reviews / 2023; Psychological Medicine / 2023 | https://doi.org/10.12703/r/12-8; https://doi.org/10.1017/S0033291722002008 | (wolitzkytaylor2023recentadvancesin pages 1-3, clark2023morethandoubling pages 1-2) |
| Familial aggregation | In a multigenerational study, first-degree relatives had higher risk than second- and third-degree relatives; partners were about **4×** more likely to have SAD than partners of controls | Family study review | Current Topics in Behavioral Neurosciences / 2024 | https://doi.org/10.1007/7854_2024_544 | (bashoogendam2024geneticvulnerabilityto pages 1-6) |
| Heritability / genetics | Twin meta-analysis estimate for social anxiety variance due to genetics about **0.41**; non-shared environment about **0.54** | Twin-study review | Current Topics in Behavioral Neurosciences / 2024 | https://doi.org/10.1007/7854_2024_544 | (bashoogendam2024geneticvulnerabilityto pages 1-6) |
| Environmental risk factor | Early life adversity (ELA) is described as a major environmental risk factor for SAD | Human molecular / epigenetic / transcriptomic evidence | Translational Psychiatry / 2021; Frontiers in Psychiatry / 2023 | https://doi.org/10.1038/s41398-021-01225-w; https://doi.org/10.3389/fpsyt.2023.1125553 | (edelmann2023bloodtranscriptomeanalysis pages 1-2, wiegand2021dnamethylationdifferences pages 1-2) |
| Gene–environment / transcriptomic link | RNA-seq found **13** DEGs for SAD; **MAPK3** was the most significantly expressed gene and was upregulated in SAD (**p = 0.003**); no direct ELA-related DEGs, suggesting an indirect link via immune-related signal transduction | Human transcriptomics | Frontiers in Psychiatry / 2023 | https://doi.org/10.3389/fpsyt.2023.1125553 | (edelmann2023bloodtranscriptomeanalysis pages 1-2, edelmann2023bloodtranscriptomeanalysis pages 6-7) |
| Immune-related mechanisms | ELA-associated co-expression modules were enriched for **interleukin regulation/production**, **JAK-STAT signaling**, and broader **signal transduction**; MAPK3 interactome highlighted **STAT3**, **RAF1**, **PTPN7** | Human transcriptomics / network analysis | Frontiers in Psychiatry / 2023 | https://doi.org/10.3389/fpsyt.2023.1125553 | (edelmann2023bloodtranscriptomeanalysis pages 6-7) |
| Epigenetic findings: SAD-associated DMRs | First EWAS in SAD identified DMRs in **SLC43A2** and **TNXB**; mean DNAm differences about **9.3%** and **5.3%** respectively | Human epigenome-wide association study | Translational Psychiatry / 2021 | https://doi.org/10.1038/s41398-021-01225-w | (wiegand2021dnamethylationdifferences pages 1-2, wiegand2021dnamethylationdifferences pages 3-6) |
| Epigenetic findings: ELA-associated DMRs | ELA-associated DMRs identified in **SLC17A3** promoter and **SIAH3** with mean DNAm differences about **8.7%** and **10.6%** | Human epigenome-wide association study | Translational Psychiatry / 2021 | https://doi.org/10.1038/s41398-021-01225-w | (wiegand2021dnamethylationdifferences pages 3-6) |
| Epigenetic interaction findings | SAD×ELA interaction DMRs included **C2CD2L** and **MRPL28**; methylation differences exceeded **9%** and **6%** in relevant subgroup contrasts | Human epigenome-wide association study | Translational Psychiatry / 2021 | https://doi.org/10.1038/s41398-021-01225-w | (wiegand2021dnamethylationdifferences pages 3-6) |
| Brain systems implicated in anxiety biology | Genetically inferred causal effects for anxiety involved reduced area/volume in **right posterior middle-cingulate gyrus** and **right anterior superior temporal gyrus** (beta about **-0.09**) | Human MR / imaging genetics (anxiety-disorder level, not SAD-specific) | medRxiv preprint / 2023 | https://doi.org/10.1101/2023.09.12.23295448 | (zanoaga2024brainwidemendelianrandomization pages 1-4) |
| Core phenotype: fear of negative evaluation | Suggested HPO: **HP:0033676 Fear of negative evaluation** | Symptom construct / scale domain | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 4-5) |
| Core phenotype: social avoidance | Suggested HPO: **HP:0000726 Social withdrawal** | Symptom construct / definition | Faculty Reviews / 2023 | https://doi.org/10.12703/r/12-8 | (wolitzkytaylor2023recentadvancesin pages 1-3) |
| Core phenotype: performance/public-speaking anxiety | Suggested HPO: **HP:0033672 Performance anxiety** | Symptom construct / review | Upsala Journal of Medical Sciences / 2023 | https://doi.org/10.48101/ujms.v128.9289 | (rejbrand2023standalonevirtualreality pages 1-2) |
| Core phenotype: functional impairment | Suggested HPO: **HP:0033677 Impaired social functioning** | Clinical impact / registry validation | BMC Psychiatry / 2020 | https://doi.org/10.1186/s12888-020-02644-7 | (vilaplanaperez2020validityandreliability pages 1-2) |
| Core phenotype: anxious mood | Suggested HPO: **HP:0000739 Anxiety** | General symptom domain | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 4-5) |
| Diagnostic instrument: LSAS | Included in primary SAD composite; used as preferred SAD scale in guideline meta-analyses | Clinician/self-report instrument | Psychological Medicine / 2023; WFSBP Guideline / 2023 | https://doi.org/10.1017/S0033291722002008; https://doi.org/10.1080/15622975.2022.2086295 | (clark2023morethandoubling pages 4-5, bandelow2023worldfederationof pages 16-20) |
| Diagnostic instrument: SPIN | Included in primary SAD outcome composite | Self-report instrument | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 4-5) |
| Diagnostic instruments: SPS and SIAS | Used in SAD trials and screening; factorial trial used cut-offs **SPS 22** and **SIAS 33** for inclusion | Self-report instruments / trial implementation | ClinicalTrials.gov NCT04879641; Psychological Medicine / 2023 | https://clinicaltrials.gov/study/NCT04879641; https://doi.org/10.1017/S0033291722002008 | (NCT04879641 chunk 3, clark2023morethandoubling pages 4-5) |
| Diagnostic instrument: FNE | Fear of Negative Evaluation scale included in the primary outcome composite | Self-report instrument | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 4-5) |
| Diagnostic interviews: ADIS / SCID | ADIS, SCID-I, and SCID-II used for structured diagnostic assessment in CT-SAD/iCT-SAD RCT | Structured diagnostic assessment | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 2-4) |
| Registry diagnostic validity | Among **95** reviewed records, **77** were true positives; PPV **0.81** (95% CI **0.72–0.88**); κ **0.72** | Registry validation / chart review | BMC Psychiatry / 2020 | https://doi.org/10.1186/s12888-020-02644-7 | (vilaplanaperez2020validityandreliability pages 1-2) |
| First-line psychotherapy | CBT is first-line; guideline suggests **individual disorder-specific CBT** over group CBT; supported self-help if face-to-face CBT is declined | Clinical guideline | Neuropsychopharmacology Reports / 2023 | https://doi.org/10.1002/npr2.12365 | (asakura2023japanesesocietyof pages 1-2) |
| CT-SAD effectiveness/application | NICE-recommended first-line individual cognitive therapy for SAD; standard protocol allowed up to **14** weekly **90-min** sessions plus boosters | RCT / implementation | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 1-2, clark2023morethandoubling pages 2-4) |
| Internet CT-SAD (iCT-SAD) comparative efficacy | **102** patients randomized; iCT-SAD and CT-SAD both superior to waitlist and **did not differ** on primary outcome at post-treatment/follow-up | Randomized controlled trial | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 1-2) |
| Internet CT-SAD therapist-time efficiency | iCT-SAD total therapist time **6.45 h** versus CT-SAD **15.8 h** for the same reduction in social anxiety; therapist support up to week 14 about **6.8 h**; live contact **4.1 h**; average **21.7** behavioral experiments completed | Randomized controlled trial / implementation | Psychological Medicine / 2023 | https://doi.org/10.1017/S0033291722002008 | (clark2023morethandoubling pages 1-2, clark2023morethandoubling pages 4-5) |
| Virtual reality exposure therapy (VRET) | Stand-alone VRET reduced social anxiety symptoms versus controls with **SMD -0.82** (95% CI **-1.52 to -0.13**); based on **5** studies, high risk of bias | Systematic review and meta-analysis | Upsala Journal of Medical Sciences / 2023 | https://doi.org/10.48101/ujms.v128.9289 | (rejbrand2023standalonevirtualreality pages 1-2, rejbrand2023standalonevirtualreality pages 4-6, rejbrand2023standalonevirtualreality media f192a911) |
| Pharmacotherapy guideline recommendation | **SSRIs** suggested; **venlafaxine (SNRI)** suggested; both recommendations graded **2C** (weak / low certainty) | Clinical guideline | Neuropsychopharmacology Reports / 2023 | https://doi.org/10.1002/npr2.12365 | (asakura2023japanesesocietyof pages 1-2) |
| Anxiety-disorder medication trajectory | Across **122 trials** (**N=15,760**), SSRIs, SNRIs, and benzodiazepines all outperformed placebo; benzodiazepines improved faster by **week 1** (**p < 0.001**); by **week 8** benzodiazepines, SSRIs, and SNRIs did not differ significantly; SAD trials showed lower placebo response at week 8 | Bayesian meta-analysis across anxiety disorders | CNS Spectrums / 2024 | https://doi.org/10.1017/S1092852924000142 | (mendez2024trajectoryandmagnitude pages 1-2) |
| Benzodiazepines role | No longer first-line; commonly used for acute episodic anxiety or adjunctively with SSRIs/SNRIs | Meta-analysis background / pharmacotherapy context | CNS Spectrums / 2024 | https://doi.org/10.1017/S1092852924000142 | (mendez2024trajectoryandmagnitude pages 1-2) |
| Suicidality association in youth | Social anxiety associated cross-sectionally with suicide attempt **r = 0.10**, suicidal ideation **r = 0.22**, suicide risk **r = 0.24** | Systematic review and meta-analysis | Research on Child and Adolescent Psychopathology / 2023 | https://doi.org/10.1007/s10802-022-00996-0 | (leigh2023socialanxietyand pages 1-2) |
| Quality-of-life / educational burden | SAD associated with marked QoL impairment and reduced academic attainment; in a Swedish cohort, odds of finishing upper secondary education were **aOR 0.19** and starting university **aOR 0.47** | Population cohort study / review | Psychological Medicine / 2021; Clinical Practice & Epidemiology in Mental Health / 2021 | https://doi.org/10.1017/S0033291719003908; https://doi.org/10.2174/1745017902117010224 | (alnemr2024prevalenceofsocial pages 19-20) |


*Table: This table compiles key identifiers, epidemiology, mechanisms, phenotypes, diagnostics, and treatment evidence for Social Anxiety Disorder using recent and authoritative sources. It is structured to support rapid knowledge-base entry and citation-backed clinical or translational review.*


## Key gaps relative to template requirements
- **MONDO ID**: not retrieved.
- **ICD-11 code number for SAD**: not retrieved (only criteria mention).
- **OMIM/Orphanet entries**: not retrieved (likely not applicable for a common multifactorial psychiatric disorder).
- **SAD-specific GWAS lead loci and ClinVar/ClinGen pathogenic variants**: not retrieved; evidence supports polygenic risk.
- **Incidence in general population**: not available in retrieved sources; registry incidence trends reflect healthcare-system coding/coverage. (vilaplanaperez2020validityandreliability pages 2-5)



References

1. (wolitzkytaylor2023recentadvancesin pages 1-3): Kate Wolitzky-Taylor and Richard LeBeau. Recent advances in the understanding and psychological treatment of social anxiety disorder. Faculty reviews, 12:8, Apr 2023. URL: https://doi.org/10.12703/r/12-8, doi:10.12703/r/12-8. This article has 27 citations.

2. (vilaplanaperez2020validityandreliability pages 2-5): Alba Vilaplana-Pérez, Josef Isung, Sonja Krig, Sarah Vigerland, Maral Jolstedt, Johan Bjureberg, Jens Högström, Kayoko Isomura, Daniel Rautio, Eva Serlachius, Christian Rück, David Mataix-Cols, and Lorena Fernández de la Cruz. Validity and reliability of social anxiety disorder diagnoses in the swedish national patient register. BMC Psychiatry, May 2020. URL: https://doi.org/10.1186/s12888-020-02644-7, doi:10.1186/s12888-020-02644-7. This article has 30 citations and is from a domain leading peer-reviewed journal.

3. (alnemr2024prevalenceofsocial pages 19-20): Lujain Alnemr, Abdelaziz H. Salama, Salma Abdelrazek, Hussein Alfakeer, Mohamed Ali Alkhateeb, and Perihan Torun. Prevalence of social anxiety disorder and its associated factors among foreign-born undergraduate students in türkiye: a cross-sectional study. PLOS Global Public Health, Apr 2024. URL: https://doi.org/10.1371/journal.pgph.0003184, doi:10.1371/journal.pgph.0003184. This article has 14 citations and is from a peer-reviewed journal.

4. (bandelow2023worldfederationof pages 16-20): Borwin Bandelow, Christer Allgulander, David S. Baldwin, Daniel Lucas da Conceição Costa, Damiaan Denys, Nesrin Dilbaz, Katharina Domschke, Elias Eriksson, Naomi A. Fineberg, Josef Hättenschwiler, Eric Hollander, Hisanobu Kaiya, Tatiana Karavaeva, Siegfried Kasper, Martin Katzman, Yong-Ku Kim, Takeshi Inoue, Leslie Lim, Vasilios Masdrakis, José M. Menchón, Euripedes C. Miguel, Hans-Jürgen Möller, Antonio E. Nardi, Stefano Pallanti, Giampaolo Perna, Dan Rujescu, Vladan Starcevic, Dan J. Stein, Shih-Jen Tsai, Michael Van Ameringen, Anna Vasileva, Zhen Wang, and Joseph Zohar. World federation of societies of biological psychiatry (wfsbp) guidelines for treatment of anxiety, obsessive-compulsive and posttraumatic stress disorders – version 3. part i: anxiety disorders. The World Journal of Biological Psychiatry, 24:79-117, Jul 2023. URL: https://doi.org/10.1080/15622975.2022.2086295, doi:10.1080/15622975.2022.2086295. This article has 262 citations.

5. (clark2023morethandoubling pages 2-4): David M. Clark, Jennifer Wild, Emma Warnock-Parkes, Richard Stott, Nick Grey, Graham Thew, and Anke Ehlers. More than doubling the clinical benefit of each hour of therapist time: a randomised controlled trial of internet cognitive therapy for social anxiety disorder. Psychological Medicine, 53:5022-5032, Jul 2023. URL: https://doi.org/10.1017/s0033291722002008, doi:10.1017/s0033291722002008. This article has 80 citations and is from a highest quality peer-reviewed journal.

6. (vilaplanaperez2020validityandreliability pages 1-2): Alba Vilaplana-Pérez, Josef Isung, Sonja Krig, Sarah Vigerland, Maral Jolstedt, Johan Bjureberg, Jens Högström, Kayoko Isomura, Daniel Rautio, Eva Serlachius, Christian Rück, David Mataix-Cols, and Lorena Fernández de la Cruz. Validity and reliability of social anxiety disorder diagnoses in the swedish national patient register. BMC Psychiatry, May 2020. URL: https://doi.org/10.1186/s12888-020-02644-7, doi:10.1186/s12888-020-02644-7. This article has 30 citations and is from a domain leading peer-reviewed journal.

7. (asakura2023japanesesocietyof pages 1-2): Satoshi Asakura, Naoki Yoshinaga, Hisashi Yamada, Yutaka Fujii, Nobuyuki Mitsui, Yoshihiro Kanai, Takeshi Inoue, and Eiji Shimizu. Japanese society of anxiety and related disorders/japanese society of neuropsychopharmacology: clinical practice guideline for social anxiety disorder (2021). Neuropsychopharmacology Reports, 43:288-309, Aug 2023. URL: https://doi.org/10.1002/npr2.12365, doi:10.1002/npr2.12365. This article has 20 citations.

8. (rejbrand2023standalonevirtualreality pages 1-2): Christian Rejbrand, Brynjar Fure, and Karin Sonnby. Stand-alone virtual reality exposure therapy as a treatment for social anxiety symptoms: a systematic review and meta-analysis. Upsala Journal of Medical Sciences, Sep 2023. URL: https://doi.org/10.48101/ujms.v128.9289, doi:10.48101/ujms.v128.9289. This article has 10 citations and is from a peer-reviewed journal.

9. (edelmann2023bloodtranscriptomeanalysis pages 1-2): Susanne Edelmann, Ariane Wiegand, Thomas Hentrich, Sarah Pasche, Julia Maria Schulze-Hentrich, Matthias H. J. Munk, Andreas J. Fallgatter, Benjamin Kreifelts, and Vanessa Nieratschker. Blood transcriptome analysis suggests an indirect molecular association of early life adversities and adult social anxiety disorder by immune-related signal transduction. Frontiers in Psychiatry, Apr 2023. URL: https://doi.org/10.3389/fpsyt.2023.1125553, doi:10.3389/fpsyt.2023.1125553. This article has 13 citations.

10. (wiegand2021dnamethylationdifferences pages 1-2): Ariane Wiegand, Benjamin Kreifelts, Matthias H. J. Munk, Nadja Geiselhart, Katia E. Ramadori, Julia L. MacIsaac, Andreas J. Fallgatter, Michael S. Kobor, and Vanessa Nieratschker. Dna methylation differences associated with social anxiety disorder and early life adversity. Translational Psychiatry, Feb 2021. URL: https://doi.org/10.1038/s41398-021-01225-w, doi:10.1038/s41398-021-01225-w. This article has 57 citations and is from a peer-reviewed journal.

11. (bashoogendam2024geneticvulnerabilityto pages 1-6): Janna Marie Bas-Hoogendam. Genetic vulnerability to social anxiety disorder. Current topics in behavioral neurosciences, Nov 2024. URL: https://doi.org/10.1007/7854\_2024\_544, doi:10.1007/7854\_2024\_544. This article has 2 citations.

12. (wiegand2021dnamethylationdifferences pages 3-6): Ariane Wiegand, Benjamin Kreifelts, Matthias H. J. Munk, Nadja Geiselhart, Katia E. Ramadori, Julia L. MacIsaac, Andreas J. Fallgatter, Michael S. Kobor, and Vanessa Nieratschker. Dna methylation differences associated with social anxiety disorder and early life adversity. Translational Psychiatry, Feb 2021. URL: https://doi.org/10.1038/s41398-021-01225-w, doi:10.1038/s41398-021-01225-w. This article has 57 citations and is from a peer-reviewed journal.

13. (clark2023morethandoubling pages 1-2): David M. Clark, Jennifer Wild, Emma Warnock-Parkes, Richard Stott, Nick Grey, Graham Thew, and Anke Ehlers. More than doubling the clinical benefit of each hour of therapist time: a randomised controlled trial of internet cognitive therapy for social anxiety disorder. Psychological Medicine, 53:5022-5032, Jul 2023. URL: https://doi.org/10.1017/s0033291722002008, doi:10.1017/s0033291722002008. This article has 80 citations and is from a highest quality peer-reviewed journal.

14. (clark2023morethandoubling pages 4-5): David M. Clark, Jennifer Wild, Emma Warnock-Parkes, Richard Stott, Nick Grey, Graham Thew, and Anke Ehlers. More than doubling the clinical benefit of each hour of therapist time: a randomised controlled trial of internet cognitive therapy for social anxiety disorder. Psychological Medicine, 53:5022-5032, Jul 2023. URL: https://doi.org/10.1017/s0033291722002008, doi:10.1017/s0033291722002008. This article has 80 citations and is from a highest quality peer-reviewed journal.

15. (edelmann2023bloodtranscriptomeanalysis pages 6-7): Susanne Edelmann, Ariane Wiegand, Thomas Hentrich, Sarah Pasche, Julia Maria Schulze-Hentrich, Matthias H. J. Munk, Andreas J. Fallgatter, Benjamin Kreifelts, and Vanessa Nieratschker. Blood transcriptome analysis suggests an indirect molecular association of early life adversities and adult social anxiety disorder by immune-related signal transduction. Frontiers in Psychiatry, Apr 2023. URL: https://doi.org/10.3389/fpsyt.2023.1125553, doi:10.3389/fpsyt.2023.1125553. This article has 13 citations.

16. (zanoaga2024brainwidemendelianrandomization pages 1-4): Mihaela-Diana Zanoaga, Eleni Friligkou, Jun He, Gita A. Pathak, Dora Koller, Brenda Cabrera-Mendoza, Murray B. Stein, and Renato Polimanti. Brainwide mendelian randomization study of anxiety disorders and symptoms. Biological Psychiatry, 95:810-817, Apr 2024. URL: https://doi.org/10.1016/j.biopsych.2023.11.006, doi:10.1016/j.biopsych.2023.11.006. This article has 35 citations and is from a highest quality peer-reviewed journal.

17. (toth2012socialfearconditioning pages 1-2): Iulia Toth, Inga D Neumann, and David A Slattery. Social fear conditioning: a novel and specific animal model to study social anxiety disorder. Neuropsychopharmacology, 37:1433-1443, Jan 2012. URL: https://doi.org/10.1038/npp.2011.329, doi:10.1038/npp.2011.329. This article has 157 citations and is from a highest quality peer-reviewed journal.

18. (leigh2023socialanxietyand pages 1-2): Eleanor Leigh, Kenny Chiu, and Elizabeth D. Ballard. Social anxiety and suicidality in youth: a systematic review and meta-analysis. Research on Child and Adolescent Psychopathology, 51:441-454, Dec 2023. URL: https://doi.org/10.1007/s10802-022-00996-0, doi:10.1007/s10802-022-00996-0. This article has 54 citations and is from a domain leading peer-reviewed journal.

19. (rejbrand2023standalonevirtualreality pages 4-6): Christian Rejbrand, Brynjar Fure, and Karin Sonnby. Stand-alone virtual reality exposure therapy as a treatment for social anxiety symptoms: a systematic review and meta-analysis. Upsala Journal of Medical Sciences, Sep 2023. URL: https://doi.org/10.48101/ujms.v128.9289, doi:10.48101/ujms.v128.9289. This article has 10 citations and is from a peer-reviewed journal.

20. (rejbrand2023standalonevirtualreality media f192a911): Christian Rejbrand, Brynjar Fure, and Karin Sonnby. Stand-alone virtual reality exposure therapy as a treatment for social anxiety symptoms: a systematic review and meta-analysis. Upsala Journal of Medical Sciences, Sep 2023. URL: https://doi.org/10.48101/ujms.v128.9289, doi:10.48101/ujms.v128.9289. This article has 10 citations and is from a peer-reviewed journal.

21. (rejbrand2023standalonevirtualreality media 5bbbb219): Christian Rejbrand, Brynjar Fure, and Karin Sonnby. Stand-alone virtual reality exposure therapy as a treatment for social anxiety symptoms: a systematic review and meta-analysis. Upsala Journal of Medical Sciences, Sep 2023. URL: https://doi.org/10.48101/ujms.v128.9289, doi:10.48101/ujms.v128.9289. This article has 10 citations and is from a peer-reviewed journal.

22. (mendez2024trajectoryandmagnitude pages 1-2): Eric M. Mendez, Jeffrey A. Mills, Vikram Suresh, Julia N. Stimpfl, and Jeffrey R. Strawn. Trajectory and magnitude of response in adults with anxiety disorders: a bayesian hierarchical modeling meta-analysis of selective serotonin reuptake inhibitors, serotonin norepinephrine reuptake inhibitors, and benzodiazepines. CNS Spectrums, 29:187-196, Mar 2024. URL: https://doi.org/10.1017/s1092852924000142, doi:10.1017/s1092852924000142. This article has 13 citations and is from a peer-reviewed journal.

23. (toth2012socialfearconditioning pages 9-10): Iulia Toth, Inga D Neumann, and David A Slattery. Social fear conditioning: a novel and specific animal model to study social anxiety disorder. Neuropsychopharmacology, 37:1433-1443, Jan 2012. URL: https://doi.org/10.1038/npp.2011.329, doi:10.1038/npp.2011.329. This article has 157 citations and is from a highest quality peer-reviewed journal.

24. (NCT04879641 chunk 3):  Optimizing Cognitive-behavioral Therapy for Social Anxiety Disorder Using the Factorial Design. University of Bern. 2021. ClinicalTrials.gov Identifier: NCT04879641