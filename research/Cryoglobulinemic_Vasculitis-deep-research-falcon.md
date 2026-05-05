---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T07:43:45.840018'
end_time: '2026-05-05T08:13:30.074874'
duration_seconds: 1784.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cryoglobulinemic Vasculitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cryoglobulinemic Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cryoglobulinemic Vasculitis** covering all of the
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
- **Disease Name:** Cryoglobulinemic Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cryoglobulinemic Vasculitis** covering all of the
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


# Cryoglobulinemic Vasculitis (CryoVas): Comprehensive Disease Characteristics Report

## Executive summary
Cryoglobulinemic vasculitis (CryoVas; also written “cryoglobulinaemic vasculitis”) is a systemic small-vessel vasculitis driven by circulating cryoglobulins—immunoglobulins that precipitate below 37 °C and resolubilize on warming—and consequent vascular immune-complex deposition and complement activation/consumption in mixed forms. The clinical spectrum ranges from the classic Meltzer triad (purpura, arthralgia, weakness) to life-/organ-threatening renal and neurologic disease. HCV historically accounted for most mixed CryoVas, but the DAA era has shifted the etiologic landscape toward autoimmune disease and lymphoproliferative disorders in many settings. (dammacco2023thewidespectrum pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)

## 1. Disease Information
### 1.1 Definition and current understanding
* **Cryoglobulins** are “immunoglobulins that reversibly precipitate at temperatures below 37 °C” (definition used in modern reviews). (dammacco2023thewidespectrum pages 1-3)
* **Cryoglobulinemic vasculitis (CryoVas/CV)** refers to a **systemic vasculitic syndrome** associated with cryoglobulin-containing immune complexes (mixed types) or cryoprotein-mediated vascular occlusion/hyperviscosity (type I), with manifestations from palpable purpura to severe neuropathy and glomerulonephritis. (dammacco2023thewidespectrum pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3)

### 1.2 Common synonyms / alternative names
* Cryoglobulinemic vasculitis; **cryoglobulinaemic vasculitis** (British spelling). (vita2011preliminaryclassificationcriteria pages 1-1)
* **Mixed cryoglobulinemic syndrome (MCS)** / mixed cryoglobulinemia syndrome (used interchangeably in some clinical literature). (ferri2026cryoglobulinemiamonoclonaland pages 4-5)
* Cryoglobulinemic syndrome / mixed cryoglobulinemia (often used historically; nomenclature harmonization has been proposed to distinguish lab finding vs clinical syndrome). (ferri2026cryoglobulinemiamonoclonaland pages 4-5, ferri2008orphanetjournalof pages 2-4)

### 1.3 Key identifiers (ICD/MeSH/MONDO/Orphanet)
Within the retrieved full-text corpus, **formal ICD-10/ICD-11, MeSH, MONDO, and Orphanet ORPHA identifiers were not explicitly stated**. The report therefore cannot provide evidence-backed codes from the available documents. (Limitation of current evidence set.)

### 1.4 Evidence source type
This report is derived from **aggregated disease-level resources** (systematic/narrative reviews, consensus recommendations, and classification-criteria studies) and selected cohort studies, rather than EHR-derived individual case aggregation. (dammacco2023thewidespectrum pages 1-3, rajendran2023riskfactorsfor pages 1-2, vita2011preliminaryclassificationcriteria pages 5-6)

## 2. Etiology
### 2.1 Primary causal factors / associated diseases
Cryoglobulinemia/CryoVas is etiologically heterogeneous, with major associated categories:
1. **Infectious**: especially **hepatitis C virus (HCV)** historically; also **HBV** and other infections. (dammacco2023thewidespectrum pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5, mazzaro2023hepatitisbvirusinfection pages 1-2)
2. **Autoimmune disease**: e.g., **Sjögren’s syndrome**, **systemic lupus erythematosus (SLE)**. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5, roubertou2022cryoglobulinemiainsystemic pages 1-2)
3. **B-cell lymphoproliferative disorders**: dominant in **type I cryoglobulinemia** and important in mixed CryoVas (including risk of NHL). (ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5, dammacco2023thewidespectrum pages 1-3)

### 2.2 Classification (etiology-relevant)
Cryoglobulins are commonly classified by Brouet type:
* **Type I**: single **monoclonal Ig**, associated with B-cell lymphoproliferative disorders. (dammacco2023thewidespectrum pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3)
* **Type II** (mixed): monoclonal IgM with RF activity + polyclonal IgG. (dammacco2023thewidespectrum pages 1-3)
* **Type III** (mixed): polyclonal IgM/IgG. (dammacco2023thewidespectrum pages 1-3)

### 2.3 Risk factors (selected quantitative)
* In type I cryoglobulinemia, **>90%** have an underlying lymphoproliferative disorder; MGUS frequency **36%–86%**, overt hematologic malignancy **20%–64%**. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)
* In mixed CryoVas, HCV markers have historically been present in the majority of cases; one review notes anti-HCV positivity ranges widely across series. (cacoub2002cryoglobulinemiavasculitis. pages 2-3, dammacco2023thewidespectrum pages 1-3)

### 2.4 Protective factors
Evidence for explicit “protective factors” (genetic or environmental) was not identified in the retrieved corpus.

### 2.5 Gene–environment interactions
Mechanistic gene–environment interaction evidence (e.g., specific susceptibility loci interacting with infections) was not identified in the retrieved corpus.

## 3. Phenotypes
### 3.1 Core phenotype spectrum
* **Meltzer triad**: purpura, arthralgia, weakness. (dammacco2023thewidespectrum pages 1-3, covic2023therapeuticpotentialof pages 1-3)
* **Cutaneous**: palpable purpura; ulcers; digital ischemia; livedo; Raynaud phenomenon (not exhaustive). (covic2023therapeuticpotentialof pages 1-3, roubertou2022cryoglobulinemiainsystemic pages 1-2)
* **Neurologic**: peripheral neuropathy; potentially severe neuropathy; occasional CNS involvement. (covic2023therapeuticpotentialof pages 1-3, dammacco2023thewidespectrum pages 1-3, roubertou2022cryoglobulinemiainsystemic pages 1-2)
* **Renal**: membranoproliferative glomerulonephritis / cryoglobulinemic glomerulonephritis. (covic2023therapeuticpotentialof pages 1-3, dammacco2023thewidespectrum pages 1-3)

### 3.2 Frequency / severity (examples)
* In an SLE cohort screened for cryoglobulins, **15%** of cryoglobulin-positive patients developed CryoVas; severe manifestations were uncommon (GN **5%**, CNS involvement **19%**) with **no deaths** reported during follow-up. (roubertou2022cryoglobulinemiainsystemic pages 1-2)
* In non-infectious CryoVas, relapse rates reported as **~28%** in type I and **22%–60%** in mixed NICV, with time-to-relapse **1–80 months**. (rajendran2023riskfactorsfor pages 1-2)

### 3.3 Suggested HPO terms (examples; ontology suggestions)
(These are suggested mappings; the retrieved sources do not provide HPO IDs.)
* Palpable purpura; skin ulcer; arthralgia; fatigue/asthenia; peripheral neuropathy; glomerulonephritis; Raynaud phenomenon; digital ischemia.

## 4. Genetic/Molecular Information
### 4.1 Causal genes / pathogenic variants
CryoVas is **not primarily a monogenic disorder** in typical adult presentations; the retrieved evidence emphasizes **secondary causes** (infection, autoimmunity, lymphoproliferation). Specific causal germline variants were not identified in the retrieved corpus. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)

### 4.2 Molecular features highlighted in recent literature
* Mixed CryoVas pathogenesis includes **B-cell aberrant lymphoproliferation and autoantibody (RF) production**, leading to immune complex formation and deposition. (ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)

## 5. Environmental Information
### 5.1 Infectious agents
* **HCV** is the dominant historical driver of mixed cryoglobulinemia/CryoVas; cryoglobulins are detectable in ~25–30% of HCV-infected individuals in one major review. (dammacco2023thewidespectrum pages 1-3)
* **HBV** can cause CryoVas; European series estimate HBV-associated CryoVas prevalence among HBV patients **0.5%–5.5%** (reviewed literature). (mazzaro2023hepatitisbvirusinfection pages 1-2)

### 5.2 Lifestyle/occupational exposures
Specific environmental toxin/lifestyle causal associations were not identified in the retrieved corpus.

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (high-level)
1. **Trigger/driver**: chronic infection (esp. HCV historically), autoimmune disease, or monoclonal B-cell disorder. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)
2. **B-cell dysregulation** with RF activity and production of cryoprecipitable immunoglobulins (mixed types). (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)
3. **Immune complex formation and deposition in small vessels** → leukocytoclastic vasculitis and end-organ damage (skin, nerves, kidneys). (ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3)
4. **Complement consumption** (often low C4) and systemic inflammation. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)

Type I differs mechanistically, tending toward **mechanical vascular occlusion/hyperviscosity** rather than classic immune-complex vasculitis. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5)

### 6.2 Suggested GO/CL terms (examples; ontology suggestions)
* GO biological processes: immune complex clearance; complement activation; B cell activation; leukocyte migration; vasculitis/inflammatory response.
* CL cell types: B cell; plasma cell; neutrophil; monocyte/macrophage; endothelial cell.

## 7. Anatomical Structures Affected
### 7.1 Organ/tissue involvement
* **Skin** (purpura, ulcers, digital ischemia). (dammacco2023thewidespectrum pages 1-3, roubertou2022cryoglobulinemiainsystemic pages 1-2)
* **Peripheral nervous system** (peripheral neuropathy). (covic2023therapeuticpotentialof pages 1-3, dammacco2023thewidespectrum pages 1-3)
* **Kidney** (membranoproliferative glomerulonephritis). (covic2023therapeuticpotentialof pages 1-3, dammacco2023thewidespectrum pages 1-3)

### 7.2 Suggested UBERON terms (examples; ontology suggestions)
Skin; peripheral nerve; kidney glomerulus; small blood vessel.

## 8. Temporal Development
### 8.1 Onset/course
* Typical onset is **adult** (reviews cite age ranges such as 45–65 in NICV contexts). (rajendran2023riskfactorsfor pages 2-3)
* Course can be **relapsing**; relapse timing reported from **1 to 80 months** in NICV. (rajendran2023riskfactorsfor pages 1-2)

## 9. Inheritance and Population
### 9.1 Epidemiology
* Essential mixed cryoglobulinemia prevalence reported as **~1:100,000** and female:male ratio **~3:1** in an Orphanet-style review article. (ferri2008orphanetjournalof pages 1-2)
* In HCV infection, cryoglobulin positivity varies widely by cohort; a large HCV prospective cohort found mixed cryoglobulin in **40%**. (cacoub2002cryoglobulinemiavasculitis. pages 2-3)
* Severe symptomatic vasculitis is relatively uncommon among cryoglobulin-positive HCV patients; one review notes only **~2–3%** develop severe vasculitis. (cacoub2002cryoglobulinemiavasculitis. pages 2-3)

### 9.2 Geographic distribution
Higher frequency in Southern Europe versus Northern Europe/North America is reported in older epidemiologic summaries. (ferri2008orphanetjournalof pages 1-2)

## 10. Diagnostics
### 10.1 Classification criteria (De Vita et al.)
The De Vita 2011 classification framework requires (i) documented cryoglobulins and (ii) positivity in **at least 2 of 3 domains** (questionnaire, clinical, laboratory), with reported sensitivity **~88.5%** and specificity **~93.6%** in key comparisons. (vita2011preliminaryclassificationcriteria pages 5-6, vita2011preliminaryclassificationcriteria pages 1-1)

A cropped figure from the original paper is available and summarizes the domains and thresholds. (vita2011preliminaryclassificationcriteria media 2dc84f3a)

### 10.2 Laboratory testing: cryoglobulin pre-analytics (critical for avoiding false negatives)
Multiple laboratory best-practice sources emphasize that cryoglobulin testing is **highly sensitive to pre-analytical temperature control**:
* Maintain whole blood at **~37 °C** from collection through clotting and serum separation; use pre-warmed tubes and warm transport (e.g., thermos). (sargur2010cryoglobulinevaluationbest pages 4-5, motyckova2011laboratorytestingfor pages 1-2, bakker2003adequatesamplingin pages 1-2)
* Typical protocols include **clotting at 37 °C for ~1 hour**, separation (preferably warm centrifugation), then serum incubation at **4 °C** for **3–7 days** to allow precipitation (type II/III may take up to a week). (sargur2010cryoglobulinevaluationbest pages 4-5, motyckova2011laboratorytestingfor pages 2-3, patel2024evaluationofcryoprotein pages 5-6)
* Insufficient volume (e.g., <10 mL) and temperature drops can cause false negatives. (mariscalrodriguez2019laboratoryguidelinesfor pages 4-5)

### 10.3 Common supportive biomarkers/tests
* Low complement (esp. **low C4**) and **RF positivity** are common in mixed CryoVas and are part of classification laboratory domains. (vita2011preliminaryclassificationcriteria pages 3-4)
* Demonstration of cryoglobulin type (immunofixation) is essential to distinguish type I versus mixed and guide etiologic work-up. (dammacco2023thewidespectrum pages 1-3, motyckova2011laboratorytestingfor pages 2-3)

### 10.4 Differential diagnosis (high-level)
CryoVas is within immune-complex small-vessel vasculitis differential; formal differentials were not comprehensively extractable from the retrieved corpus.

## 11. Outcome / Prognosis
### 11.1 Survival/mortality
* A DAA-era narrative synthesis reports mortality about **~25% at 5 years** and **~40% at 10 years** for HCV-associated CryoVas; and 10-year survival differences by subtype (HCV-positive mixed 63%, HCV-negative mixed 65%, type I 87%)—these estimates should be interpreted cautiously as they are review-level summaries rather than a single prospective cohort. (balta2025impactofdirectacting pages 5-6)

### 11.2 Relapse and prognostic factors
* NICV relapse rates: **~28%** in type I and **22–60%** in mixed NICV (systematic review). (rajendran2023riskfactorsfor pages 1-2)
* Factors associated with relapse/death in NICV syntheses include **incomplete immunologic response** (e.g., failure to normalize C4 and reduce/disappear cryoglobulins), and severe organ involvement (e.g., renal insufficiency, pulmonary/GI involvement) and older age. (rajendran2023riskfactorsfor pages 1-2, rajendran2023riskfactorsfor pages 2-3)

## 12. Treatment
### 12.1 Current standard approaches (real-world implementation)
Treatment is commonly framed as a **three-pronged strategy**:
1. **Treat underlying cause** (e.g., antivirals for HCV; nucleos(t)ide analogues for HBV). (covic2023therapeuticpotentialof pages 1-3, mazzaro2023hepatitisbvirusinfection pages 1-2)
2. **B-cell–targeted therapy** (rituximab) for moderate–severe disease, persistent disease after viral clearance, contraindications to antivirals, or organ-/life-threatening manifestations. (dammacco2023thewidespectrum pages 1-3, covic2023therapeuticpotentialof pages 1-3)
3. **Plasma exchange/apheresis and intensive immunosuppression** (high-dose glucocorticoids ± cyclophosphamide) for emergencies such as hyperviscosity or severe organ-threatening disease. (covic2023therapeuticpotentialof pages 1-3, dammacco2023thewidespectrum pages 1-3)

### 12.2 Antiviral therapy in HCV-associated CryoVas
* Direct-acting antivirals (DAAs) are recommended broadly for HCV-positive CryoVas and achieve high SVR at population level; CryoVas manifestation resolution rates are variable across studies. (dammacco2023thewidespectrum pages 1-3, dammacco2023thewidespectrum pages 3-5)

### 12.3 Rituximab (anti-CD20)
* Evidence syntheses indicate rituximab can induce remission in many mixed CryoVas patients and is used especially for severe disease or DAA-nonresponders/persistent vasculitis. (dammacco2023thewidespectrum pages 1-3, ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3)
* In HCV-associated CryoVas, a systematic review reports trial-level results where rituximab achieved remission in **83.3%** at 6 months in one trial compared with **8.3%** control; and improved sustained response in combination with interferon-era antivirals. (covic2023therapeuticpotentialof pages 1-3)

### 12.4 Glucocorticoids and cyclophosphamide
* Glucocorticoids may mitigate vasculitis acutely but are not considered maintenance therapy in some expert syntheses; cyclophosphamide use has been largely replaced by rituximab but remains relevant in severe cases. (dammacco2023thewidespectrum pages 1-3)

### 12.5 Plasma exchange / apheresis
* Therapeutic apheresis is described as an **emergency treatment** in hyperviscosity syndrome. (dammacco2023thewidespectrum pages 1-3)

### 12.6 Emerging / experimental therapies
Evidence in the retrieved corpus highlights potential rescue options in rituximab-refractory nonviral CryoVas, including alkylators and biologics (e.g., rituximab + belimumab in small series). (ezconde2023nonviralcryoglobulinemicvasculitis pages 14-16)

### 12.7 Suggested MAXO terms (examples; ontology suggestions)
Antiviral therapy; B-cell depletion therapy (anti-CD20); therapeutic plasma exchange; glucocorticoid therapy; alkylating agent chemotherapy.

## 13. Prevention
Primary prevention is largely **indirect** via prevention/treatment of underlying causes (e.g., HCV treatment and HBV suppression). Explicit prevention trial evidence was not identified in the retrieved corpus.

## 14. Other Species / Natural Disease
No evidence for naturally occurring CryoVas analogs in non-human species was identified in the retrieved corpus.

## 15. Model Organisms
No specific model-organism systems were identified in the retrieved corpus.

---

## Visual evidence: De Vita classification criteria figure
The following figure excerpt summarizes the **three-domain De Vita classification criteria** and the requirement for repeated cryoglobulin positivity. (vita2011preliminaryclassificationcriteria media 2dc84f3a)

---

## Direct abstract quotes (selected)
* Dammacco et al. 2023 (Clin Exp Med; published Mar 2023; https://doi.org/10.1007/s10238-022-00808-1): “Immunoglobulins that reversibly precipitate at temperatures below 37 °C are called cryoglobulins (CGs). Cryoglobulinemia often manifests as cryoglobulinemic vasculitis (CV), whose symptoms range in severity from purpuric eruptions to life-threatening features.” (dammacco2023thewidespectrum pages 1-3)
* De Vita et al. 2011 (Ann Rheum Dis; published Jul 2011; https://doi.org/10.1136/ard.2011.150755): “Positivity of serum cryoglobulins was defined by experts as an essential condition for CV classification.” (vita2011preliminaryclassificationcriteria pages 1-1)

---

## Evidence gaps / limitations
1. **Ontology/identifier codes** (MONDO, ORPHA, ICD, MeSH) were not explicitly present in the retrieved full-text evidence; adding them would require direct database queries beyond the current paper corpus.
2. Many quantitative outcome estimates for the DAA era are available mainly as **review-level syntheses** rather than uniformly reported prospective cohorts; where such estimates are used, they are attributed as such.
3. Genetic susceptibility loci, protective factors, and model organism data were not found in the retrieved sources.


References

1. (dammacco2023thewidespectrum pages 1-3): Franco Dammacco, Gianfranco Lauletta, and Angelo Vacca. The wide spectrum of cryoglobulinemic vasculitis and an overview of therapeutic advancements. Clinical and Experimental Medicine, 23:255-272, Mar 2023. URL: https://doi.org/10.1007/s10238-022-00808-1, doi:10.1007/s10238-022-00808-1. This article has 50 citations and is from a peer-reviewed journal.

2. (ezconde2023nonviralcryoglobulinemicvasculitis pages 1-3): Andrea N úñ ez-Conde, Ignasi Rodr í guez-Pint ó, David A. Alba-Garibay, Alba Álvarez-Abella, Alba Jerez-Lienas, Oriol Llargu é s, M. Antonio, Alba-S á nchez, Diana Oleas, and Marco A Alba. Nonviral cryoglobulinemic vasculitis: an updated review for clinical practice. Vessel Plus, Oct 2023. URL: https://doi.org/10.20517/2574-1209.2023.105, doi:10.20517/2574-1209.2023.105. This article has 3 citations.

3. (ezconde2023nonviralcryoglobulinemicvasculitis pages 3-5): Andrea N úñ ez-Conde, Ignasi Rodr í guez-Pint ó, David A. Alba-Garibay, Alba Álvarez-Abella, Alba Jerez-Lienas, Oriol Llargu é s, M. Antonio, Alba-S á nchez, Diana Oleas, and Marco A Alba. Nonviral cryoglobulinemic vasculitis: an updated review for clinical practice. Vessel Plus, Oct 2023. URL: https://doi.org/10.20517/2574-1209.2023.105, doi:10.20517/2574-1209.2023.105. This article has 3 citations.

4. (vita2011preliminaryclassificationcriteria pages 1-1): S. Vita, F. Soldano, Miriam Isola, Giuseppe Monti, A. Gabrielli, A. Tzioufas, C. Ferri, G. Ferraccioli, L. Quartuccio, L. Corazza, G. D. Marchi, M. R. Casals, M. Voulgarelis, Marco Lenzi, Francesco Saccardo, P. Fraticelli, M. Mascia, D. Sansonno, P. Cacoub, M. Tomšič, A. Tavoni, M. Pietrogrande, A. Zignego, S. Scarpato, C. Mazzaro, Pietro Pioltelli, Serge Steinfeld, P. Lamprecht, S. Bombardieri, and M. Galli. Preliminary classification criteria for the cryoglobulinaemic vasculitis. Annals of the Rheumatic Diseases, 70:1183-1190, Jul 2011. URL: https://doi.org/10.1136/ard.2011.150755, doi:10.1136/ard.2011.150755. This article has 214 citations and is from a highest quality peer-reviewed journal.

5. (ferri2026cryoglobulinemiamonoclonaland pages 4-5): Clodoveo Ferri, Laura Gragnani, Anna Linda Zignego, and Dilia Giuggioli. Cryoglobulinemia, monoclonal and mixed cryoglobulinemia syndromes, cryoglobulinemic vasculitis: a proposal for comprehensive nomenclature and definition. Frontiers in Immunology, Feb 2026. URL: https://doi.org/10.3389/fimmu.2026.1754012, doi:10.3389/fimmu.2026.1754012. This article has 0 citations and is from a peer-reviewed journal.

6. (ferri2008orphanetjournalof pages 2-4): C Ferri. Orphanet journal of rare. Unknown journal, 2008.

7. (rajendran2023riskfactorsfor pages 1-2): Nithya Rajendran, Puteri Maisarah Rameli, and Hanaa Awad. Risk factors for relapse in non-infectious cryoglobulinemic vasculitis, including type i cryoglobulinemia: a systematic review. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1215345, doi:10.3389/fimmu.2023.1215345. This article has 4 citations and is from a peer-reviewed journal.

8. (vita2011preliminaryclassificationcriteria pages 5-6): S. Vita, F. Soldano, Miriam Isola, Giuseppe Monti, A. Gabrielli, A. Tzioufas, C. Ferri, G. Ferraccioli, L. Quartuccio, L. Corazza, G. D. Marchi, M. R. Casals, M. Voulgarelis, Marco Lenzi, Francesco Saccardo, P. Fraticelli, M. Mascia, D. Sansonno, P. Cacoub, M. Tomšič, A. Tavoni, M. Pietrogrande, A. Zignego, S. Scarpato, C. Mazzaro, Pietro Pioltelli, Serge Steinfeld, P. Lamprecht, S. Bombardieri, and M. Galli. Preliminary classification criteria for the cryoglobulinaemic vasculitis. Annals of the Rheumatic Diseases, 70:1183-1190, Jul 2011. URL: https://doi.org/10.1136/ard.2011.150755, doi:10.1136/ard.2011.150755. This article has 214 citations and is from a highest quality peer-reviewed journal.

9. (mazzaro2023hepatitisbvirusinfection pages 1-2): Cesare Mazzaro, Riccardo Bomben, Marcella Visentini, Laura Gragnani, Luca Quartuccio, Francesco Saccardo, Marco Sebastiani, Davide Filippini, Gianfranco Lauletta, Giuseppe Monti, and Valter Gattei. Hepatitis b virus-infection related cryoglobulinemic vasculitis. clinical manifestations and the effect of antiviral therapy: a review of the literature. Frontiers in Oncology, Feb 2023. URL: https://doi.org/10.3389/fonc.2023.1095780, doi:10.3389/fonc.2023.1095780. This article has 12 citations.

10. (roubertou2022cryoglobulinemiainsystemic pages 1-2): Yoann Roubertou, Sabine Mainbourg, Arnaud Hot, Denis Fouque, Cyrille Confavreux, Roland Chapurlat, Sébastien Debarbieux, Denis Jullien, Pascal Sève, Laurent Juillard, Marie-Nathalie Kolopp-Sarda, and Jean-Christophe Lega. Cryoglobulinemia in systemic lupus erythematosus: a retrospective study of 213 patients. Arthritis Research & Therapy, Jul 2022. URL: https://doi.org/10.1186/s13075-022-02857-z, doi:10.1186/s13075-022-02857-z. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (cacoub2002cryoglobulinemiavasculitis. pages 2-3): Patrice Cacoub, Nathalie Costedoat-Chalumeau, Olivier Lidove, and Laurent Alric. Cryoglobulinemia vasculitis. Current opinion in rheumatology, 14 1:29-35, Jan 2015. URL: https://doi.org/10.1097/00002281-200201000-00006, doi:10.1097/00002281-200201000-00006. This article has 354 citations and is from a peer-reviewed journal.

12. (covic2023therapeuticpotentialof pages 1-3): Andreea Covic, Irina Draga Caruntu, Alexandru Burlacu, Simona Eliza Giusca, Adrian Covic, Anca Elena Stefan, Crischentian Brinza, and Gener Ismail. Therapeutic potential of rituximab in managing hepatitis c-associated cryoglobulinemic vasculitis: a systematic review. Journal of Clinical Medicine, 12:6806, Oct 2023. URL: https://doi.org/10.3390/jcm12216806, doi:10.3390/jcm12216806. This article has 7 citations.

13. (rajendran2023riskfactorsfor pages 2-3): Nithya Rajendran, Puteri Maisarah Rameli, and Hanaa Awad. Risk factors for relapse in non-infectious cryoglobulinemic vasculitis, including type i cryoglobulinemia: a systematic review. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1215345, doi:10.3389/fimmu.2023.1215345. This article has 4 citations and is from a peer-reviewed journal.

14. (ferri2008orphanetjournalof pages 1-2): C Ferri. Orphanet journal of rare. Unknown journal, 2008.

15. (vita2011preliminaryclassificationcriteria media 2dc84f3a): S. Vita, F. Soldano, Miriam Isola, Giuseppe Monti, A. Gabrielli, A. Tzioufas, C. Ferri, G. Ferraccioli, L. Quartuccio, L. Corazza, G. D. Marchi, M. R. Casals, M. Voulgarelis, Marco Lenzi, Francesco Saccardo, P. Fraticelli, M. Mascia, D. Sansonno, P. Cacoub, M. Tomšič, A. Tavoni, M. Pietrogrande, A. Zignego, S. Scarpato, C. Mazzaro, Pietro Pioltelli, Serge Steinfeld, P. Lamprecht, S. Bombardieri, and M. Galli. Preliminary classification criteria for the cryoglobulinaemic vasculitis. Annals of the Rheumatic Diseases, 70:1183-1190, Jul 2011. URL: https://doi.org/10.1136/ard.2011.150755, doi:10.1136/ard.2011.150755. This article has 214 citations and is from a highest quality peer-reviewed journal.

16. (sargur2010cryoglobulinevaluationbest pages 4-5): Ravishankar Sargur, Peter White, and William Egner. Cryoglobulin evaluation: best practice? Annals of Clinical Biochemistry, 47:16-8, Jan 2010. URL: https://doi.org/10.1258/acb.2009.009180, doi:10.1258/acb.2009.009180. This article has 153 citations and is from a peer-reviewed journal.

17. (motyckova2011laboratorytestingfor pages 1-2): Gabriela Motyckova and Mandakolathur Murali. Laboratory testing for cryoglobulins. American Journal of Hematology, 86:500-502, Jun 2011. URL: https://doi.org/10.1002/ajh.22023, doi:10.1002/ajh.22023. This article has 136 citations and is from a domain leading peer-reviewed journal.

18. (bakker2003adequatesamplingin pages 1-2): Andries J. Bakker, Jennichjen Slomp, Taede de Vries, Dick A.G. Boymans, Bert Veldhuis, Kees Halma, and Peter Joosten. Adequate sampling in cryoglobulinaemia: recommended warmly. Clinical Chemistry and Laboratory Medicine, 41:85-89, Jan 2003. URL: https://doi.org/10.1515/cclm.2003.015, doi:10.1515/cclm.2003.015. This article has 29 citations and is from a peer-reviewed journal.

19. (motyckova2011laboratorytestingfor pages 2-3): Gabriela Motyckova and Mandakolathur Murali. Laboratory testing for cryoglobulins. American Journal of Hematology, 86:500-502, Jun 2011. URL: https://doi.org/10.1002/ajh.22023, doi:10.1002/ajh.22023. This article has 136 citations and is from a domain leading peer-reviewed journal.

20. (patel2024evaluationofcryoprotein pages 5-6): Dina Patel, Ravishankar Sargur, Joanna Sheldon, Rachel D Wheeler, and Carol Stanley. Evaluation of cryoprotein investigation using a digital external quality assurance scheme. Annals of Clinical Biochemistry: International Journal of Laboratory Medicine, 61:347-355, Mar 2024. URL: https://doi.org/10.1177/00045632241239805, doi:10.1177/00045632241239805. This article has 3 citations.

21. (mariscalrodriguez2019laboratoryguidelinesfor pages 4-5): A. Mariscal-Rodríguez, L.M. Villar Guimerans, M. López-Trascasa, M. Hernández González, and E. Moga Naranjo. Laboratory guidelines for the diagnosis of patients with cryoglobulinemic syndrome. Revista Clinica Espanola, 219:505-513, Dec 2019. URL: https://doi.org/10.1016/j.rceng.2019.01.003, doi:10.1016/j.rceng.2019.01.003. This article has 6 citations and is from a peer-reviewed journal.

22. (vita2011preliminaryclassificationcriteria pages 3-4): S. Vita, F. Soldano, Miriam Isola, Giuseppe Monti, A. Gabrielli, A. Tzioufas, C. Ferri, G. Ferraccioli, L. Quartuccio, L. Corazza, G. D. Marchi, M. R. Casals, M. Voulgarelis, Marco Lenzi, Francesco Saccardo, P. Fraticelli, M. Mascia, D. Sansonno, P. Cacoub, M. Tomšič, A. Tavoni, M. Pietrogrande, A. Zignego, S. Scarpato, C. Mazzaro, Pietro Pioltelli, Serge Steinfeld, P. Lamprecht, S. Bombardieri, and M. Galli. Preliminary classification criteria for the cryoglobulinaemic vasculitis. Annals of the Rheumatic Diseases, 70:1183-1190, Jul 2011. URL: https://doi.org/10.1136/ard.2011.150755, doi:10.1136/ard.2011.150755. This article has 214 citations and is from a highest quality peer-reviewed journal.

23. (balta2025impactofdirectacting pages 5-6): Alexia Anastasia Stefania Balta, Mariana Daniela Ignat, Raisa Eloise Barbu, Caterina Dumitru, Diana Sabina Radaschin, Valentin Bulza, Silvia Aura Mateescu Costin, Catalin Pleșea-Condratovici, and Liliana Baroiu. Impact of direct-acting antivirals on extrahepatic manifestations in chronic hepatitis c: a narrative review with a hermeneutic approach. Healthcare, 13:1953, Aug 2025. URL: https://doi.org/10.3390/healthcare13161953, doi:10.3390/healthcare13161953. This article has 4 citations.

24. (dammacco2023thewidespectrum pages 3-5): Franco Dammacco, Gianfranco Lauletta, and Angelo Vacca. The wide spectrum of cryoglobulinemic vasculitis and an overview of therapeutic advancements. Clinical and Experimental Medicine, 23:255-272, Mar 2023. URL: https://doi.org/10.1007/s10238-022-00808-1, doi:10.1007/s10238-022-00808-1. This article has 50 citations and is from a peer-reviewed journal.

25. (ezconde2023nonviralcryoglobulinemicvasculitis pages 14-16): Andrea N úñ ez-Conde, Ignasi Rodr í guez-Pint ó, David A. Alba-Garibay, Alba Álvarez-Abella, Alba Jerez-Lienas, Oriol Llargu é s, M. Antonio, Alba-S á nchez, Diana Oleas, and Marco A Alba. Nonviral cryoglobulinemic vasculitis: an updated review for clinical practice. Vessel Plus, Oct 2023. URL: https://doi.org/10.20517/2574-1209.2023.105, doi:10.20517/2574-1209.2023.105. This article has 3 citations.