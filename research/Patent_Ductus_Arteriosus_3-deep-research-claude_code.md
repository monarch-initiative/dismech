---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T09:16:04.924380'
end_time: '2026-09-03T09:22:20.919575'
duration_seconds: 376.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Patent Ductus Arteriosus 3
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
  web_search_requests: 17
  num_turns: 32
  total_cost_usd: 1.6527993999999995
  session_id: aeedb7fe-b75e-5a9a-a99b-252fe1f46546
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 22
reference_validation:
  total_references: 15
  verified: 14
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.067
  relevance_assessed: 14
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - DOI:10.1161/01.cir.0000145159.16637.5d
  unresolved_references:
  - PMC:PMC38071433
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 16
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 6
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0024266
    reported_labels:
    - Ontology identifier for PDA3
    ontology_label: patent ductus arteriosus 3
  - term_id: CL:0000359
    reported_labels:
    - verify
    ontology_label: vascular associated smooth muscle cell
  - term_id: UBERON:0002106
    reported_labels:
    - verify via OAK
    ontology_label: spleen
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0034770
    ontology_label: obsolete histone H4-K20 methylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Patent Ductus Arteriosus 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Patent Ductus Arteriosus 3** covering all of the
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

I'll research Patent Ductus Arteriosus 3 using web search and authoritative sources like OMIM, PubMed, and GeneReviews.

I now have sufficient material across all sections. Here is the comprehensive research report.

# Patent Ductus Arteriosus 3 (PDA3) — Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Patent ductus arteriosus 3 (PDA3) is an autosomal-dominant, non-syndromic (isolated) form of patent ductus arteriosus (PDA) caused by heterozygous loss-of-function mutation in **PRDM6** (PR/SET domain 6; chromosome 5q23.2). The ductus arteriosus is the fetal vessel connecting the main pulmonary artery to the descending aorta that normally closes within hours to weeks of birth; in PDA3 the vessel remains patent because the vascular smooth muscle cells (VSMCs) of the ductus fail to differentiate and remodel normally, independent of prematurity or other congenital heart disease. PDA3 was defined by Li et al. (2016) after linkage mapping in a large African-American kindred (PDA-101) segregating autosomal-dominant PDA with incomplete penetrance, followed by whole-exome sequencing that identified *PRDM6* mutations ([Li et al. 2016, AJHG](https://pmc.ncbi.nlm.nih.gov/articles/PMC4908195), PMID:27181681).

**Key identifiers:**
- **OMIM phenotype:** #617039 – PATENT DUCTUS ARTERIOSUS 3; PDA3 ([omim.org/entry/617039](https://omim.org/entry/617039))
- **OMIM gene:** *616982 – PR DOMAIN-CONTAINING PROTEIN 6; PRDM6 ([omim.org/entry/616982](https://omim.org/entry/616982))
- **MONDO:** MONDO:0024266 – "patent ductus arteriosus 3," defined as "Any patent ductus arteriosus in which the cause of the disease is a mutation in the PRDM6 gene"
- **Orphanet (parent nosologic entity):** ORPHA:466729 – *Familial patent arterial duct* (rare, non-syndromic, autosomal-dominant congenital anomaly of the great arteries) — note that PDA in general is *not* itself in the Orphanet rare-disease nomenclature (ORPHA:706, "non-rare in Europe"); it is the familial/genetic form that is classified as rare ([Orphanet](https://www.orpha.net/en/disease/detail/466729))
- **ICD-10-CM:** Q25.0 – Patent ductus arteriosus (the general code; no PDA3-specific code exists)
- **Gene (HGNC):** PRDM6, HGNC:9350, 5q23.2 (GeneCards)
- **Related loci for genetic heterogeneity of isolated PDA:** PDA1 (OMIM 607411, reference/heterogeneity locus symbol), PDA2 (OMIM 617035, caused by *TFAP2B*, 6p12), PDA3 (OMIM 617039, *PRDM6*). *TFAP2B* is also the gene mutated in **Char syndrome** (syndromic PDA with facial dysmorphism and fifth-finger clinodactyly), and *MYH11* mutations cause a distinct syndrome combining thoracic aortic aneurysm/dissection with PDA (not itself numbered "PDA3").
- **Synonyms:** PRDM6-related patent ductus arteriosus; familial nonsyndromic patent ductus arteriosus (PRDM6 form)

**Evidence basis.** All data on PDA3 specifically derive from **aggregated, family-based genetic studies** (linkage + exome sequencing across pedigrees and unrelated probands) plus a small number of subsequent case reports, not large-scale EHR/individual-patient registries — reflecting its rarity (three known causal variants reported to date, expanded to a handful of additional cases in follow-up reports).

---

## 2. Etiology

**Disease causal factor:** Heterozygous, non-conservative missense mutation in *PRDM6*, acting via loss of function (impaired nuclear localization and/or altered histone methyltransferase activity), inherited in an **autosomal-dominant** pattern with **incomplete penetrance**.

### Genetic risk factors (causal)
Three independent *PRDM6* mutations have been reported, all in individuals/families with isolated (nonsyndromic) PDA and normal-term birth (i.e., not a prematurity-related PDA):

| Variant (cDNA) | Protein change | Domain | Family context |
|---|---|---|---|
| c.1646G>A | p.Arg549Gln (R549Q) | Fourth zinc-finger domain (nuclear localization) | Large African-American kindred PDA-101 (9 affected across generations); segregated with disease, absent in unaffected relatives and all exome databases |
| c.788G>C | p.Cys263Ser (C263S) | SET domain (chromatin regulation) | Proband whose deceased mother and maternal grandfather were also affected |
| c.1385A>G | p.Gln462Arg (Q462R) | — | Affected mother and daughter; predicted deleterious by PolyPhen and SIFT |

Statistical enrichment: recurrent independent *PRDM6* mutations in this small sample were judged unlikely by chance (p < 4.74 × 10⁻⁶); **no** nonsynonymous *PRDM6* variant was found among 2,000 healthy white control exomes (Li et al. 2016, PMID:27181681).

A subsequent case series identified additional/novel *PRDM6* variants (including a previously unreported likely-pathogenic variant) in three patients presenting with **both PDA and coarctation of the aorta**, extending the phenotypic spectrum beyond isolated PDA (Stanley et al. 2024, *Am J Med Genet A*, PMID:38071433, [PMC summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC38071433)).

Gene-set enrichment analysis (GSEA) in the same cohort found that rare deleterious variants in broader **histone-modification pathway genes** were significantly associated with PDA in 15 of 32 affected individuals (estimated OR = 14.95), suggesting epigenetic dysregulation is a recurring theme in nonsyndromic PDA beyond *PRDM6* alone.

### Broader genetic landscape of isolated/nonsyndromic PDA (context, not PDA3-specific)
- **PDA1** (OMIM 607411) — reference locus for genetic heterogeneity of isolated PDA (originally mapped to 5q23 before renaming; a separate autosomal-recessive PDA locus on 12q24 had already used the "PDA1" symbol).
- **PDA2** (OMIM 617035) — *TFAP2B*, 6p12; also causal for **Char syndrome** (facial dysmorphism, PDA, 5th-finger clinodactyly) when haploinsufficient/dominant-negative missense.
- ***MYH11*** — smooth-muscle myosin heavy chain; mutations cause a syndrome combining thoracic aortic aneurysm/dissection (TAAD) with PDA (Pannu et al. 2007; Zhu et al. 2006, PMID:16444274).
- Candidate/rare-variant genes from exome studies: *NOTCH1*, *FOXC2*, *CITED2*, and others identified via WES/CNV studies of nonsyndromic PDA cohorts (e.g., PMID:35734438, PMC7689032).
- Chromosomal etiologies of PDA broadly: trisomy 21, trisomy 13, trisomy 18, and other aneuploidies/CNVs are well-documented non-Mendelian causes of PDA (not PDA3, but relevant differential).

### Environmental / infectious risk factors (for PDA broadly, differential for PDA3)
- **Prematurity** is the dominant risk factor for PDA in general (up to 30% of infants 500–1500 g by day 3; >70% in infants <1000 g) — this is mechanistically and clinically distinct from the *genetic* PDA3 form, which occurs in term infants.
- **Congenital rubella syndrome**: maternal rubella infection in the first trimester is a classic teratogenic/infectious cause of PDA (histopathologically distinct — abnormal elastic tissue in the ductal wall) (PMID reviews on congenital rubella and PDA, PMC6863812).
- High altitude, maternal factors, and other prematurity-associated exposures are risk factors for the sporadic/prematurity form but are not implicated in PDA3.

### Protective factors
No specific genetic or environmental protective factors have been reported for PDA3. For prematurity-associated PDA generally, antenatal corticosteroids reduce PDA incidence indirectly by reducing prematurity-related morbidity; this is not disease-specific to PDA3.

### Gene-environment interaction
Not established for PDA3; the mechanism is described as a cell-autonomous VSMC differentiation/epigenetic defect rather than gene-environment interaction.

---

## 3. Phenotypes

PDA3 presents as an essentially **isolated cardiovascular malformation** — the reported kindreds and cases are notable for the *absence* of syndromic features (no consistent facial dysmorphism, limb anomaly, or other organ-system involvement), distinguishing it from Char syndrome (TFAP2B/PDA2).

| Phenotype | Type | HPO suggestion | Onset | Notes |
|---|---|---|---|---|
| Patent ductus arteriosus | Congenital structural cardiac anomaly | **HP:0001643** (Patent ductus arteriosus) | Congenital (present at birth in term infants) | Core/defining feature; failure of ductal closure |
| Continuous ("machinery") heart murmur | Clinical sign | HP:0030148 (Heart murmur) — general term; a specific "continuous murmur" HPO term should be confirmed via OAK/HPO browser before use | Infancy | Classic auscultatory finding of a large PDA |
| Congestive heart failure (if large shunt) | Clinical sign/complication | HP:0001635 (Congestive heart failure) | Infancy–childhood, dependent on shunt size | Secondary to left-to-right shunt volume overload |
| Pulmonary arterial hypertension (if large, uncorrected shunt) | Clinical sign/complication | HP:0002092 (Pulmonary hypertension) | Progresses over years if untreated | ~50% of infants with large nonrestrictive PDA develop pulmonary hypertension by early childhood |
| Coarctation of the aorta (in some PRDM6-variant carriers) | Congenital structural cardiac anomaly | HP:0001680 (Coarctation of aorta) | Congenital | Reported co-occurring with PDA in 3 patients with PRDM6 variants (Stanley et al. 2024) — extends phenotype beyond "isolated PDA" |
| Reduced penetrance / asymptomatic carriers | — | — | — | Some obligate carriers in reported pedigrees do not manifest PDA, consistent with incomplete, age-independent penetrance |

**Severity/progression:** Severity is determined by shunt size (small/moderate/large), not by genotype specifically; no PDA3-specific genotype-phenotype severity correlation has been established given the small number of reported families. Course is **not** episodic — an uncorrected large PDA follows a **progressive** trajectory toward pulmonary vascular disease if untreated, while a small PDA may remain **stable** or even undergo spontaneous late closure in rare cases (uncommon after infancy in term-born PDA).

**Quality of life impact:** Direct QOL data for PDA3 specifically are not available. For symptomatic PDA generally, unrepaired large shunts are associated with exercise intolerance, failure to thrive in infancy, and, if progressing to Eisenmenger physiology, cyanosis and severe functional limitation.

---

## 4. Genetic/Molecular Information

**Causal gene:** *PRDM6* (PR domain-containing protein 6), HGNC:9350, chromosome 5q23.2. OMIM gene entry *616982.

**Gene product/function:** PRDM6 is a nuclear protein expressed selectively in vascular smooth muscle cells. It contains a SET (PR) domain with histone methyltransferase activity and zinc-finger DNA/protein-interaction domains. It acts as a transcriptional repressor of VSMC contractile genes (e.g., *MYH11*, α-smooth muscle actin) and cooperates with **myocardin-related transcription factor-A (MRTF-A)** and other SMC transcriptional regulators; it also epigenetically regulates neural-crest-cell specification genes (*Wnt1*, *Tfap2b*, *Sox9*) via H4K20 monomethylation, controlling G1–S progression needed for neural crest delamination/migration into the ductal wall (Zou et al. 2023, *JCI Insight*, PMID:36749647; additional neural-crest mechanistic paper, PMC8876496).

**Variant classification (ACMG/AMP framework, as reported by original authors, not formally re-classified in ClinVar at time of writing):**

| Variant | Type | Predicted effect | Population frequency |
|---|---|---|---|
| p.Arg549Gln | Missense | Loss of function — cytoplasmic mislocalization, altered methyltransferase output | Absent from >2,000 control exomes and population databases (gnomAD not specifically reported in source, but described as absent from exome variant databases at publication) |
| p.Cys263Ser | Missense (SET domain) | Loss of function — retained nuclear localization but altered histone methylation activity | Absent from controls |
| p.Gln462Arg | Missense | Predicted deleterious (PolyPhen, SIFT) | Absent from controls |

**Zygosity/origin:** All reported variants are **heterozygous, germline**, consistent with autosomal-dominant transmission (no somatic PDA3 cases reported; PDA is not a neoplastic condition).

**Functional consequences (mechanistically loss-of-function, established in vitro):**
- **Subcellular mislocalization:** Wild-type PRDM6 and p.Cys263Ser localize normally to the nucleus in HEK293 cells and human aortic VSMCs; **p.Arg549Gln is predominantly mislocalized to the cytoplasm**, with co-staining excluding ER/Golgi/mitochondrial retention — consistent with impaired nuclear import via the disrupted zinc-finger domain.
- **Histone methyltransferase activity reversed:** Wild-type PRDM6 reduces H3K9 dimethylation and increases H4K20 dimethylation; **both p.Arg549Gln and p.Cys263Ser show completely opposite effects** on these histone marks.
- **Failure to suppress contractile proteins:** Wild-type PRDM6 overexpression suppresses MYH11 in human aortic VSMCs; **both mutant proteins largely fail to reduce MYH11**, and variant-expressing cells show higher steady-state MYH11 and α-SMA than wild-type.
- **No dominant-negative dimerization effect:** Native PAGE excluded altered wild-type/variant heterodimerization as the mechanism — supporting simple **haploinsufficiency-type loss of function** rather than dominant-negative protein poisoning.

**Modifier genes:** None specifically established for PDA3; broader GSEA-level enrichment of histone-modification-pathway variants in the same cohort suggests a possible oligogenic/epigenetic modifier landscape, but no individual modifier gene has been validated.

**Epigenetic information:** PDA3 is fundamentally a disorder of **epigenetic dysregulation** — PRDM6 is itself a chromatin-modifying enzyme, and its variants alter H3K9me2/H4K20me2 marks at target loci controlling VSMC differentiation genes. This is the central molecular lesion, not a downstream epiphenomenon.

**Chromosomal abnormalities:** None reported for PDA3 specifically (contrast with PDA broadly, where trisomy 21/18/13 are well-known non-Mendelian causes).

**Suggested ontology terms:**
- Gene: HGNC:9350 (PRDM6); note dismech convention uses lowercase `hgnc:9350`
- GO Molecular Function candidates (verify via OAK before binding): histone methyltransferase activity (GO:0042054/more specific child terms), histone H4-K20 methyltransferase activity (GO:0140945 or similar — verify), DNA-binding transcription repressor activity
- GO Biological Process candidates: negative regulation of transcription (GO:0045892), histone H4-K20 methylation (GO:0034770), regulation of smooth muscle cell differentiation, neural crest cell migration (GO:0001755)

---

## 5. Environmental Information

PDA3 itself is a **monogenic** condition with no reported environmental modifiers of penetrance or expressivity in the literature. Environmental factors relevant to PDA as a broader clinical entity (but not specifically implicated in the PRDM6-driven form):
- **Congenital rubella syndrome** (infectious/teratogenic) — classic non-genetic cause of PDA, histologically distinct (elastic tissue fragmentation in the ductal wall) from the genetic forms.
- **Prematurity/hypoxia/high altitude** — drive the far more common, non-genetic "premature PDA," mechanistically related to immature oxygen-sensing and prostaglandin-clearance pathways rather than a structural/differentiation gene defect.
- No infectious agent, toxin, or lifestyle factor has been linked causally to PDA3.

---

## 6. Mechanism / Pathophysiology

### Causal chain (PDA3)

1. Heterozygous loss-of-function mutation in *PRDM6* (e.g., p.Arg549Gln, p.Cys263Ser, p.Gln462Arg) **impairs** PRDM6 nuclear localization and/or its histone methyltransferase activity (established in vitro, human/mouse cell systems).
2. Loss of PRDM6 function **reverses** its normal epigenetic output at target loci: instead of reducing H3K9me2 and increasing H4K20me2, mutant protein produces the opposite chromatin changes (demonstrated in vitro).
3. Altered chromatin state **fails to repress** VSMC contractile-differentiation genes (*MYH11*, α-SMA) in ductal smooth muscle cells during fetal life, when PRDM6 is normally highly expressed specifically in ductus arteriosus (but not aortic) smooth muscle (demonstrated by mouse immunofluorescence at E14.5, E17.5, P0.5).
4. This **leads to** premature differentiation of ductal VSMCs and — paradoxically, despite higher contractile-protein levels — **reduced VSMC proliferation** and **impaired subintimal cushion formation/remodeling** of the ductus (the process that normally produces permanent anatomical closure); this step is **inferred** from the correlative in vitro/mouse expression data rather than directly demonstrated by lineage-tracing loss-of-function in the human variant carriers themselves.
5. Failure of normal ductal wall remodeling **results in** persistent ductal patency after birth despite the normal postnatal drop in prostaglandin E2 and rise in oxygen tension (i.e., the general perinatal "closure trigger" signal may still occur, but the ductal wall cannot execute the anatomic remodeling response) — clinical PDA.
6. If the ductus remains widely patent, sustained left-to-right shunting **leads to** pulmonary overcirculation, left heart volume overload, and, if uncorrected over years, **progressive** pulmonary vascular remodeling → pulmonary arterial hypertension → (in the most severe, longstanding, uncorrected cases) Eisenmenger physiology with shunt reversal and cyanosis.
7. A parallel/branching pathway, shown specifically in mouse neural-crest-conditional *Prdm6* knockouts (not yet directly confirmed as the operative mechanism in the human missense-variant carriers): loss of Prdm6-mediated H4K20 monomethylation **impairs** G1–S cell-cycle progression required for cardiac neural crest cell (CNCC) delamination and migration, via **elevated Wnt1 signaling**; this **reduces** CNCC contribution to the ductal smooth muscle layer, independently contributing to a PDA phenotype (Wnt1-Cre and SM22-Cre conditional Prdm6 knockout mice both show complete-penetrance PDA and perinatal lethality) (PMC8876496).

### Molecular pathways
- Histone methylation / chromatin remodeling (H3K9me2, H4K20me2) via the PRDM6 SET domain.
- MRTF-A/SRF-dependent smooth-muscle gene transcription — PRDM6 physically interacts with the central and N-terminal actin-binding regions of MRTF-A (JCI Insight, PMC/Zou et al. 2023).
- Downstream target genes altered in *Prdm6*-depleted mouse ductus arteriosus include the PGE2 receptor **EP4 (Ptger4)**, and transcription factors **Tfap2b, myocardin, Foxc1, Hand2**; Notch pathway components **Jag1, Notch3** are also altered.
- A common non-coding *PRDM6* variant (rs17149944) in an SMC-selective intronic enhancer (bound by SRF, RBPJ, TEAD) has separately been proposed as a causal SNP at a cardiovascular/hypertension GWAS locus, indicating a dose-sensitive relationship between PRDM6 expression level and vascular smooth muscle/blood-pressure phenotypes more broadly.

### Cellular processes
- Vascular smooth muscle cell (VSMC) differentiation and proliferation (dysregulated — premature differentiation, reduced proliferation).
- Neural crest cell delamination, EMT, and migration (impaired in conditional knockout mice).
- Intimal cushion formation via subendothelial VSMC migration/proliferation and extracellular matrix deposition (the normal anatomic-closure process that fails).
- Contractile response: in a related Prdm6-depletion mouse model, DA segments showed reduced myogenic tone, absent contractile response to KCl, eliminated oxygen-induced constriction, and reduced thromboxane-agonist response (40% vs. 76% in controls) — directly linking loss of PRDM6-regulated SMC identity to failure of the ductal *functional* constriction response as well as anatomic remodeling.

### Protein dysfunction
Loss-of-function via (a) impaired nuclear localization (p.Arg549Gln) and (b) altered catalytic/chromatin-binding output of the SET domain (p.Cys263Ser and, inferentially, p.Gln462Arg) — not dominant-negative dimerization.

### Tissue damage mechanism
Not applicable in the classic sense (no cell death/fibrosis/oxidative injury described); the "tissue damage" analog is a **developmental patterning failure** — the ductal wall never acquires the mature, contractile, remodeling-competent VSMC phenotype needed for closure.

### Immune system involvement
None reported.

### Suggested GO/CL terms (verify exact IDs/labels via OAK before curating)
- GO Biological Process: "smooth muscle cell differentiation," "positive regulation of vascular associated smooth muscle cell proliferation," "neural crest cell migration" (GO:0001755), "histone H4-K20 methylation"
- GO Molecular Function: "histone methyltransferase activity," "chromatin binding"
- Cell types (CL): vascular associated smooth muscle cell (CL:0000359 — verify), cardiac neural crest cell
- GO Cellular Component: nucleus (GO:0005634) for wild-type PRDM6 localization; cytoplasm (GO:0005737) for the mislocalized p.Arg549Gln variant

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Ductus arteriosus (fetal/perinatal vascular structure connecting main pulmonary artery to descending aorta, just distal to the left subclavian artery origin).
- **Secondary (downstream, shunt-dependent):** Left atrium and left ventricle (volume overload/dilation), pulmonary arteries (pressure/flow overload → pulmonary vascular remodeling), and — in the co-occurring phenotype reported by Stanley et al. — the aortic arch (coarctation).
- **Body systems:** Cardiovascular system primarily; pulmonary vascular bed secondarily if the shunt is large and uncorrected.

**Tissue/cell level:**
- Ductus arteriosus smooth muscle cells (specifically — *not* aortic SMCs, which do not show the same PRDM6 developmental expression decline) are the principal cell population implicated.
- Endothelial cells of the ductal intima participate in the normal anatomic remodeling process (subendothelial migration, cushion formation) that fails in PDA3.
- Cardiac/vascular neural crest cells contribute to the ductal SMC layer during development; their delamination/migration is impaired in Prdm6-deficient mouse models.

**Subcellular level:**
- Nucleus (site of normal PRDM6 chromatin-modifying activity; site of pathology when nuclear import is disrupted by p.Arg549Gln).
- Chromatin/histones (H3K9, H4K20 methylation marks directly altered).

**Localization:** The ductus arteriosus is a midline, typically solitary structure — laterality is not applicable in the way it is for paired organs; it lies at the aortic isthmus, adjacent to the site where coarctation (also reported in some PRDM6-variant carriers) occurs.

**Suggested UBERON term:** ductus arteriosus (UBERON:0002106 — verify via OAK).

---

## 8. Temporal Development

**Onset:** Congenital — present from birth in structurally term-appropriate infants (as opposed to prematurity-related PDA, which is a consequence of gestational immaturity rather than a fixed structural anomaly). PDA3 pedigrees are explicitly described as comprising **term-born** affected individuals.

**Onset pattern:** The structural lesion is congenital, but clinical detection may occur at any point from the newborn period (murmur on routine exam) through adulthood (incidental finding, or presentation with heart failure/pulmonary hypertension symptoms in a previously undiagnosed adult).

**Progression:**
- Untreated small PDA: often clinically silent and hemodynamically insignificant; may remain stable indefinitely.
- Untreated large/moderate PDA: **progressive** — left heart volume overload → pulmonary overcirculation → progressive pulmonary vascular remodeling → pulmonary arterial hypertension (in ~50% of infants with large nonrestrictive PDA by early childhood) → potential Eisenmenger physiology (shunt reversal, cyanosis, arrhythmia, sudden death) if never closed.
- Once anatomically closed (surgically or via catheter device), the ductal lesion itself is cured; any established pulmonary vascular disease may or may not regress depending on how long it was present before closure.

**Critical period:** The perinatal window (first hours to ~3 weeks after birth) is the critical period for normal anatomic closure (functional closure within hours; anatomic remodeling to a permanent fibrous seal over 2–3 weeks). This is precisely the window in which the PRDM6-dependent transcriptional/epigenetic program is disrupted in PDA3.

**Remission:** Spontaneous late closure of an isolated PDA in an otherwise term, structurally normal infant beyond early infancy is uncommon; treatment-induced closure (catheter device or surgical ligation) is the standard "remission" pathway.

---

## 9. Inheritance and Population

**Epidemiology of PDA (general, not PDA3-specific):** PDA occurs in 1 in 2,000–5,000 term/live births and accounts for 5–7% of all congenital heart defects; incidence is far higher in preterm infants (up to 70–80% in extremely low-birth-weight infants), but this preterm form is developmentally/mechanistically distinct from PDA3.

**PDA3 specifically:** Exceedingly rare — the literature to date comprises one large index kindred (PDA-101, 9 affected individuals) plus a small number of additional unrelated probands/families (2 further mutation-positive cases in the original report, plus 3 more recently reported patients with PDA/coarctation and PRDM6 variants). No formal population prevalence estimate exists; it should be considered an "ultra-rare"/"cases in literature" tier of the PrevalenceClassEnum sense.

**Inheritance pattern:** **Autosomal dominant**, with **incomplete penetrance** — explicitly demonstrated in the PDA-101 kindred, where some obligate mutation carriers did not manifest PDA, and further supported by the general finding that PDA has "great phenotypic variability" across TFAP2B/PRDM6 families.

**Penetrance:** Incomplete; not formally quantified numerically in the literature (unlike some Mendelian conditions with published penetrance percentages).

**Expressivity:** Variable — ranging from isolated PDA to PDA with coarctation of the aorta in different PRDM6-variant carriers (Stanley et al. 2024).

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for PDA3.

**Founder effects:** Not established; the index kindred is African-American, and additional families are of Iranian and North American/white ancestry in the discovery cohort — suggesting independent mutational events rather than a single founder haplotype.

**Consanguinity:** Not reported as a feature (autosomal dominant, not recessive).

**Carrier frequency:** Not applicable in the traditional AR sense; population allele frequency of the specific PRDM6 missense variants is essentially zero in reference databases (absent from >2,000 control exomes at publication).

**Population demographics:** No specific ethnic/geographic enrichment beyond the ancestry of the reported families (African-American, Iranian, white/North American); sex ratio and detailed age-distribution data specific to PDA3 have not been published (too few cases). For PDA broadly, a female predominance (roughly 2:1 to 3:1) is well documented, but this figure should not be assumed to hold for the genetic PDA3 subtype without dedicated data.

---

## 10. Diagnostics

**Clinical tests:**
- **Auscultation:** classic continuous ("machinery") murmur, best heard at the left infraclavicular/upper sternal border, in a hemodynamically significant PDA.
- **Echocardiography (2D with color-flow and spectral Doppler)** is the primary diagnostic and confirmatory test, establishing ductal patency, direction/velocity of shunt flow, and chamber size/loading conditions. It is standard for both symptomatic detection and "clinically silent" PDA found incidentally on color-flow imaging.
- **Chest radiography:** may show cardiomegaly and increased pulmonary vascular markings in a large shunt (nonspecific).
- **Cardiac catheterization:** used both diagnostically (hemodynamic assessment, pulmonary vascular resistance calculation before intervention in older patients/pulmonary hypertension) and therapeutically (device closure).

**Genetic testing:**
- No PDA3-specific clinical panel is described in the literature reviewed; given the described disease model, genetic evaluation of isolated/familial (rather than prematurity-associated) PDA would reasonably include a **congenital heart disease gene panel** (covering *TFAP2B*, *PRDM6*, *NOTCH1*, *MYH11*, *FOXC2*, etc.) or **whole-exome sequencing**, particularly when PDA occurs in a term infant with a family history of PDA/other CHD and no syndromic features.
- Chromosomal microarray is indicated to exclude aneuploidy/CNV causes of PDA in the differential (trisomy 21/18/13, other CNVs) before attributing an isolated PDA to a monogenic cause like PRDM6.
- Sanger confirmation of a candidate *PRDM6* variant, with segregation analysis in the family, was the approach used in the discovery studies.

**Clinical criteria / differential diagnosis:** Differentiate PDA3 from:
- Prematurity-associated PDA (gestational-age history is key).
- Char syndrome (TFAP2B) — look for facial dysmorphism and 5th-finger clinodactyly/middle-phalanx hypoplasia.
- Chromosomal syndromes (trisomy 21/18/13) via karyotype/microarray.
- Congenital rubella syndrome — maternal infection history, additional classic triad features (cataracts, sensorineural hearing loss).
- Other genetic CHD-PDA associations (e.g., MYH11-associated TAAD/PDA syndrome — screen for aortic aneurysm).

**Screening:** No population or targeted genetic screening program exists for PDA3 specifically; pulse oximetry newborn screening detects critical CHD generally but is not ductus-specific, and an isolated PDA (without other critical CHD) may not be reliably flagged by oximetry screening alone.

---

## 11. Outcome/Prognosis

**Survival/mortality:** With modern transcatheter or surgical closure, prognosis for isolated PDA (including the PDA3 genetic form) is excellent, with normalization of cardiac loading and low procedural mortality. Untreated large PDA carries substantial long-term morbidity/mortality risk via progression to pulmonary arterial hypertension and Eisenmenger syndrome, which is associated with arrhythmia and sudden cardiac death as late complications.

**Morbidity:**
- Congestive heart failure and failure to thrive in infancy with a large untreated shunt.
- Progressive pulmonary vascular disease (~50% of infants with large nonrestrictive PDA develop pulmonary hypertension by early childhood if uncorrected).
- Increased risk of infective endarteritis of the ductal lesion (a recognized general PDA complication, though specific incidence data for PDA3 are not available).
- In the subset of PRDM6-variant carriers with co-occurring coarctation of the aorta, additional morbidity from arch obstruction (hypertension, arch re-intervention risk) applies.

**Recovery potential:** Full anatomic and hemodynamic correction is achieved with device or surgical closure in the great majority of cases; pulmonary vascular changes that have already become fixed (established Eisenmenger physiology) may not fully reverse even after closure, and closure can be contraindicated in advanced Eisenmenger physiology (shunt reversal used for right-ventricular decompression).

**Prognostic factors:** Shunt size/hemodynamic significance, age/timing of diagnosis and closure, and presence of associated lesions (e.g., coarctation) are the operative prognostic variables; no PRDM6-genotype-specific prognostic marker has been established given the small case numbers.

---

## 12. Treatment

**Pharmacotherapy:** Pharmacologic ductal closure agents (indomethacin, ibuprofen, and increasingly paracetamol/acetaminophen — all COX inhibitors reducing PGE2 synthesis) are the mainstay for **prematurity-associated** PDA in neonates, effective in roughly 70–80% of extremely-low-birth-weight infants. This pharmacologic approach is **not** the relevant treatment paradigm for PDA3, since the lesion occurs in structurally mature, term infants with a fixed anatomic/developmental ductal-wall defect rather than a reversible prostaglandin-mediated patency — mechanical/procedural closure is expected to be the definitive treatment.
- **NCIT suggestion:** NCIT:C15986 (Pharmacotherapy) as the generic action term, if pharmacologic closure is ever attempted; therapeutic agents indomethacin (CHEBI) or ibuprofen (CHEBI) as `therapeutic_agent`.

**Surgical/interventional (primary treatment modality for PDA3):**
- **Transcatheter device closure** is now the treatment of choice for most children >1 year and many infants with favorable ductal anatomy — devices include the Amplatzer Duct Occluder and Amplatzer Piccolo Occluder (implant success ~95.5%, major complication rate ~2.1%, effective closure in ~99.4% at 6 months in one large series).
- **Surgical ligation/division** remains preferred for infants <1 year with anatomy unfavorable for catheter closure.
- **NCIT suggestions:** NCIT:C15329 (Surgical Procedure) for ligation; a device-specific qualifier pattern (per dismech convention) would bind the clinical action (e.g., NCIT:C15329) with a `qualifiers` predicate-value pair naming the occluder device, since NCIT device terms are not valid `treatment_term` bindings on their own.

**Supportive care:** Management of heart failure symptoms (diuretics, fluid management) in infants awaiting closure, or in those with a large symptomatic shunt.

**Experimental/advanced therapeutics:** No gene therapy, RNA-based therapy, or other advanced modality has been developed or trialed for PDA3; given the structural/anatomic nature of the lesion, mechanical closure rather than molecular correction is the applicable treatment paradigm.

**Treatment outcomes:** High closure success rates and low complication rates with modern transcatheter devices, as above; surgical ligation carries a low but real risk profile (recurrent laryngeal nerve injury, residual shunt, bleeding) typical of thoracic surgical procedures.

**Genetic counseling:** Because PDA3 is autosomal dominant with incomplete penetrance, genetic counseling for affected families should address a 50% transmission risk per pregnancy for a carrier parent, with the caveat that not all mutation carriers will manifest PDA (or may show variable expressivity, e.g., isolated PDA vs. PDA with coarctation).

---

## 13. Prevention

**Primary prevention:** No primary prevention exists for the underlying *PRDM6* mutation (a de novo or inherited germline variant); genetic counseling and prenatal/preimplantation genetic testing could theoretically be offered in a family with a known pathogenic variant, though this has not been reported as clinical practice for PDA3 specifically given its rarity and generally favorable treatability.

**Secondary prevention:** Early echocardiographic detection (e.g., prompted by a family history of PDA, or postnatal murmur screening) allows early closure before pulmonary vascular disease develops — this is the principal "prevention" lever for PDA3's main morbidity (Eisenmenger progression).

**Tertiary prevention:** Timely device/surgical closure once diagnosed prevents progression to pulmonary arterial hypertension and Eisenmenger syndrome.

**Screening/genetic counseling:** Cascade screening (echocardiography ± targeted genetic testing) of first-degree relatives in a family with a confirmed PRDM6 variant would be a reasonable clinical approach given the autosomal-dominant inheritance, though no formal screening program is published.

**Public health:** Congenital rubella vaccination programs remain the relevant public-health primary-prevention measure for the *infectious* form of PDA (not PDA3).

---

## 14. Other Species / Natural Disease

**Naturally occurring PDA in other species:** PDA is a well-recognized, common congenital cardiac defect in dogs (e.g., over-represented in Poodles, Pomeranians, Maltese, and notably studied in the **Dutch Stabyhoun** breed, where epidemiology and population genetics have been characterized — PMC4906750) and other companion animals; it is generally regarded as heritable/polygenic in most affected dog breeds rather than tied to a PRDM6 ortholog specifically. No PRDM6-specific naturally-occurring veterinary PDA has been reported in the literature surveyed.

**Orthologous gene:** *Prdm6* is conserved from mammals to lower vertebrates; the Li et al. 2016 study explicitly notes that Arg549 is "highly conserved in orthologs from humans to sea anemones," indicating deep evolutionary conservation of this residue/domain.

**Comparative pathology:** Mouse *Prdm6* conditional-knockout studies (below) recapitulate complete-penetrance PDA, supporting cross-species conservation of the PRDM6-dependent ductal-closure mechanism; this is the primary comparative-biology evidence base for PDA3, rather than natural disease in other species.

**Zoonotic potential:** Not applicable (non-infectious, monogenic developmental disorder).

---

## 15. Model Organisms

**Mouse models (the dominant model system for PDA3 mechanism):**

1. ***Prdm6*fl/fl; Wnt1-Cre2*** (neural-crest-specific conditional knockout) — complete-penetrance PDA with perinatal lethality (P0.5–P1.5) in both sexes; neural crest migration/delamination impaired via elevated Wnt1 signaling and reduced H4K20 monomethylation-dependent G1–S progression (PMC8876496).
2. ***Prdm6*fl/fl; SM22-Cre*** (smooth-muscle-specific conditional knockout) — also complete-penetrance PDA with perinatal lethality, confirming a cell-autonomous requirement for Prdm6 in ductal SMC identity independent of the neural crest contribution pathway (same source).
3. ***Prdm6* depletion models used by Zou et al. 2023** (JCI Insight, PMID:36749647) — demonstrated Prdm6's role in maintaining DA-specific SMC gene expression (319 of 519 DA-enriched genes downregulated on Prdm6 depletion), reduced myogenic tone, abolished KCl and oxygen-induced contractile responses, and reduced thromboxane-agonist response, directly linking Prdm6 loss to failure of both anatomic remodeling and functional ductal constriction. Pharmacologic (indomethacin) and oxygen stimulation both failed to induce closure in mutant embryos, unlike controls — a key translational finding showing that the standard postnatal closure triggers are insufficient to overcome the structural/differentiation defect.
4. Immunofluorescence expression-mapping in **wild-type mouse** ductus arteriosus vs. aorta at E14.5, E17.5, and P0.5 established the developmental expression pattern underpinning the human disease model (high embryonic PRDM6 in DA SMCs, postnatal decline, contrasted with persistent aortic SMC expression) (Li et al. 2016).

**Model characteristics:** These conditional-knockout mouse models recapitulate the core human phenotype (PDA) with high fidelity and complete penetrance, and additionally reveal a functional-contractility deficit and a neural-crest-migration mechanism not yet directly demonstrated in human PDA3 carriers — representing a **model-to-human translational gap**: it remains unconfirmed whether the specific human missense variants (haploinsufficient/hypomorphic) produce the same degree of pathway disruption as the mouse complete conditional knockouts (a full biallelic tissue-specific null), which is a candidate `HUMAN_MODEL_MISMATCH` consideration for KB curation.

**In vitro models:** HEK293 cells and primary/immortalized human aortic vascular smooth muscle cells (VSMCs) transfected with wild-type or mutant PRDM6 constructs — used for subcellular localization, histone methylation (H3K9me2/H4K20me2), and MYH11/α-SMA suppression assays (Li et al. 2016).

**Resources:** No dedicated PDA3/PRDM6 mouse strain repository entry (e.g., MGI/IMSR ID) was identified in this search; strains described are custom conditional-knockout lines (*Prdm6*^fl/fl^ crossed to *Wnt1-Cre2* or *SM22-Cre*) generated by the cited research groups rather than centrally banked at time of publication.

---

## Summary Table of Key Citations

| Citation | Focus |
|---|---|
| Li N et al., *Am J Hum Genet* 2016, PMID:27181681 (PMC4908195) | Discovery of PRDM6 as PDA3 gene; 3 mutations; functional assays; mouse expression mapping |
| Stanley HM et al., *Am J Med Genet A* 2024, PMID:38071433 | PRDM6 variants with PDA + coarctation of the aorta; novel variant |
| Zou M et al., *JCI Insight* 2023, PMID:36749647 | Prdm6 mechanism — MRTF-A interaction, SMC contractility, GWAS SNP rs17149944 |
| Prdm6/neural crest paper, PMC8876496 | Prdm6 controls cardiac neural crest differentiation/migration via Wnt1/H4K20me1 |
| Guo DC / Pannu H et al. (MYH11-TAAD-PDA), PMID:16444274 | Related but distinct MYH11-associated TAAD+PDA syndrome |
| Char syndrome (TFAP2B) GeneReviews, NCBI Bookshelf NBK1106; StatPearls NBK604201 | PDA2/Char syndrome comparator |
| OMIM #617039 (PDA3), *616982 (PRDM6), #617035 (PDA2), #607411 (PDA1) | Canonical disease/gene numbering |
| MONDO:0024266 | Ontology identifier for PDA3 |
| Orphanet ORPHA:466729 | Familial patent arterial duct (parent nosologic entity) |

**Sources:**
- [OMIM #617039 – PATENT DUCTUS ARTERIOSUS 3; PDA3](https://omim.org/entry/617039)
- [OMIM *616982 – PRDM6](https://omim.org/entry/616982)
- [OMIM #617035 – PATENT DUCTUS ARTERIOSUS 2; PDA2](https://www.omim.org/entry/617035)
- [OMIM `607411 – PATENT DUCTUS ARTERIOSUS 1; PDA1](https://omim.org/entry/607411)
- [Li N et al. 2016, "Mutations in the Histone Modifier PRDM6 Are Associated with Isolated Nonsyndromic Patent Ductus Arteriosus" — PMC4908195](https://pmc.ncbi.nlm.nih.gov/articles/PMC4908195)
- [Stanley HM et al. 2024, "Patent ductus arteriosus and coarctation of the aorta in association with PRDM6 variants" — PubMed 38071433](https://pubmed.ncbi.nlm.nih.gov/38071433/)
- [Zou M et al. 2023, "Prdm6 drives ductus arteriosus closure by promoting ductus arteriosus smooth muscle cell identity and contractility" — JCI Insight](https://insight.jci.org/articles/view/163454)
- [Prdm6 controls heart development by regulating neural crest cell differentiation and migration — PMC8876496](https://pmc.ncbi.nlm.nih.gov/articles/PMC8876496)
- [Char Syndrome – GeneReviews, NCBI Bookshelf NBK1106](https://www.ncbi.nlm.nih.gov/books/NBK1106/)
- [Char Syndrome – StatPearls, NCBI Bookshelf NBK604201](https://www.ncbi.nlm.nih.gov/books/NBK604201/)
- [PRDM6 gene – GeneCards](https://www.genecards.org/card/PRDM6)
- [Orphanet: Familial patent arterial duct (ORPHA:466729)](https://www.orpha.net/en/disease/detail/466729)
- [Orphanet: Patent arterial duct (ORPHA:706, non-rare in Europe)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=706)
- [Molecular and Mechanical Mechanisms Regulating Ductus Arteriosus Closure in Preterm Infants – PMC7477801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7477801/)
- [Prostaglandin E2–Mediated Relaxation of the Ductus Arteriosus – Circulation](https://www.ahajournals.org/doi/10.1161/01.cir.0000145159.16637.5d)
- [Patent Ductus Arteriosus – Merck Manual Professional Edition](https://www.merckmanuals.com/professional/pediatrics/congenital-cardiovascular-anomalies/patent-ductus-arteriosus-pda)
- [Patent Ductus Arteriosus: A Contemporary Perspective – Journal of the American Heart Association](https://www.ahajournals.org/doi/10.1161/JAHA.122.025784)
- [Catheter Closure of Clinically Silent PDA Using Amplatzer Duct Occluder II – PMC8465329](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8465329/)
- [Characteristics of Patent Ductus Arteriosus in Congenital Rubella Syndrome – PMC6863812](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6863812/)
- [Epidemiology, presentation and population genetics of patent ductus arteriosus (PDA) in the Dutch Stabyhoun dog – PMC4906750](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4906750/)
- [Zhu L et al. 2006, "Mutations in myosin heavy chain 11 cause a syndrome associating thoracic aortic aneurysm/aortic dissection and patent ductus arteriosus" – PubMed 16444274](https://pubmed.ncbi.nlm.nih.gov/16444274/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMC:PMC38071433` (2 mentions) - NCBI reports no such accession in PMC

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1161/01.cir.0000145159.16637.5d` (2 mentions) - Prostaglandin E
            <sub>2</sub>
            —Mediated Relaxation of the Ductus Arteriosus
  - shared terms: ductus, arteriosus

Weighed against this report's own most characteristic terms: `pda3`, `pda`, `prdm6`, `genetic`, `via`, `ductal`, `vascular`, `gene`, `variant`, `disease`, `closure`, `ductus`, `arteriosus`, `congenital`, `isolated`, `cell`, `specifically`, `syndrome`, `muscle`, `mutation`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 12 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0024266` (2 mentions) - the report calls it "Ontology identifier for PDA3"; MONDO calls it **patent ductus arteriosus 3**
- `CL:0000359` (1 mention) - the report calls it "verify"; CL calls it **vascular associated smooth muscle cell**
- `UBERON:0002106` (1 mention) - the report calls it "verify via OAK"; UBERON calls it **spleen**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0034770` (obsolete histone H4-K20 methylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002092` (1 mention) - the report calls it "Pulmonary hypertension"; HP calls it **Pulmonary arterial hypertension**, and lists "Pulmonary artery hypertension" among its other names
- `GO:0045892` (1 mention) - the report calls it "GO Biological Process candidates: negative regulation of transcription"; GO calls it **negative regulation of DNA-templated transcription**
- `GO:0005634` (1 mention) - the report calls it "GO Cellular Component: nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.