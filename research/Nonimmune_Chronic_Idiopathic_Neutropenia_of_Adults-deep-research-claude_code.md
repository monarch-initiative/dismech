---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-11T12:56:39.368987'
end_time: '2026-09-11T13:01:53.004068'
duration_seconds: 313.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nonimmune Chronic Idiopathic Neutropenia of Adults
  mondo_id: MONDO:0011922
  category: Complex
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
  num_turns: 30
  total_cost_usd: 1.5568651999999996
  session_id: 30472749-cc0b-5982-8425-d65a5081b928
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: perplexity
provider_attempts:
- provider: perplexity
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0100279
    reported_labels:
    - Recurrent aphthous stomatitis
    ontology_label: Ulcerative colitis
  - term_id: GO:0030851
    reported_labels:
    - Impaired granulocyte colony formation / granulocytopoiesis
    ontology_label: granulocyte differentiation
  - term_id: UBERON:0000178
    reported_labels:
    - Secondary/peripheral:** peripheral blood
    ontology_label: blood
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nonimmune Chronic Idiopathic Neutropenia of Adults
- **MONDO ID:** MONDO:0011922 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Nonimmune Chronic Idiopathic Neutropenia of Adults** covering all of the
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

I have sufficient material now. I'll compile the comprehensive research report.

I now have enough primary-literature coverage to compile the full report.

---

# Nonimmune Chronic Idiopathic Neutropenia of Adults — Comprehensive Research Report

## 1. Disease Information

### Overview and terminology (a critical naming caveat)

"Nonimmune Chronic Idiopathic Neutropenia of Adults" (NI‑CINA) names **two overlapping but distinct concepts in the literature**, and curators should be careful not to conflate them:

1. **OMIM #607847 "NEUTROPENIA, NONIMMUNE CHRONIC IDIOPATHIC, OF ADULTS"** — a specific, rare, **autosomal dominant Mendelian entity** caused by a heterozygous missense mutation (N382S) in **GFI1** (Growth Factor Independent 1 transcriptional repressor), reported in a single large multigenerational kindred by Person et al. (2003) ([Nature Genetics](https://www.nature.com/articles/ng1170); [PubMed 12778173](https://pubmed.ncbi.nlm.nih.gov/12778173/?dopt=Abstract)). This is the entity MONDO:0011922 formally maps to.
2. **"Chronic Idiopathic Neutropenia" (CIN) as a clinical syndrome** — a much more commonly described, **acquired, adult-onset, immune-microenvironment-mediated** neutropenia (Papadaki and colleagues, University of Crete, and others), affecting a substantial minority of the general adult population, with no identified monogenic cause in the vast majority of cases. Confusingly, despite the "nonimmune" label, contemporary mechanistic work (see §6) shows this syndrome is driven by **local bone-marrow T-lymphocyte/cytokine-mediated immune suppression of granulopoiesis** — it is "nonimmune" only in the narrower sense of lacking demonstrable anti-neutrophil autoantibodies against circulating/mature neutrophils, distinguishing it from classic autoimmune neutropenia (AIN).

Most of the epidemiological, mechanistic, natural-history, and treatment literature available (and cited below) is about sense 2 (the clinical syndrome), because the GFI1 kindred (sense 1) is a single reported family. A curator populating a KB entry under MONDO:0011922 should decide explicitly whether the entry models the GFI1 monogenic disorder, the broader acquired clinical syndrome, or both with clear differentiation — this is a genuine lump/split judgment call, not a research gap that more literature searching will resolve.

### Key identifiers
- **MONDO:** 0011922
- **OMIM:** #607847 ([omim.org/entry/607847](https://omim.org/entry/607847))
- **Orphanet:** ORPHA:2688 ([orpha.net/en/disease/detail/2688](https://www.orpha.net/en/disease/detail/2688))
- **GARD (NIH):** Disease ID 16605
- **ICD-10-CM:** D70.8 (Other neutropenia) is the most specific code for a defined idiopathic/chronic neutropenia; D70.9 (Neutropenia, unspecified) is used when no further specification is coded ([icd10data.com D70](https://www.icd10data.com/ICD10CM/Codes/D50-D89/D70-D77/D70-))
- **Causal gene (GFI1-associated form):** GFI1, HGNC:4238, OMIM *600871

### Synonyms
- NI-CINA
- Adult idiopathic neutropenia
- Chronic idiopathic neutropenia (CIN) of adults
- Chronic benign neutropenia of adults (used loosely, though CIN is not formally classified as "benign" congenital neutropenia)

### Source of information
Nearly all clinical and mechanistic data derive from **aggregated disease-level cohort studies and case series** (notably a multi-decade Cretan cohort under H. A. Papadaki, and a recent French prospective CYTOPAN study, NCT05931718), not individual EHR mining. The Person et al. 2003 genetic report derives from a **single multigenerational pedigree**.

---

## 2. Etiology

### Disease causal factors
- **GFI1-associated monogenic form (OMIM #607847):** heterozygous **GFI1 c.1145A>G (p.Asn382Ser, N382S)** mutation, autosomal dominant, reported in one large kindred with variably mild-to-moderate neutropenia across generations (Person et al. 2003, *Nat Genet* 33:373-377, [PMID 12778173](https://pubmed.ncbi.nlm.nih.gov/12778173/?dopt=Abstract)). N382S disrupts GFI1's zinc-finger DNA-binding domain, producing a **dominant-negative** effect on GFI1 target-gene repression.
- **Sporadic/acquired CIN (the more common syndrome):** cause remains formally "idiopathic" — no infectious, drug, autoimmune-systemic, or malignant etiology is identifiable. Emerging evidence (see §6) implicates a **chronic, low-grade, polyclonal T-lymphocyte-driven inflammatory bone-marrow microenvironment**, not a primary marrow stem-cell defect.
- A recent whole-exome sequencing comparison of pediatric non-remitting neutropenia vs. adult CIN (Genetic Landscape study, [PMID 40725177](https://pmc.ncbi.nlm.nih.gov/articles/PMC12295308/), 2025) found candidate rare variants in *SPINK5*, *BRCA1*, *RELA*, and *CARD11* in individual cases, and enrichment of rare variants in *PTPN22*, *PSMB9*, and *MYOF*, implicating **innate/adaptive immune-regulatory pathways** rather than a shared monogenic cause; pediatric and adult cohorts shared no common causal variants, supporting a **polygenic/complex** rather than Mendelian model for most adult CIN.

### Risk factors

**Genetic:**
- Heterozygous **GFI1 N382S** (family-specific; autosomal dominant) for the OMIM entity.
- **HLA class II susceptibility:** increased frequency of **HLA-DRB1\*1302** haplotype reported in NI-CINA patients (Papadaki et al., *Blood* 97:580, [ashpublications.org/blood/article/97/2/580](https://ashpublications.org/blood/article/97/2/580/52820/Increased-frequency-of-HLA-DRB1-1302-haplotype-in)) — evidence of an immunogenetic (HLA class II) predisposition to the acquired syndrome.
- **Age-related clonal hematopoiesis (CHIP):** somatic mutations in **DNMT3A, TET2, IDH1/2**, RNA-splicing genes (**SRSF2, ZRSR2**), and an **ETV6-CHIC2** rearrangement detected in ~19% of tested CIN patients, strongly age-associated (median 68 vs. 51 years in mutated vs. non-mutated, p=0.002) ([Scientific Reports 2024, PMID via PMC11412994](https://pmc.ncbi.nlm.nih.gov/articles/PMC11412994/)). TET2 mutations specifically carry a modest independent neutropenic effect (~9%, p=0.012) in general CHIP cohorts.

**Environmental/demographic:**
- **Sex:** strong female predominance (women:men ≈ 3:2 to as high as 77% female in the largest prospective cohort).
- **Age:** typically diagnosed in adulthood; roughly two-thirds of cases occur between ages 30–59, though the largest reclassification cohort (n=266) spanned ages 19–92 (median 61).
- **Ancestry:** baseline population prevalence differs by ancestry group for "benign ethnic neutropenia," a condition that must be excluded (see Diagnostics); this is now formally reclassified as **ADAN** (absolute neutrophil count [ANC] Duffy-Associated Neutropenia) in the newest nosology, not part of true CIN.

### Protective factors
No specific genetic or environmental protective factors have been established in the literature for this condition; it is not modeled as a disease with known protective alleles or exposures.

### Gene-environment interactions
Not characterized specifically for CIN; the leading model is intrinsic bone-marrow immune dysregulation (HLA-linked genetic susceptibility interacting with an unidentified triggering low-grade inflammatory process) rather than a defined exogenous exposure interacting with genotype.

---

## 3. Phenotypes

### Core hematologic finding
- **Chronic neutropenia**, defined by most recent series as **ANC persistently <1.5 × 10⁹/L on ≥3 occasions over ≥3 months** (some define using a lower ULN cutoff, e.g., <1.8 ×10⁹/L, adjusted for ancestry to exclude ADAN/benign ethnic neutropenia).
  - Suggested HPO term: **HP:0001875 (Neutropenia)**
  - Severity distribution (French CYTOPAN cohort, n=131): median ANC 0.8 ×10⁹/L; moderate (<1×10⁹/L) in 39%; severe (<0.5×10⁹/L) in 24% ([PMC11412994](https://pmc.ncbi.nlm.nih.gov/articles/PMC11412994/)).
  - Onset: adult-onset (median age 55–61 years across cohorts), though can be diagnosed earlier.
  - Course: chronic, typically **stable/non-progressive**; a subset show spontaneous partial recovery.

### Mucocutaneous/oral phenotypes
- **Recurrent aphthous stomatitis** — frequent, characteristic feature. HPO: **HP:0100279 (Recurrent aphthous stomatitis)**.
- **Exaggerated/severe gingivitis, aggressive periodontitis**, premature exfoliation of primary dentition (pediatric-onset overlap syndromes). HPO: **HP:0000230 (Gingivitis)**.
- **Recurrent mild bacterial infections** (skin, upper respiratory, oral) — generally **not life-threatening**. HPO candidate: **HP:0002718 (Recurrent infections)**.

### Immunologic/laboratory phenotypes
- Increased proportions of activated bone-marrow T-lymphocytes (HLA-DR+, CD25+, CD38+, CD69+, Fas+).
- Immunoglobulin disturbances, lymphopenia, reduced memory B cells.
- Altered monocyte subsets (Bizymi et al., [PMC6863791](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6863791/)).
- Anti-neutrophil autoantibodies: positive in a substantial minority when tested (56% in one cohort) — presence does **not** correlate with distinct clinical severity or prognosis, undermining the traditional CIN-vs-AIN dichotomy.
- Splenomegaly (~8%) and lymphadenopathy (~5%) in a minority.
- Autoimmune comorbidities (thyroiditis, Sjögren's syndrome) in ~31% of one cohort — raising the question of whether "isolated" CIN and organ-specific autoimmunity share a predisposing immunogenetic background.

### Frequency/severity table (from the largest prospective natural-history cohort, n=131, [PMC11412994](https://pmc.ncbi.nlm.nih.gov/articles/PMC11412994/))

| Feature | Frequency |
|---|---|
| Moderate neutropenia (<1×10⁹/L) | 39% |
| Severe neutropenia (<0.5×10⁹/L) | 24% |
| Anti-neutrophil autoantibody positive | 56% (57/102 tested) |
| Autoimmune comorbidity | 31% |
| Splenomegaly | 8% |
| Lymphadenopathy | 5% |
| Grade >1 infection pre-enrollment | 26% |
| Grade >1 infection during 3-yr follow-up | 28% (0.09/person-year) |
| Grade ≥3 infection during follow-up | 10% |

### Quality of life
No dedicated disease-specific QoL instrument identified in the literature; general infection burden is low, and the largest natural history study explicitly characterizes the condition as **benign** with minimal life impact for most patients, aside from anxiety related to chronic laboratory abnormality and periodic hematologic surveillance.

---

## 4. Genetic/Molecular Information

### Causal gene (Mendelian form)
- **GFI1** (Growth Factor Independent 1 transcriptional repressor), HGNC:4238, chromosome 1p22.
- **Variant:** c.1145A>G, p.Asn382Ser (N382S), heterozygous, missense, located in the C-terminal zinc-finger DNA-binding domain.
- **Classification:** dominant-negative; disrupts GFI1 DNA binding.
- **Mechanism:** GFI1 normally **represses transcription of ELANE (ELA2, neutrophil elastase)**. The N382S mutant fails to repress ELANE, and quantitative RT-PCR showed **elevated ELA2 expression** in myeloid colonies from an affected family member vs. an unaffected relative — mechanistically linking GFI1 and ELANE (the gene mutated in classic severe congenital neutropenia / ELANE-related neutropenia) in a shared pathway ([Person et al. 2003, Nature Genetics](https://www.nature.com/articles/ng1170)).
- Functional studies in murine systems confirm that GFI1 disease mutations produce a **dominant-negative block to granulopoiesis** via murine colony-stimulating factor–responsive assays ([PMID 18328744](https://pubmed.ncbi.nlm.nih.gov/18328744/)).

### Somatic/clonal findings in the acquired syndrome
- Clonal hematopoiesis detected in ~19% of a genotyped cohort (n=36): **DNMT3A, TET2, IDH1, and an ETV6-CHIC2 rearrangement**, VAF range 4.6–18.8%.
- Longitudinal studies show these clones are generally **stable** over time with limited VAF expansion ([P836 abstract, PMC9430755](https://pmc.ncbi.nlm.nih.gov/articles/PMC9430755/)).
- Clonal hematopoiesis (CH) confers markedly increased **relative risk (RR ≈ 31.24)** for progression to overt MDS/AML compared with non-clonal CIN, particularly with **IDH1/2**, splicing-gene (**SRSF2, ZRSR2**), or combined age-related CH gene mutations, and when **VAF >10%**.
- No progression to myeloid neoplasm was observed during the follow-up period of the largest prospective natural history study, despite the presence of clonal mutations — underscoring that CH in this context is a **risk marker requiring surveillance**, not a diagnostic pivot to malignancy at baseline.
- No shared causal genetic variant was found between pediatric non-remitting neutropenia and adult CIN in a comparative WES study, and candidate immune-regulatory gene variants (*SPINK5, BRCA1, RELA, CARD11, PTPN22, PSMB9, MYOF*) were individually rare, supporting complex/polygenic rather than monogenic causation for most adult CIN ([PMID 40725177](https://pmc.ncbi.nlm.nih.gov/articles/PMC12295308/)).

### Allele frequency / population genetics
No population allele-frequency data are available for the GFI1 N382S variant beyond the single reported kindred (not present in large population databases such as gnomAD, consistent with a private, family-specific variant).

### Epigenetic information
- **Abnormal, age-inappropriate telomere shortening** of peripheral-blood mononuclear cells and granulocytes has been demonstrated in CIN patients, with significantly lower telomerase activity frequency vs. controls, and granulocyte telomere length correlating with ANC (Pavlaki et al. 2012, *Haematologica* 97:743-750, [PMC3342978](https://pmc.ncbi.nlm.nih.gov/articles/PMC3342978/)). This suggests replicative/senescence stress on the granulocytic compartment, likely secondary to chronic immune-mediated marrow suppression rather than a primary telomere-biology disorder.

---

## 5. Environmental Information

No specific toxin, occupational, radiation, or infectious agent has been established as causal for CIN; by definition, secondary causes (drugs, infections, known autoimmune/rheumatologic disease, malignancy) are excluded prior to diagnosis. Environmental/lifestyle contributions are not characterized in the literature reviewed; this remains an area without mechanistic data (a legitimate knowledge gap to record rather than a search failure).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (acquired/sporadic CIN — the dominant mechanistic model)

1. An **HLA class II-linked immunogenetic predisposition** (notably increased frequency of HLA-DRB1\*1302) *predisposes to* an unidentified triggering process that establishes a **localized, low-grade chronic inflammatory reaction within the bone-marrow microenvironment** — inferred from HLA association studies rather than directly observed at the trigger step.
2. This inflammatory state *leads to* **activation and clonal/oligoclonal expansion of CD3+ T-lymphocytes within the bone marrow**, marked by increased HLA-DR+, CD25+, CD38+, CD69+, and Fas+ expression on the T-cell fraction (demonstrated directly by immunophenotyping of marrow aspirates).
3. Activated marrow T-lymphocytes (not CD14+ monocyte/macrophages) *produce* **myelosuppressive cytokines** — IFN-γ, Fas-ligand, TNF-α (and soluble TNF-RI), IL-1β, IL-6, IL-8, RANTES/CCL5, and TGF-β1 — demonstrated by cytokine profiling of bone-marrow stromal/mononuclear supernatants, with levels correlating with neutropenia severity.
4. These cytokines *result in* **Fas-mediated apoptosis of CD34+/CD33+ myeloid progenitor cells**, evidenced by a low percentage of CD34+/CD33+ cells associated with accelerated apoptosis and Fas overexpression in that compartment, and by an inverse correlation between bone-marrow stromal TNF-α production and progenitor cell numbers (directly demonstrated: Papadaki et al., *Blood* 101:2591-2600, [PMID 12517813](https://ashpublications.org/blood/article/101/7/2591/106700/Impaired-granulocytopoiesis-in-patients-with)).
5. Accelerated progenitor apoptosis *causes* **impaired granulocytopoiesis** — reduced myeloid colony formation in vitro and (in a subset) a **late maturation-arrest** pattern on bone-marrow morphology, though whether the arrest reflects a genuine terminal differentiation block or increased peripheral release of mature cells from marrow remains unresolved (inferred/uncertain, per the largest series' own characterization).
6. Chronically stressed, apoptosis-prone granulocytic precursors *show* **premature replicative senescence**, reflected in abnormal telomere shortening and reduced telomerase activity of granulocytes, correlating with ANC — a downstream cellular consequence rather than an independent causal branch.
7. The net effect *manifests clinically* as **persistent peripheral neutropenia** with recurrent mild mucosal/bacterial infections and aphthous stomatitis.
8. **Branch — clonal hematopoiesis overlay:** in a subset of (typically older) patients, age-related somatic mutations (DNMT3A, TET2, IDH1/2, splicing genes) arise independently in hematopoietic stem/progenitor cells within this chronically stressed, cytokine-rich marrow niche; most clones remain stable, but higher-risk mutations (IDH1/2, spliceosome genes, VAF >10%) *predispose to* eventual clonal evolution toward MDS/AML — a distinct, age-dependent risk pathway layered on top of the primary immune-mediated mechanism rather than its direct consequence.

**GFI1-associated (Mendelian) branch, mechanistically distinct:** heterozygous dominant-negative GFI1 N382S *impairs* GFI1's transcriptional repression of its target genes, in particular *derepressing* **ELANE (neutrophil elastase)** expression in myeloid progenitors, which *disrupts* normal granulocytic differentiation — paralleling (but molecularly distinct from) the ELANE-mutant mechanism of classic severe congenital neutropenia. Murine Gfi1-null models independently confirm that loss of Gfi1 function **blocks granulocytic maturation**, causing accumulation of an atypical immature myelomonocytic population, severe neutropenia, and relative monocytosis.

### Molecular pathways
- **GFI1 → ELANE repression axis** (GFI1 as an upstream transcriptional repressor of neutrophil elastase; suggested GO term: **GO:0030851, granulocyte differentiation**; also **GO:0045892, negative regulation of DNA-templated transcription**).
- **Fas/FasL apoptotic signaling** in myeloid progenitors (GO:0007165 signal transduction; GO:0006915 apoptotic process; GO:0036462 TRAIL-activated apoptotic signaling pathway is a related but not identical pathway — Fas pathway is more precisely GO:0097191, extrinsic apoptotic signaling pathway).
- **TNF-α / TNFR1 signaling** suppressing granulopoiesis.
- **IFN-γ–JAK/STAT signaling** in the marrow T-cell compartment.

### Cellular processes
- Increased apoptosis of CD34+/CD33+ myeloid progenitors (GO:0006915 apoptotic process; GO:0043069 negative regulation of programmed cell death is inversely relevant).
- T-lymphocyte activation (GO:0042110 T cell activation).
- Impaired granulocyte colony formation / granulocytopoiesis (GO:0030851).
- Cellular senescence of the granulocytic lineage, reflected by telomere attrition (GO:0090399 replicative senescence).

### Protein dysfunction
- GFI1 N382S: loss of normal zinc-finger DNA-binding function → dominant-negative transcriptional dysregulation (loss of repressor activity at target loci, notably ELANE).

### Immune system involvement
Central to the acquired form: bone-marrow-localized T-cell-mediated immune dysregulation causing paracrine myelosuppression (not classic autoantibody-mediated peripheral neutrophil destruction, which instead characterizes primary autoimmune neutropenia, AIN — a related but formally distinct diagnosis in current nosology).

### Tissue damage mechanisms
Cytokine-driven apoptosis is the principal damage mechanism (no fibrosis or necrosis reported as primary features; marrow fibrosis grade MF-1/2 was noted incidentally in 16% of one large cohort but is not considered a defining pathophysiologic feature).

### Molecular profiling
- **Cytokine/transcriptomic profiling** of bone-marrow stromal and mononuclear cell supernatants: elevated IL-1β, IL-6, TGF-β1, IL-8, RANTES/CCL5, TNF-α, sTNF-RI (Papadaki et al., multiple studies).
- **Whole-exome sequencing** in a small comparative cohort (25 subjects total) identified candidate rare variants without a shared adult-cohort signature (PMC12295308).
- **NGS myeloid gene panels** in the largest prospective series (n=36 tested of 266-patient reclassification cohort) identified somatic clonal mutations in 19–7/36 tested patients.

### Suggested ontology terms for pathophysiology curation
- **GO:0030851** granulocyte differentiation
- **GO:0002548** monocyte chemotaxis (context: altered monocyte subsets)
- **GO:0006915** apoptotic process
- **GO:0042110** T cell activation
- **CL:0000094** granulocyte; **CL:0000576** monocyte; **CL:0000084** T cell; **CL:0000838** lineage-negative hematopoietic progenitor cell (myeloid progenitor, CD34+/CD33+)
- **CL:0002191** granulocyte monocyte progenitor cell

---

## 7. Anatomical Structures Affected

- **Primary organ:** **bone marrow** (UBERON:0002371) — site of the T-cell/cytokine-mediated myelosuppression and impaired granulocytopoiesis.
- **Secondary/peripheral:** peripheral blood (UBERON:0000178) — site of the resultant neutropenia; oral mucosa (UBERON:0006920) — site of recurrent aphthous stomatitis and gingivitis; spleen (UBERON:0002106) — mild splenomegaly in a minority.
- **Cellular targets:** myeloid progenitor cells / granulocyte-monocyte progenitors (CD34+/CD33+) in bone marrow; mature circulating neutrophils (target of autoantibodies in the antibody-positive subset); bone-marrow T-lymphocytes (site of aberrant activation, the proximate immune effector).
- **Subcellular:** no specific organelle-level pathology reported; apoptotic (mitochondrial/Fas-extrinsic) pathway activation in progenitor cells is implicated at the biochemical level.
- **Laterality:** not applicable (systemic hematologic disorder).

---

## 8. Temporal Development

- **Onset:** adult-onset by definition; median age at diagnosis 55–61 years across the largest cohorts, though range spans 19–93 years.
- **Onset pattern:** insidious/chronic; typically detected incidentally on routine complete blood count rather than through acute symptomatic presentation.
- **Course:** chronic and generally **stable**, non-progressive in the majority; a subset shows spontaneous partial recovery of ANC over time regardless of anti-neutrophil antibody status.
- **Progression:** low overall rate of clinical worsening; infection frequency does *not* correlate with baseline neutropenia severity, antibody status, or demographics in the largest longitudinal study.
- **Critical branch point:** presence and molecular class of clonal hematopoiesis (IDH1/2, spliceosome genes, VAF>10%) identifies a subset at meaningfully higher risk of eventual clonal evolution to MDS/AML — this is the key prognostic inflection point identified in recent literature, distinguishing "benign stable CIN" from "CIN with high-risk CH" as a quasi-distinct disease trajectory.
- **Remission:** spontaneous, partial ANC normalization reported in some patients over years of follow-up; no treatment-induced remission is described as curative (G-CSF is supportive, not disease-modifying).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** the classic Cretan population screening study found **8.23%** of an apparently healthy adult population fulfilled CIN diagnostic criteria on repeated testing ([Ann Hematol, PMID 10466440](https://pubmed.ncbi.nlm.nih.gov/10466440/)) — a strikingly high figure reflecting broad screening criteria in a specific population, and should be treated cautiously as an upper-bound/local estimate rather than a global prevalence. Some general sources cite population estimates around **1% in White and up to 5% in Black populations** for "idiopathic"/benign neutropenia broadly (note: much of the Black-population estimate reflects **benign ethnic neutropenia / ADAN**, which is now nosologically separated from true CIN in current classification schemes — see §10).
- **Incidence:** not separately reported as an incidence rate; CIN is typically described via point-prevalence in screened or referred cohorts.

### Inheritance (GFI1-associated form)
- **Pattern:** autosomal dominant.
- **Penetrance:** appears high within the reported kindred but severity is variable across generations (variable expressivity).
- **Anticipation, mosaicism, founder effects:** not reported/characterized for this single-family variant.

### Inheritance (sporadic CIN)
- Not Mendelian; **HLA-DRB1\*1302** association indicates a polygenic/immunogenetic susceptibility rather than a single-gene inheritance pattern. A minority of the reclassified large cohort (6.8%) were ultimately characterized as "familial with undefined genetic defect," indicating unresolved heritable components in some cases.

### Population demographics
- **Sex ratio:** strong female predominance, ~3:2 to 77:23 (F:M) across cohorts.
- **Age distribution:** predominantly middle-aged to older adults (median 55–61 years); ~two-thirds of cases aged 30–59 in earlier series.
- **Geographic/ancestry notes:** original large descriptive cohorts are heavily Greek/Cretan (single-center, potential ascertainment bias); newer reclassification work (French CYTOPAN cohort) broadens the geographic base. Ancestry-specific normal ANC ranges (relevant to excluding ADAN/benign ethnic neutropenia, historically overrepresented in individuals of African ancestry) must be applied before diagnosing true CIN.

---

## 10. Diagnostics

### Diagnostic criteria
- ANC persistently <1.5 ×10⁹/L (adjusted for ancestry-specific normal ranges) on **≥3 occasions over a ≥3-month period**, with exclusion of drug-induced, infectious, autoimmune-systemic, congenital, and malignant causes.

### Laboratory tests
- **Serial CBC with differential** to establish chronicity and exclude cyclic neutropenia (which requires serial counts 2–3×/week over 6 weeks to detect ~21-day periodicity).
- **Anti-neutrophil autoantibody testing** (GIFT/GIIFT assays) — recommended in patients with ANC <1×10⁹/L, with re-testing of initially negative results, per current European guidelines cited in the natural-history study.
- **Immunoglobulin levels, ANA, and rheumatologic serologies** to screen for underlying autoimmune disease.

### Bone marrow evaluation
Recommended as part of a "proper" diagnostic workup (per recent guideline-referencing literature): morphology (looking for the late maturation-arrest pattern seen in a subset), flow cytometry, cytogenetics, and immunohistochemistry (IgG/IgM/C3/C4d deposition patterns, reported present in >80% of biopsies in the largest cohort — notably, patients with **negative C3 deposition** had significantly higher baseline ANC, p<0.01).

### Genetic/molecular testing
- **NGS myeloid gene panel** to detect clonal hematopoiesis (DNMT3A, TET2, IDH1/2, ASXL1, splicing genes, ETV6 rearrangements) — recommended especially in older patients, given prognostic implications for MDS/AML risk.
- **Targeted GFI1 (and ELANE) sequencing** should be considered when there is a clear autosomal-dominant family history consistent with the Mendelian entity, or overlapping features with congenital neutropenia.
- Newer **machine-learning-assisted diagnostic/prognostic tools** are emerging from large-cohort reclassification work (Tsaknakis et al., 266-patient cohort, *Blood* 2025) to better stratify patients labeled CIN into true CIN, CCUS, primary AIN, familial undefined, ADAN, secondary neutropenia, and unrecognized severe congenital neutropenia.

### Differential diagnosis (reclassification data from the largest cohort, n=266)

| Final classification | % of cohort |
|---|---|
| True CIN | 66.5% |
| Clonal cytopenia of undetermined significance (CCUS) | 12.8% |
| Primary autoimmune neutropenia (pAIN) | 6.0% |
| Familial, undefined genetic defect | 6.8% |
| ADAN (ethnic neutropenia) | 1.1% |
| Secondary neutropenia | 4.5% |
| Severe congenital neutropenia (previously missed) | 2.2% |

This reclassification data (from [Tsaknakis et al., ASH abstract, *Blood* 2025](https://ashpublications.org/blood/article/146/Supplement%201/623/552667/Novel-diagnostic-and-prognostic-tools-for-patients)) is directly relevant to knowledge-base curation: roughly a **third of patients historically labeled "CIN" carry a more specific diagnosis** on thorough re-evaluation, underscoring that "idiopathic" is a diagnosis of exclusion that shrinks as diagnostic tools improve — a live nosological caveat rather than settled fact.

### Screening
No population-level or newborn screening program exists for CIN; diagnosis is reactive, based on incidental or symptom-triggered CBC abnormalities.

---

## 11. Outcome/Prognosis

- **Mortality:** minimal and not disease-attributable — in the largest prospective cohort (n=131, median 3-year follow-up), only 2 deaths occurred (myocardial infarction, colorectal cancer), unrelated to neutropenia.
- **Malignant transformation:** **zero cases** of evolution to hematologic malignancy in the largest prospective natural-history cohort despite clonal hematopoiesis findings in a subset; however, retrospective/cross-sectional data on clonal-hematopoiesis-positive CIN patients show a substantially elevated relative risk (~31×) for eventual MDS/AML transformation versus non-clonal CIN, particularly with high-risk mutation classes (IDH1/2, spliceosome genes) or VAF >10%.
- **Infection burden:** low; grade ≥3 infections occurred in only 10% of patients over 3-year follow-up, with **no correlation** to neutropenia severity, demographics, or antibody status — an important and somewhat counterintuitive finding, suggesting ANC threshold alone is a poor infection-risk predictor in this specific syndrome (unlike classic congenital/chemotherapy-induced neutropenia).
- **Overall characterization:** the condition is repeatedly described in the primary literature as a **"benign condition without life-threatening infections"** warranting extensive hematologic evaluation (including bone marrow assessment) primarily to inform differential diagnosis and identify the clonal-hematopoiesis-positive subset needing surveillance, rather than because the baseline course itself is dangerous.
- **Prognostic factors:** presence/class of clonal hematopoiesis mutation and VAF; older age (associated with higher CH prevalence); negative marrow C3 deposition (associated with higher baseline ANC, i.e., milder disease).

---

## 12. Treatment

### Pharmacotherapy
- **Granulocyte colony-stimulating factor (G-CSF, filgrastim):** the primary specific pharmacologic intervention, but used **sparingly** in practice — only 4.6% of patients in the largest natural-history cohort received G-CSF, and only 2 patients (of 131) received it chronically, reflecting the generally low infection burden and benign course.
  - Dosing: typically initiated at ~3 μg/kg subcutaneously daily, titrated to a target ANC of 1,500–2,000/μL; patients with cyclic/idiopathic neutropenia generally respond at lower doses than those with congenital neutropenia.
  - Long-term safety: no loss of efficacy with prolonged use reported; long-term G-CSF use does **not** appear to independently increase AML risk in this population, though caution/monitoring is still advised given the theoretical concern (relevant NCIT term: **NCIT:C1177**, Filgrastim; treatment action **NCIT:C15986**, Pharmacotherapy).
- **Corticosteroids/immunosuppressants:** current expert recommendation, per the recent natural-history study, is to **avoid** steroids unless there is a clearly established co-existing autoimmune diagnosis — reflecting the recognition that antibody positivity alone does not warrant immunosuppression given no demonstrated prognostic benefit.
- **Ezatiostat (TLK199)**, a glutathione S-transferase P1-1 inhibitor, has shown case-report efficacy in **G-CSF-resistant idiopathic chronic neutropenia** ([PMC3235963](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3235963/)) — an investigational/off-label approach for refractory cases, not a standard-of-care agent.

### Surgical/interventional
Not applicable as primary therapy; splenectomy is not indicated for isolated CIN (contrasts with some AIN/hypersplenism-associated cytopenias).

### Supportive care
- Dental/oral hygiene surveillance and management of recurrent aphthous stomatitis and gingivitis.
- Antibiotic therapy for documented infections; no evidence supports prophylactic antibiotics in the absence of severe/recurrent infection.

### Experimental
Registered trial: **CYTOPAN (NCT05931718)**, the French prospective observational study underlying much of the modern natural-history and immunohistochemistry data cited above.

### Treatment strategy
Because infection risk correlates poorly with ANC severity in this specific syndrome, treatment is generally **symptom- and infection-triggered rather than ANC-threshold-triggered** — a notable departure from management paradigms for congenital or chemotherapy-induced neutropenia, and a point worth explicit note in a KB `treatments:` block or `notes:`.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies are described in the literature, consistent with CIN's idiopathic/immune-microenvironmental etiology and lack of an identified modifiable environmental trigger. Genetic counseling is relevant only for the rare GFI1-associated autosomal dominant kindred (risk assessment for at-risk relatives, prenatal/preimplantation testing not reported as utilized). No vaccination-based, screening-based, or public-health-level prevention approach applies.

---

## 14. Other Species / Natural Disease

- **Mouse (Mus musculus, NCBITaxon:10090):** *Gfi1*-null mice are severely neutropenic, showing a block in myeloid differentiation with accumulation of an atypical immature myelomonocytic population, absence of mature granulocytes, and relative monocytosis — directly recapitulating the human GFI1-mutant neutropenia phenotype at the level of blocked granulopoiesis (though via null rather than dominant-negative mechanism in most mouse models). Gfi1 knock-in models bearing SCN-associated point mutations further reveal stage-specific Gfi1-dependent checkpoints in myeloid development.
- No naturally occurring veterinary disease analog specific to GFI1-mutant or Papadaki-type immune-mediated adult CIN was identified in this search (distinct from canine cyclic neutropenia/"grey collie syndrome," which is an ELANE-pathway, not GFI1-pathway, disorder and a different clinical entity).
- **Orthologous gene:** murine *Gfi1* (MGI:95662), human GFI1 ortholog, high evolutionary conservation of the zinc-finger repressor domain relevant to the N382S mutation.

---

## 15. Model Organisms

| Model | Type | Genetic modification | Recapitulation | Key resource |
|---|---|---|---|---|
| Mouse (*Gfi1⁻/⁻*) | Genetic knockout | Complete Gfi1 loss | Severe neutropenia, block in granulocytic differentiation, immature myelomonocytic accumulation | MGI |
| Mouse (Gfi1 knock-in, SCN mutations) | Genetic knock-in | Point mutations modeling human SCN-associated GFI1 alleles | Stage-specific block in granulopoiesis; used to dissect differentiation checkpoints | [Blood ASH abstract](https://ashpublications.org/blood/article/130/Supplement%201/544/115632/Severe-Congenital-Neutropenia-Associated-Mutations) |
| Mouse (reduced Gfi1 expression, hypomorphic) | Genetic (dose-dependent) | Partial Gfi1 reduction (not full deficiency) | Distinct from full knockout: causes a **fatal myeloproliferative disease** rather than isolated neutropenia — illustrating that GFI1 dosage, not just presence/absence, determines phenotype ([Leukemia, Nature](https://www.nature.com/articles/s41375-018-0166-1)) |
| Human iPSC/primary CD34+ progenitor cultures | In vitro | Patient-derived or CRISPR-edited GFI1/ELANE variants | Used to demonstrate elevated ELA2 (ELANE) expression consequent to GFI1 N382S | Person et al. 2003 |

**Model limitations:** the complete *Gfi1* knockout is a more severe phenotype than the human heterozygous dominant-negative N382S carrier state (variable, generally milder neutropenia in the reported kindred), and murine models do not capture the T-cell/cytokine-driven immune-microenvironmental mechanism believed to underlie the far more common sporadic/acquired CIN syndrome — there is currently **no established animal model for the acquired, HLA-linked, T-cell-mediated form of adult CIN**, which is a genuine translational gap rather than an unsearched area.

---

## Summary of Key Citations (PMID-first where available)

- Person RE et al. Mutations in proto-oncogene GFI1 cause human neutropenia and target ELA2. *Nat Genet* 2003;33:373-377. [PMID 12778173](https://pubmed.ncbi.nlm.nih.gov/12778173/?dopt=Abstract) / [Nature Genetics](https://www.nature.com/articles/ng1170)
- Papadaki HA et al. Non-immune chronic idiopathic neutropenia of adult: an overview. *Eur J Haematol* 2001;66:1-8. [PMID 11553265](https://pubmed.ncbi.nlm.nih.gov/11553265/)
- Papadaki HA et al. Impaired granulocytopoiesis in patients with chronic idiopathic neutropenia is associated with increased apoptosis of bone marrow myeloid progenitor cells. *Blood* 2003;101:2591-2600. [PMID 12517813](https://ashpublications.org/blood/article/101/7/2591/106700/Impaired-granulocytopoiesis-in-patients-with)
- Papadaki HA et al. Increased frequency of HLA-DRB1*1302 haplotype in patients with nonimmune chronic idiopathic neutropenia of adults. *Blood* 2001;97:580-582. [ashpublications.org](https://ashpublications.org/blood/article/97/2/580/52820/Increased-frequency-of-HLA-DRB1-1302-haplotype-in)
- Pavlaki KI et al. Abnormal telomere shortening of peripheral blood mononuclear cells and granulocytes in patients with chronic idiopathic neutropenia. *Haematologica* 2012;97:743-750. [PMC3342978](https://pmc.ncbi.nlm.nih.gov/articles/PMC3342978/)
- Prevalence of chronic idiopathic neutropenia of adults among an apparently healthy population living on the island of Crete. *Ann Hematol* 1999. [PMID 10466440](https://pubmed.ncbi.nlm.nih.gov/10466440/)
- Natural history of chronic idiopathic neutropenia of the adult. *Sci Rep* 2024. [nature.com/articles/s41598-024-71719-2](https://www.nature.com/articles/s41598-024-71719-2) / [PMC11412994](https://pmc.ncbi.nlm.nih.gov/articles/PMC11412994/)
- Severe chronic primary neutropenia in adults: report on a series of 108 patients. *Blood* 2015;126:1643-1651. [ashpublications.org](https://ashpublications.org/blood/article/126/14/1643/34425/Severe-chronic-primary-neutropenia-in-adults)
- Genetic Landscape of Non-Remitting Neutropenia in Children and Chronic Idiopathic Neutropenia in Adults. 2025. PMID 40725177. [PMC12295308](https://pmc.ncbi.nlm.nih.gov/articles/PMC12295308/)
- Tsaknakis et al. Novel diagnostic and prognostic tools for patients with chronic idiopathic neutropenia: Data on a cohort of 266 patients. *Blood* 2025;146(Suppl 1):623. [ashpublications.org](https://ashpublications.org/blood/article/146/Supplement%201/623/552667/Novel-diagnostic-and-prognostic-tools-for-patients)
- Long-term dynamics of clonal hematopoiesis in chronic idiopathic neutropenia (CIN). [PMC9430755](https://pmc.ncbi.nlm.nih.gov/articles/PMC9430755/)
- Bizymi N et al. Altered Monocyte Subsets in Patients with Chronic Idiopathic Neutropenia. 2019. [PMC6863791](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6863791/)
- Reduced expression but not deficiency of GFI1 causes a fatal myeloproliferative disease in mice. *Leukemia* 2018. [PMC6326955](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326955/)

---

### Curatorial note on gaps and ambiguities (explicitly flagged, not silently omitted)
1. **Scope decision required:** whether the dismech entry under MONDO:0011922 should center on the GFI1 monogenic kindred (matching the strict OMIM title), the broad acquired CIN syndrome (matching nearly all available mechanistic/epidemiologic/treatment literature), or both with clear `has_subtypes` separation — this is a lump/split call, not resolved by further search, and should be checked against `docs/explanation/design-decisions.md` and the granularity conventions before curation begins.
2. **Bone-marrow maturation-arrest pattern:** whether it reflects a true terminal differentiation block or increased marrow release of mature cells is explicitly stated as unresolved in the primary literature — should be modeled as a `HUMAN_MODEL_MISMATCH`/knowledge-gap-flavored uncertainty, not asserted as settled mechanism.
3. **No animal model exists for the T-cell/cytokine-driven acquired form** — only the Mendelian GFI1 form has a validated murine model; this asymmetry should be reflected honestly in any `animal_models:` block.
4. **Prevalence figures are population/cohort-specific** (8.23% Cretan screening cohort vs. more conservative "~1% White/~5% Black" general estimates, the latter partly confounded by ADAN/ethnic-neutropenia inclusion) — a single number should not be asserted without qualifying the source population.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100279` (1 mention) - the report calls it "Recurrent aphthous stomatitis"; HP calls it **Ulcerative colitis**
- `GO:0030851` (3 mentions) - the report calls it "Impaired granulocyte colony formation / granulocytopoiesis"; GO calls it **granulocyte differentiation**
- `UBERON:0000178` (1 mention) - the report calls it "Secondary/peripheral:** peripheral blood"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001875` (1 mention) - the report calls it "Neutropenia"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0002718` (1 mention) - the report calls it "Recurrent infections"; HP calls it **Recurrent bacterial infections**, and lists "Recurrent pyogenic infections" among its other names
- `UBERON:0002371` (1 mention) - the report calls it "bone marrow", "Primary organ:** **bone marrow"; UBERON calls it **bone marrow**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002371` - called "bone marrow", "Primary organ:** **bone marrow"
- `MGI:95662` - called "Gfi1", "Orthologous gene:** murine *Gfi1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.