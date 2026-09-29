---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T14:48:22.831742'
end_time: '2026-08-31T14:52:47.092788'
duration_seconds: 264.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ageing Associated Decline in Intrinsic Capacity
  mondo_id: ''
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
  web_search_requests: 14
  num_turns: 21
  total_cost_usd: 1.2867755999999997
  session_id: f0d65932-8e18-5e63-9164-66d22aa37345
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 61
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 0
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC9819593
  - PMID:31275941
  - PMC:PMC6591451
  relevance_assessed: 42
  on_topic: 19
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 28
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 13
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0031466
    reported_labels:
    - disorientation-related
    ontology_label: Impairment in personality functioning
  - term_id: UBERON:0001846
    reported_labels:
    - columella - inner ear structures, for hearing
    ontology_label: internal ear
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0007568
    ontology_label: obsolete aging
  - term_id: GO:0055114
    ontology_label: obsolete oxidation-reduction process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ageing Associated Decline in Intrinsic Capacity
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ageing Associated Decline in Intrinsic Capacity** covering all of the
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

I have enough material from search snippets and PMC fetches to compile a comprehensive report now. Let me do one more round to fill remaining gaps: sensory/cognitive domain specifics, treatment/ICOPE steps detail, and MONDO/ontology cross-refs.

# Ageing-Associated Decline in Intrinsic Capacity: Comprehensive Research Report

## 1. Disease Information

**Overview.** Intrinsic capacity (IC) is a construct introduced by the World Health Organization (WHO) as "the composite of all physical and mental capacities that a person can draw on... including their biological reserve" ([WHO ICOPE framework](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/)). IC is one of the two pillars (alongside the environment) that determine an older person's **functional ability** in WHO's healthy-ageing model. "Ageing-associated decline in intrinsic capacity" (AADIC) is the clinical entity denoting the age-related, progressive attrition of this composite reserve — a graded, largely subclinical process that precedes and predicts frailty, disability, and death rather than a single-organ disease.

IC is operationalized across **five domains**: *locomotion* (balance, gait, muscle strength), *vitality* (the balance between energy production and consumption — considered an "overarching" domain reflecting underlying biological reserve), *cognition* (memory, intelligence, problem-solving), *psychological* (mood, sociability), and *sensory function* (hearing, vision) ([PubMed scoping review, 2022](https://pubmed.ncbi.nlm.nih.gov/35830956/); [ScienceDirect vitality review, 2025](https://www.sciencedirect.com/science/article/pii/S2260134125000490)).

**Key identifiers:**
- **ICD-11:** `MG2A` — "Ageing associated decline in intrinsic capacity," under General Symptoms/Signs, which replaced the older, non-clinical "old age" designation ([findacode.com](https://www.findacode.com/icd-11/code-835503193.html); [Lancet Healthy Longevity, 2022](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(22)00102-7/fulltext)).
- **WHO framework:** Integrated Care for Older People (ICOPE), published 2017–2019, operationalizing IC screening, assessment and management ([PMC9819593](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/)).
- MONDO/OMIM/Orphanet do not carry dedicated single-gene entries for this construct (it is a geroscience/functional syndrome rather than a Mendelian disease); MONDO indexing, where present, typically cross-references the ICD-11 MG2A code.

**Synonyms/alternative names:** age-related decline in intrinsic capacity; loss of intrinsic capacity; IC decline; (informally, and imprecisely) "biological ageing decline" — distinct from **frailty** and **disability**, discussed in §9 below.

**Data provenance.** Most evidence is derived from **aggregated cohort/population-level resources** — large longitudinal ageing cohorts (UK Biobank, Canadian Longitudinal Study on Aging [CLSA], English Longitudinal Study of Ageing [ELSA], China Health and Retirement Longitudinal Study [CHARLS], I-Lan Longitudinal Aging Study, 10/66 Dementia Research Group cohorts, MAPT study) and WHO ICOPE pilot/implementation studies — rather than individual EHR case reports, since IC is fundamentally a population health/geroscience screening construct.

---

## 2. Etiology

**Disease causal factors.** AADIC is not caused by a single lesion but by the cumulative, multisystem action of the fundamental "hallmarks of aging" (genomic instability, telomere attrition, epigenetic alterations, loss of proteostasis, mitochondrial dysfunction, cellular senescence, stem cell exhaustion, altered intercellular communication, chronic inflammation, and dysbiosis), which erode reserve capacity across the five IC domains in parallel ([Frontiers, hallmarks-of-aging framework, 2024](https://www.frontiersin.org/journals/aging/articles/10.3389/fragi.2024.1334261/full); [PMC12259695, "Targeting the hallmarks of aging," 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259695/)).

### Genetic risk factors
A 2025 genome-wide association study (GWAS; UK Biobank n=44,631 and CLSA n=13,085; total 57,716) found:
- SNP-based heritability of IC: **25.2%** (95% CI 23.2–27.2%) in UK Biobank, **19.5%** (95% CI 14.2–24.8%) in CLSA.
- **38 independent SNPs across 10 novel genomic loci**, mapping ~4,289 candidate SNPs to **197 genes**.
- Lead signal: **rs9891103** near ***MAPT*** (p = 6.50×10⁻¹⁴).
- Other implicated genes: *PTP4A2, PRPF3, LCORL, RN7SL89P, ANAPC10, HK1, DLEU1, SCN4A, STAU1*.
- Implicated pathways: cell cycle/proliferation, apoptosis and cellular senescence, synaptic vesicle trafficking/neuronal plasticity, glucose metabolism/energy production, immune/inflammatory signaling, ubiquitin-proteasome pathway — with tissue enrichment in muscle, brain, heart, adipose, and nerve, matching the five IC domains ([PMC12510315](https://pmc.ncbi.nlm.nih.gov/articles/PMC12510315/); [medRxiv preprint](https://medrxiv.org/cgi/reprint/2025.02.05.25321753v2)).
- APOE genotype and polygenic risk score for dementia interact with baseline IC to modify dementia risk in a UK Biobank prospective cohort ([Neurology, 2024, PMID 38843484](https://pubmed.ncbi.nlm.nih.gov/38843484/)).
- IC assessed via 4 domains combined with genetic risk predicts incident Parkinson disease ([Neurology, 2024](https://www.neurology.org/doi/10.1212/WNL.0000000000214144)).

### Environmental / lifestyle risk factors
- **Physical inactivity/sedentary behavior:** longitudinal data (Seniors-ENRICA-2, Spain) link physical activity and sedentary time to changes in IC trajectory ([Lancet Healthy Longevity, 2024](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00207-1/fulltext)).
- **Diet, smoking, alcohol** are recognized modifiable correlates, though evidence quality for movement-behavior specifically remains limited.
- **Socioeconomic status and sex:** low socioeconomic status and female sex are inversely associated with IC in several cohorts.
- **Living/built environment:** better living environment quality is positively associated with IC.
- **Air pollution (PM1, PM2.5, PM10):** associated with elevated stroke and frailty risk in CHARLS and meta-analytic data, plausibly via systemic inflammation/oxidative stress accelerating sarcopenia and vascular injury ([PMC12159732](https://pmc.ncbi.nlm.nih.gov/articles/PMC12159732/); [Nature Communications, IC-stroke cohort study](https://www.nature.com/articles/s41467-026-70524-x)).
- **Social participation** is protective against IC decline (CHARLS analysis, [MDPI 2026](https://www.mdpi.com/2227-9032/14/7/936)).

### Protective factors
Higher baseline physical activity, social engagement, favorable living environment, and (per the multi-domain intervention trials in §12) structured exercise/nutrition/cognitive-training programs slow or partially reverse IC decline, particularly in pre-frail individuals with lower baseline IC (TIGER trial).

### Gene-environment interaction
The interaction of polygenic dementia risk with IC trajectory (UK Biobank) is the clearest documented G×E-type interaction: genetically high-risk individuals with declining IC show amplified dementia incidence, suggesting IC decline unmasks or accelerates latent genetic risk rather than acting purely additively ([PMID 38843484](https://pubmed.ncbi.nlm.nih.gov/38843484/)).

---

## 3. Phenotypes

IC decline manifests as a constellation of graded (not binary) functional impairments across the five domains, captured operationally by the WHO ICOPE Screening Tool (six practical sub-domains: locomotion, vitality/nutrition, vision, hearing, cognition, psychological/depressive symptoms) ([PMC9945724](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9945724/)).

| Domain | Representative phenotype | Suggested HPO term | Measurement/cutoff |
|---|---|---|---|
| Locomotion | Reduced gait speed | HP:0002136 (Gait disturbance) / HP:0031936 (Slow walking) | <1.0 m/s on 6-meter timed walk |
| Locomotion | Impaired sit-to-stand / muscle weakness | HP:0001324 (Muscle weakness) | Unable to complete 5 chair rises in 14 s |
| Vitality | Unintentional weight loss | HP:0001824 (Weight loss) | Self-reported weight/appetite loss |
| Vitality | Fatigue | HP:0012378 (Fatigue) | Self-report fatigue scales |
| Cognition | Memory impairment | HP:0002354 (Memory impairment) | Failure on 3-word recall |
| Cognition | Disorientation | HP:0031466 (disorientation-related) | Incorrect time/space orientation |
| Psychological | Depressive symptoms | HP:0000716 (Depressivity) | Geriatric Depression Scale items |
| Sensory | Hearing loss | HP:0000365 (Hearing impairment) | Whisper test/audiometry |
| Sensory | Visual impairment | HP:0000505 (Visual impairment) | Self-report/near-vision testing |

**Onset/severity/progression.** Onset is insidious, beginning well before old age in some domains but clinically salient from the 60s–70s; severity is graded and multidimensional (each domain can decline independently); progression is generally gradual but accelerates near end of life — "the magnitude of the inverse association between intrinsic capacity and disability increased as death approached" ([Lancet Healthy Longevity, "dynamic relationship"](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(26)00047-4/fulltext)). A 20-year national longitudinal cohort study describes multiple distinct **IC decline trajectories** rather than one uniform slope ([PMC11567246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11567246/)).

**Frequency.** Pooled meta-analytic prevalence of decreased IC in community-dwelling older adults: **67.8%** (15 studies, n=33,070) in a 2024 meta-analysis ([PMID 39088112](https://pubmed.ncbi.nlm.nih.gov/39088112/)); an earlier 2023 meta-analysis reported a **76.1%** detection rate ([PMID 37543528](https://pubmed.ncbi.nlm.nih.gov/37543528/)) — variability reflects different screening cutoffs/tools across studies.

**Quality of life impact.** IC decline is associated with reduced functional independence, increased hospitalization/institutionalization risk, and lower quality-of-life scores; the vitality domain in particular correlates with fatigue-driven QoL reduction.

---

## 4. Genetic/Molecular Information

- **Causal/associated genes (GWAS loci):** *MAPT* (lead signal), *PTP4A2, PRPF3, LCORL, ANAPC10, HK1, DLEU1, SCN4A, STAU1* (see §2 for details and PMC12510315 citation). These are population-level risk-modifying loci, not single-gene Mendelian causes.
- **Variant classification:** No ACMG/AMP pathogenic-variant framework applies, as IC decline is polygenic/complex rather than Mendelian; GWAS SNPs are common variants of small individual effect (heritability ~20–25% overall).
- **Modifier genes:** *APOE* genotype modifies the relationship between IC and incident dementia ([PMID 38843484](https://pubmed.ncbi.nlm.nih.gov/38843484/)).
- **Epigenetic information:** A blood-based **DNA methylation "IC clock"** has been developed, trained on the five clinical IC domains (cognition, locomotion, psychological well-being, sensory, vitality); this epigenetic IC clock **outperforms earlier epigenetic clocks (e.g., PhenoAge/GrimAge-type) in predicting all-cause mortality** and correlates with clinical, immunological, and lifestyle factors ([Nature Aging, 2025](https://www.nature.com/articles/s43587-025-00883-5); preprint on [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.08.09.607252.full.pdf)).
- **Chromosomal abnormalities:** Not applicable — no described large-scale chromosomal etiology for IC decline as a construct.

**Suggested ontology terms:** GO:0007568 (aging), GO:0090398 (cellular senescence), GO:0006915 (apoptotic process), GO:0005739 (mitochondrion, GO cellular component), GO:0006914 (autophagy).

---

## 5. Environmental Information

- **Environmental/toxic factors:** Ambient air pollution (PM1, PM2.5, PM10) linked to elevated frailty and stroke risk via systemic inflammation/oxidative stress pathways accelerating sarcopenia and vascular injury ([PMC12159732](https://pmc.ncbi.nlm.nih.gov/articles/PMC12159732/)).
- **Lifestyle factors:** Physical inactivity/sedentary behavior, poor diet, smoking, alcohol use, and low social participation are recurrently associated with faster IC decline; conversely, physical activity and social engagement are protective ([Lancet Healthy Longevity, 2024](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00207-1/fulltext); [MDPI, CHARLS](https://www.mdpi.com/2227-9032/14/7/936)).
- **Infectious agents:** Not a primary etiologic category for IC decline per se, though acute infections (e.g., pneumonia, COVID-19) can precipitate abrupt IC drops via post-acute deconditioning and inflammatory insult — an indirect, exacerbating rather than causal-agent relationship.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, numbered)

1. **Cell-intrinsic molecular damage accumulates with age** — genomic instability, telomere attrition, loss of proteostasis, and epigenetic drift — which **leads to** dysfunction of the core cellular machinery of energy production and quality control (largely inferred from the broader hallmarks-of-aging literature and extrapolated to IC; direct human causal proof in IC specifically is largely correlational).
2. **Mitochondrial dysfunction develops** (impaired biogenesis, excess reactive oxygen species [ROS], defective mitophagy, mtDNA mutation accumulation), which **results in** reduced ATP production and amplified oxidative stress ([PMC12531180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12531180/); [PMC10889427](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10889427/)).
3. **Oxidative stress and damage-associated molecular patterns (DAMPs) released via piecemeal mitophagy** **trigger** chronic low-grade sterile inflammation ("inflammaging"), establishing a **vicious cycle** in which mitochondrial dysfunction amplifies ROS generation, which further accelerates cellular senescence ([PMC9246372](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9246372/)).
4. **Chronic inflammation and cellular senescence together drive tissue-specific functional decline**, branching into the five IC domains:
   - **→ Locomotion branch:** inflammaging + mitochondrial dysfunction + hormonal change (e.g., declining anabolic hormones) **lead to** sarcopenia (loss of muscle mass/strength), manifesting as reduced gait speed and muscle weakness.
   - **→ Vitality branch:** impaired mitochondrial oxidative capacity and dysregulated energy/metabolic and neuromuscular/immune-stress-response systems **result in** reduced physiological reserve, fatigue, and anorexia/weight loss — vitality is proposed as the **overarching domain**, since energy-metabolism dysfunction plausibly gates the reserve available to the other four domains ([ScienceDirect, vitality review, 2025](https://www.sciencedirect.com/science/article/pii/S2260134125000490)).
   - **→ Cognition branch:** neuroinflammation, synaptic loss, and (per the GWAS) *MAPT*-related tauopathy-adjacent pathways **contribute to** impaired memory and executive function; this link is corroborated by the *APOE*/polygenic-risk interaction with IC in predicting dementia.
   - **→ Psychological branch:** chronic inflammation and neuroendocrine dysregulation are hypothesized (with weaker direct evidence) to contribute to depressive symptoms and reduced sociability.
   - **→ Sensory branch:** age-related structural degeneration of cochlear hair cells and lens/retina (largely independent, tissue-specific ageing processes) **leads to** hearing and visual impairment, which itself **feeds back to worsen** cognitive and psychological domains (well-documented sensory-cognitive coupling in the broader ageing literature, though the report found less IC-specific direct evidence for this feedback).
5. **The cumulative, cross-domain erosion of reserve constitutes the ageing-associated decline in intrinsic capacity**, which **precedes and predicts** the downstream clinical states of frailty, disability, and mortality (step is empirically demonstrated: IC decline temporally precedes frailty onset in cohort studies).

*Where a step is inferred rather than directly demonstrated for IC as a specific construct (vs. general geroscience), this is noted above (steps 1 and the sensory→cognitive feedback loop) — most of the literature about the general hallmarks-of-aging cascade is generic rather than IC-domain-specific, and the "Biological Rationale for Integrating Intrinsic Capacity Into Frailty Models" review (PMC11890019, not independently readable in this session but summarized in secondary sources) argues IC operationalizes exactly this geroscience cascade clinically.*

### Domain-specific mechanistic detail

- **Molecular pathways:** cell cycle/apoptosis regulation, ubiquitin-proteasome system, synaptic vesicle trafficking, glucose/energy metabolism, immune/NF-κB inflammatory signaling — all nominated by the IC GWAS gene-set enrichment ([PMC12510315](https://pmc.ncbi.nlm.nih.gov/articles/PMC12510315/)).
- **Cellular processes:** cellular senescence (GO:0090398), autophagy/mitophagy (GO:0006914), apoptosis (GO:0006915), chronic low-grade inflammation.
- **Biomarkers under investigation:** interleukin-6 (IL-6), C-reactive protein (CRP), and tumor necrosis factor-alpha (TNF-α) as candidate (but not yet sufficiently specific/sensitive) inflammatory correlates of IC decline; plasma **ATPase Inhibitory Factor 1 (IF1)** studied prospectively in the MAPT cohort as a mitochondrial-function biomarker of IC ([medRxiv](https://www.medrxiv.org/content/10.1101/2022.09.02.22279534.full.pdf)); IGF-1, DHEA, and hemoglobin proposed as vitality/energy-metabolism biomarkers; GDF15 studied in related mitochondrial-myopathy contexts as a correlate of motor function, though not yet established specifically as an IC vitality biomarker ([PMID 38145874](https://pubmed.ncbi.nlm.nih.gov/38145874/); [GeroScience 2023](https://link.springer.com/article/10.1007/s11357-023-00906-2)).
- **Epigenetic profiling:** the DNA-methylation IC clock (Nature Aging, 2025) is the most advanced multi-omic signature to date, integrating methylation data trained against clinical IC domain scores and validated against mortality.

**Suggested GO terms:** GO:0007568 (aging), GO:0090398 (cellular senescence), GO:0006954 (inflammatory response), GO:0005739 (mitochondrion), GO:0055114 (oxidation-reduction process). **CL terms:** CL:0000188 (skeletal muscle myoblast/fiber-related), CL:0000540 (neuron), CL:0000738 (leukocyte, for inflammaging). **UBERON:** UBERON:0001134 (skeletal muscle tissue), UBERON:0000955 (brain), UBERON:0001846 (columella - inner ear structures, for hearing), UBERON:0000970 (eye).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** skeletal muscle (locomotion), brain/CNS (cognition, psychological), inner ear/cochlea (hearing), eye/retina/lens (vision), and systemic metabolic/endocrine organs (vitality — adipose tissue, liver, pancreas contributing to energy balance).
- **Secondary/systemic involvement:** cardiovascular system (via inflammaging and shared risk factors — IC also predicts stroke risk), immune system (chronic low-grade activation).
- **Body systems involved:** musculoskeletal, nervous, sensory, endocrine/metabolic, immune.
- **Tissue/cell level:** skeletal myofibers (sarcopenia), neurons and glia (cognition), cochlear hair cells, retinal/lens cells, adipocytes and hepatocytes (metabolic reserve), circulating immune cells (inflammaging).
- **Subcellular level:** mitochondria (bioenergetic dysfunction — GO:0005739), lysosomes/autophagosomes (impaired proteostasis/mitophagy), nucleus (epigenetic drift, genomic instability).
- **Localization/laterality:** Generally bilateral/systemic and diffuse rather than focal or lateralized, consistent with a whole-organism, multisystem process rather than a localized lesion.

---

## 8. Temporal Development

- **Onset:** insidious ("subacute-to-chronic" in character), beginning in mid-to-late adulthood with detectable domain-specific declines and becoming clinically salient in the 60s onward; some sub-processes (e.g., muscle mass loss) start as early as the 4th–5th decade.
- **Progression:** Not uniform — a 20-year national longitudinal cohort study identified **multiple distinct multi-trajectory patterns of IC decline** (rather than one single trajectory), each with different downstream age-related outcomes ([PMC11567246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11567246/)). The 10/66 cohort natural-history analysis similarly documents domain-specific longitudinal patterns rather than synchronized decline ([PMC10387229](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10387229/)).
- **Course pattern:** generally progressive, though individual domains may show plateau or partial reversibility (particularly with intervention — see §12); decline accelerates as death approaches ("dynamic relationship" with disability, [Lancet Healthy Longevity](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(26)00047-4/fulltext)).
- **Duration:** chronic and, at the population level, essentially universal with advancing age (lifelong once established, absent intervention).
- **Remission:** partial, intervention-induced improvement is documented (see §12) — spontaneous remission is not typical of the underlying biological process, though composite IC scores can improve with rehabilitation of a specific domain (e.g., cataract surgery restoring the sensory domain).
- **Critical periods:** Pre-frail state is repeatedly identified in the literature as the key window of opportunity — the TIGER trial found intervention benefit was **most pronounced among those with greater baseline IC impairment**, suggesting early-to-moderate decline (rather than end-stage decline) is the critical intervention window ([ScienceDirect, TIGER](https://www.sciencedirect.com/science/article/abs/pii/S1525861023008472)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Pooled prevalence of decreased IC among community-dwelling older adults: **67.8%** (2024 meta-analysis, 15 studies, n=33,070; [PMID 39088112](https://pubmed.ncbi.nlm.nih.gov/39088112/)); earlier estimate **76.1%** detection rate ([PMID 37543528](https://pubmed.ncbi.nlm.nih.gov/37543528/)). Estimates vary substantially by screening tool, cutoff, and setting (community vs. inpatient).

**Genetic architecture (not classical Mendelian inheritance — complex/polygenic trait):**
- SNP-heritability ~19.5–25.2% (§2/§4).
- No described penetrance/expressivity framework applies (not a single-gene disorder); genetic anticipation, germline mosaicism, and founder effects are not applicable constructs here.
- Consanguinity role: not established/applicable.
- Carrier frequency: not applicable (polygenic risk, not carrier state).

**Population demographics:**
- Affected populations: all ageing populations globally; the WHO ICOPE framework has been piloted and adopted in diverse settings including China, Singapore, and Latin America/India/China (10/66 cohorts).
- Sex: some studies report higher IC decline burden associated with female sex, though this varies by domain and cohort.
- Age distribution: prevalence and severity increase monotonically with chronological age; the construct is specifically defined for older adults (typically ≥60 years in WHO framework), though sub-clinical decline is measurable earlier.

**Relationship to frailty and disability (conceptual distinction).** IC, frailty, and disability are related but **distinct constructs**:
> "Frailty and IC are complementary, with frailty highlighting the need for specialised care in complex cases, whereas IC supports early intervention and prevention across broader populations" ([PMC6591451, "Frailty and Intrinsic Capacity: Two Distinct but Related Constructs," PMID 31275941](https://pmc.ncbi.nlm.nih.gov/articles/PMC6591451/)).

IC operates at the level of an individual's underlying physical/mental reserve; frailty is the clinical syndrome of accentuated vulnerability arising when that reserve is depleted; disability is the downstream functional/environmental-interaction outcome. Declines in IC frequently **precede** frailty and disability onset, supporting IC's role as an earlier, more modifiable target for prevention ([PMC9819593](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/); [PMC10737867](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10737867/)).

---

## 10. Diagnostics

**WHO ICOPE Screening Tool** (the primary standardized instrument) assesses six practical sub-domains:

| Sub-domain | Screening method |
|---|---|
| Locomotion | 5 chair-rises in ≤14 seconds test; 6-meter timed walk (<1.0 m/s indicates impairment) |
| Cognition | Time/space orientation questions + 3-word recall |
| Vitality/nutrition | Self-reported weight loss and appetite loss |
| Vision | Self-reported visual difficulty / near-vision testing |
| Hearing | Whisper test / self-report |
| Psychological | Depressive symptom screening (e.g., mood questions) |

The tool's sensitivity/specificity performance has been evaluated in multiple validation studies, including the VIMCI study ([PMC9945724](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9945724/)) and a scoping review of sensitivity/specificity across settings ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378512223004243)).

**Laboratory/biomarker tests (research/emerging):**
- Inflammatory panel: IL-6, CRP, TNF-α (candidate, not yet clinically validated for IC-specific staging).
- Mitochondrial-function biomarker: plasma IF1 (research use, MAPT cohort).
- Vitality/energy-metabolism biomarkers: IGF-1, DHEA, hemoglobin.
- **Epigenetic/omics:** blood-based DNA-methylation "IC clock" — a research-stage but promising quantitative composite biomarker correlating with mortality risk ([Nature Aging, 2025](https://www.nature.com/articles/s43587-025-00883-5)).

**Genetic testing:** Not part of routine clinical diagnosis; GWAS-derived polygenic risk scores (for IC itself, or for correlated outcomes like dementia via APOE/PRS) remain research tools.

**Differential diagnosis / distinguishing considerations:** Distinguish IC decline from (a) frailty (a downstream clinical syndrome), (b) disability (functional/environmental outcome), and (c) single-organ disease processes that can mimic domain-specific IC decline (e.g., major depressive disorder mimicking the psychological domain, primary sarcopenia versus disuse atrophy, age-related macular degeneration versus other visual pathology) — the ICOPE approach is explicitly a screening/triage tool, not a diagnostic replacement for organ-specific workup.

**Screening context:** The WHO ICOPE program is structured in five phases: (1) screening for IC decline, (2) in-depth assessment, (3) person-centered care planning, (4) referral, and (5) monitoring; it issues 13 recommendations covering mobility loss, malnutrition, visual/hearing impairment, cognitive impairment, and depressive symptoms, plus modules on urinary incontinence, falls risk, and caregiver support ([PMC9819593](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/); [WHO ICOPE Module 7](https://cdn.who.int/media/docs/default-source/mca-documents/ageing/icope-training-programme/module-7/who-icope_m7_generic-care-pathways_fg.pdf)).

---

## 11. Outcome/Prognosis

IC is a robust, graded predictor of adverse outcomes:

- **Mortality:** In a cohort study, IC was inversely associated with mortality (HR 0.57 per unit increase reported in one analysis); worst-quartile IC associated with **1.48-fold** higher mortality risk (attenuated to 1.41 after adjusting for comorbidity); each 1-point increase in IC score associated with a **5% decrease** in mortality risk; low IC associated with HR **1.94** for mortality in another analysis; deteriorated IC trajectory associated with mortality HR as high as **4.60** in a further longitudinal study ([ScienceDirect, 10-year mortality](https://www.sciencedirect.com/science/article/abs/pii/S0531556522002340); [PMID 35963450](https://pubmed.ncbi.nlm.nih.gov/35963450/); [I-Lan longitudinal aging study, PMC9970311](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9970311/)).
- **Cardiovascular subgroup:** Among older patients with cardiovascular disease, higher IC score associated with lower 5-year all-cause mortality (HR 0.79) ([PMC12415750](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12415750/)).
- **Functional decline meta-analysis:** A 2024 systematic review/meta-analysis of longitudinal studies confirmed IC's association with both functional decline and mortality across pooled cohorts ([PMID 38945130](https://pubmed.ncbi.nlm.nih.gov/38945130/); [Lancet Healthy Longevity](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00092-8/fulltext)).
- **Dementia/neurodegeneration:** IC decline (especially combined with high polygenic dementia risk or APOE ε4 status) predicts incident dementia and Parkinson disease ([PMID 38843484](https://pubmed.ncbi.nlm.nih.gov/38843484/); [Neurology 2024, PD](https://www.neurology.org/doi/10.1212/WNL.0000000000214144); [Sydney Memory and Ageing Study, PMC12560156](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12560156/)).
- **Stroke risk:** IC is independently associated with incident stroke across multiple cohorts ([Nature Communications](https://www.nature.com/articles/s41467-026-70524-x)).
- **Longevity (extreme age):** IC in the 70–100 age range independently associated with longevity outcomes ([PMC12759399](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12759399/)).
- **Complications:** Higher risk of falls, geriatric syndromes (urinary incontinence), hospitalization, institutionalization, and progression to frailty/disability.
- **Prognostic biomarkers:** The DNA-methylation IC clock outperforms prior epigenetic clocks for mortality prediction, suggesting future clinical utility as a prognostic biomarker.

---

## 12. Treatment

IC decline is managed through **multidomain, person-centered prevention/rehabilitation** rather than pharmacotherapy targeted at a single disease mechanism, consistent with its status as a functional-reserve construct rather than a discrete disease.

**Multidomain lifestyle/behavioral interventions (NCIT:C181743 Behavioral Counseling / NCIT:C15302 Physical Therapy / NCIT:C15447 Dietary Intervention):**
- Combined exercise + cognitive stimulation therapy significantly improved IC composite score and locomotion, vitality, cognition, and psychological sub-scores in pre-frail older adults ([PMC12275792, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12275792/)).
- **TIGER trial** (Taiwan, n=1,054): 12-month multidomain intervention (exercise, nutrition, cognitive/social engagement) significantly mitigated cognitive decline and physical frailty, with the largest benefit in those with the greatest baseline IC impairment ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1525861023008472)).
- **ENHANCE RCT:** 12-month group-based multidomain intervention (exercise, cognitive training, nutrition education) targeting brain structure/function ([PMC12134766](https://pmc.ncbi.nlm.nih.gov/articles/PMC12134766/)).
- **MIDA study** (n=248, ages 60–85): multidomain cognitive training + exercise + nutritional guidance, 12-month follow-up ([Tandfonline, 2025](https://www.tandfonline.com/doi/full/10.1080/07853890.2025.2496409)).
- Multidomain lifestyle counseling RCT in older women showed improved IC ([Aging Clinical and Experimental Research, 2025](https://link.springer.com/article/10.1007/s40520-025-03282-3)).
- Smart-care platform–delivered multi-domain interventions are being tested in ongoing RCT protocols ([BMC Geriatrics protocol](https://link.springer.com/article/10.1186/s12877-026-07210-6)).
- A non-randomized controlled study found **baseline IC itself (rather than intervention exposure)** was the stronger predictor of reversal to robustness among prefrail adults, underscoring IC's role as both a target and a prognostic moderator of intervention response ([PMID 36341237](https://pubmed.ncbi.nlm.nih.gov/36341237/)).

**Domain-specific treatment (NCIT terms):**
- Locomotion/sarcopenia: resistance/endurance exercise (NCIT:C15302 Physical Therapy), nutritional protein supplementation, and — in emerging research — pharmacological agents targeting mitochondrial health, senolytics, and exerkines ([PMC12531180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12531180/)).
- Sensory: cataract surgery, hearing aid provision (device-based; per this repo's convention, bind the surgical/clinical action term, e.g., NCIT:C15329 Surgical Procedure, and capture the device via a qualifier).
- Cognitive/psychological: cognitive stimulation therapy, behavioral counseling, social-engagement programs.
- Vitality: dietary/nutritional intervention (NCIT:C15447), management of underlying inflammatory/metabolic drivers.

**Experimental/advanced therapeutics:** Senolytics, exerkines, and gene-therapy approaches targeting mitochondrial dysfunction are cited as emerging, largely pre-clinical/early-clinical strategies for the sarcopenia component of IC decline; no disease-modifying pharmacotherapy is yet approved specifically for "IC decline" as an indication.

**Treatment outcomes:** Multidomain interventions show consistent, modest-to-moderate improvement in IC composite and domain scores, with the strongest benefit in pre-frail (moderately impaired) individuals — reinforcing the "critical period" concept in §8. A 2024 Lancet Healthy Longevity commentary argues the field has established that "intrinsic capacity assessment works" and the priority now is translating assessment into scaled clinical/public-health action ([Lancet Healthy Longevity commentary, 2024](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00110-7/fulltext)).

---

## 13. Prevention

- **Primary prevention:** population-level promotion of physical activity, healthy diet, social participation, and reduction of environmental exposures (air pollution) to preserve IC reserve before decline is clinically detectable.
- **Secondary prevention (screening/early detection):** WHO ICOPE screening tool deployment in primary care and community settings as a systematic early-detection strategy — this is the centerpiece of the WHO's global healthy-ageing strategy.
- **Tertiary prevention:** the multidomain intervention programs in §12, aimed at preventing progression from IC decline to frailty and disability once impairment is identified.
- **Risk stratification:** combining IC screening with genetic/polygenic risk information (e.g., dementia PRS + APOE) is an emerging risk-stratification approach to target intensive prevention to the highest-risk subgroups.
- **Behavioral interventions:** exercise and social-participation programs are the most consistently evidence-supported behavioral prevention strategy.
- **Public health:** WHO's ICOPE framework itself functions as a public-health/health-systems intervention, having been piloted and adapted in multiple countries (China, Singapore, Latin America, India) as national/regional healthy-ageing policy ([PMC9819593, narrative review of global ICOPE adoption](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/)).
- **Environmental interventions:** reducing air pollution exposure is supported as a modifiable public-health lever given documented associations with frailty/stroke risk.

---

## 14. Other Species / Natural Disease

IC is increasingly being operationalized as a **translational geroscience construct** in non-human species:

- A 2026 narrative review specifically examines **IC evolution during aging in mouse and fish models**, summarizing measurement approaches for each of the five IC domains and describing longitudinal IC trajectories in these organisms — explicitly framed as supporting "bidirectional translation" between preclinical geroscience models and human IC ([ScienceDirect, 2026](https://www.sciencedirect.com/science/article/abs/pii/S1568163726001753)).
- **Taxonomy:** *Mus musculus* (NCBITaxon:10090), zebrafish/other fish models (NCBITaxon varies by species) are the principal model organisms used.
- **Orthologous genes:** Mouse orthologs of the human GWAS-implicated genes (*Mapt*, *Hk1*, *Scn4a*, etc.) are used in preclinical mechanistic work on sarcopenia, neurodegeneration, and metabolic decline, though a dedicated ortholog-mapping study specific to IC as a composite trait was not identified in this search.
- **Comparative biology:** the hallmarks-of-aging framework underlying IC decline (mitochondrial dysfunction, cellular senescence, inflammaging) is evolutionarily conserved, supporting cross-species mechanistic inference, though the search did not surface IC-specific naturally-occurring veterinary disease reports (e.g., OMIA entries) — IC as formally defined is a human/WHO clinical construct, and its animal-model literature is explicitly a translational adaptation rather a naturally arising veterinary diagnosis.

---

## 15. Model Organisms

- **Mouse Frailty Index (FI):** The most mature translational tool. Based on cumulative deficit accumulation (originally ~31 invasive/non-invasive measures), the mouse FI shows a characteristic distribution, similar values at comparable life stages, a dose-response relationship with mortality, and a submaximal limit — closely paralleling human deficit-accumulation frailty indices ([Scientific Reports, PMID via Nature "srep43068"](https://www.nature.com/articles/srep43068); [PMC4271019, "Clinically Relevant Frailty Index for Mice"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4271019/)). A streamlined, non-invasive FI protocol allows rapid, longitudinal assessment of large mouse cohorts without specialized equipment, enhancing translational throughput for geroscience intervention studies ([PMID 28463656](https://pubmed.ncbi.nlm.nih.gov/28463656/)).
- **Fish models:** used alongside mice in the 2026 comparative IC-trajectory review, offering a shorter-lived, high-throughput complementary system for longitudinal multi-domain functional aging assessment.
- **Model characteristics:** Mouse FI and emerging IC-domain measures reasonably recapitulate human functional decline trajectories and mortality dose-response relationships, but **limitations** include incomplete capture of subjective/psychological domains (mood, sociability are harder to operationalize in rodents) and species differences in lifespan/pace-of-ageing that complicate direct translation of intervention timing.
- **Applications:** these models are used to test candidate geroscience interventions (senolytics, exercise mimetics, mitochondrial-targeted compounds, caloric restriction) for their effect on multidomain functional reserve before human trials, and to dissect causal mechanistic steps (e.g., mitochondrial dysfunction → sarcopenia) that are only correlational in human cohort data.
- **Resources:** Mouse Genome Informatics (MGI) and International Mouse Phenotyping Consortium (IMPC) resources support genetic (knockout/conditional) models of individual hallmark-of-aging genes (e.g., mitochondrial quality-control genes) relevant to IC-domain-specific mechanisms, though no centralized "IC model organism" database currently exists analogous to disease-specific OMIA/IMPC catalogs.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| ICD-11 | MG2A (Ageing associated decline in intrinsic capacity) |
| HPO | HP:0002136 (Gait disturbance), HP:0001324 (Muscle weakness), HP:0001824 (Weight loss), HP:0012378 (Fatigue), HP:0002354 (Memory impairment), HP:0000716 (Depressivity), HP:0000365 (Hearing impairment), HP:0000505 (Visual impairment) |
| GO (Biological Process) | GO:0007568 (aging), GO:0090398 (cellular senescence), GO:0006954 (inflammatory response), GO:0006914 (autophagy), GO:0055114 (oxidation-reduction process) |
| GO (Cellular Component) | GO:0005739 (mitochondrion) |
| CL | CL:0000188 (skeletal myofiber-related), CL:0000540 (neuron), CL:0000738 (leukocyte) |
| UBERON | UBERON:0001134 (skeletal muscle tissue), UBERON:0000955 (brain), UBERON:0000970 (eye) |
| HGNC | MAPT (HGNC:6893), PTP4A2, PRPF3, LCORL, ANAPC10, HK1, DLEU1, SCN4A, STAU1 |
| NCIT (treatment) | NCIT:C15302 (Physical Therapy), NCIT:C15447 (Dietary Intervention), NCIT:C181743 (Behavioral Counseling), NCIT:C15329 (Surgical Procedure), NCIT:C15986 (Pharmacotherapy) |

---

## Sources

- [Exploring the conceptual framework and measurement model of intrinsic capacity defined by the WHO: A scoping review (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35830956/)
- [The vitality domain of intrinsic capacity: A scoping review (ScienceDirect, 2025)](https://www.sciencedirect.com/science/article/pii/S2260134125000490)
- [Exploring the natural history of intrinsic capacity impairments: 10/66 study (PMC10387229)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10387229/)
- [Use of Intrinsic Capacity Domains as a Screening Tool in Public Health (PMC10002144)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10002144/)
- [Estimating the prevalence of intrinsic capacity decline: systematic review/meta-analysis (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2950307824000298)
- [The WHO ICOPE Framework: narrative review on global adoption (PMC9819593)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9819593/)
- [Intrinsic capacity of older people in the community using ICOPE framework (PMC8993034)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8993034/)
- [Intrinsic capacity assessment works—let's move on actions (Lancet Healthy Longevity, 2024)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00110-7/fulltext)
- [Association between aging-related biomarkers and longitudinal trajectories of IC (GeroScience, 2023)](https://link.springer.com/article/10.1007/s11357-023-00906-2)
- [From biological aging to functional decline: chronic inflammation and IC (PubMed 38145874)](https://pubmed.ncbi.nlm.nih.gov/38145874/)
- [Plasma IF1 and intrinsic capacity: MAPT Study (medRxiv)](https://www.medrxiv.org/content/10.1101/2022.09.02.22279534.full.pdf)
- [Targeting the hallmarks of aging: mechanisms and therapeutic opportunities (PMC12259695)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259695/)
- [The hallmarks of aging as a conceptual framework (Frontiers, 2024)](https://www.frontiersin.org/journals/aging/articles/10.3389/fragi.2024.1334261/full)
- [The Biological Rationale for Integrating Intrinsic Capacity Into Frailty Models (PMC11890019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11890019/)
- [A blood-based epigenetic clock for intrinsic capacity (Nature Aging, 2025)](https://www.nature.com/articles/s43587-025-00883-5)
- [Prevalence of intrinsic capacity decline among community-dwelling older adults (PMID 39088112)](https://pubmed.ncbi.nlm.nih.gov/39088112/)
- [Association of intrinsic capacity with functional decline and mortality (PMID 38945130 / Lancet Healthy Longevity)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00092-8/fulltext)
- [A genome-wide association study identified 10 novel genomic loci for IC (PMC12510315)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12510315/)
- [Intrinsic Capacity Defined Using 4 Domains, Genetic Risk, and Incident Parkinson Disease (Neurology, 2024)](https://www.neurology.org/doi/10.1212/WNL.0000000000214144)
- [Detection rate of decreased intrinsic capacity (PMID 37543528)](https://pubmed.ncbi.nlm.nih.gov/37543528/)
- [Intrinsic Capacity, Polygenic Risk Score, APOE Genotype, and Risk of Dementia (Neurology, 2024)](https://www.neurology.org/doi/10.1212/WNL.0000000000209452)
- [MG2A Ageing associated decline in intrinsic capacity — ICD-11 MMS](https://www.findacode.com/icd-11/code-835503193.html)
- [How "old age" was withdrawn as a diagnosis from ICD-11 (Lancet Healthy Longevity, 2022)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(22)00102-7/fulltext)
- [The Impact of Exercise and Cognitive Stimulation Therapy on IC Composite Score (PMC12275792)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12275792/)
- [Intrinsic capacity rather than intervention exposure influences reversal to robustness (PMID 36341237)](https://pubmed.ncbi.nlm.nih.gov/36341237/)
- [ENHANCE Trial (PMC12134766)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12134766/)
- [Effectiveness of multidomain lifestyle counseling on IC in older women (Aging Clin Exp Res, 2025)](https://link.springer.com/article/10.1007/s40520-025-03282-3)
- [MIDA study protocol (2025)](https://www.tandfonline.com/doi/full/10.1080/07853890.2025.2496409)
- [Enhancing IC via Integrated Multidomain Interventions: TIGER Trial (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1525861023008472)
- [Multi-domain interventions via smart-care platform: RCT protocol (BMC Geriatrics)](https://link.springer.com/article/10.1186/s12877-026-07210-6)
- [Frailty and Intrinsic Capacity: Two Distinct but Related Constructs (PMC6591451)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6591451/)
- [Intrinsic capacity and disability before death: a dynamic relationship (Lancet Healthy Longevity)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(26)00047-4/fulltext)
- [Associations of intrinsic capacity, fall risk and frailty in old inpatients (PMC10598390)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10598390/)
- [Mitochondrial dysfunction in age-related sarcopenia (PMC12531180)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12531180/)
- [Mitochondrial dysfunction in cell senescence and aging (PMC9246372)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9246372/)
- [Mitochondrial Quantity and Quality in Age-Related Sarcopenia (PMC10889427)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10889427/)
- [Intrinsic capacity and 10-year mortality (ScienceDirect / PMID 35963450)](https://pubmed.ncbi.nlm.nih.gov/35963450/)
- [Intrinsic capacity differs from functional ability in predicting 10-year mortality: I-Lan study (PMC9970311)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9970311/)
- [Impact of Intrinsic Capacity on 5-year Mortality in CVD patients (PMC12415750)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12415750/)
- [Multi-Trajectories of Intrinsic Capacity Decline: 20-Year Cohort (PMC11567246)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11567246/)
- [Intrinsic capacity evolution during aging in mouse and fish (ScienceDirect, 2026)](https://www.sciencedirect.com/science/article/abs/pii/S1568163726001753)
- [Clinically Relevant Frailty Index for Mice (PMC4271019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4271019/)
- [A Frailty Index Based On Deficit Accumulation Quantifies Mortality Risk in Humans and Mice (Sci Rep)](https://www.nature.com/articles/srep43068)
- [Implementation of the mouse frailty index (PMID 28463656)](https://pubmed.ncbi.nlm.nih.gov/28463656/)
- [Association between physical activity/sedentary behaviour and IC changes: Seniors-ENRICA-2 (Lancet Healthy Longevity, 2024)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00207-1/fulltext)
- [Systematic review/meta-analysis of air pollution and frailty risk (PMC12159732)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12159732/)
- [Intrinsic capacity and stroke risk in a multiple cohort study (Nature Communications)](https://www.nature.com/articles/s41467-026-70524-x)
- [Association Between Social Participation, Physical Activity, and IC Decline: CHARLS (MDPI)](https://www.mdpi.com/2227-9032/14/7/936)
- [Identification of decreased intrinsic capacity: ICOPE Screening tool performance, VIMCI study (PMC9945724)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9945724/)
- [WHO ICOPE Generic Care Pathways and Screening, Module 7](https://cdn.who.int/media/docs/default-source/mca-documents/ageing/icope-training-programme/module-7/who-icope_m7_generic-care-pathways_fg.pdf)
- [Sensitivity/specificity of ICOPE screening tool, prevalence of IC loss: scoping review (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0378512223004243)
- [A multidimensional biomarker model of vitality and its associations with IC and frailty (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1279770726001260)
- [Resilience and Intrinsic Capacity in Older Adults: A Review of Recent Literature (PMC12608230)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12608230/)
- [Intrinsic Capacity to Predict Future Adverse Health Outcomes: Scoping Review (PMC9957180)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9957180/)
- [Intrinsic Capacity Predictors of Dementia and Mortality: Sydney Memory and Ageing Study (PMC12560156)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12560156/)
- [Intrinsic Capacity And Longevity From Age 70-100 (PMC12759399)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12759399/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 42 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9819593` *(abstract only)*: "the composite of all physical and mental capacities that a person can draw on... including their biological reserve"
  - Text part not found as substring: 'the composite of all physical and mental capacities that a person can draw on' (note: only abstract available for PMID:36612480, full text may contain this excerpt)
- `PMID:31275941`: "Frailty and IC are complementary, with frailty highlighting the need for specialised care in complex cases, whereas IC supports early intervention and prevention across broader populations"
  - closest text in source: "Both frailty and IC are focused at promoting the development of person-centered care plans (ability in detecting one's impairments, needs and preferences) and lead to tailored care/healthy strategies to reverse, slow or arrest the losses"
- `PMC:PMC6591451`: "Frailty and IC are complementary, with frailty highlighting the need for specialised care in complex cases, whereas IC supports early intervention and prevention across broader populations"
  - closest text in source: "Both frailty and IC are focused at promoting the development of person-centered care plans (ability in detecting one's impairments, needs and preferences) and lead to tailored care/healthy strategies to reverse, slow or arrest the losses"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031466` (1 mention) - the report calls it "disorientation-related"; HP calls it **Impairment in personality functioning**
- `UBERON:0001846` (1 mention) - the report calls it "columella - inner ear structures, for hearing"; UBERON calls it **internal ear**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007568` (obsolete aging) (3 mentions)
- `GO:0055114` (obsolete oxidation-reduction process) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000716` (2 mentions) - the report calls it "Depressivity"; HP calls it **Depression**, and lists "Depressivity" among its other names
- `GO:0007568` (3 mentions) - the report calls it "aging"; GO calls it **obsolete aging**, and lists "ageing" among its other names
- `GO:0090398` (4 mentions) - the report calls it "cellular senescence", "Cellular processes:** cellular senescence"; GO calls it **cellular senescence**
- `GO:0005739` (4 mentions) - the report calls it "mitochondrion, GO cellular component", "mitochondrion"; GO calls it **mitochondrion**
- `GO:0055114` (2 mentions) - the report calls it "oxidation-reduction process"; GO calls it **obsolete oxidation-reduction process**
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle myoblast/fiber-related"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000738` (2 mentions) - the report calls it "leukocyte, for inflammaging"; CL calls it **leukocyte**
- `NCIT:C15447` (3 mentions) - the report calls it "Vitality: dietary/nutritional intervention"; NCIT calls it **Dietary Intervention**, and lists "Nutritional Interventions" among its other names
- `NCBITaxon:10090` (1 mention) - the report calls it "Mus musculus", "Taxonomy:** *Mus musculus"; NCBITaxon calls it **Mus musculus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0090398` - called "cellular senescence", "Cellular processes:** cellular senescence"
- `GO:0005739` - called "mitochondrion, GO cellular component", "mitochondrion"
- `NCBITaxon:10090` - called "Mus musculus", "Taxonomy:** *Mus musculus"