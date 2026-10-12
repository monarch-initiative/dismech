---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T14:29:08.049105'
end_time: '2026-10-08T14:34:25.797388'
duration_seconds: 317.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cardiomyopathy Dilated 2D
  mondo_id: MONDO:0030300
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 21
  total_cost_usd: 2.0779492000000004
  session_id: e866af8d-4ea5-4264-9c77-1c4910f5c1ff
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 10
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 17
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC9600237
  - PMID:37308880
  relevance_assessed: 26
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 7
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0081160
    reported_labels:
    - DOID
    ontology_label: dilated cardiomyopathy 2D
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 2D
- **MONDO ID:** MONDO:0030300 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 2D** covering all of the
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

RPL3L confirmed. Let me search the literature.

I'm pulling exact abstract quotes for the RPL3L/CMD2D papers. Next I'll check the variants in the original Ganapathi 2020 paper and the mechanism papers, then write the report.

I have enough sourced material and am writing the report now.

# Cardiomyopathy, Dilated, 2D (CMD2D; RPL3L-related neonatal dilated cardiomyopathy): research report

**Prepared:** 2026-10-08 · **Target:** MONDO:0030300 · **Category:** Mendelian (autosomal recessive)

**How this was made.** The PubMed records were pulled through NCBI E-utilities. Quoted sentences come from an extraction tool and are labelled as abstract quotes. They have **not** been checked against `references_cache/`, so run `just fetch-reference PMID:…` and confirm each snippet before using it as KB evidence.

The only identifiers I confirmed directly are:
- **MONDO:0030300**, from `cache/mondo/terms.csv`
- **HP:0001644** (Dilated cardiomyopathy), already in the draft entry
- **HGNC:10351** for RPL3L, which appears in the GenCC submission URL

All other ontology suggestions below are **labels to look up**, not CURIEs. That follows the repository rule against writing identifiers from memory.

---

## 1. Disease information

**Overview.** CMD2D is a rare, autosomal recessive, early-onset and usually fulminant dilated cardiomyopathy. It is caused by biallelic variants in *RPL3L*, a ribosomal protein made only in heart and skeletal muscle. Ganapathi et al. (2020) first described it: "bi-allelic pathogenic variants in RPL3L are causative of an early-onset, severe neonatal form of dilated cardiomyopathy" (PMID:32514796, abstract).

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0030300 "cardiomyopathy, dilated, 2D" | Verified (local cache) |
| OMIM phenotype | 619371 | Secondary sources only (search snippets, NORD/MONDO page). Confirm on omim.org. One 2026 case report uses OMIM #115200 (the general CMD1A series), so numbering varies between sources. |
| OMIM gene (RPL3L) | 617416 | Per Genomics England PanelApp. Confirm. |
| HGNC | HGNC:10351 (repo form `hgnc:10351`) | From the GenCC submission URL. Confirm with `just validate-terms`. |
| DOID | DOID:0081160 | Search hit only. Confirm. |
| Orphanet / ICD-10 / ICD-11 / MeSH | No CMD2D-specific code found | Falls under general DCM codes (ICD-10 I42.0). |

**Synonyms:** CMD2D; RPL3L-related dilated cardiomyopathy; neonatal dilated cardiomyopathy due to RPL3L deficiency.

**Data provenance:** Aggregated from case reports and small family series. There are no registries or EHR cohorts.

## 2. Etiology

- **Cause:** Biallelic (mostly compound heterozygous, occasionally homozygous) germline *RPL3L* variants. These are mostly missense in the conserved RPL3 domain, plus a few frameshift and synonymous/splice-region alleles (PMID:32514796, 35323613, 37308880, 42156347).
- **Carrier parents are unaffected.** Each allele was "harbored in unaffected heterozygous parents" (PMID:35323613), which supports recessive inheritance.
- **Consanguinity:** Present in some families, such as the Colombian family (PMID:32514796; Das review PMC9600237). A Saudi consanguineous cohort of 205 childhood-cardiomyopathy probands reported *RPL3L* among "7 novel candidates" with homozygous variants (PMID:32870709).
- **Environmental risk or protective factors:** None reported. This is a monogenic disorder.
- **Related heterozygous signal (a separate phenotype, not CMD2D).** Common and low-frequency *RPL3L* variants are linked to atrial fibrillation: "one missense (OR = 1.20) and one splice-donor variant (OR = 1.50) in RPL3L" (Thorolfsdottir 2018, PMID:30271950). The variants are p.Ala75Val and c.1167+1G>A, and "the splice-donor variant in RPL3L results in exon skipping." Rare-variant collapsing in UK Biobank also tied *RPL3L* to AF (PMID:38390584), and the gene is an AF / P-wave-duration locus (PMID:32822252).
  - For the KB, this is a separate susceptibility claim. If included, use `relationship_type: SUSCEPTIBILITY` or a note, not a CMD2D phenotype.
- **Gene–environment interactions:** None described.

## 3. Phenotypes

Fewer than 20 published patients exist. Zhang et al. counted "only 13 patients with RPL3L-related CMD2D" before their case (PMID:40820268), and a 2026 summary cites about 14 individuals from 11 families. Frequencies are therefore approximate counts, not prevalence estimates.

| Phenotype | HPO label to look up | Onset / course | Frequency (n ≈ 15–17) | Source |
|---|---|---|---|---|
| Dilated cardiomyopathy | Dilated cardiomyopathy (HP:0001644, verified) | Neonatal to early infancy (day 1 to about 2.5 months); fulminant | All cases | PMID:32514796, 36291431 |
| Congestive / acute heart failure | Congestive heart failure | Rapid decompensation | Almost all | "rapidly progressive neonatal DCM and heart failure with a poor prognosis" (PMID:35323613) |
| Reduced LV systolic function | Reduced left ventricular ejection fraction / Decreased fractional shortening | e.g. EF 31% (PMID:42156347); FS 13% (Das index case) | All with echo data | PMID:42156347, PMC9600237 |
| Mitral regurgitation | Mitral regurgitation | Secondary | 6/7 in Das review table | PMC9600237 |
| Tricuspid regurgitation | Tricuspid regurgitation | Secondary | 3/7 | PMC9600237 |
| ST-T abnormalities | Abnormal T-wave / ST segment (look up) | — | 5/7 | PMC9600237 |
| Right bundle branch block | Right bundle branch block | — | 1/7 | PMC9600237 |
| Pulmonary hypertension | Pulmonary arterial hypertension | — | 1/7 | PMC9600237 |
| Poor feeding, breathlessness, lethargy | Feeding difficulties; Dyspnea; Lethargy | Presenting symptoms | Case-level | PMID:42156347 |
| Myocardial fibrosis and cardiomyocyte death (histology) | Myocardial fibrosis | Explant / biopsy | 1 detailed case | "Histopathological analysis revealed cardiomyocyte death, collagen deposition…" (PMID:40820268) |
| Sarcomere and mitochondrial ultrastructural abnormalities | Look up (cellular) | — | 1 case | PMID:40820268 |
| Death in infancy | Death in infancy | Day 15 to day 124 | 5/7 in Das table | PMC9600237 |

- **Incidental findings:** Patent foramen ovale and ventricular septal defect each appear in one patient.
- **Skeletal muscle:** No clinical myopathy has been reported, even though RPL3L is expressed in skeletal muscle.
- **Quality of life:** No formal QoL data. Surviving patients are transplant recipients and carry the lifelong burden of transplant care.

## 4. Genetics and molecular information

- **Gene:** *RPL3L* (ribosomal protein L3-like), chromosome 16p13.3. It is a muscle-restricted paralog of the core 60S protein RPL3. Das et al. describe it as "exclusively expressed in cardiac and skeletal muscles" (PMC9600237). "RPL3L is highly expressed in the heart tissue of humans and mice" (PMID:38254943).
- **Gene-disease validity:**
  - The 2026 ClinGen-based DCM reassessment classified *RPL3L* as **high evidence**: "classified as high evidence: BAG5, FLII, LMOD2, MYLK3, MYZAP, NRAP, PPA2, PPP1R13L, and RPL3L" (Jordan 2026, PMID:42708185).
  - A GenCC submission for RPL3L–DCM (AR) exists.
  - Per the repository rule, record a tier only if a `CGGV:` record for this disease is cached (`just clingen-list`).

**Reported variants** (transcript NM_005061.3 where stated)

| Variant | Partner | Ancestry / origin | Outcome | Ref |
|---|---|---|---|---|
| c.923A>T p.(Asp308Val) | c.1027C>T p.(Arg343Trp) | Germany, 2 sibs | Both died (days 15 and 21) | PMID:32514796 |
| c.922G>A p.(Asp308Asn) | c.566C>T p.(Thr189Met) | Colombia, consanguineous | Transplant at 6 mo; alive at 9 y | PMID:32514796 |
| c.80G>A p.(Gly27Asp) | c.481C>T p.(Arg161Trp) | Spain, 2 sibs | One transplanted (alive at 10 y); one died (day 30) | PMID:32514796 |
| c.80G>A p.(Gly27Asp) | c.1076_1080delCCGTG p.(Ala359Glyfs*4) | USA, 2 sibs | Both died (days 68 and 124) | PMID:35323613 |
| c.151G>A p.(Ala51Thr) | c.691G>T p.(Val231Phe) | USA | LVAD (Berlin Heart EXCOR), then transplant; well at 3 mo | PMID:36291431 |
| c.80G>A p.(Gly27Asp) | c.1074dupA p.(Ala359fs*6) | China | Severe DCM at 31 days | PMID:37308880 |
| c.346C>T p.(Arg116Cys) | c.605A>G p.(Glu202Gly) | China | Fulminant DCM | PMID:40820268 |
| c.322G>A p.(Glu108Lys) | c.501G>A p.(Gln167=) (paternal) | China | Brother died; proband recovered on drug therapy | PMID:42156347 |
| p.Glu108Lys | (VUS in a trio-WES cohort) | China | — | PMID:41270882 |

- **Recurrent alleles:** **p.Gly27Asp** appears in at least 4 families, and codon **Asp308** is hit twice (Asn and Val). Murphy et al. report that "Affected individuals typically carry one of two recurrent hotspot missense variants paired with a private allele" (PMID:41495453).
  - I could not get the full text to confirm which two variants they mean. Gly27Asp and Asp308Asn/Val are the likely candidates, but that is an **inference**. Check the full text before writing it into the entry.
- **Variant classes:** Mostly missense. Frameshifts at codon 359 (two independent alleles) and one synonymous/possible splice allele (c.501G>A).
  - The c.1074dupA frameshift "may result in the absence of protein production… suggesting it is a loss-of-function" (PMID:37308880).
- **Origin:** All germline. No somatic involvement.
- **Population frequency:** No CMD2D-specific gnomAD summary was found. Pathogenic alleles are rare. p.Ala75Val (an AF risk allele, not CMD2D) has 3.65% allele frequency in Iceland (PMID:30271950).
- **Functional consequence:** Likely a mix of loss of function (null and non-hotspot alleles) and toxic gain of function (hotspots). See Section 6.
- **Modifiers:** None established. A BXD mouse systems-genetics study proposes *Myl4* and *Sdha* as upstream regulators of *Rpl3l* expression (PMID:38254943, computational/mouse).
- **Epigenetic / chromosomal:** No disease-specific findings. A 2026 preprint reports that nuclear Rpl3l binds its own locus and influences chromatin insulation at the *Rpl3l–Cacna1h* locus (PMID:42395400). This is mouse/in vitro work, is not peer reviewed, and should not be used as KB evidence yet.

## 5. Environmental information

There are no environmental, lifestyle, or infectious causes. CMD2D is not an infectious disease.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline *RPL3L* variants**, missense in the RPL3 domain or truncating (PMID:32514796, 37308880), **lead to** abnormal or absent RPL3L protein in cardiomyocytes.

2. **Two branches follow** (proposed by Murphy et al., PMID:41495453; partly model-based):
   - **2a. Loss of function** (null and non-hotspot alleles) removes RPL3L-containing ribosomes. Non-hotspot variants "behave more like" knockouts.
   - **2b. Toxic gain of function** (recurrent hotspot alleles). These "induce nucleolar protein aggregation, disrupt rRNA processing and block compensation." The preprint adds that they "sequester 28S rRNA in the nucleus, disrupt ribosome biogenesis" and show increased binding to the RPL3/RPL3L chaperone GRWD1 (PMID:39803500).

3. **This results in impaired muscle-specific ribosome function and biogenesis.**
   - Homology modelling indicates that the variants "specifically alter the interaction of RPL3L with the RNA components of the 60S ribosomal subunit" (PMID:32514796, computational).

4. **Compensation normally limits the damage, and its failure may explain disease.**
   - In mice, losing Rpl3l up-regulates RPL3. "deletion of Rpl3l forces maintenance of RPL3 expression within the heart" (PMID:36733907). Knockout hearts are therefore mildly affected: no baseline phenotype, smaller hearts by 18 months.
   - Human disease is proposed to arise because hotspot alleles **block** this RPL3 compensation, combined with a second loss-of-function allele (PMID:41495453).
   - This is a **human–model mismatch**. A `HUMAN_MODEL_MISMATCH` discussion fits here.

5. **Altered translation elongation in cardiomyocytes** (Shiraishi 2023, PMID:37080962, mouse):
   - "RPL3L-containing ribosomes were less prone to collisions compared with RPL3-containing canonical ribosomes"
   - Effects "were most pronounced for transcripts related to cardiac muscle contraction and dilated cardiomyopathy"

6. **Altered ribosome–mitochondria coupling** (Milenkovic 2023, PMID:36882085, mouse):
   - "depletion of RPL3L leads to increased ribosome-mitochondria interactions in cardiomyocytes," which changes mitochondrial activity.
   - In human explant tissue, "sarcomere and mitochondrial abnormalities" were seen (PMID:40820268).
   - The link between this mitochondrial change and contractile failure is **inferred**, not shown.

7. **Reduced contractility followed by cardiomyocyte death and fibrosis.**
   - Rpl3l knockout mice show "impaired cardiac contractility" (PMID:37080962).
   - Human histology shows "cardiomyocyte death, collagen deposition" (PMID:40820268).

8. **Left ventricular dilatation and systolic failure lead to fulminant neonatal heart failure**, secondary atrioventricular-valve regurgitation, and death or transplantation (PMID:35323613, 36291431).

**Why onset is neonatal (hypothesis).** RPL3L replaces RPL3 in the heart after birth. Chaillou's review notes that during growth stimuli "the expression of Rpl3 is markedly increased, while that of Rpl3l is highly reduced" (PMID:30605395). This links disease onset to the perinatal ribosome paralog switch. It has not been demonstrated in humans.

**Process and cell-type terms to look up (GO / CL)**

| Concept | Term label to look up |
|---|---|
| Translation | cytoplasmic translation; translational elongation |
| Ribosome assembly | ribosomal large subunit biogenesis; rRNA processing |
| Contraction | cardiac muscle contraction |
| Cell death | cardiac muscle cell apoptotic process (or cell death) |
| Fibrosis | collagen fibril organization / extracellular matrix organization |
| Compartments | cytosolic large ribosomal subunit; nucleolus; mitochondrion |
| Cell types | cardiac muscle cell; cardiac fibroblast (fibrosis node) |

**Scale tags:** MOLECULAR (variant / ribosome) → CELLULAR (translation, mitochondria, death) → TISSUE (fibrosis, LV dilatation) → ORGANISM (heart failure).

**Omics:** No CMD2D patient transcriptomic, proteomic, or single-cell datasets were found. Mouse Ribo-seq and Nano-TRAP data come from PMID:36882085 and PMID:37080962. Any GEO accessions must be checked with `just verify-datasets` and triaged for relevance.

## 7. Anatomical structures affected

- **Primary:** heart, specifically the left ventricle and myocardium. UBERON labels to look up: heart; heart left ventricle; myocardium.
- **Secondary:** mitral and tricuspid valves (functional regurgitation); pulmonary vasculature (pulmonary hypertension, one case).
- **Cells:** cardiomyocytes, with fibroblast-driven fibrosis.
- **Subcellular:** ribosome (60S), nucleolus (hotspot aggregation), mitochondria, sarcomere.
- **Skeletal muscle:** expresses RPL3L, but no clinical involvement has been reported.
- **Lateralization:** not applicable (whole-organ disease).

## 8. Temporal development

- **Onset:** from day 1 to about 2.5 months of life (day 1, 6, 12, 48, 54, 75 in the Das table; 31 days in PMID:37308880; 2 months in PMID:42156347). Onset is acute to subacute.
- **Progression:** rapid. Most untreated infants died between day 15 and day 124.
- **Remission:** one exception has been reported. A 2-month-old with EF 31% improved, and cardiac function was normal after 6 months of drug therapy (PMID:42156347). Her genotype included a synonymous allele, which may be hypomorphic; that is an inference.
- **Critical window:** the neonatal period, during the RPL3→RPL3L switch. Early listing for mechanical support or transplantation is the main intervention point.
- **Stages for `progression:`:** neonatal onset → fulminant decompensation → death, or bridge-to-transplant / transplant survival.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (PMID:32514796, 35323613). Unaffected heterozygous parents are documented.
- **Penetrance:** appears complete for biallelic genotypes, but numbers are small. Expressivity varies, from death in the first weeks to survival on medication alone.
- **Anticipation and mosaicism:** none reported.
- **Founder effects:** none established. p.Gly27Asp recurs in unrelated Spanish, US, and Chinese families, which suggests a recurrent rather than founder allele (inference).
- **Prevalence:** unknown. Fewer than 20 cases are published. Use `measure_type: CASES_IN_LITERATURE` with a qualitative `ULTRA_RARE` or `RARE` tier.
- **Geography:** Germany, Spain, Colombia, USA, China, and possibly Saudi Arabia (PMID:32870709).
- **Sex ratio:** no bias (both sexes affected).

## 10. Diagnostics

- **Imaging:** echocardiography (LV dilatation, reduced EF/FS, AV-valve regurgitation). Cardiac MRI for fibrosis is rarely feasible in neonates.
- **ECG:** ST-T abnormalities, RBBB.
- **Laboratory:** heart-failure markers (NT-proBNP, troponin). These are not specific and are not reported systematically.
- **Pathology:** cardiomyocyte death, fibrosis, and sarcomere and mitochondrial ultrastructural abnormalities on explant tissue (PMID:40820268).
- **Genetic testing:**
  - Exome (singleton or trio) is the main route. Every reported case was found by WES.
  - *RPL3L* is on the Genomics England "Dilated and arrhythmogenic cardiomyopathy" panel. Confirm that commercial DCM panels include it.
  - In the Al-Hassnan cohort, "targeted genetic test had a yield of 82.7% compared with 33.6% for whole-exome sequencing/whole-genome sequencing" (PMID:32870709).
  - Trio WES in critically ill paediatric cardiomyopathy gave a 45% diagnostic rate (PMID:41270882).
- **Differential diagnosis:**
  - Myocarditis
  - Other recessive infantile DCMs: CMD2A *TNNI3*, CMD2B *GATAD1*, CMD2C *PPA2*
  - Mitochondrial cardiomyopathies (e.g. *TAZ* / Barth syndrome; *ACAD9*)
  - Endocardial fibroelastosis
  - Anomalous left coronary artery from the pulmonary artery (ALCAPA)
  - Metabolic cardiomyopathies (Pompe disease; carnitine deficiency)
  - Dominant de novo sarcomeric DCM
- **Screening:** cascade carrier testing in families, and prenatal or preimplantation testing once both familial variants are known. There is no newborn screening.
- **GeneReviews:** no CMD2D-specific chapter was found. Run `just check-genereviews` to confirm offline.

## 11. Outcome and prognosis

- **Mortality:** about 70% died in infancy in the 2020–2022 series (5/7 in the Das table, plus additional deaths such as the sibling in PMID:42156347).
- **Transplant survivors:** "At three months follow-up after heart transplantation, she has been doing well" (PMID:36291431). Survival to 9–10 years after transplant is documented (PMC9600237).
- **Medical recovery:** one case (PMID:42156347).
- **Complications:** pulmonary hypertension, need for a VAD, and death from pump failure.
- **Prognostic factors:** none validated. Genotype class (hotspot plus a null allele versus hypomorphic alleles) has been proposed as relevant; this is speculative.

## 12. Treatment

All treatments are supportive or replacement. There is no disease-specific therapy.

| Treatment | NCIT term to look up | Modality | Evidence |
|---|---|---|---|
| Heart-failure pharmacotherapy (diuretics, inotropes such as milrinone, ACE inhibitors, β-blockers) | Pharmacotherapy (NCIT:C15986 per CLAUDE.md) | SMALL_MOLECULE | "Drug therapy improved the patient's cardiac function" (PMID:42156347) |
| Ventricular assist device as bridge to transplant (Berlin Heart EXCOR) | Bind a clinical action (e.g. a surgical procedure term), not the device term | DEVICE / SURGERY | PMID:36291431 |
| Heart transplantation | Organ Transplantation (NCIT:C15289 per CLAUDE.md); look for a more specific heart-transplant term | SURGERY | PMID:36291431; PMC9600237 |
| Genetic counseling | Genetic Counseling (NCIT:C15240 per CLAUDE.md) | — | Recessive recurrence risk |

- **Experimental:** no clinical trials. Murphy et al. suggest that boosting RPL3 compensation, or allele-specific suppression of toxic hotspot alleles, could be therapeutic. That is a hypothesis only.
- **Related skeletal-muscle work (not cardiac):** AAV knockdown of Rpl3l in skeletal muscle increased specific force in dystrophic mice (PMID:34081545). This argues that **RPL3L knockdown is not a cardiac option** given CMD2D.
- **Pharmacogenomics:** none.

## 13. Prevention

- **Primary:** genetic counseling, carrier testing of relatives, and PGT-M or prenatal diagnosis for couples who are known carriers.
- **Secondary:** early echocardiography in at-risk newborn siblings.
- **Tertiary:** early referral for mechanical circulatory support and transplant evaluation.
- **Not applicable:** vaccination and environmental measures.

## 14. Other species

- **Naturally occurring disease:** none found in OMIA.
- **Conservation:** *RPL3L* is conserved in vertebrates.
- **Chicken:** RPL3L overexpression "could promote the proliferation and inhibit the differentiation of chicken myoblasts" (PMID:36407004). This concerns muscle growth, not disease.

## 15. Model organisms

| Model | Key finding | Recapitulation | Ref |
|---|---|---|---|
| Rpl3l⁻/⁻ mouse (Grimes) | No baseline or pressure-overload phenotype; RPL3 up-regulated; smaller hearts by 18 months | FAILS_TO_RECAPITULATE (no DCM) | PMID:36733907 |
| Rpl3l⁻/⁻ mouse (Milenkovic) | Viable; RPL3 replaces RPL3L; more ribosome–mitochondria contact | PARTIALLY (mechanism only) | PMID:36882085 |
| Rpl3l KO male mouse (Shiraishi) | "impaired cardiac contractility"; altered elongation dynamics | PARTIALLY | PMID:37080962 |
| Hotspot-variant cellular models (Murphy) | Nucleolar aggregation, rRNA processing defect, severe cellular toxicity | Mechanism | PMID:41495453 / 39803500 (cell type not confirmed) |
| BXD mouse panel | Rpl3l expression correlates with cardiac traits | Computational | PMID:38254943 |
| C2C12 myotubes | RPL3L impairs myotube growth and fusion | Skeletal muscle only | PMID:26684695 |

- **Modelling gap:** a knockout cannot reproduce the human disease because of RPL3 compensation. Hotspot knock-in mice or patient iPSC-derived cardiomyocytes are the obvious missing models. Neither was confirmed as published.
- **Suggested KB discussion:** `HUMAN_MODEL_MISMATCH` attached to the compensation and loss-of-function nodes.

---

## Limits and verification to do before curation

- **OMIM 619371** and **gene 617416** come from secondary sources. Confirm them.
- The **identities of the Murphy hotspot variants** are not confirmed (see Section 4).
- **Preprints:** PMID:39803500 and PMID:42395400 are preprints. Prefer the peer-reviewed PMID:41495453.
- **All quotes need fetching and verification** via `just fetch-reference` and `just count-verified-snippets` before use as snippets. In particular, some Das et al. quotes come from PMC full text, not the abstract.
- **Evidence-source grading:**
  - Mouse studies: `MODEL_ORGANISM`
  - Homology modelling in Ganapathi: `COMPUTATIONAL` (split it from the human genetic findings)
  - Case reports: `HUMAN_CLINICAL`

## Sources

- **Case reports and series**
  - Ganapathi 2020, *Hum Genet*, PMID:32514796 — https://link.springer.com/doi/10.1007/s00439-020-02188-6
  - Nannapaneni 2022, *J Cardiovasc Dev Dis*, PMID:35323613
  - Das 2022, *Children*, PMID:36291431 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9600237/
  - Yang 2023, *BMC Med Genomics*, PMID:37308880 — https://doaj.org/article/4415fabeab54407e9db0c554fef68740
  - Zhang 2025/26, *Am J Med Genet A*, PMID:40820268
  - Mai 2026, *J Int Med Res*, PMID:42156347
  - Xu 2026, *Clin Chim Acta*, PMID:41270882
  - Al-Hassnan 2020, *Circ Genom Precis Med*, PMID:32870709
- **Gene–disease validity**
  - Jordan 2026, *Circulation*, PMID:42708185
- **Mechanism**
  - Murphy 2026, *Nat Cardiovasc Res*, PMID:41495453; preprint PMID:39803500
  - Shiraishi 2023, *Nat Commun*, PMID:37080962
  - Grimes 2023, *Front Physiol*, PMID:36733907
  - Milenkovic 2023, *Nucleic Acids Res*, PMID:36882085 — https://repositori.upf.edu/items/e573c402-8434-4039-bd67-c1ea6752d007/full
  - Bajpai 2023, *Genes*, PMID:38254943
- **Atrial fibrillation (separate phenotype)**
  - Thorolfsdottir 2018, *Commun Biol*, PMID:30271950 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6123807/
  - Zöller 2023, PMID:38390584
  - Weng 2020, PMID:32822252
- **Skeletal muscle and paralog biology**
  - Chaillou 2016, PMID:26684695
  - Chaillou 2019, PMID:30605395
  - Kao 2021, PMID:34081545
  - Lin 2022, PMID:36407004
  - Nakamura 2026 (preprint), PMID:42395400
- **Databases**
  - MalaCards CMD2D — https://malacards.org/card/cardiomyopathy_dilated_2d
  - Genomics England PanelApp — https://panelapp.genomicsengland.co.uk/panels/652/gene/RPL3L
  - GenCC — https://search.thegencc.org/submissions/GENCC_000102-HGNC_10351-MONDO_0005021-HP_0000007-GENCC_100003
  - NORD/MONDO — https://rarediseases.org/mondo-disease/cardiomyopathy-dilated-2d/
  - Disease Ontology — https://disease-ontology.org/term/DOID:0081160

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 26 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9600237` *(abstract only)*: "exclusively expressed in cardiac and skeletal muscles"
  - Text part not found as substring: 'exclusively expressed in cardiac and skeletal muscles' (note: only abstract available for PMID:36291431, full text may contain this excerpt)
- `PMID:37308880` *(abstract only)*: "may result in the absence of protein production… suggesting it is a loss-of-function"
  - closest text in source: "The latter novel variant may result in the absence of protein production with a significant decrease in mRNA level, suggesting it is a loss-of-function mutation"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0081160` (3 mentions) - the report calls it "DOID"; DOID calls it **dilated cardiomyopathy 2D**