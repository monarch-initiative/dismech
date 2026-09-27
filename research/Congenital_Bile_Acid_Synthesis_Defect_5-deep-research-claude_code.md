---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-08T07:07:31.675033'
end_time: '2026-09-08T07:11:28.472766'
duration_seconds: 236.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Bile Acid Synthesis Defect 5
  mondo_id: MONDO:0014564
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
  num_turns: 17
  total_cost_usd: 1.1605942
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:25326392
  relevance_assessed: 4
  on_topic: 3
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0031994
    reported_labels:
    - Abnormal bile acid level
    ontology_label: Bronchial breath sound
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0043433
    ontology_label: obsolete negative regulation of DNA-binding transcription factor
      activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Bile Acid Synthesis Defect 5
- **MONDO ID:** MONDO:0014564 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Bile Acid Synthesis Defect 5** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I now have sufficient primary-source material to write the full report.

I have sufficient primary-literature material now. Writing the full report.

# Congenital Bile Acid Synthesis Defect 5 (CBAS5) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Congenital Bile Acid Synthesis Defect 5 (CBAS5) is an ultra-rare autosomal recessive inborn error of peroxisomal metabolism caused by biallelic loss-of-function variants in **ABCD3** (also known as *PXMP1* / *PMP70*), which encodes a peroxisomal membrane ATP-binding cassette (ABC) half-transporter. ABCD3 imports the CoA-thioesters of the C27 bile acid intermediates di- and trihydroxycholestanoic acid (DHCA-CoA, THCA-CoA) — and branched-chain fatty acyl-CoAs — into the peroxisomal matrix, where peroxisomal β-oxidation shortens the C27 side chain to yield mature C24 primary bile acids (chenodeoxycholic acid, CA and CDCA). Loss of ABCD3 blocks this peroxisomal import step, causing failure to generate mature bile acids and pathological accumulation of hepatotoxic C27 bile acid intermediates, which presents clinically as progressive infantile cholestatic/fibrotic liver disease [Ferdinandusse et al., *Hum Mol Genet* 2015, PMID:25326392].

CBAS5 is the fifth entity in the "congenital bile acid synthesis defect" (CBAS1–5) nosological series, which groups genetically distinct single-gene defects along the classic (neutral) and alternative (acidic/peroxisomal) bile acid synthesis pathways by shared clinical phenotype (neonatal/infantile cholestasis with malabsorption) rather than by shared mechanism:

| Entry | Gene | Enzyme/protein | OMIM |
|---|---|---|---|
| CBAS1 | HSD3B7 | 3β-hydroxy-Δ5-C27-steroid dehydrogenase | #607765 |
| CBAS2 | AKR1D1 | Δ4-3-oxosteroid 5β-reductase | #235555 |
| CBAS3 | CYP7B1 | oxysterol 7α-hydroxylase | #613812 |
| CBAS4 | AMACR | α-methylacyl-CoA racemase | #214950 |
| **CBAS5** | **ABCD3** | **peroxisomal ABC transporter (PMP70)** | **#616278** |

**Key identifiers:**
- **OMIM**: #616278 (phenotype), *170995 (gene, ABCD3)
- **MONDO**: MONDO:0014564
- **Gene**: ABCD3, HGNC:67, chromosome 1p21.3
- **Orphanet**: listed among congenital bile acid synthesis defects (ABCD3-related peroxisomal bile acid synthesis defect); note Orphanet/GeneReviews coverage of this specific ultra-rare entity is sparse given only one published family
- **MedGen**: linked concept for "Congenital bile acid synthesis defect 5"

**Synonyms/alternative names**: Bile acid synthesis defect, congenital, 5; PMP70 deficiency; ABCD3 deficiency; peroxisomal bile acid transporter deficiency; "novel bile acid biosynthesis defect due to a deficiency of peroxisomal ABCD3" (as titled in the founding report).

**Evidence basis**: The disease-defining information is derived almost entirely from a **single published family** (aggregated case-level clinical/biochemical/genetic data from one affected proband, supplemented by a corroborating *Abcd3*-knockout mouse model) rather than an aggregated disease-level registry or large cohort — a point OMIM itself flags: "only one family has been described in the literature and phenotypic association is not confirmed" [OMIM #616278; PMID:25326392].

---

## 2. Etiology

**Disease causal factor**: Purely monogenic/genetic. Biallelic (homozygous, in the only reported case — consistent with consanguinity) loss-of-function variants in *ABCD3* abolish or severely impair the peroxisomal import of C27 bile acid intermediate–CoA esters, blocking peroxisomal β-oxidation shortening of the bile acid side chain.

**Genetic risk factors**:
- **Causal variant**: The index patient (girl, born to consanguineous Turkish parents) carried a **homozygous 1758-bp genomic deletion** predicted to produce a truncated ABCD3 protein lacking its C-terminal 24 amino acids (p.Tyr635AsnfsTer1/p.Y635Nfs*1), removing part of the second nucleotide-binding domain required for ATPase-driven transport [PMID:25326392].
- **Consanguinity** was present in the only reported family, consistent with autosomal recessive transmission and a rare founder/private allele rather than a population-frequent variant.
- No modifier genes or susceptibility loci have been reported given the extreme rarity (n=1 family).

**Protective factors**: None reported; no protective alleles or environmental protective factors are described for this ultra-rare condition.

**Gene-environment interactions**: None established. As a purely biosynthetic enzymatic/transport block, the phenotype is not known to be modulated by diet, toxin exposure, or infection, though — by analogy to other bile acid synthesis defects — cholestatic decompensation could plausibly be provoked by intercurrent illness or fasting (inferred from general bile acid synthesis defect biology, not demonstrated specifically for CBAS5).

---

## 3. Phenotypes

Because only one patient has been reported in detail, phenotype frequencies (e.g., "80% of patients") cannot be established; the description below is a single well-characterized case, corroborated mechanistically by mouse knockout hepatic pathology.

| Phenotype | Type | HPO term (suggested) | Notes |
|---|---|---|---|
| Hepatosplenomegaly | Physical sign | HP:0001433 (Hepatosplenomegaly) | Presenting feature at 1.5 years |
| Progressive liver failure / fibrosis | Clinical sign | HP:0001395 (Hepatic fibrosis), HP:0001394 (Cirrhosis) | Liver biopsy: fibrosis + hepatocellular regeneration |
| Severe iron-deficiency anemia | Laboratory abnormality | HP:0001891 (Iron deficiency anemia is not a direct HP term; consider HP:0001903 Anemia) | Present at initial workup |
| Coagulopathy | Laboratory abnormality | HP:0001928 (Abnormal coagulation) | Progressed to bleeding |
| Pancytopenia | Laboratory abnormality | HP:0001876 (Pancytopenia) | Developed with disease progression, likely hypersplenism-related |
| Portal hypertension | Clinical sign | HP:0001409 (Portal hypertension) | Late complication |
| Elevated liver transaminases | Laboratory abnormality | HP:0031964 (Elevated hepatic transaminase) | |
| Reduced mature C24 bile acids / accumulation of C27 bile acid intermediates (DHCA, THCA) | Laboratory/biochemical abnormality | HP:0031994 (Abnormal bile acid level) is the nearest general term; more specific ontology binding would need biochemical `Biochemical` descriptor rather than HP | Diagnostic biochemical signature |
| Normal developmental milestones | Negative/reassuring finding | — | Explicitly noted as normal — distinguishes CBAS5's isolated hepatic phenotype from the neurologic involvement typical of classic Zellweger spectrum disorder |

**Onset**: Infantile/early childhood — the index patient presented at **1.5 years of age**, later than the neonatal-onset typical of CBAS1/CBAS2, though the underlying biochemical defect is congenital.

**Severity/progression**: **Progressive** — hepatosplenomegaly and biochemical derangement at presentation evolved to overt hepatic fibrosis, pancytopenia, coagulopathy/bleeding, and portal hypertension, culminating in **liver transplantation at age 4 years**; the patient reportedly died shortly after transplantation [PMID:25326392 as summarized in search-derived sources — verify primary text before final KB citation].

**Quality of life impact**: Not formally studied (EQ-5D/SF-36 data unavailable for a single pediatric case), but the natural history described (progression to transplant-requiring liver failure) implies severe impact on growth, nutrition (fat-malabsorption from bile acid deficiency), and survival absent intervention.

---

## 4. Genetic/Molecular Information

**Causal gene**: *ABCD3* (ATP Binding Cassette Subfamily D Member 3; formerly *PXMP1*; protein alias PMP70). HGNC:67; OMIM *170995; chromosome 1p21.3; 659-amino-acid protein, 95% identical to rat ortholog.

**Gene product/function**: ABCD3 is a peroxisomal membrane **half-ABC-transporter** of the ALDP (ABCD) subfamily (which also includes ABCD1/ALDP, mutated in X-linked adrenoleukodystrophy, and ABCD2/ALDRP). Peroxisomal ABCD transporters function as homodimers or heterodimers and use ATP hydrolysis (via conserved Walker A/B nucleotide-binding-fold motifs in the C-terminal hydrophilic domain) to translocate CoA-thioesters of fatty acids and bile acid intermediates across the peroxisomal membrane. ABCD3 is the most abundant peroxisomal ABC transporter and has the broadest substrate range among the three (ABCD1–3), transporting branched-chain fatty acyl-CoAs, very-long-chain fatty acyl-CoAs, dicarboxylic fatty acyl-CoAs, and the C27 bile acid precursor-CoAs (DHCA-CoA, THCA-CoA) essential for bile acid synthesis.

**Pathogenic variant identified**:
- Homozygous ~1758 bp genomic deletion → frameshift/truncation, p.Y635Nfs*1, removing the C-terminal 24 residues (part of the second nucleotide-binding domain) [PMID:25326392].
- **Variant classification**: Pathogenic (functionally validated by immunoblot loss of protein and complementation/fibroblast studies in the founding paper, and independently corroborated by the *Abcd3*−/− mouse phenocopy).
- **Origin**: Germline, biallelic (homozygous due to consanguinity).
- **Functional consequence**: Loss of function (truncating variant predicted to destabilize/eliminate the transporter's nucleotide-binding domain, abolishing ATP-dependent transport activity).
- **Population frequency**: Not observed as a recurrent/founder allele; given a single reported family, allele frequency in gnomAD/1000 Genomes/TOPMed for this specific variant is expected to be absent or private (not independently verified against gnomAD in this session — recommend direct gnomAD lookup before KB citation).

**Modifier genes**: None established.

**Epigenetic information**: None reported for this disorder specifically.

**Chromosomal abnormalities**: None reported (variant is a small indel, not a large structural/chromosomal lesion detectable by karyotype/CMA).

**Allelic disorders**: ABCD3 variants have also been implicated more broadly in a mild/attenuated peroxisomal biogenesis-disorder-like or "Zellweger spectrum disorder"-adjacent liver phenotype in later literature discussions, though the canonical, OMIM-cataloged CBAS5 entry remains anchored to the single Ferdinandusse et al. family; this is a genuine unsettled lump/split question rather than a well-replicated distinct allelic series, and should be flagged as such rather than asserted definitively.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been reported for CBAS5. As with other congenital bile acid synthesis defects, disease expression is driven entirely by the germline enzymatic/transport block; there is no described toxin, occupational exposure, or dietary trigger. (By analogy with general bile acid synthesis defect biology, fat-soluble vitamin status and dietary fat content likely modulate the severity of secondary malabsorptive complications, but this has not been specifically documented for CBAS5.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from initiating lesion to clinical manifestation)

1. Biallelic loss-of-function *ABCD3* variant (e.g., the p.Y635Nfs*1 truncation) **leads to** loss/near-loss of functional peroxisomal ABCD3 transporter protein at the peroxisomal membrane [demonstrated, PMID:25326392].
2. Loss of ABCD3 **results in** failure of ATP-dependent import of the CoA-thioesters of the C27 bile acid intermediates DHCA-CoA and THCA-CoA (and of branched-chain fatty acyl-CoAs) into the peroxisomal matrix [demonstrated in patient fibroblasts and confirmed in *Abcd3*−/− mice].
3. Failure of peroxisomal import **blocks** the terminal peroxisomal β-oxidation step of bile acid synthesis — normally carried out by AMACR (racemization), ACOX2 (oxidation), HSD17B4/D-bifunctional enzyme (hydration/dehydrogenation), and SCPx (thiolytic chain-shortening cleavage of a propionyl-CoA unit) — that converts DHCA-CoA/THCA-CoA into the mature C24 bile acid-CoAs chenodeoxycholyl-CoA and cholyl-CoA [pathway established by prior biochemical literature; the block at the transport step is inferred from substrate accumulation, not directly visualized].
4. This block **causes** (a) **deficient synthesis of mature primary bile acids** (CA, CDCA) and (b) **pathological accumulation of unmetabolized C27 bile acid intermediates (DHCA, THCA) and their upstream precursors** in liver, plasma, and bile [demonstrated biochemically in the patient and in *Abcd3*−/− mouse tissues].
5. Deficient mature bile acid output **leads to** impaired bile flow/reduced bile acid-dependent bile secretion, **contributing to** cholestasis, and to intestinal malabsorption of dietary fat and fat-soluble vitamins (inferred by analogy with other CBAS entries; not separately quantified in the single reported case).
6. Accumulated C27 bile acid intermediates are **hepatotoxic** (per broader literature on peroxisomal C27-bile acid intermediate toxicity — see Ferdinandusse & Houten review) and **drive** progressive hepatocellular injury, manifesting histologically as **hepatic fibrosis with hepatocellular regeneration** [demonstrated by liver biopsy in the index patient].
7. Progressive hepatocyte injury and fibrosis **result in** worsening hepatosplenomegaly, impaired hepatic synthetic function (**coagulopathy**), and **secondary hematologic complications** (iron-deficiency anemia, evolving to pancytopenia, likely reflecting combined nutritional deficiency and hypersplenism) [clinical course as reported].
8. Progressive fibrosis **culminates in** cirrhosis-associated **portal hypertension** and decompensated liver failure, ultimately **requiring liver transplantation** (performed at age 4 years in the index case) [clinical outcome reported].

Where the chain is *inferred* rather than directly demonstrated for this specific human patient: the causal link from "bile acid deficiency" to "fat/vitamin malabsorption" (step 5) and the precise mechanism of C27-intermediate hepatotoxicity (step 6) are extrapolated from general bile acid synthesis defect pathophysiology and from separate toxicological literature on C27 bile acid intermediates [PMID reference: "Toxicity of peroxisomal C27-bile acid intermediates," ScienceDirect/Mol Genet Metab], not established by mechanistic study within the single CBAS5 patient.

### Molecular pathways
- **Alternative (acidic) bile acid synthesis pathway**: cholesterol → (CYP27A1, mitochondrial) → 3α,7α,12α-trihydroxycholestanoic acid (THCA) / 3α,7α-dihydroxycholestanoic acid (DHCA) → **[ABCD3-mediated peroxisomal import — the blocked step]** → peroxisomal β-oxidation (AMACR, ACOX2, HSD17B4, SCPx/thiolase) → cholyl-CoA / chenodeoxycholyl-CoA → conjugation (BAAT) → taurine/glycine-conjugated CA/CDCA.
- Suggested GO terms: **GO:0006699** (bile acid biosynthetic process); **GO:0007031** (peroxisome organization, contextual); **GO:1990542** (mitochondrial transmembrane transport, contextual to CYP27A1 step); **GO:0043433** (negative regulation of DNA-binding transcription factor activity — not relevant, omit); more precisely **GO:0006699** and a peroxisomal transmembrane transport term (e.g., **GO:1990542**-adjacent peroxisomal fatty-acyl-CoA transport — check exact GO ID during curation, e.g. GO:0015916 fatty-acyl-CoA transport).

### Cellular processes
- Peroxisomal β-oxidation dysfunction (GO:0006635, fatty acid β-oxidation).
- Secondary hepatocellular injury/fibrogenesis (activation of hepatic stellate cells — consistent with the KB's `fibrotic_response` mechanism module as a conformance target once curated).

### Protein dysfunction
ABCD3 loss of function via C-terminal truncation removing part of the nucleotide-binding domain — predicted to abolish ATP-binding/hydrolysis-coupled substrate translocation (structural inference from ABC-transporter biology; direct biophysical characterization of this specific truncated protein was not reported, though recent cryo-EM/structural work on wild-type ABCD3 substrate transport mechanism is now available — PMID:40501884, PNAS 2025 — and could inform future structure-function interpretation of pathogenic variants).

### Metabolic changes
Bile acid pool composition shift: reduced mature C24 bile acids (CA, CDCA), elevated unconjugated bile acids, marked accumulation of C26/C27 bile acid intermediates DHCA and THCA in plasma and (per mouse model) liver, bile, and intestine.

### Tissue damage mechanisms
Cholestatic/toxic hepatocellular injury progressing to fibrosis and cirrhosis, analogous to the mechanism proposed for other C27-bile-acid-intermediate-accumulating disorders (bile acid intermediate toxicity, oxidative stress in hepatocytes — inferred, not directly assayed in the human case).

### Biochemical abnormalities
Peroxisomal transporter (ABC transporter) deficiency — a transport defect rather than an enzymatic deficiency, distinguishing CBAS5 mechanistically from CBAS1 (HSD3B7), CBAS2 (AKR1D1), CBAS3 (CYP7B1), and CBAS4 (AMACR), all of which are catalytic enzyme defects.

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic (beyond targeted bile acid mass spectrometry), single-cell, or spatial data specific to the human CBAS5 patient have been published. The *Abcd3*−/− mouse has been studied with targeted and untargeted metabolomics, histology, immunoblotting, and stable isotope tracing (Ranea-Robles et al., *J Inherit Metab Dis* 2021, PMID pending verification — reported via bioRxiv/JIMD), revealing broader roles for ABCD3 in dicarboxylic fatty acid metabolism, hepatic lipid homeostasis, lipodystrophy, increased circulating free fatty acids, decreased ketone bodies, enhanced hepatic cholesterol synthesis, and decreased hepatic de novo lipogenesis — phenotypes beyond the bile acid axis alone.

**Suggested CL/UBERON/GO term bindings**: hepatocyte (CL:0000182); peroxisome (GO:0005777, cellular component); liver (UBERON:0002107); bile canaliculus (UBERON:0001281, if bile secretion specifically implicated).

---

## 7. Anatomical Structures Affected

**Organ level**:
- **Primary**: Liver (hepatocellular injury, fibrosis, cirrhosis) — UBERON:0002107.
- **Secondary**: Spleen (splenomegaly, likely secondary to portal hypertension/hypersplenism) — UBERON:0002106; hematopoietic system (anemia, pancytopenia) secondary to hypersplenism and/or nutritional deficiency; coagulation system (coagulopathy from impaired hepatic synthetic function and vitamin K malabsorption).
- **Body systems**: Hepatobiliary system primarily; hematologic system secondarily; (gastrointestinal system inferred, via fat/fat-soluble vitamin malabsorption, though not explicitly detailed in the single case report).

**Tissue/cell level**: Hepatocytes are the principal affected cell type (site of bile acid synthesis and of ABCD3 expression/peroxisomal metabolism). Cell Ontology term: hepatocyte (CL:0000182). Hepatic stellate cells are plausibly involved in the fibrotic response (CL:0000632), by analogy with the KB's general fibrotic_response module, though not specifically documented for this entry.

**Subcellular level**: **Peroxisome** (GO:0005777) is the defining subcellular compartment — ABCD3 is a peroxisomal membrane protein (GO:0005778, peroxisomal membrane), and the defect is specifically one of peroxisomal matrix protein/substrate import.

**Localization**: Diffuse hepatic involvement (not focal/lateralized); no laterality applicable.

---

## 8. Temporal Development

**Onset**: The single reported patient presented clinically at **1.5 years of age** with hepatosplenomegaly, anemia, and coagulopathy — later than the neonatal-onset cholestasis typical of CBAS1/CBAS2, though the molecular defect is congenital from birth. Onset pattern: insidious/subacute, discovered on evaluation of hepatosplenomegaly rather than at birth.

**Progression**: Progressive — hepatic fibrosis at biopsy evolved over time to pancytopenia, bleeding, and portal hypertension, ultimately requiring liver transplantation at age 4 years (roughly 2.5 years after presentation). Disease course pattern: chronic, progressive, non-remitting in the absence of effective disease-modifying therapy in this case.

**Patterns**: No remission was reported (spontaneous or treatment-induced) in the index case; the patient proceeded to transplantation, and — per available search summaries — died shortly thereafter (this specific outcome detail should be verified against the primary paper's full text before being asserted as a fact in the KB, since it was derived from a secondary summary rather than a directly quoted primary-source sentence).

**Critical periods**: Not established; given the fatal course in the only reported case, no data exist on whether earlier biochemical diagnosis (e.g., via newborn or targeted bile acid screening) and earlier bile acid replacement therapy would alter the natural history — this is an open question analogous to the demonstrated benefit of early cholic acid therapy in CBAS1/CBAS2.

---

## 9. Inheritance and Population

**Epidemiology**: CBAS5 is **exceptionally rare** — a single published family/patient as of the most recent literature identified in this search. No prevalence or incidence estimate can be computed; it should be curated as `prevalence_class: NOT_YET_DOCUMENTED` with `measure_type: CASES_IN_LITERATURE` (n=1).

**Inheritance pattern**: **Autosomal recessive** — the index patient was homozygous for the causal *ABCD3* deletion, born to consanguineous parents, consistent with AR transmission [PMID:25326392].

**Penetrance**: Presumed complete in the homozygous state based on the single reported case, but with n=1 this cannot be statistically established.

**Expressivity**: Unknown/not assessable from a single case.

**Genetic anticipation**: Not applicable (not a repeat-expansion disorder).

**Germline mosaicism**: Not reported.

**Founder effects**: Not established — the reported deletion has not been reported as a recurrent founder allele in any specific population; the consanguineous Turkish family context suggests a private/family-specific allele rather than a population founder variant, though this has not been formally tested against population databases such as gnomAD in this session.

**Consanguinity**: Present and central to the single reported case (consanguineous Turkish parents), consistent with the ultra-rare, presumably private nature of the causal allele.

**Carrier frequency**: Unknown; not calculable from gnomAD/population databases within available search results for this specific variant (would need direct gnomAD/ClinVar lookup for the ABCD3 c.della region during KB curation).

**Population demographics**: The only reported family is of Turkish ethnicity; no broader ethnic or geographic distribution data exist. Sex ratio and age distribution cannot be estimated from a single female case.

---

## 10. Diagnostics

**Clinical/laboratory tests**:
- **Plasma bile acid profiling by LC-MS/MS**: the diagnostic cornerstone — shows markedly elevated C27 bile acid intermediates (DHCA, THCA) with reduced mature C24 primary bile acids and increased unconjugated bile acid fraction. This is the same biochemical modality (LC-ESI-MS-MS) used across the CBAS1–5 spectrum and proposed for expanded newborn screening panels.
- **Urinary bile acid analysis**: shows low fraction of primary bile acids and abnormal/atypical bile acid species (as generally described for CBAS spectrum disorders; specific urinary profile for CBAS5 not separately detailed in available sources).
- **Liver biochemistry**: elevated transaminases; synthetic dysfunction (coagulopathy) in advanced disease.
- **Liver biopsy/histopathology**: fibrosis with hepatocellular regeneration in the index case; SNOMED CT/pathology term for hepatic fibrosis applicable.
- **Very-long-chain fatty acids (VLCFA) and phytanic/pristanic acid**: plausible adjunct given ABCD3's broader peroxisomal substrate range (branched-chain and dicarboxylic fatty acids), though not specifically emphasized as diagnostic in the human case (this is inferred from ABCD3 biology and mouse model findings, not confirmed as a clinical diagnostic test performed in the patient).

**Genetic testing**:
- **Single-gene ABCD3 sequencing** or **targeted bile acid synthesis defect gene panel** (alongside HSD3B7, AKR1D1, CYP7B1, AMACR) is the recommended approach once biochemical bile acid profiling suggests a peroxisomal/alternative-pathway defect.
- **Whole-exome/genome sequencing** is appropriate given the extreme rarity and lack of a "typical" mutational hotspot (the one reported variant is a large deletion, which WES with appropriate CNV-calling, or WGS, would be needed to reliably detect — a caveat for diagnostic yield).
- GTR lists a clinical test for "Bile acid synthesis defect, congenital, 5" (ABCD3 gene, full coding exon sequence analysis, postnatal).

**Differential diagnosis**: Other CBAS entries (CBAS1–4), progressive familial intrahepatic cholestasis (PFIC1–6/ABCB4, ABCB11, ATP8B1), Zellweger spectrum peroxisome biogenesis disorders (given ABCD3's peroxisomal localization and the phenotypic overlap of neonatal liver disease), biliary atresia, and other neonatal/infantile cholestasis etiologies.

**Screening**: Not currently part of standard newborn screening; the broader CBAS literature (e.g., recent AKR1D1 newborn-screening discussion, PMID:41387259) argues for adding bile acid mass spectrometry to expanded newborn panels, which would in principle also detect CBAS5, though this has not been specifically validated for ABCD3 deficiency.

---

## 11. Outcome/Prognosis

**Survival/mortality**: With a single reported case, no survival statistics can be generated. The index patient's disease progressed to liver failure requiring transplantation at age 4; available secondary sources indicate a fatal outcome shortly post-transplant, though this specific claim requires verification against the primary paper's full text before being asserted with a PMID citation in the KB (flagging per the attribution discipline that a summarized/derived claim is a lead, not a verified quote).

**Morbidity**: Severe — progressive hepatic fibrosis/cirrhosis, portal hypertension, coagulopathy, hematologic compromise (anemia progressing to pancytopenia).

**Complications**: Hepatosplenomegaly → fibrosis → cirrhosis → portal hypertension → bleeding/coagulopathy → liver failure → transplantation, with post-transplant mortality reported in the single case.

**Recovery potential**: Unknown whether earlier diagnosis and bile acid replacement therapy (as is effective in CBAS1/CBAS2) would alter the trajectory — no such intervention was reported as attempted/effective in the single published CBAS5 case, unlike the well-documented efficacy of cholic acid therapy in HSD3B7 and AKR1D1 deficiency.

**Prognostic factors**: Given n=1, no formal prognostic factor analysis exists. By analogy with other bile acid synthesis defects, earlier diagnosis/earlier bile acid replacement is plausibly prognostic, but unproven for CBAS5 specifically.

---

## 12. Treatment

**Pharmacotherapy — bile acid replacement**: Oral **cholic acid** therapy is the established, evidence-based treatment for most congenital bile acid synthesis defects, including CBAS1 (HSD3B7) and CBAS2 (AKR1D1), where it is highly effective (e.g., a case series of 16 AKR1D1-deficient patients treated with cholic acid showing favorable outcomes, PMC10704681; systematic review of cholic acid effectiveness/safety across bile acid synthesis defects, Orphanet J Rare Dis 2024). **However, whether cholic acid replacement is similarly effective in CBAS5 is not established from available sources** — CBAS5 is mechanistically a transport defect occurring *after* the mitochondrial CYP27A1 step but *before* peroxisomal chain-shortening, so exogenous cholic acid (which provides negative feedback on CYP7A1 via FXR-mediated suppression, reducing production of toxic upstream intermediates) is mechanistically plausible as a therapeutic strategy by the same rationale as for other CBAS entries, but this has not been specifically documented as attempted/successful in the single reported CBAS5 patient in the sources retrieved.
- Suggested NCIT term: **NCIT:C15986** (Pharmacotherapy), with `therapeutic_agent` bound to cholic acid (**CHEBI:29103**, cholic acid) if/when curated with supporting citation.

**Surgical/interventional**: **Liver transplantation** — performed in the index patient at age 4 years for decompensated liver failure/portal hypertension; NCIT term **NCIT:C15289** (Organ Transplantation).

**Supportive care**: Management of coagulopathy (likely including vitamin K supplementation given fat-soluble vitamin malabsorption risk — inferred, not explicitly reported), nutritional support, and management of portal hypertension complications would be standard supportive measures for progressive cholestatic liver disease, though not itemized in the single case report retrieved.

**Experimental/investigational**: No CBAS5-specific clinical trials identified (ClinicalTrials.gov searches for bile acid synthesis defects, e.g., NCT01589523 "GlycoCholic Acid Treatment for Patients With Inborn Errors in Bile Acid Synthesis," are relevant to the broader CBAS disease class but not confirmed to include or exclude ABCD3-specific enrollment).

**Treatment outcomes**: Cannot be assessed for CBAS5 specifically due to lack of reported treatment trial in the single case (the patient proceeded directly to transplantation rather than being reported as treated with bile acid replacement first, per available sources — this should be verified against full text).

---

## 13. Prevention

**Primary prevention**: Not applicable beyond genetic counseling in consanguineous families with a known familial *ABCD3* variant.

**Secondary prevention**: Early biochemical (bile acid mass spectrometry) or genetic diagnosis in at-risk families (i.e., relatives of the index family, or future consanguineous unions in populations where the variant might recur) could in principle allow earlier initiation of bile acid replacement therapy before irreversible fibrosis develops, by direct analogy with the demonstrated benefit of early treatment in CBAS1/CBAS2 — though this specific preventive strategy has not been validated in CBAS5.

**Genetic counseling**: Recommended for the reported consanguineous family given autosomal recessive inheritance and 25% recurrence risk for future pregnancies; prenatal or preimplantation genetic testing would be feasible once the familial variant is known. NCIT term: **NCIT:C15240** (Genetic Counseling).

**Carrier/prenatal screening**: Not standardized given the extreme rarity and single-family basis of the disease; would only be relevant within the specific reported family or its extended relatives.

---

## 14. Other Species / Natural Disease

No naturally occurring CBAS5/ABCD3-deficiency disease has been reported in non-human species (no OMIA entry identified). ABCD3 is broadly conserved across mammals (human protein 95% identical to rat), but no spontaneous veterinary case has been published.

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBITaxon:10090)**: The primary and only well-characterized animal model.
- **Original *Abcd3*−/− knockout** (Ferdinandusse et al., 2015, PMID:25326392): confirmed reduction of C24 bile acids with significant accumulation of C27-bile acid intermediates in liver, bile, and intestine, directly recapitulating the human biochemical phenotype and validating ABCD3's role in bile acid chain-shortening. Pronounced hepatomegaly was also observed, without histological steatosis, similar to the human phenotype pattern.
- **CRISPR-Cas9-generated *Abcd3* KO mouse** (Ranea-Robles et al., *J Inherit Metab Dis* 2021, referenced via bioRxiv preprint and PNAS-adjacent structural work): extended the phenotype characterization to broader lipid metabolism — lipodystrophy, elevated circulating free fatty acids, decreased ketone bodies, enhanced hepatic cholesterol synthesis, decreased hepatic de novo lipogenesis, and a major role for ABCD3 in dicarboxylic fatty acid metabolism — indicating the mouse model captures both the bile acid axis and additional peroxisomal fatty acid metabolic roles of ABCD3 not emphasized in the single human case.
- **Fidelity/limitations**: The mouse model faithfully recapitulates the core biochemical signature (C24 bile acid deficiency, C27 intermediate accumulation) but the reported mouse phenotype emphasizes hepatomegaly and systemic lipid/metabolic dysregulation rather than the progressive fibrosis-to-cirrhosis trajectory documented in the single human patient — it is unclear from available sources whether the mouse model recapitulates progressive hepatic fibrosis/cirrhosis or is more useful as a biochemical/metabolic model. This would need direct review of the primary mouse-phenotyping papers to assess `fidelity` and `relationship` (RECAPITULATES vs PARTIALLY_RECAPITULATES) for KB curation.

**In vitro models**: Patient-derived skin fibroblasts were used in the founding study to functionally confirm the ABCD3 protein defect (immunoblot loss of protein) — this constitutes IN_VITRO evidence supporting the causal genotype-phenotype link.

---

## Summary of Key Citation-Ready Sources

| Citation | Content |
|---|---|
| Ferdinandusse S, et al. "A novel bile acid biosynthesis defect due to a deficiency of peroxisomal ABCD3." *Hum Mol Genet*. 2015;24(2):361-370. **PMID:25326392** | Founding/sole clinical case report; genetic, biochemical, and mouse-model data |
| OMIM #616278 (BILE ACID SYNTHESIS DEFECT, CONGENITAL, 5; CBAS5) | Phenotype-gene relationship, clinical synopsis |
| OMIM *170995 (ABCD3) | Gene/protein structural information |
| Ranea-Robles P, et al. "The peroxisomal transporter ABCD3 plays a major role in hepatic dicarboxylic fatty acid metabolism and lipid homeostasis." *J Inherit Metab Dis*. 2021 (bioRxiv preprint 10.1101/2021.07.26.452046) | Extended mouse model characterization |
| Systematic review: "The clinical and biochemical effectiveness and safety of cholic acid treatment for bile acid synthesis defects." *Orphanet J Rare Dis*. 2024 | Cross-CBAS treatment evidence (not CBAS5-specific) |
| Recent structural work: "Molecular mechanism of substrate transport by human peroxisomal ABCD3." *PNAS*. 2025. **PMID:40501884** | Wild-type ABCD3 structure/mechanism, useful mechanistic background |

**Curation caveat (important for KB use)**: Nearly every clinical claim above traces to a **single published family** described in one primary paper (PMID:25326392), supplemented by mouse-model and structural-biology literature that establishes ABCD3's general biochemical role but does not independently validate the human clinical course. Several specific clinical details in this report (particularly the reported post-transplant mortality and the absence of attempted cholic acid therapy) were derived from **secondary search-engine summaries of the primary paper rather than a direct, verified quote from the paper's own text**, and should be re-verified against the primary source's exact wording (via `just fetch-reference PMID:25326392` and exact-snippet extraction) before being asserted as sourced fact in any `evidence:` block — per this repository's evidence discipline, a paraphrase is a lead, not a citation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25326392` *(abstract only)*: "only one family has been described in the literature and phenotypic association is not confirmed"
  - Text part not found as substring: 'only one family has been described in the literature and phenotypic association is not confirmed' (note: only abstract available for PMID:25326392, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031994` (1 mention) - the report calls it "Abnormal bile acid level"; HP calls it **Bronchial breath sound**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043433` (obsolete negative regulation of DNA-binding transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001928` (1 mention) - the report calls it "Abnormal coagulation"; HP calls it **Abnormality of coagulation**
- `HP:0031964` (1 mention) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating alanine aminotransferase concentration**, and lists "Elevated serum glutamic-pyruvic transaminase" among its other names