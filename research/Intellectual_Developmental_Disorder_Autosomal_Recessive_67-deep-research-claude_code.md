---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-27T16:50:49.206244'
end_time: '2026-08-27T16:59:17.820996'
duration_seconds: 508.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Developmental Disorder Autosomal Recessive 67
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 15
  num_turns: 45
  total_cost_usd: 7.863692
  session_id: 458b3185-e500-46d3-a159-ccd3c44dc2d2
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 22
reference_validation:
  total_references: 15
  verified: 13
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.133
  relevance_assessed: 13
  on_topic: 6
  unresolved_references:
  - DOI:10.1016/j.gimo.2024.101213](https://www.gimopen.org/article/S2949-7744(24)00359-5/fulltext
  - DOI:10.1371/journal.pone.0008994](https://journals.plos.org/plosone/article
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder Autosomal Recessive 67
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder Autosomal Recessive 67** covering all of the
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

I'll research MRT67 (PPP1R21-related) by checking the local reference cache and then searching the web for OMIM/ClinVar/literature details.

The cached references contain both EIF3F and PPP1R21 material — note OMIM #618295 (MRT67) is the **EIF3F** disorder, not PPP1R21. Let me check the working stub and gather more sources.

Existing partial curation found. Now gathering primary-source detail (OMIM, ClinVar, gnomAD, Simons Searchlight, 2024 abstract).

I have what I need. Writing the report now.

---

# Research Report: Intellectual Developmental Disorder, Autosomal Recessive 67 (MRT67)

**Gene: *EIF3F* • MONDO:0032662 • OMIM #618295**
Prepared 2026-08-27. Sources are cited inline; direct abstract/full-text quotes are given where they support a key claim.

---

## ⚠️ Critical disambiguation before you read further

**Two different diseases are easily confused here, and the reference cache in this worktree currently contains material for both.**

| | **MRT67 (this report)** | **PPP1R21-related El-Hattab-Schmidts syndrome (NOT this report)** |
|---|---|---|
| Gene | ***EIF3F***, 11p15.4 | *PPP1R21*, 2p16.3 |
| OMIM phenotype | #618295 | separate entry (gene *618159) |
| MONDO | MONDO:0032662 | separate term |
| Mechanism | Reduced translation initiation | Impaired early-endosomal trafficking; FERRY Rab5-effector complex |
| Key papers | Martin 2018 (PMID:30409806); Hüffmeier 2021 (PMID:33736665) | Rehman 2019 (DOI:10.1002/humu.23694); Schuhmacher 2023 FERRY (DOI:10.1016/j.molcel.2023.05.012) |

OMIM #618295 = MRT67 is unambiguously the ***EIF3F*** disorder ([OMIM 618295](https://www.omim.org/entry/618295); [MedGen C4749019](https://www.ncbi.nlm.nih.gov/medgen/?term=618295); confirmed by Hüffmeier 2021, which states: *"Bi-allelic variants in the EIF3F gene have recently been published as the cause for a syndromic neurodevelopmental disorder (NDD) (OMIM #618,295: intellectual developmental disorder, autosomal recessive 67)"*).

The cached files `DOI_10.1002_humu.23694.md`, `DOI_10.1016_j.molcel.2023.05.012.md`, `DOI_10.1101_2021.06.20.449167.md`, and `DOI_10.1101_2021.06.21.449265.md` are **PPP1R21/FERRY** references. They are legitimate curation inputs for El-Hattab-Schmidts syndrome but **must not be cited as evidence in an MRT67 entry** — doing so would be a Named Entity Confusion error of exactly the kind the dismech evidence SOP warns about. Note also that the two cached PPP1R21/FERRY *journal* files have `content_type: unavailable` (no body text), so no snippet could be verified from them in any case.

---

## 1. Disease Information

### Overview

MRT67 is a rare, syndromic, autosomal recessive neurodevelopmental disorder caused by biallelic variants in *EIF3F*, which encodes the f subunit of eukaryotic translation initiation factor 3 (eIF3) — the largest and most structurally complex of the eukaryotic initiation factors. Its mechanistic logic is unusual among Mendelian neurodevelopmental disorders: the primary lesion is a **partial, quantitative failure of general protein synthesis**, not the disruption of a neuron-specific protein or a discrete signalling pathway.

The clinical core is global developmental delay with prominent speech delay in essentially every reported individual, followed by a variable syndromic tail: behavioural problems, sensorineural hearing loss, altered muscle tone, short stature, microcephaly, ophthalmological findings, reduced pain sensitivity, sleep disturbance, and occasional orofacial clefting.

### Key identifiers

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#618295** — INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL RECESSIVE 67; MRT67 |
| MONDO | **MONDO:0032662** |
| MedGen | UID **1648350**, CUI **C4749019** |
| Gene (HGNC) | *EIF3F* — dismech CURIE form `hgnc:3275` |
| Cytoband | 11p15.4 |
| OMIM phenotypic series | PS249500 (autosomal recessive intellectual developmental disorders) |
| Orphanet | **No dedicated ORPHA entry was located in this session.** Orphanet's gene-based lookup for *EIF3F* did not resolve. Treat as "not available / needs verification" rather than absent. |
| ICD-10 / ICD-11 | No specific code. Coded generically (ICD-10 F70–F79 intellectual disability; ICD-11 6A00). |
| MeSH | No specific descriptor; indexed under *Intellectual Disability* + *Eukaryotic Initiation Factor-3* (see MeSH keywords on PMID:33736665). |

*Gene-level OMIM number for EIF3F was not verified in this session — do not assert one without checking.*

### Synonyms

- MRT67
- Mental retardation, autosomal recessive 67 (legacy OMIM/MedGen title)
- EIF3F-related neurodevelopmental disorder
- EIF3F-related syndrome (Simons Searchlight usage)
- EIF3F deficiency

### Nature of the evidence base

**Aggregated disease-level, not EHR-derived.** The entire published literature is small-*n* clinical genetics: one exome-wide burden analysis with case follow-up, one multi-centre GeneMatcher-assembled cohort, and scattered single-case reports. There is no registry, no natural-history study, and no EHR-phenotyped cohort. Simons Searchlight states plainly that *"the information available about EIF3F is limited"* and that **"As of 2025, about 31 people with EIF3F-related syndrome have been described in medical research"** ([Simons Searchlight](https://www.simonssearchlight.org/research/what-we-study/eif3f/)).

---

## 2. Etiology

### Disease causal factors

**Purely monogenic and genetic.** Biallelic *EIF3F* variants are necessary and, on current evidence, sufficient. No environmental, infectious, or toxic contribution has been proposed or investigated.

The founding association came from a genome-wide recessive burden analysis of the Deciphering Developmental Disorders study (Martin et al., *Science* 2018; PMID:30409806):

> "We identified two genes not previously associated with recessive developmental disorders, KDM5B and EIF3F, and functionally validated them with mouse and cellular models."

That study reported **nine affected individuals from seven non-consanguineous families of European ancestry**, all homozygous for the same missense allele ([OMIM 618295](https://www.omim.org/entry/618295)).

### Genetic risk factors

The disorder is driven by a single, dominant-in-frequency **founder allele**: `NM_003754.3:c.694T>G, p.(Phe232Val)`. Hüffmeier 2021 (PMID:33736665):

> "21 patients were homozygous and one compound heterozygous for c.694T>G/p.(Phe232Val) in EIF3F. Haplotype analyses in 15 families suggested that c.694T>G/p.(Phe232Val) was a founder variant."

Only one additional pathogenic allele has been published — the frameshift `c.861dup, p.(Gln288AlafsTer14)`, seen in *trans* with the founder missense in a single compound heterozygote.

**A key structural feature of this disease's genetics:** almost all recessive NDDs are caused by many private, mostly truncating variants across a handful of families. MRT67 inverts that. Hüffmeier 2021:

> "Therefore, an identical, rather frequent missense variant in EIF3F in almost all affected individuals is an uncommon finding in NDDs, particularly in a cohort with heterogeneous, ethnical and regional backgrounds."

The authors explicitly analogise to *CFTR* p.Phe508del, *HFE*, and *GJB2* founder alleles.

### Modifier genes

None established. One report (Huang 2022, PMID:35743796) describes a **heterozygous** *EIF3F* p.P4S variant as one of seven inherited rare variants in an oligogenic model of ID/ASD/psychosis in a Taiwanese proband. **This is not MRT67** — the individual was heterozygous, the variant is not the founder allele, and the authors propose only cumulative moderate effects. Cite it, if at all, as a hypothesis about heterozygote burden, never as MRT67 evidence.

### Environmental risk factors, protective factors, gene–environment interaction

**None described.** No CTD, GWAS, or exposure data exist for this entity. This is not a gap that could plausibly be filled by existing databases — it reflects the disorder's fully penetrant monogenic architecture and tiny cohort. Record explicitly as *not applicable / not studied* rather than leaving blank.

One indirect gene–environment observation exists in the **mouse**, and it is mechanistically interesting: *Eif3f* heterozygotes are normal at baseline but decompensate under a physiological stressor. Docquier 2019 (PMID:31026345):

> "We found that eIF3f partial depletion amplifies muscle atrophy compared to wild-type mice."

That is a gene-by-disuse interaction in muscle, not a disease risk factor in humans, but it is the closest thing in the literature.

---

## 3. Phenotypes

The definitive frequency table is Hüffmeier 2021 Table 2 (PMID:33736665), which reports the new cohort (n=21 evaluable) alongside the original Martin cohort (n=9). **Where the two disagree — most sharply on epilepsy — the disagreement itself is the finding.**

### Core, near-universal features

| Phenotype | HPO term | Frequency | Source |
|---|---|---|---|
| Global developmental delay | **HP:0001263** Global developmental delay | 21/21 (100%) and 9/9 (100%) | PMID:33736665 |
| Delayed speech and language development | **HP:0000750** | 21/21 (100%) | PMID:33736665 |
| Intellectual disability | **HP:0001249** | all individuals, variable degree | PMID:30409806, PMID:33736665 |
| Absent speech | **HP:0001344** | 5/21 (24%) | PMID:33736665 |

> "All affected individuals had developmental delays including delayed speech development. About half of the affected individuals had behavioral problems, altered muscular tone, hearing loss, and short stature." — PMID:33736665 (abstract)

**Motor milestone detail:** delayed unassisted sitting (>10 months) in 4/12 (33%); delayed independent walking (≥18 months) in 14/20 (70%). Severity is genuinely variable: *"one patient did not learn to walk independently, while most individuals learned walking late, and some individuals achieved motor milestones at a normal age."*

### Frequent features (~30–60%)

| Phenotype | HPO term | Frequency (Hüffmeier) | Frequency (Martin) |
|---|---|---|---|
| Behavioral abnormality | **HP:0000708** Atypical behavior | 12/21 (57%) | 3/9 (33%) |
| Sensorineural hearing impairment | **HP:0000407** | 12/21 (57%) | 3/9 (33%) |
| Abnormal muscle tone (hypo- **or** hyper-) | **HP:0003808** | 10/21 (48%) | not reported |
| Short stature (at last exam) | **HP:0004322** | 8/20 (40%) | 1/4 (25%) |
| Microcephaly at birth | **HP:0011451** Congenital microcephaly | 4/10 (40%) | 0/1 |
| Microcephaly (later) | **HP:0000252** | 6/19 (32%) | 1/8 (13%) |
| Hypermetropia / myopia | **HP:0000540** / **HP:0000545** | 8/21 (38%) | — |
| Nonspecific brain MRI findings | **HP:0012443** Abnormal brain morphology | 5/13 (38%) | 3/7 (43%) |
| Posteriorly rotated ears | **HP:0000358** | 7/20 (35%) | — |
| Deep-set / encased nails | **HP:0001800** Abnormal fingernail morphology | 6/20 (30%) | — |

Behavioural detail: *"obsessive compulsory disorder, social problems, anxiety, autism, hyperactivity, attention deficit, aggressivity or pica."* Autism has been formally instrumented in at least one case (Lakatosova 2024, PMID:39723281): *"The girl was diagnosed using Autism Diagnostic Observation Schedule-Second Edition (ADOS-2) and Autism Diagnostic Interview-Revised (ADI-R) instruments and met the criteria for autism spectrum disorder."*

### Occasional features (10–25%)

| Phenotype | HPO term | Frequency |
|---|---|---|
| Sleep disturbance | **HP:0002360** | 5/21 (24%) |
| Gastrointestinal symptoms (GERD, dysphagia, alternating constipation/diarrhoea, neonatal feeding problems) | **HP:0012719** Functional abnormality of the GI tract | 5/21 (24%) |
| Short hands/feet, slender digits | **HP:0001156** / **HP:0001773** | 5/20 (25%) |
| Nasal findings (tubular nose, pointed tip, anteverted nares) | **HP:0000429** Abnormal nose morphology | 5/20 (25%) |
| Developmental regression | **HP:0002376** | 3/21 (14%) |
| Strabismus | **HP:0000486** | 3/21 (14%) |
| Epilepsy / seizures | **HP:0001250** | **3/20 (15%) vs 6/7–6/9 (86%/67%) — see below** |
| Flat feet | **HP:0001763** Pes planus | 3/20 (15%) |
| 5th digit anomaly (shortness, clinodactyly) | **HP:0004209** Clinodactyly of the 5th finger | 3/20 (15%) |
| Cleft lip/palate (incl. minor forms) | **HP:0000202** Orofacial cleft | 2/20 (10%) |
| Meningioma | **HP:0100009** | 2/21 (10%) |
| Premature delivery | **HP:0001622** | 2/20 (10%) |

### Rare / single-case features

Reduced pain sensitivity (**HP:0007021** Pain insensitivity — 2 individuals, confirming a feature first seen by Martin); psychosis (**HP:0000709**, 1/21); encephalopathy (1/21, with concomitant B12 deficiency); nystagmus (**HP:0000639**, 1/21, 5%); coloboma (**HP:0000589**, 1/21, 5%); tetralogy of Fallot (**HP:0001636**, 1); congenital lobar emphysema; anal stenosis (**HP:0002025**); cryptorchidism (**HP:0000028**); nasal fistula; muscle atrophy (**HP:0003202**); drop attacks; arachnoid cyst (**HP:0100702**); prominent perivascular spaces; mild tonsillar ectopia (**HP:0002707** Abnormal cerebellum morphology).

**Overgrowth/macrocephaly — a phenotype-expanding outlier.** An ACMG 2024 abstract (Shad, Mbonu, Aguiar, Hassan, Repnikova; *Genetics in Medicine Open* P319, [doi:10.1016/j.gimo.2024.101213](https://www.gimopen.org/article/S2949-7744(24)00359-5/fulltext)) reports two male siblings homozygous for c.694T>G, one with typical features and the **older brother with additional overgrowth and macrocephaly** — the opposite direction from the cohort's microcephaly/short stature. This is a conference abstract, not peer-reviewed full text; grade accordingly.

**Neuroimaging in a single detailed case** (Lakatosova 2024, PMID:39723281): *"An MRI scan at 24 months of age showed randomly distributed cystic dilatations of the Virchow-Robin spaces bilaterally in the white matter, with a maximum concentration in the left parietal-temporal-occipital site, indicating atypical leukoencephalopathy. The findings also included an asymmetrically narrowed right internal auditory canal and cisterna magna."* Suggested terms: **HP:0002352** Leukoencephalopathy, **HP:0002185** Neuronal loss in central nervous system (no — prefer **HP:0012705** Abnormal cerebral white matter morphology), **HP:0002700** Enlarged cisterna magna.

### Phenotype characteristics

- **Onset:** congenital to infantile. Delays are apparent in the first two years. Pregnancy and delivery are largely uneventful (1/21 oligohydramnios; 1/19 suspected perinatal asphyxia).
- **Severity:** highly variable within an essentially uniform genotype — from near-normal motor milestones with usable speech to non-ambulatory and non-verbal.
- **Progression:** predominantly static/developmental. Regression is reported but confounded (see §11).
- **Dysmorphology:** subtle and **not gestalt-recognisable**. Hüffmeier 2021: *"Dysmorphic features were generally subtle and non-specific and were not considered a recognizable facial gestalt."* This matters clinically — you will not diagnose this on the face.

### Quality-of-life impact

No EQ-5D, SF-36, or PROMIS data exist. The one instrumented case (PMID:39723281) provides the only structured functional data in the literature: Vineland-3 showed *"a deeply below-average adaptive behavior profile in all subdomains of the test, including communication, daily living skills, socialization, and motor skills"*; BRIEF-P showed clinically elevated Inhibit, Working Memory, and Plan/Organize scales; the Children's Sleep Habits Questionnaire score was 48 against a cutoff of 41, with bedtime resistance and night waking most pronounced. The child had urinary and stool incontinence at 5y8m and a 10-word vocabulary.

---

## 4. Genetic / Molecular Information

### Causal gene

***EIF3F*** (eukaryotic translation initiation factor 3 subunit F), 11p15.4. HGNC CURIE in dismech form: `hgnc:3275`. Formerly *EIF3S5*. Encodes eIF3f, one of 13 subunits (eIF3a–m) of the eIF3 complex.

### Pathogenic variants

**1. `NM_003754.3:c.694T>G, p.(Phe232Val)` — the founder allele**

| Attribute | Value |
|---|---|
| dbSNP | **rs141976414** |
| GRCh38 | chr11:7,994,466 |
| GRCh37 | chr11:8,016,013 |
| Type | Missense (single nucleotide variant) |
| ClinVar | **RCV000754608**, germline classification **Pathogenic/Likely pathogenic**, 2-star review status (multiple submitters, no conflicts), 23 submissions (14 pathogenic / 7 likely pathogenic / 1 unclassified) |
| Origin | Germline |
| Functional consequence | Hypomorph / partial loss of function |

Population frequency, per Hüffmeier 2021:

> "This variant represents the 7th most common EIF3F missense variant in gnomAD (0.07%) with highest frequencies in Ashkenazi Jewish (0.21%) and non-Finnish European individuals (0.12%)"

> "In line with its pathogenicity, no individual in gnomAD was reported to be homozygous for this variant, in contrast to five of the six more frequent variants."

Independent ClinVar-submitter figures agree: allele frequency 0.0007 in 251,224 control chromosomes (gnomAD v2.1.1 total 0.000711), 0.0012 in non-Finnish Europeans, **no homozygotes**. The absence of homozygotes despite substantial heterozygote frequency is the population-genetic argument that carries most of the pathogenicity weight — five of the six *more common EIF3F* missense variants **do** have gnomAD homozygotes.

Functional characterisation (ClinVar interpretation summary): the variant *"results in reduced protein expression, approximately 70% of wildtype, and was associated with reduced protein translation and cellular proliferation rates."* Phe232 is evolutionarily conserved and predicted to stabilise the protein (PMID:39723281).

**2. `c.861dup, p.(Gln288AlafsTer14)` — frameshift**

Found in *trans* with the founder allele in one individual (P3 in Hüffmeier 2021). Absent from gnomAD. *"was predicted to result in a frameshift and subsequently either in mRNA decay or a truncated protein (length reduced by 20%, exon 6 of 8) with altered structure."*

### Constraint and the null-lethality argument

> "Of note, the overall number of truncating alleles in individuals in gnomAD v2.1.1 is extremely low (probability of being loss-of-function intolerant = 0.97, observed over expected variants = 0.07). Regarding lack of individuals with two truncating variants and of further affected individuals who are compound heterozygous for truncating variants, one might speculate that truncating variants on both alleles might not be compatible with life." — PMID:33736665

This is the single most important mechanistic inference in the disease, and it is triangulated three ways: (i) pLI 0.97 / o/e 0.07 constraint; (ii) no reported patient with two truncating alleles; (iii) **mouse *Eif3f*-null embryonic lethality** (§15). The founder allele is best read as a **hypomorph that survives where a null would not**.

### Genotype–phenotype correlation

Exactly one signal, from the single compound heterozygote:

> "Symptoms in the compound heterozygous individual with an additional truncating variant were at the severe end of the spectrum in regard to motor milestones, speech delay, organic problems and pre- and postnatal growth of body and head, suggesting some genotype-phenotype correlation." — PMID:33736665

That individual did not walk independently at age 5 (crawled), had no speech, tetralogy of Fallot, GI problems, IUGR, and was both short and microcephalic. This is a **dosage** disease: missense/missense < missense/null < null/null (lethal).

**Other missense variants are of unknown consequence.** Hüffmeier 2021 is explicit: *"As only the identical missense variant in EIF3F has been functionally characterized … it remains speculative whether other missense variants might have comparable effects."* Do not extrapolate pathogenicity from p.Phe232Val to novel *EIF3F* missense variants without functional work.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified.
- **Epigenetics:** no methylation episignature has been reported for *EIF3F*. Nothing in ENCODE/Roadmap/DiseaseMeth is disease-specific. Record as not studied.
- **Chromosomal abnormalities:** not a mechanism. CMA is characteristically **negative** in these patients — both the Lakatosova case (*"Microarray analysis of CNVs (aCGH) showed negative findings"*) and routine workups. This is diagnostically important (§10).
- **Somatic variation:** MRT67 is germline. Somatic *EIF3F* variants were surveyed in COSMIC for an unrelated reason (the meningioma question, §11): *"somatic EIF3F variants have been detected in 0.9% of 38,579 samples (n = 353) and did not include 130 meningioma samples."*

---

## 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents are implicated in MRT67. Searching CTD/TOXNET/NHANES for this entity is not a productive use of curation effort. Any dismech `environmental:` block should either be absent or carry a `notes:` line recording that the search was made and returned nothing, so a later curator does not repeat it.

---

## 6. Mechanism / Pathophysiology

### The causal chain

```
EIF3F c.694T>G p.(Phe232Val) homozygous  [MOLECULAR]
        ↓  reduced eIF3f protein (~70% of wild-type)
Reduced eIF3f abundance in the eIF3 complex  [MOLECULAR]
        ↓
Reduced global translation initiation rate  [CELLULAR]
   (↓ polysome content, ↓ protein synthesis rate, ↓ mTOR pathway activation)
        ↓
Reduced cell proliferation and cell growth  [CELLULAR]
        ↓
Impaired brain development and somatic growth  [ORGANISM]
   → GDD, ID, speech delay, microcephaly, short stature, altered muscle tone
```

**Upstream** is the variant → protein-abundance step (measured). **Midstream** is the translation → proliferation step (measured in iPSCs and mouse muscle). **Downstream** is the step to clinical phenotype, which is **inferred, not measured** — no neural model of the disease allele has been published.

### Molecular pathway: translation initiation

eIF3 stimulates multiple steps of initiation — 43S pre-initiation complex assembly, mRNA recruitment, prevention of premature 60S joining, AUG scanning (Moretti 2010, PMID:21124883). Crucially, eIF3 is **not** a uniform amplifier:

> "EIF3F encodes an essential subunit of the largest eukaryotic translation initiation factor eIF3 which binds to a highly specific group of mRNAs involved in cell proliferation and growth, including cell cycle control, differentiation and apoptosis" — PMID:33736665

That selectivity is the best available answer to the obvious objection — *why does a housekeeping translation factor produce a selective neurodevelopmental phenotype rather than uniform cellular failure?*

**GO terms:**
- **GO:0003743** translation initiation factor activity (modifier: DECREASED)
- **GO:0006413** translational initiation (DECREASED)
- **GO:0005852** eukaryotic translation initiation factor 3 complex (cellular component)
- **GO:0002181** cytoplasmic translation (DECREASED)
- **GO:0008283** cell population proliferation (DECREASED)
- **GO:0031929** TOR signaling (DECREASED)
- **GO:0007420** brain development (ABNORMAL)

**Reactome:** R-HSA-72613 (Eukaryotic Translation Initiation), R-HSA-72649 (Translation initiation complex formation). **KEGG:** hsa03013 (Nucleocytoplasmic transport/RNA transport).

### The mTORC1 coupling — how a translation defect becomes a growth defect

This is the best-characterised non-canonical arm and it is where the mouse data land. eIF3f is a **scaffold** connecting mTORC1 and S6K1:

- Under nutrient-rich conditions, the mTOR/raptor complex binds the TOS motif of eIF3f and phosphorylates/activates S6K1; active S6K1 is released from eIF3, increasing protein synthesis (Csibi et al., *PLoS ONE* 2010, [doi:10.1371/journal.pone.0008994](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0008994)).
- Conversely, the E3 ligase MAFbx/atrogin-1 physically interacts with the Mov34 domain of eIF3f via its leucine-charged domain, polyubiquitinating it for proteasomal degradation during muscle wasting. An eIF3f mutant insensitive to MAFbx polyubiquitination maintains S6K1/rpS6 phosphorylation.
- eIF3f thus sits at the **atrophy/hypertrophy antagonism** node in skeletal muscle (reviewed PMID:23769948).

In vivo confirmation, Docquier 2019 (PMID:31026345):

> "Skeletal muscles of heterozygous mice show a deficiency in polysome content, a decrease in protein synthesis rate and an inhibition of the mechanistic target of rapamycin (MTOR) pathway."

Hüffmeier 2021 draws the link explicitly: *"partial depletion of murine eIF3f amplified muscle atrophy compared to wild-type mice and reduced the MTOR pathway activation."*

**This is mechanistically load-bearing for the human phenotype** because it supplies a route from reduced eIF3f → reduced mTORC1 signalling → reduced growth, which is otherwise a hand-wave. GO: **GO:0031929** TOR signaling; **GO:0038202** TORC1 signaling.

### Moonlighting function 1: deubiquitinase activity on Notch

eIF3f carries an MPN/JAMM domain and has intrinsic DUB activity (Moretti 2010, PMID:21124883):

> "An immunofluorescence-based screening of an shRNA library allowed us to identify eIF3f, previously known as one of the subunits of the translation initiation factor eIF3, as a DUB targeting the activated Notch receptor. We show that eIF3f has an intrinsic DUB activity."

> "we also show that eIF3f is recruited to activated Notch on endocytic vesicles by the putative E3 ubiquitin ligase Deltex1, which serves as a bridging factor … eIF3f is a new positive regulator of the Notch pathway."

**Curation caution:** this is elegant *in vitro* cell-biology (U2OS, HEK293T, HeLa; shRNA knockdown; coculture reporter assays) and it has **never been connected to MRT67 patient biology**. Notch signalling is central to neurodevelopment, so the temptation to draw a causal edge from p.Phe232Val → impaired Notch → neurodevelopmental phenotype is strong — and unsupported. Phe232 has not been shown to affect DUB activity. If curated at all, this belongs in a `discussions:` block as a `KNOWLEDGE_GAP` with a proposed experiment, not as a pathophysiology edge. GO: **GO:0004843** cysteine-type deubiquitinase activity; **GO:0007219** Notch signaling pathway.

### Moonlighting function 2: white matter and RAN translation

eIF3f regulates repeat-associated non-ATG (RAN) translation in spinocerebellar ataxia type 8 (Ayhan et al., *EMBO J* 2018, PMID:30206144): knockdown of eIF3F reduces steady-state levels of SCA8 polySer and other RAN proteins, and the polySer aggregates accumulate preferentially in **white matter regions showing demyelination and axonal degeneration**.

Lakatosova 2024 (PMID:39723281) uses this to interpret their patient's leukoencephalopathy:

> "EIF3F was shown to be overexpressed in white matter compared to gray matter in various brain regions [19,20], suggesting its importance in myelination and white matter homeostasis, including regulation of oligodendrocyte functions."

**Grade this carefully.** It is a single-case imaging finding plus an inference from a different disease's biology. Note also that the Human Protein Atlas reports *EIF3F* as **low tissue specificity** (tau 0.21, "detected in all"), clustering with ribosomal/translation genes and showing *no* white-matter or neuron-enriched pattern ([HPA ENSG00000175390](https://www.proteinatlas.org/ENSG00000175390-EIF3F/tissue)). The white-matter-enrichment claim and the HPA data are in tension. Curate as a hypothesis with the tension recorded, not as an established mechanism.

### Cell types, tissues, subcellular compartments

- **Subcellular:** cytoplasm (**GO:0005737**), eIF3 complex (**GO:0005852**), cytosolic ribosome-associated (**GO:0022626**), and — for the Notch DUB function — early endosome (**GO:0005769**).
- **Cell types:** no disease-specific cell type is established. Speculative/inferred candidates only: **CL:0000540** neuron, **CL:0000128** oligodendrocyte (from the white-matter hypothesis), **CL:0000187** muscle cell (from mouse), **CL:0002322** embryonic stem cell (the model system actually used).
- **Do not manufacture a cell-type binding.** The measured cellular work was done in undifferentiated iPSCs and mouse skeletal muscle. Neither is the affected tissue in patients.

### Molecular profiling

- **Transcriptomics:** no patient RNA-seq published. No GEO series specific to MRT67 was identified.
- **Proteomics / metabolomics / lipidomics:** none.
- **Single-cell / spatial:** none.
- **Functional genomics:** *EIF3F* is a broadly essential gene in DepMap-class screens (consistent with pLI 0.97 and mouse null lethality), but no MRT67-specific screen exists.

**This is a real and citable gap.** No omics dataset exists for this disorder in any repository. Any `datasets:` block would have to be gene-level or model-level, and per dismech policy would need `just verify-datasets` plus manual relevance triage — searching *EIF3F* in GEO will return translation-biology and cancer datasets that are **not about this disease** (the classic Named Entity Confusion trap).

---

## 7. Anatomical Structures Affected

### Organ level

| Level | Structure | UBERON |
|---|---|---|
| Primary | Brain / central nervous system | **UBERON:0000955** brain; **UBERON:0001017** CNS |
| Primary | Cerebral white matter (single case) | **UBERON:0002316** white matter |
| Primary | Inner ear / cochlea (sensorineural HL) | **UBERON:0001846** internal ear; **UBERON:0001844** cochlea |
| Secondary | Skeletal muscle (tone, hypoplasia, atrophy) | **UBERON:0001134** skeletal muscle tissue |
| Secondary | Eye (refractive error, strabismus, nystagmus, coloboma) | **UBERON:0000970** eye |
| Secondary | Gastrointestinal tract (functional) | **UBERON:0001555** digestive tract |
| Rare | Lip and palate | **UBERON:0001833** lip; **UBERON:0001716** secondary palate |
| Rare | Heart (tetralogy of Fallot, 1 case) | **UBERON:0000948** heart |
| Rare | Lung (congenital lobar emphysema, 1 case) | **UBERON:0002048** lung |
| Rare | Testis (cryptorchidism) | **UBERON:0000473** testis |

**Body systems:** nervous, sensory (auditory, visual), musculoskeletal, digestive; growth as a cross-cutting axis.

### Lateralization

Predominantly **bilateral and symmetric** where laterality is reported (bilateral mild SNHL; bilateral Virchow-Robin space dilatation). Two asymmetric findings in the single detailed imaging case: right internal auditory canal stenosis, and left parieto-temporo-occipital predominance of the perivascular changes (PMID:39723281). One unilateral single palmar crease was noted in four individuals.

### The negative finding is important

> "In concordance with the previous study, brain imaging did not reveal specific findings and were therefore not considered diagnostically indicative in EIF3F related NDD." — PMID:33736665

There is **no structural lesion to point at**. Nonspecific findings in ~38–43% across both cohorts. This is consistent with a diffuse quantitative translation deficit rather than a focal developmental malformation, and it is why the disease is diagnosed by sequencing, not imaging.

---

## 8. Temporal Development

### Onset

- **Congenital to early infantile.** Developmental delay is the presenting feature. Microcephaly and short stature may be present at birth (4/10 and 3/15 respectively) or acquired later.
- **Onset pattern:** insidious, developmental — not acute.
- Pregnancy/delivery largely uneventful; 2/20 premature.

### Progression

- **Predominantly static.** No defined disease stages. Most affected individuals show delay rather than deterioration.
- **Growth trajectory is informative:** head circumference tracks its centiles more steadily than height does. Hüffmeier 2021: *"longitudinal data indicated that head growth had a more constant course along the centiles than height."* Four of seven individuals with short stature at last exam had **normal length at birth** — so the stature phenotype is at least partly postnatally acquired, not purely prenatal.
- **Duration:** chronic, lifelong.
- **Cohort maturity caveat:** mean age at last exam 12.1 ± 9.6 years (median 8.5); only four individuals were over 18. The natural history beyond young adulthood is essentially unknown.

### Regression — an unresolved question

> "Developmental regression or neurodegeneration at various ages (2.5 to ~ 30 years) was observed in three of the 20 affected individuals which might be relevant for prognosis. However, two of the three individuals had additional diagnoses that are not necessarily related to this syndromic disorder" — PMID:33736665

The confounds were vitamin B12-deficiency encephalopathy in one and meningioma-associated psychosis in another. The authors decline to resolve it: *"The cohort size and the relatively young ages of the majority of individuals did not allow conclusions as to whether those symptoms are part of the disease spectrum or might have an independent cause."* Curate as `supports: PARTIAL` with the confound stated.

### Critical periods

Not defined in humans. In mouse, the critical window for complete loss is **peri-implantation**: *Eif3f*<sup>-/-</sup> embryos *"die at an early stage of development but after the pre-implantation stage"* (PMID:31026345). No intervention window has been identified in patients.

---

## 9. Inheritance and Population

### Inheritance

**Autosomal recessive** (**HP:0000007**). All tested parents were heterozygous carriers and essentially unaffected:

> "All tested parents were heterozygous carriers of the variant (parents of pedigree 16 (P16) were not available for testing)." — PMID:33736665

> "Heterozygous carriers were mainly asymptomatic. One father was reported to have epilepsy, and one mother migraines. Those overlapping symptoms are likely unrelated and of different etiology." — PMID:33736665

Recurrence risk for siblings: **25%**, as counselled in the Slovak case (PMID:39723281).

- **Penetrance:** appears complete for the biallelic genotype in ascertained families. No unaffected homozygote has been reported — though ascertainment bias is total here, and the absence of gnomAD homozygotes is consistent with either full penetrance or embryonic/early attrition.
- **Expressivity:** **markedly variable**, with an essentially uniform genotype. This is the disease's defining epidemiological puzzle and no modifier has been found.
- **Anticipation:** not applicable (not a repeat expansion).
- **Germline mosaicism:** not reported.

### Consanguinity — and why it matters here

Parental consanguinity in only **1/17 (6%)** of families in Hüffmeier 2021 and **0/7** in Martin 2018. For a recessive NDD, that is remarkable, and it is a direct consequence of the founder allele being common enough that two unrelated carriers meet by chance. **Practical implication: absence of consanguinity is not a reason to deprioritise a recessive hypothesis in a European-ancestry proband.**

### Founder effect

> "This revealed that the EIF3F variant was on an identical haplotype (minimal 7.8 kb) in 15 affected individuals of all tested families, suggesting a founder variant."

The founding haplotype (C-C-A-C-C-G-C across rs79714374, rs12421289, rs12278319, rs7941782, rs4758267, rs12420464, rs56392532) had a frequency of 3.5% in 1,818 internal German control exomes. The variant arose once; *"the nascence of the missense variant cannot be determined to a more localized region."*

### Carrier frequency and derived prevalence

Reported carrier/allele frequencies (gnomAD v2.1.1):

| Population | Allele frequency |
|---|---|
| Overall | 0.07% (0.000711) |
| Non-Finnish European | 0.12% |
| Ashkenazi Jewish | 0.21% |

**Derived birth prevalence — my own Hardy-Weinberg arithmetic, not a published figure:** q² for NFE ≈ (0.0012)² ≈ 1.4 × 10⁻⁶ ≈ **1 in ~690,000**; for Ashkenazi Jewish ≈ (0.0021)² ≈ 4.4 × 10⁻⁶ ≈ **1 in ~230,000**. Carrier frequency ≈ 1 in 420 (NFE) and 1 in 240 (AJ). Label these clearly as derived; they are almost certainly higher than observed diagnosed prevalence, and the gap between ~31 published patients and this expectation is the size of the under-diagnosis problem.

### Epidemiology

- **Prevalence: not determined.** PMID:39723281 states plainly: *"the population frequency of this syndromic disorder has not been determined since then."*
- **Cases in literature: ~31** as of 2025 (Simons Searchlight), consistent with 9 (Martin) + 22 (Hüffmeier) + scattered singles.
- For a dismech `prevalence:` block: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE`, with the derived HWE estimate in `notes` — **not** in `rate_per_100000`, since it is an inference rather than an observation.

### Demographics

- **Ancestry:** European and West Asian. Hüffmeier 2021 lists *"French, English, Irish, Scottish, German, Bulgarian, Ukranian, Russian, Ashkenazi Jewish, and Iraqi."* Plus Slovak (PMID:39723281). No African, East Asian, or South Asian cases reported — consistent with a European founder allele, though ascertainment in European genomics cohorts inflates this.
- **Sex ratio:** 15 F : 7 M (Hüffmeier) and 5 F : 4 M (Martin) — **no evidence of sex bias**; the female excess in the larger cohort is unremarkable at this sample size and there is no biological reason to expect one for an autosomal recessive disorder. Report as ~1:1.
- **Age distribution:** ascertained pediatric (median 8.5 y); adults under-represented.

---

## 10. Diagnostics

### The diagnostic route is sequencing, full stop

Everything else is negative or nonspecific:

| Test | Expected result |
|---|---|
| Karyotype | Normal (46,XX in the Slovak case) |
| Chromosomal microarray / aCGH | **Negative** — *"Microarray analysis of CNVs (aCGH) showed negative findings"* (PMID:39723281) |
| Brain MRI | Nonspecific in ~38–43%; *"not considered diagnostically indicative"* |
| Routine biochemistry | No specific abnormality; no biomarker exists |
| Methylation (15q11.2-q13) | Negative |

### Genetic testing

**Recommended approach: WES or WGS, or an ID/ASD gene panel that includes *EIF3F*.** Hüffmeier 2021 is unambiguous: *"Thus, genome-wide sequencing approaches (genome or exome sequencing) represent an essential component of the diagnostic work-up."* Lakatosova 2024 makes the same argument as a health-systems point for Slovakia.

- ***EIF3F* is on Genomics England PanelApp as a GREEN (high-evidence) gene** on the "Early onset or syndromic epilepsy" panel (panel 402), mode of inheritance BIALLELIC, phenotypes: MRT67 (OMIM:618295), intellectual disability, seizures, behavioral abnormality, sensorineural hearing impairment ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/402/gene/EIF3F/)).
- **SFARI Gene score: 3 (Suggestive Evidence)** for autism, with 8 supporting reports ([SFARI](https://gene.sfari.org/database/human-gene/EIF3F)).
- **Targeted single-variant testing is genuinely viable here** — unusually for a recessive NDD. Because one founder allele explains ~95% of reported cases, Sanger or targeted genotyping of c.694T>G is a reasonable low-cost first-line test in a European-ancestry proband with GDD + speech delay + SNHL, and is the natural cascade/carrier test in families.

### A diagnostic pitfall worth flagging explicitly

The founder allele sits at **0.12% in non-Finnish Europeans**. Many recessive-model variant-filtering pipelines apply a minor-allele-frequency cutoff at or near 0.1% and would **discard this variant before a human ever sees it**. Combined with the absence of a recognisable facial gestalt and uninformative MRI, this is a plausible mechanism for systematic under-diagnosis. (This inference is mine, but it follows directly from the reported AF and from Hüffmeier's own observation that carrier frequency here *"is higher than for most other autosomal recessive NDDs."*)

### Adjunct clinical assessments (not diagnostic, but indicated once the diagnosis is made)

- **Audiology** — SNHL in ~57%, and undetected hearing loss in a child with speech delay will be mis-attributed to the developmental delay. This is the highest-yield adjunct test.
- **Ophthalmology** — refractive error/strabismus/nystagmus/coloboma in up to 38%. Note Hüffmeier's own caveat that hyper-/myopia *"might not necessarily be related to EIF3F deficiency, as they are common in the general population."*
- **Growth monitoring** with head circumference plotted longitudinally.
- **Sleep assessment** (CSHQ used in the Slovak case).
- **Developmental/behavioural assessment**: ADOS-2, ADI-R, Vineland-3, BRIEF-P, SON-R all used in published assessment.
- **EEG** if seizures are suspected.

**LOINC:** no disease-specific analyte. **No biomarker, enzyme assay, or metabolite is known.** Do not curate one.

### Differential diagnosis

| Condition | Distinguishing feature |
|---|---|
| Rett syndrome (*MECP2*) | Overlaps substantially — one individual in Hüffmeier 2021 (P2) carried **both** a homozygous *EIF3F* variant and a de novo *MECP2* frameshift, and was excluded from the phenotype summary for exactly that reason. Regression pattern and hand stereotypies favour Rett. |
| Angelman syndrome | Tested and excluded in reported patients; methylation/UBE3A. |
| Fragile X | Tested and excluded. |
| Russell-Silver syndrome | Two individuals had prior targeted testing for short stature / FTT. |
| Phelan-McDermid (22q13 del) | CMA-detectable; MRT67 CMA is negative. |
| Other AR ID syndromes (PS249500, 70 entities) | Distinguished only by sequencing. |
| **PPP1R21-related El-Hattab-Schmidts syndrome** | Coarse facies (thick arched eyebrows, thick vermilion), optic atrophy — a different gene and a different mechanism. Included here because the naming similarity is a genuine curation hazard. |

### Screening

- **Newborn screening:** not included anywhere; no biochemical marker exists to screen for.
- **Carrier screening:** *EIF3F* is not on standard expanded carrier screening panels as far as could be determined. Given the AJ frequency of 0.21%, inclusion on Ashkenazi-focused panels would be a defensible proposal — **this is my inference, not a published recommendation.**
- **Cascade screening:** straightforward and appropriate once a familial variant is known.

---

## 11. Outcome / Prognosis

**Be honest about how thin this is.** There is no natural-history study, no survival analysis, and no validated prognostic model.

### Survival and mortality

- **No deaths attributable to MRT67 have been reported.** Individuals have been described up to 48 years (Martin cohort) and ~30 years (Hüffmeier cohort).
- **Life expectancy: unknown, but not obviously shortened** on current evidence. Do not assert a figure.
- The one hard mortality statement in the literature is about the **null genotype**, which appears incompatible with life (no human reported; mouse embryonic lethal).

### Morbidity and function

Lifelong intellectual disability of variable degree with major communication impairment (24% never develop speech). The single instrumented case showed *"deeply below-average"* adaptive functioning across all Vineland domains. Most affected individuals will require lifelong support; some achieve simplified but usable language and independent ambulation.

No EQ-5D/SF-36/PROMIS/ICF data exist.

### Complications

- Sequelae of SNHL on language acquisition.
- Injury risk from reduced pain sensitivity (a practical safety issue, though no incident data exist).
- Feeding/GI problems in ~24%.
- Surgical burden where clefting or congenital heart disease is present.

### The meningioma question — genuinely unresolved

Two of 21 individuals (10%) had meningioma, and a third had psychosis co-occurring with meningioma. In a cohort of median age 8.5 years that is a striking number. Hüffmeier 2021 checked and reported a **negative** result:

> "In large collections of malignancies (COSMIC; accessed on 3rd of December 2020 at cancer.sanger.ac.uk), somatic EIF3F variants have been detected in 0.9% of 38,579 samples (n = 353) and did not include 130 meningioma samples, providing no further evidence for a role of EIF3F in tumorigenesis of meningioma"

Two events in 21 people is not a tumour-predisposition claim, and the somatic data do not support one. But it is also not nothing, and it is the single most consequential open question for surveillance recommendations. Curate as a `discussions:` `KNOWLEDGE_GAP` with the COSMIC negative recorded — **not** as a phenotype with an asserted frequency, and certainly not as a basis for recommending imaging surveillance.

### Prognostic factors

The only signal is genotype: the compound heterozygote (missense + frameshift) sat at the severe end for motor milestones, speech, organ involvement, and pre-/postnatal growth. No biomarkers, no imaging predictors.

---

## 12. Treatment

### There is no disease-specific or disease-modifying therapy.

No approved drug, no gene therapy, no ASO, no cell therapy, no clinical trial. A search of ClinicalTrials.gov concepts for *EIF3F*/MRT67 surfaces nothing interventional. **Say this plainly rather than assembling a speculative pipeline.**

Management is supportive, symptom-directed, and multidisciplinary — as practised in the reported cases, where the Slovak child was *"under the care of several clinical specialists, including neurologists, otorhinolaryngologists, psychologists, and a speech therapist."*

### Supportive and rehabilitative care (with NCIT terms)

| Intervention | NCIT term | Rationale |
|---|---|---|
| Speech and language therapy | `NCIT:C159273` Speech Therapy | Speech delay is universal and the most severely affected domain |
| Physical therapy | `NCIT:C15302` Physical Therapy | Motor delay, altered tone |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | Adaptive function deficits |
| Rehabilitation (general) | `NCIT:C15315` Rehabilitation | Umbrella term |
| Supportive care | `NCIT:C15747` Supportive Care | Umbrella term |
| Genetic counseling | `NCIT:C15240` Genetic Counseling | 25% sibling recurrence risk |
| Antiseizure pharmacotherapy | `NCIT:C15986` Pharmacotherapy | Where epilepsy present; no agent-specific data |
| Behavioral counseling / intervention | `NCIT:C181743` Behavioral Counseling | Behavioural problems in ~57% |
| Surgical repair of cleft lip/palate | `NCIT:C15329` Surgical Procedure | Where present; one case documented pre- and post-correction |
| Cardiac surgery | `NCIT:C15329` Surgical Procedure | Tetralogy of Fallot, 1 case |

`therapeutic_modality` for the therapy/counselling entries: `BEHAVIORAL`; for surgery: `SURGERY`; for antiseizure drugs: `SMALL_MOLECULE`.

**Hearing amplification** is clinically indicated given ~57% SNHL, but note the dismech-specific constraint: there is **no reliable NCIT clinical-action term for device usage** (the former "hearing aid usage" term had no NCIT equivalent and was dropped in the MAXO removal), so a hearing-aid treatment entry should carry `therapeutic_modality: DEVICE` with a free-text `preferred_term` and **no** `term:` binding.

### Pharmacogenomics

None. No *EIF3F* entry in PharmGKB/CPIC relevant to this disorder.

### A speculative therapeutic direction — label it as such

The mTORC1 coupling (§6) raises the theoretical question of whether pathway modulation could compensate for reduced eIF3f-dependent S6K1 activation. **Nothing supports this in patients.** Direction of effect is also non-obvious: the defect is *reduced* mTOR activation, so an mTOR inhibitor would be expected to worsen it, and there is no validated agonist strategy. Record as a hypothesis in `discussions:` if at all; do not curate as a treatment.

### Antipsychotics — a cautionary observation

In the *EIF3F*-heterozygous oligogenic case (PMID:35743796, which is **not** MRT67), both siblings *"responded poorly to pharmacotherapy"* and one failed ECT. In the one MRT67 individual with psychosis, the psychosis co-occurred with a meningioma. Neither supports a treatment-response claim for MRT67. Mentioned only to forestall over-reading.

---

## 13. Prevention

### Primary prevention

There is no way to prevent the disease in a conceptus who inherits two pathogenic alleles. Prevention here means **reproductive risk management**:

- **Genetic counseling** (`NCIT:C15240`) with a 25% sibling recurrence risk, as delivered in the Slovak case: *"The identification of the causal variant c.694T>G, p.(Phe232Val) in the EIF3F gene indicates a 25% recurrence risk in potential siblings of the patient, due to its autosomal recessive mode of inheritance, as explained by the clinical geneticist to the parents of the proband."* (PMID:39723281)
- **Carrier testing** of at-risk relatives (cascade testing on the familial variant).
- **Prenatal diagnosis and preimplantation genetic testing (PGT-M)** are technically straightforward once the familial variant is known. No published MRT67-specific experience.
- **Population carrier screening:** not currently offered. The AJ allele frequency of 0.21% makes a case for consideration on Ashkenazi panels — again, my inference, not a guideline position.

### Secondary prevention (early detection and intervention)

The realistic wins are all here, and they follow from the phenotype frequencies:

1. **Early audiological assessment** — the single highest-value intervention, because untreated SNHL compounds an already-universal speech delay and is present in over half of patients.
2. **Early developmental intervention** — speech, physical, and occupational therapy.
3. **Ophthalmological review** — correctable refractive error and strabismus.
4. **Growth surveillance** with plotted centiles.

### Tertiary prevention

- **Injury surveillance in individuals with reduced pain sensitivity** — a child who does not report pain normally is at risk of unrecognised fracture, burn, or intra-abdominal pathology. This follows from the phenotype and is standard practice in congenital insensitivity to pain; it is not written down anywhere for MRT67.
- Nutritional monitoring where GI symptoms or feeding difficulty are present. Note the individual whose "regression" turned out to involve **vitamin B12 deficiency** — a reminder that treatable causes should be excluded before attributing deterioration to the underlying disorder.
- Seizure management where epilepsy is present.

### Immunization, public health, environmental interventions, prophylaxis

**Not applicable.** Standard childhood immunisation as for any child; nothing disease-specific.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* **NCBITaxon:9606**; *Mus musculus* **NCBITaxon:10090** (experimental only).
- **Breed:** not applicable — no breed-associated disease. No VBO term.
- **Orthologous gene:** *Eif3f*, mouse, **MGI:1913335**. eIF3 is deeply conserved across eukaryotes; eIF3f orthologues exist throughout metazoa and in yeast the eIF3 core is conserved though subunit composition differs (mammalian eIF3 has 13 subunits including five non-PCI/MPN subunits — Moretti 2010).
- **Naturally occurring disease in other species: none known.** No OMIA entry was identified for an *EIF3F* orthologue phenotype. Record as not applicable.
- **Veterinary relevance:** none.
- **Comparative pathology:** the mouse does **not** reproduce the human disease (§15). The comparative story is one of divergence, not convergence — complete loss is embryonic-lethal in mouse and (inferentially) in human, while the human hypomorphic missense allele has no mouse counterpart.
- **Evolutionary conservation:** Phe232 is *"evolutionarily conserved and is predicted to stabilize the protein"* (PMID:39723281), which is part of the pathogenicity argument.
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### Mouse — the only in vivo model, and it does not model the disease

**Model 1: *Eif3f*-null homozygote (`Eif3f^-/-`)** — Docquier et al. 2019, PMID:31026345

> "We showed that homozygous eIF3f knockout fail to develop and that eIF3f-/- embryos die at an early stage of development but after the pre-implantation stage."

- **Relationship to disease:** `PERTURBS`, **fidelity LOW**. This genotype exists in no patient and produces a qualitatively different outcome (embryonic lethality, not a neurodevelopmental disorder).
- **What it is good for:** bounding the mechanism from the severe end. It is the experimental leg of the tripod supporting "the human founder allele must be hypomorphic."
- MGI/IMPC classify this line as **lethal** (no live homozygous null pups) ([MGI:1913335](https://www.informatics.jax.org/marker/MGI:1913335)).

**Model 2: *Eif3f* heterozygote (`Eif3f^+/-`)** — same paper

> "Although heterozygous mice are phenotypically indistinguishable from wild-type mice, they present a diminished body weight and a lean mass reduction associated with normal body size."

> "Skeletal muscles of heterozygous mice show a deficiency in polysome content, a decrease in protein synthesis rate and an inhibition of the mechanistic target of rapamycin (MTOR) pathway."

> "Interestingly, skeletal muscles are mainly affected and display an altered cell size without modification of fibre number."

> "We found that eIF3f partial depletion amplifies muscle atrophy compared to wild-type mice."

- **Relationship to "Reduced Global Translation Initiation":** `RECAPITULATES`, **fidelity MODERATE**. It reproduces the translational deficit itself and identifies the mTOR coupling.
- **Relationship to "Reduced Cell Proliferation and Growth":** `PARTIALLY_RECAPITULATES`, **fidelity MODERATE** — a cell-size rather than cell-number deficit, with normal body size.
- **Limitations (required for any dismech model link):** measurements were made in **skeletal muscle, not brain**; the animal carries a **null on one allele**, not the human missense on both; heterozygous mice are behaviourally and developmentally normal, so the model captures the biochemistry of partial eIF3f depletion **without reproducing the neurodevelopmental phenotype at all**. MGI additionally notes partial prenatal lethality in heterozygotes.

**Readouts available for curation** (`ExperimentalReadout`): polysome content (DECREASED), protein synthesis rate (DECREASED), mTOR pathway activation (DECREASED), lean mass (DECREASED), muscle fibre cross-sectional area (DECREASED), fibre number (UNCHANGED — a real negative result worth recording).

### Cellular models

**Gene-edited iPSCs homozygous for c.694T>G** — the isogenic model on which the loss-of-function interpretation rests (Martin 2018, described in Hüffmeier 2021):

> "In vitro studies of induced pluripotent stem cells (iPSC), gene-edited to be homozygous for the c.694T>G/ p.(Phe232Val) variant, demonstrated lower EIF3F protein levels and reduced proliferation rates"

> "Furthermore, both heterozygous and homozygous variants reduced translation rates in iPSC cells"

Quantified via ClinVar submitter summary as **~70% of wild-type protein expression**.

- **Fidelity:** this is the *right allele in human cells*, which is its major strength — and it is **undifferentiated stem cells**, which is its major limitation. No neuronal, cerebral-organoid, oligodendrocyte, or cochlear model of the disease allele has been published.

**Other cell systems (mechanism, not disease):** U2OS, HEK293T, HeLa, and MEF lines with shRNA knockdown for the Notch/DUB work (PMID:21124883); C2C12 myotubes for the mTORC1/MAFbx work; cell lines for SCA8 RAN-translation modulation (PMID:30206144). None carries the disease allele.

### The largest model gap

**There is no neural model of MRT67.** The disease is a brain disorder; the cellular work is in undifferentiated iPSCs and the in vivo work is in mouse muscle. This is precisely the situation the dismech schema's `HUMAN_MODEL_MISMATCH` discussion kind exists for — evidence exists in models, but its translational validity to the human neurodevelopmental phenotype is the open question. Obvious proposed experiments: differentiate the existing isogenic iPSC lines to cortical neurons and cerebral organoids and measure translation rate, proliferation, and neurite/network phenotypes; generate a *Eif3f* p.Phe232Val knock-in mouse (which does not currently exist).

### Model resources

- MGI: [MGI:1913335](https://www.informatics.jax.org/marker/MGI:1913335)
- IMPC: mousephenotype.org (note: the search result found *no publications using IMPC mice/data for the human-disease question*)
- MMRRC / IMSR for line availability
- Simons Searchlight is actively recruiting an *EIF3F* patient cohort ([link](https://www.simonssearchlight.org/research/what-we-study/eif3f/)) — the most likely source of future natural-history data

---

## Summary of evidence quality

| Domain | Strength |
|---|---|
| Gene–disease association | **Strong.** Exome-wide burden analysis + independent 22-patient replication cohort + ClinVar 2-star Pathogenic/LP + PanelApp GREEN. |
| Variant pathogenicity (c.694T>G) | **Strong.** Founder haplotype, no gnomAD homozygotes, functional validation in isogenic iPSCs. |
| Core phenotype (GDD, speech delay) | **Strong.** 100% in both cohorts. |
| Frequent phenotypes (SNHL, behaviour, tone, growth) | **Moderate.** ~50% figures from a single 21-patient cohort. |
| Epilepsy frequency | **Weak/contradictory.** 86% vs 15% between cohorts. Do not assert a frequency band. |
| Mechanism: translation → proliferation | **Moderate.** Measured, but in stem cells and mouse muscle. |
| Mechanism: → neurodevelopmental phenotype | **Weak/inferred.** No neural model, no structural correlate. |
| Notch/DUB relevance to disease | **Speculative.** In vitro only, never connected to patients. |
| White matter / oligodendrocyte relevance | **Speculative,** and in tension with Human Protein Atlas expression data. |
| Meningioma association | **Unresolved.** 2/21 observed; COSMIC somatic data negative. |
| Prevalence | **Not determined.** Only a derivable HWE estimate. |
| Treatment | **None exists.** Supportive care only. |

---

## Sources

- [OMIM #618295 — Intellectual developmental disorder, autosomal recessive 67; MRT67](https://www.omim.org/entry/618295)
- [Monarch Initiative — MONDO:0032662](https://monarchinitiative.org/MONDO:0032662)
- [MedGen — MRT67 (C4749019)](https://www.ncbi.nlm.nih.gov/medgen/?term=618295)
- [ClinVar RCV000754608 — NM_003754.3(EIF3F):c.694T>G (p.Phe232Val)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000754608/)
- [dbSNP rs141976414](https://www.ncbi.nlm.nih.gov/snp/rs141976414)
- [Martin HC et al., *Science* 2018 — Quantifying the contribution of recessive coding variation to developmental disorders (PMID:30409806)](https://pubmed.ncbi.nlm.nih.gov/30409806/)
- [Hüffmeier U et al., *Orphanet J Rare Dis* 2021 — EIF3F-related neurodevelopmental disorder (PMID:33736665)](https://ojrd.biomedcentral.com/articles/10.1186/s13023-021-01744-1)
- [Lakatosova S et al., *Cureus* 2024 — Genetic Diagnostics and Phenotypic Profiling of a Girl With AR IDD and Autism (PMID:39723281)](https://pubmed.ncbi.nlm.nih.gov/39723281/)
- [Docquier A et al., *J Physiol* 2019 — eIF3f depletion impedes mouse embryonic development (PMID:31026345)](https://pubmed.ncbi.nlm.nih.gov/31026345/)
- [Moretti J et al., *PLoS Biol* 2010 — eIF3f exhibits a deubiquitinase activity regulating Notch activation (PMID:21124883)](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1000545)
- [Csibi A et al., *PLoS ONE* 2010 — eIF3f controls kinase-dependent mTOR signaling in muscle](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0008994)
- [eIF3f: a central regulator of the antagonism atrophy/hypertrophy in skeletal muscle (PMID:23769948)](https://pubmed.ncbi.nlm.nih.gov/23769948/)
- [Ayhan F et al., *EMBO J* 2018 — SCA8 RAN polySer accumulates in white matter and is regulated by eIF3F (PMID:30206144)](https://pubmed.ncbi.nlm.nih.gov/30206144/)
- [Huang YS et al., *J Pers Med* 2022 — Two Genetic Mechanisms in Two Siblings (PMID:35743796)](https://pubmed.ncbi.nlm.nih.gov/35743796/)
- [Shad Z et al., *Genet Med Open* 2024, P319 — Expanding the phenotype of EIF3F-related neurodevelopmental disorder](https://www.gimopen.org/article/S2949-7744(24)00359-5/fulltext)
- [Simons Searchlight — EIF3F](https://www.simonssearchlight.org/research/what-we-study/eif3f/)
- [Genomics England PanelApp — EIF3F (Early onset or syndromic epilepsy)](https://panelapp.genomicsengland.co.uk/panels/402/gene/EIF3F/)
- [SFARI Gene — EIF3F](https://gene.sfari.org/database/human-gene/EIF3F)
- [MGI:1913335 — Eif3f](https://www.informatics.jax.org/marker/MGI:1913335)
- [Human Protein Atlas — EIF3F tissue expression](https://www.proteinatlas.org/ENSG00000175390-EIF3F/tissue)
- [GeneReviews — PPP1R21-Related El-Hattab-Schmidts Syndrome (for disambiguation only)](https://www.ncbi.nlm.nih.gov/books/NBK620407/)

---

## Recap for the curator

MRT67 is the ***EIF3F*** disorder (MONDO:0032662, OMIM #618295) — **not** PPP1R21/FERRY, despite four PPP1R21 reference files sitting in this worktree's cache; two of those have no retrievable body text and could not yield a verifiable snippet in any case. The disease is driven almost entirely by one European founder missense allele, c.694T>G p.(Phe232Val), on a single 7.8 kb haplotype, present at 0.12% in non-Finnish Europeans and 0.21% in Ashkenazi Jewish individuals with zero gnomAD homozygotes. Mechanism is a ~30% reduction in eIF3f protein → reduced translation initiation → reduced mTOR signalling and proliferation → impaired brain development and somatic growth; the last arrow is inferred rather than measured, since no neural model of the disease allele exists. Global developmental delay and speech delay are universal; SNHL, behavioural problems, altered tone and short stature run near 50%; epilepsy frequency is contradictory between the two cohorts (86% vs 15%) and should not be assigned a frequency band. There is no treatment, no biomarker, no prevalence figure, and no omics dataset. Three items are genuinely open and belong in `discussions:` rather than as asserted facts: the epilepsy discrepancy, the 2/21 meningioma observation (with its negative COSMIC counter-evidence), and the human-model mismatch between undifferentiated iPSCs / mouse muscle and a brain disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1016/j.gimo.2024.101213](https://www.gimopen.org/article/S2949-7744(24)00359-5/fulltext` (1 mention) - Identifier did not resolve to a record
- `DOI:10.1371/journal.pone.0008994](https://journals.plos.org/plosone/article` (1 mention) - Identifier did not resolve to a record