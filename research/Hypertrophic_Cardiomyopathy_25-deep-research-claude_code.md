---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:55:55.292769'
end_time: '2026-08-01T21:16:39.318857'
duration_seconds: 1244.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 25
  mondo_id: ''
  category: Genetic
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 13
  num_turns: 60
  total_cost_usd: 4.79203475
  session_id: b289ebde-c37f-43a8-bdfa-57274d344188
  stop_reason: end_turn
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 25
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 25** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 25 (CMH25, TCAP-related)

**Prepared:** 2026-08-01 · **Target entity:** Hypertrophic Cardiomyopathy 25 (CMH25) · **MONDO:0011843** · **OMIM #607487** · **Gene: TCAP (telethonin/titin-cap), HGNC:11610, 17q12**

---

## ⚠️ Framing Statement — Read Before Curating

**CMH25 is a *disputed* gene–disease entity.** This is the single most important fact about it and must condition every other section of a knowledge-base entry.

- The **ClinGen Hereditary Cardiovascular Disorders Gene Curation Expert Panel** reclassified TCAP–hypertrophic cardiomyopathy from **LIMITED to DISPUTED on 2022-09-14** (`CGGV:assertion_c35abc20-c04c-49ec-af02-1bd270b0b50b-2022-09-14T160000.000Z`; Curation ID CCID:006333; MOI: AD; MONDO:0005045).
- Verbatim from the ClinGen evidence summary: *"In summary, the evidence supporting the relationship between TCAP and HCM has been DISPUTED. More evidence is needed to either support or entirely refute the role TCAP plays in this disease."*
- Also verbatim: *"None of these variants have functional evidence in support of pathogenicity. Furthermore, 1 variant (2 probands) is common in the population (Bos et al, 2006, PMID 16352453), and 2 co-occurred with other variants (pathogenic TNNI3 variant, Andersen et al, 2009, PMID 19035361; VUS in MYBPC3, Bos et al. 2006, PMID 16352453). The mechanism for disease is unknown."*
- Ingles et al. 2019 (PMID:30681346) independently placed TCAP among the majority of HCM genes with limited or no evidence: *"Of 33 HCM genes, only 8 (24%) were categorized as definitive ( MYBPC3, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, and MYL3); 3 had moderate evidence ( CSRP3, TNNC1, and JPH2; 33%); and 22 (66%) had limited (n=16) or no evidence (n=6)."*

**Curation implication:** CMH25 should be modeled as a *nosological entity that exists in OMIM/MONDO/MedGen* whose **gene–disease validity is actively disputed**, not as an established Mendelian disorder. Any `pathophysiology` chain curated for it is best framed as a **mechanistic hypothesis** (dismech `mechanistic_hypotheses` with `status: EMERGING` or a `discussions` block with `kind: KNOWLEDGE_GAP`), not as established causation. TCAP's *definitive* Mendelian disease is **autosomal recessive LGMD R7 (LGMD2G, OMIM #601954)**, not HCM.

---

## 1. Disease Information

### 1.1 Overview

Hypertrophic cardiomyopathy 25 (CMH25) is the OMIM-designated, gene-indexed form of familial hypertrophic cardiomyopathy attributed to heterozygous missense variation in **TCAP**, which encodes **telethonin (titin-cap, T-cap)** — a 19 kDa, 167-amino-acid sarcomeric Z-disc protein. The designation derives from a single 2004 candidate-gene study (Hayashi et al., PMID:15582318) that identified two TCAP missense variants (T137I, R153H) in Japanese HCM probands, supported by in vitro binding assays. Clinically, reported CMH25 is indistinguishable from sarcomeric HCM: asymmetric left ventricular hypertrophy, frequently septal, with dyspnea, syncope, palpitations, chest pain, arrhythmia, and variable risk of heart failure and sudden cardiac death.

MONDO defines it strictly by gene attribution (verified locally with OAK against `sqlite:obo:mondo`):

> `def: "Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the TCAP gene." [MONDO:patterns/disease_series_by_gene]`

Notably, MONDO places MONDO:0011843 under **three** parents simultaneously — `MONDO:0016192` (neuromuscular disease caused by qualitative or quantitative defects of telethonin), `MONDO:0016333` (familial dilated cardiomyopathy), and `MONDO:0024573` (familial hypertrophic cardiomyopathy) — an ontological reflection of TCAP's phenotypic promiscuity (HCM, DCM, LGMD R7) and of the weak boundary around this entity.

### 1.2 Key Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0011843` | hypertrophic cardiomyopathy 25 — **verified locally with OAK** |
| **OMIM (phenotype)** | `607487` | CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 25; CMH25 |
| **OMIM (gene)** | `604488` | TITIN-CAP; TCAP |
| **HGNC** | `hgnc:11610` | TCAP (lowercase prefix per dismech convention) |
| **NCBI Gene** | `8557` | TCAP |
| **UniProt** | `O15273` | Telethonin, *Homo sapiens* |
| **MedGen** | CUI `C4225408` / UID `895360` | Hypertrophic cardiomyopathy 25 (CMH25) |
| **UMLS** | `C4225408` | |
| **DOID** | `DOID:0110328` | |
| **MeSH** | `C564388` | supplementary concept record |
| **GARD** | `GARD:0024827` | |
| **Orphanet** | *No CMH25-specific code.* | Orphanet models the parent as **ORPHA:155** "Familial isolated hypertrophic cardiomyopathy" (flagged NON RARE IN EUROPE). TCAP's Orphanet-recognized disease is LGMD R7. |
| **ICD-10** | `I42.1` (obstructive HCM) / `I42.2` (other HCM) | Parent-level only — **not CMH25-specific; verify before asserting** |
| **ICD-11** | `BC43.0` Hypertrophic cardiomyopathy | Parent-level only — **flagged as unverified in this session** |
| **SNOMED CT** | 233873004 Hypertrophic cardiomyopathy (parent) | **Unverified in this session** |

MONDO synonym set (verified): CMH25; TCAP hypertrophic cardiomyopathy; cardiomyopathy, familial hypertrophic, type 25; cardiomyopathy, hypertrophic, 25; hypertrophic cardiomyopathy caused by mutation in TCAP; hypertrophic cardiomyopathy type 25; cardiomyopathy, familial hypertrophic, 25 (RELATED).

### 1.3 Provenance of the Evidence Base

**All CMH25-specific information is derived from aggregated, disease-level sources**, not from individual-patient/EHR data:
- Primary case reports and small candidate-gene cohorts (n = 2 probands in the index study; ≤ 8 probands total in all HCM literature per ClinGen).
- Curated aggregators: OMIM, MONDO, MedGen, HPO, ClinVar, ClinGen Gene-Disease Validity.
- **No EHR-derived, registry-derived, or population-cohort dataset exists specifically for CMH25.** Any epidemiological figure quoted below is for HCM as a whole.

---

## 2. Etiology

### 2.1 Disease Causal Factors

**Asserted cause:** heterozygous germline missense variation in **TCAP** (17q12), inherited autosomal dominantly, producing telethonin with altered Z-disc protein-binding affinity.

**Proposed causal mechanism (Hayashi et al. 2004, PMID:15582318) — verbatim from the abstract:**

> "Two TCAP mutations, T137I and R153H, were found in patients with HCM, and another TCAP mutation, E132Q, was identified in a patient with DCM. It was demonstrated by the qualitative assays that the HCM-associated mutations augment the ability of Tcap to interact with titin and calsarcin-1, whereas the DCM-associated mutations impair the interaction of Tcap with MLP, titin, and calsarcin-1."

> "These observations suggest that the difference in clinical phenotype (HCM or DCM) may be correlated with the property of altered binding among the Z-disc components."

This is a **gain-of-interaction** model for HCM (opposite in sign to the loss-of-interaction DCM model) — mechanistically unusual and, critically, **not independently replicated**. ClinGen explicitly discounted it (*"None of these variants have functional evidence in support of pathogenicity"*), presumably because yeast two-hybrid and GST pull-down competition are qualitative in vitro binding assays without cellular or organismal validation. **This tension between the published functional claim and the ClinGen assessment should be curated explicitly as a knowledge gap, not silently resolved either way.**

### 2.2 Genetic Risk Factors

| Variant (NM_003673.4) | Protein | dbSNP | ClinVar germline classification (as of 2026-08-01) | Review status | gnomAD AF | Source study |
|---|---|---|---|---|---|---|
| c.410C>T | p.Thr137Ile (T137I) | rs773317399 | **Pathogenic** | *no assertion criteria provided* (1 submitter — OMIM legacy) | not reported | Hayashi 2004, PMID:15582318 |
| c.458G>A | p.Arg153His (R153H) | rs149585781 | **Conflicting classifications** | criteria provided, conflicting | gnomAD 2.1×10⁻⁴; ExAC 1.7×10⁻⁴; TOPMed 5×10⁻⁵ | Hayashi 2004, PMID:15582318 |
| c.171C>G | p.Cys57Trp (C57W) | rs369447207 | **Uncertain significance** (3 submitters) | criteria provided, no conflicts | gnomAD 1–2×10⁻⁵ | Toste 2020, PMID:32565061 |
| c.208C>T | p.Arg70Trp (R70W) | rs775636212 | **Uncertain significance** (12 submitters) | criteria provided, no conflicts | gnomAD 3×10⁻⁵ | Bos 2006, PMID:16352453 |
| c.394G>C | p.Glu132Gln (E132Q) | rs748358368 | **Uncertain significance** (2 submitters) | criteria provided, no conflicts | gnomAD exomes 1×10⁻⁵ | Hayashi 2004 (DCM proband) |
| c.260G>A | p.Arg87Gln (R87Q) | rs121434298 | **Uncertain significance** | criteria provided, no conflicts | gnomAD exomes 19/1,458,643 = **1.30×10⁻⁵** (nfe 1.44×10⁻⁵; sas 1.16×10⁻⁵; eas 2.52×10⁻⁵; afr 2.99×10⁻⁵); gnomAD genomes 1/152,191 | Originally DCM1N; **OMIM reclassified to VUS** |
| c.157C>T | p.Gln53Ter (Q53X) | rs104894655 | **Pathogenic/Likely pathogenic** | criteria provided, no conflicts | ~1×10⁻⁵ | **LGMD R7 (recessive)** — listed under the CMH25 trait label by ClinVar trait propagation, *not* an HCM allele |
| c.110_110+1del | — | rs786205076 | **Pathogenic** | criteria provided, no conflicts | not reported | **LGMD R7 (recessive)** |
| — (frameshift) | p.Glu12fs | — | not in ClinVar as of this search | — | — | Hu 2025 (RP-HCM), PMID:40330574 |

**Benign/common TCAP variants routinely encountered on HCM panels (do not misclassify):**
- c.453A>C p.Ala151= (rs1053651): **Benign**, allele frequency **0.45–0.71** — a common polymorphism.
- c.316C>T p.Arg106Cys (rs45578741): **Benign/Likely benign**, gnomAD 0.008, TOPMed 0.0156.
- c.191C>T p.Ser64Leu (rs45458802): **Benign**, gnomAD 0.0039–0.0042.
- c.111-15dup (rs397516860): Benign/Likely benign.

> **Analytic point worth curating:** R153H — one of only two originally asserted CMH25 alleles — sits at gnomAD AF ≈ 2.1×10⁻⁴ (~1 in 2,400 alleles). For a putatively penetrant autosomal-dominant HCM allele, that frequency is an order of magnitude above what is plausible, and it is precisely the class of observation formalized by Walsh et al. 2017 (PMID:27532257): *"We found that in some genes previously reported as important causes of a given cardiomyopathy, rare variation is not clinically informative because there is an unacceptably high likelihood of false-positive interpretation."*

**Variant class distribution:** overwhelmingly **missense**. Alaei et al. 2023 (PMID:37752589) reviewed the whole TCAP literature: *"a total of 44 variants were reported for the TCAP gene in the literature where a majority of mutations were found to be missense."* Truncating TCAP alleles are the LGMD R7 mechanism (biallelic loss of telethonin), with one heterozygous frameshift (p.Glu12fs) reported in restrictive-phenotype HCM (PMID:40330574).

**Somatic vs germline:** exclusively **germline**. No somatic TCAP involvement in cardiomyopathy; TCAP is not a recognized COSMIC/TCGA cancer driver.

**Functional consequence:** disputed. The published model is **gain of protein–protein interaction** (HCM) versus **loss of interaction** (DCM) — see §6. Truncating alleles cause **loss of function** (telethonin absent on Western blot/IHC in LGMD R7; PMID:34982307, PMID:25724973).

### 2.3 Modifier Genes / Oligogenic Contribution

This is a substantive issue for CMH25. Two of the small number of reported TCAP-HCM probands **carried a second variant in another cardiomyopathy gene**, which ClinGen counted as evidence *against* TCAP causation:
- A **pathogenic TNNI3 variant** co-occurring in the Andersen 2009 cohort (PMID:19035361).
- A **MYBPC3 VUS** co-occurring in Bos 2006 (PMID:16352453).

Andersen et al. also reported broadly that *"Six patients carried two disease-associated mutations."* In dismech terms, TCAP variants in HCM are better modeled with `relationship_type: MODIFIER` or `SUSCEPTIBILITY` than as primary causal genes, pending new evidence.

The mechanistically nearest modifier candidates are TCAP's binding partners: **CSRP3/MLP** (moderate HCM evidence per ClinGen; interaction documented in PMID:12507422 and PMID:24860983), **TTN**, **MYOZ2/calsarcin-1**, and **FLNC**.

### 2.4 Environmental Risk Factors

There are **no CMH25-specific environmental risk factors** in the literature. HCM-generic modifiers apply: age (LVH develops through adolescence/adulthood; CMH25 HPO annotation is **adult onset**), male sex (male predominance in clinical HCM cohorts), systemic hypertension and obesity as phenotype amplifiers, and **intense competitive athletic exertion as a trigger for arrhythmic events**, not as a cause of the underlying genotype.

Because telethonin is a **mechanosensitive, load-responsive** protein (Ibrahim 2013, PMID:23100327: *"Both mechanical overload and unloading alter t-tubule structure"*; Knöll 2011, PMID:21799151: heart failure develops only *"following biomechanical stress"*), **hemodynamic load is the most biologically defensible candidate environmental modifier** for a TCAP-attributed cardiomyopathy. This is an inference from model-organism data, not a human clinical finding — curate as `evidence_source: MODEL_ORGANISM`.

### 2.5 Protective Factors

None identified, genetic or environmental. No protective TCAP alleles are reported. Avoidance of burst/high-intensity competitive exertion, and blood-pressure/weight control, are prudential HCM-generic measures without CMH25-specific evidence.

### 2.6 Gene–Environment Interactions

The only substantive G×E model available is the **mechanical-load × telethonin-deficiency interaction**, demonstrated in mice and unproven in humans:

> "Telethonin knockout mice do not reveal defective heart development or heart function under basal conditions, but develop heart failure following biomechanical stress, owing at least in part to apoptosis of cardiomyocytes, an effect that may also play a role in human heart failure." (Knöll et al. 2011, PMID:21799151)

This is a textbook conditional-penetrance architecture: genotype silent at baseline, unmasked by an environmental/hemodynamic stressor. **However, it is a loss-of-function (KO) model, whereas the human HCM hypothesis is gain-of-interaction — the model does not test the human allele class.** Curate as `HUMAN_MODEL_MISMATCH` rather than as supporting evidence.

---

## 3. Phenotypes

### 3.1 Curated HPO Annotation Set for OMIM:607487

The complete HPO annotation for CMH25 (retrieved from the JAX HPO annotation API) is remarkably sparse — derived from the two Hayashi probands only:

| HPO ID | Term (OAK-verified label) | Frequency | Category | Source |
|---|---|---|---|---|
| `HP:0001639` | **Hypertrophic cardiomyopathy** | 2/2 (100%) | Cardiovascular | PMID:15582318 |
| `HP:0001712` | **Left ventricular hypertrophy** | 2/2 (100%) | Cardiovascular | PMID:15582318 |
| `HP:0001716` | **Wolff-Parkinson-White syndrome** | 1/2 (50%) | Cardiovascular | PMID:15582318 |
| `HP:0003581` | **Adult onset** | 2/2 | Clinical course | PMID:15582318 |
| `HP:0000006` | **Autosomal dominant inheritance** | — | Inheritance | PMID:15582318 |

**All five labels verified locally with OAK against `sqlite:obo:hp`.** Denominators of 2 mean these "frequencies" carry essentially no statistical information — do **not** curate `frequency: OBLIGATE`/`VERY_FREQUENT` from a 2/2. Per the dismech frequency-evidence SOP, **omit `frequency:` for these**, or record the raw 2/2 in `notes`.

### 3.2 Phenotypes from Individual Case Reports (extend the HPO set)

**Toste et al. 2020, Portuguese family, p.C57W (PMID:32565061) — verbatim:**
> "Both affected members of this family presented with late-onset HCM, moderate asymmetric left ventricular hypertrophy, atrial fibrillation and heart failure with preserved ejection fraction and low risk of sudden cardiac death."

Suggested terms: `HP:0001670` Asymmetric septal hypertrophy; `HP:0005110` Atrial fibrillation; `HP:0001635` Congestive heart failure; `HP:0003581` Adult onset (all OAK-verified).

**Hu et al. 2025, restrictive-phenotype HCM, p.Glu12fs (PMID:40330574) — verbatim:**
> "Transthoracic echocardiography and cardiac magnetic resonance imaging (CMR) revealed non-obstructive hypertrophic cardiomyopathy (HCM) with severe diastolic dysfunction, biatrial enlargement, preserved ejection fraction, and normal chamber size. Endomyocardial biopsy demonstrated cardiomyocyte hypertrophy and focal fibrosis."

> "Despite interventions, the patient's cardiac function progressively deteriorated, leading to his placement on the heart transplant waiting list 1 year later."

Suggested terms: `HP:0025168` Left ventricular diastolic dysfunction; `HP:0001723` Restrictive cardiomyopathy; `HP:0001685` Myocardial fibrosis (all OAK-verified). This is a **single case**, n=1, and is the only report of an RP-HCM presentation.

**Bos et al. 2006 (PMID:16352453) — phenotype severity, verbatim:**
> "Patients with MLP/TCAP-associated HCM clinically mimicked myofilament-HCM."

> "MLP/TCAP-HCM phenotypically mirrors myofilament-HCM and is more severe than the subset of patients who still remain without a disease-causing mutation."

Cohort context: 389 HCM patients, 215 male, mean LV wall thickness **21.6 ± 6 mm**.

### 3.3 HCM-Generic Phenotype Spectrum (inherited from the parent entity)

Applicable to CMH25 by parent-class inheritance, **not** by CMH25-specific observation. All OAK-verified:

| HPO ID | Term | Type | Typical course |
|---|---|---|---|
| `HP:0002094` | Dyspnea | Symptom | Exertional, progressive |
| `HP:0001279` | Syncope | Symptom | Episodic; exertional; SCD-risk marker |
| `HP:0001962` | Palpitations | Symptom | Episodic |
| `HP:0100749` | Chest pain | Symptom | Exertional angina without epicardial CAD |
| `HP:0030148` | Heart murmur | Clinical sign | Systolic, dynamic, in obstructive HCM |
| `HP:0032092` | Left ventricular outflow tract obstruction | Physiological | ~⅔ of HCM overall, dynamic/provocable |
| `HP:0011675` | Arrhythmia | Clinical sign | — |
| `HP:0004756` | Ventricular tachycardia | Clinical sign | NSVT is an SCD-risk marker |
| `HP:0001645` | Sudden cardiac death | Outcome | The feared endpoint |
| `HP:0001695` | Cardiac arrest | Outcome | — |
| `HP:0001644` | Dilated cardiomyopathy | Late stage | "Burnt-out"/end-stage evolution |

### 3.4 Phenotypes of the *Other* TCAP Disease (LGMD R7) — for Differential/Boundary Curation

Curators must keep these **out of** the CMH25 entry (they belong to the autosomal-recessive LGMD R7 entity), but should know them for differential purposes:
- `HP:0003701` Proximal muscle weakness, `HP:0003236` Elevated circulating creatine kinase concentration (both OAK-verified).
- Phenotypic range is wide: from asymptomatic/paucisymptomatic hyperCKemia to classic limb-girdle weakness, with a facioscapulohumeral-like pattern in some (PMID:36463458, PMID:40195250).
- A characteristic imaging sign: *"Muscle MRI of four patients revealed consistent sparing of the sartorius muscle in all patients."* (PMID:40195250)
- Cardiac involvement occurs in a **minority** of LGMD R7 patients per UniProt's disease annotation — relevant because it means TCAP loss-of-function does *not* reliably produce cardiomyopathy in humans, a point that further weakens the CMH25 hypothesis.

### 3.5 Quality of Life

**No CMH25-specific QoL data exist.** No EQ-5D, SF-36, PROMIS, or HCMSQ (Hypertrophic Cardiomyopathy Symptom Questionnaire) data are reported for TCAP genotype carriers. HCM-generic QoL burden — exertional limitation, activity restriction, ICD-related anxiety, and the psychosocial burden of familial risk — applies by inheritance. In the Toste family, both affected members had **HFpEF with preserved functional capacity and low SCD risk**, i.e., a comparatively favorable QoL trajectory; the single RP-HCM case (PMID:40330574) had the opposite — progression to transplant listing within a year.

---

## 4. Genetic / Molecular Information

### 4.1 Causal Gene

| Attribute | Value |
|---|---|
| Symbol | **TCAP** (aliases: T-cap, telethonin, TELE, CMD1N, LGMD2G) |
| OMIM gene | **604488** |
| HGNC | **hgnc:11610** |
| NCBI Gene | 8557 |
| Cytoband | **17q12** — *"In human, telethonin maps at 17q12, adjacent to the phenylethanolamine N-methyltransferase gene."* (Valle et al. 1997, PMID:9350988, verbatim) |
| Reference transcript | NM_003673.4 |
| Gene structure | 2 exons (small, compact gene) |
| UniProt | **O15273** |
| Protein length | **167 aa** |
| Molecular mass | **19,052 Da** |

**UniProt O15273 FUNCTION (verbatim):** *"Muscle assembly regulating factor. Mediates the antiparallel assembly of titin (TTN) molecules at the sarcomeric Z-disk"*

**UniProt subcellular location:** Cytoplasm → myofibril → sarcomere. **Tissue specificity:** heart and skeletal muscle.

**UniProt disease annotations:** (1) Cardiomyopathy, familial hypertrophic, 25 (CMH25), MIM #607487; (2) Muscular dystrophy, limb-girdle, autosomal recessive 7 (LGMDR7), MIM #601954 — *"Autosomal recessive myopathy with proximal/distal muscle weakness and telethonin absence; cardiac involvement in some patients."*

**Discovery (Valle et al. 1997, PMID:9350988) — verbatim:**
> "In this paper we describe a novel 19 kDa sarcomeric protein named telethonin. The cDNA sequence discloses an open reading frame of 167 amino acids that does not resemble any known protein."

> "The frequency of specific cDNA clones in different libraries indicates that the telethonin transcript is amongst the most abundant in skeletal muscle."

### 4.2 Structural Biology of Telethonin

The defining structural insight is the **palindromic titin–telethonin assembly** (Zou et al. 2006, *Nature*, PMID:16407954) — verbatim:

> "Here we show, using X-ray crystallography, how the amino terminus of the longest filament component, the giant muscle protein titin, is assembled into an antiparallel (2:1) sandwich complex by the Z-disk ligand telethonin. The pseudosymmetric structure of telethonin mediates a unique palindromic arrangement of two titin filaments, a type of molecular assembly previously found only in protein-DNA complexes."

> "The model proposed may provide a molecular paradigm of how major sarcomeric filaments are crosslinked, anchored and aligned within complex cytoskeletal networks."

The complex involves the **titin Z1Z2 Ig domains** and roughly the **N-terminal 140 residues** of telethonin, joined by intermolecular β-sheet augmentation. Structural context for CMH25 alleles: T137I and R153H fall in the **C-terminal region** (residues 137, 153 of 167), *outside* the crystallized N-terminal titin-binding β-sandwich — a structural observation that sits awkwardly with the "augmented titin binding" functional claim and is worth flagging as an open question.

### 4.3 Post-Translational Modification / Phosphoregulation

**Candasamy et al. 2014, JBC (PMID:24280220) — verbatim:**
> "kinase assays used in conjunction with MS and site-directed mutagenesis confirmed telethonin as a substrate for protein kinase D and Ca(2+)/calmodulin-dependent kinase II in vitro and identified Ser-157 and Ser-161 as the phosphorylation sites."

> "Phosphate affinity electrophoresis and MS revealed endogenous telethonin to exist in a constitutively bis-phosphorylated form in isolated adult rat ventricular myocytes and in mouse and rat ventricular myocardium."

> "Such partial replacement with S157A/S161A telethonin disrupted transverse tubule organization and prolonged the time to peak of the intracellular Ca(2+) transient and increased its variance."

> "These data reveal, for the first time, that cardiac telethonin is constitutively bis-phosphorylated and suggest that such phosphorylation is critical for normal telethonin function, which may include maintenance of transverse tubule organization and intracellular Ca(2+) transients."

Note a **curation discrepancy to flag**: UniProt O15273 lists a phosphoserine at **Ser39**, whereas the functional cardiac literature centers on **Ser157/Ser161**. Both are real; UniProt's feature table is incomplete for the cardiac PKD/CaMKII sites. Cite Candasamy for the cardiac sites.

**Mechanistic relevance to CMH25:** T137I and R153H both lie in the C-terminal segment immediately flanking the Ser157/Ser161 regulatory module. A defensible (but **untested and unpublished as such**) hypothesis is that these substitutions perturb PKD/CaMKII phosphoregulation rather than titin binding per se. Curate as a `mechanistic_hypotheses` entry with `status: EMERGING` if included at all — it is an inference drawn in this report, not a literature claim.

### 4.4 Epigenetics

**No CMH25-specific epigenetic data.** No TCAP-locus methylation, histone-modification, or chromatin-accessibility findings are reported in cardiomyopathy. Generic HCM epigenetic literature (myocardial DNA methylation remodeling, HDAC involvement in hypertrophic signaling) is not gene-attributable to TCAP. ENCODE/Roadmap contain 17q12 regulatory annotations but nothing disease-linked.

### 4.5 Chromosomal Abnormalities

**None reported.** CMH25 is a point-variant disorder. 17q12 is a recurrent CNV locus (the 17q12 recurrent deletion/duplication syndrome, associated with *HNF1B*), but **that CNV interval and its phenotype are unrelated to TCAP-mediated cardiomyopathy** — do not conflate them. No pathogenic TCAP deletions/duplications are reported in HCM; chromosomal microarray has no role in CMH25 evaluation.

---

## 5. Environmental Information

- **Environmental factors:** None established. No toxicant, radiation, pollutant, or occupational exposure is implicated in CMH25. CTD contains no TCAP–cardiomyopathy chemical-gene-disease triad of clinical relevance.
- **Lifestyle factors:** No CMH25-specific data. HCM-generic considerations: high-intensity competitive athletics as an arrhythmic trigger (not a cause); hypertension and obesity as hypertrophy amplifiers; alcohol and dehydration as precipitants of dynamic LVOT obstruction in obstructive HCM.
- **Infectious agents:** **Not applicable.** CMH25 has no infectious etiology.
- **Mechanical/hemodynamic load** is the only environmental variable with any mechanistic support (see §2.6) — and only from mouse work.

---

## 6. Mechanism / Pathophysiology

### 6.1 Proposed Causal Chain (label explicitly as HYPOTHETICAL)

```
TCAP missense variant (T137I / R153H)          [MOLECULAR]
   │
   ▼
Altered telethonin Z-disc protein-binding —
"augmented" interaction with titin and calsarcin-1   [MOLECULAR]
   │
   ├─► Perturbed titin/Tcap/MLP mechanosensor output  [MOLECULAR]
   │        │
   │        ▼
   │   Dysregulated calsarcin-1 (MYOZ2)-tethered
   │   calcineurin–NFAT hypertrophic signaling        [CELLULAR]
   │
   ├─► Disrupted T-tubule organization and
   │   Ca²⁺-induced Ca²⁺ release (CICR)               [CELLULAR]
   │
   └─► Altered nuclear p53 turnover → "mechanoptosis" [CELLULAR]
            │
            ▼
   Cardiomyocyte hypertrophy + myocyte apoptosis      [CELLULAR]
            │
            ▼
   Asymmetric LV hypertrophy, myocardial fibrosis,
   diastolic dysfunction                              [TISSUE]
            │
            ▼
   HFpEF, arrhythmia, sudden cardiac death            [ORGANISM]
```

**Every arrow downstream of the first node is imported from telethonin biology in general (KO mice, in vitro, iPSC) rather than demonstrated for the CMH25 alleles.** In dismech terms this is exactly the situation `HUMAN_MODEL_MISMATCH` was designed for.

### 6.2 The Z-Disc Mechanosensor Complex (upstream node)

**Knöll et al. 2002, *Cell* (PMID:12507422) — verbatim:**
> "Muscle cells respond to mechanical stretch stimuli by triggering downstream signals for myocyte growth and survival. The molecular components of the muscle stretch sensor are unknown, and their role in muscle disease is unclear."

> "MLP interacts with and colocalizes with telethonin (T-cap), a titin interacting protein. Further, a human MLP mutation (W4R) associated with dilated cardiomyopathy (DCM) results in a marked defect in T-cap interaction/localization."

> "We propose that a Z disc MLP/T-cap complex is a key component of the in vivo cardiomyocyte stretch sensor machinery, and that defects in the complex can lead to human DCM and associated heart failure."

The Hayashi framing (verbatim from PMID:15582318): *"The Z-disc plays a role in establishing the mechanical coupling of sarcomeric contraction and stretching, with the titin/Tcap/MLP complex serving as a mechanical stretch sensor. Tcap interacts with the calsarcin, which tethers the calcineurin to the Z-disc."*

**Calcineurin–NFAT is therefore the named signaling route to hypertrophy** in the CMH25 hypothesis — via calsarcin-1/MYOZ2 anchoring calcineurin at the Z-disc. Suggested GO term: `GO:0033173` calcineurin-NFAT signaling cascade (OAK-verified).

MLP/telethonin interaction was independently confirmed by Vafiadaki et al. 2014 (PMID:24860983), cited by ClinGen as part of the *experimental* (non-genetic) evidence: *"In differentiated striated muscles, MLP-b localizes to the sarcomeres and binds directly to Z-disc components, including α-actinin, T-cap and MLP."*

### 6.3 T-Tubule Structure and Excitation–Contraction Coupling (downstream node)

**Ibrahim et al. 2013, *Hum Mol Genet* (PMID:23100327) — verbatim:**
> "Telethonin (Tcap) is a stretch-sensitive Z-disc protein that binds to proteins in the t-tubule membrane."

> "In cardiomyocytes from 3-month-old KO (3mKO), there were isolated t-tubule defects and Ca(2+) transient dysynchrony without whole heart and cellular dysfunction. Ca(2+) spark frequency more than doubled in 3mKO. At 8 months of age (8mKO), cardiomyocytes showed progressive loss of t-tubules and remodelling of the cell surface, with prolonged and dysynchronous Ca(2+) transients."

> "Mechanical overload increased the Ca(2+) spark frequency in KO alone, where there was also significantly more t-tubule loss, with a greater deterioration in t-tubule regularity."

> "These data suggest that Tcap is a critical, load-sensitive regulator of t-tubule structure and function."

This defines an **age-dependent, load-dependent, progressive** cellular phenotype — biologically attractive for a late-onset adult cardiomyopathy, but again derived from loss of function.

### 6.4 Mechanoptosis — Nuclear p53 Turnover

**Knöll et al. 2011, *Circ Res* (PMID:21799151) — verbatim:**
> "By using a variety of different genetically altered animal models and biophysical experiments we show that contrary to previous views, telethonin is not an indispensable component of the titin-anchoring system, nor is deletion of the gene or cardiac specific overexpression associated with a spontaneous cardiac phenotype. Rather, additional titin-anchorage sites, such as actin-titin cross-links via α-actinin, are sufficient to maintain Z-disk stability despite the loss of telethonin."

> "We demonstrate that a main novel function of telethonin is to modulate the turnover of the proapoptotic tumor suppressor p53 after biomechanical stress in the nuclear compartment, thus linking telethonin, a protein well known to be present at the Z-disk, directly to apoptosis ('mechanoptosis')."

> "In addition, loss of telethonin mRNA and nuclear accumulation of this protein is associated with human heart failure, an effect that may contribute to enhanced rates of apoptosis found in these hearts."

**This paper is doubly important for curation:** it supplies the apoptosis mechanism *and* it explicitly refutes the earlier structural dogma — telethonin is **dispensable** for titin anchoring, because α-actinin provides redundancy. That redundancy is itself an argument for why heterozygous TCAP missense variants may be phenotypically tolerated, and thus part of why the gene–disease relationship is disputed.

### 6.5 Human Cellular Model — iPSC-Cardiomyocytes

Handoh et al. 2025, *Juntendo Medical Journal* 71(4), DOI 10.14789/ejmj.JMJ24-0025-OA (PMC12441175; **no PMID assigned — cite by DOI/PMCID**): CRISPR-Cas9 TCAP knockdown in human iPSC-derived cardiomyocytes produced significantly decreased contraction velocity, relaxation velocity, and contraction–relaxation duration, plus **aberrant Ca²⁺ waves and triggered activity**. The authors interpret the result as **DCM-like**, not HCM-like — another datapoint arguing that TCAP loss of function maps to dilated, not hypertrophic, physiology.

### 6.6 Protein Dysfunction Summary

| Mechanism class | Applies to CMH25? | Evidence |
|---|---|---|
| Gain of interaction / altered binding affinity | **Proposed** | PMID:15582318 (Y2H + GST pull-down; disputed by ClinGen) |
| Loss of function (haploinsufficiency) | Not the CMH25 model | Biallelic LOF → LGMD R7 (PMID:10655062) |
| Dominant negative | Speculative; the one heterozygous frameshift (p.Glu12fs, PMID:40330574) could act this way | n=1 |
| Misfolding / aggregation | No evidence | — |
| Truncated-protein incorporation | Documented in LGMD R7 | PMID:25724973: *"mutant telethonin can be incorporated into the sarcomere"* |

### 6.7 Metabolic, Immune, and Tissue-Damage Mechanisms

- **Metabolic:** No TCAP-specific metabolic defect. HCM-generic energetic-deficiency models (impaired myocardial energetics, reduced PCr/ATP) apply at the parent level and are the rationale for myosin inhibition (mavacamten "restores myocardial energetics").
- **Immune:** **No immune involvement.** CMH25 is neither autoimmune nor inflammatory.
- **Tissue damage:** Cardiomyocyte apoptosis (`GO:0006915`, PMID:21799151); interstitial and replacement **myocardial fibrosis** (`HP:0001685`; histologically confirmed in the RP-HCM case, PMID:40330574); microvascular ischemia and myocyte disarray are HCM-generic.

### 6.8 Molecular Profiling

- **Transcriptomics:** No CMH25-specific dataset. TCAP expression is heart- and skeletal-muscle-restricted and among the most abundant muscle transcripts (PMID:9350988); quantified in GTEx, Fagerberg et al. 2014 (PMID:24309898) and Uhlén et al. 2015 (PMID:25613900) — the latter two cited by ClinGen as the *expression* evidence in the (insufficient) TCAP–HCM case. **Loss of telethonin mRNA** is reported in human heart failure (PMID:21799151).
- **Proteomics:** Telethonin phospho-proteomics in cardiac myocytes (PMID:24280220). No CMH25 patient proteomic study.
- **Metabolomics / lipidomics:** None.
- **Single-cell / spatial transcriptomics:** No TCAP-cardiomyopathy-specific study. The Human Cell Atlas adult heart atlases contain telethonin expression by cardiomyocyte subtype, but no disease contrast.
- **Functional genomics screens:** No CRISPR/RNAi screen implicates TCAP in a cardiomyopathy-relevant phenotype; DepMap is uninformative (muscle-restricted, non-essential in cancer lines).

### 6.9 Suggested Ontology Terms (all OAK-verified in this session)

**Biological processes (GO):**
| GO ID | Label | Role in the chain |
|---|---|---|
| `GO:0055003` | cardiac myofibril assembly | Telethonin's core assembly function |
| `GO:0071260` | cellular response to mechanical stimulus | Mechanosensing node |
| `GO:0060048` | cardiac muscle contraction | Contractile output |
| `GO:0006936` | muscle contraction | — |
| `GO:0033173` | calcineurin-NFAT signaling cascade | Calsarcin-1/calcineurin hypertrophy route |
| `GO:0072331` | signal transduction by p53 class mediator | "Mechanoptosis" arm |
| `GO:0006915` | apoptotic process | Cardiomyocyte loss |
| `GO:0070296` | sarcoplasmic reticulum calcium ion transport | Ca²⁺ handling defect |
| `GO:0055010` | ventricular cardiac muscle tissue morphogenesis | Remodeling |

**Cellular components (GO):** `GO:0030018` Z disc · `GO:0030315` T-tubule · `GO:0030017` sarcomere · `GO:0005634` nucleus (p53 arm) · `GO:0031430` M band (context)

**Cell types (CL):** `CL:0000746` cardiac muscle cell · `CL:0002131` regular ventricular cardiac myocyte · `CL:0008002` skeletal muscle fiber (LGMD arm)

---

## 7. Anatomical Structures Affected

### 7.1 Organ Level
- **Primary:** heart (`UBERON:0000948`) — specifically the **left ventricle** (`UBERON:0002084`) and **interventricular septum** (`UBERON:0002094`), the classic site of asymmetric hypertrophy.
- **Secondary:** left atrium (dilation from chronic diastolic dysfunction; **biatrial enlargement** documented in the RP-HCM case); pulmonary circulation (post-capillary pulmonary hypertension); systemic circulation (thromboembolism secondary to atrial fibrillation).
- **Body system:** cardiovascular. (Skeletal muscle involvement belongs to LGMD R7, *not* CMH25.)

### 7.2 Tissue and Cell Level
- **Tissue:** myocardium (`UBERON:0002349`); cardiac muscle tissue (`UBERON:0001133`); cardiac interstitium (fibrotic remodeling).
- **Cells:** cardiac muscle cell (`CL:0000746`); regular ventricular cardiac myocyte (`CL:0002131`). Cardiac fibroblasts participate in the fibrotic response secondarily.
- Skeletal muscle organ (`UBERON:0001630`) and skeletal muscle fiber (`CL:0008002`) — for the *TCAP gene-level* entry, not CMH25.

### 7.3 Subcellular Level
- **Sarcomeric Z-disc** (`GO:0030018`) — the primary lesion site.
- **Transverse tubule** (`GO:0030315`) — secondary structural target (PMID:23100327, PMID:24280220).
- **Sarcomere** (`GO:0030017`), **nucleus** (`GO:0005634`, p53/mechanoptosis compartment), sarcoplasmic reticulum (Ca²⁺ handling).

### 7.4 Localization and Lateralization
Bilateral in the sense of biventricular myocardial expression, but the phenotype is characteristically **asymmetric** — septal-predominant, left-ventricular-predominant hypertrophy (`HP:0001670` Asymmetric septal hypertrophy). The Toste family showed "moderate asymmetric left ventricular hypertrophy"; the Hu case showed non-obstructive HCM with normal chamber size. Right ventricular involvement is uncommon and not reported in CMH25.

---

## 8. Temporal Development

### 8.1 Onset
- **HPO-annotated onset: `HP:0003581` Adult onset (2/2 probands).**
- Toste family: explicitly *"late-onset HCM"* (PMID:32565061).
- Hu case: symptomatic at **47 years** (PMID:40330574).
- **Onset pattern:** insidious/chronic. No congenital or pediatric CMH25 presentation is reported. (Contrast: LGMD R7 typically presents in the 2nd–3rd decade; mean onset 16 ± 1.41 y in a Chinese series, PMID:32005491.)

### 8.2 Progression

Both trajectories reported in the literature, from an evidence base of essentially three families:

| Trajectory | Description | Source |
|---|---|---|
| **Indolent** | Late-onset, moderate LVH, AF, HFpEF, **low SCD risk**; stable functional status | Toste 2020, PMID:32565061 |
| **Aggressive** | Restrictive physiology, severe diastolic dysfunction, progression to transplant listing **within 1 year** of presentation | Hu 2025, PMID:40330574 |
| **Myofilament-like** | Severity mirroring myofilament-positive HCM, i.e., more severe than genotype-negative HCM | Bos 2006, PMID:16352453 |

- **Stages:** HCM-generic — (i) subclinical/genotype-positive-phenotype-negative; (ii) established LVH with preserved systolic function; (iii) HFpEF ± AF ± obstruction; (iv) end-stage "burnt-out" HCM with systolic dysfunction and LV dilation (`HP:0001644`).
- **Rate:** variable; typically slow over decades.
- **Course pattern:** progressive, punctuated by episodic events (syncope, arrhythmia).
- **Duration:** chronic, lifelong.

### 8.3 Patterns
- **Remission:** none spontaneous. Symptomatic and hemodynamic improvement is treatment-induced (myectomy/ablation/mavacamten for obstruction). Structural hypertrophy is not reversed.
- **Critical periods:** adolescence through early adulthood for phenotype emergence in sarcomeric HCM generally — but CMH25's annotated onset is adult, so serial imaging surveillance of at-risk relatives extends well into adult life. The 2024 AHA/ACC guideline (PMID:38718139) frames the surveillance schedule.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**No prevalence or incidence estimate exists for CMH25 specifically.** Figures below are for HCM as a whole and for TCAP's share of HCM cohorts.

- **HCM overall prevalence:** ~1 in 500 clinically diagnosed; revised upward to approximately **1 in 200** when subclinical/genotype-positive individuals are counted (Semsarian et al. 2015, *JACC* 65:1249–1254, PMID:25814232).
- **TCAP variant yield in HCM cohorts:**

| Cohort | n | TCAP variants found | Rate | Source |
|---|---|---|---|---|
| Japanese/Korean HCM | 346 | 2 (T137I, R153H) | **0.58%** | PMID:15582318 |
| Mayo Clinic HCM (US) | 389 | 4 | **1.03%** | PMID:16352453 |
| Danish HCM | 90 index | (TCAP in panel; contributory variant co-occurring with pathogenic TNNI3) | — | PMID:19035361 |
| Iranian HCM+DCM | 40 | 0 pathogenic (1 intronic polymorphism, c.111-42G>A) | **0%** | PMID:37752589 |

Bos 2006 verbatim: *"Overall, 16 patients (4.1%) harbored a Z-disc mutation: 12 had a MLP mutation and 4 patients a TCAP mutation. No TTN mutations were detected."* and *"Approximately 4.1% of unrelated patients had HCM-associated MLP or TCAP mutations."*

Alaei 2023 verbatim conclusion: *"These findings suggest that the TCAP gene pathogenic mutations might not be a common cause of cardiomyopathies among Iranian patients."*

> Because the underlying gene–disease relationship is disputed, the **defensible prevalence statement for a dismech `Prevalence` record is `prevalence_class: UNKNOWN` with `measure_type: UNKNOWN`**, and a `notes` field capturing the ~0.6–1% cohort variant-detection rate with the caveat that these are variant-detection rates, not attributable-cause rates.

### 9.2 Inheritance

- **Pattern:** **Autosomal dominant** (`HP:0000006`; OMIM; ClinGen MOI field records **AD**). Contrast with **autosomal recessive** for LGMD R7 — the same gene, two inheritance modes, a point of real clinical confusion.
- **Penetrance:** Unknown and unmeasurable from the available pedigrees. Toste 2020 reported *"a co-segregation pattern was detected"* in a two-affected-member family — the strongest segregation evidence available for any TCAP-HCM allele, and it is very weak (a 2-informative-meiosis family cannot generate meaningful LOD). Given adult onset, penetrance would at minimum be **age-dependent**.
- **Expressivity:** Apparently **variable** — indolent HFpEF (Toste) versus restrictive/transplant-bound (Hu). With n≈8 probands total, "variable expressivity" is more accurately described as "unconstrained by data."
- **Genetic anticipation:** **Not applicable** (no repeat expansion).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None described for TCAP-HCM alleles. (A founder effect *is* relevant to LGMD R7 in the **Brazilian** population, where the disorder was originally mapped — PMID:10655062 — and where most reported cases have historically come from; PMID:34982307 notes reported cases *"mostly include patients from Brazil."*)
- **Consanguinity:** Relevant to **LGMD R7** (recessive), not to CMH25 (dominant).
- **Carrier frequency:** Not meaningful for a dominant condition. For LGMD R7, TCAP LOF allele frequency in gnomAD is on the order of 10⁻⁵ (e.g., Q53X ≈ 1×10⁻⁵).

### 9.3 Population Demographics

- **Affected populations:** Reported probands are **Japanese** (Hayashi 2004), **North American/predominantly white** (Bos 2006), **Danish** (Andersen 2009), **Portuguese** (Toste 2020), and **Chinese** (Hu 2025). No population enrichment is established. The gnomAD distribution of R87Q is essentially pan-ancestry at ~10⁻⁵ (nfe 1.44×10⁻⁵, sas 1.16×10⁻⁵, eas 2.52×10⁻⁵, afr 2.99×10⁻⁵) — i.e., no ancestral clustering.
- **Geographic distribution:** Global, sporadic case reports; no endemic focus.
- **Sex ratio:** No CMH25-specific ratio. HCM cohorts show male predominance (Bos 2006: 215/389 = 55% male). The single RP-HCM case was male; the Toste family included both sexes.
- **Age distribution:** Adult, with reported presentation in the 5th decade.

---

## 10. Diagnostics

### 10.1 Clinical Tests

| Modality | Findings in CMH25 | Suggested term |
|---|---|---|
| **Echocardiography** | LVH, asymmetric septal hypertrophy, diastolic dysfunction, LVOT gradient assessment (rest + provocation), atrial size | `NCIT:C16525` Echocardiography Test (OAK-verified) |
| **Cardiac MRI** | Wall-thickness mapping, late gadolinium enhancement for **myocardial fibrosis** (`HP:0001685`); in the RP-HCM case CMR established non-obstructive HCM with severe diastolic dysfunction | CMR — no exact NCIT clinical-action term found in the local NCIT adapter; use `NCIT:C16809` MRI family or free-text `preferred_term` |
| **ECG** | LVH voltage criteria, repolarization abnormality, and notably **Wolff-Parkinson-White pattern** (`HP:0001716`) in 1/2 index probands | `NCIT:C38053` Electrocardiography (OAK-verified) |
| **Ambulatory monitoring** | NSVT detection for SCD risk stratification; AF detection | — |
| **Endomyocardial biopsy** | *"cardiomyocyte hypertrophy and focal fibrosis"* (PMID:40330574) — myocyte disarray and interstitial fibrosis are the HCM-generic histology | — |
| **Exercise testing / CPET** | Functional capacity, provocable obstruction, blood-pressure response (SCD risk marker) | — |
| **Laboratory** | NT-proBNP and hs-troponin as HCM-generic prognostic markers. **Serum CK is normal in CMH25** (unlike LGMD R7, where `HP:0003236` elevated CK is characteristic) — a useful discriminator | LOINC coding available for BNP/CK |

**There is no CMH25-specific biomarker.** No FDA/BEST-listed biomarker exists for TCAP genotype.

### 10.2 Genetic Testing

**Recommended approach — and the crucial caveat:**

TCAP appears on many legacy multigene HCM panels. Because ClinGen classifies TCAP–HCM as **DISPUTED**, **TCAP should not be included on a contemporary diagnostic HCM panel, and TCAP variants should not be reported as diagnostic findings.** Ingles et al. 2019 (PMID:30681346) put this bluntly:

> "Recent trends to increase gene panel sizes often mean variants in genes with questionable association are reported to patients. Classification of HCM genes and variants is critical, as misclassification can lead to genetic misdiagnosis."

> "Of 4191 HCM variants in ClinVar, 31% were in genes with limited or no evidence of disease association."

> "The majority of genes previously reported as causative of HCM and commonly included in diagnostic tests have limited or no evidence of disease association. Systematically curated HCM genes are essential to guide appropriate reporting of variants and ensure the best possible outcomes for HCM families."

| Test | Utility in CMH25 |
|---|---|
| **Targeted HCM gene panel** | Standard of care for HCM; TCAP inclusion is discouraged. Where TCAP is on the panel, expect VUS. |
| **WES** | Used in the RP-HCM case to find p.Glu12fs (PMID:40330574). Appropriate for panel-negative HCM. |
| **WGS** | No specific advantage for a 2-exon gene. |
| **Single-gene TCAP testing** | Appropriate **only** when LGMD R7 is suspected (proximal weakness + hyperCKemia + absent telethonin on IHC), not for isolated HCM. |
| **CMA / karyotype / FISH** | **No role.** |
| **mtDNA testing** | **No role** — but relevant to the *differential* (mitochondrial cardiomyopathy is an HCM phenocopy). |
| **Repeat expansion testing** | **No role** — but Friedreich ataxia (GAA-FXN) is an HCM phenocopy worth excluding in the right clinical context. |

**NCIT term:** `NCIT:C15709` Genetic Testing (OAK-verified).

**Omics diagnostics (RNA-seq, proteomics, metabolomics, epigenomics, liquid biopsy):** **none have an established or investigational diagnostic role in CMH25.** Skeletal-muscle telethonin immunohistochemistry/Western blot is diagnostic for LGMD R7 (absent protein — PMID:34982307, PMID:12379311) but has no cardiac counterpart.

### 10.3 Clinical Criteria

Diagnosis follows the **generic HCM criteria** — LV wall thickness ≥15 mm (or ≥13 mm with family history / positive genotype) not explained by abnormal loading conditions — per the 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM Guideline (PMID:38718139) and the 2023 ESC cardiomyopathy guideline. **There are no CMH25-specific diagnostic criteria.** A "CMH25 diagnosis" is, operationally, HCM-by-standard-criteria plus a TCAP variant — and per ClinGen, the second half of that conjunction does not currently license a causal claim.

### 10.4 Differential Diagnosis

| Alternative | Distinguishing features |
|---|---|
| Sarcomeric HCM (MYBPC3, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, MYL3) | **The 8 definitive genes** — always exclude first; far higher prior probability |
| Cardiac amyloidosis (ATTR/AL) | Low-voltage ECG despite thick walls, apical sparing strain, bone-scintigraphy uptake, monoclonal screen |
| Fabry disease (GLA) | Low native T1 on CMR, α-galactosidase A activity, X-linked, angiokeratoma/acroparesthesia |
| Danon disease (LAMP2), PRKAG2 glycogen storage | **Marked pre-excitation/WPW** — highly relevant here, since WPW (`HP:0001716`) is in the CMH25 HPO set; extreme LVH with conduction disease |
| RASopathies (Noonan/PTPN11, LEOPARD) | Dysmorphology, pulmonary valve stenosis, short stature |
| Friedreich ataxia (FXN) | Neurological phenotype |
| Mitochondrial cardiomyopathy | Maternal inheritance, multisystem involvement, lactate |
| Hypertensive heart disease / athlete's heart | Load explanation; concentric, regressive with detraining |
| **LGMD R7 (TCAP, recessive)** | Same gene; skeletal-muscle-predominant, elevated CK, biallelic (usually truncating) variants |

The 2024 AHA/ACC guideline explicitly directs that *"HCM genetic testing should include genes for HCM phenocopies."*

### 10.5 Screening

- **Newborn screening:** not applicable.
- **Carrier screening:** not applicable (dominant); relevant only for LGMD R7 in consanguineous families.
- **Cascade screening:** per guideline, *"Cascade genetic testing should be extended to first-degree relatives only if a pathogenic variant is identified in the proband."* **Because essentially all TCAP-HCM variants are VUS or disputed, cascade *genetic* testing on a TCAP variant is not indicated.** First-degree relatives should instead enter **clinical/imaging surveillance** (ECG + echocardiography at guideline intervals). This is arguably the single most consequential practical statement in this report.

---

## 11. Outcome / Prognosis

### 11.1 Survival and Mortality
**No CMH25-specific survival, life-expectancy, or mortality data exist.** No registry, no cohort, no Kaplan–Meier curve. Sample sizes (≤8 probands globally) preclude any survival estimate.

HCM-generic context: contemporary HCM cohorts in expert centers report annual mortality approaching that of the general population (~0.5%/yr), with sudden cardiac death, heart failure, and AF-related stroke as the three modes of disease-related death.

### 11.2 Morbidity and Function
- Heart failure with preserved ejection fraction (both reported CMH25 families).
- Atrial fibrillation with associated thromboembolic risk (Toste family).
- Exertional limitation.
- **No CMH25-specific ICF disability data, EQ-5D, SF-36, PROMIS, or HCMSQ measurements exist.**

### 11.3 Disease Course / Complications
Reported CMH25 complications: atrial fibrillation, HFpEF, severe diastolic dysfunction with biatrial enlargement, myocardial fibrosis, progression to transplant candidacy. HCM-generic complications additionally include LVOT obstruction, ventricular arrhythmia and SCD, infective endocarditis (rare, with obstruction/SAM), and end-stage systolic evolution.

**Recovery potential:** none — the structural phenotype does not remit. Symptomatic and hemodynamic recovery is achievable with obstruction-directed therapy; transplantation is curative of the cardiac phenotype only.

### 11.4 Prognostic Factors and Biomarkers
No CMH25-specific prognostic factor has been validated. The two published families illustrate the extremes and suggest, at most, hypothesis-generating candidates:
- **Restrictive physiology / severe diastolic dysfunction** — associated with the rapidly deteriorating course (PMID:40330574).
- **Truncating vs missense allele class** — the frameshift case was the aggressive one; the missense families were indolent. **n=1 vs n=2; this is a hypothesis, not a genotype–phenotype correlation.**
- HCM-generic SCD-risk factors (family history of SCD, unexplained syncope, massive LVH ≥30 mm, NSVT, abnormal BP response to exercise, apical aneurysm, extensive LGE, low LVEF) and the HCM Risk-SCD calculator apply by parent-class inheritance.
- Toste 2020 explicitly characterized their family as **"low risk of sudden cardiac death."**

---

## 12. Treatment

**There is no CMH25-specific, genotype-directed therapy.** Management is entirely that of hypertrophic cardiomyopathy generally, per the 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR guideline (PMID:38718139). Nothing about a TCAP genotype currently alters management.

### 12.1 Pharmacotherapy

| Treatment | Class / mechanism | Suggested terms (OAK-verified) |
|---|---|---|
| **Beta-blockers** (e.g., metoprolol) | β-adrenergic antagonism → ↓ inotropy/chronotropy, ↑ diastolic filling, ↓ dynamic obstruction. **First line** for symptomatic obstructive HCM | `treatment_term` `NCIT:C15986` Pharmacotherapy; `therapeutic_agent` `NCIT:C29576` Beta-Adrenergic Antagonist and/or `CHEBI:6904` metoprolol; `therapeutic_modality: SMALL_MOLECULE` |
| **Non-dihydropyridine calcium channel blockers** (verapamil) | ↓ contractility, improved diastolic relaxation; alternative when β-blockers are not tolerated | `NCIT:C15986` + `NCIT:C333` Calcium Channel Blocker and/or `CHEBI:9948` verapamil |
| **Disopyramide** | Class IA antiarrhythmic with potent negative inotropy; added for refractory obstruction | `NCIT:C15986` + `CHEBI:4657` disopyramide |
| **Mavacamten** | **First-in-class cardiac myosin inhibitor** — allosteric inhibition of cardiac myosin ATPase, reducing actin–myosin cross-bridge formation and hypercontractility | `NCIT:C15986` + `NCIT:C174901` Mavacamten; `therapeutic_modality: SMALL_MOLECULE`. *(No CHEBI term for mavacamten in the local CHEBI release — use NCIT.)* |
| **Anticoagulation** (DOAC/warfarin) | Stroke prevention in HCM with AF — recommended irrespective of CHA₂DS₂-VASc | `NCIT:C15986` |
| **Diuretics** | Cautious use for congestion in HFpEF; risk of worsening dynamic obstruction | `NCIT:C15986` |
| **Antiarrhythmics** (amiodarone) | AF rhythm control | `NCIT:C15986` + `CHEBI:2663` amiodarone |

**Mavacamten pivotal evidence — EXPLORER-HCM (Olivotto et al., *Lancet* 2020;396:759–769, PMID:32871100):** randomized, double-blind, placebo-controlled phase 3 in 251 patients with symptomatic obstructive HCM over 30 weeks. Primary endpoint met by **45/123 (37%) on mavacamten vs 22/128 (17%) on placebo; difference +19.4% (95% CI 8.7–30.1; p=0.0005)**. Abstract background (verbatim): *"Cardiac muscle hypercontractility is a key pathophysiological abnormality in hypertrophic cardiomyopathy"*; interpretation (verbatim): *"Treatment with mavacamten improved exercise capacity, LVOT obstruction, NYHA functional class, and health status."* Mavacamten requires **REMS-governed echocardiographic monitoring** for LVEF reduction and is contraindicated in significant systolic dysfunction; **CYP2C19 poor-metabolizer status affects exposure** (the one genuinely pharmacogenomic consideration in HCM care — PharmGKB/CPIC-relevant, and unrelated to TCAP genotype).

**Pharmacogenomics specific to CMH25: none.** No TCAP variant is known to influence drug metabolism, efficacy, or toxicity.

### 12.2 Advanced Therapeutics
- **Gene therapy:** No TCAP-directed program. AAV9-*MYBPC3* gene replacement is in early clinical development for MYBPC3-HCM (a template that could in principle extend to other genes, but nothing exists for TCAP).
- **Gene editing:** Preclinical base/prime editing work in sarcomeric HCM; **nothing for TCAP**.
- **RNA-based therapies (ASO, siRNA, mRNA):** **None for TCAP.** No conformance to the `antisense_oligonucleotide_therapy` module.
- **Cell therapy, immunotherapy:** Not applicable.
- **Targeted therapy:** Mavacamten and the next-generation myosin inhibitor **aficamten** are "targeted" at the sarcomere but are genotype-agnostic — they target the pathophysiology, not the gene.

### 12.3 Surgical and Interventional
- **Septal myectomy** (extended Morrow procedure) — gold standard for drug-refractory obstructive HCM in experienced centers. `NCIT:C51591` Myectomy (OAK-verified); `therapeutic_modality: SURGERY`.
- **Alcohol septal ablation** — percutaneous alternative in selected anatomy/comorbidity; observational data suggest similar safety and efficacy to myectomy.
- **ICD implantation** — for primary or secondary SCD prevention per risk stratification. `NCIT:C80435` Implantable Cardioverter-Defibrillator Placement; device `NCIT:C93238` Implantable Cardioverter-Defibrillator (both OAK-verified); `therapeutic_modality: DEVICE`.
- **Heart transplantation** — for end-stage disease. `NCIT:C15246` Heart Transplantation (OAK-verified); `therapeutic_modality: SURGERY`. **This is the documented endpoint in the one reported RP-HCM CMH25 case** (PMID:40330574).
- **AF ablation / left atrial appendage occlusion** — as indicated.

### 12.4 Supportive, Rehabilitative, Counseling
- Supportive care: `NCIT:C15747` Supportive Care (OAK-verified) — symptom management, volume management, HF care.
- **Genetic counseling:** `NCIT:C15240` Genetic Counseling (OAK-verified); `therapeutic_modality: BEHAVIORAL`. **Central to CMH25 management, and unusually delicate**: the counselor's job here is largely to explain why a TCAP variant does *not* establish a diagnosis, why cascade testing on it is not indicated, and why relatives need clinical surveillance regardless. The guideline recommends *"evaluation by a genetic counselor... to discuss risk and benefits of genetic testing."*
- **Exercise counseling:** contemporary guidelines permit mild-to-moderate recreational exercise; competitive high-intensity athletics require shared decision-making.
- Cardiac rehabilitation: increasingly supported in non-obstructive HCM.

### 12.5 Experimental Treatments
No trial has ever enrolled by TCAP genotype. Relevant HCM-wide programs: **aficamten** (SEQUOIA-HCM and successors), **ninerafaxstat** (cardiac mitotrope, non-obstructive HCM), MYBPC3 gene therapy. **A curator should not attach any NCT identifier to CMH25** — none is CMH25-specific, and asserting one would misrepresent the evidence.

### 12.6 Treatment Outcomes and Strategy
- Response rates and adverse events: available only at the HCM parent level (see EXPLORER-HCM numbers above; mavacamten's key adverse event is asymptomatic LVEF reduction).
- **Treatment algorithm:** obstructive symptomatic HCM → β-blocker → verapamil (if intolerant) → add disopyramide *or* mavacamten → septal reduction therapy if refractory. Non-obstructive HCM → symptom-directed HF therapy; consider transplant evaluation for advanced disease. Parallel track: SCD risk stratification → ICD decision. Parallel track: family screening.
- **Personalized medicine:** genotype currently informs **family screening**, not drug selection, in HCM. For TCAP specifically, genotype informs **neither**.

---

## 13. Prevention

### 13.1 Primary Prevention
**Not achievable** — CMH25 is a germline monogenic (putatively) condition. The only primary-prevention options operate at the reproductive level: preimplantation genetic testing (PGT-M) and prenatal diagnosis. **Both are inappropriate for a disputed gene–disease relationship with VUS-level alleles**, and should not be offered on the basis of a TCAP variant. This is a clinically important negative recommendation.

### 13.2 Secondary Prevention
- **Family clinical surveillance** is the mainstay: ECG + echocardiography in first-degree relatives at guideline-specified intervals, continued into adult life given CMH25's adult onset. This applies **irrespective of TCAP genotype**, precisely because the genotype is uninformative.
- Early detection of AF (ambulatory/wearable monitoring) to enable timely anticoagulation.
- Serial SCD risk restratification.

### 13.3 Tertiary Prevention
- ICD for SCD prevention in risk-stratified patients.
- Anticoagulation for AF-related stroke prevention.
- Heart-failure guideline-directed therapy and timely transplant referral.
- Endocarditis awareness in obstructive disease with mitral involvement.

### 13.4 Immunization
**Not applicable** as disease prevention. Routine influenza/COVID-19/pneumococcal vaccination is standard supportive care in chronic heart disease.

### 13.5 Screening, Risk Stratification, Counseling
- **Population screening:** none.
- **Genetic screening:** cascade testing **not indicated** on a TCAP VUS (see §10.5).
- **Risk stratification:** HCM Risk-SCD and guideline risk markers apply generically.
- **Counseling:** should explicitly convey the **DISPUTED** ClinGen classification, the VUS status of essentially all TCAP-HCM alleles, and that surveillance — not genotype — governs family management.

### 13.6 Public Health / Environmental Interventions / Prophylaxis
No public-health or environmental intervention is relevant. No prophylactic medication prevents phenotype development in genotype-positive individuals — a long-standing unmet need in HCM generally (prior trials of diltiazem and losartan in preclinical sarcomeric HCM were not practice-changing).

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and Orthologs

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | TCAP, NCBI Gene 8557, 17q12 | — |
| *Mus musculus* | `NCBITaxon:10090` | **Tcap**, **MGI:1330233**, chromosome 11 | Principal model; KO lines available |
| *Rattus norvegicus* | `NCBITaxon:10116` | Tcap | Used for cardiomyocyte phosphoregulation work (PMID:24280220) |
| *Danio rerio* | `NCBITaxon:7955` | tcap | Telethonin orthologs studied in sarcomere assembly |
| *Xenopus laevis* | `NCBITaxon:8355` | tcap | Morpholino knockdown model (PMID:20235223) |
| *Canis lupus familiaris* | `NCBITaxon:9615` | TCAP | See below |

### 14.2 Naturally Occurring Disease in Other Species

The single relevant veterinary study is a **negative** one, and is worth curating as such:

**Philipp U, Vollmar A, Distl O. "Evaluation of the titin-cap gene (TCAP) as candidate for dilated cardiomyopathy in Irish wolfhounds." *Animal Biotechnology* 2008;19:231–236 (PMID:18855248).** Verbatim opening: *"Dilated cardiomyopathy (DCM) is a myocardial disorder characterized by left ventricular dilatation and impaired systolic contraction. Irish wolfhounds (IW) and other large breed dogs are most commonly disposed to DCM."* The study evaluated TCAP as a positional/functional candidate for canine DCM; TCAP was not established as the cause.

- **Breed (VBO):** Irish Wolfhound — a VBO identifier exists for the breed but was **not verified in this session**; look it up before asserting.
- **OMIA:** No OMIA entry for telethonin-related cardiomyopathy was identified. **Unverified — check OMIA directly before asserting absence in a KB entry.**
- **Naturally occurring HCM is common in domestic cats** (*Felis catus*, `NCBITaxon:9685`), where MYBPC3 variants in Maine Coon and Ragdoll breeds are the established genetic causes — **TCAP is not implicated in feline HCM.**

### 14.3 Comparative Biology
- **Evolutionary conservation:** Telethonin is a vertebrate striated-muscle-specific protein, highly conserved across mammals; the Toste variant p.C57W was selected in part because of *"high conservation across species"* (PMID:32565061).
- **Comparative pathology divergence — important:** mouse Tcap knockout produces **no spontaneous cardiac phenotype** (PMID:21799151), whereas human biallelic TCAP loss produces **skeletal muscular dystrophy (LGMD R7)** with only inconsistent cardiac involvement, and human heterozygous missense variants are *claimed* to produce hypertrophic cardiomyopathy. **These three do not line up.** The divergence is itself evidence for the disputed status of CMH25 and should be curated as a `HUMAN_MODEL_MISMATCH` discussion.

### 14.4 Transmission
**Not applicable** — no zoonotic potential, no cross-species transmission. CMH25 is a germline genetic condition.

---

## 15. Model Organisms

### 15.1 Available Models

| Model | Type | Key findings | Reference |
|---|---|---|---|
| **Tcap knockout mouse** (MGI:1330233) | Mammalian, germline KO | **No baseline cardiac phenotype**; heart failure only after biomechanical stress; cardiomyocyte apoptosis; nuclear p53 turnover defect ("mechanoptosis") | Knöll et al. 2011, PMID:21799151 |
| **Tcap KO mouse, aged / pressure-overloaded** | Mammalian, KO + aortic banding | 3-month KO: isolated t-tubule defects, Ca²⁺ transient dyssynchrony, **>2× Ca²⁺ spark frequency**, no whole-heart dysfunction. 8-month KO: progressive t-tubule loss, cell-surface remodeling, depressed L-type Ca²⁺ current. Overload: greater t-tubule loss and severe loss of cell-surface ultrastructure in KO | Ibrahim et al. 2013, PMID:23100327 |
| **Cardiac-specific Tcap overexpression mouse** | Mammalian, transgenic | **No spontaneous cardiac phenotype** | Knöll et al. 2011, PMID:21799151 |
| **Adult rat ventricular myocytes + adenoviral S157A/S161A telethonin** | In vitro, mammalian primary cells | Non-phosphorylatable telethonin **disrupted transverse tubule organization and prolonged the time to peak of the intracellular Ca²⁺ transient and increased its variance** | Candasamy et al. 2014, PMID:24280220 |
| **Human iPSC-CM, CRISPR-Cas9 TCAP knockdown** | Human cellular | Significantly decreased contraction velocity, relaxation velocity, contraction–relaxation duration; **aberrant Ca²⁺ waves and triggered activity**; authors interpret as **DCM-like** | Handoh et al. 2025, *Juntendo Med J* 71(4), DOI 10.14789/ejmj.JMJ24-0025-OA, PMC12441175 |
| ***Xenopus* telethonin morpholino knockdown** | Invertebrate-adjacent / amphibian embryo | Telethonin reduction *"leads to embryonic paralysis, myocyte defects, and sarcomeric disruption"*; full-length mRNA rescues, C-terminally truncated constructs do not; *"the telethonin C-terminus is required for assembly, but in a context-dependent manner"* | Sadikot et al. 2010, *Dev Dyn* 239:1124–1135, PMID:20235223 |
| **Yeast two-hybrid / GST pull-down** | In vitro biochemical | The original CMH25 functional claim: HCM variants augment titin/calsarcin-1 binding | Hayashi et al. 2004, PMID:15582318 |

### 15.2 Genetic Model Types Available
Constitutive knockout and cardiac-specific transgenic overexpression are documented. **No knock-in mouse carrying the human CMH25 alleles (T137I, R153H, C57W, or p.Glu12fs) has been reported.** No conditional/inducible or humanized TCAP line is described in the literature reviewed. IMPC/KOMP/IMSR should be queried directly for current allele availability (**not verified in this session**).

### 15.3 Phenotype Recapitulation and Limitations

**This is the crux, and it should be stated plainly in any KB entry:**

| Human CMH25 feature | Recapitulated in models? |
|---|---|
| Left ventricular hypertrophy | **No.** Tcap KO mice show no spontaneous hypertrophy; cardiac overexpression likewise produces no phenotype |
| Asymmetric septal hypertrophy | **No** |
| Adult-onset progressive course | **Partially** — age-dependent t-tubule deterioration in KO mice (3mo → 8mo) |
| Diastolic dysfunction | **Partially/indirectly** — prolonged, dyssynchronous Ca²⁺ transients |
| Load-dependent decompensation | **Yes** — the strongest recapitulation, in Tcap KO + aortic banding |
| Cardiomyocyte apoptosis / fibrosis | **Yes** (apoptosis, KO after stress) |
| **The actual human allele class (heterozygous missense, gain-of-interaction)** | **NOT MODELED AT ALL** |

**Limitations to record explicitly:**
1. **Allele-class mismatch.** Every animal model is a *loss-of-function* model; the human CMH25 hypothesis is *gain of interaction* in the heterozygous state. The models therefore cannot test the disease hypothesis — a textbook `kind: HUMAN_MODEL_MISMATCH` situation for dismech, not a generic `KNOWLEDGE_GAP`.
2. **Direction-of-phenotype mismatch.** Where TCAP perturbation does produce a cardiac phenotype (iPSC-CM knockdown; Tcap KO under stress), the phenotype is **dilated/hypocontractile**, not hypertrophic.
3. **Structural redundancy.** Knöll 2011 showed α-actinin-mediated actin–titin cross-links maintain Z-disc stability without telethonin — a built-in buffer that argues against strong dominant effects from a single missense allele.
4. No model addresses the WPW/pre-excitation component of the human annotation.

### 15.4 Research Applications
Existing models are well suited to studying: Z-disc mechanosensing and load transduction; t-tubule biogenesis, maintenance, and CICR; stretch-induced apoptosis and nuclear p53 handling; telethonin phosphoregulation by PKD/CaMKII; and sarcomere assembly (Xenopus). They are **not** suited to validating CMH25 causality.

**The single highest-value experiment for resolving the CMH25 dispute** would be a **heterozygous knock-in mouse (or isogenic iPSC-CM line) carrying human T137I or R153H**, characterized for hypertrophy at baseline and under pressure overload, with quantitative titin/calsarcin-1 binding measured in situ. Curate this as a `proposed_experiments` entry attached to the knowledge-gap discussion.

### 15.5 Model Resources
MGI (`MGI:1330233`), IMPC, IMSR, KOMP/EuMMCR (allele availability **not verified in this session**), ZFIN, Xenbase, Alliance of Genome Resources, Cellosaurus (for iPSC lines).

---

## Recommended dismech Curation Decisions

1. **Do not curate CMH25 as an established causal mechanism.** Model the pathophysiology chain under `mechanistic_hypotheses` with `status: EMERGING`, and have the causal edges opt in via `hypothesis_groups`.
2. **Add a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH`** (not `KNOWLEDGE_GAP`) attached to the "Telethonin Z-Disc Dysfunction" node: evidence exists abundantly in mouse KO, rat myocytes, and human iPSC-CM, but every model tests loss of function while the human hypothesis is heterozygous gain-of-interaction — and the models' cardiac phenotype, when present, is dilated rather than hypertrophic. Include `proposed_experiments` (heterozygous T137I/R153H knock-in).
3. **Cite the ClinGen DISPUTED assertion as first-class evidence** using the cache file already in the worktree: `reference: CGGV:assertion_c35abc20-c04c-49ec-af02-1bd270b0b50b-2022-09-14T160000.000Z`, `supports: REFUTE`, `evidence_source: OTHER`, with a quotable row such as `"TCAP | HGNC:11610 | hypertrophic cardiomyopathy | MONDO:0005045 | AD | Disputed | SOP9 | Hereditary Cardiovascular Disease Gene Curation Expert Panel | 2022-09-14T16:00:00.000Z"`.
4. **Omit `frequency:` on all phenotypes** — the HPO denominators are 2/2 and 1/2 from a single paper. Put "2/2 probands, PMID:15582318" in `notes`.
5. **Genetic block:** consider `relationship_type: SUSCEPTIBILITY` or `MODIFIER` rather than a plain causal gene assertion, and record the two documented co-occurring variants (pathogenic TNNI3, MYBPC3 VUS) as the reason.
6. **Prevalence:** `measure_type: UNKNOWN`, `prevalence_class: UNKNOWN`, with the 0.58%/1.03%/0% cohort detection rates in `notes` — these are variant-detection rates, not attributable-cause rates.
7. **Do not attach clinical trials.** No NCT is CMH25-specific.
8. **Consider `conforms_to: cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling`** for the downstream tissue-level node; the electrical module (`cardiac_ion_channel_repolarization`) does **not** apply — CMH25 is structural, and the WPW annotation is a single-proband observation, not a channelopathy.
9. **Every PMID cited here must still be run through `just fetch-reference` and `just validate-references`** before committing. Abstract text in this report was retrieved verbatim from the Europe PMC REST API; the OMIM entries (607487, 604488) returned **HTTP 403** and were **not** read directly — OMIM-attributed content here comes via MONDO, MedGen, HPO, UniProt, and search summaries, so **do not quote OMIM text as a verified snippet without fetching it.**

---

## Sources

- [Tcap gene mutations in hypertrophic cardiomyopathy and dilated cardiomyopathy — PubMed (PMID:15582318)](https://pubmed.ncbi.nlm.nih.gov/15582318/)
- [Genotype-phenotype relationships involving HCM-associated mutations in titin, MLP, and telethonin (PMID:16352453)](https://europepmc.org/article/MED/16352453)
- [Diagnostic yield... sarcomere encoding genes in Danish HCM patients (PMID:19035361)](https://europepmc.org/article/MED/19035361)
- [Identification of a novel titin-cap/telethonin mutation in a Portuguese family with HCM (PMID:32565061)](https://europepmc.org/article/MED/32565061)
- [The challenge of assessing variant pathogenicity in candidate Z-disc genes: the example of TCAP in HCM (PMID:32654878)](https://europepmc.org/article/MED/32654878)
- [Mutations in the TCAP gene may lead to restrictive phenotype HCM with poor prognosis (PMID:40330574)](https://academic.oup.com/ehjcr/article/9/5/ytaf180/8109734)
- [TCAP gene is not a common cause of cardiomyopathy in Iranian patients (PMID:37752589)](https://link.springer.com/content/pdf/10.1186/s40001-023-01019-4.pdf)
- [Telethonin deficiency is associated with maladaptation to biomechanical stress in the mammalian heart (PMID:21799151)](https://www.ahajournals.org/doi/10.1161/CIRCRESAHA.111.245787)
- [The cardiac mechanical stretch sensor machinery involves a Z disc complex... (PMID:12507422)](https://europepmc.org/article/MED/12507422)
- [Telethonin, a novel sarcomeric protein of heart and skeletal muscle (PMID:9350988)](https://europepmc.org/article/MED/9350988)
- [Palindromic assembly of the giant muscle protein titin in the sarcomeric Z-disk (PMID:16407954)](https://europepmc.org/article/MED/16407954)
- [Phosphoregulation of the titin-cap protein telethonin in cardiac myocytes (PMID:24280220)](https://pubmed.ncbi.nlm.nih.gov/24280220/)
- [A critical role for Telethonin in regulating t-tubule structure and function in the mammalian heart (PMID:23100327)](https://ncbi.nlm.nih.gov/pmc/articles/PMC3526164)
- [Muscle lim protein isoform negatively regulates striated muscle actin dynamics and differentiation (PMID:24860983)](https://europepmc.org/article/MED/24860983)
- [Limb-girdle muscular dystrophy type 2G is caused by mutations in the gene encoding telethonin (PMID:10655062)](https://europepmc.org/article/MED/10655062)
- [Evaluating the Clinical Validity of Hypertrophic Cardiomyopathy Genes (PMID:30681346)](https://europepmc.org/article/MED/30681346)
- [Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples (PMID:27532257)](https://europepmc.org/article/MED/27532257)
- [New perspectives on the prevalence of hypertrophic cardiomyopathy (PMID:25814232)](https://pubmed.ncbi.nlm.nih.gov/25814232/)
- [2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM Guideline (PMID:38718139)](https://pubmed.ncbi.nlm.nih.gov/38718139/)
- [Mavacamten for treatment of symptomatic obstructive HCM (EXPLORER-HCM) (PMID:32871100)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)31792-X/fulltext)
- [Structural and signaling proteins in the Z-disk and their role in cardiomyopathies (PMID:36935760)](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1143858/full)
- [Distinct roles for telethonin N- versus C-terminus in sarcomere assembly and maintenance (PMID:20235223)](https://pubmed.ncbi.nlm.nih.gov/20235223/)
- [Knockdown of Telethonin Reduces Contractions and Provokes Aberrant Ca2+-waves in Human iPS Cell-induced Cardiomyocytes (PMC12441175)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12441175/)
- [Two distinct phenotypes and a novel mutation in LGMD R7 telethonin-related patients, Thailand (PMID:40195250)](https://europepmc.org/article/MED/40195250)
- [Southeast Asian cohort of LGMD2G/LGMD-R7-telethonin-related (PMID:36463458)](https://europepmc.org/article/MED/36463458)
- [LGMD R7 telethonin-related patients from a Chinese neuromuscular center (PMID:34982307)](https://europepmc.org/article/MED/34982307)
- [Clinical and genetic characterization of LGMD R7 from three unrelated Chinese families (PMID:32005491)](https://europepmc.org/article/MED/32005491)
- [Conserved expression of truncated telethonin in a patient with LGMD 2G (PMID:25724973)](https://europepmc.org/article/MED/25724973)
- [Telethonin protein expression in neuromuscular disorders (PMID:12379311)](https://europepmc.org/article/MED/12379311)
- [Evaluation of the titin-cap gene (TCAP) as candidate for DCM in Irish wolfhounds (PMID:18855248)](https://europepmc.org/article/MED/18855248)
- [OMIM #607487 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 25 (HTTP 403 on direct fetch)](https://omim.org/entry/607487)
- [OMIM *604488 — TITIN-CAP; TCAP (HTTP 403 on direct fetch)](https://omim.org/entry/604488)
- [MedGen — Hypertrophic cardiomyopathy 25 (C4225408)](https://www.ncbi.nlm.nih.gov/medgen/?term=hypertrophic+cardiomyopathy+25)
- [ClinVar — TCAP variants (NCBI E-utilities esummary)](https://www.ncbi.nlm.nih.gov/clinvar/variation/12456/)
- [HPO annotations for OMIM:607487 (JAX ontology API)](https://ontology.jax.org/api/network/annotation/OMIM:607487)
- [UniProt O15273 — Telethonin](https://rest.uniprot.org/uniprotkb/O15273.json)
- [Ensembl REST — rs121434298 population frequencies](https://rest.ensembl.org/variation/human/rs121434298?content-type=application/json;pops=1)
- [MGI — Tcap (MGI:1330233)](https://www.informatics.jax.org/marker/MGI:1330233)
- [Orphanet — Familial isolated hypertrophic cardiomyopathy (ORPHA:155)](https://www.orpha.net/en/disease/detail/155)
- [ClinGen Gene-Disease Validity — TCAP / hypertrophic cardiomyopathy (Disputed)](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_c35abc20-c04c-49ec-af02-1bd270b0b50b-2022-09-14T160000.000Z)