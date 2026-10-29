---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T04:22:57.180851'
end_time: '2026-10-29T04:30:59.731998'
duration_seconds: 482.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Desmin-Related Myopathy
  mondo_id: MONDO:0016187
  category: Mendelian
  causal_genes: DES
  omim_id: not recorded
  synonyms: desminopathy; desmin-related myofibrillar myopathy; myofibrillar myopathy
    1
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
  web_search_requests: 4
  num_turns: 37
  total_cost_usd: 2.8981502999999993
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 8
reference_validation:
  total_references: 79
  verified: 79
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 18
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:25171807
  - PMID:32105824
  - PMID:29987122
  - PMID:32678709
  relevance_assessed: 79
  on_topic: 68
  off_topic: 1
  off_topic_references:
  - PMID:22336329
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 79
  verified: 67
  not_found: 0
  obsolete: 1
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 8
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0011663
    reported_labels:
    - verify the ARVC term
    ontology_label: Right ventricular cardiomyopathy
  - term_id: HP:0032654
    reported_labels:
    - verify
    ontology_label: Impaired flow-mediated arterial dilatation
  - term_id: NCBITaxon:7955
    reported_labels:
    - desmb
    ontology_label: Danio rerio
  labels_variant: 4
  obsolete_terms:
  - term_id: DOID:0110286
    ontology_label: obsolete autosomal recessive limb-girdle muscular dystrophy type
      2R
  unresolvable_prefixes:
  - Orphanet
  - GARD
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Desmin-Related Myopathy
- **MONDO ID:** MONDO:0016187 (if available)
- **Causal gene(s):** DES
- **OMIM:** not recorded
- **Synonyms:** desminopathy; desmin-related myofibrillar myopathy; myofibrillar myopathy 1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Desmin-Related Myopathy** covering all of the
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

Let me write a script file instead.

Still gathering sources: I have the PubMed IDs for the core papers and am now pulling abstracts so the quotes are exact.

# Desmin-Related Myopathy (Desminopathy, DES): Research Report

**Prepared:** 2026-10-29 · **Target:** MONDO:0016187 · **Causal gene:** *DES* (desmin; HGNC symbol DES; NCBI Gene 1674; OMIM gene *125660; chromosome 2q35)

> **Note on sourcing and quotes.** PMIDs and titles below were taken from NCBI E-utilities records retrieved during this session. In this environment, abstracts could only be read through a summarizing fetch tool. The short quoted fragments therefore came out of that tool and **have not been byte-verified against the abstracts**. Before any quote becomes a KB `snippet`, run `just fetch-reference PMID:<id>` and check it with `just count-verified-snippets`.
>
> All ontology CURIEs in this report are **leads that have not been checked against a lookup**. Confirm each one with `runoak`, the term caches, or OLS before binding it. The MONDO, OMIM and Orphanet identifiers in §1 were read from OLS (MONDO release) in this session.

---

## Executive summary

Desmin-related myopathy is caused by pathogenic variants in ***DES***, the gene for desmin. Desmin is the muscle-specific type III intermediate filament protein. It links the Z-discs of neighbouring myofibrils to each other, to the sarcolemma (costameres), to the nucleus, to mitochondria and, in the heart, to the intercalated discs and desmosomes. Most variants are dominant missense changes in the α-helical rod, especially the coil 2B domain. The mutant protein poisons filament assembly in a dominant-negative way. The result is collapse of the extrasarcomeric desmin network and granulofilamentous, desmin-positive aggregates. Downstream come Z-disc streaming and myofibrillar disintegration, failure of protein quality control, mitochondrial damage, and progressive loss of skeletal muscle and cardiomyocytes.

Clinically, the disorder is a **cardioskeletal myopathy**:
- distal-onset lower-limb weakness that spreads proximally;
- cardiac conduction disease, arrhythmia and cardiomyopathy (dilated, restrictive, arrhythmogenic, hypertrophic or non-compaction);
- respiratory insufficiency.

Each of these can occur alone or in combination. A meta-analysis of 159 carriers found neurological signs in 74% and cardiological signs in 74% (PMID:20718792). A 2025 individual-patient-data meta-analysis of 230 patients found cardiomyopathy in 53.9% and major adverse cardiac events in 57.4% (PMID:39968648). No disease-modifying therapy exists. Management is supportive: pacemaker or ICD, heart-failure therapy and heart transplantation, plus respiratory support and rehabilitation. AAV9-desmin gene transfer rescues desmin-null mice but not the dominant R349P knock-in (PMID:27101257, PMID:32322014).

---

## 1. Disease information

### Overview
Desminopathy belongs to the **myofibrillar myopathies (MFM)**: protein-aggregate myopathies defined histologically by focal disintegration of myofibrils starting at the Z-disc, with ectopic accumulation of desmin and other proteins. The first *DES* mutations were reported in families with cardiac and skeletal myopathy: "A heterozygous A337P mutation was identified in a family with an adult-onset skeletal myopathy" (Goldfarb 1998, PMID:9697706). Dalakas et al. (NEJM 2000) studied 22 patients from 8 families and 2 sporadic cases. In that series, "Mutations were clustered in the carboxy-terminal part of the rod domain, which is critical for filament assembly" and "In transfected cells, the mutant desmin was unable to form a filamentous network" (PMID:10717012).

### Identifiers (read from OLS/MONDO in this session)

| Concept | MONDO | Other identifiers |
|---|---|---|
| **qualitative or quantitative defects of desmin** (the target term) | **MONDO:0016187** | Orphanet:209041; GARD:0020426; MedGen 1842905; UMLS C5680839 |
| myofibrillar myopathy 1 (desminopathy; MFM1) | MONDO:0011076 | **OMIM:601419**, OMIM:615325; Orphanet:98909, Orphanet:363543; DOID:0080092, DOID:0110286; UMLS C1832370 |
| dilated cardiomyopathy 1I (CMD1I) | MONDO:0011482 | OMIM:604765; MeSH C565752 |
| neurogenic scapuloperoneal syndrome, Kaeser type | MONDO:0008407 | OMIM:181400; Orphanet:85146; MeSH C566695 |
| autosomal dominant LGMD type 1E (DES) | MONDO:0018098 | Orphanet:34517 |

Parents of MONDO:0016187: MONDO:0016186 (*neuromuscular disease caused by qualitative or quantitative defects of myofibrillar proteins*) and MONDO:0100545 (*hereditary neurological disease*).

**Curation flag (lump/split).** MONDO:0016187 is an **Orphanet-derived grouping** with four children. The template's synonyms ("desminopathy", "desmin-related myofibrillar myopathy", "myofibrillar myopathy 1") are MONDO synonyms of the **child** MONDO:0011076, not of the target term. The curator should decide between two options:
- **DISEASE entry on MONDO:0016187**, with CMD1I, Kaeser syndrome, LGMD1E(DES) and MFM1 as `has_subtypes`. The rationale is that the literature treats all of these as one allelic spectrum (PMID:20718792, PMID:39968648).
- **Primary binding to MONDO:0011076**, with the parent recorded in `mappings`.

Note also that MFM1 carries **ARVC7** synonyms. Lorenzon et al. nevertheless concluded that "the probability of DES mutations in ARVC is very low" (PMID:23168288), so treat an ARVC-only phenotype with caution.

**Synonyms:** desminopathy; desmin myopathy; desmin-related myopathy; desmin-related cardiomyopathy; desmin storage myopathy; myofibrillar myopathy 1 (MFM1); CMD1F/LGMD1D (historical); LGMD2R / autosomal recessive LGMD caused by DES; Kaeser syndrome; inclusion body myopathy 1 (historical).

**Nature of the data.** The knowledge is aggregated, disease-level evidence from case series, family studies, meta-analyses and reviews. No EHR-derived cohorts exist.

---

## 2. Etiology

### Causal factors
- **Genetic, monogenic:** pathogenic *DES* variants. They are mostly **heterozygous dominant missense** variants, many of which introduce a proline into the rod domain (Goldfarb 2004, PMID:14724127). Small in-frame deletions, splice variants (for example exon 3 skipping, PMID:10717012) and **recessive** variants, both biallelic loss-of-function and missense, also occur (PMID:23815709, PMID:23575897, PMID:31024060, PMID:42753430).
- **De novo** variants are common in sporadic, severe early-onset cases. R406W is the classic example (PMID:14991347, PMID:36792195).
- **Phenocopy:** "desmin-related myopathy" in its older histological sense also covers *CRYAB* (αB-crystallin) disease, because αB-crystallin chaperones desmin. "Desmin myopathy is a recently identified disease associated with mutations in desmin or alphaB-crystallin" (PMID:14724127). For this entry, keep CRYAB as a differential diagnosis and not a causal gene.

### Risk factors
- **Genetic:** the *DES* genotype itself. Domain location loosely predicts phenotype. In the meta-analysis, "The majority of DES mutations were missense mutations, mostly located in the 2B domain". 2B-domain mutations were associated with isolated neurological disease, and head/tail-domain mutations with isolated cardiac disease (PMID:20718792). A later German cohort reported: "Our data argue against distinct genotype-phenotype correlations" (PMID:18504128). Treat genotype-phenotype correlation as weak.
- **Sex:** male sex carries a higher cardiac risk. "Male sex was associated with an increased risk of sustained VA (hazard ratio, 2.28; P=0.02)". Male sex also carried an increased risk of heart-failure events (HR 2.45) (PMID:39968648). For R350P, "affected men seemingly bear a higher risk of sudden, cardiac death" (PMID:17439987).
- **Age:** penetrance depends on age (§9).
- **Environmental:** none established. Exercise-induced sarcomeric damage is documented only in R349P knock-in mice (PMID:40947309). One iPSC study reports that desmin mutations increase cardiomyocyte susceptibility to coxsackievirus B3 (PMID:41761335, in vitro). Recurrent "suspected myocarditis" presentations have also been reported (PMID:28491573). Any infection-as-trigger hypothesis should be recorded as **EMERGING / in vitro only**.

### Protective factors
None documented in humans. A common *DES* variant, rs1058261, has been studied for cardiovascular endpoints in the population-based TAMRISK and Tampere cohorts (PMID:30096250, PMID:36221331). Those studies concern general cardiovascular mortality, not desminopathy, and should not be curated as protective factors for this disease.

### Gene-environment interaction
Not established in humans. The mouse data on mechanical load are summarized in §6 and §15.

---

## 3. Phenotypes

Frequencies come mainly from the meta-analysis of 159 carriers (PMID:20718792), the 230-patient individual-patient-data meta-analysis (PMID:39968648) and the Mayo series of 25 patients (PMID:34315782). HPO CURIEs need verification.

| Phenotype | Suggested HPO (verify) | Frequency / characteristics | Source |
|---|---|---|---|
| Skeletal myopathy, any | HP:0003198 Myopathy | 74% of carriers. Onset is usually in the 20s–40s (median 20 y, range 4–50 in the Mayo series) and the course is slowly progressive. | PMID:20718792; PMID:34315782 |
| Distal lower-limb weakness at onset, spreading proximally | HP:0009053 Distal lower limb muscle weakness; HP:0003701 Proximal muscle weakness | Typical presenting pattern. The weakness spreads to the trunk, neck, face, bulbar and respiratory muscles. | PMID:14724127 |
| Scapuloperoneal / limb-girdle pattern | HP:0003691 Scapular winging (verify); limb-girdle weakness | A variable pattern, notably with R350P (Kaeser). | PMID:17439987 |
| Facial weakness | HP:0030319 Weakness of facial musculature (verify) | Occasional; can be late-onset and bilateral. | PMID:33546848; PMID:42753430 |
| Dysphagia / bulbar weakness | HP:0002015 Dysphagia | Occurs in advanced disease. | PMID:14724127 |
| Respiratory insufficiency | HP:0002747 Respiratory insufficiency due to muscle weakness | 26% (29/110) of carriers. The diaphragm is affected. | PMID:23143191 (review); PMID:20718792 |
| Cardiomyopathy, any | HP:0001638 Cardiomyopathy | Up to 50% of carriers (PMID:20718792); 53.9% in PMID:39968648. | as cited |
| Dilated cardiomyopathy | HP:0001644 | 14.8% of 230 patients. *DES* explains about 1–2% of all DCM: "The prevalence of DES mutations in DCM is between 1% and 2%". | PMID:39968648; PMID:17325244 |
| Restrictive cardiomyopathy | HP:0001723 | 13.5%. Typical of early-onset and homozygous cases. | PMID:39968648; PMID:31718026; PMID:40604581 |
| Arrhythmogenic (LV-dominant or biventricular) cardiomyopathy | HP:0011663 (verify the ARVC term) | ACM 7.0%; ARVC 5.2%. E401D is described as "severe arrhythmogenic LV cardiomyopathy"; L115I as biventricular. | PMID:39968648; PMID:33290826 |
| Hypertrophic cardiomyopathy | HP:0001639 | 6.1%. Cardiac MRI shows focal LV hypertrophy in some patients who are asymptomatic. | PMID:39968648; PMID:18504128 |
| LV non-compaction | HP:0032654 (verify) | Reported with A337P. | PMID:33478057 |
| Cardiac conduction disease / AV block | HP:0001678 Atrioventricular block; HP:0011712 RBBB; HP:0011713 LBBB (verify) | About 60% have conduction disease or arrhythmia (PMID:20718792). 41.7% have conduction disease (PMID:39968648). 11/25 had complete AV block requiring a pacemaker at a median age of 25 (PMID:34315782). The block is often infra-Hisian (PMID:39627986). | as cited |
| Ventricular arrhythmia | HP:0004308 Ventricular arrhythmia | Sustained VA in 15.7%; more common in men. | PMID:39968648 |
| Sudden cardiac death | HP:0001645 | A leading cause of premature death. 3/25 had aborted SCD. | PMID:14724127; PMID:34315782 |
| Heart failure | HP:0001635 Congestive heart failure | HF events in 18.7%. Heart transplantation has been needed (3/25, at ages 20–39). | PMID:39968648; PMID:34315782 |
| Myocardial fibrosis on cardiac MRI | (no HP; record as an imaging finding) | 4/11 patients without cardiac symptoms. | PMID:18504128 |
| Elevated serum CK | HP:0003236 Elevated circulating creatine kinase concentration | Normal to moderately raised (usually under about 5× ULN). | review literature, PMID:23143191 |
| Myopathic EMG, often with myotonic/complex repetitive discharges | HP:0003458 EMG: myopathic abnormalities | Common in MFM. | PMID:23143191 |
| Smooth-muscle involvement (intestinal pseudo-obstruction, dysphagia) | HP:0004389 Intestinal pseudo-obstruction (verify) | Rare. | reviews; mouse data PMID:8626040 |
| Neuromuscular junction / myasthenic features (recessive) | — | Recessive forms show endplate pathology. | PMID:27440146; PMID:41406637 |

**Quality of life.** No desminopathy-specific EQ-5D or SF-36 data were found. Shelly et al. noted that "Heart transplantation was tolerated with improved cardiac function and quality of life" (PMID:34315782). The main drivers of disability are loss of ambulation (eventually wheelchair dependence), ventilatory failure and device- or transplant-dependent cardiac disease.

---

## 4. Genetic / molecular information

### Causal gene
- ***DES***: 9 exons over about 8.4 kb on 2q35, encoding 470 amino acids (PMID:23143191). Domains: non-helical head; rod with coils 1A, 1B, 2A and 2B joined by linkers; non-helical tail.
- **Mutational hotspots:** coil 2B, especially around the conserved "YRKLLEGEE" motif at the end of the rod (A337P, D339Y, R350P/R349P in mouse, A357P, A360P, N393I, L385P, R406W, E401D). Coil 1A is a second hotspot (Brodehl 2022, PMID:36497166; Taylor 2007, PMID:17325244). A 2025 atlas covers coil 1B (PMID:41235435), and a 2026 study covers coil-2 hotspots (PMID:42381621).

### Variant classes and functional consequences
- **Dominant missense / small in-frame deletion → dominant negative.** "A ratio of 1 : 3 (R350P desmin/WT desmin) is sufficient to effectively block the normal polymerization" (Bär 2005, PMID:15800015). In mice, "the D7-des mutation is dominant negative" (Wang 2001, PMID:11352891). In the KB, use `functional_impact_category: DOMINANT_NEGATIVE`.
- **Recessive biallelic null or hypomorphic variants → loss of function.** These cause desmin-null muscular dystrophy with central nuclei and mitochondrial abnormalities (PMID:23575897) and compound-heterozygous LoF disease (PMID:23815709). In one family, a deep intronic splice variant silenced one allele: "Western blot showed 60-75% reduction in desmin levels, likely comprised only of missense p.(Leu190Pro) desmin" (PMID:31024060). In recessive disease, "cardiac manifestations were surprisingly rare" and "classical MFM histopathology may be absent" (Keogh 2026, PMID:42753430). Severe infantile cardiomyopathy has been reported with a homozygous deletion (PMID:19433360).
- **Frequently reported variants:** R350P (the most common in German/European cohorts; Kaeser-type phenotypes, PMID:17439987), R406W (de novo, severe, PMID:14991347), A337P, R127P (phenotypically diverse, PMID:40265264), L115I, E401D, S13F and Y122H (homozygous RCM).
- **Germline vs somatic:** germline. Somatic or mosaic origin is not established. Do not bind HP:0001442.
- **ClinVar / ACMG:** classification varies widely. Many 2B-domain proline missense variants are pathogenic, but numerous rod-domain VUS exist. Functional assembly assays (transfection into SW13/BMGE cells) are routinely used as PS3 evidence (PMID:41590830, PMID:41880120).
- **Population frequency:** pathogenic variants are absent or ultra-rare in gnomAD. The common rs1058261 is benign (see §2).

### ClinGen
A ClinGen gene-disease validity record for *DES* was not retrieved in this session. Check `cache/clingen/` or the CGGV list (`just list-gene-validity`) before recording any `gene_disease_validity`.

### Modifier genes
None established. A case with combined *DES* and *CRYAB* variants has been reported (PMID:42062882). *KLHL24* gain of function drives desmin breakdown in a separate cardiomyopathy (PMID:34292882), which is relevant as a related mechanism but not as a modifier.

### Epigenetics and chromosomal abnormalities
No disease-specific epigenetic data exist. No recurrent CNVs are reported. Contiguous 2q35 deletions are not a recognized cause.

---

## 5. Environmental information
- **Toxins, occupational exposures, lifestyle:** none documented as causal.
- **Exercise / mechanical load:** exercise-induced sarcomeric damage occurs in R349P mice (PMID:40947309), and R349P knock-in fibres show early biomechanical failure (PMID:31341183, PMID:28469177). There are no human exercise-guidance trials. *Model-organism evidence only.*
- **Infectious agents:** not causal. Increased susceptibility to coxsackievirus B3 is reported in vitro (PMID:41761335).

---

## 6. Mechanism / pathophysiology

### Ordered causal chain

1. **Germline *DES* variant**, usually a heterozygous rod-domain (coil 2B or 1A) missense change. This **leads to** a mutant desmin that is incorporated into heteropolymers with wild-type desmin. *(Demonstrated in vitro: PMID:15800015, PMID:17325244.)*
2. **Dominant-negative failure of intermediate-filament assembly.** Mutant desmin "is incapable of de novo formation of a desmin IF network" and blocks wild-type polymerization at a 1:3 ratio (PMID:15800015). This **results in** collapse of the extrasarcomeric desmin cytoskeleton that tethers Z-discs, costameres, nuclei, mitochondria and intercalated discs.
   - *Recessive branch:* biallelic LoF **leads to** absence or marked reduction of desmin (PMID:23575897, PMID:31024060). The **same** network loss follows, often **without** aggregates (PMID:42753430). This branch shows that network loss alone is sufficient for disease. Desmin-null mice point the same way: "the absence of desmin leads to muscle degeneration" (PMID:8794866).
3. **Misfolded desmin aggregates** (granulofilamentous material) that sequester partner proteins: αB-crystallin, Hsp27, plectin, synemin, syncoilin, filamin C and others. This **leads to** proteotoxic stress. The mutant protein causes "a general imbalance in skeletal muscle protein homeostasis", with increased proteasomal activity, stimulated macroautophagy and dysregulated chaperone-assisted selective autophagy (PMID:30179276). An impaired ubiquitin-proteasome system is seen in mouse hearts (PMID:16371426), and autophagic vacuolar pathology in human muscle (PMID:25557463).
   - *Contested point:* Clemen et al. argue that "not the presence of protein aggregates, but disruption of the" desmin network drives mechanical vulnerability (PMID:25394388). Aggregate toxicity versus network loss should be curated as **alternative or concurrent hypothesis groups**.
4. **Loss of mechanical coupling, leading to Z-disc streaming and myofibrillar disintegration.** Mechanical stress **results in** myofibril misalignment, sarcomere damage and fibre fragility (PMID:28715662, PMID:31341183, PMID:11352891). In the heart, damage to intercalated discs and desmosomes follows (R406W, PMID:33023321). *Partly inferred from mouse and in vitro data.*
5. **Mitochondrial dysfunction.** Without desmin anchoring, mitochondria become mispositioned, structurally abnormal and lose function. This **leads to** respiratory-chain defects, mtDNA deletions and depletion, impaired Ca²⁺ uptake and aberrant fission. "the expression of mutant desmin causes multi-level damage of mitochondria" (PMID:27393313; also PMID:25171807, PMID:32105824, PMID:29987122). This happens early and appears independent of aggregation (PMID:32105824).
6. **Cell degeneration and death** of cardiomyocytes and skeletal muscle fibres (necrosis, plus fibrosis and calcification in the heart, PMID:8794866, PMID:8626040), followed by **replacement fibrosis**.
7. **Clinical manifestations, branching by tissue:**
   - 7a. Conduction-system myocytes (sinoatrial node, His-Purkinje) **lead to** sinus node dysfunction, AV block and bundle-branch block. Desmin is "essential for sinoatrial node structure and function" (mouse, PMID:32678709). Conduction defects occur in desmin-deficient mice (PMID:20390331), and AV-node pathology with desmin deposition is seen at human autopsy (PMID:22336329 *[PMID unverified; Benvenuti 2012 retrieved as 22323329]*).
   - 7b. Working myocardium plus fibrosis **lead to** DCM, RCM, ACM or HCM, then ventricular arrhythmia, heart failure and sudden death.
   - 7c. Skeletal muscle **leads to** distal-to-proximal weakness and, through diaphragm involvement, respiratory failure.
   - 7d. Smooth muscle (inferred mainly from mice, PMID:8626040) **leads to** GI dysmotility.

### Checklist detail
- **Pathways:** intermediate-filament assembly; protein quality control (UPS, macroautophagy, CASA/BAG3–HSPB8); mitochondrial dynamics; Notch signalling is cardioprotective in S13F hiPSC-CMs (PMID:42843509, in vitro).
- **Protein dysfunction:** misfolding, aggregation and amyloid-like oligomers. In the related CRYAB R120G model, "high levels of amyloid oligomers" are reported (PMID:15220483). For desmin itself, this is an inference from the related model.
- **Immune system:** no primary role. Inflammatory infiltrates can mimic myocarditis (PMID:28491573).
- **Omics:** transcriptomic, phenotypic and machine-learning profiling of hiPSC-cardiomyocytes (PMID:40639258); mitochondrial proteomics in R405W knock-in mice (PMID:41165044); reduced proton leak and lower ADP/ATP translocase in R349P myotubes (PMID:38412640). No public single-cell or spatial atlases were identified.

### Suggested GO / CL terms (verify all)
- **GO BP:** GO:0045109 intermediate filament organization; GO:0045103 intermediate filament-based process; GO:0016236 macroautophagy; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process; GO:0007005 mitochondrion organization; GO:0006936 muscle contraction; GO:0060048 cardiac muscle contraction; GO:0086065 cell communication involved in cardiac conduction.
- **GO CC:** GO:0005882 intermediate filament; GO:0030018 Z disc; GO:0014704 intercalated disc; GO:0043034 costamere; GO:0042383 sarcolemma; GO:0005635 nuclear envelope; GO:0005739 mitochondrion; GO:0031594 neuromuscular junction.
- **CL:** CL:0000746 cardiac muscle cell; CL:0008002 skeletal muscle fiber; CL:0002068 Purkinje myocyte; CL:0000192 smooth muscle cell. The sinoatrial node cell term should be looked up.

---

## 7. Anatomical structures affected
- **Primary organs:** skeletal muscle (UBERON:0001134 skeletal muscle tissue), with the lower-limb distal compartments, the semitendinosus/gracilis/sartorius group and the diaphragm (UBERON:0001103) affected; heart (UBERON:0000948), myocardium (UBERON:0002349) and the conducting system of heart (UBERON:0002350).
- **Secondary:** respiratory system (through diaphragm and intercostal weakness); GI smooth muscle (rare); neuromuscular junction (recessive forms).
- **Whole-body MRI pattern:** in desminopathy, the iliopsoas, sartorius, gracilis and semitendinosus were each involved in 3/4 patients while the semimembranosus was spared in 3/4. Myotilinopathy differs (PMID:18648820). Peroneal-compartment involvement is also typical.
- **Lateralization:** bilateral and roughly symmetric.
- **Subcellular:** Z-disc, intercalated disc, costamere, perinuclear region, mitochondria (GO CC terms in §6).

---

## 8. Temporal development
- **Onset:** wide range, from neonatal or infantile (homozygous and de novo R406W) to the 6th decade. The median is about 20 years in the Mayo series (PMID:34315782) and the median age about 31 years in the meta-analysis (PMID:39968648). Clemen et al. describe onset "from childhood to late adulthood" (PMID:23143191).
- **Pattern:** insidious and slowly progressive. Cardiac disease may precede, follow or occur without skeletal disease. Conduction disease often appears in the 20s–30s and progresses to complete heart block (PMID:29915714).
- **Stages:** for KB `progression:`:
  1. asymptomatic carrier with subclinical myocardial fibrosis on CMR (PMID:18504128);
  2. conduction disease and early distal weakness;
  3. cardiomyopathy and proximal spread;
  4. advanced disease (wheelchair dependence, ventilatory failure, end-stage heart failure or transplantation).
- **Remission:** none spontaneously. Single-case LVEF recovery on guideline-directed medical therapy (GDMT) plus vericiguat has been reported (PMID:42062882; anecdotal).
- **Critical window:** before complete AV block or sustained VA, when surveillance (ECG, Holter, CMR) and device implantation can prevent sudden death.

---

## 9. Inheritance and population
- **Inheritance:** predominantly **autosomal dominant**, often de novo; **autosomal recessive** forms are rarer and probably under-recognised (PMID:42753430). Suggested terms (verify): HP:0000006 Autosomal dominant inheritance; HP:0000007 Autosomal recessive inheritance.
- **Penetrance:** incomplete and age-dependent. "Familial penetrance of cardiac disease was 63.6% among relatives with pathogenic/LP DES variants" (PMID:39968648).
- **Expressivity:** highly variable, even within a family (PMID:17439987).
- **Anticipation:** none (not a repeat disorder).
- **Germline mosaicism:** possible, but no systematic data were found.
- **Founder effects:** R350P is recurrent in German families (PMID:17439987, PMID:18504128). Cohorts are also described from China (PMID:20696008, PMID:30614851), Poland (PMID:25541946), India (PMID:24441330), Russia (PMID:17626518) and Turkey (recessive, PMID:23687351).
- **Prevalence:** **not documented** as a population rate. Desminopathy is a minority of MFM cases. *DES* accounts for about 1–2% of DCM (PMID:17325244). Record `prevalence_class: NOT_YET_DOCUMENTED` or `RARE` with `measure_type: UNKNOWN`, unless the Orphanet ORPHA:98909 cache supplies a figure.
- **Sex ratio:** roughly 1:1 among carriers (52.6% men, PMID:39968648). Men carry more arrhythmic and heart-failure risk.

---

## 10. Diagnostics
- **Laboratory:** CK is normal to mildly or moderately raised; troponin and NT-proBNP rise with cardiac involvement (PMID:42062882).
- **Electrophysiology:** ECG and Holter for AV block, bundle-branch block and VA; EMG showing myopathic and myotonic or complex repetitive discharges; electrophysiology studies for infra-Hisian block (PMID:39627986).
- **Imaging:**
  - Muscle MRI or whole-body MRI to identify the pattern (PMID:18648820, PMID:33546848, PMID:41406637).
  - Cardiac MRI, which "is superior to conventional echocardiography for the detection of early" cardiac involvement (PMID:18504128). A ring-like LGE pattern has been described (PMID:42062882).
- **Biopsy:** MFM pathology: desmin-positive subsarcolemmal and cytoplasmic aggregates, granulofilamentous material on EM, Z-disc streaming, rimmed or autophagic vacuoles (PMID:25557463). Immunostaining also detects αB-crystallin, myotilin and filamin C. These features may be **absent in recessive disease** (PMID:42753430, PMID:31024060).
- **Genetic testing:** NGS cardiomyopathy and neuromuscular (MFM/LGMD/distal myopathy) panels, or exome/genome sequencing. Single-gene *DES* testing is appropriate when MFM histology points to it. Functional assembly assays help classify VUS. RNA studies are needed for deep intronic variants (PMID:31024060). CMA, karyotype, FISH, mtDNA and repeat testing are **not** indicated.
- **Differential diagnosis:**
  - other MFM genes: *CRYAB*, *MYOT*, *LDB3/ZASP*, *FLNC*, *BAG3*, *DNAJB6*, *TTN*, *FHL1*, *PLEC* (myotilin MFM, PMID:15111675);
  - *LMNA* (cardiac conduction disease plus muscular dystrophy);
  - Emery-Dreifuss muscular dystrophy;
  - desmosomal ARVC;
  - sporadic inclusion-body myositis;
  - cardiac sarcoidosis and myocarditis (mimics, PMID:28491573).
- **LOINC:** CK in serum (look up the Long Common Name; do not type it). Do not bind method-level codes.
- **Screening:** cascade genetic testing of relatives with serial ECG, Holter and CMR. No newborn screening exists.

---

## 11. Outcome / prognosis
- **Mortality:** cardiac disease is the main cause of premature death (sudden death, heart failure), followed by respiratory failure (PMID:14724127, PMID:20718792). The meta-analysis reported no separate survival or transplant rates (PMID:39968648).
- **Morbidity:** MACE in 57.4%, conduction disease in 41.7%, sustained VA in 15.7% and HF events in 18.7% (PMID:39968648). Many patients need a permanent pacemaker (11/25) or an ICD (5/25), and 3/25 underwent transplantation (PMID:34315782). Progressive weakness leads to wheelchair dependence.
- **Prognostic factors:** male sex (VA, HF); early onset and homozygous or de novo R406W genotypes are severe; the RCM phenotype carries a poor prognosis; LGE on CMR.
- **Recovery potential:** limited. Heart transplantation improves cardiac function and QoL (PMID:34315782).

---

## 12. Treatment

No disease-modifying therapy exists: "no specific treatment is currently available for this severely disabling disease" (PMID:23143191). Suggested NCIT terms (verify; the general action terms appear in the project CLAUDE.md):

| Intervention | NCIT action term (verify) | `therapeutic_modality` | Evidence |
|---|---|---|---|
| Permanent pacemaker for AV block | NCIT:C15329 Surgical Procedure + device qualifier (NCIT:C16830 Medical Device → look up the pacemaker term) | DEVICE | 11/25 required one (PMID:34315782) |
| ICD for primary or secondary prevention of SCD | as above, with an ICD device term | DEVICE | PMID:34315782; the HRS 2019 ACM consensus lists *DES* (PMID to be fetched) |
| Guideline-directed heart-failure therapy (ACEi/ARNI, β-blocker, MRA, SGLT2i; vericiguat in one case) | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` | SMALL_MOLECULE | PMID:42062882 (single case) |
| Heart transplantation | NCIT:C15289 Organ Transplantation (or a more specific heart-transplant term after lookup) | SURGERY | PMID:34315782 |
| Non-invasive ventilation | look up the NCIT ventilation procedure term | DEVICE | supportive; reviews |
| Physical therapy / rehabilitation | NCIT:C15302 / NCIT:C15315 | BEHAVIORAL | supportive |
| Genetic counseling | NCIT:C15240 | — | standard |

**Experimental and preclinical:**
- **AAV9-desmin gene transfer.** In desmin-null mice it gave "improved systolic left-ventricular function" (PMID:27101257). At high dose it was "highly beneficial for the heart in DKO animals", but "Treated DKI mice, however, showed an aberrant subcellular localization of desmin" (PMID:32322014). The approach is therefore plausible for **recessive** null disease and ineffective, or even harmful, for **dominant-negative** disease. Allele-specific silencing (ASO/siRNA) of the mutant allele is a logical but untested strategy.
- **Anti-aggregation drugs.** In C2C12 models, Rac1 inhibition, antioxidants and autophagy induction reduced aggregation "by up to 75%", and combinations worked better than single agents (PMID:26333167, in vitro).
- **Notch activation** in hiPSC-CMs (PMID:42843509, in vitro).
- **Clinical trials:** no desminopathy-specific interventional trials were identified. Search ClinicalTrials.gov for "desmin" and "myofibrillar myopathy" before stating that none exist.

---

## 13. Prevention
- **Primary:** none, apart from reproductive options (prenatal or preimplantation genetic testing in families with a known variant).
- **Secondary:** cascade screening of relatives (penetrance 63.6%), with serial ECG/Holter, echocardiography and CMR from adolescence. CMR detects subclinical fibrosis (PMID:18504128).
- **Tertiary:** prophylactic pacemaker or ICD before complete heart block or VA; respiratory monitoring (FVC, sleep studies); avoiding strenuous eccentric exercise is a cautious extrapolation from mouse data (PMID:40947309).
- **Counseling:** a 50% recurrence risk for AD disease. Germline mosaicism should be discussed when a variant appears de novo. Recessive forms carry a 25% recurrence risk.
- **Vaccines and public health:** not applicable.

---

## 14. Other species / natural disease
- **Orthologs:** mouse *Des* (NCBITaxon:10090; MGI and NCBI Gene IDs to be looked up); zebrafish *desma*/*desmb* (NCBITaxon:7955); desmin is highly conserved across vertebrates.
- **Natural disease:** **no naturally occurring *DES*-variant disease was identified** in companion animals or livestock. The OMIA search returned nothing in this session. Warmblood and Arabian equine "myofibrillar myopathy" shows desmin-positive aggregates but has not been linked to *DES*. Do not curate it as a natural model without a source.
- **Zoonotic potential:** none.

---

## 15. Model organisms

| Model | Genotype / type | Recapitulation | Limitations | PMID |
|---|---|---|---|---|
| Desmin-null mouse (two independent lines) | *Des*⁻/⁻ KO | Viable and fertile. Progressive cardiomyopathy with necrosis and calcification, diaphragm myopathy, smooth-muscle lesions, conduction defects and sinoatrial-node dysfunction. | Models **recessive** null disease, not dominant-negative aggregate disease. | 8794866; 8626040; 20390331; 32678709; 11827695 |
| R349P knock-in mouse (ortholog of human R350P) | Heterozygous and homozygous KI | Age-dependent desmin aggregates, "skeletal muscle weakness, dilated cardiomyopathy, as well as cardiac arrhythmias"; mitochondrial and proteostasis defects; early biomechanical failure. | Mild in heterozygotes; the mouse lifespan compresses an adult-onset human disease. | 25394388; 27393313; 30179276; 31341183; 40947309 |
| R405W knock-in mouse | KI | MFM with mitochondrial and proteostasis changes. | Recent; little independent replication. | 41165044 |
| D7-des transgenic mouse | Cardiac-restricted transgene (7-aa deletion) | Desmin aggregates; "myofibril alignment was visibly compromised"; dominant negative. | Overexpression; heart only. | 11352891; 19299643 |
| CryAB R120G transgenic mouse | Chaperone phenocopy | Aggresomes and amyloid oligomers in desmin-related cardiomyopathy. | *CRYAB*, not *DES*. Use only for mechanism. | 15220483; 10339554 |
| Zebrafish desmin KO | *desma* KO | Altered Ca²⁺ flux without skeletal-muscle degeneration. | Teleost duplication; mild phenotype. | 33820917 |
| hiPSC-derived cardiomyocytes and engineered heart tissue | Patient-derived or edited | Mitochondrial dysfunction, transcriptomic signatures, viral susceptibility, Notch rescue. | Immature cells; no conduction-system or skeletal context. | 38167524; 40639258; 41761335; 42843509 |
| hiPSC skeletal-muscle micro-tissues (R349P) | Edited | Increased contractility and fragility. | In vitro. | 34850968 |
| C2C12 / SW13 / BMGE cell transfection | Overexpression | Assembly defect; aggregate formation; drug screening. | Overexpression artefacts. | 15800015; 26333167; 37277577 |

Repositories: MGI, IMSR and MMRRC for mouse lines; ZFIN for zebrafish; Cellosaurus for hiPSC lines. For KB curation, the R349P line is the best `animal_models` entry for the **dominant** mechanism (`RECAPITULATES`, `fidelity: MODERATE`). The KO line should be linked as `RECAPITULATES` for the recessive network-loss branch and `PARTIALLY_RECAPITULATES` for the dominant disease.

---

## Key references (PMIDs retrieved in this session)

- Goldfarb LG et al. 1998 *Nat Genet*. Missense mutations in desmin associated with familial cardiac and skeletal myopathy. **PMID:9697706**
- Dalakas MC et al. 2000 *N Engl J Med*. Desmin myopathy, a skeletal myopathy with cardiomyopathy caused by mutations in the desmin gene. **PMID:10717012**
- Goldfarb LG et al. 2004 *Brain*. Desmin myopathy. **PMID:14724127**
- Bär H et al. 2005 *Hum Mol Genet*. R350P desmin assembly. **PMID:15800015**
- Walter MC et al. 2007 *Brain*. R350P desmin and Kaeser-type scapuloperoneal syndrome. **PMID:17439987**
- Taylor MR et al. 2007 *Circulation*. Prevalence of desmin mutations in DCM. **PMID:17325244**
- Strach K et al. 2008 *Neuromuscul Disord*. Cardiac MRI in primary desminopathies. **PMID:18504128**
- Schramm N et al. 2008 *Eur Radiol*. Whole-body MRI in myotilinopathy and desminopathy. **PMID:18648820**
- van Spaendonck-Zwarts KY et al. 2011 *Clin Genet*. Desmin-related myopathy (meta-analysis, n=159). **PMID:20718792**
- Clemen CS et al. 2013 *Acta Neuropathol*. Desminopathies: pathology and mechanisms. **PMID:23143191**
- Clemen CS et al. 2015 *Acta Neuropathol*. R350P/R349P knock-in. **PMID:25394388**
- Winter L et al. 2016 *Acta Neuropathol*. Mitochondrial damage. **PMID:27393313**
- Heckmann MB et al. 2016 *Gene Ther*. AAV9-desmin in KO mice. **PMID:27101257**
- Ruppert T et al. 2020 *Gene Ther*. AAV9-desmin in DKO vs DKI mice. **PMID:32322014**
- Brodehl A et al. 2018 *Biophys Rev*. Desmin cardiomyopathies review. **PMID:29926427**
- Shelly S et al. 2021 *Neurology*. Mayo desminopathy series. **PMID:34315782**
- Asatryan B et al. 2025 *Circ Genom Precis Med*. IPD meta-analysis of DES cardiomyopathy (n=230). **PMID:39968648**
- Keogh MJ et al. 2026 *Neuromuscul Disord*. Autosomal recessive desminopathy. **PMID:42753430**
- Milner DJ et al. 1996 *J Cell Biol*. **PMID:8794866**; Li Z et al. 1996 *Dev Biol*. **PMID:8626040**. Desmin-null mice.

**Web sources consulted:** [Desminopathies: pathology and mechanisms (PMC3535371)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3535371/) · [PMC6082305](https://pmc.ncbi.nlm.nih.gov/articles/PMC6082305) · [PMC2701871](https://pmc.ncbi.nlm.nih.gov/articles/PMC2701871) · [medRxiv DES cardiomyopathy preprint](https://www.medrxiv.org/content/10.1101/2024.08.24.24311904.full.pdf) · [MedlinePlus DES](https://medlineplus.gov/genetics/gene/des) · [OLS MONDO:0016187](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0016187) · [AAV desmin gene transfer (OUCI)](https://ouci.dntb.gov.ua/works/l1KRzeo7/) · [JCI 38027](https://jci.org/articles/view/38027) · NCBI E-utilities (esearch, esummary, efetch).

**Gaps to close before curation:**
- Byte-verify every quote with `just fetch-reference`.
- Confirm the Benvenuti 2012 PMID (22323329).
- Fetch the PMID for the HRS 2019 ACM consensus statement.
- Check whether a GeneReviews chapter exists (`just check-genereviews`). None was found in this session.
- Pull ClinGen CGGV records for DES.
- Look up every HPO, GO, CL, UBERON, NCIT and LOINC CURIE suggested above before binding it.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 79 |
| Resolved | 79 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 79 |
| On topic | 68 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25171807` *(abstract only)*: "the expression of mutant desmin causes multi-level damage of mitochondria"
  - closest text in source: "Desmin, being a major intermediate filament of mature muscle cell, interacts with mitochondria within the cell and participates in mitochondria proper localization"
- `PMID:32105824` *(abstract only)*: "the expression of mutant desmin causes multi-level damage of mitochondria"
  - closest text in source: "The aim of the present study was to describe how expression of different desmin mutant isoforms effects mitochondria and contributes to the development of myocyte dysfunction"
- `PMID:29987122` *(abstract only)*: "the expression of mutant desmin causes multi-level damage of mitochondria"
  - closest text in source: "Overexpression of mutant desmin by adenoviral infection in cultured cardiomyocytes led to increased mitochondrial fission, inhibition of mitochondrial respiration, and activation of cellular toxicity"
- `PMID:32678709` *(abstract only)*: "essential for sinoatrial node structure and function"
  - closest text in source: "Our objective was to investigate the effect of desmin depletion on the structure and function of the sinoatrial pacemaker complex (SANcl) and its implication in arrhythmogenesis"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22336329` (1 mention) - Polycomb: a paradigm for genome organization from one to three dimensions.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `des`, `disease`, `desmin`, `cardiac`, `recessive`, `myopathy`, `variant`, `cardiomyopathy`, `heart`, `gene`, `skeletal`, `mice`, `conduction`, `muscle`, `block`, `mouse`, `mutation`, `weakness`, `assembly`, `failure`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 79 |
| Resolved | 67 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 11 |
| Terms whose name was checked | 15 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011663` (1 mention) - the report calls it "verify the ARVC term"; HP calls it **Right ventricular cardiomyopathy**
- `HP:0032654` (1 mention) - the report calls it "verify"; HP calls it **Impaired flow-mediated arterial dilatation**
- `NCBITaxon:7955` (1 mention) - the report calls it "desmb"; NCBITaxon calls it **Danio rerio**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `DOID:0110286` (obsolete autosomal recessive limb-girdle muscular dystrophy type 2R) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0016187` (6 mentions) - the report calls it "qualitative or quantitative defects of desmin** (the target term)"; MONDO calls it **qualitative or quantitative defects of desmin**
- `MONDO:0011076` (3 mentions) - the report calls it "myofibrillar myopathy 1 (desminopathy; MFM1)"; MONDO calls it **myofibrillar myopathy 1**
- `MONDO:0011482` (1 mention) - the report calls it "dilated cardiomyopathy 1I (CMD1I)"; MONDO calls it **dilated cardiomyopathy 1I**
- `MONDO:0018098` (1 mention) - the report calls it "autosomal dominant LGMD type 1E (DES)"; MONDO calls it **autosomal dominant limb-girdle muscular dystrophy type 1E (DES)**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `GARD`, `OMIM`, `ORPHA`.