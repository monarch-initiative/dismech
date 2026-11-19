---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:21.821526'
end_time: '2026-11-18T23:35:58.871874'
duration_seconds: 337.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 3
  mondo_id: MONDO:0014132
  category: Mendelian
  causal_genes: IBA57
  omim_id: OMIM:615330
  synonyms: IBA57 deficiency; IBA57 fatal multiple mitochondrial dysfunctions syndrome;
    fatal multiple mitochondrial dysfunctions syndrome caused by mutation in IBA57;
    multiple mitochondrial dysfunctions syndrome type 3
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
  web_search_requests: 6
  num_turns: 34
  total_cost_usd: 1.2104751999999999
  session_id: 14580e2c-af9f-484c-a690-10ef80a9cd4a
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 33
  retrieval_calls: 31
  assistant_text_blocks: 3
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 9
reference_validation:
  total_references: 35
  verified: 34
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.029
  quotes_checked: 22
  quotes_valid: 18
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:30269484
  - PMID:32817474
  - PMID:22323289
  - PMID:37588046
  relevance_assessed: 34
  on_topic: 28
  unresolved_references:
  - PMID:29343425
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 73
  verified: 69
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 5
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0014132
    reported_labels:
    - MONDO
    ontology_label: multiple mitochondrial dysfunctions syndrome 3
  - term_id: DOID:0080135
    reported_labels:
    - DOID
    ontology_label: multiple mitochondrial dysfunctions syndrome 3
  - term_id: HP:0003324
    reported_labels:
    - Sign
    ontology_label: Generalized muscle weakness
  - term_id: HP:0000252
    reported_labels:
    - Physical
    ontology_label: Microcephaly
  - term_id: HP:0011968
    reported_labels:
    - Symptom
    ontology_label: Feeding difficulties
  - term_id: HP:0012706
    reported_labels:
    - Imaging/lab
    ontology_label: Elevated brain choline level by MRS
  - term_id: HP:0002376
    reported_labels:
    - Sign
    ontology_label: Developmental regression
  - term_id: HP:0009830
    reported_labels:
    - Sign
    ontology_label: Peripheral neuropathy
  - term_id: HP:0001250
    reported_labels:
    - Sign
    ontology_label: Seizure
  - term_id: HP:0032480
    reported_labels:
    - Lab
    ontology_label: Beta-aminoisobutyric aciduria
  - term_id: HP:6000830
    reported_labels:
    - Lab
    ontology_label: Diminished alpha-ketoglutarate dehydrogenase activity in cultured
      fibroblasts
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 3
- **MONDO ID:** MONDO:0014132 (if available)
- **Causal gene(s):** IBA57
- **OMIM:** OMIM:615330
- **Synonyms:** IBA57 deficiency; IBA57 fatal multiple mitochondrial dysfunctions syndrome; fatal multiple mitochondrial dysfunctions syndrome caused by mutation in IBA57; multiple mitochondrial dysfunctions syndrome type 3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 3** covering all of the
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

Still collecting abstracts for the IBA57 literature; next I'll pull the full abstract texts directly so I can quote them exactly.

I've pulled the identifiers (HGNC, UniProt, MONDO) and the key patient and mechanism papers. Now I'm checking the SPG74 cross-reference, HPO annotations and ClinVar, then I'll write the report.

I found 65 PubMed records for IBA57 and pulled abstracts or quotes from about 35 of them. Your template has 15 sections; I combined some of them and don't cover every database it lists. This was a single run, and I could not reach OMIM, Orphanet, NCBI Gene or gnomAD directly.

# Multiple Mitochondrial Dysfunctions Syndrome 3 (MMDS3; MONDO:0014132): Research Report

**Scope.** This report covers MONDO:0014132 / OMIM #615330, caused by biallelic variants in **IBA57** (HGNC:27302; OMIM gene \*615316; chromosome 1q42.13). The same gene also causes autosomal recessive **spastic paraplegia 74 (SPG74; OMIM #616451; MONDO:0014644)**. Many recent papers report MMDS3 and SPG74 together as one IBA57 spectrum, so I mention SPG74 where it helps but keep MMDS3 as the target.

**Evidence and access limits:**
- OMIM, Orphanet's own page and NCBI Gene were blocked (HTTP 403 or a bot check).
- The PubMed text-fetch tool would only return short verbatim excerpts, under about 120 characters. The "quotes" below are exact excerpts of that length, not full abstracts.
- Anything I could not retrieve is marked as not available.

---

## 1. Disease Information

**Overview.** MMDS3 is an autosomal recessive mitochondrial disorder of energy metabolism. It is caused by loss of function of IBA57, a late-acting factor in mitochondrial iron–sulfur (Fe‑S) cluster assembly that is needed to build [4Fe‑4S] proteins.
- UniProt Q5T440 describes MMDS3 as a severe energy metabolism disorder with weakness, respiratory failure, lactic acidosis, hyperglycinemia and early death. Its biochemistry is deficiency of the 2‑oxoacid dehydrogenases, defective lipoic acid synthesis and reduced respiratory chain activity ([UniProt Q5T440](https://rest.uniprot.org/uniprotkb/Q5T440.txt)).
- The first family had "Two siblings from consanguineous parents died perinatally with a condition characterized by generalized hypotonia" (PMID 23462291, Ajit Bolar et al., *Hum Mol Genet* 2013).
- The clinical range has since widened greatly. It runs from fatal neonatal disease, to infantile cavitating leukoencephalopathy with stabilization, to childhood-onset spastic paraplegia, to almost asymptomatic adults (PMIDs 25609768, 28671726, 30258207, 39227420).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0014132 | [OLS/MONDO](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0014132) |
| OMIM (phenotype) | 615330 | MONDO xref |
| Orphanet | ORPHA:363424 | MONDO xref |
| DOID | DOID:0080135 | MONDO xref |
| GARD | 17555 | MONDO xref |
| MedGen / UMLS | 815495 / C3809165 | MONDO xref |
| Allelic disorder | SPG74, OMIM #616451; MONDO:0014644; ORPHA:468661 | [LOVD](https://databases.lovd.nl/shared/diseases/04507), [CISMeF](https://www.cismef.org/page/detail/en/MIM_PH_616451) |
| ICD-10 / ICD-11 / MeSH | Not retrieved | Orphanet page was blocked. ICD-10 E88.8 is plausible for Orphanet MMDS entries but **not verified**. |

- **MONDO definition:** "Any fatal multiple mitochondrial dysfunctions syndrome in which the cause of the disease is a mutation in the IBA57 gene."
- **Synonyms (MONDO):** MMDS3; IBA57 deficiency; IBA57 fatal multiple mitochondrial dysfunctions syndrome; fatal multiple mitochondrial dysfunctions syndrome caused by mutation in IBA57; multiple mitochondrial dysfunctions syndrome type 3. A third-party Orphanet mirror also lists "Hypotonia‑cerebral atrophy‑hyperglycinemia syndrome" ([PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/5369)).
- **Data source type:** Everything here comes from published case reports and case series, plus curated disease-level resources (OMIM, Orphanet, HPO, MONDO, UniProt). There are no EHR-derived or registry datasets.

---

## 2. Etiology

**Primary cause.** Biallelic germline pathogenic variants in IBA57. These are missense, frameshift, nonsense, splice and small in-frame duplication variants. They reduce IBA57 protein level or function (PMIDs 23462291, 25971455, 27785568, 28913435).
- "Severely decreased amounts of IBA57 protein were observed in skeletal muscle and cultured skin fibroblasts" (PMID 23462291).
- For p.Arg146Trp, the variant "was unable to restore the biochemical phenotype indicating a loss-of-function mutation of IBA57" (PMID 25971455, Debray et al., *J Inherit Metab Dis* 2015).

**Genetic risk factors**
- **Consanguinity.** The index families were consanguineous (PMIDs 23462291, 25609768).
- **Founder and recurrent alleles.** In Chinese patients, c.286T>C (p.Tyr96His) is a hotspot: "The c.286 T > C mutation was reported in 85.2% of Chinese patients" (PMID 39227420, Jiang et al., *J Hum Genet* 2024). c.310G>T (p.Gly104Cys) recurs in homozygous and compound heterozygous severe cases (PMIDs 39408793, 36360281, 42544324).
- **Genotype and residual protein.** In SPG74, higher residual IBA57 is linked to milder disease: lymphoblasts "contained 10-fold-lower levels of wild-type, but no signs of truncated IBA57 protein" (PMID 25609768).

**Environmental risk factors.** No primary environmental cause is known. One reported environmental *trigger* exists: in an SPG74/IBA57 patient, "he then developed a rapidly progressive spastic paraparesis following a febrile illness" (PMID 30258207, Hamanaka et al. 2018). HPO also lists "Recurrent fever." Infection or fever as a decompensation trigger is typical of mitochondrial disease, but for IBA57 it rests on case-level evidence only.

**Protective factors.** No genetic or environmental protective factors are known.
- Chinese patients carrying c.286T>C had lower mortality (P = 0.002 vs non-Chinese) (PMID 39227420). This suggests the allele is relatively mild, not that it protects.

**Gene–environment interactions.** No studies found. In yeast, loss of the Fe‑S assembly system makes cells more sensitive to oxidative stress induced by ethanol (PMID 24028658, *FEMS Yeast Res* 2013, title-level evidence). This is model data only.

---

## 3. Phenotypes

**Onset and course by subtype.** PMID 39227420 (61 IBA57 patients, 46 with MMDS3) proposes three subtypes:
- **Neonatal:** "Neonatal cases universally displayed hypotonia and respiratory distress at presentation, deceased within three months."
- **Infantile:** Most often onset around 9–11 months with motor regression.
  - "The median age at disease onset was 11 months" (PMID 30770271).
  - Median onset was 9 months with motor regression (PMID 28671726).
- **Childhood:** Overlaps with SPG74. "Fifteen cases from three families manifested the spastic paraplegia 74 phenotype"; spastic paraplegia 14/15, visual impairment 10/13, peripheral neuropathy 9/13 (PMID 39227420).

**Phenotype table.** HPO terms are those annotated to OMIM:615330 ([HPO/JAX annotation API](https://ontology.jax.org/api/network/annotation/OMIM:615330)). Frequencies are the HPO counts, or literature counts where cited.

| Phenotype | Type | HPO | Frequency / notes | Source |
|---|---|---|---|---|
| Hypotonia; severe muscular hypotonia | Sign | HP:0001252; HP:0006829 | 2/2 (index); universal in neonatal subtype | PMIDs 23462291, 39227420 |
| Generalized muscle weakness / myopathy | Sign | HP:0003324 | 1/2 | PMID 23462291 |
| Respiratory insufficiency / failure | Sign | HP:0002093; HP:0002878 | Universal in neonatal subtype; a major cause of death | PMID 39227420 |
| Polyhydramnios; IUGR; arthrogryposis multiplex congenita; congenital onset | Prenatal | HP:0001561; HP:0001511; HP:0002804; HP:0003577 | 2/2 (index siblings) | PMID 23462291 (via HPO) |
| Microcephaly | Physical | HP:0000252 | 2/2 | HPO |
| Dysmorphism: retrognathia, high palate, wide intermamillary distance | Physical | HP:0000278; HP:0000218; HP:0006610 | 1/2 each | HPO |
| Feeding difficulties | Symptom | HP:0011968 | 2/2 | HPO |
| Leukodystrophy / cavitating leukoencephalopathy | Imaging | HP:0002415 (consider HP:0002352, leukoencephalopathy) | Near-universal in infantile form. "Brain MRI was characterized by cavitating leukodystrophy." | PMIDs 27785568, 28671726 |
| Polymicrogyria; ventriculomegaly; corpus callosum hypoplasia; cerebral atrophy | Imaging | HP:0002126; HP:0002119; HP:0002079; HP:0002059 | 1/1 to 2/2. "Brain imaging revealed cortical malformation with polymicrogyria" | PMIDs 37903659, 34709542 |
| Elevated brain choline on MRS | Imaging/lab | HP:0012706 | 1/1 | HPO |
| Developmental (motor) regression | Sign | HP:0002376 | Most infantile cases | PMIDs 28671726, 39227420 |
| Spastic tetraplegia / spastic paraplegia | Sign | HP:0002510 / HP:0001258 | SPG74: 14/15 | PMID 39227420 |
| Optic atrophy; visual impairment; nystagmus | Sign | HP:0000648; HP:0000505; HP:0000639 | SPG74 visual impairment 10/13; optic atrophy can be the only sign in adults | PMIDs 30258207, 39227420 |
| Peripheral neuropathy | Sign | HP:0009830 | SPG74: 9/13 | PMID 39227420 |
| Seizures | Sign | HP:0001250 | Very rare (HPO); epilepsy in a Japanese girl | PMID 30258207 |
| Cognitive impairment; irritability | Behavioral | HP:0100543; HP:0000737 | Communication, problem-solving or personal-social delay in 52.9–71.4% | PMID 28671726 |
| Lactic acidosis; increased CSF lactate; elevated lactate:pyruvate ratio | Lab | HP:0003128; HP:0002490; HP:0032653 | 1/1 (HPO). Blood lactate 2.50 mmol/L in one case | PMID 38923322 |
| Hyperglycinemia; increased CSF glycine | Lab | HP:0002154; HP:0500230 | 1/1; 2/2 | PMID 34440194 ("high lactate, pyruvate, and glycine levels in body fluids") |
| Beta-aminoisobutyric aciduria; urinary 2‑hydroxy‑ and 2‑ketoadipic acids | Lab | HP:0032480 | Case-level | PMID 37903659 |
| Decreased activity of complex I and complex II | Lab | HP:0011923; HP:0008314 | 2/2. "All patients presented with combined or isolated defect of complex I and II." | PMID 27785568 |
| Diminished α‑ketoglutarate dehydrogenase activity | Lab | HP:6000830 | — | HPO |

- **Severity:** Severe to lethal in the neonatal form. Severe but often stabilizing in the infantile form. Mild to moderate in SPG74, and can be nearly asymptomatic ("related leukodystrophy can remain asymptomatic", PMID 30258207).
- **Quality of life:** No EQ‑5D, SF‑36 or PROMIS data exist. Functional outcome data from Liu et al. (PMID 28671726): severe motor handicap in 50.0%, delay in communication, problem-solving or personal-social skills in 52.9–71.4%, and mild symptom fluctuations in 20.0%.

---

## 4. Genetic / Molecular Information

**Gene.** IBA57, "iron-sulfur cluster assembly factor IBA57" ([HGNC REST](https://rest.genenames.org/fetch/symbol/IBA57)).

| Field | Value |
|---|---|
| HGNC | HGNC:27302 |
| Location | 1q42.13 |
| Previous symbol | C1orf69 |
| Entrez Gene | 200205 |
| Ensembl | ENSG00000181873 |
| OMIM gene | 615316 |
| UniProt | Q5T440 |
| MANE Select | NM_001010867.4 / ENST00000366711.4 |

**Protein** ([UniProt Q5T440](https://rest.uniprot.org/uniprotkb/Q5T440.txt)):
- 356 amino acids, about 38.2 kDa.
- Mitochondrial transit peptide at residues 1–39.
- Forms a [2Fe‑2S]-bridged heterodimer/heterotetramer with ISCA2 (ComplexPortal CPX‑2503). Arg146 is needed for the ISCA2 interaction and Cys259 for complex formation.
- Crystal structures: PDB 6GEU, 6QE3, 6QE4.
- GO: GO:0005759 (mitochondrial matrix), GO:1990229 (iron-sulfur cluster assembly complex), GO:0051604 (protein maturation).

**Reported pathogenic and likely pathogenic variants** (NM_001010867; germline, biallelic):

| Variant | Type | Context | PMID |
|---|---|---|---|
| c.941A>C, p.Gln314Pro (rs587777016) | Missense; protein destabilizing | Homozygous; perinatal lethal | 23462291 |
| c.436C>T, p.Arg146Trp | Missense; loss of function; disrupts the ISCA2 interface | Homozygous; fatal infantile leukodystrophy | 25971455, 31831856 |
| Donor splice-site variant (HGVS not retrieved) | Splice; aberrant mRNA with a premature stop | Homozygous; SPG74 | 25609768 |
| c.286T>C, p.Tyr96His | Missense | Chinese hotspot (85.2%); milder, stable course | 39227420, 34709542, 38923322 |
| c.310G>T, p.Gly104Cys | Missense; destabilizes IBA57 and the IBA57–ISCA2 complex | Homozygous (Cuban descent) and compound heterozygous; severe | 39408793, 36360281, 42544324 |
| c.189delC; c.580A>G | Frameshift; missense | Chinese patients | 34709542 |
| c.307C>T, p.Gln103Ter | Nonsense | Compound heterozygous with c.286T>C in monozygotic twins | 39779339 |
| c.697C>T | Nonsense if p.Arg233Ter (protein change not given in the abstract) | Compound heterozygous with c.286T>C; the PGT family | 40602968 |
| c.826C>T | Not given | Compound heterozygous with c.310G>T | 42544324 |
| c.395_400dup (p.V132_Q133dup); c.832delC (p.R278Afs\*23) | In-frame dup; frameshift (classified likely pathogenic, PVS1+PM2) | Compound heterozygous | 41559004 |
| c.992T>A (p.L331Q) | Missense; VUS | Compound heterozygous with c.286T>C | 38923322 |
| c.338A>G (p.Tyr113Cys) | Missense | iPSC donor | 41108822 |

- **ClinVar:** An NCBI query for IBA57[gene] returned 410 records. I did not retrieve the breakdown by classification. UniProt lists p.Gly211Ser (rs2298014) as a non-disease polymorphism.
- **Allele frequency:** gnomAD was not retrieved. No population frequency is available here for c.286T>C or other alleles.
- **Functional consequence:** Loss of function or hypomorphism throughout (PMIDs 23462291, 25971455, 28913435). There is no evidence of gain of function or dominant-negative effect, and heterozygous carriers are unaffected.
- **Modifier genes:** None identified.
  - IBA57 stability depends on its partners: "IBA57 seems to require BOLA3, NFU1 and ISCA2 for its stability" (PMID 28803783).
  - IBA57 loss lowers NFU1: "Defects in IBA57 essentially regulate NFU1 expression" (PMID 28913435).
- **Epigenetics:** No data.
- **Chromosomal abnormalities:** None reported (1q42 deletions would be expected to unmask a recessive allele, but no such case was retrieved).

---

## 5. Environmental Information

There is no known environmental, lifestyle or infectious cause. The only reported trigger is a febrile illness preceding rapid decline (PMID 30258207). CTD, TOXNET and EPA resources had no relevant data in this search.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic loss-of-function IBA57 variants **lead to** reduced amounts of IBA57 protein, or IBA57 that cannot work properly in the mitochondrial matrix. This is shown in patient muscle and fibroblasts (PMIDs 23462291, 28913435) and biophysically for Gly104Cys (PMID 39408793).
2. Loss of IBA57 **prevents** formation of the functional [2Fe‑2S]-bridged ISCA2–IBA57 complex, and the reductive fusion of [2Fe‑2S] into [4Fe‑4S] clusters on ISCA1–ISCA2.
   - "IBA57 forms a heterodimeric complex with ISCA2 by bridging a [2Fe-2S] cluster" (PMID 30269484).
   - "Electrons from FDX2 catalyze the reductive [2Fe-2S] cluster fusion on ISCA1-ISCA2 in an IBA57-dependent fashion" (PMID 32817474).
   - A 2026 study proposes that IBA57 is an electron-transfer activator that "acts catalytically as an efficient electron donor" via a "17 Å electron transfer pathway" from FDX2 (PMID 43036033). This is in vitro work. IBA57 works without folate (PMID 36075292).
3. Failed [4Fe‑4S] delivery **results in** apo or unstable target proteins. The [2Fe‑2S] proteins are largely spared: "the mitochondrial [2Fe-2S] enzyme ferrochelatase and cellular heme content were unaffected" (PMID 22323289, HeLa cells).
   - Partial exception: yeast data show a role in maturing the Rieske [2Fe‑2S] protein and in III/IV supercomplexes (PMID 29343425).
4. Step 3 branches into three downstream defects:
   - **4a. Respiratory chain.** Loss of [4Fe‑4S] in complex I and in SDHB (complex II) **leads to** combined complex I+II deficiency (PMIDs 23462291, 27785568). "Immunoblotting revealed substantially reduced expression of SDHB" (PMID 28913435). The NFU1 depletion that follows IBA57 loss also lowers SDH (PMID 28913435).
   - **4b. Lipoic acid synthesis.** Loss of the [4Fe‑4S] cluster in lipoic acid synthase (LIAS, a radical SAM enzyme; PMID 18086897) **leads to** reduced lipoylation of the lipoate-dependent enzymes PDH, α‑KGDH, BCKDH and the glycine cleavage H protein (PMID 25971455). This **results in** lactic acidosis, hyperglycinemia, and urinary 2‑keto/2‑hydroxyadipic and other organic acids.
   - The link from reduced lipoylation to hyperglycinemia goes through the glycine cleavage system. That step is inferred from the known biochemistry of lipoylation and the MMDS literature (PMID 34440194), not shown directly for IBA57.
   - The link to 2‑ketoadipate goes through the lipoylated 2‑oxoadipate dehydrogenase. Here 2‑ketoadipate stands for lysine/tryptophan catabolite biomarkers (PMID 37903659), and that link is inferred.
   - **4c. Aconitase.** Loss of mitochondrial aconitase activity (a [4Fe‑4S] enzyme) impairs the TCA cycle (PMIDs 22323289, 18086897).
5. Combined impairment of oxidative phosphorylation (OXPHOS) and the TCA cycle **leads to** an energy deficit. In depleted cells this was accompanied by structural damage: "massively swollen and enlarged mitochondria that were virtually devoid of cristae membranes" (PMID 22323289).
6. High-energy-demand tissues fail. The specific vulnerability of white matter and myelinating glia is inferred:
   - Brain white matter **leads to** cavitating leukoencephalopathy and leukodystrophy.
   - Long corticospinal tracts and the optic nerve **lead to** spastic paraplegia and optic atrophy.
   - Peripheral nerve **leads to** neuropathy.
   - Skeletal muscle and respiratory drive **lead to** hypotonia and respiratory failure.
   - The fetal brain **leads to** polymicrogyria and ventriculomegaly.
7. These organ effects **result in** clinical outcomes ranging from neonatal death to a static or slowly progressive motor disability.

**Secondary pathways (model or omics evidence):**
- Fe‑S assembly defects in yeast activate the DNA damage response. Loss of Iba57 requires Mec1 and Chk1 (PMID 26567217).
- RNA‑seq of patient-derived material "revealed transcriptional dysregulation of the PI3K-Akt signaling pathway" (PMID 42544324). This finding is associative.
- Patient fibroblast proteomics show interdependent stability of NFU1, BOLA3, ISCA2 and IBA57 (PMID 28803783).

**Not applicable / no data:** immune involvement, epigenetic changes, single-cell, spatial omics, CRISPR screens specific to IBA57.

**Suggested GO terms:**
- GO:0044572 [4Fe-4S] cluster assembly
- GO:0016226 iron-sulfur cluster assembly
- GO:0009107 lipoate biosynthetic process
- GO:0006120 mitochondrial electron transport, NADH to ubiquinone
- GO:0006099 tricarboxylic acid cycle
- GO:0042552 myelination
- GO:0051604 protein maturation

**Suggested CL terms:**
- CL:0000128 oligodendrocyte
- CL:0000540 neuron
- CL:0000100 motor neuron
- CL:0000740 retinal ganglion cell
- CL:0000188 skeletal muscle cell
- CL:0000057 fibroblast (diagnostic tissue)

---

## 7. Anatomical Structures Affected

- **Primary organs:**
  - Brain white matter (UBERON:0002316), mainly periventricular and central, with cavitation (PMID 28671726).
  - Cerebral cortex (UBERON:0000956), with polymicrogyria (PMID 37903659).
  - Corpus callosum (UBERON:0002336).
  - Spinal cord / corticospinal tract (UBERON:0002240 / UBERON:0002707).
  - Optic nerve (UBERON:0000941).
  - Skeletal muscle (UBERON:0001134).
- **Secondary organs:** Respiratory system (respiratory failure), peripheral nerves (UBERON:0001021), and liver (complex II deficiency found in fetal liver, PMID 42544324).
- **Body systems:** Nervous, neuromuscular, respiratory, metabolic.
- **Subcellular:** Mitochondrial matrix (GO:0005759), mitochondrial inner membrane / respiratory chain complexes (GO:0005743), iron-sulfur cluster assembly complex (GO:1990229).
- **Lateralization:** Bilateral, symmetric white-matter involvement is the usual imaging description. I did not retrieve explicit laterality statements.

---

## 8. Temporal Development

- **Onset:**
  - Prenatal or congenital in the severe form (polyhydramnios, IUGR, arthrogryposis).
  - Infantile, at a median of 9–11 months (PMIDs 28671726, 30770271).
  - Childhood (first decade) in SPG74.
  - Onset is usually acute or subacute regression, sometimes after fever.
- **Course:**
  - Neonatal: rapidly fatal, with death within 3 months (PMID 39227420).
  - Infantile cavitating form: an acute phase followed by stabilization. "Thirty-five children (35/37) exhibited a stabilized or improved pattern" (PMID 30770271, all genes). "All cases survived and remained stable" (PMID 28671726).
  - MRI evolves from cavitation and patchy restricted diffusion at peak to atrophy in the recovery phase (PMID 28671726).
  - SPG74: slowly progressive.
- **Remission:** Partial spontaneous recovery of regression is reported. "Both children showed partial recovery of neurodevelopmental regression" (PMID 39779339).
- **Critical periods:** Mostly inferred. Fetal brain development is one (polymicrogyria). The infantile window of about 6–18 months, when acute white-matter injury happens, is another. Febrile illness is a likely period of vulnerability.

---

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007), with full penetrance for biallelic pathogenic genotypes as reported.
- **Expressivity:** Markedly variable, even within families. In one family, one brother's leukodystrophy stayed asymptomatic apart from optic atrophy, while the other developed progressive paraparesis (PMID 30258207).
- **Not reported:** anticipation, germline mosaicism.
- **Prevalence:**
  - A third-party mirror of Orphanet lists 0.1/100,000, which is unverified ([PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/5369)).
  - Case counts: 52 cases had been reported by 2022 (PMID 36360281), 56 MMDS3 cases by 2024 (PMID 38923322), and 61 IBA57 patients (46 MMDS3) in the 2024 pooled analysis (PMID 39227420).
  - Incidence is unknown.
- **Population distribution:**
  - Chinese patients are over-represented: 58.7% of the pooled cohort in PMID 39227420.
  - c.286T>C is a probable founder or recurrent allele in China.
  - Other reported ancestries: Sephardi Jewish and Japanese (PMID 30258207); Cuban descent (PMID 36360281); a consanguineous family with SPG74 (PMID 25609768; ancestry not verified here).
- **Sex ratio:** No sex bias reported.
- **Carrier frequency:** Not available (gnomAD not retrieved).

---

## 10. Diagnostics

- **Laboratory:**
  - Plasma and CSF lactate, pyruvate and lactate:pyruvate ratio.
  - Plasma and CSF glycine (raised CSF glycine with hyperglycinemia).
  - Urine organic acids: 2‑hydroxyadipic and 2‑ketoadipic acids, β‑aminoisobutyric aciduria. Lysine and tryptophan metabolites are proposed as biomarkers: an "increase of 2-hydroxyadipic and 2-ketoadipic acids in urine organic acid analysis" (PMID 37903659).
  - Results can be normal or only mildly abnormal (lactate 2.50 mmol/L, PMID 38923322).
- **Tissue biochemistry:**
  - Respiratory chain enzymology in muscle, fibroblasts or liver shows combined or isolated complex I/II deficiency with normal III/IV (PMIDs 23462291, 27785568, 41559004).
  - Immunoblotting shows reduced SDHB, LIAS, NFU1 and lipoylated PDH‑E2 and KGDH‑E2 (PMIDs 28913435, 25971455, 28803783).
  - Reduced aconitase activity.
- **Imaging:**
  - MRI shows cavitating leukoencephalopathy in periventricular and central white matter, restricted diffusion in the acute phase, then atrophy (PMID 28671726). Corpus callosum dysplasia and cortical malformation can also appear (PMIDs 34709542, 37903659).
  - MRS shows raised choline and possibly a lactate peak.
  - Unusual subependymal pseudocysts were reported in one newborn (PMID 33890810, title-level).
- **Electrophysiology:** Nerve conduction studies for neuropathy and visual evoked potentials / ophthalmology for optic atrophy, especially in SPG74 (PMID 39227420). Specific values were not retrieved.
- **Genetic testing:**
  - Exome or genome sequencing is the main route (e.g., "Exome sequencing revealed three IBA57 variants", PMID 34709542).
  - IBA57 is on leukodystrophy, mitochondrial and HSP panels, including Genomics England PanelApp HSP panels ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/165/gene/IBA57)).
  - Targeted testing for c.286T>C is reasonable in Chinese patients.
  - mtDNA testing is useful only to exclude other causes.
  - Karyotype, FISH, CMA and repeat-expansion testing are not first-line.
  - A splice variant (PMID 25609768) shows that RNA studies can confirm splicing effects.
- **Differential diagnosis** (other MMDS / Fe‑S and lipoate disorders):
  - MMDS1 (NFU1), MMDS2 (BOLA3), MMDS4 (ISCA2), MMDS5 (ISCA1), MMDS6 (PMPCB, not retrieved here) (PMID 34440194).
  - Lipoic acid synthesis defects: LIAS, LIPT1, LIPT2 (PMIDs 27586888, 24777537, 24256811).
  - Nonketotic hyperglycinemia (GLDC/AMT).
  - Cavitating leukoencephalopathies from other genes (PMID 30770271; 22 genes).
  - SPOAN and other complicated HSPs (for SPG74).
  - Leigh syndrome.
  - PDH deficiency (PMID 32742935 cautions against relying on genetics alone).
- **Screening:** No newborn screening exists. Carrier, cascade and preimplantation genetic testing are feasible once familial variants are known (PMID 40602968).

---

## 11. Outcome / Prognosis

- **Neonatal form:** Lethal, with death within 3 months (PMID 39227420). The index siblings died perinatally (PMID 23462291).
- **Infantile and Chinese cohorts:** Survival is "exceeding 90% at 5 years" in the relatively stable c.286T>C-dominated Chinese group. Mortality was significantly lower than in non-Chinese patients (P = 0.002) (PMID 39227420).
- **Morbidity:** Severe motor handicap in 50%, plus developmental and communication delay (PMID 28671726). Spastic quadriplegia, visual impairment and epilepsy occur in some patients (PMID 30258207).
- **Complications:** Respiratory failure, feeding difficulty, and decompensation with intercurrent illness.
- **Prognostic factors:**
  - Age at onset: neonatal onset predicts death.
  - Genotype: p.Gly104Cys is linked to "a severe MMDS3 phenotype" (PMID 39408793); c.286T>C to a milder course.
  - Amount of residual IBA57 protein (PMID 25609768).
- **No validated prognostic biomarkers.**

---

## 12. Treatment

- **No disease-modifying therapy and no IBA57-specific trials.** I found none on ClinicalTrials.gov for IBA57 in this search. The general MMDS literature states "there is no established treatment" ([ACMG abstract on BOLA3/MMDS2](https://www.acmgmeeting.net/conference-program/treatment-bola3-associated-multiple-mitochondrial-dysfunctions-syndrome-2-mitochondrial-cocktail)).
- **Empiric "mitochondrial cocktail":**
  - Lipoic acid, riboflavin and ubiquinol have been proposed for the related MMDS2 based on one case.
  - A BOLA3 metabolomics study cautions that the [4Fe‑4S] pathway itself would need targeting (PMID 40273865, per search summary).
  - Lipoate supplementation may not help, because the defect is endogenous lipoate *synthesis* on the protein (LIAS), not lipoate supply. This is a mechanistic inference.
- **Supportive care:**
  - Respiratory support, feeding and nutritional support (gastrostomy where needed).
  - Seizure management.
  - Treat fever and infection promptly to avoid decompensation.
  - Physical, occupational and speech therapy; spasticity management and orthotics (SPG74).
  - Vision support.
- **Pharmacogenomics:** No data.
- **Gene, cell or RNA therapies:** None. An iPSC line (NIMHi020‑A) has been made, which enables preclinical work (PMID 41108822).
- **Suggested NCIT terms:**
  - Supportive Care (C15292)
  - Physical Therapy (C15373)
  - Mechanical Ventilation (C70909)
  - Enteral Nutrition (C15238)
  - Lipoic acid (C1025, thioctic acid)
  - Coenzyme Q10 (C385)
  - Riboflavin (C793)
  - Genetic Counseling (C15516)

  These NCIT codes are suggestions and were not verified in this session.

---

## 13. Prevention

- **Primary:** Genetic counseling for families who have had an affected child (25% recurrence risk per pregnancy), carrier testing and prenatal diagnosis.
  - The first successful IBA57 preimplantation genetic testing pregnancy: "delivery of a healthy male infant at 38 + 3 weeks of gestation" (PMID 40602968).
  - Prenatal recognition is possible: one affected fetus was diagnosed (PMID 42544324), and polyhydramnios and IUGR may be prenatal clues.
- **Secondary:** Early diagnosis by exome sequencing in infants with regression and cavitating leukoencephalopathy.
- **Tertiary:** Avoid catabolic stress and fever, and manage infections early (inferred from general mitochondrial disease practice).
- **Not applicable:** immunization, public-health and environmental measures.

---

## 14. Other Species / Natural Disease

- **Dog (*Canis lupus familiaris*, NCBITaxon:9615), Kooiker breed:** Hereditary necrotizing myelopathy, autosomal recessive, "characterized by progressive ataxia and paralysis."
  - Mapped to "the centromeric 5 Mb region of canine chromosome 14" (LOD 6.1).
  - IBA57 p.R147W, the residue equivalent to human Arg146, a known human pathogenic site.
  - Human IBA57 carrying the substitution "could only partially restore the biochemical defects of several mitochondrial [4Fe-4S] proteins" (PMID 37588046, Mandigers et al., *Front Genet* 2023).
  - This is a natural model of the spinal-cord (SPG74-like) end of the spectrum.
  - The OMIA ID and VBO breed ID were not retrieved.
- **Conservation:**
  - Yeast Iba57p is "essential for mitochondrial DNA maintenance," and human C1orf69/IBA57 complements the yeast deletion (PMID 18086897).
  - *Arabidopsis* mitochondrial orthologs rescue yeast mutants (PMID 29902489).
  - The *E. coli* homolog is YgfZ (PMID 36902159).
  - Mouse Iba57 has a KOMP allele and CRISPR null/floxed alleles listed at MGI and GemPharmatech. NCBI Gene IDs for the orthologs were not retrieved.
- **Zoonotic potential:** None.

---

## 15. Model Organisms

| Model | Type | Key findings | PMID / source |
|---|---|---|---|
| *S. cerevisiae* iba57Δ | Knockout | Loss of aconitase and radical SAM enzymes (biotin, lipoate synthases); mtDNA loss; Rieske/supercomplex defects; DNA damage response (Mec1/Chk1); ROS | 18086897, 21987576, 29343425, 26567217, 24028658, 36075292 |
| HeLa RNAi (ISCA1/ISCA2/IBA57) | Human cell knockdown | [4Fe‑4S] defects (aconitase, complex I, LIAS); [2Fe‑2S] spared; mitochondria swollen and without cristae | 22323289 |
| Patient fibroblasts, myoblasts, lymphoblasts | Human ex vivo | Reduced IBA57, SDHB, LIAS, NFU1, lipoylation; rescued by WT IBA57 | 25971455, 28913435, 25609768, 28803783 |
| iPSC NIMHi020‑A (p.Tyr113Cys) | Human iPSC | Normal karyotype; available for neural/glial differentiation | 41108822 |
| In vitro reconstitution and structure | Biochemical | ISCA2–IBA57 [2Fe‑2S] complex; FDX2-driven cluster fusion; electron-transfer activator role; Gly104Cys destabilization | 30269484, 31831856, 32817474, 43036033, 39408793 |
| Kooiker dog | Natural disease | Necrotizing myelopathy; partial-function R147W | 37588046 |
| Mouse | KOMP / CRISPR null and floxed alleles exist | No published phenotype retrieved; embryonic lethality not confirmed | MGI/IMPC (not retrieved) |

- **Strengths of current models:** They capture the biochemistry well: the [4Fe‑4S], lipoylation and complex I/II defects.
- **Limitations:** No mammalian in vivo model of leukoencephalopathy has been published. The yeast mtDNA-loss phenotype does not appear in human disease. The dog captures the myelopathy but not the infantile cavitating leukoencephalopathy.

---

## Key References (PMIDs retrieved this session)

- **Disease and phenotype papers:** 23462291 (index family), 25971455, 25609768 (SPG74), 27785568, 28671726, 28913435, 30258207, 30770271, 34440194 (MMDS review), 34709542, 36360281, 37903659, 38923322, 39227420, 39408793, 39779339, 40602968, 41108822, 41559004, 42544324.
- **Mechanism papers:** 18086897, 22323289, 28803783, 29343425, 30269484, 31831856, 32817474, 36075292, 43036033.
- **Animal model:** 37588046.

**Gaps that need primary-database checks:**
- ICD-10/11, MeSH and the official Orphanet prevalence figure.
- The HGVS name of the SPG74 splice variant, and the ancestry of that family.
- gnomAD frequencies, and ClinVar counts by classification.
- MGI/IMPC mouse phenotypes and the OMIA entry for the dog disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 34 |
| On topic | 28 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:29343425` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30269484` *(abstract only)*: "IBA57 forms a heterodimeric complex with ISCA2 by bridging a [2Fe-2S] cluster"
  - closest text in source: "IBA57 forms a heterodimeric complex with ISCA2 by bridging a [2Fe-2S] cluster"
- `PMID:32817474`: "Electrons from FDX2 catalyze the reductive [2Fe-2S] cluster fusion on ISCA1-ISCA2 in an IBA57-dependent fashion"
  - closest text in source: "Electrons from FDX2 catalyze the reductive [2Fe-2S] cluster fusion on ISCA1-ISCA2 in an IBA57-dependent fashion"
- `PMID:22323289` *(abstract only)*: "the mitochondrial [2Fe-2S] enzyme ferrochelatase and cellular heme content were unaffected"
  - closest text in source: "the mitochondrial [2Fe-2S] enzyme ferrochelatase and cellular heme content were unaffected"
- `PMID:37588046` *(abstract only)*: "could only partially restore the biochemical defects of several mitochondrial [4Fe-4S] proteins"
  - closest text in source: "could only partially restore the biochemical defects of several mitochondrial [4Fe-4S] proteins"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 73 |
| Resolved | 69 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 21 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014132` (3 mentions) - the report calls it "MONDO"; MONDO calls it **multiple mitochondrial dysfunctions syndrome 3**
- `DOID:0080135` (1 mention) - the report calls it "DOID"; DOID calls it **multiple mitochondrial dysfunctions syndrome 3**
- `HP:0003324` (1 mention) - the report calls it "Sign"; HP calls it **Generalized muscle weakness**
- `HP:0000252` (1 mention) - the report calls it "Physical"; HP calls it **Microcephaly**
- `HP:0011968` (1 mention) - the report calls it "Symptom"; HP calls it **Feeding difficulties**
- `HP:0012706` (1 mention) - the report calls it "Imaging/lab"; HP calls it **Elevated brain choline level by MRS**
- `HP:0002376` (1 mention) - the report calls it "Sign"; HP calls it **Developmental regression**
- `HP:0009830` (1 mention) - the report calls it "Sign"; HP calls it **Peripheral neuropathy**
- `HP:0001250` (1 mention) - the report calls it "Sign"; HP calls it **Seizure**
- `HP:0032480` (1 mention) - the report calls it "Lab"; HP calls it **Beta-aminoisobutyric aciduria**
- `HP:6000830` (1 mention) - the report calls it "Lab"; HP calls it **Diminished alpha-ketoglutarate dehydrogenase activity in cultured fibroblasts**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005759` (2 mentions) - the report calls it "mitochondrial matrix", "Subcellular:** Mitochondrial matrix"; GO calls it **mitochondrial matrix**
- `GO:0044572` (1 mention) - the report calls it "4Fe-4S"; GO calls it **[4Fe-4S] cluster assembly**
- `UBERON:0002316` (1 mention) - the report calls it "Brain white matter"; UBERON calls it **white matter**, and lists "CNS white matter" among its other names
- `UBERON:0000941` (1 mention) - the report calls it "Optic nerve"; UBERON calls it **cranial nerve II**, and lists "optic nerve" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "Skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005759` - called "mitochondrial matrix", "Subcellular:** Mitochondrial matrix"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.