---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T12:12:12.552728'
end_time: '2026-08-20T12:17:10.268438'
duration_seconds: 297.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: NEUROD2-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 27
  total_cost_usd: 1.8745021000000002
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 16
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NEUROD2-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **NEUROD2-Related Developmental and Epileptic Encephalopathy** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I'll research NEUROD2-Related Developmental and Epileptic Encephalopathy now, using web search and literature sources, then compile a comprehensive report.

I have comprehensive data now. Compiling the full research report.

---

# NEUROD2-Related Developmental and Epileptic Encephalopathy (DEE72): Comprehensive Research Report

## 1. Disease Information

**Overview:** NEUROD2-related developmental and epileptic encephalopathy (also designated **Developmental and Epileptic Encephalopathy 72, DEE72**; also described in the literature as "NEUROD2-related disorder" or "NEUROD2 neurodevelopmental syndrome") is a rare, autosomal dominant neurodevelopmental disorder caused by heterozygous, typically de novo, pathogenic variants in *NEUROD2* on chromosome 17q12. It was first described in 2019 (Sega et al., *Journal of Medical Genetics*, PMID:30323019) in two unrelated children with early infantile epileptic encephalopathy, and the phenotypic spectrum was substantially expanded by Runge et al. (2021, *Molecular Psychiatry*, PMID:34667263) to 11 patients from 8 families, and further by later case reports including patients without seizures (Rots et al./Guerin et al., *Am J Med Genet A*, PMID:33438828) and neonatal-onset presentations (Exploration Pub case report, 2024).

Core features across the spectrum: developmental delay/intellectual disability, autism spectrum disorder (ASD) features, and — in a subset — early-onset (often infantile-spasm/West syndrome-type) epilepsy that is frequently treatment-refractory. Not all patients have seizures; the phenotype is now understood as a continuum from isolated developmental delay/ASD to a severe DEE with infantile spasms.

**Key identifiers:**
- **Gene:** *NEUROD2* (Neuronal Differentiation 2), HGNC:7763 (per GeneCards/Wikigenes sourcing; some sources list 7761 — confirm against current HGNC), NCBI Gene ID 4762, chromosome **17q12**
- **OMIM Gene:** *601725 — NEUROGENIC DIFFERENTIATION 2; NEUROD2
- **OMIM Phenotype:** #618374 — DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 72; DEE72
- **UniProt (human protein):** Q15784 (Neurogenic differentiation factor 2 / NDF2 / NEUROD2)
- **Inheritance:** Autosomal dominant, virtually all reported cases de novo (one familial transmission reported: Runge cohort case with c.804C>A/p.Arg268Trp segregating with a milder phenotype in a parent)
- **Synonyms:** NDF2, NEUROD-related developmental disorder, DEE72; historically the gene product is also called "NDRF" (NeuroD-related factor) or "bHLHa1"

**Note on data provenance:** All information below is derived from aggregated case series and case reports in the peer-reviewed literature (not large-scale EHR/registry data), reflecting the rarity of the condition (currently >20 published cases across all reports).

Sources: [OMIM #618374](https://omim.org/entry/618374), [OMIM *601725](https://www.omim.org/entry/601725), [GeneCards NEUROD2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NEUROD2), [UniProt Q15784](https://www.uniprot.org/uniprotkb/Q15784/entry)

---

## 2. Etiology

**Disease causal factor:** Monogenic — heterozygous loss-of-function (predominantly missense, DNA-binding/dimerization-domain) variants in *NEUROD2*, a proneural basic helix-loop-helix (bHLH) transcription factor gene. All functionally tested pathogenic variants show reduced or absent transactivation/DNA-binding capacity in cellular (P19 embryonal carcinoma cell differentiation) and in vivo (*Xenopus laevis* ectopic-neuron induction) assays, consistent with **loss of function via haploinsufficiency** — heterozygous *Neurod2* knockout mice recapitulate defects seen in homozygous nulls, confirming dosage sensitivity (Runge et al. 2021, PMID:34667263).

**Genetic risk factors:**
- De novo heterozygous missense variants clustering in the bHLH DNA-binding/dimerization domain (residues ~120–170) are associated with the most severe (DEE/infantile spasms) phenotype: p.Glu130Gln (recurrent — reported in at least 4 independent patients), p.Met134Thr, p.Arg129Trp, p.Glu130Lys, p.Leu163Pro.
- Variants outside the canonical bHLH hotspot (e.g., p.Ala235Thr, p.Arg268Trp, p.Ala264Thr) are associated with milder phenotypes (developmental delay/ASD without seizures, or mild ID), though a 2024 neonatal-onset case (p.Ala264Thr, outside the bHLH domain) demonstrated that severe disease can arise from non-canonical regions too — indicating genotype-phenotype correlation is imperfect.
- No established genetic modifier loci or susceptibility variants reported to date; no protective genetic variants described.
- gnomAD: all reported pathogenic variants are absent from population databases (gnomAD v2/v4), consistent with strong purifying selection against *NEUROD2* loss-of-function alleles, though a formal published pLI/LOEUF constraint value for *NEUROD2* was not identified in this search.

**Environmental risk factors:** None established; this is a purely monogenic Mendelian disorder with no known environmental, toxin, infectious, or lifestyle contributors identified in the literature to date.

**Gene-environment interactions:** None reported.

Sources: [Sega et al. 2019, PMID:30323019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Runge et al. 2021, Mol Psychiatry, PMID:34667263](https://www.nature.com/articles/s41380-021-01179-x); [Rots et al./Guerin, PMID:33438828](https://pubmed.ncbi.nlm.nih.gov/33438828/); [NEUROD2-related disorder neonatal-onset case report, Exploration Pub 2024](https://www.explorationpub.com/Journals/ent/Article/1004154)

---

## 3. Phenotypes

### Core clinical features (aggregated from ~15–22 published cases):

| Phenotype | Type | Frequency (approx.) | Onset | Course | Suggested HPO term |
|---|---|---|---|---|---|
| Global developmental delay / intellectual disability | Clinical sign | Near-universal (primary defining feature) | Infancy–early childhood | Stable to progressive; variable severity | HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability) |
| Infantile spasms / West syndrome | Symptom/seizure type | Subset (severe end of spectrum, ~5/11–3/7 in various series) | ~5 months (range: neonatal–infancy) | Often refractory to standard ASMs | HP:0011097 (Infantile spasms); HP:0002373 (Hypsarrhythmia) |
| Epilepsy (general, not otherwise specified) | Symptom | Variable across series (~30–50%) | Infancy to childhood | Often drug-resistant | HP:0001250 (Seizure) |
| Autism spectrum disorder features | Behavioral | Common, "core phenotype" per Runge et al. | Early childhood | Stable | HP:0000729 (Autistic behavior) |
| ADHD symptoms / hyperactivity | Behavioral | ~5/7 (Runge cohort) | Childhood | Stable | HP:0007018 (Attention deficit hyperactivity disorder); HP:0000737 (Irritability)/HP:0000722 (Hyperactivity) |
| Hypotonia | Sign | Common in infantile-onset cases | Neonatal/infantile | Often improves partially | HP:0001252 (Hypotonia) |
| Hyperkinetic movements / stereotypies | Behavioral/motor | Variable, more common infantile-onset severe cases | Infancy–childhood | Chronic | HP:0002119 (Hyperkinesia); HP:0000733 (Stereotypy) |
| Absent or impaired walking | Motor | Common in severe cases | Persistent | Static/lifelong | HP:0002540 (Inability to walk) |
| Absent or impaired language | Speech | Common in severe cases | Persistent | Static/lifelong | HP:0002465 (Absent speech); HP:0000750 (Delayed speech and language) |
| Cortical visual impairment | Sensory | Variable feature | Infancy | Variable | HP:0100704 (Cerebral visual impairment) |
| Feeding difficulties / dysphagia | Sign | Common in neonatal-onset cases | Neonatal | Often improves | HP:0011968 (Feeding difficulties); HP:0002015 (Dysphagia) |
| Respiratory depression/distress (neonatal) | Sign | Reported in severe neonatal-onset case | Birth | Transient | HP:0002878 (Respiratory failure) |
| Rett-like features | Behavioral | Reported in ≥2 cases (p.Glu130Gln, p.Glu130Lys) | Infancy–childhood | Chronic | HP:0002185 (Neurodevelopmental regression, Rett-like) |
| Microcephaly | Growth | Reported in a subset | Infancy | Static | HP:0000252 (Microcephaly) |
| Central/generalized obesity | Growth | Reported in one case (p.Arg129Trp) | Childhood | Chronic | HP:0001513 (Obesity) |
| Aggressive behavior | Behavioral | Reported (familial p.Arg268Trp case) | Childhood/adult | Chronic | HP:0000718 (Aggressive behavior) |
| Fifth-finger clinodactyly, short stature | Dysmorphic/growth | Reported in one non-seizure case | Congenital | Static | HP:0004209 (Clinodactyly of the 5th finger); HP:0004322 (Short stature) |
| Cardiac septal defect (VSD) | Structural | Reported in one case (p.Leu163Pro) | Congenital | — | HP:0001629 (Ventricular septal defect) |
| Subcortical white-matter T2 hyperintensity | Neuroimaging | Reported in neonatal-onset case | Infancy | — | HP:0002500 (delayed myelination)/nonspecific white matter signal change |
| Bilateral putaminal T2 signal change, thin corpus callosum | Neuroimaging | Reported (Sega case 1) | Infancy | — | HP:0002079 (Hypoplasia of the corpus callosum) |
| Discontinuous/burst-suppression-like EEG | EEG | Reported in neonatal-onset case | Neonatal | — | HP:0010851 (Burst-suppression); HP:0011182 (Electroencephalographic abnormality) |

**Age of onset:** Bimodal — a severe neonatal/early-infantile presentation with respiratory depression, hypotonia, feeding difficulty, and seizures within the first weeks-to-months of life (infantile spasms peaking ~5 months), versus a milder presentation recognized later in childhood/adolescence with developmental delay/ASD and no seizures.

**Severity/progression:** Highly variable expressivity even for the same variant (e.g., p.Glu130Gln reported with DEE/infantile spasms in most carriers but developmental delay/ID±ASD without seizures in at least one). Disease course is generally static/non-progressive developmentally once the acute neonatal/infantile period resolves, though seizures can remain drug-resistant long-term in the severe subgroup.

**Quality of life impact:** Severely delayed or absent independent ambulation and language in the severe DEE subgroup substantially impacts activities of daily living and requires lifelong multidisciplinary support (physiotherapy, speech therapy, special education); the milder ASD/ID-only subgroup has better functional independence but persistent learning, social, and attentional impairment.

Sources: [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Runge et al. 2021 (PMC commentary summary)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/); [Guerin/Rots et al. 2021, PMID:33438828](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414); [neonatal case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154); [OMIM #618374](https://omim.org/entry/618374)

---

## 4. Genetic / Molecular Information

**Causal gene:** *NEUROD2* (OMIM *601725), a single-exon-poor, intron-containing gene on 17q12 encoding a class II bHLH transcription factor of the NeuroD family (paralogs: *NEUROD1*, *NEUROD4*, *NEUROD6*, *ATOH1*, *NEUROG1/2*).

**Reported pathogenic/likely pathogenic variants (composite literature list, cDNA reference NM_006160):**

| Variant (cDNA) | Protein | Domain | Inheritance | Recurrence | Associated phenotype |
|---|---|---|---|---|---|
| c.385C>T | p.Arg129Trp | bHLH basic domain | De novo | 1 | DD/ID±ASD, central obesity |
| c.388G>C | p.Glu130Gln | bHLH basic domain | De novo | ≥4 (recurrent hotspot) | DEE/infantile spasms (most), also DD/ID±ASD/Rett-like in some carriers |
| c.388G>A | p.Glu130Lys | bHLH basic domain | De novo | 1 | Severe delay, Rett-like/stereotypies |
| c.401T>C | p.Met134Thr | bHLH basic domain | De novo | 1 | DEE/infantile spasms |
| c.488T>C | p.Leu163Pro | bHLH second helix | De novo | 1 | DD/ID without seizures, VSD |
| c.703G>A | p.Ala235Thr | Outside bHLH | Unknown/uncertain | 1 | ASD/DD (functional testing showed normal activity — possible non-causal) |
| c.790G>A | p.Ala264Thr | Outside bHLH (exon 2) | De novo | 1 | Neonatal-onset DEE, ASD |
| c.804C>A | p.Arg268Trp | Outside bHLH | Familial (1) and unknown/de novo (1) | 2 | DD/ID±ASD, aggressive behavior (familial); mild ID (isolated) |

Functional testing (P19 embryonal carcinoma neuronal-differentiation assay and *Xenopus* ectopic-neuron induction) demonstrates that pathogenic missense variants impair or abolish NEUROD2's ability to induce neuronal differentiation — wild-type NEUROD2 induces ectopic neurons in ~90% of assayed cells, while the most severe variants (e.g., p.Glu130Gln) show near-complete loss, and others (e.g., p.Met134Thr) show an intermediate ~45% activity, correlating loosely with phenotypic severity.

**Variant classification:** All confirmed pathogenic variants are missense, de novo (with one reported familial transmission), and classified pathogenic/likely pathogenic per ACMG/AMP criteria (PS2/PM1/PM2/PP3 typically invoked); absent from gnomAD.

**Functional consequence:** Loss-of-function via impaired DNA binding/dimerization (bHLH domain variants) or reduced transactivation capacity, producing **haploinsufficiency** — confirmed directly in mouse models where *Neurod2+/-* heterozygotes phenocopy (with reduced severity) *Neurod2-/-* homozygous nulls.

**Modifier genes:** None formally established, though variable expressivity even for the identical p.Glu130Gln variant across unrelated patients suggests unidentified genetic or stochastic modifiers.

**Epigenetic information:** Not specifically characterized for this disorder; NEUROD2 itself functions upstream of chromatin/gene-regulatory programs (it is a "pioneer-adjacent" proneural transcription factor cooperating with E-proteins) but no disease-specific DNA methylation or histone signature has been reported.

**Chromosomal abnormalities:** Disease is caused by intragenic point mutation, not by large chromosomal rearrangement; no microdeletion/microduplication syndrome involving 17q12 is described as the DEE72 mechanism (note: 17q12 recurrent microdeletion/duplication syndrome, involving *HNF1B*, is a distinct, unrelated genomic disorder that also happens to map to 17q12 but is a different condition).

**Suggested GO terms for gene function:** GO:0006357 (regulation of transcription by RNA polymerase II), GO:0030154 (cell differentiation), GO:0021953 (central nervous system neuron differentiation), GO:0000981 (DNA-binding transcription factor activity, RNA polymerase II-specific), GO:0046983 (protein dimerization activity)

Sources: [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Runge et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/); [Guerin/Rots et al. 2021](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414); [neonatal case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154); [GeneCards NEUROD2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NEUROD2); [OMIM *601725](https://www.omim.org/entry/601725)

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated as causal or contributory in NEUROD2-related DEE — it is a purely monogenic disorder with no reported gene-environment interaction literature.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway/protein function:** NEUROD2 is a class II bHLH proneural transcription factor expressed at peak cortical excitatory neurogenesis, acting downstream of proneural genes and dimerizing with ubiquitous class I bHLH "E-proteins" (E2A/TCF3, HEB) to bind E-box (CANNTG) DNA elements in promoters of neuronal differentiation genes (e.g., GAP-43). ChIP/genome-wide target analysis shows NEUROD2 binds and regulates genes required for **Reelin signaling** (governing radial neuronal migration), layer-specific cortical differentiation, and axonal pathfinding of cortical projection neurons (PMID reference: BMC Genomics 2015 genome-wide target study).

**Cellular processes/causal chain (from mouse and Xenopus models):**
1. **Trigger:** Heterozygous loss-of-function *NEUROD2* variant → reduced transcription factor DNA-binding/dimerization activity → haploinsufficiency
2. **Cortical development defect:** In *Neurod2* knockout/heterozygous mouse embryos, cortical projection neurons **over-migrate**, altering the size and laminar position of cortical layers (particularly layer 5); amygdala nuclei (lateral and basolateral) fail to form properly in nulls, with reduced neuron numbers in heterozygotes
3. **Synaptic/circuit defect:** Altered dendritic spine density and turnover in layer 5 pyramidal neurons; dysregulated expression of genes controlling neuronal excitability and synaptic function (including AMPA receptor subunits, GABA-A receptor γ subunit, and the gene *Ulip1*), whose human orthologs are strongly enriched for ASD associations
4. **Network hyperexcitability:** Increased intrinsic neuronal excitability; in the *Xenopus* CRISPR knockdown model, calcium imaging reveals prolonged, strong hyperactivity signals sweeping through the brain, and behavioral C-shaped seizure-like contractions
5. **Blood-brain barrier dysfunction:** NeuroD2-deficient tadpoles show significantly increased BBB permeability (sodium fluorescein leakage 5.5–7.7× higher than controls), associated with elevated neural progenitor marker Vimentin and reduced BBB-associated aquaporin-1 expression — a novel, non-neuronal contributor to the seizure phenotype
6. **Clinical output:** Developmental delay/ID, ASD-like behaviors, hyperactivity/stereotypies, and — when excitability/BBB dysfunction crosses a threshold — clinical seizures, often as infantile spasms

**Cell types involved:** Cortical excitatory/glutamatergic projection neurons (primary), amygdala neurons (lateral/basolateral nuclei), radial glia/neural progenitors (Reelin-responsive migration), and blood-brain barrier endothelial/glial components (newly implicated).

**Tissue damage mechanism:** Not classic tissue injury (no oxidative stress/fibrosis/necrosis reported) — this is a **neurodevelopmental circuit-wiring disorder**: aberrant neuronal migration/lamination and synaptic dysregulation rather than degenerative tissue damage.

**Molecular profiling data:** Bulk RNA-sequencing in *Neurod2* KO mouse cortex shows dysregulation of genes controlling neuronal excitability and synaptic function, with human orthologs strongly overlapping ASD risk-gene sets (Runge et al. 2021). Preliminary Xenopus transcriptomic data show altered neural progenitor and BBB-associated gene expression (elevated Vimentin, reduced aquaporin-1).

**Emerging therapeutic mechanistic insight:** In the Xenopus DEE72 model, the TGF-β pathway antagonist **losartan** reduced seizure-like C-shaped contractions by >4-fold and calcium hyperactivity spikes by nearly 4-fold, and transiently improved BBB integrity — implicating TGF-β/BBB-mediated hyperexcitability as a druggable downstream mechanism (a pathway also implicated in other genetic epilepsies with BBB involvement).

**Suggested GO/CL terms:**
- GO:0021953 (central nervous system neuron differentiation), GO:0021799 (cerebral cortex radially oriented cell migration), GO:0007399 (nervous system development), GO:0035418 (protein localization to synapse), GO:0007268 (chemical synaptic transmission)
- CL:0000679 (glutamatergic neuron), CL:0002605 (astrocyte of the cerebral cortex — BBB), CL:0000115 (endothelial cell — BBB)
- UBERON:0001950 (neocortex), UBERON:0002884 (basolateral amygdaloid nucleus), UBERON:0001902 (epithelium of choroid plexus / BBB structures as relevant)

Sources: [BMC Genomics 2015, genome-wide NEUROD2 target analysis](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-1882-9); [Frontiers 2021, Role of Neurod genes in brain development](https://www.frontiersin.org/articles/10.3389/fnmol.2021.662774); [Runge et al. 2021, Mol Psychiatry](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/); [Xenopus DEE72 model, PMC11228833](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228833/); [Lin et al. 2005, PNAS — amygdala/emotional learning, PMID:16203979](https://www.pnas.org/doi/10.1073/pnas.0506785102)

---

## 7. Anatomical Structures Affected

**Organ level:** Primary organ affected is the **brain** (central nervous system); no primary involvement of other organ systems is described (occasional congenital comorbidities such as a ventricular septal defect have been reported in single cases but are not considered core disease features).

**Body systems:** Nervous system (primary); secondary developmental/behavioral system involvement (cognitive, motor, psychiatric/behavioral).

**Tissue/cell level:**
- Cerebral cortex — excitatory/glutamatergic projection neurons across cortical layers (particularly layer 5), affected by migration and lamination defects
- Amygdala — lateral and basolateral nuclei, hypoplastic/absent in severe loss-of-function models
- Blood-brain barrier — endothelial/glial limiting membrane components, showing increased permeability in models

**Subcellular level:** Nucleus (site of NEUROD2 transcription factor DNA binding/E-box activity); dendritic spines (altered density/turnover in layer 5 pyramidal neurons); synapse (altered excitatory/inhibitory receptor expression — AMPA and GABA-A receptor subunits).

**Localization:** Bilateral, diffuse cortical/subcortical involvement (not unilateral or focal); neuroimaging findings when present are typically bilateral (e.g., bilateral putaminal T2 signal change, thin corpus callosum, diffuse white matter signal change).

**Suggested UBERON/GO-CC terms:** UBERON:0000955 (brain), UBERON:0001950 (neocortex), UBERON:0002884 (basolateral amygdaloid nucleus), UBERON:0002360 (corpus callosum), UBERON:0001133 (neostriatum/putamen); GO:0005634 (nucleus), GO:0043198 (dendritic shaft)/GO:0043197 (dendritic spine)

Sources: [Frontiers 2021 Neurod genes review](https://www.frontiersin.org/articles/10.3389/fnmol.2021.662774); [Lin et al. 2005 PNAS](https://www.pnas.org/doi/10.1073/pnas.0506785102); [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/)

---

## 8. Temporal Development

**Onset:**
- **Neonatal/early infantile subtype:** Presents at birth or within the first weeks of life with respiratory depression, hypotonia, hyporeactivity, and feeding difficulties, followed within the first month(s) by neonatal/infantile seizures (documented as early as birth in the 2024 neonatal case report).
- **Infantile-spasm subtype:** Infantile spasms/West syndrome onset around **5 months of age** (OMIM #618374).
- **Later-recognized subtype:** Developmental delay/ASD recognized in early-to-mid childhood without a seizure history (some patients identified only in adolescence/adulthood via exome sequencing, e.g., a 14-year-old and even adult mildly-affected relatives in familial cases).

**Onset pattern:** Insidious for the developmental-delay/ASD-predominant phenotype; acute/subacute for the neonatal-encephalopathy and infantile-spasms phenotypes.

**Progression:** Generally a **static/stable** neurodevelopmental encephalopathy after the acute neonatal/infantile period — this is not a degenerative disease. Seizures, when present, are frequently **drug-resistant** initially but some patients achieve seizure freedom with specific interventions (ketogenic diet, vagus nerve stimulation, or combined vigabatrin plus high-dose prednisolone for infantile spasms).

**Disease course pattern:** Chronic, lifelong; no spontaneous remission of the underlying neurodevelopmental phenotype is described, though seizure control can improve substantially with treatment (e.g., seizure freedom reported by 24 months in the neonatal-onset case with levetiracetam).

**Critical periods:** The prenatal/early postnatal period of cortical neurogenesis and migration (peak NEUROD2 expression window) is the biologically critical period during which the causal mechanism operates, though this is a developmental-window concept from animal models rather than a clinically actionable intervention window at present.

Sources: [OMIM #618374](https://omim.org/entry/618374); [neonatal-onset case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154); [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/)

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — fewer than ~25 patients reported in the peer-reviewed literature as of 2024–2025 across all published case series (Sega 2019: 2 patients; Runge 2021: 11 patients from 8 families; Rots/Guerin 2021: 2 additional patients; subsequent isolated case reports: several more). No formal population prevalence or incidence estimate has been established (ultra-rare/ORPHA "not yet documented" tier equivalent).

**Inheritance pattern:** Autosomal dominant. The overwhelming majority of cases are **de novo**; one instance of familial (parent-to-child) transmission is reported (p.Arg268Trp), associated with a milder phenotype (mild ID in one relative, more pronounced ID/ASD/aggressive behavior in the child), suggesting reduced penetrance or variable expressivity is possible for milder alleles.

**Penetrance:** Appears to be high but not fully characterized quantitatively; the familial case suggests incomplete penetrance or highly variable expressivity for at least one variant (p.Arg268Trp).

**Expressivity:** **Markedly variable** — the same variant (p.Glu130Gln) has been reported with DEE/infantile spasms in the majority of carriers but with milder developmental delay/ID±ASD (no seizures) or Rett-like features in others, indicating expressivity is not tightly variant-determined and likely involves stochastic or unidentified modifier factors.

**Genetic anticipation:** Not reported/not applicable (missense disorder, not a repeat-expansion disease).

**Germline mosaicism:** Not specifically documented in the literature reviewed, though as with other de novo dominant NDDs it cannot be excluded as a recurrence-risk consideration for future pregnancies in unaffected parents.

**Founder effects:** None reported; variants have arisen independently (recurrent p.Glu130Gln likely reflects a mutational hotspot rather than a founder effect, given occurrence in unrelated families of different backgrounds).

**Carrier frequency:** Not applicable (dominant disorder, not applicable to "carrier" framing); population frequency of pathogenic variants is essentially zero in gnomAD.

**Consanguinity role:** Not implicated (autosomal dominant, de novo mechanism).

**Population demographics:** No specific ethnic, geographic, or sex-based enrichment has been reported; cases have been described across multiple countries/regions (North America, Europe) with both male and female patients affected in roughly comparable numbers across the small published cohort (e.g., Sega cases: 1 female, 1 male; broader cohort mixed).

Sources: [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Runge et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/); [Guerin/Rots et al. 2021, PMID:33438828](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414); [OMIM #618374](https://omim.org/entry/618374)

---

## 10. Diagnostics

**Clinical/laboratory tests:** No specific biochemical or laboratory biomarker exists; standard metabolic/biochemical workup in these patients is typically pursued to exclude alternative diagnoses (e.g., inborn errors of metabolism) and is generally unremarkable/nonspecific.

**Imaging:** Brain MRI findings are variable and sometimes normal; when abnormal, reported findings include bilateral putaminal T2 hyperintensity, thin corpus callosum, mild cerebral volume loss, and subcortical white matter T2 hyperintensity. MRI is not diagnostic on its own but supports the encephalopathy workup and excludes structural/acquired causes.

**Electrophysiology (EEG):** Central to diagnosis and monitoring in the seizure-associated subtype — findings include hypsarrhythmia (consistent with West syndrome/infantile spasms), excessively discontinuous/burst-suppression-like background patterns in neonatal-onset disease, and electrographic seizures with minimal clinical correlation.

**Genetic testing (primary diagnostic modality):**
- **Exome sequencing (trio, proband + parents)** is the diagnostic method by which essentially all reported cases have been identified, given the absence of a recognizable clinical gestalt and the rarity/novelty of the gene-disease association.
- **Gene panels** for developmental and epileptic encephalopathy or intellectual disability/autism increasingly include *NEUROD2*, given its established OMIM phenotype entry (#618374).
- **Chromosomal microarray** is typically performed as part of standard first-tier NDD workup but does not detect the causal point mutations; it is used to exclude copy-number etiologies.
- **Single-gene Sanger sequencing** confirmatory testing (used in reported cases to confirm de novo status by testing both parents).
- Variant interpretation relies on **ACMG/AMP criteria** (absence from gnomAD, in silico deleteriousness — SIFT, PolyPhen-2, CADD — and, where available, functional assay data).

**Differential diagnosis:** Other genetic developmental and epileptic encephalopathies (e.g., *STXBP1*, *SCN2A*, *SCN8A*, *CDKL5*, *KCNQ2* DEEs), Rett syndrome (*MECP2* — explicitly excluded by genetic testing in at least one reported case), other syndromic autism/ID genes, and metabolic encephalopathies.

**Screening:** No population-level or newborn screening applicable (ultra-rare Mendelian disorder identified only via clinical exome/genome sequencing in symptomatic individuals); prenatal/preimplantation testing could theoretically be offered in families with a known variant (e.g., the reported familial case), though this is not documented as having occurred.

Sources: [neonatal-onset case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154); [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Guerin/Rots et al. 2021](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414); [OMIM #618374](https://omim.org/entry/618374)

---

## 11. Outcome / Prognosis

**Survival/mortality:** No mortality has been reported in the published case series; this does not appear to be a life-limiting condition in the classic sense (unlike some severe DEEs), though the literature base is too small to generate a formal survival statistic.

**Morbidity/function:** Substantial and often lifelong: severely delayed or absent independent ambulation and expressive language reported in the severe infantile-spasm subgroup; more variable but still significant functional impairment (ID, ASD, ADHD) in the milder subgroup. No formal quality-of-life instrument (EQ-5D, SF-36) data specific to this condition were identified.

**Disease course/complications:** Drug-resistant epilepsy is the principal disease-specific complication in the severe subgroup; hyperkinetic movement disorders and cortical visual impairment are additional variable complications. Some patients achieve good seizure control with combination or nonpharmacologic approaches (ketogenic diet, VNS, vigabatrin + high-dose prednisolone), suggesting favorable seizure prognosis is achievable in at least a subset despite initial refractoriness.

**Recovery potential:** With early, aggressive antiseizure treatment, seizure freedom has been documented (e.g., seizure-free by 24 months on levetiracetam in the neonatal-onset case; seizure freedom with ketogenic diet in the more severe Sega variant carrier; seizure freedom with VNS in the milder Sega variant carrier). The neurodevelopmental (cognitive/ASD) phenotype does not appear to remit but can be supported with early intervention/therapy services.

**Prognostic factors:** Variant location (bHLH domain vs. outside) shows a loose correlation with severity but is not fully predictive (documented exceptions in both directions); presence/absence and severity of neonatal seizures appears to correlate with overall developmental outcome severity.

Sources: [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [BMC Neurology vigabatrin/prednisolone case report 2022](https://link.springer.com/article/10.1186/s12883-022-02992-9); [neonatal-onset case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154)

---

## 12. Treatment

**Pharmacotherapy (antiseizure):**
- **Levetiracetam** — used successfully in the neonatal-onset case, with seizure control achieved by 24 months (NCIT:C29073, or generically NCIT:C15986 Pharmacotherapy + therapeutic_agent CHEBI levetiracetam)
- **Vigabatrin combined with high-dose prednisolone** — a specific reported combination therapy for NEUROD2-associated epileptic spasms, with documented favorable response (BMC Neurology 2022 case report) — the standard first-line hormonal/GABAergic combination for infantile spasms/West syndrome of any etiology, here shown effective in a NEUROD2-confirmed case
- Standard antiseizure medications are generally trialed first-line per usual DEE/infantile-spasms protocols, though initial refractoriness is common

**Non-pharmacologic/device-based therapy:**
- **Ketogenic diet** — reported to achieve seizure freedom in a patient with the more severe E130Q (p.Glu130Gln) variant (NCIT:C15447, Dietary Intervention)
- **Vagus nerve stimulation (VNS)** — reported to achieve seizure freedom in the M134T (p.Met134Thr) variant patient (NCIT device-based intervention; therapeutic_modality: DEVICE)

**Investigational/mechanism-based approaches (preclinical):**
- **Losartan** (an angiotensin receptor blocker with TGF-β pathway antagonist activity) showed a >4-fold reduction in seizure-like behavior and calcium-imaging hyperactivity, plus transient improvement in blood-brain barrier integrity, in the *Xenopus laevis* NeuroD2 CRISPant model — a promising repurposing candidate not yet tested in human NEUROD2 patients (target_mechanisms: TGF-β pathway inhibition on the BBB-dysfunction/hyperexcitability node)

**Supportive/rehabilitative care:**
- Multidisciplinary developmental support: physiotherapy, occupational therapy, speech and language therapy (documented as ongoing follow-up in the neonatal-onset case)
- Nutritional/feeding support (orogastric tube feeding acutely, transition to oral feeding) for neonatal-onset presentations with feeding difficulty
- Respiratory support (non-invasive ventilation) in severe neonatal presentations

**Experimental treatments in trials:** No disease-specific clinical trials for *NEUROD2*-related DEE were identified in this search (consistent with its extreme rarity and recent gene-disease discovery).

**Treatment strategy:** No formal evidence-based treatment algorithm exists specific to NEUROD2-DEE given the small case numbers; management follows general DEE/infantile-spasms treatment pathways (hormonal therapy ± vigabatrin as first line for spasms, escalation to ketogenic diet or neuromodulation for drug-resistant epilepsy), individualized based on response, alongside standard developmental/behavioral intervention for the ID/ASD phenotype.

**Pharmacogenomics:** No NEUROD2-specific pharmacogenomic data identified.

Sources: [BMC Neurology 2022, vigabatrin + prednisolone case](https://link.springer.com/article/10.1186/s12883-022-02992-9); [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Xenopus DEE72 model / losartan, PMC11228833](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228833/); [neonatal-onset case report 2024](https://www.explorationpub.com/Journals/ent/Article/1004154)

---

## 13. Prevention

**Primary prevention:** Not applicable — this is a de novo genetic disorder with no known modifiable risk factor; no vaccination or exposure-avoidance strategy is relevant.

**Secondary prevention/early detection:** Early recognition via genetic testing (trio exome sequencing) in infants presenting with unexplained neonatal encephalopathy, hypotonia, and seizures could enable earlier targeted antiseizure treatment selection (e.g., prioritizing vigabatrin/prednisolone or ketogenic diet given documented efficacy signals in NEUROD2-specific cases) and earlier initiation of developmental therapies.

**Genetic counseling:** Recommended for families of an affected child given the predominantly de novo inheritance pattern (low empiric recurrence risk for future pregnancies, with residual risk from potential parental germline mosaicism not formally quantified for this gene). For the one reported familial case, predictive testing and reproductive counseling for at-risk relatives would be appropriate given documented intrafamilial transmission and variable expressivity.

**Screening:** No population or newborn screening program exists or is anticipated for this ultra-rare condition; diagnosis remains reactive (symptomatic testing) rather than proactive.

**Prophylaxis:** Not applicable.

Sources: General inference from inheritance data above; [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/); [Guerin/Rots et al. 2021](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414)

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring NEUROD2-associated disease has been reported in non-human species (companion animals, livestock, or wildlife); no veterinary case series or OMIA entry was identified in this search.

**Orthologous gene:** *Neurod2* is highly conserved; the mouse ortholog (NCBI Gene, chromosome 11) has been extensively studied via targeted knockout models (see Section 15). The variant residues implicated in human disease (e.g., Glu130, Met134) are described in the literature as "highly conserved across multiple species," supporting cross-species functional relevance of the bHLH domain.

**Comparative biology:** The bHLH DNA-binding mechanism and E-box-dependent proneural gene regulation are deeply conserved across vertebrates, which is why *Xenopus laevis* (frog) and *Mus musculus* (mouse) are both tractable and validated model systems for this human disease (see Section 15).

**Transmission:** Not applicable (non-infectious, non-zoonotic monogenic disorder).

---

## 15. Model Organisms

**Mouse models (*Mus musculus*, NCBITaxon:10090):**
- ***Neurod2* knockout (null) mice** — the foundational model (Bormuth et al. and related lines), showing failure of lateral and basolateral amygdala nuclei formation, deficits in emotional learning (fear conditioning), and reduced expression of AMPA receptor subunits, GABA-A receptor γ subunit, and *Ulip1* (Lin et al. 2005, PNAS, PMID:16203979). Cortical phenotypes include projection-neuron over-migration and altered layer 5 spine density/turnover, plus autism/schizophrenia-like behaviors (bioRxiv cortical morphofunctional study).
- ***Neurod2* heterozygous (+/−) mice** — directly model the human haploinsufficiency mechanism; **phenocopy homozygous null defects** (reduced amygdala neuron number, profound emotional-learning deficits), confirming dosage sensitivity (Lin et al. 2005; Runge et al. 2021). Behaviorally, KO and het mice show social interaction deficits, stereotypies, hyperactivity, and occasional spontaneous seizures (Runge et al. 2021, *Molecular Psychiatry*, PMID:34667263).
- **Fidelity/limitations:** The mouse model recapitulates core ASD-like behavioral domains (sociability, stereotypy, hyperactivity) and some seizure susceptibility, and directly demonstrates the haploinsufficiency mechanism central to human disease — high translational relevance for the neurodevelopmental/behavioral phenotype. It has been less thoroughly characterized for the severe infantile-spasms/hypsarrhythmia EEG phenotype specifically.
- **Resources:** MGI:107755 (Neurod2 mouse gene detail, Mouse Genome Informatics)

**Xenopus laevis models (frog; NCBITaxon:8355):**
- **CRISPR/Cas9 F0 "CRISPant" NeuroD2 knockdown/knockout tadpoles** — two independent guide RNA strategies: an in-frame 15bp deletion removing 5 amino acids from the bHLH domain (rnk5), and a frameshift 4bp deletion producing a premature stop codon and truncated protein (rnk20). This model **directly recapitulates seizure-like behavior** (C-shaped contractions), **neuronal hyperactivity** on calcium imaging, and — notably — a **leaky blood-brain barrier**, a novel disease mechanism not previously described in the mouse literature (PMC11228833, 2024).
- **Fidelity:** High construct validity (models the loss-of-function mechanism directly) and demonstrates strong face validity for the seizure phenotype (quantifiable seizure-like behavior and network hyperactivity), plus reveals a testable BBB-dysfunction mechanism. Used as a rapid in vivo drug-screening platform — losartan showed therapeutic effect in this model.
- Earlier Sega et al. (2019) and Guerin/Rots et al. (2021) also used **Xenopus mRNA microinjection "ectopic neuron induction" assays** as the primary variant-functional-validation tool (wild-type NEUROD2 mRNA induces ectopic neurons in injected embryos; pathogenic variant mRNA fails to do so), establishing loss-of-function for each newly identified human variant.

**Cellular models:**
- **P19 mouse embryonal carcinoma cells** — used as an in vitro neuronal-differentiation reporter assay to quantify the transactivation/differentiation-inducing capacity of wild-type versus mutant NEUROD2 protein (wild-type ~90% differentiation efficiency; loss-of-function variants show reduced-to-absent, or intermediate ~45%, efficiency) (Runge et al. 2021).

**Applications:** These models collectively enable (1) variant-level functional validation for clinical variant classification, (2) mechanistic dissection of the developmental (migration/lamination), synaptic (spine/excitability), and newly identified vascular (BBB) contributions to disease, and (3) preclinical drug screening (demonstrated for losartan in the Xenopus platform).

Sources: [Lin et al. 2005, PNAS, PMID:16203979](https://www.pnas.org/doi/10.1073/pnas.0506785102); [Runge et al. 2021, Mol Psychiatry](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/); [Xenopus DEE72 CRISPant model, PMC11228833, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228833/); [MGI:107755](https://www.informatics.jax.org/marker/MGI:107755); [Sega et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30323019/)

---

## Summary Table: Key Ontology Term Suggestions

| Category | Term | ID |
|---|---|---|
| Disease | Developmental and epileptic encephalopathy 72 | OMIM:618374 |
| Gene | NEUROD2 | HGNC:7763 (verify current); NCBI Gene:4762 |
| Protein | Neurogenic differentiation factor 2 | UniProt:Q15784 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Infantile spasms | HP:0011097 |
| Phenotype | Autistic behavior | HP:0000729 |
| Phenotype | Hypsarrhythmia | HP:0002373 |
| GO Process | Central nervous system neuron differentiation | GO:0021953 |
| GO Function | RNA polymerase II transcription factor activity | GO:0000981 |
| Cell type | Glutamatergic neuron | CL:0000679 |
| Anatomy | Neocortex | UBERON:0001950 |
| Anatomy | Basolateral amygdaloid nucleus | UBERON:0002884 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Dietary intervention (ketogenic diet) | NCIT:C15447 |

---

### Notes on Evidence Gaps
- No MONDO ID was directly confirmable for this specific entry in this search session (the disease is very recently described; a MONDO cross-reference likely exists via the OMIM #618374 mapping but was not directly located).
- Formal gnomAD constraint metrics (pLI/LOEUF) specific to *NEUROD2* were not located in this search.
- Precise HGNC numeric ID (7761 vs. 7763) should be confirmed directly against the current HGNC database before curation, as sources were inconsistent.
- No dedicated GeneReviews chapter was identified for this condition, consistent with its recent (2019+) description and small case count.

**Sources (consolidated):**
- [OMIM #618374 — DEE72](https://omim.org/entry/618374)
- [OMIM *601725 — NEUROD2](https://www.omim.org/entry/601725)
- [Sega et al. 2019, J Med Genet, PMID:30323019](https://pubmed.ncbi.nlm.nih.gov/30323019/)
- [Runge et al. 2021, Mol Psychiatry, PMID:34667263](https://www.nature.com/articles/s41380-021-01179-x) / [commentary PMC8988728](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988728/)
- [Guerin/Rots et al. 2021, Am J Med Genet A, PMID:33438828 / PMC8212414](https://ncbi.nlm.nih.gov/pmc/articles/PMC8212414)
- [Xenopus DEE72 CRISPant/losartan model, PMC11228833](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228833/)
- [BMC Neurology, vigabatrin + prednisolone case, 2022](https://link.springer.com/article/10.1186/s12883-022-02992-9)
- [Neonatal-onset NEUROD2 case report, Exploration Pub, 2024](https://www.explorationpub.com/Journals/ent/Article/1004154)
- [Lin et al. 2005, PNAS, PMID:16203979](https://www.pnas.org/doi/10.1073/pnas.0506785102)
- [BMC Genomics 2015, NEUROD2 target analysis](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-1882-9)
- [Frontiers 2021, Neurod gene family review](https://www.frontiersin.org/articles/10.3389/fnmol.2021.662774)
- [GeneCards NEUROD2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NEUROD2)
- [UniProt Q15784](https://www.uniprot.org/uniprotkb/Q15784/entry)
- [MGI:107755](https://www.informatics.jax.org/marker/MGI:107755)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.