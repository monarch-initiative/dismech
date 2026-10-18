---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-06T19:49:26.411290'
end_time: '2026-09-06T19:54:01.797549'
duration_seconds: 275.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Blastic Plasmacytoid Dendritic Cell Neoplasm
  mondo_id: MONDO:0019467
  category: ''
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
  web_search_requests: 18
  num_turns: 22
  total_cost_usd: 1.3488164000000002
  session_id: 4bf4a114-75db-54c3-885d-72412fe47716
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 44
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 23
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 25
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0031969
    reported_labels:
    - Skin nodule
    ontology_label: Reduced blood urea nitrogen
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blastic Plasmacytoid Dendritic Cell Neoplasm
- **MONDO ID:** MONDO:0019467 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Blastic Plasmacytoid Dendritic Cell Neoplasm** covering all of the
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

I'll research Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN) comprehensively using web search and fetch tools, then compile the full report.

I have gathered comprehensive research data. I'll now compile the full report.

I now have sufficient depth across all sections to compile the comprehensive report.

---

# Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN): Comprehensive Research Report

## 1. Disease Information

**Overview.** Blastic plasmacytoid dendritic cell neoplasm (BPDCN) is a rare, clinically aggressive hematologic malignancy derived from the malignant transformation of precursors of plasmacytoid dendritic cells (pDCs). It was formally recognized as a distinct disease entity by the WHO in 2008, following the identification of the plasmacytoid dendritic cell as its cell of origin, and it remains classified as a distinct entity ("Plasmacytoid dendritic cell neoplasms") in the WHO 5th edition classification of haematolymphoid tumours ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK589661/); [PMC10517032](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10517032/), PMID:37407876). It typically presents with disseminated violaceous/bluish-livid cutaneous plaques or nodules together with bone marrow, peripheral blood, and lymph node involvement, and is notable for a high rate of occult central nervous system (CNS) disease.

**Key identifiers:**
- **MONDO:** MONDO:0019467
- **Orphanet:** ORPHA:86870
- **WHO classification (5th ed.):** Plasmacytoid dendritic cell neoplasms lineage, within myeloid neoplasms/acute leukemias of ambiguous lineage
- A specific OMIM entry was not identified in available sources (BPDCN is a somatic/clonal myeloid neoplasm rather than a classic Mendelian OMIM phenotype entry; searches of OMIM did not surface a dedicated phenotype MIM number).

**Synonyms/alternative names:** Blastic NK-cell lymphoma (older term), CD4+/CD56+ hematodermic neoplasm/tumor, agranular CD4+ NK-cell leukemia, blastic natural killer-cell lymphoma, plasmacytoid dendritic cell leukemia.

**Data provenance:** Most quantitative claims below derive from aggregated disease-level resources — population-based cancer registries (SEER), retrospective institutional case series, and pooled clinical-trial cohorts — rather than a single large prospective cohort, reflecting the disease's rarity (**incidence 0.05 per 100,000**; [Blood, ASH abstract 5185](https://ashpublications.org/blood/article/142/Supplement%201/5185/504096/Epidemiology-and-Survival-Outcomes-in-Blastic)).

---

## 2. Etiology

**Disease causal factors.** BPDCN arises from acquired (somatic) genetic and epigenetic lesions in a plasmacytoid dendritic cell precursor; there is no known infectious cause, and known heritable/monogenic causation is limited to rare predisposition contexts (below). Its pathogenesis is best understood as **clonal evolution of an epigenetically dysregulated myeloid/pDC precursor** rather than a single driver mutation.

**Genetic risk factors:**
- **Recurrent somatic mutations in epigenetic-regulator genes** — *TET2*, *ASXL1*, *IDH2*, *EZH2*, *DNMT3A*, *ARID1A/ARID2* — are found in roughly half of cases and are thought to be early/founder events ([eJHaem 2023](https://onlinelibrary.wiley.com/doi/10.1002/jha2.617); [PMC9928664](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9928664/)). **Biallelic TET2 mutations and the canonical ASXL1 c.1934dupG frameshift mutation frequently co-occur.** TET2-mutant pDCs show resistance to UV-induced apoptosis, mechanistically implicating TET2 loss in survival of the malignant clone and its skin tropism.
- **TET2 truncating mutations predict worse outcome** ([Blood Advances](https://doi.org/10.1182/bloodadvances.2022007879)).
- **NPM1 mutations** occur in a subset of cases.
- **Cytogenetic/copy-number lesions:** complex karyotype is common; recurrent deletions of tumor-suppressor loci include **9p21.3 (CDKN2A/CDKN2B, plus neighboring CDKN1B, RB1, CDKN2C)** — biallelic CDKN2A/B deletion is one of the few cytogenetic lesions with proven prognostic (adverse) impact — as well as deletions of **12p13 (ETV6/CDKN1B)**, **13q13-14 (RB1)**, and **6q**. **MYC (8q24) rearrangements/amplification occur in ~40% of cases.**
- **NR3C1 (glucocorticoid receptor, 5q31) monoallelic deletion** occurs in ~28% of BPDCN cases (13/47 in the index cohort), producing haploinsufficiency, reduced glucocorticoid-receptor expression, and steroid resistance, and defines a molecular subgroup with markedly inferior overall survival ([PubMed 27060168](https://pubmed.ncbi.nlm.nih.gov/27060168/)).
- **Germline predisposition context:** BPDCN can arise on a background of **GATA2 deficiency syndrome**, a germline heterozygous loss-of-function GATA2 predisposition to MDS/AML and immunodeficiency; ~75% of symptomatic carriers develop a myeloid malignancy (median onset age 17). While MDS/AML are the dominant GATA2-related myeloid outcomes, GATA2 deficiency is a recognized predisposition backdrop worth screening for in pediatric/young-adult or familial BPDCN.
- **Secondary/clonally-related BPDCN:** 10–20% of BPDCN cases arise in the context of a prior or concomitant myeloid neoplasm (MDS, CMML, AML, CML). Paired sequencing of skin tumor and bone marrow shows **shared ASXL1/TET2 variants**, demonstrating a common clonal origin via progressive clonal hematopoiesis (a shared precursor undergoing divergent differentiation into either a myeloid or a pDC-committed malignant clone).

**Environmental risk factors:** No established environmental, toxin, radiation, or infectious causal exposure is documented in the literature reviewed; this is consistent with BPDCN's classification as a sporadic somatic myeloid neoplasm. **Age** (median 60–70 years) and **sex** (male predominance) are the principal recognized epidemiologic risk correlates (see §9).

**Protective factors:** No specific genetic or environmental protective factors are described in the literature for BPDCN.

**Gene-environment interactions:** Not established; the epigenetic-mutation-driven pathogenesis (TET2/ASXL1) combined with UV-resistance of mutant pDCs may partly explain the tropism for sun-exposed skin, representing a plausible but not fully proven gene–environment mechanistic link.

---

## 3. Phenotypes

**Cutaneous manifestations (most common presenting feature; symptom/sign, HPO-mappable):**
- Violaceous, bluish-livid, or bruise-like cutaneous plaques and nodules, often on sun-exposed sites (trunk, face, extremities), up to ~10 cm; present in **60–100% of patients** depending on the series ([PMC10517032](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10517032/); SEER). Occasionally cutaneous involvement is entirely absent (aleukemic/non-cutaneous presentations do occur).
  - Suggested HPO: **HP:0031969** (skin nodule) / **HP:0100678** (nodular skin lesions); general **HP:0000988** (skin lesion).

**Systemic/laboratory phenotypes:**
- **Cytopenias** (anemia, thrombocytopenia, neutropenia) from marrow infiltration — HP:0001903 (anemia), HP:0001873 (thrombocytopenia), HP:0001875 (neutropenia).
- **Lymphadenopathy** — HP:0002716.
- **Hepatosplenomegaly** — HP:0001433 / HP:0001744.
- **Constitutional symptoms:** fatigue, night sweats, weight loss, pruritus (HP:0025143 fatigue, HP:0000989 pruritus).
- **CNS involvement** at diagnosis or relapse (occult in most cases; ~30% overall incidence, ranging 10–100% depending on detection method) — leptomeningeal infiltration is common; despite this, most patients are neurologically asymptomatic at detection ([Oncotarget](https://www.oncotarget.com/article/7101/); [Cells 2024](https://doi.org/10.3390/cells13030243)).

**Phenotype characteristics:**
- **Age of onset:** Bimodal — a major peak in the 7th decade (60–70 years) and a smaller pediatric/young-adult peak (<20 years) ([PMC10517032](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10517032/)).
- **Severity/progression:** Uniformly aggressive; without treatment the disease progresses rapidly from a cutaneous-predominant phase to leukemic dissemination (marrow, blood, CNS) over weeks to months.
- **Course:** Progressive; frequent early relapse even after chemotherapy-induced remission.
- **Frequency table (site of involvement, note that reported percentages vary substantially by cohort/diagnostic criteria):**
  | Site | Reported frequency |
  |---|---|
  | Skin | 60–100% (one large cohort: 13% as *primary* site) |
  | Bone marrow/peripheral blood | 80–90% (SEER-cohort primary site: 19.1%) |
  | Lymph node | 40–56.6% |
  | CNS (occult, at diagnosis) | ~30% (range 10–100%) |

**Quality of life impact:** Disfiguring, often painful/pruritic skin lesions; systemic B-symptoms; rapid clinical deterioration; substantial psychosocial burden from a rapidly fatal diagnosis. No BPDCN-specific EQ-5D/SF-36 data were identified; QoL data are generally extrapolated from acute leukemia literature.

---

## 4. Genetic/Molecular Information

**Causal/driver genes (recurrently mutated, no single Mendelian causal gene):**
| Gene | HGNC | Role | Approx. frequency |
|---|---|---|---|
| TET2 | hgnc:25941 | Epigenetic (5mC oxidation); loss-of-function, often biallelic | ~30–70% (cohort-dependent) |
| ASXL1 | hgnc:18318 | Epigenetic/PRC2 modulator; canonical c.1934dupG frameshift | ~20–30%, co-occurs with TET2 |
| NPM1 | hgnc:7910 | Nucleophosmin; a subset carry classic AML-type NPM1 insertions | Minority of cases |
| IDH2 | hgnc:5383 | Epigenetic (2-HG-producing neomorphic mutant) | Subset |
| EZH2 | hgnc:3527 | PRC2 catalytic subunit; loss-of-function | Subset; C1 subtype EZH2-dependence |
| DNMT3A | hgnc:2978 | De novo methyltransferase | More frequent in C2/atypical subtype |
| ARID1A/ARID2 | hgnc:11110 / hgnc:16168 | SWI/SNF chromatin remodeling | C1 subtype enrichment |
| NF1, NOTCH2, SF3B1 | — | Enriched in C1 (typical pDC) subtype | Subset |
| SRSF2 | hgnc:10783 | Splicing factor; enriched in C2 (atypical) subtype | Subset |
| TP53 | hgnc:11998 | Tumor suppressor | Subset; adverse prognosis |
| ZRSR2, RAS family | — | Splicing/signaling | Reported recurrently |

**Variant classification:** Most reported variants are somatic; ACMG/AMP germline classification is not generally applicable except in the rare GATA2-deficiency-predisposed cases. ASXL1 c.1934dupG is a well-characterized recurrent truncating (loss-of-function/dominant-negative) frameshift also seen in myeloid neoplasms broadly.

**Somatic vs. germline:** BPDCN is overwhelmingly a **somatic** clonal disease; germline predisposition (GATA2 deficiency) is a minority context, mainly relevant in pediatric/young patients or those with a personal/family history of MDS, immunodeficiency, or lymphedema.

**Functional consequences:**
- TET2/IDH2/DNMT3A/EZH2/ASXL1 lesions converge on **DNA/histone methylation dysregulation**, producing a differentiation block and epigenetically permissive state for malignant transformation.
- TET2-mutant pDCs are **resistant to UV-induced apoptosis**, a proposed mechanistic link to cutaneous tropism.
- **Diphthamide-pathway gene silencing** via DNA methylation confers resistance to tagraxofusp (a diphtheria-toxin fusion); azacitidine can reactivate diphthamide synthesis genes and reverse resistance ([PMID:38338733, cited via PMC10855071](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10855071/)).
- **Decreased TXNRD1** expression has recently been associated with tagraxofusp resistance in a phase II cohort ([Leukemia 2026, s41375-026-03022-0](https://www.nature.com/articles/s41375-026-03022-0)).

**Cytogenetic/structural lesions:**
- Complex karyotype common.
- Deletions: **9p21.3 (CDKN2A/CDKN2B)** — biallelic loss confers poor prognosis; also 12p13, 13q14 (RB1), 6q, and **5q31 (NR3C1)**.
- **MYC (8q24) rearrangement/amplification in ~40%** of cases.

**Chromosomal microarray findings** confirm recurrent 9p21.3 losses spanning cell-cycle regulators (CDKN2A/2B, CDKN1B, RB1, CDKN2C/p18).

**Molecular subtypes (integrative transcriptomic/genomic classification):** Two molecularly and clinically distinct subgroups have been defined ([Blood Cancer Journal 2022, medRxiv 2022.05.26.22275640](https://www.nature.com/articles/s41408-022-00699-1)):
- **C1 ("typical" pDC-derived):** younger patients, higher tumor mutational burden, enriched for EP300, ARID2, NF1, NOTCH2, SF3B1 mutations; EZH2-dependent signaling.
- **C2 ("atypical"/cDC-enriched):** older patients, fewer mutations, enriched for DNMT3A and SRSF2 mutations, higher JAK-STAT and NF-κB transcription-factor activity, and a **trend toward inferior survival**.

A separate genome-wide DNA methylation study further delineates BPDCN's distinct epigenetic signature from related myeloid entities ([Leukemia 2024, s41375-024-02240-8](https://www.nature.com/articles/s41375-024-02240-8)).

---

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or infectious trigger is established for BPDCN in the literature surveyed. Unlike many hematologic malignancies (e.g., no clear benzene, radiation, or chemotherapy-exposure link is consistently documented for de novo BPDCN), the principal recognized "environmental" association is prior cytotoxic therapy/clonal hematopoiesis in the small subset of therapy-related or MDS-antecedent cases. No specific infectious agent (viral, bacterial, fungal, parasitic) has been implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from initiating lesion to clinical manifestation):**

1. **Acquired somatic mutations in epigenetic regulators** (TET2, ASXL1, DNMT3A, IDH2, EZH2 — often biallelic and co-occurring) arise in a hematopoietic/plasmacytoid dendritic cell precursor, **leading to** disrupted DNA methylation and chromatin remodeling (demonstrated in sequencing studies; PMID association strong, mechanistic causality for transformation inferred from parallel clonal-hematopoiesis biology).
2. This epigenetic dysregulation **results in** a partial arrest of pDC differentiation and dysregulated activity of the pDC master transcriptional network (**TCF4/E2-2**, together with **IRF8**, and the **ZEB2–ID2** axis that normally commits progenitors to the pDC versus conventional-DC fate), **leading to** accumulation of an immature, blast-like pDC-lineage clone that nonetheless retains defining pDC identity markers (CD123, TCF4, TCL1, CD303/BDCA2, CD304/BDCA4) — demonstrated directly by TCF4-dependent transcriptional dependency shown in cell-line and xenograft models ([Cancer Cell 2016, PMID:27846392](https://pubmed.ncbi.nlm.nih.gov/27846392/)).
3. TCF4 acts as a **master regulator establishing BPDCN-specific super-enhancers**, which recruit **BRD4**, **leading to** a druggable TCF4–BRD4-dependent transcriptional network that sustains the malignant gene-expression program (demonstrated: BET-inhibitor disruption of this network induces apoptosis in BPDCN cell lines and xenografts).
4. In parallel, cooperating structural/copy-number lesions accumulate — **9p21.3 (CDKN2A/CDKN2B) deletion** disables the RB/p16 cell-cycle checkpoint, **leading to** loss of G1/S control and unchecked proliferation; **MYC rearrangement/amplification** (~40% of cases) **leads to** further transcriptional amplification of proliferative and biosynthetic programs; and **5q31 (NR3C1) deletion** causes glucocorticoid-receptor haploinsufficiency, **resulting in** intrinsic corticosteroid resistance and (via associated dysregulation of the polycomb complex/EZH2 and the HOXA locus) a block in normal pDC differentiation.
5. The malignant pDC-lineage blasts constitutively overexpress **CD123 (IL3RA)**; IL-3 binding **activates JAK/STAT, RAS/MAPK, and PI3K signaling cascades**, **leading to** strong anti-apoptotic and pro-proliferative signaling that supports clonal expansion and survival (demonstrated mechanistically; PMID:38338733).
6. Aberrant, constitutive **NF-κB pathway activation** (a hallmark of BPDCN gene-expression profiling) **leads to** further anti-apoptotic transcriptional output and provides a rationale for NF-κB-pathway-inhibitor sensitivity in preclinical models.
7. The malignant clone exhibits **cutaneous tropism**, homing preferentially to sun-exposed skin — proposed (inferred, not fully proven) to reflect (a) TET2-mutant pDCs' resistance to UV-induced apoptosis and (b) retained normal pDC skin-homing chemokine-receptor biology, **leading to** the characteristic disseminated violaceous cutaneous plaques/nodules that are the most common presenting sign.
8. Concurrently or subsequently, the clone disseminates to **bone marrow, peripheral blood, lymph nodes, and the CNS** (occult leptomeningeal involvement in up to ~30% of patients at diagnosis, a step whose mechanism is largely undemonstrated beyond generic leukemic dissemination), **resulting in** cytopenias, lymphadenopathy, hepatosplenomegaly, and (rarely symptomatic) CNS disease.
9. Without CD123-targeted or intensive multi-agent therapy, this progression **leads to** rapid clinical deterioration and death, with median untreated survival of 8–14 months.
10. Under **tagraxofusp (SL-401)** therapy, CD123 binding **triggers internalization of the fused diphtheria-toxin payload**, **leading to** inhibition of protein synthesis and cell death in CD123-high malignant pDCs — but epigenetic silencing (DNA methylation) of the diphthamide-biosynthesis pathway genes can **block toxin activation**, **resulting in** treatment resistance; azacitidine can reverse this by reactivating diphthamide-pathway gene expression, and reduced TXNRD1 expression has also been separately associated with resistance.

**Molecular pathways involved:** JAK/STAT, RAS/MAPK, PI3K-AKT (downstream of CD123/IL3RA), NF-κB (constitutively active, druggable), EZH2/PRC2 polycomb signaling (C1 subtype dependency), TCF4–BRD4 super-enhancer network.
- Suggested GO terms: **GO:0038156** (interleukin-3-mediated signaling pathway), **GO:0007249** (I-kappaB kinase/NF-kappaB signaling), **GO:0007259** (JAK-STAT cascade), **GO:0016575** (histone deacetylation)/**GO:0006306** (DNA methylation).

**Cellular processes:** Block of terminal pDC differentiation; resistance to apoptosis (both UV-induced and drug-induced); clonal expansion; T-cell exhaustion in the tumor microenvironment (single-cell data below).

**Protein dysfunction:** TET2 loss-of-function (impaired 5-methylcytosine oxidation), ASXL1 truncation (loss of PRC2-interacting function), EZH2 dysregulation (either loss- or context-dependent gain-of-function across myeloid neoplasms), NR3C1 haploinsufficiency (reduced glucocorticoid receptor protein dosage).

**Immune system involvement:** Malignant pDCs are professional type-I interferon-producing immune cells; the disease itself is a proliferation *of* an immune-lineage cell rather than classically autoimmune. Single-cell studies show **increased CD8+ T-cell exhaustion**, **upregulated interferon-alpha response signatures**, and **downregulated TNF-alpha signaling** within the BPDCN bone marrow microenvironment, indicating an immunosuppressive niche ([Frontiers Immunol 2022, PMC8960171](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8960171/)).

**Molecular profiling (single-cell/omics):**
- Bulk RNA-seq/gene-expression profiling defined the C1/C2 molecular subtypes (above).
- Single-cell multiomics (bone marrow, 5 BPDCN patients vs. 5 healthy controls, 52,803 cells including 18,779 T-cells) revealed clonal T-cell expansions, CD8+ exhaustion, IFN-alpha upregulation, and TNF-alpha downregulation.
- A 2024–2025 multi-organ single-cell study (bone marrow, PBMC, skin) found that **skin-infiltrating malignant cells show greater maturity/differentiation than bone-marrow blasts**, suggesting bone marrow as the more likely disease origin, and identified **PLD4** as a candidate biomarker/therapeutic target ([Cancer Cell Int 2025, s12935-025-04038-9](https://link.springer.com/article/10.1186/s12935-025-04038-9)).
- Genome-wide DNA methylation profiling delineates BPDCN from related AML/MDS entities by distinct methylation signatures, particularly in interleukin/inflammatory signaling genes ([Leukemia 2024](https://www.nature.com/articles/s41375-024-02240-8)).

Suggested CL (Cell Ontology) terms: **CL:0000784** (plasmacytoid dendritic cell); suggested GO Cellular Component terms for subcellular involvement: nuclear chromatin (epigenetic dysregulation), plasma membrane (CD123/IL3RA receptor complex).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin (dermis/subcutis), bone marrow, peripheral blood, lymph nodes.
- **Secondary/extramedullary:** Spleen, liver, CNS/leptomeninges, occasionally other extranodal sites.
- **Body systems:** Hematologic/lymphoid system primarily; integumentary system (skin) as the dominant presenting site; nervous system in a substantial minority (CNS).

**Tissue and cell level:**
- Neoplastic infiltrate of small- to medium-sized basophilic blasts extending from dermis into subcutaneous fat.
- Cell type: malignant plasmacytoid dendritic cell precursor — **CL:0000784** (plasmacytoid dendritic cell), or a precursor/blast state thereof.
- Suggested UBERON terms: **UBERON:0002097** (skin), **UBERON:0002371** (bone marrow), **UBERON:0000029** (lymph node), **UBERON:0001017** (central nervous system).

**Subcellular level:**
- Nucleus: hyperchromatic nuclei with prominent nucleoli, chromatin/epigenetic dysregulation (GO:0000785 chromatin).
- Cell surface: CD123 (IL3RA) receptor overexpression on the plasma membrane, the basis for CD123-targeted therapeutics.

**Localization:** Cutaneous lesions frequently favor sun-exposed sites (trunk, face, extremities); disease is typically **multifocal/disseminated** rather than strictly lateralized, though individual lesions can be solitary at initial presentation.

---

## 8. Temporal Development

**Onset:** Bimodal age distribution — predominant peak in the 7th decade (60–70 years), secondary smaller peak in children/young adults (<20 years). Onset is typically **subacute to acute**, with rapidly evolving cutaneous lesions over weeks and systemic dissemination following if untreated.

**Progression:**
- **Stages:** Cutaneous-only/localized disease may be the initial presentation, but the disease is understood as **systemic from the outset** in the majority of cases (occult marrow/CNS involvement often present even when clinically localized).
- **Rate:** Rapid/aggressive; without treatment, progression from skin-limited to leukemic/disseminated disease and death occurs within months.
- **Course pattern:** Progressive, with frequent early relapse post-chemotherapy; CNS relapse is a recognized recurrence pattern even during systemic remission.
- **Duration:** Without treatment, median survival 8–14 months (SEER/pooled clinical literature); rare cases described as smoldering/indolent are anecdotal.

**Patterns:**
- Remission is achievable pharmacologically (tagraxofusp, chemotherapy) but is rarely durable without consolidative hematopoietic stem cell transplantation (HSCT).
- No well-defined spontaneous-remission pattern is described.
- **Critical intervention window:** Achieving a complete or clinical-complete response with induction therapy, followed promptly by allogeneic (or in select cases autologous) HSCT while in remission, is the recognized period of maximal opportunity to improve long-term survival.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** ~0.05 cases per 100,000 population overall (US population-based estimate); BPDCN comprises **~0.44–0.5% of all hematologic malignancies** and <1% of acute leukemias/cutaneous lymphomas ([ASH 2023 abstract 5185](https://ashpublications.org/blood/article/142/Supplement%201/5185/504096/Epidemiology-and-Survival-Outcomes-in-Blastic); [PMC10517032](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10517032/)).
- **Prevalence** figures specific to BPDCN were not identified in a dedicated registry; given its incidence and aggressive/short natural history, point prevalence is expected to be extremely low (ultra-rare).

**Inheritance pattern:** BPDCN itself is not a classically inherited Mendelian disease; it is an acquired somatic clonal neoplasm. A minority of cases arise on a background of germline **GATA2 deficiency** (autosomal dominant, with variable penetrance; ~75% of symptomatic carriers develop myeloid malignancy by a median age of 17, though BPDCN specifically is a less common outcome than MDS/AML in this syndrome).

**Penetrance/expressivity:** Not applicable to sporadic BPDCN; for GATA2-deficiency-associated cases, myeloid malignancy penetrance is high (~75%) but age-dependent and variably expressive across the phenotypic spectrum (MDS, AML, BPDCN, immunodeficiency, lymphedema).

**Population demographics:**
- **Sex ratio:** Marked **male predominance**, approximately **3:1 (M:F)**.
- **Race/ethnicity:** Incidence is reported to be lower in females than males and **lower in African Americans compared with Caucasians**; the majority of reported cases are in Caucasian males.
- **Geographic distribution:** No strong endemic geographic clustering reported; case series are global (US, Europe, Asia) without a clearly described geographic incidence gradient.
- **Age distribution:** Bimodal, with the dominant burden in older adults (60–70s) and a smaller pediatric/young-adult cluster.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Peripheral blood/bone marrow examination:** cytopenias, circulating blasts, marrow blast infiltration.
- **Biopsy (skin, marrow, or nodal):** histopathology showing diffuse infiltrates of small-to-medium basophilic blasts with high mitotic/apoptotic rate; immunohistochemistry is central to diagnosis.

**Immunophenotype/diagnostic criteria (WHO 5th edition, updated criteria):**
Diagnosis requires either:
1. **CD123 plus at least one other pDC marker** (TCF4, TCL1, CD303/BDCA2, or CD304/BDCA4) **in addition to CD4 and/or CD56**, or
2. **Any three of the four pDC markers (TCF4, TCL1, CD303, CD304)** together with **absence of expected negative lineage markers**.

- **Expected positive markers:** CD123, TCF4, TCL1, CD303, CD304, CD4, CD56 (CD56 often only weakly/dimly expressed).
- **Expected negative markers:** CD3, CD14, CD19, CD34, myeloperoxidase, lysozyme.
- Dual TCF4/CD123 expression is reported as highly sensitive and specific.
- 10-color flow cytometric panels have been developed both for initial diagnosis and for measurable/residual disease monitoring.

**Genetic testing:** No single confirmatory gene test; **targeted or comprehensive NGS panels** covering TET2, ASXL1, NPM1, IDH2, EZH2, DNMT3A, TP53, ARID1A/2, SF3B1, SRSF2, NF1, NOTCH2 are used to characterize the clone, assess molecular subtype (C1 vs. C2), and detect prognostically relevant lesions (e.g., biallelic 9p21.3/CDKN2A-B deletion, 5q31/NR3C1 deletion, MYC rearrangement). **Chromosomal microarray/karyotyping** is used to detect complex karyotype and specific deletions.

**Omics-based diagnostics:** Not yet standard of care but under active research — gene-expression profiling for C1/C2 subtyping, genome-wide DNA methylation profiling for entity-defining epigenetic signatures, and single-cell transcriptomics for microenvironment characterization.

**Clinical criteria/differential diagnosis:** BPDCN must be distinguished from other CD56+ cutaneous-tropic hematologic malignancies, including **leukemia cutis (AML/myeloid sarcoma)**, **extranodal NK/T-cell lymphoma**, and **cutaneous T-cell lymphoma**; a specific diagnostic pitfall is AML mimicking BPDCN immunophenotypically, prompting proposed refinements incorporated into the WHO-5 criteria ([Case Reports in Hematology 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/5014728)).

**Screening:** No population or targeted screening programs exist given the disease's rarity and sporadic nature; in known GATA2-deficiency kindreds, periodic hematologic surveillance (not BPDCN-specific) is recommended.

---

## 11. Outcome/Prognosis

**Survival and mortality:**
- **Untreated/historical median overall survival: 8–14 months.**
- With modern regimens including tagraxofusp and/or intensive chemotherapy: **median OS in the range of 18–24 months** in several series ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK589661/); pooled literature).
- **First-line tagraxofusp pivotal trial (NCT02113982):** complete response/clinical CR in **57%**, overall response rate **75%**, median duration of CR/CRc **24.9 months** ([ASH abstract](https://ashpublications.org/blood/article/138/Supplement%201/874/482632/); [JCO 2022](https://ascopubs.org/doi/10.1200/JCO.22.00034)).
- **Allogeneic HSCT in first remission** is associated with markedly better outcomes: in one series, **median OS not reached** after allo-SCT versus **2.6 months** in non-transplanted patients, with **1-year OS of 64%** post-transplant.

**Morbidity/complications:** Cytopenia-related infections and bleeding, CNS relapse, capillary leak syndrome (a recognized tagraxofusp-specific adverse effect), and disease-related disfigurement from cutaneous lesions.

**Prognostic factors:**
- **Adverse:** biallelic CDKN2A/CDKN2B (9p21.3) deletion, TET2 truncating mutations, NR3C1 (5q31) deletion/haploinsufficiency, complex karyotype, older age, C2 (atypical/cDC-enriched) molecular subtype.
- **Favorable:** achievement of CR with induction, consolidation with allogeneic (or autologous) HSCT, C1 (typical pDC-derived) molecular subtype (though it can still relapse), younger age.

**Prognostic biomarkers:** 9p21.3/CDKN2A-B deletion status, NR3C1 deletion, TET2 mutation type (truncating vs. missense), C1/C2 molecular classification, and emerging resistance markers (diphthamide-pathway silencing, TXNRD1 expression) for tagraxofusp response prediction.

---

## 12. Treatment

**Pharmacotherapy — targeted (CD123-directed):**
- **Tagraxofusp-ersz (SL-401):** the **only FDA- and EMA-approved therapy for BPDCN**. It is a fusion protein of recombinant human IL-3 and a truncated diphtheria toxin; binding to CD123/IL3RA triggers receptor-mediated internalization and toxin-mediated cell death. NCCN designates it the **preferred first-line therapy** for patients eligible for intensive induction ([Medscape/NCCN 2023](https://reference.medscape.com/viewarticle/995535); [NEJM 2019](https://www.nejm.org/doi/full/10.1056/NEJMoa1815105)).
  - Suggested NCIT term: therapeutic agent (CD123-targeted fusion toxin); treatment_term likely **NCIT:C15986** (Pharmacotherapy) with therapeutic_agent bound to tagraxofusp's NCIT identifier if available, or targeted therapy **NCIT:C93352**.
- Notable adverse effect: **capillary leak syndrome**, a class effect of IL-3/toxin fusion proteins requiring monitoring (albumin, weight, blood pressure).

**Combination/novel regimens:**
- **Tagraxofusp + venetoclax** (BCL2 inhibitor) — under phase II investigation for treatment-naive patients (e.g., NCT07007052), rationale being that tagraxofusp-surviving cells upregulate BCL2.
- **Tagraxofusp + hyper-CVAD + venetoclax** — phase II trial for newly diagnosed or relapsed/refractory disease.
- **Azacitidine + venetoclax** — used particularly to re-sensitize tagraxofusp-resistant clones by reversing diphthamide-pathway silencing, or as an alternative regimen.
- **Hyper-CVAD (ALL-type)** and **CHOP (lymphoma-type)** regimens remain NCCN-listed alternate induction options; AML-type regimens are also used.

**Advanced therapeutics (investigational):**
- **CAR-T cell therapy (CD123-directed):** Autologous CD28/4-1BB CD123 CAR-T constructs eliminate patient-derived BPDCN cells preclinically without significant off-tumor toxicity; **allogeneic UCART123** offers an off-the-shelf option. A phase 1 trial (41 AML/BPDCN patients, 21 receiving CAR-T infusion including 2 BPDCN patients) showed no dose-limiting toxicity, prolonged myelosuppression, or GVHD ([PMC13536854](https://pmc.ncbi.nlm.nih.gov/articles/PMC13536854/)). A December 2024 case report describes autologous stem-cell rescue followed by anti-CD123 CAR-T (Day +2), achieving MRD-negative CR with disease-free survival >13 months.
- **CD123-targeted CAR-NK cell therapy:** actively in phase 1 trials (NCT06006403, NCT06690827) as of 2025–2026.
- **Bispecific T-cell engagers:** flotetuzumab (CD123×CD3) showed 26.7% CR/CRh, median OS 10.2 months, primarily studied in AML with relevance to BPDCN; newer constructs (e.g., APVO436) show improved tolerability.
- **BET inhibitors:** target the TCF4–BRD4 super-enhancer dependency; preclinical efficacy in xenografts, not yet approved.

**Hematopoietic stem cell transplantation:**
- **Allogeneic HSCT in first CR** is the standard consolidation for eligible patients and confers the largest survival benefit demonstrated to date (median OS not reached vs. 2.6 months without transplant in one cohort; 1-year OS 64% post-transplant).
- **Autologous HSCT** is considered for patients ineligible for allogeneic transplant, sometimes combined with CAR-T consolidation.

**CNS-directed therapy:** Given the high rate of occult CNS involvement (~30%), **prophylactic or therapeutic intrathecal chemotherapy (methotrexate and/or cytarabine)** is increasingly recommended as mandatory alongside first-line induction, based on retrospective evidence of improved OS and CNS-relapse-free survival with early IT treatment ([Oncotarget](https://www.oncotarget.com/article/7101/); [Cells 2024](https://doi.org/10.3390/cells13030243)).

**Supportive care:** Management of cytopenias, infection prophylaxis, and skin-lesion wound care; capillary leak syndrome monitoring/prophylaxis (e.g., albumin supplementation) during tagraxofusp therapy.

**Treatment algorithm summary:** Induction (tagraxofusp preferred, or hyper-CVAD/CHOP/AML-type regimen) + intrathecal CNS prophylaxis → assessment of response → consolidation with allogeneic HSCT (preferred) or autologous HSCT if in CR → relapsed/refractory disease managed with venetoclax-based combinations, CAR-T/CAR-NK, or clinical trial enrollment.

**Pharmacogenomics:** Not well characterized specifically for BPDCN beyond the diphthamide-pathway/TXNRD1 resistance biology described above for tagraxofusp.

---

## 13. Prevention

Given BPDCN's sporadic, non-environmentally-linked etiology, there are **no established primary prevention strategies** (no vaccination, no modifiable lifestyle risk factor identified). 

**Secondary prevention/early detection:** Population or targeted screening is not feasible or recommended given extreme rarity; however, **clinical vigilance for cutaneous violaceous lesions in older males**, and **hematologic surveillance in known GATA2-deficiency kindreds** (a nonspecific myeloid-malignancy screening context rather than BPDCN-specific), represent the closest analogs to secondary prevention.

**Tertiary prevention:** Early recognition of occult CNS disease with **prophylactic intrathecal chemotherapy** at diagnosis is the clearest evidence-based tertiary-prevention measure, reducing CNS relapse risk.

**Genetic counseling:** Relevant specifically for patients found to have germline GATA2 pathogenic variants, where family screening and counseling regarding myeloid malignancy risk is appropriate (per general GATA2-deficiency-syndrome guidance, not BPDCN-specific literature).

---

## 14. Other Species / Natural Disease

No dedicated report of spontaneously occurring BPDCN in companion animals or wildlife was identified in the reviewed literature (searches for veterinary/OMIA-cataloged natural disease did not surface BPDCN-specific entries). Plasmacytoid dendritic cells and their developmental transcription-factor network (TCF4/E2-2 orthologs, IRF8, ZEB2) are conserved across mammals (mouse well characterized), but no natural neoplastic pDC disease analogous to human BPDCN in mouse, dog, cat, or other veterinary species was found in this search. This should be treated as a **gap** rather than a confirmed absence, pending a dedicated OMIA/veterinary-pathology search.

**Taxonomy:** Human disease — NCBITaxon:9606 (*Homo sapiens*).

---

## 15. Model Organisms

**Cell line models:** **CAL-1** and **GEN2.2** are the principal established human BPDCN cell lines used across the mechanistic literature (TCF4-BRD4 network studies, drug screening).

**Xenograft models:** Human BPDCN xenografts are generated by subcutaneous injection of CAL-1/GEN2.2 cells into **NOD/SCID mice**; these models demonstrated that **BET inhibition (e.g., CPI-203) attenuates tumor growth** in vivo, supporting BET inhibitors as a targeted therapeutic strategy ([Cancer Cell 2016, PMID:27846392](https://www.cell.com/cancer-cell/fulltext/S1535-6108(16)30489-5)). Patient-derived xenograft (PDX) models in immunodeficient mice (e.g., NSG) are also used more generally for pediatric leukemia modeling and, by extension, rare leukemia subtypes such as BPDCN, to test CD123-directed CAR-T efficacy preclinically.

**Genetic/induced models:** No conventional BPDCN-specific knockout/knock-in mouse model recapitulating the full disease was identified; instead, the field relies on (a) human cell-line xenografts and (b) mechanistic mouse genetics of normal pDC development (Zeb2, Id2, Irf8, Tcf4/E2-2 conditional knockouts) to infer the differentiation-block mechanism underlying BPDCN, since these transcription factors govern the normal pDC-versus-cDC1 fate decision that BPDCN is thought to hijack ([PNAS 2016](https://www.pnas.org/doi/10.1073/pnas.1611408114); [Nat Immunol 2019](https://www.nature.com/articles/s41590-019-0449-3)).

**Model characteristics/limitations:** CAL-1/GEN2.2 xenografts faithfully recapitulate the CD123-high, TCF4-dependent transcriptional program and respond to BET inhibition and CD123-targeted immunotherapy preclinically, but do not model the full clonal-evolution process (founder TET2/ASXL1 mutations, secondary MDS-to-BPDCN transformation) or the tumor-immune microenvironment (T-cell exhaustion) seen in patients — these remain modeled only indirectly via patient single-cell data rather than in animal systems.

**Applications:** These models are primarily used for (1) mechanistic validation of the TCF4-BRD4 transcriptional dependency, (2) preclinical testing of CD123-directed agents (tagraxofusp analogs, CAR-T/CAR-NK, bispecifics), and (3) drug-resistance mechanism studies (diphthamide pathway, BCL2 upregulation).

---

## Summary of Suggested Ontology Term Bindings

| Category | Term | ID |
|---|---|---|
| Disease | Blastic plasmacytoid dendritic cell neoplasm | MONDO:0019467 / ORPHA:86870 |
| Cell type | Plasmacytoid dendritic cell | CL:0000784 |
| Anatomy | Skin | UBERON:0002097 |
| Anatomy | Bone marrow | UBERON:0002371 |
| Anatomy | Lymph node | UBERON:0000029 |
| Anatomy | Central nervous system | UBERON:0001017 |
| Gene | TET2 | hgnc:25941 |
| Gene | ASXL1 | hgnc:18318 |
| Gene | NPM1 | hgnc:7910 |
| Gene | IDH2 | hgnc:5383 |
| Gene | EZH2 | hgnc:3527 |
| Gene | DNMT3A | hgnc:2978 |
| Gene | CDKN2A | hgnc:1787 |
| Gene | NR3C1 | hgnc:7978 |
| Gene | MYC | hgnc:7553 |
| Gene | IL3RA (CD123) | hgnc:6012 |
| Gene | GATA2 | hgnc:4172 |
| Phenotype | Skin nodule | HP:0031969 |
| Phenotype | Anemia | HP:0001903 |
| Phenotype | Thrombocytopenia | HP:0001873 |
| Phenotype | Lymphadenopathy | HP:0002716 |
| GO Process | Interleukin-3-mediated signaling pathway | GO:0038156 |
| GO Process | JAK-STAT cascade | GO:0007259 |
| GO Process | I-kappaB kinase/NF-kappaB signaling | GO:0007249 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Hematopoietic cell transplantation | NCIT:C15431 |
| Treatment | Targeted therapy | NCIT:C93352 |

---

## Sources

- [Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN): 2025 Update on Diagnosis, Pathophysiology, Risk Assessment, and Management (PMID:40525728)](https://pubmed.ncbi.nlm.nih.gov/40525728/)
- [Blastic Plasmocytoid Dendritic Cell Neoplasm (BPDCN): Clinical Features and Histopathology with a Therapeutic Overview (PMC10742669)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10742669/)
- [SEER Hematopoietic and Lymphoid Neoplasm Database — BPDCN](https://seer.cancer.gov/seertools/hemelymph/51f6cf56e3e27c3994bd530c/)
- [StatPearls — Blastic Plasmacytoid Dendritic Cell Neoplasm](https://www.ncbi.nlm.nih.gov/books/NBK589661/)
- [Integrative molecular profiling identifies two molecularly and clinically distinct subtypes of BPDCN — Blood Cancer Journal](https://www.nature.com/articles/s41408-022-00699-1)
- [BPDCN: a rare hematologic neoplasm with frequent cutaneous involvement (PMID:37407876)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10517032/)
- [Biallelic TET2 mutations and canonical ASXL1 mutations in BPDCN — eJHaem 2023](https://onlinelibrary.wiley.com/doi/10.1002/jha2.617)
- [TET2 truncating mutations predict worse outcome in BPDCN — Blood Advances](https://doi.org/10.1182/bloodadvances.2022007879)
- [BPDCN: ontogeny, immunophenotype, genetics and epigenetics — Leukemia (2026)](https://www.nature.com/articles/s41375-026-03067-1)
- [Breakthrough in BPDCN Cancer Therapy Owing to Precision Targeting of CD123 (PMC10855071)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10855071/)
- [Recent Advances in the Biology and CD123-Directed Treatment of BPDCN](https://www.sciencedirect.com/science/article/pii/S2152265023021985)
- [Tagraxofusp in Blastic Plasmacytoid Dendritic-Cell Neoplasm — NEJM 2019](https://www.nejm.org/doi/full/10.1056/NEJMoa1815105)
- [Long-Term Benefits of Tagraxofusp for Patients With BPDCN — JCO 2022](https://ascopubs.org/doi/10.1200/JCO.22.00034)
- [Tagraxofusp subanalyses of pivotal trial — ASH 2021](https://ashpublications.org/blood/article/138/Supplement%201/874/482632/)
- [Epidemiology and Survival Outcomes in BPDCN: A US Population-Based Study — ASH 2023](https://ashpublications.org/blood/article/142/Supplement%201/5185/504096/)
- [BPDCN: a comprehensive review in pediatrics, adolescents, and young adults — Leukemia 2023](https://www.nature.com/articles/s41375-023-01968-z)
- [Genetics of Blastic Plasmacytoid Dendritic Cell Neoplasms — Encyclopedia MDPI](https://encyclopedia.pub/entry/26994)
- [Blastic plasmacytoid dendritic cell neoplasm: a short review and update (PMC11406213)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11406213/)
- [Haploinsufficiency for NR3C1 in BPDCN (PMID:27060168)](https://pubmed.ncbi.nlm.nih.gov/27060168/)
- [Genetics and Epigenetics in Neoplasms with Plasmacytoid Dendritic Cells — Cancers 2022](https://www.mdpi.com/2072-6694/14/17/4132)
- [BPCDN Clinical Practice Guidelines (NCCN, 2023) — Medscape](https://reference.medscape.com/viewarticle/995535)
- [BPDCN: state of the art — Hematology ASH Education Program 2024](https://ashpublications.org/hematology/article/2024/1/279/526238/)
- [Anti-CD123 CAR-T combined with autologous SCT and venetoclax maintenance in refractory BPDCN (PMC13473410)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13473410/)
- [A phase 1 trial of CD123-directed CAR T-cell therapy in AML/BPDCN (PMC13536854)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13536854/)
- [CD123-directed allogeneic CAR-T (UCART123) in BPDCN — clinicopathological insights](https://pubmed.ncbi.nlm.nih.gov/35963025/)
- [Current status and future potential of CD123-based targeted therapies for acute leukemia — 2025](https://www.tandfonline.com/doi/full/10.1080/14712598.2025.2608209)
- [A Druggable TCF4- and BRD4-Dependent Transcriptional Network Sustains Malignancy in BPDCN — Cancer Cell 2016 (PMID:27846392)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(16)30489-5)
- [Transcription factor Zeb2 regulates commitment to plasmacytoid dendritic cell and monocyte fate — PNAS 2016](https://www.pnas.org/doi/10.1073/pnas.1611408114)
- [An Nfil3–Zeb2–Id2 pathway imposes Irf8 enhancer switching during cDC1 development — Nature Immunology 2019](https://www.nature.com/articles/s41590-019-0449-3)
- [Blastic plasmacytoid dendritic cell neoplasm frequently shows occult CNS involvement and benefits from intrathecal therapy — Oncotarget](https://www.oncotarget.com/article/7101/)
- [BPDCN: A Comprehensive Review of the Disease, CNS Presentations, and Treatment Strategies — Cells 2024](https://doi.org/10.3390/cells13030243)
- [Single-Cell Multiomics Reveals Clonal T-cell Expansions and Exhaustion in BPDCN — Frontiers in Immunology 2022 (PMC8960171)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8960171/)
- [Multi-organ single-cell analysis reveals PLD4 as a biomarker of BPDCN — Cancer Cell International 2025](https://link.springer.com/article/10.1186/s12935-025-04038-9)
- [Genome-wide DNA methylation-analysis delineates BPDCN from related entities — Leukemia 2024](https://www.nature.com/articles/s41375-024-02240-8)
- [Decreased TXNRD1 associated with tagraxofusp resistance in BPDCN — Leukemia 2026](https://www.nature.com/articles/s41375-026-03022-0)
- [The spectrum of GATA2 deficiency syndrome — PubMed](https://pubmed.ncbi.nlm.nih.gov/36455197/)
- [GATA2 deficiency syndrome: A decade of discovery (PMC9291163)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9291163/)
- [BPDCN secondary to AML with shared TET2/DNMT3A mutations — case report and literature review (PMC12727995)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12727995/)
- [Early detection of transformation to BPDCN in a patient with MDS (PMID:30323983)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6174068/)
- [Mondo Disease Ontology — GitHub issue on Orphanet/OMIM mapping](https://github.com/monarch-initiative/mondo/issues/2693)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031969` (2 mentions) - the report calls it "Skin nodule"; HP calls it **Reduced blood urea nitrogen**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (1 mention)
- `GO:0006306` (obsolete DNA methylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001875` (1 mention) - the report calls it "neutropenia"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `GO:0007249` (2 mentions) - the report calls it "I-kappaB kinase/NF-kappaB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0007259` (2 mentions) - the report calls it "JAK-STAT cascade"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "JAK-STAT cascade" among its other names
- `UBERON:0002097` (2 mentions) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001903` - called "anemia", "Anemia"
- `HP:0001873` - called "thrombocytopenia", "Thrombocytopenia"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.