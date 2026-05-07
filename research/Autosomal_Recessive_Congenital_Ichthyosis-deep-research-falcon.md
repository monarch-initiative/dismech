---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T08:58:10.531656'
end_time: '2026-05-07T09:08:56.693208'
duration_seconds: 646.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Congenital Ichthyosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Congenital Ichthyosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Congenital Ichthyosis** covering all of the
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
- **Disease Name:** Autosomal Recessive Congenital Ichthyosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Congenital Ichthyosis** covering all of the
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


## Autosomal Recessive Congenital Ichthyosis (ARCI): Disease Characteristics Research Report

### Scope and evidence base
This report synthesizes evidence from recent primary cohort genetics (2023–2024), diagnostic practice research (2024), a treatment-focused review (2023), a gene/cell therapy review (2024), and clinical trial registry records (2016–2023 postings, with ongoing/updated trials) retrieved in this run. Evidence is largely **aggregated disease-level resources** (cohorts, reviews, guidelines, trial registries) rather than EHR-only single-patient data, except where explicitly noted. (diociaiuti2024crosssectionalstudyon pages 2-3, hotz2023mutationalspectrumof pages 1-2, penacorona2023advancesinthe pages 1-2, salo2024genetictestingand pages 1-2, NCT04047732 chunk 1)

---

## 1. Disease Information

### 1.1 What is the disease?
Autosomal recessive congenital ichthyosis (ARCI) is a **non-syndromic, congenital disorder of cornification** characterized by generalized scaling with variable erythema and barrier dysfunction, typically presenting at birth (often as a collodion baby) and persisting lifelong. (hotz2023mutationalspectrumof pages 1-2, penacorona2023advancesinthe pages 1-2)

Direct abstract quote (treatment review): “Autosomal recessive congenital ichthyoses (ARCI) are a skin pathology due to genetic causes characterized by a variable degree of desquamation, accompanied by erythema.” (Frontiers in Pharmacology; 2023-11-09) (penacorona2023advancesinthe pages 1-2)

### 1.2 Key identifiers
Evidence retrieved here did **not** include authoritative identifier pages (OMIM/Orphanet/MONDO/MeSH/ICD-10/ICD-11). Therefore, **OMIM/Orphanet/MONDO/ICD/MeSH identifiers cannot be reliably asserted from this tool run**.

### 1.3 Common synonyms / alternative names
ARCI is often used as an umbrella for major phenotypes/subtypes including:
- **Lamellar ichthyosis (LI)**
- **Congenital ichthyosiform erythroderma (CIE)**
- **Harlequin ichthyosis (HI)** (most severe)
- Minor/related clinical presentations: **self-healing collodion baby**, **bathing suit ichthyosis**, and related “collodion baby” neonatal presentations. (diociaiuti2024crosssectionalstudyon pages 2-3, hotz2023mutationalspectrumof pages 1-2, penacorona2023advancesinthe pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
ARCI is a **Mendelian (autosomal recessive) genetic disorder** caused by biallelic pathogenic variants in multiple genes involved in cornified envelope formation and epidermal lipid processing/transport, leading to skin barrier failure. (hotz2023mutationalspectrumof pages 1-2, penacorona2023advancesinthe pages 1-2)

In a 2024 Italian ARCI cohort study (n=74), the genetic distribution was: **TGM1 24.3%**, **ALOX12B 24.3%**, **CYP4F22 16.2%**, **ABCA12 12.2%**, **ALOXE3 9.5%**, **NIPAL4 9.5%**, and **CERS3/PNPLA1/SDR9C7 1.4% each**. (Diociaiuti et al., Dermatology; 2024-04; https://doi.org/10.1159/000536366) (diociaiuti2024crosssectionalstudyon pages 1-2)

### 2.2 Risk factors
- **Genetic risk**: family history consistent with autosomal recessive inheritance and biallelic pathogenic variants in ARCI genes (see Section 4). (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 1-2)
- **Consanguinity** can increase likelihood of autosomal recessive disease: in the 74-patient Italian series, **consanguinity was 13/73 families (17.8%)**. (diociaiuti2024crosssectionalstudyon pages 2-3)

Evidence retrieved here did not include robust environmental, toxin, or lifestyle risk factors for ARCI as a genetic disorder.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction studies were identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum and frequencies (recent cohort data)
In a 2024 cross-sectional Italian series (74 genetically confirmed ARCI patients):
- Subtype distribution: **LI 67.5% (50/74)**; **CIE 24.3% (18/74)**; **HI 2.7% (2/74)**; other minor ARCI subtypes 5.4% (4/74). (diociaiuti2024crosssectionalstudyon pages 1-2)
- Symptom/feature frequencies (reported across cohort):
  - **Pruritus:** 86.3% (63/73); mean itch VAS **5.7 ± 2.0**
  - **Pain:** 15.1% (11/73); pain VAS **5.2 ± 2.7**
  - **Palmoplantar keratoderma (PPK):** 97.3% (72/74)
  - **Fissures:** 28.4% (21/74)
  - **Ectropion:** 25.7% (19/74)
  - **Eclabium:** 14.9% (11/74)
These data support high burden of itch and frequent keratoderma with variable ocular/perioral involvement. (diociaiuti2024crosssectionalstudyon pages 2-3)

### 3.2 Severity measurement in current research/practice
The Italian cohort operationalized severity using a **SCORAD-based ichthyosis severity score** incorporating body surface involvement, 10 clinical features, and VAS itch and pain. (diociaiuti2024crosssectionalstudyon pages 2-3)

### 3.3 Genotype-associated phenotypes (selected)
- **TGM1 and ABCA12** variants were associated with **higher severity**, and with **alopecia/ectropion/eclabium**. (diociaiuti2024crosssectionalstudyon pages 1-2)
- **CYP4F22** group had the **lowest mean severity score** in that cohort. (diociaiuti2024crosssectionalstudyon pages 1-2)
- **NIPAL4**: association with **psoriasis-like lesions**, **reticulate trunk scale**, and **striated keratoderma**, emphasized as diagnostically relevant. (diociaiuti2024crosssectionalstudyon pages 1-2)

### 3.4 Quality of life impact
ARCI is described as having symptoms that “drastically affect patients’ quality of life” in a 2023 treatment review. (penacorona2023advancesinthe pages 1-2)
A diagnostic-practice study also states that ichthyosis has a negative effect on QoL, citing prior literature. (salo2024genetictestingand pages 1-2)

### 3.5 Suggested HPO terms (examples; not exhaustive)
- Ichthyosis/scaling: **HP:0008064 (Ichthyosis)**, **HP:0000969 (Generalized dry skin)**
- Erythroderma: **HP:0001043 (Erythroderma)**
- Collodion baby: **HP:0001012 (Collodion membrane)**
- Pruritus: **HP:0000989 (Pruritus)**
- Palmoplantar keratoderma: **HP:0000982 (Palmoplantar keratoderma)**
- Ectropion/eclabium: **HP:0000656 (Ectropion)**, **HP:0000233 (Eclabium)**
- Alopecia: **HP:0001596 (Alopecia)**

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and gene functions (current understanding)
ARCI is genetically heterogeneous; recent sources list core causal genes including **ABCA12, ALOX12B, ALOXE3, CERS3, CYP4F22, NIPAL4, PNPLA1, SDR9C7, SULT2B1, TGM1**. (hotz2023mutationalspectrumof pages 1-2)

A large 2023 ABCA12 cohort paper states: “ARCI is caused by biallelic mutations in ABCA12, ALOX12B, ALOXE3, CERS3, CYP4F22, NIPAL4, PNPLA1, SDR9C7, SULT2B1, and TGM1.” (Genes; 2023-03; https://doi.org/10.3390/genes14030717) (hotz2023mutationalspectrumof pages 1-2)

#### Gene–phenotype synthesis table
| Gene | Protein/function (1 phrase) | ARCI subtype associations | Key genotype–phenotype notes/statistics | Key source (include DOI and year) |
|---|---|---|---|---|
| **TGM1** | Transglutaminase-1; cornified envelope cross-linking | LI, CIE, bathing suit ichthyosis; severe ARCI | In the 74-patient Italian ARCI cohort, **18/74 (24.3%)** had **TGM1** variants; mean severity was among the **highest** across genes. **Alopecia, ectropion, and eclabium** were significantly associated with **TGM1**; **large, thick, brownish scales** were particularly linked to this genotype. On ultrastructure, **cholesterol clefts were 100% specific** for TGM1-mutated cases. TGM1 is also described as the **most common cause** of ARCI in review literature (diociaiuti2024crosssectionalstudyon pages 1-2, penacorona2023advancesinthe pages 1-2). | Diociaiuti 2024, DOI: **10.1159/000536366**; Peña-Corona 2023, DOI: **10.3389/fphar.2023.1274248** (diociaiuti2024crosssectionalstudyon pages 1-2, penacorona2023advancesinthe pages 1-2) |
| **ALOX12B** | 12R-lipoxygenase; epidermal lipid processing | LI, CIE, collodion baby/self-improving phenotypes | In the Italian cohort, **18/74 (24.3%)** had **ALOX12B** variants, tying TGM1 as the most frequent gene. Severity was lower than TGM1/ABCA12 overall. Reviews identify ALOX12B as a major ARCI gene involved in barrier lipid metabolism; phenotypes can range from collodion baby to later generalized ichthyosis (diociaiuti2024crosssectionalstudyon pages 1-2, penacorona2023advancesinthe pages 1-2). | Diociaiuti 2024, DOI: **10.1159/000536366**; Peña-Corona 2023, DOI: **10.3389/fphar.2023.1274248** (diociaiuti2024crosssectionalstudyon pages 1-2, penacorona2023advancesinthe pages 1-2) |
| **CYP4F22** | Cytochrome P450 ω-hydroxylase; acylceramide synthesis | LI/CIE spectrum, often milder ARCI | In the Italian cohort, **12/74 (16.2%)** had **CYP4F22** variants. This group had the **lowest mean ichthyosis severity score** among the common ARCI genes in that study. Founder effects are reported for some variants in prior population studies, supporting population-specific enrichment (diociaiuti2024crosssectionalstudyon pages 1-2). | Diociaiuti 2024, DOI: **10.1159/000536366** (diociaiuti2024crosssectionalstudyon pages 1-2) |
| **ABCA12** | Lipid transporter for lamellar granule cargo/glucosylceramides | **HI**, also LI and CIE | In the Italian cohort, **9/74 (12.2%)** had **ABCA12** variants; severity was among the **highest** and **alopecia, ectropion, eclabium** were significantly associated. In the dedicated **64-patient ABCA12** cohort, **34 novel variants** expanded the known spectrum to **217 mutations**; putative hotspots included **c.4541G>A p.(Arg1514His)** and **c.4139A>G p.(Asn1380Ser)**. Strong correlation: **biallelic loss-of-function usually causes HI**, whereas **biallelic missense variants mainly cause CIE or LI** (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 1-2). | Hotz 2023, DOI: **10.3390/genes14030717**; Diociaiuti 2024, DOI: **10.1159/000536366** (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 1-2) |
| **ALOXE3** | Epidermal lipoxygenase eLOX3; lipid barrier metabolism | LI/CIE spectrum | In the Italian cohort, **7/74 (9.5%)** had **ALOXE3** variants. Included among core ARCI genes in multiple recent reviews and diagnostic papers; phenotype overlaps with other lipid-metabolism ARCI genes, supporting need for molecular confirmation (diociaiuti2024crosssectionalstudyon pages 1-2, fioretti2024comprehensivemolecularanalysis pages 16-17). | Diociaiuti 2024, DOI: **10.1159/000536366**; Fioretti 2024, DOI: **10.3390/biomedicines12051112** (diociaiuti2024crosssectionalstudyon pages 1-2, fioretti2024comprehensivemolecularanalysis pages 16-17) |
| **NIPAL4** | Ichthyin; epidermal lipid homeostasis/acylceramide pathway | LI/CIE spectrum, distinctive patterned/psoriasiform ARCI | In the Italian cohort, **7/74 (9.5%)** had **NIPAL4** variants. Distinctive associations included **psoriasis-like lesions**, **reticulate trunk scale pattern**, and **striated keratoderma**; these were highlighted as a **novel phenotypic feature** with possible diagnostic/therapeutic implications. Prior referenced literature also links NIPAL4 to reduced stratum corneum acylceramides (diociaiuti2024crosssectionalstudyon pages 1-2, diociaiuti2024crosssectionalstudyon pages 17-17). | Diociaiuti 2024, DOI: **10.1159/000536366** (diociaiuti2024crosssectionalstudyon pages 1-2, diociaiuti2024crosssectionalstudyon pages 17-17) |
| **CERS3** | Ceramide synthase 3; very-long-chain ceramide synthesis | Rare ARCI, LI/CIE-like phenotypes | Rare in the Italian cohort (**1/74; 1.4%**). Ultrastructural review showed **abnormal lamellar bodies** in the **CERS3** case, consistent with a barrier-lipid trafficking/synthesis defect (diociaiuti2024crosssectionalstudyon pages 1-2). | Diociaiuti 2024, DOI: **10.1159/000536366** (diociaiuti2024crosssectionalstudyon pages 1-2) |
| **PNPLA1** | Patatin-like phospholipase; acylceramide biosynthesis | Rare ARCI, typically LI/CIE-like | Rare in the Italian cohort (**1/74; 1.4%**). Included among established ARCI genes in recent reviews and sequencing studies; contributes to defective epidermal lipid barrier formation (diociaiuti2024crosssectionalstudyon pages 1-2, hotz2023mutationalspectrumof pages 1-2). | Diociaiuti 2024, DOI: **10.1159/000536366**; Hotz 2023, DOI: **10.3390/genes14030717** (diociaiuti2024crosssectionalstudyon pages 1-2, hotz2023mutationalspectrumof pages 1-2) |
| **SDR9C7** | Short-chain dehydrogenase/reductase; epidermal retinoid/vitamin A-related metabolism | Rare ARCI, LI/CIE-like | Rare in the Italian cohort (**1/74; 1.4%**). Ultrastructural analysis showed **abnormal lamellar bodies** in the **SDR9C7** patient; referenced literature links SDR9C7 to impaired epidermal barrier function and vitamin A metabolism (diociaiuti2024crosssectionalstudyon pages 1-2, diociaiuti2024crosssectionalstudyon pages 17-17). | Diociaiuti 2024, DOI: **10.1159/000536366** (diociaiuti2024crosssectionalstudyon pages 1-2, diociaiuti2024crosssectionalstudyon pages 17-17) |
| **SULT2B1** | Cholesterol sulfotransferase; epidermal sterol metabolism | Rare ARCI / nonsyndromic ichthyosis | Not represented among the 74 Italian patients, but listed as an established ARCI gene in recent ABCA12-focused and multi-gene diagnostic papers. Multi-gene NGS studies support inclusion of **SULT2B1** on ichthyosis panels because phenotype overlaps with other ARCI forms (hotz2023mutationalspectrumof pages 1-2, fioretti2024comprehensivemolecularanalysis pages 16-17). | Hotz 2023, DOI: **10.3390/genes14030717**; Fioretti 2024, DOI: **10.3390/biomedicines12051112** (hotz2023mutationalspectrumof pages 1-2, fioretti2024comprehensivemolecularanalysis pages 16-17) |


*Table: This table summarizes major ARCI genes, their biological roles, subtype associations, and the most informative genotype–phenotype findings from the provided evidence. It emphasizes cohort-based frequencies from Diociaiuti 2024 and the ABCA12-specific correlations from Hotz 2023 for diagnostic and knowledge-base use.*

### 4.2 Pathogenic variants and variant classes
- **ABCA12** (2023 cohort, n=64): identified **34 novel ABCA12 mutations**, expanding the reported spectrum to **217 mutations** and noting possible hotspots **c.4541G>A p.(Arg1514His)** and **c.4139A>G p.(Asn1380Ser)**. (hotz2023mutationalspectrumof pages 1-2)
- **Genotype–phenotype rule (ABCA12)**: “Loss-of-function mutations on both alleles generally result in harlequin ichthyosis, whereas biallelic missense mutations mainly lead to CIE or LI.” (hotz2023mutationalspectrumof pages 1-2)
- **ARCI cohort (Italy, 2024)**: identified **25 previously undescribed mutations**, plus structural events (microduplications in **TGM1**, microdeletions in **CYP4F22** and **NIPAL4**), illustrating that **CNVs** are relevant in ARCI diagnostics. (diociaiuti2024crosssectionalstudyon pages 1-2)

### 4.3 Modifier genes
No validated modifier genes were identified in the retrieved sources.

### 4.4 Epigenetic information
No ARCI-specific epigenetic mechanisms were identified in the retrieved sources.

### 4.5 Chromosomal abnormalities
Structural variants (CNVs) were reported in ARCI genes in the 2024 Italian cohort (microduplications/microdeletions), supporting CNV-aware diagnostic pipelines. (diociaiuti2024crosssectionalstudyon pages 1-2)

---

## 5. Environmental Information
No consistent non-genetic environmental causes were identified in the retrieved sources, consistent with ARCI being primarily monogenic. Supportive care often includes environmental management (e.g., avoiding overheating due to hypohidrosis/heat intolerance), but specific external causal exposures were not established in these sources. (diociaiuti2024crosssectionalstudyon pages 2-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (upstream→downstream causal chain)
**Upstream trigger:** biallelic pathogenic variants in genes mediating **cornified envelope formation** (e.g., **TGM1**) and/or **epidermal lipid transport/metabolism** (e.g., **ABCA12**, lipoxygenases, acylceramide pathway genes). (hotz2023mutationalspectrumof pages 1-2, penacorona2023advancesinthe pages 1-2)

**Intermediate biological effects:** defective cornification and impaired lipid processing/transport produce an abnormal stratum corneum architecture and permeability barrier; ultrastructural signatures can be gene-informative (e.g., “cholesterol clefts” in TGM1). (diociaiuti2024crosssectionalstudyon pages 1-2)

**Clinical manifestations:** generalized hyperkeratosis/scaling with variable erythema, fissuring, ectropion/eclabium, pruritus and pain; severe ABCA12 loss-of-function produces harlequin ichthyosis with life-threatening neonatal complications. (diociaiuti2024crosssectionalstudyon pages 2-3, hotz2023mutationalspectrumof pages 1-2)

### 6.2 Inflammatory/immune involvement (emerging theme)
A 2023 treatment review frames ARCI as having an “inflammatory process” and motivates repurposing biologics based on overlapping immune signatures with psoriasis/atopic dermatitis. (penacorona2023advancesinthe pages 1-2)
Clinical trial development targeting **IL-17** (secukinumab) and **IL-12/23** (ustekinumab) further reflects this mechanistic direction. (NCT03041038 chunk 1, penacorona2023advancesinthe pages 6-7)

### 6.3 Suggested ontology mappings
- **GO Biological Process** (examples): keratinization; epidermis development; lipid metabolic process; establishment of skin barrier.
- **Cell types (CL)**: **CL:0000312 keratinocyte**; (optionally) differentiated keratinocytes/corneocytes.
- **Anatomy (UBERON)**: **UBERON:0002097 skin of body**; **UBERON:0001003 epidermis**; stratum corneum.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary organ: **skin** (epidermis/stratum corneum). (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 1-2)
Secondary/complication-relevant systems include eyes (ectropion), mouth/lips (eclabium), thermoregulation (hypohidrosis/heat intolerance), and infection susceptibility due to barrier compromise. (diociaiuti2024crosssectionalstudyon pages 2-3)

### 7.2 Tissue/cell level
Key affected tissue: **keratinizing stratified squamous epithelium** of the epidermis; key cell type: **keratinocytes** undergoing abnormal terminal differentiation/cornification. (penacorona2023advancesinthe pages 1-2)

### 7.3 Subcellular/cellular components (suggested)
Cornified envelope structures and lipid-processing/transport organelles (e.g., lamellar body biology) are implicated; ultrastructural abnormalities were used diagnostically (including abnormal lamellar bodies in CERS3/SDR9C7 cases). (diociaiuti2024crosssectionalstudyon pages 1-2)

---

## 8. Temporal Development

### 8.1 Onset
ARCI is typically **congenital/early-onset**; the “collodion baby” presentation is frequently described across ARCI. (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 2-3)

### 8.2 Progression
The 2024 cohort includes ages from infancy to adulthood (0.1–48.8 years), supporting the view that ARCI is generally **chronic and lifelong**, with variable severity across genotypes. (diociaiuti2024crosssectionalstudyon pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal recessive inheritance is explicit in the disease definition. (hotz2023mutationalspectrumof pages 1-2)

### 9.2 Epidemiology (available estimates in retrieved sources)
A 2023 ARCI treatment review cites:
- **TGM1-related prevalence** “at 1:100,000 population” (citing Vahlquist et al., 2008), and
- a French epidemiologic study reporting **ARCI prevalence 7:1,000,000** (citing Dreyfus et al., 2014). (penacorona2023advancesinthe pages 1-2)

Because these are secondary citations within a review, they should be treated as contextual estimates rather than definitive contemporary global prevalence.

### 9.3 Population structure: consanguinity
The 2024 Italian cohort reported **17.8% consanguinity (13/73 families)**. (diociaiuti2024crosssectionalstudyon pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis and differential diagnosis
Diagnosis generally starts from clinical phenotype (LI/CIE/HI spectrum, collodion baby) and is increasingly confirmed by genetic testing. (diociaiuti2024crosssectionalstudyon pages 1-2, salo2024genetictestingand pages 1-2)

### 10.2 Histopathology/ultrastructure as diagnostic support
The 2024 Italian ARCI study incorporated **transmission electron microscopy** and reported gene-informative ultrastructural patterns (e.g., “cholesterol clefts” specific for TGM1). (diociaiuti2024crosssectionalstudyon pages 1-2)

### 10.3 Genetic testing: current real-world approach
A 2024 register-based Finnish study (2000–2020; n=88) describes how diagnostic practice evolved:
- “Diagnosis of ichthyosis was confirmed with genetic testing in **33** cases … and with conventional diagnostic methods … in **55** cases.” (Accepted 2024-08-06; https://doi.org/10.1002/mgg3.70000) (salo2024genetictestingand pages 1-2)
- “When genetic testing became available, it was offered primarily to patients with severe forms of ichthyosis. During the study period next-generation sequencing became the genetic testing method of choice…” (salo2024genetictestingand pages 1-2)

The 2024 Italian cohort used **targeted NGS panels** and escalation to clinical exome/other methods, plus **qPCR/array CGH** for CNV detection and Sanger validation. (diociaiuti2024crosssectionalstudyon pages 2-3)

### 10.4 Suggested testing algorithm (evidence-aligned)
1) Phenotype-driven evaluation (LI/CIE/HI; collodion baby) with assessment of extracutaneous features to exclude syndromic ichthyoses. (salo2024genetictestingand pages 1-2)
2) **NGS multigene panel** covering core ARCI genes; consider **CNV-aware methods** (microarray/MLPA/NGS CNV calling) given reported microdeletions/duplications. (diociaiuti2024crosssectionalstudyon pages 1-2, salo2024genetictestingand pages 1-2)
3) If negative/uncertain: clinical exome or genome sequencing; segregation analysis where needed. (diociaiuti2024crosssectionalstudyon pages 2-3, salo2024genetictestingand pages 1-2)

---

## 11. Outcome / Prognosis
The retrieved sources emphasize clinical heterogeneity and mention improved outcomes for severe forms with intensive neonatal care, but they do not provide cohort-level survival curves for ARCI/HI within 2023–2024 primary literature in this run. The Italian cohort supports long-term survivorship into adulthood across subtypes, while HI is highlighted as the most severe and high-burden neonatal condition. (hotz2023mutationalspectrumof pages 1-2, diociaiuti2024crosssectionalstudyon pages 1-2)

---

## 12. Treatment

### 12.1 Current standard management (symptom-directed)
A 2023 review states: “Topical treatments are a first-choice strategy due to their ease of application and cost; however, enteral administration of retinoids offers greater efficacy, although with certain limitations.” (Published 2023-11-09; https://doi.org/10.3389/fphar.2023.1274248) (penacorona2023advancesinthe pages 1-2)

### 12.2 Systemic retinoids and alternatives
The retrieved evidence establishes systemic retinoids as commonly used in severe inherited ichthyosis management (review-level statement), but does not provide ARCI-specific response rates in 2023–2024 primary trials in this run. (penacorona2023advancesinthe pages 1-2)

### 12.3 Recent developments and real-world implementations (prioritizing 2023–2024)

#### (A) Topical isotretinoin (TMB-001) — late-phase repurposing in congenital ichthyosis
Trial: **NCT04154293** (Timber Pharmaceuticals; Phase 2; completed). (NCT04154293 chunk 1)
- Population: age **≥9 years**, genetically confirmed congenital ichthyosis including ARCI-LI and RXLI; **10–90% BSA** involvement. (NCT04154293 chunk 1)
- Design: randomized, double-blind, vehicle-controlled; **34 participants**; 1:1:1 to **0.05% BID**, **0.1% BID**, or vehicle for **12 weeks**. (Study start 2019-12-03; completion 2021-08-30) (NCT04154293 chunk 1)
- Primary endpoint: **VIIS-50** responder at Week 12 (≥50% reduction in VIIS scaling). (NCT04154293 chunk 1)
- Patient-centered secondary endpoints included itch scale change and DLQI. (NCT04154293 chunk 1)
URL: https://clinicaltrials.gov/study/NCT04154293 (registry-derived). (NCT04154293 chunk 1)

#### (B) Topical gene replacement for TGM1-deficient ARCI — KB105 (HSV-1 vector)
Gene/cell therapy review (2024) states: “Gene therapy for the most common type of ichthyosis, lamellar ichthyosis caused by biallelic pathogenic variants in TGM1, is currently being developed using an engineered herpes simplex virus type 1 vector.” (Published online 2024-08-07; https://doi.org/10.1007/s13555-024-01239-4) (koutsoukos2024highlightsofgene pages 1-3)

ClinicalTrials.gov trials:
- **NCT04047732** (KB105; Phase 1/2; single-group, intra-patient comparison; up to **6 adults**; started **2019-08-27**; primary completion estimated Oct 2022; completion estimated Mar 2025). Endpoints include safety (TEAEs) and improvement by Investigator’s Global Assessment (IGA), VIIS-L changes, and immunofluorescence measurement of TGM1 in treated skin. (NCT04047732 chunk 1)
- **NCT05735158** (KB105-02; Phase 2; randomized, placebo-controlled, double-blind intra-subject design; estimated **15**; weekly dosing; primary endpoint Composite IGA responder at Week 9; includes systemic retinoid stability/washout rules). (Posted as 2023 trial record; sponsor Krystal Biotech) (NCT05735158 chunk 1)
URLs: https://clinicaltrials.gov/study/NCT04047732 and https://clinicaltrials.gov/study/NCT05735158 (registry-derived). (NCT04047732 chunk 1, NCT05735158 chunk 1)

#### (C) Anti–IL-17A biologic therapy (secukinumab) — mechanism-based repositioning
Trial: **NCT03041038** (Northwestern University; Phase 2; completed; results posted 2021). (NCT03041038 chunk 1)
- Enrollment: **20 adults**.
- Dosing: secukinumab **300 mg SC weekly ×5 then monthly** vs placebo with crossover/open-label phases. (NCT03041038 chunk 1)
- Primary efficacy endpoint: Week 16 reduction in **Ichthyosis Area Severity Index (IASI)**.
- Primary safety endpoint: bacterial/fungal mucocutaneous infections through Week 16. (NCT03041038 chunk 1)
URL: https://clinicaltrials.gov/study/NCT03041038 (registry-derived). (NCT03041038 chunk 1)

#### (D) Anti–IL-12/23 (ustekinumab) — trial-scale testing in ichthyoses
A 2023 ARCI repositioning review notes a trial “with 13 participants receiving injections every 8 weeks for one year” aiming to reduce severity and assess infection safety endpoints (review-level summary). (penacorona2023advancesinthe pages 6-7)

### 12.4 MAXO (Medical Action Ontology) suggestions (examples)
- Topical emollient therapy; keratolytic therapy; systemic retinoid therapy; topical retinoid therapy; biologic anti–IL-17 therapy; biologic anti–IL-12/23 therapy; gene replacement therapy (topical viral vector).

---

## 13. Prevention
Primary prevention is genetic (not environmental): carrier testing, prenatal diagnosis, and reproductive counseling are standard concepts for autosomal recessive disorders, but explicit ARCI-specific prevention guideline statements were not retrieved in this run. Genetic counseling is emphasized as enabled by molecular diagnosis in diagnostic-practice literature. (salo2024genetictestingand pages 1-2)

---

## 14. Other Species / Natural Disease
The retrieved sources in this run do not provide primary evidence for naturally occurring ARCI-equivalent disease across species. (No species-specific evidence retrieved.)

---

## 15. Model Organisms
The retrieved sources in this run mention that gene and cell therapy development for ichthyosis is supported by preclinical work (review-level), but do not provide specific animal model identifiers or detailed phenotype recapitulation for ARCI subtypes in the captured excerpts. (koutsoukos2024highlightsofgene pages 1-3)

---

# Key 2023–2024 highlights (executive summary)
1) **Genotype–phenotype resolution is improving with large cohorts**: a 2024 single-center ARCI cohort (n=74) provides gene frequencies and statistically associated clinical features and ultrastructural signatures (including itch burden and high prevalence of PPK). (diociaiuti2024crosssectionalstudyon pages 2-3, diociaiuti2024crosssectionalstudyon pages 1-2)
2) **ABCA12 genotype–phenotype correlation is reinforced**: biallelic loss-of-function → HI; biallelic missense → LI/CIE; 34 novel variants in a 64-patient cohort (2023). (hotz2023mutationalspectrumof pages 1-2)
3) **Diagnostics are shifting to NGS as first-tier** with increasing use over time and improved classification/prognosis and counseling; conventional methods remain common where testing is unavailable (2024 register study). (salo2024genetictestingand pages 1-2)
4) **Therapeutic innovation is moving toward targeted biologics and gene therapy**: topical HSV-1–vector TGM1 gene therapy trials are ongoing/expanding; topical isotretinoin and IL-17 blockade have been tested in controlled trial frameworks. (koutsoukos2024highlightsofgene pages 1-3, NCT04047732 chunk 1, NCT05735158 chunk 1, NCT04154293 chunk 1, NCT03041038 chunk 1)

---

## URLs and publication dates for key cited sources
- Diociaiuti et al. “Cross-Sectional Study on Autosomal Recessive Congenital Ichthyoses…” **Apr 2024**. DOI/URL: https://doi.org/10.1159/000536366 (diociaiuti2024crosssectionalstudyon pages 1-2)
- Hotz et al. “Mutational Spectrum of the ABCA12 Gene…” **Mar 2023**. DOI/URL: https://doi.org/10.3390/genes14030717 (hotz2023mutationalspectrumof pages 1-2)
- Peña‑Corona et al. “Advances in the treatment of autosomal recessive congenital ichthyosis…” **Published 2023-11-09**. DOI/URL: https://doi.org/10.3389/fphar.2023.1274248 (penacorona2023advancesinthe pages 1-2)
- Salo et al. “Genetic testing and new variants in diagnosis of congenital ichthyoses” **Accepted 2024-08-06**. DOI/URL: https://doi.org/10.1002/mgg3.70000 (salo2024genetictestingand pages 1-2)
- Koutsoukos & Bilousova “Highlights of Gene and Cell Therapy…” **Published online 2024-08-07**. DOI/URL: https://doi.org/10.1007/s13555-024-01239-4 (koutsoukos2024highlightsofgene pages 1-3)
- ClinicalTrials.gov: NCT04154293 https://clinicaltrials.gov/study/NCT04154293 (NCT04154293 chunk 1)
- ClinicalTrials.gov: NCT04047732 https://clinicaltrials.gov/study/NCT04047732 (NCT04047732 chunk 1)
- ClinicalTrials.gov: NCT05735158 https://clinicaltrials.gov/study/NCT05735158 (NCT05735158 chunk 1)
- ClinicalTrials.gov: NCT03041038 https://clinicaltrials.gov/study/NCT03041038 (NCT03041038 chunk 1)



References

1. (diociaiuti2024crosssectionalstudyon pages 2-3): Andrea Diociaiuti, Marialuisa Corbeddu, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Tonia Samela, Simona Giancristoforo, Adriano Angioni, Giovanna Zambruno, Antonio Novelli, Rita Alaggio, Damiano Abeni, and May El Hachem. Cross-sectional study on autosomal recessive congenital ichthyoses: association of genotype with disease severity, phenotypic, and ultrastructural features in 74 italian patients. Dermatology (Basel, Switzerland), 240:397-413, Apr 2024. URL: https://doi.org/10.1159/000536366, doi:10.1159/000536366. This article has 10 citations.

2. (hotz2023mutationalspectrumof pages 1-2): Alrun Hotz, Julia Kopp, Emmanuelle Bourrat, Vinzenz Oji, Kira Süßmuth, Katalin Komlosi, Bakar Bouadjar, Iliana Tantcheva-Poór, Maritta Hellström Pigg, Regina Betz, Kathrin Giehl, Fiona Schedel, Lisa Weibel, Solveig Schulz, Dora Stölzl, Gianluca Tadini, Emine Demiral, Karin Berggard, Andreas Zimmer, Svenja Alter, and Judith Fischer. Mutational spectrum of the abca12 gene and genotype–phenotype correlation in a cohort of 64 patients with autosomal recessive congenital ichthyosis. Genes, 14:717, Mar 2023. URL: https://doi.org/10.3390/genes14030717, doi:10.3390/genes14030717. This article has 27 citations.

3. (penacorona2023advancesinthe pages 1-2): Sheila I. Peña-Corona, Stephany Celeste Gutiérrez-Ruiz, Ma de los Dolores Campos Echeverria, Hernán Cortés, Manuel González-Del Carmen, and Gerardo Leyva-Gómez. Advances in the treatment of autosomal recessive congenital ichthyosis, a look towards the repositioning of drugs. Frontiers in Pharmacology, Nov 2023. URL: https://doi.org/10.3389/fphar.2023.1274248, doi:10.3389/fphar.2023.1274248. This article has 9 citations.

4. (salo2024genetictestingand pages 1-2): Milja Salo, Teija Kimpimäki, Heini Huhtala, and Tanja Saarela. Genetic testing and new variants in diagnosis of congenital ichthyoses. Molecular Genetics & Genomic Medicine, Aug 2024. URL: https://doi.org/10.1002/mgg3.70000, doi:10.1002/mgg3.70000. This article has 1 citations and is from a peer-reviewed journal.

5. (NCT04047732 chunk 1):  Topical KB105 Gene Therapy for the Treatment of TGM1-deficient Autosomal Recessive Congenital Ichthyosis (ARCI). Krystal Biotech, Inc.. 2019. ClinicalTrials.gov Identifier: NCT04047732

6. (diociaiuti2024crosssectionalstudyon pages 1-2): Andrea Diociaiuti, Marialuisa Corbeddu, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Tonia Samela, Simona Giancristoforo, Adriano Angioni, Giovanna Zambruno, Antonio Novelli, Rita Alaggio, Damiano Abeni, and May El Hachem. Cross-sectional study on autosomal recessive congenital ichthyoses: association of genotype with disease severity, phenotypic, and ultrastructural features in 74 italian patients. Dermatology (Basel, Switzerland), 240:397-413, Apr 2024. URL: https://doi.org/10.1159/000536366, doi:10.1159/000536366. This article has 10 citations.

7. (fioretti2024comprehensivemolecularanalysis pages 16-17): Tiziana Fioretti, Fabrizio Martora, Ilaria De Maggio, Adelaide Ambrosio, Carmelo Piscopo, Sabrina Vallone, Felice Amato, Diego Passaro, Fabio Acquaviva, Francesca Gaudiello, Daniela Di Girolamo, Valeria Maiolo, Federica Zarrilli, Speranza Esposito, Giuseppina Vitiello, Luigi Auricchio, Elena Sammarco, Daniele De Brasi, Roberta Petillo, Antonella Gambale, Fabio Cattaneo, Rosario Ammendola, Paola Nappa, and Gabriella Esposito. Comprehensive molecular analysis of disease-related genes as first-tier test for early diagnosis, classification, and management of patients affected by nonsyndromic ichthyosis. Biomedicines, 12:1112, May 2024. URL: https://doi.org/10.3390/biomedicines12051112, doi:10.3390/biomedicines12051112. This article has 2 citations.

8. (diociaiuti2024crosssectionalstudyon pages 17-17): Andrea Diociaiuti, Marialuisa Corbeddu, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Tonia Samela, Simona Giancristoforo, Adriano Angioni, Giovanna Zambruno, Antonio Novelli, Rita Alaggio, Damiano Abeni, and May El Hachem. Cross-sectional study on autosomal recessive congenital ichthyoses: association of genotype with disease severity, phenotypic, and ultrastructural features in 74 italian patients. Dermatology (Basel, Switzerland), 240:397-413, Apr 2024. URL: https://doi.org/10.1159/000536366, doi:10.1159/000536366. This article has 10 citations.

9. (NCT03041038 chunk 1): Amy Paller. The Efficacy and Safety of Secukinumab in Patients With Ichthyoses. Northwestern University. 2016. ClinicalTrials.gov Identifier: NCT03041038

10. (penacorona2023advancesinthe pages 6-7): Sheila I. Peña-Corona, Stephany Celeste Gutiérrez-Ruiz, Ma de los Dolores Campos Echeverria, Hernán Cortés, Manuel González-Del Carmen, and Gerardo Leyva-Gómez. Advances in the treatment of autosomal recessive congenital ichthyosis, a look towards the repositioning of drugs. Frontiers in Pharmacology, Nov 2023. URL: https://doi.org/10.3389/fphar.2023.1274248, doi:10.3389/fphar.2023.1274248. This article has 9 citations.

11. (NCT04154293 chunk 1):  A Vehicle Controlled Study to Evaluate Safety and Efficacy of Topical TMB-001 for Treatment of Congenital Ichthyosis. Timber Pharmaceuticals Inc.. 2019. ClinicalTrials.gov Identifier: NCT04154293

12. (koutsoukos2024highlightsofgene pages 1-3): Stefanos A. Koutsoukos and Ganna Bilousova. Highlights of gene and cell therapy for epidermolysis bullosa and ichthyosis. Dermatology and Therapy, 14:2379-2392, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01239-4, doi:10.1007/s13555-024-01239-4. This article has 5 citations.

13. (NCT05735158 chunk 1):  Topical KB105 for the Treatment of TGM1-deficient Autosomal Recessive Congenital Ichthyosis (ARCI). Krystal Biotech, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05735158