---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T09:45:49.678017'
end_time: '2026-04-28T10:13:35.596302'
duration_seconds: 1665.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Body Dysmorphic Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 5000
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Body Dysmorphic Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Body Dysmorphic Disorder** covering all of the
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
- **Disease Name:** Body Dysmorphic Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Body Dysmorphic Disorder** covering all of the
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


# Body Dysmorphic Disorder (BDD) — Disease Characteristics Research Report (Psychiatric)

**Date prepared:** 2026-04-28  
**Primary recent anchors:** *Nature Reviews Disease Primers* (Dec 2024) and *Psychological Medicine* meta-analysis (Dec 2024 online) (ruck2024bodydysmorphicdisorder. pages 1-3, liu2024theefficacyof pages 1-2)

## 1. Disease information

### 1.1 Concise overview (current understanding)
Body dysmorphic disorder (BDD) is an obsessive–compulsive and related disorder characterized by an intense, persistent **preoccupation with perceived defects or flaws in physical appearance** that are not observable (or are only slight) to others, accompanied by **repetitive behaviors or mental acts** (e.g., checking, camouflaging, comparing) and associated distress/impairment (ruck2024bodydysmorphicdisorder. pages 1-3, ruck2024bodydysmorphicdisorder. pages 9-11).

### 1.2 Key identifiers and classification
- **ICD-11 code:** **6B21 Body dysmorphic disorder** (explicitly identified and defined in the ICD-11 OCRD grouping) (sjogren2019thediagnosticworkup pages 2-4, sjogren2019thediagnosticworkupa pages 2-4).  
  - **Verbatim ICD-11 essential-feature description (as reproduced in Sjögren 2019):** persistent preoccupation with perceived defects (unnoticeable or slight to others), **excessive self-consciousness often with ideas of reference**, and **repetitive/excessive behaviors** (repeated examination, camouflaging/alteration attempts, or marked avoidance) that cause significant distress or impairment (sjogren2019thediagnosticworkupa pages 2-4).
- **DSM-5 / DSM-5-TR context:** BDD is placed in **Obsessive-Compulsive and Related Disorders** and includes an **insight specifier** and a **muscle dysmorphia specifier** (ruck2024bodydysmorphicdisorder. pages 9-11).
- **Other identifiers requested (MONDO, MeSH, OMIM, Orphanet):** not retrievable from the tool-sourced evidence corpus used here; therefore not asserted.

### 1.3 Common synonyms / alternative names
- Body dysmorphia (colloquial; not a formal diagnosis in ICD/DSM) (loewen2024prevalenceofbody pages 1-2). 
- Muscle dysmorphia (DSM specifier; often conceptualized as a BDD specifier/subtype) (ruck2024bodydysmorphicdisorder. pages 9-11).

### 1.4 Evidence-source type
Information in this report is derived from **aggregated disease-level resources** (e.g., *Nature Reviews Disease Primers*), **systematic reviews/meta-analyses**, and **primary human studies** (population surveys, RCTs, fMRI studies), rather than individual EHR-only case series (ruck2024bodydysmorphicdisorder. pages 1-3, liu2024theefficacyof pages 1-2).

## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
BDD etiology is described as an **interplay of genetic and environmental factors**, with comparatively limited biological research versus other OCRDs (ruck2024bodydysmorphicdisorder. pages 1-3, ruck2024bodydysmorphicdisorder. pages 3-4).

### 2.2 Risk factors
**Genetic liability**
- Twin studies suggest **heritability ~37–49%** for BDD-related phenotypes, consistent with partial genetic liability (ruck2024bodydysmorphicdisorder. pages 3-4).
- A key knowledge gap is that **no BDD GWAS exists yet**, limiting locus-level inference (ruck2024bodydysmorphicdisorder. pages 3-4).

**Environmental / psychosocial risk**
- Environmental stressors implicated include **bullying and childhood trauma**, consistent with diathesis–stress models (ruck2024bodydysmorphicdisorder. pages 3-4).

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence; thus this remains **insufficiently characterized** in this report.

### 2.4 Gene–environment interactions
No explicit GxE interaction studies were identified in the retrieved evidence; thus **not currently characterizable here**.

## 3. Phenotypes (clinical presentation)

### 3.1 Core symptoms and behaviors (with frequency data when available)
**Core phenotype**: appearance-related preoccupation, self-focused attention/ideas of reference, repetitive behaviors/mental acts, avoidance, and impaired insight (ruck2024bodydysmorphicdisorder. pages 9-11, sjogren2019thediagnosticworkupa pages 2-4).

**Common body areas of preoccupation (ranges across samples):**
- Skin **50–92%**, hair **47–64%**, nose **33–64%**, face **27–64%**, teeth **30–51%**, weight **29–51%**, stomach **23–53%**, eyes **20–43%**, thighs **17–42%** (ruck2024bodydysmorphicdisorder. pages 32-33).

**Common repetitive behaviors (prevalence ranges across samples):**
- Comparing with others **87–97%**, mirror checking **85–92%**, camouflaging **70–94%**, grooming **59–72%**, reassurance seeking **53–73%**, applying make-up **51–65%**, touching body areas **47–59%**, distraction techniques **45–55%**, clothes changing **44–56%** (ruck2024bodydysmorphicdisorder. pages 32-33).

**Time burden**
- BDD thoughts/behaviors are described as time-consuming, averaging about **3–8 hours/day** in one clinical overview source (champlain2015bodydysmorphicdisorder pages 108-111).

**Insight/delusionality**
- Insight is on a continuum from good to absent (delusional conviction); poor/absent insight can impede help-seeking (ruck2024bodydysmorphicdisorder. pages 9-11, sjogren2019thediagnosticworkup pages 4-5).

### 3.2 Age of onset, severity, and progression
- Onset is typically **before age 18 in ~two-thirds** of cases (ruck2024bodydysmorphicdisorder. pages 1-3, ruck2024bodydysmorphicdisorder. pages 3-4).
- A population-survey summary in Spain reports **mean age of onset 16.9 years** (and in their web sample, mean age of participants meeting BDD criteria was 23.5 years) (loewen2024prevalenceofbody pages 1-2).

### 3.3 Functional impact / quality of life
BDD can lead to profound social/educational/occupational impairment (including isolation/housebound behavior) (ruck2024bodydysmorphicdisorder. pages 9-11). A large impairment signal is also reflected by proportions **not working (36%)** or **not in school (32%)** in cited clinical cohorts (ruck2024bodydysmorphicdisorder. pages 14-16).

### 3.4 Suggested HPO terms (examples)
*(Ontology suggestions; exact mapping should be validated against HPO)*
- Preoccupation/obsessional thoughts: **Obsessive thoughts (HP:0000722)**
- Compulsions/repetitive behaviors: **Compulsive behavior (HP:0008763)**
- Avoidance: **Social withdrawal (HP:0000740)**
- Poor insight/delusional conviction: **Delusions (HP:0000746)**
- Anxiety/depression commonly comorbid: **Anxiety (HP:0000739)**; **Depression (HP:0000716)**

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
BDD is **not currently characterized as a monogenic disorder**, and the retrieved evidence does not support specific causal genes/variants (ruck2024bodydysmorphicdisorder. pages 3-4).

### 4.2 Polygenic liability
- Twin-based heritability estimates support polygenic liability (37–49%), but **gene discovery is limited** and GWAS is absent in the cited primer (ruck2024bodydysmorphicdisorder. pages 3-4).

### 4.3 Epigenetics / chromosomal abnormalities
No BDD-specific epigenetic or chromosomal-abnormality evidence was retrieved.

## 5. Environmental information

BDD risk appears influenced by psychosocial exposures (e.g., bullying/trauma) and sociocultural appearance pressures; the retrieved evidence supports bullying/trauma as relevant stressors but does not provide toxin/radiation/infectious triggers (ruck2024bodydysmorphicdisorder. pages 3-4).

## 6. Mechanism / pathophysiology

### 6.1 Conceptual causal chain (integrated model)
A working model supported by the 2024 primer and human neuroimaging studies is that **genetic liability + adverse developmental/social experiences** predispose to **cognitive-affective and perceptual processing alterations** (e.g., attention biases, aberrant visual processing of faces/bodies). These alterations contribute to **persistent appearance-related preoccupations**, **compulsions/avoidance**, and functional impairment; poor insight and ideas of reference can maintain the cycle and delay care (ruck2024bodydysmorphicdisorder. pages 3-4, ruck2024bodydysmorphicdisorder. pages 9-11).

### 6.2 Visual processing and attention circuitry (human neuroimaging)
- A mechanistic fMRI + eye-tracking experiment in **37 unmedicated adults with BDD** and **30 controls** tested “visual-attention modification” (fixating gaze at the image center while viewing one’s face). The study reports that modulated viewing increased fixation duration and strengthened connectivity from occipital to parietal dorsal visual stream regions in BDD, with persistence into subsequent natural viewing (wong2022neuralandbehavioral pages 1-2). The authors conclude that holding gaze may increase dorsal stream communication and “facilitating global/holistic visual processing,” relevant to perceptual retraining approaches (wong2022neuralandbehavioral pages 1-2).

### 6.3 Serotonergic mechanisms and novel interventions (translational/experimental)
- An open-label neuroimaging study administered **single-dose psilocybin (25 mg)** with psychological support to **8 adults** with moderate-to-severe nondelusional BDD and found **BDD-YBOCS decreases at week 1 and week 12 (p<0.001)**, with rs-fMRI connectivity changes (ECN and ECN–DMN/Salience links) predicting week-1 improvement; authors emphasize the small sample and uncontrolled design (zhu2024singledosepsilocybinalters pages 1-3).

### 6.4 Suggested GO biological process terms (examples)
*(Ontology suggestions; validate in GO)*
- **Visual perception**; **attention**; **response to serotonin**; **fear response**; **learning**.

### 6.5 Suggested CL cell types (examples)
Neural circuitry models implicate cortical and limbic systems; plausible CL terms include **cortical pyramidal neuron** and **GABAergic interneuron** (conceptual; not directly evidenced in retrieved texts).

## 7. Anatomical structures affected

BDD is psychiatric/behavioral but implicates brain systems involved in visual, attentional, and emotional processing.

### 7.1 Organ/system level (UBERON suggestions)
- **Brain (UBERON:0000955)**, including **cerebral cortex (UBERON:0000956)** and **visual cortex** (UBERON term selection dependent on knowledge-base conventions).

### 7.2 Tissue/cell and subcellular levels
No disease-specific tissue pathology or subcellular lesions are described in the retrieved evidence; abnormalities are primarily functional-network level (wong2022neuralandbehavioral pages 1-2, zhu2024singledosepsilocybinalters pages 1-3).

## 8. Temporal development

### 8.1 Onset and course
BDD typically begins in adolescence (two-thirds before 18), and can become chronic with substantial impairment if untreated (ruck2024bodydysmorphicdisorder. pages 1-3, ruck2024bodydysmorphicdisorder. pages 3-4).

### 8.2 Remission patterns
- CBT gains may be **maintained up to 4 years** in follow-up studies cited in the primer (ruck2024bodydysmorphicdisorder. pages 12-14).
- SSRI continuation reduces relapse in an escitalopram relapse-prevention trial (18% relapse on continued escitalopram vs 40% on placebo over 6 months) (ruck2024bodydysmorphicdisorder. pages 12-14).

## 9. Inheritance and population

### 9.1 Epidemiology (recent quantitative data)
- **General adult prevalence (high-income countries):** ~**2%** (ruck2024bodydysmorphicdisorder. pages 1-3).
- **Children <12:** ~**0.1%**; **adolescents:** ~**1.9%**, with adolescent girls **3.4%** vs boys **0.4%** (ruck2024bodydysmorphicdisorder. pages 3-4).
- **Clinical settings (approximate):** ~**7%** inpatient psychiatry, **13%** cosmetic surgery, **11%** dermatology (ruck2024bodydysmorphicdisorder. pages 3-4).
- **Plastic/reconstructive surgery populations (meta-analysis, 65 studies; n=17,107):** **18.6%** (kaleeny2024bodydysmorphicdisorder pages 12-14).
- **Spain web-based survey (Jan 2024, n=2091):** **15.2%** met BDDQ criteria, with higher proportions in women and students; interpretation should consider sampling and survey methodology (loewen2024prevalenceofbody pages 1-2).

### 9.2 Sex ratio and age distribution
- Female preponderance appears stronger in youth; adult sex differences are described as smaller in the primer (ruck2024bodydysmorphicdisorder. pages 3-4).

### 9.3 Comorbidity (visual evidence)
The primer reports high psychiatric comorbidity; Figure 1 in the primer summarizes comorbidity prevalence patterns in adults vs young people (ruck2024bodydysmorphicdisorder. media f77f1d9b).

## 10. Diagnostics

### 10.1 Clinical criteria (ICD-11/DSM framing)
Diagnosis requires: appearance preoccupation + repetitive behaviors/mental acts and associated distress/impairment; eating-disorder explanations should be excluded (ruck2024bodydysmorphicdisorder. pages 9-11, sjogren2019thediagnosticworkupa pages 2-4).

### 10.2 Screening and diagnostic instruments
- **Brief screening tools:** BDDQ; COPS (cosmetic procedure screening) (ruck2024bodydysmorphicdisorder. pages 11-12). Dermatology/cosmetic variants include **BDDQ-DV** and **DCQ** (sjogren2019thediagnosticworkupa pages 2-4).
- **Structured/semi-structured diagnostic interviews:** BDD Module; DIAMOND; SCID BDD module referenced in diagnostic work-up literature (ruck2024bodydysmorphicdisorder. pages 11-12, sjogren2019thediagnosticworkupa pages 2-4).
- **Severity scales:** clinician-rated **BDD-YBOCS** and **BDD-YBOCS-A** (ruck2024bodydysmorphicdisorder. pages 11-12).
  - **Response definition:** ≥**30%** reduction in BDD-YBOCS/BDD-YBOCS-A (ruck2024bodydysmorphicdisorder. pages 11-12).  
  - **Partial/full remission:** BDD-YBOCS ≤**16** (ruck2024bodydysmorphicdisorder. pages 11-12).
- **No laboratory tests** are required/used diagnostically in the diagnostic work-up review (sjogren2019thediagnosticworkupa pages 2-4).

### 10.3 Differential diagnosis (examples)
Differentials include eating disorders (shape/weight focus), OCD, psychotic disorders, social anxiety disorder, trichotillomania/excoriation disorder, gender dysphoria, and other OCRDs; careful assessment of insight and symptom focus is emphasized (sjogren2019thediagnosticworkup pages 4-5, ruck2024bodydysmorphicdisorder. pages 9-11).

## 11. Outcome / prognosis

### 11.1 Suicidality and mortality risk
- Lifetime suicide attempt prevalence is reported as **10–35%** in the 2024 primer synthesis (ruck2024bodydysmorphicdisorder. pages 3-4).
- A Swedish population-based study cited in the primer found increased suicide risk: **HR 3.47 (95% CI 1.76–6.85)** (ruck2024bodydysmorphicdisorder. pages 3-4).

### 11.2 Morbidity and disability
BDD is associated with marked quality-of-life impairment and functional disability, including occupational and educational non-participation (ruck2024bodydysmorphicdisorder. pages 14-16).

## 12. Treatment

### 12.1 Evidence-based first-line treatments
**Cognitive behavioral therapy (CBT), tailored for BDD**
- The 2024 primer describes CBT as the most evidence-based psychotherapy; a meta-analysis of seven RCTs found a **large effect (d = −1.22)** (ruck2024bodydysmorphicdisorder. pages 12-14).
- **Response rates** (≥30% BDD-YBOCS reduction) range **~40–82%** (ruck2024bodydysmorphicdisorder. pages 12-14).
- **Core components** include psychoeducation, formulation, exposure with response prevention, behavioral experiments, cognitive restructuring, plus techniques like mirror retraining/imagery rescripting/self-compassion (ruck2024bodydysmorphicdisorder. pages 12-14).

**Digital/Internet CBT (implementation-relevant)**
- Digital CBT shows sizable effects (e.g., **d = 1.44 vs waitlist; d = 0.95 vs supportive therapy**) with relatively low therapist input, supporting scalability (ruck2024bodydysmorphicdisorder. pages 12-14).
- A 2024 meta-analysis across 15 RCTs found that mode of delivery (face-to-face vs digital) did not significantly moderate outcomes, and pooled effects improved BDD symptoms (g = −0.97) and QoL (g = 0.44) (liu2024theefficacyof pages 1-2).

**Selective serotonin reuptake inhibitors (SSRIs)**
- SSRIs (fluoxetine, sertraline, escitalopram) are first-line pharmacotherapy; RCTs show **response rates 53–65% vs 18–35%** in control groups (ruck2024bodydysmorphicdisorder. pages 12-14).
- Relapse prevention: continued escitalopram reduced relapse (**18% vs 40%** over 6 months) (ruck2024bodydysmorphicdisorder. pages 12-14).

### 12.2 Augmentation and non-first-line options
- Evidence for antipsychotic augmentation is limited; one RCT found **pimozide augmentation of fluoxetine** was not better than placebo (response rates ~18% in both arms) (ruck2024bodydysmorphicdisorder. pages 14-16).

### 12.3 Experimental/novel therapeutics
- Psilocybin open-label trial with neuroimaging suggests symptom improvements with network-level predictors, but requires larger controlled trials (zhu2024singledosepsilocybinalters pages 1-3).

### 12.4 Real-world implementation and applications
- High BDD prevalence in cosmetic/plastic surgery settings motivates **routine preoperative screening and multidisciplinary care**, with the 2024 plastic-surgery meta-analysis highlighting screening needs and prevalence (18.6%) (kaleeny2024bodydysmorphicdisorder pages 12-14).
- The 2024 primer notes barriers to evidence-based care: poor insight, cosmetic-procedure seeking, stigma, scarcity of trained CBT therapists, and limited dissemination outside specialist centers (ruck2024bodydysmorphicdisorder. pages 12-14).

### 12.5 Suggested MAXO terms (examples)
*(Ontology suggestions; validate in MAXO)*
- Cognitive behavioral therapy; Exposure and response prevention; Selective serotonin reuptake inhibitor therapy; Internet-based psychotherapy; Suicide risk assessment.

## 13. Prevention

Evidence-based prevention strategies are described as lacking; the primer emphasizes need for early detection and dissemination of effective treatments rather than established primary prevention programs (ruck2024bodydysmorphicdisorder. pages 11-12, ruck2024bodydysmorphicdisorder. pages 12-14).

## 14. Other species / natural disease

No validated naturally occurring BDD analogs in other species were identified in the retrieved evidence.

## 15. Model organisms

No model-organism systems were identified in the retrieved evidence. Current mechanistic work is largely human (neuroimaging/behavioral) (wong2022neuralandbehavioral pages 1-2, zhu2024singledosepsilocybinalters pages 1-3).

---

## Key quantitative snapshot (2023–2024–anchored)

| Domain | Statistic | Population/Setting | Notes/Definition | Source |
|---|---:|---|---|---|
| Epidemiology | ~2% point prevalence | General adult population in high-income countries | Community-based adult prevalence estimate | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 1-3, ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 0.1% | Children aged <12 years | Youth prevalence reported as low before adolescence | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 1.9% | Adolescents | Prevalence rises in adolescence | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 3.4% vs 0.4% | Adolescent girls vs boys | Female preponderance in youth | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | ~7% | Inpatient psychiatry settings | Clinical setting prevalence higher than community prevalence | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 13% | Cosmetic surgery settings | Approximate prevalence in cosmetic surgery clinics | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 11% | Dermatology settings | Approximate prevalence in dermatology clinics | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Epidemiology | 18.6% | Aesthetic and reconstructive plastic surgery populations | Meta-analysis of 65 studies; 17,107 patients | Kaleeny & Janis, 2024 (kaleeny2024bodydysmorphicdisorder pages 12-14) |
| Suicidality | 10–35% | Individuals with BDD | Lifetime suicide attempt prevalence across studies | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Suicidality | HR 3.47 (95% CI 1.76–6.85) | Swedish population-level cohort | >3-fold increased risk of death by suicide | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 3-4) |
| Psychotherapy | d = -1.22 | CBT for BDD | Meta-analysis of 7 RCTs found a large effect on BDD symptoms | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 12-14) |
| Psychotherapy | 40–82% response | CBT-treated BDD samples | Response commonly defined as >=30% reduction on BDD-YBOCS | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 12-14, ruck2024bodydysmorphicdisorder. pages 11-12) |
| Psychotherapy | d = 1.44 vs waitlist; d = 0.95 vs supportive therapy | Digitalized CBT | Evidence suggests benefit comparable to face-to-face formats | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 12-14) |
| Psychotherapy | g = -0.97 | Psychological treatments across 15 RCTs (n=905) | Meta-analysis: improvement in BDD symptoms; benefits sustained 1–6 months | Liu et al., 2024 (liu2024theefficacyof pages 1-2) |
| Pharmacotherapy | 53–65% vs 18–35% | SSRI trials vs controls | First-line SSRIs include fluoxetine, sertraline, escitalopram | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 12-14) |
| Pharmacotherapy | 18% vs 40% relapse over 6 months | Escitalopram responders continuing SSRI vs placebo | Continuation treatment reduced relapse | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 12-14, ruck2024bodydysmorphicdisorder. pages 14-16) |
| Functional impact | 36% not working; 32% not in school | Individuals with BDD | Indicates substantial occupational/educational impairment | Rück et al., 2024 (ruck2024bodydysmorphicdisorder. pages 14-16) |


*Table: This table summarizes key epidemiologic, suicidality, treatment-response, and functional-impact statistics for body dysmorphic disorder from the gathered evidence. It is useful as a compact evidence snapshot for clinical or knowledge-base reporting.*

## Visual evidence (comorbidity patterns)

Figure 1 from the 2024 *Nature Reviews Disease Primers* article provides a visual summary of psychiatric comorbidity prevalence in adults vs young people with BDD (ruck2024bodydysmorphicdisorder. media f77f1d9b).

---

## Reference URLs and publication dates (from retrieved sources)
- Rück C, Mataix-Cols D, Feusner JD, et al. **Body dysmorphic disorder.** *Nature Reviews Disease Primers.* **Dec 2024**. https://doi.org/10.1038/s41572-024-00577-z (ruck2024bodydysmorphicdisorder. pages 1-3)
- Liu Y, Lai L, Wilhelm S, Phillips KA, et al. **The efficacy of psychological treatments on body dysmorphic disorder: a meta-analysis and trial sequential analysis of randomized controlled trials.** *Psychological Medicine.* First published online **03 Dec 2024**. https://doi.org/10.1017/S0033291724002733 (liu2024theefficacyof pages 1-2)
- Loewen Á, Blasco-Fontecilla H, Li C, et al. **Prevalence of Body Dysmorphic Disorder in the Spanish Population: Cross-Sectional Web-Based Questionnaire Study.** *JMIR Formative Research.* **Jan 2024**. https://doi.org/10.2196/46515 (loewen2024prevalenceofbody pages 1-2)
- Kaleeny JD, Janis JE. **Body Dysmorphic Disorder in Aesthetic and Reconstructive Plastic Surgery—A Systematic Review and Meta-Analysis.** *Healthcare (Basel).* **Jul 2024**. https://doi.org/10.3390/healthcare12131333 (kaleeny2024bodydysmorphicdisorder pages 12-14)
- Wong W-W, Rangaprakash D, Diaz-Fong JP, et al. **Neural and behavioral effects of modification of visual attention in body dysmorphic disorder.** *Translational Psychiatry.* **Aug 2022**. https://doi.org/10.1038/s41398-022-02099-2 (wong2022neuralandbehavioral pages 1-2)
- Zhu X, Zhang C, Hellerstein D, et al. **Single-dose psilocybin alters resting state functional networks in patients with body dysmorphic disorder.** *Psychedelics (NY).* Published in final form **2025** (study reports trial ID NCT04656301). https://doi.org/10.61373/pp024r.0028 (zhu2024singledosepsilocybinalters pages 1-3)



References

1. (ruck2024bodydysmorphicdisorder. pages 1-3): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

2. (liu2024theefficacyof pages 1-2): Yinong Liu, Lizu Lai, Sabine Wilhelm, Katharine A. Phillips, Yunxiao Guo, Jennifer L. Greenberg, and Zhihong Ren. The efficacy of psychological treatments on body dysmorphic disorder: a meta-analysis and trial sequential analysis of randomized controlled trials. Psychological Medicine, 54:4048-4061, Nov 2024. URL: https://doi.org/10.1017/s0033291724002733, doi:10.1017/s0033291724002733. This article has 12 citations and is from a highest quality peer-reviewed journal.

3. (ruck2024bodydysmorphicdisorder. pages 9-11): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

4. (sjogren2019thediagnosticworkup pages 2-4): M Sjogren. The diagnostic work-up of body dysmorphic disorder. Unknown journal, 2019.

5. (sjogren2019thediagnosticworkupa pages 2-4): M Sjogren. The diagnostic work-up of body dysmorphic disorder. Unknown journal, 2019.

6. (loewen2024prevalenceofbody pages 1-2): Álvaro Loewen, Hilario Blasco-Fontecilla, Chao Li, Marcos Bella-Fernández, and Belén Ruiz-Antorán. Prevalence of body dysmorphic disorder in the spanish population: cross-sectional web-based questionnaire study. JMIR Formative Research, 8:e46515, Jan 2024. URL: https://doi.org/10.2196/46515, doi:10.2196/46515. This article has 10 citations.

7. (ruck2024bodydysmorphicdisorder. pages 3-4): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

8. (ruck2024bodydysmorphicdisorder. pages 32-33): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

9. (champlain2015bodydysmorphicdisorder pages 108-111): Amanda Champlain and Anne Laumann. Body dysmorphic disorder: screening patients and associated algorithms. ArXiv, pages 147-163, Jan 2015. URL: https://doi.org/10.1007/978-3-319-17867-7\_11, doi:10.1007/978-3-319-17867-7\_11. This article has 5 citations.

10. (sjogren2019thediagnosticworkup pages 4-5): M Sjogren. The diagnostic work-up of body dysmorphic disorder. Unknown journal, 2019.

11. (ruck2024bodydysmorphicdisorder. pages 14-16): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

12. (wong2022neuralandbehavioral pages 1-2): Wan-Wa Wong, D. Rangaprakash, Joel P. Diaz-Fong, Natalie M. Rotstein, Gerhard S. Hellemann, and Jamie D. Feusner. Neural and behavioral effects of modification of visual attention in body dysmorphic disorder. Translational Psychiatry, Aug 2022. URL: https://doi.org/10.1038/s41398-022-02099-2, doi:10.1038/s41398-022-02099-2. This article has 20 citations and is from a peer-reviewed journal.

13. (zhu2024singledosepsilocybinalters pages 1-3): Xi Zhu, Chen Zhang, David Hellerstein, Jamie D. Feusner, Michael G. Wheaton, Gloria J. Gomez, and Franklin R Schneier. Single-dose psilocybin alters resting state functional networks in patients with body dysmorphic disorder. Psychedelics, 1:25-31, Sep 2024. URL: https://doi.org/10.61373/pp024r.0028, doi:10.61373/pp024r.0028. This article has 4 citations.

14. (ruck2024bodydysmorphicdisorder. pages 12-14): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

15. (kaleeny2024bodydysmorphicdisorder pages 12-14): Joseph D. Kaleeny and Jeffrey E. Janis. Body dysmorphic disorder in aesthetic and reconstructive plastic surgery—a systematic review and meta-analysis. Healthcare, 12:1333, Jul 2024. URL: https://doi.org/10.3390/healthcare12131333, doi:10.3390/healthcare12131333. This article has 31 citations.

16. (ruck2024bodydysmorphicdisorder. media f77f1d9b): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.

17. (ruck2024bodydysmorphicdisorder. pages 11-12): Christian Rück, David Mataix-Cols, Jamie D. Feusner, Roseli Gedanke Shavitt, David Veale, Georgina Krebs, and Lorena Fernández de la Cruz. Body dysmorphic disorder. Nature reviews. Disease primers, 10 1:92, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00577-z, doi:10.1038/s41572-024-00577-z. This article has 35 citations.