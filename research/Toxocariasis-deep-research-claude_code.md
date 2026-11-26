---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T20:05:03.311857'
end_time: '2026-11-25T20:08:25.818069'
duration_seconds: 202.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Toxocariasis
  mondo_id: MONDO:0005988
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Toxocara disease or disorder; Toxocara infectious disease; Toxocara caused
    disease or disorder; Toxocara infection; visceral larva migrans
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
  web_search_requests: 19
  num_turns: 25
  total_cost_usd: 1.296942
  session_id: 0df572b3-5de6-49c8-bc1e-3b0642e17134
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 24
  retrieval_calls: 20
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:8643687
  relevance_assessed: 37
  on_topic: 16
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 42
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 8
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: MONDO:0005988
    reported_labels:
    - MONDO
    ontology_label: toxocariasis
  - term_id: DOID:9790
    reported_labels:
    - Disease Ontology
    ontology_label: toxocariasis
  - term_id: HP:0001880
    reported_labels:
    - Laboratory
    ontology_label: Increased total eosinophil count
  - term_id: HP:0002240
    reported_labels:
    - Sign (VLM)
    ontology_label: Hepatomegaly
  - term_id: HP:0001945
    reported_labels:
    - Sign
    ontology_label: Fever
  - term_id: HP:0002113
    reported_labels:
    - Imaging
    ontology_label: Pulmonary infiltrates
  - term_id: HP:0007663
    reported_labels:
    - Symptom (OT)
    ontology_label: Reduced visual acuity
  - term_id: HP:0025245
    reported_labels:
    - approx
    ontology_label: Cutaneous cyst
  - term_id: HP:0000541
    reported_labels:
    - Sign (OT)
    ontology_label: Retinal detachment
  - term_id: HP:0001250
    reported_labels:
    - Neurological
    ontology_label: Seizure
  - term_id: HP:0003212
    reported_labels:
    - Laboratory
    ontology_label: Increased circulating IgE concentration
  - term_id: HP:0001974
    reported_labels:
    - Laboratory
    ontology_label: Increased total leukocyte count
  - term_id: GO:0072676
    reported_labels:
    - eosinophil migration; approximate
    ontology_label: lymphocyte migration
  - term_id: UBERON:0002108
    reported_labels:
    - entry point
    ontology_label: small intestine
  labels_variant: 2
  service_unreachable: 7
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Toxocariasis
- **MONDO ID:** MONDO:0005988 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Toxocara disease or disorder; Toxocara infectious disease; Toxocara caused disease or disorder; Toxocara infection; visceral larva migrans
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Toxocariasis** covering all of the
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

I'm searching the literature on toxocariasis epidemiology, clinical forms and treatment. Next I'll look up neurological, allergic, animal-model and veterinary sources, then write the report.

# Toxocariasis (MONDO:0005988): disease characteristics research report

**Scope and limits.** Toxocariasis is an infectious zoonosis. No human causal gene is recorded, and the literature I found does not name one. Its cause is infection with larvae of the roundworms *Toxocara canis* (dog roundworm) and *Toxocara cati* (cat roundworm). I took this to be the intended entity, matching the synonyms given ("Toxocara infection", "visceral larva migrans").

The sources were retrieved by web search during this session, mostly from abstracts and index records. I did not read full texts. Where a PMID shown below did not appear explicitly on a retrieved PubMed or index page, I say so. Template items that apply only to Mendelian or genetic diseases are marked "Not applicable".

---

## 1. Disease information

**Overview.** Toxocariasis is a zoonotic helminth infection caused by the larvae of *T. canis* and *T. cati*. People usually become infected by swallowing embryonated eggs, or by eating larvae in the tissues of paratenic (transport) hosts. In humans the larvae do not mature into adult worms. Instead they migrate through the tissues. This produces visceral, ocular, neurological and "covert/common" forms of disease.

A Lancet Infectious Diseases review (Ma et al., 2018; PMID 28781085, https://pubmed.ncbi.nlm.nih.gov/28781085/) says: "These parasites are usually directly transmitted to the human host via the faecal-oral route and can cause toxocariasis and associated complications, including allergic and neurological disorders." It adds that "global epidemiological information on the relationship between seropositivity and toxocariasis is limited."

**Identifiers**

| Resource | ID | Source / verification |
|---|---|---|
| MONDO | MONDO:0005988 | Given in the template |
| MeSH | D014120 "Toxocariasis" (synonym "Larva Migrans, Visceral"); D007816 is also cross-referenced by DO and KEGG | https://meshb.nlm.nih.gov/record/ui?ui=D014120 |
| ICD-10(-CM) | B83.0 (visceral larva migrans) | Disease Ontology https://disease-ontology.org/term/DOID:9790/owl |
| ICD-11 | 1F6D (secondary source only; not checked against WHO) | KEGG H01056 https://www.kegg.jp/entry/H01056+-ja |
| Disease Ontology | DOID:9790 | Same DO page |
| KEGG DISEASE | H01056 | Same KEGG page |
| OMIM | None (not a Mendelian disease) | — |
| Orphanet | Not retrieved in this session | — |

**Synonyms.** Toxocarosis; Toxocara infection; visceral larva migrans (VLM); ocular larva migrans / ocular toxocariasis (OT); neurotoxocariasis (NT); covert toxocariasis; common toxocariasis.

**Source of information.** Aggregated disease-level resources: reviews, meta-analyses, the US NHANES survey, and case series. No EHR-derived individual-patient data were used.

---

## 2. Etiology

### Causal factors
- **Infectious cause.** The causal agents are *Toxocara canis* (NCBI Taxon 6265) and *Toxocara cati* (NCBI Taxon 6266; taxon IDs are from general knowledge and were not retrieved here). KEGG describes VLM as caused by *T. canis* or *T. cati* larvae, "usually acquired by swallowing embryonated eggs from soil or raw vegetables" (https://www.kegg.jp/entry/H01056+-ja).

### Risk factors
**Genetic.** No human susceptibility loci, GWAS hits or ClinVar entries were found. In mice, host genotype affects susceptibility to cerebral disease: BALB/c mice are susceptible and NIH mice are resistant (PMID 16476184).

**Environmental and behavioural**
- **Contact with contaminated soil.** Pooled global prevalence of *Toxocara* eggs in public places is 21% (95% CI 16–27%), from 109 studies and 42,797 soil samples in 40 countries. WHO-region estimates range from 13% to 35%, and the Western Pacific is highest (Fakhri et al., 2018; PMID 30142562). The authors conclude that "public places are often heavily contaminated with eggs of *Toxocara*."
- **Dog and cat reservoir.**
  - Global *T. canis* prevalence in dogs is 11.1% (95% CI 10.6–11.7%), and "at least 100 million dogs" are estimated to be carriers (Rostami et al., 2020; PMID 32381218).
  - Global *T. cati* prevalence in cats by coproparasitology is 17.0% (95% CI 16.2–17.8%), from 289 studies (Animals 2024; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11011152/).
- **Raw liver or meat from paratenic hosts (especially in adults).** In Korean healthy adults, 79.1% of seropositive people reported eating raw cow liver in the past year, compared with 45.3% of seronegative people. Raw cow liver was associated with seropositivity at OR 7.8 in patients with unexplained pulmonary infiltrates and OR 10.04 in a Gwangju/Jeonnam cohort (Korean J Parasitol series; e.g., https://pmc.ncbi.nlm.nih.gov/articles/PMC3309047, https://pmc.ncbi.nlm.nih.gov/articles/PMC2553335). Dog ownership was also associated with infection.
- **Socioeconomic factors and age.**
  - In US NHANES 2011–2014, seropositivity was associated with a household head with less than college education (OR 1.9) and with birth outside the US (OR 3.6; 95% CI 2.6–5.1) (Liu et al., Clin Infect Dis 2018; https://pmc.ncbi.nlm.nih.gov/articles/PMC5806997).
  - Globally, seroprevalence is higher in lower-income and lower-HDI countries and in warmer, more humid climates (Rostami et al., 2019; PMID 31856156).
- **Childhood and male sex.** A 2024 meta-analysis of children found about 25% seroprevalence and higher odds of seropositivity in males (PMID 38195773).

### Protective factors
- No genetic protective factors have been described.
- **Environmental protective factors:** regular deworming of dogs and cats, removing pet faeces, hand hygiene, washing vegetables, and avoiding raw liver or meat (Magnaval et al., 2022; PMID 35208697, PMC8875715; CDC).

### Gene–environment interaction
- No human data were found.
- In mice, host genetic background (BALB/c vs NIH) changes cerebral larval pathology and behaviour after the same egg dose (PMID 16476184).

---

## 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / course | Frequency / evidence |
|---|---|---|---|---|
| Eosinophilia | Laboratory | HP:0001880 | Acute or chronic | Often present, but 27% of high-titre patients had normal counts (Taylor et al., Lancet 1988; DOI 10.1016/S0140-6736(88)91486-9). In a 1987 covert-toxocariasis series it was present in 7/14 (https://informahealthcare.com/doi/abs/10.3109/00365548709117206) |
| Recurrent abdominal pain | Symptom | HP:0002574 (Episodic abdominal pain) / HP:0002027 | Childhood, recurrent | 61% of patients with raised titres (Taylor 1988) |
| Hepatomegaly | Sign (VLM) | HP:0002240 | Childhood, acute | Classic VLM sign; no frequency retrieved |
| Fever | Sign | HP:0001945 | Acute | VLM; no frequency retrieved |
| Wheezing / asthma | Sign | HP:0030828 / HP:0002099 | Childhood | Seropositivity is associated with childhood asthma, OR 1.91 (1.47–2.47) across 17 studies (Aghaei et al., Acta Trop 2018) |
| Pulmonary infiltrates | Imaging | HP:0002113 | Variable | Korean case-control data (PMC2553335) |
| Reduced visual acuity | Symptom (OT) | HP:0007663 | Childhood and adult | 74% of presenting OT cases in a prospective series of 211 cases (cited in PMC4116038) |
| Strabismus | Sign (OT) | HP:0000486 | Childhood | 22% of OT cases in the same series |
| Retinal granuloma, peripheral or posterior pole | Sign (OT) | HP:0007906 (Ocular inflammation, approx.) / HP:0000554 (Uveitis) | Chronic | Peripheral 40% and posterior pole 18% of eyes (same series) |
| Endophthalmitis | Sign (OT) | HP:0025245 (approx.) | Subacute | 41% of eyes (same series) |
| Tractional retinal detachment | Sign (OT) | HP:0000541 | Late | Adult cohort of 101 patients (PMC4055477) |
| Seizures / epilepsy | Neurological | HP:0001250 | Childhood mostly | Association OR 1.69 (1.42–2.01) across 11 case-control studies (PMID 30028858) |
| Meningoencephalitis, myelitis, cerebral vasculitis | Neurological (NT) | HP:0002383, HP:0002921 | Adult predominant | Systematic review (Deshayes 2016; PMID 27084369) |
| Elevated IgE | Laboratory | HP:0003212 | — | Shown in mice (PMC1364382); typical in human disease but no human frequency retrieved |
| Leucocytosis | Laboratory | HP:0001974 | Acute VLM | — |

**Quality-of-life impact.** No EQ-5D or SF-36 studies were retrieved.
- In ocular disease, permanent unilateral vision loss is the main burden.
- In covert disease, chronic abdominal pain and asthma symptoms are the main burden.

---

## 4. Genetic and molecular information

- **Human causal genes, pathogenic variants, ACMG classification, allele frequencies, somatic/germline origin, chromosomal abnormalities and human epigenetics:** not applicable. The disease is infectious, and no human causal gene has been recorded (consistent with the template).
- **Pathogen genome.** The *T. canis* draft genome (Zhu et al., Nat Commun 2015;6:6145; DOI 10.1038/ncomms7145; PMID not retrieved):
  - about 317 Mb, 13.5% repeats;
  - at least 18,596 protein-coding genes, including at least 373 peptidases, 458 kinases, 408 phosphatases, 273 receptors and 530 transporters/channels;
  - 6,037 genes (32.5%) unique to *T. canis* compared with four other nematodes.

  It is available on WormBase ParaSite as PRJNA248777.
- **Key pathogen molecules (the *T. canis* excretory–secretory antigens, TES)** (Maizels 2013, PMC3611597):
  - **TES-120:** mucins encoded by three genes; they form the shed surface coat.
  - **TES-32 (Tc-CTL-1) and TES-70 (Tc-CTL-4):** C-type lectins that mimic host molecules.
  - **TES-26 and TES-30:** used as recombinant antigens in serological tests.

  Shedding of the surface coat was proposed as "the basis of immune evasion" (1995 study, PMID 8643687, per the search snippet).
- **Host modifier genes (mouse evidence):**
  - IL-5 is required for eosinophilia, but its loss does not change larval numbers (PMC1456701; PMC1415117).
  - CD4 deficiency lowers IgE (PMC1364382).

---

## 5. Environmental information

- **Infectious agents:** *T. canis* and *T. cati* (Nematoda: Ascarididae). Definitive hosts are canids and felids. Paratenic hosts include rodents, cattle, poultry and others.
- **Environmental reservoir:** embryonated eggs in soil; 21% of public-place soil samples are contaminated worldwide (PMID 30142562).
- **Lifestyle factors:**
  - eating soil (geophagia/pica) and poor hand hygiene in children;
  - eating raw cow liver in adults (Korean data above);
  - unwashed vegetables (KEGG).
- **Lead exposure:** examined alongside *Toxocara* serostatus in NHANES (Farmer et al., PLoS NTD 2017; PMC5552322), but no causal claim was retrieved.
- **Toxins (CTD):** not applicable.

---

## 6. Mechanism and pathophysiology

### Causal chain
1. **Ingestion.** Swallowing embryonated *Toxocara* eggs (from soil, hands or produce) or larvae in raw paratenic-host tissue (such as cow liver) **leads to** hatching of third-stage larvae in the small intestine (Ma 2018; PMID 28781085).
2. **Invasion.** Larvae penetrate the intestinal wall and enter the portal and systemic circulation. This **results in** arrival in the liver first, then the lungs, and onward systemic migration (larvae reach the liver early in mice; Frontiers Immunol 2025).
3. **Arrested development.** In humans, as a non-definitive (paratenic) host, larvae cannot complete their life cycle. This **leads to** prolonged somatic migration and tissue persistence, sometimes for years. In mice, *T. canis* larvae persist in the brain (PMC5436879).
4. **Antigen release.** Larvae continuously release TES glycoproteins and shed their surface coat. This **results in** strong antigenic stimulation and, inferred from in vitro and mouse data, immune evasion by coat shedding and lectin-mediated host mimicry (PMC3611597; PMID 8643687).
5. **Type 2 response.** TES antigens **lead to** a Th2-polarised response (IL-4, IL-5, IL-13, IL-33 in mice; PMC4494798), with polyclonal and specific IgE (PMC1364382) and IL-5-dependent eosinophilia (PMC1456701; PMC1415117). This is shown in mice and inferred for humans.
6. **Tissue damage.** Eosinophil and granulomatous inflammation around migrating or dead larvae **results in** tissue injury. The mechanism then branches by organ:
   - 6a. **Liver and lung → VLM / covert disease:** hepatomegaly, eosinophilic hepatic granulomas, pulmonary infiltrates, wheeze. Airway Th2 inflammation plausibly **contributes to** asthma, though the human association is epidemiological only (OR 1.91; Aghaei 2018).
   - 6b. **Eye (usually a single larva) → OT:** a retinochoroidal granuloma (peripheral or posterior pole) or endophthalmitis, then vitreoretinal traction, retinal detachment and vision loss.
   - 6c. **Central nervous system → neurotoxocariasis:** eosinophilic meningoencephalitis, myelitis or vasculitis (PMID 27084369). An association with epilepsy is supported epidemiologically (PMID 30028858), but the mechanism has not been shown in humans.
7. **Possible chronic neurological sequel (mouse only).** Persistent cerebral larvae **lead to** ubiquitin–proteasome impairment, raised APP and phosphorylated tau, amyloid-β accumulation in the hippocampus, and memory deficits (PMC5741903; BMC Infect Dis 2008 8:84; PMC5436879). Whether this happens in humans is speculative.

### Checklist detail
- **Immune system:** Th2 cytokines, IgE, eosinophils, granuloma formation.
  - Suggested GO terms: GO:0042092 (type 2 immune response), GO:0072676 (eosinophil migration; approximate), GO:0002544 (chronic inflammatory response), GO:0002432 (granuloma formation).
  - Suggested CL terms: CL:0000771 (eosinophil), CL:0000545 (T-helper 2 cell), CL:0000236 (B cell), CL:0000235 (macrophage), CL:0000097 (mast cell).
- **Neural pathology (mouse):** GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0007611 (learning or memory).
- **Pathogen proteins:** mucins and C-type lectins (Pfam lectin_C, PF00059).
- **Metabolic changes, lipidomics, human transcriptomics/proteomics, single-cell, spatial and CRISPR data:** none retrieved for human disease.

---

## 7. Anatomical structures affected

| Level | Structures (suggested UBERON / CL) |
|---|---|
| Primary organs | Liver UBERON:0002107; lung UBERON:0002048; eye UBERON:0000970 (retina UBERON:0000966, vitreous body UBERON:0001797); brain UBERON:0000955; spinal cord UBERON:0002240 |
| Secondary | Small intestine UBERON:0002108 (entry point); skeletal muscle; skin (urticaria, pruritus; not retrieved) |
| Body systems | Hepatic/digestive, respiratory, visual, nervous, immune/haematological |
| Cells | Eosinophil CL:0000771; macrophage CL:0000235; Th2 cell CL:0000545; retinal cells; hippocampal neurons (mouse) |
| Subcellular | Extracellular region (TES; GO:0005576); proteasome complex (GO:0000502; mouse brain) |
| Lateralization | OT is typically unilateral (consistent with single-larva invasion; series in PMC4116038 and PMC4055477) |

---

## 8. Temporal development

- **Onset:**
  - VLM and covert toxocariasis: mostly childhood. In the 2024 meta-analysis, child seroprevalence was about 25% (PMID 38195773).
  - OT: classically under 16 years, but OT series span ages 1–77 and include an adult cohort of 101 patients (PMC4055477).
  - Neurotoxocariasis: mostly adults (Deshayes 2016).
- **Onset pattern:**
  - acute or subacute for VLM;
  - insidious or chronic for OT and covert disease;
  - subacute for neurotoxocariasis.
- **Course:**
  - Systemic disease is often self-limited, and most infections are asymptomatic.
  - Larvae can persist for long periods, so disease can relapse. In OT, inflammation can recur and cause progressive traction damage.
- **Remission:** spontaneous in most systemic infections; treatment-induced with albendazole and corticosteroids.
- **Critical period:** early childhood, when hand-to-mouth exposure and geophagia peak.

---

## 9. Inheritance and population

- **Inheritance, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity and carrier frequency:** not applicable (infectious disease).
- **Global seroprevalence:** 19.0% (95% CI 16.6–21.4%), from 250 studies, 265,327 people and 71 countries (Rostami et al., PLoS NTD 2019; PMID 31856156).
  - Highest region: Africa, 37.7%.
  - Lowest region: Eastern Mediterranean, 8.2%.
- **Children:**
  - About 25% seropositive (95% CI 22–29%) across 65 articles and 22 countries; Thailand had the highest estimate (58.2%) and Colombia the lowest (7.04%) (PMID 38195773).
  - A 2025 BMC Infect Dis meta-analysis reported 20.3% (17.9–22.8%), with Southeast Asia at 37.3% and Africa at 31.9% (PMID not confirmed).
- **United States:**
  - 5.1% (95% CI 4.4–5.9%) in NHANES 2011–2014, about 12 million people (Farmer et al., 2017; PMC5552322).
  - 5.0% age-standardised in a CDC analysis (Liu et al., 2018; PMC5806997), compared with 13.9% in NHANES III (1988–1994).
  - The two eras used different assays, so the apparent decline should be read with caution.
- **Incidence:** no population incidence estimates were retrieved. Seroprevalence reflects exposure, not clinical disease.
- **Sex:** male children have higher odds of seropositivity (PMID 38195773).
- **Demographic disparities:** higher prevalence with low socioeconomic status, foreign birth (US), and tropical or low-HDI settings.

---

## 10. Diagnostics

**Diagnosis rests on clinical, serological and imaging findings.** Larvae are rarely recovered, and stool examination is not useful because humans do not harbour adult worms.

- **Serology:**
  - The standard method is TES-antigen ELISA followed by Western blot confirmation, which improves specificity. Across studies, ELISA sensitivity ranges from 60% to 100% and specificity from 36% to 100%. Older TES-ELISA data cite 78% sensitivity and 92% specificity (https://pmc.ncbi.nlm.nih.gov/articles/PMC6292589/; PMC6807093).
  - A Western blot prototype showed 91.5% sensitivity and 94.6% specificity (Parasitology 2021; PMC7890350).
  - Recombinant rTES-120 plus rTES-30 IgG4 ELISA achieved 100% sensitivity in one study.
  - Deglycosylated *T. cati* ES antigen raised ELISA specificity from 80.0% to 88.3% (PMC10365917).
- **Supporting laboratory tests:** eosinophil count (whose absence does not exclude infection; Taylor 1988), total IgE, and leucocytosis.
- **Ocular samples:** aqueous or vitreous antibody testing (Goldmann–Witmer coefficient) is used. This is common practice but was not retrieved here.
- **Imaging:**
  - ultrasound or CT for hepatic lesions;
  - MRI for neurotoxocariasis (Frontiers Neurol 2018, DOI 10.3389/fneur.2018.00053);
  - fundoscopy, ultrasound B-scan and OCT for OT.
- **Histopathology:** an eosinophilic granuloma containing larval fragments is definitive, but histological confirmation "is rarely followed" in neurotoxocariasis (Frontiers Neurol 2018).
- **Genetic testing (WES, WGS, panels, CMA, karyotype and similar):** not applicable. Pathogen PCR on tissue or fluid is a research tool.
- **Diagnostic criteria:** no consensus international criteria were retrieved.
- **Differential diagnosis:**
  - OT: retinoblastoma (critical in children with leukocoria), toxoplasmic retinochoroiditis, Coats disease, persistent fetal vasculature.
  - VLM: other helminthic eosinophilias (strongyloidiasis, fascioliasis), hypereosinophilic syndrome.
  - Neurotoxocariasis: other causes of eosinophilic meningitis (*Angiostrongylus*, *Gnathostoma*).

  These are standard clinical differentials, not individually sourced here.
- **Screening:** no population screening exists. Serology is targeted to people with eosinophilia and exposure history (Korean guidance, PMC7462808).

---

## 11. Outcome and prognosis

- **Mortality:** rare. No GBD or CDC mortality figures were retrieved.
- **Morbidity:**
  - OT is the main cause of permanent disability, as unilateral vision loss.
  - Neurotoxocariasis can leave neurological sequelae (Deshayes 2016).
  - Possible long-term contributions to epilepsy (OR 1.69, PMID 30028858; earlier OR 1.92 from 7 studies, PMID 22905274) and to asthma (OR 1.91). These come from case-control and cross-sectional designs, so causality is not established.
- **Recovery:** systemic and covert disease usually resolves. Visual outcome in OT depends on where the lesion is (posterior pole lesions do worse) and on complications.
- **Prognostic biomarkers:** none validated. Serology stays positive long after cure, which limits its use for monitoring.
- **Quality-of-life measures:** no data retrieved.

---

## 12. Treatment

| Intervention | Details | Suggested NCIT term |
|---|---|---|
| Albendazole (benzimidazole; inhibits β-tubulin polymerisation) | CDC regimen: 400 mg orally twice daily for 5 days, adults and children. Magnaval 2022 calls it the drug of choice. "Optimal duration … undefined" (CDC). | Albendazole (C61626; approximate) |
| Mebendazole | 100–200 mg twice daily for 5 days (CDC) | Mebendazole |
| Corticosteroids (systemic or periocular) | Reduce ocular and severe inflammatory damage; the mainstay in OT | Corticosteroid therapy |
| Vitrectomy, laser photocoagulation, cryotherapy | For OT complications such as traction detachment or endophthalmitis (MSD Manual; case reports) | Vitrectomy; laser therapy |
| Supportive care | Bronchodilators for wheeze; antiepileptic drugs for seizures | — |

Sources: CDC clinical care page (https://www.cdc.gov/toxocariasis/hcp/clinical-care); Magnaval et al., 2022 (PMID 35208697).

- **Evidence quality.** Only four drugs are registered for human use, and "their efficacy has rarely been tested in prospective controlled trials." The role of anthelmintics in neurological or ocular disease "remains to be clarified" (Magnaval 2022). In the US, albendazole and mebendazole are not FDA-approved for this indication.
- **Ocular disease.** Albendazole with corticosteroids may reduce recurrences, but there is no evidence that albendazole improves visual outcome.
- **Adverse effects.** Prolonged albendazole has been linked to pancytopenia in people with liver impairment, so serial blood counts are advised. Data on use in pregnancy are limited (CDC).
- **Pharmacogenomics, gene or cell therapy, RNA therapies, targeted therapy and immunotherapy:** none.
- **Clinical trials:** no trials were retrieved, so no NCT identifiers are given.

---

## 13. Prevention

- **Primary prevention** (CDC; Magnaval 2022):
  - regular deworming of puppies, kittens and adult pets;
  - prompt removal of pet faeces;
  - covering sandpits;
  - hand washing;
  - washing produce;
  - avoiding raw liver or meat.
- **Vaccine:** no human or animal vaccine exists. The *T. canis* genome is expected to support vaccine and diagnostic development (Zhu 2015).
- **Secondary prevention:** serological testing in people with eosinophilia and risk exposures; eye examination in children with strabismus or leukocoria.
- **Tertiary prevention:** corticosteroids and ophthalmic follow-up to limit retinal damage.
- **Public health and One Health measures:** responsible pet ownership, controlling stray dog and cat populations, and restricting dogs from playgrounds. These are justified by soil contamination of 21% and roughly 100 million infected dogs (PMIDs 30142562, 32381218).
- **Genetic counselling:** not applicable.

---

## 14. Other species and natural disease

- **Definitive hosts:**
  - dogs (*Canis lupus familiaris*, NCBI Taxon 9615) and other canids, including foxes;
  - cats (*Felis catus*, Taxon 9685).
  - Prevalence: *T. canis* 11.1% in dogs (PMID 32381218); *T. cati* 17.0% in cats (PMC11011152).
  - Puppies are infected transplacentally and through milk (standard parasitology; not individually sourced here).
- **Paratenic hosts:** rodents, cattle, sheep, horses and poultry. Recombinant TES-30 and TES-120 ELISAs have been used for serodiagnosis in cattle, horses and sheep (PMC6417707).
- **Breeds:** no breed predisposition was found. VBO terms are not applicable.
- **Zoonotic potential:** high. Transmission runs from animal to environment to human, with no human-to-human spread.
- **OMIA:** not applicable, as this is not a Mendelian trait.

---

## 15. Model organisms

| Model | Findings | Recapitulation and limitations |
|---|---|---|
| Mouse, BALB/c (susceptible) vs NIH (resistant) | Cerebral larvae; memory impairment; brain larval counts do not reliably indicate susceptibility (PMID 16476184) | Good model of paratenic infection; strain-dependent |
| Mouse, *T. canis* vs *T. cati* | Both reduce exploration and impair memory; only *T. canis* larvae persist in the brain (PMC5436879) | Models neurotoxocarosis |
| ICR mouse, dose-ranging over 20 weeks | Hippocampal neurodegeneration markers, UPS impairment and amyloid-β accumulation (PMC5741903) | Human relevance unproven |
| IL-5-deficient mice, anti-IL-5 antibody, IL-5 transgenic mice | IL-5 drives eosinophilia but does not control larval burden (PMC1456701; PMC1415117; PMC96418) | Immunology tool |
| CD4-deficient mice | Reduced IgE (PMC1364382) | Immunology tool |
| Mouse asthma model | Lung changes consistent with asthma at different egg doses (AJTMH 103(6):2305) | Supports the asthma link experimentally |

- **Other approaches:** in vitro culture of larvae to produce TES antigen is standard. Ocular models in other species were not retrieved.
- **Host genetic models (KO/KI) used in this research:** the cytokine knockouts above. MGI holds the strain records.
- **Pathogen genetic models:** none; *T. canis* cannot yet be genetically manipulated.
- **Resources:** WormBase ParaSite (*T. canis* PRJNA248777); MGI for mouse strains.

---

## Main evidence items

| PMID / ID | Claim | Evidence type |
|---|---|---|
| 31856156 | Global seroprevalence 19.0% | Human meta-analysis |
| 38195773 | Child seroprevalence about 25%; male predominance | Human meta-analysis |
| 28781085 | Overview; faecal-oral transmission; allergic and neurological complications | Review |
| 30142562 | 21% of public-place soil contaminated | Environmental meta-analysis |
| 32381218 | 11.1% of dogs infected; at least 100 million carriers | Veterinary meta-analysis |
| 22905274; 30028858 | Epilepsy association, OR 1.92 and OR 1.69 | Human meta-analyses |
| 27084369 | Neurotoxocariasis systematic review | Human review (PMID taken from the BVS index ID mdl-27084369) |
| 35208697 | Albendazole is the drug of choice; few controlled trials | Review |
| 16476184 | Strain-dependent cerebral susceptibility in mice | Mouse |
| PMC5552322, PMC5806997 | US seroprevalence about 5% | Human survey |

**Unverified or unretrieved items:**
- The PMIDs for the Aghaei 2018 asthma meta-analysis (Acta Trop 182:298–304), Zhu 2015, the 2025 BMC Infect Dis meta-analysis and Taylor 1988 were not confirmed. 29573999 and 2895221 appeared in search results and are candidates for Aghaei 2018 and Taylor 1988.
- No human genetic data exist for this disease.
- Orphanet code, the official ICD-11 code, GBD burden figures, quality-of-life instruments and clinical trial NCT numbers were not retrieved.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 37 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:8643687` *(abstract only)*: "the basis of immune evasion"
  - closest text in source: "The association of overexpression of some membrane-associated mucins with immunosuppression and tumor metastasis suggests a possible model for the role of the surface coat in immune evasion by parasitic nematodes."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 24 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005988` (2 mentions) - the report calls it "MONDO"; MONDO calls it **toxocariasis**
- `DOID:9790` (3 mentions) - the report calls it "Disease Ontology"; DOID calls it **toxocariasis**
- `HP:0001880` (1 mention) - the report calls it "Laboratory"; HP calls it **Increased total eosinophil count**
- `HP:0002240` (1 mention) - the report calls it "Sign (VLM)"; HP calls it **Hepatomegaly**
- `HP:0001945` (1 mention) - the report calls it "Sign"; HP calls it **Fever**
- `HP:0002113` (1 mention) - the report calls it "Imaging"; HP calls it **Pulmonary infiltrates**
- `HP:0007663` (1 mention) - the report calls it "Symptom (OT)"; HP calls it **Reduced visual acuity**
- `HP:0025245` (1 mention) - the report calls it "approx"; HP calls it **Cutaneous cyst**
- `HP:0000541` (1 mention) - the report calls it "Sign (OT)"; HP calls it **Retinal detachment**
- `HP:0001250` (1 mention) - the report calls it "Neurological"; HP calls it **Seizure**
- `HP:0003212` (1 mention) - the report calls it "Laboratory"; HP calls it **Increased circulating IgE concentration**
- `HP:0001974` (1 mention) - the report calls it "Laboratory"; HP calls it **Increased total leukocyte count**
- `GO:0072676` (1 mention) - the report calls it "eosinophil migration; approximate"; GO calls it **lymphocyte migration**
- `UBERON:0002108` (1 mention) - the report calls it "entry point"; UBERON calls it **small intestine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000486` (1 mention) - the report calls it "Sign (OT)"; HP calls it **Strabismus**, and lists "Squint" among its other names
- `CL:0000545` (2 mentions) - the report calls it "T-helper 2 cell"; CL calls it **T-helper 1 cell**

### Terms the ontology service could not be reached for

7 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `GO:0007611` (1 mention)
- `UBERON:0002107` (1 mention)
- `UBERON:0000966` (1 mention)
- `UBERON:0001797` (1 mention)
- `UBERON:0000955` (1 mention)
- `UBERON:0002240` (1 mention)
- `GO:0005576` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `GO:0043161` (1 mention)