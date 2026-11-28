---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T23:09:54.284876'
end_time: '2026-11-27T23:13:06.628883'
duration_seconds: 192.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pleural Tuberculosis
  mondo_id: MONDO:0005922
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: pleura tuberculosis; tuberculosis of pleura; tuberculous pleurisy; tuberculous
    pleuritis
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
  web_search_requests: 22
  num_turns: 29
  total_cost_usd: 1.2062636999999998
  session_id: 5cbc6947-ed9d-4c22-a876-fc8343a39100
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 28
  retrieval_calls: 23
  assistant_text_blocks: 2
citation_count: 49
reference_validation:
  total_references: 36
  verified: 35
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.028
  quotes_checked: 10
  quotes_valid: 5
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMID:26150911
  - PMC:PMC4466424
  - PMID:9484963
  - PMID:17426219
  relevance_assessed: 35
  on_topic: 25
  unresolved_references:
  - DOI:10.1164/artpd.1955.71.5.616
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 38
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0005922
    reported_labels:
    - MONDO
    ontology_label: pleural tuberculosis
  - term_id: HP:0031291
    reported_labels:
    - pleural thickening, suggested
    ontology_label: Ichthyosis follicularis
  labels_variant: 4
  service_unreachable: 11
  obsolescence_unchecked: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pleural Tuberculosis
- **MONDO ID:** MONDO:0005922 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** pleura tuberculosis; tuberculosis of pleura; tuberculous pleurisy; tuberculous pleuritis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pleural Tuberculosis** covering all of the
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

I'm searching the literature on pleural tuberculosis. Bash can't call PubMed here, so I'm using web search instead.

# Pleural Tuberculosis (MONDO:0005922): Research Report for a Disease Knowledge Base

**How this was researched and what is missing.** Every source here was found with web search, because direct PubMed E-utilities calls were blocked in this run. I give a PMID only where one appeared in a retrieved result. Otherwise I cite a PMC ID or URL. Several template sections were not supported by anything I retrieved (pharmacogenomics, epigenetic GO detail, quality-of-life instruments, OMIA, and others), and they are marked as such. Ontology term IDs (HPO, GO, CL, UBERON, NCIT, CHEBI) are my suggestions and were not checked against the ontology browsers in this session; please check them before loading.

**Interpretation of the target.** Pleural tuberculosis (MONDO:0005922) is an infectious disease. **It has no causal human gene.** The causal agent is *Mycobacterium tuberculosis* complex. The "Causal gene(s): not recorded" field is therefore correct. Host-genetic findings below are susceptibility associations only.

---

## 1. Disease Information

**Overview.** Pleural TB is a form of extrapulmonary TB. *M. tuberculosis* infects the pleural space and causes a usually unilateral, lymphocyte-predominant, exudative pleural effusion.
- The older idea was that the effusion was purely a delayed-type hypersensitivity reaction. That view "has given way to the idea that it stems from direct infection of the pleural space" (Vorster et al. 2015, PMID 26150911; https://pmc.ncbi.nlm.nih.gov/articles/PMC4466424).
- The gold-standard diagnosis still depends on detecting *M. tuberculosis* in pleural fluid or a pleural biopsy (PMID 26150911).
- Because the effusion is paucibacillary, diagnosis is hard, and pleural biopsy is needed when fluid studies are indeterminate (PMID 34536698, Respir Med 2021).

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0005922 | provided |
| MeSH | D014396 "Tuberculosis, Pleural"; entry term "Pleurisy, Tuberculous" | https://meshb.nlm.nih.gov/record/ui?ui=D014396 |
| ICD-10-CM | A15.6 Tuberculous pleurisy (includes tuberculosis of pleura and tuberculous empyema; excludes primary respiratory TB A15.7) | https://www.aapc.com/codes/icd-10-codes/A15.6 |
| ICD-10-GM | A15.6 "confirmed bacteriologically, molecularly or histologically" | https://gesund.bund.de/en/icd-code-suche/a15-6 |
| ICD-11 | A third-party crosswalk maps A15.6 to 1B10.0 (respiratory TB, confirmed). **Not verified** in the WHO browser | autoicdapi.com |
| OMIM / Orphanet | None. Not a Mendelian or rare-disease entry | — |

**Synonyms.** Tuberculous pleurisy; tuberculous pleuritis; tuberculosis of pleura; pleura tuberculosis; tuberculous pleural effusion (TPE); tuberculous empyema (a distinct, more advanced form).

**Data provenance.** The information is aggregated at the disease level, from cohort studies, surveillance data and meta-analyses. None of it comes from individual patient records.

---

## 2. Etiology

**Causal factor (infectious).** The cause is *Mycobacterium tuberculosis* (NCBITaxon:1773), or less commonly another member of the MTB complex such as *M. bovis* (NCBITaxon:1765).

**Two disease forms**
- **Primary pleurisy.** This follows recent primary infection, often in young people in high-burden settings.
- **Reactivation pleurisy.** This occurs in older adults in low-burden settings.
- **HIV changes the picture.** In sub-Saharan Africa, TB pleurisy "ha[s] become associated with older age, a chronic onset, and an increased mycobacterial load" (Zimbabwe cohort, PMID 9484963).

**Risk factors**
- **HIV co-infection.**
  - In Uganda, 80% of 142 adults with TB pleurisy were HIV-positive, and they had more severe and longer illness (PMID 11495266).
  - In Harare, 85% of 90 patients were HIV-positive, and a CD4 count below 200 was linked to a positive pleural smear (37% vs 0%) (PMID 9484963).
- **Age and sex.**
  - In US surveillance for 1993–2003, pleural TB was more frequent than pulmonary TB among people aged 65 or older (30.4% vs 23.3%) (PMID 17426219).
  - The male-to-female ratio is about 2:1 (https://pmc.ncbi.nlm.nih.gov/articles/PMC4958858).
- **TB exposure.** Contact with a TB case is a key clue in children (Brazilian pediatric series, https://scielo.br/j/jped/a/9cQPGk7GL4pz4M3WFPZ3Trs/).
- **Host genetics (susceptibility only, weak evidence).**
  - One Taiwanese study hypothesized that TLR2 polymorphisms predispose pulmonary-TB patients to pleural involvement (https://pmc.ncbi.nlm.nih.gov/articles/PMC2824655).
  - IL10 promoter variants (−1082G/A in Caucasians, −592C/A in Asians) are associated with TB generally, not specifically with pleurisy (meta-analysis in the same search results).
  - **No pleurisy-specific GWAS or ClinVar entries were found.**

**Protective factors.** Nothing pleurisy-specific was retrieved. General TB control measures (BCG vaccination, treating latent infection, HIV antiretroviral therapy) are plausible protective factors, but I did not retrieve pleural-specific evidence for them.

**Gene–environment interaction.** No data were retrieved. The interaction of host immune genotype with HIV status is a plausible but unstudied area.

---

## 3. Phenotypes

| Phenotype | Suggested HPO | Frequency / details | Source |
|---|---|---|---|
| Pleural effusion, unilateral | HP:0002202 | ~96% unilateral in children | scielo.br pediatric series |
| Fever | HP:0001945 | 88% (children); typically acute illness with fever | scielo.br; PMC4958858 |
| Cough | HP:0012735 | 72% (children) | scielo.br |
| Pleuritic chest pain | HP:0033771 (pleuritic chest pain) / HP:0100749 (chest pain) | 70% (children) | scielo.br |
| Weight loss | HP:0001824 | More frequent in HIV+ patients | PMC4958858 |
| Lymphocytic pleural exudate (lab) | HP:0002202 + lab annotation | 90% (children); 100% of HIV− and 97% of HIV+ adults (Uganda) | scielo.br; PMID 11495266 |
| Elevated pleural ADA (lab) | no specific HPO; LOINC pleural ADA | >40 U/L in 85% of children | scielo.br |
| Pleural loculation | — | 27 of 154 children (17.5%); risk factors male sex, empyema, monocyte count | https://pmc.ncbi.nlm.nih.gov/articles/PMC8716631 |
| Residual pleural thickening (sequela) | HP:0031291 (pleural thickening, suggested) | 47–81% (RPT >2 mm), ~20–32% with RPT ≥10 mm | koreamed; PMC3051910 |
| Coexisting pulmonary TB | — | 57.8% of children | PMC8716631 |

- **Onset and course.** Onset is usually acute or subacute (PMC4958858). It is more chronic in HIV-associated disease (PMID 9484963).
- **Severity.** Illness is more severe and longer in HIV+ patients (PMID 11495266).
- **Quality of life.** No EQ-5D or SF-36 data were retrieved. The Cochrane review found percent-predicted FVC similar with and without steroids (very low certainty) (PMID 28290161).

---

## 4. Genetic / Molecular Information

- **Causal genes:** none. The disease is infectious.
- **Pathogenic variants, ClinVar/ACMG classification, allele frequencies, somatic findings and chromosomal abnormalities:** not applicable.
- **Modifier or susceptibility genes:** only weak candidate evidence exists (TLR2, IL10; see §2).
- **Pathogen genetics:** isoniazid resistance was less frequent in pleural than pulmonary isolates (6.0% vs 7.8%) (PMID 17426219).
- **Epigenetics (model organism).** A 2025 MedComm study profiled DNA methylation and transcriptomes of pleural macrophages and CD4⁺ T cells at days 0–14 in an intrapleural-BCG mouse model (https://pmc.ncbi.nlm.nih.gov/articles/PMC11959155; the PubMed result 40170749 appeared alongside it, but I did not confirm that this PMID is the same paper).

---

## 5. Environmental Information

- **Infectious agent:** *M. tuberculosis* (NCBITaxon:1773), transmitted by airborne droplet nuclei. *M. bovis* (NCBITaxon:1765) is the zoonotic route.
- **Co-infection:** HIV (NCBITaxon:12721) is the dominant environmental modifier (PMIDs 11495266, 9484963).
- **Toxins and lifestyle:** no pleurisy-specific data were retrieved.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Primary infection or reactivation.** Inhaled *M. tuberculosis* is taken up by alveolar macrophages and forms a subpleural focus. This **leads to** a caseous subpleural lesion that ruptures into the pleural space, or to haematogenous or lymphatic seeding. Rupture is the classical model; direct infection of the pleura is now favoured (PMID 26150911).
2. **Mycobacterial antigens enter the pleural space.** This **results in** antigen uptake by pleural macrophages and mesothelial cells, and production of chemokines and cytokines. Mesothelial cells present antigen and promote Th9 differentiation, and anaphylatoxins drive cytokine secretion by mesothelial cells and CD16⁺ monocytes (https://pmc.ncbi.nlm.nih.gov/articles/PMC8291687; in vitro and human samples).
3. **Recruitment of effector T cells.** Chemokines **lead to** compartmentalised accumulation of CD4⁺ Th1 and Th17 cells in the pleura. In single-cell RNA sequencing, CD4 T cells were about 43% of pleural mononuclear cells and "favored a Th1 and Th17 response" (Yang et al. 2023, PMID 37435066). Parietal pleura shows more CD3, CD4, CCR4 and Th17 cells than nonspecific pleuritis (https://doi.org/10.1371/journal.pone.0031710).
4. **Delayed-type hypersensitivity / Th1 effector response.** IFN-γ, TNF and IL-27 release **leads to** macrophage activation, raised ADA (from lymphocyte and monocyte activation, an inferred link) and raised pleural IFN-γ. This is the basis of the diagnostic biomarkers (§10).
5. **Inflammation increases pleural capillary permeability and blocks lymphatic drainage.** This **results in** a protein-rich exudative effusion, which is the clinical manifestation. The mechanism is classically described and is inferred here; no primary experiment was retrieved.
6. **Granuloma formation.** TNF/TNFR signalling **leads to** containment. In mice lacking TNF or TNFR1/2, BCG pleurisy was "uncontrolled and progressive" and caused disseminated, fatal infection (Chavez-Galan et al. 2016, PMID 27456129; mouse).
7. **Branch A, resolution.** Most effusions resolve with treatment, or even spontaneously.
   **Branch B, fibrosis.** Fibrin deposition, with higher pleural LDH, lysozyme, TNF-α and IFN-γ and lower glucose and pH, **leads to** residual pleural thickening (koreamed; PMC3051910; associations only).
   **Branch C, failed containment.** This **leads to** tuberculous empyema or later pulmonary or extrapulmonary TB.
8. **Immune regulation and exhaustion.** Effector Tregs are expanded via mesothelial adhesion molecules (https://pmc.ncbi.nlm.nih.gov/articles/PMC3777994), NK cells become exhausted, and TNF/XAF1 pathways drive T-cell apoptosis (PMID 37435066). These are likely modulators of bacillary persistence (inferred).

### Supporting detail

- **Molecular pathways.** TNF/TNFR1/TNFR2 signalling (mouse, PMID 27456129; transmembrane TNF regulates MDSCs via TNFR2, https://pmc.ncbi.nlm.nih.gov/articles/PMC5574880), IFN-γ signalling, the IL-17 axis, and complement anaphylatoxins C3a/C5a (PMC8291687).
- **Suggested GO terms.**
  - GO:0002250 adaptive immune response
  - GO:0032609 type II interferon production
  - GO:0032620 interleukin-17 production
  - GO:0002544 chronic inflammatory response
  - GO:0002432 granuloma formation
  - GO:0033209 tumor necrosis factor-mediated signaling pathway
  - GO:0006954 inflammatory response
- **Suggested CL terms.**
  - CL:0000624 CD4⁺ αβ T cell
  - CL:0000899 Th17 cell
  - CL:0000545 Th1 cell
  - CL:0000623 NK cell
  - CL:0000077 mesothelial cell
  - CL:0000235 macrophage
  - CL:0000815 regulatory T cell
  - CL:0000940 MAIT cell
- **Molecular profiling.** In single-cell RNA sequencing of 6 TPE and 4 control effusions, myeloid cells showed stronger phagocytosis, antigen presentation and IFN-γ response, and macrophages were the main source of pro-inflammatory cytokines (PMID 37435066). A separate study with TCR sequencing showed functional diversity of T cells in TPE (cited in the same results).
- **Not retrieved:** proteomics, metabolomics, lipidomics, spatial transcriptomics and CRISPR screen data.

---

## 7. Anatomical Structures Affected

- **Primary:** pleura (UBERON:0000977), specifically the parietal pleura (UBERON:0002400), visceral pleura (UBERON:0002401) and pleural cavity (UBERON:0002402).
- **Secondary:** lung (UBERON:0002048; coexisting pulmonary TB in 57.8% of children, PMC8716631) and mediastinal lymph nodes (~22% in an Iranian paediatric series).
- **Body system:** respiratory.
- **Cells:** see the CL terms in §6.
- **Subcellular:** phagosome (GO:0045335), where *M. tuberculosis* persists. This is general TB biology, not pleurisy-specific.
- **Lateralization:** usually unilateral (96% in children; 100% in the Iranian series).

---

## 8. Temporal Development

- **Onset:** acute or subacute in most patients; chronic in HIV-associated disease in Africa (PMID 9484963).
- **Age:** occurs from childhood (mean age 10.9 years in the Brazilian paediatric series) to old age (in the US, over-represented at age 65 or older, PMID 17426219).
- **Natural history:** effusions may resolve spontaneously, but later active TB is common if untreated. Roper & Waring (Am Rev Tuberc 1955; DOI 10.1164/artpd.1955.71.5.616) is the classic source. **I could not retrieve the frequently quoted ~65% figure, so it is unverified.**
- **Treated course:**
  - About 47% of patients had residual pleural thickening after 6 months of chemotherapy (Korean 1999 study).
  - About 53% had slow but complete resorption (Korean 2001 study).
  - No relapse occurred over a mean 41 months among 115 patients treated with isoniazid plus rifampicin for 6 months (https://pmc.ncbi.nlm.nih.gov/articles/PMC1021356; Thorax 1994).
- **Critical window:** early drainage and treatment may limit loculation and thickening, but the evidence is inconclusive (koreamed).

---

## 9. Inheritance and Population

- **Inheritance:** not applicable. The disease is infectious, and host susceptibility is multifactorial.
- **US epidemiology:**
  - 1993–2003: 7,549 pleural cases; the annual share of all TB was stable at a median of 3.6% (range 3.3–4.0%) (PMID 17426219).
  - 2024: pleural disease was 24% of extrapulmonary TB, second after lymphatic disease at 28% (CDC, https://www.cdc.gov/tb-surveillance-report-2024/data/site-of-disease.html).
- **Global:** the share of patients with TPE who are HIV-positive varies widely, from about 85% (Zimbabwe) to about 10% (Spain) (PMC4958858). No GBD-specific incidence for the pleural form was retrieved.
- **Sex ratio:** about 2:1 male to female (PMC4958858).
- **Founder effects, penetrance and carrier frequency:** not applicable.

---

## 10. Diagnostics

**Pleural fluid biomarkers**

| Test | Performance | Source |
|---|---|---|
| ADA (63 studies) | Sensitivity 0.92 (0.90–0.93), specificity 0.90 (0.89–0.91), DOR ≈110 | PMID 18222681 |
| ADA (174 studies, 2019) | At 40±4 IU/L: sensitivity 0.93, specificity 0.90; all included studies at high risk of bias | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6435228/ |
| ADA (12 studies) | Best performance at ≥50 U/L | PMID 25419343 |
| ADA2 isoenzyme | Sensitivity 0.91, specificity 0.93 | 2022 meta-analysis (PMC8224977 in the search results) |
| Unstimulated IFN-γ | Sensitivity 0.93, specificity 0.96; better than ADA, especially for specificity | comparative meta-analysis (search results) |
| IL-27 | Sensitivity 92.7%, specificity 99.1% (single centre, 68 TPE patients) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3392223 |

A practical rule from the reviews is "ADA >40 U/L in a lymphocytic effusion" in high-prevalence settings (PMID 27499981). No single pleural-fluid test is accurate enough alone (PMID 31246102).

**Microbiology**
- Pleural fluid culture yield is 63% with liquid media, and sputum culture yield is 48%. Combined, they reach 79% (382-patient study, search results).
- Induced sputum is culture-positive in 52% of patients even without parenchymal disease (Conde et al. 2003, as cited in PMC4958858).
- Liquid culture outperforms solid culture (PMID 11495266).

**Molecular tests**
- Xpert MTB/RIF has pooled sensitivity of 30% and specificity of 99% (Huo & Peng, in the search results). Against a composite reference it detects 22.7% of patients, and against culture 51.4% (Sehgal; https://pmc.ncbi.nlm.nih.gov/articles/PMC6019837).
- Xpert Ultra has sensitivity of 52% and specificity of 98% against a composite reference (Medicine 2022). Head to head, it is more sensitive than Xpert (PLoS ONE 2022, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9273090/).
- Xpert and Ultra are useful to rule in TB, but not to rule it out.

**Biopsy**
- Closed needle biopsy has sensitivity of 66% for histology, 48% for culture and 79% combined. Thoracoscopy reaches 100%, 76% and 100% (ERJ 2003, https://publications.ersnet.org/content/erj/22/4/589).
- In a 2018 randomized trial, ultrasound-guided biopsy had 82% sensitivity versus 90% for thoracoscopy (p=0.30) (https://pmc.ncbi.nlm.nih.gov/articles/PMC6192452).
- The typical histological finding is caseating granuloma.

**Clinical criteria and differential diagnosis**
- A working definition is a lymphocytic exudate with ADA ≥35 U/L after other causes are excluded (Porcel group, Arch Bronconeumol 2019).
- The differential diagnosis includes malignant effusion (low ADA, cytology positive), lymphoma (which can also raise ADA), parapneumonic effusion/empyema (neutrophilic), and rheumatoid effusion.

**Genetic testing:** not applicable to the host. Pathogen drug-resistance testing (rpoB with Xpert) applies.

**Screening:** none specific beyond TB contact tracing and IGRA or tuberculin skin testing.

---

## 11. Outcome / Prognosis

- **Mortality:** no disease-specific mortality data were retrieved. HIV-associated disease is more severe (PMID 11495266).
- **Recovery:** treatment is highly effective. There were no relapses in 115 patients at about 41 months (PMC1021356).
- **Complications:**
  - Residual pleural thickening in 47–81%, with ≥10 mm in about 20–32% (koreamed; PMC3051910)
  - Loculation (17.5% in children)
  - Empyema
  - Later pulmonary TB if untreated (historical data; figure unverified)
- **Prognostic factors for residual thickening:** positive AFB and granuloma on biopsy, higher LDH, IFN-γ, TNF-α and lysozyme, and lower glucose and pH. The findings are inconsistent across studies (koreamed; PMC3051910).

---

## 12. Treatment

**Antituberculous therapy**
- Standard regimen: 6 months of isoniazid, rifampicin, pyrazinamide and ethambutol (2HRZE/4HR). Suggested NCIT and ChEBI codes:

| Drug | NCIT | ChEBI |
|---|---|---|
| Isoniazid | C574 | CHEBI:6030 |
| Rifampicin | C800 | CHEBI:28077 |
| Pyrazinamide | C788 | CHEBI:45285 |
| Ethambutol | C470 | CHEBI:4877 |

- Older evidence shows isoniazid plus rifampicin for 6 months is effective (PMC1021356). Isoniazid plus rifampicin was as effective as adding pyrazinamide, with fewer adverse effects (2019 report via TB Online).
- Current guidelines add ethambutol because of isoniazid resistance (NCT01560078 background).

**Corticosteroids (adjunctive prednisolone)**
- In the Cochrane review (6 trials, 590 participants), residual effusion was lower with steroids:
  - At 8 weeks: RR 0.54 (0.37–0.78)
  - At 24 weeks: RR 0.35 (0.18–0.66)
- The evidence was low certainty, there was no clear long-term lung-function benefit, and steroids caused more adverse events leading to discontinuation.
- Kaposi's sarcoma occurred in 6/99 steroid recipients versus 0/98 controls in the HIV-positive trial.
- The authors note the evidence raises "doubt as to whether such treatment is worthwhile" (PMID 28290161). They are not routinely recommended.

**Procedures**
- Therapeutic thoracentesis or pigtail drainage relieves symptoms. Its effect on residual thickening is inconclusive (koreamed).
- Decortication is used for symptomatic fibrothorax or empyema.
- Intrapleural fibrinolytics: no trial data were retrieved.

**Gaps**
- **Pharmacogenomics:** not retrieved. NAT2 acetylator status is a general isoniazid issue and was not verified here.
- **Experimental:** NCT01560078 (AIIMS, thrice-weekly DOTS; outcome is ultrasound resolution at 6 months). It is listed as completed, but no results were found.
- **Gene, cell and RNA therapies:** not applicable.

---

## 13. Prevention

- **Primary:**
  - BCG vaccination
  - Infection control and contact tracing
  - Treatment of latent TB infection
  - Antiretroviral therapy for HIV (inferred from the HIV association; not retrieved as pleural-specific evidence)
- **Secondary:** early diagnosis with ADA and culture, and sputum culture even when no infiltrate is present (PMC4958858).
- **Tertiary:** a full course of therapy to prevent later pulmonary TB, and drainage to limit loculation and fibrothorax.
- **Genetic counselling:** not applicable.

---

## 14. Other Species

- **Cattle:** *M. bovis* causes bovine TB, which involves the pleura. Typical lesions were found in the pleura of slaughtered cattle and buffalo in an Egyptian abattoir study (https://jcvr.journals.ekb.eg/article_462651_749f23b959eb595ad910fdb58a301894.pdf). The respiratory tract had the highest lesion frequency in a Brazilian series.
- **Zoonotic potential:** *M. bovis* can be transmitted to humans.
- **Not retrieved:** OMIA or VBO breed data.

---

## 15. Model Organisms

| Model | Method | Recapitulation | Source |
|---|---|---|---|
| Guinea pig (*Cavia porcellus*, NCBITaxon:10141) | Intrapleural BCG, or heat-killed virulent *M. tuberculosis*, in BCG-sensitized animals | "Experimental tuberculous pleuritis with effusion, closely resembling the human disease" | https://pmc.ncbi.nlm.nih.gov/articles/PMC166002 |
| Mouse (NCBITaxon:10090), wild type and knockouts | Intrapleural BCG | Pleural lesions and cellular influx (peaks at day 1 and day 15); strain-dependent eosinophil recruitment | Inflamm Res 2000 (https://link.springer.com/doi/10.1007/s000110050581) |
| Mouse *Tnf*−/−, *Tnfr1/2*−/−, *Ccr5*−/− | Intrapleural BCG | TNF/TNFR deficiency gives progressive, fatal disseminated infection; CCR5 is dispensable | PMID 27456129 |
| Mouse transmembrane-TNF knock-in | Intrapleural BCG | tmTNF controls MDSCs via TNFR2 | PMC5574880; PMC6073837 |
| Mouse (2025) | Intrapleural BCG | Methylome and transcriptome of pleural macrophages and CD4⁺ T cells | PMC11959155 |

**Limitations**
- BCG is attenuated, and a mouse model using intrapleural virulent *M. tuberculosis* was not found.
- The guinea pig model needs prior sensitization.
- No model recapitulates HIV co-infection or reactivation disease.

---

## Key Evidence Quotes

- "the view that the effusion was purely a delayed hypersensitivity reaction has given way to the idea that it stems from direct infection of the pleural space" (PMID 26150911)
- "the CD4 lymphocyte population in TPE favored a Th1 and Th17 response" (PMID 37435066)
- "BCG-induced pleural infection was uncontrolled and progressive in absence of TNF or TNF receptor 1 (TNFR1)/TNFR2" (PMID 27456129)
- "From 1993 through 2003, 7,549 cases of pleural TB … the annual proportion of pleural TB was relatively stable (median rate, 3.6%)" (PMID 17426219)
- "research findings are inconsistent and raise doubt as to whether such treatment is worthwhile" (PMID 28290161)

---

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC4466424 (PMID 26150911)
- https://pubmed.ncbi.nlm.nih.gov/34536698/
- https://jtd.amegroups.org/article/view/4221 (PMID 27499981)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4958858
- https://pubmed.ncbi.nlm.nih.gov/9363161/
- https://www.pubmed.gov/18222681/
- https://pubmed.ncbi.nlm.nih.gov/25419343
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6435228/
- https://pubmed.ncbi.nlm.nih.gov/28290161/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6019837/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9273090/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9276415/
- https://pubmed.ncbi.nlm.nih.gov/17426219/
- https://www.cdc.gov/tb-surveillance-report-2024/data/site-of-disease.html
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3392223
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310016/
- https://www.pubmed.gov/37435066/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8291687/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3777994/
- https://dx.doi.org/10.1371/journal.pone.0031710
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2824655
- https://pubmed.ncbi.nlm.nih.gov/11495266/
- https://pubmed.ncbi.nlm.nih.gov/9484963/
- https://meshb.nlm.nih.gov/record/ui?ui=D014396
- https://www.aapc.com/codes/icd-10-codes/A15.6
- https://gesund.bund.de/en/icd-code-suche/a15-6
- https://publications.ersnet.org/content/erj/22/4/589
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6192452
- https://synapse.koreamed.org/articles/1061968
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3051910/table/T3
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1021356
- https://clinicaltrials.gov/study/NCT01560078
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8716631/
- https://scielo.br/j/jped/a/9cQPGk7GL4pz4M3WFPZ3Trs/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC166002
- https://link.springer.com/doi/10.1007/s000110050581
- https://searchworks.jioinstitute.edu.in/articles/cmedm__27456129
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5574880/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073837/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11959155/
- https://jcvr.journals.ekb.eg/article_462651_749f23b959eb595ad910fdb58a301894.pdf
- https://www.qxmd.com/r/14361976 (Roper & Waring 1955)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 35 |
| On topic | 25 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1164/artpd.1955.71.5.616` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26150911` *(abstract only)*: "has given way to the idea that it stems from direct infection of the pleural space"
  - closest text in source: "Our understanding of the pathogenesis of the disease has evolved and what was once thought to be an effusion as a result of a pure delayed hypersensitivity reaction is now believed to be the consequence of direct infection of the pleural space with a cascade of events including an immunological response"
- `PMC:PMC4466424` *(abstract only)*: "has given way to the idea that it stems from direct infection of the pleural space"
  - closest text in source: "Our understanding of the pathogenesis of the disease has evolved and what was once thought to be an effusion as a result of a pure delayed hypersensitivity reaction is now believed to be the consequence of direct infection of the pleural space with a cascade of events including an immunological response"
- `PMID:9484963` *(abstract only)*: "ha[s] become associated with older age, a chronic onset, and an increased mycobacterial load"
  - closest text in source: "CONCLUSION: In sub-Saharan Africa, TB pleural effusions have become associated with older age, a chronic onset, and an increased mycobacterial load"
- `PMID:26150911` *(abstract only)*: "the view that the effusion was purely a delayed hypersensitivity reaction has given way to the idea that it stems from direct infection of the pleural space"
  - closest text in source: "Our understanding of the pathogenesis of the disease has evolved and what was once thought to be an effusion as a result of a pure delayed hypersensitivity reaction is now believed to be the consequence of direct infection of the pleural space with a cascade of events including an immunological response"
- `PMID:17426219` *(abstract only)*: "From 1993 through 2003, 7,549 cases of pleural TB … the annual proportion of pleural TB was relatively stable (median rate, 3.6%)"
  - closest text in source: "The annual proportion of pleural TB was relatively stable (median rate, 3.6%; range, 3.3 to 4.0%) compared to that for pulmonary TB, which steadily decreased (average annual decrease, 0.9%; p < 0.01)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005922` (3 mentions) - the report calls it "MONDO"; MONDO calls it **pleural tuberculosis**
- `HP:0031291` (1 mention) - the report calls it "pleural thickening, suggested"; HP calls it **Ichthyosis follicularis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1765` (2 mentions) - the report calls it "M. bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `HP:0002202` (2 mentions) - the report calls it "Pleural effusion, unilateral"; HP calls it **Pleural effusion**
- `UBERON:0000977` (1 mention) - the report calls it "Primary:** pleura"; UBERON calls it **pleura**
- `GO:0045335` (1 mention) - the report calls it "Subcellular:** phagosome"; GO calls it **phagocytic vesicle**, and lists "phagosome" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:1773` - called "Mycobacterium tuberculosis", "M. tuberculosis"

### Terms the ontology service could not be reached for

11 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `NCBITaxon:1773` (2 mentions)
- `HP:0001945` (1 mention)
- `HP:0012735` (1 mention)
- `HP:0100749` (1 mention)
- `NCBITaxon:12721` (1 mention)
- `GO:0002250` (1 mention)
- `GO:0002544` (1 mention)
- `CL:0000899` (1 mention)
- `CL:0000545` (1 mention)
- `CL:0000623` (1 mention)
- `UBERON:0002401` (1 mention)

### Terms whose obsolescence could not be checked

7 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `NCBITaxon:1765` (2 mentions)
- `GO:0032620` (1 mention)
- `GO:0006954` (1 mention)
- `CL:0000077` (1 mention)
- `CL:0000815` (1 mention)
- `CL:0000940` (1 mention)
- `GO:0045335` (1 mention)