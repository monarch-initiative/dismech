---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-19T12:38:24.035306'
end_time: '2026-10-19T12:43:39.828644'
duration_seconds: 315.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Seizures, Spasticity, And Complete
    Or Partial Agenesis Of The Corpus Callosum
  mondo_id: MONDO:0859516
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
  web_search_requests: 9
  num_turns: 27
  total_cost_usd: 2.2698743999999995
  session_id: 8cd064c0-c7be-4ce8-ad0f-144091459ebb
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 11
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 44
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0859516
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with seizures, spasticity, and complete
      or partial agenesis of the corpus callosum
  - term_id: HP:0011968
    reported_labels:
    - infancy
    ontology_label: Feeding difficulties
  - term_id: HP:0000365
    reported_labels:
    - variable
    ontology_label: Hearing impairment
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Seizures, Spasticity, And Complete Or Partial Agenesis Of The Corpus Callosum
- **MONDO ID:** MONDO:0859516 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Seizures, Spasticity, And Complete Or Partial Agenesis Of The Corpus Callosum** covering all of the
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

I'm pulling the full text of the founding paper (Faqeih et al. 2023) to get variant and phenotype detail.

Gathering the HECTD4 molecular-function papers (COX-2 degradation, GluN2B/MALT1 in neurons) before writing.

# Research Report: Neurodevelopmental Disorder With Seizures, Spasticity, and Complete or Partial Agenesis of the Corpus Callosum (NEDSSACC; HECTD4-related)

**Prepared:** 2026-10-19 · **Target:** MONDO:0859516 · **Category:** Mendelian (autosomal recessive)

## Scope and limits

The evidence base is very small. The disorder is defined by **one primary clinical paper**: Faqeih et al., *Genet Med* 2023, PMID:36401616. That paper describes **7 HECTD4 patients from 5 families**. The same paper also reports UBE3C patients, who have a different disease.

- I could read only the abstract of PMID:36401616. It is cached in this repo at `references_cache/PMID_36401616.md`.
- PMC, OMIM (403) and the Marmara open-access copy (503) were all unreachable. So the per-patient variant list, phenotype counts and RNA-study details below come from the abstract and from secondary aggregators: MedGen/GTR, PanelApp and GenCC.
- **Specific variant nomenclature (cDNA/protein) could not be verified** and is not given here.
- A targeted search found no 2024–2026 reports of new HECTD4 patients. Europe PMC lists 13 papers citing PMID:36401616. Three of them might contain HECTD4 cases and were not checked: PMID:39313616, PMID:42016445 and PMID:38274568.
- All ontology CURIEs below are **leads to be looked up** (runoak or cache) before they go into the KB, as CLAUDE.md requires.

---

## 1. Disease Information

**Overview.** OMIM's definition, as reproduced in MedGen/GTR: an autosomal recessive disorder with "axial hypotonia and global developmental delay evident from the first days or months of life." Other features are:
- feeding difficulties
- early-onset seizures that are usually well controlled
- peripheral spasticity with hyperreflexia
- variable dysmorphic features
- impaired intellectual development
- behavioural abnormalities
- hypoplasia or absence of the corpus callosum on brain imaging

([MedGen C5830296](https://www.ncbi.nlm.nih.gov/medgen/C5830296); [GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5830296))

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0859516 |
| OMIM (phenotype) | #620250 |
| OMIM (gene, HECTD4) | *620209 (PanelApp says it cross-checked this against Ensembl and HGNC) |
| MedGen | C5830296 (UID 1840932) |
| Orphanet | none found |
| ICD-10/ICD-11, MeSH | no disease-specific code; falls under generic intellectual disability / CNS-malformation codes |
| Gene | HECTD4, 12q24.13; HGNC:26611 (lowercase `hgnc:26611` in this repo); NCBI Gene 283450 |

**Synonyms.** NEDSSACC (the MedGen record writes it as "NEDSSCC"); "HECTD4-related neurodevelopmental disorder". Gene alias: **C12orf51**.

**Data provenance.** The disease concept is built from aggregated case-series data: one multi-centre exome study with cases from Saudi Arabia, France, Italy, Turkey, the USA and Morocco, judging by the author list. There are no EHR or registry data.

## 2. Etiology

- **Cause.** Biallelic germline HECTD4 variants. The abstract states: "4 patients were found to have 3 different homozygous loss-of-function (LoF) variants, and 3 patients had 4 compound heterozygous missense variants in the candidate E3 ligase gene, HECTD4, that were rare, absent from controls as homozygous, and predicted to be deleterious in silico" (PMID:36401616). PanelApp's summary: "seven patients from five unrelated families with either homozygous (3 families)" or compound-heterozygous (2 families) variants.
- **Supporting functional data.** "The RNA studies in 4 patients with LoF variants in HECTD4 and UBE3C provided evidence for the LoF effect" (PMID:36401616). This was in vitro work on patient RNA. The abstract does not say how many of the 4 were HECTD4 patients.
- **Risk factors.** The only identified risk factor is parental consanguinity. Homozygous families came from Middle-East/North-Africa cohorts; this is inferred from the cohorts and not counted per family.
- **Environmental, protective and gene–environment factors.** None reported for the Mendelian disorder.
- **A separate signal that should not be conflated with this disease.** Common HECTD4 SNPs at 12q24 (rs11066280, rs2074356, rs77768175) are associated in Korean/East Asian cohorts with alcohol intake, type 2 diabetes risk, fasting glucose and triglycerides ([PMC4758657](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4758657/); [PMC9325801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9325801/)). These variants sit in the same region as ALDH2 rs671, and nothing links them to NEDSSACC.

## 3. Phenotypes

Source: the MedGen/OMIM clinical synopsis (49 HPO features). Frequencies are reported only for intellectual disability. PanelApp states: "All seven patients had severe (4 cases) or moderate (3 cases) intellectual disability." Everything else is listed qualitatively. Onset is neonatal or early infantile for hypotonia and delay, and seizures start early. The course appears to be a static encephalopathy, but there are no natural-history data.

| Phenotype | Type | Characteristics | Suggested HPO (verify) |
|---|---|---|---|
| Axial hypotonia | sign | first days to months of life | HP:0008936 Axial hypotonia; HP:0001252 Hypotonia |
| Global developmental delay / motor delay | sign | infancy | HP:0001263; HP:0001270 Motor delay |
| Intellectual disability | sign | moderate in 3/7, severe in 4/7 | HP:0001249 (HP:0002342 moderate / HP:0010864 severe) |
| Seizures | sign | early onset, "usually well controlled" | HP:0001250 Seizure |
| Peripheral/appendicular spasticity | sign | — | HP:0001257 Spasticity (an appendicular-specific term may exist; search) |
| Hyperreflexia | sign | — | HP:0001347 |
| Agenesis or partial agenesis of the corpus callosum | imaging | defining feature | HP:0001274; HP:0001338 Partial agenesis of the corpus callosum |
| Feeding difficulties | symptom | infancy | HP:0011968 |
| Gastroesophageal reflux | sign | — | HP:0002020 |
| Autism, aggression, anxiety | behavioural | — | HP:0000717; HP:0000718; HP:0000739 |
| Apraxia / oculomotor apraxia | sign | — | HP:0002186; HP:0000657 |
| Movement disorder | sign | named in the abstract, not specified | — |
| Macrocephaly, overgrowth, obesity | growth | variable | HP:0000256; HP:0001548; HP:0001513 |
| Hearing impairment | sign | variable | HP:0000365 |
| Scoliosis, thoracic kyphosis | skeletal | variable | HP:0002650; HP:0002943 |
| Dysmorphism | physical | variable | see list below |

The dysmorphic features listed are:
- forehead: broad or prominent forehead, frontal bossing
- eyes: down- or upslanted palpebral fissures, hypertelorism, proptosis, blue sclerae, synophrys, long eyelashes
- nose and philtrum: wide nasal bridge, short nose, long or short philtrum
- mouth and jaw: wide or narrow mouth, thick vermilion, narrow palate, micro- or retrognathia
- ears: macrotia or microtia
- teeth: hypodontia, dental hypoplasia
- other: short neck, tapered fingers, fine hair

Several listed features are opposites (wide and narrow mouth, long and short philtrum, up- and downslanting fissures, macrotia and microtia). This means the dysmorphism is heterogeneous across families rather than a recognisable gestalt.

**Quality of life.** No QoL data exist. The disability burden comes from moderate-to-severe ID, motor impairment and behavioural comorbidity.

## 4. Genetic/Molecular Information

- **Gene.** HECTD4 (HECT domain E3 ubiquitin protein ligase 4), 12q24.13. It is a very large HECT-family E3 ligase; UniProt Q9Y4D8, about 4,400 aa, both from memory and unverified. The C-terminal HECT domain is related to E6AP/UBE3A. PNAS 2025 describes it as encoding a ubiquitin transferase with an E6AP-C-terminus-like domain.
- **Variant classes.** Homozygous LoF in 3 families; the abstract does not separate nonsense, frameshift and splice. Compound-heterozygous missense in 2 families (4 alleles). There are no somatic or structural variants and no chromosomal abnormalities.
- **ACMG classifications and allele frequencies.** Not retrieved; check ClinVar. "Absent from controls as homozygous" is the only population statement available.
- **Functional consequence.** Loss of function, supported by the patient RNA studies (PMID:36401616). For the missense alleles, LoF is presumed.
- **Gene–disease validity.** GenCC has several submissions (Strong / Moderate / Limited, AR) ([GenCC HGNC:26611](https://thegencc.org/genes/HGNC:26611)). In this repo a tier may only be copied with its source record (`classified_by`); I did not retrieve a ClinGen CGGV record, so leave `gene_disease_validity` absent unless one is cached. PanelApp rates it green, biallelic, on the Malformations of cortical development panel (promoted 2 May 2024) ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/96/gene/HECTD4/)).
- **Modifier genes and epigenetics.** None reported.

## 5. Environmental Information

Not applicable. There are no known environmental, lifestyle or infectious contributors.

## 6. Mechanism / Pathophysiology

**Causal chain** (★ = shown in this disease; ◇ = inferred from other HECTD4 biology or from the HECT-ligase class, and not shown in patients):

1. ★ Biallelic HECTD4 LoF or missense variants **lead to** loss of HECTD4 transcript or function. The RNA studies support LoF (PMID:36401616).
2. ◇ Loss of HECTD4 **results in** reduced ubiquitin conjugation and slower proteasomal turnover of its substrates. Purified HECTD4 "mediates ubiquitin conjugation in vitro". Its substrates include COX-2/PTGS2 and MKK7 in epithelial cancer cells (PMID:40768362, PNAS 2025). In neurons the reported substrates are GluN2B and MALT1 (PMID:36527595, rat stroke model).
3. ◇ In neurons, reduced GluN2B/MALT1 ubiquitination **leads to** increased GluN2B phosphorylation, which goes through MALT1 and STEP61 degradation. That in turn **leads to** NMDA-receptor-driven Ca²⁺ overload. "Knockdown of HECTD4 exacerbated hypoxia- or NMDA-induced injury in nerve cells" (PMID:36527595). This is an *acquired-injury* model and has not been shown developmentally.
4. ◇ Branch A: disturbed protein homeostasis and glutamatergic signalling during brain development **is hypothesised to cause** neuronal hyperexcitability (→ seizures) and impaired cortical circuit function (→ ID, autism, behavioural features). This is a proposed link and is not demonstrated.
5. ◇ Branch B: defects in callosal axon development **result in** complete or partial corpus callosum agenesis. The mechanism is entirely unknown. No HECTD4 substrate has been tied to axon guidance or midline crossing.
6. ◇ Branch C: upper-motor-neuron or corticospinal tract dysfunction **results in** peripheral spasticity and hyperreflexia, alongside axial hypotonia. The mechanism is not studied.
7. The clinical picture overlaps with Angelman syndrome, which the authors frame through HECT-paralog logic (UBE3A/UBE3C). This is phenotypic analogy, not a shared demonstrated pathway.

**Pathways and processes.** Ubiquitin–proteasome system; NMDA-receptor signalling; prostaglandin synthesis (COX-2), shown in cancer cells only. Common GWAS variants link the gene to glucose homeostasis; this is a GO annotation that is largely computational. There are no metabolic, immune, transcriptomic, proteomic, single-cell or CRISPR data specific to this disease.

**Suggested GO terms** (verify): protein ubiquitination GO:0016567; ubiquitin protein ligase activity GO:0061630; ubiquitin-dependent protein catabolic process GO:0006511; corpus callosum development GO:0022038; NMDA-receptor-related regulation terms (search).

**Suggested CL terms** (verify): neuron CL:0000540; a callosal/cortical projection neuron term (search CL); glutamatergic neuron CL:0000679.

## 7. Anatomical Structures Affected

- **Primary:** brain, specifically the corpus callosum (UBERON:0002336, verify), cerebral cortex and corticospinal motor system.
- **Secondary:** GI tract (reflux, feeding), spine (scoliosis/kyphosis), ear/auditory system, teeth, craniofacial structures.
- **Subcellular (inferred):** cytoplasm and postsynaptic NMDA-receptor complex (GluN2B interaction), proteasome-associated ubiquitination.
- **Laterality:** bilateral or midline. Not otherwise reported.

## 8. Temporal Development

- **Onset:** congenital or neonatal to early infancy; hypotonia and delay appear "from the first days or months of life".
- **Course:** a static neurodevelopmental disorder; no progression or regression is reported.
- **Seizure tempo:** early onset, generally controllable.
- **Stages and remission:** none defined.
- **Critical period:** the prenatal window for callosal formation, by inference.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007, verify).
- **Prevalence:** unknown. There are 7 published patients, so use measure type `CASES_IN_LITERATURE`.
- **Penetrance, expressivity and anticipation:** penetrance is presumed complete for biallelic variants. Expressivity varies, especially for dysmorphism and growth. No anticipation or mosaicism is reported.
- **Consanguinity:** relevant for the homozygous families.
- **Founder effects, carrier frequency and sex ratio:** not reported.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing is the route to diagnosis; all published cases were found by ES, with chromosomal analysis first. HECTD4 is on PanelApp's Malformations of cortical development panel and the Australian Angelman/Rett-like panel ([PanelApp AUS](https://panelapp-aus.org/panels/41/gene/HECTD4/)). Patient RNA studies can support LoF splice or NMD effects.
- **Imaging:** brain MRI for corpus callosum agenesis or hypoplasia.
- **Electrophysiology:** EEG for seizures.
- **Biomarkers and metabolic tests:** none specific.
- **Clinical criteria:** none established.
- **Differential diagnosis:**
  - Angelman syndrome (UBE3A, 15q11-q13 methylation) and UBE3C-related Angelman-like disorder
  - other syndromic corpus callosum agenesis disorders (e.g. DCC, ARID1B, ZEB2/Mowat-Wilson)
  - other recessive NDDs with spasticity
- **Screening:** not applicable. Carrier and prenatal testing are possible once familial variants are known.

## 11. Outcome/Prognosis

No survival or mortality data exist. Morbidity comes from moderate-to-severe ID, motor disability, behavioural disorders and feeding problems. Seizures are reported as generally well controlled, which is favourable. No prognostic factors are known.

## 12. Treatment

There is no disease-specific therapy, no trials and no pharmacogenomic data. Supportive management, with NCIT leads to look up:

| Intervention | NCIT (verify) | `therapeutic_modality` |
|---|---|---|
| Antiseizure pharmacotherapy | NCIT:C15986 Pharmacotherapy | SMALL_MOLECULE |
| Physical therapy | NCIT:C15302 | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Speech-language therapy | NCIT:C159273 | BEHAVIORAL |
| Feeding / nutritional support (GERD management) | NCIT:C15433 Nutritional Support | judge per case (see CLAUDE.md) |
| Behavioural interventions | NCIT:C181743 | BEHAVIORAL |
| Genetic counseling | NCIT:C15240 | — |

## 13. Prevention

Only genetic counselling applies: a 25% recurrence risk for carrier parents, with carrier testing of relatives and prenatal or preimplantation diagnosis once the familial variants are known. Tertiary prevention covers seizure control, scoliosis surveillance and nutrition.

## 14. Other Species / Natural Disease

No naturally occurring animal disease is known; there is no OMIA entry. Orthologues:
- mouse *Hectd4*, MGI:3647820, NCBI Gene 269700 ([IMPC](https://www.mousephenotype.org/data/genes/MGI:3647820))
- rat *Hectd4*, used in the stroke study

Drosophila *poe* is a UBR4-family ligase, **not** a HECTD4 orthologue, so do not cite it.

## 15. Model Organisms

- **Mouse knockout (IMPC):** significant phenotypes in vision/eye, immune, homeostasis/metabolism and haematopoietic systems. No neurodevelopmental, corpus callosum or seizure phenotype is reported, and there is no dedicated publication. This is a candidate `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion; it depends on whether brain imaging was ever examined. Commercial KO lines exist (GemPharmatech).
- **Rat MCAO stroke model and cultured neurons (PMID:36527595):** HECTD4 knockdown models acquired excitotoxic injury, not development. Use `MODEL_ORGANISM` and `IN_VITRO` evidence, with fidelity LOW for developmental nodes.
- **Breast CTC / mouse xenograft CRISPR screen (PMID:40768362):** biochemical evidence for E3 activity only.
- **No patient iPSC, organoid, zebrafish or fly models** exist.

---

## Curation notes for the KB entry

- Keep the evidence structure for PMID:36401616 honest. It is abstract-only in the cache, so snippets must come from the abstract. Usable quotes are the "4 patients… homozygous loss-of-function…" sentence and the "RNA studies… provided evidence for the LoF effect" sentence.
- The abstract does not quote the phenotype frequencies, corpus callosum findings or spasticity. ORPHA has no record. Consider citing OMIM-derived content only through a cacheable source. Otherwise leave phenotype evidence limited and say so in `notes`.
- Pathophysiology nodes beyond "HECTD4 loss of function" are inferential. Model them with `mechanistic_hypotheses` (status EMERGING) and a `KNOWLEDGE_GAP` discussion on the corpus callosum and seizure mechanisms, rather than as established causal edges.
- Fetch PMID:36527595 and PMID:40768362 with `just fetch-reference` before citing them.

## Sources
- Faqeih EA et al. Genet Med 2023;25(2). PMID:36401616 ([DOI](https://doi.org/10.1016/j.gim.2022.10.006); [Baylor record](https://digitalcommons.library.tmc.edu/baylor_docs/5069))
- [MedGen C5830296](https://www.ncbi.nlm.nih.gov/medgen/C5830296) · [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5830296)
- [GenCC HECTD4](https://thegencc.org/genes/HGNC:26611)
- [Genomics England PanelApp – HECTD4](https://panelapp.genomicsengland.co.uk/panels/96/gene/HECTD4/) · [PanelApp Australia](https://panelapp-aus.org/panels/41/gene/HECTD4/)
- Zhang YY et al. Mol Neurobiol 2023;60(3):1563-1579. PMID:36527595 (via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:36527595&format=json&resultType=core))
- Vuille JA et al. PNAS 2025;122(32):e2425621122. PMID:40768362, PMC12358835
- [IMPC Hectd4](https://www.mousephenotype.org/data/genes/MGI:3647820) · [Wikipedia HECTD4](https://en.wikipedia.org/wiki/HECTD4) · [FlyBase poe](https://flybase.org/reports/FBgn0011230)
- KoGES HECTD4 and T2D: [PMC4758657](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4758657/), [PMC9325801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9325801/), [Arch Toxicol 2022](https://link.springer.com/article/10.1007/s00204-022-03325-y)
- [Affinage HECTD4 summary](https://affinage.wi.mit.edu/gene/HECTD4) (secondary aggregator; used only to locate primary papers)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 8 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859516` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with seizures, spasticity, and complete or partial agenesis of the corpus callosum**
- `HP:0011968` (1 mention) - the report calls it "infancy"; HP calls it **Feeding difficulties**
- `HP:0000365` (1 mention) - the report calls it "variable"; HP calls it **Hearing impairment**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C181743` (1 mention) - the report calls it "Behavioural interventions"; NCIT calls it **Behavioral Counseling**, and lists "Behavioral Psychotherapy" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `EXT_ID`.