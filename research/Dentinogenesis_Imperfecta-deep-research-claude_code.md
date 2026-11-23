---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-19T19:38:13.921614'
end_time: '2026-11-19T19:54:19.882133'
duration_seconds: 965.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dentinogenesis Imperfecta
  mondo_id: MONDO:0018849
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: DGI without OI; DGI; DI; dentinogenesis imperfecta (disease); dentinogenesis
    imperfecta without osteogenesis imperfecta; non-syndromic DGI; non-syndromic dentinogenesis
    imperfecta; opalescent teeth without OI
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
  - claude-opus-5
  web_search_requests: 29
  num_turns: 1
  total_cost_usd: 6.419895399999999
  session_id: 8cf6c783-d52a-414e-9aee-757a7d025c33
  stop_reason: end_turn
  tool_calls: 146
  retrieval_calls: 146
  assistant_text_blocks: 22
citation_count: 89
reference_validation:
  total_references: 117
  verified: 117
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 15
  quotes_unsupported: 12
  unsupported_quote_references:
  - PMID:22934831
  - PMID:16937369
  - PMID:12721295
  - PMID:28288297
  - PMID:19021896
  - DOI:10.1186/1750-1172-3-31
  - PMC:PMC2600777
  - PMID:34667213
  - PMC:PMC8526674
  - PMID:23509818
  - PMC:PMC8835393
  quotes_not_checkable: 2
  relevance_assessed: 117
  on_topic: 60
  off_topic: 5
  off_topic_references:
  - PMID:24281365
  - PMID:19125428
  - PMID:39347039
  - PMID:42266834
  - PMC:PMC4350590
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 122
  verified: 96
  not_found: 3
  obsolete: 0
  unverifiable: 23
  confabulation_rate: 0.03
  labels_checked: 21
  labels_matching: 8
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0018849
    reported_labels:
    - ClinGen and MONDO links
    - human dentinogenesis imperfecta
    - dentinogenesis imperfecta**, the *non-syndromic
    ontology_label: dentinogenesis imperfecta
  - term_id: HP:0000703
    reported_labels:
    - HPO (as a phenotype term)
    ontology_label: Dentinogenesis imperfecta
  - term_id: MONDO:0007442
    reported_labels:
    - DGI type 3
    ontology_label: dentinogenesis imperfecta type 3
  - term_id: HP:0033780
    reported_labels:
    - Bulbous crowns with marked cervical constriction
    ontology_label: Bulbous tooth
  - term_id: DOID:4154
    reported_labels:
    - Disease Ontology
    ontology_label: dentinogenesis imperfecta
  - term_id: HP:0030756
    reported_labels:
    - "Congenital erythropoietic porphyria** \u2014 erythrodontia"
    ontology_label: Erythrodontia
  labels_variant: 7
  unresolved_terms:
  - DOID:9003089
  - DOID:9004572
  - DOID:9007364
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - MGI
  - NCBIGene
  - MIM
  - RGD
  - Chr5
  - NCBI_Gene
  - OMIA
  service_unreachable: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dentinogenesis Imperfecta
- **MONDO ID:** MONDO:0018849 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** DGI without OI; DGI; DI; dentinogenesis imperfecta (disease); dentinogenesis imperfecta without osteogenesis imperfecta; non-syndromic DGI; non-syndromic dentinogenesis imperfecta; opalescent teeth without OI
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Dentinogenesis Imperfecta** covering all of the
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

I'll research this systematically. Let me start with the core identifiers and gene.

OMIM returned HTTP 403 on all four pages. As instructed, I'll try the NCBI fallbacks.

I could not read any of the four OMIM pages. OMIM returned HTTP 403 Forbidden for all of them, so the OMIM-specific content you asked for (variant nomenclature, allelic variants, Brandywine isolate, 4q21-q22 mapping history, OMIM references) is not in this report. Sending those OMIM URLs again would fail the same way.

**Fetch results**

| URL | Result |
|---|---|
| https://omim.org/entry/125490 | HTTP 403 Forbidden |
| https://omim.org/entry/125500 | HTTP 403 Forbidden |
| https://omim.org/entry/125420 | HTTP 403 Forbidden |
| https://omim.org/entry/125485 | HTTP 403 Forbidden |
| https://www.ncbi.nlm.nih.gov/medgen/?term=125490 | HTTP 200, read. Redirects to the MedGen record for "Dentinogenesis imperfecta type 2" |
| https://www.ncbi.nlm.nih.gov/gene/1834 | HTTP 200, but the response was a reCAPTCHA "Checking your browser" interstitial, so no gene content was returned |

**What the MedGen page (125490) said**

- Title: "Dentinogenesis imperfecta type 2 (Concept Id: C2973527)". The record shows "DGI1" as the short name.
- MedGen UID 424922. Cross-references: OMIM 125490, MONDO:0007441, ORPHA166260.
- Synonyms: "CAPDEPONT TEETH; Dentinogenesis imperfecta - Shield's type II; Dentinogenesis imperfecta without osteogenesis imperfecta; DGI1; Hereditary Opalescent Dentin; OPALESCENT DENTIN; OPALESCENT TEETH WITHOUT OSTEOGENESIS IMPERFECTA".
- Inheritance: autosomal dominant (listed from Orphanet).
- Gene: DSPP, shown with location 4q22.1.
- Definition (OMIM-sourced, cited as Song et al., 2008): it is a disorder of dentin formation. The page describes amber or gray-yellow opalescent tooth discoloration, obliteration of the pulp chambers and root canals, and attrition, affecting both deciduous and permanent teeth. I have paraphrased this rather than quoting it, because the quotable text is longer than the permitted limit for this source.
- MedlinePlus text on the page says tooth discoloration is "most often a blue-gray or yellow-brown color" and that the teeth are translucent and weaker than normal. It also says that "A few older individuals with type II have had progressive high-frequency hearing loss", and that it is "not known whether this hearing loss is related to dentinogenesis imperfecta". The page also notes that type II and type III, and dentin dysplasia type II, may be forms of a single disorder.
- HPO clinical features listed: "Dentinogenesis imperfecta" (C0011436) and "Yellow-brown discoloration of the teeth" (C1863008).
- Genetic testing (GTR): 14 sequence-analysis entries, 11 deletion/duplication, 3 targeted variant, 1 research. The page gives counts only, not variant names.
- PMIDs on the page, all under general "Professional guidelines" and "Recent clinical studies" headings rather than an OMIM section: 39674968, 38828893, 36597617 (the latter is about a DSPP frameshift causing dentin dysplasia type 2), 34678748, 29964251. The first two concern osteogenesis imperfecta cohorts, and the last two are case reports. The page gives no PMID for the OMIM definition beyond the Song et al., 2008 citation.

**Not obtained**

- The gene page for DSPP (NCBI Gene 1834) was blocked by a reCAPTCHA challenge. I did not retry it.
- The MedGen record for 125500, 125420 or 125485 was not requested and was not fetched.

I could not retrieve the Orphanet disease record. orpha.net returned a bot-verification interstitial, so the requested fields (prevalence class, ICD/OMIM/UMLS/MeSH/MedDRA codes, clinical sections) are unknown from that source. The GARD page, which draws on Orphanet data, gave partial content, and the Orphadata epidemiology file is available but I did not read its contents.

**1. orpha.net (ORPHA:49042 and ORPHA:166260): blocked**
- https://www.orpha.net/en/disease/detail/49042 returned HTTP 200 with an 83-character page reading "Vérification de la connexion... protégé par haphash". That is a verification challenge, not the disease record.
- https://www.orpha.net/en/disease/detail/166260 returned the same challenge page, so I cannot confirm whether that record exists.
- Retrying or using a variant URL would likely fail the same way, so I did not try further.

**2. GARD: https://rarediseases.info.nih.gov/diseases/6258/dentinogenesis-imperfecta (last updated September 2026)**
- **Definition (Summary):** "Dentinogenesis imperfecta is a disorder of tooth development." Teeth are discolored (often "blue-gray or yellow-brown"), translucent, weaker, and prone to "rapid wear, breakage, and loss," affecting primary and permanent teeth.
- **Types:** GARD says researchers describe three types with similar dental abnormalities. Type I occurs with osteogenesis imperfecta. Types II and III usually occur without other inherited disorders. Some older type II patients had progressive high-frequency hearing loss, though its relation to the disorder is unknown. Some researchers think type II and III, and dentin dysplasia type II, may be one disorder.
- **Synonyms (Other Names):** dentinogenesis imperfecta (disease); dentinogenesis imperfecta without osteogenesis imperfecta; DGI; DGI without OI; DI; hereditary opalescent dentin; non-syndromic dentinogenesis imperfecta; non-syndromic DGI; opalescent teeth without OI; opalescent teeth without osteogenesis imperfecta.
- **Cross-references visible on the page:** MONDO:0018849 (ClinGen and MONDO links), and the Orphanet link to /en/disease/detail/49042. No ICD-10, ICD-11, OMIM, UMLS, MeSH, or MedDRA codes appear on the page.
- **Prevalence:** not stated on the page.
- **Age of onset:** "Symptoms of this disease may start to appear as a Child." (GARD cites Orphanet for this.)
- **Inheritance:** not stated for this disease. The page shows a generic autosomal dominant explainer box that is not specific to dentinogenesis imperfecta.
- **Cause:** "Changes in your genes (also called variants) cause Dentinogenesis imperfecta." This is generic wording.
- **Clinical features (HPO, common):** abnormal dental pulp morphology; abnormal dentin morphology; abnormal dental root morphology; hypocalcification of dental enamel; joint hypermobility; fragile teeth; generalized hypoplasia of dental enamel; grayish enamel; odontodysplasia; pulp obliteration; yellow-brown discoloration of teeth.
- **Clinical features (HPO, uncommon):** bruising susceptibility; short dental root; persistence of primary teeth; hearing impairment; hyperextensibility at elbow; finger and knee joint hypermobility; prolonged bleeding time; selective tooth agenesis; blue sclerae.
- **Etiology, diagnostic methods, differential diagnosis, antenatal diagnosis, genetic counseling, management and treatment, and prognosis:** not disease-specific on this page. The only related content is generic: diagnosis "can take more than six years," GARD says "only about 5% of rare diseases have FDA-approved treatments," and the page suggests geneticists and odontologists. The page also names dentin dysplasia type II as the condition it most resembles.
- **Patient organizations:** Osteogenesis Imperfecta Foundation (https://oif.org/) and National Foundation for Ectodermal Dysplasias (https://www.nfed.org/).

**3. Orphadata epidemiology data: accessible**
- https://www.orphadata.com/ describes Orphanet datasets (CC BY 4.0). It is a landing page and lists no epidemiology file directly.
- https://sciences.orphadata.com/orphanet-scientific-knowledge-files/ lists the July 2026 release, with an "Epidemiology of rare diseases" section. Files are released in July and December.
- https://sciences.orphadata.com/epidemiology/ states that epidemiology (prevalence and/or incidence) is "available in XML file" in several languages. The July 2026 English file is en_product9_prev.xml, with 6728 entries, 15.43 MB, dated 23 Jun 26. The download is at https://www.orphadata.com/data/xml/en_product9_prev.xml. Its format description is at https://sciences.orphadata.com/docs/OrphadataFreeAccessProductsDescription.pdf.
- I did not download or parse the XML, so I have no prevalence class for ORPHA:49042. To get it, fetch the English XML and search it for ORPHA code 49042 (or the disease name) to read the PrevalenceClass entry.

I could not retrieve the full text of either article, so I have no content from either paper to report. Neither the Shields criteria, the revised grading, the genetics, nor any of the other items you listed were available to me, and I have not filled the gaps from memory.

**1. Barron et al., Orphanet J Rare Dis 2008 (DOI 10.1186/1750-1172-3-31)**
- https://ojrd.biomedcentral.com/articles/10.1186/1750-1172-3-31 returned a 301 redirect to https://link.springer.com/article/10.1186/1750-1172-3-31.
- That Springer URL returned a 303 redirect to an authentication page (https://idp.springer.com/authorize?...). It did not serve the article.
- Permanent failure for this path: fetching the same URL again would redirect the same way. I did not try other variants.
- To get this paper, the full text needs to be supplied, or a URL that serves it without a login.

**2. de La Dure-Molla, Fournier & Berdal, Eur J Hum Genet 2015 (DOI not verified)**
- https://www.nature.com/articles/ejhg2014159 returned a 303 redirect to a Nature login page (https://idp.nature.com/authorize?...). No article content was served.
- The PMC fallback you gave, https://pmc.ncbi.nlm.nih.gov/articles/PMC4350590/, returned the wrong paper. It is Peng et al., "Retrieving Y chromosomal haplogroup trees using GWAS data", Eur J Hum Genet 2014 (published online 2013), PMID 24281365, DOI 10.1038/ejhg.2013.272. It is a population-genetics study with no dental content. The PMCID in your request appears to be incorrect.
- I did not search for the correct PMCID, because that would mean guessing at identifiers. Please check the article's PMCID or PMID in PubMed and send it back, and I can fetch it.

**What would unblock this**
- A working full-text URL for each paper (for example, a PMC or PubMed Central page for the Barron paper, and the correct PMCID for the 2015 paper), or the text pasted in directly.
- Once I have the text, I can extract the classification criteria, clinical and radiographic findings, dentin histology, DSPP mutations, epidemiology, hearing loss evidence and the OI statement, with exact quotes kept within the length limits for non-preapproved sources.

I could not get any of the requested HPO, OLS, or Mondo content. Every data page returned either a 404 or an empty JavaScript shell, so I have no verified IDs, labels, or annotations to report.

**Results by URL**

1. `https://hpo.jax.org/browse/term/HP:0000703`: HTTP 404 Not Found. Permanent, so resending it will fail the same way.
2. `https://hpo.jax.org/browse/term/HP:0010299`: HTTP 404 Not Found. Permanent.
3. `https://hpo.jax.org/browse/disease/OMIM:125490`: HTTP 404 Not Found. Permanent.
4. `https://hpo.jax.org/browse/disease/OMIM:125500`: HTTP 404 Not Found. Permanent.
5. `https://monarchinitiative.org/MONDO:0018849`: HTTP 200, but the body is only the text "Monarch Initiative" (28 characters). The page content is rendered client-side, so no definition, synonyms, cross-references, children, genes, or phenotypes were returned.

**Search and fallback sources**

- `https://hpo.jax.org/` returned HTTP 200 with only the text "Human Phenotype Ontology" (27 characters). No search box or term links were visible, so the search route is unusable through this fetch.
- `https://www.ebi.ac.uk/ols4/ontologies/hp` returned HTTP 200 with only "Ontology Lookup Service (OLS)" (41 characters). It is also a JavaScript shell.
- `https://bioportal.bioontology.org` returned HTTP 403 Forbidden.

**Term IDs**

None of the requested labels could be verified. I have not listed any HPO IDs from memory. The only IDs I saw are those in your request (HP:0000703, HP:0010299, OMIM:125490, OMIM:125500, MONDO:0018849), and I could not confirm any of them on a page.

I did not query the search endpoints with the labels from your list. That would mean putting your task text into a URL, which I am not permitted to do.

**What would unblock this**

- Rendered or API access. These sites serve their content through JavaScript, so a browser-rendered fetch or the public JSON APIs would be needed. The HPO and Monarch APIs are the likely routes, but I would need you to say whether you want me to try them, since that means building URLs from the IDs.
- A local copy. If you have the HPO `hp.obo` or `phenotype.hpoa` files, or the Mondo `mondo.obo` file, those would answer all five items and the ID lookup directly.

The MGI ID in the request is wrong: MGI:94908 resolves to Dmc (DMCM susceptibility), not Dspp. I'll search MGI for Dspp, and try GeneCards as the fallback for human DSPP since NCBI returned a reCAPTCHA page.

I could not produce the requested Dspp data. Only the Dmc page and the OMIA home and search pages returned usable content, and the MGI ID in the request is wrong.

**1. Mouse Dspp (MGI)**
- **Wrong ID:** https://www.informatics.jax.org/marker/MGI:94908 resolves to **Dmc** ("DMCM susceptibility", feature type "heritable phenotypic marker"), not Dspp. It lists NCBI Gene 104147, no genome coordinates ("Genome coordinates not available from the current reference assembly"), and chromosome "Unknown". It has no alleles, MP terms, or DO/OMIM links shown. The page says "last database update 11/10/2026, MGI 6.29".
- **Search:** I fetched https://www.informatics.jax.org/searchtool/Search.do?query=Dspp. It returned the MGI search landing page with no result list, so I did not get a Dspp accession from it. The search URL embedded the gene symbol, which you asked for, but I should have checked that against my URL rule first.
- **Not verified:** I have no MGI accession for mouse Dspp, so no chromosome, human ortholog, alleles, MP terms, or DO/OMIM associations. Querying the MGI Genes & Markers form with "Dspp" directly, or giving me the accession, would unblock this.

**2. Alliance Genome (MGI:94908)**
- https://www.alliancegenome.org/gene/MGI:94908 returned only the page title "Alliance of Genome Resources" (29 characters). The content appears to be JavaScript-rendered, so no orthologs, disease associations, or phenotypes were visible. This page also carries the MGI:94908 (Dmc) ID, so it does not cover Dspp.

**3. Human DSPP**
- **NCBI:** https://www.ncbi.nlm.nih.gov/gene/1834 returned a reCAPTCHA "Checking your browser" challenge (HTTP 200, 176 characters). No gene data.
- **GeneCards:** https://www.genecards.org/cgi-bin/carddisp.pl?gene=DSPP returned HTTP 403 Forbidden. Sending the same URL again would fail the same way.
- Result: no HGNC ID, Entrez ID, Ensembl ID, UniProt accession, cytogenetic band, exon count, transcript, protein length, or domain data. Nothing was filled from memory.

**4. OMIA**
- https://omia.org/home/ and https://omia.org/search/ were read. The home page describes OMIA as covering 804 animal species, excluding human, mouse, rat, zebrafish and Xenopus. Its news notes that OMIA's exhaustive search is disabled (posted 4 Nov 2026) and that gateway time-out errors have occurred.
- The search page documents the simple, exhaustive and advanced forms, but does not return results. Running a query needs a results URL containing "dentinogenesis imperfecta" or "DSPP", and I did not construct one, because the URL rule forbids putting task text into a query string. I therefore have no OMIA IDs, species, or breed entries for either term.
- To complete this, run the OMIA simple search on those two terms in a browser, or confirm that I may fetch the results URL.

**Summary of what is still missing:** the correct mouse Dspp MGI accession and its allele, MP and disease data; all human DSPP identifiers and domain data (NCBI blocked, GeneCards 403); the Alliance ortholog and disease tables (JavaScript-rendered); and all OMIA dentinogenesis imperfecta and DSPP entries.

Final URLs read: https://www.informatics.jax.org/marker/MGI:94908, https://www.informatics.jax.org/searchtool/Search.do?query=Dspp, https://www.alliancegenome.org/gene/MGI:94908, https://www.ncbi.nlm.nih.gov/gene/1834 (challenge page), https://www.genecards.org/cgi-bin/carddisp.pl?gene=DSPP (403), https://omia.org/home/, https://omia.org/search/.

## Summary

I read two of the three papers I could retrieve, plus the PubMed search page. ScienceDirect (item 3) returned HTTP 403, and the PubMed article page for item 4 returned a cookie wall (HTTP 203), so I could not get the von Marschall 2012 abstract. Neither of those failures is worth retrying. Quotes below are kept under 125 characters because the sources are not preapproved.

Two pages needed care:
- The item 2 URL (`www.ncbi.nlm.nih.gov/pmc/articles/PMC8526674/`) returned a 301 to `pmc.ncbi.nlm.nih.gov/articles/PMC8526674/`, the same PMC ID on the same NCBI site, so I followed it.
- For item 1, the model-written tail of the page said no abstract or results were present. That is wrong: the verbatim text before the cutoff contains the full abstract, results and discussion, and I relied on that verbatim text.

---

## 1. PMC3591212: "A DSPP Mutation Causing Dentinogenesis Imperfecta and Characterization of the Mutational Effect"

- **Bibliographic:** Lee SK, Lee KE, Song SJ, Hyun HK, Lee SH, Kim JW. *Biomed Res Int* 2013;2013:948181 (epub 2012 Dec 27). DOI 10.1155/2013/948181. PMID 23509818. PMCID PMC3591212.
- **Variant:** c.50C>T, p.P17L, in exon 2 of DSPP (reference NM_014208.3). The authors note that c.49C>T (p.P17S) is the Brandywine mutation and that p.P17T (c.49C>A) has also been reported.
- **Human subjects:** A Korean family with DGI type III. The proband was 2.5 years old at first visit. The paper says "This sequence variation correlated perfectly with the presence of the disease."
- **Experimental systems:**
  - Splicing assay in COS-7 cells using a pSPL3 minigene. The mutation did not alter splicing.
  - Secretion assay in HEK293T cells transfected with GFP-tagged DSP (aa 1–382), wild-type and mutant.
  - Confocal immunofluorescence in HEK293T cells with calnexin (ER) and GM130 (Golgi) markers.
- **Mechanistic conclusions:**
  - Splicing was normal: "The mutation did not influence pre-mRNA splicing but caused ER retention and defective protein secretion."
  - Secretion: wild-type DSP was more than 7-fold higher in the medium than P17L (P < 0.01). Intracellular P17L was 12.1-fold higher than wild-type (P < 0.01).
  - Localisation: wild-type DSP was "localized exclusively in the Golgi apparatus," while the mutant "largely remained in the ER."
  - Mechanism of retention: the authors suggest reduced signal peptide cleavage (SignalP predictions, and P17 at the P2′ position from the cleavage site), or loss of an ER export signal.
  - Dominant negative: the authors say the mutant "is expected to have a dominant-negative effect." They also state: "It is possible that the severe phenotype observed in the affected family is caused by a dominant negative effect."
  - ER stress/UPR and Ca²⁺-dependent aggregation: not tested or discussed in the verbatim text.
  - Haploinsufficiency: not addressed.
- **Mouse model:** None. This paper has no knock-in or knockout mouse.
- **DSP/DGP/DPP processing and BMP1:** The introduction says DSPP is "rapidly cleaved by proteases" into DSP, DGP and DPP, and cites refs 3–4. Ref 3 is von Marschall & Fisher, *Matrix Biol* 2010 ("…cleaved into its two natural dentin matrix products by three isoforms of BMP1"; PMID 20079836). Ref 4 is Yamakoshi et al., *JBC* 2006 ("Dentin sialophosphoprotein is processed by MMP-2 and MMP-20…"). These appear only as reference titles. The paper does not test BMP1 itself.
- **DPP and hydroxyapatite nucleation:** Not addressed.

## 2. PMC8526674: "Mouse Dspp frameshift model of human dentinogenesis imperfecta"

- **Bibliographic:** Liang T, Hu Y, Zhang H, Xu Q, Smith CE, Zhang C, Kim JW, Wang SK, Saunders TL, Lu Y, Hu JC, Simmer JP. *Sci Rep* 2021 Oct 19;11:20653. DOI 10.1038/s41598-021-00219-4. PMID 34667213. PMCID PMC8526674. Received 2021 Jul 27; accepted Oct 1.
- **Abstract, verbatim:** the paper describes "two classes of dominant negative/gain-of-function mutations in dentin sialophosphoprotein (DSPP)": 5′ mutations in the N-terminal targeting sequence, and 3′ mutations that shift translation into the −1 frame.
- **Variants and HGVS:**
  - 5′ mutation: Dspp P19L in the mouse, equivalent to human p.Pro17Leu. The human reference for it is cited as "(p.Pro17Leu)". The mouse HGVS string is not given in the verbatim text.
  - 3′ mutation: a CRISPR-made −1 frameshift with a single-nucleotide deletion, **c.1365delG**, plus an inserted FLAG tag (DYKDDDK) before the DPP N-terminus (DDPK). It produces 493 extraneous amino acids before a stop.
  - Human HGVS for the −1fs class is not given in the verbatim text.
- **Mouse alleles and genotypes:**
  - Dspp P19L: heterozygous (Dspp+/P19L) and homozygous (Dspp P19L/P19L) mice.
  - Dspp−1fs: heterozygous (Dspp+/−1fs) and homozygous (Dspp−1fs/−1fs) mice. The MMRRC ID 67179 comes from the model-written tail and is unverified.
  - The paper also describes a separate spontaneous Dspp−DPP allele (c.1380_1381insT), which it says "is being characterized but is not discussed further."
- **Dental phenotype (verbatim unless noted):**
  - P19L: "Dspp P19L dentin contained dentinal tubules but grew slowly and was softer and less mineralized than the wild-type." Enamel was "softer than normal" in incisors and showed reduced rod/interrod definition in molars.
  - −1fs: "lacked dentinal tubules, contained cellular debris, and was significantly softer and thinner" than wild-type and P19L dentin. Enamel was normal.
  - Nanohardness, dentin (GPa): WT 1.24; P19L het 1.08, hom 1.04; −1fs het 0.84, hom 0.8.
  - Nanohardness, enamel (GPa): WT 3.82; P19L het 2.88, hom 2.94; −1fs het 3.76, hom 3.78. The enamel reduction was P19L-specific.
  - Accelerated attrition: P19L molars showed accelerated attrition. −1fs molars showed "accelerated attrition, and sometimes crown failures." Whole-crown failures occurred only in −1fs mice.
  - Alveolar bone: recession was seen in −1fs molars and incisors at 7 weeks.
  - Predentin width, pulp chamber measurements and dentin mineral density values: not given in the verbatim text. The model-written tail says the same.
- **Human DGI type II vs III correspondence:** The verbatim text does not state this. The model-written tail says the authors propose 5′ mutations be classed as DGI-III and severe −1 frameshifts as DGI-II, and that mild ones be DD-II. I could not check this against the source. It rests on the model-written summary.
- **Heterozygotes:** Affected. Dspp+/−1fs incisors and molars showed translucent dentin and the same dentin-tubule loss as homozygotes. Dspp+/P19L dentin showed the same malformations as homozygotes, with "minimal differences" between them. The introduction also says that Dspp heterozygous knockout mice "show either no dentin phenotype, or mild dentin defects not evident until old age."
- **Mechanism:**
  - Impaired secretion: "Secretion of the mutant Dspp P19L protein was impaired and it accumulated within the ER." This is stated in the introduction, citing the earlier in vitro work (ref 17), which is the Lee 2013 paper above.
  - For −1fs, the authors describe the frameshifted DSPP as retained in cells, not secreted; that is in the model-written tail. The verbatim text includes the in situ and immunohistochemistry data on this but I did not read that section in full.
  - Dspp mRNA: the −1fs allele's mRNA was lower, "suggesting that the Dspp−1fs mRNA was selectively degraded or the cells expressing it deteriorated."
  - ER stress/UPR: mentioned only as a possible cause of variable severity, according to the model-written tail. Not tested in the read text.
  - Ca²⁺-dependent aggregation: not addressed.
  - Loss-of-function and haploinsufficiency: the introduction says "simple loss-of-function mutations do not cause dominant dentin malformations in humans." The model-written tail adds that the authors argue against loss of function.
- **DSP/DGP/DPP processing and BMP1:** Not addressed in the read text. The FLAG tag is placed at the DSP-DPP cleavage site.
- **DPP and hydroxyapatite nucleation:** Not addressed in the read text. The model-written tail mentions pig DSP covalent dimers, cited from a review.

## 3. ScienceDirect S1882761626000013: not retrieved

WebFetch returned HTTP 403 from ScienceDirect. Per the rules, this is permanent, so I did not retry or try variants. Nothing from this paper is in this report.

## 4. von Marschall / Fisher 2012, J Bone Miner Res

- **Found via search:** the PubMed search page (HTTP 200) lists the paper as PMID **22392858**. Authors: von Marschall Z, Mok S, Phillips MD, McKnight DA, Fisher LW. *J Bone Miner Res* 2012 Jun;27(6):1309-21. DOI 10.1002/jbmr.1573. The title begins "Rough endoplasmic reticulum trafficking errors by different classes of mutant dentin sialophosphoprotein (DSPP)" and continues with a claim about dominant-negative effects in DGI and DD by entrapping normal DSPP.
- **Abstract: not retrieved.** The PubMed article page (`pubmed.ncbi.nlm.nih.gov/22392858/`) returned HTTP 203 with a cookie prompt, so I could not get the abstract. The search snippet gives only fragments, including "Families with nonsyndromic dentinogenesis imperfecta (DGI)…" and "Trafficking out of the rER by coexpressed normal DSPP was reduced in a dose…". The snippet is truncated, so it is not the abstract. The PMC free full text was linked from the search page, but I did not have its link and did not fetch it.
- **Related search result:** Nam AS et al. 2014, PMID 24844412, is listed. Its snippet says that most DSPP mutations causing non-syndromic dentin disease start their dominant-negative effects by failing to exit the ER. It is a different paper and I did not read it.
- **Relationship to item 1:** The Lee 2013 paper (item 1) cites a rough-ER trafficking study as ref 27, which matches this paper's topic. It does not name the paper.

---

## Not retrieved or not answered

- Item 3 (ScienceDirect): HTTP 403. Skipped.
- Item 4 abstract: PubMed article page returned HTTP 203 (cookie wall). Not verbatim.
- BMP1/tolloid processing and DPP hydroxyapatite nucleation: not covered by any page I could read. The Lee 2013 paper only cites refs on this. Those cited papers are not fetched.
- Ca²⁺-dependent aggregation: not covered by any page I could read.
- Human HGVS for the −1 frameshift class and the mouse HGVS for P19L: not given in the verbatim text.

## Source status

- **Paper 1, PMC2600777 (Barron et al. 2008): not retrieved.** The fetch returned HTTP 200 with a reCAPTCHA "Checking your browser" interstitial and no article text. This is a permanent failure for this URL, so sending it again would likely return the same page. Nothing from paper 1 is reported below. The DOI is 10.1186/1750-1172-3-31 if you want another route.
- **Paper 2, PMC4666581 (de La Dure-Molla et al. 2015): read.** The verbatim text covers the abstract, introduction, dentinogenesis, the Shields-type descriptions, the proposed classification, the conclusion and references 1–14. The model-extracted summary for the rest said the body was missing, which conflicts with the verbatim text, so I relied on the verbatim text. Table 2 (the mutation table) did not render as text, so the named mutations are not available to me.
- **Paper 3, PMC7818184 (Chen et al. 2018/2019): read.** This is a review of dentin dysplasia type I, not DGI. The verbatim text covers the abstract and body.

Quotes below are from non-preapproved sources and are kept under 125 characters. Other text is paraphrase.

## Paper 2: de La Dure-Molla M, Philippe Fournier B, Berdal A. Eur J Hum Genet 2015;23(4):445-51. PMID 25118030. Final URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC4666581/

**Shields classification (1973), as described in the paper**
- DGI type I: syndromic, associated with osteogenesis imperfecta. The paper says DGI-I "is not an independent dental disease but an oral manifestation of osteogenesis imperfecta" (quoted from paper 3's text, which uses the same wording). The paper excludes it from the new classification.
- DGI type II (OMIM 125490): autosomal dominant. "The teeth exhibit a grey blue, or amber brown and opalescent discolouration and small height."
- DGI type III (OMIM 125500): "Clinically, it is like DGI-II." Pulp enlargement gives "shell teeth" on radiographs. The paper says it is "quite exclusively described in the triracial sub-population of Maryland, the 'Brandywine isolate'."
- DD type I (OMIM 125400), radicular: teeth look normal. Roots are shorter, sometimes absent, merged or taurodont, with a conical apex. Pulp is replaced by mineralised tissue with crescent-shaped radiolucent lines. Periapical lesions are frequent. The first sign is tooth mobility leading to premature exfoliation. The paper says the "autosomal dominant trait with complete penetrance" applies here.
- DD type II (OMIM 125420), coronal: same expression as DGI-II but only in deciduous teeth. Permanent teeth are "normal in colour, shape and height." Radiographs show a "thistle-tube" pulp and frequent pulp stones.

**Proposed classification (Table 1 and Table 3)**
- Radicular dentin dysplasia replaces Shields DD-I.
- All DSPP-related isolated disease is called "Dentinogenesis Imperfecta (DI)", on a mild / moderate / severe continuum. The paper's words: "We propose that all DSPP diseases are called exclusively 'Dentinogenesis Imperfecta (DI)'."
- Shields DD-II is treated as a mild form. Shields DGI-III is treated as a severe form. DGI-II is the moderate form.
- Table 3, as recoverable from the rendered text (cells are fragmented, so the column mapping is my reading):
  - Mild: crown colour normal or light grey; crown bulbous with increased constriction at the CEJ and short; attrition from enamel chipping upward; partial pulp obliteration with a "thistle-shaped" appearance; thin, short roots; periapical pathology.
  - Moderate: blue-grey, amber, opalescent; bulbous, short crown; attrition; roots thinner and shorter; "Narrowed pulp to complete obliteration".
  - Severe: brown, opalescent; enlarged pulp with "shell teeth" appearance; all DI features, especially permanent teeth.
- Mild forms "were described solely in permanent teeth" and were previously diagnosed as DD-II.

**Clinical description (DGI)**
- Colour: grey-blue, amber-brown, opalescent. The paper notes that for DD-I, colour is not a reliable criterion, since some authors describe brown/blue or yellow/grey discolouration.
- Crowns: "bulbous crowns because of an important cervical constriction, short and thick roots and pulp obliteration." The paper also says "Crowns showed a short and bulbous aspect."
- Enamel: enamel is often dislodged because the enamel-dentin junction is altered. The exposed hypomineralised dentin wears quickly. Attrition ranges from a few facets to complete loss of the crown.
- Pulp: obliteration ranges from total or partial, in either dentition. In DGI-III the pulp is enlarged.
- Periodontal disease is frequent without caries.
- Deciduous vs permanent: "Primary teeth are often more severely affected than permanent teeth." The paper says this was confirmed in all reviewed cases.
- Periapical radiolucency was not constant across reports.

**Radiographic features**
- DGI: bulbous crowns with marked cervical constriction, short and thick roots, pulp obliteration, which the paper calls "pathognomonic".
- DD-I: short roots with conical apex, taurodontism, crescent-shaped pulpal remnants parallel to the cementoenamel junction, or total obliteration.
- DD-II: "thistle-tube" pulp, large pulp chamber with thin canals, pulp stones.
- DGI-III: pulp enlargement, "shell teeth".

**Dentin histology and ultrastructure**
- Histology of DGI teeth shows few, large dentinal tubules running in different directions, with atubular areas.
- Enamel fractures follow the striae of Retzius. The enamel-dentin junction is altered, which explains enamel chipping.
- Synchrotron tomography and small-angle X-ray scattering showed abnormal shape and thickness of crystallites.
- Dentin is about 90% type I collagen and 10% non-collagenous proteins. The paper does not give mineral content or microhardness values.
- DSP is described as "a sialic acid-rich proteoglycan with few phosphorylations", and DPP as highly phosphorylated.
- DPP initiates hydroxyapatite formation at low concentration and inhibits growth at high concentration (in vitro).
- Mantle dentin, DEJ scalloping (beyond the enamel-dentin junction alteration above) and microhardness are not described in the text I read.

**Genetics**
- DSPP encodes a single mRNA that gives three proteins (DSP, DGP, DPP), cleaved by astacin and MMP-family proteases.
- "The DSPPs are encoded by a 5-exon gene." Exons 2, 3, 4 and the start of exon 5 encode DSP. DGP and DPP are encoded by the end of exon 5.
- DSPP is expressed mainly in odontoblasts. Low levels are also found in the inner ear, periodontal ligament and bone.
- Chromosome: the paper gives chromosome 4 (via reference 12). It places the DGI-II candidate gene "on chromosome 4q21 by linkage analysis between markers D4S2691 and D4S2692." It does not say 4q22.
- The DSPP gene is said to belong to the SIBLING cluster, described as "implicated in mineralization of dental and bone tissues notably by modulation of matrix metalloproteinases activity."
- Variants: "To date 38 pathological variants have been described in the DSPP gene, located in the peptide signal region, within the DSP region and within the DPP region." Of these, 28 cause DGI-II, 8 cause DD-II and 2 cause DGI-III. None is in the DGP coding region.
- Named mutations, nomenclature, signal-peptide variants, the IPV motif and exon 5 frameshifts: not in the readable text. These are in Table 2, which did not render.
- Genotype-phenotype: "The same DSPP variant could result in a moderate or severe phenotype, previously diagnosed for DG-II or/and DGI-III." The paper also says correlating genotype and phenotype is hard because of environmental factors and the three protein products, with DSP:DPP molar ratio cited as 1:10.
- The paper cites Dong et al for a DSPP variant in a Brandywine DGI-III family that confirmed the allelic relation between DGI-II and DGI-III.

**Penetrance and expressivity**
- For DD-I: "autosomal dominant trait with complete penetrance" (citing reference 49).
- Expressivity: "The expression variability, even in the same family, is a constant observation in this hereditary condition." The paper also says DGI-II and DGI-III "could be found on subjects of the same family, and even in the same patient."

**Incidence and prevalence**
- Witkop (1975, ref 5): DGI estimated at 1/6000 to 1/8000. DD at 1/100,000. The paper notes these are US-only data from 1975.
- Brandywine isolate: "the highest incidence of all dental genetic diseases at 1 in 15" (citing ref 40).
- DD-I: about 1/100,000 (citing Witkop and Kalk et al 1998 in paper 3).
- DD-II prevalence is not reported.

**Differential diagnosis**
- DD-I is distinguished from hypophosphatasia by premature loss of teeth with root-length changes.
- Paper 2 also says DD-II and DGI-II are very similar and can be told apart mainly by permanent-tooth appearance.

**Management and treatment**
- The readable text of paper 2 gives no management section. Treatment is covered in paper 3 (below).

**Other statements**
- Paper 2 does not mention DGI with hearing loss or DFNA39, or a relation to COL1A1/COL1A2. Its only OI statement is the note that syndromic DGI-I "is not concerned by this new classification since it is a whole different pathology."
- The model summary says reference 28 covers "DGI type I with or without hearing loss linked to distinct DSPP mutations". I could not verify this in the body text.
- Its conclusion: "isolated dentinogenesis imperfecta should actually be regarded as a single entity with an important variability of expression."
- Variants are catalogued at the LOVD DSPP site (lovd.nl/DSPP) per the paper.

## Paper 3: Chen D, Li X, Lu F, Wang Y, Xiong F, Li Q. "Dentin dysplasia type I—A dental disease with genetic heterogeneity." Oral Dis 2018 Apr 10;25(2):439-446 (issue date 2019 Mar). PMID 29575674. DOI 10.1111/odi.12861. Final URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC7818184/

This review is about DD-I, so its DGI content is limited to classification and genes:
- DGI type I, "considered a clinical manifestation of syndrome osteogenesis imperfecta", is linked to COL1A1 and COL1A2 (abstract).
- DSPP mutations are responsible for DGI-II, DGI-III and DD-II (abstract).
- The paper says DSPP is "the pathogenic gene of DGI-II, DGI-III, and DD-II, but not DD-I."
- It describes DGI-I, II, III and DD-II as sharing "amber translucent crowns accompanied by significant attrition," with short, thin roots and obliterated pulp. DD-I teeth look normal but have sharp or absent roots.
- It gives the DD-I radiographic types 1a–1d (after Carroll et al 1991).
- Histology: "Deeper layers of dentin exhibit an atypical tubular pattern with an amorphous, atubular area." The DEJ "is either smooth or scalloped."
- DD-I genes (Table 1): SMOC2 (6q27, splice mutation, autosomal recessive family), VPS4B (18q21.33, splice mutation), SSUH2 (3p26.1, missense c.353C>A).
- Treatment: "Treatment aims to remove infection, preserve existing teeth, enhance occlusion, and restore esthetics." Options include endodontic therapy, periapical curettage, and extraction for necrotic teeth with abscess.
- Differential diagnosis includes Morris and Augsburger skeletal syndrome, VDDR-I, VDRR, and familial tumoral calcinosis.

## Paper 1 (PMC2600777)

Not retrieved, so no content from it is reported. Items 1 and 2 of your list (the Shields definitions, the clinical features and the genetics in Barron et al) are therefore only covered by paper 2.

## Gaps
- Named DSPP mutations, phenotypes, signal-peptide variants, IPV motif and exon 5 frameshifts are in Table 2, which did not render. The LOVD site above is the paper's own pointer.
- Mantle dentin, microhardness and mineral content are not given in the text I read.
- Paper 2 gives chromosome 4q21, not 4q22, for the DGI-II linkage.
- Management is only covered for DD-I in paper 3.
- The DGI-with-hearing-loss / DFNA39 statement rests only on the model summary and is not verified.

All 15 URLs were fetched. Fourteen returned content; the MONDO annotation request returned HTTP 404. The HGNC response came back as XML, not JSON, because WebFetch cannot send the Accept header.

## HPO terms (ontology.jax.org)

**1. HP:0000703, Dentinogenesis imperfecta** (`https://ontology.jax.org/api/hp/terms/HP%3A0000703`)
- Definition: "Developmental dysplasia of dentin."
- Comment: teeth are discolored (blue-gray or yellow-brown) and translucent, weaker than normal, and prone to wear, breakage and loss.
- Synonyms: none. Xrefs: none. descendantCount: 3.
- Parent terms: not in the response.
- Translations are present (TR, DE, ES, IT, NL, JA, CS, FR, ZH).

**2. HP:0010299, Abnormal dentin morphology** (`https://ontology.jax.org/api/hp/terms/HP%3A0010299`)
- Definition: "Any abnormality of dentin."
- Synonyms: Abnormal dentin; Abnormality of dentin; Abnormality of dentine; Dentin anomaly.
- descendantCount: 5. Parent terms: not in the response.

**3. HP:0010292, Absent uvula** (`https://ontology.jax.org/api/hp/terms/HP%3A0010292`)
- Definition: "Lack of the uvula."
- Comment: sometimes accompanies submucous cleft palate, which should be coded separately.
- Synonyms: Absent palatine uvula; Congenital absence of uvula; Missing uvula; Uvula aplasia; Agenesis of uvula.
- publicationReferences: PMID:19125428. descendantCount: 0. Parent terms: not in the response.

**4. HP:0000670, Carious teeth** (`https://ontology.jax.org/api/hp/terms/HP%3A0000670`)
- Definition: a multifactorial bacterial infection affecting tooth structure, used for more than expected dental caries.
- Synonyms: Caries; Cariosity of teeth; Dental caries; Dental cavities; Early dental caries; Frequent caries; Tooth cavities; Tooth decay; Dental decay; Rotting teeth.
- descendantCount: 0. Parent terms: not in the response.

## HPO annotation endpoints (ontology.jax.org)

**5. MONDO:0018849, annotation** (`https://ontology.jax.org/api/network/annotation/MONDO%3A0018849`): **HTTP 404 Not Found.** This is a permanent failure, so resending the URL would fail the same way. No data was returned.

**6. OMIM:125490** (`https://ontology.jax.org/api/network/annotation/OMIM%3A125490`)
- Disease: name "Dentinogenesis imperfecta 1", mondoId MONDO:0007441. The description text refers to DGI-2 ("weakness and discoloration of all teeth").
- Phenotypes (frequency, onset and sex are blank for all):
  - Connective tissue: HP:0000703 Dentinogenesis imperfecta (PMID:11175779)
  - Inheritance: HP:0000006 Autosomal dominant inheritance (PMID:11175779)
  - Head and neck: HP:0006286 Yellow-brown discoloration of the teeth (PMID:11175779)
- Genes: NCBIGene:1834 (DSPP). medicalActions: none.

**7. OMIM:125500** (`https://ontology.jax.org/api/network/annotation/OMIM%3A125500`)
- Disease: name "Dentinogenesis imperfecta, shields type III", mondoId MONDO:0007442.
- Phenotypes (frequency, onset and sex are blank for all):
  - Connective tissue: HP:0000694 Odontodysplasia (OMIM:125500); HP:0009722 Dental enamel pits (PMID:6579461); HP:0000703 Dentinogenesis imperfecta (PMID:6579461)
  - Inheritance: HP:0000006 Autosomal dominant inheritance (OMIM:125500)
  - Head and neck: HP:0009102 Anterior open-bite malocclusion (PMID:6579461); HP:0000700 Periapical bone loss (PMID:6579461)
- Genes: NCBIGene:1834 (DSPP). medicalActions: none.

## EBI OLS4 searches

**8. "pulp obliteration", ontology=hp** (`https://www.ebi.ac.uk/ols4/api/search?q=pulp%20obliteration&ontology=hp`): numFound 1.
- HP:0006350, label "Pulp obliteration", not obsolete.
- Exact synonyms: Obliteration of the pulp chamber; Pulp canal obliteration; Reduced size of pulp chamber of tooth; Small pulp chamber of tooth.
- Narrow synonym: Narrowing of pulp chamber of tooth. Related synonym: Crescent/chevron-shaped pulp chambers.
- Description: "Mineralized substance filling the entire dental pulp space."

**9. "bulbous tooth crown", ontology=hp** (`https://www.ebi.ac.uk/ols4/api/search?q=bulbous%20tooth%20crown&ontology=hp`): numFound 1.
- HP:0033780, label "Bulbous tooth", not obsolete. No synonyms listed.
- Description: "A tooth crown with a marked cervical area constriction."

**10. "dentinogenesis imperfecta", ontology=mondo** (`https://www.ebi.ac.uk/ols4/api/search?q=dentinogenesis%20imperfecta&ontology=mondo`): numFound 12; the response contains 10 of these docs.
- MONDO:0018849, "dentinogenesis imperfecta". Exact synonyms include DGI, DI, non-syndromic DGI, DGI without OI, opalescent teeth without OI.
- HP:0000703, "Dentinogenesis imperfecta" (listed under the MONDO ontology, no description).
- MONDO:0007442, "dentinogenesis imperfecta type 3". Exact synonyms include DGI-III and Brandywine type dentinogenesis imperfecta.
- MONDO:0007441, "dentinogenesis imperfecta type 2". Exact synonyms include DGI-2, DI-2, Capdepont teeth. Related synonym: DGI1.
- MONDO:0011571, "deafness, autosomal dominant 39, with dentinogenesis imperfecta 1".
- MONDO:0011501, "wormian bone-multiple fractures-dentinogenesis imperfecta-skeletal dysplasia". Exact synonym: Suarez-Stickler syndrome.
- MONDO:0019102, "dentinogenesis imperfecta-short stature-hearing loss-intellectual disability syndrome".
- MONDO:7770372, "dentinogenesis imperfecta, dog".
- MONDO:0100325, "odontochondrodysplasia 1". Exact synonyms include Goldblatt syndrome, ODCD.
- MONDO:0008148, "osteogenesis imperfecta type 4".

**11. "abnormal tooth wear", ontology=hp** (`https://www.ebi.ac.uk/ols4/api/search?q=abnormal%20tooth%20wear&ontology=hp`): HTTP 200, numFound 0, no docs returned.

**12. "odontoblast", ontology=cl** (`https://www.ebi.ac.uk/ols4/api/search?q=odontoblast&ontology=cl`): numFound 15; the response contains 10 of these docs.
- CL:0000060, "odontoblast". Description: "Skeletogenic cell that secretes dentine matrix, is derived from the odontogenic papilla, and develops from a preodontoblast cell."
- CL:0007012, "non-terminally differentiated odontoblast"
- CL:0007013, "terminally differentiated odontoblast"
- CL:0000140, "odontocyte"
- CL:0000345, "dental papilla cell"
- CL:0007003, "preodontoblast"
- CL:0007001, "skeletogenic cell". Exact synonym: scleroblast.
- GO:1901330, "negative regulation of odontoblast differentiation"
- GO:1901331, "positive regulation of odontoblast differentiation"
- GO:0071895, "odontoblast differentiation"

**13. "dentine", ontology=uberon** (`https://www.ebi.ac.uk/ols4/api/search?q=dentine&ontology=uberon`): numFound 31; the response contains 10 of these docs.
- UBERON:0001751, "dentine". Exact synonyms: dentine of tooth, dentin. Narrow synonym: predentin.
- UBERON:0011587, "pre-dentine". Exact synonyms: pre-dentine tissue, predentin, predentine tissue.
- UBERON:0004755, "skeletal tissue"
- UBERON:4000106, "vasodentine". Exact synonym: vascular dentine.
- UBERON:0001091, "calcareous tooth". Exact synonyms include tooth, vertebrate tooth, dental element.
- UBERON:0001752, "enamel". Exact synonyms: enamel of tooth, tooth enamel, enamel tissue. Related: enameloid.
- UBERON:0001763, "odontogenic papilla". Exact synonym: odontogenic condensation. Related: dental papilla, dentinal papilla, dermal papilla.
- UBERON:7500085, "endodontium". Exact synonyms: endodont, pulp-dentin complex.
- UBERON:0003268, "tooth of lower jaw"
- UBERON:4000123, "odontode tissue". Related: dental tissue.

## UniProt (rest.uniprot.org)

**14. Q9NZW4** (`https://rest.uniprot.org/uniprotkb/Q9NZW4.txt`), flat file, HTTP 200
- ID: DSPP_HUMAN, Reviewed (Swiss-Prot). Length 1301 aa, MW 131151 Da. Sequence version 2, entry version 178 (04-NOV-2026).
- Accessions: Q9NZW4 (primary), A8MUI0, O95815.
- Protein name: Dentin sialophosphoprotein. It contains Dentin phosphoprotein (alt name Dentin phosphophoryn, short DPP) and Dentin sialoprotein (short DSP). The entry does not use "DGP" anywhere.
- Gene: DSPP. Organism: Homo sapiens (9606).
- Chain features:
  - Signal peptide: 1–15
  - Chain 16–1301: Dentin sialophosphoprotein
  - Chain 16–462: Dentin sialoprotein (DSP)
  - Chain 463–1301: Dentin phosphoprotein (DPP)
- Other features: disordered regions at 55–89, 146–171 and 202–1301. Cell attachment site at 488–490.
- PTMs:
  - N-linked (GlcNAc...) asparagine glycosylation at 41, 49, 81, 130, 150, 190, 191, 209, 222, 275, 336 and 387
  - Phosphoserine at 259 ("by CK1") and 301
  - Comment: "DSP is glycosylated."
- Subcellular location: Secreted, extracellular space, extracellular matrix.
- Tissue specificity: expressed in teeth. DPP is synthesized by odontoblasts and transiently expressed by pre-ameloblasts.
- Function (from the entry): DSP may be important in dentinogenesis; DPP may bind calcium and facilitate initial mineralization of dentin matrix collagen.
- Disease annotations and variants (positions are in the mature-protein numbering the entry uses):
  - DFNA39/DGI1 [MIM:605594]: progressive high-frequency sensorineural hearing loss with dentinogenesis imperfecta. Variants Thr-17 (P→T) and Phe-18 (V→F).
  - DGI2 / Dentinogenesis imperfecta Shields type 2 [MIM:125490]: amber-brown, opalescent teeth that fracture and lose enamel; bulbous crown; pulpal obliteration common. Variants Val-15 (A→V), Ser-17 (P→S), Asp-18 (V→D) and Trp-68 (R→W, rs36094464). Dominant negative.
  - DGI3 / Dentinogenesis imperfecta Shields type 3 [MIM:125500]: similar teeth, with multiple periapical radiolucencies. Variants Leu-17 (P→L), Ser-17 (P→S) and Phe-18 (V→F).
  - DTDP2 / Dentin dysplasia 2 [MIM:125420]: deciduous teeth opalescent; permanent-tooth pulp chambers obliterated with thistle-tube deformity and pulp stones. Variant Asp-6 (Y→D), which does not translocate into the ER.
- Other annotated variant: Asn-243 (D→N, rs3750025), not linked to disease in the entry.
- Cross-references: HGNC:3054, MIM:125485 (gene), Ensembl ENSG00000152591, GeneID 1834, Orphanet 166260 (DGI2) and 166265 (DGI3).

## HGNC (rest.genenames.org)

**15. DSPP** (`https://rest.genenames.org/fetch/symbol/DSPP`): HTTP 200, returned as text/xml, not JSON.
- HGNC ID: HGNC:3054. Status: Approved. Locus type: gene with protein product.
- Entrez: 1834. Ensembl: ENSG00000152591. UniProt: Q9NZW4. OMIM: 125485.
- Location: 4q22.1.
- Alias symbol: DMP3. Previous symbols: DFNA39, DGI1.
- Name: dentin sialophosphoprotein. Gene group: SIBLING family.
- Other identifiers in the record: RefSeq NM_014208; MANE Select ENST00000651931.1 (NP_055023.2); CCDS43248; UCSC uc003hqu.3; MGI:109172; RGD:2525; Vega OTTHUMG00000161061; LRG_1242.
- Dates: approved 1997-01-08; modified 2023-01-20.

## 1. Gilani, Saikia, Anthonappa, "The genetics of non-syndromic dentinogenesis imperfecta: a systematic review" (PMC11865110)

- **Bibliographic:** Eur Arch Paediatr Dent. 2025 Jan 13;26(1):3–16. PMID 39806231. DOI 10.1007/s40368-024-00992-6. PMCID PMC11865110.
- **Fetch:** HTTP 200. Verbatim text covered the abstract, methods, results, Table 1, Table 2, and the start of the discussion. The tail (rest of discussion, conclusion, references) came from a model summary.
- **Studies:** 3,475 articles identified; 135 full texts assessed; 41 included; 10 with histopathology.
- **Total variants:** 59 DSPP mutations reported, from 37 publications. Table 1 row totals sum to 59. Four studies found variants in other genes (all by WES), in 15 patients from 6 families.
- **Distribution by region (Table 1 "total number of reported mutations"):** exon 2 = 5; intron 2 = 7; exon 3 = 7; intron 3 = 5; exon 4 = 1; exon 5 = 34. The text says exon 5 holds "58% of the reported mutations (34/59)".
- **Variant types, as the text reports them:** splice site 45% (n=118); missense 30% (n=79); nonsense 7% (n=18); insertion/deletion 4% (n=10). All frameshifts (n=38) are in exon 5. The text gives a denominator of "263 mutation categories". These n-values are the table's per-row counts, so the 263 appears to count cases or reports, not distinct variants. The percentages are consistent with that denominator. The text is internally inconsistent here and should not be read as 59 distinct variants by type.
- **COL1A1/COL1A2:** The abstract says four studies identified mutations in COL1A1 and COL1A2 "revealing non-syndromic DI cases, predominantly in individuals of Asian descent." The discussion says these genes "may serve as notable mutational hotspots associated with non-syndromic DI."
- **Ethnicity:** Text says "All reported mutations were identified in those of Asian descent" for COL1A1/COL1A2. Table 1 DSPP ethnicity counts include exon 2: Asian n=27, European n=10, American n=8; exon 5: Asian n=27, American n=23, European n=22, African n=9. The summary adds a remark that the higher Asian share may reflect geography, sampling, awareness, and publication bias. That remark is from the unread-by-me summary, not the verbatim text.
- **Genotype-phenotype statements (verbatim):**
  - "Exon 5 mutation leads to frameshift changes, often resulting in severe DI forms."
  - Non-DSPP DI "can exhibit a broader range of phenotypic presentations, sometimes overlapping with OI symptoms."
  - Histopathological differences "further distinguish non-DSPP cases from DSPP-related DI."
  - Summary only: the review's conclusion says variants in DSPP, COL1A1 and COL1A2 are implicated in "non-syndromic DI-II, -III and DD-II."
- **Specific variants (Table 1, selected):**
  - Exon 2: c.16T>G p.Y6D (7); c.44C>T p.A15V (8); c.49C>A p.P17T; c.49C>T p.P17S (9); c.50C>T p.P17L (18, DI-II).
  - Intron 2 (splice): c.52-3C>G; c.52-3C>A (20); c.52-2A>G; c.52-25del23bp (24).
  - Exon 3: c.52G>T p.V18F (13); c.133C>T p.Q45X (18, DI-II); c.53T>A p.V18D (18, DI-II/III); c.53T>G p.Val18Gly (2, DI-II); c.53T>C p.Val18Ala (2, DI-III).
  - Intron 3 (splice): c.135+1G>A (19); c.135+2T>C (16); c.135+3A>G (25).
  - Exon 4: c.202A>T p.R68W (9, DI-II).
  - Exon 5 (frameshift, selected): c.1918_1921delTCAG p.S640TfsX673 (6); c.2525delG (4); c.3135delC (7); c.3676delA (9); c.2134delA (4, DD-II).
  - COL1A1: c.1463G>C p.Gly488Ala (1, DI-I).
  - COL1A2: c.1009G>A p.Gly337Ser (2, Thailand); c.1171G>A p.Gly391Ser (9, Thailand/Korea, DI-I); c.3233G>A p.Gly1078Asp (3, Korea).
  - Table 1 contains more rows than these. I did not transcribe the whole exon 5 list.
- **Inconsistency noted:** Inclusion criteria were DI-II, DI-III, or DD-II, yet Table 1 labels several COL1A1/COL1A2 and some DSPP cases as DI-I.

## 2. Boonyakanog et al., "Beyond the diagnosis: Unraveling DSPP genotype-phenotype correlations in dentin dysplasia and dentinogenesis imperfecta" (PMC12830278)

- **Bibliographic (from the Europe PMC XML):** The Japanese Dental Science Review, vol 62, pp 46–56. Epub 15 Jan 2026 (print date shown as 12/2026). Authors: Boonyakanog A, Sriwangyang K, Eamtanaporn T, Krasaesin A, Fakhruddin KS, Chantarangsu S, Cho SD, Rokny HA, Porntaveetus T. PMID 41583696. PMCID PMC12830278. DOI 10.1016/j.jdsr.2026.01.001.
- **Fetch:** HTTP 200. The XML was read verbatim through the Table 1 section. Findings below marked "summary" come from the model summary of the rest, not the verbatim text.
- **Scope:** Systematic review of 48 publications, 70 distinct DSPP variants, 99 genotype-phenotype records. Searched PubMed, Scopus, Embase and ProQuest, Jan 1997–Aug 2025. PROSPERO CRD420251170506.
- **Exon distribution (verbatim):** exon 5 holds 61% (43/70). Exons 2, 3 and 4 plus introns 2 and 3 hold the other 39%. Exon 4 has the fewest, 4% (3/70).
- **Variant types (verbatim):** frameshift 60% (42/70); splice site 22% (15/70); missense, nonsense and signal-peptide variants 4–6% each.
- **Exon × type (verbatim):** all intronic variants are splice site. Exon 2 has 3 signal-peptide and 3 cleavage-site variants. Exon 3 is 57% splice and 43% missense. Exon 4 is mostly nonsense (67%) with one missense. Exon 5 is 98% frameshift (42/43) plus one nonsense.
- **Phenotype distribution (verbatim):** DGI-II 47% (47/99); DD-II 22% (22/99); unspecified DGI 14% (14/99); DGI-III 13% (13/99); DD-II/DGI-II 3% (3/99).
- **Correlations (verbatim):**
  - DD-II "was significantly associated with variants in exon 5" and most often frameshift.
  - DGI-III "was strongly linked to variants in exons 2 and 3 and was notably absent in cases with exon 5 variants," "primarily driven by missense variants." The abstract instead names signal-peptide, splice-site and missense variants for DGI-III, so the two passages differ in emphasis.
  - Unspecified DGI showed association with exon 4 and nonsense variants.
  - DGI-II and DD-II/DGI-II showed no significant association with location or type, which the authors read as an intermediate phenotype.
- **Dental features:** Table 1 gives chi-square p-values (verbatim). Summary only: DD-II had clinically normal permanent dentition (95.45%), thistle-shaped pulp chambers (72.73%), and pulp stones (27.27%). DGI-III had severe attrition (84.62%), shell teeth (30.77%) and pulp exposure (38.46%). DGI-II had complete pulp obliteration (74.47%).
- **Mechanism classes (summary only, not verified verbatim):** dominant-negative Ca²⁺-dependent aggregation for exon 5 frameshifts; ER retention for signal-peptide, IPV-motif and missense variants; splicing defects in introns 2–3 causing exon 3 skipping; haploinsufficiency or partial dominant-negative effects proposed for DGI-II. The summary calls these hypotheses. It also reports mouse-model data (Dspp P19L, Dspp −1fs) that the summary attributes to the paper.
- **Verbatim abstract wording:** the review highlights "a continuous spectrum of DSPP disorders," and says integrating DSPP genotyping into diagnostic workflows is "essential to predict disease progression."
- **Caveats (abstract/summary):** evidence is mainly case reports and small families; the summary notes publication bias toward severe presentations.

## 3. Caravello et al., "Diagnosis complexity of dentinogenesis imperfecta involving DSPP genetic variants" (PMC13217078)

- **Bibliographic:** J Med Genet. 2026 Mar 12;63(6):e111345. PMID 41819808. DOI 10.1136/jmg-2025-111345. PMCID PMC13217078. Received 2025 Nov 4; accepted 2026 Feb 13. Authors: Caravello G, Jiménez-Armijo A, Kawczynski M, Rey T, Antin M, Roth A, Lamouche JB, Gouronc A, Alioua A, Schluth-Bolard C, Bloch-Zupan A (on behalf of the O-Rares Consortium). Note: the model summary gave 2025 and no PMID. The verbatim page says 2026 and gives PMID 41819808.
- **Fetch:** HTTP 200. The page was read verbatim through the discussion start. Summary-only items are marked.
- **Cohort:** 112 individuals (42 index cases, 70 relatives), recruited 2016–2024. Molecular diagnosis in 41 families. Verbatim: DSPP variants were found in all index cases except one. Summary: 22 pathogenic/likely pathogenic variants, 14 novel, 8 previously reported.
- **Method:** GenoDENT NGS panel (653 genes) with added DSPP repeat probes. Sanger and long-range PCR for exon 5. Oxford Nanopore long-read sequencing for inconclusive or negative cases.
- **Variants (verbatim):**
  - NGS identified 14 variants: 1 in exon 3 and 13 in exon 5.
  - c.52G>T p.(Val18Phe), previously described, found in families 1–3 with isolated DI.
  - c.2656_2657insGTGAAGCA was first called by NGS in families 21–28, then reclassified. ONT with the T2T reference gave c.2652del p.(Asp884Glufs*430) instead.
  - Novel ONT-detected variants: c.1887del (family 13), c.1937del (15), c.2483del (17), c.2827del (29), c.3180del (32).
  - Summary only: c.3480del, c.1729_1924del p.(Ser577Alafs672), c.1814del p.(Ser605Metfs709).
- **Phenotypic variability (verbatim):** the findings "confirm that DSPP variants harbour a high degree of phenotypic variability, particularly within exon 5." Families 6, 14 and 15 show dentin dysplasia features. Summary only: relatives sharing a variant can differ in severity, and modifier factors are proposed. The abstract says the variability "suggests the influence of modifier factors."
- **Mechanism (verbatim):** the mutant frameshifts give a −1 frame shift with a hydrophobic C-terminal extension and termination at a downstream stop codon.
- **Diagnostic recommendations:**
  - Verbatim: ONT should serve "as an effective second-line strategy" when short-read sequencing is inconclusive. The authors revised the workflow "to begin directly with long-read DSPP exon 5 sequencing using ONT."
  - Verbatim conclusion: "integrating long-read sequencing into routine diagnostics" is valuable.
  - Summary only: send VUS for functional analysis; use a short-read gene panel or exome if no variant is found; offer genetic counselling to affected families.

## 4. Xue, Wu, Zhao, Wei, Hu, "Progress in the pathogenic mechanism, histological characteristics of hereditary dentine disorders and clinical management strategies" (fcell.2024.1474966)

- **Bibliographic:** Front Cell Dev Biol. 2024; 12:1474966. Published 9 Dec 2024. Review article, section Molecular and Cellular Pathology. DOI 10.3389/fcell.2024.1474966. Authors: Qing Xue and Zhina Wu (equal first), Yinuo Zhao, Xiaoxi Wei, Min Hu (corresponding). Affiliation: Hospital of Stomatology, Jilin University. PMID not shown in the fetched content.
- **Fetch:** HTTP 200. The verbatim text covers the abstract, introduction, and start of section 2. The middle (DSPP biology, odontoblast biology, management) came from the model summary. A re-read of the tail returned only boilerplate; I did not read the section 3 management text verbatim.
- **Verbatim statements:**
  - Abstract: hereditary dentine disorders are "autosomal dominant diseases that affect the development and structure of dentine."
  - Abstract: "the pathogenesis of hereditary dentine disorders has been poorly clarified and the clinical intervention is limited."
  - Introduction: common causative genes are DSPP, COL1A1, COL1A2, SMOC2, VPS4B and SSUH2.
  - Incidence (citing Barron et al. 2008): DGI about 1/6000–1/8000; DD about 1/100,000.
  - DGI-I is "a main manifestation of OI in the oral system"; COL1A1/COL1A2 mutations cause DGI-I. Table 1 lists many variants.
  - DGI-II is "commonly referred to as hereditary opalescent dentine." Its prevalence is cited as about 1/8000, and DSPP is the cause.
  - DGI-III "also known as 'Brandywine isolate'" is described as a rare, severe phenotype with "shell teeth."
  - DD-II primarily affects crown dentine, with "thistle tube" pulp chambers and pulp stones.
- **Dentin formation, DSPP biology, odontoblast biology (summary only):**
  - DSPP-derived proteins regulate "dentine mineralization initiation, collagen mineralization and maturation processes."
  - Exon 2 encodes the signal peptide; exons 2–4 the N-terminal DSP; exon 5 the C-terminal of DSP and DPP.
  - DPP is an acidic protein rich in Asp-Ser-Ser that promotes crystal nucleation. Signal-peptide mutations can impair ER translocation.
  - DSPP is expressed in odontoblasts and transiently in ameloblasts. VPS4B regulates odontoblast differentiation via Wnt/β-catenin.
- **Hereditary dentine disorders (summary only):** over 50 DSPP mutation sites are linked to DGI-II, with genotype-phenotype correlation for DPP frameshifts. DGI-II and DGI-III may be one disease, since two families with the same mutation differed. DD-I is linked to SMOC2, VPS4B and SSUH2. Management is interdisciplinary: restoration, endodontics, oral surgery, and genetic counselling.

## Cross-checks and caveats

- All four fetches returned HTTP 200. No fetch failed.
- Several summary-tool statements were wrong. Paper 1's summary said its Results were absent, but the verbatim text includes them. Paper 2's summary said title and authors were not in the text, but the XML gives both. Paper 3's summary gave the wrong year and no PMID. Those points are corrected above.
- Paper 2 and paper 1 give different exon 5 shares (61% of 70 variants vs 58% of 59). They cover different variant sets and inclusion rules.
- Paper 2's DD-II/DGI-III/DGI-II correlations and percentages are chi-square-based. Only the summary gave the percentages, so treat those as unverified.

## Results for the five requests

Several of these pages are non-preapproved sources, so I kept every quoted fragment under 125 characters and paraphrased the rest. That means I could not reproduce the full abstracts or titles verbatim. The Europe PMC and PMC pages are linked below if you need the full text.

Every fetch returned HTTP 200. Some pages were truncated, and for those the later portion is a model-extracted summary, not verbatim text. I flag those parts.

### 1. Europe PMC record for PMID 22392858 (HTTP 200, JSON)

- **Title (paraphrased):** The paper is about rough ER trafficking errors caused by different classes of mutant DSPP, which produce dominant-negative effects in both dentinogenesis imperfecta and dentin dysplasia by entrapping normal DSPP. The title begins "Rough endoplasmic reticulum trafficking errors by different classes of mutant dentin sialophosphoprotein (DSPP)".
- **Authors:** von Marschall Z, Mok S, Phillips MD, McKnight DA, Fisher LW.
- **Journal:** J Bone Miner Res, 2012 Jun, volume 27, issue 6, pages 1309-1321.
- **Identifiers:** PMID 22392858; PMCID PMC3390460; DOI 10.1002/jbmr.1573.
- **Abstract (paraphrased, with short quotes):** The abstract says DSPP mutations cause nonsyndromic DGI and DD. It describes three mutation classes, with the mid-leader Y6D mutation not investigated. The second class changes or removes the first residues of mature DSPP ("IPV"), or retains the leader (A15V). These mutants were retained in the rER of transfected HEK293 cells. The third class is frameshifts in the 3' repeat domain. The abstract states that "Trafficking out of the rER by coexpressed normal DSPP was reduced in a dose-responsive manner." It proposes that DD is milder because the shorter remaining repeat domain captures less normal DSPP.
- **Full-text status:** Free full text is available in PMC.

### 2. Full text, PMC3390460 (HTTP 200)

Final URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC3390460/

The verbatim text covers the abstract, methods, and results up to the 5' and frameshift section. The rest was summarised by the extraction model, so the points marked "summary" below are not verbatim.

- **Mutation classes tested:**
  - Y6D (mid-leader missense) was not investigated in this report.
  - IPV-motif changes: ISV, ITV, IPD, IPF, and IPD3 (exon 3 skipping), plus the leader change A15V.
  - 3' frameshifts in the repeat domain, modelled as a DGI-like frameshift (about 287 repeat residues retained) and a DD-like frameshift (no repeats retained).
  - The readable text does not describe exon 5 frameshifts in those words.
- **Cell systems:** HEK293/HEK293A cells with transient transfection. Methods included Western blots, endoglycosidase H digestion, confocal microscopy with the rER marker PDI, a FLAG sandwich ELISA, and furin inhibition. Hybrid OPN-DSPP and DMP1-DSPP constructs, plus native OPN and chromogranin A, were used to test the IPV-like motif. Summary: no experiments in odontoblasts are reported.
- **How mutant DSPP is retained in the rER:**
  - Mutant full-length DSPP was sensitive to endoglycosidase H, which the authors read as high-mannose, rER-type glycosylation.
  - Mutants co-localised with PDI. The text says mutants were "predominantly co-localized (yellow) with the abundant and more widespread rER marker" (green), while WT was mostly in Golgi-like puncta.
  - Leader removal was normal for the IPV-motif mutants, so the block is not at signal-peptide cleavage.
- **Evidence that mutants entrap normal DSPP, and dose-dependence:**
  - The abstract reports dose-responsive reduction of normal DSPP exit.
  - Summary: with WT held constant, more mutant DNA reduced WT secretion. ISV caused about a 40% loss at equal amounts and more than 70% at a 4:1 mutant-to-WT ratio. The DGI-like frameshift suppressed WT more than the DD-like frameshift at each dose.
  - The authors used lanthanum precipitation as an in vitro stand-in for calcium binding, and state that some co-transfection data are "data not shown."
- **ER stress / UPR markers:** I did not find measurements of BiP/GRP78, CHOP, XBP1, ATF6 or PERK in the text I could read. Summary: the authors say rER stress is "likely activated," and treat this as a hypothesis. I could not read the full discussion, so this is not a complete check.
- **Conclusion:** The authors conclude the effects are dominant-negative, with mutant DSPP retained in the rER and trapping WT DSPP. They argue against haploinsufficiency: "loss of a single allele is recessive and that haploinsufficiency does not explain DD or DGI." Their supporting points are that +/- mice have normal teeth and -/- mice have dentin defects.

### 3. PMC4707025 (HTTP 200)

Final URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC4707025/

- **Title:** "The dentin phosphoprotein repeat region and inherited defects of dentin"
- **Authors:** Jie Yang, Kazuhiko Kawasaki, Moses Lee, Bryan M Reid, Stephanie M Nunez, Murim Choi, Figen Seymen, Mine Koruyucu, Yelda Kasimoglu, Ninna Estrella-Yuson, Brent P J Lin, James P Simmer, Jan C-C Hu.
- **Journal and year:** Mol Genet Genomic Med, 2015 Sep 7; 4(1):28-38.
- **Identifiers:** PMID 26788535; PMCID PMC4707025; DOI 10.1002/mgg3.176.
- **Repeat region and length polymorphism (verbatim text):**
  - Human DPP varies between 770 and 902 amino acids.
  - "There are 165 DSS sequences in human DPP." The page uses "Asp-Ser-Ser (DSS)" motifs rather than "SerSerAsp."
  - Overall, the study found 32 indels, forming 36 haplotypes.
- **Difficulty sequencing (verbatim text):** "the only way to sequence the DPP repetitive region was to clone PCR amplification products." The study used SMRT sequencing to read the repeat without cloning.
- **Frameshifts and disease:**
  - The abstract reports a novel frameshift, c.3504_3508dup (p.Asp1170Alafs*146), in Family 2.
  - Summary: 21 3' frameshifts in the exon 5 repeat region cause DD-II or DGI-II. The mutant protein is longer than normal DPP, and the authors propose rER retention with a dominant-negative effect.
  - The summary's title field was marked "not shown," but the verbatim page header gives the title, which I used above.

### 4. BMP1 query (hitCount 96, HTTP 200)

Final URL read: the query URL you gave, page 1 of 10. I read 6 records verbatim and the other 4 from the summary.

None of the top 10 abstracts I could read is about BMP1 processing of DSPP into DSP, DGP and DPP. The results are general DSPP or dental-biology papers.

- **Chun YP, Foster BL, Liang T, Kawasaki K. (2025)** "Functions of secretory calcium-binding phosphoproteins in dental mineralization." J Bone Miner Res 40(8):909-930. PMID 40318225; PMCID PMC12308831; DOI 10.1093/jbmr/zjaf062. Review. The abstract describes the DSP and DPP roles but does not mention BMP1.
- **Liang T, Smith CE, Hu Y, Zhang H, Zhang C, Simmer JP, Hu JC. (2025)** "DSP and DPP are dispensable for initiation of dentin and enamel mineralization but critical for circumpulpal dentin mineralization." Sci Rep 15(1):24913. PMID 40640300; PMCID PMC12246090; DOI 10.1038/s41598-025-09743-z. The abstract describes a Dspp-DPP CRISPR mouse, and says DSPP "is cleaved into the N-terminal dentin sialoprotein (DSP) proteoglycan." It does not mention BMP1 in the abstract.
- **Records not relevant to BMP1:** Equine tooth proteomics (PMID 42141522, 2026); Wairooy VW et al. on Bio-C Repair vs Biodentine in hDPSCs (PMID 39029909, 2025); Le SH and Nguyen SH on A-PRF+ and i-PRF in SCAPs (PMID 39347039, 2024); Zhang L et al. review of enamel matrix derivative (PMID 42266834, 2026).
- **Summary-derived, not verbatim:** Yan W et al. (2026, PMID 42966771, DOI 10.1038/s41368-026-00472-1); Seefried L et al. (2024, PMID 39276275); Iaquinta MR et al. (2025, PMID 40332455); Ruan X et al. (2023, PMID 37457289). Their titles and abstract excerpts concern pulp regeneration, hypophosphatasia, a collagen graft material and ALK3, not BMP1 processing.

A more targeted query, such as restricting BMP1 to the title or abstract fields, may find the processing papers. I did not run that search.

### 5. DFNA39 / hearing loss query (hitCount 64, HTTP 200)

Final URL read: the query URL you gave, page 1 of 10. I read 3 records verbatim and the other 7 from the summary.

None of the abstracts I could read mentions hearing loss or DFNA39 in its text. DFNA39 appears only as a keyword on the first record.

- **Boonyakanog A et al. (2026)** "Beyond the diagnosis: Unraveling DSPP genotype-phenotype correlations in dentin dysplasia and dentinogenesis imperfecta." Jpn Dent Sci Rev 62:46-56. PMID 41583696; PMCID PMC12830278; DOI 10.1016/j.jdsr.2026.01.001. Systematic review of 48 publications. Quote: "Exon 5 harboured 61 % of variants, predominantly frameshifts disrupting the repetitive dentin phosphoprotein (DPP) domain." Keywords include Dfna39.
- **Gao Q et al. (2025)** "A family study of dentinogenesis imperfecta shields type II caused by a novel DSPP mutation and investigations on the isolated stem cells from human exfoliated deciduous teeth." BMC Oral Health 25:503. PMID 40197225; PMCID PMC11978159; DOI 10.1186/s12903-025-05912-8. Quote: "A novel frameshift mutation, DSPP c.2695delA.N899fs, was identified in the family."
- **Wang Y et al. (2025)** "A Novel Variant in Dentin Sialophosphoprotein (DSPP) Gene Causes Dentinogenesis Imperfecta Type III: Case Report." Mol Genet Genomic Med 13(3):e70087. PMID 40040554; PMCID PMC11880773; DOI 10.1002/mgg3.70087. Novel signal-peptide variant c.38C>A (p.A13E). Quote: "The secretion of the variant DSPP protein was not detected."
- **Summary-derived, not verbatim:**
  - Zhu J et al. (2026), expert consensus on tooth developmental anomalies, PMID 41554697, DOI 10.1038/s41368-025-00401-8.
  - Hassib NF et al. (2024), isolated DGI with novel DSPP nonsense variants, PMID 38630328, DOI 10.1007/s00784-024-05636-z.
  - Xue Q et al. (2024), review of hereditary dentine disorders, PMID 39717845, DOI 10.3389/fcell.2024.1474966.
  - Joy-Thomas A et al. (2025), genetics of oral health review, PMID 40136761, DOI 10.3390/dj13030133.
  - Du Q et al. (2021), DGI-II family with a novel DSPP mutation, PMID 34988181, DOI 10.21037/atm-21-5369.
  - Off-topic in the summary: Hoff FW et al. (2026, PMID 41742372) on POLD1 lipodystrophy, and Piekos KM et al. (2024, PMID 39559541) on a dog with DGI.

Failures: none. All five fetches returned HTTP 200.

## Mouse and rat Dspp (items 1-5)

**1. MGI gene page** (https://www.informatics.jax.org/marker/MGI:109172, HTTP 200, last database update 11/10/2026)
- Symbol Dspp; name "dentin sialophosphoprotein"; synonyms Dmp3, Dpp, Dsp. MGI:109172; NCBI Gene 666279.
- Location: Chr5:104318578-104327993 bp, + strand (GRCm39); genetic map Chr5, 50.59 cM.
- Human ortholog: DSPP, HGNC:3054, NCBI Gene 1834, UniProt Q9NZW4, 4q22.1.
- Alleles (17 total, by type): Endonuclease-mediated 7; Targeted 3; Transgenic 4; Chemically induced (other) 1; Radiation induced 1; Spontaneous 1. Individual allele symbols other than the one below were not in the fetched content.
- Named allele: Dspp<sup>tm1Kul</sup> (MGI:2653208; synonym "Dspp-"), a targeted allele.
- Disease models: DOID:4154 dentinogenesis imperfecta (1 model, Dspp<sup>tm1Kul</sup> homozygotes, background involves 129/Sv x C57BL/6, J:84378). DOID:3388 periodontal disease (1 model, same allele, background B6;129-Dspp<sup>tm1Kul</sup>/Mmnc, J:241990).
- Phenotype summary on the page: 33 phenotypes from 4 alleles.

**2. Alliance gene API** (https://www.alliancegenome.org/api/gene/MGI:109172, HTTP 200, JSON)
- Symbol Dspp; species Mus musculus; primaryExternalId MGI:109172; GRCm39 chr5:104318569-104327993 (+).
- The JSON has no ortholog block, so no HGNC, RGD or ZFIN ortholog entries were returned. Human (HGNC:3054) and rat (RGD:2525) orthologs appear on the MGI and RGD pages instead. No zebrafish ZFIN ID appeared in any fetched page.
- Automated description (paraphrased): predicted collagen binding activity; used to study dentinogenesis imperfecta and periodontal disease; human orthologs implicated in autosomal dominant nonsyndromic deafness, dentin dysplasia type II, and dentinogenesis imperfecta.
- Cross-references include NCBI_Gene:666279, ENSEMBL:ENSMUSG00000053268, and UniProt A1L2Z1, E9Q9Z9, P97399, Q1JQ89.

**3. Alliance disease API** (https://www.alliancegenome.org/api/gene/MGI:109172/disease?limit=50): HTTP 404. This is a permanent failure, so resending the URL would fail the same way. No disease data from this endpoint.

**4. Alliance phenotypes API** (https://www.alliancegenome.org/api/gene/MGI:109172/phenotypes?limit=100, HTTP 200, 842,022 characters)
- Only the first 39,913 characters were read verbatim. The rest is a model-extracted summary, and the last 702,109 characters were not read at all. The fetch tool offers offset 139913 to read on.
- Verbatim portion, two annotations:
  - MP:0004189 "abnormal alveolar process morphology" (allele MGI:2653208; genotype MGI:5911481; PMID:22934831, Gibson MP 2013).
  - MP:0011035 "abnormal branching involved in alveolar duct morphogenesis" (genotype MGI:2673970; PMID:16937369, Alvares K 2006).
- Model summary, unverified against the page text (MP IDs and PMIDs as the summary reports them):
  - MP:0003933 "abnormal cementum morphology" (PMID:22934831). This conflicts with MP:0004189 for the same reference in the verbatim text, so treat the summary with caution.
  - MP:0002819 "abnormal dental pulp cavity morphology", MP:0030451 "abnormal dentin mineralization", and MP:0002818 "abnormal dentin morphology" (genotype MGI:2673970; PMID:12721295, Sreenath T 2003).
- The summary's list is described as possibly incomplete.

**5. RGD gene report** (https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=2525, HTTP 200, 163,016 characters)
- RGD ID 2525; symbol Dspp; name "dentin sialophosphoprotein"; type protein-coding; RefSeq status VALIDATED.
- Location: chromosome 14, cytogenetic band p22. GRCr8: 14:5,870,232-5,876,339 (-). Rnor_6.0: 14:6,926,972-6,933,079 (-).
- Orthologs (RGD IDs): human DSPP 69028; mouse Dspp 10493; dog DSPP 12376540; chinchilla 9019199; bonobo 11940477; squirrel 12518008; pig 14209522; green monkey 18528396; naked mole-rat 18925654; black rat 626032507. Alliance IDs: RGD:2525, HGNC:3054, MGI:109172.
- Disease annotations, from the verbatim portion (the page was truncated, so the list may be incomplete):
  - DOID:9003089 Autosomal Dominant Deafness 39 with Dentinogenesis Imperfecta 1 (ISO, via human DSPP; OMIM).
  - DOID:4154 dentinogenesis imperfecta (ISO; ISS via MouseDO, with OMIM:125490 | OMIM:125500; OMIM).
  - DOID:9004572 Dentinogenesis Imperfecta, Shields Type 3 (ISO; OMIM; CTD).
  - DOID:701 dentin dysplasia (ISO); DOID:0070707 dentin dysplasia type II (ISO; OMIM).
  - DOID:3388 periodontal disease (ISS, MouseDO).
  - DOID:11476 osteoporosis (IEP, PMID:23974864).
  - DOID:9007364 Mouth Neoplasms (CTD); DOID:1749 squamous cell carcinoma (ISO, CTD, PMID:21103065).
- The gene description marks Dspp as a "biomarker of osteoporosis" and notes that human orthologs are implicated in dentinogenesis imperfecta.

## Animal natural disease (items 6-7)

**6. MONDO:7770372** (https://www.ebi.ac.uk/ols4/api/terms?obo_id=MONDO:7770372&ontology=mondo, HTTP 200)
- Label: "dentinogenesis imperfecta, dog". Definition: "Dentinogenesis imperfecta that occurs in dog."
- Synonyms: none.
- Cross-references: OMIA:002792-9615 (https://omia.org/phene/omia:002792-9615). Cross-species exact match: MONDO:0018849 (human dentinogenesis imperfecta).
- Not obsolete; no children.

**7. MONDO search, "dentinogenesis imperfecta"** (https://www.ebi.ac.uk/ols4/api/search?q=dentinogenesis+imperfecta&ontology=mondo&rows=20, HTTP 200, numFound 12, all returned)
- MONDO:0018849 dentinogenesis imperfecta (non-syndromic; exact synonyms include DGI, DI, "non-syndromic dentinogenesis imperfecta").
- HP:0000703 "Dentinogenesis imperfecta" (returned under the MONDO index).
- MONDO:0007442 dentinogenesis imperfecta type 3 (Shields type III, DGI-III, Brandywine type).
- MONDO:0007441 dentinogenesis imperfecta type 2 (Shields type II, DGI-2; related synonyms "dentinogenesis imperfecta 1", DGI1).
- MONDO:0011571 deafness, autosomal dominant 39, with dentinogenesis imperfecta 1.
- MONDO:0011501 wormian bone-multiple fractures-dentinogenesis imperfecta-skeletal dysplasia (Suarez-Stickler syndrome).
- MONDO:0019102 dentinogenesis imperfecta-short stature-hearing loss-intellectual disability syndrome.
- MONDO:7770372 dentinogenesis imperfecta, dog (the only animal-specific match).
- MONDO:0100325 odontochondrodysplasia 1 (Goldblatt syndrome).
- MONDO:0008148 osteogenesis imperfecta type 4; MONDO:0009804 osteogenesis imperfecta type 3; MONDO:0012591 osteogenesis imperfecta type 5 (no dentinogenesis imperfecta in type 5).

## HPO, GO and NCIT searches (items 8-19)

All searches returned HTTP 200. Definitions are paraphrased.

**8. "shell teeth", HP** (numFound 2): HP:0000694 **Odontodysplasia**. Exact synonyms: Ghost teeth; Shell teeth; Teeth with dentinal dysplasia; Teeth with thin dentin and large pulp chambers; Teeth with type iii dentinogenesis imperfecta. Definition: enlarged pulp chambers with thin enamel and dentin, in dentinogenesis imperfecta. The second hit is UBERON:0004755 skeletal tissue, not an HP term.

**9. "periapical", HP** (numFound 2):
- HP:0000700 **Periapical bone loss**. Related synonyms: Periapical radiolucencies; Periapical radiolucency; Bone loss around tooth root; Periapical cyst; Periapical granuloma. Exact: Dark spot around tooth root on x-ray; Periapical lesion.
- HP:0030758 **Periapical tooth abscess**. No synonyms.

**10. "attrition teeth", HP** (numFound 1): HP:4000181 **Excessive dental attrition**. Exact synonyms: Excessive tooth attrition; Excessive wear and tear on teeth.

**11. "opalescent teeth", HP** (numFound 1): HP:0030756 **Erythrodontia**. Definition: reddish-brown opalescent discoloration in normal light, characteristic of congenital erythropoietic porphyria. Exact synonym: Red teeth. No opalescent-dentinogenesis-imperfecta term was returned.

**12. "short dental root", HP** (numFound 3, rows 5):
- HP:0006336 **Short dental root**. Definition: root length more than 2 SD below the mean. Exact synonyms include Dental root hypoplasia; Dental root hypotrophy; Rhizomicry; Root dwarfism; Short tooth roots; Underdeveloped dental roots. Broad: Underdeveloped tooth roots.
- HP:0000679 **Taurodontia** (exact: Taurodontism, Taurodont; related: Large elongated pulp chamber).
- HP:0033784 **Dentin dysplasia**.

**13. "enamel hypoplasia", HP** (numFound 4):
- HP:0006297 **Enamel hypoplasia**. Exact synonyms include Dental enamel hypoplasia; Enamel hypotrophy; Hypoplasia of tooth enamel; Underdeveloped teeth enamel. Related: Enamel dysplasia; Dysplasia of tooth enamel. Broad: Thin tooth enamel; Defective enamel matrix.
- HP:0006282 Generalized hypoplasia of dental enamel.
- HP:0011074 Localized hypoplasia of dental enamel.
- HP:0033786 **Hypomature enamel** (exact: Enamel opacity).

**14. "premature loss of teeth", HP** (numFound 4):
- HP:0006323 **Premature loss of primary teeth**. Exact synonyms include Premature loss of deciduous teeth; Early loss of primary teeth; Premature loss of baby teeth.
- HP:0006480 **Spontaneous tooth loss**. Exact synonyms: Premature loss of teeth; Early tooth loss; Premature tooth loss.
- HP:0006357 **Premature loss of permanent teeth** (exact: Early loss of permanent teeth; Premature loss of adult teeth).
- HP:4000093 Ectopic tooth eruption.

**15. "dentin mineralization", GO** (numFound 8):
- GO:0097188 **dentin mineralization** (exact: dentine mineralization). Definition: deposition of calcium salts into dentin.
- GO:0097187 dentinogenesis (exact: dentin development; dentine development).
- GO:0034505 tooth mineralization (exact: tooth calcification).
- GO:0046848 hydroxyapatite binding.
- UBERON:0001751 dentine; UBERON:0001752 enamel; UBERON:0004755 skeletal tissue.
- CL:0007001 skeletogenic cell.

**16. "odontogenesis", GO** (numFound 8):
- GO:0042476 **odontogenesis** (exact: odontogeny; odontosis; tooth morphogenesis; related: tooth development).
- GO:0042475 odontogenesis of dentin-containing tooth.
- Regulation terms: GO:0042481 regulation of odontogenesis; GO:0042482 positive regulation of odontogenesis; GO:0042483 negative regulation of odontogenesis; GO:0042487, GO:0042488 and GO:0042489 (the dentin-containing-tooth variants of the same three).

**17. "biomineral tissue development", GO** (numFound 4, rows 5):
- GO:0031214 **biomineral tissue development**. Definition: formation of hard tissues made mainly of inorganic compounds, with small amounts of organic matrix. No synonyms.
- GO:0070167 regulation of biomineral tissue development; GO:0070169 positive regulation of biomineral tissue development; GO:0070168 negative regulation of biomineral tissue development.

**18. "dental restoration", NCIT** (numFound 18, 10 returned):
- NCIT:C60718 **Dental Restoration**. Definition: replacement or reconstruction of lost tooth structure.
- NCIT:C60719 Permanent Dental Restoration (exact: Final Dental Restoration; Permanent Dental Restoration).
- NCIT:C60720 Temporary Dental Restoration (exact: Temporization).
- NCIT:C62565 Restorative Material (exact: Dental Restorative Material).
- NCIT:C52577 Microetching; NCIT:C52583 Amalgam; NCIT:C52585 Resin Modified Glass Ionomer Liner; NCIT:C52586 Resin-Based Composite.
- NCIT:C66855 **Full Crown**; NCIT:C66859 Partial Crown.

**19. "dental crown procedure", NCIT**: HTTP 200, numFound 0. No NCIT matches. "Full Crown" (NCIT:C66855) from item 18 may be the closest term.

## Final URLs read
- https://www.informatics.jax.org/marker/MGI:109172
- https://www.alliancegenome.org/api/gene/MGI:109172
- https://www.alliancegenome.org/api/gene/MGI:109172/phenotypes?limit=100 (partial)
- https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=2525 (partial)
- https://www.ebi.ac.uk/ols4/api/terms?obo_id=MONDO:7770372&ontology=mondo
- https://www.ebi.ac.uk/ols4/api/search?q=dentinogenesis+imperfecta&ontology=mondo&rows=20
- https://www.ebi.ac.uk/ols4/api/search?q=shell+teeth&ontology=hp
- https://www.ebi.ac.uk/ols4/api/search?q=periapical&ontology=hp&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=attrition+teeth&ontology=hp&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=opalescent+teeth&ontology=hp&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=short+dental+root&ontology=hp&rows=5
- https://www.ebi.ac.uk/ols4/api/search?q=enamel+hypoplasia&ontology=hp&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=premature+loss+of+teeth&ontology=hp&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=dentin+mineralization&ontology=go&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=odontogenesis&ontology=go&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=biomineral+tissue+development&ontology=go&rows=5
- https://www.ebi.ac.uk/ols4/api/search?q=dental+restoration&ontology=ncit&rows=10
- https://www.ebi.ac.uk/ols4/api/search?q=dental+crown+procedure&ontology=ncit&rows=10

Failed: https://www.alliancegenome.org/api/gene/MGI:109172/disease?limit=50 returned HTTP 404 (permanent; not retried).

## 1. Barron et al. 2008, Europe PMC full text (Orphanet J Rare Dis)

URL read: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2600777/fullTextXML (HTTP 200, XML)

Coverage: The fetch returned verbatim text for about the first third of the article, up to the start of the Diagnosis section. Everything after that is a model-extracted summary, marked [summary] below and not checked against the source. The summary says the article lacks definitions, epidemiology, and hearing-loss content. That is wrong for the verbatim part, which contains them.

**Bibliographic:** Barron MJ, McDonnell ST, MacKie I, Dixon MJ. "Hereditary dentine disorders: dentinogenesis imperfecta and dentine dysplasia." Orphanet J Rare Dis 2008;3:31. PMID 19021896; PMC2600777; DOI 10.1186/1750-1172-3-31. Review article, CC BY 2.0, epub 20 Nov 2008.

**Names and synonyms:** DGI synonyms listed include "Hereditary opalescent dentine", "Capdepont teeth", and "Brandywine Type DGI". DD synonyms include "Rootless teeth" and "Radicular dentine dysplasia".

**Definition:** Autosomal dominant conditions with "abnormal dentine structure affecting either the primary or both the primary and secondary dentitions." Teeth appear amber, brown/blue, or opalescent brown.

**Epidemiology:** Non-syndromic DGI incidence is reported as 1 in 6,000 to 1 in 8,000. DD type I is 1 in 100,000. Citations are refs 1 (Kim and Simmer 2007) and 3. Ref 3 is not identified in the read text.

**Clinical descriptions (Shields 1973 scheme, ref 4; the authors call it "increasingly out of date"):**
- **DGI-I:** Occurs with osteogenesis imperfecta (OI). Teeth in both dentitions are "typically amber and translucent and show significant attrition." Roots are short and constricted, with dentine hypertrophy and pulp obliteration before or just after eruption. Expressivity varies.
- **DGI-II:** "penetrance is virtually complete and osteogenesis imperfecta is not a feature." "Bulbous crowns are a typical feature with marked cervical constriction." "Normal teeth are never found in DGI-II."
- **DGI-III:** Brandywine isolate (tri-racial population, Maryland and Washington DC). Primary teeth show multiple pulp exposures. Radiographically, "shell" teeth, described as hollow from dentine hypotrophy.
- **DD-I:** Teeth are "generally unremarkable clinically." Roots are sharp with conical apical constrictions. Pre-eruptive pulp obliteration leaves a crescent-shaped remnant in permanent teeth and total obliteration in deciduous teeth. Numerous periapical radiolucencies occur in non-carious teeth.
- **DD-II:** Deciduous teeth resemble DGI-II. Permanent teeth are "either unaffected" or show "thistle-tube deformity of the pulp chamber and frequent pulp stones."
- The authors note the categories overlap, and suggest DD-II, DGI-II, and DGI-III may be allelic.
- Enamel loss: the enamel may "shear off," leaving exposed dentine that is sclerotic and glassy. Patients "rarely complain of sensitivity." Attrition and abscesses are noted in the clinical examination section.
- MIM numbers: DGI-I (formerly DGI-II in the MIM renaming) 125490; DGI-III 125500; DD-I 125400; DD-II 125420; OI 166240. The text notes this renaming conflicts with Shields' numbering.

**Radiographic features (verbatim):** "Crowns may appear bulbous with marked cervical constriction." Pulp chambers may be "partially or totally obliterated." "Roots are often short but may be of normal length or absent." Periapical radiolucencies can occur in non-carious teeth.

**Dentine histopathology and ultrastructure:** Not in the read portion, so unknown. The read text gives only normal dentinogenesis background: dentine is about 70% hydroxyapatite, 20% organic, and 10% water. Mantle dentine is 15–20 µm and has thick type III collagen fibrils at right angles to the DEJ.

**Genetics:**
- DSPP is "located within human chromosome 4q22.1 and consists of 5 exons spanning approximately 8343 bp." Expression in dentine is "hundreds of times higher" than in other tissues.
- Products: DSP is residues 16–374, DGP 375–462, and DPP the remainder.
- Table 1 examples (p. notation, cDNA, phenotype):
  - p.Y6D (c.16T>G): DD-II
  - p.A15V (c.44C>T): DGI-II
  - p.P17T (c.49C>A): DGI-II
  - p.P17S (c.49C>T): DGI-II
  - p.V18F (c.52G>T): DGI-II/III
  - p.Q45X (c.133C>T): DGI-II
  - DPP frameshifts: p.S624TfsX687 and p.S640TfsX671 (DD-II); p.S758AfsX554 and p.S842TfsX471 (DGI-II/III); p.S865fsX1313 and p.S895fsX1313 (DGI-II); p.D1146fsX1313 and p.D1182fsX1312 (DGI-II)
- The authors describe a genotype-phenotype trend, based on few samples: the most 5' DPP frameshifts underlie DD-II and the more 3' ones DGI-II/III.
- Proposed mechanism: intracellular retention and possibly a dominant-negative effect. The text says heterozygous null mice have a normal dentition, while homozygous nulls resemble DGI-II.
- Polymorphisms: g.1480A>T has control allele frequencies of 15% (Finnish), 6% (Caucasian), and 16% (African-American).
- No bone defects are seen with DSPP mutations, despite expression in bone.
- DD-I: the abstract says all forms "except DD-1" appear to result from DSPP mutations. The DD-I gene is not named in the read text.
- COL1A1/COL1A2 in DGI-I: "mutations in the genes encoding collagen type 1, COL1A1 and COL1A2, underlie this condition." OI is usually from missense mutations in either gene, and DGI is "occasionally the most penetrant feature."
- [summary] A specific COL1A1 variant linked to mild OI and DGI (ref 16). Not verified.

**Hearing loss (verbatim):** DGI-II sensorineural hearing loss is a "rare feature." Sensorineural loss is "associated with the g.49 C>A and g.1197 G>T mutations (MIM 605594)." The authors call this "difficult to explain," since the expected type would be conductive. They cite Kim and Simmer's suggestion that it may be secondary to attrition, and say "the cause of the hearing loss remains unresolved."

**Differential diagnosis (verbatim, abstract):** Hypocalcified amelogenesis imperfecta; congenital erythropoietic porphyria; early tooth loss conditions (Kostmann's disease, cyclic neutropenia, Chediak-Hegashi syndrome, histiocytosis X, Papillon-Lefevre syndrome); tetracycline discolouration; vitamin D-dependent and vitamin D-resistant rickets.
- [summary] The detailed differential list, including regional odontodysplasia and radiation or chemotherapy effects, is not verified.

**Management and prognosis (verbatim, abstract):** Treatment "involves removal of sources of infection or pain," improves aesthetics, and protects posterior teeth from wear. It "usually continues into adulthood" and includes "crowns, over-dentures and dental implants." Where diagnosis is early and treatment follows the recommendations, "good aesthetics and function can be obtained."
- [summary] Detailed recommendations (stainless steel crowns, composite strip crowns, overdentures, cast onlays, minimal preparation, endodontic difficulty, dentures until about age 18, implants after growth, fluoride and prevention) are not verified.
- [summary] Counselling content (for example, a 50% recurrence chance per affected parent) is not in the read text and is not verified.
- Antenatal counselling: not seen in the read portion.

## 2. JOCPD PDF, "Dentinogenesis Imperfecta Type II in Children: A Scoping Review"

URL read: https://oss.jocpd.com/files/article/20220701-226/pdf/JOCPD43.3.1.pdf (HTTP 200, application/pdf)

Failed to extract content. The file is compressed PDF binary (Flate streams and embedded fonts), not readable text. The summary of the rest of the file also could not extract any article text. The file was about 474,542 characters, and the summary says the last 334,625 characters were not read.

The only readable items were PubMed link annotations in the binary: authors "Beltrame AP, Rosa MM, Noschang RA, Almeida IC" (linked to PMID 28288297) and "Smith GD" (linked to PMID 11451790). These may be cited works rather than this article, so I have not treated them as this article's identifiers.

Not obtained: authors, year, volume and pages, PMID or DOI, number of included studies, treatment modalities and outcomes, and age or dentition-stage recommendations.

The harness saved a local copy of the PDF. Text extraction on that copy would be needed to get the content. Sending this URL again would fail the same way. The DOI or PubMed link would help me look for a text version.

## 3. Europe PMC search, DGI management and treatment, 2022–2026

URL read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22dentinogenesis%20imperfecta%22%20AND%20(treatment%20OR%20management)%20AND%20PUB_YEAR%3A%5B2022%20TO%202026%5D&resultType=core&format=json&pageSize=15 (HTTP 200, JSON)

**hitCount: 721.** The summary of the page said no hitCount appeared. The JSON does contain "hitCount":721, so the summary is wrong on this point. A next page exists (nextCursorMark is present) and was not fetched.

Verbatim records (within the read portion):

1. **PMID 42771210**, PMC13597538, DOI 10.1007/s00784-026-07142-w. "The German S3-level guideline for the diagnosis and management of rare dental disorders." Dujic H, Bücher K, Schüler IM, ... Kühnisch J. Clin Oral Investig 2026 Sep;30(10):459. Open access, CC BY. Abstract: "A total of 41 evidence- and consensus-based recommendations" were developed. Coverage includes "restorative and prosthetic treatment, and orthodontic and surgical interventions." DGI is one of six disorders covered.

2. **PMID 42814194**, DOI 10.1007/s00784-026-07194-y. "Evaluating dental developmental abnormalities in osteogenesis imperfecta: associations with timing and cumulative exposure to intravenous pamidronate- a pilot study." Demir K, Kardelen AD, ... Toksoy G. Clin Oral Investig 2026 Sep;30(10):489. Not open access. Pilot study of 58 OI individuals (38 treated with pamidronate, 20 untreated). It examines dental abnormalities including dentinogenesis imperfecta and pulpal obliteration. It is not a DGI treatment study.

3. **PMID 42639249**, PMC13501098, DOI 10.1002/ccr3.73383. "Multidisciplinary Oral Rehabilitation in Osteogenesis Imperfecta: 18-Year-Old Case Report." Mozafari PM, Noghani MT, Kashani I, Beyragh R. Clin Case Rep 2026;14(9):e73383. Open access, CC BY. Case of an OI patient under general anaesthesia. Management included vital pulp therapy, stainless steel crowns, composite with universal adhesive containing 10-MDP, and a non-extraction strategy. This is OI, not DGI-specific.

4. **PMID 42409477**, DOI 10.1016/j.adaj.2026.03.031. "Inherited dentin defects with comorbidities." Chu KY, Prakash R, Wang SK, Simmer JP, Wright JT, Hu JC. J Am Dent Assoc 2026 Jul;157(7):773-786.e1. Review, not open access. Abstract: "Timely recognition and multidisciplinary management are crucial." The read text does not describe the specific management strategies.

5. **PMID 42029463**, PMC13108200, DOI 10.3390/reports9020115. "Dentinogenesis Imperfecta in Primary Dentition: Case Report." Petrova L, Ustiča J, Čēma I. Reports (MDPI) 2026;9(2):115. Open access, CC BY. Single 1.5-year-old case followed 2020–2025. Management: composite veneers on maxillary incisors and sealants on second primary molars. Asymptomatic periapical pathology and root resorption were found. The conclusions stress early diagnosis, regular radiographic monitoring, and risk-based planning.

6. **PMID 42390399**, DOI 10.1016/j.adaj.2026.04.013. "Dental manifestations of rare skeletal disorders: Diagnosis and treatment for the oral health care provider." Lee K, Kramer K, Foster BL, Meyer BD. J Am Dent Assoc. The record is truncated in the read portion before its volume and abstract.
   - [summary] The summary gives 157(8):904-916 and an erratum DOI. These are not verified.

Other verbatim records (PMC13728728, a PLS3 osteoporosis abstract) are not relevant to DGI treatment.

Summary-only records (beyond the read portion, not verified): World J Pediatr PMID 42814222 (DOI 10.1007/s12519-026-01086-7); Diagnostics PMID 42449779 (DOI 10.3390/diagnostics16131997; DI in 68.1% of 47 patients); Cureus PMIDs 42403844 (orthopaedic) and 42220822 (OI type 4 case). The summary says none of these gives DGI-specific treatment.

MDPI returned HTTP 403, so I'm trying the two fallback URLs you named.

Europe PMC returned the bibliographic record and abstract. The PMC search page returned 404, so I'm fetching the full text at the PMCID that Europe PMC gave.

**Bibliographic details** (from the verbatim part of the page)

- **Title:** The German S3-level guideline for the diagnosis and management of rare dental disorders
- **Authors:** Helena Dujic, Katharina Bücher, Ina Manuela Schüler, Peter Schmidt, Susann Hertel, Julia Timpel, Anahita Jablonski-Momeni, Reinhard Schilke, Ines Kapferer-Seebacher, Johannes Zschocke, Anja Liebermann, Jan Frederik Güth, Daniel Edelhoff, Roswitha Heinrich-Weltzien, Jan Kühnisch (corresponding)
- **Journal:** Clinical Oral Investigations (Clin Oral Investig), 30(10):459
- **Year:** 2026 (published 2026 Sep 22)
- **PMID:** 42771210
- **DOI:** 10.1007/s00784-026-07142-w
- **PMCID:** PMC13597538

The primary URL returned HTTP 200, so the Europe PMC fallback was not needed. The page is a Springer open-access article (CC BY 4.0).

**Source caveat:** The verbatim text covers only the first ~40k of ~77k characters. The rest was summarised by a model, so statements in the DI genetics and management sections below that are not in the tables are from that summary and could not be checked against the page text.

---

### Guideline scope and overall statements (verbatim)

- Overall: "A total of 41 evidence- and consensus-based recommendations" (33 evidence-based, 80.5%; 8 consensus-based, 19.5%).
- Evidence: "Given the predominance of case reports and case series in this field, evidence was generally rated as low quality."
- Recommendation 1 (all rare disorders): "Expert consensus", strength "Strong". Diagnosis and lifelong care "should be carried out with interdisciplinary and, if necessary, interprofessional involvement and should be started at an early stage."
- Recommendation 3 (all rare disorders): "lifelong, risk-oriented and intensive preventive care", "Expert consensus", strength "Strong".

### Diagnostic recommendations

- **Dedicated DI diagnostic recommendations:** None. Table 3 (DI) contains only management recommendations (Nos. 5–12).
- **General (all rare disorders), Recommendation 2:** "If clinical and radiological findings suggest a genetic cause for a rare dental disorders, genetic diagnostics should be performed, usually in combination with a clinical consultation at a genetic practice or outpatient clinic." Expert consensus; strength "Moderate".
- **Clinical diagnosis (verbatim):** Diagnosis is "usually based on visual assessment by an experienced dentist." For DI, "all teeth in the primary and permanent dentition may appear nearly identical."
- **Radiographs (verbatim):** "radiographs taken according to indications provide additional diagnostic information."
- **Genetic role (verbatim):** "only genetic analyses can provide precise information about the aetiology and prognosis of the disease, potential complications, and possible involvement of other organ systems."
- **Clinical indicators for a genetic cause (verbatim, partly cut off):** an unusual or generalised symptom pattern, atypical primary tooth shape or structure, multisystem or syndromic pattern, and similar findings in several family members. Family history should be taken across several generations. Referral to a medical genetics clinic is "prudent" for clarification.
- **Referral and OI exclusion:** The verbatim text does not reach a DI-specific referral or osteogenesis imperfecta exclusion statement. None appears in the tables.

### Genetic testing

- **Gene panels, specific genes (e.g., DSPP), and counselling for DI:** Not in the verbatim text. The summary says no gene panels or specific genes are named.
- **Summary-only statements:** Suspected monogenic disorders are usually investigated by massively parallel sequencing. A variant of uncertain significance is not diagnostic. A normal result does not exclude a genetic cause. "If a genetically determined dental disease is confirmed, genetic counselling is indicated."

### Management by dentition stage (DI, Table 3, verbatim)

**Primary and mixed dentition**
- **Rec 5** (evidence "Very low"; strength "Strong"): "Direct restorations and prefabricated stainless steel crowns should be used in the primary and mixed dentition to avoid DI-associated loss of dental hard tissues, to compensate for it, and/or to restore the occlusal vertical dimension."
- **Rec 6** (Very low; "Strong"): For reduced occlusal vertical dimension, rehabilitate "with prefabricated stainless steel crowns on the primary molars and with either prefabricated stainless steel crowns or individually fabricated indirect single-tooth restorations on first permanent molars."
- **Rec 7** (Very low; "Moderate"): After primary tooth extraction, "space-maintaining and/or interim prosthetic measures should be undertaken" to restore function and prevent mesialisation.

**Early permanent dentition**
- **Rec 8** (Very low; "Strong"): Direct restorations and individually fabricated indirect single-tooth crowns, which "form part of a long-term care strategy."
- **Rec 9** (Very low; "Strong"): "The definitive treatment should be implemented starting with the early permanent dentition using the full-mouth rehabilitation approach."

**Adult permanent dentition**
- **Rec 10** (Very low; "Strong"): Indirect single-tooth crowns on posterior teeth to prevent progressive loss, stabilise or restore vertical dimension, and "ensure the longevity of anterior restorations."
- **Rec 11** (Very low; "Strong"): Direct restorations and indirect single-tooth crowns on anterior teeth.
- **Rec 12** (Very low; "Strong"): "Fixed, implant-supported or removable prosthetic restorations" to compensate for or prevent tooth loss and restore occlusion and masticatory function.

**Summary-only DI details:** Definitive restoration of the whole permanent dentition is usually undertaken late in the second or early in the third decade. Indirect restorations "require strategic planning." Priority is stable posterior function and vertical dimension, then anterior restorations. Indirect restorations on first permanent molars begin in adolescence.

**Not covered for DI in the text I could read:** Fluoride regimens, direct composite technique details, endodontics, extraction criteria beyond Rec 7, orthodontics, and overdentures as a named option. Rec 12's "removable prosthetic restorations" is the nearest match to overdentures. The summary says the preventive measures (sugar counselling, oral hygiene, professional cleaning, fluoride) are listed for rare disorders in general, not for DI specifically.

### Strength and consensus levels

- **DI recommendations (Table 3):** All 8 are rated evidence "Very low" (⊕⊝⊝⊝). Strengths: Recs 5, 6, 8, 9, 10, 11 and 12 are "Strong"; Rec 7 is "Moderate." None is a consensus-only recommendation in Table 3.
- **Symbols:** The tables render strength as arrows (⇑⇑ = Strong, ⇑ = Moderate, ⇔ = Open). The page's own legend was not in the text I read.
- **Summary claim to disregard:** The summary says no recommendation grades are given. The tables in the verbatim text do give them, so that claim is wrong.

### Prognosis, follow-up, psychosocial support, quality of life

- **Prognosis:** Verbatim, only that genetic analysis informs "prognosis" in general. No DI prognosis is given.
- **Follow-up intervals:** None for DI in the text I read. (Amelogenesis imperfecta has a six-monthly examination interval only in the XLH recommendation, No. 22, which is not DI.)
- **Psychosocial support / QoL:** Verbatim, rare dental disorders "are frequently associated with severe functional impairments" and "a reduced oral health–related quality of life." The clinical relevance statement says the guideline "is expected to improve oral health outcomes and quality of life in this vulnerable patient group." No DI-specific data or psychosocial recommendations appear.
- **Evidence base for DI (summary):** Only case reports and case series. No clinical studies.

### DI vs amelogenesis imperfecta (AI) management

- **Parallel recommendations (verbatim):** AI Recs 13–21 (Table 4) cover direct restorations, prefabricated stainless steel crowns, indirect restorations, and full-mouth rehabilitation starting in the early permanent dentition (Rec 20: "Definitive treatment should begin in the early permanent dentition using the concept of full-mouth rehabilitation.").
- **Differences in the tables:**
  - AI direct restorations (Rec 13) are aimed at "pain relief, restore function, and improve aesthetics." DI Rec 5 has no pain goal.
  - AI Rec 16 recommends indirect restorations on permanent anterior teeth already in the mixed dentition. DI Rec 11 places anterior indirect/direct restorations in the adult dentition.
  - AI Rec 21 (Moderate evidence, "Strong") is "Definitive, individually fabricated indirect single-tooth crowns should be placed in the permanent dentition." DI's evidence is "Very low" throughout.
  - AI evidence ranges Low to Moderate; DI is Very low throughout.
- **Summary-only AI statements:** Indirect restorations are the "treatment of choice" for permanent AI dentition. The page reports improvements in oral health-related and social quality of life for AI.

---

**URL read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13597538/

The PMC full text was cut at 39,942 of 180,007 characters, and the rest is a model summary. I'll read the final part directly to check the summary's claims on the mechanism, haploinsufficiency, and the recommendations.

## Bibliographic record

- **Title:** The Modified Shields Classification and 12 Families with Defined DSPP Mutations
- **Authors:** James P Simmer, Hong Zhang, Sophie J H Moon, Lori A-J Donnelly, Yuan-Ling Lee, Figen Seymen, Mine Koruyucu, Hui-Chen Chan, Kevin Y Lee, Suwei Wu, Chia-Lan Hsiang, Anthony T P Tsai, Rebecca L Slayton, Melissa Morrow, Shih-Kai Wang, Edward D Shields, Jan C-C Hu
- **Journal:** Genes (Basel), volume 13, issue 5, article 858
- **Year:** 2022 (epub 12 May 2022)
- **PMID:** 35627243
- **PMCID:** PMC9141616
- **DOI:** 10.3390/genes13050858

## Access log

- MDPI (https://www.mdpi.com/2073-4425/13/5/858): HTTP 403. Permanent, so I did not retry.
- PMC search (https://pmc.ncbi.nlm.nih.gov/articles/?term=Modified+Shields+Classification+DSPP): HTTP 404.
- Europe PMC REST search: HTTP 200. It gave the metadata and the full abstract, which I quote below.
- PMC full text (https://pmc.ncbi.nlm.nih.gov/articles/PMC9141616/): HTTP 200. The page is 180,007 characters. I read the first 39,942 characters verbatim and the last 40,065 verbatim (references and back matter only). The middle roughly 100,000 characters (the Results and Discussion) were not read. Everything below that depends on that middle section comes from a model-generated summary and is marked "(summary)". Those statements are paraphrased, not verified quotes.

## 1. Proposed modified classification rule

- Abstract (verbatim): the authors propose that "patients identified with 5′-DSPP defects be diagnosed as DGI-III, while those with 3′-DSPP defects be diagnosed as DGI-II."
- Abstract, reasoning (verbatim): the rule is "based upon the causative mutation rather than phenotypic severity." It follows from "distinct differences in the cell pathology observed between knockin mice with 5′-Dspp or 3′-Dspp mutations."
- (summary) The authors describe an exception: dominant 5′ mutations are classed as DGI-III "except those in the signal peptide coding segment." They also say the 5′ knockin caused ER retention of DSPP, while the 3′ frameshift knockin caused cell toxicity with autophagy and little ER stress or enamel attrition.

## 2. The 12 families and their DSPP mutations (HGVS, NM_014208.3)

Table 1 (5′ group) and Table 2 (3′ group), verbatim:

- Family 1: c.50C>T, p.(Pro17Leu), Table 1 #5 (5′)
- Family 2: c.52-1G>A, Table 1 #11, intron 2 splice acceptor (5′)
- Family 3: c.53T>C, p.(Val18Ala), Table 1 #15 (5′, novel)
- Family 4: c.135+3A>G, Table 1 #21, intron 3 (5′)
- Family 5: c.1915_1918delAAGT, p.(Lys639Glnfs*674), Table 2 #5 (3′)
- Family 6: c.1918_1921delTCAG, p.(Ser640Thrfs*673), Table 2 #6 (3′)
- Family 7: c.2134delA, p.(Ser712Alafs*602), Table 2 #10 (3′)
- Families 8 and 9: c.2525delG, p.(Ser842Thrfs*472), Table 2 #13 ("Fam 8&9") (3′)
- Family 10: c.3135delC, p.(Ser1045Argfs*269), Table 2 #18 (3′)
- Family 11: c.3461delG, p.(Ser1154Metfs*160), Table 2 #21 (3′, novel)
- Family 12: c.3700delA, p.(Ser1234Alafs*80), Table 2 #30 (3′, novel)

The text does not give exon or zygosity for every family. Zygosity statements such as "heterozygous" for Family 2 come from the summary. Table 2 also says that mutations with a mild permanent-dentition (DD-II) phenotype are highlighted in cyan and DGI-II in green. The colours are not visible in the extracted text.

Other points from the verbatim text:
- The Brandywine isolate variant is c.49C>T (p.Pro17Ser), Table 1 #4. The Discussion says the earlier attribution to C-terminal indels was wrong.
- The Results say "eleven families" while the study describes twelve.

## 3. Phenotype descriptions (5′ vs 3′)

Verbatim:
- "Mutations in the 5′-DSPP (N-terminal) group often cause DGI with enamel defects."
- Shields DGI-III: "a distinct type of dentinogenesis imperfecta, perhaps genetically allelic to type II."
- DD-II (intro): the primary dentition shows hereditary opalescent dentin, while the "permanent dentition shows only a minor phenotype."
- Radiographic DD-II features are a "thistle-tube" pulp deformity and pulp stones, which are transient.

(summary) The 5′ group (DGI-III) has true enamel malformations, accelerated attrition, bulbous crowns, short tapered roots, and pulp obliteration. Family 4 has very thin enamel. The 3′ group has enamel of normal thickness in Families 8 and 9, and the authors expect DGI-II to show minimal enamel malformation and less risk of rapid attrition. Family 5 had mainly radiographic findings and mildly bulbous crowns.

## 4. Whether DD-II is part of the same spectrum

- Verbatim (intro): "DD-II, DGI-II, and DGI-III are all autosomal dominant conditions caused by single allele mutations" in DSPP.
- (summary) The authors describe the three Shields types as levels of severity within one continuum of isolated autosomal dominant dental phenotypes. They say DD-II-type mutations cluster in the most 5′ region. They also reject the earlier suggestion that the Shields classification be abandoned. The proposed rule gives DD-II no separate category. Family 10 is described as borderline between DD-II and DGI-II.

## 5. Two mechanistic classes

- 5′ group (verbatim, intro): mutations "adjacent to the signal peptide cleavage site that likely interferes with signal peptide cleavage" and/or cause mutant DSPP "to be retained in the rough endoplasmic reticulum (rER)."
- 3′ group (verbatim, intro): "−1 frameshift mutations in the last coding exon (#5)" that "translate beyond the native DSPP translation termination codon."
- (summary) The frameshift position in exon 5 "correlates only roughly" with DD-II or DGI-II (this exact phrase is verbatim in the intro). A signal-peptide variant, c.16T>G p.Tyr6Asp, is one of two mutations the authors say do not fit cleanly into either group.
- The IPV motif is not mentioned in any part I read verbatim (the first 40k and last 40k characters). I cannot say whether it appears in the unread middle section.

## 6. Why DSPP loss of function does not cause disease

Not in the verbatim text I read. (summary) The authors argue that the autosomal dominant conditions are caused by cell pathology rather than loss of function. They cite the lack of a dental phenotype in heterozygous Dspp knockout mice and the absence of haploinsufficiency-type variants such as premature termination codons. I have not verified these statements.

## 7. Sequencing and diagnostic recommendations (DPP repeat region)

- Abstract (verbatim): "We propose genetic analysis start with WES analysis of proband DNA" to find COL1A1/COL1A2 variants, 5′-DSPP mutations, and "3′-DSPP frameshifts near the margins of the DSPP repeat region," with "SMRT sequencing when the disease-causing mutation is not identified."
- (summary) If WES is negative, SMRT sequencing should be run on amplified 3′ DSPP products. Each patient yields two haplotype sequences because of allelic length variation. Reads should be aligned to the repeat region using the 16 known indels, which are listed in Supplementary Table S1. For Family 9, the authors say Sanger sequencing failed because indel 5 sat close to the mutation and to repeat sequence.

## Other notes

- The data availability statement points to dbGaP study phs001491.v2.p1 for the WES data.
- The article is open access under CC BY 4.0.

**Scope note / interpretation:** This report covers **MONDO:0018849 — dentinogenesis imperfecta**, the *non-syndromic* (isolated, "without osteogenesis imperfecta") grouping term whose causal gene is **DSPP** (dentin sialophosphoprotein, HGNC:3054, 4q22.1). It is kept deliberately separate from dentinogenesis imperfecta occurring as an oral manifestation of osteogenesis imperfecta (COL1A1/COL1A2), which is a different entity and is discussed only where sources explicitly bear on the boundary. **OMIM could not be retrieved in this session** (omim.org returned HTTP 403 for entries 125485, 125490, 125500, 125420); OMIM-derived content below is cited to the secondary resources that actually served it (MedGen, UniProt, the HPO annotation API, OLS4), and is labelled as such.

---

# Dentinogenesis Imperfecta (MONDO:0018849, *DSPP*) — Comprehensive Disease Characteristics Report

---

## 1. Disease Information

### Overview

Dentinogenesis imperfecta (DI/DGI) is an autosomal dominant hereditary dentine disorder in which odontoblast-derived dentine is structurally and mineralogically abnormal, producing discoloured, mechanically weak teeth in both dentitions. The causal gene for the isolated/non-syndromic form is **DSPP**. The Disease Ontology definition served through GARD describes it as "a tooth disease characterized by discolored, opalescent teeth that has_material_basis_in mutation in the DSPP gene on chromosome 4q22" ([GARD 6258](https://rarediseases.info.nih.gov/diseases/6258/dentinogenesis-imperfecta)).

GARD's own summary (page last updated September 2026) states: "Dentinogenesis imperfecta is a disorder of tooth development," with teeth that are discoloured — "most often a blue-gray or yellow-brown color" — translucent, weaker than normal, and prone to "rapid wear, breakage, and loss," affecting both primary and permanent dentitions ([GARD 6258](https://rarediseases.info.nih.gov/diseases/6258/dentinogenesis-imperfecta)).

The field is in the middle of a **nomenclature transition** that matters for any knowledge-base entry:

- The **Shields (1973) classification** recognises DGI types I, II, III and dentine dysplasia (DD) types I and II. Barron et al. call this scheme "increasingly out of date as it does not account for the molecular aetiologies of these defects" (Barron MJ, McDonnell ST, MacKie I, Dixon MJ, *Orphanet J Rare Dis* 2008;3:31; **PMID 19021896**, PMC2600777, DOI 10.1186/1750-1172-3-31).
- **de La Dure-Molla et al. 2015** proposed collapsing all DSPP-related isolated disease into a single graded entity: "We propose that all DSPP diseases are called exclusively 'Dentinogenesis Imperfecta (DI)'," with Shields DD-II = mild, DGI-II = moderate, DGI-III = severe, and Shields DD-I reclassified as "radicular dentin dysplasia" (de La Dure-Molla M, Philippe Fournier B, Berdal A, *Eur J Hum Genet* 2015;23(4):445–451; **PMID 25118030**, PMC4666581, DOI 10.1038/ejhg.2014.159). Their conclusion: "isolated dentinogenesis imperfecta should actually be regarded as a single entity with an important variability of expression."
- **Simmer et al. 2022** proposed a *genotype-anchored* "modified Shields classification": classify by causative mutation rather than phenotypic severity, so that "patients identified with 5′-DSPP defects be diagnosed as DGI-III, while those with 3′-DSPP defects be diagnosed as DGI-II" (*Genes* 2022;13(5):858; **PMID 35627243**). (Retrieved from the PubMed record and indexing services; full text not retrieved in this session.)
- **Lump/split call to surface:** MONDO:0018849 is the *parent* grouping. Its children MONDO:0007441 (DGI type 2) and MONDO:0007442 (DGI type 3) correspond to Shields II and III. Given that de La Dure-Molla 2015 and Simmer 2022 both argue these are one allelic entity, a KB may reasonably annotate at MONDO:0018849 and record the Shields subtypes as severity grades rather than as separate diseases. This is a curation decision, not a settled fact — both the split (MONDO/OMIM) and lump (2015/2022 literature) views are currently in use.

### Key identifiers

| Resource | Identifier | Source retrieved |
|---|---|---|
| Mondo (this entry) | **MONDO:0018849** "dentinogenesis imperfecta" | [OLS4 MONDO search](https://www.ebi.ac.uk/ols4/api/search?q=dentinogenesis+imperfecta&ontology=mondo) |
| Mondo children | MONDO:0007441 (type 2 / Shields II); MONDO:0007442 (type 3 / Shields III) | OLS4 |
| Related Mondo | MONDO:0011571 (deafness, AD 39, with dentinogenesis imperfecta 1); MONDO:7770372 (dentinogenesis imperfecta, dog) | OLS4 |
| OMIM (gene) | 125485 *DSPP* | HGNC REST record |
| OMIM (phenotypes) | 125490 (DGI1/Shields II); 125500 (Shields III); 125420 (DD-2); 605594 (DFNA39 + DGI1) | UniProt Q9NZW4 disease annotations; HPO annotation API |
| Orphanet | **ORPHA:49042** (dentinogenesis imperfecta); ORPHA:166260 (DGI2); ORPHA:166265 (DGI3) | GARD 6258; MedGen 424922; UniProt Q9NZW4 |
| Disease Ontology | **DOID:4154** | GARD 6258; MGI disease-model annotation |
| MedGen | UID 424922, concept **C2973527** (Dentinogenesis imperfecta type 2) | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/424922) |
| UMLS / MeSH / SNOMED (grouping xrefs listed by GARD) | C0011436; D003811; 196286005; MEDGEN:8313 | GARD 6258 xref block |
| GARD | 6258 | GARD |
| HPO (as a phenotype term) | **HP:0000703** | [HPO API](https://ontology.jax.org/api/hp/terms/HP%3A0000703) |

**ICD-10/ICD-11 codes could not be verified in this session** — Orphanet (orpha.net) returned a bot-verification interstitial for ORPHA:49042 and ORPHA:166260, and GARD's page does not display ICD codes. I am not supplying ICD codes from memory.

### Synonyms (verified)

From OLS4 (Mondo exact synonyms) and GARD: *DGI; DI; dentinogenesis imperfecta (disease); dentinogenesis imperfecta without osteogenesis imperfecta; non-syndromic DGI; non-syndromic dentinogenesis imperfecta; DGI without OI; opalescent teeth without OI; opalescent teeth without osteogenesis imperfecta; hereditary opalescent dentin.*

From MedGen (DGI type 2 record): *CAPDEPONT TEETH; Dentinogenesis imperfecta – Shield's type II; DGI1; Hereditary Opalescent Dentin; OPALESCENT DENTIN.*

Barron 2008 additionally lists *Brandywine Type DGI* for Shields III, and for DD: *rootless teeth, radicular dentine dysplasia*.

### Data provenance

The information in this report is **disease-level aggregated** (ontologies, curated databases, systematic reviews, case series) rather than EHR/individual-patient-derived. The two largest *individual-level* datasets retrieved are the Swedish nationwide registry-based prevalence study (Andersson et al. 2018) and the French GenoDENT cohort of 112 individuals (Caravello et al. 2026).

---

## 2. Etiology

### Primary cause

Heterozygous pathogenic variants in **DSPP** (dentin sialophosphoprotein), 4q22.1, acting predominantly by **dominant-negative / gain-of-function** mechanisms (see §6). DSPP belongs to the **SIBLING** (Small Integrin-Binding LIgand N-linked Glycoprotein) gene cluster on 4q (HGNC gene-group assignment: "SIBLING family"); de La Dure-Molla 2015 notes this cluster is "implicated in mineralization of dental and bone tissues notably by modulation of matrix metalloproteinases activity."

Critically, **simple loss of function does not cause the dominant disease**. Liang et al. state in their introduction that "simple loss-of-function mutations do not cause dominant dentin malformations in humans," and that *Dspp* heterozygous knockout mice "show either no dentin phenotype, or mild dentin defects not evident until old age" (*Sci Rep* 2021;11:20653; **PMID 34667213**, PMC8526674). von Marschall et al. conclude that "loss of a single allele is recessive and that haploinsufficiency does not explain DD or DGI" (*J Bone Miner Res* 2012;27(6):1309–21; **PMID 22392858**, PMC3390460).

### Genetic risk factors

- **Causal variants:** see §4. Essentially 100% of the risk in isolated DI is monogenic *DSPP*.
- **Modifier genes:** none identified. Caravello et al. 2026 observed that relatives sharing the same variant differ in severity and that the data "suggest the influence of modifier factors" — the modifiers themselves are unidentified (*J Med Genet* 2026;63(6):e111345; **PMID 41819808**, PMC13217078).
- **Susceptibility loci / GWAS:** no GWAS data were retrievable for this Mendelian trait; none is expected.
- **Family history** is the dominant non-molecular risk factor (autosomal dominant, near-complete penetrance).

### Environmental risk factors

**No established environmental cause or risk factor.** This is a developmental, genetically determined matrix defect. Barron 2008 lists environmental mimics (tetracycline discolouration, rickets) under *differential diagnosis*, not aetiology. Attrition rate and secondary infection are plausibly modulated by diet, bruxism, and oral hygiene, but I retrieved no study quantifying this.

### Protective factors

No genetic protective alleles or modifier alleles were identified in any retrieved source. Environmentally, early diagnosis and protective full-coverage restoration are the only intervention shown to alter outcome — Barron 2008's abstract states that where diagnosis is early and treatment follows recommendations, "good aesthetics and function can be obtained." This is a *tertiary* protective measure, not a disease-risk modifier.

### Gene–environment interactions

**None documented.** CTD/GxE databases were not productive for this disease. The only gene–environment statement retrieved is speculative: Caravello et al. invoke unspecified "modifier factors" to explain intrafamilial variability, and de La Dure-Molla 2015 states that correlating genotype and phenotype is hard "because of environmental factors and the three protein products." Both are hypotheses, not demonstrated interactions.

---

## 3. Phenotypes

### Core dental phenotypes with suggested HPO terms

All HPO IDs below were verified against the HPO API or EBI OLS4 in this session.

| Phenotype | HPO term | Type | Onset | Severity / course | Frequency |
|---|---|---|---|---|---|
| Dentinogenesis imperfecta (the defining dentine dysplasia) | **HP:0000703** — def. "Developmental dysplasia of dentin" | Physical manifestation | Congenital/neonatal (present at tooth formation; apparent at eruption) | Variable | Obligate |
| Yellow-brown tooth discolouration | **HP:0006286** | Clinical sign | Infancy, at eruption | Stable colour; worsens with wear | Very frequent — HPO-annotated to OMIM:125490 (cited PMID:11175779) |
| Opalescent / blue-grey / amber discolouration | *No dedicated HPO term for opalescent teeth.* HP:0030756 "Erythrodontia" is specific to congenital erythropoietic porphyria and must **not** be used here | Clinical sign | Infancy | — | Characteristic |
| Bulbous crowns with cervical constriction | **HP:0033780** "Bulbous tooth" — def. "A tooth crown with a marked cervical area constriction" | Radiographic/physical | Eruption | — | Barron 2008: "Bulbous crowns are a typical feature with marked cervical constriction" (DGI-II) |
| Pulp obliteration | **HP:0006350** (syn. pulp canal obliteration; "Crescent/chevron-shaped pulp chambers") | Radiographic | Pre- or peri-eruptive | Progressive | Boonyakanog 2026 (summary-level): complete pulp obliteration in 74.47% of DGI-II records |
| Enlarged pulp / "shell teeth" | **HP:0000694** "Odontodysplasia" — exact synonyms include *Shell teeth*, *Teeth with type iii dentinogenesis imperfecta* | Radiographic | Primary dentition | Severe end of spectrum | HPO-annotated to OMIM:125500 |
| Excessive attrition / rapid wear | **HP:4000181** "Excessive dental attrition" | Physical | Early childhood | **Progressive** | Boonyakanog (summary): severe attrition 84.62% of DGI-III records |
| Enamel chipping / loss (secondary to a defective DEJ) | **HP:0006297** Enamel hypoplasia; **HP:0033786** Hypomature enamel; **HP:0006282** Generalized hypoplasia of dental enamel | Physical | At/after eruption | Progressive | Frequent |
| Periapical radiolucency / bone loss | **HP:0000700** "Periapical bone loss" | Radiographic | Childhood | Episodic | HPO-annotated to OMIM:125500 (PMID:6579461); Barron 2008: periapical radiolucencies occur in non-carious teeth |
| Periapical abscess | **HP:0030758** "Periapical tooth abscess" | Clinical sign | Childhood | Episodic | Common in DGI-III and DD |
| Short dental roots | **HP:0006336** "Short dental root" | Radiographic | — | Stable | Frequent |
| Premature tooth loss | **HP:0006323** (primary); **HP:0006357** (permanent); **HP:0006480** Spontaneous tooth loss | Clinical | Childhood onward | Progressive | Variable |
| Anterior open-bite malocclusion | **HP:0009102** | Clinical | Mixed/permanent dentition | — | HPO-annotated to OMIM:125500 (PMID:6579461) |
| Dental enamel pits | **HP:0009722** | Physical | — | — | HPO-annotated to OMIM:125500 (PMID:6579461) |
| Taurodontia | **HP:0000679** | Radiographic | — | — | Listed in DD contexts |
| Caries | **HP:0000670** "Carious teeth" | Clinical | — | — | Notably, de La Dure-Molla 2015 report that "periodontal disease is frequent without caries" |
| Dentin dysplasia (umbrella) | **HP:0033784** | — | — | — | — |
| Parent term | **HP:0010299** "Abnormal dentin morphology" | — | — | — | — |

GARD lists the following HPO features for this disease, split by frequency — **common:** abnormal dental pulp morphology; abnormal dentin morphology; abnormal dental root morphology; hypocalcification of dental enamel; joint hypermobility; fragile teeth; generalized hypoplasia of dental enamel; grayish enamel; odontodysplasia; pulp obliteration; yellow-brown discoloration of teeth. **Uncommon:** bruising susceptibility; short dental root; persistence of primary teeth; hearing impairment; hyperextensibility at elbow; finger and knee joint hypermobility; prolonged bleeding time; selective tooth agenesis; blue sclerae ([GARD 6258](https://rarediseases.info.nih.gov/diseases/6258/dentinogenesis-imperfecta)).

> **Curation caution:** several GARD "common" and "uncommon" items — joint hypermobility, blue sclerae, bruising susceptibility, prolonged bleeding time, hyperextensibility at elbow — are **osteogenesis imperfecta / connective-tissue features that have leaked into the grouping annotation**. They are not features of isolated DSPP-related DI and should not be propagated to MONDO:0018849. Barron 2008 explicitly notes that "no bone defects are seen with DSPP mutations, despite expression in bone."

### Clinical description by severity grade

**Moderate (Shields DGI-II; MONDO:0007441 — the commonest presentation).** de La Dure-Molla 2015: "The teeth exhibit a grey blue, or amber brown and opalescent discolouration and small height." Crowns show "bulbous crowns because of an important cervical constriction, short and thick roots and pulp obliteration"; the authors call pulp obliteration with bulbous crowns and short thick roots "pathognomonic" radiographically. Barron 2008: in DGI-II "penetrance is virtually complete and osteogenesis imperfecta is not a feature," and "**Normal teeth are never found in DGI-II**."

**Severe (Shields DGI-III; MONDO:0007442).** de La Dure-Molla: "Clinically, it is like DGI-II," but with pulp *enlargement* giving "shell teeth" on radiographs; historically "quite exclusively described in the triracial sub-population of Maryland, the 'Brandywine isolate'." Barron 2008 adds multiple pulp exposures in the primary teeth and describes shell teeth as hollow from dentine hypotrophy.

**Mild (Shields DD-II).** de La Dure-Molla: same expression as DGI-II but only in deciduous teeth; permanent teeth "normal in colour, shape and height," with a "thistle-tube" pulp chamber and frequent pulp stones on radiographs. Mild forms "were described solely in permanent teeth."

**Enamel involvement is secondary.** de La Dure-Molla: enamel is often dislodged because the enamel–dentine junction is altered, and the exposed hypomineralised dentine then wears quickly; attrition ranges "from a few facets to complete loss of the crown." Barron 2008 adds that the enamel may "shear off," leaving exposed dentine that is sclerotic and glassy, and — clinically important for paediatric assessment — that patients "rarely complain of sensitivity."

**Dentition asymmetry (pediatrically substantive).** de La Dure-Molla state, confirmed across all cases they reviewed: "**Primary teeth are often more severely affected than permanent teeth**." This inverts the usual expectation and means a child can present with a devastated primary dentition and a far less affected adult dentition — relevant to both prognosis counselling and the timing of definitive restorative work.

### Extra-dental phenotype: progressive sensorineural hearing loss (DFNA39)

Xiao et al. (*Nat Genet* 2001;27:201–204; **PMID 11175790**) described two families with DGI plus "bilateral progressive high-frequency sensorineural hearing loss, designated DFNA39," with onset "in the high frequency range at an age of 20 to 30 years," associated with missense changes in exons 2 and 3; a third family with a splice-donor change in intron 3 had no hearing loss.

Barron 2008 treats this as "a rare feature" of DGI-II, associated with "the g.49 C>A and g.1197 G>T mutations (MIM 605594)," and is explicitly sceptical: they call it "difficult to explain," since the expected type would be conductive, cite the suggestion that it may be secondary to attrition, and conclude that "the cause of the hearing loss remains unresolved." MedlinePlus/GARD similarly state that "A few older individuals with type II have had progressive high-frequency hearing loss" and that it is "not known whether this hearing loss is related to dentinogenesis imperfecta."

UniProt Q9NZW4 annotates DFNA39 (MIM:605594) to variants Thr-17 (P→T) and Phe-18 (V→F) in its mature-protein numbering. **This association remains contested**; it should be curated as an uncertain pleiotropic feature with explicit evidence qualification, not as a core disease phenotype.

### Quality-of-life impact

Disease-specific QoL data are **thin and largely absent for isolated DI**.

- A 2018 qualitative study stated that the psychosocial impact of DGI "have never been investigated" (retrieved as a cited statement; primary full text not fetched).
- A paediatric OI OHRQoL study found that "Limited data on the presence of dentinogenesis imperfecta did not impact overall score (P = 0.109), but was significant in the oral-health domain (P = 0.033)" ([Eur Arch Paediatr Dent, 10.1007/s40368-021-00664-9](https://link.springer.com/article/10.1007/s40368-021-00664-9)).
- A 2024 study of craniofacial/dental OI manifestations using the CPQ found "no significant difference in OHRQoL between children and adolescents, nor associated with the disease severity or the presence of DI" ([10.1007/s00784-024-05568-8](https://link.springer.com/article/10.1007/s00784-024-05568-8)).
- **The only DI-specific prospective QoL study retrieved is a trial, not yet published as results:** NCT04927962 ("AiDiBull," University Hospital Toulouse), an observational study of 87 participants aged 10–18 with non-syndromic amelogenesis or dentinogenesis imperfecta across seven French rare oral disease centres, primary outcome the **Child Oral Health Impact Profile (COHIP)**, with bullying/cyberbullying and dental anxiety instruments; start 2021-09-22, primary completion 2024-04-03, listed as completed ([ClinicalTrials.gov NCT04927962](https://clinicaltrials.gov/study/NCT04927962)).

The German S3 guideline states generally that rare dental disorders "are frequently associated with severe functional impairments" and "a reduced oral health–related quality of life," but gives **no DI-specific QoL data** (Dujic H et al., *Clin Oral Investig* 2026;30(10):459; **PMID 42771210**, PMC13597538).

---

## 4. Genetic / Molecular Information

### Causal gene

**DSPP — dentin sialophosphoprotein.** Verified identifiers from the HGNC REST record and UniProt:

- HGNC:3054; approved name "dentin sialophosphoprotein"; locus type: gene with protein product
- Entrez Gene **1834**; Ensembl **ENSG00000152591**; UniProt **Q9NZW4**; OMIM **125485**
- Cytogenetic location **4q22.1**
- RefSeq **NM_014208**; MANE Select **ENST00000651931.1 / NP_055023.2**; CCDS43248; LRG_1242
- Previous symbols: **DFNA39, DGI1**; alias **DMP3**; gene group: **SIBLING family**
- Mouse ortholog MGI:109172; rat ortholog RGD:2525

Gene structure: Barron 2008 states DSPP is "located within human chromosome 4q22.1 and consists of 5 exons spanning approximately 8343 bp," with dentine expression "hundreds of times higher" than in other tissues. de La Dure-Molla 2015: "The DSPPs are encoded by a 5-exon gene," with exons 2, 3, 4 and the start of exon 5 encoding DSP, and the end of exon 5 encoding DGP and DPP. The original DGI-II mapping was "on chromosome 4q21 by linkage analysis between markers D4S2691 and D4S2692" (de La Dure-Molla 2015) — note the 4q21 vs 4q22.1 discrepancy between the mapping history and the current HGNC assignment.

### Protein architecture (UniProt Q9NZW4, entry version 178, 04-NOV-2026)

- Length **1301 aa**, MW 131,151 Da
- **Signal peptide 1–15**
- **Chain 16–1301** dentin sialophosphoprotein; **chain 16–462 dentin sialoprotein (DSP)**; **chain 463–1301 dentin phosphoprotein (DPP / phosphophoryn)**
- Disordered regions 55–89, 146–171, **202–1301**; cell-attachment (RGD) site 488–490
- N-glycosylation at N41, N49, N81, N130, N150, N190, N191, N209, N222, N275, N336, N387; phosphoserine at S259 (by CK1) and S301; "DSP is glycosylated"
- Subcellular location: **secreted, extracellular space, extracellular matrix**
- Tissue specificity: expressed in teeth; DPP synthesised by odontoblasts and **transiently expressed by pre-ameloblasts**

> **Discrepancy to flag:** UniProt does not annotate a separate **DGP** (dentin glycoprotein) chain and assigns DSP residues 16–462. Barron 2008 instead gives DSP = residues 16–374, DGP = 375–462, DPP = remainder. de La Dure-Molla 2015 treats DSPP as yielding three proteins (DSP, DGP, DPP) cleaved by astacin- and MMP-family proteases. A KB should record the three-product model (literature consensus) and note that UniProt's chain annotation merges DSP+DGP.

### Pathogenic variant landscape

Two independent systematic reviews provide the current counts. **They disagree on denominators because of different inclusion rules — record both.**

**Boonyakanog A, Sriwangyang K, Eamtanaporn T, Krasaesin A, Fakhruddin KS, Chantarangsu S, Cho SD, Rokny HA, Porntaveetus T.** "Beyond the diagnosis: Unraveling DSPP genotype-phenotype correlations in dentin dysplasia and dentinogenesis imperfecta." *Jpn Dent Sci Rev* 2026;62:46–56. **PMID 41583696**, PMC12830278, DOI 10.1016/j.jdsr.2026.01.001. PROSPERO CRD420251170506. 48 publications, **70 distinct DSPP variants, 99 genotype–phenotype records**, search Jan 1997–Aug 2025.

- Exon distribution: **exon 5 = 61% (43/70)**; exon 4 fewest at 4% (3/70)
- Variant types: **frameshift 60% (42/70); splice site 22% (15/70);** missense, nonsense and signal-peptide variants 4–6% each
- Exon × type: all intronic variants are splice site; exon 2 has 3 signal-peptide + 3 cleavage-site variants; exon 3 is 57% splice / 43% missense; exon 4 mostly nonsense (67%); **exon 5 is 98% frameshift (42/43)** plus one nonsense
- Phenotype distribution across 99 records: **DGI-II 47%; DD-II 22%; unspecified DGI 14%; DGI-III 13%; DD-II/DGI-II 3%**
- Quoted: "Exon 5 harboured 61 % of variants, predominantly frameshifts disrupting the repetitive dentin phosphoprotein (DPP) domain"; the review highlights "a continuous spectrum of DSPP disorders"

**Gilani M, Saikia A, Anthonappa R.** "The genetics of non-syndromic dentinogenesis imperfecta: a systematic review." *Eur Arch Paediatr Dent* 2025;26(1):3–16. **PMID 39806231**, PMC11865110, DOI 10.1007/s40368-024-00992-6. PROSPERO CRD42023470897. 3,475 articles screened → 41 included; **59 DSPP mutations from 37 publications**.

- Region distribution: exon 2 = 5; intron 2 = 7; exon 3 = 7; intron 3 = 5; exon 4 = 1; **exon 5 = 34** ("58% of the reported mutations (34/59)")
- "**All frameshift mutations (n = 38) were found within exon 5**"
- "Exon 5 mutation leads to frameshift changes, often resulting in severe DI forms"

> **Internal-consistency caveat (verified in the retrieved text):** Gilani et al.'s variant-type percentages (splice 45% n=118; missense 30% n=79; nonsense 7% n=18; indel 4% n=10) use a denominator of "263 mutation categories," which counts reported *cases*, not distinct variants. These percentages must not be read as a breakdown of the 59 distinct variants. The same paper's Table 1 also labels several cases as "DI-I" despite inclusion criteria restricted to DI-II, DI-III and DD-II.

### Specific variants (HGVS as reported in the retrieved sources)

Reference transcript NM_014208.3 unless otherwise stated.

**5′ region — signal peptide, cleavage site, IPV motif, DSP (exons 2–4, introns 2–3):**

| Variant | Protein | Reported phenotype | Source |
|---|---|---|---|
| c.16T>G | p.Tyr6Asp (Y6D) | DD-II | Barron 2008 Table 1; Gilani Table 1; UniProt annotates Asp-6 as "does not translocate into the ER" |
| c.38C>A | p.Ala13Glu (A13E) | DGI-III (novel) | Wang Y et al., *Mol Genet Genomic Med* 2025;13(3):e70087, **PMID 40040554**, PMC11880773 — "The secretion of the variant DSPP protein was not detected" |
| c.44C>T | p.Ala15Val (A15V) | DGI-II | Barron 2008; Gilani |
| c.49C>A | p.Pro17Thr (P17T) | DGI-II; DFNA39-associated per Barron 2008 and UniProt | Barron 2008; UniProt |
| c.49C>T | p.Pro17Ser (P17S) | DGI-II; **the Brandywine mutation** per Lee et al. 2013 | Barron 2008; Lee SK et al. 2013 |
| c.50C>T | p.Pro17Leu (P17L) | DGI-III | Lee SK, Lee KE, Song SJ, Hyun HK, Lee SH, Kim JW, *Biomed Res Int* 2013;2013:948181, **PMID 23509818**, PMC3591212 |
| c.52G>T | p.Val18Phe (V18F) | DGI-II/III; also isolated DI in French families 1–3 | Barron 2008; Caravello 2026 |
| c.53T>A / c.53T>G / c.53T>C | p.Val18Asp / p.Val18Gly / p.Val18Ala | DI-II, DI-II, DI-III respectively | Gilani Table 1 |
| c.52-3C>G; c.52-3C>A; c.52-2A>G; c.52-25del23bp | splice (intron 2) | DI | Gilani Table 1 |
| c.133C>T | p.Gln45Ter (Q45X) | DGI-II | Barron 2008; Gilani |
| c.135+1G>A; c.135+2T>C; c.135+3A>G | splice (intron 3) | DI | Gilani Table 1 |
| c.202A>T | p.Arg68Trp (R68W) | DGI-II per Gilani/Barron | **Contested** — see below |
| c.255G>A | p.Trp85Ter | Isolated DI (de novo) | Hassib NF et al., *Clin Oral Investig* 2024, **PMID 38630328**, DOI 10.1007/s00784-024-05636-z |
| c.288T>A | p.Tyr96Ter | Isolated DI | Hassib 2024 |

> **Variant-classification conflict to carry forward:** ClinVar Miner lists 12 variants reported pathogenic for "dentinogenesis imperfecta type 2," including **c.202A>T (p.Arg68Trp)**, but reports a gnomAD allele frequency of ≈0.145 for it; GeneBe lists rs36094464 as **Likely benign (★★)**. UniProt still annotates Trp-68 under DGI2. A frequency of ~15% is incompatible with a dominant pathogenic allele for a 1-in-6,000 to 1-in-45,000 disease. **Treat p.Arg68Trp as a common polymorphism, not a pathogenic variant, unless primary re-evaluation says otherwise.** Barron 2008 separately records a DSPP polymorphism g.1480A>T with control allele frequencies of 15% (Finnish), 6% (Caucasian), 16% (African-American), which may be the same locus.

**3′ region — DPP repeat domain frameshifts (exon 5):**

| Variant | Protein | Phenotype | Source |
|---|---|---|---|
| p.S624TfsX687; p.S640TfsX671 | — | DD-II | Barron 2008 Table 1 |
| p.S758AfsX554; p.S842TfsX471 | — | DGI-II/III | Barron 2008 |
| p.S865fsX1313; p.S895fsX1313; p.D1146fsX1313; p.D1182fsX1312 | — | DGI-II | Barron 2008 |
| c.1918_1921delTCAG | p.Ser640Thrfs*673 | — | Gilani Table 1 |
| c.2134delA | — | DD-II | Gilani Table 1 |
| c.2525delG; c.3135delC; c.3676delA | — | DI | Gilani Table 1 |
| c.2317del; c.3555del | — | DGI (two novel, families A and B) | 2025 report retrieved via search; primary full text not fetched |
| c.2652del | p.Asp884Glufs*430 | DI — **reclassified** from an NGS mis-call of c.2656_2657insGTGAAGCA after ONT long-read with T2T reference | Caravello 2026 |
| c.1887del; c.1937del; c.2483del; c.2827del; c.3180del | — | DI (novel, ONT-detected) | Caravello 2026 |
| c.2695delA | p.Asn899fs | DGI Shields II (novel) | Gao Q et al., *BMC Oral Health* 2025;25:503, **PMID 40197225**, PMC11978159 |
| c.3504_3508dup | p.Asp1170Alafs*146 | DGI/DD (novel) | Yang J et al., *Mol Genet Genomic Med* 2015;4(1):28–38, **PMID 26788535**, PMC4707025 |

**Mechanistic nature of 3′ frameshifts:** Caravello 2026 (verbatim) describes these as producing "a −1 frame shift with a hydrophobic C-terminal extension and termination at a downstream stop codon."

### Genotype–phenotype correlation

Three independent statements, all pointing the same direction but with an important dissent:

1. **Barron 2008:** a trend, acknowledged as based on few samples — the most 5′ DPP frameshifts underlie DD-II and the more 3′ ones DGI-II/III.
2. **Boonyakanog 2026:** "DD-II was significantly associated with variants in exon 5" and most often frameshift; "DGI-III was strongly linked to variants in exons 2 and 3 and was **notably absent in cases with exon 5 variants**"; DGI-II and DD-II/DGI-II showed no significant association with location or type, read as an intermediate phenotype. (The abstract names signal-peptide, splice-site and missense variants for DGI-III, while the body emphasises missense — the two passages differ in emphasis.)
3. **Simmer 2022** formalises this into the modified Shields classification: 5′ defects → DGI-III, 3′ defects → DGI-II (**PMID 35627243**).

**Dissent:** de La Dure-Molla 2015 report that "The same DSPP variant could result in a moderate or severe phenotype, previously diagnosed for DG-II or/and DGI-III," and that DGI-II and DGI-III "could be found on subjects of the same family, and even in the same patient." Caravello 2026 similarly "confirm that DSPP variants harbour a high degree of phenotypic variability, particularly within exon 5."

**Net:** the 5′/3′ correlation is a real statistical signal at the cohort level but is **not reliable for individual prognostication**. Both views should be curated.

### Allele frequency / population data

- gnomAD constraint metrics (pLI, LOEUF, missense Z) for DSPP **could not be retrieved in this session** — the gnomAD page was not accessible and I am not reporting values from memory. Note that DSPP's long, repetitive, low-complexity DPP domain makes short-read constraint metrics unreliable in any case.
- Barron 2008's polymorphism data: g.1480A>T at 15% / 6% / 16% in Finnish / Caucasian / African-American controls.
- UniProt annotates a non-disease variant Asn-243 (D→N, rs3750025).

### Somatic vs germline

**Germline exclusively.** No somatic DSPP involvement in this disease. (RGD annotates *Dspp* to mouth neoplasms and squamous cell carcinoma via CTD/ISO inference — this is expression/toxicogenomic association, not somatic causation of DI, and should not be imported.) De novo germline events occur: Hassib 2024 confirmed c.255G>A p.Trp85Ter as de novo.

### Functional consequences

**Dominant-negative / gain-of-function, not loss-of-function** — see §6 for the causal chain and the primary evidence (von Marschall 2012; Liang 2021; Lee 2013).

### Epigenetics

No disease-specific DNA methylation, histone-modification or chromatin data were retrievable for DSPP-related DI. The one adjacent finding is transcriptional, not epigenetic in the classical sense: a mouse study titled "Transcriptional Repression of the *Dspp* Gene Leads to Dentinogenesis Imperfecta Phenotype in Col1a1-Trps1 Transgenic Mice" (PMC3399940) — retrieved as a title only; primary text not fetched, so treat as a lead.

### Chromosomal abnormalities

**None described.** DI is not caused by aneuploidy, translocation or CNV in any retrieved source. CMA and karyotype have no diagnostic role.

---

## 5. Environmental Information

- **Environmental factors:** none established as causal or contributory. No CTD/TOXNET/EPA-sourced exposure is linked to DSPP-related DI.
- **Lifestyle factors:** none established as disease-causing. Diet (acid/abrasive), parafunction and oral-hygiene practice plausibly modulate the *rate* of attrition and secondary infection, but no retrieved study quantifies this.
- **Infectious agents:** not applicable as a cause. Infection is a **downstream complication** — once the obliterated or exposed pulp becomes infected, periapical abscess follows (see §11).

This section is genuinely empty of positive findings; I did not substitute weaker adjacent citations.

---

## 6. Mechanism / Pathophysiology

### Causal chain — isolated DSPP-related dentinogenesis imperfecta

> Steps 1–6 differ by mutation class; the branch is shown explicitly. "Demonstrated" = direct experimental evidence retrieved in this session; "inferred" = stated by authors as hypothesis.

**1.** A heterozygous *DSPP* variant arises in the germline (inherited from an affected parent in ~most cases; de novo documented — Hassib 2024). → **leads to** expression of a mutant DSPP allele in odontoblasts (CL:0000060), the sole high-expressing cell type (Barron 2008: dentine expression "hundreds of times higher" than other tissues). *Demonstrated.*

**→ BRANCH A — 5′ mutations (signal peptide, signal-peptidase cleavage site, IPV motif; exons 2–3)**

**2A.** The variant alters the signal peptide or the first residues of mature DSPP (the "IPV" motif) → **results in** failure of the nascent protein to exit the rough endoplasmic reticulum (GO:0005788 ER lumen). von Marschall et al. showed mutant full-length DSPP is **endoglycosidase H-sensitive** (high-mannose, rER-type glycosylation) and co-localises with the rER marker PDI, while WT appears in Golgi-like puncta; leader cleavage itself was normal for IPV mutants, so the block is *after* signal-peptide processing (**PMID 22392858**). *Demonstrated (HEK293/HEK293A transfection).*

**3A.** Mutant DSPP accumulating in the rER **physically entraps co-expressed normal DSPP** → **results in** reduced secretion of the wild-type product from the same cell. von Marschall: "Trafficking out of the rER by coexpressed normal DSPP was reduced in a dose-responsive manner." Reported dose-dependence (from the paper's results, partly via extraction summary): ISV caused ~40% loss of WT secretion at equal plasmid amounts and >70% at a 4:1 mutant:WT ratio. *Demonstrated in vitro; this is the core dominant-negative step.*

**3A′.** Independent confirmation for p.P17L: wild-type DSP-GFP was >7-fold more abundant in medium than P17L; intracellular P17L was 12.1-fold higher than WT (both P<0.01); WT "localized exclusively in the Golgi apparatus" while mutant "largely remained in the ER." Splicing was unaffected — "The mutation did not influence pre-mRNA splicing but caused ER retention and defective protein secretion" (Lee et al. 2013, **PMID 23509818**). *Demonstrated (HEK293T; pSPL3 minigene splicing assay in COS-7).*

**4A.** Secretion failure → **results in** reduced DSPP delivery to the predentine (UBERON:0011587) matrix. In the *Dspp*^P19L knock-in mouse (mouse equivalent of human p.P17L), "Secretion of the mutant Dspp P19L protein was impaired and it accumulated within the ER," and odontoblasts of both het and hom mice had reduced DSPP expression versus WT (Liang et al. 2021, **PMID 34667213**; Liang et al., *Front Physiol* 2021;12:724098). *Demonstrated in vivo.*

**5A.** rER overload is **inferred** to activate ER stress / the unfolded protein response. **No UPR marker measurements (BiP/GRP78, CHOP, XBP1, ATF6, PERK) were found in any retrieved primary paper.** von Marschall state rER stress is "likely activated." Boonyakanog 2026 lists ER retention as a mechanism class but frames it as hypothesis. *Inferred, not demonstrated — flag as a genuine evidence gap.*

**→ BRANCH B — 3′ mutations (exon 5, DPP repeat domain, −1 frameshift)**

**2B.** A single-base indel in the long repetitive exon-5 DPP region shifts translation into the **−1 reading frame** → **results in** a protein with a hydrophobic C-terminal extension terminating at a downstream stop codon (Caravello 2026, verbatim; Boonyakanog 2026). In the mouse model this extension adds 493 extraneous residues (Liang 2021). *Demonstrated.*

**3B.** The hydrophobic extension is **inferred** to anchor the mutant protein to the rER membrane; the exposed acidic repeat domains then form **Ca²⁺-bridged aggregates** that sequester wild-type DSPP. Boonyakanog 2026 presents this as the mechanism class for exon-5 frameshifts. von Marschall used lanthanum precipitation as an in vitro stand-in for calcium binding. *Partly demonstrated, partly inferred — the Ca²⁺-aggregation step is a model, not a measured mechanism in odontoblasts.*

**3B′ (severity rule).** von Marschall's proposal for why DD-II is milder than DGI-II: a shorter remaining repeat domain captures less normal DSPP. Their DGI-like frameshift construct (≈287 repeat residues retained) suppressed WT secretion more than the DD-like construct (no repeats retained), at every dose. *Demonstrated in vitro — this is the molecular basis of the 5′/3′ severity gradient.*

**4B.** Additionally, *Dspp*^−1fs mRNA was reduced, "suggesting that the Dspp−1fs mRNA was selectively degraded or the cells expressing it deteriorated" (Liang 2021). *Demonstrated (mouse), mechanism uncertain.*

**→ CONVERGENCE**

**5.** Loss of functional secreted DSPP in predentine → **results in** failure of normal proteolytic processing (by BMP1/tolloid astacin-family proteases and MMP-2/MMP-20) into DSP, DGP and DPP. *Cited in Lee 2013's introduction (refs to von Marschall & Fisher, Matrix Biol 2010, PMID 20079836; Yamakoshi et al., JBC 2006) but **not independently verified in this session** — a targeted BMP1-DSPP literature search did not return the processing papers.*

**6.** Loss of DPP — a highly phosphorylated, Asp-Ser-Ser-rich polyanion — → **results in** failure of normal hydroxyapatite nucleation and growth control at the mineralisation front. de La Dure-Molla 2015: DPP initiates hydroxyapatite formation at low concentration and inhibits growth at high concentration (in vitro). UniProt: "DPP may bind calcium and facilitate initial mineralization of dentin matrix collagen." A 2025 mouse paper refines the requirement: "DSP and DPP are dispensable for initiation of dentin and enamel mineralization but critical for circumpulpal dentin mineralization" (Liang T et al., *Sci Rep* 2025;15:24913, **PMID 40640300**, PMC12246090). *Demonstrated in vitro and in mouse.*

**7.** Defective circumpulpal dentine mineralisation → **results in** hypomineralised, irregularly tubular or atubular dentine with abnormal crystallite shape and thickness. de La Dure-Molla 2015: histology shows "few, large dentinal tubules running in different directions, with atubular areas"; synchrotron tomography and SAXS showed abnormal crystallite shape and thickness. In *Dspp*^−1fs mice dentine "lacked dentinal tubules, contained cellular debris, and was significantly softer and thinner." *Demonstrated (human histology + mouse).*

**8.** Hypomineralised dentine → **branches into three clinical consequences:**

- **8a.** Altered enamel–dentine junction → **leads to** enamel shearing/chipping (enamel fractures follow the striae of Retzius; de La Dure-Molla 2015) → **leads to** exposure of soft dentine → **leads to** rapid attrition (HP:4000181), crown height loss, and loss of occlusal vertical dimension.
- **8b.** Continued pathological dentine apposition into the pulp space → **leads to** pulp chamber and root canal obliteration (HP:0006350) — or, at the severe/5′ end, failure of circumpulpal dentine deposition → **leads to** enlarged pulp, "shell teeth," and pulp exposure (HP:0000694).
- **8c.** Bacterial ingress through worn or fractured dentine, plus (per a micro-CT/polarising-microscopy study) persistence of vessel remnants in apparently obliterated pulp chambers → **leads to** pulp necrosis, periapical inflammation (HP:0000700), abscess (HP:0030758), and tooth loss (HP:0006323 / HP:0006357).

**9.** An **off-chain but experimentally real** finding: 5′ mutations also affect **enamel**, via the transient pre-ameloblast expression of DSPP. In *Dspp*^P19L mice enamel was "softer than normal" with reduced rod/interrod definition and reduced enamel volume in mandibular first molars, whereas *Dspp*^−1fs enamel was normal (nanohardness: WT enamel 3.82 GPa; P19L het 2.88, hom 2.94; −1fs het 3.76, hom 3.78 GPa) (Liang 2021). This is a **mutation-class-specific** secondary effect.

### Category checklist against the chain

- **Molecular pathways:** no canonical signalling cascade (Wnt/MAPK/mTOR/PI3K-AKT) is implicated in *DSPP*-related DI. The relevant process is **secretory protein trafficking and extracellular matrix biomineralisation**, not signal transduction. (Wnt/β-catenin appears in hereditary dentine disorders only via *VPS4B* in dentin dysplasia type I — a different gene and disease; Xue Q et al., *Front Cell Dev Biol* 2024;12:1474966, **PMID 39717845**.)
- **Cellular processes:** ER protein retention; impaired secretory trafficking; inferred ER stress; odontoblast secretory dysfunction. Suggested GO: **GO:0097188** dentin mineralization; **GO:0097187** dentinogenesis; **GO:0034505** tooth mineralization; **GO:0042475** odontogenesis of dentin-containing tooth; **GO:0031214** biomineral tissue development; **GO:0071895** odontoblast differentiation; **GO:0046848** hydroxyapatite binding.
- **Protein dysfunction:** dominant-negative via rER entrapment of the wild-type product; misfolding/mislocalisation rather than catalytic loss. Explicitly **not** haploinsufficiency (von Marschall 2012; Liang 2021).
- **Metabolic changes:** none. No metabolomic or lipidomic signature was retrievable, and none is expected.
- **Immune system involvement:** none primary. Secondary pulpal/periapical inflammation only.
- **Tissue damage mechanisms:** mechanical — attrition and fracture of a hypomineralised composite — plus secondary infection. Not oxidative stress, ischaemia or fibrosis.
- **Biochemical abnormalities:** reduced mineral density and microhardness of dentine; one study with a known DSPP mutation reported lower mineral density, lower microhardness and **reduced magnesium** (**PMID 32585446**, retrieved via abstract listing). Reported DI dentine microhardness ≈1.18 GPa vs ≈1.72 GPa for normal permanent dentine (single study, 2010; retrieved via abstract listing — treat as a lead). A 2025 nanomechanics study of DGI-II dentine found reduced Young's modulus and greater indentation depth (PMC12139306).
- **Epigenetic changes:** none retrievable.
- **Molecular profiling:** no human DI transcriptomic, proteomic, metabolomic or lipidomic datasets were retrievable. **Explicitly not available.**
- **Advanced technologies:** no single-cell, spatial-transcriptomic, multi-omic or CRISPR/RNAi screen data specific to DI were retrievable. The only CRISPR work is targeted mouse allele construction (Liang 2021), not screening.

### Cell types and anatomical compartments

- **CL:0000060** odontoblast (primary); **CL:0007003** preodontoblast; **CL:0007013** terminally differentiated odontoblast; **CL:0000345** dental papilla cell; **CL:0007001** skeletogenic cell (parent). Pre-ameloblasts are transiently involved (UniProt tissue specificity) but no distinct CL term was verified for them in this session.
- Subcellular (GO Cellular Component): rough endoplasmic reticulum / ER lumen (site of mutant retention); Golgi apparatus (where WT, but not mutant, is trafficked); extracellular matrix / extracellular space (normal destination, per UniProt).

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** the **tooth** (UBERON:0001091 "calcareous tooth"), both dentitions, all tooth classes. de La Dure-Molla 2015 report that in DI "all teeth in the primary and permanent dentition may appear nearly identical" — generalised, not focal, involvement.
- **Secondary:** periodontium and alveolar bone, via periapical inflammation and premature tooth loss. de La Dure-Molla: "Periodontal disease is frequent without caries." In *Dspp*^−1fs mice, alveolar bone recession was seen in molars and incisors at 7 weeks (Liang 2021). MGI annotates *Dspp*^tm1Kul homozygotes as a model of **DOID:3388 periodontal disease** in addition to DOID:4154.
- **Possible, contested:** inner ear (DFNA39 — see §3).
- **Not affected:** the skeleton. Barron 2008: no bone defects are seen with DSPP mutations despite DSPP expression in bone. This is the single most important anatomical discriminator from OI-associated DGI.
- **Body systems:** digestive (upper — masticatory function); integumentary/skeletal only insofar as teeth are mineralised tissues. Not cardiovascular, nervous, respiratory or endocrine.

### Tissue and cell level

| Structure | UBERON | Involvement |
|---|---|---|
| Dentine | **UBERON:0001751** (exact syn. dentin) | **Primary site** — hypomineralised, abnormal tubules |
| Pre-dentine | **UBERON:0011587** | Widened in *Dspp* KO mice (Sreenath 2003) |
| Enamel | **UBERON:0001752** | Secondary — shears off due to altered DEJ; primarily affected only by 5′ mutations in mouse |
| Dental pulp / endodontium | **UBERON:7500085** (syn. pulp-dentin complex) | Obliterated or (severe form) enlarged |
| Odontogenic papilla | **UBERON:0001763** | Origin of odontoblasts |

Cell populations: **CL:0000060 odontoblast** (the effector cell), with pre-ameloblast involvement explaining the secondary enamel defect.

### Subcellular level

Rough ER / ER lumen (mutant protein retention); Golgi apparatus (normal trafficking route, blocked); secretory vesicles; extracellular matrix destination. UniProt subcellular location for normal DSPP: "Secreted, extracellular space, extracellular matrix."

### Localization and lateralization

**Generalised and bilateral/symmetric**, affecting the whole dentition. Barron 2008: "Normal teeth are never found in DGI-II." There is no unilateral or segmental form — a segmental presentation should redirect the differential to **regional odontodysplasia**.

---

## 8. Temporal Development

### Onset

- **Biologically congenital** — the dentine defect is laid down during odontogenesis in utero (primary teeth) and childhood (permanent teeth). Barron 2008 describes dentine hypertrophy and pulp obliteration occurring "before or just after eruption."
- **Clinically apparent in infancy/early childhood**, at eruption of the primary dentition (~6 months onward). GARD states: "Symptoms of this disease may start to appear as a Child" (citing Orphanet). One documented case was first assessed at 1.5 years (Petrova L, Ustiča J, Čēma I, *Reports* 2026;9(2):115, **PMID 42029463**, PMC13108200); another proband at 2.5 years (Lee 2013).
- **Onset pattern: insidious/chronic**, not acute. The acute events are superimposed abscesses.
- Suggested HPO onset terms: congenital/neonatal onset for the dentine defect; infantile/childhood onset for clinical manifestation. (I did not verify specific HP onset term IDs in this session; the HPO annotations for OMIM:125490 and OMIM:125500 carry **blank onset fields** — a real annotation gap in HPO.)

### Progression

- **Course: chronic, lifelong, progressive** with respect to wear and tooth loss; the underlying dentine defect itself is static (the matrix is already laid down abnormally).
- **Stages (de facto, from the clinical literature rather than a formal staging system — no validated staging system exists):**
  1. *Eruption stage* — discoloured, translucent, bulbous crowns; intact enamel.
  2. *Enamel-loss stage* — chipping/shearing at the DEJ, dentine exposure.
  3. *Attrition stage* — rapid wear, crown height loss, reduced occlusal vertical dimension; de La Dure-Molla: attrition ranges "from a few facets to complete loss of the crown."
  4. *Endodontic/periapical stage* — pulp necrosis, periapical radiolucency, abscess.
  5. *Edentulism / rehabilitation stage* — tooth loss and prosthetic replacement.
- **Rate:** rapid in the primary dentition, often slower in the permanent dentition (de La Dure-Molla: "Primary teeth are often more severely affected than permanent teeth").
- **Mouse parallel for temporal evolution:** *Dspp*^P19L mice "at a younger age displayed a tooth phenotype resembling human DGI type III, with enlarged pulp chambers, while older mice had smaller pulp chambers mimicking DGI type II" — the Shields "types" may partly be snapshots of the same process at different ages (Liang et al., *Front Physiol* 2021;12:724098).
- **Duration:** lifelong. No remission, spontaneous or treatment-induced; treatment is compensatory, not curative.

### Critical periods for intervention

The German S3 guideline places the decision points explicitly (Dujic et al. 2026, **PMID 42771210**):

- **Primary/mixed dentition:** protective restoration "as soon as such teeth erupt" — stainless steel crowns and direct restorations (Rec 5, Rec 6).
- **Early permanent dentition:** "The definitive treatment should be implemented starting with the early permanent dentition using the full-mouth rehabilitation approach" (Rec 9). Per the guideline's narrative, definitive restoration of the whole permanent dentition is usually undertaken late in the second or early in the third decade; indirect restorations on first permanent molars begin in adolescence.
- **Post-growth:** implants only after skeletal growth is complete (Barron 2008 lists implants as part of treatment "usually continu[ing] into adulthood").

---

## 9. Inheritance and Population

### Epidemiology

| Estimate | Figure | Design | Source |
|---|---|---|---|
| Classic incidence | **1 in 6,000 – 1 in 8,000** | Witkop, US data, 1975 | Cited by Barron 2008 (refs 1 and 3) and de La Dure-Molla 2015 (ref 5), who stress "These data only came from United States" and date from 1975 |
| French clinic-based prevalence | **0.057%** (≈1 in 1,750) | 8,830 panoramic radiographs from a Paris maxillofacial imaging centre; **5 cases**, two of them siblings; males 0.080% vs females 0.039% | Cassia et al. 2017, PMC5390575 |
| Swedish nationwide, population-based | **0.0022%** (95% CI 0.0016–0.0029), **≈1 in 45,455** | 44 children/adolescents (19 M, 25 F) born 1996–2015; denominator 2,044,530 births | Andersson et al., *Orphanet J Rare Dis* 2018, **PMID 30134932** |
| Saudi children | 0.1% | Single-centre, retrospective | Cited in the Swedish paper |
| Brandywine isolate | "the highest incidence of all dental genetic diseases at **1 in 15**" | Historical, triracial isolate, Maryland | de La Dure-Molla 2015 (citing ref 40) |
| Dentine dysplasia (for contrast) | ~1 in 100,000 (DD / DD-I) | Witkop | Barron 2008; de La Dure-Molla 2015 |

> **Recommended curation:** the Swedish figure (≈1/45,455) is the only **population-based, nationwide, registry-ascertained** estimate and is ~7–18× lower than the classic Witkop figure. Its authors "concluded that these results show a significantly lower prevalence of DGI type II than previously reported." The French figure is referral-biased upward. The Witkop figure, though ubiquitous, is 50-year-old US-only data. Record all three with their designs rather than a single number.

GARD's own listing gives a very wide "worldwide estimate of 800,000 to 5,000,000" and ~200,000 US cases — these are **not** reconcilable with the Swedish data and appear to be order-of-magnitude placeholders; I would not import them.

### Inheritance

- **Autosomal dominant** (HP:0000006). HPO annotates AD inheritance to both OMIM:125490 (cited PMID:11175779) and OMIM:125500. MedGen lists AD from Orphanet.
- **Penetrance:** Barron 2008 — in DGI-II "penetrance is virtually complete"; de La Dure-Molla 2015 cite "autosomal dominant trait with complete penetrance." A 2004 study notes "complete penetrance and a low frequency of de novo mutations" (retrieved as a cited statement). **Treat penetrance as complete/near-complete.**
- **Expressivity:** **variable**. de La Dure-Molla 2015: "The expression variability, even in the same family, is a constant observation in this hereditary condition," and DGI-II and DGI-III "could be found on subjects of the same family, and even in the same patient."
- **Recurrence risk:** 50% per offspring of an affected individual (standard AD; no retrieved source states this number explicitly for DI, so it is stated here as the arithmetic consequence of the inheritance mode, not as a cited figure).
- **Genetic anticipation:** **not applicable** — no repeat-expansion mechanism. (Note: DSPP *does* contain a repeat region, but it is a protein-coding Asp-Ser-Ser repeat with length polymorphism, not an unstable expanding repeat. Yang et al. 2015 found 32 indels forming 36 haplotypes in normal DPP, with human DPP varying between 770 and 902 amino acids and "165 DSS sequences in human DPP" — **PMID 26788535**.)
- **Germline mosaicism:** not documented in any retrieved source. De novo variants are documented (Hassib 2024, confirmed de novo c.255G>A).
- **Founder effects:** the **Brandywine triracial isolate** (Maryland / Washington DC) is the classic example, historically the source of Shields DGI-III. Lee et al. 2013 identify **c.49C>T (p.P17S)** as "the Brandywine mutation." de La Dure-Molla cite work confirming a DSPP variant in a Brandywine DGI-III family that "confirmed the allelic relation between DGI-II and DGI-III."
- **Consanguinity:** no established role — this is a dominant disorder.
- **Carrier frequency:** not applicable (dominant, fully penetrant; "carriers" are affected).

### Population demographics

- **Ethnic distribution:** Gilani 2025's Table 1 ethnicity counts show reported DSPP variants across Asian, European, American and African ancestries (exon 2: Asian 27, European 10, American 8; exon 5: Asian 27, American 23, European 22, African 9). The same review states "All reported mutations were identified in those of Asian descent" for the COL1A1/COL1A2 non-syndromic cases. Hassib 2024 describes DSPP as "the most common DI causative gene **irrespective of patients' ethnicity**." The apparent Asian over-representation most plausibly reflects publication and ascertainment patterns rather than true prevalence difference — Gilani's own discussion raises geography, sampling, awareness and publication bias (that remark came via extraction summary and is flagged as unverified against the page text).
- **Geographic:** worldwide. The Swedish study found the highest absolute number in Stockholm County (n=16) but the highest relative prevalence in Gotland (0.009%) — consistent with a founder/clustering effect in a small island population, though the authors did not characterise it as such.
- **Sex ratio:** **no established sex difference**, as expected for an autosomal dominant trait. The French study found 0.080% in males vs 0.039% in females but concluded "there was no disparity in prevalence among genders" (n=5 cases). The Swedish cohort was 19 male : 25 female.
- **Age distribution:** all ages; clinical burden concentrated in childhood (primary dentition destruction) and early adulthood (definitive rehabilitation).

---

## 10. Diagnostics

### Clinical diagnosis

The German S3 guideline states that diagnosis is "usually based on visual assessment by an experienced dentist," supplemented by radiographs "taken according to indications," which "provide additional diagnostic information" (Dujic 2026, **PMID 42771210**). Barron 2008 notes diagnosis rests on family history, pedigree and clinical examination.

**Key clinical/radiographic findings:**
- Generalised opalescent amber/blue-grey/brown discolouration of both dentitions
- Bulbous crowns with marked cervical constriction (HP:0033780)
- Enamel chipping with sclerotic, glassy exposed dentine — and characteristically **little or no sensitivity**
- Short, thick roots (HP:0006336)
- Pulp obliteration (HP:0006350) — de La Dure-Molla call bulbous crowns + cervical constriction + short thick roots + pulp obliteration "pathognomonic" — **or**, in the severe form, "shell teeth" (HP:0000694)
- Periapical radiolucencies in non-carious teeth (HP:0000700) — Barron 2008

**Laboratory tests, biomarkers, functional tests, electrophysiology:** **none exist and none are indicated.** There is no blood/urine biomarker, no enzyme assay, no circulating marker. The only non-dental investigation with a clear role is **audiometry**, where the DFNA39 question arises, and the evidence for that association is unresolved (§3).

**Imaging:** intraoral periapical and bitewing radiographs, plus panoramic radiography (the modality used in the French prevalence study). CBCT/CT and histopathology were used in the canine case report. No validated RadLex-coded protocol was retrieved.

**Biopsy/pathology (research, not routine):** extracted-tooth histology shows few, large, irregularly oriented dentinal tubules with atubular areas; enamel fractures following the striae of Retzius; an altered enamel–dentine junction (de La Dure-Molla 2015). Micro-CT, polarising microscopy, synchrotron tomography, SAXS and nanoindentation have all been applied in research settings.

### Genetic testing

**Recommended approach (synthesising the retrieved guideline + cohort evidence):**

1. **Exclude osteogenesis imperfecta first.** Simmer 2022's suggested workflow: start with exome sequencing of the proband, then check **COL1A1/COL1A2** for dominant OI, then 5′ *DSPP*, then 3′ frameshifts near the edges of the repeat region, with SMRT sequencing if nothing is found (**PMID 35627243**). The Swedish prevalence authors "stressed excluding osteogenesis imperfecta (OI) in children with DGI."
2. **Targeted gene panel.** Caravello 2026 used the **GenoDENT** NGS panel (653 genes) with **added DSPP repeat probes** (**PMID 41819808**).
3. **The exon-5 repeat region is the hard part.** Yang et al. 2015: "the only way to sequence the DPP repetitive region was to clone PCR amplification products"; they used **SMRT (PacBio) long-read** sequencing to read the repeat without cloning (**PMID 26788535**).
4. **Long-read sequencing is now moving to first line.** Caravello et al. first used **Oxford Nanopore** as "an effective second-line strategy" when short reads were inconclusive, then revised their workflow "to begin directly with long-read DSPP exon 5 sequencing using ONT," concluding that "integrating long-read sequencing into routine diagnostics" is valuable. Their cohort demonstrates why: an apparent NGS call of c.2656_2657insGTGAAGCA in families 21–28 was **reclassified by ONT against the T2T reference** as c.2652del p.(Asp884Glufs*430).
5. **Yield:** in 112 individuals (42 index cases), DSPP variants were found in all index cases except one; molecular diagnosis was reached in 41 families; 22 P/LP variants, 14 of them novel (Caravello 2026).

**Modality-by-modality utility:**

| Modality | Utility for DI |
|---|---|
| Targeted *DSPP* single-gene / panel | **First line** (with COL1A1/COL1A2 included) |
| **Long-read (ONT / PacBio SMRT)** | **Essential** for exon-5 DPP repeat; short reads mis-call indels here |
| WES | Useful when the phenotype is uncertain or syndromic; **unreliable for the DPP repeat** |
| WGS | Same repeat limitation as WES unless long-read |
| CMA, karyotype, FISH | **No role** — no CNV/structural mechanism |
| mtDNA testing | **No role** |
| Repeat-expansion testing | **No role** (the DPP repeat is coding and non-expanding) |
| RNA-seq / proteomics / metabolomics / epigenomics / liquid biopsy | **No established diagnostic role**; no DI datasets retrievable |

The German S3 guideline's Recommendation 2 (expert consensus; strength "Moderate"): "If clinical and radiological findings suggest a genetic cause for a rare dental disorders, genetic diagnostics should be performed, usually in combination with a clinical consultation at a genetic practice or outpatient clinic." It adds that "only genetic analyses can provide precise information about the aetiology and prognosis of the disease, potential complications, and possible involvement of other organ systems," and that a VUS is not diagnostic while a normal result does not exclude a genetic cause. The guideline **names no specific genes or panels** for DI.

The MedGen GTR summary for OMIM 125490 lists 14 sequence-analysis entries, 11 deletion/duplication, 3 targeted-variant and 1 research test.

**Variant catalogue:** de La Dure-Molla 2015 point to the **LOVD DSPP** database (lovd.nl/DSPP) as the variant repository.

### Clinical criteria

**No formally validated diagnostic criteria exist.** The Shields (1973) classification functions as the de facto descriptive framework and is explicitly criticised as outdated (Barron 2008; de La Dure-Molla 2015; Simmer 2022). The German S3 guideline provides management, not diagnostic, recommendations for DI.

### Differential diagnosis

Barron 2008's abstract list: **hypocalcified amelogenesis imperfecta; congenital erythropoietic porphyria; conditions causing early tooth loss (Kostmann's disease, cyclic neutropenia, Chediak-Higashi syndrome, histiocytosis X, Papillon-Lefèvre syndrome); tetracycline discolouration; vitamin D-dependent and vitamin D-resistant rickets.**

Key discriminators retrieved:
- **Amelogenesis imperfecta** — enamel-only defect; "The dentin, pulp, and cementum will not exhibit pathologic changes." Dentine, pulp morphology and root form are normal.
- **Congenital erythropoietic porphyria** — erythrodontia (HP:0030756), red fluorescence under Wood's lamp; diagnosed by "finding the abnormal levels [of porphyrins] in erythrocytes and plasma," i.e. a systemic blood workup.
- **Dentine dysplasia type I (radicular)** — "teeth in DD-I appear generally unremarkable clinically with normal shape, form and consistency. Radiographically, the roots are sharp with conical, apical constrictions"; crescent-shaped pulpal remnants; caused by **SMOC2, VPS4B, SSUH2** — *not DSPP* (Chen D et al., *Oral Dis* 2019;25(2):439–446, **PMID 29575674**, PMC7818184: DSPP is "the pathogenic gene of DGI-II, DGI-III, and DD-II, **but not DD-I**"). DD-I is distinguished from hypophosphatasia by premature tooth loss with root-length changes.
- **DGI with osteogenesis imperfecta (COL1A1/COL1A2)** — the critical exclusion. Look for fractures, blue sclerae, short stature, hearing loss, positive family history of fragility fracture. In a 294-patient paediatric OI cohort, DI was present in 49% of those with COL1A1/COL1A2 variants vs 15% without (PMC11499677); a Ukrainian cohort reported DI in 55% overall (PMC6696896); a retrospective cohort found DI risk higher when the glycine substitution lay C-terminal to Gly305 in COL1A1 or Gly211 in COL1A2 ([PLOS ONE 10.1371/journal.pone.0176466](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0176466)). **Caveat flagged by that search:** the glycine-position thresholds came through partially garbled and should be checked against the full paper before use.
- **Regional odontodysplasia** — segmental/unilateral, not generalised.
- **Tetracycline staining, fluorosis, enamel hypoplasia from environmental insult** — history-dependent, not familial, dentine normal.

**Complication (per Gilani 2025):** four studies identified COL1A1/COL1A2 variants in individuals reported as *non-syndromic* DI, predominantly of Asian descent (e.g. COL1A1 c.1463G>C p.Gly488Ala; COL1A2 c.1009G>A p.Gly337Ser, c.1171G>A p.Gly391Ser, c.3233G>A p.Gly1078Asp). This means **collagen genes belong on a non-syndromic DI testing panel**, and that a COL1A1/COL1A2 finding obliges a skeletal and ophthalmological assessment even when the presentation looks purely dental.

### Screening

- **No newborn screening, no population screening, no carrier screening.** Not applicable: dominant, fully penetrant, non-lethal, visually diagnosable at eruption.
- **Cascade testing** within affected families is the relevant genetic-screening activity. The German S3 guideline advises taking a family history across several generations and flags "similar findings in several family members" as an indicator of genetic aetiology.
- **Prenatal diagnosis / PGT-M:** technically feasible once the familial variant is known. **No retrieved source documents PGT-M for a DSPP variant**, and I did not find any guideline addressing it. Hassib 2024 discusses genetic counselling for DI families "taking into account religious, cultural, and legal considerations." Given a non-lethal, treatable dental phenotype, prenatal testing would be an unusual request and is not a standard offering.

---

## 11. Outcome / Prognosis

### Survival and mortality

**Not a cause of mortality.** No excess mortality, no reduction in life expectancy, no disease-specific deaths. SEER/GBD/CDC Wonder data are not applicable. Isolated DI does not affect survival.

### Morbidity and function

The morbidity is entirely dental and functional:
- Progressive loss of tooth structure and occlusal vertical dimension
- Impaired mastication
- Aesthetic impairment with likely psychosocial sequelae (under-studied — see §3)
- Risk of partial or complete edentulism requiring lifelong prosthetic care
- The German S3 guideline states generally that rare dental disorders "are frequently associated with severe functional impairments" and "a reduced oral health–related quality of life"

**No DI-specific disability, ICF or DALY quantification was retrievable.** No validated DI-specific PROM exists; NCT04927962 used COHIP in a mixed AI/DI paediatric population.

### Complications

- **Pulp necrosis and periapical abscess**, including in teeth that are non-carious and apparently pulp-obliterated. A micro-CT/polarising-microscopy study of primary DGI-II teeth suggested that vessel remnants persisting in the apparently obliterated pulp chamber may explain abscess formation in teeth with no visible pulp.
- **Pulp therapy frequently fails.** Barron 2008's review states that once abscesses develop, pulp therapy generally fails and the affected teeth need removal. Endodontic treatment is not advised when the canals are completely obliterated.
- **Premature tooth loss**, periodontal disease without caries, loss of occlusal vertical dimension, malocclusion.
- **Frequency conflict to note:** the AAPD heritable-disorders guidance says primary teeth "often" show periapical radiolucencies and that abscess potential justifies periodic radiographic monitoring; a ScienceDirect overview says periapical rarefaction in the primary dentition is seen "only occasionally." Both are narrative sources; no cohort-level frequency was retrieved.

### Recovery potential

**None spontaneously.** The dentine defect is permanent and the tissue is not renewable. Outcome depends entirely on restorative intervention. Barron 2008's abstract: where diagnosis is early and treatment follows the recommendations, "good aesthetics and function can be obtained."

### Prognostic factors

| Factor | Direction | Evidence quality |
|---|---|---|
| Mutation location (5′ vs 3′) | 5′ → more severe (DGI-III, shell teeth, pulp exposure); 3′ distal → milder (DD-II) | Cohort-level statistical association (Boonyakanog 2026); **unreliable individually** (de La Dure-Molla 2015; Caravello 2026) |
| Dentition | Primary dentition more severely affected than permanent | de La Dure-Molla 2015, confirmed across all reviewed cases |
| Age at diagnosis / timing of protective restoration | Earlier → better outcome | Barron 2008 (expert narrative, not trial evidence) |
| Presence of pulp exposure / abscess | Predicts endodontic failure and extraction | Barron 2008 |
| Presence of a COL1A1/COL1A2 variant | Implies possible skeletal involvement; changes the whole prognostic frame | Gilani 2025 |

**No prognostic biomarkers exist.** Boonyakanog 2026 argue that integrating DSPP genotyping into diagnostic workflows is "essential to predict disease progression" — this is an aspiration based on cohort-level correlation, not a validated prognostic tool.

---

## 12. Treatment

### The evidence base — state it plainly

The German S3-level guideline is the **highest-quality synthesis available** and it rates **every one of its eight dentinogenesis imperfecta recommendations as "Very low" (⊕⊝⊝⊝) quality of evidence**, noting that "Given the predominance of case reports and case series in this field, evidence was generally rated as low quality" (Dujic H, Bücher K, Schüler IM, Schmidt P, Hertel S, Timpel J, Jablonski-Momeni A, Schilke R, Kapferer-Seebacher I, Zschocke J, Liebermann A, Güth JF, Edelhoff D, Heinrich-Weltzien R, Kühnisch J. *Clin Oral Investig* 2026;30(10):459; **PMID 42771210**, PMC13597538, DOI 10.1007/s00784-026-07142-w, CC BY). The guideline contains "A total of 41 evidence- and consensus-based recommendations" (33 evidence-based, 80.5%; 8 consensus-based, 19.5%) across six rare dental disorders, of which DI is one.

### German S3 guideline recommendations for DI (verbatim, Table 3, Recs 5–12)

**Cross-cutting (all rare dental disorders):**
- **Rec 1** (expert consensus; **Strong**): diagnosis and lifelong care "should be carried out with interdisciplinary and, if necessary, interprofessional involvement and should be started at an early stage."
- **Rec 3** (expert consensus; **Strong**): "lifelong, risk-oriented and intensive preventive care."

**Primary and mixed dentition:**
- **Rec 5** (Very low; **Strong**): "Direct restorations and prefabricated stainless steel crowns should be used in the primary and mixed dentition to avoid DI-associated loss of dental hard tissues, to compensate for it, and/or to restore the occlusal vertical dimension."
- **Rec 6** (Very low; **Strong**): for reduced occlusal vertical dimension, rehabilitate "with prefabricated stainless steel crowns on the primary molars and with either prefabricated stainless steel crowns or individually fabricated indirect single-tooth restorations on first permanent molars."
- **Rec 7** (Very low; **Moderate**): after primary tooth extraction, "space-maintaining and/or interim prosthetic measures should be undertaken."

**Early permanent dentition:**
- **Rec 8** (Very low; **Strong**): direct restorations and individually fabricated indirect single-tooth crowns, which "form part of a long-term care strategy."
- **Rec 9** (Very low; **Strong**): "The definitive treatment should be implemented starting with the early permanent dentition using the full-mouth rehabilitation approach."

**Adult permanent dentition:**
- **Rec 10** (Very low; **Strong**): indirect single-tooth crowns on posterior teeth to prevent progressive loss, stabilise or restore vertical dimension, and "ensure the longevity of anterior restorations."
- **Rec 11** (Very low; **Strong**): direct restorations and indirect single-tooth crowns on anterior teeth.
- **Rec 12** (Very low; **Strong**): "Fixed, implant-supported or removable prosthetic restorations" to compensate for or prevent tooth loss and restore occlusion and masticatory function.

**Notably not covered for DI in the guideline text retrieved:** specific fluoride regimens, endodontic protocols, extraction criteria beyond Rec 7, orthodontics, and overdentures as a named option (Rec 12's "removable prosthetic restorations" is the nearest match).

**DI vs amelogenesis imperfecta — a substantive management difference:** the guideline places AI anterior indirect restorations already in the **mixed** dentition (AI Rec 16), whereas DI anterior indirect/direct restorations sit in the **adult** dentition (DI Rec 11). AI evidence ranges Low to Moderate; **DI is Very low throughout**. AI Rec 13 includes "pain relief" as a goal; DI Rec 5 does not — consistent with Barron's observation that DI patients "rarely complain of sensitivity."

### Other treatment literature

- **Barron 2008 (abstract, verbatim):** treatment "involves removal of sources of infection or pain," improves aesthetics, and protects posterior teeth from wear; it "usually continues into adulthood" and includes "crowns, over-dentures and dental implants."
- **Chu KY, Prakash R, Wang SK, Simmer JP, Wright JT, Hu JC.** "Inherited dentin defects with comorbidities." *J Am Dent Assoc* 2026;157(7):773–786.e1. **PMID 42409477.** "Timely recognition and multidisciplinary management are crucial." (Abstract-level only; full text not retrieved.)
- **Lee K, Kramer K, Foster BL, Meyer BD.** "Dental manifestations of rare skeletal disorders: Diagnosis and treatment for the oral health care provider." *J Am Dent Assoc*, **PMID 42390399** (retrieved record truncated).
- **AAPD:** the retrieved AAPD-hosted documents support stainless steel crowns for DI and discuss overdenture candidacy, but the files retrieved were draft/unformatted versions (one bearing the disclaimer "this draft does not constitute an official AAPD health oral policy or clinical guideline until approval by the General Assembly"). **The final approved AAPD text was not retrieved; its exact wording and grading should be confirmed at aapd.org before citation.**
- **Case-level modalities:** indirect composite restorations in an adolescent, concluding they "can be a valuable tool for improving occlusion, esthetics and function" (**PMID 30206577**); CAD/CAM nanoceramic resin crowns in a 12-year-old (*J Clin Pediatr Dent* 2024, 10.22514/jocpd.2024.047); composite veneers plus sealants in a case followed from age 1.5 over 2020–2025 (**PMID 42029463**); implant-supported overdenture chosen over a fixed prosthesis for ridge resorption in one of three DI patients. A JOCPD scoping review of DI type II management in children (literature 1986–2017) lists stainless steel crowns, pedoform/composite strip crowns and low-fusion metal-ceramic restorations — **its PDF could not be text-extracted in this session**, so I cannot report its study count or outcomes.
- **Durability signal:** one case series found that some anterior composite restorations "chipped away and needed replacement within six months."

### Implant outcomes — DI-specific data do not exist

**No DI-specific implant survival data were found.** The nearest quantitative evidence is a systematic review in **osteogenesis imperfecta** (a different disease): across 23 OI patients, "only seven implants were lost, giving a survival rate of 94.0% (109 implants)," with the caveat that "the literature is still sparse and long-term outcomes are still unpredictable" (PMC8835393). **Do not transfer this figure to isolated DI.**

### Pharmacotherapy, advanced therapeutics, pharmacogenomics

- **Pharmacotherapy:** none disease-modifying. Management is restorative/prosthetic plus topical preventive agents (fluoride) as part of the guideline's general "lifelong, risk-oriented and intensive preventive care." No systemic drug, drug class or mechanism of action applies.
- **Pharmacogenomics:** not applicable. No PharmGKB/CPIC entry relevant to DSPP.
- **Gene therapy, cell therapy, RNA therapeutics, targeted therapy, immunotherapy:** **none exist, none in trials.** The dominant-negative mechanism in principle makes allele-specific knockdown (ASO/siRNA) a conceptually attractive target — the mutant allele's toxicity, not the WT allele's absence, drives disease — but **no such programme was found in any retrieved source.** This is an inference about druggability, not a reported development.
- **Experimental/regenerative:** a regenerative endodontic case in DI-induced apical periodontitis (PMC10787646) and stem cells from human exfoliated deciduous teeth (SHED) characterised from a DGI-II family (Gao 2025, **PMID 40197225**) represent early research directions, not therapies.
- **Clinical trials:** the only DI trial identified is observational — **NCT04927962** (COHIP/bullying/dental anxiety, completed 2024). **No interventional trial for DI was identified.**

### Suggested NCIT clinical-intervention terms (verified via OLS4)

- **NCIT:C60718** Dental Restoration
- **NCIT:C60719** Permanent Dental Restoration
- **NCIT:C60720** Temporary Dental Restoration
- **NCIT:C66855** Full Crown
- **NCIT:C66859** Partial Crown
- **NCIT:C62565** Restorative Material (syn. Dental Restorative Material)
- **NCIT:C52586** Resin-Based Composite
- **NCIT:C52585** Resin Modified Glass Ionomer Liner
- **NCIT:C52583** Amalgam

*A query for "dental crown procedure" in NCIT returned numFound 0; NCIT:C66855 "Full Crown" is the closest verified match. I did not locate verified NCIT terms for "stainless steel crown," "overdenture" or "dental implant placement" in this session — these should be looked up before curation rather than guessed.*

---

## 13. Prevention

### Primary prevention

**Not possible.** The disease is monogenic, dominant and congenital. The only primary-prevention lever is **reproductive** — informed reproductive decision-making after genetic counselling, with prenatal diagnosis or PGT-M theoretically available once the familial variant is known (see §10; no retrieved source documents either being used for DSPP). There is no vaccination, no modifiable risk factor, no public-health or environmental intervention.

### Secondary prevention (early detection and early intervention)

This is where essentially all preventive value lies.

- **Early diagnosis at eruption of the primary dentition**, enabling protective restoration before structural loss — German S3 Rec 1: lifelong care "should be started at an early stage" (expert consensus, **Strong**).
- **Cascade clinical examination of first-degree relatives** of an affected individual — straightforward given near-complete penetrance and a visually obvious phenotype.
- **Periodic radiographic monitoring** for periapical pathology, including in asymptomatic, non-carious teeth. Petrova et al. 2026 found **asymptomatic** periapical pathology and root resorption in a child followed from 1.5 years, and concluded in favour of early diagnosis, regular radiographic monitoring and risk-based planning (**PMID 42029463**).
- **No population screening programme exists or is warranted.**

### Tertiary prevention (preventing complications in affected individuals)

- German S3 **Rec 3** (expert consensus, **Strong**): "lifelong, risk-oriented and intensive preventive care" — per the guideline's narrative this comprises sugar counselling, oral hygiene, professional cleaning and fluoride (stated for rare dental disorders generally, not DI-specifically).
- Protective full coverage of posterior teeth as soon as they erupt (Rec 5, Rec 6) to prevent attrition and loss of occlusal vertical dimension.
- Space maintenance after primary tooth extraction to prevent mesialisation (Rec 7).
- Posterior stabilisation before anterior restoration, to "ensure the longevity of anterior restorations" (Rec 10).

### Genetic counselling

German S3: "If a genetically determined dental disease is confirmed, genetic counselling is indicated." Family history should be taken across several generations, and referral to a medical genetics clinic is "prudent." Counselling content should cover: autosomal dominant inheritance; near-complete penetrance but **highly variable expressivity, even within a family**; 50% offspring recurrence risk; the fact that a child's severity cannot be predicted from the parent's, nor reliably from the variant's position; the possibility of de novo occurrence; and — where a COL1A1/COL1A2 variant is found in an apparently isolated DI presentation — the need for skeletal evaluation. Hassib 2024 additionally discusses the religious, cultural and legal dimensions of counselling in differing jurisdictions (**PMID 38630328**).

### Immunization, behavioural interventions, public health, prophylaxis

**Not applicable.** No vaccine, no behavioural risk factor to modify, no public-health or environmental intervention, no prophylactic medication.

---

## 14. Other Species / Natural Disease

### Taxonomy and naturally occurring disease

**Dog (*Canis lupus familiaris*, NCBI:txid9615)** — the only non-human species with a curated naturally occurring entity.

- **Ontology:** **MONDO:7770372** "dentinogenesis imperfecta, dog," defined as "Dentinogenesis imperfecta that occurs in dog," cross-referenced to **OMIA:002792-9615** and with a cross-species exact match to **MONDO:0018849** (verified via OLS4).
- **Primary report:** Piekos KM, Freeman A, Fleming K, Bell C. "Dentinogenesis imperfecta in a 6-year-old male neutered Labrador retriever: Case report with atypical clinical presentation and treatment review." *Front Vet Sci* 2024;11:1473390; **PMID 39559541**, DOI 10.3389/fvets.2024.1473390 (published 4 Nov 2024). The dog had DI **without** concurrent osteogenesis imperfecta, was older than typical reported cases, showed a translucent, structurally abnormal permanent dentition by 10 months, and underwent staged full-mouth extractions which resolved the clinical signs. The authors note "it is unclear whether the human Shield classification applies directly to dogs."
- **Breed:** Labrador retriever in this report. **No VBO identifier was retrieved** — OMIA's exhaustive search was disabled at the time of this session (notice posted 4 Nov 2026), so I could not confirm breed-level predisposition or additional OMIA entries. No breed predisposition should be asserted from a single case.
- **Canine *DSPP* gene:** RGD lists a dog *DSPP* ortholog, RGD ID 12376540 (ortholog-table entry; NCBI Gene ID for dog DSPP was not retrieved). **The Piekos dog was not reported as genetically tested in the abstract material retrieved** — the causal link in dogs rests on phenotypic analogy plus the authors' citation of human DSPP genetics, not on a demonstrated canine *DSPP* variant.

### Orthologous genes (verified)

| Species | Gene | ID | Location |
|---|---|---|---|
| Human | DSPP | HGNC:3054 / Entrez 1834 / UniProt Q9NZW4 | 4q22.1 |
| Mouse | Dspp | **MGI:109172** / Entrez **666279** / Ensembl ENSMUSG00000053268 | Chr5:104,318,578–104,327,993 (GRCm39, + strand); 50.59 cM |
| Rat | Dspp | **RGD:2525** | Chr14p22; GRCr8 14:5,870,232–5,876,339 (− strand) |
| Dog | DSPP | RGD ortholog 12376540 | — |
| Others listed by RGD | chinchilla 9019199; bonobo 11940477; squirrel 12518008; pig 14209522; green monkey 18528396; naked mole-rat 18925654; black rat 626032507 | | |

**No zebrafish ZFIN ortholog appeared** in any retrieved record — consistent with DSPP being a mammalian SCPP-cluster innovation, though I did not retrieve a source stating that explicitly.

### Comparative biology and conservation

- Mouse and human DI phenotypes correspond closely at the tissue level (hypomineralised dentine, abnormal predentine, pulp-chamber changes, accelerated attrition — see §15), supporting conservation of the DSPP-dependent mineralisation mechanism across mammals.
- A review of secretory calcium-binding phosphoproteins in dental mineralisation provides the comparative framework: Chun YP, Foster BL, Liang T, Kawasaki K. "Functions of secretory calcium-binding phosphoproteins in dental mineralization." *J Bone Miner Res* 2025;40(8):909–930; **PMID 40318225**, PMC12308831, DOI 10.1093/jbmr/zjaf062.
- Rat *Dspp* carries ISO/ISS disease annotations mirroring the human ones: DOID:4154 dentinogenesis imperfecta (with OMIM:125490 | OMIM:125500), DOID:9004572 Shields type 3, DOID:0070707 dentin dysplasia type II, DOID:9003089 DFNA39 with DGI1 (RGD).

### Transmission

**Zero zoonotic potential; no cross-species transmission.** This is a germline monogenic disorder. Not applicable.

---

## 15. Model Organisms

### Mouse — the principal model system

**MGI:109172 (*Dspp*)** lists **17 alleles**: 7 endonuclease-mediated, 3 targeted, 4 transgenic, 1 chemically induced, 1 radiation induced, 1 spontaneous. MGI records **33 phenotypes from 4 alleles** and two human-disease model associations: **DOID:4154 dentinogenesis imperfecta** and **DOID:3388 periodontal disease**, both modelled by *Dspp*^tm1Kul homozygotes.

#### Model 1 — *Dspp* null (knockout): ***Dspp*^tm1Kul** (MGI:2653208, synonym "Dspp−")

- **Type:** targeted knockout, 129/Sv × C57BL/6 background (MGI J:84378); periodontal model on B6;129-*Dspp*^tm1Kul/Mmnc (J:241990).
- **Founding paper:** Sreenath T et al., "Dentin Sialophosphoprotein Knockout Mouse Teeth Display Widened Predentin Zone and Develop Defective Dentin Mineralization Similar to Human Dentinogenesis Imperfecta Type III." *J Biol Chem* 2003;278(27):24874–80; **PMID 12721295**.
- **Homozygous phenotype:** enlarged pulp chambers, widened predentine, hypomineralised dentine — described by later authors as matching **human DGI-III**. Associated MP terms reported via the Alliance phenotype API include MP:0002819 abnormal dental pulp cavity morphology, MP:0030451 abnormal dentin mineralization, MP:0002818 abnormal dentin morphology (PMID:12721295) *(these three came through an extraction summary rather than verbatim text and should be re-verified before import)*; verbatim-confirmed annotations include **MP:0004189** abnormal alveolar process morphology (PMID:22934831, Gibson MP 2013) and **MP:0011035** (PMID:16937369, Alvares K 2006).
- **Downstream matrix finding:** the proteoglycans **biglycan and decorin accumulate in the widened predentine**, with elevated decorin contributing to the predentine defect (PMC2683192).
- **Heterozygotes:** unaffected or minimally affected. Liang 2021: *Dspp* heterozygous knockout mice "show either no dentin phenotype, or mild dentin defects not evident until old age." PMC2758621 reports heterozygotes with no obvious abnormality.
- **Key limitation — and the most important modelling insight in this disease:** the null allele models *recessive* loss of function, **not** the human dominant mechanism. von Marschall 2012 use exactly this to argue that "loss of a single allele is recessive and that haploinsufficiency does not explain DD or DGI." **The knockout is therefore the wrong model for human DI pathogenesis**, though it is the right model for DSPP's normal role in mineralisation.

#### Model 2 — *Dspp*^P19L knock-in (5′ / signal-peptide class)

- Mouse equivalent of human **p.Pro17Leu** (c.50C>T). Generated by the Simmer/Hu group.
- **Heterozygotes are affected**, matching human dominant inheritance: "similar dental malformations were observed in both heterozygous and homozygous mice," with "minimal differences" between them (Liang 2021, **PMID 34667213**).
- **Dentine:** "*Dspp*^P19L dentin contained dentinal tubules but grew slowly and was softer and less mineralized than the wild-type." Nanohardness (GPa): WT 1.24; het 1.08; hom 1.04.
- **Enamel (class-specific):** "softer than normal" in incisors, reduced rod/interrod definition in molars, significant reduction in enamel volume in mandibular first molars. Nanohardness: WT 3.82; het 2.88; hom 2.94 GPa. Decussating enamel rods were evident in heterozygotes but only poorly defined in homozygotes.
- **Temporal evolution:** younger mice resembled **DGI-III** (enlarged pulp chambers), older mice **DGI-II** (smaller pulp chambers) — a direct in vivo demonstration that the Shields "types" can be stages of one process (Liang et al., *Front Physiol* 2021;12:724098).
- **Mechanism confirmed in vivo:** "Secretion of the mutant Dspp^P19L protein was impaired and it accumulated within the ER"; odontoblasts of both genotypes showed reduced DSPP expression.
- **Phenotype recapitulation:** **high** for 5′-class human disease, including dominance, dentine softening, accelerated attrition and the age-dependent pulp-chamber transition.

#### Model 3 — *Dspp*^−1fs frameshift knock-in (3′ / DPP-repeat class)

- CRISPR-generated single-nucleotide deletion **c.1365delG** plus an inserted FLAG tag (DYKDDDK) before the DPP N-terminus, producing 493 extraneous amino acids before a stop codon (Liang 2021, **PMID 34667213**). An MMRRC ID of 67179 was reported via extraction summary and is **unverified**.
- **Dentine:** "lacked dentinal tubules, contained cellular debris, and was significantly softer and thinner" than WT and P19L dentine. Nanohardness: het 0.84, hom 0.80 GPa (vs WT 1.24) — **the most severe dentine phenotype of the three models**.
- **Enamel:** **normal** (het 3.76, hom 3.78 GPa vs WT 3.82) — a clean dissociation from the P19L model, and direct evidence that the enamel defect is specific to the 5′ mutation class.
- **Attrition:** accelerated, "and sometimes crown failures"; whole-crown failures occurred only in −1fs mice. Alveolar bone recession in molars and incisors at 7 weeks.
- **Heterozygotes affected:** *Dspp*^+/−1fs incisors and molars showed translucent dentine and the same tubule loss as homozygotes.
- **mRNA:** reduced, "suggesting that the Dspp−1fs mRNA was selectively degraded or the cells expressing it deteriorated."
- A separate spontaneous allele, ***Dspp*^−DPP** (c.1380_1381insT), is mentioned as "being characterized but is not discussed further."

#### Model 4 — *Dspp*-DPP CRISPR mouse (domain-dissection)

Liang T, Smith CE, Hu Y, Zhang H, Zhang C, Simmer JP, Hu JC. "DSP and DPP are dispensable for initiation of dentin and enamel mineralization but critical for circumpulpal dentin mineralization." *Sci Rep* 2025;15:24913; **PMID 40640300**, PMC12246090. Localises DSPP's requirement to **circumpulpal** dentine rather than to mineralisation initiation.

#### Model 5 — *Col1a1-Trps1* transgenic (transcriptional repression)

"Transcriptional Repression of the *Dspp* Gene Leads to Dentinogenesis Imperfecta Phenotype in Col1a1-Trps1 Transgenic Mice" (PMC3399940). **Retrieved as a title only; full text not fetched — treat as a lead, not a verified finding.**

### In vitro and cellular systems

| System | Use | Source |
|---|---|---|
| **HEK293 / HEK293A** transient transfection | rER retention, EndoH sensitivity, PDI co-localisation, FLAG sandwich ELISA, furin inhibition, dose-dependent WT entrapment; hybrid OPN-DSPP and DMP1-DSPP constructs to test the IPV-like motif | von Marschall 2012, **PMID 22392858** |
| **HEK293T** transfection with GFP-tagged DSP (aa 1–382) | Secretion quantification; confocal with calnexin (ER) and GM130 (Golgi) | Lee 2013, **PMID 23509818** |
| **COS-7** with pSPL3 minigene | Splicing assay (showed p.P17L does not affect splicing) | Lee 2013 |
| **SHED** (stem cells from human exfoliated deciduous teeth) from a DGI-II family | Patient-derived cellular model | Gao 2025, **PMID 40197225**, PMC11978159 |

**No odontoblast-based, iPSC-derived or organoid model of DI was found.** von Marschall explicitly report no experiments in odontoblasts — this is a recognised limitation, since every mechanistic conclusion about rER entrapment rests on heterologous kidney-derived cell lines.

### Model limitations (aggregate)

1. The **knockout models loss of function, which is not the human disease mechanism** — the single most important caveat.
2. **No UPR/ER-stress markers have been measured** in any model; rER stress remains an inference.
3. **Ca²⁺-dependent aggregation** of mutant DPP is a model based on lanthanum-precipitation surrogate experiments, not a measured phenomenon in odontoblasts.
4. Mouse incisors grow continuously — a developmental difference from human teeth that complicates translation of attrition and wear findings.
5. **No model recapitulates the hearing loss** or allows the DFNA39 question to be resolved.
6. **No model addresses the psychosocial / QoL burden**, which is where much of the human disease impact sits.

### Resources

MGI (informatics.jax.org/marker/MGI:109172); Alliance of Genome Resources; RGD (rgd.mcw.edu, RGD:2525); OMIA (omia.org — **note: exhaustive search was disabled as of 4 Nov 2026, limiting veterinary curation**); IMSR/MMRRC for strain distribution (the specific MMRRC ID for the −1fs line could not be verified in this session).

---

## Evidence quality summary and explicit gaps

**Source classes used:** curated structured databases (HGNC, UniProt, MGI, RGD, HPO, Mondo/OLS4, MedGen, GARD, ClinicalTrials.gov); one evidence- and consensus-based clinical guideline (German S3, 2026); three systematic reviews (2025, 2026 ×2); primary experimental literature (cell transfection, knock-in mouse); clinical cohorts (Swedish registry n=44; French GenoDENT n=112); case reports and case series.

**Retrieval failures in this session — stated so the gaps are visible, not papered over:**

- **OMIM** returned HTTP 403 for all four entries; no OMIM allelic-variant table, no Brandywine mapping history, no OMIM reference lists were obtained.
- **Orphanet** (orpha.net) returned a bot-verification page; **no Orphanet prevalence class, ICD-10/ICD-11 codes, or Orphanet clinical sections were obtained.**
- **gnomAD** constraint metrics for DSPP were not obtained.
- **NCBI Gene** and **GeneCards** were blocked (reCAPTCHA / 403).
- **ClinVar** was reached only through a third-party aggregator (ClinVar Miner / GeneBe); counts should be re-derived from ClinVar directly.
- **Table 2 of de La Dure-Molla 2015** (the mutation table) did not render; its named mutations are absent from this report, though Barron 2008's Table 1 and Gilani 2025's Table 1 cover much of the same ground.
- The **JOCPD scoping review PDF** could not be text-extracted; its study count and outcome data are missing.
- The **Simmer 2022 Genes** full text was not retrieved; its content here derives from the PubMed record and indexing services and is labelled accordingly.
- **No HPO onset or frequency qualifiers** are populated for OMIM:125490 or OMIM:125500 — all frequency, onset and sex fields are blank in the HPO annotation API. Frequency figures in §3 come from the systematic-review literature, not from HPO.
- Several items within the fetched reviews came through extraction summaries rather than verbatim page text; these are individually flagged in-line and should be re-verified against the primary source before being entered as curated assertions.

**Highest-confidence assertions for KB entry:** DSPP as sole causal gene for isolated DI; autosomal dominant with near-complete penetrance and variable expressivity; dominant-negative rER-retention mechanism with explicit rejection of haploinsufficiency; exon 5 as the dominant mutational location with frameshift as the dominant variant type; the requirement for long-read sequencing of the DPP repeat; the Swedish population-based prevalence of ≈1/45,455; and the German S3 management recommendations with their "Very low" evidence rating stated alongside them.

**Addendum to the report — Simmer et al. 2022 full text now retrieved**

A full-text fetch that was still pending when I delivered the report has returned. It adds verified detail and changes two things I had flagged as uncertain. Appending rather than reissuing the whole report:

---

### Corrected/completed citation (§1, §4, §10)

**Simmer JP, Zhang H, Moon SJH, Donnelly LA-J, Lee Y-L, Seymen F, Koruyucu M, Chan H-C, Lee KY, Wu S, Hsiang C-L, Tsai ATP, Slayton RL, Morrow M, Wang S-K, Shields ED, Hu JC-C.** "The Modified Shields Classification and 12 Families with Defined DSPP Mutations." *Genes (Basel)* 2022;13(5):858. **PMID 35627243, PMCID PMC9141616**, DOI 10.3390/genes13050858, epub 12 May 2022, CC BY 4.0. WES data: dbGaP phs001491.v2.p1. (My report cited this from the PubMed record only; PMCID and author list are now verified.)

Abstract, verbatim: the proposal is that "patients identified with 5′-DSPP defects be diagnosed as DGI-III, while those with 3′-DSPP defects be diagnosed as DGI-II," made "based upon the causative mutation rather than phenotypic severity," and justified by "distinct differences in the cell pathology observed between knockin mice with 5′-Dspp or 3′-Dspp mutations."

### The 12 families and their variants (NM_014208.3) — add to the §4 variant tables

| Family | Variant | Protein | Group |
|---|---|---|---|
| 1 | c.50C>T | p.(Pro17Leu) | 5′ |
| 2 | c.52-1G>A | intron 2 splice acceptor | 5′ |
| 3 | c.53T>C | p.(Val18Ala) | 5′, **novel** |
| 4 | c.135+3A>G | intron 3 | 5′ |
| 5 | c.1915_1918delAAGT | p.(Lys639Glnfs*674) | 3′ |
| 6 | c.1918_1921delTCAG | p.(Ser640Thrfs*673) | 3′ |
| 7 | c.2134delA | p.(Ser712Alafs*602) | 3′ |
| 8 & 9 | c.2525delG | p.(Ser842Thrfs*472) | 3′ |
| 10 | c.3135delC | p.(Ser1045Argfs*269) | 3′ |
| 11 | c.3461delG | p.(Ser1154Metfs*160) | 3′, **novel** |
| 12 | c.3700delA | p.(Ser1234Alafs*80) | 3′, **novel** |

This supplies full protein-level nomenclature for c.2134delA, c.2525delG, c.3135delC and c.1918_1921delTCAG, which I had listed from Gilani/Barron without complete annotation.

**Brandywine variant confirmed:** c.49C>T, p.(Pro17Ser), Table 1 entry #4 — consistent with Lee 2013. The paper's Discussion states the earlier attribution of the Brandywine phenotype to C-terminal indels was wrong.

### Mechanism — this changes §6, step 5A/3B

I wrote that no ER-stress/UPR measurements existed in any retrieved source. Simmer et al. report a dissociation between the two mutation classes: the 5′ knockin causes **rER retention of DSPP**, while the 3′ frameshift knockin causes **cell toxicity with autophagy and little ER stress**, and also little enamel attrition. If that holds, the two branches of the causal chain converge on defective dentine but diverge in cell pathology — autophagic/toxic for 3′, secretory-retention for 5′ — and the "inferred UPR activation" step I assigned to both belongs only to the 5′ branch.

**Caveat, stated plainly:** this came from the unread middle section of the paper (Results/Discussion, ~100,000 characters not read verbatim); only the abstract, introduction and references were read directly. Treat the autophagy/low-ER-stress finding as a **lead requiring verification against the primary text** before entering it as a curated mechanistic assertion. The 5′ rER-retention half is independently confirmed by von Marschall 2012 and Lee 2013 and stands as reported.

Verbatim from the introduction, both classes: 5′ mutations lie "adjacent to the signal peptide cleavage site that likely interferes with signal peptide cleavage" and/or cause mutant DSPP "to be retained in the rough endoplasmic reticulum (rER)"; 3′ mutations are "−1 frameshift mutations in the last coding exon (#5)" that "translate beyond the native DSPP translation termination codon."

### Classification — a genuine disagreement I under-stated in §1

Simmer et al. **reject abandoning the Shields classification**, which puts them in direct opposition to de La Dure-Molla et al. 2015 ("We propose that all DSPP diseases are called exclusively 'Dentinogenesis Imperfecta (DI)'"). Under the Simmer rule, DD-II gets no separate category; DD-II-type mutations are said to cluster in the most 5′ portion of the repeat region, and Family 10 is described as borderline DD-II/DGI-II. The rule also carries an exception: dominant 5′ mutations are classed DGI-III **except those in the signal-peptide coding segment**, and two variants — including c.16T>G p.(Tyr6Asp) — are said not to fit cleanly into either group.

Verbatim from the introduction: "DD-II, DGI-II, and DGI-III are all autosomal dominant conditions caused by single allele mutations" in DSPP; and the frameshift position in exon 5 "correlates only roughly" with DD-II versus DGI-II — the authors' own hedge on the genotype–phenotype rule, which supports the caution I recorded in §4.

So the curation choice at MONDO:0018849 is now a **three-way** call, not two-way: Shields phenotypic types (MONDO/OMIM status quo) vs. one graded entity (de La Dure-Molla 2015) vs. retained Shields labels reassigned by genotype (Simmer 2022). All three are in current use.

### Diagnostic workflow (§10) — now verbatim

"We propose genetic analysis start with WES analysis of proband DNA" to identify COL1A1/COL1A2 variants, 5′-DSPP mutations, and "3′-DSPP frameshifts near the margins of the DSPP repeat region," with "SMRT sequencing when the disease-causing mutation is not identified." Supplementary detail (summary-level, unverified): SMRT reads are aligned to the repeat using 16 known indels listed in Supplementary Table S1; each patient yields two haplotype sequences because of allelic length variation; in Family 9 Sanger sequencing failed because indel 5 lay close to both the mutation and repeat sequence. This independently corroborates the Caravello 2026 long-read recommendation from a different group four years earlier.

### Minor

The paper's Results say "eleven families" while the study describes twelve — an internal inconsistency in the source, noted so it isn't propagated. The IPV motif does not appear in the portions read verbatim; I cannot confirm whether the paper discusses it.

Everything else in the delivered report stands as written.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 117 |
| Resolved | 117 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 12 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 117 |
| On topic | 60 |
| Off topic | 5 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22934831` *(abstract only)*: "abnormal alveolar process morphology"
  - Text part not found as substring: 'abnormal alveolar process morphology' (note: only abstract available for PMID:22934831, full text may contain this excerpt)
- `PMID:16937369` *(abstract only)*: "abnormal branching involved in alveolar duct morphogenesis"
  - closest text in source: "Inclusion of anti-DPP antibodies in organ culture of metanephroi, harvested from E13.5 wild-type mice, likewise resulted in altered ureteric bud morphogenesis, suggesting a role for DPP in epithelial-mesenchymal interactions in meristic tissues during embryonic development."
- `PMID:22934831` *(abstract only)*: "abnormal cementum morphology"
  - Text part not found as substring: 'abnormal cementum morphology' (note: only abstract available for PMID:22934831, full text may contain this excerpt)
- `PMID:12721295` *(abstract only)*: "abnormal dentin morphology"
  - Text part not found as substring: 'abnormal dentin morphology' (note: only abstract available for PMID:12721295, full text may contain this excerpt)
- `PMID:28288297` *(abstract only)*: "Beltrame AP, Rosa MM, Noschang RA, Almeida IC"
  - Text part not found as substring: 'Beltrame AP, Rosa MM, Noschang RA, Almeida IC' (note: only abstract available for PMID:28288297, full text may contain this excerpt)
- `PMID:19021896` *(abstract only)*: "increasingly out of date as it does not account for the molecular aetiologies of these defects"
  - closest text in source: "Clinically, the teeth are discoloured and show structural defects such as bulbous crowns and small pulp chambers radiographically"
- `DOI:10.1186/1750-1172-3-31` *(abstract only)*: "increasingly out of date as it does not account for the molecular aetiologies of these defects"
  - closest text in source: "Clinically, the teeth are discoloured and show structural defects such as bulbous crowns and small pulp chambers radiographically"
- `PMC:PMC2600777` *(abstract only)*: "increasingly out of date as it does not account for the molecular aetiologies of these defects"
  - closest text in source: "Clinically, the teeth are discoloured and show structural defects such as bulbous crowns and small pulp chambers radiographically"
- `PMID:34667213` *(abstract only)*: "show either no dentin phenotype, or mild dentin defects not evident until old age"
  - closest text in source: "DSPP defects cause an overlapping spectrum of phenotypes classified as dentin dysplasia type II and dentinogenesis imperfecta types II and III"
- `PMC:PMC8526674` *(abstract only)*: "show either no dentin phenotype, or mild dentin defects not evident until old age"
  - closest text in source: "DSPP defects cause an overlapping spectrum of phenotypes classified as dentin dysplasia type II and dentinogenesis imperfecta types II and III"
- `PMID:23509818` *(abstract only)*: "The mutation did not influence pre-mRNA splicing but caused ER retention and defective protein secretion"
  - closest text in source: "Exons and exon-intron boundaries of DSPP gene were sequenced, and the effects of the identified mutation on the pre-mRNA splicing and protein secretion were investigated"
- `PMC:PMC8835393` *(abstract only)*: "the literature is still sparse and long-term outcomes are still unpredictable"
  - Text part not found as substring: 'the literature is still sparse and long-term outcomes are still unpredictable' (note: only abstract available for PMID:35162583, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:24281365` (1 mention) - Retrieving Y chromosomal haplogroup trees using GWAS data.
  - shared terms: none
- `PMID:19125428` (1 mention) - Elements of morphology: standard terminology for the lips, mouth, and oral region.
  - shared terms: phenotype
- `PMID:39347039` (1 mention) - The in vitro efficacy of advanced platelet-rich fibrin plus versus injectable platelet-rich fibrin on the proliferation, migration, and differentiation of stem cells from apical papilla.
  - shared terms: dentin
- `PMID:42266834` (1 mention) - Enamel Matrix Derivative in Dental Pulp Regeneration: Biological Basis, Mechanistic Insights, and Translational Considerations.
  - shared terms: dental
- `PMC:PMC4350590` (2 mentions) - Retrieving Y chromosomal haplogroup trees using GWAS data.
  - shared terms: none

Weighed against this report's own most characteristic terms: `dspp`, `imperfecta`, `disease`, `verbatim`, `dentinogenesis`, `type`, `dentin`, `variant`, `teeth`, `mutation`, `dental`, `read`, `dgi-ii`, `primary`, `phenotype`, `barron`, `loss`, `gene`, `dgi`, `abstract`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1038/ejhg.2014.159`: "radicular dentin dysplasia"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00784-024-05568-8`: "no significant difference in OHRQoL between children and adolescents, nor associated with the disease severity or the presence of DI"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 122 |
| Resolved | 96 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 0 |
| Unverifiable | 23 |
| Terms whose name was checked | 21 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018849` (16 mentions) - the report calls it "ClinGen and MONDO links", "human dentinogenesis imperfecta", "dentinogenesis imperfecta**, the *non-syndromic"; MONDO calls it **dentinogenesis imperfecta**
- `HP:0000703` (10 mentions) - the report calls it "HPO (as a phenotype term)"; HP calls it **Dentinogenesis imperfecta**
- `MONDO:0007442` (6 mentions) - the report calls it "DGI type 3"; MONDO calls it **dentinogenesis imperfecta type 3**
- `HP:0033780` (3 mentions) - the report calls it "Bulbous crowns with marked cervical constriction"; HP calls it **Bulbous tooth**
- `DOID:4154` (6 mentions) - the report calls it "Disease Ontology"; DOID calls it **dentinogenesis imperfecta**
- `HP:0030756` (3 mentions) - the report calls it "Congenital erythropoietic porphyria** — erythrodontia"; HP calls it **Erythrodontia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `DOID:9003089` (2 mentions) - DOID does not contain this term
- `DOID:9004572` (2 mentions) - DOID does not contain this term
- `DOID:9007364` (1 mention) - DOID does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0007441` (7 mentions) - the report calls it "DGI type 2"; MONDO calls it **dentinogenesis imperfecta type 2**, and lists "DGI-2" among its other names
- `HP:0000006` (3 mentions) - the report calls it "Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `HP:0006286` (2 mentions) - the report calls it "Yellow-brown tooth discolouration"; HP calls it **Yellow-brown discoloration of the teeth**, and lists "Yellow-brown discoloured teeth" among its other names
- `HP:0000694` (5 mentions) - the report calls it "shell teeth"; HP calls it **Odontodysplasia**, and lists "Shell teeth" among its other names
- `HP:0000700` (5 mentions) - the report calls it "Periapical radiolucencies in non-carious teeth"; HP calls it **Periapical bone loss**, and lists "Periapical radiolucencies" among its other names
- `HP:0006336` (3 mentions) - the report calls it "Short, thick roots"; HP calls it **Short dental root**, and lists "Short tooth roots" among its other names
- `HP:0033784` (2 mentions) - the report calls it "Dentin dysplasia (umbrella)"; HP calls it **Dentin dysplasia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0018849` - called "ClinGen and MONDO links", "human dentinogenesis imperfecta", "dentinogenesis imperfecta**, the *non-syndromic"

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MEDGEN:8313` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`, `NCBIGene`, `MIM`, `RGD`, `Chr5`, `NCBI_Gene`, `OMIA`.