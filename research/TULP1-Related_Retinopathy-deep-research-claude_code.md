---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-10T18:32:25.248104'
end_time: '2026-11-10T18:38:32.479516'
duration_seconds: 367.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TULP1-Related Leber Congenital Amaurosis
  mondo_id: MONDO:0013457
  category: Mendelian
  causal_genes: TULP1
  omim_id: OMIM:613843
  synonyms: LCA15; Leber congenital amaurosis caused by mutation in TULP1; Leber congenital
    amaurosis type 15; TULP1 Leber congenital amaurosis
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
  num_turns: 22
  total_cost_usd: 2.6511424000000003
  session_id: 89bd0667-a693-4eac-824e-1b78181aebdc
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
reference_validation:
  total_references: 39
  verified: 36
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.077
  quotes_checked: 32
  quotes_valid: 29
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:25342276
  - PMID:31087526
  - PMID:41493298
  quotes_not_checkable: 9
  relevance_assessed: 36
  on_topic: 30
  unresolved_references:
  - PMID:36128853
  - PMID:25074776
  - PMID:9462750
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 3
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0007754
    reported_labels:
    - Bull's eye maculopathy
    ontology_label: Macular dystrophy
  - term_id: HP:0007843
    reported_labels:
    - Retinal arteriolar attenuation
    ontology_label: Attenuation of retinal blood vessels
  - term_id: CL:0000604
    reported_labels:
    - CL:** rod photoreceptor cell
    ontology_label: retinal rod cell
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TULP1-Related Leber Congenital Amaurosis
- **MONDO ID:** MONDO:0013457 (if available)
- **Causal gene(s):** TULP1
- **OMIM:** OMIM:613843
- **Synonyms:** LCA15; Leber congenital amaurosis caused by mutation in TULP1; Leber congenital amaurosis type 15; TULP1 Leber congenital amaurosis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TULP1-Related Leber Congenital Amaurosis** covering all of the
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


# TULP1-Related Leber Congenital Amaurosis (LCA15): Research Report

**Target:** MONDO:0013457 · OMIM:613843 · causal gene **TULP1** (tubby-like protein 1; HGNC:12423, written `hgnc:12423` in dismech) · autosomal recessive

> **Note on identifiers.** Every PMID cited below, and every quoted abstract sentence, was fetched from PubMed's E-utilities during this session. The ClinGen record came from the repository's committed `cache/clingen/gene_validity.csv`. The ontology CURIEs I suggest (HP, GO, CL, UBERON, NCIT, MGI/ZFIN) are **leads from memory and were not looked up**. Per the repository's term contract, check each one with `runoak`/OLS or `just validate-terms` before binding it. The OLS lookup for MONDO xrefs timed out (it returned an empty response), so the Orphanet and ICD codes below are also unverified.

---

## 1. Disease Information

**Overview.** LCA15 is the Leber congenital amaurosis (LCA) form caused by biallelic pathogenic variants in **TULP1**. TULP1 is a protein found only in photoreceptors, and it is needed to transport outer-segment proteins and to keep the photoreceptor ribbon synapse working. Patients have nystagmus and severe visual impairment from infancy, with absent or barely detectable rod and cone electroretinograms (ERGs). The same gene causes early-onset severe retinal dystrophy (EOSRD) and early-onset retinitis pigmentosa (RP14). LCA15 is the most severe end of one continuous spectrum. Within a single family, some affected members are diagnosed with LCA and others with early-onset retinal degeneration:

> "Seven of 30 examined family members were affected, including five with EORD and two with LCA." (PMID:17962469)

| Identifier | Value | Status |
|---|---|---|
| MONDO | MONDO:0013457 "Leber congenital amaurosis 15" | confirmed via ClinGen cache row |
| OMIM (phenotype) | 613843 | given in brief |
| OMIM (gene) | 602280 (TULP1) | from memory, verify |
| Allelic RP | RP14 (OMIM 600132) | from memory, verify |
| Orphanet | ORPHA:65 (Leber congenital amaurosis, umbrella) | from memory, verify; no LCA15-specific ORPHA code is known to me |
| ICD-10 | H35.5 (hereditary retinal dystrophy) | verify |
| MeSH | D057130 Leber Congenital Amaurosis | verify |
| HGNC | HGNC:12423 | confirmed (ClinGen row) |

**Synonyms:** LCA15; Leber congenital amaurosis type 15; TULP1 Leber congenital amaurosis; Leber congenital amaurosis caused by mutation in TULP1. Related allelic labels: TULP1-associated IRD, RP14, EOSRD/EORD.

**Source of information:** aggregated disease-level resources (OMIM, ClinGen, GeneReviews overview PMID:30285347) plus case series and cohorts of individual patients (PMIDs 17962469, 25074776, 36128853, 36769033, 25342276).

## 2. Etiology

- **Cause:** biallelic germline loss-of-function or misfolding variants in TULP1 (chromosome 6p21.3). There are no environmental or infectious causes.
- **ClinGen gene-disease validity (copied from the cache, not assigned by me):**
  `TULP1 | HGNC:12423 | Leber congenital amaurosis 15 | MONDO:0013457 | AR | Definitive` (Retina GCEP, SOP11, 2025-06-05). Assertion ID: `CGGV:assertion_ecc6101d-f936-48a2-b2f1-34bfd785542d-2025-06-05T160000.000Z`. This is the same MONDO term as the entry's `disease_term`, so it qualifies for `gene_disease_validity`.
- **Genetic risk factors:** consanguinity, and founder alleles in particular populations (see §9). Maternal uniparental isodisomy of chromosome 6 can unmask a recessive TULP1 variant (PMID:30090012; PMID:23499059, the latter in a cone-dysfunction phenotype). Title-level only: I did not read these abstracts.
- **Modifier genes:** none established in humans. Mataftsi et al. raised the possibility for the variability within one family:
  > "The observed intrafamilial phenotypic variability could be attributed to disease progression or possibly modifier alleles." (PMID:17962469)

  In mouse, a protective **Mtap1a** allele reduces photoreceptor loss:
  > "The protective Mtap1a(129P2/OlaHsd) allele was shown to reduce photoreceptor loss in both Tulp1(tm1Pjn/tm1Pjn) and Tub(tub/tub) mice." (PMID:22323461, MODEL_ORGANISM)
- **Protective factors and gene-environment interactions:** none reported.

## 3. Phenotypes

The core features below come from human cohorts. Frequencies are given only where a source states them.

| Phenotype | Suggested HP (verify) | Onset / course | Frequency / source |
|---|---|---|---|
| Nystagmus | HP:0000639 | from soon after birth | "All patients had nystagmus, hemeralopia, mild myopia, and low visual acuity" (PMID:17962469, 7/7); "All 10 children … had nystagmus since soon after birth" (PMID:25342276, 10/10) |
| Severely reduced visual acuity | HP:0007663 / HP:0001141 | infantile, progressive | homozygotes "visual acuity of 20/200 or worse" (PMID:10440267); mean loss of 0.027 logMAR/yr (PMID:36128853) |
| Undetectable ERG (rod and cone) | HP:0000550 | from first assessment | "Both scotopic and photopic electroretinograms were nondetectable" (PMID:17962469); "No evidence of rod function was present at any age" (PMID:25074776) |
| Nyctalopia / hemeralopia | HP:0000662 | early | PMID:17962469. Note that the paper says "hemeralopia", whose meaning is ambiguous in the literature. Bind with care. |
| Pigmentary retinopathy, salt-and-pepper changes leading to bone spicules | HP:0000580; HP:0007737 | fundus normal in infancy, then evolves | "Retinal ophthalmoscopy was primarily normal converting to peripheral pigmentary retinopathy and maculopathy" (PMID:36128853) |
| Bull's eye maculopathy | HP:0007754 | childhood | homozygotes had "bull's eye maculopathy, and peripheral pigmentary retinopathy" (PMID:10440267) |
| Perifoveal hyperautofluorescent ring | (no specific HP; possibly HP:0030496-type FAF term, verify) | childhood | PMID:17962469; PMID:25342276 |
| Retinal arteriolar attenuation | HP:0007843 | childhood | PMID:25342276 |
| Abnormal color vision | HP:0000551 | — | PMID:10440267 |
| Constricted visual field / peripheral islands | HP:0001133 | progressive with age | "older patients had only peripheral islands" (PMID:10440267) |
| Refractive error: hyperopia (Arabian founder series) or mild myopia (Algerian family) | HP:0000540 / HP:0000545 | — | PMID:25342276 vs PMID:17962469; genuinely variable |
| Outer retinal (photoreceptor) thinning on OCT | — | progressive, starting outside the fovea | "progressive extra-foveal loss of the ellipsoid zone (EZ), the outer plexiform layer (OPL), and the outer nuclear layer (ONL)" (PMID:36128853) |
| Absence of photophobia | negation, do not bind | — | PMID:17962469 |

**Quality of life.** No EQ-5D or SF-36 data specific to TULP1 were found. The impact is lifelong severe visual disability that begins in infancy.

## 4. Genetic / Molecular Information

- **Gene:** TULP1, HGNC:12423, 6p21.3. The protein has an N-terminal region and a conserved C-terminal "tubby" domain of about 200 residues (PMID:9462750). The first TULP1 RP mutations: "Three of the mutations are missense changes affecting the conserved C-terminal region; the fourth mutation affects a splice donor site" (PMID:9462750).
- **Variant classes:** missense (clustered in the tubby domain), nonsense, frameshift, splice, and in-frame indels. The largest cohort found "eight missense variants, six nonsense variants, one in-frame deletion variant, and two splice site variants" (PMID:36769033).
- **Named alleles:**
  - c.901C>T p.(Gln301*): Arabian Peninsula founder (PMID:25342276).
  - c.148delG: Finnish founder, "associated with infantile and early childhood onset IRD" (PMID:36128853; founder status also reported in PMID:31087526, title-level).
  - IVS14+1G>A: Dominican kindreds (PMID:10440267; PMID:9462751).
  - A 6-bp in-frame duplication in an Algerian family (PMID:17962469).
  - p.F492L and p.D89Y, modelled as knock-in mice (PMID:41493298).
- **Functional consequence:**
  - Truncating alleles cause loss of function. Minigene assays showed the splice variants produce "aberrant transcripts containing frameshifts and premature termination codons" (PMID:36769033).
  - Missense alleles cause misfolding, ER retention and the unfolded protein response (UPR). Lobo et al. showed "common missense mutations in TULP1 express as misfolded protein products that accumulate within the endoplasmic reticulum (ER)" (PMID:26987071, IN_VITRO). Whether this is a toxic gain on top of loss of function is not settled. Use `LOSS_OF_FUNCTION` for truncating alleles. Do not assert `DOMINANT_NEGATIVE`: heterozygotes are normal ("Heterozygotes had normal visual function", PMID:10440267).
- **Origin:** germline, biallelic (homozygous in consanguineous families, otherwise compound heterozygous).
- **Contribution to LCA:** small. TULP1 accounted for 1.7% of a 179-patient LCA series: "GUCY2D appeared to account for most LCA cases of our series (21.2%), followed by CRB1 (10%), RPE65 (6.1%), RPGRIP1 (4.5%), AIPL1 (3.4%), TULP1 (1.7%)" (PMID:15024725). This is a candidate `case_fractions` record (population: French LCA series, Hanein 2004).
- **Allele frequencies (gnomAD), epigenetics, chromosomal abnormalities:** not retrieved. No epigenetic mechanism is known. UPD6 is the only chromosomal mechanism reported.

## 5. Environmental Information

Not applicable. No environmental, lifestyle or infectious contributors are reported. The `environmental:` section should stay empty.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic TULP1 variants** (truncating or misfolding) **lead to** absence of functional TULP1 in rod and cone photoreceptors. *(Human genetics + mouse; demonstrated.)*
2. **Branch A: inner segment trafficking.** Loss of TULP1 **results in** misrouting of nascent rhodopsin, cone opsins and the guanylate cyclase carrier pathway from the inner segment to the outer segment. *(Mouse; demonstrated.)*
   - "A lack of TULP1 function results in misrouting of nascent rhodopsin." (PMID:11481257)
   - "guanylate cyclase 1 and guanylate cyclase activating proteins 1 and 2 are mislocalized in the absence of Tulp1" (PMID:21867699)
   - Interactors suggest an adapter that links vesicles to motors: "an IS-specific interaction between Tulp1 and the motor protein Kinesin family member 3a (Kif3a)" (PMID:34360830). TULP1 is also needed for PRCD localization to the outer segment (PMID:33213002).
   - 2a. Misrouted opsin **leads to** rhodopsin-bearing extracellular vesicles collecting around the inner segment: "Electron microscopy revealed massive accumulation of extracellular vesicles surrounding the distal inner segments." (PMID:10549638)
3. **Branch B: ribbon synapse.** Loss of TULP1 at the presynaptic terminal **leads to** disrupted ribbons and impaired periactive-zone endocytosis. That in turn **causes** stunted bipolar cell dendrites and reduced signal transmission, *before* photoreceptors degenerate. *(Mouse; demonstrated.)*
   - "Tulp1 is essential to keep endocytic proteins enriched at the periactive zone and to maintain high levels of endocytic activity close to the synaptic ribbon" (PMID:26911694)
   - "the spatial relationship between the ribbon-associated proteins Bassoon and Piccolo are disrupted, and few intact ribbons are present. Furthermore, bipolar cell dendrites are stunted." (PMID:19218615)
   - This may explain the human "preserved but insensitive" foveal cones (PMID:25074776). That link is *inferred*.
4. **Branch C: missense alleles.** Misfolded TULP1 is retained in the ER, which **results in** prolonged ER stress and activation of the PERK and IRE1 arms of the UPR, with CHOP upregulation. *(In vitro, plus 2026 knock-in mice.)*
   - "the two major apoptotic arms of the UPR pathway, PERK and IRE1, are activated" (PMID:26987071)
   - In vivo: "activation of the IRE1 branch … in Tulp1-/- and Tulp1F492L retinas" (PMID:41493298). Note that IRE1 is also active in the *null* mouse, so ER stress is not limited to misfolded protein.
5. **Steps 2–4 converge on** apoptotic death of rods and then cones. Zebrafish data suggest ferroptosis as a further death pathway *(model, suggestive)*: "ferroptosis might be activated in the tulp1-dKO zebrafish" (PMID:36396940).
6. **Photoreceptor loss leads to** absent ERG, nystagmus from infancy, nyctalopia, and progressive loss of acuity and visual field. Secondary RPE changes **lead to** pigmentary retinopathy and bull's eye maculopathy. *(Human; demonstrated clinically.)*
7. **Possible branch D (speculative):** TULP1 may act as a MerTK "eat-me" ligand for RPE phagocytosis of shed outer segments (PMID:20978472, IN_VITRO). Its relevance to the disease is undemonstrated, so keep it as an emerging hypothesis at most.
8. **Possible branch E:** non-photoreceptor expression. Mouse Tulp1 is detected in the inner retina, and "lack of TULP1 may lead to primary degeneration not only of photoreceptor but also non-photoreceptor cells" (PMID:32655363). In human tissue, "A few inner nuclear and ganglion cells are weakly TULP1-positive" (PMID:10892883). Evidence is weak.

### Suggested ontology terms (all need verification)

- **GO:** protein transport to the photoreceptor outer segment / "protein localization to photoreceptor outer segment"; rhodopsin-containing vesicle trafficking; synaptic vesicle endocytosis (GO:0048488); photoreceptor ribbon synapse (GO:0098684, a cellular component); response to endoplasmic reticulum stress (GO:0034976); IRE1-mediated unfolded protein response (GO:0036498); PERK-mediated UPR (GO:0036499); photoreceptor cell death / retinal cell apoptotic process; ferroptosis (GO:0097707, mark as model-only); phagocytosis (MerTK branch).
- **CL:** rod photoreceptor cell (CL:0000604); cone photoreceptor cell (CL:0000573); retinal bipolar neuron (CL:0000748); retinal pigment epithelial cell (CL:0002586).
- **Biological scale:** step 1 is MOLECULAR; steps 2–4 are CELLULAR; photoreceptor degeneration is CELLULAR or TISSUE; clinical blindness is ORGANISM.
- **Molecular profiling:** zebrafish RNA-seq found *tekt2* downregulated (PMID:36396940). Interactome by IP-MS (PMID:34360830). No human omics.

## 7. Anatomical Structures Affected

- **Organ:** retina, bilateral and symmetric (UBERON:0000966 retina; UBERON:0000970 eye). The disease is non-syndromic: the knockout mouse showed "normal hearing ability and, surprisingly, normal body weight" (PMID:10607826), unlike the related tubby (*Tub*) mouse.
- **Tissue:** photoreceptor layer / outer nuclear layer, outer plexiform layer, ellipsoid zone, macula and fovea (UBERON:0000053 macula lutea; UBERON:0001786 fovea centralis), RPE.
- **Subcellular (GO CC):** photoreceptor inner segment (GO:0001917), cytoplasm, synapse; TULP1 is excluded from the outer segment and the nucleus: "TULP1 is distributed throughout the photoreceptor cytoplasm but is excluded from the outer segments and the nuclei" (PMID:11481257). ER retention applies to missense alleles.
- **Development:** expressed in human fetal cones from 8.4–11 weeks (PMID:10892883).

## 8. Temporal Development

- **Onset:** congenital or infantile. Nystagmus appears "since soon after birth" (PMID:25342276).
- **Progression:** progressive. "The TULP1-RD patients were severely affected already in the first decade of life and there was rapidly progressive visual loss" (PMID:25074776). Modelled acuity loss is 0.027 logMAR per year (PMID:36128853).
- **Stages (suggested `progression:` phases):**
  1. Infancy: nystagmus and absent ERG with a near-normal fundus.
  2. Childhood: peripheral pigmentary change, a perifoveal hyperautofluorescent ring, and residual cone function.
  3. Later childhood and adulthood: loss of the recordable cone ERG, maculopathy, and only peripheral visual-field islands.
- **Critical window:** "suggesting a potential time window for therapeutic interventions" (PMID:36128853). The preserved foveal cone island in early life (PMID:25074776) is the treatment target.
- **Remission:** none.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007), ClinGen AR Definitive. Heterozygous carriers are unaffected (PMID:10440267). No anticipation. Penetrance appears complete for biallelic null alleles. Expressivity varies even within families (PMID:17962469). The spectrum covers LCA, EORD, adult-onset RP and cone/cone-rod dystrophy (PMID:36769033).
- **Epidemiology:** no LCA15-specific prevalence figure exists. LCA as a whole is commonly cited at roughly 1–3 per 100,000 (not retrieved this session, so needs a source), and TULP1 accounts for about 1.7% of LCA in one series (PMID:15024725). "Mutation in the TULP1 gene is a rare cause of LCA/EORD" (PMID:17962469). Use `prevalence_class` cautiously, or `CASES_IN_LITERATURE`.
- **Founder effects and geography:**
  - Arabian Peninsula, p.Gln301*: "represents a founder mutation on the Arabian Peninsula" (PMID:25342276).
  - Finland: c.148delG.
  - Dominican Republic: IVS14+1G>A.
  - Pakistan (PMID:20065226: one of 14 LCA families; PMID:39766915, title-level).
  - Algeria (PMID:17962469).
- **Consanguinity:** a major contributor; homozygosity mapping found TULP1 in consanguineous LCA and juvenile RP families (PMID:18055821, title and summary).
- **Sex ratio:** expected 1:1. No data.
- **Carrier frequency:** not retrieved (gnomAD not queried).

## 10. Diagnostics

- **Electrophysiology:** full-field ERG is non-recordable or reduced to microvolt-level cone responses (PMID:10440267). Pupillometry can quantify residual rod and cone activity in LCA (PMID:22801849, title-level).
- **Imaging:** spectral-domain OCT (ellipsoid zone width and OPL-ONL thickness as disease-stage biomarkers): "The width of the foveal EZ and the thickness of the foveal OPL-ONL layers could serve as biomarkers of the disease stage" (PMID:36128853). Fundus autofluorescence shows a perifoveal hyperautofluorescent ring (PMID:17962469, PMID:25342276).
- **Psychophysics:** kinetic and chromatic static perimetry (PMID:25074776).
- **Genetic testing:** an inherited retinal disease (IRD) or LCA multigene panel, or exome/genome sequencing. Whole-exome sequencing finds novel TULP1 alleles that targeted approaches miss (PMID:24547928, title). Homozygosity mapping helps in consanguineous families (PMID:18055821). Consider UPD6 testing when only one parent carries the variant (PMID:30090012). Minigene assays for splice variants (PMID:36769033). Single-gene testing is suitable for founder alleles in Arabian or Finnish patients.
- **Laboratory biomarkers:** none. LOINC is not applicable beyond genetic test codes.
- **Differential diagnosis:** other LCA/EOSRD genes (GUCY2D, CRB1, RPE65, RPGRIP1, AIPL1, CEP290, LCA5, CRX); ciliopathy retinopathies (Jacobson compared TULP1 with MAK, RPGR, BBS1 and USH2A, finding that TULP1 cones were "less sensitive than expected from the residual structure", PMID:25074776); achromatopsia; congenital stationary night blindness; syndromic ciliopathies (Joubert, Bardet-Biedl, Senior-Løken). Exclude syndromic features. Note the GeneReviews LCA/EOSRD Overview (PMID:30285347) is an Overview-format chapter (statement-of-purpose abstract), and the original LCA chapter is retired (PMID:20301475).
- **Screening:** no newborn screening. Carrier screening and cascade testing in founder populations.

## 11. Outcome / Prognosis

- Life expectancy is normal (non-syndromic). No mortality data.
- Morbidity is severe lifelong visual impairment, often legal blindness by childhood or adolescence. TULP1 acuity outcomes were "similar to that previously reported in patients carrying other truncating TULP1 variants" (PMID:36128853). Visual acuity data across LCA and early-childhood RP genes are in PMID:20079931 (title-level).
- **Prognostic factors:** allele type (truncating vs missense; a missense mouse, D89Y, was mild, PMID:41493298), age, and residual foveal EZ width.
- **Complications:** the PubMed search also returned a TULP1-associated Coats-like exudative vasculopathy series (PMID:33441055, title-level, to verify).

## 12. Treatment

- **No approved disease-specific therapy.** No ClinicalTrials.gov studies match "TULP1" (API query, 2026-11-10: zero results).
- **Gene augmentation (preclinical):** an AAV2/5 vector with the GRK1 promoter in *Tulp1*−/− mice restored protein but gave minimal benefit: "the thickness of the outer nuclear layer (ONL) did not improve in treated Tulp1-/- mice" (PMID:32973439). Possible reasons are very early, rapid degeneration and non-photoreceptor expression (PMID:32655363).
- **Targeting the ER stress response (preclinical concept):** "modulating the UPR pathways might be a strategy for therapeutic intervention" (PMID:26987071). An acetylation switch that controls tubby-like protein stability has been proposed as a pharmacological lever (PMID:33187986, title-level).
- **Supportive care:** low-vision rehabilitation and aids, refractive correction, orientation and mobility training, educational support, and genetic counseling.
- **Suggested NCIT terms (verify):** Genetic Counseling (NCIT:C15240); Rehabilitation (NCIT:C15315); Supportive Care (NCIT:C15747); Gene Therapy (NCIT:C15238) only as a `clinical_trials`- or `discussions`-level experimental note, not as an established treatment.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary prevention:** none beyond reproductive options.
- **Genetic counseling:** recurrence risk is 25% per pregnancy for carrier parents. Options include carrier testing of relatives, prenatal diagnosis and preimplantation genetic testing, and carrier screening in founder or consanguineous communities (Arabian, Pakistani, Finnish).
- **Tertiary prevention:** early visual rehabilitation, and monitoring the foveal island for trial eligibility.

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** none known (no OMIA entry found; not searched exhaustively).
- **Orthologs:** mouse *Tulp1* (MGI; ID to verify); zebrafish paralogs *tulp1a* and *tulp1b* (PMID:36396940). Chicken *tulp1* has been cloned (PMID:11483369, title-level).
- **Conservation:** the C-terminal tubby domain is conserved in plants, invertebrates and vertebrates (PMID:9462750).

## 15. Model Organisms

| Model | Recapitulates | Limitations | PMID |
|---|---|---|---|
| *Tulp1*−/− mouse (tm1Pjn and others) | early-onset rapid rod and cone degeneration, opsin mislocalization, extracellular vesicles, synaptic defects | null allele only; no obesity or deafness (unlike *Tub*), and mouse lacks a macula | 10607826, 10549638, 11481257, 19218615, 26911694 |
| *Tulp1*−/−;*tub*/*tub* double mutant | fulminant degeneration complete by P17 | shows partial redundancy only | 11481257 |
| *Tulp1*^F492L^ knock-in mouse | rapid degeneration, opsin mistrafficking, abnormal ribbons, IRE1 activation | single allele | 41493298 |
| *Tulp1*^D89Y^ knock-in mouse | mild changes only up to 12 months | **does not recapitulate** severe human disease (`FAILS_TO_RECAPITULATE` or `PARTIALLY_RECAPITULATES` candidate) | 41493298 |
| Zebrafish *tulp1a*/*tulp1b* single and double knockouts | dKO: all-photoreceptor opsin mislocalization and very early degeneration, "mimicking the clinical manifestations of TULP1 patients" | ferroptosis and *tekt2* findings not confirmed in mammals | 36396940 |
| Cell models (transfected missense TULP1) | ER retention, PERK/IRE1/CHOP activation | overexpression in vitro | 26987071 |
| Mouse QTL modifier (*Mtap1a*) | modification of degeneration | mouse only | 22323461 |

No human iPSC-derived retinal organoid model of TULP1 was found in this search (it is not proven absent; the search was a title search).

---

## Curation notes for the draft entry

1. The draft `genetic:` row uses `association: Causal`. Per the schema it should be `relationship_type: CAUSATIVE`, with a `gene_disease_validity` block copying the ClinGen Definitive AR assertion above. Quote the CGGV row as evidence after running `just fetch-reference CGGV:assertion_ecc6101d-…`.
2. Promising subtypes or stratification: none needed. LCA vs EORD is a spectrum rather than separate MONDO subtypes. Put the founder alleles under `variants` and `population_effects`, and only where a source states a population-specific difference. PMID:25342276 states a recognisable phenotype for the founder; it does not compare it with other populations.
3. Phenotype-to-mechanism edges should run from photoreceptor degeneration to the ERG, nystagmus, acuity and field phenotypes, so the phenotypes are not left disconnected in the causal graph.
4. Mechanisms supported only by animal models (synapse, ferroptosis) need `evidence_source: MODEL_ORGANISM`. Consider a `HUMAN_MODEL_MISMATCH` discussion for the D89Y mouse, and for the minimal benefit of gene therapy in mice despite protein restoration.
5. Still to do: look up every suggested CURIE, fetch the reference cache for each cited PMID, and run `just count-verified-snippets` on the quotes above. Nothing here has been committed.

Checked during the run: the PMIDs, abstract quotes, ClinGen row, and the empty trials search. The ontology CURIEs, the Orphanet/ICD codes, and the overall LCA prevalence figure are not yet written. Check those before they go into the YAML.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| Quoted claims checked | 32 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 9 |
| References weighed for topical relevance | 36 |
| On topic | 30 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:36128853` (8 mentions) - Identifier did not resolve to a record
- `PMID:25074776` (6 mentions) - Identifier did not resolve to a record
- `PMID:9462750` (3 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25342276` *(abstract only)*: "All 10 children … had nystagmus since soon after birth"
  - closest text in source: "RESULTS: All 10 children (2-8 years old; mean 5.2, median 6) had nystagmus since soon after birth, a grossly normal posterior pole other than arteriolar attenuation, peripheral mottling with apparent evolution to bone spicules, and hyperopia"
- `PMID:31087526` *(abstract only)*: "associated with infantile and early childhood onset IRD"
  - Text part not found as substring: 'associated with infantile and early childhood onset IRD' (note: only abstract available for PMID:31087526, full text may contain this excerpt)
- `PMID:41493298` *(abstract only)*: "activation of the IRE1 branch … in Tulp1-/- and Tulp1F492L retinas"
  - closest text in source: "Moreover, building on our prior in vitro results, we observed activation of the IRE1 branch of the endoplasmic reticulum (ER)-unfolded protein response (UPR) complex in Tulp1-/- and Tulp1F492L retinas, identifying ER stress as a key disease mechanism leading to photoreceptor death and as a potential therapeutic target in TULP1-associated forms of IRD."

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:25074776`: "No evidence of rod function was present at any age"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "Retinal ophthalmoscopy was primarily normal converting to peripheral pigmentary retinopathy and maculopathy"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "progressive extra-foveal loss of the ellipsoid zone (EZ), the outer plexiform layer (OPL), and the outer nuclear layer (ONL)"
  - Reference did not resolve, so the quote could not be checked
- `PMID:9462750`: "Three of the mutations are missense changes affecting the conserved C-terminal region; the fourth mutation affects a splice donor site"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "associated with infantile and early childhood onset IRD"
  - Reference did not resolve, so the quote could not be checked
- `PMID:25074776`: "The TULP1-RD patients were severely affected already in the first decade of life and there was rapidly progressive visual loss"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "suggesting a potential time window for therapeutic interventions"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "The width of the foveal EZ and the thickness of the foveal OPL-ONL layers could serve as biomarkers of the disease stage"
  - Reference did not resolve, so the quote could not be checked
- `PMID:36128853`: "similar to that previously reported in patients carrying other truncating TULP1 variants"
  - Reference did not resolve, so the quote could not be checked

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 9 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007754` (1 mention) - the report calls it "Bull's eye maculopathy"; HP calls it **Macular dystrophy**
- `HP:0007843` (1 mention) - the report calls it "Retinal arteriolar attenuation"; HP calls it **Attenuation of retinal blood vessels**
- `CL:0000604` (1 mention) - the report calls it "CL:** rod photoreceptor cell"; CL calls it **retinal rod cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000550` (1 mention) - the report calls it "Undetectable ERG (rod and cone)"; HP calls it **Undetectable electroretinogram**, and lists "Undetectable ERG" among its other names
- `HP:0000662` (1 mention) - the report calls it "Nyctalopia / hemeralopia"; HP calls it **Nyctalopia**
- `HP:0001133` (1 mention) - the report calls it "Constricted visual field / peripheral islands"; HP calls it **Constriction of peripheral visual field**, and lists "Constricted visual fields" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.