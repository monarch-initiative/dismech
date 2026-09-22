---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T03:42:59.360949'
end_time: '2026-09-04T03:48:37.006629'
duration_seconds: 337.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: KMT2B-Related Dystonia
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
  num_turns: 20
  total_cost_usd: 1.2686674
  session_id: fda9c4a1-6781-59ef-81f2-a9c8fd6c1932
  stop_reason: end_turn
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
citation_count: 31
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - DOI:10.1186/s13148-021-01145-y
  relevance_assessed: 17
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 37
  not_found: 0
  obsolete: 3
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001608
    reported_labels:
    - Dysphonia
    ontology_label: Abnormality of the voice
  obsolete_terms:
  - term_id: GO:0051568
    ontology_label: obsolete histone H3-K4 methylation
  - term_id: GO:0034968
    ontology_label: obsolete histone lysine methylation
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KMT2B-Related Dystonia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KMT2B-Related Dystonia** covering all of the
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

I'll research KMT2B-Related Dystonia comprehensively using web search tools, then compile the full report.

I have comprehensive data now. Let me do a couple more targeted searches to fill remaining gaps (variant spectrum/hotspots, ClinVar/gnomAD constraint, HPO/GO term suggestions context, and animal models beyond zebrafish) before compiling the final report.

I now have sufficient depth to compile the comprehensive report.

---

# KMT2B-Related Dystonia (DYT-KMT2B / DYT28): Comprehensive Research Report

## 1. Disease Information

### Overview
KMT2B-related dystonia (also designated **DYT-KMT2B**, formerly **DYT28**) is an autosomal dominant, complex, childhood-onset progressive movement disorder caused by heterozygous pathogenic variants in *KMT2B* (Lysine Methyltransferase 2B), which encodes an H3K4 histone methyltransferase. The disorder typically presents with lower-limb dystonia in early-to-mid childhood that progresses in a caudocranial pattern to generalized dystonia with prominent cervical, cranial (oromandibular), and laryngeal involvement, often accompanied by developmental delay, intellectual disability, short stature, and dysmorphic facial features ([GeneReviews, NBK493766](https://www.ncbi.nlm.nih.gov/books/NBK493766/); [Meyer et al. 2017, *Brain*](https://academic.oup.com/brain/article/143/11/3242/5956324)). *KMT2B* pathogenic variants also cause a distinct, non-dystonic **KMT2B-related neurodevelopmental disorder (KMT2B-related NDD)** — together these constitute "KMT2B-related disorders."

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM (gene) | *606834 — KMT2B* |
| OMIM (phenotype) | #617284 — Dystonia 28, Childhood-Onset (DYT28) |
| OMIM (NDD phenotype) | #619934 — Intellectual Developmental Disorder, Autosomal Dominant 68 (MRD68) |
| Orphanet | KMT2B-related dystonia is catalogued in Orphanet's dystonia group (specific ORPHA code not independently confirmed in this search — recommend direct Orphanet lookup) |
| HGNC | KMT2B (formerly *MLL4*, *MLL2* in older nomenclature — note the confusing dual naming with *KMT2D*, which was also called *MLL2*/*MLL4* in some papers) |
| Gene locus | 19q13.12 |
| Historic name | DYT28 |

### Synonyms / Alternative Names
- KMT2B-deficient dystonia
- DYT28
- Complex early-onset dystonia (Zech-type)
- Childhood-onset generalized dystonia due to KMT2B haploinsufficiency
- MLL4-related/MLL2-related dystonia (older literature — nomenclature ambiguity with *KMT2D*)

### Data Source Character
Nearly all available information derives from **aggregated case-series and cohort studies** (not large-scale EHR/claims data), since this is an ultra-rare monogenic disorder. As of the most recent GeneReviews update, approximately **246 individuals from 229 families** with DYT-KMT2B and **27 individuals from 25 families** with KMT2B-related NDD have been reported in the literature ([GeneReviews, NBK493766](https://www.ncbi.nlm.nih.gov/books/NBK493766/)). Largest cohorts include Meyer et al. 2017 (*Brain*, n=53), Zech et al. 2016 (parallel report), and more recent expansion cohorts (e.g., a 2025 *Brain* follow-up cohort and Austrian national cohort, [PMC12926133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12926133/)).

---

## 2. Etiology

### Disease Causal Factors
KMT2B-related dystonia is a **purely monogenic disorder** — there is no polygenic or complex-trait risk architecture. Disease is caused by:
1. **Heterozygous pathogenic single-nucleotide variants or small indels in *KMT2B*** (missense, nonsense, frameshift, splice-site) — accounts for ~88% of affected individuals ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)).
2. **Heterozygous microdeletions of 19q13.11–19q13.12 encompassing *KMT2B*** — accounts for ~12% of cases.

The two founding reports were published in parallel in 2016:
- **Zech et al. 2016** (*Nat Genet* / related) identified protein-truncating *KMT2B* variants causing childhood-onset generalized dystonia, demonstrating that **haploinsufficiency** of KMT2B is sufficient to cause disease.
- **Meyer et al. 2016/2017** (*Nat Genet*; expanded cohort in *Brain* 2017) reported heterozygous *KMT2B* variants (including missense) in 27 unrelated individuals with complex progressive childhood-onset dystonia, often with characteristic facial appearance and MRI findings, "highlighting a clinically recognizable form of dystonia and demonstrat[ing] a crucial role for KMT2B in the physiological control of voluntary movement" ([Nature Genetics, ng.3740](https://www.nature.com/articles/ng.3740)).

### Genetic Risk Factors
- **Causal variant classes**: missense (most common overall), nonsense, splice-site, frameshift indels, and contiguous gene deletions (19q13.11–19q13.12).
- **Mutational hotspot**: a recurrent missense hotspot at **codon 2565** has been described, associated with variable disease severity and expressivity ([Pubmed 39933316](https://pubmed.ncbi.nlm.nih.gov/39933316/)).
- **Domain clustering**: missense variants cluster in putative functional domains (e.g., CXXC-type zinc finger, PHD fingers, SET domain), whereas protein-truncating variants are distributed throughout the gene body — a pattern paralleling the related Wiedemann–Steiner syndrome gene *KMT2A*, where CXXC-domain missense variants are pathogenic and AlphaFold2-classifiable ([PMC9249231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9249231/)). A comparable, though less exhaustively characterized, hotspot pattern has been proposed for KMT2B's CXXC/PHD region.
- No specific gnomAD constraint metrics for *KMT2B* were retrieved in this search, but as a large chromatin-modifier gene causing a dominant haploinsufficiency phenotype, *KMT2B* is expected to show strong loss-of-function intolerance (consistent with other KMT2 family members such as KMT2A, KMT2D, and KMT2E, which show pLI ≈ 1.0). This should be verified directly against gnomAD for a curated entry.
- **Modifier genes**: none specifically established; genotype only weakly predicts phenotype (see Genetics section).

### Environmental Risk Factors
No environmental, toxic, occupational, or infectious risk factors have been identified — this is a fully genetically determined (monogenic) disorder. Age and sex do influence phenotype expression and DBS outcome (see below) but are not causal/risk factors for disease occurrence itself.

### Protective Factors
No genetic or environmental protective factors have been reported. **Reduced penetrance** is documented — asymptomatic heterozygous carriers exist within families, particularly among individuals with the milder/NDD-only phenotype — but no specific protective allele or modifier variant has been characterized.

### Gene-Environment Interactions
None established; not applicable for this monogenic disorder.

---

## 3. Phenotypes

Data below are drawn primarily from the GeneReviews synthesis of cohort studies (Meyer et al., Zech et al., Cif et al., Lange et al.) ([NBK493766](https://www.ncbi.nlm.nih.gov/books/NBK493766/)) and the 2016 founding papers.

### DYT-KMT2B (dystonia phenotype) — represents ~93% of families

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Dystonia (generalized, evolving from focal) | 100% | HP:0001332 (Dystonia); HP:0002340 (Lower limb dystonia — early feature) |
| Laryngeal dysfunction (dysphonia) | ~51% | HP:0001608 (Dysphonia) |
| Intellectual disability | ~42% | HP:0001249 (Intellectual disability) |
| Microcephaly | ~44% | HP:0000252 (Microcephaly) |
| Systemic features (short stature, precocious puberty, hypothyroidism) | ~38% | HP:0004322 (Short stature); HP:0000826 (Precocious puberty); HP:0000821 (Hypothyroidism) |
| Additional movement disorder features (myoclonus, spasticity, tremor, ataxia) | ~27% | HP:0001336 (Myoclonus); HP:0001257 (Spasticity); HP:0001251 (Ataxia) |
| Bulbar/feeding difficulties, dysphagia | ~30% | HP:0002015 (Dysphagia) |
| Neurobehavioral/psychiatric (ADHD 10%, anxiety/OCD 11%, ASD 4%) | ~26% | HP:0007018 (Attention deficit); HP:0000717 (Autism); HP:0000739 (Anxiety) |
| Developmental delay | ~26% | HP:0001263 (Global developmental delay) |
| Eye movement abnormalities | ~8% | HP:0000496 (Abnormal eye movements) |
| Seizures | ~2% | HP:0001250 (Seizure) |
| Facial dysmorphism (elongated face, nasal tip) | not separately quantified but common | HP:0000276 (Long face); HP:0000448 (Prominent nose) |
| Isolated progressive sensorineural hearing loss (subset) | reported in some individuals | HP:0000407 (Sensorineural hearing loss) |

**Onset:** median age of onset **6 years** (range 0–43 years, reflecting the newly recognized adult-onset subgroup) ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)). A recent natural history cohort (n=44) reported median symptom onset of **5.0 years**, with progression to generalized dystonia over a median of **2.0 years** ([2025 Brain cohort, arXiv summary](https://arxiv.org/pdf/2502.06320)).

**Classic disease course:** begins with **lower-limb focal dystonia** — foot deformity (equinovarus), toe-walking, gait disturbance — and evolves in a **caudocranial** pattern into **generalized dystonia** with prominent **cervical, cranial (oromandibular), and laryngeal** involvement, producing dysphagia and/or dysphonia, typically 2–11 years after initial onset. Early motor features (hypotonia, impaired coordination, gait difficulty) can emerge in infancy ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/); [Frontiers 2022](https://www.frontierspartnerships.org/journals/dystonia/articles/10.3389/dyst.2022.10287/full)).

**Severity/functional range:** from minor gait disturbance to wheelchair dependence, classified by Gross Motor Function Classification System (GMFCS) grades II–V.

**Classification:** in a 68-individual cohort, 58% had complex/combined dystonia (dystonia plus other neurological features) and 41% had isolated dystonia.

**Adult-onset variant:** a distinct, milder **adult-onset focal or segmental dystonia** phenotype (often cervical dystonia or writer's cramp) without prominent developmental delay has been increasingly recognized, broadening the age spectrum considerably ([Adult-onset KMT2B-related dystonia, *Brain Communications* 2022](https://academic.oup.com/braincomms/article/4/6/fcac276/6775143); [PMC9724767](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9724767/)).

### KMT2B-related NDD (non-dystonic phenotype) — ~7% of families
- Developmental delay ~81%
- Intellectual disability ~89% (mild to severe)
- Bulbar dysfunction ~44%
- Neurobehavioral/psychiatric manifestations ~21% (ADHD, ASD)
- Febrile seizures ~11%
- Eye movement abnormalities ~11%
- In deletion cases specifically: ectodermal dysplasia, genital malformations in affected males (reflecting contiguous gene effects from the 19q13 microdeletion, not KMT2B haploinsufficiency alone)

### Quality of Life Impact
Laryngeal, oromandibular, and cervical dystonia are frequently the most disabling elements — often requiring enteral feeding, augmentative/alternative communication (AAC) technology, and adapted seating. Loss of independent ambulation is common as disease progresses; DBS can partially reverse this (see Treatment). No disease-specific EQ-5D/SF-36 data were identified in this search; QoL impact is documented qualitatively in cohort/natural-history papers rather than via standardized instruments.

---

## 4. Genetic/Molecular Information

### Causal Gene
- **Gene:** *KMT2B* (HGNC symbol; historically *MLL4*/*MLL2* — nomenclature caution, as *KMT2D* was also called *MLL4*/*MLL2* in older literature)
- **OMIM gene entry:** *606834
- **Locus:** 19q13.12
- **Protein:** Histone-lysine N-methyltransferase 2B (KMT2B), a member of the SET1/MLL family of H3K4 methyltransferases.

### Pathogenic Variants
- **Variant types:** missense (most common), nonsense, splice-site, frameshift indels, and 19q13.11–19q13.12 microdeletions.
- **Detection yield:** exome/genome sequence analysis detects ~94% of pathogenic variants (may miss exon 1 variants and synonymous splice-affecting variants); chromosomal microarray analysis (CMA) detects the remaining ~6% (large deletions/duplications).
- **Classification:** per ACMG/AMP criteria via ClinVar/ClinGen — specific pathogenic/likely-pathogenic/VUS counts were not retrieved directly in this search; DNA methylation episignature testing has become an important adjunct specifically for resolving KMT2B VUS (see Diagnostics).
- **Genotype-phenotype correlation:** loss-of-function (truncating) variants are associated with **statistically significantly earlier disease onset** than missense variants (mean onset ~4.4 years for insertions/frameshift vs. ~8.7 years for missense variants), but variant class does **not** significantly influence rate of progression, overall severity, or DBS responsiveness ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)).
- **Domain clustering:** missense variants cluster within putative functional/structural domains (zinc-finger CXXC-type, PHD fingers), while truncating variants occur throughout the gene ([ResearchGate summary of KMT2B rare missense variants](https://www.researchgate.net/publication/317015962_KMT2B_rare_missense_variants_in_generalized_dystonia)). A recurrent missense hotspot at **codon 2565** produces variable expressivity ([PubMed 39933316](https://pubmed.ncbi.nlm.nih.gov/39933316/)).
- **Allele frequency:** *KMT2B* pathogenic variants are essentially absent from population databases (gnomAD) consistent with a severe, highly penetrant dominant disorder subject to strong purifying selection; specific o/e or pLI figures were not independently retrieved in this search.
- **Somatic vs. germline:** disease-causing variants are germline (constitutional); no somatic mosaic or cancer-associated *KMT2B* variant relevance was identified for this phenotype (note: *KMT2B*, like other MLL-family genes, has separate literature in somatic cancer genomics that is unrelated to this dystonia phenotype).
- **Functional consequence:** predominantly **loss of function / haploinsufficiency** (both truncating variants and many missense variants), though genotype-phenotype nuance exists (see hotspot above) suggesting some missense alleles may have distinct or partial dominant-negative effects — this remains incompletely resolved mechanistically.

### Modifier Genes
None specifically validated; phenotypic variability (including intrafamilial variability with different family members manifesting dystonic vs. NDD-predominant phenotypes from the same variant) is well documented but unexplained by additional genetic modifiers to date ([PMC8932353, "variable phenotypes among family members"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8932353/)).

### Epigenetic Information
This is the most epigenetically well-characterized dystonia gene:
- **Blood DNA methylation** provides an accurate biomarker of KMT2B-related disease: Ciolfi et al. and colleagues demonstrated **genome-wide DNA hypermethylation**, non-randomly distributed and enriched at regulatory regions such as gene promoters, in individuals carrying pathogenic *KMT2B* variants, "indicating a general repression of transcriptional activity" ([*Brain* 2022, academic.oup.com/brain/article/145/2/644](https://academic.oup.com/brain/article/145/2/644/6378248); [Clinical Epigenetics 2021](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-021-01145-y)).
- Mechanistically, work in mouse embryonic stem cells shows KMT2B does not merely deposit the H3K4 methyl mark but **prevents transcriptional silencing by repelling components of Polycomb Repressive Complex 2 (PRC2) and DNA methyltransferases (DNMTs)** at target loci — providing a direct molecular explanation for the observed promoter hypermethylation when KMT2B is haploinsufficient ([Clinical Epigenetics 2021](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-021-01145-y)).
- A **DNA methylation episignature (EpiSign)** has been clinically validated as a diagnostic/functional-classification tool for *KMT2B* variants of uncertain significance, using Illumina Infinium EPIC arrays ([Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01780-1); case report [PMC10902455](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10902455/)). Notably, a 2024 paper asks "Are there two disjunct episignatures for KMT2B-related disease?" ([PMC11631077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11631077/)), suggesting the dystonia and NDD phenotypes may have partially distinguishable methylation signatures — an active area of investigation.

### Chromosomal Abnormalities
Heterozygous deletions of **19q13.11–19q13.12** encompassing *KMT2B* (and potentially neighboring genes) account for ~12% of DYT-KMT2B and a larger proportion of NDD-predominant cases; contiguous gene deletion may explain additional features (ectodermal dysplasia, genital malformations in males) not attributable to *KMT2B* haploinsufficiency alone.

---

## 5. Environmental Information

- **Environmental/toxic factors:** none identified; disease is fully genetically determined.
- **Lifestyle factors:** not causally relevant to disease occurrence; physical activity/therapy is relevant to management (see Treatment/Prevention).
- **Infectious agents:** none identified as causal. (Note: intercurrent infections/fever can precipitate **status dystonicus**, a dystonic emergency, in already-affected individuals — this is a disease-course exacerbating factor rather than a cause; see [ScienceDirect case report on status dystonicus in KMT2B](https://www.sciencedirect.com/science/article/abs/pii/S1769721220303098).)

---

## 6. Mechanism / Pathophysiology

### Causal Chain (numbered, from mutation to clinical phenotype)

1. A **heterozygous loss-of-function or missense variant in *KMT2B*** (or a 19q13 microdeletion spanning the gene) **reduces functional KMT2B protein dosage** → **KMT2B haploinsufficiency** (demonstrated directly for truncating variants; inferred/probable for many missense variants clustering in functional domains) ([Zech et al. 2016](https://www.nature.com/articles/ng.3740)).
2. Reduced KMT2B activity **leads to** impaired deposition/maintenance of **H3K4 methylation (H3K4me1/me3)** at target promoters and enhancers, since KMT2B is a SET-domain histone-lysine N-methyltransferase specific for H3K4 ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)).
3. Independent of methyltransferase catalysis, reduced KMT2B occupancy at chromatin **results in** failure to repel **Polycomb Repressive Complex 2 (PRC2)** and **DNA methyltransferases (DNMTs)** from target regulatory loci — demonstrated experimentally in mouse embryonic stem cells (this step is **inferred to extend to human neurons/patient tissue** rather than directly demonstrated in situ) ([Clinical Epigenetics 2021](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-021-01145-y)).
4. This **leads to** aberrant, non-random **DNA hypermethylation**, disproportionately enriched at gene promoters and other positive regulatory elements — directly confirmed in patient peripheral blood as a robust, clinically validated biomarker/episignature ([Ciolfi et al.; *Brain* 2022](https://academic.oup.com/brain/article/145/2/644/6378248)).
5. Combined loss of activating H3K4 methylation and gain of repressive promoter DNA methylation **results in** **general repression of transcriptional activity** at a broad set of KMT2B target genes, including genes important for neurodevelopment and neuronal/motor circuit function (specific downstream target genes driving the dystonic phenotype remain **not yet fully elucidated** — "the exact molecular mechanism by which KMT2B variants cause dystonia remains to be elucidated," per the pathophysiology literature).
6. Dysregulated gene expression during critical periods of **basal ganglia and corticostriatal circuit development** is proposed (by analogy with other monogenic dystonias — DYT1/TOR1A, DYT6/THAP1 — and by the neuroimaging findings below) to **produce** disrupted **striatal/pallidal network function**, particularly implicating the **external and internal globus pallidus**.
7. This circuit dysfunction **manifests clinically** as progressive dystonia, beginning focally in the lower limbs and **evolving (caudocranial progression)** into generalized, cervical, cranial, and laryngeal dystonia, frequently accompanied by cognitive/developmental and psychiatric comorbidity reflecting broader cortical/neurodevelopmental transcriptional disruption.

**Branch point:** In a minority of cases, haploinsufficiency manifests **without** dystonia, producing the **KMT2B-related NDD phenotype** (developmental delay/intellectual disability alone) — the branch point between the dystonic and purely neurodevelopmental outcome is not mechanistically resolved but appears to correlate loosely with variant type/location and shows marked **intrafamilial variability**, implying stochastic or unidentified modifying factors rather than a strict genotype rule.

### Molecular Pathways
- **H3K4 methylation / chromatin regulation pathway** (SET1/MLL/COMPASS-like complex biology). Relevant GO terms: **GO:0051568** (histone H3-K4 methylation), **GO:0034968** (histone lysine methylation), **GO:0000123** (histone acetyltransferase complex — for COMPASS-related complex context), **GO:0006357** (regulation of transcription by RNA polymerase II).
- **PRC2/Polycomb repression antagonism** pathway: **GO:0031519** (PcG protein complex), **GO:0006306** (DNA methylation).
- No canonical signaling cascade (Wnt/MAPK/mTOR/PI3K-AKT) has been specifically implicated; this is fundamentally an **epigenetic/chromatin-regulatory** disease mechanism rather than a signal-transduction disorder.

### Cellular Processes
- Primary process: **epigenetic transcriptional dysregulation** (GO:0010629, negative regulation of gene expression; broadly, chromatin-mediated transcriptional repression).
- Downstream/secondary: presumed disruption of **neuronal differentiation and synaptic gene programs** during CNS development (inferred from the NDD phenotype and broad promoter hypermethylation, not directly demonstrated at single-cell resolution in patient neurons).

### Protein Dysfunction
KMT2B protein (UniProt Q9UMN6) is a large multidomain SET-family methyltransferase; disease variants act principally through **loss of function / haploinsufficiency** rather than aggregation or gain-of-function misfolding. Missense variant clustering in zinc-finger (CXXC-type) and PHD-finger domains suggests these variants disrupt chromatin/DNA-binding or protein-protein interaction functions required for proper complex assembly, by analogy with the CXXC-domain missense mechanism established for the paralog **KMT2A** in Wiedemann–Steiner syndrome, where AlphaFold2 structural modeling accurately classifies pathogenicity of CXXC-domain missense variants ([PMC9249231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9249231/)).

### Metabolic Changes
No disease-specific metabolic pathway abnormality has been established; KMT2B-related dystonia is not classified among the inborn errors of metabolism (it is specifically listed as a differential-diagnosis exclusion target — see Diagnostics — against metabolic dystonias such as glutaric acidemia type 1, methylmalonic acidemia, and Wilson disease).

### Immune System Involvement
No evidence of autoimmune or immune-mediated pathophysiology.

### Tissue Damage Mechanisms
Not a degenerative/necrotic process in the classic sense; rather a **neurodevelopmental circuit dysfunction**. Neuroimaging (see Anatomical Structures) shows subtle globus pallidus signal changes rather than structural tissue destruction, consistent with a functional/metabolic rather than neurodegenerative process, though "progressive" clinical course implies an ongoing pathophysiological process not fully explained by static developmental miswiring alone.

### Biochemical Abnormalities
Genome-wide/loci-specific **DNA hypermethylation** at gene promoters (directly measured in patient blood) is the best-characterized biochemical correlate of disease and is used diagnostically (EpiSign episignature).

### Epigenetic Changes
As above — this is the disease's defining molecular signature. Reference: [Ciolfi et al., *Brain* 2022, "Blood DNA methylation provides an accurate biomarker of KMT2B-related disease"](https://academic.oup.com/brain/article/145/2/644/6378248).

### Molecular Profiling
- **Transcriptomics:** broad transcriptional repression inferred from methylation data; no large-scale patient-derived RNA-seq dataset was identified in this search.
- **Proteomics/metabolomics/lipidomics:** no disease-specific data identified.
- **Genomic structural features:** 19q13.11–19q13.12 microdeletions define a subset; breakpoint mapping via CMA/array data (dbVar, DECIPHER) is used clinically but no dedicated structural-variant landscape paper was retrieved here.

### Advanced Technologies
- **Single-cell/spatial transcriptomics:** not identified for this specific disorder.
- **Multi-omics integration:** the DNA methylation episignature work (EpiSign platform, Aref-Eshghi and colleagues' broader Mendelian neurodevelopmental disorder episignature framework) is the most advanced omics application to date, spanning 42+ Mendelian NDDs including KMT2B-related disease.
- **Functional genomics screens (CRISPR/RNAi):** not identified specifically for KMT2B dystonia modeling in this search.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** central nervous system, specifically the **basal ganglia** (particularly external and internal globus pallidus) and corticostriatal motor circuitry.
- **Secondary involvement:** musculoskeletal system (foot/limb deformities, scoliosis from chronic dystonic posturing), speech/laryngeal apparatus (dysarthria, dysphonia), swallowing apparatus (dysphagia, aspiration risk), endocrine system (short stature, precocious puberty, hypothyroidism in a subset), auditory system (sensorineural hearing loss in some individuals), and craniofacial structures (dysmorphism).
- **Body systems:** nervous system (primary); musculoskeletal, endocrine, gastrointestinal (feeding), and psychiatric/behavioral systems secondarily.

Suggested UBERON terms: **UBERON:0002210** (globus pallidus), **UBERON:0002037** (cerebellum, for the subset with cerebellar atrophy), **UBERON:0001873** (globus pallidus externa/interna substructure terms as applicable), **UBERON:0001896** (basal ganglion).

### Tissue and Cell Level
- Primarily affects **neurons within the basal ganglia** — specifically **medium spiny neurons of the striatum** and **GABAergic pallidal neurons** are the presumptive cell types implicated by anatomical/circuit logic and DBS target choice (globus pallidus internus), though direct cell-type-resolved patient data were not identified in this search.

Suggested CL terms: **CL:0000617** (GABAergic neuron), **CL:0000679** (medium spiny neuron), **CL:0000031** (central nervous system neuron, generic).

### Subcellular Level
- **Nucleus** — chromatin/histone modification machinery (KMT2B acts on nucleosomal histone H3).

Suggested GO Cellular Component terms: **GO:0005634** (nucleus), **GO:0000785** (chromatin), **GO:0035097** (histone methyltransferase complex).

### Localization
- Neuroimaging finding: **subtle, symmetrical hypointense lateral streaks in the external globus pallidus** on T2-weighted, T2*-weighted, and susceptibility-weighted MRI sequences — described in ~27% of cases with brain imaging abnormalities; this pattern may be **age-dependent, becoming less prominent over time**. Brain MRI is otherwise **normal in ~40%** of cases. Cerebellar atrophy has been described in three individuals. DaTscan was normal in four individuals and showed decreased striatal dopamine-transporter uptake in two ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)).
- **Lateralization:** dystonia is typically bilateral/symmetric in the generalized form, though focal onset (e.g., unilateral lower-limb dystonia, or the adult-onset cervical/segmental forms) can be asymmetric or unilateral initially.

---

## 8. Temporal Development

### Onset
- **Median age of onset: 6 years** (range 0–43 years across the full reported spectrum, including newly recognized adult-onset cases) ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)). A recent 44-patient natural history cohort reported median onset **5.0 years** ([2025 Brain expansion cohort](https://arxiv.org/pdf/2502.06320)).
- **Onset pattern:** typically **insidious**, beginning with subtle gait disturbance or foot posturing; genetically determined subtype differences exist (earlier onset with truncating/insertion variants, mean 4.4 years, vs. later onset with missense variants, mean 8.7 years).
- Distinct **adult-onset** (focal/segmental, e.g., cervical dystonia) subtype now recognized, expanding the classical pediatric-onset paradigm.

### Progression
- **Disease course:** progressive, evolving in a **caudocranial pattern** — lower-limb focal dystonia → generalized dystonia with cervical, cranial, laryngeal involvement — typically over **2–11 years** from initial onset (median ~2.0 years to generalization in the 2025 cohort).
- **Functional staging:** GMFCS grades II (mild) through V (wheelchair-dependent, most severe) are used to stage motor severity.
- **Progression rate:** variable — generally described as gradually progressive rather than rapidly fulminant, though acute severe exacerbations (**status dystonicus**) can occur, sometimes precipitated by intercurrent illness ([ScienceDirect case report](https://www.sciencedirect.com/science/article/abs/pii/S1769721220303098)).
- **Disease duration:** chronic, lifelong; not self-limited.

### Patterns
- **Remission:** spontaneous remission is not a feature; DBS produces substantial and sometimes sustained (multi-year) improvement in several dystonia domains but is a treatment effect, not a disease remission.
- **Critical periods:** early GPi-DBS intervention — specifically **before loss of independent ambulation** — is associated with better long-term motor outcomes, suggesting a clinically actionable window for intervention timing ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/); [PMC12926133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12926133/)).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** "**not yet established**" per GeneReviews — this is an ultra-rare disorder without formal population-based prevalence/incidence estimates.
- **Reported case counts:** ~246 individuals/229 families (DYT-KMT2B) and 27 individuals/25 families (KMT2B-related NDD) as of the most recent GeneReviews synthesis — likely an undercount given ongoing case reports (e.g., recent Indian cohort, [e-jmd.org](https://www.e-jmd.org/upload/jmd-23035.pdf); Austrian national cohort, [PMC12926133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12926133/)).
- *KMT2B* variants are estimated in some cohort studies to account for a meaningful minority of childhood-onset isolated/complex dystonia of unknown cause when systematically screened (e.g., a single-center pediatric cohort study on "Frequency and phenotypic spectrum of KMT2B dystonia in childhood" — [ResearchGate summary](https://www.researchgate.net/publication/333886384_Frequency_and_phenotypic_spectrum_of_KMT2B_dystonia_in_childhood_A_single-center_cohort_study)), making it one of the more common monogenic causes of early-onset generalized dystonia identified via next-generation sequencing.

### Genetic Etiology
- **Inheritance pattern:** **autosomal dominant**, with **reduced penetrance** (documented asymptomatic heterozygous carriers within families).
- **De novo rate:** ~84% de novo for DYT-KMT2B; ~91% de novo for KMT2B-related NDD.
- **Inherited cases:** ~16% (dystonia) / ~11% (NDD) inherited from a parent; among inherited cases, ~58% are inherited from a dystonic-phenotype parent and ~42% from an NDD-phenotype (sometimes clinically unaffected/subclinical) parent.
- **Penetrance:** incomplete — some carrier parents are clinically asymptomatic.
- **Expressivity:** highly **variable**, including well-documented **intrafamilial variability** where different family members carrying the identical variant manifest markedly different phenotypes (isolated dystonia vs. NDD vs. asymptomatic) ([PMC8932353](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8932353/)).
- **Genetic anticipation:** not reported/established for this disorder (it is not a repeat-expansion disease).
- **Germline mosaicism:** implied by the ~1% empiric sibling recurrence risk quoted for ostensibly de novo, unaffected-parent cases (accounting for possible parental gonadal mosaicism).
- **Founder effects:** none specifically reported; variants are largely private/family-specific, consistent with a highly heterogeneous mutational spectrum (~100 reported variants across the gene).
- **Consanguinity:** not a relevant risk factor (dominant, not recessive, disorder).
- **Carrier frequency:** not applicable in the classic recessive-carrier sense; population carrier frequency of pathogenic *KMT2B* alleles is expected to be near zero given the severity and reduced (but real) reproductive fitness effect of the phenotype and the predominance of de novo occurrence.

### Recurrence Risk
- De novo proband, unaffected parents: **~1%** risk to future siblings (gonadal mosaicism).
- Affected parent: **50%** risk to each child.
- Affected individual (proband) to offspring: **50%** per child.

### Population Demographics
- **Affected populations:** no specific ethnic or geographic enrichment has been established; cases have been reported across European, North American, and Asian cohorts (e.g., a recent Indian case series, [e-jmd.org](https://www.e-jmd.org/upload/jmd-23035.pdf)), consistent with a pan-ethnic, de novo-predominant Mendelian disorder.
- **Geographic distribution:** no endemic pattern; reporting is concentrated in centers with access to trio exome/genome sequencing and specialized movement-disorder clinics (Europe — UK, Germany, Austria, Italy; North America; increasingly Asia).
- **Sex ratio:** not clearly skewed in overall disease occurrence, but **DBS outcome is reported to be better in males** than females in some cohort analyses ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)) — the biological basis for this sex-based outcome difference is unclear and warrants cautious interpretation given small cohort sizes.
- **Age distribution:** predominantly pediatric-onset historically, but the age range of reported affected individuals now spans neonatal/infantile through the 5th–7th decade (rare adult-onset and long-surviving cases).

---

## 10. Diagnostics

### Establishing the Diagnosis
Per GeneReviews, diagnosis requires **suggestive clinical findings PLUS** one of:
1. A heterozygous pathogenic/likely pathogenic *KMT2B* sequence variant (~88% of cases), or
2. A heterozygous 19q13.11–19q13.12 deletion encompassing *KMT2B* (~12% of cases).

### Genetic Testing Approaches
- **Exome/genome sequencing (first-tier for suspected monogenic dystonia):** detects ~94% of pathogenic variants; may miss exon 1 variants and variants affecting synonymous splice sites.
- **Chromosomal microarray analysis (CMA):** detects the remaining ~6%, chiefly the 19q13 deletions.
- **Gene panel testing** for early-onset/complex dystonia typically includes *KMT2B* alongside *TOR1A, THAP1, ATP1A3*, NBIA genes, and others.
- **DNA methylation episignature (EpiSign) analysis:** an important adjunct for resolving *KMT2B* **variants of uncertain significance (VUS)**, using genome-wide Illumina Infinium EPIC methylation arrays; validated as accurately distinguishing pathogenic-variant carriers from controls and successfully used for early diagnosis even in a pre-dystonic 4-year-old ([Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01780-1); [PMC10902455 case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10902455/)). A 2024 paper questions whether **two distinct episignatures** exist corresponding to the dystonia vs. NDD phenotypic subgroups ([PMC11631077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11631077/)).

### Neuroimaging
- **Brain MRI:** normal in ~40%; ~27% show subtle, symmetric hypointense streaks in the **external globus pallidus** on T2/T2*/SWI sequences (may attenuate with age); cerebellar atrophy in rare cases.
- **DaTscan:** typically normal (4 of 6 reported); occasionally shows decreased striatal dopamine-transporter uptake (2 of 6).

### Electrophysiology
No disease-specific EEG/EMG signature beyond standard dystonia work-up (surface EMG can characterize dystonic muscle activation patterns for clinical/DBS-programming purposes, but this is not diagnostic of the genetic etiology).

### Laboratory/Biochemical
No specific serum/urine biomarker beyond the DNA methylation episignature described above; standard metabolic work-up (to exclude Wilson disease, organic acidemias, etc.) remains part of the differential diagnostic pathway rather than being confirmatory for KMT2B disease itself.

### Differential Diagnosis
**For DYT-KMT2B:**
- Neurodegeneration with brain iron accumulation (NBIA) genes: *ATP13A2, C19orf12, COASY, FA2H, PANK2, PLA2G6, WDR45*
- *ATP1A3*-related rapid-onset dystonia-parkinsonism / alternating hemiplegia of childhood
- *TOR1A*-related DYT1 (early-onset generalized torsion dystonia)
- *THAP1*-related dystonia (DYT6)
- Wilson disease (copper metabolism)
- Glutaric acidemia type 1
- Methylmalonic acidemia
- Niemann-Pick disease type C
- *POLG*-related mitochondrial disorders and other primary mitochondrial disease (>350 causal genes)

**For KMT2B-related NDD** (nonspecific intellectual disability differential):
- Kleefstra syndrome (*EHMT1*)
- Kabuki syndrome (*KMT2D, KDM6A*)
- Wiedemann-Steiner syndrome (*KMT2A* — same gene family, notably also chromatin-modifier-related and CXXC-domain-relevant)
- Silver-Russell syndrome
- Seckel syndrome

### Screening
No population/newborn screening program exists (ultra-rare, no metabolic analyte to screen for). Cascade/predictive genetic testing is offered to at-risk relatives once a familial variant is identified, given the 50% transmission risk from an affected/carrier parent.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** no formal survival statistics or standardized mortality ratio have been published; the disorder is not classically fatal, and **individuals into the seventh decade of life** have been reported, though the disease is progressive and morbidity-heavy. For KMT2B-related NDD, insufficient long-term outcome data exist.
- **Morbidity/functional outcomes:** progressive loss of independent ambulation is common without treatment; laryngeal/oromandibular dystonia frequently necessitates enteral (tube) feeding and augmentative communication devices. GMFCS staging (II–V) is used as a functional severity/outcome metric.
- **Complications:** aspiration risk from dysphagia, orthopedic complications (contractures, scoliosis, joint deformity) from chronic dystonic posturing, **status dystonicus** (a dystonic emergency, potentially triggered by intercurrent illness), and psychiatric comorbidity (anxiety, OCD, ADHD, ASD features).
- **Recovery potential with treatment:** substantial — GPi-DBS produces **mean reductions of ~35–49% in BFMDRS-M (movement)** and **~30–38% in BFMDRS-D (disability)** scores at 1 year, with sustained (though partially attenuated) benefit at 5-year and even up to 22-year follow-up in the largest reported cohort (n=18) ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/); [PMC12926133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12926133/)). At 1 year, roughly half of assessed cases (8/15 for BFMDRS-M; 7/15 for BFMDRS-D) meet the >30% "optimal response" threshold.
- **Regional variability of benefit:** at median 7.5-year follow-up, sustained improvement is seen for **trunk (53.2%), neck (50.5%), and oromandibular (35.7%)** dystonia, but **gait (16.2%) and speech (3.4%)** show markedly suboptimal long-term response, and **freezing of gait** has emerged as a recognized late complication (5/8 patients in one long-term subgroup), particularly associated with truncating variants; **no patient in the long-term subgroup maintained fully autonomous gait**, though DBS preserved ambulation in some and restored walking ability in others.

### Prognostic Factors
- **Male sex** and **greater baseline dystonia severity** are associated with better DBS response.
- **Earlier DBS placement (before loss of ambulation)** predicts better long-term motor outcome.
- **Severe preoperative speech impairment and older age at DBS** are negative prognostic factors.
- Variant class (truncating vs. missense) affects age of onset but **not** DBS responsiveness or overall disease severity/progression rate.

---

## 12. Treatment

### Pharmacotherapy
- **Antimuscarinic/anticholinergic agents (e.g., trihexyphenidyl):** considered **first-line pharmacologic treatment**, producing significant motor improvement in **about 50%** of individuals; recommended to start at low dose with slow titration per published dystonia-treatment guidelines.
  - NCIT term: `NCIT:C15986` (Pharmacotherapy); consider `therapeutic_agent` → CHEBI trihexyphenidyl term.
- **Levodopa and other anti-dystonic agents** (baclofen, gabapentin, tetrabenazine): a trial is reasonable, but these **have not resulted in long-term benefit for most individuals** ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK493766/)).
- **Botulinum toxin injection** for focal dystonic segments (implied standard-of-care adjunct in dystonia management generally; not separately quantified for KMT2B in the retrieved sources but consistent with general early-onset dystonia management pathways).

### Advanced Therapeutics
- **Gene therapy / RNA-based / cell therapy:** none specifically developed or in trials for KMT2B-related dystonia as of this search — this is fundamentally a haploinsufficiency (loss-of-function) disorder, which is mechanistically more challenging to correct with antisense/knockdown strategies (which typically address gain-of-function) and would more plausibly require gene-augmentation approaches; none identified as being in active clinical development.

### Surgical / Interventional — Deep Brain Stimulation (mainstay advanced therapy)
- **Bilateral GPi-DBS (globus pallidus internus)** has become the **therapeutic mainstay** for medically refractory KMT2B-related dystonia, performed in **~80 individuals** reported to date.
  - NCIT term candidate: `NCIT:C15329` (Surgical Procedure), with `therapeutic_modality: DEVICE` and device detail via `qualifiers` (as per dismech convention for device+action, analogous to cochlear implantation) — DBS device term (e.g., an NCIT/relevant device code) should be looked up specifically during curation.
  - **Efficacy:** mean BFMDRS-M reduction ~35% (1 yr) to ~44% (5 yr); mean BFMDRS-D reduction ~30% (1 yr) to ~31% (5 yr) in the largest long-term cohort (18 patients, up to 22 years follow-up).
  - **Best responding domains:** trunk, neck, upper limb, oromandibular dystonia.
  - **Poorly responding domains:** gait/lower-limb dystonia (may worsen; loss of ambulation reported in some individuals) and laryngeal dystonia (DBS has **not** been effective for laryngeal dystonia specifically).
  - **Complication:** freezing of gait, particularly associated with truncating *KMT2B* variants.
  - Systematic review/meta-analysis: [GPi-DBS for KMT2B-Associated Dystonia](https://pubmed.ncbi.nlm.nih.gov/35005062/).

### Supportive and Rehabilitative Care
- **Physical therapy:** early initiation to maintain function and prevent secondary orthopedic complications (contractures, deformity).
- **Occupational therapy:** for fine motor function.
- **Speech-language therapy:** for feeding/swallowing safety and communication; videofluoroscopy used to assess aspiration risk.
- **Augmentative and alternative communication (AAC):** for individuals with severe dysarthria/anarthria.
- **Nutritional support:** assessment and intervention, including enteral feeding when indicated.
- **Adaptive equipment:** ankle-foot orthoses, walkers, adapted seating.
- **Neurobehavioral/psychiatric management:** including applied behavior analysis (ABA) therapy for ASD/behavioral features.
- **Early intervention (ages 0–3) and individualized education plans (IEP)** for developmental/cognitive needs.

### Experimental
No KMT2B-specific interventional clinical trials (with NCT identifiers) were identified in this search; management is guided by expert consensus/cohort experience rather than randomized trial data, reflecting the disorder's rarity.

### Treatment Strategy / Algorithm
General approach per GeneReviews: **trial of anticholinergic therapy (particularly trihexyphenidyl) as first-line pharmacotherapy** → consider other anti-dystonic agents (levodopa, baclofen, gabapentin, tetrabenazine) with modest expectations → **early referral for GPi-DBS evaluation**, ideally before loss of ambulation, for medically refractory or progressive generalized dystonia → lifelong multidisciplinary supportive care (PT/OT/speech/nutrition/psychiatry).

### Pregnancy/Reproductive Considerations
Isolated case reports of trihexyphenidyl, levodopa/carbidopa, and clonazepam exposure during pregnancy in affected women showed no adverse fetal effects, though data are extremely limited (single case reports only) — genetic counseling regarding medication risk-benefit in pregnancy is recommended.

---

## 13. Prevention

- **Primary prevention:** not applicable in the traditional sense (no modifiable risk factor); however, **genetic counseling and reproductive options** (prenatal diagnosis, preimplantation genetic testing) are available once a familial pathogenic variant is identified, for families wishing to reduce recurrence risk.
- **Secondary prevention/early detection:** early molecular diagnosis (including via the DNA methylation episignature, which has enabled diagnosis in a pre-symptomatic/pre-dystonic 4-year-old) allows earlier initiation of surveillance and supportive interventions, and earlier consideration of DBS before irreversible functional loss (loss of ambulation) — a clinically meaningful "critical window."
- **Tertiary prevention:** proactive multidisciplinary management (PT/OT/speech/nutrition, orthopedic surveillance, psychiatric care) to prevent secondary complications (contractures, aspiration, psychosocial morbidity) in individuals with established disease.
- **Genetic counseling:** offered per standard autosomal dominant disease counseling — 50% transmission risk from an affected/carrier parent, ~1% empiric sibling recurrence risk for apparent de novo cases (accounting for possible germline mosaicism), reduced penetrance discussed explicitly given documented asymptomatic carriers.
- **Screening:** no population-level or newborn screening program exists; testing is targeted (symptomatic individuals, at-risk relatives via cascade testing).
- **Immunization/public health/environmental interventions:** not applicable (non-infectious, non-environmental monogenic disorder).

---

## 14. Other Species / Natural Disease

- No naturally occurring companion-animal, livestock, or wildlife disease model attributable to spontaneous *KMT2B* orthologous mutation was identified in this search (no OMIA entry surfaced).
- **Orthologous gene:** *Kmt2b* is conserved across vertebrates (mouse *Kmt2b*, zebrafish *kmt2b*); NCBI Gene IDs for mouse *Kmt2b* and zebrafish *kmt2b* should be confirmed directly during curation.
- **Comparative note:** functionally related family members show naturally occurring or engineered disease relevance in other species context (e.g., *Kmt2d* embryonic-lethal knockout phenotypes, discussed under Model Organisms below), but this is paralog, not ortholog, biology and should not be conflated with *KMT2B* itself.
- **Zoonotic potential:** not applicable (this is a purely genetic, non-infectious human disease).

---

## 15. Model Organisms

### Mouse Models
Direct *Kmt2b*-specific dystonia mouse model data were not clearly retrieved in this search; most mouse constraint/phenotype data available relate to the paralogous methyltransferase genes:
- ***Kmt2d* (historically also confusingly labeled *Mll4* in some papers) knockout mice:** embryonic lethal at E9.5; conditional knockout in somitic precursors (giving rise to brown adipose tissue and back skeletal muscle) causes marked reduction in BAT/muscle mass and perinatal lethality from respiratory failure; adult conditional knockouts show craniofacial defects (midfacial hypoplasia, midline palate defects) ([biorxiv/PMC11803150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11803150/)).
- ***Kmt2c* (*Mll3*) haploinsufficient mice:** show autism-like behavioral deficits, illustrating that KMT2-family haploinsufficiency in mice can recapitulate neurobehavioral phenotypes relevant to the human NDD spectrum ([PMC12650575](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12650575/)).
- ***Mll2* (a related H3K4 methyltransferase) heterozygous mice:** hyperglycemic, hyperinsulinemic, and develop non-alcoholic fatty liver disease — illustrating pleiotropic, dosage-sensitive phenotypes of H3K4 methyltransferase family haploinsufficiency, though this is metabolic rather than movement-disorder phenotype and again reflects a different family member ([PMC3691224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3691224/)).

**Note for curation:** because *KMT2B, KMT2D,* and *KMT2A* have overlapping/confusing historical aliases (*MLL2, MLL4*), any model-organism claims sourced from search snippets should be re-verified against the current official gene symbol before being attached as `modeled_mechanisms` evidence — several search results returned data for *KMT2D* (Kabuki syndrome gene) under ambiguous "MLL4" labeling that must not be misattributed to *KMT2B*.

### Zebrafish
- Zebrafish *kmt2b* has been referenced in variant-conservation analyses (e.g., noting that the residue affected by a human p.Phe1662 variant is naturally a tyrosine in zebrafish/*Drosophila*, used for cross-species conservation assessment of variant pathogenicity) ([PMC8932353](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8932353/); [tremorjournal.org](https://tremorjournal.org/articles/10.5334/tohm.679)). No dedicated zebrafish loss-of-function movement-phenotype model paper for *kmt2b* was identified in this search — this is a candidate model-development gap.

### Cellular/In Vitro Models
- **Mouse embryonic stem cells** have been used to dissect the direct molecular function of KMT2B in repelling PRC2/DNMT complexes from chromatin — this is the best-established functional model system for KMT2B mechanism to date, though it models the general epigenetic function of the protein rather than the dystonia phenotype specifically ([Clinical Epigenetics 2021](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-021-01145-y)).
- **Patient-derived peripheral blood** is used for the DNA methylation episignature assay — a translational biomarker model rather than a mechanistic disease model, but functionally validates variant pathogenicity.

### Model Limitations
No iPSC-derived neuronal model, patient-derived organoid, or in vivo movement-disorder animal model specific to *KMT2B* dystonia was identified in this search — representing a clear translational research gap relative to other monogenic dystonias (e.g., *TOR1A*/DYT1, which has multiple mouse models). This gap should be flagged explicitly in any `experimental_models`/`animal_models` curation as an evidence limitation (`HUMAN_MODEL_MISMATCH` candidate discussion) rather than assumed absent from a literature-completeness perspective — confirm with a dedicated search before finalizing this claim in the KB entry.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease (MONDO) | Search directly on mondo.monarchinitiative.org for "KMT2B-related dystonia" / "DYT28" — not independently confirmed in this search |
| OMIM | 617284 (DYT28); 619934 (MRD68); *606834 (gene) |
| Gene (HGNC) | KMT2B, hgnc: ID to confirm |
| Phenotype (HP) | HP:0001332 Dystonia; HP:0002340 Lower limb dystonia; HP:0001608 Dysphonia; HP:0002015 Dysphagia; HP:0001249 Intellectual disability; HP:0000252 Microcephaly; HP:0004322 Short stature; HP:0001336 Myoclonus; HP:0001257 Spasticity; HP:0001251 Ataxia; HP:0007018 Attention deficit hyperactivity; HP:0000717 Autistic behavior; HP:0000407 Sensorineural hearing loss |
| Biological process (GO) | GO:0051568 histone H3-K4 methylation; GO:0034968 histone lysine methylation; GO:0006306 DNA methylation; GO:0031519 PcG protein complex; GO:0006357 regulation of transcription by RNA Pol II |
| Cell type (CL) | CL:0000679 medium spiny neuron; CL:0000617 GABAergic neuron |
| Anatomy (UBERON) | UBERON:0002210 globus pallidus; UBERON:0001896 basal ganglion; UBERON:0002037 cerebellum |
| Treatment (NCIT) | NCIT:C15986 Pharmacotherapy (trihexyphenidyl/anticholinergics as therapeutic_agent); NCIT:C15329 Surgical Procedure (GPi-DBS; device qualifier needed) |

---

## Notes on Evidence Gaps for Curation

1. **Population prevalence** is explicitly "not yet established" — do not fabricate a numeric estimate; use `prevalence_class: NOT_YET_DOCUMENTED` per dismech convention.
2. **Mechanistic link from promoter hypermethylation to specific dystonia-driving target genes** is not resolved in the literature — the causal chain above flags this as inferred.
3. **Animal/cellular model coverage specific to KMT2B (as opposed to paralogs KMT2A/KMT2D)** is thin — verify carefully before attaching `modeled_mechanisms` links, given the historical *MLL2/MLL4* naming ambiguity across the gene family.
4. **gnomAD constraint metrics (pLI/LOEUF) for KMT2B** were not directly retrieved — look these up directly at gnomad.broadinstitute.org before including in a Genetic block.
5. **Orphanet ORPHA code** was not confirmed in this search and should be verified directly at orphadata.com before citing.

---

### Sources

- [KMT2B-Related Disorders — GeneReviews®, NCBI Bookshelf (NBK493766)](https://www.ncbi.nlm.nih.gov/books/NBK493766/)
- [Mutations in the histone methyltransferase gene KMT2B cause complex early-onset dystonia — Nature Genetics](https://www.nature.com/articles/ng.3740)
- [KMT2B-related disorders: expansion of the phenotypic spectrum and long-term efficacy of deep brain stimulation — Brain 2020](https://academic.oup.com/brain/article/143/11/3242/5956324)
- [KMT2B-related disorders: expansion of the phenotypic spectrum and long-term efficacy of DBS — 2025 update (arXiv preprint of published paper)](https://arxiv.org/pdf/2502.06320)
- [Adult-onset KMT2B-related dystonia — Brain Communications 2022](https://academic.oup.com/braincomms/article/4/6/fcac276/6775143) / [PMC9724767](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9724767/)
- [KMT2B-Related Dystonia: Challenges in Diagnosis and Treatment — Karger 2022](https://karger.com/msy/article/13/2/159/825171/KMT2B-Related-Dystonia-Challenges-in-Diagnosis-and) / [PMC8928205](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8928205/)
- [KMT2B-related disorders in Austria: clinical features and long-term outcome after DBS — Frontiers in Neurology 2026](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12926133/)
- [Childhood-onset dystonia-causing KMT2B variants result in a specific DNA hypermethylation profile — Clinical Epigenetics 2021](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-021-01145-y)
- [Blood DNA methylation provides an accurate biomarker of KMT2B-related disease — Brain 2022](https://academic.oup.com/brain/article/145/2/644/6378248)
- [Methylation assay in KMT2B-related dystonia: a novel diagnostic validation tool — Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01780-1)
- [Diagnostic utility of DNA methylation episignature analysis for early diagnosis of KMT2B-related disorders: case report — PMC10902455](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10902455/)
- [Are there two disjunct episignatures for KMT2B-related disease? — PMC11631077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11631077/)
- [GPi-DBS for KMT2B-Associated Dystonia: Systematic Review and Meta-Analysis — PubMed 35005062](https://pubmed.ncbi.nlm.nih.gov/35005062/)
- [Deep Brain Stimulation in KMT2B-Related Dystonia: Case Report and Review — PMC8160374](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8160374/)
- [A New Pathologic KMT2B Variant Associated with Childhood Onset Dystonia Presenting as Variable Phenotypes among Family Members — PMC8932353](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8932353/)
- [Variable expressivity of KMT2B variants at codon 2565 — PubMed 39933316](https://pubmed.ncbi.nlm.nih.gov/39933316/)
- [Missense variants causing Wiedemann-Steiner syndrome preferentially occur in the KMT2A-CXXC domain — PMC9249231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9249231/)
- [KMT2B rare missense variants in generalized dystonia — ResearchGate](https://www.researchgate.net/publication/317015962_KMT2B_rare_missense_variants_in_generalized_dystonia)
- [OMIM #617284 — Dystonia 28, Childhood-Onset](https://omim.org/entry/617284)
- [OMIM #619934 — Intellectual Developmental Disorder, Autosomal Dominant 68](https://www.omim.org/entry/619934)
- [OMIM *606834 — KMT2B gene](https://omim.org/entry/606834)
- [Kmt2c/Mll3 Haploinsufficiency Causes Autism-like Behavioral Deficits in Mice — PMC12650575](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12650575/)
- [MLL4 regulates postnatal palate growth and midpalatal suture development — PMC11803150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11803150/)
- [Mutations in Mll2, an H3K4 Methyltransferase, Result in Insulin Resistance — PMC3691224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3691224/)
- [A severe case of status dystonicus caused by a de novo KMT2B missense variant — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1769721220303098)
- [KMT2B-Related Dystonia in Indian Patients With Literature Review](https://www.e-jmd.org/upload/jmd-23035.pdf)
- [Frequency and phenotypic spectrum of KMT2B dystonia in childhood — single-center cohort study, ResearchGate](https://www.researchgate.net/publication/333886384_Frequency_and_phenotypic_spectrum_of_KMT2B_dystonia_in_childhood_A_single-center_cohort_study)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 17 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `DOI:10.1186/s13148-021-01145-y` *(abstract only)*: "indicating a general repression of transcriptional activity"
  - Text part not found as substring: 'indicating a general repression of transcriptional activity' (note: only abstract available for DOI:10.1186/s13148-021-01145-y, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001608` (2 mentions) - the report calls it "Dysphonia"; HP calls it **Abnormality of the voice**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051568` (obsolete histone H3-K4 methylation) (2 mentions)
- `GO:0034968` (obsolete histone lysine methylation) (2 mentions)
- `GO:0006306` (obsolete DNA methylation) (2 mentions)