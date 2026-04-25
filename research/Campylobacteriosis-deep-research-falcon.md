---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:40:19.188016'
end_time: '2026-04-04T12:50:13.850469'
duration_seconds: 594.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Campylobacteriosis
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Campylobacteriosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Campylobacteriosis** covering all of the
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
- **Disease Name:** Campylobacteriosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Campylobacteriosis** covering all of the
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


# Campylobacteriosis (Disease Characteristics Research Report)

## Target disease
- **Disease name:** Campylobacteriosis (Campylobacter infection; Campylobacter gastroenteritis)
- **Category:** Infectious (bacterial, zoonotic, foodborne)
- **MONDO ID:** Not retrieved in tool-accessible sources; not asserted here.

## High-yield 2023–2024 summary table
| Topic | Key quantitative/statements | Source (author/year/journal) | URL | Evidence context ID |
|---|---|---|---|---|
| Definition | Acute zoonotic bacterial infection of the gastrointestinal tract or blood caused by *Campylobacter* spp.; enteric infections are most commonly associated with *C. jejuni* (island2024guidelinesforthe pages 1-5) | PE Island 2024 / guidelines document | N/A | (island2024guidelinesforthe pages 1-5) |
| Main causative species | *C. jejuni* and *C. coli* cause the vast majority of human disease; one review states *C. jejuni* causes >80% and *C. coli* up to ~18.6% of human Campylobacter disease (khairullah2024campylobacteriosisarising pages 2-3) | Khairullah et al. 2024 / Open Veterinary Journal | https://doi.org/10.5455/ovj.2024.v14.i8.1 | (khairullah2024campylobacteriosisarising pages 2-3) |
| Common transmission sources | Major routes include contaminated poultry meat/products, untreated water, and contact with infected animals or contaminated environments; poultry is the primary reservoir/source (tikhomirova2024campylobacterjejunivirulence pages 1-2, khairullah2024campylobacteriosisarising pages 2-3) | Tikhomirova et al. 2024 / Journal of Biomedical Science; Khairullah et al. 2024 / Open Veterinary Journal | https://doi.org/10.1186/s12929-024-01033-6; https://doi.org/10.5455/ovj.2024.v14.i8.1 | (tikhomirova2024campylobacterjejunivirulence pages 1-2, khairullah2024campylobacteriosisarising pages 2-3) |
| Incubation and duration | Incubation typically 24–72 h (Finland review/study) and often 2–5 days in broader review literature; illness usually lasts about 1 week, sometimes up to 10 days (suominen2024campylobacteriosisinfinland pages 1-2, tikhomirova2024campylobacterjejunivirulence pages 1-2, myintzaw2023areviewon pages 4-6) | Suominen et al. 2024 / Microorganisms; Tikhomirova et al. 2024 / Journal of Biomedical Science; Myintzaw et al. 2023 / Food Reviews International | https://doi.org/10.3390/microorganisms12010132; https://doi.org/10.1186/s12929-024-01033-6; https://doi.org/10.1080/87559129.2021.1942487 | (suominen2024campylobacteriosisinfinland pages 1-2, tikhomirova2024campylobacterjejunivirulence pages 1-2, myintzaw2023areviewon pages 4-6) |
| Key symptoms | Diarrhea (sometimes bloody), abdominal pain/cramping, fever, nausea, vomiting, malaise; asymptomatic infection can occur (myintzaw2023areviewon pages 1-4, island2024guidelinesforthe pages 1-5) | Myintzaw et al. 2023 / Food Reviews International; PE Island 2024 / guidelines document | https://doi.org/10.1080/87559129.2021.1942487; N/A | (myintzaw2023areviewon pages 1-4, island2024guidelinesforthe pages 1-5) |
| Major sequelae | Major post-infectious sequelae include Guillain–Barré syndrome (GBS), reactive arthritis, Miller Fisher syndrome, and post-infectious IBS; one review notes GBS risk about 1/1,000 to 1/5,000 infections (myintzaw2023areviewon pages 1-4, olveraramirez2023asystematicreview pages 1-2, myintzaw2023areviewon pages 4-6) | Myintzaw et al. 2023 / Food Reviews International; Olvera-Ramírez et al. 2023 / Animals | https://doi.org/10.1080/87559129.2021.1942487; https://doi.org/10.3390/ani13081334 | (myintzaw2023areviewon pages 1-4, olveraramirez2023asystematicreview pages 1-2, myintzaw2023areviewon pages 4-6) |
| Finland epidemiology (2024) | In Finland pilot case-control/WGS study, 39% of cases were estimated domestic; WGS found 22 clusters among 185 domestic cases, none reported to the outbreak register; 41% of notifications lacked travel history (suominen2024campylobacteriosisinfinland pages 1-2) | Suominen et al. 2024 / Microorganisms | https://doi.org/10.3390/microorganisms12010132 | (suominen2024campylobacteriosisinfinland pages 1-2) |
| Burkina Faso epidemiology (2024) | Real-time PCR detected *Campylobacter* in 25.0% (324/1,295) of acute gastroenteritis samples; 95% of positives were in children <5 years (308/324) (badjo2024burdenandepidemiology pages 1-2) | Badjo et al. 2024 / BMC Infectious Diseases | https://doi.org/10.1186/s12879-024-09709-y | (badjo2024burdenandepidemiology pages 1-2) |
| Portugal epidemiology (2024 analysis of 2009–2021 surveillance) | 5,205 non-duplicated human isolates analyzed; ~50% of isolates were not notified in some years, indicating substantial under-reporting; 77.7% of cases were pediatric, with 1–4 years the highest annual age group; mean age 12.79 years (duarte2024epidemiologicaldataand pages 4-6, duarte2024epidemiologicaldataand pages 1-2) | Duarte et al. 2024 / Pathogens | https://doi.org/10.3390/pathogens13020147 | (duarte2024epidemiologicaldataand pages 4-6, duarte2024epidemiologicaldataand pages 1-2) |
| Diagnostics: CIDT/PCR shift | FoodNet reported continuing increases in infections diagnosed by CIDTs in 2023 and decreasing percentages yielding culture isolates; 29,607 infections, 7,234 hospitalizations, and 177 deaths were reported in 2023 across the expanded catchment (shah2024…commonlythrough pages 1-2) | Shah 2024 / FoodNet report | N/A | (shah2024…commonlythrough pages 1-2) |
| Diagnostics: direct stool WGS | In 37 Campylobacter-positive diarrheal stools, detection was 65% by direct metagenomic sequencing, 73% by culture, and 97% by qPCR; for assemblies >60% completeness, species ID was 100%, ST assignment 72%, and AMR determinant identification 95%; thresholds included >12,500 Campylobacter reads and >5× coverage (djeghout2024capturingclinicallyrelevant pages 7-9, djeghout2024capturingclinicallyrelevant pages 9-11, djeghout2024capturingclinicallyrelevant pages 1-2) | Djeghout et al. 2024 / Microbial Genomics | https://doi.org/10.1099/mgen.0.001284 | (djeghout2024capturingclinicallyrelevant pages 7-9, djeghout2024capturingclinicallyrelevant pages 9-11, djeghout2024capturingclinicallyrelevant pages 1-2) |
| Diagnostics: public-health WGS use | WGS improves outbreak detection and source attribution; Finland authors recommend sequencing all domestic isolates because unrecognized clusters were found despite no outbreak reports (suominen2024campylobacteriosisinfinland pages 1-2) | Suominen et al. 2024 / Microorganisms | https://doi.org/10.3390/microorganisms12010132 | (suominen2024campylobacteriosisinfinland pages 1-2) |
| Antimicrobial resistance: Italy 2020–2023 | Among 820 human isolates, 80.1% were resistant to ≥1 antibiotic; ciprofloxacin 72.1%, tetracycline 52.9%, erythromycin 3.2%, aminoglycosides 5.4%; MDR 5.7% (tramuta2024phenotypicantimicrobialresistance pages 2-4) | Tramuta et al. 2024 / Microorganisms | https://doi.org/10.3390/microorganisms12030426 | (tramuta2024phenotypicantimicrobialresistance pages 2-4) |
| Antimicrobial resistance: Portugal 2009–2021 | Among 2,174 isolates tested, ciprofloxacin resistance 94.2% overall (93.7% *C. jejuni*, 96.5% *C. coli*), tetracycline 81.6% overall, erythromycin 11.8% overall but 52.3% in *C. coli* vs 3.3% in *C. jejuni*; gentamicin resistance 0.5% (duarte2024epidemiologicaldataand pages 7-8) | Duarte et al. 2024 / Pathogens | https://doi.org/10.3390/pathogens13020147 | (duarte2024epidemiologicaldataand pages 7-8) |
| Antimicrobial resistance + WGS determinants: Spain 2020–2023 | In 114 human *C. jejuni* isolates, ciprofloxacin resistance 90.3%, tetracycline 66.7%, erythromycin 0.88%; key determinants: *gyrA* T86I 88.9%, CmeABC 92.1%, RE-CmeABC 7.9%, *bla*OXA-61 72.6%, *tet(O)* 65.8%, *ant*(6)-Ia 17.1%; GBS-related *wlaN/cstIII* in 20.1% (fernandezpalacios2024genotypiccharacterizationand pages 1-2) | Fernández-Palacios et al. 2024 / Microbiology Spectrum | https://doi.org/10.1128/spectrum.01028-24 | (fernandezpalacios2024genotypiccharacterizationand pages 1-2) |
| Vaccine trial: CJCV1 | Phase 1 completed trial of intramuscular capsule-conjugate vaccine CJCV1 with/without alum; 48 healthy adults, 2 vaccinations, dose escalation 2/5/10 μg; prevention purpose; MeSH condition listed as “Campylobacter Infections” (NCT02067676 chunk 1, NCT02067676 chunk 2) | ClinicalTrials.gov NCT02067676 | https://clinicaltrials.gov/study/NCT02067676 | (NCT02067676 chunk 1, NCT02067676 chunk 2) |
| Vaccine trial: CJCV2 | First-in-human Phase 1 randomized, double-blind trial of CJCV2 with/without ALFQ; 59 participants, three IM vaccinations, 1/3/10 μg dose levels; primary aim safety, secondary aim capsule-specific IgG immunogenicity (NCT05500417 chunk 1, NCT05500417 chunk 2) | ClinicalTrials.gov NCT05500417 | https://clinicaltrials.gov/study/NCT05500417 | (NCT05500417 chunk 1, NCT05500417 chunk 2) |


*Table: This table compiles high-yield disease facts and recent 2023–2024 evidence for human campylobacteriosis, including epidemiology, diagnostics, AMR, and vaccine pipeline data. It is designed as a compact reference for a disease knowledge base or research report.*

---

## 1. Disease information

### Overview (current understanding)
Campylobacteriosis is an acute zoonotic bacterial infection that most commonly manifests as gastroenteritis (enteric infection), but can also present as extra-intestinal infection (e.g., bacteremia) caused by **Campylobacter species**, most often **Campylobacter jejuni**. (island2024guidelinesforthe pages 1-5, tikhomirova2024campylobacterjejunivirulence pages 1-2)

Common symptom complexes include diarrhea (sometimes bloody), abdominal pain/cramping, fever, nausea/vomiting, and malaise; asymptomatic infection occurs. (myintzaw2023areviewon pages 1-4, island2024guidelinesforthe pages 1-5)

### Key identifiers / ontologies
- **MeSH:** *Campylobacter Infections* (**D002169**) (ClinicalTrials.gov derived MeSH browse for NCT02067676). (NCT02067676 chunk 1)
- **ICD-10 / ICD-11 / MONDO:** Not present in the retrieved full-text evidence; therefore not reported to avoid mislabeling.

### Common synonyms and alternative names
- Campylobacteriosis; **Campylobacter gastroenteritis**; **Campylobacter enteritis**; **Campylobacter infection**. (khairullah2024campylobacteriosisarising pages 2-3, bristiUnknownyearcampylobacteriosisinthe pages 8-10)

### Evidence provenance
This report draws on **aggregated disease-level resources** (reviews, surveillance studies, and guidelines) and includes supporting **human clinical** and **public health surveillance** evidence and selected **animal-model** and **reservoir** studies. (suominen2024campylobacteriosisinfinland pages 1-2, duarte2024epidemiologicaldataand pages 4-6, bacon2024diversityofcampylobacter pages 1-2)

---

## 2. Etiology

### Disease causal factors
- **Infectious etiology:** Campylobacter spp. infection.
- **Major causative agents:** **C. jejuni** and **C. coli**, commonly reported as the dominant causes of human disease (e.g., one 2024 review notes C. jejuni causes >80% of human Campylobacter disease and C. coli up to ~18.6%). (khairullah2024campylobacteriosisarising pages 2-3)
- **Other Campylobacter species:** have been isolated from human clinical samples and may contribute to disease, but less commonly than C. jejuni/coli (e.g., C. lari, C. fetus, C. concisus). (olveraramirez2023asystematicreview pages 1-2)

### Risk factors (exposure and host)
- **Foodborne exposure:** contaminated/undercooked poultry and cross-contamination during preparation are repeatedly highlighted as major drivers of human infection. (myintzaw2023areviewon pages 1-4, tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **Water and dairy exposure:** contaminated water and **unpasteurized milk** are recognized sources. (tikhomirova2024campylobacterjejunivirulence pages 1-2, island2024guidelinesforthe pages 5-8)
- **Animal contact/environment:** contact with infected animals and contaminated environments contributes (including domestic animals and farm environments). (khairullah2024campylobacteriosisarising pages 2-3, veronese2024campylobacterjejunicoliinfection pages 2-4)
- **Travel:** surveillance/case-control evidence indicates a large travel-associated component in some settings; in Finland, a key limitation was that 41% of notifications lacked travel history, and a case-control study estimated **39%** of cases were domestic (implying many remaining cases are travel-associated or unknown). (suominen2024campylobacteriosisinfinland pages 1-2)
- **Host vulnerability:** immunocompromise and other risk conditions influence severity and treatment decisions in guidance documents. (veronese2024campylobacterjejunicoliinfection pages 9-11, island2024guidelinesforthe pages 5-8)

### Protective factors
Specific protective factors (e.g., genetic variants or interventions) were not identified in the retrieved evidence corpus.

### Gene–environment interactions
No explicit human gene–environment interaction studies were retrieved; however, multiple sources emphasize that clinical outcomes depend on both **pathogen factors** (e.g., LOS configuration, virulence genes) and **host immune responses**. (olveraramirez2023asystematicreview pages 1-2, imbrea2024exploringthecontribution pages 1-2)

---

## 3. Phenotypes (clinical presentation and sequelae)

### Acute gastroenteritis phenotype
- **Symptoms/signs (typical):** diarrhea (may be bloody), abdominal pain, malaise, fever, nausea, vomiting. (myintzaw2023areviewon pages 1-4, island2024guidelinesforthe pages 1-5)
- **Incubation:** commonly reported as **2–5 days**; another surveillance-oriented source reports **24–72 hours**. (myintzaw2023areviewon pages 4-6, suominen2024campylobacteriosisinfinland pages 1-2)
- **Duration:** can be self-limited and about **~1 week** (or “within two to five days” in one guideline). (tikhomirova2024campylobacterjejunivirulence pages 1-2, island2024guidelinesforthe pages 5-8)
- **Asymptomatic infection:** explicitly noted. (myintzaw2023areviewon pages 1-4, island2024guidelinesforthe pages 1-5)

**Suggested HPO terms** (non-exhaustive)
- Diarrhea **HP:0002014**; Bloody diarrhea **HP:0002024**
- Abdominal pain **HP:0002027**
- Fever **HP:0001945**
- Nausea **HP:0002018**; Vomiting **HP:0002013**
- Malaise **HP:0033834**

### Extra-intestinal disease and major sequelae
- **Bacteremia / extra-intestinal infection:** one guideline states bacteremia occurs in **<1%** of cases. (island2024guidelinesforthe pages 5-8)
- **Guillain–Barré syndrome (GBS):** post-infectious autoimmune neuropathy linked to C. jejuni; one guideline quantifies GBS at about **1 case per 2000 infections**. (island2024guidelinesforthe pages 5-8)
  - Mechanistic expert synthesis (Nature Reviews Disease Primers 2024): “*in patients with preceding Campylobacter jejuni infection, molecular mimicry causes a cross-reactive antibody response to nerve gangliosides*.” (NCT05500417 chunk 2)
- **Reactive arthritis:** repeatedly listed as a late complication. (myintzaw2023areviewon pages 1-4, olveraramirez2023asystematicreview pages 1-2)
- **Post-infectious IBS (PI-IBS):** a 2024 systematic review/meta-analysis across acute gastroenteritis reports PI-IBS prevalence **14.5% overall**, and states that in the available studies **Campylobacter was associated with the highest PI-IBS prevalence (20.7%)**. (badjo2024burdenandepidemiology pages 1-2)

**Suggested HPO terms** (non-exhaustive)
- Guillain-Barre syndrome **HP:0001308**
- Arthritis **HP:0001369**
- Irritable bowel syndrome **HP:0002570**

### Quality-of-life impact
QoL instruments were not directly reported in retrieved sources; however, long-term sequelae (GBS, PI-IBS) are emphasized as drivers of disability and prolonged symptoms. (myintzaw2023areviewon pages 1-4, NCT05500417 chunk 2)

---

## 4. Genetic / molecular information

### Human causal genes / inherited etiology
Campylobacteriosis is not primarily a Mendelian genetic disorder; no causal human genes or pathogenic human germline variants were retrieved.

### Pathogen genetic determinants (clinically relevant)
Recent WGS of human **C. jejuni** isolates (southern Spain; Oct 2020–Jun 2023) reported high prevalence of resistance/virulence determinants, including:
- **gyrA T86I** (fluoroquinolone resistance) in **88.9%** of isolates,
- **CmeABC** efflux in **92.1%**,
- **blaOXA-61** in **72.6%**,
- **tet(O)** in **65.8%**,
- GBS-associated loci **wlaN/cstIII** in **20.1%**. (fernandezpalacios2024genotypiccharacterizationand pages 1-2)

(These are pathogen determinants; they inform antimicrobial resistance and risk stratification rather than host inheritance.)

---

## 5. Environmental information

### Environmental and lifestyle contributors
- Food handling and consumption practices (especially poultry) are highlighted as a key exposure pathway. (myintzaw2023areviewon pages 1-4)
- Waterborne transmission and unpasteurized milk exposures are repeatedly listed. (tikhomirova2024campylobacterjejunivirulence pages 1-2, island2024guidelinesforthe pages 5-8)

### Infectious agent taxonomy
- Primary human pathogens: *Campylobacter jejuni* and *Campylobacter coli*. (myintzaw2023areviewon pages 1-4, khairullah2024campylobacteriosisarising pages 2-3)

---

## 6. Mechanism / pathophysiology (2024 updates prioritized)

### Core causal chain (trigger → cellular events → clinical disease)
1. **Ingestion** of low infectious dose Campylobacter (one guideline notes “low (500 organisms or less)”). (island2024guidelinesforthe pages 5-8)
2. **Colonization** of gut, supported by **motility/chemotaxis** (Tlps/Che proteins) and **adhesion** (e.g., CadF/FlpA). (tikhomirova2024campylobacterjejunivirulence pages 1-2)
3. **Invasion and barrier disruption**, including **HtrA-dependent junctional protein cleavage** enabling paracellular transmigration. (imbrea2024exploringthecontribution pages 15-17)
4. **Host inflammatory activation**, including LOS-driven innate immune activation (TLR4 agonism) and pro-inflammatory signaling; one review describes ADP-heptose triggering an NF-κB cascade requiring **ALPK1**. (imbrea2024exploringthecontribution pages 14-15, imbrea2024exploringthecontribution pages 15-17)
5. **Toxin effects** (e.g., cytolethal distending toxin, CDT) contribute to cytotoxicity and inflammation. (tikhomirova2024campylobacterjejunivirulence pages 1-2)
6. **Post-infectious sequelae**: in some infections, **sialylated LOS molecular mimicry** induces cross-reactive antibodies targeting host gangliosides, contributing to GBS. (NCT05500417 chunk 2, imbrea2024exploringthecontribution pages 15-17)

### Key molecular factors (pathogen)
- **Flagella**: enable corkscrew motility and can function as a **type III secretion system** for invasion-associated effectors. (tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **Adhesins**: CadF, FlpA. (tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **Protease**: HtrA implicated in paracellular translocation via junctional cleavage. (imbrea2024exploringthecontribution pages 15-17)
- **Secretion systems / effectors**: T3SS/T6SS; CiaI noted as facilitating intracellular survival. (tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **LOS**: TLR4 activation; sialylation linked to immune evasion/molecular mimicry. (imbrea2024exploringthecontribution pages 14-15, imbrea2024exploringthecontribution pages 15-17)

### Immune system involvement
- Innate immune activation via TLR4 (LOS lipid A) and downstream pro-inflammatory cascades is emphasized; neutrophil activation/NET formation is described in PI-IBS–focused mechanistic review (SliP-related). (imbrea2024exploringthecontribution pages 14-15)

### Suggested ontology terms
- **GO biological processes (examples):**
  - chemotaxis **GO:0006935**; bacterial chemotaxis **GO:0006935** (contextual)
  - epithelial barrier disruption **GO:0007165** (signal transduction) and tight junction organization **GO:0120192** (conceptual mapping)
  - NF-κB signaling **GO:0043122**
  - inflammatory response **GO:0006954**
- **CL cell types (examples):** intestinal epithelial cell **CL:0000066**; neutrophil **CL:0000775**

---

## 7. Anatomical structures affected

### Primary sites
- **Gastrointestinal tract:** distal ileum and colon epithelium are described as target sites in one 2024 review. (khairullah2024campylobacteriosisarising pages 4-5)

### Secondary sites (complications)
- Bloodstream in invasive disease (bacteremia). (island2024guidelinesforthe pages 5-8)
- Peripheral nervous system in GBS via immune-mediated injury. (NCT05500417 chunk 2)

### Suggested UBERON terms
- Small intestine **UBERON:0002108** (distal ileum **UBERON:0002116**)
- Colon **UBERON:0001155**
- Peripheral nervous system **UBERON:0000010**

---

## 8. Temporal development

### Onset and course
- **Onset:** acute, typically after an incubation of days (commonly 2–5 days). (myintzaw2023areviewon pages 4-6)
- **Course:** usually self-limited; one guideline notes symptoms often cease within **2–5 days**, whereas other reviews cite ~1 week typical duration. (island2024guidelinesforthe pages 5-8, tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **Relapse:** in Finland-oriented epidemiology, relapses were reported in **10–25%** of cases. (suominen2024campylobacteriosisinfinland pages 1-2)

---

## 9. Inheritance and population

### Epidemiology (recent surveillance-based statistics)
- **Burkina Faso (2018–2021; PCR-based):** Campylobacter detected in **25.0%** (324/1,295) acute gastroenteritis samples; **95%** (308/324) positives were in children <5 years. (badjo2024burdenandepidemiology pages 1-2)
- **Finland (pilot July–Aug 2022; reported 2024):** estimated **39% domestic**; WGS identified **22 clusters** among 185 domestic cases not recorded in the outbreak register; 41% notifications lacked travel history. (suominen2024campylobacteriosisinfinland pages 1-2)
- **Portugal (2009–2021 surveillance, reported 2024):** large under-notification suggested by mismatch between NRL isolate counts and notified cases; one excerpt reports ~50% isolates not notified in some years and strong pediatric skew (77.7% pediatric; 1–4 years highest). (duarte2024epidemiologicaldataand pages 4-6)
- **United States FoodNet (2023):** 29,607 infections, 7,234 hospitalizations, and 177 deaths were reported; the proportion diagnosed by CIDTs increased while culture isolate recovery decreased. (shah2024…commonlythrough pages 1-2)

---

## 10. Diagnostics (and real-world implementation)

### Clinical testing
- **Culture and NAAT/CIDT (PCR):** Guidelines define confirmed cases by culture isolation from appropriate specimens and probable cases by nucleic acid detection (PCR/NAT). (island2024guidelinesforthe pages 1-5)
- **Implementation impact:** FoodNet data emphasize that CIDT adoption increases detection but reduces isolate availability for subtyping/AMR testing, complicating surveillance interpretations. (shah2024…commonlythrough pages 1-2)

### Genomics-enabled diagnostics and surveillance (latest developments)
**Direct stool metagenomic WGS (2024):** Djeghout et al. evaluated direct WGS from stool as an isolate-independent route to obtain sequence types and AMR markers.
- In 37 Campylobacter-positive diarrheal stools, detection rates: **65%** metagenomic WGS vs **73%** culture vs **97%** qPCR. (djeghout2024capturingclinicallyrelevant pages 1-2)
- For metagenome-derived genomes with **>60% completeness**, species identification was **100%**, ST typing **72%**, and AMR determinant identification **95%**. (djeghout2024capturingclinicallyrelevant pages 1-2)
- Performance thresholds included **>12,500 Campylobacter reads** and **>5× coverage**; stool filtration improved recovery/assembly metrics. (djeghout2024capturingclinicallyrelevant pages 9-11, djeghout2024capturingclinicallyrelevant pages 1-2)

**Visual evidence:** the workflow and performance tables are shown in the cropped figure/table images from this study. (djeghout2024capturingclinicallyrelevant media 24d62d1a, djeghout2024capturingclinicallyrelevant media ebf6dfbb, djeghout2024capturingclinicallyrelevant media 86150b86)

### Differential diagnosis
Not systematically retrieved in this evidence set; in practice, differentials include other bacterial/viral gastroenteritides and inflammatory bowel disease flares, but those statements are not asserted here without direct citations.

---

## 11. Outcomes / prognosis

- **Usually self-limited:** several sources note that campylobacteriosis frequently resolves without antibiotic treatment. (barata2024adecadeof pages 1-2, island2024guidelinesforthe pages 5-8)
- **Invasive disease is uncommon:** bacteremia <1% in one guideline. (island2024guidelinesforthe pages 5-8)
- **Sequelae drive long-term burden:** GBS and PI-IBS are emphasized; PI-IBS can persist long-term in a substantial fraction of cases after acute gastroenteritis in general. (NCT05500417 chunk 2, badjo2024burdenandepidemiology pages 1-2)
- **Hospitalization markers:** in Finland case-control data, approximately one-third hospitalized and ~17% reported bloody diarrhea; EU hospitalization cited as 23% in 2021. (suominen2024campylobacteriosisinfinland pages 11-13)

---

## 12. Treatment

### Standard of care (guidelines and expert consensus)
- **Supportive care** (rehydration/electrolytes) is the mainstay; antimotility agents not recommended in one guideline. (island2024guidelinesforthe pages 5-8)
- **When to use antibiotics:** reserved for severe disease or high-risk groups; one guideline lists criteria including immune compromise, high fever, >8 stools/day, worsening after a week, bloody diarrhea, pregnancy. (island2024guidelinesforthe pages 5-8, island2024guidelinesforthe pages 8-10)
- **Preferred antibiotics:** macrolides (erythromycin/azithromycin) commonly recommended as first-line, with fluoroquinolones as second-line depending on resistance context; a 2024 review notes macrolides first-line and fluoroquinolones second-line. (barata2024adecadeof pages 1-2, veronese2024campylobacterjejunicoliinfection pages 9-11)

### Antimicrobial resistance (recent statistics)
- **NW Italy (2020–2023; n=820):** resistance to ≥1 antibiotic **80.1%**; ciprofloxacin **72.1%**, tetracycline **52.9%**, erythromycin **3.2%**; MDR **5.7%**. (tramuta2024phenotypicantimicrobialresistance pages 2-4)
- **Portugal surveillance (2009–2021; n=2174 tested):** ciprofloxacin **94.2%**, tetracycline **81.6%**, erythromycin **11.8% overall** (but **52.3%** in C. coli vs 3.3% in C. jejuni). (duarte2024epidemiologicaldataand pages 7-8)
- **Southern Spain WGS (2020–2023; n=114 C. jejuni):** ciprofloxacin **90.3%**, tetracycline **66.7%**, erythromycin **0.88%**, with high prevalence of gyrA T86I and cmeABC. (fernandezpalacios2024genotypiccharacterizationand pages 1-2)

### MAXO term suggestions (examples)
- Oral rehydration therapy **MAXO:0000747** (conceptual mapping)
- Antibiotic therapy **MAXO:0000749**

(Exact MAXO IDs may require ontology lookup; terms given as suggested actions.)

---

## 13. Prevention

### Primary prevention (food and water safety)
Guidelines emphasize:
- Thoroughly cook poultry and meat (e.g., poultry to **74°C / 165°F**). (island2024guidelinesforthe pages 8-10)
- Avoid unpasteurized milk; ensure safe water (boil uncertain water). (island2024guidelinesforthe pages 8-10)
- Prevent cross-contamination (cutting boards/surfaces) and maintain hand hygiene. (island2024guidelinesforthe pages 8-10, island2024guidelinesforthe pages 5-8)

### Public health / One Health prevention
Reducing contamination at poultry production and along the food chain is repeatedly identified as central to reducing human disease. (khairullah2024campylobacteriosisarising pages 2-3, barata2024adecadeof pages 1-2)

---

## 14. Other species / natural disease (zoonosis)

- **Reservoirs:** Poultry are repeatedly identified as primary reservoirs; other livestock reservoirs include cattle, pigs, and sheep; domestic cats/dogs also implicated as possible sources. (tikhomirova2024campylobacterjejunivirulence pages 1-2)
- **Wildlife:** a 2023 systematic review compiles prevalence data for >150 wild vertebrate species and frames wildlife as potential reservoirs/amplifiers with some host specificity. (olveraramirez2023asystematicreview pages 1-2)
- **Poultry disease context:** Campylobacter colonizes poultry intestines and is usually nonpathogenic in poultry; specific species (e.g., C. hepaticus) are linked to poultry diseases such as spotty liver disease. (sadek2023campylobacteriosisinpoultry pages 1-2)

---

## 15. Model organisms

- **Rhesus macaque (Macaca mulatta) natural model:** A 2024 mSphere study states rhesus macaques are susceptible to acute campylobacteriosis and may model chronic enterocolitis/PI-IBS-like outcomes; it reports prevalence in colonies and describes use of culture, qPCR and WGS for characterization. (bacon2024diversityofcampylobacter pages 1-2)
- **Other model systems referenced in the broader literature base** (not deeply detailed in retrieved excerpts): mouse models and other experimental systems are cited in the wildlife-reservoir review’s references. (olveraramirez2023asystematicreview pages 11-12)

---

## Recent developments and real-world implementations (2023–2024 highlights)

1. **Genomics in surveillance:** Finland’s 2024 analysis demonstrates that WGS can detect clusters missed by traditional outbreak reporting and recommends sequencing all domestic isolates. (suominen2024campylobacteriosisinfinland pages 1-2)
2. **Diagnostic paradigm shift:** Increasing use of CIDTs in FoodNet surveillance changes apparent incidence and reduces culture isolate availability for subtyping/AMR testing. (shah2024…commonlythrough pages 1-2)
3. **Direct-from-stool WGS methods:** 2024 Microbial Genomics work provides actionable thresholds for when metagenomic WGS can recover species, ST, and AMR determinants, helping close the isolate gap created by CIDTs. (djeghout2024capturingclinicallyrelevant pages 1-2, djeghout2024capturingclinicallyrelevant media 24d62d1a)
4. **AMR burden:** 2024 surveillance studies report high fluoroquinolone and tetracycline resistance in multiple settings, reinforcing macrolide-first guidance and One Health AMR monitoring needs. (tramuta2024phenotypicantimicrobialresistance pages 2-4, duarte2024epidemiologicaldataand pages 7-8)

---

## Experimental prevention: human vaccine clinical trials (selected)

- **CJCV1 (capsule-conjugate C. jejuni vaccine), Phase 1, completed:** NCT02067676; 48 healthy volunteers; dose-escalation and alum adjuvant evaluation; results posted 2018-01-25. (NCT02067676 chunk 1, NCT02067676 chunk 2)
  - URL: https://clinicaltrials.gov/study/NCT02067676 (posted 2014-02-20; results posted 2018-01-25). (NCT02067676 chunk 1)
- **CJCV2 ± ALFQ, Phase 1, completed:** NCT05500417; 59 participants; randomized, quadruply masked; 3 IM vaccinations; results posted 2026-01-30. (NCT05500417 chunk 1, NCT05500417 chunk 2)
  - URL: https://clinicaltrials.gov/study/NCT05500417 (first posted 2022-08-15; results posted 2026-01-30). (NCT05500417 chunk 1)

---

## Limitations of this tool-grounded report
- Formal **ICD-10/ICD-11 and MONDO** identifiers were not available in the retrieved evidence corpus, and are therefore intentionally omitted.
- Differential diagnosis and QoL metrics were not systematically retrieved in the accessible texts.



References

1. (island2024guidelinesforthe pages 1-5): PE Island. Guidelines for the management and control of campylobacteriosis. Unknown journal, 2024.

2. (khairullah2024campylobacteriosisarising pages 2-3): A. Khairullah, S. Yanestria, M. Effendi, I. Moses, Muhammad Khaliim Jati Kusala, K. A. Fauzia, Siti Rani Ayuti, Ima Fauziah, Otto Sahat Martua Silaen, Katty Hendriana Priscilia Riwu, Suhita Aryaloka, Fidi Nur Aini Eka Puji Dameanti, Ricadonna Raissa, Abdullah Hasib, and A. Furqoni. Campylobacteriosis: a rising threat in foodborne illnesses. Open Veterinary Journal, 14:1733-1750, Aug 2024. URL: https://doi.org/10.5455/ovj.2024.v14.i8.1, doi:10.5455/ovj.2024.v14.i8.1. This article has 24 citations.

3. (tikhomirova2024campylobacterjejunivirulence pages 1-2): Alexandra Tikhomirova, Emmylee R. McNabb, Luca Petterlin, Georgia L. Bellamy, Kyaw H. Lin, Christopher A. Santoso, Ella S. Daye, Fatimah M. Alhaddad, Kah Peng Lee, and Anna Roujeinikova. Campylobacter jejuni virulence factors: update on emerging issues and trends. Journal of Biomedical Science, May 2024. URL: https://doi.org/10.1186/s12929-024-01033-6, doi:10.1186/s12929-024-01033-6. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (suominen2024campylobacteriosisinfinland pages 1-2): Kristiina Suominen, Tessa Häkkänen, Jukka Ranta, Jukka Ollgren, Rauni Kivistö, Päivikki Perko-Mäkelä, Saara Salmenlinna, and Ruska Rimhanen-Finne. Campylobacteriosis in finland: passive surveillance in 2004–2021 and a pilot case-control study with whole-genome sequencing in summer 2022. Microorganisms, 12:132, Jan 2024. URL: https://doi.org/10.3390/microorganisms12010132, doi:10.3390/microorganisms12010132. This article has 6 citations.

5. (myintzaw2023areviewon pages 4-6): Peter Myintzaw, Amit K. Jaiswal, and Swarna Jaiswal. A review on campylobacteriosis associated with poultry meat consumption. Food Reviews International, 39:2107-2121, Jul 2023. URL: https://doi.org/10.1080/87559129.2021.1942487, doi:10.1080/87559129.2021.1942487. This article has 72 citations and is from a domain leading peer-reviewed journal.

6. (myintzaw2023areviewon pages 1-4): Peter Myintzaw, Amit K. Jaiswal, and Swarna Jaiswal. A review on campylobacteriosis associated with poultry meat consumption. Food Reviews International, 39:2107-2121, Jul 2023. URL: https://doi.org/10.1080/87559129.2021.1942487, doi:10.1080/87559129.2021.1942487. This article has 72 citations and is from a domain leading peer-reviewed journal.

7. (olveraramirez2023asystematicreview pages 1-2): Andrea Margarita Olvera-Ramírez, Neil Ross McEwan, Karen Stanley, Remedios Nava-Diaz, and Gabriela Aguilar-Tipacamú. A systematic review on the role of wildlife as carriers and spreaders of campylobacter spp. Animals, 13:1334, Apr 2023. URL: https://doi.org/10.3390/ani13081334, doi:10.3390/ani13081334. This article has 40 citations and is from a peer-reviewed journal.

8. (badjo2024burdenandepidemiology pages 1-2): Ange Oho Roseline Badjo, Nongodo Firmin Kabore, Arsène Zongo, Kobo Gnada, Aminata Ouattara, Merci Muhigwa, Soumeya Ouangraoua, Armel Poda, Satouro Arsène Some, Grit Schubert, Tim Eckmanns, Fabian H. Leendertz, Essia Belarbi, and Abdoul-Salam Ouedraogo. Burden and epidemiology of campylobacter species in acute enteritis cases in burkina faso. BMC Infectious Diseases, Aug 2024. URL: https://doi.org/10.1186/s12879-024-09709-y, doi:10.1186/s12879-024-09709-y. This article has 9 citations and is from a peer-reviewed journal.

9. (duarte2024epidemiologicaldataand pages 4-6): Andreia Duarte, Luísa Pereira, Maria-Leonor Lemos, Miguel Pinto, João Carlos Rodrigues, Rui Matias, Andrea Santos, and Mónica Oleastro. Epidemiological data and antimicrobial resistance of campylobacter spp. in portugal from 13 years of surveillance. Pathogens, 13:147, Feb 2024. URL: https://doi.org/10.3390/pathogens13020147, doi:10.3390/pathogens13020147. This article has 4 citations.

10. (duarte2024epidemiologicaldataand pages 1-2): Andreia Duarte, Luísa Pereira, Maria-Leonor Lemos, Miguel Pinto, João Carlos Rodrigues, Rui Matias, Andrea Santos, and Mónica Oleastro. Epidemiological data and antimicrobial resistance of campylobacter spp. in portugal from 13 years of surveillance. Pathogens, 13:147, Feb 2024. URL: https://doi.org/10.3390/pathogens13020147, doi:10.3390/pathogens13020147. This article has 4 citations.

11. (shah2024…commonlythrough pages 1-2): HJ Shah. … commonly through food: impact of increased use of culture-independent diagnostic tests—foodborne diseases active surveillance network, 1996–2023. Unknown journal, 2024.

12. (djeghout2024capturingclinicallyrelevant pages 7-9): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

13. (djeghout2024capturingclinicallyrelevant pages 9-11): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

14. (djeghout2024capturingclinicallyrelevant pages 1-2): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

15. (tramuta2024phenotypicantimicrobialresistance pages 2-4): C. Tramuta, Aitor Garcia-Vozmediano, CeRTiS Clinical Laboratories Group, C. Maurella, D. Bianchi, L. Decastelli, and Monica Pitti. Phenotypic antimicrobial resistance profiles of human campylobacter species isolated in northwest italy, 2020–2023. Microorganisms, 12:426, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030426, doi:10.3390/microorganisms12030426. This article has 5 citations.

16. (duarte2024epidemiologicaldataand pages 7-8): Andreia Duarte, Luísa Pereira, Maria-Leonor Lemos, Miguel Pinto, João Carlos Rodrigues, Rui Matias, Andrea Santos, and Mónica Oleastro. Epidemiological data and antimicrobial resistance of campylobacter spp. in portugal from 13 years of surveillance. Pathogens, 13:147, Feb 2024. URL: https://doi.org/10.3390/pathogens13020147, doi:10.3390/pathogens13020147. This article has 4 citations.

17. (fernandezpalacios2024genotypiccharacterizationand pages 1-2): Pablo Fernández-Palacios, Fátima Galán-Sánchez, Carlos S. Casimiro-Soriguer, Estefanía Jurado-Tarifa, Federico Arroyo, María Lara, J. Alberto Chaves, Joaquín Dopazo, and Manuel A. Rodríguez-Iglesias. Genotypic characterization and antimicrobial susceptibility of human <i>campylobacter jejuni</i> isolates in southern spain. Microbiology Spectrum, Oct 2024. URL: https://doi.org/10.1128/spectrum.01028-24, doi:10.1128/spectrum.01028-24. This article has 9 citations and is from a domain leading peer-reviewed journal.

18. (NCT02067676 chunk 1):  Safety Study of a Capsule-Conjugate Vaccine to Prevent Campylobacter-Caused Diarrhea. U.S. Army Medical Research and Development Command. 2014. ClinicalTrials.gov Identifier: NCT02067676

19. (NCT02067676 chunk 2):  Safety Study of a Capsule-Conjugate Vaccine to Prevent Campylobacter-Caused Diarrhea. U.S. Army Medical Research and Development Command. 2014. ClinicalTrials.gov Identifier: NCT02067676

20. (NCT05500417 chunk 1):  Safety and Immunogenicity of CJCV2 With and Without ALFQ. National Institute of Allergy and Infectious Diseases (NIAID). 2022. ClinicalTrials.gov Identifier: NCT05500417

21. (NCT05500417 chunk 2):  Safety and Immunogenicity of CJCV2 With and Without ALFQ. National Institute of Allergy and Infectious Diseases (NIAID). 2022. ClinicalTrials.gov Identifier: NCT05500417

22. (bristiUnknownyearcampylobacteriosisinthe pages 8-10): UP Bristi, M Hasan, S Dutta, NH Siddiquee, and S Rajia. Campylobacteriosis in the spotlight: insights from southeast asia. Unknown journal, Unknown year.

23. (bacon2024diversityofcampylobacter pages 1-2): Rebecca L. Bacon, Carolyn L. Hodo, Jing Wu, Shannara Welch, Colette Nickodem, Javier Vinasco, Deborah Threadgill, Stanton B. Gray, Keri N. Norman, and Sara D. Lawhon. Diversity of <i>campylobacter</i> spp. circulating in a rhesus macaque ( <i>macaca mulatta</i> ) breeding colony using culture and molecular methods. mSphere, Nov 2024. URL: https://doi.org/10.1128/msphere.00560-24, doi:10.1128/msphere.00560-24. This article has 6 citations and is from a peer-reviewed journal.

24. (island2024guidelinesforthe pages 5-8): PE Island. Guidelines for the management and control of campylobacteriosis. Unknown journal, 2024.

25. (veronese2024campylobacterjejunicoliinfection pages 2-4): Piero Veronese and Icilio Dodi. Campylobacter jejuni/coli infection: is it still a concern? Microorganisms, 12:2669, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122669, doi:10.3390/microorganisms12122669. This article has 22 citations.

26. (veronese2024campylobacterjejunicoliinfection pages 9-11): Piero Veronese and Icilio Dodi. Campylobacter jejuni/coli infection: is it still a concern? Microorganisms, 12:2669, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122669, doi:10.3390/microorganisms12122669. This article has 22 citations.

27. (imbrea2024exploringthecontribution pages 1-2): Ana-Maria Imbrea, Igori Balta, Gabi Dumitrescu, David McCleery, Ioan Pet, Tiberiu Iancu, Lavinia Stef, Nicolae Corcionivoschi, and Petculescu-Ciochina Liliana. Exploring the contribution of campylobacter jejuni to post-infectious irritable bowel syndrome: a literature review. Applied Sciences, 14:3373, Apr 2024. URL: https://doi.org/10.3390/app14083373, doi:10.3390/app14083373. This article has 17 citations.

28. (imbrea2024exploringthecontribution pages 15-17): Ana-Maria Imbrea, Igori Balta, Gabi Dumitrescu, David McCleery, Ioan Pet, Tiberiu Iancu, Lavinia Stef, Nicolae Corcionivoschi, and Petculescu-Ciochina Liliana. Exploring the contribution of campylobacter jejuni to post-infectious irritable bowel syndrome: a literature review. Applied Sciences, 14:3373, Apr 2024. URL: https://doi.org/10.3390/app14083373, doi:10.3390/app14083373. This article has 17 citations.

29. (imbrea2024exploringthecontribution pages 14-15): Ana-Maria Imbrea, Igori Balta, Gabi Dumitrescu, David McCleery, Ioan Pet, Tiberiu Iancu, Lavinia Stef, Nicolae Corcionivoschi, and Petculescu-Ciochina Liliana. Exploring the contribution of campylobacter jejuni to post-infectious irritable bowel syndrome: a literature review. Applied Sciences, 14:3373, Apr 2024. URL: https://doi.org/10.3390/app14083373, doi:10.3390/app14083373. This article has 17 citations.

30. (khairullah2024campylobacteriosisarising pages 4-5): A. Khairullah, S. Yanestria, M. Effendi, I. Moses, Muhammad Khaliim Jati Kusala, K. A. Fauzia, Siti Rani Ayuti, Ima Fauziah, Otto Sahat Martua Silaen, Katty Hendriana Priscilia Riwu, Suhita Aryaloka, Fidi Nur Aini Eka Puji Dameanti, Ricadonna Raissa, Abdullah Hasib, and A. Furqoni. Campylobacteriosis: a rising threat in foodborne illnesses. Open Veterinary Journal, 14:1733-1750, Aug 2024. URL: https://doi.org/10.5455/ovj.2024.v14.i8.1, doi:10.5455/ovj.2024.v14.i8.1. This article has 24 citations.

31. (djeghout2024capturingclinicallyrelevant media 24d62d1a): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

32. (djeghout2024capturingclinicallyrelevant media ebf6dfbb): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

33. (djeghout2024capturingclinicallyrelevant media 86150b86): Bilal Djeghout, Thanh Le-Viet, Leonardo de Oliveira Martins, George M. Savva, Rhiannon Evans, David Baker, Andrew Page, Ngozi Elumogo, John Wain, and Nicol Janecko. Capturing clinically relevant campylobacter attributes through direct whole genome sequencing of stool. Microbial Genomics, Aug 2024. URL: https://doi.org/10.1099/mgen.0.001284, doi:10.1099/mgen.0.001284. This article has 6 citations and is from a peer-reviewed journal.

34. (barata2024adecadeof pages 1-2): Rita Barata, Maria José Saavedra, and Gonçalo Almeida. A decade of antimicrobial resistance in human and animal campylobacter spp. isolates. Antibiotics, 13:904, Sep 2024. URL: https://doi.org/10.3390/antibiotics13090904, doi:10.3390/antibiotics13090904. This article has 19 citations.

35. (suominen2024campylobacteriosisinfinland pages 11-13): Kristiina Suominen, Tessa Häkkänen, Jukka Ranta, Jukka Ollgren, Rauni Kivistö, Päivikki Perko-Mäkelä, Saara Salmenlinna, and Ruska Rimhanen-Finne. Campylobacteriosis in finland: passive surveillance in 2004–2021 and a pilot case-control study with whole-genome sequencing in summer 2022. Microorganisms, 12:132, Jan 2024. URL: https://doi.org/10.3390/microorganisms12010132, doi:10.3390/microorganisms12010132. This article has 6 citations.

36. (island2024guidelinesforthe pages 8-10): PE Island. Guidelines for the management and control of campylobacteriosis. Unknown journal, 2024.

37. (sadek2023campylobacteriosisinpoultry pages 1-2): Sabry A. S. Sadek, Raafat M. Shaapan, and Ashraf M. A. Barakat. Campylobacteriosis in poultry: a review. Journal of World's Poultry Research, Jun 2023. URL: https://doi.org/10.36380/jwpr.2023.19, doi:10.36380/jwpr.2023.19. This article has 20 citations.

38. (olveraramirez2023asystematicreview pages 11-12): Andrea Margarita Olvera-Ramírez, Neil Ross McEwan, Karen Stanley, Remedios Nava-Diaz, and Gabriela Aguilar-Tipacamú. A systematic review on the role of wildlife as carriers and spreaders of campylobacter spp. Animals, 13:1334, Apr 2023. URL: https://doi.org/10.3390/ani13081334, doi:10.3390/ani13081334. This article has 40 citations and is from a peer-reviewed journal.
