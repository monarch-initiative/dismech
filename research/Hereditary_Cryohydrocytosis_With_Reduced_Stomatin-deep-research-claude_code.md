---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-18T15:00:27.623600'
end_time: '2026-11-18T15:20:41.998396'
duration_seconds: 1214.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hereditary Cryohydrocytosis With Reduced Stomatin
  mondo_id: MONDO:0012143
  category: Mendelian
  causal_genes: SLC2A1
  omim_id: OMIM:608885
  synonyms: ChC type 2; hereditary cryohydrocytosis type 2; sdCHC; stomatin-deficient
    cryohydrocytosis
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
  web_search_requests: 7
  num_turns: 35
  total_cost_usd: 5.0641090800000015
  session_id: daf15eb3-dc3a-4dc2-adb5-de79a0a00012
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 162
  retrieval_calls: 160
  assistant_text_blocks: 50
citation_count: 89
reference_validation:
  total_references: 70
  verified: 69
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.014
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 69
  on_topic: 21
  off_topic: 1
  off_topic_references:
  - PMC:PMC370348
  unresolved_references:
  - DOI:10.1002/ajh.70274
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 180
  verified: 154
  not_found: 1
  obsolete: 1
  unverifiable: 24
  confabulation_rate: 0.006
  labels_checked: 39
  labels_matching: 24
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0011972
    reported_labels:
    - label not visible
    - Hypoglycorrhachia
    ontology_label: Hypoglycorrhachia
  - term_id: HP:0040282
    reported_labels:
    - Frequent
    - label not visible
    ontology_label: Frequent
  - term_id: HP:0040283
    reported_labels:
    - Occasional
    - label cut off
    ontology_label: Occasional
  - term_id: GO:0015758
    reported_labels:
    - Glucose transmembrane transport
    ontology_label: GO_0015758
  - term_id: UBERON:0002420
    reported_labels:
    - exertion-induced energy deficit in the basal ganglia
    ontology_label: basal ganglion
  - term_id: UBERON:0002106
    reported_labels:
    - splenomegaly, hypersplenic sequestration; 10 cm on ultrasound in Lee et al
    ontology_label: spleen
  - term_id: UBERON:0002107
    reported_labels:
    - hepatomegaly, elevated GGT, hepatic dysfunction, cholestatic hepatitis
    ontology_label: liver
  - term_id: GO:0042470
    reported_labels:
    - melanosome
    - UniProt also records GLUT1 at the **melanosome
    ontology_label: melanosome
  labels_variant: 7
  unresolved_terms:
  - RO:0004003
  obsolete_terms:
  - term_id: GO:0015758
    ontology_label: GO_0015758
    replaced_by: GO:1904659
  unresolvable_prefixes:
  - OMIM
  - NCBIGene
  - MIM
  - PubMed
  - EXT_ID
  - MGI
  - ORPHA
  - GARD
  - Orphanet
  - UMLS
  service_unreachable: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Cryohydrocytosis With Reduced Stomatin
- **MONDO ID:** MONDO:0012143 (if available)
- **Causal gene(s):** SLC2A1
- **OMIM:** OMIM:608885
- **Synonyms:** ChC type 2; hereditary cryohydrocytosis type 2; sdCHC; stomatin-deficient cryohydrocytosis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hereditary Cryohydrocytosis With Reduced Stomatin** covering all of the
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

I'll research this disease now, starting with the core identifiers and primary literature.

The primary URL returned HTTP 403. You named a fallback on a different host, so I'll try that one.

The NCBI URL redirects back to omim.org, the host that already returned 403, so I won't follow that. I'll try the third fallback you named.

The PubMed page returned a cookie interstitial instead of the article, and ScienceDirect returned 403. You gave an ASH Publications fallback for the second article, so I'll try that one.

I could not retrieve the abstract, the bibliographic details, or the full text of this paper. All three sources failed:

1. **PubMed** (https://pubmed.ncbi.nlm.nih.gov/21791420/): HTTP 203 (Non-Authoritative Information). The body was a cookie-enablement interstitial ("Cookies must be enabled ... reload this page to continue"), not the article. I did not retry or try variants, since the response is not a standard error and retrying would be a workaround.
2. **ScienceDirect** (https://www.sciencedirect.com/science/article/pii/S0006497120461800): HTTP 403 Forbidden. Permanent for this host, so retrying would fail the same way.
3. **ASH Publications** (https://ashpublications.org/blood/article/118/19/5267/29161): HTTP 403 Forbidden, also permanent. This is the fallback you named.

Because of these, I have no abstract text, PMID confirmation, DOI, author list, or mutation, clinical, Xenopus, stomatin, mechanism, brain, or treatment content to report. Nothing from the paper is in this report beyond the citation you supplied.

Options to get the content:
- **PMC version:** send me the PMC ID (e.g., PMCxxxxxxx) and I will fetch it. I did not guess one, since a constructed ID could point to the wrong article.
- **Authenticated access:** the publisher and PubMed pages seem to require a login or cookies. An authenticated tool or a browser session you control could retrieve the pages.
- **Paste the text:** if you have the abstract or full text open, paste it here and I can extract the mutations, cohort details, and other items you listed.

PubMed blocked that fetch; I'll pull abstracts directly from NCBI E-utilities instead.

The page was cut at 39,897 of 165,125 characters, and the rest was only summarized. The fetch note gives an offset for the final section, so I'll read that tail.

I could not extract the paper's text. The fetch returned the PDF's raw binary, and the extraction step found no readable article text, so I have no abstract, case description, treatment, or discussion for this paper.

**What I could read (PDF metadata only):**
- DOI: 10.1002/epd2.20039 (from the embedded XMP and Crossref metadata)
- Version: "VoR" (version of record)
- Crossmark major version date: 2023-04-27
- The journal name, authors, volume, pages, and PMID do not appear in the readable portion. I have not inferred them.

**What I could not read:**
- Citation details beyond the DOI and date, including authors, journal, volume, issue, and pages
- Abstract
- Case details: age, sex, SLC2A1 variant, clinical features, potassium values, temperature dependence, red cell findings, and ektacytometry
- Diagnostic method
- Treatment, including whether a ketogenic diet was used
- Mechanism discussion and any reference to other sdCHC/CHC cases

The fetched content stopped at about 40,000 of roughly 1.4 million characters. The rest was not read. Re-fetching the same URL would return the same result, so I did not retry.

**Options for getting the content:**
1. Paste the abstract or full text here, and I will extract the details you asked for.
2. The PDF was saved to a local file by the harness. A tool that extracts PDF text, such as `pdftotext`, would likely read it.
3. The DOI above should lead to the publisher's version. I did not fetch it because it was not a URL you gave me.

I could not get the full OMIM entry verbatim. The official site blocked access, and the mirror I could read was truncated, so several sections you asked for are missing. The 125-character limit on quoting non-preapproved sources also rules out a verbatim dump, so most of what follows is paraphrased.

**Access attempts**
- `https://omim.org/entry/608885`: HTTP 403 Forbidden. Retrying the same URL would fail the same way.
- `https://www.ncbi.nlm.nih.gov/omim/608885`: 303 redirect to `http://omim.org/entry/608885`. I did not follow it, since it is the host that already returned 403.
- `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/608885`: HTTP 200, a third-party text mirror of the OMIM HTML page. It was 165,125 characters. I read the first 39,897 and the last 25,228. The middle 100,000 characters were only summarized by the tool, and I could not verify that summary, so I have left it out.

**What I could verify**
- **Title:** Stomatin-deficient cryohydrocytosis with neurologic defects (SDCHCN), MIM 608885.
- **Phenotype-gene table:** key 3 (the header tooltip reads "molecular basis known"), gene SLC2A1, MIM 138140. Chromosome location and the inheritance column were in the cut-off part, so I did not confirm them.
- **Description:** SDCHCN is an autosomal dominant disorder with delayed psychomotor development, seizures, cataracts and pseudohyperkalemia from red cell membrane defects. It combines the neurologic features of GLUT1 deficiency syndrome 1 (606777) with hemolytic anemia and stomatocytosis from an erythrocyte cation leak. The entry cross-references 194380 for red cell stomatocyte disorders.
- **Clinical features (cited as Fricke et al., 2004; Lande et al., 1982; Bawazir et al., 2012):**
  - Fricke et al. (2004) described two stomatin-deficient patients, neither from a consanguineous family. Both had seizures, intellectual disability, cataracts and hepatosplenomegaly. One of them had been reported earlier by Lande et al. (1982).
  - The first patient was a 40-year-old French man with cerebellar ataxia, communicating hydrocephalus treated with ventriculoperitoneal shunting, a congenital zonular cataract, chronic jaundice, and three severe hemolytic crises.
  - The second was a 32-year-old Irish woman with spastic paraplegia, "blueberry muffin" skin spots, short stature below the 3rd centile, and lifelong hemolysis.
  - Bawazir et al. (2012) described a neonate with conjugated hyperbilirubinemia at 22 hours, later hypertonia, seizures, splenomegaly, microcephaly, nystagmus, cataracts, periventricular calcifications, thalamic atrophy, global white matter loss, and delayed myelination. Lumbar puncture showed hypoglycorrhachia. A ketogenic diet gave some clinical improvement.
- **Inheritance:** The SLC2A1 mutations in the patients reported by Flatt et al. (2011) and Bawazir et al. (2012) arose de novo.
- **Molecular genetics:**
  - Flatt et al. (2011) found two different heterozygous SLC2A1 mutations, 138140.0023 and 138140.0024, in two unrelated patients. In one family the parents did not carry the mutation. In the other it was presumed de novo.
  - Expressed in Xenopus oocytes, the mutant proteins did not transport glucose and leaked cations.
  - Bawazir et al. (2012) found a de novo heterozygous mutation, 138140.0024, in an infant. GLUT1 was expressed normally at the red cell membrane. The same mutation was found in one patient from Flatt et al. (2011).
  - The amino acid changes were not in the portion I read, so the full variant list is unconfirmed.
- **References (as listed in the entry):**
  - Bawazir, W. M., et al. (2012). J. Clin. Endocrinol. Metab. 97: E987-E993. PubMed 22492876.
  - Flatt, J. F., et al. (2011). Blood 118: 5267-5277. PubMed 21791420.
  - Fricke, B., et al. (2004). Brit. J. Haematol. 125: 796-803. PubMed 15180870.
  - Lande, W. M., et al. (1982). J. Clin. Invest. 70: 1273-1280. PubMed 7174793.
- **Contributors and dates:** Cassandra L. Kniffin (updated 12/16/2015); Ada Hamosh (updated 8/18/2005). Creation: Victor A. McKusick, 8/30/2004. Latest edit history entry: carol, 08/29/2024.
- **External IDs:** ORPHA 168577 (in the page's ICD+ tooltip and the OrphaNet link).

**Not obtained**
- The mapping section.
- The complete list of allelic variants, including amino acid changes and numbering beyond .0023 and .0024.
- The clinical synopsis. The mirror's clinical synopsis link points to `/clinicalSynopsis/608885`, which I did not fetch.
- The see-also list.
- MedGen and GARD IDs.

The summary of the unread middle section listed a clinical synopsis, see-also entries, and an alternative title, but I could not verify any of it, so I have not reported those items.

Final URL read: `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/608885` (offset 0 and offset 139897).

Excellent — the Furia 2023 paper gives a full literature table. Reading its reference list and fanning out to the other primary sources.

The HPO browser URL returned a 404, so I'm falling back to the ontology API URL you named. The Orphanet page returned a bot-check challenge instead of content.

## Source 1: NCBI MedGen (https://www.ncbi.nlm.nih.gov/medgen/332390), HTTP 200

- **Title:** Hereditary cryohydrocytosis with reduced stomatin (MedGen UID 332390; Concept ID C1837206). The page's own title line says "(SDCHCN)".
- **Definition (from OMIM):** Describes an autosomal dominant disorder with delayed psychomotor development, seizures, and cataracts. Quoted fragment: "is an autosomal dominant disorder characterized by delayed psychomotor development, seizures, cataracts". The definition also covers pseudohyperkalemia, GLUT1 deficiency features, and red cell cation leak. The remainder is paraphrased because of the quote limit for non-preapproved sources.
- **Synonyms:** "GLUT1 DEFICIENCY SYNDROME WITH PSEUDOHYPERKALEMIA AND HEMOLYSIS"; "Stomatin-deficient cryohydrocytosis with neurologic defects"
- **Mode of inheritance:** Autosomal dominant inheritance (MedGen UID 141047, C0443147, source Orphanet)
- **Cross-references:**
  - OMIM: 608885
  - MONDO: MONDO:0012143
  - Orphanet: ORPHA168577
  - UMLS CUI: C1837206
  - GARD: not listed as an ID on this page, only as a link to GARD 17036
  - SNOMED CT: not shown
  - Also linked: MalaCards, MedlinePlus, ClinicalTrials.gov, Coriell, ClinVar (~variants), and OMIM 138140 (the Gene Hierarchy entry for the parent, Hereditary stomatocytosis, MedGen 490161)
- **Associated gene:** SLC2A1 (NCBI Gene ID 6513; 1p34.2)
- **Clinical features and HPO IDs:** MedGen does not show HP IDs or frequency annotations for these features. It lists 30 features with MedGen UIDs. The HP IDs for matching terms appear in Source 3.
  - Short stature (MedGen 87607)
  - Growth delay (99124)
  - Hepatomegaly (42428)
  - Jaundice (43987)
  - Ataxia (13945)
  - Spasticity (7753)
  - Seizure (20693)
  - Hyperreflexia (57738)
  - Convulsive status epilepticus (137148)
  - Global developmental delay (107838)
  - Inability to walk (107860)
  - Hypoglycorrhachia (488927)
  - Absent speech (340737)
  - Intellectual disability (811461)
  - Delayed CNS myelination (867393)
  - Hemolytic anemia (1916)
  - Stomatocytosis (760280)
  - Hypertonia (10132)
  - Intracerebral periventricular calcifications (373287)
  - Microcephaly (1644158)
  - Splenomegaly (52469)
  - Hyperkalemia (5691)
  - Conjugated hyperbilirubinemia (82787)
  - Elevated gamma-glutamyltransferase level (1370086)
  - Fetal distress (5164)
  - Polyhydramnios (6936)
  - Nystagmus (45166)
  - Cataract (39462)
  - Nuclear cataract (140274)
- **Other:** The page lists 24 GTR tests and a hierarchy under Hereditary stomatocytosis. It does not show ICD-10/ICD-11 codes, prevalence, or age of onset.

## Source 2: GARD (https://rarediseases.info.nih.gov/diseases/17036/hereditary-cryohydrocytosis-with-reduced-stomatin), HTTP 200

- **Other names:** chc type 2; glut1 deficiency syndrome with pseudohyperkalemia and hemolysis; hereditary cryohydrocytosis type 2; sdchc; stomatin-deficient cryohydrocytosis; stomatin-deficient cryohydrocytosis with neurologic defects
- **Summary (GARD):** Paraphrased because of the quote limit. It describes a rare hemolytic anemia with neurologic features (psychomotor delay, seizures, variable movement disorders) and stomatocytosis, with cation-leaky erythrocytes, pseudohyperkalemia, hemolytic crises, hepatosplenomegaly, and cataracts. The page's own wording starts "A rare hemolytic anemia characterized by combination of neurologic features".
- **Symptoms and onset:** Symptoms "may start to appear as a Newborn and as an Infant" (Orphanet-sourced onset).
  - **Common** (no percentages given): Cataract; hepatosplenomegaly; global developmental delay; postnatal growth delay; intellectual disability; jaundice; seizure; spontaneous hemolytic crises; stomatocytosis
  - **Uncommon** (no percentages given): abnormality of movement; microcephaly; ataxia; broad neck; cerebral white matter hypoplasia; communicating hydrocephalus; decreased thalamic volume; delayed myelination; hypertonia; macrocephaly; intracerebral periventricular calcifications; nystagmus; large ears (macrotia); recurrent infections; brachydactyly; short neck; short stature; short thorax; spastic paraplegia; zonular cataract
  - The uncommon list is marked "Show more" on the page, so this may not be the complete list. The page does not give HP IDs.
- **Prevalence estimate:** None given on the page.
- **Inheritance:** Autosomal dominant. The page states that a person affected has a 50% chance of passing on the mutated gene to a biological child.
- **Genes:** SLC2A1
- **Cross-references:** MONDO:0012143; Orphanet 168577 (link); RARe-SOURCE. Categories: genetic, neurological, and blood diseases. No OMIM, UMLS, ICD, or SNOMED IDs are shown.
- **Last updated:** September 2026

## Source 3: HPO annotations for OMIM:608885

- **hpo.jax.org/browse/disease/OMIM:608885:** HTTP 404, so the page was not retrieved.
- **Fallback, https://ontology.jax.org/api/network/annotation/OMIM:608885:** HTTP 200, JSON.
  - **Disease:** "Stomatin-deficient cryohydrocytosis with neurologic defects", OMIM:608885, MONDO:0012143, gene NCBIGene:6513 (SLC2A1). The description field is empty.
  - **Annotated terms:** 32 in total. Format is HP ID, term, frequency, onset.
    - **Eye:**
      - HP:0100018 Nuclear cataract, frequency 1/1 (PMID:22492876)
      - HP:0000518 Cataract, no frequency (OMIM:608885)
      - HP:0000639 Nystagmus, frequency 1/1 (PMID:22492876)
    - **Prenatal and Birth:**
      - HP:0025116 Fetal distress, frequency 1/1 (PMID:22492876)
      - HP:0001561 Polyhydramnios, frequency 1/1 (PMID:22492876)
    - **Clinical course:**
      - HP:0003593 Infantile onset, no frequency (OMIM:608885)
      - HP:0003623 Neonatal onset, frequency 1/1 (PMID:22492876)
    - **Metabolism/Laboratory abnormality:**
      - HP:0002153 Hyperkalemia, frequency 1/1 (PMID:22492876)
      - HP:0002908 Conjugated hyperbilirubinemia, frequency 1/1 (PMID:22492876)
      - HP:0030948 Elevated gamma-glutamyltransferase level, frequency 1/1 (PMID:22492876)
      - HP:0011972 Hypoglycorrhachia, no frequency (OMIM:608885)
    - **Nervous System:**
      - HP:0001251 Ataxia, no frequency (OMIM:608885)
      - HP:0032660 Convulsive status epilepticus, frequency 1/1 (PMID:22492876)
      - HP:0001347 Hyperreflexia, no frequency (OMIM:608885)
      - HP:0002188 Delayed CNS myelination, frequency 1/1 (PMID:22492876)
      - HP:0001250 Seizure, frequency 1/1 (PMID:22492876)
      - HP:0007229 Intracerebral periventricular calcifications, frequency 1/1 (PMID:22492876)
      - HP:0002540 Inability to walk, no frequency (OMIM:608885)
      - HP:0001263 Global developmental delay, no frequency (OMIM:608885)
      - HP:0001344 Absent speech, no frequency (OMIM:608885)
      - HP:0001249 Intellectual disability, no frequency (OMIM:608885)
    - **Cardiovascular (as categorized by the API):**
      - HP:0001744 Splenomegaly, frequency 1/1 (PMID:22492876)
    - **Growth:**
      - HP:0004322 Short stature, no frequency (OMIM:608885)
      - HP:0001510 Growth delay, no frequency (OMIM:608885)
    - **Inheritance:**
      - HP:0000006 Autosomal dominant inheritance (PMID:22492876)
    - **Head and neck:**
      - HP:0000252 Microcephaly, no frequency (OMIM:608885)
    - **Digestive System:**
      - HP:0000952 Jaundice, frequency 1/1 (PMID:22492876)
      - HP:0002240 Hepatomegaly, no frequency (OMIM:608885)
    - **Musculature:**
      - HP:0001257 Spasticity, no frequency (OMIM:608885)
      - HP:0001276 Hypertonia, frequency 1/1 (PMID:22492876)
    - **Blood and blood-forming tissues:**
      - HP:0004446 Stomatocytosis, frequency 1/1 (PMID:22492876)
      - HP:0001878 Hemolytic anemia, frequency 1/1 (PMID:22492876)
  - **Onset:** The per-term onset field is empty for every term. Onset appears only through the two clinical-course terms above.
  - **Note:** "1/1" is the frequency code the API uses for terms reported in PMID:22492876. It is not a percentage. The API does not show ICD, Orphanet, or prevalence data.

## Source 4: Orphanet (https://www.orpha.net/en/disease/detail/3202)

- **Result:** Not retrieved. The server returned HTTP 200, but the body was an 83-character bot-verification challenge ("Vérification de la connexion...", protected by haphash) with no disease content.
- I did not try an Orphanet search for "cryohydrocytosis" or other orpha.net variants. The challenge would likely block them too, and retrying a rejection would be a workaround.
- So I cannot confirm whether ORPHA 3202 is the right disease, and I have no ORPHAcode definition, prevalence, clinical description, inheritance, age of onset, or ICD-10/ICD-11 codes from Orphanet.
- Orphanet ID cited by other sources: ORPHA168577 (per MedGen and GARD). I did not fetch it.
- Sending the same 3202 URL again would likely hit the same challenge.

## Gaps across all sources

- No source I read gives ICD-10 or ICD-11 codes.
- No source gives a prevalence estimate.
- No source gives percentage frequencies for GARD symptoms. The HPO "1/1" codes are the only frequency data.
- The GARD symptom list is marked "Show more", so the uncommon list may be incomplete.

The clinical synopsis URL returned HTTP 404, which is a permanent failure, so I will not retry it. The SLC2A1 page is 724,552 characters, and the first read only covered the start. I'll read further along it to look for the ALLELIC VARIANTS section.

The ALLELIC VARIANTS heading is visible in the summary of this chunk, but .0023 and .0024 are not in the verbatim text I read. I'll read from where the verbatim text stopped.

The verbatim text now reaches the ALLELIC VARIANTS heading, but .0023 and .0024 are still further on. I'll read the next chunk.

## Summary

Only two of the four sources returned data. ClinVar (both sites) and gnomAD were blocked or returned no data, so items 1 and 4 are missing. UniProt and ExPASy gave full verbatim content. The UniProt flat file was longer than one fetch, so I read the rest with the offset parameter and checked the variant list against the verbatim text.

## 1. ClinVar: no variant data obtained

- **https://www.ncbi.nlm.nih.gov/clinvar/?term=...** returned HTTP 200 with a reCAPTCHA "Checking your browser" interstitial (176 characters). No variants were listed. This is a permanent block for this fetch, so retrying the URL would hit the same page.
- **https://clinvarminer.genetics.utah.edu/variants-by-condition/Hereditary%20cryohydrocytosis%20with%20reduced%20stomatin** returned a 301 to `https://www.clinvarminer.org/variants-by-condition/Hereditary%20cryohydrocytosis%20with%20reduced%20stomatin`. I followed that redirect once, and the proxy refused the connection. Retrying would fail the same way.

As a result I have no HGVS names, ClassiFication, review status, variation IDs, or RCV/VCV accessions from ClinVar. The condition name in ClinVar may also need checking, since UniProt lists this disorder as SDCHCN (MIM:608885).

## 2. UniProt P11166 (GTR1_HUMAN), entry version 265, sequence version 2

Final URL read: https://rest.uniprot.org/uniprotkb/P11166.txt (read in two chunks, character 0 and character 39945 onward). The whole flat file was read verbatim.

- **Protein name:** "Solute carrier family 2, facilitated glucose transporter member 1". Alternative names include GLUT-1 and "Glucose transporter type 1, erythrocyte/brain".
- **Length:** 492 aa, 54,084 Da.
- **Transmembrane topology (FT TRANSMEM, verbatim):** 12 helices at 12–33, 67–87, 91–112, 121–144, 156–176, 186–206, 272–293, 307–328, 335–355, 366–388, 402–422, 430–450. The N-terminus (1–11) and C-terminus (451–492) are cytoplasmic.
- **Subcellular location (CC, verbatim):** "Cell membrane" (multi-pass membrane protein), "Melanosome", and "Photoreceptor inner segment" (by similarity). The note says it "Localizes primarily at the cell surface".
- **Function (CC, verbatim opening):** "Facilitative glucose transporter, which is responsible for constitutive or basal glucose uptake". It also says it is the "Most important energy carrier of the brain".
- **Tissue specificity (CC, verbatim):** "Detected in erythrocytes (at protein level). Expressed at variable levels in many human tissues."

**CC -!- DISEASE entries (verbatim, with 125-character quote limit applied to the non-preapproved source):**

- **GLUT1 deficiency syndrome 1 (GLUT1DS1) [MIM:606777]:** "A neurologic disorder showing wide phenotypic variability." The full line describes infantile-onset epileptic encephalopathy and related features.
- **GLUT1 deficiency syndrome 2 (GLUT1DS2) [MIM:612126]:** "A clinically variable disorder characterized primarily by onset in childhood of paroxysmal exercise-induced dyskinesia." Some patients have epilepsy or macrocytic hemolytic anemia.
- **Epilepsy, idiopathic generalized 12 (EIG12) [MIM:614847]:** "A disorder characterized by recurring generalized seizures in the absence of detectable brain lesions and/or metabolic abnormalities."
- **Dystonia 9 (DYT9) [MIM:601042]:** "An autosomal dominant neurologic disorder characterized by childhood onset of paroxysmal choreoathetosis and progressive spastic paraplegia."
- **Stomatin-deficient cryohydrocytosis with neurologic defects (SDCHCN) [MIM:608885]:** the entry name is quoted above. Its description is a rare stomatocytosis with episodic hemolytic anemia, cold-induced red cell cation leak, erratic hyperkalemia, neonatal hyperbilirubinemia, hepatosplenomegaly, cataracts, seizures, intellectual disability, and movement disorder.

Orphanet cross-reference (DR, verbatim): "Orphanet; 168577; Hereditary cryohydrocytosis with reduced stomatin."

**Natural variants (FT VARIANT, verbatim; 53 total).** Format: position, change, disease code(s), UniProt variant ID, dbSNP where given.

- 34 N→I, GLUT1DS2, VAR_054755 (rs80359812)
- 34 N→S, GLUT1DS1, VAR_054756
- 34 N→Y, GLUT1DS1, VAR_065206
- 51 R→H, EIG12, VAR_076226
- 60 T→M, EIG12, VAR_076227
- 66 S→F, GLUT1DS1, VAR_013283
- 77 M→T, EIG12, VAR_076228
- 91 G→D, GLUT1DS1, VAR_013182
- 92 R→W, GLUT1DS2, VAR_069077
- 93 R→W, GLUT1DS2, VAR_065207
- 95 S→I, GLUT1DS2, VAR_065208
- 96 M→V, GLUT1DS1, VAR_065209
- 126 R→C, GLUT1DS1, GLUT1DS2, DYT9, VAR_054757
- 126 R→H, GLUT1DS1, VAR_013183
- 126 R→L, GLUT1DS1, VAR_013184
- 130 G→S, GLUT1DS1, VAR_054758
- 146 E→K, GLUT1DS1, VAR_013284
- 149 P→A, EIG12, VAR_076229
- 153 R→C, GLUT1DS1, VAR_054759
- 153 R→H, GLUT1DS2, VAR_065210
- 155 A→V, GLUT1DS1, VAR_065211
- 165 V→I, GLUT1DS2, VAR_065212
- 169 deletion, GLUT1DS1, VAR_054760
- 212 R→C, GLUT1DS1, DYT9, VAR_065213
- 212 R→H, GLUT1DS1, VAR_065214
- 218 R→S, EIG12, VAR_076230
- 223 R→P, EIG12, VAR_065215
- 223 R→Q, EIG12, VAR_076231
- 223 R→W, GLUT1DS1, VAR_065216
- 232 R→C, EIG12, VAR_069078
- 243 E→V, EIG12, VAR_076232
- 256 K→E, GLUT1DS1, VAR_013185
- 275 A→T, GLUT1DS2, VAR_054761
- 282–285 deletion, GLUT1DS2, VAR_054762
- **286 G→D, SDCHCN, VAR_076233 (rs864309514)**
- 292 Y→YY, GLUT1DS1, VAR_069079
- 294 S→P, GLUT1DS2, VAR_065784
- 295 T→M, GLUT1DS1, VAR_054763
- 303 V→L, no disease code (note: "found in a patient with GLUT1 deficiency syndrome"), VAR_065217
- 310 T→I, GLUT1DS1, VAR_013285
- 314 G→S, GLUT1DS2, VAR_054764
- 317 N→T, GLUT1DS2, VAR_065218
- 324 S→L, GLUT1DS2, VAR_065219
- 329 E→Q, GLUT1DS1, VAR_065220
- 333 R→Q, GLUT1DS1, GLUT1DS2, VAR_065221
- 333 R→W, GLUT1DS1, VAR_013286
- 382 G→D, GLUT1DS1, VAR_065222
- 405 A→D, GLUT1DS1, VAR_065223
- 411 N→S, EIG12, VAR_076234
- **435 deletion, SDCHCN, VAR_076235**
- 458 R→W, EIG12, VAR_076236
- 468 R→W, GLUT1DS1, VAR_069080
- 485 P→L, GLUT1DS1, VAR_065224

**SDCHCN-linked variants specifically:** G286D (VAR_076233) and the ILE-435 deletion (VAR_076235). The verbatim literature lines name "VARIANTS SDCHCN ASP-286 AND ILE-435 DEL" (Flatt et al., Blood 2011, PubMed:21791420) and "ILE-435 DEL" (Bawazir et al., J Clin Endocrinol Metab 2012, PubMed:22492876).

Note on the earlier summary: a model-written summary of the tail of the file had claimed the page had no CC lines and no OMIM codes. That was wrong. The verbatim text has the CC lines and the MIM numbers, so I did not use that summary.

## 3. ExPASy VAR_076233

Final URL read: https://web.expasy.org/variant_pages/VAR_076233.html

- **Variant:** "Variant p.Gly286Asp" in UniProtKB/Swiss-Prot P11166, gene SLC2A1, residue change G286D. dbSNP rs864309514.
- **Classification on page:** LP/P (likely pathogenic or pathogenic).
- **Disease association:** SDCHCN. The page's variant description begins "In SDCHCN; no effect on protein abundance", and adds that the variant has no effect on plasma membrane localization, loss of D-glucose transporter activity, and increased cation leakage.
- **Literature:** Flatt JF et al., "Stomatin-deficient cryohydrocytosis results from mutations in SLC2A1: a novel form of GLUT1 deficiency syndrome.", Blood 118:5267-5277 (2011).

This matches the UniProt FT VARIANT entry for position 286.

## 4. gnomAD SLC2A1 constraint: not obtained

Final URL read: https://gnomad.broadinstitute.org/gene/ENSG00000117394?dataset=gnomad_r4

The page returned HTTP 200 with only the text "gnomAD" (6 characters). It appears to be a JavaScript shell with no rendered data. I have no pLI, LOEUF, o/e LoF or missense values, Z score, or LoF observed/expected counts from this source.

The variant list continues past .0020, and .0023 and .0024 are still ahead. I'll read the next chunk.

The summary gives .0023 and .0024, but it is model-extracted, not verbatim. I'll confirm those two entries from the verbatim text, and also check the gene-phenotype table and location, which fall outside the chunks read so far.

The .0023 and .0024 entries are still only in model summary, because the verbatim text stopped at .0017. The gene-phenotype table is also only summarized. I'll make two final reads, one at each offset.

I could not get the clinical synopsis for SDCHCN. The SLC2A1 gene entry is verified for location, the gene-phenotype table, and the allelic variant list, with .0023 and .0024 confirmed from the mirror's verbatim text. Quotes are kept under the 125-character limit for this non-preapproved source, so most of the content is paraphrased.

**1. Clinical synopsis for SDCHCN (608885): not obtained**
- `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/clinicalSynopsis/608885` returned HTTP 404 Not Found. That is a permanent failure, so I did not retry it.
- No synopsis lines are available from this mirror, so I cannot list them by system.

**2. SLC2A1 (MIM 138140)**

*Location:* 1p34.2. Genomic coordinates (GRCh38, from NCBI): 1:42,925,353-42,958,868.

*Gene-phenotype relationships (verbatim table; location 1p34.2 for every row):*

| Phenotype | MIM | Inheritance | Mapping key |
|---|---|---|---|
| {Epilepsy, idiopathic generalized, susceptibility to, 12} | 614847 | AD | 3 |
| Dystonia 9 | 601042 | AD | 3 |
| GLUT1 deficiency syndrome 1, infantile onset, severe | 606777 | AD, AR | 3 |
| GLUT1 deficiency syndrome 2, childhood onset | 612126 | AD | 3 |
| Stomatin-deficient cryohydrocytosis with neurologic defects | 608885 | AD | 3 |

Mapping key 3 is defined as "The molecular basis of the disorder is known."

*Allelic variants (headings and SLC2A1 notation as on the page):*

| Variant | Phenotype heading | Notation | Nucleotide change (as in body) | Amino acid change | Reference |
|---|---|---|---|---|---|
| .0001 | GLUT1DS1 | DEL | Heterozygous deletion of GLUT1 | not given | Seidner 1998 |
| .0002 | GLUT1DS1 | LYS456TER (rs80359829) | 1545A-T transversion | K456X | Seidner 1998 |
| .0003 | GLUT1DS1 | TYR449TER (rs80359828) | 1526C-A transversion | Y449X | Seidner 1998 |
| .0004 | GLUT1DS1, AR | LYS256VAL (rs80359822) | 945A-G transition, exon 5 | K256V (compound het with .0005) | Wang 2000; Rotstein 2010 |
| .0005 | GLUT1DS1, AR | ARG126LEU (rs80359816) | 556G-T transversion, exon 4 | R126L | Wang 2000 |
| .0006 | GLUT1DS1 | GLY91ASP (rs80359814) | not given | G91D | Klepper 2001 |
| .0007 | GLUT1DS1 | ARG126HIS (rs80359816) | not given | R126H | Brockmann 2001 |
| .0008 | GLUT1DS2 | 12-BP DEL, NT1022 (rs2124448824) | 12-bp deletion, 1022_1033del, exon 6 | loss of 4 amino acids | Weber 2008 |
| .0009 | GLUT1DS2 | GLY314SER (rs121909739) | 1119G-A | G314S | Weber 2008 |
| .0010 | GLUT1DS2 | ALA275THR (rs121909740) | 1002G-A | A275T | Weber 2008 |
| .0011 | GLUT1DS2 | ASN34ILE (rs80359812) | 280A-T transversion, exon 2 | N34I | Overweg-Plandsoen 2003 |
| .0012 | GLUT1DS2 | SER95ILE (rs267607060) | T-A and C-T at nt 283 and 284 | S95I | Suls 2008 |
| .0013 | GLUT1DS2 | ARG93TRP (rs267607061) | not given | R93W | Joshi 2008; Rotstein 2009 |
| .0014 | GLUT1DS1 (also GLUT1DS2, DYT9) | ARG126CYS (rs80359818) | 376C-T transition, exon 4 | R126C | Zorzi 2008; Suls 2009; Weber 2011 |
| .0015 | GLUT1DS2 | ARG91TRP (rs202060209) | 274C-T transition | R91W | Schneider 2009 |
| .0016 | GLUT1DS1, AR | ARG468TRP (rs267607059) | 1402C-T transition, exon 10 (homozygous) | R468W | Klepper 2009 |
| .0017 | GLUT1DS2 | 3-BP INS, TAT (rs2124448406) | 3-bp TAT insertion | adds tyrosine at codon 292 | Perez-Duenas 2009 |
| .0018 | DYSTONIA 9 | ARG212CYS (rs387907312) | 634C-T transition | R212C | Weber 2011 |
| .0019 | EIG12 | ARG232CYS (rs387907313) | 694C-T transition | R232C | Striano 2012 |
| .0020 | EIG12 | ARG223PRO (rs397514564) | 668G-C transversion, exon 5 | R223P | Suls 2009 |
| .0021 | EIG12 | ARG458TRP (rs13306758) | c.1372C-T transition, exon 10 | R458W | Arsov 2012 |
| .0022 | EIG12 | ASN411SER (rs398123069) | c.1232A-G transition, exon 9 | N411S | Arsov 2012 |
| .0023 | SDCHCN (608885) | GLY286ASP (rs864309514) | G-to-A transition (summary only) | G286D | Flatt 2011; patient sdCHC-A (Fricke 2004 patient D-II-2) |
| .0024 | SDCHCN (608885) | 3-BP DEL, ATC | in-frame 3-bp deletion (ATCdel) (summary only) | deletion of ile435 or ile436 | Flatt 2011; patient sdCHC-B (Fricke 2004 patient E-II-1); Bawazir 2012 |

- The page's notation for .0023 and .0024 is verbatim. The nucleotide change for .0023 and the full .0024 description come from model summaries of the page, which agree with each other, so treat them as unconfirmed.
- The page writes nucleotide changes as bare notation such as "1119G-A", not HGVS "c." notation, except for .0021 and .0022, which use "c.".
- The only variant annotated to hemolysis is .0008 (Weber 2008). It is listed under GLUT1DS2, not under any cryohydrocytosis or stomatocytosis heading. The page describes it as a family with "macrocytic hemolytic anemia with reticulocytosis."
- .0009 is from the same Weber 2008 paper, and the page says "Hematologic abnormalities were not observed."
- No SLC2A1 entry is headed cryohydrocytosis or stomatocytosis, apart from .0023 and .0024.

**Not obtained from this mirror**
- The clinical synopsis (see above).
- Any text beyond .0024 in the allelic variants section, and the "See Also" section.

**URLs read**
- `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/138140`, at character offsets 0, 39897, 79794, 139897, 219691, 259588, 299485 and 339382.
- `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/clinicalSynopsis/608885` (404, not retried).

The OUP URL returned a different article (Anderson et al., calcium intake and bone density, DOI 10.1210/jc.2012-1407), so I'm moving to the next URL for Paper A. I'm also getting the Paper B abstract from Europe PMC and checking the Wiley page for full text.

The JCI page returned HTTP 200, but the verbatim text cut off before the abstract. The rest came as a model summary. I'll try the PMC copy you named to get the abstract and PMID.

I'll start with the ClinVar searches, the gnomAD GraphQL query, and the NCBI Gene summary, since none depends on the others.

## Paper A: Bawazir et al., J Clin Endocrinol Metab 2012 (PMID 22492876)

**Bibliographic details (Europe PMC record):** Title is "An infant with pseudohyperkalemia, hemolysis, and seizures: cation-leaky GLUT1-deficiency syndrome due to a SLC2A1 mutation." J Clin Endocrinol Metab 2012 Jun;97(6):E987-93, DOI 10.1210/jc.2012-1399. Electronically published 2012-04-06. Authors and DOI match your citation.

**Abstract:** I cannot reproduce the abstract verbatim because the source is not a preapproved one, and I am limited to quotes of 125 characters or fewer. In summary, the abstract is structured as Context, Objective, Subjects and methods, Results and Conclusion:
- **Context and objective:** GLUT1 deficiency is well known in pediatrics. Very rare GLUT1 mutations can also make red cells leaky to sodium and potassium. The aim was to describe a pediatric patient with GLUT1 deficiency and this cation-leaky state.
- **Clinical course:** The infant had erratic hyperkalemia, neonatal hyperbilirubinemia, anemia, hepatic dysfunction and microcephaly. Seizures and delayed developmental milestones came later. Brain MRI and CT showed multiple abnormalities, including periventricular calcification. Visual impairment was attributed to both cataracts and retinal dysfunction.
- **Results:** Red cell cation measurements showed extremely leaky red cells, which caused the hemolysis. Potassium loss from red cells was temperature-dependent, which explains the hyperkalemia as pseudohyperkalemia. The proband carried a trinucleotide deletion in SLC2A1 that removes isoleucine 435 or 436 of GLUT1.
- **Conclusion:** This is the fourth pedigree described with this syndrome. The authors propose that the multisystem disease combines reduced glucose transport at the blood-brain barrier with osmotic effects of a cation-leaky membrane in GLUT1-expressing cells, notably red cells.

**Full text: not reached.**
- The OUP URL (academic.oup.com/jcem/article/97/6/E987/2536513) returned a different article: Anderson et al., "Calcium Intakes and Femoral and Lumbar Bone Density..." (DOI 10.1210/jc.2012-1407). I did not use it.
- The Europe PMC record shows isOpenAccess "N", inPMC "N", and full text only by subscription via DOI. I did not fetch the PMC search URL, because Europe PMC indicates there is no PMC copy to find.
- Not available to me: red cell potassium values, temperature-dependence data, MCV, reticulocytes, bilirubin, osmotic fragility, cation content, stomatin or band 7 data, the full neurological and ophthalmological workup, and treatment. The HGVS variant nomenclature is also not in the abstract.

Read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22492876&resultType=core&format=json (the OUP URL was also read, but it returned a different article).

## Paper B: Fricke et al., Br J Haematol 2004 (PMID 15180870)

**Bibliographic details (Europe PMC record):** Title is "Four new cases of stomatin-deficient hereditary stomatocytosis syndrome: association of the stomatin-deficient cryohydrocytosis variant with neurological dysfunction." Br J Haematol 2004 Jun;125(6):796-803, DOI 10.1111/j.1365-2141.2004.04965.x. Authors match your citation. Europe PMC lists 34 citing articles.

**Abstract:** Verbatim reproduction is again restricted, so here is a summary:
- The report concerns congenitally sodium- and potassium-leaky red cells of the hereditary stomatocytosis class. It describes three new isolated cases and one new pedigree, and expands one previously reported case.
- In all cases, Western blotting of red cell membranes showed a deficiency of stomatin. Quoted: "deficiency in the 32 kDa membrane protein, stomatin."
- All cases had pronounced cation leaks at 37 °C with abnormal intracellular sodium and potassium.
- Immunocytochemistry showed the stomatin deficiency is incomplete. On blood films, some red cells were stomatin-positive and most were negative. In one case only a minority were negative. All platelets and neutrophils were stomatin-positive.
- The cases differed in how the potassium leak depends on temperature. Three showed a simple monotonic dependence. Two showed a minimum near 20–25 °C and were extremely leaky at 0 °C, which is the cryohydrocytosis phenotype. The authors call these the only two known stomatin-deficient cryohydrocytosis cases.
- Both of those patients had a congenital syndrome of intellectual disability, seizures, cataracts and massive hepatosplenomegaly. The authors suggest this defines a new hematoneurological syndrome.

**Full text: not reached.**
- The Wiley DOI page returned HTTP 403 Forbidden. That refusal is permanent for this URL, so sending it again would fail the same way. I did not try other Wiley URLs.
- The Europe PMC record shows isOpenAccess "N" and no PMC copy. It also lists a Wiley "pdfdirect" link marked free through Unpaywall. I did not fetch it, because the Wiley host has already refused automated access.
- Not available to me: red cell indices, reticulocytes, bilirubin, osmotic fragility, cation content values, the detailed clinical and ophthalmological findings, and treatment.

Read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15180870&resultType=core&format=json (the Wiley URL returned 403).

## Summary

Both papers' abstracts are available (paraphrased here), but neither full text was reachable. To get the verbatim abstracts, use the Europe PMC URLs above. The full-text details you asked for will need institutional or publisher access, or a copy obtained another way.

The three searches returned data. ClinVar's first search reports 172 hits and returned 100 IDs, so I'll fetch summaries for those 100. The second search's 50 IDs are the first 50 of the first list, so they are covered by the same summary request.

The NCBI page returned a reCAPTCHA browser check instead of the chapter. You listed the PMC mirror as a fallback, so I'll try that.

I could not read the GeneReviews chapter, so I have no content to report on the seven points.

- **https://www.ncbi.nlm.nih.gov/books/NBK1430/** returned HTTP 200, but the body was a reCAPTCHA browser-check page ("Checking your browser before accessing www.ncbi.nlm.nih.gov"), not the chapter. This looks like a bot challenge on the NCBI host.
- **https://pmc.ncbi.nlm.nih.gov/books/NBK1430/** returned HTTP 404 Not Found, with no body retrieved. Sending this URL again would fail the same way.
- **https://www.ncbi.nlm.nih.gov/books/NBK1430/?report=reader** was not fetched. It is a variant on the same NCBI host that served the challenge, and that host appears to refuse automated fetches.

Options for you:
- Open the chapter in a normal browser, or save it locally and point me at the file.
- Use an authenticated or alternate retrieval route if one exists for NCBI Bookshelf in your setup.
- Give me a different URL for the same content, such as a full-text copy on another host, and I will fetch that.

Several sources are paywalled; I'll pull open-access PDFs that I can read directly for verbatim text.

I could not give you the verbatim abstract. Neither page returned the abstract as verbatim text, and I did not fill that gap from memory. Most of the other details below come from model-extracted summaries of the pages, not from verbatim text, so treat them as needing verification against the paper.

**URLs read**
- https://www.jci.org/articles/view/34438 (HTTP 200). The verbatim text stopped at the author list, before the abstract. The rest was a model summary.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2350432/ (HTTP 200). This was the fallback you named, though the JCI page was not blocked. It also stopped before the abstract and the rest was a summary.

**Abstract**
- Not available verbatim from either page. The JCI summary says it is about 250 words, and the PMC summary declined to reproduce it.
- Summary of the abstract (not verbatim): a three-generation family with paroxysmal exertion-induced dyskinesia (PED), epilepsy, developmental delay, hemolytic anemia and echinocytosis. A 4-residue deletion (Q282_S285del) in GLUT1 reduced glucose transport and caused a cation leak. Two other GLUT1 mutations in PED families reduced glucose transport without a cation leak.
- To get the verbatim abstract, open the PDF or the abstract section of the article directly.

**Identifiers**
- DOI: 10.1172/JCI34438 (both pages).
- PMCID: PMC2350432 (PMC page).
- PMID: the two sources conflict. The JCI page says it "does not list a PMID". The PMC summary gives 18451999. I could not confirm that number from verbatim text, so verify it in PubMed before citing.

**SLC2A1 mutations (from the summaries, both sources agree unless noted)**

| Family | Nucleotide (cDNA) | Protein | Segregation / inheritance |
|---|---|---|---|
| PED1 | c.1022_1033del (in-frame, 12 bp) | p.Q282_S285del (loss of QQLS, transmembrane segment 7) | Cosegregates with disease. Absent in 150 controls. Described as de novo with dominant inheritance. The PMC summary adds microsatellite confirmation of parentage. |
| PED2 | c.G1119A | p.G314S (transmembrane segment 8) | Found in one unaffected person. The PMC summary says that person inherited it from an unaffected deceased mother, and the authors suggest nonpenetrance. Absent in 150 controls. |
| PED4 | c.G1002A | p.A275T (cytoplasmic end of transmembrane segment 7) | The PMC summary quotes the authors: "Perfectly cosegregates with the PED phenotype." Absent in 150 controls. |
| PED3, PED5 | None found | None | Coding sequence and splice sites sequenced; MLPA excluded copy-number variants. The PMC summary notes promoter and UTR variants were not examined. |

**Clinical phenotype (PED1, from the JCI summary)**
- The index patient (III-2) had PED from age 6, with dystonic and choreoathetotic movements in exercised limbs. His exam was normal between attacks.
- IV-1 and IV-2 had hemolytic anemia, epilepsy and developmental delay. Seizures improved with carbohydrate intake.
- Echinocyte levels were 14.8–41.6% in affected members, versus a normal range below 6.3%.
- CSF/serum glucose ratio was 0.39–0.55 in affected members, versus 0.62–0.68 in controls. The summary notes this is higher than usual for GLUT1 deficiency.
- Other PED families had no hemolysis, except mild anemia in PED3. PED3 and PED5 had no echinocytosis.

**Electrophysiology and functional results (JCI summary only; the PMC summary did not cover these)**
- Expression systems: *Xenopus* oocytes and human erythrocytes. Patch clamp was at room temperature, and the summary reports no temperature-dependence study.
- Glucose uptake: reduced for all three mutants in oocytes. Vmax fell (WT 213 vs. Q282_S285del 37 pmol/oocyte/min), with Km unchanged. Patient erythrocyte uptake was reduced (slope −0.0201 vs. −0.0280 s⁻¹, P < 0.05).
- Cation leak: Q282_S285del oocytes had higher [Na⁺]i, lower [K⁺]i and increased ⁸⁶Rb⁺ flux. Erythrocyte ⁸⁶Rb⁺ flux was about 6-fold higher in 3 of 4 patients. Whole-cell conductance rose from 83 pS (controls) to 363 pS (patients). Resting membrane potential in oocytes was −19 mV (mutant) vs. −43 mV (WT).
- Ions: reversal-potential shifts indicate permeability to K⁺, Na⁺, Ca²⁺ and NMDG⁺, in that order. The PMC summary gives the sequence as K⁺ > Na⁺ > Ca²⁺.
- Calcium: erythrocyte [Ca²⁺]i was higher in patients (fluo-3 7.6 vs. 6.0).
- G314S and A275T did not increase cation permeability.

**Mechanism of cation conduction**
- The authors propose that the deleted QQLS residues normally form a bottleneck in the GLUT1 pore. The PMC summary quotes the phrase "bottle neck within the pore of GLUT1." Molecular modeling suggests the deletion widens the central channel.
- The JCI summary says the cation leak is "independent of the glucose transport function". The PMC summary says the leak is unique to Q282_S285del.
- The PMC summary links hemolysis to osmotic swelling of erythrocytes with increased cation leak.

**Stomatin**
- Neither summary mentions stomatin. Both pages were cut off before the Discussion, so I cannot say whether the paper mentions it.

**Treatment (ketogenic diet)**
- The index patient improved on a ketogenic diet, with dyskinesias appearing later during exercise. He stopped because the diet was hard to follow.
- IV-1 started the diet at age 11 and had complete seizure control, with better school performance.
- IV-2 had complete seizure resolution and improved mental development.
- The PMC summary paraphrases the authors as describing a ketogenic diet that changes the brain's main energy source from glucose to ketone bodies.

**Caveats**
- Quotes attributed above come from the model summaries, not verbatim text. Check them against the paper before citing.
- The two summaries disagree on a few details (the PMID, the PED2 inheritance wording and the ion permeability order). Treat these as unresolved.

The Bristol record has the abstract but no PDF link, so I'm moving on to the Blood journal URL.

Both Blood journal URLs returned 403. Trying the DOI last.

I could not give you the full verbatim abstracts for #1-#3, and #4 is only partly covered. Europe PMC's responses came from a non-preapproved source, so I can quote only short fragments (125 characters or fewer). The abstracts below are paraphrased, and the metadata is exact. The full abstracts are at the DOIs listed, or in PubMed for the same PMIDs.

## 1. PMID 21791420
- **Title:** "Stomatin-deficient cryohydrocytosis results from mutations in SLC2A1: a novel form of GLUT1 deficiency syndrome."
- **Authors:** Flatt JF, Guizouarn H, Burton NM, Borgese F, Tomlinson RJ, Forsyth RJ, Baldwin SA, Levinson BE, Quittet P, Aguilar-Martinez P, Delaunay J, Stewart GW, Bruce LJ
- **Journal:** Blood
- **Year:** 2011 (Nov; electronic publication 2011-07-26)
- **Volume/pages:** 118(19): 5267-5277
- **DOI:** 10.1182/blood-2010-12-326645
- **PMCID:** none (not in PMC)
- **Abstract (paraphrased):** Opens with the hereditary stomatocytoses, which involve abnormal cation permeability of the red cell membrane. The authors report that stomatin-deficient cryohydrocytosis, a form linked to a cold-induced cation leak, is caused by SLC2A1 (GLUT1) mutations. In Xenopus oocytes, these mutations reduce glucose transport and cause a cation leak. They use a 3D model of GLUT1 to propose mechanisms and find that stomatin is lost during reticulocyte maturation through endocytosis. The paper compares this phenotype with GLUT1 deficiency syndrome and paroxysmal exercise-induced dyskinesia.

## 2. PMID 22399508
- **Title:** "Biological relevance of medullary thyroid microcarcinoma."
- **Authors:** Machens A, Dralle H
- **Journal:** The Journal of Clinical Endocrinology and Metabolism (J Clin Endocrinol Metab)
- **Year:** 2012 (May; electronic publication 2012-03-07)
- **Volume/pages:** 97(5): 1547-1553
- **DOI:** 10.1210/jc.2011-2534
- **PMCID:** none
- **Abstract (paraphrased):** A retrospective study at a tertiary referral centre of 233 patients with medullary thyroid microcarcinoma, 126 hereditary and 107 sporadic, all treated with compartment-oriented surgery. Lymph node metastases became more common as tumour diameter increased, and biochemical cure rates fell. Distant disease was rare (1.3%). Positive nodal status and the number of involved nodes were the strongest predictors of calcitonin not normalising after surgery. The authors conclude that both hereditary and sporadic microcarcinomas carry a significant risk of nodal metastasis and postoperative calcitonin elevation.

## 3. PMID 18451999
- **Title:** "GLUT1 mutations are a cause of paroxysmal exertion-induced dyskinesias and induce hemolytic anemia by a cation leak."
- **Authors:** Weber YG, Storch A, Wuttke TV, Brockmann K, Kempfle J, Maljevic S, Margari L, Kamm C, Schneider SA, Huber SM, Pekrun A, Roebling R, Seebohm G, Koka S, Lang C, Kraft E, Blazevic D, Salvo-Vargas A, Fauler M, Mottaghy FM, Münchau A, Edwards MJ, Presicci A, Margari F, Gasser T, Lang F, Bhatia KP, Lehmann-Horn F, Lerche H
- **Journal:** The Journal of Clinical Investigation (J Clin Invest)
- **Year:** 2008 (Jun)
- **Volume/pages:** 118(6): 2157-2168
- **DOI:** 10.1172/JCI34438
- **PMCID:** PMC2350432
- **Abstract (paraphrased):** Describes a three-generation family with paroxysmal exertion-induced dyskinesia, epilepsy, developmental delay, low CSF glucose, and hemolytic anemia with echinocytosis. The authors identify a deletion of four conserved residues (Q282_S285del) in the GLUT1 pore. In Xenopus oocytes and human erythrocytes, this mutation reduces glucose transport and causes a cation leak. Screening four more families found two further GLUT1 mutations (A275T, G314S) that reduce glucose transport without affecting cation permeability. The authors propose that the dyskinesias reflect an exertion-induced energy deficit in the basal ganglia, and that the hemolysis reflects a cation leak through mutant GLUT1.

## 4. Search for "cryohydrocytosis" (pageSize=50)
- **hitCount:** 223, with a nextCursorMark, so there are more pages. I did not list all of them.
- **Coverage:** I read about 80,000 of the 327,779 characters on this first page verbatim. The rest came back only as a model-extracted summary, and the last 48,059 characters were not read. That summary contradicted the verbatim text in places (it called record 42944837 "not visible" when the verbatim text shows it), so I treat the summary-only items as unverified.

**Verbatim records relevant to cryohydrocytosis:**
- **PMID 41793238** (PMC13139882). "Cryohydrocytosis: When Cold Breaks the Membrane." Ntoumaziou A et al. Am J Hematol, 2026, 101(6): 1217-1219. DOI 10.1002/ajh.70274. The JSON has no abstractText field for this record.
- **PMID 42245163** (PMC13230118). "Case Report: Atypical hepatobiliary manifestations associated with erythrocyte membrane instability in glucose transporter type 1 deficiency syndrome." Lee H, Ryu SW, Hong J. Front Pediatr, 2026, 14: 1790301. DOI 10.3389/fped.2026.1790301. Paraphrased abstract: a 5-year-old boy with GLUT1 deficiency and an SLC2A1 in-frame deletion, with recurrent hemolysis and gallstone-related cholestasis. A temperature-dependent potassium leak test at age 11 showed cold-enhanced cation leakage, which the authors attribute to cryohydrocytosis.
- **PMID 35356079** (PMC8959883). "Reticulocyte Maturation and Variant Red Blood Cells." Stevens-Hernandez CJ, Flatt JF, Kupzig S, Bruce LJ. Front Physiol, 2022, 13: 834463. DOI 10.3389/fphys.2022.834463. Cryohydrocytosis appears as a keyword. The abstract is about reticulocyte maturation in variant red cells, including overhydrated hereditary stomatocytosis cells.
- **PPR505246** (preprint, DOI 10.12688/f1000research.18553.2). "Impact of pathogenic mutations of the GLUT1 glucose transporter on solute carrier dynamics using ComDYN enhanced sampling." Mouhib H et al. F1000Research, 2022 (preprint, version 2). The abstract lists cryohydrocytosis with neurological defects (Dystonia-9) among the disease categories it covers.

**Summary-only (unverified):**
- **PMID 36938875.** "Pseudohyperkalemia due to cryohydrocytosis in GLUT1 deficiency syndrome. A case report and literature review." Epileptic Disorders, 2023. This is the most relevant item I could not verify in the verbatim text.
- **PMID 40405536.** "Glut1 Deficiency Syndrome: Novel Pathomechanisms, Current Concepts, and Challenges." J Inherit Metab Dis, 2025. A GLUT1 review, not specific to cryohydrocytosis.

**Other verbatim hits** (CRSwNP, lymphoma, TSC2, hemochromatosis, sneezing reflex, and so on) do not mention cryohydrocytosis in the text I read.

**Next step:** The full-text search returns many off-topic hits. A narrower query such as `TITLE_ABS:"cryohydrocytosis"` would likely give a manageable list. I can run that and page through it with the nextCursorMark if you want.

The first ClinVar summary was cut off after about 11 records, and the tool's summary of the rest is not reliable enough to report. I'll re-request the remaining IDs in smaller batches so each one comes back complete.

I did not obtain the full text or a PDF. No PDF was saved to a local file, so there is no harness note to point you to.

**What happened, in order**

1. **eprints.ncl.ac.uk/190091**: 301 redirect to `https://outputs.ncl.ac.uk/articles/journal_contribution/Stomatin-deficient_cryohydrocytosis_results_from_mutations_in_SLC2A1_a_novel_form_of_GLUT1_deficiency_syndrome/34195836`. That target returned **HTTP 403 Forbidden**.
2. **Bristol record** (`https://research-information.bris.ac.uk/en/publications/stomatin-deficient-cryohydrocytosis-results-from-mutations-in-isl/`): fetched (HTTP 200), but it has only the abstract and citation data. It has no PDF or full-text link, only the DOI.
3. **bloodjournal.org/content/118/19/5267**: **HTTP 403 Forbidden**.
4. **bloodjournal.org/content/118/19/5267.full.pdf**: **HTTP 403 Forbidden**.
5. **doi.org/10.1182/blood-2010-12-326645**: 302 redirect to `https://ashpublications.org/blood/article/118/19/5267/29357/Stomatindeficient-cryohydrocytosis-results-from`. That target returned **HTTP 403 Forbidden**.

The 403s are permanent for WebFetch, so retrying those URLs would fail the same way. The publisher and the repository both block automated fetches. Access probably needs a logged-in browser session or institutional access.

**Abstract (from the Bristol record)**

The abstract describes hereditary stomatocytoses as dominantly inherited hemolytic anemias with increased erythrocyte permeability to monovalent cations, with known causes in RHAG and SLC4A1. It then says that SLC2A1 (encoding GLUT1) mutations cause glucose transport loss and a cation leak, shown by expression in Xenopus oocytes. The authors previously reported two cases of stomatin-deficient cryohydrocytosis (sdCHC), with cold-induced cation leak, hemolytic anemia, hepatosplenomegaly, cataracts, seizures, intellectual disability and movement disorder. They used a 3D GLUT1 model to propose mechanisms for the two mutations. They also found stomatin is lost during reticulocyte maturation through endocytosis. The paper compares the molecular basis of GLUT1 deficiency syndrome, paroxysmal exercise-induced dyskinesia and sdCHC.

**Not covered**

I could not read the Results and Discussion, the oocyte electrophysiology, glucose uptake, stomatin immunoblot/flow data, the 3D model interpretation, or the patient clinical data. Those sections are unknown to me.

**DOI note**

The Bristol record lists the DOI as `10.1182/blood-2010-12-3266`, which is shorter than the `blood-2010-12-326645` you gave. The DOI you gave does resolve to the ASH article page, so it appears correct.

**Options**

- Fetch the article from a machine with institutional access and save the PDF.
- If you have an authenticated tool or a `gh`-style client for the publisher, I can try that route instead.
- If you have a copy of the PDF, you can share it and I can summarize it, though that would need a different route into this session.

Found some very recent open-access papers (2026 Am J Hematol and Front Pediatr). Fetching those plus model-organism data.

Each batch still truncated near 39.8k characters, so about 28 IDs were only summarized by the tool. I'll re-request those in smaller batches so the records come back verbatim.

Item 1's PMID 18555780 resolves to a different paper (Skerker et al., Cell 2008), so I'm searching Europe PMC by the title the caller gave.

## Summary

Only one of the four sources was read. Source 1 (PMC5911802) gave usable content, though part of its middle section came from a model-extracted summary. Source 2 (PMC2719024) and source 4 (PMC5731088) returned a reCAPTCHA browser-check page instead of the article. Source 3 (Wiley) returned HTTP 403, and the fallback you named (PMC5726881) is an unrelated ovarian angiosarcoma case report. Details are below.

---

## Source 1: Flatt JF & Bruce LJ, PMC5911802 (read)

**Citation**
- Title: "The Molecular Basis for Altered Cation Permeability in Hereditary Stomatocytic Human Red Blood Cells"
- Authors: Joanna F Flatt, Lesley J Bruce (Bristol Institute for Transfusion Sciences, NHS Blood and Transplant, Bristol, UK)
- Journal: Front Physiol. 2018 Apr 16;9:367 (volume 9, article 367)
- PMID: 29713289
- PMCID: PMC5911802
- DOI: 10.3389/fphys.2018.00367
- License: CC BY
- URLs read: https://pmc.ncbi.nlm.nih.gov/articles/PMC5911802/ and the same URL at offset 139942 (reference list only)

**Classification of hereditary stomatocytoses**

The abstract (read verbatim) gives the gene assignments:
- "The cryohydrocytosis phenotype, including South-east Asian Ovalocytosis, results from mutations in _SLC4A1_" (CHC, band 3)
- "the very rare condition, stomatin-deficient cryohydrocytosis, is caused by mutations in _SLC2A1_" (sdCHC, GLUT1)
- Over-hydrated stomatocytosis (OHSt): mutations in RHAG, causing a very leaky membrane
- Familial pseudohyperkalemia (FP): mutations in ABCB6
- Dehydrated stomatocytosis (DHSt/xerocytosis): PIEZO1 (FAM38A) and KCNN4 (per the Introduction and Table 1)

Table 1 and the summary give these details:
- **OHSt 1 and 2:** RHAG (e.g., Phe65Ser, Ile61Arg). Leak "× 40" normal, monotonic temperature dependence.
- **Cryohydrocytosis (CHC):** SLC4A1, including the subtype HS-LTL (Asp705Tyr or Arg760Gln, which also shows spherocytes). Temperature-dependent leak; the text states "Cryohydrocytosis is so named because of the temperature-dependence of the cation leak." South-east Asian ovalocytosis (SAO) is a 9-residue band 3 deletion (residues 400–408) within this group.
- **sdCHC:** SLC2A1 (see below).
- **DHSt:** PIEZO1 (FAM38A) and KCNN4 (Gardos channel). Leak about 2× normal per the summary. The text says these mutations "alter the activation and deactivation kinetics of these channels, leading to increased opening."
- **FP:** ABCB6 (e.g., Arg375Gln/Trp, Arg723Gln, Arg276Trp, Val454Ala). Near-normal at 37 °C with a "shoulder" or U-shaped leak on cooling. The summary notes that one FP cohort was linked to a PIEZO1-region locus, so the FP gene assignment is not fully consistent within the text.

Temperature dependence (main text, verbatim): "From 37°C downwards the leak decreases with temperature in a monotonic manner." The text also notes that normal human RBCs show a U-shaped leak curve, with a minimum near 8 °C, which "increases with decreasing temperature" below 10 °C.

**sdCHC and SLC2A1/GLUT1**

Most of the following comes from the model-extracted summary of the unread middle section, not verbatim text:
- Frequency: "very rare," with three patients reported to date.
- Cation leak: about 10× normal at 37 °C. Table 1 lists two pedigrees: Montpellier (Gly286Asp, U-shaped leak) and San Francisco (ΔIle435/436).
- Mechanism: the text says GLUT1 mutants "lost their ability to transport their usual substrate, and instead induced a cation leak" in *Xenopus* oocytes. It suggests the leak may come from altered protein–protein or protein–lipid interactions rather than conduction through the GLUT1 transport channel.
- Clinical features: non-hematological features not seen in other stomatocytoses, including cataracts, seizures, and severe learning difficulties. Table 1 also lists "sdCHC + neuro." phenotypes.
- Splenectomy: not discussed for sdCHC in the text read.

**Stomatin (STOM gene, band 7.2b)**

The verbatim text I read does not mention the STOM gene or the band 7.2b designation. The summary says the same. The article's reference list does include stomatin-related titles:
- Rungaldier et al. 2013: "Stomatin interacts with GLUT1/SLC2A1, band 3/SLC4A1, and aquaporin-1 in human erythrocyte membrane domains" (Biochim Biophys Acta 1828:956–966)
- Salzer & Prohaska 2001: "Stomatin, flotillin-1, and flotillin-2 are major integral proteins of erythrocyte lipid rafts"
- Stewart et al. 1992: "Isolation of cDNA coding for an ubiquitous membrane protein deficient in high Na+, low K+ stomatocytic erythrocytes"

From the summary (not verbatim):
- Proposed functions: cholesterol binding, actin binding, vesiculation, regulation of ion channels, and a scaffolding role ("probably acts as a scaffolding protein").
- GLUT1 link: stomatin is said to convert GLUT1 into a transporter of oxidized vitamin C (dehydroascorbic acid) in species that cannot synthesize vitamin C.
- Why it is reduced in sdCHC: the summary says the text does not explain this. In OHSt, stomatin deficiency is described as "a secondary effect of the disorder," with RhAG as the primary defect.

**Splenectomy and thrombosis**

The only splenectomy statement the summary reports concerns DHSt. Per the summary, the text says splenectomy "is not recommended for patients with DHSt because it often results in thrombo-embolic events" (summary wording; not verified verbatim). The reference list includes Stewart et al. 1996, "Thrombo-embolic disease after splenectomy for hereditary stomatocytosis" (Br J Haematol 93:303–310; PMID 8639421).

**Coverage gap:** The last 26,300 characters were read as the reference list only. The middle section (about characters 39,942–139,942) was only summarized. Stomatin and sdCHC details may therefore be incomplete. Re-reading the middle section would return the same summary, so this is the most I can get from this URL.

---

## Source 2: Haematologica 2009 review, PMC2719024 (not read)

- Fetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC2719024/ returned HTTP 200 with a reCAPTCHA "Checking your browser" interstitial (176 characters). No article content was returned.
- Status: permanent for this fetch. Retrying the URL will return the same page.
- Citation: not verified. I cannot confirm the PMID 19644134 or DOI from this source.

## Source 3: Wiley, 10.1002/ajh.24929 (not read)

- Fetch: https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.24929 returned HTTP 403 Forbidden.
- Fallback: https://pmc.ncbi.nlm.nih.gov/articles/PMC5726881/ was fetched, but it is not a stomatocytosis review. It is Kudela E et al., "Bilateral ovarian angiosarcoma arising from the mature cystic teratomas – A case report and review of the literature," Int J Surg Case Rep 2017;42:90–93 (PMID 29227858, PMCID PMC5726881, DOI 10.1016/j.ijscr.2017.11.064). It contains nothing on diagnosis or management of red cell hydration disorders.
- Status: no usable content on osmotic gradient ektacytometry, cation flux studies, or management. The 403 is a permanent failure, so retrying the Wiley URL would fail the same way. The correct article for this DOI and its PMCID need to be identified by the caller.

## Source 4: Gallagher PG, Blood 2017, PMC5731088 (not read)

- Fetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC5731088/ returned HTTP 200 with a reCAPTCHA "Checking your browser" interstitial (176 characters). No article content was returned.
- Status: permanent for this fetch. I did not search PMC for an alternative PMCID, since the page is a browser challenge rather than a wrong ID.
- Citation: the PMCID PMC5731088 is unverified. The title and journal details (Blood 2017;130(25):2699–2708) are from your request only.

---

**Next steps:** The caller could confirm PMIDs/PMCIDs for sources 2–4 through PubMed or NCBI search, or use an authenticated/alternate route for the Wiley and PMC pages. The reCAPTCHA pages may clear with a later attempt from a different session, but I did not retry them.

## Papers 1 and 2: not retrieved

Both PMC pages returned a browser verification interstitial instead of article text. The fetches returned HTTP 200 with a 176-character "Checking your browser - reCAPTCHA" page, so I have no content from either paper.

- **Paper 1** (Ntoumaziou et al., PMC13139882): https://pmc.ncbi.nlm.nih.gov/articles/PMC13139882/ was blocked by the reCAPTCHA challenge. Nothing about the case, variant, labs, subtypes, or management is verified. Sending the same URL again will likely hit the same challenge.
- **Paper 2** (Lee et al., PMC13230118): https://pmc.ncbi.nlm.nih.gov/articles/PMC13230118/ returned the same challenge. The abstract, HGVS variant, patient details, potassium leak testing, and treatment are all unverified.

I did not try other hosts such as the DOI or publisher pages, since you gave me PMC URLs. If you want these two, you could retrieve them from the publisher site, or ask me to try a specific alternate URL.

## Paper 3: Stevens-Hernandez CJ, Flatt JF, Kupzig S, Bruce LJ. "Reticulocyte Maturation and Variant Red Blood Cells." Front Physiol 2022;13:834463, PMID 35356079

Final URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC8959883/

The page was truncated. I read the verbatim text through the Discussion's variant-cell section. The rest, including Figure 3, the Conclusion, and the stomatin discussion, came only as a model-written summary. Quotes from that summary are marked below and could not be checked word for word. Quotes are kept under 125 characters because this source is not on the preapproved list.

**Abstract (verbatim):** "We propose that the size and composition of these variant cell types correlate with the different stages of reticulocyte maturation." The abstract also says the overhydrated hereditary stomatocytosis (OHSt) cells "are the least mature, they barely reduced their plasma membrane."

**Stomatin loss in variant cells (verbatim intro):**
- "OHSt RBCs also lack stomatin, although no gene defect was found in _STOM_ to account for this loss."
- "sdCHC RBCs also lack stomatin although again there is no associated gene defect in _STOM_."

**Stomatin in the membrane-protein results (verbatim):**
- "Stomatin and spectrin were present in normal amounts in SAO membranes."
- "as expected, stomatin was reduced in the sdCHC RBCs."
- For OHSt: "OHSt RBC membranes contained normal levels of spectrin but very low levels of stomatin as expected."

**Stomatin and maturation (from the summary, not verbatim):**
- "the presence or absence of stomatin appeared to have little effect on the ability of the reticulocyte to mature." CHC and sdCHC cells matured to a similar level even though sdCHC cells have almost no stomatin.
- "Our data suggests that the budding mechanism of vesiculation is not employed in reticulocyte maturation." (The summary quotes this as a Discussion or Conclusion sentence. I could not confirm its location.)
- "Stomatin does not appear to be required, although lack of stomatin may affect maturation in OHSt RBCs."
- "lack of stomatin, depending on when it is lost in these variant cells, may affect this process."

**Cryohydrocytosis, sdCHC, and GLUT1 (verbatim intro):**
- "sdCHC is caused by variants of _SLC2A1_, the gene encoding glucose transporter 1 (GLUT1)." The intro adds that these RBCs have a cation leak about ten times normal.
- SAO, CHC, and sdCHC all have intermediate cation leak and MCVs of 100-120 fL. SAO and CHC are caused by variants of _SLC4A1_ (band 3).
- The sdCHC patient in this study has a heterozygous Gly286Asp variant in _SLC2A1_ (rs864309514), first reported by Fricke et al. 2004 and later by Flatt et al. 2011.
- Table 1 lists the sdCHC patient as male, Hb 12.7 g/dL, MCV 121.3 fL, reticulocytes 1.4%, with "neurological disorder and cataracts, hemolytic anemia, loss of stomatin." It lists CHC (male, MCV 91.2 and 87.7 fL) with "mild hemolytic anemia, stomatocytes, gall stones, jaundice."

The summary says GLUT1 and SLC2A1 appear only in the reference list. That is wrong. The verbatim intro discusses them in the text, so I am relying on the verbatim text here.

**Mechanism of membrane protein loss and variant cells (from the summary, not verbatim):**
- Variant cell size tracks maturation stage, with OHSt the least mature.
- "Mitochondria and lysosomes predominantly being lost early probably through an autophagy and exosome release mechanism."
- "Residual ER, TfR and CD147 predominantly lost later probably through the autophagic-endocytic macrovesicle mechanism."

**Verbatim Discussion on variant groups:** The sdCHC, CHC, and SAO cells "all cleared the mitochondrial and lysosomal proteins but retained more ER membranes." The OHSt cells "have not matured much further than the R1 stage."

**Not read:** the Figure 1 and Figure 2 images, the supplementary Table 1 (a separate file), and the cited papers (Flatt 2011, Bawazir 2012, and others). Some parts of the summary are based on titles of those papers only.

All 100 IDs from the first search are now covered. Three records (697940, 392030, 1304066) came back with incomplete trait lists, so I'll re-request just those.

Europe PMC gives the PMCID as PMC370344, not PMC370348. The PMC page for PMC370348 was blocked by a reCAPTCHA. Trying the full text for PMC370344 and the JCI page.

## Stomatin (STOM) and GLUT1: primary-literature report

**Caveat on the Montel-Hagen PMID:** the caller's PMID 18555780 is wrong. Europe PMC returns Skerker JM et al., "Rewiring the specificity of two-component signal transduction systems," Cell 2008, for that ID. The correct record came from a title search (below). Europe PMC marks this paper as not open access.

### 1. Montel-Hagen A et al., Cell 2008 (corrected identifiers)
- **PMID:** 18358815
- **DOI:** 10.1016/j.cell.2008.01.042
- **Citation:** Cell 2008 Mar; 132(6):1039-1048. Authors: Montel-Hagen A, Kinet S, Manel N, Mongellaz C, Prohaska R, Battini JL, Delaunay J, Sitbon M, Taylor N.
- **Title:** "Erythrocyte Glut1 triggers dehydroascorbic acid uptake in mammals unable to synthesize vitamin C."
- **Abstract (paraphrased; the full text is in the Europe PMC response):**
  - Glucose transport falls during human erythropoiesis even though Glut1 transcripts rise more than 1000-fold.
  - Glut1-mediated transport of dehydroascorbic acid (DHA), the oxidized form of ascorbic acid, rises sharply over the same period.
  - The authors identify stomatin, an integral erythrocyte membrane protein, as regulating the switch from glucose transport to DHA transport.
  - Erythrocyte Glut1 and DHA uptake are traits of humans and a few other mammals that have lost the ability to make vitamin C from glucose.
  - Mice, which can make vitamin C, express Glut4 but not Glut1 in mature erythrocytes.
  - The authors conclude that Glut1 co-expression with stomatin is a compensatory mechanism in mammals that cannot synthesize vitamin C.
- **Comments on the paper:** Cell 2008 Mar 21;132(6):921-2 (PMID 18358804), and Cell 2009 Apr 17;137(2):200-1 (PMID 19379682).

### 2. Rungaldier S et al., BBA 2013
- **Title:** "Stomatin interacts with GLUT1/SLC2A1, band 3/SLC4A1, and aquaporin-1 in human erythrocyte membrane domains."
- **PMID:** 23219802
- **DOI:** 10.1016/j.bbamem.2012.11.030
- **Citation:** Biochim Biophys Acta 2013 Mar; 1828(3):956-966. Authors: Rungaldier S, Oberwagner W, Salzer U, Csaszar E, Prohaska R.
- **PMC:** PMC3790964 (open access, CC BY-NC-ND).
- **Abstract (paraphrased):**
  - Stomatin is a homo-oligomeric, lipid raft-associated monotopic membrane protein. It is a major erythrocyte membrane protein and associates with GLUT1.
  - Earlier attempts to purify stomatin complexes failed, so the authors cross-linked erythrocyte membranes in situ before immunoaffinity purification.
  - Mass spectrometry of the cross-linked complexes identified GLUT1, band 3 (anion exchanger), and aquaporin-1 as the major partners.
  - Other partners included ferroportin-1, urea transporter-1, a nucleoside transporter, the Ca-ATPase-4, CD47, and flotillins.
  - The authors propose stomatin as a membrane scaffold that modulates transport proteins.

### 3. UniProt P27105 (STOM_HUMAN)
- **Entry:** P27105, STOM_HUMAN, reviewed (Swiss-Prot). Entry version 228. Sequence 288 aa, 31,731 Da.
- **Recommended name:** Stomatin.
- **Alternative names:** Erythrocyte band 7 integral membrane protein; Erythrocyte membrane protein band 7.2; Protein 7.2b. Synonyms: BND7, EPB72.
- **Subcellular location:** Cell membrane (peripheral, cytoplasmic side; lipid-anchored); cytoplasm, cytoskeleton; membrane raft; melanosome; cytoplasmic vesicle. Localizes to a juxtanuclear structure probably from the Golgi.
- **FUNCTION (verbatim):** "Regulates ion channel activity and transmembrane ion transport. Regulates ASIC2 and ASIC3 channel activity."
- **SUBUNIT (key points):** Homodimer and higher-order homo-oligomer; banana-shaped dimer. Interacts with SLC2A1 (GLUT1) and SLC4A1 (band 3), and with ASIC1-3 (by similarity). Also interacts with LANCL1 and STOML1.
- **Tissue specificity:** "Detected in erythrocytes (at protein level). Widely expressed."
- **Domain/family:** Belongs to the band 7/mec-2 family. SPFH/band 7 domain (PROSITE PS01270; Pfam PF01145). Structures are in PDB, including 9Z7U and 9OH9.
- **Disease annotation:** None in the flat file. There is no DISEASE comment, and cryohydrocytosis is not mentioned.
- **Relevant references listed:** Gallagher PG and Forget BG, JBC 1995 (PMID 7592848), titled as a candidate gene for "hereditary hydrocytosis." Snyers et al., JBC 1998 (PMID 9642292), on oligomerization. Genetet S et al., Sci Rep 2017 (DOI 10.1038/srep46170), "Stomatin modulates the activity of the Anion Exchanger 1 (AE1, SLC4A1)." That 2017 paper was not fetched; I know it only from the UniProt record.

### 4. NCBI Gene 2040 (STOM)
- **Official name:** stomatin (symbol STOM, status Official).
- **Aliases:** BND7, EPB7, EPB72.
- **Other designations:** erythrocyte band 7 integral membrane protein; erythrocyte membrane protein band 7.2 (stomatin); erythrocyte surface protein band 7.2; protein 7.2b.
- **Location:** chromosome 9, 9q33.2 (NC_000009.12, 8 exons). MIM 133090. A pseudogene is on chromosome 6.
- **RefSeq summary (partly quoted):** "Loss of localization of the encoded protein is associated with hereditary stomatocytosis, a form of hemolytic anemia." The summary does not mention cryohydrocytosis.

### 5. Brand J et al., EMBO J 2012
- **Title:** "A stomatin dimer modulates the activity of acid-sensing ion channels."
- **PMID:** 22850675
- **DOI:** 10.1038/emboj.2012.203
- **Citation:** EMBO J 2012 Aug; 31(17):3635-3646. Authors: Brand J, Smith ES, Schwefel D, Lapatsina L, Poole K, Omerbašić D, Kozlenkov A, Behlke J, Lewin GR, Daumke O.
- **PMC:** PMC3433786 (open access, CC BY-NC-SA).
- **Abstract (paraphrased):**
  - The authors solved three crystal structures of the conserved stomatin domain of mouse stomatin. It forms a banana-shaped dimer.
  - Dimerization is needed to repress acid-sensing ion channel 3 (ASIC3) activity.
  - A hydrophobic pocket on the concave face of the dimer opens when an internal peptide ligand is bound and closes without it. This pocket contributes to ASIC3 inhibition.
  - In one crystal form, stomatin forms a cylindrical oligomer through two conserved surfaces. Both surfaces are needed for ASIC3 current inhibition.
  - The authors suggest this assembly could model related membrane-remodelling proteins such as flotillin and prohibitin.
- **Scope note:** This paper studies mouse stomatin and ASIC3 electrophysiology. It does not address GLUT1, erythrocytes, or cryohydrocytosis directly.

### Summary for the cryohydrocytosis question
- Among these sources, only the Montel-Hagen paper links stomatin to a red-cell transport function (DHA uptake via GLUT1), and it does so through the vitamin C context.
- Rungaldier 2013 is the direct biochemical evidence for a stomatin-GLUT1 complex in erthyrocyte membranes.
- None of the fetched sources mention cryohydrocytosis. The UniProt and NCBI records describe the disease only as hereditary stomatocytosis or hydrocytosis, so any cryohydrocytosis-specific claim would need a separate source.

**URLs read:**
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18555780&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Erythrocyte%20Glut1%20triggers%20dehydroascorbic%20acid%20uptake%22&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Stomatin%20interacts%20with%20GLUT1%22&resultType=core&format=json
- https://rest.uniprot.org/uniprotkb/P27105.txt
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=2040&retmode=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22stomatin%20dimer%20modulates%20the%20activity%20of%20acid-sensing%20ion%20channels%22&resultType=core&format=json

The JCI HTML page has only the abstract, with the body as scanned page images. Europe PMC's full-text XML returned HTTP 500. Trying the JCI PDF linked from that page, which is the only remaining route to the body text.

## Report: GLUT1DS epidemiology, treatment, mechanism, gene therapy, and trials

**Step 1 (full text) failed.** The Europe PMC record resolved (PMID 40405536 = PMCID PMC12099281, DOI 10.1002/jimd.70044, open access, license cc by-nc-nd). But the PMC page at https://pmc.ncbi.nlm.nih.gov/articles/PMC12099281/ returned an HTTP 200 reCAPTCHA interstitial, not the article. The Wiley URL https://onlinelibrary.wiley.com/doi/10.1002/jimd.70044 returned HTTP 403. Both are permanent for this session, so I did not retry. Sending the same URLs again will fail the same way. The Europe PMC full-text XML (`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12099281/fullTextXML`) is a possible route for you to try, but I did not fetch it.

What the Europe PMC record does show: Klepper J (single author, Aschaffenburg), J Inherit Metab Dis 2025 May, 48(3):e70044, cited by 16. Its abstract says the disease "has emerged as a treatable, but complex entity." It says KDT are "ineffective in some patients for reasons yet unknown." It also says KDT in pregnancy and neonatal/adult features are "poorly understood." The mechanism discussion goes "beyond the concept of brain energy depletion" toward "alternative substrates, transport mechanisms, and metabolic interactions of different brain cell types." Future items named are neonatal screening, biomarkers, and "alternative therapies." The abstract does not mention gene therapy, hematologic features, incidence, or specific diets such as modified Atkins, MCT, or alpha-lipoic acid. Those items remain unverified.

**Incidence/prevalence (Step 2).** No population-based figure was found in these search results. Figures seen:
- PMID 31055589 (Kloka J et al., Am J Case Rep 2019, PMC6512754): "G1DS is a rare disease, with an estimated incidence of 1: 90 000." No source is cited in the abstract.
- PMID 29144225 (Hewson S et al., Can J Neurol Sci 2018; DOI 10.1017/cjn.2017.246): "prevalence of GLUT1 deficiency was 2.4%" in a retrospective cohort of 85 patients from one ketogenic diet clinic. This is a clinic proportion, not a population estimate. By my arithmetic it is about 2 of 85.
- PMID 38795333 (Barbour K et al., Epilepsia 2024): a NYC population study that listed GLUT1 deficiency among genetic epilepsies with "Data were limited." No figure given.
- No Australian, Danish, or Japanese incidence figure was found.

**Phenotype (from PMID 42406126, Bercini Z et al., J Neurol 2026;273:446; DOI 10.1007/s00415-026-13976-x; closed access, abstract only):** A systematic review of 68 studies covering 96 patients (94 published plus 2 unpublished). Movement disorders were the presenting symptom in 34.4%. Paroxysmal dyskinesias were in 63.5% and ataxia in 47.9%. Ketogenic therapies were associated with motor improvement in most reported cases, but the outcome data were heterogeneous.

**Hematologic features.** None of the sources I read mention hemolytic anemia, pseudohyperkalemia, or cryohydrocytosis. The only related text is from NCT04137692: "many G1D patients also have low levels of GLUT1 in their red blood cells."

**Treatments and drugs to avoid (from trial records, not reviews):**
- Triheptanoin (UX007, C7 oil) was tested in several trials, summarized below.
- NCT02036853 excluded "Concomitant administration of valproic acid" and "Concomitant administration of a ketogenic diet."
- NCT02960217 listed prohibited medications as "barbiturates, pancreatic lipase inhibitors," along with MCT oil and KetoCal.
- NCT02021526 excluded patients on "medium chain triglyceride-supplemented diets, Atkins diet, low glycemic index diet."
- Modified Atkins and alpha-lipoic acid were not found in any source I read.

**Gene therapy / AAV (Step 3):** Only one relevant preclinical item was found.
- PPR1216810 (bioRxiv preprint, DOI 10.64898/2026.03.04.709430; Tamura S, Hirai S et al., 2026; not peer reviewed). It shows GLUT1 is expressed in astrocytes as well as endothelial cells. Conditional haploinsufficiency in either cell type reproduced disease-like CSF glucose and cognitive/motor deficits. AAV restoration in one compartment gave partial benefit. Quote: "endothelial GLUT1 restoration alone is insufficient for robust rescue" (dual-compartment restoration worked better).
- PMID 40221358 (Auvin S, 2025) states "This article does not explicitly address antisense oligonucleotides or gene therapy."
- PMID 30870728 (Perucca, 2019) is a general epilepsy review, not GLUT1-specific.
- No clinical gene therapy trial appeared in the ClinicalTrials.gov results I read.

**ClinicalTrials.gov (Step 4).** The response was about 631 KB and I could not read all of it. The list below is partial and not exhaustive. Parts of the response, including the final portion past character 459,556, were read only as model summaries or not at all. The total hit count was not visible.

| NCT | Title (short) | Status | Phase | Intervention | Sponsor | Start |
|---|---|---|---|---|---|---|
| NCT02021526 | Triheptanoin (C7 Oil), a Food Supplement, for G1D | WITHDRAWN ("NIH funding resulted in new clinical trial") | PHASE1/PHASE2 | Triheptanoin (DRUG) | UT Southwestern (Juan Pascual) | 2015-12 |
| NCT01993186 | Phase 2 Study of Triheptanoin (UX007) for Glut1 DS | COMPLETED | PHASE2 | UX007; Placebo (DRUG) | Ultragenyx | 2014-02-28 (from summary only) |
| NCT02599961 | Open-label extension, UX007 long-term safety (enrollment 15) | TERMINATED ("halted prematurely due to lack of efficacy") | PHASE2 | UX007 (triheptanoin) | Ultragenyx | 2015-09-10 |
| NCT02960217 | Crossover, UX007 for movement disorders in Glut1 DS | TERMINATED | PHASE3 | UX007; Placebo (DRUG) | Ultragenyx | 2017-04-19 |
| NCT02036853 | Open-label triheptanoin, GLUT1DS (enrollment 20) | COMPLETED | PHASE2 | Triheptanoin (DRUG) | Cook Children's (Adrian Lacy) | 2014-02-20 |
| NCT04137692 | RBC exchange transfusion for GLUT1 deficiency | SUSPENDED ("PI is transferring institutions") | NA | Red Blood Cell Transfusion (OTHER) | Weill Cornell | 2027-09 (estimated) |
| NCT02013583 | G1D Registry | COMPLETED | observational | No intervention | UT Southwestern | 2013-12 |
| NCT04112862 | Sodium lactate infusion in GLUT1DS | COMPLETED | EARLY_PHASE1 | sodium lactate (OTHER) | Radboud UMC | 2022-05-20 |
| NCT03202108 | Krio in children and adults with epilepsy | WITHDRAWN ("Product manufacturing issues.") | NA | Krio (DIETARY_SUPPLEMENT) | Vitaflo | 2018-05-11 |
| NCT03655223 | Early Check: Expanded Screening in Newborns | ACTIVE_NOT_RECRUITING | observational | Confirmatory Testing (DIAGNOSTIC_TEST) | RTI International | 2018-10-15 |
| NCT05687474 | Baby Detect: Genomic Newborn Screening | COMPLETED | not visible | not visible | CHU Liège | 2022-09-01 (from summary only) |

A truncated record, NCT02018315, appeared with no other fields visible.

**Key trial results:**
- NCT02960217 (verbatim): the primary outcome of movement disorder frequency gave a Hodges-Lehmann median difference of 1.46 (95% CI -1.12 to 4.36), p = 0.2684. This was not significant. Randomized n = 43.
- NCT02599961 was terminated for lack of efficacy.

**Coverage gaps:** The CT.gov response was not fully read, and the full list may include more GLUT1 trials. The PMC and Wiley full text was not obtained.

## Summary

Most of the MGI data came through. The Alliance and IMPC pages returned little usable content, the Slc2a1 Europe PMC search failed with a 503, and the MGI ID given for stomatin points to a different gene. Nothing I read shows a red cell, hemolysis, or cation-leak phenotype in any Slc2a1 or Stom model.

## 1. MGI, Slc2a1 (https://www.informatics.jax.org/marker/MGI:95755)

- **MGI ID:** MGI:95755. NCBI Gene 20525. Ensembl ENSMUSG00000028645.
- **Synonyms:** Glut-1, Glut1, M100200, Rgsc200.
- **Mouse location:** Chr4, GRCm39 chr4:118966001-118994527 (+ strand). The cM value did not render.
- **Human ortholog:** SLC2A1, HGNC:11005, NCBI 6513, UniProt P11166, on 1p34.2.
- **Alleles:** 69 total, per the marker page. By type: gene trapped 53, targeted 7, endonuclease-mediated 5, chemically induced (other) 2, chemically induced (ENU) 1, radiation induced 1. 63 strains or lines are listed in IMSR.
- **Named alleles:** I could only identify one. Slc2a1Rgsc200 (MGI:3811855), used in strain B6(D2)-Slc2a1Rgsc200 (MGI:7664091), with reference J:281292. The allele summary page (https://www.informatics.jax.org/allele/summary?markerId=MGI:95755) loaded only its template, so the full table of symbols is not available from this fetch.
- **Phenotype summary (MGI's own annotation text, paraphrased):**
  - Homozygous null embryos are small, lack visible eyes, show developmental delay, and die at E10 to E14.
  - Heterozygotes show spontaneous seizures, impaired motor performance, low cerebrospinal fluid glucose (hypoglycorrhachia), microcephaly, and reduced brain glucose uptake.
  - Mice homozygous for p.P485L die just after birth. The allele symbol for this is not shown; it may be the ENU allele, but that is my inference.
- **Phenotype categories:** The page lists 36 phenotypes from 4 alleles across 7 backgrounds. Eleven categories have annotation links, including behavior/neurological, nervous system, embryo, growth/size/body, mortality/aging, and hematopoietic system. The contents of the hematopoietic link were not read.
- **Disease model:** One mouse model, Slc2a1Rgsc200/Slc2a1+, is annotated to "glucose transporter type 1 deficiency syndrome 1" (DOID:0070561, OMIM:606777). The page gives no phenotype details for it.

## 2. Alliance (https://www.alliancegenome.org/gene/MGI:95755)

The page returned only its title, with no content. I could not get orthologs or disease annotations from it. The MGI page does give some ortholog data: human as above, rat, two zebrafish (slc2a1a and slc2a1b, per ZFIN links), and Xenopus slc2a1 (Xenbase). I did not find Drosophila or C. elegans identifiers.

## 3. IMPC (https://www.mousephenotype.org/data/genes/MGI:95755)

- The page is JavaScript-rendered. Its tables show "Loading..." and no data.
- It reports 0 significant phenotypes and 0 of 24 physiological systems tested.
- It lists 12 associated diseases, but the list did not load.
- The viability section is named, but no outcome is shown.
- **Viability:** The MGI annotation above says homozygous nulls die at E10 to E14. I could not confirm this from IMPC.
- **Hematology:** Nothing shown.

## 4. Europe PMC, GLUT1 mouse model search

This fetch failed with HTTP 503, and no Retry-After was given. Retrying would likely fail the same way, so I did not retry. As a result I could not verify Wang D et al., Ann Neurol 2006, or any haploinsufficient Slc2a1+/- model paper. I have not filled this from memory.

## 5. Stomatin

- **MGI:1095733 is not stomatin.** The URL https://www.informatics.jax.org/marker/MGI:1095733 is Pros1 (protein S), which is associated with neonatal thrombosis and hemorrhage in knockouts. I did not guess a different Stom ID, so the correct MGI ID for Stom is still unknown.
- **Europe PMC stomatin search** (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE_ABS%3A%22stomatin%22%20AND%20TITLE_ABS%3A(%22knockout%22%20OR%20%22deficient%20mice%22)&resultType=core&format=json&pageSize=20) returned 17 hits. The verbatim part of the response covered only the first few. The remaining records come from a model-extracted summary, so treat the details below as unverified.
  - Sedensky-type study, Anesthesiology 2006 (PMID 16931982): stomatin-deficient mice were about 12% more sensitive to diethyl ether, with no locomotion defect. The abstract reports no red blood cell data.
  - Stoml3 knockout mice: olfactory discrimination and mechanosensation. No red cell data.
  - Stoml2 knockout mice (PMID 41619509): normal spermatogenesis and fertility. No red cell data.
  - Stomatin knockout in neutrophils (PMID 38185615, Burns 2024) and in macrophages (PMID 36719247, mSphere 2023): immune cell data only.
- **Stom-null red cell phenotype:** None of the papers in this set reports cation leak, hemolysis, cryohydrocytosis, or osmotic fragility in stomatin-deficient mice. As far as this search shows, no Stom-null red cell model has been published. That is a negative finding from one search, not proof of absence.

## 6. OMIA (https://omia.org/results/?search_type=advanced&gene=SLC2A1)

- The search returned 6152 phene records, but the gene filter did not appear to apply. The rows are sorted alphabetically across all species, and the visible portion stops partway through the B entries.
- The gene-record view (https://omia.org/results/?search_type=advanced&gene=SLC2A1&result_type=gene) lists 1959 records, but only reached LHX1B on the visible page. SLC2A1 would sort after that point.
- **Result:** No SLC2A1 entry is visible in either view. The check is incomplete, not negative. A direct OMIA search by gene name is needed to settle this.

## Final URLs read

- https://www.informatics.jax.org/marker/MGI:95755
- https://www.informatics.jax.org/allele/summary?markerId=MGI:95755
- https://www.alliancegenome.org/gene/MGI:95755 (title only)
- https://www.mousephenotype.org/data/genes/MGI:95755
- https://www.informatics.jax.org/marker/MGI:1095733 (this is Pros1)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE_ABS%3A%22stomatin%22%20AND%20TITLE_ABS%3A(%22knockout%22%20OR%20%22deficient%20mice%22)&resultType=core&format=json&pageSize=20
- https://omia.org/results/?search_type=advanced&gene=SLC2A1
- https://omia.org/results/?search_type=advanced&gene=SLC2A1&result_type=gene

The Slc2a1 Europe PMC search (step 4) was not read, because it returned 503.

## Task 1: Lande, Thiemann, Mentzer 1982 (PMID 7174793)

**Bottom line:** I got the metadata and the abstract. I could not get the article body, so the patients' clinical features, red cell Na and K values, flux data, temperature dependence, and lipid findings are not available from my reads. The source is not pre-approved, so I paraphrased the abstract and kept quotes short.

**PMCID:** PMC370348 is wrong. Europe PMC gives **PMC370344**.
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC370348/` returned HTTP 200 with a reCAPTCHA "Checking your browser" page, not the article.
- `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC370344/fullTextXML` returned **HTTP 500**. I did not retry it.
- `https://www.jci.org/articles/view/110726` has the abstract and "Free access" status. The body is only scanned page images (pp. 1273–1280).
- `https://www.jci.org/articles/view/110726/pdf` returned the HTML article page again, not the PDF text.

**Metadata (Europe PMC search):** Title "Missing band 7 membrane protein in two patients with high Na, low K erythrocytes." Authors Lande WM, Thiemann PV, Mentzer WC (Jr). J Clin Invest 1982 Dec;70(6):1273-1280. DOI 10.1172/jci110726. PMCID PMC370344. Europe PMC lists `isOpenAccess: "N"` but `inPMC: "Y"` and free full-text links (Europe PMC HTML, PDF render, and JCI PDF). Grant NHLBI HL27058. MeSH: Erythrocytes/analysis, Erythrocyte Membrane/analysis, Anemia, Hemolytic/blood, Potassium/blood, Sodium/blood, Membrane Proteins/analysis, Cell Membrane Permeability.

**Abstract (paraphrased; quotes limited):**
- Two patients with congenital hemolytic anemia from increased erythrocyte permeability to Na and K, described as hereditary stomatocytosis and cryohydrocytosis.
- One-dimensional SDS gel electrophoresis split band 7 into three components of approximately 30,000, 28,000 and 26,000 daltons. The 28,000-dalton component was decreased in both patients.
- Two-dimensional electrophoresis resolved the 28,000-dalton component into two proteins with different isoelectric points, named 22 x 8 and 60 x 8. In both patients, 22 x 8 was "completely absent," while 60 x 8 was detected as usual.
- Normal subjects and reticulocytosis controls had all band 7 proteins, including 22 x 8.
- Conclusion (hedged): the missing band 7 protein "raises the possibility" that its absence causes the increased Na and K permeability.

**Not retrieved:** clinical features of the two patients, red cell Na and K (mmol/L), cation flux and temperature dependence, membrane lipid findings, and the full conclusions section. The abstract gives no Na or K values.

**Unfetched alternative:** `https://europepmc.org/articles/PMC370344?pdf=render` is listed by Europe PMC as a free PDF. I did not fetch it because it was not one of the routes you named.

## Task 2: ORPHA:168577

**Core identifiers and text (from orphadata cross-referencing, 2026-06-23 record, and ORDO):**
- ORPHA code: **168577**
- Preferred term: "Hereditary cryohydrocytosis with reduced stomatin"
- Synonyms: "CHC type 2"; "Hereditary cryohydrocytosis type 2"; "Stomatin-deficient cryohydrocytosis"; "sdCHC"
- Definition (paraphrased): a rare hemolytic anemia with neurologic features (psychomotor delay, seizures, variable movement disorders) plus hemolytic anemia with stomatocytosis. Cation-leaky erythrocytes cause pseudohyperkalemia, hemolytic crises and hepatosplenomegaly. Cataracts can be a presenting feature.

**Cross-references:**
- ICD-10: **D58.8** (Orphanet-attributed code; the ORPHA entity is narrower, "NTBT")
- ICD-11: **3A10.Y** (index term; narrower, "NTBT")
- MONDO: **0012143** (exact)
- OMIM: **608885** (exact)
- UMLS: **C5190707** (exact)
- MeSH, MedDRA, GARD: none listed in either source

**Epidemiology (orphadata):**
- Prevalence class: "<1 / 1 000 000" (point prevalence, worldwide, class only)
- Cases/families: 3.0 (worldwide, source PMID 22492876)

**Age of onset and inheritance:** Only ORDO gives these: age of onset "Infancy", "Neonatal"; inheritance "Autosomal dominant". The orphadata natural-history and classification endpoints failed (see below), and the epidemiology endpoint has no such fields. Treat these two values as single-source.

**HPO phenotypes (orphadata rd-phenotypes, 32 entries, last validated 2019-09-13):**
- Frequent (79-30%): Cataract HP:0000518; Jaundice HP:0000952; Intellectual disability HP:0001249; Seizure HP:0001250; Global developmental delay HP:0001263; Hepatosplenomegaly HP:0001433; Increased intracellular sodium HP:0003575; Stomatocytosis HP:0004446; Spontaneous hemolytic crises HP:0005525; Postnatal growth retardation HP:0008897; Hypoglycorrhachia HP:0011972.
- Occasional (29-5%): Microcephaly HP:0000252; Macrocephaly HP:0000256; Macrotia HP:0000400; Short neck HP:0000470; Broad neck HP:0000475; Nystagmus HP:0000639; Brachydactyly HP:0001156; Ataxia HP:0001251; Spastic paraplegia HP:0001258; Hypertonia HP:0001276; Communicating hydrocephalus HP:0001334; Recurrent infections HP:0002719; Conjugated hyperbilirubinemia HP:0002908; Short stature HP:0004322; Intracerebral periventricular calcifications HP:0007229; Short thorax HP:0010306; Zonular cataract HP:0010920; Cerebral white matter hypoplasia HP:0012430; Delayed myelination HP:0012448; Decreased thalamic volume HP:0012695; Abnormality of movement HP:0100022.
- Phenotype sources (PMIDs): 7174793, 21791420, 15071792, 22492876, 15180870.

**ORDO (ebi OLS4, ORDO_en_4.9):** Same definition, synonyms, and cross-references as above. Also gives age of onset and inheritance as noted.

**Failures:**
- (b) classifications: `https://api.orphadata.com/rd-classification/orphacodes/168577/classifications?lang=en` returned **HTTP 404**. Not retried. No classification hierarchy obtained.
- (f) natural history: `https://api.orphadata.com/rd-natural-history/orphacodes/168577?lang=en` returned **HTTP 404**. Not retried.
- (c) `en_product1.xml`: not fetched. Not needed given the other endpoints.
- No endpoint asked for a key. The orphadata routes (a), (d), (e) and the ORDO route all returned data.

**URLs read:**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC370348/
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7174793&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/PMC370344/fullTextXML
- https://www.jci.org/articles/view/110726
- https://www.jci.org/articles/view/110726/pdf
- https://api.orphadata.com/rd-cross-referencing/orphacodes/168577?lang=en
- https://api.orphadata.com/rd-classification/orphacodes/168577/classifications?lang=en
- https://api.orphadata.com/rd-phenotypes/orphacodes/168577?lang=en
- https://api.orphadata.com/rd-epidemiology/orphacodes/168577?lang=en
- https://api.orphadata.com/rd-natural-history/orphacodes/168577?lang=en
- https://www.ebi.ac.uk/ols4/api/ontologies/ordo/terms?iri=http%3A%2F%2Fwww.orpha.net%2FORDO%2FOrphanet_168577

## Paper 1: Ntoumaziou A et al., "Cryohydrocytosis: When Cold Breaks the Membrane," Am J Hematol 2026;101(6):1217-1219

Retrieved via Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13139882/fullTextXML. The full text was read. It is a short "Images in Hematology" case report with one figure. I did not fetch the Wiley URL because Europe PMC succeeded.

- **Case:** An 8-week-old male, born at 33 weeks, with a reported family history of spherocytosis. He had congenital non-immune hemolytic anemia and prolonged neonatal hyperbilirubinemia treated with phototherapy. At 8 weeks: Hb 8.8 g/dL, platelets 477 x 10^3/µL, absolute reticulocytes 0.2526 x 10^6/µL (9.8%). The smear showed numerous stomatocytes. The father had been presumed to have HS since childhood and carries the same variant.
- **Gene and variant:** Heterozygous NM_000342.4:c.2286T>A, p.(Ser762Arg) in SLC4A1 (band 3). The text says this is a "known pathogenic variant."
- **Mechanism (verbatim):** the variant alters band 3 "into a temperature-sensitive, leaky cation conduit causing cryohydrocytosis (CHC)."
- **Ektacytometry:** At room temperature, about 2 h after draw, the proband's curve showed decreased Omin, EImax, and Ohyp. After 14 and 24 h at 4°C it shifted right, with "a dramatic increase in Omin and Ohyp." The father's sample showed the same pattern (not shown).
- **Red cell indices:** The father's Advia histograms showed normocytic cells with mildly increased HC at room temperature. After 24 h at 4°C, HC decreased and volume increased, which the authors read as cell swelling. No numeric MCV or MCHC values are given in the text for either patient.
- **Cation flux:** After about 2 h at room temperature, intracellular Na+ was slightly raised and K+ slightly decreased. After 24 h at 4°C, the text describes "massive influx of Na+ along with K+ leak." Exact values appear only in Figure 1D, which I could not read. The legend gives reference ranges: Day 0 Na+ 11.7-37.9 and K+ 260.9-315.2; Day 1 Na+ 12.7-66.1 and K+ 257.8-334.2.
- **Potassium at different temperatures:** The text gives no plasma potassium values at any temperature. The only temperature data are the qualitative temperature-dependence statements below.
- **Temperature dependence (verbatim):** "pronounced sodium influx and potassium efflux at 4°C–8°C," with a mild leak at 37°C partly offset by an overactive Na+/K+ pump, and minimal leak "around 23°C (RT)."
- **Subtype classification (verbatim):** "CHC is a rare, autosomal dominant, hemolytic anemia classified as a subtype of stomatocytosis." It is caused by missense SLC4A1 variants clustering in transmembrane helices 8-12.
- **Stomatin-deficient CHC and SLC2A1/GLUT1:** Not mentioned anywhere in the article.
- **Clinical features:** "Clinically, patients present with hemolytic anemia of mild or moderate severity, jaundice, fatigue, and splenomegaly."
- **Diagnosis (verbatim):** "A distinctive laboratory finding is pseudohyperkalemia due to potassium leak from fragile RBCs" (paraphrased in part). The authors recommend RBC permeability studies plus genetic testing for definitive diagnosis. They also say that "Patient education about cold avoidance and maintaining their specimens at RT prior to analysis is essential."
- **Management:** "Management is primarily supportive." The authors write that splenectomy "is contraindicated because it does not improve the hemolysis." They cite thromboembolic and pulmonary hypertension risks. They suggest prophylactic anticoagulation for CHC patients who have had a splenectomy.

## Paper 2: Lee H, Ryu SW, Hong J, "Case Report: Atypical hepatobiliary manifestations associated with erythrocyte membrane instability in glucose transporter type 1 deficiency syndrome," Front Pediatr 2026;14:1790301

Retrieved via Europe PMC JATS XML: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13230118/fullTextXML. The Frontiers HTML at https://www.frontiersin.org/articles/10.3389/fped.2026.1790301/full was also read and matches the XML. Both were truncated at Table 2, and the tail was only summarized. The Frontiers summary said the abstract was not present, but its verbatim portion does include it, and the XML confirms it. I did not use the Frontiers summary for any claim.

- **Abstract:** I cannot reproduce it in full because the article is not on the preapproved list and quotes are capped at 125 characters. Key sentences:
  - Background: "GLUT1 deficiency syndrome (GLUT1DS) is a rare neurometabolic disorder caused by pathogenic variants in SLC2A1."
  - Case: "We report a boy diagnosed with GLUT1DS at five years of age who presented with intractable seizures."
  - Case: "A temperature-dependent potassium leak test demonstrated cold-enhanced cation leakage."
  - Conclusion: "This case expands the phenotypic spectrum of GLUT1DS by linking erythrocyte membrane instability to recurrent hemolysis."
- **Patient:** A boy, 5.5 years old at referral. Born at 37+5 weeks, birth weight 2.5 kg, exchange transfusion for severe neonatal jaundice on day 3. He had congenital cataracts, developmental delay, and periventricular leukomalacia on neonatal MRI. Recurrent poorly controlled seizures began at 10 months. At referral he weighed 17 kg (8th percentile) and was wheelchair-dependent.
- **Variant:** NM_006516.3:c.1306_1308del (p.Ile436del), heterozygous in-frame deletion. Classified as likely pathogenic (ACMG PS3, PM4, PM1, PM2). Not found in either parent or the sibling, so likely de novo, with germline mosaicism not excluded.
- **Co-occurring UGT1A1 variants:** c.335C>G (p.Thr112Arg), a variant of uncertain significance, plus three promoter variants (c.-3275T>G, c.-3152G>A, c.-41_-40dup). The authors judge these to be "modifiers of bilirubin metabolism rather than causative factors."
- **Clinical course (Table 1 and text):**
  - Initial (5.5 y): Hb 13.4, MCV 101.8, TB 2.5, DB 1.1. Splenomegaly 10 cm on ultrasound.
  - Ketogenic diet (KD) started at diagnosis. The KD was later stopped about two years before the next presentation because of adherence problems.
  - At about 9 years: several months of nausea and new jaundice. Hb 11.3, MCV 104.9, reticulocytes 12.2%, TB 14.6, DB 9.3. Smear showed stomatocytes and echinocytes, with low haptoglobin and raised plasma Hb.
  - At 11.2 years: abdominal pain and severe cholestatic hepatitis. TB 27.4, DB 19.2, AST 51, ALT 119. Rising to TB/DB 30.8/22.2 before ERCP with stone removal and stent placement.
  - At 11.5 years: after a febrile respiratory infection, Hb 9.3, MCV 103.7, reticulocytes 11.9%, TB 6.4, DB 1.4. This was read as another hemolytic episode.
  - At 11.6 years (follow-up): Hb 12.1, reticulocytes 6.5%, TB 2.7, DB 0.8.
- **Hemolysis:** The text attributes the recurrent episodes to hemolysis. Quoted: "hemolysis represents the predominant pathogenic mechanism." The precipitants noted in the verbatim text are the febrile infection and the physical therapy that had been withheld.
- **Gallstones and cholestasis:** MRCP at about 9 years showed gallbladder and common bile duct stones with ductal dilatation. Treated with ursodeoxycholic acid, which improved symptoms and cholestasis, and folate for presumed chronic hemolysis. Later ERCP cleared the common bile duct stones.
- **Potassium leak test:** The method is cited to refs 4 and 5 ("conducted as previously described"). The test was run on heparinized whole blood at 20-25°C and at 2-4°C. Plasma potassium rose over time at both temperatures, more steeply when refrigerated. Figure 4A shows the curves over about 6 h, but I could not read its numeric values. Figure 4B shows more stomatocytes on the refrigerated smear. The authors conclude this confirmed "pseudohyperkalemia and cryohydrocytosis."
- **Treatment:** KD (started at diagnosis, later stopped), ursodeoxycholic acid, folate, and ERCP with stone removal and stent. Cholecystectomy and splenectomy are not mentioned in the verbatim text. Neither is mentioned in the portion summarized after Table 2.
- **Mechanism (verbatim discussion):** "hemolysis in GLUT1DS is caused by a dual functional defect: impaired glucose transport and pathological cation leakage." The authors attribute the leakage to tertiary structural changes that widen the GLUT1 pore region. They write that "rather than erythrocyte glucose deprivation alone, drives erythrocyte fragility." Cryohydrocytosis is described as Na+ and K+ leakage at 0-4°C. GLUT1DS is not classed as hereditary stomatocytosis, but "both conditions share features of altered erythrocyte cation permeability."
- **Genotype-phenotype (verbatim):** Cases with hemolysis, pseudohyperkalemia, or cryohydrocytosis "have frequently involved a subset of SLC2A1 variants affecting the C-terminal transmembrane domains of GLUT1, particularly in-frame deletions." The authors say the p.Ile436del variant "has not been reported in these cohorts." Table 2 lists prior cases, including p.Gly286Asp (Fricke 2004) and p.Ile435 or 436del (Flatt 2011). I did not read the table's full rows.

**Not read verbatim:** the rest of Table 2, the end of the Discussion, the references, and the detailed leak-test numbers in Figure 4A. The summarized tail of either page is unverified and I did not rely on it. Any quotes from that summary (for example, about prolonged fasting or sustained KD) should be treated as unconfirmed.

## Summary

- **Task 1 (ClinVar):** Complete. The first search matched 172 records and returned 100 IDs (`retmax=100`), so 72 hits were not retrieved. The second search matched 174 records; its 50 IDs are the first 50 of the first list, so they are covered by the table below. All 100 summaries were retrieved, but in batches, because the tool truncated large responses.
- **Task 2 (gnomAD):** Obtained from the gnomAD GraphQL API. The response does not name the gnomAD dataset version; the query specified GRCh38. The other fallbacks (Ensembl, DECIPHER, GenCC) were not needed.
- **Task 3 (NCBI Gene):** Complete. The summary text is limited in this report (see the note there).

## Task 1: ClinVar

**Searches**
- (a) `"Hereditary cryohydrocytosis with reduced stomatin"[All Fields]`: count 172, 100 IDs returned.
- (c) `SLC2A1[gene] AND cryohydrocytosis[All Fields]`: count 174, 50 IDs returned. Its ID list is identical to the first 50 IDs of (a).

**Trait codes:** A = Hereditary cryohydrocytosis with reduced stomatin; B = GLUT1 deficiency syndrome 1, autosomal recessive; C = Childhood onset GLUT1 deficiency syndrome 2; D = Encephalopathy due to GLUT1 deficiency; E = Dystonia 9; F = Epilepsy, idiopathic generalized, susceptibility to, 12; G = not provided; H = SLC2A1-related disorder; I = Inborn genetic diseases; J = not specified.

**Review codes:** MS = criteria provided, multiple submitters, no conflicts; SS = criteria provided, single submitter; CC = criteria provided, conflicting classifications.

All titles use transcript NM_006516.4(SLC2A1). "no date" means the record returned the placeholder 1/01/01 as the last-evaluated date.

| # | UID | HGVS title | Type | Germline classification (last evaluated) | Review | Traits |
|---|---|---|---|---|---|---|
| 1 | 5006594 | NM_006516.4(SLC2A1):c.1405C>T (p.Gln469Ter) | SNV | Uncertain significance (no date) | SS | A,C,D,E,F |
| 2 | 3584186 | NM_006516.4(SLC2A1):c.1407G>T (p.Gln469His) | SNV | Uncertain significance (2024/05/01) | SS | A,C,D,E,F |
| 3 | 3376227 | NM_006516.4(SLC2A1):c.680-12C>A | SNV | Likely pathogenic (2022/05/09) | SS | A |
| 4 | 2682545 | NM_006516.4(SLC2A1):c.2T>G (p.Met1Arg) | SNV | Pathogenic/Likely pathogenic (2023/11/15) | MS | D,H |
| 5 | 2197801 | NM_006516.4(SLC2A1):c.1084C>T (p.Pro362Ser) | SNV | Uncertain significance (2024/10/30) | MS | A,B,C,D,E,F,J |
| 6 | 2182226 | NM_006516.4(SLC2A1):c.1342A>G (p.Thr448Ala) | SNV | Uncertain significance (2025/02/05) | MS | A,B,C,D,E,F,G |
| 7 | 2108956 | NM_006516.4(SLC2A1):c.275G>A (p.Arg92Gln) | SNV | Conflicting classifications of pathogenicity (2025/10/01) | CC | A,B,C,D,E,F,G |
| 8 | 2056982 | NM_006516.4(SLC2A1):c.1012C>T (p.Leu338Phe) | SNV | Uncertain significance (2025/01/22) | MS | A,B,C,D,E,F,G |
| 9 | 1721931 | NM_006516.4(SLC2A1):c.1130C>A (p.Ala377Asp) | SNV | Conflicting classifications of pathogenicity (2025/04/21) | CC | A,B,C,D,E,F,G |
| 10 | 1708121 | NM_006516.4(SLC2A1):c.250G>A (p.Gly84Ser) | SNV | Uncertain significance (2023/07/06) | MS | A,C,D,E,F,G,I |
| 11 | 1708118 | NM_006516.4(SLC2A1):c.484C>G (p.Leu162Val) | SNV | Uncertain significance (2022/06/30) | SS | A |
| 12 | 1447855 | NM_006516.4(SLC2A1):c.1260G>A (p.Met420Ile) | SNV | Conflicting classifications of pathogenicity (2025/12/18) | CC | A,B,C,D,E,F,G |
| 13 | 1446752 | NM_006516.4(SLC2A1):c.374G>C (p.Gly125Ala) | SNV | Uncertain significance (2026/02/24) | MS | A,B,C,D,E,F,G |
| 14 | 1439394 | NM_006516.4(SLC2A1):c.266G>A (p.Arg89His) | SNV | Uncertain significance (2025/04/15) | MS | A,B,C,D,E,F,H |
| 15 | 1402777 | NM_006516.4(SLC2A1):c.121G>A (p.Glu41Lys) | SNV | Uncertain significance (2025/07/21) | MS | A,B,C,D,E,F,H |
| 16 | 1375401 | NM_006516.4(SLC2A1):c.757C>T (p.Arg253Trp) | SNV | Uncertain significance (2026/01/12) | MS | A,B,C,D,E,F,G |
| 17 | 1333113 | NM_006516.4(SLC2A1):c.1278+31_1278+32insCTCACCATTT | Insertion | Benign (2021/07/15) | SS | A,C,D,E |
| 18 | 1320581 | NM_006516.4(SLC2A1):c.523G>A (p.Gly175Ser) | SNV | Conflicting classifications of pathogenicity (2025/11/03) | CC | A,B,C,D,E,F,G |
| 19 | 1314217 | NM_006516.4(SLC2A1):c.439G>A (p.Val147Met) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 20 | 1308217 | NM_006516.4(SLC2A1):c.646A>G (p.Ile216Val) | SNV | Uncertain significance (2025/08/27) | MS | A,B,C,D,E,F,G |
| 21 | 1307401 | NM_006516.4(SLC2A1):c.1450C>T (p.His484Tyr) | SNV | Uncertain significance (2025/06/25) | MS | A,B,C,D,E,F,G |
| 22 | 1304066 | NM_006516.4(SLC2A1):c.1192G>A (p.Gly398Ser) | SNV | Uncertain significance (2024/10/08) | MS | A,B,C,D,E,F,G |
| 23 | 1264296 | NM_006516.4(SLC2A1):c.957C>A (p.Ala319=) | SNV | Likely benign (2023/06/05) | MS | A,B,C,D,E,F,G |
| 24 | 1218965 | NM_006516.4(SLC2A1):c.587C>T (p.Pro196Leu) | SNV | Uncertain significance (2023/10/16) | MS | A,B,C,D,E,F,G |
| 25 | 1203673 | NM_006516.4(SLC2A1):c.1297G>A (p.Val433Ile) | SNV | Conflicting classifications of pathogenicity (2025/09/17) | CC | A,B,C,D,E,F,G,I |
| 26 | 1192119 | NM_006516.4(SLC2A1):c.684A>G (p.Leu228=) | SNV | Likely benign (2023/04/11) | MS | A,B,C,D,E,F,G |
| 27 | 1189059 | NM_006516.4(SLC2A1):c.399C>A (p.Cys133Ter) | SNV | Pathogenic (2025/11/20) | MS | A,C,D,E,F,G |
| 28 | 1182494 | NM_006516.4(SLC2A1):c.586C>G (p.Pro196Ala) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 29 | 1101313 | NM_006516.4(SLC2A1):c.312C>T (p.Phe104=) | SNV | Likely benign (2025/08/15) | MS | A,B,C,D,E,F,G,I |
| 30 | 1093513 | NM_006516.4(SLC2A1):c.1069C>T (p.Leu357=) | SNV | Likely benign (2023/08/30) | MS | A,B,C,D,E,F,J |
| 31 | 1057778 | NM_006516.4(SLC2A1):c.630T>A (p.Ser210Arg) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 32 | 1047248 | NM_006516.4(SLC2A1):c.1435C>A (p.Pro479Thr) | SNV | Likely benign (2025/04/01) | MS | A,B,C,D,E,F,G |
| 33 | 1046974 | NM_006516.4(SLC2A1):c.679+5G>A | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 34 | 1031052 | NM_006516.4(SLC2A1):c.1348T>A (p.Phe450Ile) | SNV | Uncertain significance (2025/02/16) | MS | A,B,C,D,E,F,G |
| 35 | 992655 | NM_006516.4(SLC2A1):c.787T>C (p.Phe263Leu) | SNV | Uncertain significance (2026/03/28) | MS | A,C,D,E,F,G |
| 36 | 985976 | NM_006516.4(SLC2A1):c.625G>A (p.Glu209Lys) | SNV | Uncertain significance (2024/11/15) | MS | A,B,C,D,E,F,G,I |
| 37 | 985526 | NM_006516.4(SLC2A1):c.152G>A (p.Arg51His) | SNV | Uncertain significance (2024/08/29) | MS | A,B,C,D,E,F,G,I |
| 38 | 973266 | NM_006516.4(SLC2A1):c.1028dup (p.Met344fs) | Duplication | Pathogenic (2018/10/30) | SS | A,C,D,E |
| 39 | 951860 | NM_006516.4(SLC2A1):c.991G>A (p.Ala331Thr) | SNV | Uncertain significance (2024/01/20) | MS | A,B,C,D,E,F,G |
| 40 | 944647 | NM_006516.4(SLC2A1):c.511G>A (p.Ala171Thr) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 41 | 943804 | NM_006516.4(SLC2A1):c.392T>C (p.Val131Ala) | SNV | Uncertain significance (2024/04/23) | MS | A,B,C,D,E,F,I |
| 42 | 876778 | NM_006516.4(SLC2A1):c.798C>T (p.Pro266=) | SNV | Benign/Likely benign (2026/03/01) | MS | A,B,C,D,E,F,G |
| 43 | 842670 | NM_006516.4(SLC2A1):c.668G>A (p.Arg223Gln) | SNV | Uncertain significance (2025/10/22) | MS | A,B,C,D,E,F,G,I |
| 44 | 828198 | NM_006516.4(SLC2A1):c.601T>G (p.Cys201Gly) | SNV | Uncertain significance (2023/12/06) | MS | A,B,C,D,E,F,G,H |
| 45 | 806116 | NM_006516.4(SLC2A1):c.763AAG[1] (p.Lys256del) | Microsatellite | Uncertain significance (2025/12/15) | MS | A,B,C,D,E,F,G |
| 46 | 772934 | NM_006516.4(SLC2A1):c.1107C>T (p.Ile369=) | SNV | Likely benign (2025/10/23) | MS | A,B,C,D,E,F,G,J |
| 47 | 757771 | NM_006516.4(SLC2A1):c.123G>A (p.Glu41=) | SNV | Likely benign (2024/09/29) | MS | A,B,C,D,E,F,I |
| 48 | 747060 | NM_006516.4(SLC2A1):c.1134C>T (p.Phe378=) | SNV | Likely benign (2025/07/23) | MS | A,B,C,D,E,F,I |
| 49 | 745206 | NM_006516.4(SLC2A1):c.354C>T (p.Ser118=) | SNV | Likely benign (2025/07/08) | MS | A,B,C,D,E,F |
| 50 | 702163 | NM_006516.4(SLC2A1):c.318C>T (p.Ser106=) | SNV | Likely benign (2025/06/09) | MS | A,B,C,D,E,F,G,I |
| 51 | 697940 | NM_006516.4(SLC2A1):c.939C>T (p.Ser313=) | SNV | Likely benign (2025/09/09) | MS | A,B,C,D,E,F,J |
| 52 | 697103 | NM_006516.4(SLC2A1):c.696C>T (p.Arg232=) | SNV | Likely benign (2023/10/09) | MS | A,B,C,D,E,F,G |
| 53 | 665484 | NM_006516.4(SLC2A1):c.806G>A (p.Arg269His) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F |
| 54 | 663015 | NM_006516.4(SLC2A1):c.73C>A (p.Gln25Lys) | SNV | Uncertain significance (2025/04/01) | MS | A,B,C,D,E,F,G,I,J |
| 55 | 662300 | NM_006516.4(SLC2A1):c.1223G>A (p.Gly408Asp) | SNV | Conflicting classifications of pathogenicity (2025/10/03) | CC | A,B,C,D,E,F |
| 56 | 662199 | NM_006516.4(SLC2A1):c.101A>G (p.Asn34Ser) | SNV | Pathogenic (2025/04/09) | MS | A,B,C,D,E,F,G,H, Seizure |
| 57 | 656374 | NM_006516.4(SLC2A1):c.26C>T (p.Thr9Met) | SNV | Conflicting classifications of pathogenicity (2026/10/20) | CC | A,B,C,D,E,F,G,H,I |
| 58 | 651573 | NM_006516.4(SLC2A1):c.554T>C (p.Leu185Pro) | SNV | Uncertain significance (2024/12/02) | MS | A,B,C,D,E,F,G,I |
| 59 | 626019 | NM_006516.4(SLC2A1):c.75G>A (p.Gln25=) | SNV | Uncertain significance (no date) | SS | A,C,D,E,F |
| 60 | 626018 | NM_006516.4(SLC2A1):c.192C>G (p.Leu64=) | SNV | Conflicting classifications of pathogenicity (2019/09/10) | CC | A,B,C,D,E,F |
| 61 | 619980 | NM_006516.4(SLC2A1):c.161dup (p.Ser55fs) | Duplication | Pathogenic (no date) | SS | A,C,D,E,F |
| 62 | 595526 | NM_006516.4(SLC2A1):c.1171G>A (p.Val391Met) | SNV | Uncertain significance (2025/09/23) | MS | A,B,C,D,E,F,G,I |
| 63 | 594894 | NM_006516.4(SLC2A1):c.322G>A (p.Val108Met) | SNV | Conflicting classifications of pathogenicity (2025/07/21) | CC | A,B,C,D,E,F,G,I |
| 64 | 589975 | NM_006516.4(SLC2A1):c.495C>T (p.Val165=) | SNV | Likely benign (2026/01/22) | MS | A,B,C,D,E,F,H,I |
| 65 | 588477 | NM_006516.4(SLC2A1):c.339G>A (p.Ser113=) | SNV | Likely benign (2025/10/10) | MS | A,B,C,D,E,F,G,I,J |
| 66 | 588214 | NM_006516.4(SLC2A1):c.606C>T (p.Ile202=) | SNV | Likely benign (2026/06/01) | MS | A,B,C,D,E,F,G,I,J |
| 67 | 588187 | NM_006516.4(SLC2A1):c.338C>T (p.Ser113Leu) | SNV | Uncertain significance (2025/01/21) | MS | A,B,C,D,E,F,H,I |
| 68 | 583250 | NM_006516.4(SLC2A1):c.31C>T (p.Arg11Cys) | SNV | Uncertain significance (2024/02/20) | MS | A,B,C,D,E,F,G |
| 69 | 581517 | NM_006516.4(SLC2A1):c.136C>G (p.Gln46Glu) | SNV | Uncertain significance (2025/12/30) | MS | A,B,C,D,E,F,G |
| 70 | 580258 | NM_006516.4(SLC2A1):c.902C>G (p.Ala301Gly) | SNV | Uncertain significance (2023/12/13) | MS | A,B,C,D,E,F,G |
| 71 | 538683 | NM_006516.4(SLC2A1):c.19-5C>T | SNV | Benign/Likely benign (2026/01/11) | MS | A,B,C,D,E,F,G,J |
| 72 | 538681 | NM_006516.4(SLC2A1):c.172C>T (p.Pro58Ser) | SNV | Uncertain significance (2025/09/08) | MS | A,B,C,D,E,F,I |
| 73 | 520805 | NM_006516.4(SLC2A1):c.1001G>A (p.Arg334Gln) | SNV | Uncertain significance (2025/12/16) | MS | A,B,C,D,E,F,G,I |
| 74 | 516467 | NM_006516.4(SLC2A1):c.903G>A (p.Ala301=) | SNV | Conflicting classifications of pathogenicity (2025/10/24) | CC | A,B,C,D,E,F,G,J |
| 75 | 515240 | NM_006516.4(SLC2A1):c.657C>T (p.Asn219=) | SNV | Benign/Likely benign (2026/02/02) | MS | A,B,C,D,E,F,G,I |
| 76 | 514622 | NM_006516.4(SLC2A1):c.750G>A (p.Gln250=) | SNV | Likely benign (2023/04/11) | MS | A,B,C,D,E,J |
| 77 | 512361 | NM_006516.4(SLC2A1):c.972+7C>G | SNV | Likely benign (2023/04/11) | MS | A,B,C,D,E,F,J |
| 78 | 511899 | NM_006516.4(SLC2A1):c.1362G>A (p.Glu454=) | SNV | Likely benign (2025/08/14) | MS | A,B,C,D,E,F,G |
| 79 | 511516 | NM_006516.4(SLC2A1):c.852G>A (p.Leu284=) | SNV | Likely benign (2025/03/17) | MS | A,B,C,D,E,F,J |
| 80 | 509365 | NM_006516.4(SLC2A1):c.1278+12del | Deletion | Conflicting classifications of pathogenicity (2025/07/21) | CC | A,B,C,D,E,F,G,J |
| 81 | 509157 | NM_006516.4(SLC2A1):c.972+20C>G | SNV | Likely benign (2023/11/10) | MS | A,B,C,D,E,F,J |
| 82 | 507123 | NM_006516.4(SLC2A1):c.1152C>T (p.Gly384=) | SNV | Likely benign (2023/04/11) | MS | A,B,C,D,E,F,J |
| 83 | 493037 | NM_006516.4(SLC2A1):c.791G>A (p.Arg264His) | SNV | Uncertain significance (2025/01/17) | MS | A,B,C,D,E,F,G |
| 84 | 493036 | NM_006516.4(SLC2A1):c.946G>A (p.Val316Ile) | SNV | Uncertain significance (2026/02/02) | MS | A,B,C,D,E,F,G |
| 85 | 471348 | NM_006516.4(SLC2A1):c.697G>A (p.Gly233Arg) | SNV | Uncertain significance (2024/01/02) | MS | A,B,C,D,E,F,G |
| 86 | 452565 | NM_006516.4(SLC2A1):c.1418G>A (p.Ser473Asn) | SNV | Uncertain significance (2025/06/22) | MS | A,B,C,D,E,F,G |
| 87 | 449349 | NM_006516.4(SLC2A1):c.907G>T (p.Val303Leu) | SNV | Uncertain significance (2025/06/01) | MS | A,B,C,D,E,F,G |
| 88 | 448410 | NM_006516.4(SLC2A1):c.1005C>G (p.Thr335=) | SNV | Benign/Likely benign (2025/12/01) | MS | A,B,C,D,E,F,G,I |
| 89 | 444164 | NM_006516.4(SLC2A1):c.953C>T (p.Thr318Met) | SNV | Uncertain significance (2025/03/11) | MS | A,B,C,D,E,F,G |
| 90 | 441137 | NM_006516.4(SLC2A1):c.1060G>A (p.Ala354Thr) | SNV | Uncertain significance (2026/09/30) | MS | A,B,C,D,E,F,G |
| 91 | 436751 | NM_006516.4(SLC2A1):c.180G>A (p.Thr60=) | SNV | Likely benign (2025/10/22) | MS | A,B,C,D,E,F,G,I,J |
| 92 | 429618 | NM_006516.4(SLC2A1):c.313G>C (p.Val105Leu) | SNV | Uncertain significance (2023/04/11) | MS | A,B,C,D,E,F,G |
| 93 | 424896 | NM_006516.4(SLC2A1):c.19-207T>C | SNV | Benign (2026/09/01) | MS | A,B,C,D,E,F,G,J |
| 94 | 414166 | NM_006516.4(SLC2A1):c.189G>A (p.Thr63=) | SNV | Likely benign (2025/11/16) | MS | A,B,C,D,E,F,I |
| 95 | 406880 | NM_006516.4(SLC2A1):c.188C>T (p.Thr63Met) | SNV | Conflicting classifications of pathogenicity (2026/01/02) | CC | A,B,C,D,E,F,G,I |
| 96 | 392030 | NM_006516.4(SLC2A1):c.624C>G (p.Pro208=) | SNV | Likely benign (2024/08/22) | MS | A,B,C,D,E,F,G,I |
| 97 | 384863 | NM_006516.4(SLC2A1):c.492C>T (p.Ile164=) | SNV | Likely benign (2025/08/18) | MS | A,B,C,D,E,F,J |
| 98 | 384500 | NM_006516.4(SLC2A1):c.275+17C>T | SNV | Benign/Likely benign (2026/02/02) | MS | A,B,C,D,E,F,J |
| 99 | 384061 | NM_006516.4(SLC2A1):c.822C>T (p.Ile274=) | SNV | Likely benign (2025/10/12) | MS | A,B,C,D,E,F,G,J |
| 100 | 383605 | NM_006516.4(SLC2A1):c.945C>T (p.Ile315=) | SNV | Likely benign (2025/05/27) | MS | A,B,C,D,E,F,G |

Caveat: the trait and classification values were extracted from the raw JSON by the fetch tool's model. Several batches were truncated and re-requested, but I did not check each field against the raw text by hand.

## Task 2: gnomAD constraint for SLC2A1

Source: gnomAD GraphQL API, `https://gnomad.broadinstitute.org/api`, query for `gene_symbol: "SLC2A1"`, `reference_genome: GRCh38`. The response does not state the gnomAD version.

| Metric | Value |
|---|---|
| pLI | 0.9999999792865079 (≈1.00) |
| LOEUF (`oe_lof_upper`) | 0.19642251319410758 |
| `oe_lof` | 0.08583475387880889 |
| `oe_lof_lower` | 0.04227682581970786 |
| missense Z (`mis_z`) | 5.201395250914363 |
| `oe_mis` | 0.5277627646480363 |
| observed LoF (`obs_lof`) | 4 |
| expected LoF (`exp_lof`) | 46.60117049613316 |

## Task 3: NCBI Gene (ID 6513)

Source: `esummary.fcgi?db=gene&id=6513&retmode=json`.

- **Official name:** SLC2A1, "solute carrier family 2 member 1" (nomenclaturestatus: Official).
- **Aliases:** CSE, DYT17, DYT18, DYT9, EIG12, GLUT, GLUT-1, GLUT1, GLUT1DS, HTLVR, PED, SDCHCN.
- **Other designations (selected):** "glucose transporter type 1, erythrocyte/brain"; "receptor for HTLV-1 and HTLV-2"; "dystonia gene 9"; "dystonia gene 18".
- **Location:** chromosome 1, map location 1p34.2. GRCh38 (NC_000001.11): chrstart 42958867, chrstop 42925352, 10 exons. MIM 138140.
- **Summary text:** The 125-character limit for quotes from non-preapproved sources means I cannot reproduce the full summary verbatim here. The first sentence is quoted: "This gene encodes a major glucose transporter in the mammalian blood-brain barrier." The rest, in paraphrase: the protein sits mainly in the cell membrane and surface, where it can also act as a receptor for HTLV-I and HTLV-II; mutations were found in one family with paroxysmal exertion-induced dyskinesia. The summary is credited to RefSeq, Apr 2013.

## URLs read

- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=%22Hereditary+cryohydrocytosis+with+reduced+stomatin%22&retmax=100&retmode=json`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=SLC2A1%5Bgene%5D+AND+cryohydrocytosis&retmax=50&retmode=json`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=…&retmode=json` (ClinVar summaries, requested in batches of 3 to 15 IDs from the search results above)
- `https://gnomad.broadinstitute.org/api?query=…` (gnomAD GraphQL, SLC2A1, GRCh38)
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=6513&retmode=json`

## Summary

All requested sources were reached. The MONDO term came from the first URL, so no fallback was needed. Several model-written summaries in the tool output contradicted the raw JSON, so I checked the disputed points against the raw text or re-fetched them. Items marked **[summary only]** were never seen in raw page text. Treat them as unverified.

## 1. MONDO term (OLS4, first URL, verbatim JSON)

- **MONDO ID:** MONDO:0012143
- **Label:** hereditary cryohydrocytosis with reduced stomatin
- **Definition:** None. The OLS `description` field is empty `[]`, and Monarch's `description` is `null`.
- **Exact synonyms:** "ChC type 2", "hereditary cryohydrocytosis type 2", "sdCHC", "stomatin-deficient cryohydrocytosis"
- **Related synonyms:** "SDCHCN" (type: abbreviation); "cryohydrocytosis, stomatin-deficient, with mental retardation, seizures, cataracts, and massive hepatosplenomegaly" (type: "A synonym that is historic and discouraged")
- **Database cross-references:** GARD:0017036, MEDGEN:332390, MESH:C563840, OMIM:608885, Orphanet:168577, UMLS:C1837206, icd11.foundation:1459095719
- **Exact matches also listed:** https://omim.org/entry/608885, http://www.orpha.net/ORDO/Orphanet_168577, http://identifiers.org/mesh/C563840, http://identifiers.org/medgen/332390, http://linkedlifedata.com/resource/umls/id/C1837206, http://id.who.int/icd/entity/1459095719
- **DOID:** not present on this term.
- **SCTID/SNOMED:** not present on this term.
- **Parents (is_a), from the OLS `/parents` endpoint (4 total):**
  - MONDO:0003689, familial hemolytic anemia
  - MONDO:0017706, disorder of carbohydrate transmembrane transport and absorption
  - MONDO:0020102, hereditary stomatocytosis
  - MONDO:0100601, autosomal dominant syndromic intellectual disability
- **Other:** OLS reports `has_children: false` for this term. Its curated sources include MalaCards pages for both names.

## 2. Monarch entity and HPO associations

**Entity record (verbatim portion):**
- `name`: "hereditary cryohydrocytosis with reduced stomatin". The summary of the rest of the page said the name was "not provided", which is wrong.
- `description`: null
- `category`: biolink:Disease
- Synonyms and xrefs match the OLS record above.
- `has_phenotype_count`: 47

**Causal gene:** SLC2A1 (HGNC:11005), via RO:0004003 "has material basis in germline mutation in", and HP:0000006 autosomal dominant inheritance. **[summary only]** I did not see these in the raw text.

**Associations (`total`: 61, verbatim):** Only a fraction of the 455 KB response was read as raw text. The summary of the rest claimed 13 associations, which contradicts `total: 61`, so I did not use it. The verbatim-visible `biolink:has_phenotype` records, all sourced from Orphanet via HPO annotations (ECO:0000304):

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0001249 | Intellectual disability | Frequent (HP:0040282) |
| HP:0001250 | Seizure | Frequent |
| HP:0001258 | Spastic paraplegia | Occasional (HP:0040283) |
| HP:0001276 | Hypertonia | Occasional |
| HP:0007229 | Intracerebral periventricular calcifications | Occasional |
| HP:0012695 | Decreased thalamic volume | HP:0040283 (label cut off) |
| HP:0000518 | Cataract | Frequent |
| HP:0000952 | Jaundice | Frequent |
| HP:0001263 | Global developmental delay | Frequent |
| HP:0001433 | Hepatosplenomegaly | Frequent |
| HP:0011972 | label not visible | HP:0040282 |

The other 50 associations were not read as raw text, so the list is incomplete. The record I read at offset 139842 was truncated mid-record. Other phenotypes named in the entity record or summaries (e.g., Stomatocytosis HP:0004446, Seizure, Microcephaly HP:0000252) are **[summary only]**.

## 3. HGNC record for SLC2A1 (verbatim XML)

- **HGNC ID:** HGNC:11005
- **Approved symbol:** SLC2A1
- **Approved name:** solute carrier family 2 member 1
- **Previous symbols:** GLUT1, GLUT, HTLVR, CSE
- **Alias symbols:** DYT18, DYT9, GLUT-1
- **Alias names:** "dystonia gene 18", "dystonia gene 9"
- **Location:** 1p34.2
- **Ensembl gene ID:** ENSG00000117394
- **UniProt ID:** P11166
- **NCBI (Entrez) gene ID:** 6513
- **OMIM ID:** 138140
- **RefSeq accession:** NM_006516 (MANE select NM_006516.4 / ENST00000426263.10)

## 4. GO annotations for UniProt P11166 (SLC2A1)

Neither source gives a complete list. QuickGO reports `numberOfHits: 151` and I read only page 1 (about 26 records in raw text). The GO API response is about 203 KB and I read roughly 60% of it. The GO API gives labels, while QuickGO `goName` is null in every record. For that reason, most GO names below are verbatim only where the GO API gave them.

**Molecular Function (verbatim IDs):**
- GO:0055056, D-glucose transmembrane transporter activity. Label **[summary only]**. Several annotations, including IMP ECO:0000315 and IDA.
- GO:0033300, dehydroascorbic acid transmembrane transporter activity. Label **[summary only]**. IEA ECO:0000501 and EXP ECO:0000269.
- GO:0005324, long-chain fatty acid transmembrane transporter activity (verbatim label)
- GO:0022857, transmembrane transporter activity (IEA)
- GO:0015150, fucose transmembrane transporter activity (IEA)
- GO:0042910, xenobiotic transmembrane transporter activity (IEA)
- GO:0005515, protein binding (many IPI annotations)
- GO:0042802, identical protein binding (IPI)
- GO:0019900, kinase binding (IEA)

**Biological Process (verbatim IDs):**
- GO:1904659, "D-glucose transmembrane transport" (verbatim label, ~10 annotations)
- GO:0098708, "D-glucose import across plasma membrane" (verbatim label)
- GO:0070837, "dehydroascorbic acid transport" (verbatim label; IBA, IEA, ECO:0000501)
- GO:0015756, fucose transmembrane transport (IEA)
- GO:0015911, long-chain fatty acid import across plasma membrane (IMP)
- GO:0055085, transmembrane transport (IEA)
- GO:0019852, L-ascorbic acid metabolic process (TAS)
- GO:0150104, transport across blood-brain barrier (verbatim label)
- GO:0007417, central nervous system development (verbatim label)
- GO:0065003, protein-containing complex assembly (verbatim label)
- GO:0071260, cellular response to mechanical stimulus; GO:0071474, cellular hyperosmotic response; GO:1904016, response to thyroglobulin triiodothyronine (verbatim labels in GO API)
- Also seen: GO:0001666 response to hypoxia; GO:0007565 female pregnancy; GO:0021987 cerebral cortex development; GO:0032868 response to insulin; GO:0042908 xenobiotic transport; GO:0045494 photoreceptor cell maintenance

**Cellular Component:**
- None seen in raw text.
- **[summary only]** GO:0005886 plasma membrane (IBA GO_Central, and experimental ECO:0000315), GO:0000139 Golgi membrane, GO:0016323 basolateral plasma membrane, GO:0016324 apical plasma membrane, GO:0045202 synapse, GO:0005737 cytoplasm.

**Requested flags:**
- Glucose transmembrane transport (GO:0015758): not seen in what I read. The related term GO:1904659 is present.
- D-glucose transmembrane transporter activity (GO:0055056): present.
- Dehydroascorbic acid transport: GO:0070837 present (verbatim). Its activity counterpart GO:0033300 is present.
- Plasma membrane (GO:0005886): **summary only**. Not seen in raw text.
- Cation/ion transport: no such term seen in the portions read. This is not a full negative.

## What failed or was unreliable

- No fetch failed outright. Every URL returned HTTP 200.
- Several model summaries contradicted the raw JSON:
  - The QuickGO summary said GO:0055056, GO:0033300, GO:0070837, and GO:0022857 were absent. The raw text shows all of them.
  - The Monarch entity summary said the name was missing. The raw text has it.
  - The first Monarch association summary said 13 associations. `total` is 61.
- I did not read the full GO API or Monarch association responses, so both lists are partial.

**Interpretive note:** This report covers the disease indexed as MONDO:0012143 / OMIM #608885 — *hereditary cryohydrocytosis with reduced stomatin*, i.e. **stomatin-deficient cryohydrocytosis (sdCHC)**, caused by heterozygous variants in **SLC2A1** (GLUT1). This is *not* the band 3/*SLC4A1*-related cryohydrocytosis (CHC type 1), which is a distinct entity; I flag the distinction throughout because the two are conflated in secondary sources. Many primary sources were paywalled or bot-blocked in this session; where I could not reach a full text, I say so and cite only what was retrievable. Verbatim quoting is limited for most non-open-access sources; the Furia et al. 2023 article (CC BY-NC) was read directly as a PDF and is therefore quoted at length.

---

# Hereditary Cryohydrocytosis With Reduced Stomatin (Stomatin-Deficient Cryohydrocytosis, sdCHC)

## 1. Disease Information

### Overview

Hereditary cryohydrocytosis with reduced stomatin is an ultra-rare, autosomal dominant, multisystem disorder caused by heterozygous pathogenic variants in **SLC2A1**, the gene encoding **GLUT1**, the facilitative glucose transporter of the blood–brain barrier and the erythrocyte membrane. It sits at the intersection of two disease families: it is simultaneously (a) a **hereditary stomatocytosis** — a hemolytic anemia caused by abnormal monovalent cation permeability of the red cell membrane, with a leak that is markedly enhanced by cooling ("cryo-hydrocytosis") — and (b) a form of **GLUT1 deficiency syndrome (GLUT1DS)**, with epilepsy, developmental delay, movement disorder and hypoglycorrhachia. Its defining red-cell biochemical marker is near-total absence of the 32-kDa band 7.2b membrane protein **stomatin**, even though the *STOM* gene itself is normal.

Furia et al. (2023) summarize the entity concisely (verbatim from the abstract, *Epileptic Disord*. 2023;25:410–415, DOI [10.1002/epd2.20039](https://doi.org/10.1002/epd2.20039)):

> "Cryohydrocytosis is a form of stomatocytosis characterized by the leakage of sodium and potassium from red blood cells at low temperatures, characterized by pseudohyperkalemia. Stomatin-deficient cryohydrocytosis is an extremely rare variant that only recently has been related to pathogenic variants in the SLC2A1 gene, encoding the main glucose transporter of the blood–brain barrier and red blood cells, GLUT1. It follows that GLUT1 deficiency syndrome, a rare but significant cause of metabolic epilepsy, may present with stomatin-deficient cryohydrocytosis, although this correlation has only been reported in a few instances."

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0012143** — "hereditary cryohydrocytosis with reduced stomatin" |
| OMIM | **#608885** — "STOMATIN-DEFICIENT CRYOHYDROCYTOSIS WITH NEUROLOGIC DEFECTS; SDCHCN" |
| Orphanet | **ORPHA:168577** |
| MedGen | UID **332390**; UMLS CUI **C1837206** |
| MeSH | **C563840** |
| GARD | **0017036** |
| ICD-10 | **D58.8** (Orphanet-attributed; ORPHA entity is narrower than the code) |
| ICD-11 | Foundation entity **1459095719**; index term **3A10.Y** (narrower-than) |
| UMLS (Orphanet mapping) | **C5190707** (note: discrepant with MedGen/MONDO's C1837206) |
| Causal gene | **SLC2A1** — HGNC:**11005**, NCBI Gene **6513**, Ensembl **ENSG00000117394**, UniProt **P11166**, OMIM ***138140**, locus **1p34.2** |
| MANE transcript | NM_006516.4 / ENST00000426263.10 |

Sources: OLS4 MONDO record; Orphadata rd-cross-referencing API for ORPHA:168577; MedGen 332390; HGNC REST (`rest.genenames.org/fetch/symbol/SLC2A1`).

MONDO places the term under four parents, which captures its hybrid nature well: **MONDO:0003689** familial hemolytic anemia; **MONDO:0020102** hereditary stomatocytosis; **MONDO:0017706** disorder of carbohydrate transmembrane transport and absorption; **MONDO:0100601** autosomal dominant syndromic intellectual disability.

### Synonyms and alternative names

From MONDO (exact synonyms): *ChC type 2*; *hereditary cryohydrocytosis type 2*; *sdCHC*; *stomatin-deficient cryohydrocytosis*. Related synonyms: **SDCHCN** (abbreviation); and the historic/discouraged term *"cryohydrocytosis, stomatin-deficient, with mental retardation, seizures, cataracts, and massive hepatosplenomegaly."* MedGen additionally lists *"GLUT1 DEFICIENCY SYNDROME WITH PSEUDOHYPERKALEMIA AND HEMOLYSIS"* and *"Stomatin-deficient cryohydrocytosis with neurologic defects."* GARD adds *sdchc*.

### Nature of the evidence base

All disease-level knowledge derives from **individual published case reports and small case series** (n ≈ 6–8 patients worldwide across 45 years), supplemented by *in vitro* and *Xenopus* oocyte functional work. There is **no registry, no EHR-derived cohort, and no natural-history study** for this specific entity. Aggregated resources (OMIM, Orphanet, HPO, MedGen) re-encode those same few case reports, which is why HPO frequencies for this disease are often literally "1/1" (one patient, PMID:22492876).

---

## 2. Etiology

### Disease causal factors

**Entirely genetic and monogenic.** The disease results from heterozygous, typically *de novo*, pathogenic variants in **SLC2A1** that produce a **dual molecular lesion**: loss of D-glucose transport activity *plus* acquisition of a pathological monovalent-cation leak through (or around) the mutant GLUT1 protein. This dual-defect model is stated explicitly in the most recent case report (Lee H, Ryu SW, Hong J, *Front Pediatr*. 2026;14:1790301, PMID 42245163, PMCID PMC13230118): hemolysis in GLUT1DS is caused by *"a dual functional defect: impaired glucose transport and pathological cation leakage"* — and it is that leakage, *"rather than erythrocyte glucose deprivation alone,"* that *"drives erythrocyte fragility."*

The foundational genetic demonstration is Flatt JF, Guizouarn H, Burton NM, Borgese F, Tomlinson RJ, Forsyth RJ, Baldwin SA, Levinson BE, Quittet P, Aguilar-Martinez P, Delaunay J, Stewart GW, Bruce LJ. *"Stomatin-deficient cryohydrocytosis results from mutations in SLC2A1: a novel form of GLUT1 deficiency syndrome."* **Blood. 2011;118(19):5267–5277. PMID 21791420, DOI 10.1182/blood-2010-12-326645.** (Full text was not reachable in this session — ASH, bloodjournal.org, and both institutional repositories returned HTTP 403.) The abstract establishes that sdCHC is associated with *SLC2A1* mutations causing both loss of glucose transport and a cation leak, demonstrated by expression in *Xenopus* oocytes, with a 3D GLUT1 homology model used to rationalize the two mutations; the paper also shows that stomatin is lost during reticulocyte maturation by endocytosis.

### Genetic risk factors

- **Causal variants:** see §4. Two canonical alleles (p.Gly286Asp; p.Ile435del/p.Ile436del) plus two more recently reported in-frame deletions (p.Ile446del; p.Ile436del in a Korean patient).
- **Susceptibility loci / modifier genes:** none identified for this disorder. No GWAS exists (and could not exist meaningfully at n≈8).
- **Candidate modifier observed once:** Lee et al. (2026) found co-occurring *UGT1A1* variants in their patient — c.335C>G (p.Thr112Arg, VUS) plus promoter variants c.-3275T>G, c.-3152G>A, c.-41_-40dup — which they interpreted as *"modifiers of bilirubin metabolism rather than causative factors."* This is a single-patient observation and should be treated as hypothesis-generating.
- ***STOM* is not mutated.** This is an important negative. Stevens-Hernandez CJ, Flatt JF, Kupzig S, Bruce LJ (*Front Physiol*. 2022;13:834463, PMID 35356079, PMCID PMC8959883) state verbatim: *"sdCHC RBCs also lack stomatin although again there is no associated gene defect in STOM."* Stomatin deficiency is therefore **secondary** to the GLUT1 lesion.

### Environmental risk factors

None are known to cause the disease. However, **environmental and physiological triggers modulate expression of the phenotype**:

- **Cold exposure** is the defining trigger of the red-cell cation leak (in vitro, and for specimen handling). Ntoumaziou et al. (*Am J Hematol*. 2026;101(6):1217–1219, PMID 41793238, PMCID PMC13139882 — writing about band 3 CHC but directly applicable to specimen handling) note *"pronounced sodium influx and potassium efflux at 4°C–8°C"* and advise that *"Patient education about cold avoidance and maintaining their specimens at RT prior to analysis is essential."*
- **Fasting / low glucose availability** worsens the neurological phenotype. Furia et al. note GLUT1DS *"encompasses a spectrum of neurological conditions sharing clinical worsening in states of low glucose availability, most commonly fasting"*; in the Weber et al. family, seizures *"worsened in the morning before breakfast and improved after meals."*
- **Exertion** triggers paroxysmal dyskinesia in the cation-leak-associated *SLC2A1* phenotype (Weber et al., *J Clin Invest*. 2008;118(6):2157–2168, PMID 18451999, PMCID PMC2350432).
- **Febrile infection** precipitated a hemolytic episode in the Lee et al. (2026) patient (Hb fell to 9.3 g/dL, reticulocytes 11.9%).
- **Non-adherence to ketogenic diet** precipitated clinical worsening in both Furia et al. (2023) and Lee et al. (2026).
- **Age, sex, family history:** no sex predilection reported; disease is essentially always *de novo*, so family history is typically negative.

### Protective factors

- **Genetic:** none identified. gnomAD constraint (below) indicates *SLC2A1* loss-of-function is strongly selected against, so protective LoF alleles are not expected.
- **Environmental:** **ketogenic diet therapy** is protective against the neurological manifestations (see §12). **Maintaining samples and patients at ambient temperature** is protective against the artifactual/clinical consequences of the cold-induced leak. **Ursodeoxycholic acid and folate** were protective against hemolysis-related hepatobiliary complications in Lee et al. (2026).

### Gene–environment interactions

Two well-documented interactions, both mechanistically clear:

1. **Genotype × temperature.** Only specific *SLC2A1* alleles confer temperature-dependent cation leakage. Furia et al. state this explicitly: *"stomatin-deficient cryohydrocytosis still appears to be a remarkably rare entity compared with the incidence of GLUT1DS, meaning that only specific SLC2A1 mutations can induce temperature-dependent cation loss and erythrocyte deformities."*
2. **Genotype × dietary glucose/ketone availability.** Heterozygous GLUT1 haploinsufficiency is clinically silent at rest but decompensates with fasting/exertion; ketogenic diet bypasses the transport block by supplying ketone bodies as an alternative brain fuel.

CTD, PheGenI and formal GxE databases contain no entries specific to this disease.

---

## 3. Phenotypes

### Orphanet/HPO annotation set for ORPHA:168577 (32 terms, last validated 2019-09-13)

This is the most complete frequency-annotated phenotype set available. Source PMIDs cited by Orphanet: 7174793, 15071792, 15180870, 21791420, 22492876.

**Frequent (30–79% of patients):**

| HPO ID | Term | Type |
|---|---|---|
| HP:0000518 | Cataract | Clinical sign (ophthalmologic) |
| HP:0000952 | Jaundice | Clinical sign |
| HP:0001249 | Intellectual disability | Behavioral/cognitive |
| HP:0001250 | Seizure | Clinical sign (neurologic) |
| HP:0001263 | Global developmental delay | Behavioral/developmental |
| HP:0001433 | Hepatosplenomegaly | Physical sign |
| HP:0003575 | Increased intracellular sodium | **Laboratory abnormality** |
| HP:0004446 | Stomatocytosis | **Laboratory abnormality (morphology)** |
| HP:0005525 | Spontaneous hemolytic crises | Clinical event |
| HP:0008897 | Postnatal growth retardation | Growth |
| HP:0011972 | Hypoglycorrhachia | **Laboratory abnormality (CSF)** |

**Occasional (5–29%):** HP:0000252 Microcephaly; HP:0000256 Macrocephaly; HP:0000400 Macrotia; HP:0000470 Short neck; HP:0000475 Broad neck; HP:0000639 Nystagmus; HP:0001156 Brachydactyly; HP:0001251 Ataxia; HP:0001258 Spastic paraplegia; HP:0001276 Hypertonia; HP:0001334 Communicating hydrocephalus; HP:0002719 Recurrent infections; HP:0002908 Conjugated hyperbilirubinemia; HP:0004322 Short stature; HP:0007229 Intracerebral periventricular calcifications; HP:0010306 Short thorax; HP:0010920 Zonular cataract; HP:0012430 Cerebral white matter hypoplasia; HP:0012448 Delayed myelination; HP:0012695 Decreased thalamic volume; HP:0100022 Abnormality of movement.

### HPO (ontology.jax.org) annotations for OMIM:608885

32 terms. Most frequency-annotated terms are "1/1" from **PMID:22492876** (Bawazir et al. 2012) — i.e. a single patient, not a percentage. Additional terms beyond the Orphanet set: **HP:0100018** Nuclear cataract (1/1); **HP:0025116** Fetal distress (1/1); **HP:0001561** Polyhydramnios (1/1); **HP:0002153** Hyperkalemia (1/1); **HP:0030948** Elevated gamma-glutamyltransferase level (1/1); **HP:0032660** Convulsive status epilepticus (1/1); **HP:0002188** Delayed CNS myelination (1/1); **HP:0001347** Hyperreflexia; **HP:0002540** Inability to walk; **HP:0001344** Absent speech; **HP:0001257** Spasticity; **HP:0001878** Hemolytic anemia (1/1); **HP:0001744** Splenomegaly (1/1); **HP:0002240** Hepatomegaly; **HP:0001510** Growth delay. Clinical-course terms: **HP:0003593** Infantile onset; **HP:0003623** Neonatal onset. Inheritance: **HP:0000006** Autosomal dominant inheritance.

### Additional phenotypes from primary case reports (not yet in HPO annotation sets)

- **Pseudohyperkalemia** (HP:0002153 Hyperkalemia is the closest HPO term; "pseudohyperkalemia" has no distinct HP term — a candidate ontology gap). Furia et al.: serum K⁺ 7.2 mmol/L initially, then 6.0 (age 10), 6.4 (age 15), 6.0 mmol/L (age 16), with **normal** arterial blood-gas potassium and unremarkable serial ECGs.
- **Echinocytosis** — reported with the related *SLC2A1* cation-leak allele p.Gln282_Ser285del (Weber et al. 2008: echinocytes 14.8–41.6% in affected family members vs normal <6.3%) and in Lee et al. (2026). Suggested term: **HP:0004430** (Acanthocytosis is distinct; echinocytosis lacks a precise HP term — ontology gap).
- **Macrocytosis** — MCV 121.3 fL in the Gly286Asp patient (Stevens-Hernandez 2022, Table 1); MCV 101.8–104.9 fL in Lee et al. HPO: **HP:0001972** Macrocytic anemia / **HP:0005518** Increased mean corpuscular volume.
- **Cholelithiasis / choledocholithiasis and cholestasis** — Lee et al. (2026): gallbladder and common bile duct stones with ductal dilatation on MRCP; total bilirubin peaked at 30.8 mg/dL with direct 22.2 mg/dL. HPO: **HP:0001081** Cholelithiasis; **HP:0001396** Cholestasis.
- **Retinal dysfunction** — Bawazir et al. (2012) attributed visual impairment to both cataracts and retinal dysfunction. HPO: **HP:0000608** Macular degeneration / **HP:0000546** Retinal degeneration (approximate).
- **Thalamic atrophy, global white-matter loss, delayed myelination, periventricular calcification** on CT/MRI (Bawazir et al. 2012).
- **"Blueberry muffin" skin spots** in the Irish patient of Fricke et al. (2004) — HPO: **HP:0001000** Abnormality of skin pigmentation (approximate; the specific finding has no HP term).
- **Cerebellar ataxia with communicating hydrocephalus requiring VP shunting**, in the French patient (Lande 1982 / Fricke 2004). A hemolytic crisis occurred during the shunting procedure.
- **Drug-resistant absence epilepsy with eyelid myoclonia**; EEG with generalized spike-and-slow-wave abnormalities, hyperventilation-enhanced (Furia et al. 2023, Figures 1–2).

### Phenotype characteristics

- **Age of onset:** **Neonatal to infantile.** Orphanet/ORDO: onset "Neonatal", "Infancy." GARD: symptoms "may start to appear as a Newborn and as an Infant." Neonatal jaundice/hyperbilirubinemia is frequently the first sign (Furia: jaundice and congenital bilateral cataracts in the neonatal period; Lee: exchange transfusion for severe neonatal jaundice on day 3; Bawazir: conjugated hyperbilirubinemia at 22 hours of life). Seizures typically begin in infancy to early childhood (Furia: age 6 years; Lee: 10 months).
- **Severity:** **Variable but generally moderate–severe overall**, with a characteristic dissociation: the **hematological phenotype is mild** (compensated or mildly anemic) while the **neurological phenotype is severe**. Furia et al. call it a *"'mild' hematologic phenotype"* and warn that *"it is reasonable to hypothesize that cryohydrocytosis is at risk of being missed in patients with GLUT1DS."* Confirming the mild hematology: the Gly286Asp patient had Hb 12.7 g/dL with reticulocytes only 1.4% (Stevens-Hernandez 2022).
- **Progression:** **Chronic and lifelong, with an episodic/crisis-punctuated course superimposed.** Hemolysis is chronic-compensated with acute crises (HP:0005525); seizures are chronic with fluctuation tied to diet adherence; cognitive impairment is static-to-slowly-evolving rather than neurodegenerative. Furia: *"periods of clinical worsening related to poor KD compliance persisted during adolescence. However, upon reaching adulthood the patient attained acceptable control of seizures."*
- **Frequency among affected individuals:** use the Orphanet Frequent/Occasional bands above. Given n≈8, all percentages should be regarded as indicative only.

### Quality-of-life impact

**No EQ-5D, SF-36, PROMIS or disease-specific QoL instrument data exist for this disease.** Qualitative statements only:
- Furia et al. report that after starting a 4:1 ketogenic diet there was *"a rapid, significant overall improvement in seizures, EEG, and quality of life."*
- Lee et al.'s patient was **wheelchair-dependent** at 5.5 years, weight 17 kg (8th percentile).
- HP:0002540 (Inability to walk) and HP:0001344 (Absent speech) are annotated to OMIM:608885, indicating severe functional impairment at the severe end of the spectrum.
- A striking illustration of the social burden of unrecognized pseudohyperkalemia, from Furia et al. (verbatim): *"a concerned laboratory doctor, unaware of our patient's condition, contacted the police force upon discovering his high potassium level to find and help the patient, who was meanwhile at home and in normal conditions."*

---

## 4. Genetic/Molecular Information

### Causal gene

**SLC2A1** (solute carrier family 2 member 1), 1p34.2, OMIM *138140, HGNC:11005, NCBI Gene 6513, Ensembl ENSG00000117394. GRCh38: chr1:42,925,352–42,958,867 (minus strand), 10 exons. Aliases per NCBI Gene: CSE, DYT17, DYT18, DYT9, EIG12, GLUT, GLUT-1, GLUT1, GLUT1DS, HTLVR, PED, **SDCHCN**. Protein: GLUT1, UniProt **P11166**, 492 aa, 54,084 Da, 12 transmembrane helices (TM1 12–33, TM2 67–87, TM3 91–112, TM4 121–144, TM5 156–176, TM6 186–206, TM7 272–293, TM8 307–328, TM9 335–355, TM10 366–388, TM11 402–422, TM12 430–450), with cytoplasmic N- (1–11) and C-termini (451–492).

OMIM lists five phenotypes for *SLC2A1*, all mapping key 3 (molecular basis known): GLUT1 deficiency syndrome 1 (606777, AD/AR); GLUT1 deficiency syndrome 2 (612126, AD); Dystonia 9 (601042, AD); Epilepsy, idiopathic generalized, susceptibility to, 12 (614847, AD); and **SDCHCN (608885, AD)**.

### Pathogenic variants reported in sdCHC

| Variant (protein) | Nucleotide | Type | Location | First report / Source | Identifiers |
|---|---|---|---|---|---|
| **p.Gly286Asp** | G>A transition | Missense | TM7 region | Fricke et al. 2004 (patient D-II-2); genotyped by Flatt et al. 2011 | OMIM 138140.**0023**; UniProt **VAR_076233**; dbSNP **rs864309514**; ExPASy classification **LP/P** |
| **p.Ile435del** (or p.Ile436del) | 3-bp ATC deletion | In-frame deletion | TM11–TM12 region | Lande et al. 1982 / Fricke et al. 2004 (patient E-II-1); genotyped by Flatt et al. 2011; also Bawazir et al. 2012 | OMIM 138140.**0024**; UniProt **VAR_076235** |
| **p.Ile446del** | c.1336_1338del | In-frame deletion | TM12 | Furia et al. 2023 (patient first reported 2014) | Novel; *de novo* confirmed by segregation |
| **p.Ile436del** | NM_006516.3:c.1306_1308del | In-frame deletion | TM12 | Lee et al. 2026 | Classified **likely pathogenic** (ACMG: PS3, PM4, PM1, PM2); absent in both parents and sibling |

**Closely related but formally classified as GLUT1DS2:** **p.Gln282_Ser285del** (c.1022_1033del, 12-bp in-frame deletion, TM7) — Weber et al. 2008, OMIM 138140.**0008**, UniProt **VAR_054762**. This allele causes macrocytic hemolytic anemia with reticulocytosis and echinocytosis plus a cation leak, and is mechanistically the same class of lesion. Weber et al.'s two other alleles (p.Gly314Ser / OMIM .0009; p.Ala275Thr / OMIM .0010) reduced glucose transport **without** a cation leak and produced **no** hematologic abnormality — an elegant internal control for the dual-defect model.

**Structural clustering:** all sdCHC-associated alleles affect **C-terminal transmembrane segments of GLUT1**, and most are **in-frame deletions**. Lee et al. (2026) state verbatim that cases with hemolysis, pseudohyperkalemia or cryohydrocytosis *"have frequently involved a subset of SLC2A1 variants affecting the C-terminal transmembrane domains of GLUT1, particularly in-frame deletions."* Furia et al. make the same point about their p.Ile446del: it *"affects a transmembrane portion of the GLUT1 receptor located near the previously reported mutation in Ile 435–436, described in 2011. The closeness of this mutation could point to a similar pathophysiological mechanism, meaning that mutations of the transmembrane portions of GLUT1 lead to both glucose transport impairment and low-temperature cation leakage."*

### Variant classification and ClinVar — important caveat

A ClinVar query for "Hereditary cryohydrocytosis with reduced stomatin" returns **172 records**, but this figure is **misleading**: commercial laboratories submit *SLC2A1* variants against a bundled trait list covering all five *SLC2A1* phenotypes simultaneously (GLUT1DS1 AR, GLUT1DS2, encephalopathy due to GLUT1 deficiency, DYT9, EIG12, and SDCHCN). Of the top 100 records retrieved by esummary, the overwhelming majority are **VUS or likely benign/benign synonymous and intronic variants** carrying the SDCHCN trait label merely as part of that bundle. Representative pathogenic entries in that set (none specific to sdCHC) include Variation ID 1189059 `NM_006516.4(SLC2A1):c.399C>A (p.Cys133Ter)` — Pathogenic; 662199 `c.101A>G (p.Asn34Ser)` — Pathogenic; 973266 `c.1028dup (p.Met344fs)` — Pathogenic; 619980 `c.161dup (p.Ser55fs)` — Pathogenic; 2682545 `c.2T>G (p.Met1Arg)` — Pathogenic/Likely pathogenic. Notably, **the two canonical sdCHC alleles (p.Gly286Asp; p.Ile435/436del) did not appear in the top-100 ID set**, which further underlines that the ClinVar trait label is not a curated sdCHC variant list. For knowledge-base curation, the authoritative sdCHC variant set is the four-variant table above, anchored on OMIM 138140.0023/.0024 and UniProt VAR_076233/VAR_076235.

### Allele frequency in population databases

All four sdCHC alleles are **private/ultra-rare** and arise *de novo*; none has a reportable gnomAD frequency. **gnomAD constraint metrics for SLC2A1** (retrieved via the gnomAD GraphQL API, GRCh38; the API response did not state the dataset version):

| Metric | Value |
|---|---|
| pLI | **0.99999998** (≈1.00) |
| LOEUF (o/e LoF upper bound) | **0.196** |
| o/e LoF (point estimate) | 0.0858 (90% CI 0.0423–0.196) |
| Observed LoF | **4** |
| Expected LoF | **46.6** |
| Missense Z | **5.20** |
| o/e missense | **0.528** |

*SLC2A1* is therefore among the most loss-of-function-intolerant genes in the genome and is also strongly missense-constrained — consistent with near-complete penetrance and *de novo* origin of pathogenic alleles.

### Somatic vs germline origin

**Germline, and almost always *de novo*.** OMIM states that the mutations in the patients reported by Flatt et al. (2011) and Bawazir et al. (2012) arose *de novo*; in one Flatt family the parents did not carry the mutation and in the other it was presumed *de novo*. Furia et al.: *"Segregation analysis disclosed that the variant arose de novo."* Lee et al.: variant absent in both parents and the unaffected sibling, *"so likely de novo, with germline mosaicism not excluded."* There is **no somatic/cancer component**; COSMIC/TCGA are not relevant to this disease.

### Functional consequences

**Combined loss-of-function (glucose transport) and gain-of-function (cation conductance)** — i.e. a *neomorphic* allele class. The ExPASy/UniProt annotation for VAR_076233 (p.Gly286Asp) captures all four functional observations from Flatt et al. 2011: *"no effect on protein abundance"*; no effect on plasma-membrane localization; **loss of D-glucose transporter activity**; and **increased cation leakage**. Bawazir et al. similarly reported that GLUT1 was expressed normally at the red cell membrane. The mutant protein is thus correctly made and correctly trafficked — this is **not** a misfolding/degradation disease.

Because the glucose-transport arm is a loss of function on a haploinsufficiency-intolerant gene, and the cation-leak arm is a gain of function, the disease is simultaneously a haploinsufficiency syndrome in brain and a toxic-gain-of-function channelopathy in red cells.

### Modifier genes

None established. The *UGT1A1* variants in Lee et al. (2026) are the only candidate modifiers reported, interpreted by the authors as bilirubin-metabolism modifiers rather than causative.

### Epigenetic information

**No data.** No DNA methylation, histone-modification, chromatin, or episignature studies of sdCHC exist. ENCODE/Roadmap/DiseaseMeth contain nothing disease-specific. This is a genuine evidence gap.

### Chromosomal abnormalities

**Not applicable as a disease mechanism.** Karyotype was normal in the Furia patient. Note that whole-gene *SLC2A1* deletions do occur in GLUT1DS1 (OMIM 138140.0001) and 11–14% of GLUT1DS cases are detected by deletion/duplication analysis (Zhang et al. 2025, *World J Pediatr*. 21(2):149–158, PMID 39745620), but no sdCHC case has been attributed to a large structural rearrangement — consistent with the mechanism requiring a specific missense/in-frame-deletion neomorph rather than simple dosage loss.

---

## 5. Environmental Information

- **Environmental factors (toxins, radiation, pollution, occupational exposure):** **None known.** CTD/TOXNET/EPA contain no disease-specific entries. Not an environmentally caused disease.
- **Lifestyle factors:** No lifestyle exposure causes the disease. Three behavioral/dietary factors modulate it: (i) **fasting** worsens neurological symptoms; (ii) **exertion** precipitates paroxysmal dyskinesia; (iii) **ketogenic diet adherence** determines seizure control. Additionally, several common pharmacologic/dietary substances inhibit GLUT1 *in vitro* and are relatively contraindicated — phenobarbital, diazepam, sodium valproate, chloral hydrate, **methylxanthine derivatives** (which covers caffeine by class), and **ethanol** (Zhang et al. 2025). Carbamazepine and phenytoin showed no inhibitory effect in the same assays.
- **Cold exposure** is an environmental modifier of the laboratory phenotype and of specimen integrity, and patients are advised on cold avoidance (Ntoumaziou et al. 2026).
- **Infectious agents:** **None causal.** Intercurrent febrile infection acted as a hemolysis trigger in one patient (Lee et al. 2026), which is the ordinary behavior of a compensated hemolytic anemia, not an etiologic role.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**Initiating lesion → clinical manifestation.** Branch points are shown explicitly. Steps marked *[inferred]* are model-based or extrapolated rather than directly demonstrated in sdCHC patients.

1. A **heterozygous *de novo* variant in *SLC2A1*** — a missense substitution (p.Gly286Asp) or a single-/multi-residue in-frame deletion (p.Ile435/436del, p.Ile446del, p.Gln282_Ser285del) affecting a **C-terminal transmembrane helix of GLUT1** — is introduced into the germline. *This leads to:*
2. Production of a **full-length, normally abundant, correctly plasma-membrane-targeted mutant GLUT1 protein** (demonstrated: UniProt VAR_076233 annotation, "no effect on protein abundance"/localization; Bawazir et al. 2012 confirmed normal red-cell membrane GLUT1 expression). *This rules out a degradation mechanism and means the next two steps are both consequences of altered conformation, not of protein absence.* **The chain now branches.**

**Branch A — loss of substrate transport (upstream of the neurological phenotype):**

3. The transmembrane lesion **distorts the central substrate-translocation pathway**, so the protein **loses D-glucose transporter activity** (GO:0055056) — demonstrated in *Xenopus* oocytes by Flatt et al. (2011) and, for the homologous Gln282_Ser285del allele, quantified by Weber et al. (2008): Vmax fell from 213 to 37 pmol/oocyte/min with Km unchanged, i.e. reduced transporter throughput rather than altered affinity. *This results in:*
4. **Reduced facilitated glucose flux across the blood–brain barrier** (GO:0150104 transport across blood–brain barrier), where GLUT1 is the principal glucose carrier on brain microvascular endothelium (CL:0002139) and astrocytes (CL:0000127). *This results in:*
5. **Hypoglycorrhachia** — CSF glucose typically 0.9–2.9 mmol/L (16.2–52.0 mg/dL), CSF:blood ratio 0.19–0.59, with most patients <2.2 mmol/L and <0.4 (Zhang et al. 2025). Documented in sdCHC by Bawazir et al. (2012) and Fricke/Flatt patients. *This results in:*
6. **Chronic cerebral energy deficit**, most severe in regions and states of highest glucose demand. *This results in, by three sub-routes:*
   - 6a. **Epileptic encephalopathy** — generalized seizures, absence seizures with eyelid myoclonia, convulsive status epilepticus (HP:0032660), generalized spike-and-slow-wave EEG. Exacerbated by fasting; improved by ketone substrate.
   - 6b. **Movement disorder** — paroxysmal exertion-induced dyskinesia, choreoathetosis, cerebellar ataxia, spastic paraplegia; *[inferred]* attributed by Weber et al. to an **exertion-induced energy deficit in the basal ganglia** (UBERON:0002420).
   - 6c. **Impaired neurodevelopment** — global developmental delay, intellectual disability, delayed CNS myelination (HP:0002188), reduced thalamic volume, cerebral white matter hypoplasia, microcephaly. *[Inferred]* chronic substrate limitation during the period of maximal myelination and synaptogenesis.

**Branch B — gain of cation conductance (upstream of the hematological phenotype):**

3′. The same conformational change **widens or destabilizes the GLUT1 central channel**, converting the transporter into a **non-selective monovalent cation leak pathway**. Weber et al. (2008) localized this to the deleted QQLS residues, which normally form a *"bottle neck within the pore of GLUT1"*; molecular modeling indicated the deletion widens the central channel. Flatt et al. (2011) used a 3D GLUT1 model to propose analogous mechanisms for the two sdCHC alleles. **An important alternative is on record:** Flatt & Bruce (*Front Physiol*. 2018;9:367, PMID 29713289, PMCID PMC5911802) suggest the leak may arise from **altered protein–protein or protein–lipid interactions rather than conduction through the GLUT1 transport channel itself** — this branch point is *not settled*. *Either way, this results in:*
4′. **Increased Na⁺ influx and K⁺ efflux across the erythrocyte membrane.** Measured ion selectivity for the Gln282_Ser285del allele: K⁺ > Na⁺ > Ca²⁺ > NMDG⁺. Quantitatively (Weber et al.): oocyte whole-cell conductance rose from 83 pS to 363 pS; oocyte resting potential depolarized from −43 mV to −19 mV; erythrocyte ⁸⁶Rb⁺ flux was ~6-fold elevated in 3 of 4 patients. In sdCHC red cells the leak is **~10× normal at 37 °C** (Flatt & Bruce 2018). *This results in:*
5′. **A U-shaped (cryohydrocytic) temperature–leak relationship.** Fricke et al. (2004) distinguished two leak patterns among stomatin-deficient stomatocytosis patients: three with simple monotonic temperature dependence, and **two with a leak minimum near 20–25 °C that became extremely leaky at 0 °C** — defining the cryohydrocytosis subset. Flatt & Bruce (2018) assign the U-shaped curve to the Montpellier Gly286Asp pedigree. *This results in two parallel consequences:*
   - 5′a. **In vivo (37 °C): net cation gain and osmotic water entry → erythrocyte swelling (overhydration) → stomatocyte and echinocyte morphology, macrocytosis (MCV 101–121 fL), increased osmotic fragility, reduced deformability → splenic and intravascular hemolysis.** Zhang et al. (2025) put it plainly: *"Erythrocytes with an increased cation leak tend to swell and eventually undergo hemolysis."* Lee et al. (2026): *"hemolysis represents the predominant pathogenic mechanism."*
   - 5′b. ***Ex vivo* (specimen cooled to 4–8 °C): massive K⁺ efflux into plasma → PSEUDOHYPERKALEMIA.** This is a **laboratory artifact, not a true electrolyte disorder** — confirmed in the Furia patient by normal potassium on arterial blood-gas analysis and serially unremarkable ECGs. It is nonetheless clinically consequential because it triggers unnecessary nephrology/endocrine workups and potentially harmful treatment of a non-existent hyperkalemia.
6′. **Chronic hemolysis → unconjugated and conjugated hyperbilirubinemia, neonatal jaundice (sometimes requiring exchange transfusion), hepatosplenomegaly, elevated GGT, low haptoglobin, raised plasma Hb, reticulocytosis (up to 12.2%), and pigment gallstone formation → choledocholithiasis and cholestatic hepatitis** (Lee et al. 2026: TB 30.8 / DB 22.2 mg/dL, requiring ERCP with stone extraction and stenting).

**Branch C — secondary stomatin loss (the disease's eponymous feature):**

3″. *[Partly inferred]* The mutant GLUT1 perturbs the **stomatin–GLUT1 complex**. Stomatin (UniProt **P27105**, 288 aa, band 7.2b, SPFH/band-7 family, lipid-raft-associated monotopic membrane protein) is a direct binding partner of GLUT1, demonstrated biochemically by Rungaldier S, Oberwagner W, Salzer U, Csaszar E, Prohaska R. *"Stomatin interacts with GLUT1/SLC2A1, band 3/SLC4A1, and aquaporin-1 in human erythrocyte membrane domains."* **BBA. 2013;1828(3):956–966. PMID 23219802, PMCID PMC3790964** — in-situ cross-linking plus immunoaffinity purification and mass spectrometry identified GLUT1, band 3 and aquaporin-1 as the major stomatin partners, supporting a **membrane scaffold that modulates transport proteins**. *This results in:*
4″. **Failure to retain stomatin during reticulocyte maturation.** Flatt et al. (2011) showed stomatin is normally lost during reticulocyte maturation via **endocytosis**; in sdCHC, that loss goes to completion. The result is near-total absence of stomatin in mature red cells with a structurally normal *STOM* gene. Stevens-Hernandez et al. (2022) confirm: *"as expected, stomatin was reduced in the sdCHC RBCs."* Importantly, the same group found that *"the presence or absence of stomatin appeared to have little effect on the ability of the reticulocyte to mature"* — sdCHC and band-3 CHC cells matured comparably despite sdCHC cells having almost no stomatin.
5″. **Functional consequence of stomatin loss — disputed, and probably a marker rather than a driver.** Two lines of argument exist:
   - Montel-Hagen A, Kinet S, Manel N, Mongellaz C, Prohaska R, Battini JL, Delaunay J, Sitbon M, Taylor N. *"Erythrocyte Glut1 triggers dehydroascorbic acid uptake in mammals unable to synthesize vitamin C."* **Cell. 2008;132(6):1039–1048. PMID 18358815, DOI 10.1016/j.cell.2008.01.042** — stomatin **switches GLUT1 from glucose transport to dehydroascorbic acid (DHA) transport** in mature human erythrocytes. On this model, losing stomatin would release GLUT1 back toward glucose transport. Furia et al. describe the resulting hypothesis: *"stomatin binds GLUT1, inhibiting glucose uptake and triggering dehydroascorbic acid uptake. Therefore, stomatin downregulation may be viewed as a way of enhancing alternative energy pathways in absence of viable glucose transportation, although such an idea has been debated."* Note the explicit hedge — this model was contested in published correspondence (*Cell*. 2009;137(2):200–201, PMID 19379682; and 137:201–2).
   - Stomatin also regulates ion-channel activity generally. UniProt P27105 FUNCTION, verbatim: *"Regulates ion channel activity and transmembrane ion transport. Regulates ASIC2 and ASIC3 channel activity."* Structural basis: Brand J, Smith ES, Schwefel D, Lapatsina L, Poole K, Omerbašić D, et al. *"A stomatin dimer modulates the activity of acid-sensing ion channels."* **EMBO J. 2012;31(17):3635–3646. PMID 22850675, PMCID PMC3433786** — a banana-shaped stomatin dimer, whose dimerization is required to repress ASIC3. *[Inferred for sdCHC]* loss of such a regulatory scaffold could in principle aggravate the leak, but this has not been tested in sdCHC red cells.
   - **Decisive negative evidence against stomatin loss being the primary cause:** in overhydrated hereditary stomatocytosis (OHSt), stomatin is also absent, yet the primary defect is *RHAG*; Flatt & Bruce call the stomatin deficiency in OHSt *"a secondary effect of the disorder."* The same logic applies to sdCHC. Historical note: Lande, Thiemann and Mentzer first described the missing protein in 1982 and were appropriately cautious — their conclusion was that the absence *"raises the possibility"* that the missing band 7 protein causes the increased Na and K permeability.

### Molecular pathways, cellular processes and biochemistry — checklist coverage

- **Molecular pathways:** this is a **transport/channelopathy disease, not a signaling-cascade disease.** No Wnt/MAPK/mTOR/PI3K-AKT involvement is reported. Relevant pathway content is carbohydrate transmembrane transport (Reactome/KEGG: facilitative hexose transport; GO:1904659 D-glucose transmembrane transport; GO:0098708 D-glucose import across plasma membrane) and ascorbate recycling (GO:0070837 dehydroascorbic acid transport; GO:0019852 L-ascorbic acid metabolic process; CHEBI:17242 dehydroascorbic acid; CHEBI:29073 L-ascorbic acid).
- **Cellular processes:** osmotic cell swelling and volume dysregulation; erythrocyte membrane destabilization and hemolysis; reticulocyte maturation and endocytic membrane remodeling; compensatory Na⁺/K⁺-ATPase pump upregulation (Ntoumaziou et al. describe a mild 37 °C leak partly offset by *"an overactive Na⁺/K⁺ pump"*). GO terms: **GO:0006873** intracellular monoatomic ion homeostasis; **GO:0055085** transmembrane transport; **GO:0030218** erythrocyte differentiation; **GO:0071474** cellular hyperosmotic response; **GO:0006897** endocytosis.
- **Protein dysfunction:** gain-of-function pore widening + loss-of-function transport, with **normal folding, abundance and trafficking** — explicitly *not* a misfolding or aggregation disease.
- **Metabolic changes:** cerebral glucose hypometabolism; ketone-body utilization as the therapeutic bypass; possible perturbation of erythrocyte ascorbate recycling via the DHA route. Furia et al. note novel CSF metabolite findings in GLUT1DS more broadly (Zhang et al. 2025 cite decreased gluconic + galactonic acid and xylose-α1-3-glucose species in CSF).
- **Immune system involvement:** **none.** Not autoimmune, not immunodeficiency. "Recurrent infections" (HP:0002719) is listed as an occasional Orphanet feature but is unexplained and likely secondary (hyposplenism is *not* documented).
- **Tissue damage mechanisms:** osmotic lysis and splenic sequestration of rigid/overhydrated red cells; bilirubin-driven hepatobiliary injury (pigment gallstones, obstructive cholestasis); chronic substrate-deprivation injury to developing white matter; dystrophic intracerebral periventricular calcification.
- **Biochemical abnormalities:** the core lesion is a **transporter-turned-ion-channel defect** — a facilitative carrier (not an enzyme, not a receptor) acquiring aberrant conductance.
- **Epigenetic changes:** no data (see §4).
- **Molecular profiling:** **Proteomics** — the only directly relevant dataset is the red-cell membrane proteomic/immunoblot work of Stevens-Hernandez et al. 2022, which quantified stomatin loss in sdCHC and showed retained ER membranes with cleared mitochondrial and lysosomal proteins, indicating a specific arrest point in reticulocyte maturation; the sdCHC patient in that study carried heterozygous Gly286Asp (rs864309514), Hb 12.7 g/dL, MCV 121.3 fL, reticulocytes 1.4%. **Transcriptomics, metabolomics, lipidomics, single-cell, spatial transcriptomics, multi-omics, and CRISPR/RNAi screens: no disease-specific studies exist.** One computational study is available: Mouhib H et al., *"Impact of pathogenic mutations of the GLUT1 glucose transporter on solute carrier dynamics using ComDYN enhanced sampling"*, F1000Research preprint PPR505246 (DOI 10.12688/f1000research.18553.2), which models pathogenic GLUT1 variants including the cryohydrocytosis-with-neurological-defects class.

### Upstream vs downstream summary

**Upstream (single node):** the mutant GLUT1 protein in the plasma membrane. **Immediately downstream, in parallel:** (i) loss of glucose flux; (ii) gain of cation conductance; (iii) perturbed stomatin–GLUT1 complex. **Terminal:** neurological phenotype derives almost entirely from (i) in brain endothelium/astrocytes; hematological phenotype derives almost entirely from (ii) in erythrocytes; (iii) is the diagnostic biomarker and probably a bystander. This parallel-branch architecture explains the otherwise puzzling clinical dissociation between severe neurology and mild hematology, and explains why most GLUT1DS alleles cause no blood phenotype at all.

### Cell types and biological processes

- **CL:0000232** erythrocyte — primary site of the cation leak and hemolysis
- **CL:0000558** reticulocyte — site of aberrant stomatin loss
- **CL:0002139** endothelial cell of vascular tree / brain microvascular endothelial cell — site of blood–brain-barrier glucose transport failure
- **CL:0000127** astrocyte — second GLUT1-expressing CNS compartment (see §15 for the 2026 preclinical evidence that both compartments matter)
- **CL:0000540** neuron — downstream target of energy deficit
- **CL:0000573** retinal cone cell / photoreceptor — GLUT1 is annotated to photoreceptor inner segment (UniProt) and GO:0045494 photoreceptor cell maintenance; relevant to the reported retinal dysfunction
- **CL:0000188 / lens fiber cell (CL:0011004)** — relevant to cataract

---

## 7. Anatomical Structures Affected

### Organ level

**Primary organs directly affected:**
- **Blood / hematopoietic system** — UBERON:0000178 blood; UBERON:0002390 hematopoietic system. The erythron is the primary site of the gain-of-function lesion.
- **Brain** — UBERON:0000955. Primary site of the loss-of-function lesion, via the blood–brain barrier (UBERON:0000120).
- **Eye / lens** — UBERON:0000970 eye; UBERON:0000965 lens of camera-type eye. Cataract is a *primary* manifestation, not a complication: Flatt et al. note the hemolysis **and the cataract** both appear attributable to altered cation permeability of the mutant transporter — a mechanistically important point, since lens fiber cells are critically dependent on both glucose transport and cation homeostasis for transparency.

**Secondary organ involvement (complications of chronic hemolysis):**
- **Spleen** — UBERON:0002106 (splenomegaly, hypersplenic sequestration; 10 cm on ultrasound in Lee et al.)
- **Liver** — UBERON:0002107 (hepatomegaly, elevated GGT, hepatic dysfunction, cholestatic hepatitis)
- **Gallbladder and biliary tree** — UBERON:0002110 gallbladder; UBERON:0001174 common bile duct (pigment cholelithiasis, choledocholithiasis)
- **Skeleton/growth** — postnatal growth retardation, short stature, short thorax, brachydactyly, short/broad neck

**Body systems involved:** nervous (central), hematopoietic/circulatory, hepatobiliary/digestive, visual/sensory, musculoskeletal/growth. **Not involved:** cardiovascular (apart from the *spurious* arrhythmia risk attributed to pseudohyperkalemia — serial ECGs were unremarkable in Furia's patient), respiratory, renal (explicitly excluded as a cause of the hyperkalemia), endocrine, immune.

### Tissue and cell level

- **Erythrocyte membrane** (UBERON:0000178 / CL:0000232) — lipid-raft microdomains containing the stomatin–GLUT1–band 3–aquaporin-1 complex
- **Bone marrow erythroid lineage** (UBERON:0002371) — reticulocytes (CL:0000558) with arrested maturation and failed stomatin retention
- **Cerebral microvascular endothelium** (UBERON:0001986 endothelium; CL:0002139) — the rate-limiting GLUT1 barrier
- **Astroglia** (CL:0000127) and **neurons** (CL:0000540) of cerebral cortex (UBERON:0000956), basal ganglia (UBERON:0002420), cerebellum (UBERON:0002037), thalamus (UBERON:0001897)
- **Cerebral white matter** (UBERON:0002316) — hypoplasia, delayed myelination; oligodendrocytes (CL:0000128) as the presumed vulnerable population *[inferred]*
- **Periventricular region** (UBERON:0002410 periventricular white matter) — calcification
- **Lens fiber cells** (CL:0011004) and **retina** (UBERON:0000966; photoreceptors CL:0000210)

### Subcellular level

- **GO:0005886** plasma membrane — principal site of GLUT1 action and of the pathology
- **GO:0016020 / GO:0045121** membrane; membrane raft — stomatin and GLUT1 co-reside in erythrocyte lipid rafts (Rungaldier et al. 2013; Salzer & Prohaska 2001)
- **GO:0098590** plasma membrane region; **GO:0016323 / GO:0016324** basolateral and apical plasma membrane (polarized endothelium)
- **GO:0005856** cytoskeleton — stomatin is annotated to cytoplasm/cytoskeleton and is actin-binding
- **GO:0000139** Golgi membrane; **GO:0031410** cytoplasmic vesicle — trafficking and the endocytic route of stomatin loss
- UniProt also records GLUT1 at the **melanosome** (GO:0042470) and **photoreceptor inner segment** (GO:0001917), by similarity
- **Not involved:** mitochondria, nucleus, lysosome, peroxisome as primary compartments

### Localization and lateralization

**Bilateral and systemic.** Cataracts are bilateral (Furia: *"congenital bilateral cataracts"*; Bawazir: bilateral cataracts). CNS involvement is diffuse/symmetric (generalized EEG abnormalities, global white-matter loss, bilateral periventricular calcification, symmetric thalamic volume loss). Hemolysis is by definition systemic. **No asymmetric or unilateral pattern is reported.** HPO modifier: HP:0012832 Bilateral.

---

## 8. Temporal Development

### Onset

- **Typical age:** **congenital to neonatal/infantile.** ORDO lists onset as "Neonatal" and "Infancy"; HPO annotates both **HP:0003623** Neonatal onset (1/1) and **HP:0003593** Infantile onset to OMIM:608885. Cataracts may be **congenital** (Furia: congenital bilateral cataracts; Lee: congenital cataracts). Prenatal abnormalities are documented in one case: polyhydramnios (HP:0001561) and fetal distress (HP:0025116) (Bawazir et al.).
- **Onset pattern:** **subacute-to-insidious in the neonatal period** (jaundice, hyperbilirubinemia, anemia emerging over hours to days — Bawazir: conjugated hyperbilirubinemia at 22 hours of life; Lee: exchange transfusion on day 3), then **chronic** with superimposed **episodic** events (seizures, hemolytic crises). Neurological symptoms characteristically declare later than hematological ones: seizures at 10 months (Lee), 6 years (Furia); PED typically in childhood.
- Note a diagnostically important asymmetry: in classical GLUT1DS the neonatal period is *"typically being asymptomatic"* (Zhang et al. 2025), whereas in sdCHC the **hematological phenotype provides a neonatal clue**. This is an under-exploited opportunity for earlier diagnosis.

### Progression

- **Stages:** no formal staging system exists. A pragmatic natural-history framing from the published cases: **(i) neonatal** — jaundice/hyperbilirubinemia, anemia, hepatosplenomegaly, congenital cataract; **(ii) infancy–early childhood** — seizure onset, developmental delay, failure to thrive, hypotonia/hypertonia; **(iii) childhood–adolescence** — epilepsy (often drug-resistant until KD), movement disorder, intellectual disability becoming apparent, erratic "hyperkalemia" discovered on routine bloods; **(iv) late childhood–adulthood** — hemolysis-related hepatobiliary complications (gallstones, choledocholithiasis), stabilization of seizures, persistent cognitive impairment.
- **Progression rate:** **slow and variable.** Neurocognitive impairment behaves as a static-to-slowly-evolving encephalopathy rather than a neurodegeneration; hemolysis is chronic-compensated.
- **Course pattern:** **chronic with episodic exacerbations** — "spontaneous hemolytic crises" is itself a Frequent HPO annotation (HP:0005525). The Lande/Fricke French patient had **three severe hemolytic crises**, one precipitated by VP shunt surgery. The Lee patient had at least three discrete hemolytic episodes between ages 9 and 11.6 years.
- **Duration:** **chronic, lifelong.** Patients have been followed to age 40 (French patient, Fricke et al. 2004) and into adulthood (Furia's patient was 21 at transition to adult care).

### Patterns

- **Remission:** **no spontaneous remission of the underlying disorder.** Treatment-induced remission of seizures is well documented and can be dramatic. Furia et al.: a 4:1 ketogenic diet produced *"a rapid, significant overall improvement in seizures, EEG, and quality of life."* Weber et al. report two children with **complete seizure control** on the ketogenic diet. Zhang et al. (2025) report seizure control typically **within days to weeks**, movement-disorder improvement over **several months**. Partial, spontaneous remission of the hematologic phenotype was observed in one neonate: Bawazir et al. describe anemia that *"persisted through her perinatal period of life, later remitting."*
- **Critical periods / windows for intervention:** (i) **Neonatal period** — recognition of unexplained hemolysis + hyperbilirubinemia + cataract should prompt *SLC2A1* testing before neurological damage accrues. (ii) **Infancy to early childhood** — Zhang et al. state *"Early KDT initiation correlates with better Glut1DS prognosis,"* and that classical ketogenic diet is preferred *"for younger children, especially infants and toddlers."* This is the principal therapeutic window; brain glucose demand and myelination peak here. (iii) **Adolescent transition** — the documented point of diet non-adherence and clinical relapse in two of the four most recently reported patients. (iv) **Any cooling event / venepuncture** — the window in which pseudohyperkalemia generates iatrogenic risk.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** Orphanet assigns the prevalence class **"<1 / 1,000,000"** (point prevalence, worldwide). Orphadata records **3.0 cases/families worldwide**, sourced to PMID 22492876. Flatt & Bruce (2018) describe sdCHC as *"very rare,"* with **three patients reported to date**.
- **Cumulative published cases:** counting conservatively from the literature table in Furia et al. (2023) plus subsequent reports: Lande 1982 (2 patients, 1 genotyped); Fricke 2004 (2 sdCHC patients, one overlapping with Lande); Flatt 2011 (genotyped the Fricke pair); Bawazir 2012 (1 new infant); Furia 2023 (1 new patient); Lee 2026 (1 new patient). This gives roughly **6–8 unrelated individuals worldwide across 44 years.** Bawazir et al. described their patient as *"the fourth pedigree reported with this syndrome."*
- **Incidence:** **no incidence estimate exists for sdCHC specifically.** For the parent disorder GLUT1DS, Zhang et al. (2025, *World J Pediatr*) compile: European/American *de novo* single-gene studies estimating **1.65–4.13 per 100,000 live births** (citing López-Rivera 2020 and Symonds 2019); retrospective Danish and Australian prevalence of **1 in 83,000** and **1 in 90,000** respectively (citing Klepper 2020); and *SLC2A1* variant frequency in epilepsy of about **1 in 80,000** (Larsen et al.). The authors explicitly caution these *"are likely underestimates due to the potential for underdiagnosis."* The Klepper 2025 review (*J Inherit Metab Dis*. 48(3):e70044, PMID 40405536, PMCID PMC12099281) is cited in secondary sources as reporting an incidence of 1 per 24,300 (4.13/100,000; 95% CI 1.07–7.19) — I was unable to reach the full text to verify this directly, so treat it as second-hand.
- **GARD's "estimated 1,000 US cases"** figure, which circulates in some aggregators, is **not credible for this specific entity** and is inconsistent with Orphanet's <1/1,000,000 class and with ~8 published cases worldwide; it appears to be a default/placeholder. I recommend excluding it from a knowledge base entry.

### Genetic etiology parameters

- **Inheritance pattern:** **Autosomal dominant** (OMIM; HP:0000006; Orphanet; GARD; MedGen; HGNC/OMIM phenotype table entry for 608885 lists "AD"). *Note a conflict in the literature:* a EuroBloodNet webinar slide deck listed autosomal recessive inheritance — this is **incorrect** and contradicted by every primary and authoritative secondary source retrieved here. GARD states the standard AD recurrence counseling: an affected person has a 50% chance of passing on the variant to a biological child.
- **De novo rate:** **essentially 100% of reported cases.** OMIM: the *SLC2A1* mutations in Flatt (2011) and Bawazir (2012) arose *de novo*. Furia (2023) and Lee (2026) both confirmed *de novo* origin by parental segregation. No vertical transmission of sdCHC has been documented — unsurprising given the severity. (By contrast, the related cation-leak allele p.Gln282_Ser285del in Weber et al. 2008 *did* cosegregate through a three-generation family, showing dominant transmission is biologically possible for this allele class.)
- **Penetrance:** **presumed complete** for the specific sdCHC alleles; no unaffected carrier of a confirmed sdCHC variant has been reported. (Caveat: with ~8 patients, penetrance cannot be formally estimated. Within the broader *SLC2A1* allelic series, non-penetrance *has* been documented — Weber et al. reported an unaffected carrier of p.Gly314Ser in family PED2 — so complete penetrance should not be assumed for every allele.)
- **Expressivity:** **variable.** Compare the Furia patient (normal-range head circumference, mild intellectual disability, good adult seizure control, no reported anemia) with the Bawazir infant (microcephaly, periventricular calcification, thalamic atrophy, nystagmus, status epilepticus). Both carry Ile435/436-region in-frame deletions.
- **Genetic anticipation:** **not applicable** — no repeat expansion; and with essentially all cases *de novo*, multigenerational observation is unavailable.
- **Germline mosaicism:** **not demonstrated, but explicitly not excluded.** Lee et al. (2026) state the variant was absent from both parents and the sibling, so *de novo*, "with germline mosaicism not excluded." This is the correct counseling posture: recurrence risk for parents of a *de novo* case is low but not zero.
- **Founder effects:** **none.** All four reported alleles are independent *de novo* events in unrelated individuals of differing ancestry (French, Irish, Italian, Korean, and the Bawazir infant). The alleles cluster by **protein domain** (C-terminal TM helices), not by population.
- **Consanguinity:** **no role.** Fricke et al. (2004) specifically noted that neither stomatin-deficient patient came from a consanguineous family — appropriate for a dominant *de novo* disorder.
- **Carrier frequency:** **not applicable** (dominant, *de novo*, not a carrier-screening target). gnomAD contains no sdCHC alleles at appreciable frequency, consistent with pLI ≈ 1.

### Population demographics

- **Affected populations:** reported patients are of French, Irish, Italian and Korean ancestry, plus unspecified others. **No ethnic predilection**; the global distribution reflects where specialized red-cell cation-flux testing is available, not true epidemiology.
- **Geographic distribution:** sporadic and worldwide. Flatt & Bruce (2018) name the two historical pedigrees by referral center — **Montpellier (Gly286Asp)** and **San Francisco (ΔIle435/436)**; the latter traces to Lande/Mentzer's original 1982 UCSF patients. No endemic area exists.
- **Geographic distribution of specific variants:** no variant shows geographic clustering; the Ile435/436del allele has been independently reported in at least three unrelated patients on different continents, indicating a **recurrent mutational event at a mutational hotspot** rather than a shared founder haplotype.
- **Sex ratio:** no sex bias expected or reported (autosomal). Published cases include both sexes — male (Furia; Stevens-Hernandez's sdCHC subject; Lee) and female (Fricke's Irish patient; Bawazir's infant). The reported series is too small for a meaningful ratio.
- **Age distribution:** cases have been identified from the neonatal period to age 40; because the disorder is congenital, chronic and non-lethal, affected individuals span all ages, with the diagnostic yield highest in infancy and childhood.

---

## 10. Diagnostics

### Clinical/laboratory tests

**Hematology (the gateway tests):**
- **Full blood count with indices** — macrocytosis is characteristic. Documented values: Hb 12.7 g/dL with MCV **121.3 fL** and reticulocytes 1.4% in the Gly286Asp patient (Stevens-Hernandez 2022); Hb 13.4→9.3 g/dL with MCV **101.8–104.9 fL** and reticulocytes up to **12.2%** in Lee et al. LOINC: 718-7 (Hgb), 787-2 (MCV), 17849-1 (reticulocyte %).
- **Peripheral blood smear** — **stomatocytes** (HP:0004446) and **echinocytes**. Critically, morphology is temperature-sensitive: Lee et al.'s Figure 4B showed **more stomatocytes on the refrigerated smear**. A smear made from a cold-stored sample will exaggerate the finding; a smear from a warm sample may understate it.
- **Hemolysis panel** — unconjugated and conjugated bilirubin, LDH, **low haptoglobin**, **raised plasma free hemoglobin**, elevated GGT. LOINC: 1975-2 (bilirubin total), 1968-7 (direct), 4542-7 (haptoglobin).
- **Serum potassium measured at defined temperatures — the pathognomonic test.** The **temperature-dependent potassium leak test** is the key confirmatory assay. Lee et al. performed it on **heparinized whole blood held at 20–25 °C versus 2–4 °C**, sampling plasma K⁺ serially over ~6 hours: plasma potassium rose at both temperatures but **far more steeply when refrigerated**, confirming *"pseudohyperkalemia and cryohydrocytosis."* The discriminating comparison in routine practice is **serum/plasma K⁺ (high, artifactually) versus whole-blood/arterial blood-gas K⁺ (normal)** — the approach that resolved the Furia case.
- **Red cell cation content and flux studies** — intracellular Na⁺ and K⁺ (HP:0003575 Increased intracellular sodium is a Frequent Orphanet feature), and ⁸⁶Rb⁺ (K⁺ congener) influx/efflux measured across a temperature series (0 °C, 8 °C, 20–25 °C, 37 °C) to generate the **leak-versus-temperature curve**. The diagnostic signature of cryohydrocytosis is a **U-shaped curve with a minimum near 20–25 °C and a steep rise toward 0 °C** (Fricke et al. 2004). sdCHC red cells leak **~10× normal at 37 °C** (Flatt & Bruce 2018). Reference ranges from a contemporary CHC report (Ntoumaziou et al. 2026, for intracellular ion measurement): Day 0 Na⁺ 11.7–37.9, K⁺ 260.9–315.2; Day 1 Na⁺ 12.7–66.1, K⁺ 257.8–334.2 (units as per that assay). **Available only in specialized red-cell physiology laboratories.**
- **Osmotic gradient ektacytometry** — in CHC generally, Ntoumaziou et al. found a room-temperature curve with decreased Omin, EImax and Ohyp, which after 14 and 24 h at 4 °C shifted right with *"a dramatic increase in Omin and Ohyp"* — i.e. the diagnostic maneuver is to **run the assay before and after cold incubation**. (This specific dataset is from a band 3/*SLC4A1* CHC patient; the principle extends to sdCHC but has not been separately published for *SLC2A1* cases.)
- **Red cell membrane protein analysis** — **SDS-PAGE and Western blot for stomatin (band 7.2b)**, the historical diagnostic hallmark. Lande et al. (1982) resolved band 7 into ~30, 28 and 26 kDa components, found the 28-kDa component reduced, and by two-dimensional electrophoresis showed the "22 × 8" protein *"completely absent"* in both patients while "60 × 8" was present. Fricke et al. (2004) demonstrated by **immunocytochemistry that the deficiency is incomplete and mosaic at the cell level** — on blood films some red cells were stomatin-positive and most negative (in one case only a minority were negative), while **all platelets and neutrophils were stomatin-positive**. That cell-type restriction is itself diagnostically informative.

**CSF studies:**
- **Lumbar puncture after 4–6 hours of fasting**, with a paired blood glucose drawn **before** the procedure (Zhang et al. 2025). **CSF glucose** in GLUT1DS is typically **0.9–2.9 mmol/L (16.2–52.0 mg/dL)**, *"consistently below the threshold of 3.3 mmol/L (60 mg/dL),"* with most patients below **2.2 mmol/L (40 mg/dL)**. **CSF:blood glucose ratio** ranges **0.19–0.59**, most below **0.4**. Zhang et al. judge absolute CSF glucose *"a more reliable indicator than the CSF glucose/blood glucose ratio."* **CSF lactate** normal or low *"supports the clinical diagnosis"*; elevated lactate redirects toward mitochondrial disease or HK1 deficiency. HPO: **HP:0011972** Hypoglycorrhachia. LOINC: 2342-4 (glucose, CSF). Hypoglycorrhachia was documented in the sdCHC patients of Bawazir et al. and in the Weber family (CSF/serum ratio 0.39–0.55 vs 0.62–0.68 in controls).

**GLUT1-specific functional assays:**
- **Erythrocyte 3-O-methyl-D-glucose (3-OMG) uptake.** Zhang et al. report ~**98.6%** of genetically confirmed patients have reduced uptake, at **35–74% of control (average 50%)**; a commonly used cutoff is 74% of control. Limitations are practical and important: the assay *"requires prompt completion after blood collection"* and needs radiotracer-capable laboratories. False negatives occur. **Special caution for sdCHC:** because the red cell membrane is itself abnormal in this disease, uptake results require careful interpretation.
- **METAglut1 flow cytometry** (surface GLUT1 on erythrocytes). A prospective multicenter study found it **80% sensitive and >99% specific** (Zhang et al. 2025, citing ref 42). Separately, ~**78%** of patients show at least a 20% reduction in erythrocyte surface GLUT1 (Gras et al.). Flow cytometry can detect cases the 3-OMG assay misses. **Caveat for sdCHC specifically:** since mutant GLUT1 is expressed at normal abundance and normal plasma-membrane localization in sdCHC (UniProt VAR_076233 annotation; Bawazir et al.), **METAglut1 may be falsely normal in this subtype** — a genuinely important negative-predictive limitation that, to my knowledge, has not been formally studied in sdCHC patients. Flag this as an inference, not an established finding.

**Imaging:**
- **Brain MRI and CT** — findings reported in sdCHC: **intracerebral periventricular calcification** (HP:0007229, best seen on CT), **delayed/deficient myelination** (HP:0002188), **global white matter loss**, **decreased thalamic volume** (HP:0012695), **communicating hydrocephalus** (HP:0001334, one patient required VP shunting), **periventricular leukomalacia** (Lee et al.). Importantly, MRI can be **normal**: Furia et al. report *"brain MRI was negative for developmental abnormalities"* in their patient. A normal MRI does not exclude the diagnosis.
- **Abdominal ultrasound / MRCP** — splenomegaly (10 cm, Lee et al.), hepatomegaly, gallbladder and common bile duct stones with ductal dilatation.
- RadLex/UBERON anchors: UBERON:0002410 periventricular white matter; UBERON:0001897 thalamus.

**Electrophysiology:**
- **EEG** — in the Furia patient, pre-diet EEG at 14 years showed *"frequent generalized spike-and-slow wave abnormalities, sometimes in bursts, enhanced by hyperventilation (HP) without apparent clinical correlations"*; post-diet EEG at 15 years showed abnormalities *"now significantly less frequent at rest but still tend to be enhanced by hyperventilation."* **Hyperventilation-enhanced generalized discharges that improve on a ketogenic diet are a useful supportive sign.** LOINC: 24708-7.
- **ECG** — indicated to exclude true hyperkalemic cardiac effects; in sdCHC it is characteristically **normal despite alarming serum potassium**, and this normality is diagnostically meaningful (Furia et al.: *"Repeated electrocardiography tests always resulted unremarkable"*).
- EMG/NCS: no role.

**Biopsy/pathology:** no role. Diagnosis is hematological, biochemical and molecular; bone marrow examination is not indicated.

### Genetic testing

- **Recommended approach:** **targeted *SLC2A1* sequencing** is the definitive test and should be sent whenever the clinical triad (hemolytic/stomatocytic anemia + neurological features + cataract) or the dyad (unexplained pseudohyperkalemia + epilepsy) is present. Furia et al. illustrate the real-world diagnostic path: *"At 15 years of age, based on the clinical picture, sequencing of SLC2A1 was performed, allowing the identification of a novel pathogenic variant (c.1336_1338del, p.Ile446del) and, consequently, the diagnosis of GLUT1DS."* That is a **15-year diagnostic delay** in a patient with congenital cataracts, neonatal jaundice and daily seizures — the single most actionable finding in this report.
- **Single-gene testing:** *SLC2A1* (NM_006516.4). First-line when the phenotype is suggestive. GTR lists 24 tests linked to this condition via MedGen.
- **Gene panels:** two panel families are relevant and clinicians should be aware that **the wrong panel will miss this disease**. (i) **Hereditary hemolytic anemia / red cell membrane panels** — must include *SLC2A1* alongside *SLC4A1*, *RHAG*, *PIEZO1*, *KCNN4*, *ABCB6*, *STOM*, *SPTA1*, *SPTB*, *ANK1*, *EPB42*. (ii) **Epilepsy / developmental and epileptic encephalopathy panels** — reliably include *SLC2A1*. A patient worked up purely as "hereditary spherocytosis" on an older membrane panel lacking *SLC2A1* will be missed; so will a patient worked up purely as epilepsy whose pseudohyperkalemia is attributed to hemolyzed specimens.
- **Exome (WES) / genome (WGS):** high utility given the multisystem, syndromic presentation and the possibility of a novel allele. WGS additionally captures deep-intronic and structural variants. Zhang et al. report that **81–89%** of positive GLUT1DS cases carry *de novo* or rare point variants, and **11–14%** are found by deletion/duplication analysis — so **copy-number analysis must accompany sequencing**.
- **Chromosomal microarray (CMA):** reasonable in the undiagnosed global-developmental-delay workup and will detect whole-gene *SLC2A1* deletions, but has **not** identified any sdCHC case; the sdCHC mechanism requires a neomorphic missense/in-frame deletion, not dosage loss.
- **Karyotyping:** low yield; normal in the Furia patient. **FISH:** no role. **Mitochondrial DNA testing:** no role, except as a differential (elevated CSF lactate should redirect to mitochondrial disease). **Repeat expansion testing:** no role.
- **Interpretation note:** because all four sdCHC alleles are in-frame deletions or a missense in a constrained transmembrane helix, ACMG criteria applied by Lee et al. were **PS3 (functional evidence), PM4 (protein length change, in-frame indel in a non-repeat region), PM1 (mutational hot spot/functional domain), PM2 (absent from population databases)** → likely pathogenic. PS2 (*de novo* with confirmed parentage) would typically also apply.

### Omics-based diagnostics

- **Proteomics:** red cell membrane proteomics/immunoblotting for stomatin is in effect a **disease-defining proteomic assay** (Lande 1982; Fricke 2004; Stevens-Hernandez 2022), though performed in research settings only.
- **Metabolomics:** Zhang et al. cite novel CSF markers in GLUT1DS — **gluconic + galactonic acid, xylose-α1-3-glucose, and xylose-α1-3-xylose-α1-3-glucose significantly decreased**. Not yet validated for sdCHC specifically; promising as a less invasive adjunct.
- **RNA-seq / transcriptomics, epigenomics, liquid biopsy:** no established role.

### Clinical criteria and diagnostic algorithm

No sdCHC-specific criteria exist. The GLUT1DS framework from Zhang et al. (2025) applies: a **clear diagnosis** requires characteristic symptoms + low CSF glucose + a pathogenic *SLC2A1* variant; a **"highly probable"** diagnosis is permissible without the variant or without classic symptoms, and in those cases **a ketogenic diet trial should be undertaken**. Note that **5–15% of patients with typical phenotype and low CSF glucose are *SLC2A1*-negative.**

A practical sdCHC-specific pathway: unexplained hemolytic anemia with stomatocytes + macrocytosis + neonatal jaundice → add neurological features (seizures/developmental delay) and ophthalmologic exam (cataract) → check for discordant serum vs blood-gas potassium → temperature-dependent K⁺ leak test and red cell cation flux → *SLC2A1* sequencing with CNV analysis → CSF glucose (which also establishes eligibility for ketogenic therapy).

### Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **Cryohydrocytosis type 1 (band 3/*SLC4A1*)** | Most CHC is *SLC4A1*; MCV normal-to-mildly raised (91.2, 87.7 fL) rather than 100–120 fL; **stomatin present and normal**; **no neurological features, no cataract**; missense variants cluster in TM8–12 of band 3 (e.g. p.Ser762Arg). Ntoumaziou et al. 2026 illustrate this entity. |
| **Overhydrated hereditary stomatocytosis (*RHAG*)** | Leak ~40× normal and **monotonic**, not U-shaped; stomatin also absent (secondary); MCV markedly raised; no neurological phenotype. |
| **Dehydrated stomatocytosis / xerocytosis (*PIEZO1*, *KCNN4*)** | Dehydrated not overhydrated cells; leak ~2× normal; **splenectomy strongly contraindicated** due to thromboembolism. |
| **Familial pseudohyperkalemia (*ABCB6*)** | Near-normal leak at 37 °C with a "shoulder"/U-shaped curve on cooling; **pseudohyperkalemia without significant hemolysis or neurological disease**. |
| **Hereditary spherocytosis** | A real-world trap: in Ntoumaziou et al.'s CHC family the father had been *"presumed to have HS since childhood."* Spherocytes vs stomatocytes; normal cation-leak temperature profile. |
| **Classic GLUT1DS1/GLUT1DS2 without hematologic features** | Same gene, same neurology, but **no cation leak, no hemolysis, no pseudohyperkalemia**; most *SLC2A1* alleles behave this way (cf. Weber's p.Gly314Ser and p.Ala275Thr). |
| **True hyperkalemia (renal, adrenal, drug-induced)** | Excluded in the Furia patient by nephrology evaluation (no CKD, reflux nephropathy, or obstructive uropathy), normal blood-gas potassium and normal ECGs. |
| **HK1 deficiency** | Low CSF glucose **with elevated CSF lactate**. |
| **PURA syndrome** | Low CSF glucose with a distinct neurodevelopmental phenotype. |
| **Congenital infection (TORCH)** | Mimics the Bawazir presentation closely — neonatal hyperbilirubinemia, microcephaly, **periventricular calcification**, cataract, hepatosplenomegaly, "blueberry muffin" skin lesions. This differential is a genuine diagnostic hazard and should be flagged. |
| **Neonatal hemolytic disease / G6PD deficiency / UGT1A1-related hyperbilirubinemia** | Explain jaundice but not the neurological or ocular features; note *UGT1A1* variants may legitimately co-occur as modifiers. |

### Screening

- **Newborn screening:** sdCHC is **not** on any newborn screening panel. GLUT1DS more broadly is proposed as a future NBS candidate — Klepper (2025) names neonatal screening and biomarkers among future priorities. Two genomic newborn screening studies that include *SLC2A1*-class genes are running: **NCT03655223** (Early Check, RTI International, active not recruiting) and **NCT05687474** (Baby Detect, CHU Liège, completed).
- **Carrier screening:** **not applicable** (dominant, *de novo*).
- **Cascade screening:** test parents for the proband's variant to establish *de novo* status (which informs recurrence risk) — performed in Furia et al. and Lee et al. Testing of at-risk relatives is otherwise low-yield given the *de novo* pattern.
- **Opportunistic case-finding — the highest-value strategy:** any patient with **GLUT1DS plus unexplained hyperkalemia, jaundice, splenomegaly, or anemia** should be evaluated for cryohydrocytosis; and any patient with **unexplained pseudohyperkalemia plus epilepsy or developmental delay** should have *SLC2A1* sequenced. Furia et al. make exactly this argument: *"we expect that our report will facilitate both neurologists and hematologists to diagnose this underrecognized condition in further patients with GLUT1DS, avoiding unnecessary clinical concern and investigations due to pseudohyperkalemia."*

---

## 11. Outcome/Prognosis

### Survival and mortality

- **No survival data, no life-expectancy estimate, no mortality rate exists for this disease.** There is no registry, no SEER-equivalent, and no GBD entry. With ~8 reported patients, formal survival statistics are not computable.
- What is known: the disease is **not rapidly fatal**. Documented survival to age **40** (French patient, Fricke et al. 2004) and to adulthood (Furia's patient at 21). No disease-attributable death has been reported in the retrievable literature.
- **Plausible causes of disease-attributable mortality**, by analogy and from documented complications *[inferred]*: severe hemolytic crisis (three such crises in one patient, one peri-operative); status epilepticus (documented, HP:0032660); complications of biliary obstruction/cholangitis; and **iatrogenic harm from mistreated pseudohyperkalemia**. Furia et al. frame the last of these as the principal avoidable danger: hyperkalemia *"must be readily addressed, especially when severe, as it may lead to potentially fatal cardiac arrhythmia. Moreover, incorrectly treating pseudohyperkalemia might also be deleterious."*

### Morbidity and function

- **Principal drivers of morbidity are neurological, not hematological.** Intellectual disability (mild to severe), drug-resistant epilepsy, movement disorder, spasticity/spastic paraplegia, ataxia, and in severe cases inability to walk (HP:0002540) and absent speech (HP:0001344). Lee et al.'s patient was wheelchair-dependent at 5.5 years. Furia et al.'s patient had *"mild intellectual disability"* on formal neuropsychological testing at 12 years and achieved adult independence with weekly seizures.
- **Hematological morbidity is comparatively mild** but not trivial: chronic compensated hemolysis, episodic crises, transfusion in the neonatal period (exchange transfusion in one case), and gallstone disease requiring ERCP.
- **Quality-of-life measures:** **no EQ-5D, SF-36, PROMIS or disease-specific instrument has been applied.** Only the qualitative statement from Furia et al. that ketogenic diet produced significant improvement in quality of life. ICF-based disability coding is not available. **This is a clear gap for a knowledge base to flag.**

### Disease course and complications

Documented complications: **spontaneous hemolytic crises** (HP:0005525, Frequent); **peri-operative hemolytic crisis** (during VP shunting); **pigment cholelithiasis → choledocholithiasis → obstructive cholestatic hepatitis** requiring ERCP with stone extraction and stenting; **communicating hydrocephalus requiring ventriculoperitoneal shunting**; **convulsive status epilepticus**; **visual impairment from cataract plus retinal dysfunction**; **growth failure**; **recurrent infections** (HP:0002719, Occasional, mechanism unexplained); and the iatrogenic cascade from unrecognized pseudohyperkalemia.

### Recovery potential

- **Seizures: substantial and often dramatic recovery with ketogenic diet therapy.** Zhang et al. (2025) state KDT *"is highly effective in seizure control,"* often producing seizure freedom, EEG normalization, and withdrawal of anti-seizure medications *"in most patients,"* with control typically achieved *"within days to weeks."* Movement-disorder improvement follows over *"several months."* Furia et al. documented rapid improvement in seizures, EEG and QoL on a 4:1 diet, with relapse on non-adherence and re-stabilization in adulthood. Weber et al. reported complete seizure control in two children on the diet.
- **Cognition: limited recovery.** Zhang et al. state plainly: *"Cognitive impairment may persist throughout life."*
- **Hemolysis: not correctable by diet**, since the cation leak is a structural property of the mutant protein independent of substrate availability. Lee et al.'s patient had hemolytic episodes both on and off the ketogenic diet. Management is supportive.
- **Cataract:** surgically correctable; not reversed by any medical therapy.

### Prognostic factors

From Zhang et al. (2025), applicable to GLUT1DS including sdCHC:
- **Earlier initiation of ketogenic diet → better prognosis** (*"Early KDT initiation correlates with better Glut1DS prognosis"*). The strongest modifiable factor.
- **Higher CSF:blood glucose ratio → more favorable outcome.** This is the only quantitative **prognostic biomarker** identified in this session.
- **Late-onset seizures, delayed diagnosis, or late diet initiation** predict KDT failure.
- **Diet adherence** is a major determinant of the clinical trajectory through adolescence — demonstrated in two of the most recent cases.
- **Genotype:** within GLUT1DS generally, missense variants tend to be milder and complete gene deletions most severe, though Zhang et al. note the genotype–phenotype correlation is *"not entirely clear."* For sdCHC specifically, no genotype–severity relationship can be established from four alleles.
- **No molecular prognostic biomarkers** (FDA Biomarker/BEST-listed) exist for this disease.

---

## 12. Treatment

**Framing: there is no disease-modifying therapy and no sdCHC-specific guideline.** Management is (a) ketogenic diet for the neurological arm, (b) supportive hematology, and (c) — uniquely important here — **recognition and non-treatment of pseudohyperkalemia**. All recommendations below are extrapolated from GLUT1DS guidance and from hereditary stomatocytosis practice.

### Pharmacotherapy and dietary therapy

- **Ketogenic diet therapy (KDT)** — the standard of care for the neurological phenotype. NCIT: **Ketogenic Diet (C94236)**; NCIT Dietary Intervention (C15313).
  - **Classic ketogenic diet** — *"typically inducing higher ketosis levels,"* recommended *"for younger children, especially infants and toddlers"* (Zhang et al. 2025). Furia et al. used a **4:1 ratio**, with rapid improvement.
  - **Modified Atkins Diet (MAD)** — *"may suit non-compliant children, adolescents, and adults."*
  - **Low glycemic index treatment (LGIT)** — *"not recommended due to its minimal ketone production."*
  - Follow International Ketogenic Diet Study Group recommendations. Duration: *"usually into adolescence or adulthood, although lifelong necessity remains uncertain."*
  - Mechanism: supplies ketone bodies (CHEBI:17790 acetoacetate; CHEBI:17935 (R)-3-hydroxybutyrate) as an alternative cerebral fuel that bypasses the defective GLUT1 transporter — i.e. it corrects the *consequence* of Branch A while leaving Branch B (cation leak) untouched.
  - Critically, **KDT works in sdCHC as in classical GLUT1DS**: Bawazir et al. reported *"A ketogenic diet improved control over seizures and the overall clinical picture"*; Furia et al. documented rapid, significant improvement; Weber et al. achieved complete seizure control in two children.
- **Anti-seizure medications** — *"generally not recommended"* as primary therapy because they *"do not address the inherent metabolic defects."* Ethosuximide, carbamazepine, oxcarbazepine and zonisamide *"have shown ineffectiveness"*; carbonic anhydrase inhibitors risk acidosis and urolithiasis, especially combined with KDT. In practice, adjunctive ASMs are used — the Furia patient achieved adult control on **lamotrigine and valproate** despite earlier failure of ethosuximide, levetiracetam, lamotrigine and valproate as monotherapy before KDT. NCIT: Lamotrigine (C61801), Valproic Acid (C927), Levetiracetam (C29181).
- **Substances to avoid** (GLUT1 inhibitors *in vitro*): **phenobarbital, diazepam, sodium valproate, chloral hydrate, methylxanthine derivatives (caffeine, theophylline), and ethanol.** Carbamazepine and phenytoin showed no inhibitory effect. Note the tension: valproate is both listed as a GLUT1 inhibitor *in vitro* and used successfully in a real patient — clinical judgment, not a blanket ban, is warranted. Interestingly, the phenytoin metabolite 5-(4-hydroxyphenyl)-5-phenylhydantoin *"may enhance glucose transport by 30% to 60%"*, with unclear *in vivo* relevance.
- **Ursodeoxycholic acid** — used for cholestasis in Lee et al., *"which improved symptoms and cholestasis."* NCIT: Ursodiol (C29561).
- **Folic acid** — given for presumed chronic hemolysis (Lee et al.). Standard supportive care in chronic hemolytic anemia. NCIT: Folic Acid (C198).
- **Carnitine monitoring** — Zhang et al.: *"regular assessment of carnitine levels is recommended"* on KDT; supplement if deficient. NCIT: Levocarnitine (C61793).
- **Pharmacogenomics:** no PharmGKB/CPIC guideline exists for *SLC2A1*. The relevant pharmacogenetic consideration is pharmacodynamic, not metabolic: GLUT1-inhibiting drugs are relatively contraindicated in a GLUT1-haploinsufficient patient. The co-occurring *UGT1A1* promoter variants in Lee et al. are theoretically relevant to irinotecan/atazanavir handling, but incidental to this disease.

### Advanced therapeutics

- **Gene therapy:** **none clinically available; no clinical trial.** The only relevant preclinical work retrieved is a 2026 bioRxiv preprint (PPR1216810, DOI 10.64898/2026.03.04.709430; Tamura S, Hirai S et al.; **not peer reviewed**) showing GLUT1 is expressed in astrocytes as well as endothelial cells, that conditional haploinsufficiency in *either* compartment reproduces disease-like CSF glucose and cognitive/motor deficits, and that AAV-mediated restoration in one compartment gives only partial benefit — *"endothelial GLUT1 restoration alone is insufficient for robust rescue"*, with dual-compartment restoration working better. **Important mechanistic caveat for sdCHC:** because sdCHC alleles are *neomorphic* (gain-of-function cation leak), simple gene *augmentation* would not be expected to correct the hematological phenotype — allele-specific silencing or editing would be required. This is my inference, not a published statement.
- **RNA-based therapies (ASO, siRNA):** none reported for GLUT1DS or sdCHC.
- **Cell therapy:** not applicable, with one conceptual exception — **red cell exchange transfusion** has been *proposed* as an approach in GLUT1DS on the rationale that patient erythrocytes have low glucose (Zhang et al., citing ref 41). A trial exists: **NCT04137692** (Weill Cornell, "RBC exchange transfusion for GLUT1 deficiency"), currently **SUSPENDED** ("PI is transferring institutions"). Its rationale explicitly notes *"many G1D patients also have low levels of GLUT1 in their red blood cells."* This is the only intervention in development that targets the red cell compartment, and is conceptually the most relevant trial to sdCHC — though it addresses the glucose-transport arm, not the cation leak.
- **Targeted/immunotherapies:** not applicable.

### Surgical and interventional

- **Cataract surgery** — indicated for visually significant congenital/zonular cataract. NCIT: Cataract Extraction (C15278).
- **ERCP with stone extraction and biliary stenting** — performed for choledocholithiasis with cholestatic hepatitis (Lee et al. 2026). NCIT: Endoscopic Retrograde Cholangiopancreatography (C17556).
- **Cholecystectomy** — standard for symptomatic pigment gallstones in chronic hemolysis; not explicitly reported in the sdCHC cases retrieved.
- **Ventriculoperitoneal shunting** — required for communicating hydrocephalus in one patient; note that a **severe hemolytic crisis occurred during this procedure**, so peri-operative hematological precautions (warming, avoidance of cold IV fluids, hemolysis monitoring) are warranted.
- **⚠ SPLENECTOMY — AVOID.** This is the most important negative treatment recommendation in the disease area. In hereditary stomatocytosis generally, splenectomy carries a high risk of thromboembolic disease (Stewart GW et al., *"Thrombo-embolic disease after splenectomy for hereditary stomatocytosis,"* Br J Haematol 1996;93:303–310, PMID 8639421). Flatt & Bruce (2018) state splenectomy *"is not recommended for patients with DHSt because it often results in thrombo-embolic events."* For cryohydrocytosis specifically, Ntoumaziou et al. (2026) are explicit: splenectomy *"is contraindicated because it does not improve the hemolysis,"* citing thromboembolic and pulmonary hypertension risks, and they recommend **prophylactic anticoagulation for CHC patients who have already undergone splenectomy.** Given the risk of sdCHC being misdiagnosed as hereditary spherocytosis — for which splenectomy *is* standard — this is a concrete, avoidable source of harm. NCIT: Splenectomy (C15356) — contraindicated.

### Supportive and rehabilitative

- **Cold avoidance and specimen handling** — patient and laboratory education that blood samples must be kept at room temperature and analyzed promptly (Ntoumaziou et al.). This should be documented prominently in the medical record and, ideally, flagged in the laboratory information system to prevent repeated false alarms.
- **Transfusion support** for severe hemolytic crises; exchange transfusion for severe neonatal hyperbilirubinemia.
- **Phototherapy** for neonatal jaundice.
- **Rehabilitation:** physical therapy (note that withholding physical therapy was among the circumstances surrounding a clinical decline in Lee et al.), occupational therapy, speech and language therapy, special education support, low-vision services, wheelchair/mobility provision.
- **Nutrition:** dietitian-led ketogenic diet management, growth monitoring, and avoidance of prolonged fasting.

### Experimental treatments (ClinicalTrials.gov)

No trial has ever enrolled sdCHC patients specifically. GLUT1DS trials retrieved:

| NCT | Intervention | Phase | Status | Sponsor |
|---|---|---|---|---|
| **NCT01993186** | UX007 (triheptanoin) vs placebo | 2 | Completed | Ultragenyx |
| **NCT02599961** | UX007 open-label extension | 2 | **Terminated** — "halted prematurely due to lack of efficacy" | Ultragenyx |
| **NCT02960217** | UX007 crossover for movement disorders | 3 | **Terminated** | Ultragenyx |
| **NCT02036853** | Triheptanoin open-label (n=20) | 2 | Completed | Cook Children's |
| **NCT02021526** | Triheptanoin (C7 oil) | 1/2 | Withdrawn | UT Southwestern |
| **NCT04112862** | Sodium lactate infusion | Early 1 | Completed | Radboud UMC |
| **NCT04137692** | RBC exchange transfusion | N/A | **Suspended** | Weill Cornell |
| **NCT02013583** | G1D Registry | Observational | Completed | UT Southwestern |
| **NCT03202108** | Krio (ketogenic supplement) | N/A | Withdrawn (manufacturing) | Vitaflo |
| **NCT03655223** | Early Check newborn screening | Observational | Active, not recruiting | RTI International |
| **NCT05687474** | Baby Detect genomic NBS | Observational | Completed | CHU Liège |

**Key result:** NCT02960217 (phase 3, n=43 randomized) **failed its primary endpoint** — movement-disorder frequency, Hodges-Lehmann median difference **1.46 (95% CI −1.12 to 4.36), p = 0.2684**. Zhang et al. summarize the position: triheptanoin may reduce absence seizures in some patients but *"does not significantly reduce overall seizure frequency and paroxysmal movement disorders"* in patients not on KDT.

**Other experimental options noted by Zhang et al.:** **sodium lactate** (preliminary benefit); **diazoxide** (raises blood glucose; an alternative when KDT fails or is not tolerated); **acetazolamide** (one concise study: seizure reduction in 76% of patients, with >50% reduction in 58% — note the conflict with the same guideline's warning about carbonic anhydrase inhibitors plus KDT); **alpha-lipoic acid** — *in vitro* only, with *"no clinical evidence,"* and oral doses *"may not reach the experimental levels needed for efficacy."* NCIT: Triheptanoin (C171501), Thioctic Acid (C1127), Acetazolamide (C28810), Diazoxide (C47454).

### Treatment strategy and algorithm

1. **Confirm the diagnosis** molecularly; document the pseudohyperkalemia explicitly in the record.
2. **Start ketogenic diet therapy promptly** — classic 4:1 for infants/toddlers, MAD for older children/adults; manage per International Ketogenic Diet Study Group standards; monitor carnitine, growth, renal stones and lipids.
3. **Rationalize anti-seizure medications** — avoid GLUT1-inhibiting agents where feasible; retain adjuncts only if they add benefit.
4. **Hematology supportive care** — folate, transfusion for crises, gallstone surveillance, UDCA for cholestasis; **do not splenectomize**; if splenectomy has already occurred, consider prophylactic anticoagulation.
5. **Ophthalmology** — cataract assessment and surgery; retinal evaluation.
6. **Laboratory and patient education** — room-temperature specimen handling; warm environment; avoid fasting; pre-operative hematology input.
7. **Developmental and rehabilitation services**; genetic counseling.

**Personalized medicine:** the disease is already "genotype-guided" in the sense that recognizing the *SLC2A1* genotype redirects management from hematology (splenectomy) to metabolic neurology (ketogenic diet) and prevents treatment of a phantom electrolyte disorder. **Combination therapy** in practice means KDT + adjunctive ASM + hematologic supportive care; no combination has been formally trialed.

---

## 13. Prevention

### Primary prevention

**The disease itself is not preventable** — it arises from *de novo* germline mutation. No vaccination, risk-factor modification, behavioral intervention, public-health measure, environmental intervention, or prophylactic medication can prevent its occurrence. Primary prevention is limited to **reproductive options for a family with an affected proband**: prenatal diagnosis by chorionic villus sampling or amniocentesis, and **preimplantation genetic testing for monogenic disease (PGT-M)**, both available once the familial variant is known. Recurrence risk for parents of a *de novo* case is low but non-zero because of the possibility of parental germline mosaicism (explicitly not excluded by Lee et al.). An affected individual has a **50% transmission risk** to each offspring (GARD).

### Secondary prevention (early detection)

This is where the real opportunity lies, and where the literature is unanimous.

- **Shorten the diagnostic delay.** The Furia case took 15 years from congenital cataract and neonatal jaundice to molecular diagnosis. Earlier *SLC2A1* testing enables earlier ketogenic diet, which is the single strongest prognostic factor.
- **Targeted case-finding in two directions:** screen GLUT1DS patients for hematologic abnormalities, and screen unexplained pseudohyperkalemia-with-neurological-features for *SLC2A1*. Furia et al.'s stated purpose was exactly this.
- **Population newborn screening:** not currently available. Klepper (2025) lists neonatal screening and biomarkers among the field's priorities. Genomic newborn screening programs (NCT03655223, NCT05687474) may incidentally identify cases.
- **Genetic screening:** carrier screening is not applicable; **cascade testing of parents** is appropriate to establish *de novo* status and refine recurrence counseling.
- **Risk stratification:** no validated model exists. Practical stratification uses CSF:blood glucose ratio (higher = more favorable) and age at diet initiation.

### Tertiary prevention (preventing complications in affected individuals)

This is the most actionable category and should be the core of a management checklist:

1. **Prevent misdiagnosis-driven splenectomy** — the single highest-value intervention, given the thromboembolic and pulmonary-hypertension risk and the documented tendency for these patients to be labeled "hereditary spherocytosis."
2. **Prevent iatrogenic harm from pseudohyperkalemia** — flag the diagnosis in the laboratory system; confirm with blood-gas potassium; do not treat; do not repeat renal/adrenal workups.
3. **Prevent cold-induced leak** — patient education on cold avoidance; room-temperature specimen transport and prompt analysis.
4. **Prevent seizure breakthrough** — maintain ketogenic diet adherence (the documented failure point in adolescence in two of four recent cases); avoid prolonged fasting; avoid GLUT1-inhibiting drugs.
5. **Prevent and detect hepatobiliary complications** — periodic abdominal ultrasound for gallstones in a chronic hemolytic state; UDCA for cholestasis; early ERCP for obstruction.
6. **Prevent nutritional complications of KDT** — carnitine monitoring, growth monitoring, surveillance for nephrolithiasis and cardiovascular risk (Zhang et al.: *"growth delays, kidney stones, and cardiovascular risks, require regular monitoring"*).
7. **Peri-operative precautions** — a hemolytic crisis occurred intraoperatively in one patient; maintain normothermia, warm IV fluids, and hematology involvement.
8. **Prevent avoidable visual loss** — timely cataract surgery and retinal assessment.
9. **Standard chronic hemolysis care** — folate supplementation; routine childhood immunizations (noting that pneumococcal/meningococcal/Hib immunization becomes critical *if* splenectomy ever occurs, though it should not).

### Counseling

Genetic counseling should cover: autosomal dominant inheritance with essentially universal *de novo* origin; low-but-non-zero recurrence risk for parents due to possible germline mosaicism; 50% transmission risk from an affected individual; availability of prenatal testing and PGT-M; the limits of prognostic prediction given fewer than ten reported patients; and the practical, lifelong importance of the specimen-handling and splenectomy-avoidance warnings. Resources: NSGC, ACMG guidelines, GeneReviews chapter NBK1430 (*Glucose Transporter Type 1 Deficiency Syndrome*, Wang D, Pascual JM, De Vivo D — cited by Furia et al.; the chapter itself was reCAPTCHA-blocked in this session and I have not quoted it).

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologous genes

| Species | NCBI Taxon | Gene | Gene ID |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | **SLC2A1** | NCBI Gene 6513; HGNC:11005 |
| *Mus musculus* | NCBITaxon:10090 | **Slc2a1** | NCBI Gene 20525; **MGI:95755**; Ensembl ENSMUSG00000028645; Chr4 (GRCm39 chr4:118,966,001–118,994,527, + strand); synonyms Glut-1, Glut1, M100200, Rgsc200 |
| *Rattus norvegicus* | NCBITaxon:10116 | Slc2a1 | RGD ortholog listed by MGI |
| *Danio rerio* | NCBITaxon:7955 | **slc2a1a**, **slc2a1b** (duplicated) | ZFIN |
| *Xenopus* spp. | NCBITaxon:8355 / 8364 | slc2a1 | Xenbase |

Drosophila and *C. elegans* orthologs were not resolvable from the sources reached; the sugar-transporter family is ancient and broadly conserved, but a single clear 1:1 ortholog assignment could not be verified here.

**Stomatin orthology** is separately relevant: human **STOM** (NCBI Gene 2040, 9q33.2, MIM 133090, UniProt P27105) belongs to the **band 7/MEC-2 family** — the *C. elegans* mechanosensation protein **MEC-2** is the founding family member, and this deep conservation underlies the general role of band-7 proteins in modulating ion channels.

### Breed

**Not applicable.** No VBO breed association; no breed-specific disease.

### Natural disease in other species

**No naturally occurring *SLC2A1*/cryohydrocytosis disease has been reported in any non-human species.** An OMIA search for *SLC2A1* in this session returned no entry (the search interface did not filter correctly, so this is an **incomplete check rather than a confirmed negative**). No veterinary relevance has been established, and the condition has no importance in animal health.

### Comparative biology — a genuinely important species difference

The most significant comparative finding bears directly on disease modeling. **Mature mouse erythrocytes do not express GLUT1 at all.** Montel-Hagen et al. (*Cell*. 2008;132(6):1039–1048, PMID 18358815) showed that erythrocyte GLUT1 expression, and the stomatin-dependent switch from glucose to dehydroascorbic acid transport, is a trait of **humans and the few other mammals that have lost the ability to synthesize vitamin C**; **mice, which synthesize their own vitamin C, express GLUT4 rather than GLUT1 in mature erythrocytes.** The authors concluded that GLUT1 co-expression with stomatin is a compensatory mechanism in mammals unable to synthesize vitamin C.

**Consequence:** the red-cell arm of sdCHC — the cation leak, the stomatin deficiency, the hemolysis, the pseudohyperkalemia — **cannot be modeled in wild-type mice**, because the relevant protein is not in the relevant cell type. This is a first-order limitation on the entire model-organism program for this disease and explains the complete absence of a hematological animal model (see §15). (Note that this model was contested — see the *Cell* correspondence at PMID 19379682 and 137:201–2 — so the strength of the stomatin-switch claim is debated even though the species difference in erythrocyte GLUT1/GLUT4 expression is not.)

### Evolutionary conservation of mechanism

The **glucose-transport arm is deeply conserved** (GLUT1/SLC2A1 orthologs across all vertebrates; the blood–brain barrier glucose transport function is conserved in mammals). The **cation-leak arm is a property of the specific mutant protein**, not of normal biology, and would be expected to manifest in any heterologous system expressing the mutant — which is precisely why *Xenopus* oocytes have been the workhorse system (Weber et al. 2008; Flatt et al. 2011). The **stomatin–GLUT1 interaction arm is NOT conserved** in rodents, per the above.

### Transmission

**No zoonotic potential and no cross-species susceptibility.** This is a non-transmissible germline genetic disorder. (Incidental note: GLUT1 is the cell-surface receptor for HTLV-1 and HTLV-2 — NCBI Gene alias "HTLVR" — but this is unrelated to the disease mechanism.)

---

## 15. Model Organisms

### Available model systems

**Heterologous expression systems (the primary and most informative models for this disease):**
- ***Xenopus laevis* oocytes** (NCBITaxon:8355) — the system in which both the glucose-transport loss and the cation leak were demonstrated for sdCHC alleles (Flatt et al. 2011) and for the related p.Gln282_Ser285del allele (Weber et al. 2008). Readouts: two-electrode voltage clamp (whole-cell conductance, reversal potential, ion selectivity), ⁸⁶Rb⁺ flux, intracellular Na⁺/K⁺ measurement, and radiolabeled glucose uptake. Quantitative anchors from Weber et al.: Vmax 213 → 37 pmol/oocyte/min; conductance 83 → 363 pS; resting potential −43 → −19 mV; selectivity K⁺ > Na⁺ > Ca²⁺ > NMDG⁺.
- **Patient-derived primary erythrocytes** — arguably the single most valuable "model," since the affected cell type is directly and non-invasively accessible. Used for cation flux (⁸⁶Rb⁺, ~6-fold elevated), intracellular Ca²⁺ (fluo-3, 7.6 vs 6.0), 3-OMG uptake (slope −0.0201 vs −0.0280 s⁻¹, p<0.05), membrane proteomics/immunoblotting, ektacytometry, and temperature-series leak curves. This direct accessibility is a real advantage of this disease over most Mendelian disorders.
- **Computational/structural models** — 3D homology modeling of GLUT1 was used by both Weber et al. (pore "bottle neck" widening) and Flatt et al. (mechanisms for the two sdCHC alleles). Modern resources: PDB structures of human GLUT1, AlphaFold model for P11166, and the ComDYN enhanced-sampling study of pathogenic GLUT1 variants (F1000Research preprint PPR505246).

**Mouse (*Mus musculus*), Slc2a1 / MGI:95755:**
- **69 alleles** recorded at MGI, by type: 53 gene-trapped, 7 targeted, 5 endonuclease-mediated, 2 chemically induced (other), 1 ENU, 1 radiation-induced. **63 strains/lines** listed in IMSR. Named allele identified: **Slc2a1^Rgsc200^** (MGI:3811855), used in strain B6(D2)-Slc2a1^Rgsc200^ (MGI:7664091).
- **Phenotype summary (MGI annotations):** homozygous null embryos are small, lack visible eyes, are developmentally delayed, and **die at E10–E14** (embryonic lethal). **Heterozygotes show spontaneous seizures, impaired motor performance, hypoglycorrhachia, microcephaly, and reduced brain glucose uptake** — i.e. the heterozygous mouse recapitulates the **neurological** arm of GLUT1DS well. Mice homozygous for p.Pro485Leu die shortly after birth.
- **Disease model annotation:** one model, **Slc2a1^Rgsc200^/Slc2a1^+^**, is annotated to *glucose transporter type 1 deficiency syndrome 1* (DOID:0070561, OMIM:606777). **No mouse model is annotated to SDCHCN/OMIM:608885.**
- MGI lists 36 phenotypes from 4 alleles across 7 backgrounds, with 11 annotated categories including behavior/neurological, nervous system, embryo, growth/size, mortality/aging, and hematopoietic system (the contents of the hematopoietic annotation were not retrievable in this session).
- **IMPC** (mousephenotype.org/data/genes/MGI:95755) reports **0 significant phenotypes and 0 of 24 physiological systems tested** — the IMPC pipeline has not productively characterized this gene, presumably because homozygous nulls are embryonic lethal.
- **Note:** I was unable to verify the primary reference for the haploinsufficient model (commonly cited as Wang D et al., *Ann Neurol* 2006) — the Europe PMC search returned HTTP 503. The MGI phenotype annotations above are retrieved and reliable; the specific citation is not confirmed here.

**Stomatin (*Stom*) mouse:** stomatin-deficient mice exist and have been phenotyped, but **no red-cell phenotype has been reported.** The published characterization concerns anesthetic sensitivity (~12% increased sensitivity to diethyl ether, with normal locomotion; *Anesthesiology* 2006, PMID 16931982). Related family members (Stoml2, Stoml3) knockouts address mechanosensation, olfaction and spermatogenesis. A literature search returned **no report of cation leak, hemolysis, cryohydrocytosis or osmotic fragility in stomatin-deficient mice** — a negative finding from one search rather than proof of absence, but consistent with the species difference in erythrocyte GLUT1 expression described in §14. (The correct MGI ID for *Stom* was not resolved in this session; MGI:1095733 is *Pros1*, not *Stom*.)

**Zebrafish, Drosophila, C. elegans, yeast:** no disease models reported for this condition.

**Cellular models / iPSC / organoids:** **none reported.** No patient-derived iPSC line, no erythroid differentiation model, no brain microvascular endothelial organoid, and no blood–brain-barrier-on-chip study of sdCHC was found. Given that erythroid differentiation from iPSC and BBB organoid technology are both mature, this is a conspicuous and tractable gap.

**Induced models (drug/surgical/environmental):** none; and the obvious pharmacological approach (GLUT1 inhibition) would model only the loss-of-function arm, not the neomorphic cation leak.

### Phenotype recapitulation

| Disease feature | Best model | Recapitulation |
|---|---|---|
| Loss of glucose transport | *Xenopus* oocyte; Slc2a1^+/−^ mouse | **Excellent** — quantified in both |
| Cation leak / altered permeability | *Xenopus* oocyte; patient RBC | **Excellent** in oocyte; directly measurable in patient cells |
| Hypoglycorrhachia | Slc2a1^+/−^ mouse | **Good** — reproduced |
| Seizures, impaired motor performance, microcephaly | Slc2a1^+/−^ mouse | **Good** — reproduced |
| Reduced brain glucose uptake | Slc2a1^+/−^ mouse | **Good** |
| **Hemolytic anemia / stomatocytosis** | **none** | **Not recapitulated in any animal model** |
| **Stomatin deficiency** | **none** | **Not recapitulated** — mouse RBCs use GLUT4, not GLUT1 |
| **Pseudohyperkalemia / cold-induced leak** | **none** | **Not recapitulated** |
| **Cataract** | **none reported** | Not recapitulated |
| **Hepatosplenomegaly / cholelithiasis** | **none** | Not recapitulated |

### Model limitations

1. **The decisive limitation:** no animal model captures the hematological phenotype, for the species-biology reason given in §14 (mouse mature erythrocytes express GLUT4, not GLUT1). Any attempt to model sdCHC hematology in mice would require humanization of the erythroid GLUT1/stomatin system.
2. The Slc2a1^+/−^ mouse models **haploinsufficiency**, not the **neomorphic gain-of-function** that defines sdCHC. A knock-in of p.Gly286Asp or the Ile435/436 deletion would be required to model the actual allele class — **no such knock-in is reported.**
3. Homozygous nulls are embryonic lethal (E10–E14), constraining the genetic toolkit; conditional and cell-type-specific approaches are necessary, as the 2026 preprint demonstrates.
4. *Xenopus* oocytes faithfully report transport and conductance but cannot model hemolysis, membrane remodeling during reticulocyte maturation, or stomatin loss.
5. IMPC has generated no usable phenotype data for this gene.

### Research applications

Available models support: structure–function dissection of GLUT1 transport versus conductance; ion-selectivity and temperature-dependence studies; screening for compounds that modulate GLUT1; testing of ketogenic/alternative-substrate therapy; and — using the 2026 conditional/AAV approach — determining the cell-type contributions (endothelial versus astrocytic) to the neurological phenotype and the compartment requirements for gene-therapy rescue. **Not supported:** any preclinical testing of therapies aimed at the cation leak, hemolysis, or stomatin deficiency.

### Resources

MGI (informatics.jax.org, marker MGI:95755; 69 alleles); IMSR (63 strains/lines); IMPC (mousephenotype.org, no significant phenotypes); Alliance of Genome Resources (alliancegenome.org/gene/MGI:95755 — did not render in this session); ZFIN (slc2a1a, slc2a1b); Xenbase (slc2a1); RGD (rat Slc2a1); OMIA (no *SLC2A1* entry found; check incomplete).

---

## Summary of Evidence Sources

**Primary human clinical literature (the complete disease-defining set):**

| Citation | PMID | DOI | Contribution |
|---|---|---|---|
| Lande WM, Thiemann PV, Mentzer WC Jr. "Missing band 7 membrane protein in two patients with high Na, low K erythrocytes." J Clin Invest. 1982;70(6):1273–1280. | **7174793** | 10.1172/jci110726 | First description; 2D electrophoresis showed the "22 × 8" protein *"completely absent"*. PMCID PMC370344. |
| Fricke B, Jarvis HG, Reid CD, Aguilar-Martinez P, Robert A, Quittet P, et al. "Four new cases of stomatin-deficient hereditary stomatocytosis syndrome: association of the stomatin-deficient cryohydrocytosis variant with neurological dysfunction." Br J Haematol. 2004;125(6):796–803. | **15180870** | 10.1111/j.1365-2141.2004.04965.x | Defined the hematoneurological syndrome; *"deficiency in the 32 kDa membrane protein, stomatin"*; U-shaped leak curves; mosaic stomatin deficiency. |
| Weber YG, Storch A, Wuttke TV, Brockmann K, Kempfle J, Maljevic S, et al. "GLUT1 mutations are a cause of paroxysmal exertion-induced dyskinesias and induce hemolytic anemia by a cation leak." J Clin Invest. 2008;118(6):2157–2168. | **18451999** | 10.1172/JCI34438 | First demonstration of the GLUT1 cation leak; p.Gln282_Ser285del; full electrophysiology. PMCID PMC2350432. |
| **Flatt JF, Guizouarn H, Burton NM, Borgese F, Tomlinson RJ, Forsyth RJ, Baldwin SA, Levinson BE, Quittet P, Aguilar-Martinez P, Delaunay J, Stewart GW, Bruce LJ. "Stomatin-deficient cryohydrocytosis results from mutations in SLC2A1: a novel form of GLUT1 deficiency syndrome." Blood. 2011;118(19):5267–5277.** | **21791420** | 10.1182/blood-2010-12-326645 | **The defining paper.** Identified p.Gly286Asp and p.Ile435/436del; oocyte functional work; stomatin lost by endocytosis during reticulocyte maturation. *(Full text not reachable in this session.)* |
| Bawazir WM, Gevers EF, Flatt JF, Ang AL, Jacobs B, Oren C, et al. "An infant with pseudohyperkalemia, hemolysis, and seizures: cation-leaky GLUT1-deficiency syndrome due to a SLC2A1 mutation." J Clin Endocrinol Metab. 2012;97(6):E987–E993. | **22492876** | 10.1210/jc.2012-1399 | The source of most HPO frequency annotations for OMIM:608885; fourth pedigree; ketogenic diet benefit. |
| **Furia A, Muccioli L, Santucci M, Licchetta L, Bisulli F. "Pseudohyperkalemia due to cryohydrocytosis in GLUT1 deficiency syndrome. A case report and literature review." Epileptic Disord. 2023;25(3):410–415.** | **36938875** | 10.1002/epd2.20039 | **The best available review of this specific entity**, with a complete literature table; novel p.Ile446del. Open access (CC BY-NC); read in full. |
| Lee H, Ryu SW, Hong J. "Case Report: Atypical hepatobiliary manifestations associated with erythrocyte membrane instability in glucose transporter type 1 deficiency syndrome." Front Pediatr. 2026;14:1790301. | **42245163** | 10.3389/fped.2026.1790301 | **Most recent case.** p.Ile436del; temperature-dependent K⁺ leak test; hepatobiliary complications. PMCID PMC13230118. |

**Supporting mechanistic and review literature:** Flatt JF & Bruce LJ, Front Physiol. 2018;9:367 (PMID 29713289, PMCID PMC5911802); Stevens-Hernandez CJ, Flatt JF, Kupzig S, Bruce LJ, Front Physiol. 2022;13:834463 (PMID 35356079, PMCID PMC8959883); Rungaldier S et al., BBA. 2013;1828(3):956–966 (PMID 23219802, PMCID PMC3790964); Montel-Hagen A et al., Cell. 2008;132(6):1039–1048 (PMID 18358815); Brand J et al., EMBO J. 2012;31(17):3635–3646 (PMID 22850675, PMCID PMC3433786); Bruce LJ et al., Nat Genet. 2005;37(11):1258–1263 (band 3 CHC); Gallagher PG, Blood. 2017;130(25):2699–2708; Stewart GW et al., Br J Haematol. 1996;93:303–310 (PMID 8639421, post-splenectomy thromboembolism); Ntoumaziou A et al., Am J Hematol. 2026;101(6):1217–1219 (PMID 41793238, PMCID PMC13139882); Zhang MJ et al., World J Pediatr. 2025;21(2):149–158 (PMID 39745620, PMCID PMC11885374, DOI 10.1007/s12519-024-00864-5); Klepper J, J Inherit Metab Dis. 2025;48(3):e70044 (PMID 40405536, PMCID PMC12099281); De Vivo DC et al., N Engl J Med. 1991;325(10):703–709 (the original GLUT1DS description).

**Database sources retrieved:** OMIM #608885 and *138140 (via mirror; omim.org returned 403); Orphadata APIs for ORPHA:168577 (cross-referencing, phenotypes, epidemiology); ORDO via EBI OLS4; MONDO:0012143 via OLS4 and Monarch v3 API; HPO via ontology.jax.org annotation API; MedGen 332390; GARD 17036; UniProt P11166 and P27105; ExPASy VAR_076233; NCBI Gene 6513 and 2040 (E-utilities); ClinVar (E-utilities esearch/esummary, 172 records); gnomAD GraphQL API (constraint); HGNC REST; MGI MGI:95755; IMPC; QuickGO and GO API for P11166; ClinicalTrials.gov API v2.

## Principal Evidence Gaps

1. **No epigenetic, transcriptomic, metabolomic, lipidomic, single-cell, spatial, or multi-omic study** of this disease exists.
2. **No validated quality-of-life, disability, survival or mortality data** — no instrument has ever been applied.
3. **No animal model of the hematological phenotype**, and a clear biological reason why the obvious one (mouse) cannot work.
4. **No patient-derived iPSC, erythroid, or BBB organoid model** — a readily closable gap.
5. **No knock-in mouse carrying an sdCHC allele** — only haploinsufficiency models exist, which model the wrong mechanism for the red-cell phenotype.
6. **METAglut1 performance in sdCHC is unknown** and may be falsely reassuring, since mutant GLUT1 is expressed at normal surface abundance. This warrants direct study.
7. **ClinVar's 172 "sdCHC" records are a trait-bundling artifact**, not a curated variant set; the real set is four alleles.
8. **"Pseudohyperkalemia" and "echinocytosis" lack precise HPO terms** — candidate ontology additions.
9. **Diagnostic delay remains the dominant clinical problem** (15 years in the best-documented case), and it is the gap with the largest achievable patient benefit.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 70 |
| Resolved | 69 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 69 |
| On topic | 21 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1002/ajh.70274` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC370348` (7 mentions) - Protective human hybridoma antibody to tetanus toxin.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `slc2a1`, `glut1`, `patient`, `disease`, `stomatin`, `cryohydrocytosis`, `glucose`, `variant`, `cation`, `cell`, `gene`, `hemolytic`, `seizure`, `sdchc`, `phenotype`, `leak`, `hemolysis`, `cataract`, `membrane`, `clinical`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 180 |
| Resolved | 154 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 24 |
| Terms whose name was checked | 39 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011972` (5 mentions) - the report calls it "label not visible", "Hypoglycorrhachia"; HP calls it **Hypoglycorrhachia**
- `HP:0040282` (2 mentions) - the report calls it "Frequent", "label not visible"; HP calls it **Frequent**
- `HP:0040283` (2 mentions) - the report calls it "Occasional", "label cut off"; HP calls it **Occasional**
- `GO:0015758` (1 mention) - the report calls it "Glucose transmembrane transport"; GO calls it **GO_0015758**
- `UBERON:0002420` (2 mentions) - the report calls it "exertion-induced energy deficit in the basal ganglia"; UBERON calls it **basal ganglion**
- `UBERON:0002106` (1 mention) - the report calls it "splenomegaly, hypersplenic sequestration; 10 cm on ultrasound in Lee et al"; UBERON calls it **spleen**
- `UBERON:0002107` (1 mention) - the report calls it "hepatomegaly, elevated GGT, hepatic dysfunction, cholestatic hepatitis"; UBERON calls it **liver**
- `GO:0042470` (1 mention) - the report calls it "melanosome", "UniProt also records GLUT1 at the **melanosome"; GO calls it **melanosome**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (1 mention) - RO does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0015758` (GO_0015758) (1 mention) - replaced by `GO:1904659`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002188` (4 mentions) - the report calls it "delayed/deficient myelination"; HP calls it **Delayed CNS myelination**
- `HP:0004446` (5 mentions) - the report calls it "Stomatocytosis", "stomatocytes", "Peripheral blood smear** — **stomatocytes"; HP calls it **Stomatocytosis**, and lists "erythrocyte stomatocytes" among its other names
- `GO:0055056` (4 mentions) - the report calls it "D-glucose transmembrane transporter activity", "loses D-glucose transporter activity"; GO calls it **D-glucose transmembrane transporter activity**
- `CL:0000127` (3 mentions) - the report calls it "Astroglia"; CL calls it **astrocyte**, and lists "astrocytic glia" among its other names
- `UBERON:0002371` (1 mention) - the report calls it "Bone marrow erythroid lineage"; UBERON calls it **bone marrow**
- `UBERON:0002316` (1 mention) - the report calls it "Cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names
- `NCBITaxon:8355` (2 mentions) - the report calls it "Xenopus laevis* oocytes"; NCBITaxon calls it **Xenopus laevis**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0011972` - called "label not visible", "Hypoglycorrhachia"
- `HP:0004446` - called "Stomatocytosis", "stomatocytes", "Peripheral blood smear** — **stomatocytes"
- `MGI:95755` - called "title only", "did not render in this session"
- `ORPHA:168577` - called "Orphanet", "32 terms, last validated 2019-09-13", "cross-referencing, phenotypes, epidemiology"
- `HP:0012695` - called "Decreased thalamic volume", "decreased thalamic volume"
- `HP:0040282` - called "Frequent", "label not visible"
- `HP:0040283` - called "Occasional", "label cut off"
- `GO:0055056` - called "D-glucose transmembrane transporter activity", "loses D-glucose transporter activity"
- `GO:0042470` - called "melanosome", "UniProt also records GLUT1 at the **melanosome"

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MEDGEN:332390` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `NCBIGene`, `MIM`, `PubMed`, `EXT_ID`, `MGI`, `ORPHA`, `GARD`, `Orphanet`, `UMLS`.