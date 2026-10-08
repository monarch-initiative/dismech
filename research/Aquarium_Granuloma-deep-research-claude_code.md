---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-28T04:40:04.089705'
end_time: '2026-09-28T04:59:26.482187'
duration_seconds: 1162.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Aquarium Granuloma
  mondo_id: MONDO:0043314
  category: Infectious Disease
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 9
  num_turns: 46
  total_cost_usd: 9.298952000000002
  session_id: a5a85834-223d-49be-89a2-9de78f1e1b4a
  stop_reason: end_turn
  assistant_text_blocks: 7
citation_count: 34
reference_validation:
  total_references: 55
  verified: 55
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 55
  on_topic: 40
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 94
  verified: 94
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 24
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0043314
    reported_labels:
    - MONDO
    ontology_label: aquarium granuloma
  - term_id: NCBITaxon:1781
    reported_labels:
    - NCBI Taxonomy (agent)
    - M. marinum
    - Mycobacterium marinum
    ontology_label: Mycobacterium marinum
  - term_id: UBERON:0001473
    reported_labels:
    - Egress of infected macrophages into dermal lymphatics
    - lymphatic vessel
    ontology_label: lymphatic vessel
  - term_id: NCIT:C15986
    reported_labels:
    - Clarithromycin
    - Rifampicin
    - Rifabutin
    - Ethambutol
    - Doxycycline
    - Minocycline
    - Trimethoprim-sulfamethoxazole
    - Moxifloxacin
    - Linezolid
    - Amikacin
    - Azithromycin
    ontology_label: Pharmacotherapy
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aquarium Granuloma
- **MONDO ID:** MONDO:0043314 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Aquarium Granuloma** covering all of the
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

I'll research aquarium granuloma (Mycobacterium marinum infection) across the requested sections and write the report inline. First I'll load the web tools.

I'll run the independent searches in parallel now.

Now fetching the key primary sources for exact quotes and PMIDs.

Verifying identifiers against PubMed directly.

Network works via curl. I'll pull abstracts directly from PubMed for the core reference set.

Now verifying every ontology term I plan to suggest against OLS, rather than writing CURIEs from memory.

# Research Report: Aquarium Granuloma (*Mycobacterium marinum* cutaneous infection)

**MONDO:** MONDO:0043314 · **Category:** Infectious disease · **Report date:** 2026-09-28

**Evidence-provenance convention used throughout.** Quotes marked **[A]** were retrieved verbatim from the PubMed abstract via NCBI E-utilities in this session and are safe to use as dismech `snippet:` values after `just fetch-reference`. Quotes marked **[F]** come from article full text or a search-engine snippet of full text; they are leads and must be re-verified against `references_cache/` before use. Every ontology CURIE below was resolved against EBI OLS4 or NCBI in this session; none was written from memory.

---

## 1. Disease Information

### Overview

Aquarium granuloma is a localized, chronic, granulomatous skin and soft-tissue infection caused by *Mycobacterium marinum*, a slow-growing, photochromogenic nontuberculous mycobacterium (NTM) of fresh and salt water. It is an inoculation infection: the organism enters through a pre-existing break in the skin during contact with aquarium water, fish, shellfish, or non-chlorinated pools. Because *M. marinum* grows optimally near 30 °C and poorly at core body temperature, disease is confined almost entirely to the cool, distal skin — above all the hand and forearm — and progression to deep structures or dissemination is the exception rather than the rule.

Two conditions are jointly necessary, which is the single most useful framing for curation:

> "Two conditions are required to develop M. marinum infection: (1) skin solution of continuity and (2) exposure to the contaminated water or direct contact with fish or shellfish." **[A]** — Canetti et al. 2022, PMID:35864075

Among NTM, it occupies a distinctive epidemiological position:

> "Among nontuberculous mycobacteria (NTM), it is the leading cause of extrarespiratory human infections worldwide." **[A]** — Aubry et al. 2017, PMID:28387180

### Key identifiers (all resolved in this session)

| Resource | Identifier | Label |
|---|---|---|
| MONDO | MONDO:0043314 | aquarium granuloma |
| MeSH (supplementary concept) | C535526 | — |
| SNOMED CT | 240417004 | — |
| UMLS | C0275708 | — |
| MedGen | 78814 | — |
| ICD-10-CM | A31.1 | Cutaneous mycobacterial infection |
| NCBI Taxonomy (agent) | NCBITaxon:1781 | *Mycobacterium marinum* |

MONDO's own definition: "A skin condition caused by Mycobacterium marinum, characterized by a skin lesion that presents roughly three weeks after exposure." MONDO places the term under two parents, both verified: MONDO:0020590 (mycobacterial infectious disease) and MONDO:0024295 (skin disease caused by bacterial infection). The term conforms to MONDO's `infectious_disease_by_agent` design pattern, which is the correct model for a dismech `disease_term` binding here.

**ICD-11:** not verified in this session. The WHO ICD-11 API requires OAuth, so no ICD-11 code should be written into the entry from this report. ICD-10-CM A31.1 was confirmed against the NLM Clinical Tables service and is exact.

**OMIM / Orphanet:** not applicable. This is an acquired environmental infection with no Mendelian basis, so no OMIM phenotype number exists, and the concept is not a rare-disease entity in the Orphanet sense.

### Synonyms

MONDO records: *fish tank granuloma*, *Mycobacterium marinum infection*, *Mycobacterium marinum skin disease*, *Mycobacterium marinum caused skin disease*, *M. marinum*, *aquarium granuloma*.

Additional names in the literature but **not** in MONDO's synonym list: *swimming pool granuloma*, *fish fancier's finger*, *fish handler's disease*, *fish gambler's tenosynovitis*. The name tracks the exposure rather than the biology:

> "M. marinum causes the so-called 'fish finger's fancier' or fish tank granuloma, or swimming pool granuloma in humans, depending on where the infection was contracted." **[F]** — search snippet, Hashish et al. 2018, PMID:29493404

*M. balnei* and *M. platypoecilus* are historical taxonomic synonyms of the organism.

### Level of aggregation

All quantitative data below are **individual-patient case series and retrospective cohorts**, not registry or EHR-derived aggregates. There is no disease registry for aquarium granuloma. The largest denominators available are laboratory-based: a nationwide Dutch laboratory cohort (n=40) and single-centre dermatology series from China (n=145 and n=200 isolates), Thailand (n=27), France (n=63), Taiwan (n=27), and the USA (n=31). Prevalence figures therefore rest on culture-confirmed case counts, which systematically undercount because culture sensitivity is poor (see §10).

---

## 2. Etiology

### Causal factor

A single necessary and sufficient agent: ***Mycobacterium marinum*** (NCBITaxon:1781). This is a monomicrobial infectious etiology; there is no genetic cause and no known non-infectious mimic of the entity itself.

Microbiological properties that drive the clinical picture:

> "Microbiological characteristics include the fact that it grows in 7 to 14 days with photochromogenic colonies and is difficult to differentiate from Mycobacterium ulcerans and other mycolactone-producing NTM on a molecular basis." **[A]** — Aubry et al. 2017, PMID:28387180

The organism is a Runyon group I photochromogen. Its restricted thermal optimum (roughly 30–33 °C) is the single most important physiological fact for this disease, since it both explains the anatomical distribution of lesions and defeats routine mycobacterial culture at 37 °C.

Historical first description (two dates circulate and should be recorded carefully — they refer to different events):

> "The first human cases of M. marinum infection were reported from skin lesions of swimmers in a contaminated pool, in 1951, in Sweden by Norden and Linell." **[A]** — Canetti et al. 2022, PMID:35864075

> "Mycobacterium marinum was first described in humans in 1954, known to infect fish species and contaminate water and fish products." **[A]** — Kravvas et al. 2024, PMID:39759953

### Risk factors — environmental and behavioural (the dominant axis)

Exposure source distribution, from the largest systematic exposure review (193 infections with a known exposure):

| Exposure | Share |
|---|---|
| Aquarium-related | 49% |
| Fish or shellfish injury | 27.4% |
| Saltwater or brackish-water injury | 8.8% |

> "Of 193 infections with known exposures, 49% were aquarium-related, 27.4% were related to fish or shellfish injuries, and 8.8% were related to injuries associated with saltwater or brackish water." **[A]** — Jernigan & Farr 2000, PMID:10987702

In the French national series, fish-tank exposure dominated even more heavily:

> "In 53 (84%) of the patients, inoculation was related to fish tank exposure." **[A]** — Aubry et al. 2002, PMID:12153378

Occupational and hobby exposures recorded across series: home aquarium keeping and tank cleaning, ornamental-fish trade, commercial fishing, fish mongering and fish processing, seafood preparation, shellfish handling, aquaculture work, and swimming in non-chlorinated pools. In a Chinese series of 35, fish-bone puncture wounds accounted for 54.3% and an aquatic-related occupation for 37.1% (PMID:39262684). In the Thai cohort, only 59.3% of patients reported any fish or water exposure at all — meaning roughly 40% of culture-confirmed cases had no elicited aquatic history (PMID:40535516). A negative exposure history does not exclude the diagnosis.

**Iatrogenic risk factor of particular importance — intralesional corticosteroid.** This is both a risk factor for deep extension and a diagnostic trap, because trigger-finger injection sites are exactly where tenosynovitis then appears:

> "Tenosynovitis occurred in 22.2% of patients, with a female preponderance (adjusted p = 0.028), advanced age (p = 0.032), and prior steroid injections at the lesion site (p = 0.007) being common factors." **[A]** — Jirawattanadon et al. 2025, PMID:40535516

> "Additionally, three patients (11.1%) developed lesions at the same site as previously reported for intralesional triamcinolone injections, which had been administered 3–8 weeks before the onset of the lesion for the treatment of stenosing tenosynovitis (or trigger fingers)." **[F]** — Jirawattanadon et al. 2025, PMID:40535516

The 2017 review makes the same point for deep disease generally: lesions "disseminated to joint and bone" are "often related with the local use of corticosteroids" **[A]** (PMID:28387180).

**Systemic immunosuppression.** TNF-α inhibitors, systemic corticosteroids, solid-organ and haematopoietic stem-cell transplantation, HIV infection, poorly controlled diabetes, and autoimmune disease on immunosuppressants. These do not appear to greatly increase susceptibility to the ordinary cutaneous form but strongly shift the disease toward deep, multifocal, and disseminated presentations and toward longer treatment:

> "The mean duration of cure was 5.6 ± 3.1 months, with immunosuppression significantly associated with a longer duration (p = 0.047)." **[A]** — PMID:40535516

> "Systemic dissemination is exceptional and has been reported to occur only in immunocompromised patients (e.g., solid-organ and hematopoietic stem cell transplant recipients or those on anti-TNF treatment)." **[F]** — search snippet, Aubry et al. 2017, PMID:28387180

**Demographic factors.** Female sex is associated with tenosynovitis specifically (adjusted OR 16.8, p=0.028; PMID:40535516), plausibly confounded by trigger-finger injection practice. Advancing age is associated with tenosynovitis (p=0.032). Mean or median ages across recent series cluster between 45 and 55 years.

### Genetic risk factors

**No established human genetic risk factor is specific to *M. marinum*.** A targeted PubMed search combining *M. marinum* with Mendelian susceptibility to mycobacterial disease (MSMD) genes (`IFNGR1`, `STAT1`, `IL12RB1`, "host genetics", "polymorphism", "innate immune") returned no study establishing a *M. marinum*-specific susceptibility locus; the top hits were antimicrobial-susceptibility papers about the bacterium, not the host. Two things follow for curation:

1. Do **not** populate a `genetic:` section with MSMD genes for this entry. Any inference from the broader NTM/MSMD literature would be an extrapolation this disease's own literature does not support.
2. The generic IL-12/IFN-γ-axis argument is mechanistically plausible and worth recording as a `discussions:` `KNOWLEDGE_GAP`, not as a curated gene.

One host-genetic finding from the closely related zebrafish model is worth flagging as mechanistically informative but non-human: `LTA4H` (leukotriene A4 hydrolase) genotype modulates the inflammatory set-point in mycobacterial disease, with heterozygote advantage and both extremes disadvantaged (Tobin et al. 2012, PMID:22304914). That work was done in zebrafish–*M. marinum* and human tuberculosis cohorts, not in aquarium granuloma patients.

### Protective factors

- **Mechanical barrier.** Intact skin is fully protective given the requirement for a "skin solution of continuity" **[A]** (PMID:35864075). Waterproof gloves during tank maintenance and fish handling are therefore primary prevention, not adjunct advice.
- **Water chlorination.** The disease's swimming-pool form essentially disappeared with routine pool chlorination; the organism persists in non-chlorinated water. ECTO has a term for the relevant exposure: ECTO:5000002 (exposure to public swimming pool).
- **Post-exposure skin antisepsis.** The 2017 review recommends "use of alcohol disinfection after contact" **[A]** (PMID:28387180).
- **Genetic protective factors:** none identified; not applicable.

### Gene–environment interaction

Not applicable in the usual GxE sense. The interaction that matters is **drug–environment**: an environmental inoculation event whose outcome is determined by pharmacological interference with host TNF signalling. This is mechanistically grounded rather than merely epidemiological — TNF is the cytokine the zebrafish model shows to be rate-limiting for containment (§6) — and it has a direct management consequence:

> "It should be recommended to stop TNF-α inhibitor or other immunosuppressive therapy during the course of antibiotics when M. marinum infection occurs in patients treated with these medications." **[F]** — search snippet, Aubry et al. 2017, PMID:28387180

---

## 3. Phenotypes

### Core cutaneous phenotypes with frequencies

Frequencies differ substantially between series, and the differences are informative rather than noise: the Chinese series recruited through a dermatology mycobacterium referral centre (sporotrichoid 71.4%), the Thai series through a general tertiary hospital (sporotrichoid 29.6%). Curate both, stratified by `population`.

| Phenotype | Suggested HP term | Frequency | Source |
|---|---|---|---|
| Skin nodule | HP:0200036 Skin nodule | 27/35 (77.1%) | PMID:39262684 |
| Papules and nodules | HP:0200034 Papule | 8/27 (29.6%) | PMID:40535516 |
| Skin plaque | HP:0200035 Skin plaque | 14/27 (51.9%) | PMID:40535516 |
| Erythema | HP:0010783 Erythema | 20/35 (57.1%) | PMID:39262684 |
| Abscess | HP:0025615 Abscess | 18.5% (Thai); 1/35 (2.9%) (Chinese) | PMID:40535516; PMID:39262684 |
| Skin ulcer | HP:0200042 Skin ulcer | 3.7% | PMID:40535516 |
| Pustule | HP:0200039 Pustule | 3.7% | PMID:40535516 |
| Granuloma (histological) | HP:0032252 Granuloma | 35/35 (100%) histology; 22/35 (63%) biopsies | PMID:39262684; PMID:8002687 |
| Tenosynovitis | HP:6001438 Tenosynovitis | 6/27 (22.2%) | PMID:40535516 |
| Arthritis | HP:0001369 Arthritis | reported, not quantified in these series | PMID:28387180 |
| Osteomyelitis | HP:0002754 Osteomyelitis | reported, not quantified in these series | PMID:25664190 |
| Joint swelling | HP:0001386 Joint swelling | all tenosynovitis patients had pain and soft-tissue swelling | PMID:40535516 |
| Unusual mycobacterial skin infection | HP:5210242 | the entity-level descriptor | OLS4, verified |
| Disseminated NTM infection | HP:0032283 | exceptional; immunocompromised only | PMID:28387180 |

**The sporotrichoid pattern has no HPO term.** Explicit OLS4 searches of the HP ontology for `Sporotrichoid` and for `Lymphangitis` returned **no** defining-ontology match (the latter returned only lymphangioma, lymphangiectasis, and pulmonary lymphangiomyomatosis, which are different concepts). Record the ascending linear arrangement of nodules in `preferred_term` and `description`, bind the nodule itself to HP:0200036, and put the searched-and-absent finding in `notes` naming both queries. Do not stretch a lymphatic-malformation term to cover it.

Frequency of the pattern, both series:

> "Nodules were the most common cutaneous manifestation (27/35, 77.1%)" and, of those, a sporotrichoid arrangement in 25/27 — 71.4% of the whole series **[F]** (PMID:39262684).

> "A linear arrangement, indicative of a lymphocutaneous or sporotrichoid pattern, was noted in 8 cases (29.6%)." **[F]** — PMID:40535516

An older US series found local or lymphatic spread even more often:

> "The upper extremity was affected in 90% of cases, and lymphatic or local spread was seen during the initial examination or during observation in 25 patients (81%)." **[A]** — Edelstein 1994, PMID:8002687

### Phenotype characteristics

**Onset.** Age of onset is exposure-determined, not developmental: adult-onset in essentially all series (mean 45.5 ± 15.4 years, Thailand; median 55 years, IQR 49–59, China). Paediatric cases occur with aquarium exposure but are not the reported norm. There is no congenital, neonatal, or late-onset pattern to record.

**Incubation period — a key curation number.**

> "Forty cases had known incubation periods (median, 21 days; range, 5-270 days). Thirty-five percent of cases had an incubation period > or =30 days." **[A]** — Jernigan & Farr 2000, PMID:10987702

The practical consequence, which is the reason the paper exists:

> "Because the incubation period for cutaneous M. marinum infection can be prolonged, patients with atypical cutaneous infections should be questioned about high-risk exposures that may have occurred up to 9 months before the onset of symptoms." **[A]** — PMID:10987702

Note that MONDO's definition ("roughly three weeks after exposure") matches the 21-day median and understates the tail.

**Severity.** Variable, and best modelled as a staged spectrum rather than a severity grade. The Dutch cohort used a four-stage scheme in which stage IV (deep) disease was 15% of cases (6/40; PMID:35308482). The veterinary/human review describes a type I–IV clinical classification **[A]** (PMID:29493404). Most disease is mild and localized; morbidity concentrates in the deep-infection minority.

**Progression.** Chronic, indolent, and slowly progressive if untreated. Lesions evolve over weeks to months from a papule to a nodule, then plaque, with possible superficial crusting, verrucous change, or ulceration; sporotrichoid spread follows lymphatic drainage proximally. Deep extension unfolds over months:

> "These infections can progress over several months to involve deeper soft tissues, resulting in arthritis, tenosynovitis, and osteomyelitis, irrespective of the patient's immunological status." **[F]** — PMID:40535516

Spontaneous resolution over months to years is described but is not a reliable outcome, and the untreated course can run for years — one report documents a 20-year infection.

**Quality-of-life impact.** No EQ-5D, SF-36, or PROMIS data exist for this disease; a search of the clinical literature surfaces none. What is documented is functional rather than instrumented: hand and finger involvement in 81.5–82.9% of cases, pain and soft-tissue swelling in all tenosynovitis patients, surgical debridement in 28–48% of cohorts, and treatment courses of 4–6 months minimum. Record the absence of formal QoL measurement as a gap rather than substituting a plausible-sounding estimate.

---

## 4. Genetic/Molecular Information

**This section is largely not applicable and should be curated as such.** Aquarium granuloma is an acquired bacterial infection. There are no causal human genes, no pathogenic variants, no inheritance pattern, no carrier frequency, no ACMG variant classifications, no allele frequencies in gnomAD, and no chromosomal abnormalities. Populating a `genetic:` section with human genes would be a category error.

Two genuinely relevant molecular-genetic topics exist, and both belong to the **pathogen**, not the host.

### Pathogen genome (the substrate for §6's mechanism)

> "The genome of the M strain of M. marinum comprises a 6,636,827-bp circular chromosome with 5424 CDS, 10 prophages, and a 23-kb mercury-resistance plasmid. Prominent features are the very large number of genes (57) encoding polyketide synthases (PKSs) and nonribosomal peptide synthases (NRPSs) and the most extensive repertoire yet reported of the mycobacteria-restricted PE and PPE proteins, and related-ESX secretion systems." **[A]** — Stinear et al. 2008, PMID:18403782

Relatedness to *M. tuberculosis* (NCBITaxon:1773) is the reason this organism matters beyond dermatology:

> "Genome comparisons confirmed the close genetic relationship between these two species, as they share 3000 orthologs with an average amino acid identity of 85%." **[A]** — PMID:18403782

And the evolutionary asymmetry:

> "M. tuberculosis has undergone genome downsizing and extensive lateral gene transfer to become a specialized pathogen of humans and other primates without retaining an environmental niche. M. marinum has maintained a large genome so as to retain the capacity for environmental survival while becoming a broad host range pathogen that produces disease strikingly similar to M. tuberculosis." **[A]** — PMID:18403782

*M. marinum* is also the direct progenitor of *M. ulcerans* (NCBITaxon:1809), which arose by plasmid acquisition and reductive evolution — the basis for the molecular-identification difficulty noted in §1. Reported figures of >97% nucleotide identity with *M. ulcerans*, >85% with *M. tuberculosis*, and 29 *esx* genes in *M. marinum* against 23 in *M. tuberculosis* come from **[F]** secondary-review snippets and must be sourced to the primary paper before use.

### Antimicrobial resistance genotypes

Acquired resistance is genuinely rare in *M. marinum*, which distinguishes it sharply from *M. abscessus*:

> "All strains showed the same susceptibility pattern without acquired resistance." **[A]** — Aubry et al. 2002, PMID:12153378

The largest modern isolate panel (200 *M. marinum*) confirms a broadly susceptible wild-type phenotype and, notably, found no resistance determinant worth sequencing in *M. marinum* — the `erm(41)`, `rrl`, `rrs`, `gyrA`, `gyrB` sequencing in that study was applied to the *M. abscessus* comparator arm only (PMID:41135669). See §12 for the MIC data.

**Epigenetics, modifier genes, chromosomal abnormalities:** not applicable.

---

## 5. Environmental Information

### Infectious agent

*Mycobacterium marinum*, NCBITaxon:1781. Environmental niche is aquatic and extremely broad:

> "M. marinum is a nontuberculous mycobacterium (NTM) and zoonotic pathogen that has been isolated from mammals, fish, amphibians, reptiles, birds, invertebrates, and protists; M. marinum is also widely distributed in nature, especially in aquatic environments." **[F]** — search snippet, Hashish et al. 2018, PMID:29493404

Reservoirs: fresh, brackish, and marine water; aquarium water, gravel, and biofilm; fish and their mucus and viscera; shellfish; non-chlorinated swimming pools; aquaculture ponds. Tank biofilm matters more than free water, which is why cleaning is the risk activity.

### Exposure routes and ECTO term availability

Transmission to humans is **percutaneous inoculation only**. There is no human-to-human transmission, no respiratory route, and no foodborne route for this disease; the oral route described in the fish literature is fish-to-fish.

> "Inoculation to humans occurs through injured skin resulting in the formation of a solitary nodule known as 'fish tank granuloma.'" **[A]** — Kravvas et al. 2024, PMID:39759953

**ECTO binding is a real gap, and the searches are recorded here so the note can be honest.** OLS4 searches of the ECTO ontology returned:

| Query | Result |
|---|---|
| `Mycobacterium marinum` | no match |
| `marinum` | no match |
| `aquarium` | no match |
| `seafood` | no match |
| `wound` | no match |
| `exposure to fish` | only ingestion terms (ECTO:0070164 fish oil supplement, ECTO:0070209 dark fish flesh, ECTO:0070189 whitefish) |
| `exposure to bacterium` | only unrelated taxa |
| `exposure to Mycobacterium` | ECTO:3000134 *M. tuberculosis*, ECTO:3000132 *M. avium* subsp. *paratuberculosis*, ECTO:3000133 *M. tuberculosis* subsp. *tuberculosis* — **no *M. marinum*** |
| `exposure to water` | **ECTO:9000156 exposure to water** |
| `swimming pool` | **ECTO:5000002 exposure to public swimming pool** |
| `shellfish` | ECTO:0070188 exposure to shellfish via ingestion (ingestion route — wrong route) |

So: two usable terms (ECTO:9000156 for the generic aquatic exposure, ECTO:5000002 for the swimming-pool form), no term for aquarium-water contact, fish handling by contact, or *M. marinum* exposure. Bind what exists, leave the aquarium-contact exposure with a free-text `preferred_term` and no `term:`, and record these exact queries in `notes`. A new ECTO term request for aquarium-water contact exposure is the right follow-up.

### Lifestyle factors

Home aquarium keeping is the single dominant behavioural exposure (49% of known exposures, PMID:10987702). Recreational fishing, seafood preparation at home, and swimming in untreated water follow. Smoking, alcohol, diet, and exercise have no established role and should not be curated.

### Non-aquatic exposure — a 2024 addition worth recording

A reptile-associated case with no aquatic history at all was reported as the first of its kind:

> "Our patient had no history of exposure to aquatic organisms but had previously cared for an inland bearded dragon with an unknown illness. Although infection with M. marinum has been reported in reptiles, cases of nonaquatic zoonotic transmission have not been described in the literature." **[A]** — Kravvas et al. 2024, PMID:39759953

That patient had rheumatoid arthritis and bronchiectasis, was initially diagnosed with Sweet's syndrome, improved on prednisolone and then deteriorated — a clean worked example of the immunosuppression-plus-misdiagnosis trajectory.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

The chain below is assembled from human clinicopathological data for steps 1–3 and 9–12, and from the zebrafish–*M. marinum* model for steps 4–8. The species provenance of each step is stated because it is the central translational caveat of this entry: the granuloma biology is known in extraordinary molecular detail, but almost all of that detail comes from zebrafish infected with the same organism, not from human aquarium granuloma lesions.

1. **Skin barrier breach** (abrasion, laceration, fish-spine or fish-bone puncture) **leads to** direct inoculation of *M. marinum* into the dermis. *Human; necessary condition, PMID:35864075.*
2. **Dermal inoculation leads to** phagocytosis of bacilli by resident dermal macrophages (CL:0000235) and recruited monocytes (CL:0000576). *Human inference from histology; mechanism demonstrated in model.*
3. **Local tissue temperature near 30–33 °C in distal skin permits replication**, whereas 37 °C core temperature restricts it. This **results in** the confinement of disease to hand, forearm, and other cool distal sites, and is the reason ~90% of lesions are on the upper extremity. *Human; inferred from the organism's growth optimum plus lesion distribution, PMID:3840985, PMID:8002687.*
4. **Surface phthiocerol dimycocerosate (PDIM) masks pathogen-associated molecular patterns, which leads to** evasion of microbicidal macrophages, while **phenolic glycolipids (PGL) lead to** CCR2-dependent recruitment of *permissive* macrophages. The bacterium thus selects its own host cell. *Demonstrated in zebrafish and mice, PMID:24336213.*

   > "This immune evasion is accomplished by using cell-surface-associated phthiocerol dimycoceroserate (PDIM) lipids to mask underlying pathogen-associated molecular patterns (PAMPs)... Concordantly, the related phenolic glycolipids (PGLs) promote the recruitment of permissive macrophages through a host chemokine receptor 2 (CCR2)-mediated pathway." **[A]** — PMID:24336213

5. **ESX-1/RD1 secretion of ESAT-6 (EsxA) induces MMP9 in neighbouring epithelial cells, which leads to** further macrophage recruitment and nascent granuloma maturation. This is the branch point where the granuloma becomes a bacterial asset rather than a host defence. *Zebrafish, PMID:20007864.*

   > "The bacterial secreted protein 6-kD early secreted antigenic target (ESAT-6), which has long been implicated in virulence, induced matrix metalloproteinase-9 (MMP9) in epithelial cells neighboring infected macrophages. MMP9 enhanced recruitment of macrophages, which contributed to nascent granuloma maturation and bacterial growth." **[A]** — PMID:20007864

6. **Arriving macrophages phagocytose infected apoptotic macrophages, which results in** iterative expansion of the infected-macrophage pool and hence of bacterial numbers. *Zebrafish intravital microscopy, PMID:19135887.*

   > "This motility enables multiple arriving macrophages to efficiently find and phagocytose infected macrophages undergoing apoptosis, leading to rapid, iterative expansion of infected macrophages and thereby bacterial numbers. The primary granuloma then seeds secondary granulomas via egress of infected macrophages." **[A]** — PMID:19135887

7. **TNF signalling restricts intramacrophage bacterial growth, which leads to** maintenance of granuloma integrity — indirectly, not by organizing the structure. *Zebrafish, PMID:18691913.*

   > "TNF is not required for tuberculous granuloma formation, but maintains granuloma integrity indirectly by restricting mycobacterial growth within macrophages and preventing their necrosis." **[A]** — PMID:18691913

   **Branch — TNF loss (the anti-TNF-drug arm):** loss of TNF signalling **leads to** accelerated intracellular growth, then necrotic death of overladen macrophages and granuloma breakdown. This is the mechanistic account of why TNF-inhibitor-treated patients get deep and disseminated disease.

   **Branch — TNF excess:** excess TNF **induces** mitochondrial ROS through RIP1–RIP3, driven by reverse electron transport at complex I after TNF-activated glutamine uptake raises succinate; mROS then **induces** macrophage necroptosis via cyclophilin D and acid-sphingomyelinase–ceramide, **which releases** bacteria into the permissive extracellular milieu. *Zebrafish, PMID:23582643 and PMID:35737799.*

   > "TNF excess induces mitochondrial reactive oxygen species (ROS) in infected macrophages through RIP1-RIP3-dependent pathways. While initially increasing macrophage microbicidal activity, ROS rapidly induce programmed necrosis (necroptosis) and release mycobacteria into the growth-permissive extracellular milieu." **[A]** — PMID:23582643

   > "Excess TNF in mycobacterium-infected macrophages elevates mROS production by reverse electron transport (RET) through complex I. TNF-activated cellular glutamine uptake leads to an increased concentration of succinate, a Krebs cycle intermediate. Oxidation of this elevated succinate by complex II drives RET, thereby generating the mROS superoxide at complex I." **[A]** — PMID:35737799

8. **Granuloma core enlargement leads to** hypoxia, HIF-1 induction, suppressed mitochondrial respiration, and sensitization of macrophages to EsxA mitotoxicity, **which results in** caseous necrosis. *Zebrafish; this is the most recently characterized step and the least established in human aquarium granuloma.* **[F]** — search snippet, granuloma-hypoxia work.
9. **Granulomatous dermal inflammation produces** the clinically visible nodule, plaque, or verrucous lesion, with a histological spectrum from suppurative to well-formed granulomatous. *Human, PMID:3840985.*
10. **Egress of infected macrophages into dermal lymphatics (UBERON:0001473) leads to** seeding of successive nodules along the lymphatic drainage — the sporotrichoid pattern. *Mechanism of egress from zebrafish (PMID:19135887); the lymphatic distribution itself is a human observation (PMID:8002687).*
11. **Contiguous extension to tendon sheath (UBERON:0000304), synovium (UBERON:0002018), and bone (UBERON:0001474) results in** tenosynovitis, arthritis, bursitis, and osteomyelitis. Local corticosteroid injection and systemic immunosuppression are the permissive conditions. *Human, PMID:28387180, PMID:40535516.*
12. **In profound immunosuppression, escape from thermal and immune restriction leads to** disseminated infection. Exceptional. *Human, PMID:28387180.*

### Molecular pathways and cellular processes, with suggested GO terms

All GO CURIEs below were resolved in OLS4 in this session.

| Process | GO term |
|---|---|
| Granuloma formation | GO:0002432 granuloma formation |
| Macrophage activation | GO:0042116 macrophage activation |
| Phagocytosis | GO:0006909 phagocytosis |
| Macrophage chemotaxis (MMP9/CCR2-driven recruitment) | GO:0048246 macrophage chemotaxis |
| Necroptosis of infected macrophages | GO:0070266 necroptotic process |
| Apoptosis of infected macrophages | GO:0006915 apoptotic process |
| TNF production | GO:0032640 tumor necrosis factor production |
| Positive regulation of TNF production | GO:0032760 |
| Type II interferon (IFN-γ) production | GO:0032609 type II interferon production |
| Cellular response to IFN-γ | GO:0071346 cellular response to type II interferon |
| Mitochondrial ROS generation | GO:0072593 reactive oxygen species metabolic process |
| Granuloma-core hypoxia | GO:0001666 response to hypoxia |
| MMP9-mediated matrix remodelling | GO:0022617 extracellular matrix disassembly |

Note GO:0002432's own definition names the cell types the granuloma contains — "compactly grouped T lymphocytes and modified phagocytes such as epithelioid cells, giant cells, and other macrophages" — which makes it the right anchor for the central pathophysiology node.

### Cell types with suggested CL terms

| Cell type | CL term | Role |
|---|---|---|
| macrophage | CL:0000235 | primary host cell; site of replication and of necroptosis |
| monocyte | CL:0000576 | recruited precursor |
| epithelioid macrophage | CL:0002150 | granuloma architecture |
| multinucleated giant cell | CL:0000647 | granuloma architecture (Langhans-type) |
| neutrophil | CL:0000775 | suppurative pole of the histological spectrum; necrosis-associated program |
| T cell | CL:0000084 | adaptive control; sparse in fish granulomas, prominent in human |
| keratinocyte | CL:0000312 | epidermal compartment; epithelial MMP9 source in the model |
| fibroblast | CL:0000057 | granuloma-associated fibroblast population (2026 single-cell work) |

### Protein dysfunction, metabolic changes, biochemical abnormalities

These categories apply to the **pathogen's effectors and the host's infected-cell metabolism**, not to a host protein defect. Key molecules: EsxA/ESAT-6 and EsxB/CFP-10 (ESX-1 substrates, mitotoxic and MMP9-inducing); PDIM and PGL cell-wall lipids; host MMP9; host RIPK1/RIPK3; cyclophilin D (mitochondrial permeability transition); acid sphingomyelinase and ceramide; HIF-1. The metabolic lesion is specific and druggable: TNF-driven glutamine uptake → succinate accumulation → complex II oxidation → reverse electron transport at complex I → superoxide. There are no systemic metabolic abnormalities in patients.

### Immune system involvement

Chronic granulomatous inflammation with a demonstrated Th1 component in human lesions, plus signals that complicate a pure-Th1 reading:

> Immunohistochemistry on lesional tissue showed significant upregulation of IFN-γ (p<0.01), IL-4 (p<0.05), IL-9 (p<0.05) and FOXP3 (p<0.05), with no significant difference for IL-17 or IL-22. **[F]** — PMID:39262684

The co-elevation of IL-4, IL-9 and FOXP3 alongside IFN-γ is worth curating as a mixed Th1/Th2/Treg lesional profile rather than flattening it to "Th1 response".

Adaptive immunity is required for control, established genetically in the model:

> "However, like rag1 mutant mice infected with M. tuberculosis, we find that rag1 mutant zebrafish are hypersusceptible to M. marinum infection, demonstrating that the control of fish tuberculosis is dependent on adaptive immunity." **[A]** — Swaim et al. 2006, PMID:17057088

Peripheral IFN-γ release is measurable and clinically exploitable — T-SPOT.TB is positive in 71% of cutaneous cases, reflecting ESAT-6/CFP-10 cross-reactivity between *M. marinum* and *M. tuberculosis* (PMID:41147233). This is a direct clinical readout of step 5 of the causal chain.

### Molecular profiling — datasets available

All accessions below were retrieved from NCBI GEO in this session and are real. Note that all but two are zebrafish or mouse; **no human lesional transcriptomic dataset for aquarium granuloma was found**.

| Accession | Organism | n | Content |
|---|---|---|---|
| GSE289727 | *Danio rerio*; *M. marinum* | 17 | Granuloma dual RNA-seq; neutrophil- and necrosis-driven composite transcriptional programs in necrotic granulomas |
| GSE296119 | *Danio rerio* | 15 | Paired single-cell and spatial profiling; osteopontin (*spp1*) macrophage response mediating granuloma formation |
| GSE314022 | *Danio rerio* | 1 | Wild-type granuloma cells from *M. marinum*-infected zebrafish |
| GSE324157 / GSE299987 | *Danio rerio* | 2 / 1 | Single-cell; eicosanoid-defined granuloma-associated fibroblast population, *apodb* mutant vs WT |
| GSE328953 | *Homo sapiens* | 15 | THP-1-derived macrophages infected with mycobacteria (cell line, not lesion) |
| GSE235124 | *Mus musculus* | 11 | Single-cell RNA-seq of infected vs bystander monocytes; WT, *espK*::tn, ΔRD1 *M. marinum* |
| GSE289727, GSE287594, GSE189627 | *Danio rerio* | 17/12/24 | *pycard* (inflammasome) mutant neutrophil and kidney responses |
| GSE270105 / GSE269547 | *Danio rerio* | 15 / 6 | mRNA vaccine inducing antimycobacterial immunity via DNA damage repair and autophagy |

GSE296119's own summary states the finding compactly: "mycobacterial infection induces spp1 expression in macrophages and that spp1 ablation results in granuloma formation defects and reduced survival in adult animals." **[F]**

**Proteomics, metabolomics, lipidomics, epigenomics of human lesions:** none found. Curate as absent.

---

## 7. Anatomical Structures Affected

### Organ and regional level

| Level | Structure | UBERON term | Involvement |
|---|---|---|---|
| Primary | skin of manus | UBERON:0001519 | hand lesions 81.5%; fingers/hands 82.9% |
| Primary | manual digit skin | UBERON:0003533 | commonest single site |
| Primary | skin of forearm | UBERON:0003403 | sporotrichoid extension target |
| Primary | manus | UBERON:0002398 | regional container |
| Primary | dermis | UBERON:0002067 | the granuloma's compartment |
| Primary | hypodermis | UBERON:0002072 | deeper cutaneous extension |
| Secondary | tendon sheath | UBERON:0000304 | tenosynovitis, 22.2% |
| Secondary | synovial membrane of synovial tendon sheath | UBERON:0011233 | tenosynovitis, precise site |
| Secondary | synovial membrane of synovial joint | UBERON:0002018 | arthritis |
| Secondary | bone element | UBERON:0001474 | osteomyelitis |
| Secondary | olecranon | UBERON:0006810 | bursitis site |
| Secondary | lymphatic vessel | UBERON:0001473 | route of sporotrichoid spread |

Body systems: integumentary (primary), musculoskeletal (secondary), lymphatic (spread route). Respiratory, cardiovascular, nervous, endocrine, and digestive systems are uninvolved except in exceptional dissemination.

The upper-limb predominance is one of the most reproducible numbers in this literature:

> "The site of infection was mainly the upper limb (in 60 [95%] of the 63 patients), and infection was spread to deeper structures in 18 (29%) of the patients." **[A]** — Aubry et al. 2002, PMID:12153378

Independent series: 90% upper extremity (PMID:8002687), 97.1% upper extremities with 82.9% fingers/hands (PMID:39262684), 81.5% hand (PMID:40535516). Lower-limb and knee cases occur — the Thai series includes a leg wound in an agricultural worker and a sporotrichoid plaque on a knee.

### Tissue, cell, and subcellular level

Tissues: dermal connective tissue (UBERON:0003585 dermis connective tissue), subcutaneous adipose tissue (UBERON:0002190), synovium, tendon, bone. Cell populations as tabulated in §6.

Subcellular compartments matter unusually much here, because the necrosis mechanism is mitochondrial. Relevant GO cellular components to bind at curation time if a subcellular node is created: the mitochondrion and the phagosome. These two were **not** resolved in this session — look them up before writing the CURIEs rather than carrying them over from this report.

### Localization and lateralization

Predominantly **unilateral**, matching a single inoculation event, and right-sided more often than left in the one series that reported laterality: right 18/35 (51.4%), left 12/35 (34.3%), bilateral 5/35 (14.3%) — with multiple lesions in 71.4% (PMID:39262684). Bilateral disease should prompt a search for immunosuppression or repeated exposure. The lesion distribution is **acral and distal**, which is a thermal constraint rather than an anatomical affinity.

---

## 8. Temporal Development

### Onset

- **Age:** adult-onset; means and medians 45–55 years across recent series. Exposure-determined, not age-determined.
- **Incubation:** median 21 days, range 5–270 days; ≥30 days in 35% (PMID:10987702).
- **Pattern:** subacute to chronic and insidious. Never acute in the sepsis sense.

### Stages

The Dutch cohort's four-stage scheme, with stage IV (deep structures) at 15% of cases, is the most usable staging for a `stages:` block (PMID:35308482). A four-type clinical classification (type I–IV) is also described **[A]** (PMID:29493404). Deep-structure involvement rates across cohorts: 29% (France, PMID:12153378), 22.2% (Thailand, tenosynovitis only, PMID:40535516), 15% (Netherlands stage IV, PMID:35308482); a review states 20–40% **[F]** (PMID:28387180).

### Progression and diagnostic delay

Diagnostic delay is a defining temporal feature and should be curated as such, not as an aside. Reported time from lesion onset to diagnosis:

| Series | Delay |
|---|---|
| China, n=35 | median 3 months (IQR 2.0–4.0) |
| Thailand, n=27 | median 6 months, range 1–120 |

> "The median onset duration, defined as the time between the initial appearance of lesions and the culture report, was 6 (1, 120) months." **[F]** — PMID:40535516

The 120-month outlier is not an error; multi-year untreated infections are documented. The mechanism of delay is structural:

> "The diagnosis of cutaneous Mycobacterium marinum infection is often delayed for months after presentation, perhaps because important clinical clues in the patient's history are frequently overlooked." **[A]** — PMID:10987702

> "Its non-specific cutaneous manifestations frequently lead to diagnostic delay and misdiagnosis." **[A]** — Yang et al. 2026, PMID:42639276

### Duration and course

Treated disease resolves over months. Treatment durations (a proxy for disease duration, since therapy runs until resolution): mean 25 weeks (~5.8 months) in the Netherlands, mean 5.6 ± 3.1 months in Thailand, median 4.0 months (IQR 3.0–6.0) in China, median 3.5 months in France. Untreated disease is chronic and can persist for years; spontaneous remission is described but unreliable.

### Remission patterns and critical windows

Remission is essentially **treatment-induced**. Relapse after adequate therapy is uncommon — the Thai series reported no recurrence in any tenosynovitis patient across 1 year of follow-up after debridement plus antibiotics (PMID:40535516); the Dutch cohort had 3/40 failures or relapses (PMID:35308482).

Two critical windows are worth recording:

1. **The nine-month exposure-history window.** Asking about aquatic exposure up to 9 months back is what converts an "atypical cutaneous infection" into a diagnosis (PMID:10987702).
2. **The pre-deep-extension window.** Failure is tied to deep involvement, so the interval before extension is where intervention changes outcome: "Failure was related to deep structure involvement (3 of 45 vs 5 of 18 patients; P =.04) but not to any antibiotic regimen." **[A]** (PMID:12153378).

A third pattern deserves a note: a persistent sterile necrotizing granulomatous dermatitis has been reported *after* successful treatment of a long-standing infection, i.e. an apparent paradoxical/immunopathological reaction rather than treatment failure. Confirm the primary source before curating.

---

## 9. Inheritance and Population

### Epidemiology

**Incidence.** One population-denominated figure is solid:

> "The annual incidence rate was 0.15/100 000/year during the study period." **[A]** — Hendrikx et al. 2022, PMID:35308482 (Netherlands, 2011–2018, laboratory-based)

A figure of 0.04 per 100,000 per year attributed to a French study appeared in search summaries in this session but was **not verified against a primary source**; do not curate it without confirmation.

For a `Prevalence` record, use `measure_type: ANNUAL_INCIDENCE`, `rate_per_100000: 0.15`, and set `rate_denominator` explicitly — the Dutch figure is per population per year, so `POPULATION_PER_YEAR`. Do **not** attach a qualitative tier such as RARE to an incidence record. `prevalence_class: BAND_1_9_PER_1000000` is the Orphanet-aligned magnitude band for 0.15/100,000 (= 1.5 per million).

**Prevalence.** No point-prevalence estimate exists. Case counts are the only available measure for most regions, so `CASES_IN_LITERATURE` is the honest `measure_type` for series-derived records.

**Underestimation.** Every incidence figure here is a culture-confirmed count, and culture is insensitive (culture-positive in only 74.3% of a clinically diagnosed series, PMID:39262684; AFB-positive in 2/22 and 6/35 biopsies). True incidence is higher by an unknown factor.

### Inheritance

**Not applicable.** No inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency. Leave the `inheritance:` section absent rather than populating it with a placeholder.

### Population demographics

**Sex ratio — genuinely discordant between series, and the discordance is a finding.**

| Series | Male : Female |
|---|---|
| Thailand, n=27 | 20 : 7 (male-predominant) |
| China (Han), n=35 | 6 : 29 (82.9% female) |

The Chinese series' female predominance tracks its exposure profile — fish-bone puncture wounds during food preparation (54.3%) — whereas male predominance elsewhere tracks aquarium keeping and fishing. Curate both with `population` set, and do not average them into a single ratio.

**Age distribution.** Adults, mode in the fifth and sixth decades. Median 55 (IQR 49–59) in China; mean 45.5 ± 15.4 in Thailand.

**Geographic distribution.** Worldwide, wherever people keep aquaria, handle fish, or swim in untreated water. There is no endemic focus in the vector-borne sense. Published series come from France, the Netherlands, the USA, Taiwan, China, Thailand, India (Kerala), the UK, and Egypt. Regional case mix is driven by local exposure practice, not by organism distribution. Geographic variation in *variants* of the organism is not established.

**Ethnic predisposition.** None. The Han Chinese series (PMID:39262684) reflects the recruiting centre, not a susceptibility.

---

## 10. Diagnostics

### The central diagnostic fact

Routine mycobacterial workup misses this organism, for a specific and correctable reason:

> "Therefore, culture of the biopsy tissue at 30 degrees C is crucial in establishing the diagnosis." **[A]** — Travis et al. 1985, PMID:3840985

> "In clinical microbiology, microscopy and culture are often negative because growth requires low temperature (30°C) and several weeks to succeed in primary cultivation." **[A]** — Aubry et al. 2017, PMID:28387180

**The laboratory must be told to incubate at 30 °C.** This is the single highest-yield action in the diagnostic pathway and belongs in the entry's `definitions` or `notes` as such.

### Microbiological tests, with sensitivities

| Test | Yield | Source |
|---|---|---|
| Tissue culture at 30 °C | 26/35 (74.3%) | PMID:39262684 |
| qPCR on tissue | 17/35 (48.6%) | PMID:39262684 |
| AFB (Ziehl-Neelsen) on biopsy | 6/35 (17.1%) | PMID:39262684 |
| AFB on biopsy | 2/22 (9%) | PMID:8002687 |
| Organisms visible on histology | 1/9 cases | PMID:3840985 |
| T-SPOT.TB (IFN-γ release) | 71% (95% CI 63.2–77.8) | PMID:41147233 |
| Targeted NGS | evaluated 2022–2024; cross-sectional | PMID:40833738 |

Culture turnaround is 7–14 days for colonies from a growing subculture but 2–8 weeks for primary isolation **[F]**, which is why molecular methods matter clinically. Species identification uses *hsp65* PCR, *rpoB* sequencing, line-probe assay (e.g. INNO-LiPA MYCOBACTERIA), and increasingly NGS. Be aware of the identification pitfall: *M. marinum* "is difficult to differentiate from Mycobacterium ulcerans and other mycolactone-producing NTM on a molecular basis" **[A]** (PMID:28387180).

### Histopathology

The pattern is a spectrum, not a single picture — which is exactly why biopsy alone under-diagnoses:

> "A range of inflammatory changes were seen in both synovial and skin lesions, varying from mostly acute inflammation with suppuration to a more chronic process with numerous, well-formed granulomas." **[A]** — PMID:3840985

> "These cases emphasize the importance of considering mycobacterial infection and performing cultures even when granulomatous changes in the synovium or skin are subtle." **[A]** — PMID:3840985

Granulomatous inflammation was present in 100% of the Chinese series (PMID:39262684) and 63% of biopsies in the Kaiser series (PMID:8002687) — the difference reflecting lesion age and sampling.

### Immunological adjunct — T-SPOT.TB

A 2025 study of 145 patients supports IFN-γ release assays both diagnostically and as a treatment-response monitor:

> "The baseline T-SPOT.TB positivity rate was 71% (95% CI: 63.2-77.8%). Among 17 patients retested at 3 months, positivity was 64.7% (p = 0.125), with median spot-forming cells (SFCs) significantly decreasing from 20.0 (IQR 8.5-41.0) to 8.0 (IQR 2.5-28.0) (p = 0.0007)." **[A]** — PMID:41147233

> "The T-SPOT.TB assay shows significant diagnostic value for cutaneous M. marinum infections and facilitates early diagnosis. Declining SFC counts post-treatment provide useful reference for evaluating therapeutic response." **[A]** — PMID:41147233

Interpretive caveat for curation: a positive T-SPOT.TB reflects ESAT-6/CFP-10 responses shared with *M. tuberculosis*, so it cannot distinguish the two. That study explicitly excluded tuberculosis cases.

### Imaging and functional tests

MRI and ultrasound for suspected tenosynovitis, and plain radiography or MRI for osteomyelitis. No imaging finding is specific. Electrophysiology, pulmonary function, and cardiac testing are not applicable.

### Genetic testing

**Not applicable to the host.** No WGS, WES, gene panel, single-gene test, chromosomal microarray, karyotype, FISH, mtDNA, or repeat-expansion testing has any role. *Pathogen* sequencing (`hsp65`, `rpoB`, targeted NGS, metagenomic NGS) is the relevant molecular testing and should be curated under diagnostics, not under genetic testing.

### Omics-based diagnostics

Targeted NGS is the one omics modality with a 2025 diagnostic evaluation (PMID:40833738); it is a JAMA Dermatology research letter, so extract its sensitivity and specificity from the full text before curating numbers. Proteomic, metabolomic, epigenomic, and liquid-biopsy diagnostics: none.

### Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria**. Diagnosis rests on the triad of a compatible acral lesion, an aquatic exposure history within nine months, and microbiological or molecular confirmation. The pragmatic rule:

> "Careful patient's history collection, high clinical suspicion and appropriate sample (e.g. cutaneous biopsy) for microbiological culture are crucial for a timely diagnosis." **[A]** — PMID:35864075

**Differential diagnosis**, with the distinguishing feature in each case:

| Alternative | Distinguishing feature |
|---|---|
| Sporotrichosis (*Sporothrix*) | fungal culture; soil/plant exposure; the classic sporotrichoid mimic |
| Nocardiosis | branching filamentous GPR; modified AFB |
| Cutaneous leishmaniasis | travel history; Giemsa amastigotes |
| Cutaneous tuberculosis | *M. tuberculosis* on culture/PCR; note IGRA cannot separate them |
| Other NTM (*M. abscessus*, *M. chelonae*, *M. fortuitum*, *M. ulcerans*) | species identification; *M. abscessus* is far more drug-resistant |
| Sweet's syndrome / neutrophilic dermatosis | the documented misdiagnosis in PMID:39759953 — biopsy showed neutrophilic dermatosis before AFB were found |
| Pyoderma gangrenosum | steroid response is misleading; consider before immunosuppressing |
| Foreign-body granuloma, sea-urchin or fish-sting granuloma | history and imaging |
| Squamous cell carcinoma, keratoacanthoma | verrucous lesions can mimic; biopsy |

Two of these are actively dangerous: treating a presumed neutrophilic dermatosis or pyoderma gangrenosum with corticosteroids accelerates *M. marinum* disease, which is precisely the reported trajectory in the bearded-dragon case.

### Screening

Not applicable. There is no asymptomatic carrier state, no newborn or carrier screening, and no basis for population screening. Occupational health education is prevention, not screening.

---

## 11. Outcome / Prognosis

### Survival and mortality

**Mortality from aquarium granuloma is essentially zero** in immunocompetent hosts, and no series in this review reported a disease-attributable death. No 5-year or 10-year survival figures exist because survival is not the relevant endpoint. Death is confined to exceptional disseminated disease in profoundly immunocompromised patients; the bearded-dragon case reached neutropenic sepsis (PMID:39759953). Curate mortality as not established rather than as a number.

### Cure rates

| Cohort | Cure | Notes |
|---|---|---|
| Netherlands, n=40 | 36/40 (90%) | mean 25 weeks; susceptibility-guided |
| France, n=63 | 55/63 (87%) | median 3.5 months; 48% surgery |
| China (Han), n=35 | 29/35 (82.9%) | 6 lost to follow-up |
| USA (Kaiser), n=31 | 22/27 (81%) evaluable | cure or improvement |
| Taiwan, n=27 | 18/27 (67%) | 8 failures, 1 lost |

> "Antibiotic treatment cured 36/40 patients (90%) after a mean treatment duration of 25 weeks. Failure/relapse occurred in 3 patients, and 1 patient was lost to follow-up." **[A]** — PMID:35308482

> "Prolonged and susceptibility-guided treatment results in a 90% cure rate in M. marinum disease." **[A]** — PMID:35308482

### Prognostic factors

**Depth of involvement is the dominant prognostic factor**, and it is the one that survives multivariable framing:

> "Failure was related to deep structure involvement (3 of 45 vs 5 of 18 patients; P =.04) but not to any antibiotic regimen." **[A]** — PMID:12153378

The 2017 review reaches the same conclusion: therapy achieves "successful outcome in most of the skin diseases but less frequently in deep tissue infections" **[A]** (PMID:28387180).

Other factors with supporting data:

- **Treatment duration.** Longer therapy predicted cure in the Taiwanese cohort: "The duration of clarithromycin (147 vs. 28; p = 0.0297), and rifampicin (201 vs. 91; p = 0.0266) treatment in the cured patients was longer than that in the others." **[A]** (PMID:22911774). Read the direction of causality cautiously — failures may have been stopped early *because* they were failing.
- **Surgical debridement.** "Surgical debridement was performed in 10 out of the 18 cured patients, and in 1 of another group (p = 0.0417)." **[A]** (PMID:22911774).
- **In vitro susceptibility, specifically to tetracyclines.** "Tetracycline resistance seemed correlated with poor response to tetracycline monotherapy." **[A]** (PMID:35308482).
- **Immunosuppression** prolongs time to cure (p=0.047; PMID:40535516).

### Morbidity, disability, and complications

Complications: tenosynovitis (the commonest deep complication, 22.2%), septic arthritis, osteomyelitis, bursitis, tendon rupture, scarring and disfigurement of the hand, and — rarely — dissemination. Functional hand morbidity plus a 4–6 month treatment course is the realistic burden.

No ICF-coded disability data, no GBD estimate, and no validated QoL instrument has been applied to this disease. Record the gap.

### Recovery potential

Excellent with appropriate therapy. Recurrence after adequate treatment plus debridement was zero across one year in the Thai tenosynovitis subgroup (PMID:40535516). Prognostic biomarkers: declining T-SPOT.TB spot-forming counts are the only candidate treatment-response biomarker with supporting data (PMID:41147233), and the authors frame it as a "useful reference", not a validated endpoint.

---

## 12. Treatment

### The honest headline

> "The treatment is not standardized, and no randomized control trials have been done." **[A]** — Aubry et al. 2017, PMID:28387180

Every regimen below rests on retrospective cohorts and expert consensus. The 2020 ATS/ERS/ESCMID/IDSA guideline (PMID:32797222, PMID:32636299) covers **NTM pulmonary disease only** and does not address *M. marinum* skin infection; the 2007 ATS/IDSA statement (PMID:17277290) is the guideline document that does. Do not cite the 2020 guideline as the source of a skin-infection recommendation.

### Pharmacotherapy

**Principle:** two active agents, guided by susceptibility testing where available, continued for months, with surgery for deep disease. Monotherapy is used for limited disease but is increasingly discouraged.

> "Therapy is a combination of surgery and antimicrobial agents such as cyclines and rifampin, with successful outcome in most of the skin diseases but less frequently in deep tissue infections." **[A]** — PMID:28387180

> "The treatment is not standardized yet and relies on administration of two active antimycobacterial agents, always guided by antimicrobial susceptibility test on culture, with macrolides and rifampin as pivotal drugs, as well as prompt surgery when feasible." **[A]** — PMID:35864075

> "Two-drug regimens of ethambutol and a macrolide are effective for moderately severe infections. Tetracycline monotherapy in limited disease should be used vigilantly, preferably with proven in vitro susceptibility." **[A]** — PMID:35308482

**Regimens actually used, with frequencies** (China, n=35; PMID:39262684):

| Regimen tier | Share | Composition |
|---|---|---|
| Monotherapy | 9/35 (25.7%) | minocycline 6, clarithromycin 2, doxycycline 1 |
| Dual | 17/35 (48.6%) | clarithromycin+rifampin 13, clarithromycin+minocycline 4 |
| Triple | 9/35 (25.7%) | clarithromycin+rifampin+doxycycline 8, clarithromycin+rifampin+ethambutol 1 |

Agent frequency in that series: clarithromycin 80.0%, rifampin 62.9%, minocycline 28.6%, doxycycline 25.7%. Median duration 4.0 months (IQR 3.0–6.0). In the Netherlands, final regimens were most often ethambutol–macrolide (35%), with monotherapy in 35% and two drugs in 63% (PMID:35308482).

One older comparison favoured the ethambutol–rifampin pair over minocycline, without reaching significance:

> "Treatment with ethambutol plus rifampin appeared more successful (effective in five [100%] of five cases) than minocycline treatment (effective in 10 [71%] of 14 cases), although not significantly so (P = .28)." **[A]** — PMID:8002687

### Antimicrobial susceptibility — and a genuine geographical conflict on doxycycline

Modern, large panel (200 isolates, China):

> "M. marinum demonstrated high susceptibility (82.5%-100%) to clarithromycin, rifampin, rifabutin, moxifloxacin, linezolid, trimethoprim-sulfamethoxazole, with moderate susceptibility to tetracyclines and ciprofloxacin. Ethambutol showed favourable activity against M. marinum with MIC90 of 2 µg/mL." **[A]** — Peng et al. 2025, PMID:41135669

MIC90 values from the French national panel:

> "The 90% minimum inhibitory concentrations of rifampin and rifabutin were far lower (0.5 and 0.06 micro g/mL, respectively) than the 90% minimum inhibitory concentrations of clarithromycin (2 micro g/mL) and the cyclines (minocycline, 4 micro g/mL; and doxycycline, 8 micro g/mL)." **[A]** — PMID:12153378

**The tetracycline discordance is large and should be curated as a real disagreement, not resolved by picking one number.** Three independent panels disagree sharply:

| Panel | Doxycycline susceptibility |
|---|---|
| Taiwan, 30 isolates | **1/30 (3.3%)** |
| Netherlands, 40 isolates | 36% of isolates *resistant* to tetracyclines |
| China, 200 isolates | "moderate" susceptibility to tetracyclines |
| Thailand cohort | doxycycline named among the most effective drugs |

> "All the 30 isolates were susceptible to clarithromycin, amikacin, and linezolid; 29 (96.7%) were susceptible to ethambutol; 28 (93.3%) were susceptible to sulfamethoxazole; and 26 (86.7%) were susceptible to rifampicin. However, only 1 (3.3%) isolate was susceptible to doxycycline." **[A]** — PMID:22911774

Part of this is breakpoint-driven: the Thai study used a CLSI doxycycline breakpoint of ≤1 µg/mL against a French MIC90 of 8 µg/mL, so "resistant" and "effective" can both be defensible statements about the same organism. Curate each panel as its own evidence item with its population and, where known, its breakpoint, rather than asserting a single susceptibility.

Note also that "routine susceptibility testing is not recommended and should be reserved for cases of treatment failure" **[F]** is longstanding advice that the Dutch cohort's tetracycline finding directly challenges. This is a live disagreement worth a `discussions:` entry.

### Suggested NCIT and CHEBI bindings (all resolved in OLS4 this session)

| Treatment | NCIT `treatment_term` | CHEBI/NCIT `therapeutic_agent` |
|---|---|---|
| Combination antimycobacterial therapy | NCIT:C15986 Pharmacotherapy | see below |
| Clarithromycin | NCIT:C15986 | CHEBI:3732 clarithromycin (or NCIT:C1054 Clarithromycin) |
| Rifampicin | NCIT:C15986 | CHEBI:28077 rifampicin (or NCIT:C811 Rifampin) |
| Rifabutin | NCIT:C15986 | CHEBI:45367 rifabutin |
| Ethambutol | NCIT:C15986 | CHEBI:4877 ethambutol (or NCIT:C61755 Ethambutol) |
| Doxycycline | NCIT:C15986 | CHEBI:50845 doxycycline (or NCIT:C457 Doxycycline) |
| Minocycline | NCIT:C15986 | CHEBI:50694 minocycline (or NCIT:C61849 Minocycline) |
| Trimethoprim-sulfamethoxazole | NCIT:C15986 | CHEBI:3770 co-trimoxazole |
| Moxifloxacin | NCIT:C15986 | CHEBI:63611 moxifloxacin |
| Linezolid | NCIT:C15986 | CHEBI:63607 linezolid |
| Amikacin | NCIT:C15986 | CHEBI:2637 amikacin |
| Azithromycin | NCIT:C15986 | CHEBI:2955 azithromycin |
| Surgical debridement | NCIT:C51682 Debridement | — |
| Surgical excision / tenosynovectomy | NCIT:C15329 Surgical Procedure | — |
| Cryosurgery (historical adjunct) | NCIT:C15215 Cryosurgery | — |
| Supportive care | NCIT:C15747 Supportive Care | — |
| Patient/occupational education | NCIT:C16664 Health Education | — |

Drug-class alternatives if a class-level `therapeutic_agent` is wanted: NCIT:C261 Macrolide Antibiotic, NCIT:C1595 Tetracycline Antibiotic, NCIT:C280 Antitubercular Agent. **Caution:** `therapeutic_agent` binds the `ChemicalEntityTerm` enum rooted at NCIT:C1909 (Pharmacologic Substance), and NCIT files some classes elsewhere. Run `just validate-terms` after binding any NCIT class term here rather than trusting this table. `NCIT:C51682` Debridement likewise needs an enum check against the `NCIT:C25218` root before use as a `treatment_term`.

Therapeutic modality for every pharmacological entry here is `SMALL_MOLECULE`; debridement and excision are `SURGERY`. No oligonucleotide, biologic, or delivery-system detail applies.

### Surgery

Adjunctive and often decisive, especially for tenosynovitis. Surgery rates: 48% (France), 28% (Netherlands), 10/18 of cured patients (Taiwan).

> "Surgical debridement combined with oral antibiotics successfully treated all tenosynovitis patients, with no recurrence during the 1-year follow-up." **[A]** — PMID:40535516

### Management of immunosuppression — a treatment decision, not a footnote

Discontinuing or reducing TNF-α inhibitors and other immunosuppressants during antimicrobial therapy is recommended, with the caveat that the evidence base is small (PMID:28387180 **[F]**). The 2026 review "summarize[s] adjustments to immunosuppressive agents for immunocompromised patients with M. marinum infection" **[A]** (PMID:42639276) and is the place to look for current practical guidance. A counterpoint exists in the literature — a report proposing a possible therapeutic role for anti-TNF monoclonal antibodies in *M. marinum* infection — which fits the model's finding that both TNF excess and TNF deficiency are harmful (PMID:23582643). Curate that as a genuine open question rather than an error.

### Advanced therapeutics, pharmacogenomics, experimental treatment

- **Gene therapy, cell therapy, RNA therapeutics, targeted therapy, immunotherapy:** none for this disease. Not applicable.
- **Pharmacogenomics:** no PharmGKB/CPIC guidance specific to this indication. Generic considerations apply — rifampicin is a potent CYP3A4 inducer with major interaction potential, and clarithromycin is a CYP3A4 inhibitor; that interaction is pharmacological rather than pharmacogenomic.
- **Host-directed therapy — the most interesting experimental direction, and it is preclinical.** The zebrafish work identifies repurposable drugs that block TNF-driven necrosis: alisporivir (cyclophilin D), desipramine (acid sphingomyelinase), and metformin (complex I).

  > "Similarly, the cyclophilin D-inhibiting drug alisporivir and the acid sphingomyelinase-inactivating drug, desipramine, synergize to reverse susceptibility, suggesting the therapeutic potential of these orally active drugs against tuberculosis and possibly other TNF-mediated diseases." **[A]** — PMID:23582643

  > "The complex I inhibitor metformin, a widely used antidiabetic drug, prevents TNF-induced mROS and necrosis of Mycobacterium tuberculosis-infected zebrafish and human macrophages; metformin may therefore be useful in tuberculosis therapy." **[A]** — PMID:35737799

  Both are framed for **tuberculosis**, not aquarium granuloma. Record them as model-derived host-directed candidates with an explicit `HUMAN_MODEL_MISMATCH` framing; do not curate them as treatments for this disease.

- **Clinical trials:** no interventional trial of aquarium granuloma treatment was identified in this session. No NCT or ICTRP identifier should be curated without a targeted registry search.

### Adverse events

> "Adverse reactions, most of which were gastrointestinal, occurred in five patients (18%)." **[A]** — PMID:8002687

Regimen changes are common — the initial regimen was modified in 22/63 (35%) of the French cohort (PMID:12153378).

### Treatment algorithm (synthesis; no formal published algorithm exists)

1. Biopsy for histology **and** culture, specifying 30 °C incubation; add tissue PCR or targeted NGS.
2. Limited superficial disease: two active oral agents, commonly clarithromycin plus either rifampicin or ethambutol; a single tetracycline only with documented in vitro susceptibility.
3. Moderate disease: ethambutol plus a macrolide.
4. Deep disease (tenosynovitis, arthritis, osteomyelitis): three agents including rifampicin, plus surgical debridement.
5. Continue 1–2 months beyond clinical resolution; expect total 4–6 months, longer in immunosuppressed patients.
6. Stop or reduce TNF inhibitors and other immunosuppressants during therapy.
7. Reserve susceptibility testing for failure — but obtain it early where tetracycline monotherapy is contemplated.

---

## 13. Prevention

### Primary prevention

This is the level that matters, because primary prevention is nearly fully effective and rests on interrupting one necessary step: skin breach plus aquatic contact.

> "Prevention can be useful with hand protection recommendations for professionals and all persons manipulating fishes or fish tank water and use of alcohol disinfection after contact." **[A]** — Aubry et al. 2017, PMID:28387180

Concrete measures:

- Waterproof gloves for aquarium cleaning, fish handling, and seafood preparation. Long gloves for tank work.
- Do not put a hand with a cut, abrasion, or eczematous skin into tank water; cover breaks with a waterproof dressing.
- Alcohol-based hand disinfection immediately after contact.
- Chlorinate and maintain public and domestic swimming pools — the intervention that historically removed the swimming-pool form.
- Targeted risk counselling for people on TNF inhibitors or other immunosuppressants who keep fish, where the downside is deep or disseminated disease rather than a nodule.
- Occupational hygiene in ornamental-fish retail, aquaculture, and fish processing.

Suggested NCIT bindings: NCIT:C16664 Health Education, NCIT:C18975 Public Health Education.

### Secondary prevention

Early recognition is the whole of secondary prevention, and the actionable form of it is a history question rather than a test: ask about aquatic exposure in the preceding **nine months** in any patient with an atypical, non-resolving acral nodule or plaque (PMID:10987702). The second element is a laboratory instruction — request 30 °C mycobacterial culture on the biopsy. Together these two habits address the 3–6 month median diagnostic delay.

A specific, avoidable harm to flag: **do not inject a corticosteroid into an undiagnosed acral nodule or an unexplained trigger finger in someone with aquatic exposure.** Intralesional triamcinolone preceded lesion onset in 11.1% of the Thai cohort, and prior steroid injection at the site was associated with tenosynovitis (p=0.007) (PMID:40535516).

### Tertiary prevention

Adequate duration of two-drug therapy, timely surgical debridement for deep disease, susceptibility-guided regimen selection, and withdrawal of immunosuppression during treatment. Together these carry cure rates to 87–90% and prevent the tenosynovitis-to-osteomyelitis progression.

### Immunization, genetic screening, counselling, prophylaxis

- **Vaccination:** no vaccine exists or is in development for human *M. marinum* disease. Not applicable. A zebrafish mRNA vaccine study exists (GEO GSE270105, GSE269547) but is a tuberculosis-model experiment, not a human product.
- **Genetic screening, carrier screening, PGD, prenatal testing, genetic counselling:** not applicable.
- **Antimicrobial prophylaxis after fish-related injury:** no evidence base; not recommended. Wound cleaning and observation are the practice.
- **Risk stratification:** informal only — immunosuppressed aquarists are the group worth counselling.

### Public health and environmental interventions

Pool chlorination and maintenance standards; hygiene guidance at point of sale for ornamental fish; aquaculture biosecurity and culling of infected stock (which protects fish health and reduces the human exposure reservoir); no notifiable-disease reporting requirement in most jurisdictions.

---

## 14. Other Species / Natural Disease

This is unusually rich for a human dermatological infection, because the human disease is a spillover from a major fish disease, and the fish disease is the source of the mechanism in §6.

### Taxonomy of susceptible hosts

*M. marinum* (NCBITaxon:1781) has been isolated from "mammals, fish, amphibians, reptiles, birds, invertebrates, and protists" **[F]** (PMID:29493404). Host range is exceptionally broad, which the genome explains — *M. marinum* "has maintained a large genome so as to retain the capacity for environmental survival while becoming a broad host range pathogen" **[A]** (PMID:18403782).

Verified taxonomy identifiers for the entities relevant to this entry:

| Organism | NCBITaxon |
|---|---|
| *Mycobacterium marinum* | NCBITaxon:1781 |
| *Danio rerio* (zebrafish) | NCBITaxon:7955 |
| *Mus musculus* | NCBITaxon:10090 |
| *Mycobacterium tuberculosis* | NCBITaxon:1773 |
| *Mycobacterium ulcerans* | NCBITaxon:1809 |

### Natural disease in fish — piscine mycobacteriosis ("fish tuberculosis")

> "Mycobacterium marinum is an opportunistic pathogen inducing infection in fresh and marine water fish. This pathogen causes necrotizing granuloma like tuberculosis, morbidity and mortality in fish." **[A]** — Hashish et al. 2018, PMID:29493404

> "Mycobacterium species have long been recognized as a significant source of morbidity and mortality in finfish aquaculture, as well as in wild finfishes." **[F]** — search snippet, fish mycobacteriosis review

All fish species should be considered susceptible; documented outbreaks include striped bass in the USA, sturgeon in China, and captive-bred Australian lungfish **[F]**. Clinical signs in fish: emaciation, skin ulceration, scale loss, spinal deformity, exophthalmos, and disseminated visceral granulomas. In fish, the route is oral and branchial rather than percutaneous: "The primary route of infection is the oral one via consumption of infected dead fish, contact with affected fish skin or through gills" **[F]**.

Reptile infection is established, and is the source of the first reported non-aquatic human transmission (bearded dragon, PMID:39759953).

### Veterinary relevance

Substantial: economic losses in ornamental-fish and food-fish aquaculture, and no practical treatment for infected stock, so management is culling and biosecurity. Nine different NTM species were isolated from sixteen aquatic animals including fish, frogs, and a crocodile in one South African farmed-animal survey **[F]**.

### Comparative biology and evolutionary conservation

The comparative pathology is the reason this organism became a model system. Zebrafish infected with *M. marinum* develop caseating granulomas that are structurally homologous to human tuberculous granulomas:

> "Zebrafish tuberculous granulomas undergo caseous necrosis, similar to human tuberculous granulomas." **[A]** — Swaim et al. 2006, PMID:17057088

The conserved virulence machinery spans the species: "The cell wall-associated lipid phthiocerol dimycocerosates, phenolic glycolipids and ESAT-6 secretion system 1 (ESX-1) are the conserved virulence determinant of the organism" **[A]** (PMID:29493404). The RD1/ESX-1 locus is syntenic between *M. marinum* and *M. tuberculosis*, with EsxB and EsxA sharing 97% and 91% amino-acid identity respectively **[F]** — a figure to verify against the primary ESX-1 review before curating.

One important divergence: zebrafish granulomas "contain few lymphocytes" in contrast to mammalian tuberculous granulomas **[A]** (PMID:17057088), even though adaptive immunity is required for control. This is the key fidelity caveat for any model link.

### Zoonotic potential and cross-species susceptibility

Zoonotic, unidirectionally: fish, amphibians, and reptiles to humans, by percutaneous inoculation. There is **no** human-to-human and no human-to-animal transmission of concern. Not a foodborne zoonosis — eating fish does not transmit it; handling and injury do. Immunocompromised people are the group for whom the zoonotic risk is materially higher.

> "Mycobacteria infecting fishes include zoonotic pathogens that can cause protracted illness, especially in immunocompromised individuals." **[F]** — search snippet, fish mycobacteriosis review

### Orthologous genes

Not applicable in the usual sense — there is no human disease gene to find an ortholog of. The relevant cross-species gene mapping is of *host defence* genes used in the model: zebrafish *tnfa*, *tnfr1*, *tnfr2*, *rag1*, *pycard*, *spp1*, *apodb*, and *hif1a*. If a `genetic:` or `animal_models` section names these, use ZFIN identifiers, and note that dismech's gene descriptors are HGNC-bound, so a zebrafish gene cannot be bound the same way a human gene is.

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*, NCBITaxon:7955) — the flagship model

This is a **natural-host** model, not an engineered one, which is why its fidelity is unusual:

> "The zebrafish, a genetically tractable model vertebrate, is naturally susceptible to tuberculosis caused by Mycobacterium marinum, a close genetic relative of the causative agent of human tuberculosis, Mycobacterium tuberculosis." **[A]** — PMID:17057088

**Two distinct preparations, and they answer different questions.**

*Larval/embryo model* — optically transparent, innate immunity only, permits intravital microscopy of single macrophages. This is where granuloma initiation, macrophage recruitment, and necroptosis were worked out (PMID:19135887, PMID:20007864, PMID:18691913, PMID:23582643, PMID:24336213, PMID:35737799).

*Adult model* — innate plus adaptive immunity, caseating granulomas, dose-dependent acute versus chronic disease:

> "Intraperitoneal injection of five organisms produces persistent granulomatous tuberculosis, while the injection of approximately 9,000 organisms leads to acute, fulminant disease. Bacterial burden, extent of disease, pathology, and host mortality progress in a time- and dose-dependent fashion." **[A]** — PMID:17057088

**Genetic models available:** *rag1* mutant (adaptive-immunity-deficient, hypersusceptible), *tnfa* / *tnfr1* / *tnfr2* mutants and morphants, *pycard* (inflammasome) mutants, *spp1* (osteopontin) ablation, *apodb* mutants, *hif1a* manipulation, plus transgenic macrophage and neutrophil reporter lines. On the pathogen side: ΔRD1 and ESX-1 substrate mutants (e.g. *espK*::tn).

**Phenotype recapitulation — what it captures:** granuloma formation and maturation; caseous necrosis; macrophage-centred pathogenesis; ESX-1 dependence; dose-dependent acute versus chronic course; adaptive-immunity dependence; TNF's dual protective and pathogenic roles.

**Limitations — what it does not capture.** These matter for any `modeled_mechanisms` link and belong in `divergences`:

- **Few lymphocytes in lesions**, unlike mammalian granulomas (PMID:17057088) — a `POPULATION_MISMATCH`/`INCOMPLETE_PHENOTYPE`-shaped gap.
- **The model is a systemic/visceral tuberculosis model, not a cutaneous inoculation model.** Infection is intraperitoneal or by caudal-vein injection, and the disease is disseminated and lethal. Human aquarium granuloma is a localized, self-limited-to-the-skin, non-lethal infection. This is the single most important caveat: the zebrafish model reproduces *granuloma biology* faithfully while reproducing *this disease's clinical form* hardly at all.
- **No thermal restriction.** Zebrafish are housed near the organism's growth optimum, so the temperature constraint that shapes the entire human anatomical distribution is absent.
- **ΔRD1 produces "nonnecrotizing, loose macrophage aggregates"** (PMID:17057088), a useful negative control but a divergence from any wild-type human lesion.
- Fidelity for a human *cutaneous* pathophysiology node should be recorded as `MODERATE` at best, with `relationship: PARTIALLY_RECAPITULATES`, and `model_scale` set to `CELLULAR` or `MOLECULAR` for the larval intravital work — which makes most links to a tissue-level node an **upward extrapolation** requiring `limitations`.

### Mouse (*Mus musculus*, NCBITaxon:10090)

The mouse tail-lesion model exploits the same thermal biology that shapes human disease: the tail is cool enough to support *M. marinum* growth, which makes it a better anatomical analogue of the human acral lesion than any zebrafish preparation. Recent single-cell work used mice infected with wild-type, *espK*::tn, and ΔRD1 *M. marinum*, sorting infected and bystander monocytes 14 days post infection (GEO GSE235124). Mice are not natural hosts and control the infection well, which limits chronic-disease modelling.

### In vitro and cellular systems

Human THP-1-derived macrophages infected with mycobacteria (GEO GSE328953, 15 samples) — the only human-cell dataset found. Primary human monocyte-derived macrophages are used in the TNF/mROS work (PMID:35737799 tested human macrophages alongside zebrafish). No organoid, iPSC-derived, or organ-on-chip model of *M. marinum* skin infection was identified; a human skin-equivalent model would be the obvious gap to name in a `discussions:` entry.

### Research applications

Granuloma initiation and maturation; macrophage–pathogen interaction and immune evasion by cell-wall lipids; necroptosis and its pharmacological blockade; host-directed therapy screening (alisporivir, desipramine, metformin); ESX-1 secretion biology; inflammasome and neutrophil contributions to necrosis; antimycobacterial drug screening; TB vaccine candidate testing.

### Resources

ZFIN (zebrafish genes, alleles, and lines), Alliance of Genome Resources, MGI and IMSR (mouse), IMPC/KOMP (mouse knockouts), Cellosaurus and ATCC (cell lines), GEO (the eleven datasets listed in §6).

---

## Curation Notes for the dismech Entry

**Ontology bindings — status.** Every CURIE in this report was resolved in this session against OLS4 (HP, GO, CL, UBERON, CHEBI, NCIT, ECTO, MONDO) or NCBI (Taxonomy, ICD-10-CM via NLM Clinical Tables). The working tree already carries `MONDO:0043314` and `NCBITaxon:1781` in `cache/mondo/terms.csv` and `cache/ncbitaxon/terms.csv`. Two bindings still need verification before use: the GO cellular-component terms for mitochondrion and phagosome (§7) were **not** looked up, and every NCIT term intended for a `treatment_term` or `therapeutic_agent` slot needs `just validate-terms` to confirm dynamic-enum membership (NCIT:C51682 Debridement against the `NCIT:C25218` root; any NCIT drug class against `NCIT:C1909`).

**Recorded negative searches** (so the `notes` can state them rather than assert absence): ECTO has no term for *M. marinum* exposure, aquarium exposure, seafood exposure, or wound exposure — queries run were `Mycobacterium marinum`, `marinum`, `aquarium`, `seafood`, `wound`, `exposure to fish`, `exposure to bacterium`, `exposure to Mycobacterium`; usable terms found were ECTO:9000156 and ECTO:5000002. HPO has no term for a sporotrichoid pattern or for lymphangitis — queries run were `Sporotrichoid` and `Lymphangitis`.

**Three deliberate disagreements to curate as such**, rather than resolving by preference: the doxycycline susceptibility conflict across four panels (§12), the sex-ratio reversal between the Chinese and Thai series (§9), and whether routine susceptibility testing is warranted (§12). Each is a real divergence in the literature with a plausible methodological explanation, and flattening any of them would misrepresent the evidence.

**The dominant model-fidelity caveat**, which should appear as a `HUMAN_MODEL_MISMATCH` discussion rather than buried in a `limitations` string: the mechanism in §6 steps 4–8 is known in molecular detail from zebrafish infected with this exact organism, but as *disseminated visceral tuberculosis*, not as a localized cool-skin granuloma. The pathogen is identical; the disease is not.

**Sources**

- [Aubry A et al. *Mycobacterium marinum*. Microbiol Spectr 2017 — PMID:28387180](https://pubmed.ncbi.nlm.nih.gov/28387180/)
- [Aubry A et al. Sixty-three cases of *Mycobacterium marinum* infection. Arch Intern Med 2002 — PMID:12153378](https://pubmed.ncbi.nlm.nih.gov/12153378/)
- [Canetti D et al. *Mycobacterium marinum*: a brief update for clinical purposes. Eur J Intern Med 2022 — PMID:35864075](https://pubmed.ncbi.nlm.nih.gov/35864075/)
- [Hendrikx L et al. Treatment and Outcome of Culture-Confirmed *Mycobacterium marinum* Disease. Open Forum Infect Dis 2022 — PMID:35308482](https://academic.oup.com/ofid/article/9/4/ofac077/6549659)
- [Jirawattanadon P et al. Cutaneous Infection Caused by *Mycobacterium marinum* in Thailand. Health Sci Rep 2025 — PMID:40535516](https://pmc.ncbi.nlm.nih.gov/articles/PMC12174614/)
- [A Series of 35 Cutaneous Infections Caused by *Mycobacterium marinum* in Han Chinese Population. J Trop Med 2023 — PMID:39262684](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11390208/)
- [Jernigan JA, Farr BM. Incubation period and sources of exposure. Clin Infect Dis 2000 — PMID:10987702](https://pubmed.ncbi.nlm.nih.gov/10987702/)
- [Edelstein H. *Mycobacterium marinum* skin infections. Report of 31 cases. Arch Intern Med 1994 — PMID:8002687](https://pubmed.ncbi.nlm.nih.gov/8002687/)
- [Wu TS et al. Fish tank granuloma caused by *Mycobacterium marinum*. PLoS One 2012 — PMID:22911774](https://pubmed.ncbi.nlm.nih.gov/22911774/)
- [Travis WD et al. The histopathologic spectrum in *Mycobacterium marinum* infection. Arch Pathol Lab Med 1985 — PMID:3840985](https://pubmed.ncbi.nlm.nih.gov/3840985/)
- [Cen C et al. Application of T-SPOT.TB in cutaneous *M. marinum* infections. Acta Derm Venereol 2025 — PMID:41147233](https://pmc.ncbi.nlm.nih.gov/articles/PMC12579364/)
- [Peng J et al. Antimicrobial susceptibility patterns and genotypic characteristics. J Glob Antimicrob Resist 2025 — PMID:41135669](https://pubmed.ncbi.nlm.nih.gov/41135669/)
- [Gu AK et al. Targeted Next-Generation Sequencing for Etiologic Diagnosis. JAMA Dermatol 2025 — PMID:40833738](https://pmc.ncbi.nlm.nih.gov/articles/PMC12368782/)
- [Yang X et al. *Mycobacterium marinum* Infection: Case Report and 5-Year Systematic Review (2021–2025). Clin Cosmet Investig Dermatol 2026 — PMID:42639276](https://pmc.ncbi.nlm.nih.gov/articles/PMC13502333/)
- [Kravvas G et al. A Novel, Nonaquatic Zoonotic Transmission of *Mycobacterium marinum*. Case Rep Infect Dis 2024 — PMID:39759953](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11698610/)
- [Jagadeesan S et al. Cutaneous infection due to *Mycobacterium marinum*: four cases from Kerala. Trop Med Int Health 2024 — PMID:39039624](https://onlinelibrary.wiley.com/doi/10.1111/tmi.14033)
- [Mycobacterium marinum Cutaneous Infection: Three Cases and Literature Review. Cureus 2022 — PMID:36579262](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9780696/)
- [Stinear TP et al. Complete genome sequence of *Mycobacterium marinum*. Genome Res 2008 — PMID:18403782](https://genome.cshlp.org/content/18/5/729)
- [Davis JM, Ramakrishnan L. The role of the granuloma. Cell 2009 — PMID:19135887](https://pubmed.ncbi.nlm.nih.gov/19135887/)
- [Volkman HE et al. Tuberculous granuloma induction via ESAT-6/MMP9. Science 2010 — PMID:20007864](https://pubmed.ncbi.nlm.nih.gov/20007864/)
- [Clay H et al. TNF signaling mediates resistance to mycobacteria. Immunity 2008 — PMID:18691913](https://pubmed.ncbi.nlm.nih.gov/18691913/)
- [Roca FJ, Ramakrishnan L. TNF dually mediates resistance and susceptibility. Cell 2013 — PMID:23582643](https://pubmed.ncbi.nlm.nih.gov/23582643/)
- [Roca FJ et al. TNF induces pathogenic mitochondrial ROS through reverse electron transport. Science 2022 — PMID:35737799](https://pubmed.ncbi.nlm.nih.gov/35737799/)
- [Cambier CJ et al. Mycobacteria manipulate macrophage recruitment. Nature 2014 — PMID:24336213](https://pubmed.ncbi.nlm.nih.gov/24336213/)
- [Swaim LE et al. *M. marinum* infection of adult zebrafish. Infect Immun 2006 — PMID:17057088](https://journals.asm.org/doi/10.1128/iai.00887-06)
- [Tobin DM et al. LTA4H and inflammation in mycobacterial disease. Cell 2012 — PMID:22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)
- [Hashish E et al. *Mycobacterium marinum* infection in fish and man. Vet Q 2018 — PMID:29493404](https://www.tandfonline.com/doi/full/10.1080/01652176.2018.1447171)
- [Griffith DE et al. ATS/IDSA statement on nontuberculous mycobacterial diseases. Am J Respir Crit Care Med 2007 — PMID:17277290](https://pubmed.ncbi.nlm.nih.gov/17277290/)
- [Daley CL et al. Treatment of NTM Pulmonary Disease: ATS/ERS/ESCMID/IDSA guideline. Clin Infect Dis 2020 — PMID:32797222](https://pubmed.ncbi.nlm.nih.gov/32797222/)
- [Osteomyelitis Infection of *Mycobacterium marinum*: Case Report and Review — PMID:25664190](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4312609/)
- [Mycobacterium marinum as a model for mycobacterial pathogenesis. J Bacteriol 2025](https://journals.asm.org/doi/full/10.1128/jb.00047-25)
- [Modeling Tubercular ESX-1 Secretion Using *Mycobacterium marinum*. Microbiol Mol Biol Rev](https://journals.asm.org/doi/full/10.1128/mmbr.00082-19)
- [Mycobacteriosis in fishes: A review. Vet J](https://www.sciencedirect.com/science/article/abs/pii/S109002330800186X)
- [MONDO:0043314, EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0043314)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 55 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 55 |
| On topic | 40 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 94 |
| Resolved | 94 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 34 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0043314` (6 mentions) - the report calls it "MONDO"; MONDO calls it **aquarium granuloma**
- `NCBITaxon:1781` (6 mentions) - the report calls it "NCBI Taxonomy (agent)", "M. marinum", "Mycobacterium marinum"; NCBITaxon calls it **Mycobacterium marinum**
- `UBERON:0001473` (2 mentions) - the report calls it "Egress of infected macrophages into dermal lymphatics", "lymphatic vessel"; UBERON calls it **lymphatic vessel**
- `NCIT:C15986` (12 mentions) - the report calls it "Clarithromycin", "Rifampicin", "Rifabutin", "Ethambutol", "Doxycycline", "Minocycline", "Trimethoprim-sulfamethoxazole", "Moxifloxacin", "Linezolid", "Amikacin", "Azithromycin"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0032283` (1 mention) - the report calls it "Disseminated NTM infection"; HP calls it **Disseminated non-tuberculous mycobacterial infection**, and lists "Disseminated NTM infection" among its other names
- `NCBITaxon:1773` (2 mentions) - the report calls it "M. tuberculosis", "Mycobacterium tuberculosis"; NCBITaxon calls it **Mycobacterium tuberculosis**, and lists "Bacterium tuberculosis" among its other names
- `NCBITaxon:1809` (2 mentions) - the report calls it "M. ulcerans", "Mycobacterium ulcerans"; NCBITaxon calls it **Mycobacterium ulcerans**
- `UBERON:0000304` (2 mentions) - the report calls it "Contiguous extension to tendon sheath", "tendon sheath"; UBERON calls it **tendon sheath**, and lists "synovial tendon sheath" among its other names
- `GO:0032760` (1 mention) - the report calls it "Positive regulation of TNF production"; GO calls it **positive regulation of tumor necrosis factor production**, and lists "positive regulation of TNF production" among its other names
- `NCBITaxon:7955` (2 mentions) - the report calls it "Danio rerio* (zebrafish)"; NCBITaxon calls it **Danio rerio**, and lists "Danio rerio frankei" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:1781` - called "NCBI Taxonomy (agent)", "M. marinum", "Mycobacterium marinum"
- `NCBITaxon:1773` - called "M. tuberculosis", "Mycobacterium tuberculosis"
- `NCBITaxon:1809` - called "M. ulcerans", "Mycobacterium ulcerans"
- `UBERON:0001473` - called "Egress of infected macrophages into dermal lymphatics", "lymphatic vessel"
- `UBERON:0000304` - called "Contiguous extension to tendon sheath", "tendon sheath"
- `NCIT:C15986` - called "Clarithromycin", "Rifampicin", "Rifabutin", "Ethambutol", "Doxycycline", "Minocycline", "Trimethoprim-sulfamethoxazole", "Moxifloxacin", "Linezolid", "Amikacin", "Azithromycin"