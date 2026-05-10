---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T04:59:26.375604'
end_time: '2026-05-10T05:15:51.156873'
duration_seconds: 984.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Trifunctional Protein Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Trifunctional Protein Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Trifunctional Protein Deficiency** covering all of the
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
- **Disease Name:** Mitochondrial Trifunctional Protein Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Trifunctional Protein Deficiency** covering all of the
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


## Comprehensive Research Report: Mitochondrial Trifunctional Protein Deficiency (MTPD)

### Executive summary
Mitochondrial trifunctional protein deficiency (MTPD) is an autosomal recessive long‑chain fatty‑acid β‑oxidation disorder caused by biallelic pathogenic variants in **HADHA** and/or **HADHB**, encoding the α and β subunits of the mitochondrial trifunctional protein (TFP/MTP). It presents as a spectrum ranging from lethal neonatal cardiomyopathy/metabolic crisis to later‑onset episodic myopathy/rhabdomyolysis with chronic complications such as peripheral neuropathy and retinopathy. Newborn screening (NBS) via tandem mass spectrometry (MS/MS) acylcarnitines is widely implemented but has variable positive predictive value and can miss milder/atypical cases. Current standard management is dietary and catabolic‑stress prevention; **triheptanoin (C7 triglyceride)** is used in long‑chain FAO disorders and is associated with reduced hospitalization/event burden in cohorts, while **2023–2024 translational work** highlights cardiolipin remodeling defects and gene‑addition rescue strategies in retinal models. (neto2024mitochondrialbioenergeticsand pages 1-2, schwantje2022geneticbiochemicaland pages 2-2, stinton2021newbornscreeningfor pages 5-6, porta2024triheptanoininpatients pages 4-6, devine2024ipscderivedlchaddretinal pages 1-2)

---

## 1. Disease information

### 1.1 Definition and current understanding
**MTPD** is an inherited metabolic disorder in which mitochondrial long‑chain fatty‑acid β‑oxidation is impaired due to deficiency of the mitochondrial trifunctional protein complex. The complex catalyzes the final three steps of long‑chain β‑oxidation and is composed of α and β subunits. (fletcher2012observationsregardingretinopathy pages 1-2, schwantje2022geneticbiochemicaland pages 2-2)

A 2024 mechanistic study summarizes: “**Mitochondrial trifunctional protein (TFP) deficiency is an inherited metabolic disorder leading to a block in long-chain fatty acid β-oxidation**.” (neto2024mitochondrialbioenergeticsand pages 1-2)

### 1.2 Key identifiers (best available from retrieved sources)
- **MONDO:** **MONDO_0012172** “mitochondrial trifunctional protein deficiency” (Open Targets mapping). (OpenTargets Search: mitochondrial trifunctional protein deficiency)
- **OMIM:** **MTPD (complete/generalized)** referenced as **OMIM #609015** and **isolated LCHAD deficiency** referenced as **OMIM #609016** in retrieved literature. (gaston2023ag1528chadha pages 1-2, fletcher2012observationsregardingretinopathy pages 1-2)
- **MeSH / ICD‑10 / ICD‑11:** Not located in the retrieved full‑text evidence set for this run (should be confirmed in MeSH/ICD resources externally).

### 1.3 Synonyms / alternative names
- Mitochondrial trifunctional protein deficiency (MTPD), trifunctional protein deficiency (TFP deficiency), generalized MTP deficiency
- Related MTP disorders (often discussed together for screening/management): **long‑chain 3‑hydroxyacyl‑CoA dehydrogenase deficiency (LCHADD/LCHAD deficiency)** and **long‑chain 3‑ketoacyl‑CoA thiolase deficiency (LCKATD)**. (schwantje2022geneticbiochemicaland pages 2-2, schwantje2022geneticbiochemicaland pages 1-2)

### 1.4 Evidence source type
Evidence in this report is drawn from **aggregated disease resources** (e.g., Open Targets disease mapping) plus **human cohort studies/case series**, **newborn screening systematic reviews**, and **model systems** (mouse and patient‑derived iPSC cellular models). (OpenTargets Search: mitochondrial trifunctional protein deficiency, stinton2021newbornscreeningfor pages 5-6, gaston2023ag1528chadha pages 1-2, devine2024ipscderivedlchaddretinal pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **HADHA** and/or **HADHB** affecting the MTP complex. A 2024 paper states: “**Mutations in HADHA and HADHB, which encode the TFP α and β subunits, respectively, usually result in combined TFP deficiency. A single common mutation, HADHA c.1528G>C … leads to isolated 3-hydroxyacyl-CoA dehydrogenase deficiency**.” (neto2024mitochondrialbioenergeticsand pages 1-2)

**Inheritance:** autosomal recessive. (grunert2021thespectrumof pages 1-2, baydakova2023newacylcarnitineratio pages 1-2)

### 2.2 Risk factors
- **Genetic:** having biallelic pathogenic variants in HADHA/HADHB. (neto2024mitochondrialbioenergeticsand pages 1-2, grunert2021thespectrumof pages 1-2)
- **Physiologic/environmental triggers** (disease decompensation triggers rather than susceptibility loci): catabolic stress including fasting, illness, fever, and exercise. Later‑onset forms can manifest with episodic rhabdomyolysis triggered by fasting/exertion. (grunert2021thespectrumof pages 1-2, baydakova2023newacylcarnitineratio pages 1-2)

### 2.3 Protective factors
No validated genetic protective variants were identified in the retrieved evidence set. Prevention of crises is largely **behavioral/medical** (avoid fasting, prompt sick‑day management). (schwantje2022geneticbiochemicaland pages 2-2, kim2021triheptanoininthe pages 1-2)

### 2.4 Gene–environment interaction (GxE)
The clearest GxE pattern supported by retrieved evidence is **thermo‑sensitivity and fever**: variants leading to thermo‑sensitive enzymes can precipitate episodic myopathic decompensation when body temperature rises (e.g., during febrile illness). (grunert2021thespectrumof pages 1-2)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotype categories (with HPO suggestions)
1. **Neonatal/infantile severe disease** (symptoms/signs)
   - Hypoketotic hypoglycemia (**HP:0001943 Hypoglycemia**, **HP:0002046 Hypoketonemia**) (fletcher2012observationsregardingretinopathy pages 1-2, grunert2021thespectrumof pages 1-2)
   - Metabolic acidosis (**HP:0001942 Metabolic acidosis**) (grunert2021thespectrumof pages 1-2)
   - Cardiomyopathy/arrhythmia (**HP:0001638 Cardiomyopathy**, **HP:0001649 Tachycardia/arrhythmia**) (fletcher2012observationsregardingretinopathy pages 1-2, schwantje2022geneticbiochemicaland pages 1-2)
   - Liver dysfunction (**HP:0001399 Hepatic failure**, **HP:0002910 Elevated transaminases**) (fletcher2012observationsregardingretinopathy pages 1-2, grunert2021thespectrumof pages 1-2)

2. **Infantile/childhood hepatic/cardiac phenotype**
   - Recurrent metabolic decompensation with hypoglycemia and cardiomyopathy (schwantje2022geneticbiochemicaland pages 2-2, schwantje2022geneticbiochemicaland pages 1-2)

3. **Later‑onset neuromyopathic phenotype**
   - Exercise/illness‑triggered rhabdomyolysis (**HP:0003236 Rhabdomyolysis**, **HP:0003201 Myoglobinuria**) (fletcher2012observationsregardingretinopathy pages 1-2, grunert2021thespectrumof pages 1-2)
   - Myopathy/weakness (**HP:0003198 Myopathy**, **HP:0001324 Muscle weakness**) (grunert2021thespectrumof pages 1-2)
   - Peripheral neuropathy (**HP:0009830 Peripheral neuropathy**) (grunert2021thespectrumof pages 1-2)

4. **Chronic complications (notably LCHADD‑predominant)**
   - Pigmentary retinopathy/chorioretinopathy (**HP:0001103 Abnormality of the retina**, **HP:0000486 Retinopathy**) (fletcher2012observationsregardingretinopathy pages 1-2)
   - Progressive peripheral neuropathy (**HP:0009830**) (grunert2021thespectrumof pages 1-2)

### 3.2 Frequency and phenotype statistics from cohorts/series
- **Peripheral neuropathy prevalence:** overall **58%** in one cohort (8 LCHADD; 11 MTPD), with **70% in MTPD vs 50% in LCHADD**; median onset earlier in MTPD (**4.7 vs 15.3 years**, P=0.047). (grunert2021thespectrumof pages 1-2)
- Neuropathy phenotype distribution: **45.5% sensorimotor**, **27.3% pure motor**, **27.3% isolated sensory**. (grunert2021thespectrumof pages 1-2)
- **Retinopathy frequency (LCHADD):** “**In 30 to greater than 50% of cases of isolated LCHAD deficiency**” with pigment changes evident by age 2 in “**around 50%**.” (fletcher2012observationsregardingretinopathy pages 1-2)
- **MTPD vs LCHADD retinopathy/neuropathy contrast:** TFPD long‑term neuropathy “**up to 80%**,” retinopathy with vision loss “**5–13%**.” (fletcher2012observationsregardingretinopathy pages 1-2)
- Dutch NBS era cohort: 13 patients (7 LCHADD, 5 MTPD, 1 LCKATD). Four MTPD and the single LCKATD developed cardiomyopathy and died in early life; among LCHADD, “**Five LCHADD patients developed subclinical neuropathy and/or retinopathy**.” (schwantje2022geneticbiochemicaland pages 1-2, schwantje2022geneticbiochemicaland pages 2-2)

### 3.3 Quality of life impacts (supported proxy endpoints)
Direct QoL instruments specific to MTPD were not prominent in the retrieved primary cohort papers. However, triheptanoin trials in LC‑FAOD report improvements in patient‑reported outcomes (SF‑12v2) alongside reduced event burden. (kim2021triheptanoininthe pages 4-5)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **HADHA** (TFP α‑subunit; includes LCHAD and LCEH activities) (schwantje2022geneticbiochemicaland pages 2-2)
- **HADHB** (TFP β‑subunit; includes long‑chain ketoacyl‑CoA thiolase activity) (schwantje2022geneticbiochemicaland pages 2-2)

### 4.2 Pathogenic variants and variant classes (examples from retrieved sources)
- **Common founder variant for isolated LCHADD:** **HADHA c.1528G>C** (reported as p.E510Q or p.Glu510Gln in retrieved sources), stated to represent **~87% of alleles** in isolated LCHAD deficiency in one 2024 source and **~90%** in European patients in another. (neto2024mitochondrialbioenergeticsand pages 1-2, baydakova2023newacylcarnitineratio pages 1-2)
- **Frameshift (loss‑of‑function) example:** **HADHB c.1059del (p.Gly354AspfsTer10)** (compound heterozygous context in siblings). (schwantje2022geneticbiochemicaland pages 2-2)
- **Deep intronic/splicing example:** **HADHB c.1390‑515_1390‑499del** causing pseudoexon inclusion with premature termination codon. (schwantje2022geneticbiochemicaland pages 2-2)
- **Thermo‑sensitive variant example:** **HADHA c.2132C>T (p.Pro711Leu)** associated with fever‑triggered episodes; enzyme activity and protein expression diminished at 40°C vs 37°C in fibroblasts. (grunert2021thespectrumof pages 1-2)

### 4.3 Genotype–phenotype correlations (high level)
- Homozygosity for **HADHA c.1528G>C** is used to classify **isolated LCHADD**, while other biallelic combinations in HADHA or HADHB more often yield **generalized MTPD** (with different complication patterns and earlier neuropathy). (grunert2021thespectrumof pages 1-2, neto2024mitochondrialbioenergeticsand pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic signatures, or recurrent chromosomal structural variants were identified in the retrieved evidence set.

---

## 5. Environmental information
Environmental *causes* are not supported (Mendelian disorder), but **environmental/physiologic triggers** (fasting, illness, fever, exercise) are strongly implicated in triggering decompensation and rhabdomyolysis, especially in milder/thermo‑sensitive forms. (grunert2021thespectrumof pages 1-2, baydakova2023newacylcarnitineratio pages 1-2)

---

## 6. Mechanism / pathophysiology (with ontology suggestions)

### 6.1 Canonical causal chain (upstream → downstream)
1. **Biallelic HADHA/HADHB variants** → reduced MTP complex stability and/or enzymatic activities (LCEH/LCHAD/LCKAT) (grunert2021thespectrumof pages 1-2, neto2024mitochondrialbioenergeticsand pages 1-2)
2. **Block in long‑chain fatty‑acid β‑oxidation** → reduced energy production/ketogenesis and accumulation of long‑chain hydroxyacyl intermediates (fletcher2012observationsregardingretinopathy pages 1-2, devine2024ipscderivedlchaddretinal pages 1-2)
3. **Accumulation/export of long‑chain 3‑hydroxyacylcarnitines** detectable in blood spots (biomarker) and potentially toxic to tissues (heart, nerve, retina) (baydakova2023newacylcarnitineratio pages 1-2, devine2024ipscderivedlchaddretinal pages 1-2)
4. **Tissue vulnerability under fasting/illness/exercise** → metabolic crises, cardiomyopathy/arrhythmias, rhabdomyolysis; chronic retinal/nerve injury in many patients (fletcher2012observationsregardingretinopathy pages 1-2, grunert2021thespectrumof pages 1-2)

### 6.2 Recent mechanistic developments (2023–2024 prioritized)
**(A) Cardiolipin remodeling and bioenergetics (2024)**
A 2024 JCI Insight study links MTP deficiency to cardiolipin (CL) remodeling defects: “**TFP also catalyzes a step in the remodeling of cardiolipin (CL)**,” and in patient fibroblasts “**CL reduction was universally identified**” with variable MLCL changes and variable oxygen consumption phenotypes. (neto2024mitochondrialbioenergeticsand pages 1-2)

A key figure set showing quantitative CL/MLCL metrics and mitochondrial respiration phenotyping is available from this paper (Figure panels retrieved). (neto2024mitochondrialbioenergeticsand media cb4f3939, neto2024mitochondrialbioenergeticsand media e05c4916)

**GO term suggestions (mechanism):**
- **GO:0006635** fatty acid beta‑oxidation
- **GO:0005739** mitochondrion
- **GO:0004623 / cardiolipin remodeling-related processes** (exact GO term mapping should be validated; the concept is supported by the MLCLAT activity link) (neto2024mitochondrialbioenergeticsand pages 1-2)

**(B) Retinal pigment epithelium (RPE) lipid peroxidation + gene‑addition rescue (2024)**
A 2024 iPSC‑RPE study reports that LCHADD‑RPE “**cannot oxidize palmitate, and release fewer ketones than WT-RPE**,” show DHA‑induced oxidative stress and lipid peroxidation with decreased viability, and are “**rescued by antioxidant agents**.” It further demonstrates proof‑of‑concept gene addition: AAV‑HADHA delivery reduced hydroxyacylcarnitine accumulation and improved oxidative‑stress resistance. (devine2024ipscderivedlchaddretinal pages 1-2)

**GO term suggestions (mechanism):**
- lipid peroxidation (GO mapping should be validated), oxidative stress response

**Cell type (CL) suggestions:**
- **CL:0000066 retinal pigment epithelial cell** (supported conceptually by the iPSC‑RPE model) (devine2024ipscderivedlchaddretinal pages 1-2)

### 6.3 Biochemical abnormalities (diagnostic / mechanistic)
- Elevated long‑chain hydroxyacylcarnitines (e.g., C16‑OH, C18:1‑OH) used for screening. (lotzhavla2018fatalpitfallsin pages 1-2)
- Proposed 2023 biomarker: **HADHA ratio = (C16OH + C18OH + C18:1OH) / C0**, elevated in all **54** confirmed patients in one study. (baydakova2023newacylcarnitineratio pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level (UBERON suggestions)
- **Heart** (UBERON:0000948): cardiomyopathy/arrhythmia; early mortality in severe MTPD/LCKATD. (schwantje2022geneticbiochemicaland pages 1-2)
- **Liver** (UBERON:0002107): hepatic dysfunction/failure in severe forms and some LCHADD presentations. (fletcher2012observationsregardingretinopathy pages 1-2)
- **Skeletal muscle** (UBERON:0001134): episodic myopathy/rhabdomyolysis. (grunert2021thespectrumof pages 1-2)
- **Peripheral nervous system** (UBERON:0000010 concept): peripheral neuropathy as common chronic complication. (grunert2021thespectrumof pages 1-2)
- **Eye/retina/RPE** (UBERON:0000966 retina; RPE concept): progressive retinopathy/chorioretinopathy; mechanistic vulnerability in RPE models. (fletcher2012observationsregardingretinopathy pages 1-2, devine2024ipscderivedlchaddretinal pages 1-2)

### 7.2 Subcellular compartments (GO cellular component suggestions)
- **Mitochondrion** (GO:0005739)
- **Mitochondrial inner membrane** (GO:0005743), relevant to cardiolipin remodeling and respiratory chain organization (neto2024mitochondrialbioenergeticsand pages 1-2)

---

## 8. Temporal development (natural history)
- **Onset:** ranges from neonatal/early‑infantile to childhood/adult. (fletcher2012observationsregardingretinopathy pages 1-2, grunert2021thespectrumof pages 1-2)
- **Progression/course:**
  - Severe forms can lead to early death from cardiomyopathy/metabolic crisis (Dutch cohort: deaths within 1 month to 13 months for MTPD/LCKATD with cardiomyopathy). (schwantje2022geneticbiochemicaland pages 1-2)
  - Later‑onset forms are often episodic (rhabdomyolysis episodes) with risk of progressive/irreversible neuropathy and retinopathy despite early diagnosis and treatment. (grunert2021thespectrumof pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (best available from retrieved sources)
- LCHADD incidence in European populations reported as **<1.5 per 100,000 births** in one 2023 study context. (baydakova2023newacylcarnitineratio pages 1-2)
- Screening paper cites live prevalence **~1:140,000** for MTP/LCHAD deficiency. (lotzhavla2018fatalpitfallsin pages 1-2)

### 9.2 Population genetics / founder effects
The retrieved evidence emphasizes the high frequency of the recurrent **HADHA c.1528G>C** allele in European LCHADD, but detailed geographic/founder breakdowns were not consistently available across primary studies in this run. (neto2024mitochondrialbioenergeticsand pages 1-2, baydakova2023newacylcarnitineratio pages 1-2)

---

## 10. Diagnostics

### 10.1 Core diagnostic tests and biomarkers (real‑world implementation)
1. **Newborn screening (NBS)**
   - MS/MS acylcarnitine profiling in dried blood spots; commonly cited primary markers include **C16‑OH and C18:1‑OH**. (lotzhavla2018fatalpitfallsin pages 1-2)
   - Limitation: “**screening may not identify some patients**” noted in retinopathy-focused clinical review. (fletcher2012observationsregardingretinopathy pages 1-2)

2. **Confirmatory testing**
   - Evidence highlights pitfalls of relying only on plasma acylcarnitines and urine organic acids: “**analyses of acylcarnitines in blood and organic acids in urine alone are not suitable for confirmatory testing**,” with missed cases described when urine organic acids were normal. (lotzhavla2018fatalpitfallsin pages 1-2)
   - Confirmatory workup often requires **molecular testing** (HADHA/HADHB) and/or **functional enzyme studies**. (schwantje2022geneticbiochemicaland pages 2-2)

3. **Improved biochemical metric (2023)**
   - HADHA ratio **(C16OH + C18OH + C18:1OH)/C0** elevated in **all 54** confirmed patients in one study, proposed to reduce false negatives. (baydakova2023newacylcarnitineratio pages 1-2)

### 10.2 NBS test accuracy statistics
A systematic review of NBS test accuracy (acylcarnitines in dried blood spots) reported:
- **~4,000,000 babies screened**, **23 cases** identified (11 reported as LCHAD) (stinton2021newbornscreeningfor pages 5-6)
- **Positive predictive value (PPV) range 0% to 100%**, with specific examples:
  - **0% PPV:** 0 true positives, 28 false positives / 276,565 screened
  - **100% PPV:** 13 true positives, 0 false positives / 2,037,824 screened (stinton2021newbornscreeningfor pages 5-6)
- Sensitivity/specificity/NPV were **not calculable** due to lack of systematic follow‑up of screen‑negative infants. (stinton2021newbornscreeningfor pages 5-6, stinton2021newbornscreeningfor pages 1-2)

### 10.3 Differential diagnosis
Not comprehensively extracted in this run; however, screening pitfalls literature notes false positives can occur in NICU/preterm contexts and emphasizes specialized metabolic evaluation. (stinton2021newbornscreeningfor pages 1-2, lotzhavla2018fatalpitfallsin pages 1-2)

---

## 11. Outcomes / prognosis
- Outcomes are **highly variable**; Dutch cohort data illustrate severe early mortality in generalized MTP deficiencies with cardiomyopathy (“**Four MTPD patients and one LCKATD patient developed cardiomyopathy and died within 1 month and 13 months of life, respectively**.”) (schwantje2022geneticbiochemicaland pages 1-2)
- Even with early diagnosis and therapy, chronic complications may persist: neuropathy may not be preventable in all cases (“**Despite early diagnosis by newborn screening and early initiation of therapy, peripheral neuropathy cannot be prevented in all patients… and has severe impact on the life of affected patients**.”) (grunert2021thespectrumof pages 1-2)

---

## 12. Treatment

### 12.1 Standard management (current practice)
- Avoid fasting and catabolic stress; prompt sick‑day/emergency carbohydrate provision.
- Dietary long‑chain triglyceride restriction and supplementation with medium‑chain triglycerides (MCT) is the historical standard, but does not eliminate symptoms and does not reliably prevent long‑term complications. (kim2021triheptanoininthe pages 1-2, schwantje2022geneticbiochemicaland pages 2-2)

**MAXO suggestions (conceptual, for curation):** dietary fat modification; avoidance of fasting; emergency management of metabolic crisis.

### 12.2 Triheptanoin (Dojolvi/UX007) — evidence and implementation
**Mechanism/role:** an odd‑chain triglyceride providing acetyl‑CoA and propionyl‑CoA (anaplerosis), used for LC‑FAODs including LCHAD/TFP defects. (kim2021triheptanoininthe pages 1-2, NCT01379625 chunk 1)

**Dosing in real-world cohort (Italy, retrospective; publication Oct 2024, URL: https://doi.org/10.1186/s13052-024-01782-y):**
- Mean dose **1.5 ± 0.9 g/kg/day** in four divided administrations, providing **23.9 ± 8.9%** of daily calories; treatment duration **2.2 ± 0.9 years**. (porta2024triheptanoininpatients pages 1-2)

**Outcome statistics (Italy cohort; triheptanoin vs prior MCT):**
- Intercurrent catabolic episodes **4.3 ± 5.3 vs 22.0 ± 22.2** (p=0.034)
- Hospitalized metabolic decompensations **2.0 ± 2.5 vs 18.3 ± 17.7** (p=0.014)
- CK outside decompensation decreased (**828 ± 1238 → 274 ± 242 UI/L**; p=0.207); CK during decompensation decreased (**66,178 ± 57,565 → 30,550 ± 24,958 IU/L**; p=0.218)
- No ICU admissions during triheptanoin treatment; GI adverse effects reported (epigastric pain, diarrhea). (porta2024triheptanoininpatients pages 4-6)

**Trial‑level effect sizes (summarized in 2021 profile; CL201 severe LC‑FAOD; URL: https://doi.org/10.1007/s40267-021-00816-3):**
- Major clinical event rate reduction **48.1%** (1.69 → 0.88 events/year; p=0.021)
- Hospitalization event rate reduction **53.1%** (1.39 → 0.65 events/year; p=0.016)
- Hospitalization duration reduction **51.5%** (5.66 → 2.74 days/year; p=0.032) (kim2021triheptanoininthe pages 4-5)

### 12.3 Clinical trials (applications / real-world pipeline)
- **NCT01379625 (OHSU; randomized, double‑masked phase 2):** triheptanoin vs MCT, 20% energy for 4 months; inclusion includes confirmed **TFP or LCHAD deficiency** among LC‑FAODs; endpoints include energy expenditure and ejection fraction change. (NCT01379625 chunk 1)
- **NCT01886378 (Ultragenyx; open‑label phase 2):** triheptanoin titrated to **25–35% caloric intake**, 24‑week primary period with extension to 78 weeks; includes LCHAD and other LC‑FAODs; functional exercise endpoints. (NCT01886378 chunk 1)
- **NCT05933200 (Ultragenyx; phase 3, quadruple‑masked pediatric):** triheptanoin vs even‑chain MCT; **primary endpoint annualized major clinical event rate**; includes LCHAD/TFP defects. (NCT05933200 chunk 1)
- **NCT02214160 (extension; open‑label):** long‑term MCE rate and safety (TEAEs/serious TEAEs). (NCT02214160 chunk 1)

### 12.4 Emerging/experimental therapeutics (2024 translational)
- **AAV-HADHA gene addition** showed rescue of metabolic and oxidative‑stress phenotypes in patient‑derived iPSC‑RPE, supporting a potential therapy for LCHADD-associated chorioretinopathy (preclinical proof‑of‑concept). (devine2024ipscderivedlchaddretinal pages 1-2)

---

## 13. Prevention
- **Primary prevention:** not applicable in the classic public‑health sense for a Mendelian disorder, but **carrier screening, prenatal testing, and genetic counseling** are standard preventive strategies.
- **Secondary prevention:** NBS enables pre‑symptomatic dietary management; however, evidence shows NBS can miss cases and has variable PPV, so programs consider improved ratios/second‑tier methods. (stinton2021newbornscreeningfor pages 5-6, baydakova2023newacylcarnitineratio pages 1-2, lotzhavla2018fatalpitfallsin pages 1-2)
- **Tertiary prevention:** prevention of metabolic crises via fasting avoidance/sick‑day protocols and potentially triheptanoin to reduce event burden. (porta2024triheptanoininpatients pages 4-6, kim2021triheptanoininthe pages 4-5)

---

## 14. Other species / natural disease
No naturally occurring veterinary disease associations were identified in the retrieved evidence set.

---

## 15. Model organisms and experimental systems

### 15.1 Mouse model (2023)
A CRISPR/Cas9 **Hadha G1528C knock‑in mouse** models the common human LCHADD allele and recapitulates key phenotypes: lower fasting ketones, accumulation of plasma 3‑hydroxyacylcarnitines, earlier treadmill exhaustion, **dilated cardiomyopathy**, and retinal/RPE dysfunction with reduced cone function. (gaston2023ag1528chadha pages 1-2)

### 15.2 Human iPSC cellular model (2024)
Patient‑derived **iPSC‑RPE** shows impaired palmitate oxidation and heightened DHA‑induced lipid peroxidation, reversible with antioxidants and with AAV‑HADHA gene addition (proof‑of‑concept). (devine2024ipscderivedlchaddretinal pages 1-2)

---

## Structured summary table
| Category | Summary |
|---|---|
| Disease / identifiers | **Mitochondrial trifunctional protein deficiency (MTPD)**; MONDO **MONDO:0012172** from Open Targets disease mapping. Related subtype entries in retrieved sources: **MTP deficiency / complete MTP deficiency OMIM 609015** and **isolated LCHAD deficiency OMIM 609016**; LCHADD is treated as an MTP-related deficiency in screening/clinical papers. **MeSH/ICD:** not found in retrieved sources. Data here are from aggregated disease resources plus patient/cohort studies, not EHR-only sources (OpenTargets Search: mitochondrial trifunctional protein deficiency, neto2024mitochondrialbioenergeticsand pages 1-2, schwantje2022geneticbiochemicaland pages 2-2) |
| Causal genes / inheritance / major variants | **Autosomal recessive** disease caused by biallelic variants in **HADHA** (TFP α-subunit; LCEH/LCHAD activities) or **HADHB** (TFP β-subunit; LCKAT activity). Most **HADHA** and all **HADHB** pathogenic variants usually cause generalized MTP deficiency; recurrent **HADHA c.1528G>C** (reported as p.E510Q / p.Glu510Gln in retrieved sources) causes isolated **LCHAD deficiency** and accounts for ~**87% of alleles** in isolated LCHADD in one 2024 review and ~**90% of European patients** in another source. Recent examples include **HADHB c.1059del** plus deep intronic **HADHB c.1390-515_1390-499del** causing aberrant splicing, **HADHA p.Pro711Leu** thermo-sensitive disease, and **HADHB c.1175C>T** adult neuropathic disease (neto2024mitochondrialbioenergeticsand pages 1-2, baydakova2023newacylcarnitineratio pages 1-2, grunert2021thespectrumof pages 1-2, schwantje2022geneticbiochemicaland pages 2-2) |
| Core biochemical biomarkers (NBS / diagnosis) | Newborn screening and diagnostic workup rely on tandem MS acylcarnitine profiling in dried blood spots with elevated long-chain hydroxyacylcarnitines, especially **C16-OH** and **C18:1-OH**; broader marker set reported includes **C14-OH, C14:1-OH, C16-OH, C16:1-OH, C18-OH, C18:1-OH**. A newer 2023 diagnostic metric is the **“HADHA ratio” = (C16OH + C18OH + C18:1OH) / C0**, which was **elevated in all 54 confirmed LCHAD/MTP patients** and not elevated in **19 VLCAD** patients, improving sensitivity/specificity versus standard acylcarnitines alone. Confirmatory diagnosis may require enzymatic and molecular testing because plasma/urine biochemistry alone can miss cases (baydakova2023newacylcarnitineratio pages 1-2, lotzhavla2018fatalpitfallsin pages 1-2, schwantje2022geneticbiochemicaland pages 2-2) |
| Key phenotypic subtypes | **Severe neonatal/infantile form:** hypoketotic hypoglycemia, metabolic acidosis, liver dysfunction, cardiomyopathy, arrhythmia/sudden death. **Infantile hepatic/cardiomyopathic form:** recurrent decompensation, hypoglycemia, cardiomyopathy. **Later-onset neuromyopathic form:** exercise/fasting/fever-triggered rhabdomyolysis, myopathy, peripheral neuropathy; thermo-sensitive forms may have near-normal acylcarnitines at baseline and episodic myopathy with fever. **LCHADD-specific chronic complications:** chorioretinopathy/retinopathy more prominent. **MTPD:** neuropathy more prominent than vision loss. Adult CNS involvement has also been reported (grunert2021thespectrumof pages 1-2, schwantje2022geneticbiochemicaland pages 2-2, fletcher2012observationsregardingretinopathy pages 1-2, devine2024ipscderivedlchaddretinal pages 11-12, gaston2023ag1528chadha pages 1-2) |
| Major complications / frequencies | **Peripheral neuropathy:** overall prevalence **58%** in one cohort; **70% in MTPD vs 50% in LCHADD**; median onset **4.7 y vs 15.3 y** respectively. Neuropathy subtypes: **45.5% sensorimotor**, **27.3% pure motor**, **27.3% isolated sensory**. **Retinopathy:** in isolated LCHADD, irreversible retinopathy reported in **30% to >50%** of cases, with pigment changes by age 2 in **~50%**; peripheral neuropathy in older LCHADD reports **~5–10%**. In TFPD, neuropathy may occur in **up to 80%** long term, while retinopathy with vision loss reported in **5–13%**. In the Dutch post-NBS cohort, **5/7 LCHADD** patients developed subclinical neuropathy and/or retinopathy. **Cardiomyopathy mortality:** **4/5 MTPD** patients and **1/1 LCKATD** patient in the Dutch cohort developed cardiomyopathy and died within **1 month to 13 months** of life (grunert2021thespectrumof pages 1-2, fletcher2012observationsregardingretinopathy pages 1-2, schwantje2022geneticbiochemicaland pages 2-2, schwantje2022geneticbiochemicaland pages 1-2) |
| Epidemiology / screening performance | Retrieved prevalence estimates include **<1.5 per 100,000 births** for LCHADD in European populations and **~1:140,000 live births** for MTP/LCHAD deficiency in one screening paper. NBS performance is variable: systematic review identified **23 babies** with LCHAD/MTP deficiencies across ~**4 million** screened newborns, with PPV ranging from **0%** (0 true positives, 28 false positives / 276,565 screened) to **100%** (13 true positives / 2,037,824 screened). Sensitivity/specificity/NPV could not be calculated because negatives were not systematically followed. False negatives and missed mild cases occur, especially with normal or only mildly abnormal acylcarnitines (stinton2021newbornscreeningfor pages 5-6, stinton2021newbornscreeningfor pages 1-2, lotzhavla2018fatalpitfallsin pages 1-2, schwantje2022geneticbiochemicaland pages 2-2) |
| Current standard management | Standard care centers on **avoidance of fasting**, prevention of catabolic stress, **long-chain fat restriction**, and **medium-chain triglyceride (MCT) supplementation**; emergency feeding during illness is important. Current treatment can reduce hypoglycemia risk but often does **not** prevent cardiomyopathy or later neuropathy/retinopathy. Some reports mention carnitine use and monitoring of free carnitine/acylcarnitines, but benefit remains individualized in retrieved sources (kim2021triheptanoininthe pages 1-2, kochan2025howgenesmeet pages 7-9, schwantje2022geneticbiochemicaland pages 2-2) |
| Triheptanoin / treatment outcomes | **Triheptanoin** is an approved odd-chain MCT for LC-FAODs including LCHAD/TFP-related disease; typical target **25–35% of total daily calories**, given in **≥4 divided doses**. In a 2024 Italian LC-FAOD cohort switching from MCT to triheptanoin, mean dose was **1.5 ± 0.9 g/kg/day**, providing **23.9 ± 8.9%** of calories; **intercurrent catabolic episodes** fell from **22.0 ± 22.2** to **4.3 ± 5.3** (**p=0.034**), **hospitalized metabolic decompensations** from **18.3 ± 17.7** to **2.0 ± 2.5** (**p=0.014**), with lower non-decompensation CK in 7 patients and no ICU admissions on treatment. In CL201 summarized in a 2021 profile, triheptanoin reduced mean annualized major clinical event rate by **48.1%** (**1.69 to 0.88 events/year; p=0.021**) and hospitalization event rate by **53.1%** (**1.39 to 0.65/year; p=0.016**). GI adverse effects (diarrhea, epigastric pain) are the most common. Severe neonatal cardiomyopathy may still fail to respond in some cases (porta2024triheptanoininpatients pages 1-2, porta2024triheptanoininpatients pages 4-6, kim2021triheptanoininthe pages 4-5, kim2021triheptanoininthe pages 1-2, NCT01886378 chunk 1, NCT02214160 chunk 1) |
| Recent mechanistic / translational developments (2023–2024) | **2024 JCI Insight:** patient fibroblasts showed **universal cardiolipin reduction** with variable monolysocardiolipin increase and heterogeneous bioenergetic impairment, linking MTP deficiency to defective cardiolipin remodeling and genotype-dependent mitochondrial dysfunction. **2024 iPSC-RPE model:** LCHADD RPE cells accumulated 3-hydroxyacylcarnitines, failed to oxidize palmitate, released fewer ketones, and were vulnerable to **DHA-induced oxidative stress/lipid peroxidation**; antioxidant rescue and **AAV-HADHA** gene addition improved these defects. **2023 knock-in mouse:** Hadha G1528C mice recapitulated lower fasting ketones, plasma 3-hydroxyacylcarnitine accumulation, dilated cardiomyopathy, retinal dysfunction, and motor deficits (neto2024mitochondrialbioenergeticsand pages 1-2, devine2024ipscderivedlchaddretinal pages 11-12, devine2024ipscderivedlchaddretinal pages 1-2, gaston2023ag1528chadha pages 1-2, neto2024mitochondrialbioenergeticsand media cb4f3939) |


*Table: This table condenses the most actionable evidence for mitochondrial trifunctional protein deficiency, including identifiers, genetics, diagnostic biomarkers, major phenotypes, complication frequencies, and current treatment data. It is designed as a quick-reference artifact for building a structured disease knowledge base entry.*

---

## Figures (visual evidence)
- Quantitative cardiolipin/monolysocardiolipin remodeling and mitochondrial respiration phenotyping in MTP‑deficient patient fibroblasts (JCI Insight 2024; figure panels retrieved). (neto2024mitochondrialbioenergeticsand media cb4f3939, neto2024mitochondrialbioenergeticsand media e05c4916)

---

## Notes on gaps / items not resolved in this tool-assisted run
- **ICD/MeSH identifiers** were not located in the retrieved evidence set; they should be verified via OMIM/Orphanet/MeSH/ICD resources.
- **Maternal AFLP/HELLP association** is widely discussed in the broader literature for fetal FAO disorders, but primary sources specifically evidencing this association were not successfully incorporated into the citeable evidence set in this run.



References

1. (neto2024mitochondrialbioenergeticsand pages 1-2): Eduardo Vieira Neto, Meicheng Wang, Austin J. Szuminsky, Lethicia Ferraro, Erik Koppes, Yudong Wang, Clinton Van’t Land, Al-Walid Mohsen, Geancarlo Zanatta, Areeg H. El-Gharbawy, Tamil S. Anthonymuthu, Yulia Y. Tyurina, Vladimir A. Tyurin, Valerian Kagan, Hülya Bayır, and Jerry Vockley. Mitochondrial bioenergetics and cardiolipin remodeling abnormalities in mitochondrial trifunctional protein deficiency. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.176887, doi:10.1172/jci.insight.176887. This article has 16 citations and is from a domain leading peer-reviewed journal.

2. (schwantje2022geneticbiochemicaland pages 2-2): Marit Schwantje, Sabine A. Fuchs, Lonneke de Boer, Annet M. Bosch, Inge Cuppen, Eugenie Dekkers, Terry G. J. Derks, Sacha Ferdinandusse, Lodewijk Ijlst, Riekelt H. Houtkooper, Rose Maase, W. Ludo van der Pol, Maaike C. de Vries, Rendelien K. Verschoof‐Puite, Ronald J. A. Wanders, Monique Williams, Frits Wijburg, and Gepke Visser. Genetic, biochemical, and clinical spectrum of patients with mitochondrial trifunctional protein deficiency identified after the introduction of newborn screening in the netherlands. Journal of Inherited Metabolic Disease, 45:804-818, Apr 2022. URL: https://doi.org/10.1002/jimd.12502, doi:10.1002/jimd.12502. This article has 18 citations and is from a peer-reviewed journal.

3. (stinton2021newbornscreeningfor pages 5-6): Chris Stinton, Hannah Fraser, Julia Geppert, Rebecca Johnson, Martin Connock, Samantha Johnson, Aileen Clarke, and Sian Taylor-Phillips. Newborn screening for long-chain 3-hydroxyacyl-coa dehydrogenase and mitochondrial trifunctional protein deficiencies using acylcarnitines measurement in dried blood spots—a systematic review of test accuracy. Frontiers in Pediatrics, Mar 2021. URL: https://doi.org/10.3389/fped.2021.606194, doi:10.3389/fped.2021.606194. This article has 15 citations.

4. (porta2024triheptanoininpatients pages 4-6): Francesco Porta, Arianna Maiorana, Vincenza Gragnaniello, Elena Procopio, Serena Gasperini, Roberta Taurisano, Marco Spada, Carlo Dionisi-Vici, and Alberto Burlina. Triheptanoin in patients with long-chain fatty acid oxidation disorders: clinical experience in italy. Italian Journal of Pediatrics, Oct 2024. URL: https://doi.org/10.1186/s13052-024-01782-y, doi:10.1186/s13052-024-01782-y. This article has 11 citations and is from a peer-reviewed journal.

5. (devine2024ipscderivedlchaddretinal pages 1-2): Tiffany DeVine, Gabriela Elizondo, Garen Gaston, Shannon J. Babcock, Dietrich Matern, Mikhail S. Shchepinov, Mark E. Pennesi, Cary O. Harding, and Melanie B. Gillingham. Ipsc-derived lchadd retinal pigment epithelial cells are susceptible to lipid peroxidation and rescued by transfection of a wildtype aav-<i>hadha</i> vector. Investigative Ophthalmology &amp; Visual Science, 65:22, Sep 2024. URL: https://doi.org/10.1167/iovs.65.11.22, doi:10.1167/iovs.65.11.22. This article has 3 citations and is from a domain leading peer-reviewed journal.

6. (fletcher2012observationsregardingretinopathy pages 1-2): Autumn L. Fletcher, Mark E. Pennesi, Cary O. Harding, Richard G. Weleber, and Melanie B. Gillingham. Observations regarding retinopathy in mitochondrial trifunctional protein deficiencies. Molecular genetics and metabolism, 106 1:18-24, May 2012. URL: https://doi.org/10.1016/j.ymgme.2012.02.015, doi:10.1016/j.ymgme.2012.02.015. This article has 90 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: mitochondrial trifunctional protein deficiency): Open Targets Query (mitochondrial trifunctional protein deficiency, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (gaston2023ag1528chadha pages 1-2): Garen Gaston, Shannon Babcock, Renee Ryals, Gabriela Elizondo, Tiffany DeVine, Dahlia Wafai, William Packwood, Sarah Holden, Jacob Raber, Jonathan R. Lindner, Mark E. Pennesi, Cary O. Harding, and Melanie B. Gillingham. A g1528c hadha knock-in mouse model recapitulates aspects of human clinical phenotypes for long-chain 3-hydroxyacyl-coa dehydrogenase deficiency. Communications Biology, Aug 2023. URL: https://doi.org/10.1038/s42003-023-05268-1, doi:10.1038/s42003-023-05268-1. This article has 15 citations and is from a peer-reviewed journal.

9. (schwantje2022geneticbiochemicaland pages 1-2): Marit Schwantje, Sabine A. Fuchs, Lonneke de Boer, Annet M. Bosch, Inge Cuppen, Eugenie Dekkers, Terry G. J. Derks, Sacha Ferdinandusse, Lodewijk Ijlst, Riekelt H. Houtkooper, Rose Maase, W. Ludo van der Pol, Maaike C. de Vries, Rendelien K. Verschoof‐Puite, Ronald J. A. Wanders, Monique Williams, Frits Wijburg, and Gepke Visser. Genetic, biochemical, and clinical spectrum of patients with mitochondrial trifunctional protein deficiency identified after the introduction of newborn screening in the netherlands. Journal of Inherited Metabolic Disease, 45:804-818, Apr 2022. URL: https://doi.org/10.1002/jimd.12502, doi:10.1002/jimd.12502. This article has 18 citations and is from a peer-reviewed journal.

10. (grunert2021thespectrumof pages 1-2): Sarah C. Grünert, Matthias Eckenweiler, Dorothea Haas, Martin Lindner, Konstantinos Tsiakas, René Santer, Sara Tucci, and Ute Spiekerkoetter. The spectrum of peripheral neuropathy in disorders of the mitochondrial trifunctional protein. Journal of Inherited Metabolic Disease, 44:893-902, Mar 2021. URL: https://doi.org/10.1002/jimd.12372, doi:10.1002/jimd.12372. This article has 32 citations and is from a peer-reviewed journal.

11. (baydakova2023newacylcarnitineratio pages 1-2): Galina V. Baydakova, Polina G. Tsygankova, Natalia L. Pechatnikova, Olga A. Bazhanova, Yana D. Nazarenko, and Ekaterina Y. Zakharova. New acylcarnitine ratio as a reliable indicator of long-chain 3-hydroxyacyl-coa dehydrogenase deficiency. International Journal of Neonatal Screening, 9:48, Aug 2023. URL: https://doi.org/10.3390/ijns9030048, doi:10.3390/ijns9030048. This article has 7 citations.

12. (kim2021triheptanoininthe pages 1-2): Esther S. Kim and Susan J. Keam. Triheptanoin in the management of long-chain fatty acid oxidation disorders: a profile of its use. Drugs & Therapy Perspectives, 37:187-193, Mar 2021. URL: https://doi.org/10.1007/s40267-021-00816-3, doi:10.1007/s40267-021-00816-3. This article has 7 citations and is from a peer-reviewed journal.

13. (kim2021triheptanoininthe pages 4-5): Esther S. Kim and Susan J. Keam. Triheptanoin in the management of long-chain fatty acid oxidation disorders: a profile of its use. Drugs & Therapy Perspectives, 37:187-193, Mar 2021. URL: https://doi.org/10.1007/s40267-021-00816-3, doi:10.1007/s40267-021-00816-3. This article has 7 citations and is from a peer-reviewed journal.

14. (neto2024mitochondrialbioenergeticsand media cb4f3939): Eduardo Vieira Neto, Meicheng Wang, Austin J. Szuminsky, Lethicia Ferraro, Erik Koppes, Yudong Wang, Clinton Van’t Land, Al-Walid Mohsen, Geancarlo Zanatta, Areeg H. El-Gharbawy, Tamil S. Anthonymuthu, Yulia Y. Tyurina, Vladimir A. Tyurin, Valerian Kagan, Hülya Bayır, and Jerry Vockley. Mitochondrial bioenergetics and cardiolipin remodeling abnormalities in mitochondrial trifunctional protein deficiency. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.176887, doi:10.1172/jci.insight.176887. This article has 16 citations and is from a domain leading peer-reviewed journal.

15. (neto2024mitochondrialbioenergeticsand media e05c4916): Eduardo Vieira Neto, Meicheng Wang, Austin J. Szuminsky, Lethicia Ferraro, Erik Koppes, Yudong Wang, Clinton Van’t Land, Al-Walid Mohsen, Geancarlo Zanatta, Areeg H. El-Gharbawy, Tamil S. Anthonymuthu, Yulia Y. Tyurina, Vladimir A. Tyurin, Valerian Kagan, Hülya Bayır, and Jerry Vockley. Mitochondrial bioenergetics and cardiolipin remodeling abnormalities in mitochondrial trifunctional protein deficiency. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.176887, doi:10.1172/jci.insight.176887. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (lotzhavla2018fatalpitfallsin pages 1-2): Amelie S. Lotz-Havla, Wulf Röschinger, Katharina Schiergens, Katharina Singer, Daniela Karall, Vassiliki Konstantopoulou, Saskia B. Wortmann, and Esther M. Maier. Fatal pitfalls in newborn screening for mitochondrial trifunctional protein (mtp)/long-chain 3-hydroxyacyl-coa dehydrogenase (lchad) deficiency. Orphanet Journal of Rare Diseases, Jul 2018. URL: https://doi.org/10.1186/s13023-018-0875-6, doi:10.1186/s13023-018-0875-6. This article has 31 citations and is from a peer-reviewed journal.

17. (stinton2021newbornscreeningfor pages 1-2): Chris Stinton, Hannah Fraser, Julia Geppert, Rebecca Johnson, Martin Connock, Samantha Johnson, Aileen Clarke, and Sian Taylor-Phillips. Newborn screening for long-chain 3-hydroxyacyl-coa dehydrogenase and mitochondrial trifunctional protein deficiencies using acylcarnitines measurement in dried blood spots—a systematic review of test accuracy. Frontiers in Pediatrics, Mar 2021. URL: https://doi.org/10.3389/fped.2021.606194, doi:10.3389/fped.2021.606194. This article has 15 citations.

18. (NCT01379625 chunk 1): Melanie B Gillingham. Study of Triheptanoin for Treatment of Long-Chain Fatty Acid Oxidation Disorder. Oregon Health and Science University. 2011. ClinicalTrials.gov Identifier: NCT01379625

19. (porta2024triheptanoininpatients pages 1-2): Francesco Porta, Arianna Maiorana, Vincenza Gragnaniello, Elena Procopio, Serena Gasperini, Roberta Taurisano, Marco Spada, Carlo Dionisi-Vici, and Alberto Burlina. Triheptanoin in patients with long-chain fatty acid oxidation disorders: clinical experience in italy. Italian Journal of Pediatrics, Oct 2024. URL: https://doi.org/10.1186/s13052-024-01782-y, doi:10.1186/s13052-024-01782-y. This article has 11 citations and is from a peer-reviewed journal.

20. (NCT01886378 chunk 1):  A Study of UX007 (Triheptanoin) in Participants With Long-Chain Fatty Acid Oxidation Disorders (LC-FAOD). Ultragenyx Pharmaceutical Inc. 2014. ClinicalTrials.gov Identifier: NCT01886378

21. (NCT05933200 chunk 1):  A Study to Determine the Effect of Triheptanoin Compared With Even-Chain MCT on MCEs in Pediatric Patients With LC-FAOD. Ultragenyx Pharmaceutical Inc. 2023. ClinicalTrials.gov Identifier: NCT05933200

22. (NCT02214160 chunk 1):  Long-Chain Fatty Acid Oxidation Disorders (LC-FAOD) Extension Study for Subjects Previously Enrolled in Triheptanoin Studies. Ultragenyx Pharmaceutical Inc. 2014. ClinicalTrials.gov Identifier: NCT02214160

23. (devine2024ipscderivedlchaddretinal pages 11-12): Tiffany DeVine, Gabriela Elizondo, Garen Gaston, Shannon J. Babcock, Dietrich Matern, Mikhail S. Shchepinov, Mark E. Pennesi, Cary O. Harding, and Melanie B. Gillingham. Ipsc-derived lchadd retinal pigment epithelial cells are susceptible to lipid peroxidation and rescued by transfection of a wildtype aav-<i>hadha</i> vector. Investigative Ophthalmology &amp; Visual Science, 65:22, Sep 2024. URL: https://doi.org/10.1167/iovs.65.11.22, doi:10.1167/iovs.65.11.22. This article has 3 citations and is from a domain leading peer-reviewed journal.

24. (kochan2025howgenesmeet pages 7-9): Zdzislaw Kochan and Joanna Karbowska. How genes meet diet in lchad deficiency: nutrigenomics of fatty acid oxidation disorder. International Journal of Molecular Sciences, 26:10140, Oct 2025. URL: https://doi.org/10.3390/ijms262010140, doi:10.3390/ijms262010140. This article has 2 citations.
