---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:46:53.886733'
end_time: '2026-10-01T10:51:31.901740'
duration_seconds: 278.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability X-linked 93
  mondo_id: MONDO:0010393
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 21
  total_cost_usd: 2.0270526
  session_id: a39f5b48-c084-4889-aeb4-75329a1210eb
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
citation_count: 28
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 5
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:17668385
  - PMID:36414205
  relevance_assessed: 22
  on_topic: 15
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 56
  verified: 56
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: DOID:0112045
    reported_labels:
    - GlyCosmos
    ontology_label: non-syndromic X-linked intellectual disability 93
  - term_id: HP:0000256
    reported_labels:
    - Macrocephaly (postnatal; mean OFC +2.8 SD)
    ontology_label: Macrocephaly
  - term_id: HP:0001513
    reported_labels:
    - Obesity (mean BMI +2.0 SD)
    ontology_label: Obesity
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability X-linked 93
- **MONDO ID:** MONDO:0010393 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability X-linked 93** covering all of the
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

Use E-utilities directly.

Now abstracts for the key papers.

I've collected the key literature and checked HPO IDs against the local cache. Next I'm looking up the remaining ontology IDs, then I'll write the report.

# Intellectual Disability, X-linked 93 (MRX93 / XLID93; BRWD3-related XLID): Research Report

**Target:** MONDO:0010393 · Category: Mendelian · Report date: 2026-10-01

**About the sources.** Abstracts were pulled from PubMed E-utilities through a summarizing fetch tool. The abstracts for PMIDs 17668385, 24462886, 30628072, 31714006 and 36414205 came back in full and look verbatim. A few others were partly paraphrased: 16094372, 15543602, 26323392, 30086552, 38751117 and 40282429. Before any snippet goes into the KB, run `just fetch-reference PMID:<id>` and copy the quote from `references_cache/`. Inline quotation marks that the tool added inside some abstracts (e.g. in 37722046 and 25666827) are not part of the source. HPO, GO, CL, UBERON and NCIT IDs below were checked against this repo's `cache/*/terms.csv` unless marked **[lookup needed]**.

---

## Summary

- **The disease.** XLID93 is X-linked intellectual disability caused by hemizygous loss-of-function variants in **BRWD3** (hgnc:17342, Xq21.1).
- **Core features in males.** Mild-to-moderate intellectual disability (ID), speech delay, postnatal macrocephaly, obesity and a recognizable face. The face includes a prominent or broad forehead, large or cupped ears, a tall or pointed chin and prognathism.
- **"Non-syndromic" is a misnomer.** OMIM/MONDO originally filed it as non-syndromic. The case series now describe a reproducible overgrowth–ID (OGID) syndrome.
- **Size of the literature.** About 45 published individuals (43 males, 2 females) in the 2023 meta-analysis (PMID:36414205). At least 5 females in total by 2026 (PMID:42298746).
- **Mechanism (proposed).** BRWD3 is a chromatin reader (two bromodomains plus WD40 repeats). It acts as a substrate receptor (DCAF) for the CUL4–DDB1 E3 ubiquitin ligase. Its best-characterized molecular functions come from *Drosophila* and cell work:
  - degrading the H3K4 demethylase KDM5;
  - restraining HIRA/YEM-mediated deposition of histone H3.3.
- **What is not shown.** No human tissue, iPSC or mouse study of the disease mechanism has been found.

---

## 1. Disease information

**Overview.** "In the course of systematic screening of the X-chromosome coding sequences in 250 families with nonsyndromic X-linked mental retardation (XLMR), two families were identified with truncating mutations in BRWD3… Affected males have macrocephaly with a prominent forehead, large cupped ears, and mild-to-moderate intellectual disability." (PMID:17668385, Field et al., *Am J Hum Genet* 2007; human clinical)

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0010393 "intellectual disability, X-linked 93" (parent MONDO:0019181 non-syndromic X-linked ID) |
| OMIM phenotype | #300659 (XLID93), cited in PMID:42298746 |
| OMIM gene | *300553 BRWD3 |
| DOID | DOID:0112045 "non-syndromic X-linked intellectual disability 93" |
| Gene | hgnc:17342 BRWD3 · Entrez 254065 · Ensembl ENSG00000165288 · UniProt Q6RI45 |
| ClinGen | BRWD3 is **Definitive** for *X-linked syndromic intellectual disability* (MONDO:0020119), from the Syndromic Disorders GCEP. **This is not MONDO:0010393** (see §4). |
| Orphanet / ICD | No disease-specific ORPHA code was confirmed; the orpha.net page was blocked. Specific ICD-10/11 codes are not applicable: it falls under the general X-linked ID codes. **[lookup needed]** |
| GeneReviews | **No chapter.** Confirmed against the repo's `cache/bookshelf/genereviews.csv`, where the only XLID match is ATR-X. |

**Synonyms** (from the MONDO stub): MRX93; mental retardation, X-linked 93; intellectual developmental disorder, X-linked 93; intellectual disability / mental retardation, X-linked, with macrocephaly; BRWD3 non-syndromic X-linked ID; XMR93 syndrome; XLID-BRWD3-related syndrome.

**Data basis.** All information is aggregated from case series and case reports. There are no EHR or registry data.

**Lump/split note for curators.** The stub records `entry_type: DISEASE`, decided in dismech#12227. MRX93 was declined as a subtype row of `Non-Syndromic_X-Linked_Intellectual_Disability` because the phenotype is reproducibly syndromic.

## 2. Etiology

- **Cause.** Germline, hemizygous (males) loss-of-function variants in BRWD3:
  - nonsense, frameshift and canonical-splice variants;
  - intragenic or whole-gene deletions.
- **Haploinsufficiency (loss of function) is the established mechanism.** "Our patient confirms that the haploinsufficiency due to BRWD3 deletion is a causal genetic mechanism" (PMID:38813790; the 586 kb deletion contained only BRWD3).
- **Inheritance pattern.** "Among the 28 variants with available segregation reported, 19 were inherited from unaffected mothers and 9 were de novo." (PMID:36414205)
- **Environmental risk or protective factors and gene–environment interactions.** None reported; not applicable.
- **Modifiers.**
  - **X-inactivation skewing** modifies severity in heterozygous females (PMID:42298746).
  - **Variant class or position may modify phenotype.** Missense variants in the WD40 repeats and bromodomain have been associated with X-linked partial epilepsy *without* ID (PMID:36514184). This is a single Chinese cohort, all variants maternally inherited, so treat it as an allelic or uncertain association rather than XLID93 itself.

## 3. Phenotypes

The main frequency sources are:
- (a) Grotto 2014, n = 9 (PMID:24462886);
- (b) Ostrowski 2019, 17 males (PMID:31714006);
- (c) Delanne 2023 meta-analysis, 43 males and 2 females (PMID:36414205).

| Phenotype | HPO | Frequency (males) | Source |
|---|---|---|---|
| Intellectual disability (mild 35%, moderate 65%) | HP:0001249; mild/moderate child terms **[lookup needed]** | 39/39 | (c), (b) |
| Delayed speech and language development | HP:0000750 | 24/25 | (c) |
| Macrocephaly (postnatal; mean OFC +2.8 SD) | HP:0000256 | 28/35 | (c), (b) |
| Prominent forehead | HP:0011220 | 18/25 | (c) |
| Broad forehead | HP:0000337 | shared feature | (b) |
| Large ears / cupped ears | HP:0000400 Macrotia; HP:0000378 Cupped ear | 14/26 | (c), PMID:17668385 |
| Obesity (mean BMI +2.0 SD) | HP:0001513 | 12/27 | (c), (b) |
| Tall stature (mean height +1.3 SD; overgrowth) | HP:0000098; HP:0001548 | mild trend | (b), PMID:30628072 |
| Tall chin / pointed chin | HP:0400000; HP:0000307 | shared | (b), (a) |
| Prognathism | HP:0000303 Mandibular prognathia | shared | (b) |
| Prominent supraorbital ridges | HP:0000336 | shared | (b) |
| Deeply set eye | HP:0000490 | reported | (a) |
| Behavioral abnormality (aggression, ADHD, ASD) | HP:0000718; HP:0007018; HP:0000729 | 75% (b); 7/8 (a) | (a), (b) |
| Broad hands and feet | HP:0001769 Broad foot; broad hand **[lookup needed]** | 6/6 | (a) |
| Skeletal: pes planus, scoliosis, kyphosis, cubitus valgus | HP:0001763; HP:0002650; HP:0002808; HP:0002967 | 7/7 (any) | (a) |
| Cryptorchidism | HP:0000028 | <30% | (b) |
| Neonatal hypotonia | HP:0001319 | <30% | (b) |
| Joint hypermobility (small joints) | HP:0001382 | <30% | (b) |
| Seizure | HP:0001250 | 4/41 males; 2/2 females | (c) |

**Key quotes**

- (a) "The main symptoms are mild to moderate intellectual disability (n = 9/9) with speech delay (n = 8/8), behavioral disturbances (n = 7/8), macrocephaly (n = 7/9), dysmorphic facial features (n = 9/9)…"
- (b) "Mean head circumference was +2.8 SD… and mean BMI was +2.0 SD (in the context of a mean height of +1.3 SD), indicating a predominant macrocephaly/obesity phenotype."
- (c) "The most common features in males… included ID (39/39 males), speech delay (24/25 males), postnatal macrocephaly (28/35 males) with prominent forehead (18/25 males) and large ears (14/26 males), and obesity (12/27 males)."

**Onset, course and quality of life**
- Onset is congenital or infantile, recognized through developmental delay. Macrocephaly is postnatal.
- The course is static (non-progressive neurodevelopmental).
- No quality-of-life instrument data exist. The main burdens are the ID and the behavioral disorder.

**Females.** Across 5 reported females: developmental delay 60%, neurological signs 60%, OFC above the 95th centile 60%, facial features 40%. Overall they are milder than males, and severity tracks the direction of X-inactivation skewing (PMID:42298746). Most carrier mothers are asymptomatic (PMID:38813790).

## 4. Genetic and molecular information

**Gene and protein.** BRWD3 (Xq21.1), formerly *BRODL*, "bromo domain-containing protein disrupted in leukemia". The protein has eight WD40 repeats and two bromodomains (from the *Drosophila* ortholog *ramshackle*, PMID:16904300).

**Variant spectrum.** Delanne 2023 counted 33 different variants:
- Ostrowski 2019 alone reported "17 males with 12 distinct null variants and 2 partial gene deletions" (PMID:31714006).
- Specific examples:
  - p.Tyr1131* (PMID:24462886);
  - a de novo 74 kb deletion of exons 11–41 (PMID:24462886);
  - a 586 kb whole-gene deletion (PMID:38813790);
  - a de novo exon 21–30 deletion in a female (PMID:42298746).
- One case has a mosaic variant (PMID:36414205).

**Gene–disease validity classification**
- ClinGen rates BRWD3 **Definitive** for *X-linked syndromic intellectual disability* (MONDO:0020119), with loss of function as the mechanism (ClinGen/GenCC).
- Under the repo's rules (*Gene-Disease Validity Is Copied, Never Assigned*), that assertion counts only if MONDO:0020119 is this entry's `disease_term`, a `has_subtypes` term, or an exactMatch mapping. Otherwise it is an `other_disease` case: cite it in `notes` and do not record it as a `gene_disease_validity` row without deciding entity identity first.
- The `CGGV:` record is not yet cached in the repo.

**Population frequency.** Truncating variants are absent from controls: "No truncating variants were found in 520 control X chromosomes" (PMID:17668385). gnomAD constraint was not retrieved **[lookup needed]**.

**Copy-number events**
- Large Xq21.1 contiguous deletions that include BRWD3 cause a broader phenotype. One 5.8 Mb, 14-gene deletion also involved TBX22 and POU3F4, giving cleft palate and deafness (PMID:26323392).
- A maternally inherited duplication of only BRWD3 is of uncertain significance (PMID:30086552).

**Epigenetic biomarker.** A BRWD3 episignature was reported as matched in one test case (PMID:38751117; partly paraphrased, so verify).

**Somatic, not relevant to XLID93.** BRWD3 was originally found disrupted by t(X;11)(q13;q23) in B-cell CLL (PMID:15543602).

## 5. Environmental information

Not applicable. There are no environmental, lifestyle or infectious factors.

## 6. Mechanism and pathophysiology

**Ordered causal chain** (steps 3–5 are model-system inferences, not shown in human neurons)

1. **The lesion.** A hemizygous BRWD3 null variant or deletion **results in** loss of BRWD3 protein. This step is demonstrated: the variants are truncating or deletions, and haploinsufficiency is accepted (PMID:31714006, 38813790).
2. **Loss of the CRL4 adaptor.** Loss of BRWD3 **removes** a substrate-specificity factor of the CUL4–DDB1 E3 ligase (*Drosophila*, PMID:23479607, 37722046).
3. **Two chromatin branches.**
   - **(3a)** KDM5 escapes BRWD3/CUL4-dependent K48-polyubiquitination and degradation. This **leads to** increased H3K4me1 and decreased H3K4me3 at BRWD3-bound sites. *Drosophila* cells; "depleting KDM5 fully restores altered H3K4me3 levels" (PMID:37722046).
   - **(3b)** Loss of negative regulation of HIRA/YEM **leads to** increased H3.3 deposition (*Drosophila*, PMID:25666827).
4. **Transcriptional dysregulation.** Steps 3a and 3b **result in** global transcriptional dysregulation. In fly mutants this causes defects in dendrite morphogenesis and sensory-organ differentiation that are suppressed by inactivating *yem* or H3.3 (PMID:25666827). This step is in vivo, but invertebrate.
5. **Clinical outcome (inferred).** Abnormal neuronal differentiation and dendritic morphogenesis **are proposed to lead to** intellectual disability, speech delay and behavioral disorder. No direct human evidence exists.
6. **Growth branch (speculative).**
   - BRWD3 sits in growth and proliferation pathways: it was a JAK/STAT-pathway hit in a *Drosophila* genome-wide RNAi screen (PMID:16094372). The fly gene dBRWD3 is also required for Polycomb-mutant tissue overgrowth (PMID:27588417).
   - DDB1–BRWD3 promotes adipogenic transcription; Ddb1+/- mice resist diet-induced obesity (PMID:34161765).
   - How *loss* of BRWD3 produces macrocephaly and obesity is **unexplained**. The adipogenesis data predict the opposite direction for obesity. Record this as a knowledge gap, not an edge.

**Suggested terms (all in repo cache)**
- **GO biological process:** GO:0016567 protein ubiquitination; GO:0006511 ubiquitin-dependent protein catabolic process; GO:0006338 chromatin remodeling; GO:0006334 nucleosome assembly (for H3.3 deposition); GO:0006355 regulation of DNA-templated transcription; GO:0048813 dendrite morphogenesis; GO:0030182 neuron differentiation; GO:0007420 brain development; GO:0045444 fat cell differentiation.
- **GO terms not in cache:** regulation of histone H3K4 methylation and JAK-STAT signaling **[lookup needed]**.
- **CL:** CL:0000540 neuron; CL:0000598 pyramidal neuron (speculative); CL:0000136 adipocyte (only for the obesity hypothesis).
- **GO cellular component:** nucleus / chromatin **[lookup needed]**.

**Not available:** human transcriptomic, proteomic, metabolomic, single-cell or spatial data.

## 7. Anatomical structures

- **Primary:** brain (UBERON:0000955) and cerebral cortex (UBERON:0000956), presumed. No consistent MRI lesion has been reported.
- **Secondary:** skull and craniofacial structures (UBERON:0003129 skull), adipose tissue (UBERON:0001013), skeleton (spine, feet), testis/scrotum (cryptorchidism).
- **Subcellular:** nucleus and chromatin.
- **Laterality:** bilateral or systemic.

## 8. Temporal development

- **Onset:** congenital; delay is recognized in infancy or early childhood. Macrocephaly is postnatal (PMID:36414205), and obesity emerges in childhood.
- **Course:** non-progressive and lifelong. Index patients range up to adulthood (a 20-year-old in PMID:24462886).
- **Stages, remission and natural history:** no stages, no remission, no formal natural-history study.
- **Critical period:** early childhood, for speech and developmental intervention.

## 9. Inheritance and population

- **Inheritance:** X-linked recessive (HP:0001419) with occasional affected heterozygous females. Females are affected through skewed X-inactivation, and in one case through a de novo exon deletion (PMID:42298746, 36414205).
- **Penetrance:** apparently complete in hemizygous males. Heterozygous females are mostly unaffected (PMID:38813790).
- **Expressivity:** variable (ID mild versus moderate; macrocephaly in about 80% and obesity in about 44% of males).
- **De novo rate:** 9 of 28 variants with segregation data (32%). No anticipation, founder effect or consanguinity role.
- **Germline mosaicism:** not reported. One somatic-mosaic male is reported (PMID:36414205).
- **Prevalence:** unknown, about 45–50 published cases. Use `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
- **Sex ratio:** overwhelmingly male. Reports are worldwide: UK, Australia, USA, France, Spain, China.

## 10. Diagnostics

- **Testing route:** genotype-first. "BRWD3-related phenotypes are largely non-specific… A genotype-first approach, however, allows for the more efficient diagnosis" (PMID:36414205).
  - Exome or genome sequencing; NCIT:C101295 Whole Exome Sequencing (in cache).
  - XLID or overgrowth gene panels.
  - Chromosomal microarray or array-CGH for deletions (PMID:24462886, 38813790).
  - Exon-level CNV confirmation by qPCR (PMID:42298746).
- **Females:** X-inactivation testing is recommended (PMID:42298746).
- **Episignature:** DNA methylation analysis may help resolve VUS (PMID:38751117).
- **Not diagnostic:** no specific laboratory biomarker, imaging feature or electrophysiology finding.
- **Differential diagnosis (OGID / macrocephaly-ID):**
  - PTEN hamartoma tumor syndrome;
  - Sotos syndrome (NSD1);
  - PPP2R5D-related disorder;
  - fragile X syndrome (FMR1);
  - Simpson-Golabi-Behmel syndrome;
  - other XLID with macrocephaly.
  - PMID:31714006 says BRWD3 should be in the OGID differential. In one macrocephaly-ASD panel cohort, PTEN and PPP2R5D dominated the diagnostic yield (PMID:40282429).
- **Screening:** no newborn screening. Cascade carrier testing of female relatives is indicated.

## 11. Outcome and prognosis

- **Life expectancy:** no reduction has been reported, and there are no mortality data.
- **Morbidity:** lifelong ID, behavioral disorders, and obesity-related comorbidity risk (inferred).
- **Epilepsy:** uncommon in males (about 10%) and drug-responsive in the allelic IPE cohort (PMID:36514184).
- **Prognostic factors:** severity of ID; in females, the direction of X-inactivation skewing (PMID:42298746).

## 12. Treatment

There is no disease-specific or targeted therapy, and no clinical trials were identified. Management is supportive:

| Intervention | NCIT (cache-verified) |
|---|---|
| Early developmental intervention / special education | free text; NCIT term **[lookup needed]** |
| Speech and language therapy | NCIT:C159273 per CLAUDE.md table **[not in cache, verify]** |
| Physical therapy (hypotonia) | NCIT:C15302 |
| Occupational therapy | NCIT:C121351 |
| Behavioral management (ADHD/ASD/aggression); pharmacotherapy as indicated | NCIT:C15986 Pharmacotherapy |
| Antiseizure medication where seizures occur (valproate and lamotrigine effective in the allelic IPE cohort, PMID:36514184) | NCIT:C15986 + CHEBI agent **[lookup needed]** |
| Weight and dietary management | NCIT:C15447 Dietary Intervention (from CLAUDE.md; not in cache) |
| Orthopedic follow-up (scoliosis, pes planus) | — |
| Genetic counseling | NCIT:C15240 |
| Supportive care | NCIT:C15747 |

Pharmacogenomic, gene, cell and RNA therapies: none.

## 13. Prevention

- **Primary prevention:** none.
- **Genetic counseling and cascade testing:** counsel families and test at-risk female relatives. A carrier mother has a 50% risk of an affected son. Prenatal diagnosis and PGT are available once the familial variant is known (PMID:38813790, 42298746).
- **Tertiary prevention:** weight management, and surveillance for seizures, behavior and scoliosis.

## 14. Other species

- No naturally occurring animal disease is known; no OMIA entry was found.
- Orthologs exist: *Drosophila* *ramshackle* / dBRWD3 (CG31132) and mouse *Brwd3*. **[NCBI Gene IDs lookup needed]**
- One donkey GWAS reports BRWD3 among body-size candidate genes (PMID:36926587; title only, weak).

## 15. Model organisms

| Model | Findings | Fidelity / limits |
|---|---|---|
| *Drosophila* ram/dBRWD3 null mutants | Larval lethal; eye cells show disrupted apical junctions and cytoskeleton (PMID:16904300). Excess H3.3, altered transcriptome, defective dendrite morphogenesis, rescued by yem/H3.3 loss (PMID:25666827). Required for PcG-mutant overgrowth (PMID:27588417). | Invertebrate. The null is lethal, unlike the human hemizygous viable phenotype. No macrocephaly or obesity readout. |
| *Drosophila* S2 cells (in vitro) | BRWD3 as a CRL4 DCAF for Cryptochrome (PMID:23479607) and KDM5 (PMID:37722046). JAK/STAT RNAi hit (PMID:16094372). | Non-neuronal cell line. |
| Mouse (Ddb1+/-, 3T3-L1 adipogenesis) | DDB1–BRWD3 promotes adipogenesis (PMID:34161765). | Not a Brwd3 knockout. The direction conflicts with human obesity. |
| Brwd3 knockout mouse / iPSC neurons | **None identified** (check MGI/IMPC **[lookup needed]**) | The main translational gap; a `HUMAN_MODEL_MISMATCH` / `KNOWLEDGE_GAP` candidate |

---

## Curation recommendations for the dismech entry

1. **Phenotypes:** use the cache-verified HP IDs above, with frequencies from PMID:36414205 and 31714006. Look up the ID mild/moderate terms and broad hand before binding them.
2. **Pathophysiology:**
   - Root node: BRWD3 loss of function (`functional_impact_category: LOSS_OF_FUNCTION`, hemizygous germline).
   - Two chromatin nodes: KDM5 accumulation / H3K4 methylation imbalance, and excess H3.3 deposition. Cite these as `MODEL_ORGANISM` / `IN_VITRO` with `directness: INDIRECT`.
   - A neuronal differentiation / dendrite node, leading to the ID phenotypes.
   - Leave macrocephaly and obesity mechanisms as a `KNOWLEDGE_GAP` discussion rather than edges.
3. **Genetic:** CAUSATIVE with hgnc:17342. Handle ClinGen per the `other_disease` rule: the assertion is against MONDO:0020119.
4. **Allelic epilepsy (PMID:36514184):** consider a `notes` caveat or a `REFUTE`/`NO_EVIDENCE`-style item rather than a subtype.
5. **Prevalence:** `CASES_IN_LITERATURE`, about 45 individuals (PMID:36414205).

## Sources

- PubMed records: [17668385](https://pubmed.ncbi.nlm.nih.gov/17668385/), [24462886](https://pubmed.ncbi.nlm.nih.gov/24462886/), [30628072](https://pubmed.ncbi.nlm.nih.gov/30628072/), [31714006](https://pubmed.ncbi.nlm.nih.gov/31714006/), [36414205](https://pubmed.ncbi.nlm.nih.gov/36414205/), [42298746](https://pubmed.ncbi.nlm.nih.gov/42298746/), [38813790](https://pubmed.ncbi.nlm.nih.gov/38813790/), [36514184](https://pubmed.ncbi.nlm.nih.gov/36514184/), [37722046](https://pubmed.ncbi.nlm.nih.gov/37722046/), [34161765](https://pubmed.ncbi.nlm.nih.gov/34161765/), [25666827](https://pubmed.ncbi.nlm.nih.gov/25666827/), [27588417](https://pubmed.ncbi.nlm.nih.gov/27588417/), [23479607](https://pubmed.ncbi.nlm.nih.gov/23479607/), [16904300](https://pubmed.ncbi.nlm.nih.gov/16904300/), [16094372](https://pubmed.ncbi.nlm.nih.gov/16094372/), [15543602](https://pubmed.ncbi.nlm.nih.gov/15543602/), [26323392](https://pubmed.ncbi.nlm.nih.gov/26323392/), [30086552](https://pubmed.ncbi.nlm.nih.gov/30086552/), [38751117](https://pubmed.ncbi.nlm.nih.gov/38751117/), [40282429](https://pubmed.ncbi.nlm.nih.gov/40282429/)
- [HGNC BRWD3 REST record](https://rest.genenames.org/fetch/symbol/BRWD3)
- [ClinGen Syndromic Disorders GCEP (PMC11601709)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11601709/)
- [GenCC BRWD3 submission](https://search.thegencc.org/submissions/GENCC_000102-HGNC_17342-MONDO_0020119-HP_0001417-GENCC_100001)
- [PanelApp Australia BRWD3](https://panelapp-aus.org/panels/151/gene/BRWD3/)
- [DOID:0112045 (GlyCosmos)](https://glycosmos.org/diseases/DOID:0112045)
- [MalaCards MRX93](https://www.malacards.org/card/non_syndromic_x_linked_intellectual_disability_93)
- [NORD entry](https://rarediseases.org/?p=262849)
- [Southampton eprint of Ostrowski 2019](https://eprints.soton.ac.uk/435055)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 22 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17668385`: "In the course of systematic screening of the X-chromosome coding sequences in 250 families with nonsyndromic X-linked mental retardation (XLMR), two families were identified with truncating mutations in BRWD3… Affected males have macrocephaly with a prominent forehead, large cupped ears, and mild-to-moderate intellectual disability."
  - closest text in source: "In the course of systematic screening of the X-chromosome coding sequences in 250 families with nonsyndromic X-linked mental retardation (XLMR), two families were identified with truncating mutations in BRWD3, a gene encoding a bromodomain and WD-repeat domain-containing protein"
- `PMID:36414205` *(abstract only)*: "BRWD3-related phenotypes are largely non-specific… A genotype-first approach, however, allows for the more efficient diagnosis"
  - closest text in source: "A genotype-first approach, however, allows for the more efficient diagnosis of the BRWD3-related nonsyndromic ID"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0112045` (4 mentions) - the report calls it "GlyCosmos"; DOID calls it **non-syndromic X-linked intellectual disability 93**
- `HP:0000256` (1 mention) - the report calls it "Macrocephaly (postnatal; mean OFC +2.8 SD)"; HP calls it **Macrocephaly**
- `HP:0001513` (1 mention) - the report calls it "Obesity (mean BMI +2.0 SD)"; HP calls it **Obesity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001382` (1 mention) - the report calls it "Joint hypermobility (small joints)"; HP calls it **Joint hypermobility**
- `UBERON:0000955` (1 mention) - the report calls it "Primary:** brain"; UBERON calls it **brain**
- `NCIT:C15302` (1 mention) - the report calls it "Physical therapy (hypotonia)"; NCIT calls it **Physical Therapy**