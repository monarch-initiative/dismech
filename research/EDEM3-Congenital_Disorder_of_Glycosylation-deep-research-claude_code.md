---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-09-28T12:07:03.358561'
end_time: '2026-09-28T12:10:56.550062'
duration_seconds: 233.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: EDEM3-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0030423
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 20
  total_cost_usd: 2.4040778000000005
  session_id: 0fc32209-332f-4b98-be40-d5a29502bf72
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
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
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 29
  quotes_valid: 29
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 5
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: DOID:0051050
    reported_labels:
    - DOID
    ontology_label: congenital disorder of glycosylation type IIv
  - term_id: CL:0000540
    reported_labels:
    - inferred target tissue only
    ontology_label: neuron
  - term_id: NCIT:C15747
    reported_labels:
    - a gastrostomy procedure term needs lookup
    ontology_label: Supportive Care
  - term_id: NCIT:C15986
    reported_labels:
    - agent unspecified in the source
    ontology_label: Pharmacotherapy
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EDEM3-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0030423 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **EDEM3-Congenital Disorder of Glycosylation** covering all of the
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

Status: I've read the six cached EDEM3 references and am now checking identifiers (MONDO/Orphanet) and a few supporting papers before writing the report.

# EDEM3-Congenital Disorder of Glycosylation (EDEM3-CDG; CDG2V): Research Report

**Prepared:** 2026-09-28 · **Target:** MONDO:0030423 · **Category:** Mendelian (autosomal recessive)

**How to read this report.** Six full-text or abstract records were read from the local `references_cache/`: PMID:34143952, 16431915, 29784879, 34698634, 35500441 and 39838427. Text in quotation marks from those PMIDs is copied exactly and can be used as a snippet. Everything else comes from web or PubMed-summary retrieval and is paraphrased; it has to be fetched with `just fetch-reference` before it can back a snippet. I list ontology identifiers as leads only. The repo requires every CURIE to be looked up (runoak or the term caches) before it is written into YAML, and I have marked the ones I could not source in this session.

**Main limitation.** The whole human clinical literature is **one paper**: Polla et al., 2021, *Am J Hum Genet* (PMID:34143952), describing 12 patients from 7 families. A PubMed search for "EDEM3" (54 hits as of today) turned up no later case series or case report. Every phenotype frequency below is therefore an n=12 figure.

---

## 1. Disease Information

**Overview.** EDEM3-CDG is an autosomal recessive congenital disorder of glycosylation. It is caused by biallelic loss-of-function variants in *EDEM3*, which encodes an ER-lumenal class I (GH47) α1,2-mannosidase that trims mannose in glycoprotein ER-associated degradation (gpERAD). The clinical picture is non-specific developmental delay or intellectual disability with speech delay, variable hypotonia and mild facial dysmorphism.

> "The affected individuals present with an inherited congenital disorder of glycosylation (CDG) consisting of neurodevelopmental delay and variable facial dysmorphisms." (PMID:34143952)

> "We propose to call this deficiency EDEM3-CDG." (PMID:34143952)

**Identifiers** (from the MONDO record via OLS, retrieved today):

| Resource | ID |
|---|---|
| MONDO | MONDO:0030423 "congenital disorder of glycosylation, type 2v" (cached in `cache/mondo/terms.csv`) |
| OMIM (phenotype) | 619493 |
| OMIM (gene) | 610214 (EDEM3) |
| Orphanet | ORPHA:695783 |
| DOID | DOID:0051050 |
| GARD | 0025557 |
| MedGen / UMLS | 1794181 / C5561971 |
| ICD-10 / ICD-11 | No disease-specific code. It would fall under the CDG group code (ICD-10 E77.8 / ICD-11 5C51.1 group level), which I have not verified. |
| MeSH | No specific heading; indexed under "Congenital Disorders of Glycosylation". |

**Synonyms:** EDEM3-CDG; CDG2V; CDG-IIv; congenital disorder of glycosylation type IIv.

**Nature of the data:** aggregated case-level data from one exome/GeneMatcher-assembled cohort. There is no registry-level or EHR data. The FCDGC natural-history study (NCT04199000) enrolls CDG patients generally and may include EDEM3-CDG.

---

## 2. Etiology

- **Cause:** biallelic germline *EDEM3* variants, mostly protein-truncating.
  > "we have identified seven independent families with 11 individuals with bi-allelic protein-truncating variants and one individual with a compound heterozygous missense variant in EDEM3." (PMID:34143952)
- **Genetic risk factors:**
  - Consanguinity and founder effect in the Portuguese Romani population, where c.1859del was found in 1/96 controls.
    > "Because families 1 and 2 are of Portuguese Romani origin, this suggests a possible founder effect." (PMID:34143952)
  - Uniparental isodisomy (family 4).
    > "In family 4, a bi-allelic nonsense variant, c.940A>T (p.Arg314∗), was found, resulting from maternal uniparental isodisomy of chromosome 1." (PMID:34143952)
- **Environmental risk, protective or GxE factors:** none reported. Not applicable to a monogenic recessive enzyme deficiency.
- **Related common-variant biology (not disease risk):** the low-frequency missense variant rs78444298 (p.Pro746Ser, protease-associated domain, MAF ~1.5%) is associated with about 5% lower plasma triglycerides.
  > "A low-frequency EDEM3 missense variant in the protease-associated domain (rs78444298, p.Pro746Ser, minor allele frequency ∼1.5%) was associated with an approximately 5% decrease in triglyceride levels." (PMID:34143952)
  - The mechanism (EDEM3 loss → higher LRP1 → faster VLDL uptake) is from Xu et al., *iScience* 2020, PMID:32213464, which needs fetching.
  - EDEM3-CDG patients nevertheless had normal fasting triglycerides:
    > "In our subjects for whom fasting triglyceride levels are available (Table S1), all triglyceride measurements were within the normal range." (PMID:34143952)

---

## 3. Phenotypes

Frequencies are from PMID:34143952 (n=12). Onset is infantile or early childhood. Severity is mild to moderate and course appears static. Quality-of-life data do not exist.

| Phenotype | Freq. | Suggested HPO (verify before use) |
|---|---|---|
| Developmental delay and/or intellectual disability | 12/12 | Global developmental delay HP:0001263; Intellectual disability HP:0001249 |
| Speech delay | 12/12 | Delayed speech and language development HP:0000750 |
| Hypotonia | 6/12 | Hypotonia HP:0001252 |
| Hypoplastic alae nasi | 9/12 | Hypoplasia of the ala nasi (look up the CURIE) |
| Thin upper lip | 9/12 | Thin upper lip vermilion HP:0000219 |
| Increased nasal height | 8/12 | Long nose / "increased nasal height" (look up) |
| Narrow palpebral fissures | 6/12 | Narrow palpebral fissure HP:0045025 |
| Epicanthal folds | 6/12 | Epicanthus HP:0000286 |
| Bulbous nasal tip | 6/12 | Bulbous nose HP:0000414 |
| Short philtrum | 6/12 | Short philtrum HP:0000322 |
| Retrognathia | 6/12 | Retrognathia HP:0000278 |
| Gastroesophageal reflux | 3/12 | Gastroesophageal reflux HP:0002020 |
| Early feeding difficulty requiring NG tube (1 of these 2 needed PEG) | 2/12 | Feeding difficulties HP:0011968 |
| Normal brain MRI (families 2, 3, 5) | 3 families tested | Negative finding; do not assert a brain anomaly |
| Laboratory: abnormal plasma N-glycan profile (↑M9:M3, ↓M3:M4/M5:M9/M6:M9/M7:M9) | 12/12 | Abnormal protein N-linked glycosylation (look up); keep as biochemical biomarker |
| Laboratory: normal transferrin isoelectric focusing | 3/3 tested (family 3) | Negative finding |

Supporting quotes (PMID:34143952):

> "All affected individuals presented with developmental delay and/or intellectual disability (ID) and speech delay (Table S1). Hypotonia was present in six out of 12 persons."

> "Additionally, gastroesophageal reflux was observed in three persons, and two individuals had early feeding difficulties requiring a nasogastric tube; of these, one individual needed a percutaneous endoscopic gastrostomy placement."

> "Brain magnetic resonance imaging (MRI) of affected individuals from families 2, 3, and 5 did not detect structural abnormalities or myelination defects."

**Additional features listed by CDG Hub** (secondary source summarizing Table S1; each needs a primary-source check against the Polla supplement before curation): anosmia, apnea, delayed bone age, muscle atrophy, Poland sequence (one case), astigmatism, strabismus, failure to thrive, hyperactivity, anxiety and attention deficit.

---

## 4. Genetic / Molecular Information

**Gene:** *EDEM3*, located at 1q25.3.
- HGNC:16787. Write it as `hgnc:16787` in YAML, and confirm with `just validate-terms`.
- NCBI Gene 80267 and UniProt Q9BZQ6. Both are from memory; verify them.
- OMIM 610214.
- Transcript NM_025191.3.

**Protein:** a 931-aa soluble ER-lumenal protein (mouse). It has an N-terminal GH47 α-mannosidase homology domain and a C-terminal protease-associated (PA) domain.
> "EDEM3 consists of 931 amino acids and has all the signature motifs of Class I alpha-mannosidases (glycosyl hydrolase family 47) in its N-terminal domain and a protease-associated motif in its C-terminal region." (PMID:16431915)

**Reported pathogenic variants** (PMID:34143952; NM_025191.3). All were germline, with carrier parents. None has an ACMG classification in the paper; check ClinVar.

| Family | Genotype | Type |
|---|---|---|
| 1, 2 (Portuguese Romani) | c.1859del p.(Ile620Thrfs*7), homozygous | frameshift, NMD |
| 3 | c.2001dup p.(Ala668Serfs*9) / c.1369del p.(Arg457Glufs*28) | frameshift |
| 4 | c.940A>T p.(Arg314*), homozygous by maternal UPD1 | nonsense |
| 5 | c.853+1G>T / c.1407T>A p.(Tyr469*) | splice donor / nonsense |
| 6 | c.1382_1385del p.(Phe461Serfs*23), homozygous | frameshift |
| 7 | c.182A>G p.(Asp61Gly) / c.1366G>A p.(Asp456Asn) | missense, both in the GH47 domain |

- **Allele frequency:** p.Asp61Gly is in 6/218,508 gnomAD alleles (rs777353823). p.Asp456Asn is absent from gnomAD.
- **Functional consequence:** loss of function via nonsense-mediated decay and absent protein.
  > "These demonstrated the absence of EDEM3 in individual IV-4 (family 1) and individual II-1 (family 3) consistent with loss of function of EDEM3 (Figure 3C)." (PMID:34143952)
- **Modifier genes:** none established.
  - *EDEM1* is a candidate functional backup, but it is not upregulated in patient cells: "EDEM1 levels were at 97% of normal levels (p = 0.9373) in fibroblast cell lines from affected individuals" (PMID:34143952).
  - *TXNL4/ERp46* (ERp46 = TXNDC5) is required for EDEM3 activity (PMID:29784879). It is a plausible modifier, but this is unproven.
- **Epigenetic and chromosomal findings:** none, apart from the UPD1 mechanism above.

---

## 5. Environmental Information

Not applicable. No toxins, lifestyle factors or infectious triggers are described. Tunicamycin is used only as an experimental ER-stress inducer. This section should be left empty rather than filled.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic truncating or missense *EDEM3* variants** lead to NMD of mRNA (about 17–18% residual) and absent EDEM3 protein. *[Demonstrated: patient LCLs and fibroblasts, PMID:34143952]*
2. **Loss of ER α1,2-mannosidase activity** (GH47; needs a Cys82–Cys441 disulfide and is activated by ERp46) leads to failure to trim Man8GlcNAc2 isomer B to Man7/6/5. *[Demonstrated: patient fibroblasts, patient plasma and Edem3-KO mouse plasma/brain (PMID:34143952); biochemistry (PMID:34698634, 29784879, 16431915)]*
   - **Branch 2a, global N-glycome change** (secreted and cellular glycoproteins): lower M3–M7, relatively preserved or raised M8/M9, ↑M9:M3 and ↓M3:M4. This is the diagnostic biomarker. *[Demonstrated]*
   - **Branch 2b, M5 → M4 trimming deficit with Glc1Man5 accumulation.** The authors speculate that lipid-linked oligosaccharide (LLO) synthesis is impaired. *[Observation demonstrated; LLO mechanism speculative]*
3. **Lack of the α1,6-mannose-exposing glycan degron** (M7A/M6/M5) leads to reduced recognition by OS-9/XTP3-B and slower gpERAD of misfolded glycoproteins. *[Inferred for patients. Demonstrated in EDEM1/3 double-KO HCT116 cells (PMID:34698634); patient-cell ERAD-substrate kinetics not measured]*
4. **Altered ER proteostasis and unfolded protein response (UPR)**: patient LCLs show blunted induction of PERK (EIF2AK3) by tunicamycin. *[Demonstrated in vitro, n=3 vs n=3; direction is ambiguous — "impaired UPR" or "increased capacity to eliminate misfolded proteins"]*
   - **Branch 4b (contrasting model):** EDEM3-KO HepaRG hepatic cells show *increased* BiP/PERK/p-eIF2α, rising apoptosis and loss of viability with passage (PMID:39838427, a cancer cell line). The UPR direction therefore appears to depend on cell context.
5. **Neurodevelopmental dysfunction** leads to DD/ID, speech delay and hypotonia, and dysmorphism arises through an undetermined craniofacial developmental route. *[Not demonstrated. No neural cell or organoid model of EDEM3-CDG exists; MRI is normal]*
   > "Further functional studies are necessary to determine the precise pathophysiological mechanism of EDEM3-CDG." (PMID:34143952)

### Key supporting quotes

- Enzymatic step:
  > "Experiments in human fibroblast cell lines, human plasma, and mouse plasma and brain tissue demonstrated decreased trimming of Man8GlcNAc2 isomer B to Man7GlcNAc2, consistent with loss of EDEM3 enzymatic activity." (PMID:34143952)
- M5 trimming:
  > "In human cells, Man5GlcNAc2 to Man4GlcNAc2 conversion is also diminished with an increase of Glc1Man5GlcNAc2." (PMID:34143952)
- UPR:
  > "Furthermore, analysis of the unfolded protein response showed a reduced increase in EIF2AK3 (PERK) expression upon stimulation with tunicamycin as compared to controls, suggesting an impaired unfolded protein response." (PMID:34143952)
- EDEM3 as the main second-step enzyme:
  > "Thus, EDEM3 is a major α1,2-mannosidase for the second step from M8B." (PMID:34698634, IN_VITRO)
- Disulfide requirement:
  > "Results showed that the mutations C160A and C529A of EDEM1 as well as C82A and C441A of EDEM3 indeed inactivated EDEM1 and EDEM3, respectively, in gpERAD" (PMID:34698634)
- ERp46 partner:
  > "the mannose-trimming activity of EDEM3 toward the model misfolded substrate, the glycoprotein T-cell receptor α locus (TCRα), was reconstituted only when ERp46 had established a covalent interaction with EDEM3." (PMID:29784879)
- ERAD enhancement:
  > "EDEM3 accelerates glycoprotein ERAD in transfected HEK293 cells, as shown by increased degradation of misfolded alpha1-antitrypsin variant (null (Hong Kong)) and of TCRalpha." (PMID:16431915)
- Trimming beyond misfolded proteins:
  > "Overexpression of EDEM3 also greatly stimulates mannose trimming not only from misfolded alpha1-AT null (Hong Kong) but also from total glycoproteins" (PMID:16431915)
- M9 substrate (in vitro):
  > "EDEM3 can convert an asparagine-linked M9 glycan to M8 and M7 glycans in contrast to glycine-linked M9 glycan, and the activity is enhanced in the presence of ERp46" (PMID:35500441)
- Loss in hepatic cells:
  > "Conversely, cell depletion of EDEM3 resulted in significant ER stress inducing pro-apoptotic mechanisms and cell death." (PMID:39838427, IN_VITRO, HCC context)

### Ontology suggestions (all require lookup)

- **GO biological process:**
  - ERAD pathway GO:0036503
  - protein alpha-1,2-demannosylation GO:0036508
  - protein N-linked glycosylation GO:0006487
  - response to endoplasmic reticulum stress GO:0034976
  - PERK-mediated unfolded protein response GO:0036499
  - ER mannose trimming involved in glycoprotein ERAD pathway (check whether a specific term exists)
- **GO molecular function:** mannosyl-oligosaccharide 1,2-alpha-mannosidase activity GO:0004571.
- **GO cellular component:** endoplasmic reticulum lumen GO:0005788.
- **CL:** fibroblast CL:0000057 (skin fibroblasts studied); B cell–derived lymphoblastoid lines (bind to B cell, CL:0000236, with a note); neuron CL:0000540 (inferred target tissue only).
- **Biological scale:** step 1 MOLECULAR; step 2 MOLECULAR; step 3 CELLULAR; step 4 CELLULAR; step 5 ORGANISM.
- **Candidate modules:** check `just list-modules` for an ERAD/UPR or glycosylation module before creating any `conforms_to`.

---

## 7. Anatomical Structures Affected

- **Organ/system:** central nervous system (functional, with no structural MRI lesion), craniofacial region and GI tract (reflux, feeding).
- **Subcellular:** ER lumen, where EDEM3 localizes with PDI:
  > "showing the expected EDEM3 localization within the ER compartment, as revealed by significant overlapping with the ER marker, PDI" (PMID:39838427)
- **UBERON suggestions (verify):** brain UBERON:0000955, face UBERON:0001456, esophagus UBERON:0001043.
- **Lateralization:** not applicable; the facial features are symmetric. The single Poland sequence case is unilateral by definition and unverified.

---

## 8. Temporal Development

- **Onset:** congenital or infantile. Feeding difficulty appears in infancy, and delays are recognized in early childhood.
- **Course:** apparently static neurodevelopmental disorder. No regression is reported. The oldest reported patient was 33 years old (CDG Hub).
- **No staging, no remission, no longitudinal natural-history data.** The critical period is early childhood, for developmental therapy.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007), with carrier parents confirmed by Sanger sequencing:
  > "The unaffected parents were all heterozygous carriers." (PMID:34143952)
- **Penetrance and expressivity:** apparently complete for DD/ID. Dysmorphism and hypotonia vary (about 50%).
- **Founder effect:** c.1859del in the Portuguese Romani population (1/96 control carrier; shared 3.16 Mb homozygous haplotype).
- **Prevalence:** unknown. There are 12 reported cases. Use `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
- **Sex ratio, anticipation, mosaicism:** not reported, not applicable and not reported, respectively.
- **Carrier frequency:** not estimated. gnomAD pLoF counts could be queried.

---

## 10. Diagnostics

- **Genetic:** exome or genome sequencing is how every case was found (exome + GeneMatcher). *EDEM3* is included on some CDG panels. Chromosomal microarray and SNP array can reveal UPD1 or runs of homozygosity.
- **Biochemical (key):** semiquantitative plasma N-glycan profiling (MALDI/LC-MS).
  > "M9:M3 was increased in all 12 affected individuals." (PMID:34143952)

  > "M6:M9 ratio provided the highest discrimination between tested obligate heterozygotes (parents, n = 4) and affected individuals (n = 12; Table S3)." (PMID:34143952)

  > "Therefore, the combination of high M9:M3 and low M3:M4 ratios might also provide diagnostic clues for EDEM3-CDG when M5:M9 and M6:M9 ratios are normal." (PMID:34143952)
  - Reference ratios reported: M3:M4 normal 0.39–0.56; M9:M3 normal 1.16–2.92.
- **The standard CDG screen misses it:**
  > "Of note, human transferrin was normally glycosylated in the common clinical screening test for CDG in the three affected individuals from family 3." (PMID:34143952)
- **Variant validation:**
  > "The aberrant plasma N-glycan profile provides a quick, clinically available test for validating variants of uncertain significance that may be identified by molecular genetic testing." (PMID:34143952)
- **Research assays:** fibroblast [2-³H]mannose pulse-chase glycan analysis; EDEM3 immunoblot; qPCR.
- **Imaging:** brain MRI is normal, which usefully separates it from many CDGs with cerebellar hypoplasia (e.g., PMM2-CDG).
- **Differential diagnosis:**
  - Other type II/ERAD-related CDGs with normal transferrin: MAN1B1-CDG (which has a transferrin abnormality), MOGS-CDG, and PMM2-/ALG-CDG (distinguished by ↑M3/M4).
  - Non-specific ID syndromes.
- **Screening:** no newborn screening. Carrier and prenatal testing are possible once familial variants are known. Targeted carrier testing is a consideration in the Portuguese Romani community.

---

## 11. Outcome / Prognosis

- Survival, mortality and QoL data: **none**.
- Survival into adulthood is documented (age 33).
- Morbidity comes from ID, speech impairment and feeding problems; one patient needed a gastrostomy.
- No prognostic biomarkers.

---

## 12. Treatment

There is no disease-specific therapy; care is supportive and multidisciplinary (CDG Hub, FCDGC). NCIT candidates below come from the CLAUDE.md list; confirm each by lookup.

| Intervention | NCIT (verify) | Modality |
|---|---|---|
| Physical therapy | NCIT:C15302 | BEHAVIORAL |
| Speech-language therapy | NCIT:C159273 | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Feeding support: NG tube / gastrostomy (1 case PEG) | Supportive Care NCIT:C15747 (a gastrostomy procedure term needs lookup) | SURGERY / OTHER |
| Reflux management | Pharmacotherapy NCIT:C15986 (agent unspecified in the source) | — |
| Genetic counseling | NCIT:C15240 | — |

- **Experimental:** NCT04199000, the FCDGC natural-history study. It is an observational CDG study (dietary interventions are explored generally) and not EDEM3-specific. Fetch it before citing.
- No gene, RNA or targeted therapy exists.
- **Caution on pharmacology:** kifunensine inhibits ER α1,2-mannosidases, so it would phenocopy the defect rather than treat it. EDEM3 *inhibition* has been proposed for hypertriglyceridemia (PMID:32213464) and cancer (PMID:39838427). That therapeutic vector runs opposite to this disease.

---

## 13. Prevention

- Primary prevention is limited to genetic counseling, cascade carrier testing, and prenatal or preimplantation diagnosis for known familial variants.
- Tertiary prevention covers early developmental intervention and feeding and reflux management.
- No vaccination, public-health or environmental measures apply.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease has been reported (OMIA not checked in this session).
- Orthologs: mouse *Edem3*; yeast *HTM1/MNL1*, whose activity likewise needs a PDI partner (Pdi1p), paralleling ERp46 (PMID:29784879); *C. elegans* edem-3.
- The mechanism is conserved across eukaryotes:
  > "This mechanism is conserved among eukaryotes, and mannose trimming from N-glycans is crucial for the degradation of glycoproteins by ER-associated degradation (ERAD)" (PMID:29784879)
- Not zoonotic.

---

## 15. Model Organisms and Experimental Models

| Model | Findings | Fidelity / limitations |
|---|---|---|
| ***Edem3* knockout mouse** (PMID:34143952, MODEL_ORGANISM) | Plasma and brain show ↑M8/M9 and ↓M5:M9 and M6:M9 ratios. There is no obvious phenotype; brain and body weight are reduced and genotype ratios are skewed. | PARTIALLY_RECAPITULATES the glycan node. It does not model the neurodevelopmental phenotype. Species difference: the mouse does not reproduce the ↓M3:M4 ratio, and its most significant change is ↑M6:M7 rather than human ↓M7:M8. This is a `HUMAN_MODEL_MISMATCH` discussion candidate. |
| Hepatic *Edem3* knockdown mouse (PMID:32213464; fetch) | Plasma TG ↓, hepatic LRP1 ↑ | Lipid biology; not relevant to CDG phenotypes |
| **Patient fibroblasts and EBV-LCLs** (PMID:34143952, IN_VITRO) | NMD, absent protein, glycan defect, blunted PERK induction. Complementation with WT EDEM3 was performed (Fig. 3C–D). | Strongest disease-relevant cellular model; not neural |
| EDEM1/3 double-KO HCT116 (PMID:34698634) | M8B accumulation, delayed degradation of ATF6α and mCD3-δ | Cancer cell line; double KO, not an EDEM3-only knockout |
| EDEM3-KO HepaRG (PMID:39838427) | ↑BiP/PERK/p-eIF2α, apoptosis via p53/BAX, cell death at high passage | Context is HCC/HBV; contradicts the direction of UPR in patient LCLs |
| *C. elegans* edem mutants (Ghenea et al. 2022, *PLoS Genet*, PMID:35192599; fetch) | EDEM-2 acts on basal ERAD, EDEM-1/3 under stress; EDEM loss activates protective stress responses | Invertebrate; no neurodevelopmental readout |

**Model gap:** there is no iPSC-derived neuronal or organoid model of EDEM3-CDG.

---

## Evidence-source summary for curation

| PMID | Type | Use |
|---|---|---|
| 34143952 | HUMAN_CLINICAL (+ IN_VITRO + MODEL_ORGANISM sentences; split them by sentence) | Disease definition, phenotypes, variants, biomarker, UPR, mouse |
| 16431915 | IN_VITRO (abstract only) | EDEM3 GH47 mannosidase, ERAD enhancement |
| 29784879 | IN_VITRO | ERp46 activation, Cys83/Cys442 disulfide |
| 34698634 | IN_VITRO | EDEM3 as main M8B→M7/M6/M5 enzyme; EDEM1/3 DKO cells |
| 35500441 | IN_VITRO (abstract only) | Asn-linked M9 substrate, ERp46 enhancement |
| 39838427 | IN_VITRO (cancer context; use cautiously) | ER localization; KO → ER stress and apoptosis in hepatic cells |
| 32213464, 35192599, 25092655, NCT04199000 | Not cached | Fetch with `just fetch-reference` before quoting |

**Gaps for the entry:**
- No GeneReviews chapter (confirm with `just check-genereviews`).
- No natural-history, prevalence, prognosis or treatment data.
- The neural mechanism is unmodeled.
- The direction of the UPR change is unresolved: blunted in patient LCLs, activated in KO hepatic cells. This is a good `KNOWLEDGE_GAP` discussion.

---

**Sources:**
- Local `references_cache/` records: PMID_34143952, PMID_16431915, PMID_29784879, PMID_34698634, PMID_35500441, PMID_39838427
- [CDG Hub – EDEM3-CDG (CDG-IIv)](https://www.cdghub.com/cdg/edem3-cdg/)
- [FCDGC – EDEM3-CDG](https://fcdgc.rarediseasesnetwork.org/diseases-studied/edem3-cdg)
- [OLS – MONDO:0030423](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0030423)
- [EDEM3 Modulates Plasma Triglyceride Level through LRP1 (PMC7093811 / PMID:32213464)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7093811/)
- [Exome-wide association study of plasma lipids, Nat Genet 2017](https://www.nature.com/articles/ng.3977)
- [CDG state of the art 2022, Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-023-02879-z)
- [PubMed E-utilities search for "EDEM3"](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=EDEM3&retmax=100)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 29 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0051050` (1 mention) - the report calls it "DOID"; DOID calls it **congenital disorder of glycosylation type IIv**
- `CL:0000540` (1 mention) - the report calls it "inferred target tissue only"; CL calls it **neuron**
- `NCIT:C15747` (1 mention) - the report calls it "a gastrostomy procedure term needs lookup"; NCIT calls it **Supportive Care**
- `NCIT:C15986` (1 mention) - the report calls it "agent unspecified in the source"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000057` (1 mention) - the report calls it "skin fibroblasts studied"; CL calls it **fibroblast**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.