---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T20:08:22.222239'
end_time: '2026-08-19T20:12:56.614982'
duration_seconds: 274.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PACS2-Related Developmental and Epileptic Encephalopathy
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 12
  num_turns: 27
  total_cost_usd: 1.8559034000000003
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 22
reference_validation:
  total_references: 12
  verified: 10
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.167
  relevance_assessed: 10
  on_topic: 5
  off_topic: 2
  off_topic_references:
  - PMID:32673704
  - PMC:PMC6627983
  unresolved_references:
  - DOI:10.1002/epd2.20184](https://onlinelibrary.wiley.com/doi/abs/10.1002/epd2.20184
  - DOI:10.1159/000539473/911172/PACS2-PACS1-and-VACTERL-A-Clinical-Overlap
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PACS2-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **PACS2-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research this now with parallel searches covering the key domains.

Good — found the PACS2 Research Foundation and evidence of mouse models being developed. Let me gather a few more details on the drug repurposing/cell painting study, VACTERL overlap, and the migrating focal seizures paper.

I have sufficient material now. Let me pull one more source — the Perlara PACS2 Cure Roadmap for model organism/therapeutic pipeline detail — then compile the full report.

# PACS2-Related Developmental and Epileptic Encephalopathy (DEE66): Comprehensive Research Report

## 1. Disease Information

**Overview.** PACS2-Related Developmental and Epileptic Encephalopathy — officially catalogued as **Developmental and Epileptic Encephalopathy 66 (DEE66)**, and previously termed Early Infantile Epileptic Encephalopathy 66 (EIEE66) — is an autosomal dominant neurodevelopmental disorder caused by a heterozygous, almost always *de novo*, missense variant in **PACS2** (phosphofurin acidic cluster sorting protein 2), located at chromosome **14q32.33**. It is characterized by neonatal- or early-infantile-onset epilepsy, global developmental delay/intellectual disability, hypotonia, characteristic facial dysmorphism, and cerebellar dysgenesis on brain MRI, often accompanied by extraneurologic features (ophthalmologic, cardiac, limb, hematologic) ([OMIM #618067](https://omim.org/entry/618067); [Olson et al. 2018, PMID:29656858](https://pubmed.ncbi.nlm.nih.gov/29656858/)).

**Key identifiers:**
- **OMIM:** #618067 (DEE66, phenotype); *610423 (PACS2, gene)
- **Gene:** PACS2, HGNC:23794, chromosome 14q32.33
- **NIH GTR condition:** C4748070 ("Developmental and epileptic encephalopathy, 66")
- **Disease Ontology:** DOID:0080446
- Likely MONDO term for this entity corresponds to DEE66 (curators should verify exact MONDO CURIE via OMIM/Mondo cross-reference at curation time — not independently confirmed in this research pass)

**Synonyms:** Early Infantile Epileptic Encephalopathy 66 (EIEE66); PACS2 syndrome; DEE66; PACS2-related neurodevelopmental disorder.

**Evidence basis:** Nearly all published knowledge derives from **aggregated case series and systematic reviews** of individually reported and cohort patients (not large-cohort EHR/registry data) — the disease was first delineated in 2018 in 14 unrelated patients ([PMID:29656858](https://pubmed.ncbi.nlm.nih.gov/29656858/)) and subsequent literature has grown the total to roughly **~50–100 reported individuals worldwide** as of 2022–2024 ([PACS2 Research Foundation](https://www.pacs2research.org/); [Genetics in Medicine Open 2024](https://www.gimopen.org/article/S2949-7744(24)00425-4/fulltext)).

---

## 2. Etiology

**Disease causal factor:** A single, essentially monogenic mechanism — heterozygous missense variation in PACS2, almost always the recurrent **c.625G>A, p.(Glu209Lys) [E209K]** variant, arising *de novo* in the vast majority of cases ([PMID:29656858](https://pubmed.ncbi.nlm.nih.gov/29656858/); [PMC10968252](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968252/) — 30/30 reviewed patients carried this variant).

**Genetic risk factors:**
- The E209K substitution affects a highly conserved glutamic acid residue within a domain of PACS2 involved in phosphorylation-dependent regulatory interactions (Ser207/208/213 cluster) ([Mammalian Genome 2024, doi:10.1007/s00335-024-10098-5]).
- A second, rarer recurrent variant, **E211K**, has also been reported and studied mechanistically alongside E209K, both impairing mitochondria-associated membrane (MAM) integrity via disturbance of PACS2 phosphorylation at the Ser207/208/213 cluster.
- Additional distinct missense variants have been reported in isolated cases with atypical/milder or expanded phenotypes (e.g., malformations of cortical development, migrating focal seizures of infancy), suggesting some allelic heterogeneity beyond the two hotspot residues ([Checri et al. 2024, Epileptic Disorders, doi:10.1002/epd2.20184](https://onlinelibrary.wiley.com/doi/abs/10.1002/epd2.20184); [ScienceDirect migrating focal seizures paper](https://www.sciencedirect.com/science/article/pii/S2949918624000536)).
- No inherited/parental transmission has been documented in the majority of families — parents are typically wild-type at the variant position, confirming de novo origin (e.g., the Saudi family study, [PMC10963950](https://pmc.ncbi.nlm.nih.gov/articles/PMC10963950/)).
- PACS2's paralog **PACS1** causes the related Schuurs-Hoeijmakers syndrome (PACS1 neurodevelopmental disorder, recurrent p.Arg203Trp), with substantial phenotypic overlap (developmental delay 100%, dysmorphism 100%, seizures 63% in PACS1) — evidence of a shared pathway mechanism ([Karger Molecular Syndromology 2024, PACS2/PACS1/VACTERL overlap](https://karger.com/msy/article/doi/10.1159/000539473/911172/PACS2-PACS1-and-VACTERL-A-Clinical-Overlap)).

**Environmental risk factors:** None established; this is a purely genetic, non-environmentally-triggered disorder based on current literature.

**Protective factors:** None reported in the literature (genetic or environmental). No modifier alleles have been characterized.

**Gene-environment interactions:** Not applicable / not studied — no evidence of environmental modulation of phenotype severity.

---

## 3. Phenotypes

### Seizures / epilepsy (universal, ~100%)
- **Onset:** Neonatal to early infantile; in the largest systematic review (n=30), onset ranged from day 1 of life to 10 months, with 76.7% (23/30) presenting within the first 2 weeks of life ([PMC10968252](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968252/)).
- **Seizure semiology:** Focal motor seizures, tonic seizures (often affecting upper limbs), autonomic manifestations (apnea, cyanosis), abnormal eye movements/eye rolling, myoclonic seizures, and generalized tonic-clonic seizures (often febrile-triggered); focal-onset with secondary generalization predominates in the neonatal period ([PMC10137075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137075/)).
- **Course:** Seizures are typically difficult to control in infancy/early childhood, requiring multiple anti-seizure medication trials, but frequently become easier to control — or resolve — with advancing age; 29% of patients ≥5 years old discontinued anti-seizure medication in one cohort.
- **HPO suggestions:** HP:0032796 (Seizure — DEE), HP:0032810 (focal-onset seizure), HP:0002123 (generalized tonic-clonic seizure), HP:0002121 (generalized non-motor seizure), HP:0011097 (epileptic spasm as needed), HP:0007359 (focal-onset seizure), HP:0011182 (electroencephalographic abnormality), HP:0002133 (status epilepticus if applicable).

### Global developmental delay / intellectual disability (~80%, universal in most series)
- Delayed motor and speech milestones (delayed global development 80% [24/30]; speech delay 63% [19/30]).
- Intellectual disability ranges mild to severe; progressive cognitive decline reported in adult cases.
- HPO: HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0000750 (Delayed speech and language development).

### Hypotonia (~57%, 17/30)
- HPO: HP:0001252 (Hypotonia).

### Behavioral abnormalities (~50%, 15/30) including autism spectrum features
- ASD reported in ~18% (4/22 with data) in one cohort.
- HPO: HP:0000708 (Behavioral abnormality), HP:0000717 (Autism).

### Movement/neurological signs
- Nystagmus (13%, 4/30), wide-based gait (13%), pyramidal syndrome (13%).
- HPO: HP:0000639 (Nystagmus), HP:0002136 (Broad-based gait), HP:0007256 (Progressive spasticity/pyramidal signs).

### Facial dysmorphism (common but variable/subtle)
- Hypertelorism, broad/wide nasal root, thin upper lip, highly arched eyebrows, long eyelashes, wide-spaced teeth, down-turned corners of the mouth, down-slanting palpebral fissures.
- HPO: HP:0000316 (Hypertelorism), HP:0000414 (Broad nasal tip/root — HP:0000455), HP:0000219 (Thin upper lip vermilion), HP:0004585 (Highly arched eyebrow), HP:0000582 (Downslanted palpebral fissures), HP:0000160 (Narrow mouth or wide mouth per variant description).

### Ophthalmologic features (~37%, 11/30)
- Strabismus, nystagmus, hypermetropia, astigmatism, myopia, coloboma.
- HPO: HP:0000486 (Strabismus), HP:0000540 (Hypermetropia), HP:0000544 (Coloboma).

### Cardiac (septal defects; also tetralogy of Fallot reported in one case expanding the phenotype)
- Atrial/ventricular septal defects: 4/30 cases (~13%); complex congenital heart disease (tetralogy of Fallot) reported in a novel case with VACTERL-like overlap.
- HPO: HP:0001631 (ASD), HP:0001629 (VSD), HP:0001636 (Tetralogy of Fallot).

### Other systemic features
- Cryptorchidism (5 cases), distal limb malformations (12 cases), hematologic disturbances (5 cases), hydronephrosis (2 cases); anal atresia and vertebral anomalies reported in one expanded VACTERL-overlap case.
- HPO: HP:0000028 (Cryptorchidism), HP:0002830 (Limb undergrowth/distal anomaly per specific finding), HP:0004320 (Ectopic anus/anal atresia — HP:0002023), HP:0000924 (Abnormality of the skeletal system for vertebral anomalies).

### Brain imaging (MRI) findings
- Cerebellar foliar dysgenesis (50%, 15/30) — the most characteristic neuroimaging finding.
- Mega cisterna magna (43%, 13/30).
- Inferior vermis hypoplasia (27%, 8/30).
- Reduced white matter (20%, 6/30).
- Lateral ventricle enlargement (13%).
- Hypothalamic fusion anomalies (10%).
- Negative/normal neuroimaging in ~20% (6/30).
- Progressive findings in adults: severe cerebral/cerebellar atrophy, demyelinating lesions.
- HPO: HP:0007033 (Cerebellar dysplasia/dysgenesis), HP:0002324 (Cerebellar vermis hypoplasia), HP:0002534 (Cisterna magna malformation — mega cisterna magna HP:0006955), HP:0002500 (delayed CNS myelination/HP:0002500 or reduced white matter HP:0002119), HP:0002119 (Ventriculomegaly).

**Quality of life impact:** Not systematically studied via validated instruments (EQ-5D/SF-36) in the literature reviewed; qualitative reports describe substantial burden from refractory neonatal/infantile seizures, limited verbal communication, poor social functioning, and — in adults — progressive neurological decline including new-onset facial hemispasm, ataxia, and tetraparesis in the oldest reported cases ([PMC10968252](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968252/)).

---

## 4. Genetic/Molecular Information

**Causal gene:** PACS2 (HGNC:23794; OMIM *610423), chromosome 14q32.33.

**Recurrent pathogenic variant:**
- **c.625G>A, p.Glu209Lys (E209K)** — the dominant, recurrent, de novo variant found in the overwhelming majority (~30/30 in the largest systematic review) of published DEE66 patients ([PMID:29656858](https://pubmed.ncbi.nlm.nih.gov/29656858/); [PMC10968252](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968252/)).
- **c.631G>A, p.Glu211Lys (E211K)** — a second, rarer recurrent hotspot variant, mechanistically studied alongside E209K.
- Additional rare missense variants reported in association with somewhat expanded/atypical phenotypes (cortical malformation, migrating focal seizures of infancy, complex congenital heart disease/VACTERL overlap).

**Variant classification:** Pathogenic/likely pathogenic per ACMG criteria for the recurrent hotspot variants (de novo, absent from population databases, functionally validated). Curators should confirm current ClinVar star-rating and classification directly.

**Variant type/class:** Missense, heterozygous, gain-of-function/dominant-negative-like mechanism (see below) rather than simple loss-of-function.

**Population frequency:** The E209K and E211K variants are not present in gnomAD population databases (consistent with a highly penetrant de novo dominant disorder); specific PACS2 gene-level constraint metrics (pLI/LOEUF) were not confirmed in this research pass and should be pulled directly from the gnomAD browser at curation time.

**Origin:** Predominantly germline de novo; no confirmed cases of parental mosaicism or inherited transmission were found in this search, though the possibility of parental gonadal mosaicism has not been excluded in the literature.

**Functional consequence — molecular mechanism:**
- PACS2 is a multifunctional sorting protein and a key regulator of **mitochondria-associated membranes (MAMs)** — physical tethering sites between the endoplasmic reticulum (ER) and mitochondria — controlling ER–mitochondria calcium signaling, lipid synthesis, mitophagy, ER homeostasis, and apoptosis ([PACS-2: A key regulator of MAMs, PMID:32673704](https://pubmed.ncbi.nlm.nih.gov/32673704/); [PMC6627983](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627983/)).
- The E209K (and E211K) mutations disturb PACS2 phosphorylation at the **Ser207/208/213 cluster**, impairing MAM integrity (Mammalian Genome 2024, doi:10.1007/s00335-024-10098-5).
- Functional studies (HCT116 cell model) show E209K PACS-2 has **slower protein turnover** relative to wild-type upon cycloheximide treatment, and **increased association with 14-3-3ε** by co-immunoprecipitation. Upon apoptotic stress (staurosporine), E209K-expressing cells show markedly increased apoptosis (~80% apoptotic cells vs. ~41% for wild-type PACS-2), whereas wild-type PACS-2 is protective against stress-induced cell death ([PMC9520720](https://pmc.ncbi.nlm.nih.gov/articles/PMC9520720/)). The authors state: *"increased levels of apoptosis agree with DEE66 patient phenotypes involving epilepsy and cerebellar dysgenesis."*
- This suggests a **gain-of-function/altered-function** mechanism (aberrant 14-3-3 client recruitment promoting apoptosis) rather than simple haploinsufficiency — consistent with the recurrent, hotspot nature of the variant and absence of reported loss-of-function (truncating) alleles causing the same phenotype.
- Downstream cellular consequences implicated: disrupted MAM formation, impaired ER–mitochondria Ca²⁺ flux, inhibited mitophagy, impaired energy metabolism, and increased apoptotic susceptibility in neurons/cerebellar cells, plausibly explaining the progressive cerebellar dysgenesis/atrophy phenotype.
- Suggested GO terms: GO:0032865 (regulation of mitochondrial outer membrane permeabilization), GO:0032469 (endoplasmic reticulum calcium ion homeostasis), GO:0044233 (ER-mitochondrion membrane contact site organization), GO:0006915 (apoptotic process), GO:0000422 (mitophagy).

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism or chromosomal-scale abnormality has been implicated; disease is driven by point missense variants.

---

## 5. Environmental Information

No environmental factors, lifestyle exposures, or infectious triggers have been implicated as causal or modifying for PACS2-related DEE66 in the literature reviewed. Febrile illness has been noted as a trigger for individual generalized tonic-clonic seizure episodes in some patients (a symptomatic exacerbant, not a disease cause) ([PMC10137075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137075/)).

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed):**
1. **Trigger:** De novo heterozygous PACS2 missense variant (predominantly E209K) alters a conserved residue near the Ser207/208/213 phosphorylation cluster.
2. **Molecular consequence:** Altered PACS2 phosphorylation/turnover kinetics and increased binding to 14-3-3ε, altering the normal pool of PACS2 client protein interactions.
3. **MAM/organelle consequence:** Impaired mitochondria-associated membrane (ER-mitochondria contact site) integrity; disrupted ER-mitochondria Ca²⁺ transfer; disrupted mitophagy and mitochondrial energy metabolism.
4. **Cellular consequence:** Increased susceptibility to apoptosis under cellular stress, particularly relevant to cerebellar granule/Purkinje neuron populations and cortical neurons during critical developmental windows.
5. **Tissue/organ consequence:** Cerebellar foliar dysgenesis, vermis hypoplasia, progressive cerebral/cerebellar atrophy (especially notable in the few reported adult cases), and cortical network dysfunction predisposing to neonatal-onset epilepsy.
6. **Clinical manifestation:** Neonatal/infantile-onset, often refractory, focal-onset epilepsy; global developmental delay/ID; hypotonia; behavioral/autistic features; and variable dysmorphic/extraneurologic features.

**Upstream vs. downstream:** The PACS2 phosphorylation/14-3-3 interaction defect is the most upstream molecular lesion identified; MAM/Ca²⁺-handling disruption and apoptotic susceptibility are intermediate; cerebellar dysgenesis/atrophy and cortical hyperexcitability are downstream tissue-level consequences producing the clinical phenotype.

**Cell types implicated:** Cerebellar Purkinje and granule neurons (dysgenesis/atrophy phenotype), cortical neurons (epileptogenesis), and more broadly any cell type dependent on ER-mitochondria MAM signaling (vascular smooth muscle cells and cardiomyocytes have also been separately studied for PACS2's MAM role, relevant to the cardiac phenotype overlap with PACS1/VACTERL).

**Molecular pathway/GO terms:** Suggested — GO:0044233 (ER-mitochondrion membrane contact site organization), GO:0051560 (mitochondrial calcium ion homeostasis), GO:0000422 (mitophagy), GO:0006915 (apoptotic process), GO:0035556 (intracellular signal transduction, for 14-3-3-mediated signaling).

**Cell Ontology suggestions:** CL:0000121 (Purkinje cell), CL:0000120 (granule cell), CL:0000540 (neuron), CL:0002319 (neural cell, generic).

**Advanced/omics data:** No large-scale transcriptomic, proteomic, or single-cell datasets specific to PACS2 patient tissue were identified in this search; iPSC-neuron models are in active development (see Model Organisms, section 15) but published multi-omic datasets from these models were not found as of this research date.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system — cerebrum (cortex), cerebellum (vermis and foliae).
- **Secondary/associated:** Cardiovascular system (septal defects, tetralogy of Fallot), ophthalmologic structures (globe/refraction, strabismus), genitourinary (cryptorchidism, hydronephrosis), gastrointestinal (anal atresia in expanded phenotype), hematologic system, and craniofacial skeleton (dysmorphic features).
- **Body systems:** Nervous, cardiovascular, ophthalmologic, musculoskeletal, genitourinary.

**UBERON suggestions:** UBERON:0002037 (cerebellum), UBERON:0002038 (cerebellar vermis), UBERON:0000955 (brain), UBERON:0001017 (central nervous system), UBERON:0007100 (primary circulatory organ/heart region for septal defects), UBERON:0000970 (eye).

**Tissue/cell level:** Cerebellar cortex (Purkinje/granule cell layers), cerebral cortical neurons; craniofacial soft tissue (dysmorphism).

**Subcellular level:** Mitochondria-associated ER membranes (MAMs), mitochondrial outer membrane, endoplasmic reticulum. GO Cellular Component: GO:0044233 (ER-mitochondrion membrane contact site), GO:0005741 (mitochondrial outer membrane), GO:0005783 (endoplasmic reticulum).

**Localization:** Bilateral/symmetric cerebellar involvement typically; no reported lateralization pattern.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal-to-infantile for the core neurological phenotype; seizure onset from day 1 of life to 10 months, with the large majority (76.7%) within the first two weeks of life. Rare later-onset (childhood) presentations reported for milder allelic variants.
- **Onset pattern:** Typically acute/abrupt seizure onset in the neonatal period.
- **Progression:** Epilepsy often initially difficult to control (multiple ASM trials/combinations needed in infancy/childhood), frequently improving or resolving with age (many patients seizure-free or medication-free by later childhood/adolescence). In contrast, the cognitive/neurodegenerative trajectory in the very limited adult cohort (only 4 adults reported as of the 2024 systematic review) shows **progressive** cerebral/cerebellar atrophy, new-onset movement abnormalities (facial hemispasm, ataxia), and cognitive regression — suggesting a biphasic course (early epileptic encephalopathy, later progressive neurodegeneration).
- **Disease course pattern:** Chronic, lifelong; not classically relapsing-remitting but with an early severe epileptic phase that may partially remit, followed by potential later-life progressive decline.
- **Critical periods:** Neonatal/early infantile period represents the critical window of epileptogenic vulnerability; timely genetic diagnosis in this window is emphasized in the literature as important for guiding management (e.g., trial of pyridoxal phosphate) and counseling.

---

## 9. Inheritance and Population

**Epidemiology:** True population prevalence/incidence is unknown (ultra-rare disease). Approximately **~50 cases** were known by December 2022, growing to roughly **~100 individuals described worldwide** by 2024 ([PACS2 Research Foundation](https://www.pacs2research.org/); [PMC10968252](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968252/)).

**Inheritance pattern:** Autosomal dominant, with the overwhelming majority of cases arising **de novo**. No confirmed familial recurrence via germline transmission was found in this search; recurrence risk beyond the general de novo/gonadal mosaicism risk (~1%) has not been formally established in the literature.

**Penetrance:** Appears to be high/complete for the core epilepsy/developmental phenotype among E209K carriers reported to date, though one case of a "developmentally typical" patient with the classic c.625G>A variant and a milder phenotype (responsive to carbamazepine) has been reported, raising the possibility of variable expressivity (mosaicism was considered but excluded by deep sequencing coverage in that case).

**Expressivity:** Variable — phenotype severity ranges from classic severe DEE66 with refractory neonatal seizures and marked cerebellar dysgenesis to milder presentations with typical development.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not formally documented but biologically plausible given the pattern of exclusively de novo occurrence; not excluded as an explanation for rare phenotypic variability.

**Founder effects:** None reported; cases have been described across diverse populations (including a Saudi family), consistent with recurrent de novo mutation at a mutational hotspot rather than a founder allele.

**Consanguinity:** Not implicated as a risk factor (autosomal dominant de novo mechanism).

**Sex ratio:** Roughly equal in the largest reviewed cohort (16 male, 14 female, n=30) — no strong sex bias reported.

**Geographic distribution:** Global; cases reported from North America, Europe, Middle East (Saudi Arabia), and elsewhere with no evident geographic clustering.

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES)** or **whole genome sequencing (WGS)**, typically trio-based (proband + parents), is the standard diagnostic approach given the phenotype's genetic heterogeneity overlap with other early-infantile DEEs; this is how essentially all reported cases have been ascertained.
- **Epilepsy/DEE gene panels** including PACS2 are also used clinically (e.g., listed on Genomics England PanelApp "Early onset or syndromic epilepsy" panel).
- **Single-gene Sanger confirmation** of the recurrent E209K hotspot can be pursued when clinical suspicion is high (classic facial/cerebellar/seizure phenotype).
- Genetic diagnosis timing in the reviewed cohort ranged widely (4 months to 37 years of age), reflecting historically low disease awareness, especially in adults.

**Neuroimaging:** Brain MRI is a key diagnostic-supportive test — cerebellar foliar dysgenesis, mega cisterna magna, and vermis hypoplasia are characteristic (though absent in ~20% of cases, so a normal MRI does not exclude the diagnosis).

**EEG:** Variable findings — focal/multifocal interictal discharges (often centrotemporal/frontal), burst suppression, or hypsarrhythmia in some neonatal presentations; some normalize over time.

**Differential diagnosis:** Other genetic DEEs presenting in the neonatal/early infantile period (e.g., KCNQ2-, SCN2A-, STXBP1-, CDKL5-related DEEs), pyridoxine-dependent epilepsy (given some PACS2 patients show transient pyridoxal-phosphate responsiveness), other cerebellar dysgenesis syndromes, and — given phenotypic overlap — PACS1-related neurodevelopmental disorder (Schuurs-Hoeijmakers syndrome).

**Screening:** No population or newborn screening program exists (ultra-rare, not detected by standard newborn metabolic screening); diagnosis relies entirely on clinical suspicion triggering genetic testing.

**Standardized diagnostic criteria:** No formal consensus diagnostic criteria; diagnosis is molecular (identification of a pathogenic PACS2 variant) in the appropriate clinical context per ILAE epilepsy classification framework for developmental and epileptic encephalopathies.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No systematic mortality data identified in this search; the disorder is not classically described as life-limiting in early reports, though severity varies widely.

**Seizure outcome:** Often improves with age — many patients achieve better seizure control or seizure freedom in later childhood, with ~29% of patients ≥5 years old able to discontinue anti-seizure medication in one series.

**Developmental/cognitive outcome:** Ranges from low-average intelligence to severe developmental impairment; most patients have some degree of intellectual disability, speech delay, and behavioral disturbance (including autism spectrum features in ~18%).

**Adult/long-term course:** Limited data (only 4 adult cases reported by 2024) suggest a concerning pattern of **progressive neurodegeneration** in adulthood — accelerating cerebral/cerebellar atrophy, demyelinating changes, cognitive regression, and new motor symptoms (facial hemispasm, ataxia, tetraparesis) — highlighting a need for longitudinal natural history studies as the cohort ages.

**Prognostic factors:** Specific genotype-phenotype correlations beyond "E209K = classic/most common phenotype" are not well established; the rarer E211K and other missense variants may correlate with atypical presentations (milder or with additional features like cortical malformation or complex congenital heart disease), but sample sizes are too small for robust conclusions.

---

## 12. Treatment

**Anti-seizure pharmacotherapy** (symptomatic, not disease-modifying):
- **Valproic acid** and **levetiracetam** — reported effective in roughly half of patients.
- **Phenobarbital** — improvement in about one-third.
- **Carbamazepine/oxcarbazepine** — effective in about one-quarter; notably one patient with typical development responded well to carbamazepine.
- **Vigabatrin** — reported effective in some cases.
- **Pyridoxal phosphate (vitamin B6, active form)** — showed promising, though sometimes transient, effectiveness in some cases; seizure recurrence occurred when switched to standard oral B6 (pyridoxine) in at least one report, suggesting a possible pyridoxal-phosphate-specific responsiveness worth trialing early.

NCIT suggestion: NCIT:C15986 (Pharmacotherapy) as the treatment_term, with therapeutic_agent bound to CHEBI terms for valproic acid (CHEBI:39867), levetiracetam (CHEBI:6437), carbamazepine (CHEBI:3387), vigabatrin (CHEBI:9944), phenobarbital (CHEBI:8069).

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, speech therapy for hypotonia, motor delay, and speech delay; behavioral/developmental interventions for autism spectrum features. NCIT: NCIT:C15302 (Physical Therapy), NCIT:C159273 (Speech Therapy), NCIT:C121351 (Occupational Therapy).

**Surgical/interventional:** Cardiac surgical repair for structural congenital heart defects (septal defect closure, tetralogy of Fallot repair) in affected individuals. NCIT:C15329 (Surgical Procedure).

**Experimental / emerging precision therapies (active development, not yet clinically available):**
- **Antisense oligonucleotide (ASO) therapy:** An allele-specific ASO strategy targeting the mutant E209K transcript while sparing wild-type PACS2 expression is in development in partnership with the **n-Lorem Foundation** (a nonprofit providing individualized ASO therapies for ultra-rare diseases), modeled on the analogous, more advanced PACS1 syndrome ASO program (see PACS1 mouse model RNA-targeted therapy work, [PMC9901029](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9901029/); [Nature Communications 2023](https://www.nature.com/articles/s41467-023-42176-8)).
- **Drug repurposing via high-throughput Cell Painting screening:** The **PACS2 Research Foundation**, in partnership with Charles River Laboratories (Leiden), screened the Broad Institute's Drug Repurposing Hub (~6,808 compounds) against patient-derived fibroblasts using morphological (Cell Painting) profiling compared to an unaffected twin sibling's cells, identifying several candidate compounds that shifted the diseased-cell morphological signature toward the healthy phenotype; potency/dose-optimization screening is ongoing as of the most recent reporting ([Charles River Eureka blog](https://www.criver.com/eureka/drug-repurposing-through-cell-painting-could-treat-rare-disease)).
- **PROTAC (targeted protein degradation)** approaches to selectively degrade mutant PACS2 protein are proposed as an emerging strategy, pending further mechanistic clarification ([PACS2 Cure Roadmap, Perlara](https://perlara.substack.com/p/pacs2-cure-roadmap)).

**Genetic counseling:** Recommended for all newly diagnosed families given the near-universal de novo occurrence, low but non-zero recurrence risk (germline mosaicism), and autosomal dominant inheritance pattern once established. NCIT:C15240 (Genetic Counseling).

**Clinical trials:** No PACS2-specific registered interventional clinical trials (NCT identifiers) were identified in this search; the disease remains in the preclinical/translational research stage for targeted therapies.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies exist for this de novo genetic disorder — there are no known modifiable risk factors. The main "prevention" mechanism available is **prenatal/preimplantation genetic diagnosis** for families with a previously affected child (relevant given theoretical germline mosaicism recurrence risk), and **genetic counseling** for recurrence risk discussion. No immunization, screening program, or public health intervention is applicable. NCIT:C15240 (Genetic Counseling) remains the most relevant preventive/counseling intervention captured in ontology terms.

---

## 14. Other Species / Natural Disease

No naturally occurring PACS2-associated disease has been reported in non-human species (companion animals or wildlife) in the literature reviewed — this is a human-only reported condition to date, consistent with its very recent (2018) delineation and ultra-rare status. PACS2 is evolutionarily conserved (the E209 residue is conserved down to zebrafish, per the PACS2 Cure Roadmap document), supporting cross-species relevance for engineered models (see below) but no evidence of spontaneous veterinary cases.

---

## 15. Model Organisms

This is an area of very active, ongoing translational development, primarily driven by the **PACS2 Research Foundation** and academic/industry collaborators (Perlara PBC "cure roadmap"; Jackson Laboratory; Charles River Laboratories):

- **Yeast:** Not a viable model — PACS2 has **no ortholog in yeast**.
- **Drosophila / C. elegans:** Deprioritized — the critical glutamate at position 209 is **not conserved** in fly or worm PACS orthologs, limiting translational relevance.
- **Zebrafish:** E209 **is conserved** in zebrafish PACS2, making a heterozygous E209K knock-in zebrafish model biologically feasible; proposed for future generation (deprioritized pending cellular-assay proof of concept as of the most recent roadmap update). No published zebrafish PACS2 model was identified as of this search.
- **Mouse:** A **Pacs2^E209K/+ mouse model** reportedly exists (noted as "approved in Poland" per the PACS2 Research Foundation) but requires further phenotypic characterization; a humanized Pacs2 E209K/+ mouse model at **The Jackson Laboratory** has been proposed specifically to support preclinical ASO testing. No peer-reviewed publication describing detailed phenotype recapitulation in this mouse model was identified in this search — this represents a **knowledge gap** in the current literature (model exists per foundation reporting, but published characterization is not yet available).
- **Patient-derived iPSCs:** Multiple iPSC lines have been generated from PACS2 patients (e.g., "Lena's" fibroblast-derived iPSCs) and are being differentiated into neurons in collaboration with academic labs (e.g., Dr. A. Guemez-Gamboa) to study E209K effects on neuronal mitochondrial function, protein interactions, and developmental phenotypes, alongside CRISPR-corrected isogenic controls. No published dataset from these iPSC-neuron models was identified as of this research pass.
- **Cell line models (non-neuronal):** HCT116 human colorectal carcinoma cells transfected with PACS-2 WT vs. E209K have been used to directly demonstrate increased apoptotic susceptibility and altered 14-3-3ε binding ([PMC9520720](https://pmc.ncbi.nlm.nih.gov/articles/PMC9520720/)). Patient-derived dermal fibroblasts have been used for the Cell Painting drug-repurposing screen described above.

**Model limitations:** No model to date has published in vivo confirmation of the characteristic cerebellar dysgenesis or epilepsy phenotype seen in human patients — this is an important translational gap. Curators modeling this disease should flag a `HUMAN_MODEL_MISMATCH`-type caveat: current functional/mechanistic data (apoptosis susceptibility, MAM/14-3-3 interaction) derive from heterologous cell-line overexpression systems (HCT116) rather than neurons or an in vivo nervous system model, so translational validity of the apoptosis-centric mechanism to human cerebellar/cortical pathology in situ remains to be directly confirmed.

---

## Summary of Key Ontology Term Suggestions

| Domain | Suggested terms |
|---|---|
| Disease | OMIM:618067; DOID:0080446; (MONDO CURIE to be confirmed) |
| Gene | HGNC:23794 (PACS2); OMIM:*610423 |
| Phenotypes (HP) | HP:0032796/HP:0032810 (seizures), HP:0001263 (global DD), HP:0001249 (ID), HP:0001252 (hypotonia), HP:0000717 (autism), HP:0007033 (cerebellar dysgenesis), HP:0002324 (vermis hypoplasia), HP:0006955 (mega cisterna magna), HP:0000582 (downslanted palpebral fissures), HP:0000316 (hypertelorism), HP:0001629/HP:0001631 (septal defects), HP:0000486 (strabismus) |
| GO (biological process) | GO:0044233 (ER-mitochondrion MCS organization), GO:0051560 (mitochondrial Ca²⁺ homeostasis), GO:0000422 (mitophagy), GO:0006915 (apoptotic process) |
| CL (cell type) | CL:0000121 (Purkinje cell), CL:0000120 (cerebellar granule cell), CL:0000540 (neuron) |
| UBERON | UBERON:0002037 (cerebellum), UBERON:0002038 (cerebellar vermis), UBERON:0000955 (brain) |
| CHEBI (drugs) | CHEBI:39867 (valproic acid), CHEBI:6437 (levetiracetam), CHEBI:3387 (carbamazepine), CHEBI:9944 (vigabatrin), CHEBI:8069 (phenobarbital) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling), NCIT:C15329 (Surgical Procedure) |

---

### Sources
- [Entry - #618067 - DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 66; DEE66 - OMIM](https://omim.org/entry/618067)
- [Entry - *610423 - PHOSPHOFURIN ACIDIC CLUSTER SORTING PROTEIN 2; PACS2 - OMIM](https://www.omim.org/entry/610423)
- [A Recurrent De Novo PACS2 Heterozygous Missense Variant Causes Neonatal-Onset Developmental Epileptic Encephalopathy, Facial Dysmorphism, and Cerebellar Dysgenesis - PubMed (PMID:29656858)](https://pubmed.ncbi.nlm.nih.gov/29656858/)
- [Characteristics of Developmental and Epileptic Encephalopathy Associated with PACS2 p.Glu209Lys Pathogenic Variant—Our Experience and Systematic Review of the Literature - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10968252/)
- [Long-Term Outcome of Neonatal Seizure with PACS2 Mutation: Case Series and Literature Review - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137075/)
- [A missense variant in the PACS2 gene cause Epileptic Encephalopathy and seizures in Saudi family - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10963950/)
- [The Phosphofurin Acidic Cluster Sorting Protein 2 (PACS-2) E209K Mutation Responsible for PACS-2 Syndrome Increases Susceptibility to Apoptosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9520720/)
- [PACS-2: A key regulator of mitochondria-associated membranes (MAMs) - PubMed](https://pubmed.ncbi.nlm.nih.gov/32673704/)
- [The Multifunctional Sorting Protein PACS-2 Controls Mitophagosome Formation in Human Vascular Smooth Muscle Cells through Mitochondria-ER Contact Sites - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627983/)
- [Understanding PACS2 syndrome's pathomechanism by studying E209K and E211K mutations - Mammalian Genome](https://link.springer.com/article/10.1007/s00335-024-10098-5)
- [PACS2, PACS1, and VACTERL: A Clinical Overlap - Molecular Syndromology, Karger](https://karger.com/msy/article/doi/10.1159/000539473/911172/PACS2-PACS1-and-VACTERL-A-Clinical-Overlap)
- [Migrating focal seizures of infancy associated with pathogenic variants in PACS2 - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2949918624000536)
- [P385: PACS2-related developmental and epileptic encephalopathy: A review of molecular mechanisms and clinical aspects - Genetics in Medicine Open](https://www.gimopen.org/article/S2949-7744(24)00425-4/fulltext)
- [PACS2 Research Foundation](https://www.pacs2research.org/)
- [Drug Repurposing Through Cell Painting Could Treat Rare Disease - Charles River Eureka blog](https://www.criver.com/eureka/drug-repurposing-through-cell-painting-could-treat-rare-disease)
- [PACS2 Cure Roadmap - Perlara](https://perlara.substack.com/p/pacs2-cure-roadmap)
- [Developmental and epileptic encephalopathy, 66 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4748070/)
- [Developmental and Epileptic Encephalopathy 66 - MalaCards](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_66)
- [PACS2 pathogenic variant associated with malformation of cortical development and epilepsy - Epileptic Disorders, Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/epd2.20184)
- [RNA-targeted therapy corrects neuronal deficits in PACS1 syndrome mice - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9901029/)
- [Neural deficits in a mouse model of PACS1 syndrome are corrected with PACS1- or HDAC6-targeting therapy - Nature Communications](https://www.nature.com/articles/s41467-023-42176-8)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 2 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1002/epd2.20184](https://onlinelibrary.wiley.com/doi/abs/10.1002/epd2.20184` (1 mention) - Identifier did not resolve to a record
- `DOI:10.1159/000539473/911172/PACS2-PACS1-and-VACTERL-A-Clinical-Overlap` (3 mentions) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:32673704` (4 mentions) - PACS-2: A key regulator of mitochondria-associated membranes (MAMs).
  - shared terms: disease
- `PMC:PMC6627983` (4 mentions) - The Multifunctional Sorting Protein PACS-2 Controls Mitophagosome Formation in Human Vascular Smooth Muscle Cells through Mitochondria-ER Contact Sites.
  - shared terms: cell, model

Weighed against this report's own most characteristic terms: `phenotype`, `pacs2`, `seizure`, `disease`, `cerebellar`, `patient`, `developmental`, `variant`, `genetic`, `e209k`, `hpo`, `cell`, `dysgenesis`, `epilepsy`, `novo`, `model`, `development`, `disorder`, `neonatal`, `feature`.