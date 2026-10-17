---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T14:29:07.901899'
end_time: '2026-10-08T14:33:09.606596'
duration_seconds: 241.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cardiomyopathy Dilated 2I
  mondo_id: MONDO:0957545
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
  web_search_requests: 3
  num_turns: 26
  total_cost_usd: 2.0843121000000004
  session_id: 5652a402-41cd-4fcc-8c56-6f68fff633d1
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
citation_count: 7
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 8
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:23022774
  relevance_assessed: 14
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 47
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0030042
    reported_labels:
    - DECREASED
    ontology_label: actin filament depolymerization
  - term_id: CL:0000057
    reported_labels:
    - patient cells
    ontology_label: fibroblast
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 2I
- **MONDO ID:** MONDO:0957545 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 2I** covering all of the
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

Gathering the CAP2 primary literature now; next I'll pull the exact abstract text so the report's quotes are verbatim.

Using the E-utilities endpoint instead, one paper at a time.

I've got the literature and verified the ontology terms against the local caches. Checking a few treatment terms, then I'll write the report.

# Cardiomyopathy, Dilated, 2I (CMD2I; CAP2-related dilated cardiomyopathy): research report

**MONDO:** MONDO:0957545 · **OMIM phenotype:** 620462 · **Gene:** *CAP2* (hgnc:20039; OMIM 618385; 6p22.3; NM_006366.3 / NP_006357.1; UniProt P40123)
**Prepared:** 2026-10-08

**How to read this report.** Quoted text was checked in one of two ways:
- Text quoted from PMID:30518548 was copied from the committed `references_cache/PMID_30518548.md`.
- Text quoted from every other paper came from PubMed E-utilities abstracts, read through a summarizing fetch tool. Those quotes need confirming with `just fetch-reference` before they go into a YAML snippet.

Every ontology CURIE listed in **Term suggestions** was checked against this repository's `cache/*/terms.csv`. Terms marked *(lead)* were not checked.

---

## Key caveats for curation

1. **Evidence base.** About five patients from four families have been described (three PanelApp-cited reports plus one 2026 case report), along with three independent mouse models. Most of the evidence about mechanism comes from mice.
2. **Symbol collision.** **"CAP2" is also a previous symbol for *SERPINB8* (hgnc:8952).** This is a ready-made route to a Named Entity Confusion error, and there are three more in the literature:
   - PubMed searches return "CAP2" studies about the PROTECT‑AF/PREVAIL continued-access registries.
   - They also return a "C‑CAP" ablation questionnaire.
   - Some papers name the gene "adenylyl cyclase-associated protein 2".
   The correct binding is **hgnc:20039**.
3. **Inheritance conflict.** PanelApp and OMIM give biallelic inheritance. A GenCC-derived record (seen on GeneBe) lists *CAP2*–"familial isolated DCM" as **AD, Supportive**. Every human case to date is homozygous, and every heterozygous parent reported so far is unaffected.
4. **No ClinGen classification.** The repository's pinned ClinGen gene-validity snapshot (`kb/genes/ingest/clingen_gene_validity.tsv`) has no *CAP2* row. Leave `gene_disease_validity` absent unless a GenCC source is cited.

---

## 1. Disease information

**Overview.** CMD2I is a severe, autosomal recessive dilated cardiomyopathy that begins in infancy or childhood. It is caused by biallelic loss-of-function variants in *CAP2*, which encodes a regulator of actin filament dynamics. Features:
- ventricular dilation and impaired systolic function, with early congestive heart failure;
- in some patients, supraventricular tachycardia or conduction disease;
- in one patient, nemaline rods in skeletal and cardiac muscle.

MalaCards and OMIM summarize it this way: "a severe, autosomal recessive form of dilated cardiomyopathy with onset in infancy or childhood… early, severe congestive heart failure and increased risk of premature death" ([MalaCards](https://malacards.org/card/cardiomyopathy_dilated_2i)).

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0957545 "cardiomyopathy, dilated, 2I" (verified in `cache/mondo/terms.csv`) |
| OMIM | 620462 (phenotype); 618385 (gene) |
| Orphanet | No CMD2I-specific code found. Orphanet's parent concept is "familial isolated dilated cardiomyopathy" (ORPHA:154; *(lead)* — confirm in the ORPHA cache) |
| ICD-10 | I42.0 (dilated cardiomyopathy) |
| MeSH | D002311 Cardiomyopathy, Dilated *(lead)* |

**Synonyms:** CMD2I; CAP2-related dilated cardiomyopathy; dilated cardiomyopathy 2I; autosomal recessive DCM due to CAP2 deficiency.

**Source type:** case reports and family studies (individual patients), plus panel curation (PanelApp, GenCC). There is no registry or EHR data.

## 2. Etiology

- **Cause:** biallelic loss-of-function variants in *CAP2* (splice, nonsense, frameshift).
- **Genetic risk:** consanguinity. Families reported so far are Bedouin (Israel), Pakistani, North American, and Chinese.
- **Protective factors:** none known.
- **Modifier or second-hit trigger:** in Pan et al. 2026 (PMID:42344352), a homozygous child developed fulminant cardiac dysfunction during a rhinovirus infection ("Respiratory pathogen panel was positive for rhinovirus"). The authors frame this as a "double-hit". This is a single case, so treat it as a hypothesis.
- **Sex as a modifier (mouse only):** in Field 2015 (PMID:26616005), "~70% died by 12 weeks of age" in male knockouts, while "females survived at close to the expected levels and lived normal life spans". DCM was "most noticeably in the males". No sex bias has been shown in humans, because there are too few cases.

## 3. Phenotypes

| Phenotype | HPO (verified) | Onset / frequency | Source |
|---|---|---|---|
| Dilated cardiomyopathy | HP:0001644 | Neonatal–childhood; all reported cases | PMID:30518548, 34862840, 33083013, 42344352 |
| Congestive heart failure | HP:0001635 | Early, severe | PMID:42344352 (fulminant at age 5); OMIM |
| Reduced LV ejection fraction | HP:0012664 | Common | inferred from DCM description |
| Supraventricular tachycardia | HP:0004755 | Bedouin family | PMID:30518548 (title) |
| Left ventricular noncompaction | HP:0011664 | 1 neonate | PMID:34862840: "severe dilated cardiomyopathy, biventricular dysfunction and left ventricular noncompaction" |
| Nemaline bodies (skeletal and cardiac) | HP:0003798 | 1 patient | PMID:34862840: "muscle biopsy on the 8th day of life… identified nemaline rods" |
| Hypotonia (mild) | HP:0001252 | 1 patient | PMID:34862840: "mild hypotonia" |
| Conduction disease / heart block | HP:0012722, HP:0001678 | Shown in mice; in humans only by implication | PMID:26616005, 26925136 |
| Sudden cardiac death | HP:0001645 | Risk (mouse: complete heart block) | PMID:26616005 |
| Congenital onset | HP:0003577 | Neonatal case | PMID:34862840: "within the first few hours of life" |

Other notes:
- PMID:34862840 also reports "atrophic and widened scarring" of the skin. There is no clear HPO match; it needs a lookup.
- **Quality of life:** no PROs or QoL data. The burden follows from paediatric heart failure, transplantation in infancy (1 of 5 patients), and arrhythmia.

## 4. Genetic and molecular information

**Reported variants** (all homozygous; all parents tested are heterozygous and unaffected):

| Variant | Type | Consequence | Family | PMID |
|---|---|---|---|---|
| Exon 7 donor splice-site change (exact HGVS not in abstract; get it from the full text or ClinVar) | canonical splice | "causes skipping of exons 6 and 7. The resulting protein is missing 64 amino acids in its N-CAP domain"; "CAP2 protein level was markedly reduced without notable compensation by the homolog CAP1" | 2 Bedouin cousins (consanguineous) | 30518548 |
| p.(Tyr316*) | nonsense | not characterized | Pakistani DCM/heart-failure patient | 33083013 (variant per PanelApp summary; the abstract only names "CAP2-dilated cardiomyopathy" as a validated diagnostic gene) |
| c.1288delT, p.C430fs (NM_006366) | frameshift | "appears to cause loss of both CAP2 protein and mRNA" (patient fibroblasts and iPSC-cardiomyocytes) | US neonate, non-consanguinity not stated | 34862840 |
| c.551G>A, p.W184* (NM_006366.3) | nonsense | "resides within the N-terminal helical folded domain"; "Abrogation of WH2 domain is predicted to completely abolish CAP2 function" | Chinese 5-year-old | 42344352 |

- **Functional class:** loss of function (amorphic or null). The variant origin is germline.
- **Classification:** ClinVar *CAP2* entries are mostly VUS. PanelApp rates the gene **Green** for both GEL "Paediatric or syndromic cardiomyopathy" (panel 749; biallelic; PMIDs 30518548, 33083013, 34862840) and PanelApp Australia DCM (panel 95).
- **Population frequency:** not reported in these sources. Query gnomAD for LoF observed/expected.
- **Chromosomal context:** *CAP2* lies at 6p22. Field 2015 notes that the knockout mice "resembled patients with 6p22 syndrome" (6p22 deletion). This is a possible contiguous-gene contribution, not CMD2I itself.
- **Epigenetics:** no data.

## 5. Environmental information

There is no established environmental cause. Pan 2026 reports viral infection (rhinovirus) as a possible precipitant of decompensation; NCBITaxon binding is a lead only. There is no lifestyle or toxin data.

## 6. Mechanism and pathophysiology

**Ordered causal chain**

1. **Biallelic *CAP2* LoF variant → loss of CAP2 protein in cardiomyocytes.** Shown in human cells: the splice variant reduces CAP2 protein, and c.1288delT causes "loss of both CAP2 protein and mRNA". CAP1 does not compensate (PMID:30518548).
2. **Loss of CAP2 → disordered actin turnover.** CAP2 normally "sequesters G-actin and efficiently fragments filaments" (PMID:22945801, Peche 2013). In cardiomyocytes it sits at thin-filament pointed ends and "depolymerizes and inhibits actin incorporation" (PMID:33742108, Colpan 2021). Patient fibroblasts show altered "kinetics of repolymerization of actin", with elevated β-actin mRNA (PMID:30518548).
3. **Disordered actin dynamics → impaired myofibrillogenesis and sarcomere maturation.** "CAP2 plays an essential role in cardiomyocyte maturation by modulating pre-sarcomeric actin assembly" (PMID:33742108). In skeletal muscle, the switch between α-actin isoforms is delayed (PMID:30962377). This step is shown in vitro and in mice.
4. **Branch A (structural): sarcomere disarray, fibrosis, nemaline rods → contractile failure.**
   - Mouse: "disarrayed sarcomeres with development of fibrosis" and reduced "cooperativity of calcium-regulated force development" (PMID:22945801).
   - Human explant: "nemaline rods and additionally disintegration of the myofibrillar structure" (PMID:34862840).
   - These lead to ventricular dilation and systolic dysfunction (DCM), then heart failure.
5. **Branch B (signalling): altered G/F-actin balance → MRTF/SRF dysregulation → fetal gene program.**
   - CAP2-KO hearts show "overactivation of fetal genes".
   - The SRF inhibitor CCG‑1423‑8u "reduced expression of the SRF targets Myl9 and Acta2, as well as… Nppa". Median survival of CKO mice rose from 98 to 116 days (PMID:30762586).
   - Direction caveat: in fibroblasts, CAP2 loss *reduced* basal nuclear MRTF‑A and SRF activity (PMID:33637797). Whether SRF moves up or down depends on cell type, so in cardiomyocytes it is inferred from the inhibitor rescue.
6. **Branch C (electrical): cardiomyocyte-autonomous conduction disease.**
   - In the gene-trap model, connexin43 is maldistributed and fibrosis increases, with "marked conduction delays at atrial and ventricular levels" and "spontaneous ventricular arrhythmias" (PMID:26925136).
   - Cardiomyocyte-specific KO mice show conduction disease leading to "sudden cardiac death from complete heart block", without DCM (PMID:26616005).
   - Human counterparts are SVT and the risk of sudden death.

Upstream/downstream: steps 1–3 are upstream. Branch A produces DCM and heart failure; branch C produces arrhythmia and SCD; branch B modifies progression and is a candidate drug target.

**Term suggestions** (all verified in the caches):
- **Biological processes (GO):** actin filament depolymerization GO:0030042 (DECREASED); actin cytoskeleton organization GO:0030036; actin filament organization GO:0007015; cardiac myofibril assembly GO:0055003; sarcomere organization GO:0045214; cardiac muscle contraction GO:0060048; positive regulation of transcription by RNA polymerase II GO:0045944 (for the SRF program; consider a more specific SRF term *(lead)*).
- **Cellular components (GO):** sarcomere GO:0030017; actin filament GO:0005884.
- **Molecular function (GO):** actin binding GO:0003779.
- **Cell types (CL):** cardiac muscle cell CL:0000746; fibroblast CL:0000057 (patient cells); cell of skeletal muscle CL:0000188.
- **Anatomy (UBERON):** heart UBERON:0000948; heart left ventricle UBERON:0002084; cardiac ventricle UBERON:0002082; His-Purkinje system UBERON:0004146; skeletal muscle tissue UBERON:0001134.
- **Omics:** RNA-seq of CAP2-KO mouse heart and cardiomyocytes (PMID:30762586); the GEO accession is not given in the abstract and needs `just discover-datasets`. There are no human single-cell or proteomic data.

## 7. Anatomical structures

- **Primary:** the myocardium, both ventricles (biventricular dysfunction in PMID:34862840).
- **Conduction system:** atrial, AV and ventricular conduction (mouse).
- **Secondary:** skeletal muscle (nemaline rods, hypotonia).
- **Mouse-only:** eye (microphthalmia) and body size. Aspit et al. state these are **not** recapitulated in humans: "but not the other effects on growth, viability, wound healing and eye development".
- **Subcellular:** thin-filament pointed ends and sarcomere; actin cytoskeleton.
- **Laterality:** bilateral or biventricular.

## 8. Temporal development

- **Onset:** neonatal (first hours of life) to childhood (age 5).
- **Course:** rapidly progressive in the neonate, who was transplanted at age 1. The 5-year-old presented with fulminant decompensation during an infection.
- **Natural history:** no studies exist.
- **Window for intervention (mouse):** SRF inhibition delayed onset in mice (PMID:30762586).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). This is supported by homozygosity in all probands and unaffected heterozygous parents: "Both parents were heterozygous for the same variant but have no history of heart or muscle disease" (PMID:34862840); "This is the first report of a recessive deleterious mutation in CAP2" (PMID:30518548).
- **Penetrance:** apparently complete in homozygotes, but n≈5.
- **Founder effect / consanguinity:** consanguineous Bedouin and Pakistani families. Cheema 2020 found a higher diagnostic yield in consanguineous families (60.1% vs 39.5%).
- **Prevalence:** unknown. Use measure_type CASES_IN_LITERATURE and prevalence_class ULTRA_RARE (roughly 5 published cases).
- **Sex ratio:** no human data. In mice, males are more severely affected.

## 10. Diagnostics

- **Imaging and functional tests:** echocardiography (LV dilation, reduced EF, noncompaction); cardiac MRI.
- **Electrophysiology:** ECG and Holter monitoring for SVT and conduction block.
- **Biomarker:** NT-proBNP/BNP (heart failure). Note that *Nppa* was reduced by SRF inhibition in mice.
- **Biopsy:** skeletal muscle and myocardium can show nemaline rods and myofibrillar disintegration.
- **Genetic testing:** exome sequencing found every reported case. *CAP2* is on the GEL paediatric cardiomyopathy panel and the PanelApp Australia DCM panel. Splice variants can be confirmed with RNA studies from fibroblasts (PMID:30518548). Cheema 2020 reports that "the genetic diagnosis had a direct impact on clinical management".
- **Differential diagnosis:**
  - other recessive paediatric DCM (CMD2A *TNNI3*, CMD2B *GATAD1*, CMD2C *PPCS*, and others);
  - Barth syndrome (*TAZ*);
  - nemaline myopathy with cardiomyopathy (*ACTA1*, *NEB*, *KLHL40*);
  - LVNC genes (*MYH7*, *TAZ*);
  - myocarditis, which matters because CMD2I can present during a viral infection.
- **Screening:** cascade testing of siblings, and carrier testing in consanguineous families.

## 11. Outcome and prognosis

- The disease is severe:
  - one neonate needed a heart transplant at age 1;
  - one child had fulminant heart failure at age 5;
  - OMIM describes an "increased risk of premature death".
- No survival statistics exist.
- Likely prognostic factors are neonatal onset, noncompaction, and conduction disease (mouse evidence for SCD).

## 12. Treatment

There is no disease-specific therapy. Standard paediatric heart-failure and DCM management applies:

| Intervention | NCIT (verified) | Agent / notes |
|---|---|---|
| Heart-failure pharmacotherapy | NCIT:C15986 Pharmacotherapy | ACE inhibitor NCIT:C247 (enalapril CHEBI:4784); beta-blocker NCIT:C29576 (carvedilol CHEBI:3441, metoprolol CHEBI:6904); spironolactone CHEBI:9241; furosemide CHEBI:47426; milrinone CHEBI:50693 (acute decompensation); sacubitril/valsartan NCIT:C222078 |
| Heart transplantation | NCIT:C15246 | Performed at age 1 (PMID:34862840) |
| Mechanical support | NCIT:C80452 Ventricular Assist Device Placement / NCIT:C172327 LVAD insertion | bridge to transplant (general practice; not reported in CMD2I) |
| ICD | NCIT:C80435 | given conduction disease and SCD risk (inferred from mouse) |
| Genetic counseling | NCIT:C15240 | AR recurrence risk of 25% |

- **Experimental:** MRTF/SRF inhibition (CCG‑1423‑8u), mouse only (PMID:30762586): "inhibiting signaling through SRF may benefit DCM by reducing cytoskeletal stress".
- **Gene therapy:** none.
- **Clinical trials:** no CAP2-specific trials were found.

## 13. Prevention

- **Primary:** genetic counseling, carrier testing, and PGD or prenatal diagnosis in families with a known variant.
- **Secondary:** cascade echocardiography and ECG in siblings.
- **Tertiary:** arrhythmia surveillance, and early treatment of intercurrent infections (suggested by Pan 2026).

## 14. Other species

- There are no naturally occurring cases in OMIA.
- In Hu sheep, *CAP2* polymorphisms are associated with body height, and the gene is expressed strongly in heart (PMID:34481004). This is not a disease.
- **Orthologs:** mouse *Cap2*; zebrafish *cap2*. Zebrafish knockdown causes "short bodies and pericardial edema" (PMID:23022774, paraphrased).

## 15. Model organisms

| Model | Phenotype | Fidelity | PMID |
|---|---|---|---|
| *Cap2* gene-trap (gt/gt) mouse, Noegel lab | DCM, sarcomere disarray, fibrosis, reduced Ca²⁺-force cooperativity, reduced survival; conduction delay, ventricular arrhythmia, Cx43 maldistribution | Recapitulates DCM and conduction disease | 22945801 (erratum 28852764); 26925136 |
| *Cap2* whole-body KO, Field lab | Male-biased lethality, small size, microphthalmia, CCD, DCM after 6 months | Partial: extracardiac features absent in humans | 26616005 |
| Cardiomyocyte-specific *Cap2* CKO (Cre) | CCD leading to SCD from complete heart block; no DCM | Isolates the electrical branch | 26616005, 30762586 |
| *Cap2* mutant mouse, skeletal muscle (Rust lab) | delayed α-actin isoform switch, ring fibers, motor deficits | Models skeletal muscle involvement | 30962377 |
| Patient fibroblasts and iPSC-cardiomyocytes | loss of protein/mRNA; altered actin repolymerization | Human in vitro | 30518548, 34862840 |
| Neonatal rat and mouse cardiomyocytes (CAP2 knockdown/KO) | impaired pre-sarcomeric actin assembly and maturation | In vitro | 33742108 |
| Zebrafish morphants | pericardial edema | Low | 23022774 |

**Main gaps between the models and human disease:** sex bias, microphthalmia and growth failure occur in mice but not in humans. The relative contributions of systemic versus cardiomyocyte-autonomous mechanisms to DCM are unresolved: the CKO mouse has no DCM, but the CKO used in PMID:30762586 had shortened survival. This is a candidate `HUMAN_MODEL_MISMATCH` discussion.

---

## Key references

| PMID | Citation |
|---|---|
| 30518548 | Aspit L et al. *J Med Genet* 2019. CAP2 mutation leads to impaired actin dynamics and associates with SVT and DCM. **Cached** |
| 34862840 | Gurunathan S et al. *Am J Med Genet A* 2022. Homozygous CAP2 variant in a neonate with rapidly progressive cardiomyopathy and nemaline rods |
| 33083013 | Cheema H et al. *NPJ Genom Med* 2020. Genomic testing in 1019 individuals from 349 Pakistani families |
| 42344352 | Pan Z et al. *Front Cardiovasc Med* 2026. "Double-hit" fulminant cardiac dysfunction with a homozygous CAP2 variant |
| 26616005 | Field J et al. *Sci Rep* 2015. CAP2 in cardiac conduction, sudden cardiac death and eye development |
| 22945801 | Peche VS et al. *Cell Mol Life Sci* 2013. Ablation of CAP2 leads to cardiomyopathy (erratum PMID:28852764) |
| 26925136 | Stöckigt F et al. *Arch Med Sci* 2016. CAP2 deficiency promotes arrhythmias with Cx43 maldistribution and fibrosis |
| 30762586 | Xiong Y et al. *JCI Insight* 2019. Targeting MRTF/SRF in CAP2-dependent DCM delays disease onset |
| 33742108 | Colpan M et al. *Commun Biol* 2021. CAP2 regulates actin pointed-end dynamics and myofibrillogenesis |
| 30962377 | Kepser LJ et al. *PNAS* 2019. CAP2 deficiency delays myofibril actin differentiation in skeletal muscle |
| 33637797 | Kepser LJ et al. *Sci Rep* 2021. CAP2 controls MRTF-A localization and SRF activity in MEFs |
| 35150966 | Rust MB, Marcello E. *Eur J Cell Biol* 2022. Review of CAP disease associations |

**Next steps before writing YAML:**
1. Run `just fetch-reference PMID:<id>` for each paper above except 30518548, then run `just count-verified-snippets`.
2. Get the HGVS notation for the Aspit splice variant from the full text or ClinVar.
3. Run `just check-genereviews` to confirm that no GeneReviews chapter exists.

Sources:
- [MalaCards: CMD2I](https://malacards.org/card/cardiomyopathy_dilated_2i)
- [Genomics England PanelApp: CAP2](https://panelapp.genomicsengland.co.uk/panels/749/gene/CAP2/)
- [PanelApp Australia DCM: CAP2](https://panelapp-aus.org/panels/95/gene/CAP2)
- [GeneBe: CAP2](https://genebe.net/gene/hg38/CAP2)
- [PomBase: MONDO:0957545](https://www.pombase.org/term/MONDO:0957545)
- [Field et al. 2015 (PMC4663486)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4663486/)
- [PubMed E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23022774` *(abstract only)*: "short bodies and pericardial edema"
  - closest text in source: "Knockdown using two different morpholinos against CAP2 resulted in a short-body morphant zebrafish phenotype with pericardial edema"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0030042` (1 mention) - the report calls it "DECREASED"; GO calls it **actin filament depolymerization**
- `CL:0000057` (1 mention) - the report calls it "patient cells"; CL calls it **fibroblast**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012664` (1 mention) - the report calls it "Reduced LV ejection fraction"; HP calls it **Reduced left ventricular ejection fraction**, and lists "Reduced ejection fraction" among its other names
- `HP:0011664` (1 mention) - the report calls it "Left ventricular noncompaction"; HP calls it **Left ventricular noncompaction cardiomyopathy**
- `HP:0003798` (1 mention) - the report calls it "Nemaline bodies (skeletal and cardiac)"; HP calls it **Nemaline bodies**
- `HP:0001252` (1 mention) - the report calls it "Hypotonia (mild)"; HP calls it **Hypotonia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.