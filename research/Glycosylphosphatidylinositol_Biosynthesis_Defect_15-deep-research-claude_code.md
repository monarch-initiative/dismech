---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T13:20:22.942717'
end_time: '2026-10-14T13:22:29.156688'
duration_seconds: 126.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glycosylphosphatidylinositol Biosynthesis Defect 15
  mondo_id: MONDO:0060627
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 19
  total_cost_usd: 1.9418459000000003
  session_id: ccd42b98-927f-4db2-86f2-74355a887fde
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 3
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:34703884
  - PMID:38963495
  relevance_assessed: 14
  on_topic: 7
  off_topic: 2
  off_topic_references:
  - PMID:35551457
  - PMID:20301507
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 48
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0032794
    reported_labels:
    - unverified
    ontology_label: Myoclonic seizure
  - term_id: HP:0033052
    reported_labels:
    - unverified
    ontology_label: Non-epileptic seizure
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycosylphosphatidylinositol Biosynthesis Defect 15
- **MONDO ID:** MONDO:0060627 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycosylphosphatidylinositol Biosynthesis Defect 15** covering all of the
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

I've gathered the main sources. Now I'm writing the report.

# Glycosylphosphatidylinositol Biosynthesis Defect 15 (GPIBD15; GPAA1 deficiency): research report

**Source basis.** Most claims below come from ten references cached in this worktree (`references_cache/PMID_*.md`), with quotes copied verbatim from those files. Identifiers and the structural literature were added from web searches. Where a claim rests only on a search result, an unread abstract, or my own inference, it is marked **[unverified]** or **[inference]**.

---

## 1. Disease information

**Overview.** GPIBD15 is an autosomal recessive inherited GPI deficiency (IGD) caused by biallelic variants in **GPAA1**. GPAA1 is a non-catalytic subunit of the ER-resident GPI transamidase (GPI-T). GPI-T attaches the GPI anchor to the C-terminus of precursor proteins. The core picture is:
- global developmental delay or intellectual disability
- hypotonia
- early-onset epilepsy, often fever-sensitive
- cerebellar atrophy, frequently acquired or progressive
- osteopenia in some patients

> "we report bi-allelic mutations in GPAA1 in ten individuals from five families… Most individuals presented with global developmental delay, hypotonia, early-onset seizures, cerebellar atrophy, and osteopenia." — PMID:29100095 (Nguyen et al., *Am J Hum Genet* 2017)

> "Glycosylphosphatidylinositol biosynthesis defect 15 is a rare autosomal recessive disorder due to biallelic loss of function of GPAA1." — PMID:37510348 (Fontana et al., *Genes* 2023)

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0060627, "glycosylphosphatidylinositol biosynthesis defect 15" (verified in `cache/mondo/terms.csv`) |
| OMIM (phenotype) | 617810 |
| OMIM (gene) | GPAA1 *603048 |
| Orphanet | ORPHA:529665 [web search; no local ORPHA cache file exists, so fetch it with `just fetch-reference ORPHA:529665` before citing] |
| MedGen | C4540520 |
| Gene | GPAA1, chromosome 8q24.3; HGNC ID not looked up here, so resolve it with OAK before binding |
| ICD-10/ICD-11, MeSH | No disease-specific code. It falls under the congenital disorders of glycosylation (CDG) / GPI-deficiency parent concepts. |

**Synonyms:** GPIBD15; GPAA1 deficiency; GPAA1-related GPI deficiency; GPAA1-CDG; "GPI anchoring deficiency due to biallelic variants in GPAA1" (PMID:34703884).

**Data source type.** Everything is aggregated case-level literature: about 30 patients in case series and case reports. There are no registries or EHR cohorts.

---

## 2. Etiology

- **Cause.** Biallelic (homozygous or compound heterozygous) germline hypomorphic variants in GPAA1. These reduce GPI-T activity, which lowers the amount of GPI-anchored protein (GPI-AP) on the cell surface.
- **Genetic risk factors.**
  - Consanguinity and genetic isolates explain the homozygous cases (PMID:37510348; PMID:39152716 in consanguineous Pakistani families).
  - No susceptibility loci or modifier genes are known.
- **Environmental risk factors.** None cause the disease. **Fever is a seizure trigger**: febrile sensitivity was present in 66.7% of the pooled cohort (PMID:42001530), and in 4 of 7 patients in PMID:34703884.
- **Protective factors and gene–environment interactions.** None reported.
- **Disputed heterozygous phenotype.** One study (PMID:32533362) proposed that a heterozygous GPAA1 c.968A>G variant causes familial vascular anomalies. Castle et al. (PMID:34703884) found no vascular anomalies in biallelic patients or in carrier parents. Fontana et al. state the association "has not been confirmed by other authors." This should be treated as unconfirmed and kept out of the GPIBD15 entity.

---

## 3. Phenotypes

Pooled frequencies are from Ouyang et al. 2026 (PMID:42001530), covering 24 patients: 5 new plus 19 published.

> "The clinical manifestations included global developmental delay (100%), hypotonia (95.8%), and epilepsy (83.3%). 60% of patients experienced seizure onset before the age of one. The main seizure types were generalized tonic-clonic seizures (GTCS) (82.4%) and myoclonic seizures (70.6%). Febrile sensitivity was presented in 66.7% of patients. 60.9% of patients had cerebellar atrophy."

| Phenotype | Suggested HPO term (verify every ID with OAK) | Frequency / features | Key source |
|---|---|---|---|
| Global developmental delay | HP:0001263 Global developmental delay (in the YAML) | 100%; onset around 3 months | 42001530, 34703884 |
| Intellectual disability | HP:0001249 | Usually moderate to severe; can be mild | 37510348 |
| Hypotonia (neonatal or infantile) | HP:0001252 Hypotonia | 95.8%; noted by 4 months | 34703884 |
| Seizures / epilepsy | HP:0001250 Seizure | 83.3%; onset 3 months to 3 years | 42001530 |
| Generalized tonic-clonic seizures | HP:0002069 Bilateral tonic-clonic seizure | 82.4% of those with epilepsy | 42001530 |
| Myoclonic seizures | HP:0032794 [unverified] | 70.6% | 42001530 |
| Febrile seizures / fever sensitivity | HP:0002373 Febrile seizure | 66.7% | 42001530 |
| Drug-resistant epilepsy | HP:0033052 [unverified] | 5/5 in the Chinese cohort; elsewhere often controlled | 42001530, 37510348 |
| Cerebellar atrophy | HP:0001272 Cerebellar atrophy | 60.9%; acquired or progressive | 42001530, 34703884, 37510348 |
| Ataxia / gait ataxia | HP:0001251 / HP:0002066 | Common | 29100095 |
| Dysarthria | HP:0001260 | Variable | 34703884 |
| Dysmetria | HP:0001310 | Variable | 34703884 |
| Nystagmus | HP:0000639 | About half | 37510348 table |
| Spasticity | HP:0001257 | 2/7 | 34703884 |
| Osteopenia | HP:0000938 | Universal in the first cohort; 1/2 assessed in the second; absent in Fontana's patient | 29100095, 34703884 |
| Low serum alkaline phosphatase | HP:0003282 Low alkaline phosphatase | Occasional (1/6); ALP is never elevated | 34703884 |
| Delayed myelination; thin or hypoplastic corpus callosum | HP:0012448; HP:0033725 / HP:0002079 | Occasional | 34703884 |
| Strabismus | HP:0000486 | Occasional | 37510348 |
| Dysmorphism: prominent forehead, tented upper lip, broad nose | HP:0011220, HP:0010804 | Variable and nonspecific | 34703884, 37510348 |
| Microcephaly / relative macrocephaly | HP:0000252 / HP:0004482 | Both reported | 37510348 |
| Preauricular and cheek skin tags | HP:0000384 | 1 case | 37510348 |
| Periodic fever with raised CRP/ESR; aphthae; tonsillitis | HP:0001954 Recurrent fever | 1 case; responded to glucocorticoids | 38112147 |
| Reduced GPI-APs on granulocytes or fibroblasts (FLAER, CD16, CD59, CD73, CD109) | Lab finding; no specific HPO term | Variable; CD16 is the most sensitive marker | 29100095, 34703884 |

**Course and impact on daily life.**
- Most patients are non-ambulant or walk late. One patient walked at 6 years.
- Many are nonverbal or have severely limited speech.
- The oldest reported patient (38 years) cannot stand, read or write, but eats and undresses independently (PMID:34703884).
- No formal quality-of-life (QoL) instruments have been used.

---

## 4. Genetic and molecular information

- **Gene.** GPAA1 (glycosylphosphatidylinositol anchor attachment 1), RefSeq NM_003801.3, 8q24.3.
- **Variant spectrum.** Ouyang 2026 counts 28 variants: 19 missense, 5 frameshift, 3 intronic splicing and 1 nonsense.

| Source | Variants reported |
|---|---|
| PMID:29100095 (Nguyen 2017) | p.Ser51Leu, p.Ala54Asn (c.160_161delinsAA), p.Trp176Ser, p.Leu290Pro, p.Leu291Pro, p.Ala389Pro, p.Gln327Hisfs\*102, p.Gly307Alafs\*11, c.1164+5C>T (splice; lowers mRNA) |
| PMID:34703884 (Castle 2021) | p.Met50Lys, p.Met55Thr, p.His306Arg, p.Ala316Val (recurrent: Kurdish-Turkish and Israeli patients), p.Leu350Arg, p.Leu520Arg, p.Trp611Arg, p.Pro412Tyrfs\*19, p.Arg493Glyfs\*152, p.Met207Cysfs\*21 |
| PMID:37510348 (Fontana 2023) | Homozygous c.424G>A p.Glu142Lys. ACMG classification VUS (PP4, PP3, PM2, BP1). Absent from gnomAD; CADD 26.8. |

- **Genotype.** No patient carries two null alleles:
  > "Similar to the previous cohort, no homozygous loss-of-function variants were identified… suggestive of the importance of having residual functional gene product" (PMID:34703884)

  The functional class is hypomorphic, i.e. partial loss of function. Complete GPAA1 knockout is presumed embryonic lethal [inference, by analogy with null GPI-pathway genes].
- **Variant origin.** All germline. Missense variants cluster in the luminal domain (residues 66–348) (PMID:34703884, 37510348).
- **Variant interpretation.** Flow cytometry is recommended to support variant classification (PMID:34703884).
- **Gene curation.** Genomics England PanelApp rates GPAA1 Green for early-onset or syndromic epilepsy. ClinGen gene-disease validity: not found in the local cache (no CGGV file).
- **Not reported:** modifier genes, epigenetic findings, chromosomal abnormalities. A SNP microarray was normal in the Fontana case.

---

## 5. Environmental information

There are no environmental, lifestyle or infectious causes. Fever, including infection-driven fever, precipitates seizures. One patient had a recurrent sterile periodic-fever syndrome (PMID:38112147).

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic GPAA1 variants** (missense in the luminal domain, frameshift, splice) **lead to** reduced GPAA1 mRNA or protein, or a destabilized subunit. Splice c.1164+5C>T lowers mRNA (demonstrated, PMID:29100095). Missense variants are predicted to disrupt the luminal domain (PMID:37510348, computational).
2. A deficient GPAA1 subunit **impairs assembly and activity of the heteropentameric GPI transamidase** (PIGK–GPAA1–PIGT–PIGS–PIGU) in the ER membrane.
   - > "GPI-TA consists of five subunits: PIGK, GPAA1, PIGT, PIGS, and PIGU, and the absence of any subunit leads to the loss of activity." (PMID:34576938, in vitro)
   - Cryo-EM structures (Zhang 2022, PMID:35165458; Xu 2022, *Nat Commun*, PMID:35551457 [PMID from search, not cached]) place catalysis in PIGK (C206-H164-N58). GPAA1 is structural, not catalytic: "they suggest that unlike previously proposed, GPAA1 is not a catalytic subunit… most of the disease mutations occur near the active site or the subunit interfaces" (PMID:38963495, review). GPAA1 Asp250 is required for activity (PMID:34576938).
3. Reduced GPI-T activity **results in** failed replacement of the C-terminal GPI-attachment signal with a GPI anchor on proproteins. This reduces the delivery of GPI-APs to the cell surface:
   > "several GPI-anchored proteins had decreased cell-surface abundance in leukocytes (FLAER, CD16, and CD59) or fibroblasts (CD73 and CD109). Transduction of fibroblasts with a lentivirus encoding the wild-type protein partially rescued the deficiency" (PMID:29100095; human ex vivo / in vitro)

   Because the defect sits at the attachment step, the GPI precursor and the unanchored protein are not released as soluble protein, which is why ALP is not raised. Instead, ALP is normal or low, unlike defects of the post-attachment / remodeling steps that cause hyperphosphatasia (PMID:34703884).
4. **Branch A: nervous system.** Loss of neural GPI-APs, which act in axon growth, synapse formation and synaptic plasticity (PMID:34703884), **leads to**:
   - impaired neurodevelopment, giving developmental delay and intellectual disability
   - neuronal hyperexcitability, giving epilepsy with fever sensitivity. The specific GPI-APs responsible are **not demonstrated**.
   - cerebellar micro-organization and Purkinje-cell dendritic defects, giving progressive cerebellar atrophy and ataxia. Fontana cites a transamidase model showing "it impairs cerebellum micro-organization and Purkinje cell dendritic arborization." That is model-organism evidence from a related subunit; GPAA1 itself has no mouse model. A Purkinje-specific *Pigk* knockout mouse shows cerebellar atrophy, ataxia and Purkinje-cell loss with apoptosis and neuroinflammation [web search, PMID not retrieved].
   - Atrophy is often **acquired**: the cerebellum was normal at 7 months and atrophic at 2 years (PMID:34703884), and normal at 15 months and atrophic at 33 months (PMID:37510348).
5. **Branch B: bone.** Reduced osteoblast-surface tissue-nonspecific ALP **is hypothesized to** reduce bone formation, giving osteopenia (PMID:34703884; stated as a hypothesis). Immobility and antiseizure drugs may contribute.
6. **Branch C: immune system [speculative].** Reduced complement regulators (CD59, CD55) and loss of CD16 on granulocytes could contribute to the inflammatory or periodic-fever phenotype in one patient (PMID:38112147). This parallels autoinflammation in PIGT-PNH (PMID:34576938 background) but is **not demonstrated** for GPAA1.

### Ontology suggestions (all unverified; look up before binding)

| Category | Suggested terms |
|---|---|
| GO biological process | GO:0016255 attachment of GPI anchor to protein; GO:0006506 GPI anchor biosynthetic process; GO:0021680 cerebellar Purkinje cell layer development; GO:0001503 ossification |
| GO cellular component | GO:0042765 GPI-anchor transamidase complex; GO:0005789 endoplasmic reticulum membrane |
| CL cell types | CL:0000121 Purkinje cell; CL:0000062 osteoblast; CL:0000775 neutrophil (CD16 readout); CL:0000057 fibroblast |
| Biomarkers | CD16 (FCGR3B), CD59, CD55, FLAER, CD73 (NT5E), CD109, ALP (ALPL) |

No transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data specific to this disease exist. HEK293 GPAA1-KO cells exist as a complementation system (PMID:34576938).

---

## 7. Anatomical structures

| Level | Structures | Suggested terms (unverified) |
|---|---|---|
| Primary | Brain, especially the cerebellum (vermis and hemispheres); dentate nuclei T2 hyperintensity in one case (PMID:37510348) | UBERON:0002037 cerebellum; UBERON:0004720 cerebellar vermis |
| Secondary | Corpus callosum; cerebral white matter (myelination); skeleton (bone mineral density); granulocytes / immune system | UBERON:0002336; UBERON:0001474 bone element |
| Subcellular | ER membrane (site of GPI-T); plasma membrane / lipid rafts (where GPI-APs act) | GO cellular component |
| Lateralization | Bilateral and symmetric | — |

---

## 8. Temporal development

- **Onset.** Hypotonia from birth to 4 months. Delay is evident by about 3 months. Seizures start at 3 months to 3 years, before 1 year in 60%.
- **Course.**
  - Chronic and lifelong.
  - Cerebellar atrophy can **progress in early childhood** and then remain stable into adulthood: stable at 21, 25 and 29 years in the oldest patient (PMID:34703884).
  - Developmental skills are acquired slowly, not lost.
- **Formal staging and remission.** None. Seizures may be controlled or drug-resistant.
- **Critical window [inference].** Neuroimaging should be repeated after infancy, because a normal early MRI does not exclude later atrophy.

---

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007).
- **Penetrance and expressivity.** Penetrance appears complete for biallelic pathogenic variants. Expressivity is markedly variable: one 22-month-old with p.Leu350Arg had only mild delay and no seizures (PMID:34703884).
- **Carriers.** Heterozygous parents are unaffected and have normal flow cytometry (PMID:34703884).
- **Prevalence.** Unknown. Count of reported patients over time:

| Year | Patients reported | Source |
|---|---|---|
| 2017 | 10 (5 families) | PMID:29100095 |
| 2021 | 17 | PMID:34703884 |
| 2023 | 18 | PMID:37510348 |
| 2026 | about 24 pooled | PMID:42001530 |

  Plus further cases in Pakistani (PMID:39152716) and Chinese (PMID:38112147) families. Suggested `prevalence_class`: `CASES_IN_LITERATURE` / `ULTRA_RARE`.
- **Populations.** Reported from European, North American, Egyptian, Finnish, Israeli, Kurdish-Turkish, Italian (genetic isolate in Benevento), Pakistani and Chinese families.
- **Founder effects and anticipation.** No founder variant is established. p.Ala316Val recurred in two unrelated families. No anticipation (not a repeat disorder). Sex ratio is about 1:1.

---

## 10. Diagnostics

- **Genetic testing.** Exome or genome sequencing is the main route, used in essentially all cases. GPAA1 is also on CDG and epilepsy panels (PanelApp Green).
- **Functional confirmation.**
  - Flow cytometry of granulocytes for FLAER, CD16, CD59 and CD55. CD16 is the most sensitive marker, with reductions of 12–47% (PMID:34703884).
  - Fibroblast CD73/CD109 and lentiviral rescue (PMID:29100095).
  - GPAA1 has no characteristic flow profile, unlike PIGT and PIGU.
- **Biochemistry.**
  - Serum ALP is normal or low, never high. This separates the transamidase disorders from the HPMRS (hyperphosphatasia) group.
  - Inflammatory markers (CRP, ESR) rise only during febrile episodes in the periodic-fever case.
  - Suggested LOINC for ALP: 6768-6 [unverified; seed with `just loinc-seed-cache`].
- **Imaging.** Brain MRI shows cerebellar (vermian) atrophy, delayed myelination and a thin corpus callosum. DXA can detect osteopenia.
- **EEG.** No consistent pattern: findings include normal, multifocal spike-and-wave, polyspike and slow discharges.
- **Differential diagnosis.**
  - Other transamidase IGDs: PIGT (intractable seizures, nephrocalcinosis, dental and skeletal findings); PIGS (coarse face, gingival hypertrophy, pontine hypoplasia); PIGK (microcephaly); PIGU (thin corpus callosum).
  - Other IGDs: PIGA, PIGN, PIGG, PGAP1.
  - Hyperphosphatasia–intellectual disability syndromes (HPMRS: PIGV, PIGO, PGAP2/3), which have high ALP.
  - Other CDGs, e.g. PMM2-CDG with cerebellar atrophy.
  - Pontocerebellar hypoplasias and early-onset spinocerebellar ataxias. GPIBD15 spares the brainstem (PMID:37510348).
- **Screening.** No newborn screening. Carrier and prenatal or preimplantation testing are possible once familial variants are known.

---

## 11. Outcome and prognosis

- **Survival.** No survival data. Patients have been reported up to 38 years, so survival into adulthood is documented.
- **Morbidity.**
  - Severe neurodevelopmental disability: most are non-ambulant and many nonverbal.
  - Drug-resistant epilepsy in a subset.
  - Fracture risk from osteopenia is inferred, not documented for GPAA1, though fractures occur in PIGT deficiency (PMID:34703884).
- **Prognostic factors.** None validated. Milder cases may carry higher residual activity, but no genotype–phenotype correlation is established.

---

## 12. Treatment

No disease-modifying therapy exists. Management is symptomatic. Suggested NCIT terms below are unverified; look them up before binding.

| Intervention | Evidence | Suggested NCIT |
|---|---|---|
| Antiseizure medication: levetiracetam and others | Seizures controlled in some patients (PMID:37510348); drug-resistant in others (PMID:42001530) | NCIT:C15986 Pharmacotherapy plus `therapeutic_agent` CHEBI levetiracetam |
| Ketogenic diet | Partial but significant seizure reduction in 1 of 2 patients (PMID:34703884) | NCIT:C15447 Dietary Intervention |
| Pyridoxine (vitamin B6) | Tried in 3/7 patients; "not felt to have contributed significantly" (PMID:34703884) | Pharmacotherapy plus CHEBI pyridoxine |
| Glucocorticoids for periodic fever | Fever controlled in 1 case (PMID:38112147) | Pharmacotherapy plus a corticosteroid agent (CHEBI:50858) |
| PT / OT / speech therapy, bone-health monitoring | Recommended (PMID:34703884) | NCIT:C15302, C121351, C159273 |

- **Experimental therapy.** No trials. Lentiviral GPAA1 gene transfer rescued GPI-APs in patient fibroblasts in vitro (PMID:29100095). That is a proof of concept only.
- **Butyrate.** Effective only in PIGM promoter disease, so not applicable here.
- **Pharmacogenomics.** None known.

---

## 13. Prevention

- **Primary:** genetic counseling, which carries a 25% recurrence risk; carrier testing; prenatal or preimplantation diagnosis.
- **Tertiary:**
  - Fever control or avoidance to reduce fever-triggered seizures [inference from the febrile-sensitivity data].
  - Bone-density surveillance.
  - Serial MRI.
- **Not applicable:** vaccines, public-health measures.

---

## 14. Other species

No naturally occurring GPAA1 disease is known in animals. A query of OMIA was not performed. GPAA1 is conserved across eukaryotes; the yeast ortholog is GAA1 (*S. cerevisiae*). Zoonotic potential: not applicable.

---

## 15. Model organisms

| Model | Findings | Evidence / limits |
|---|---|---|
| **Zebrafish gpaa1 knockout / crispant** (PMID:32533362) | "displayed several types of developmental defects as well as vascular dysplasia"; shortened length, back hyperextension, small eyes | MODEL_ORGANISM. Made for the disputed vascular-anomaly claim, and neurological or cerebellar phenotypes were not characterized, so fidelity to GPIBD15 is low or unknown. |
| **HEK293 GPAA1-KO cells** (PMID:34576938) | Loss of CD55/CD59; rescue by wild-type but not D250A GPAA1 | IN_VITRO complementation assay. Useful for testing variant function. |
| **Patient fibroblasts and leukocytes** (PMID:29100095, 34703884) | Reduced GPI-APs; partial lentiviral rescue | IN_VITRO / ex vivo |
| **Mouse** | No Gpaa1 mutant published (MGI not checked). The nearest analogues are Purkinje-specific *Pigk* knockout (cerebellar atrophy, ataxia) and Nestin-Cre *Piga* (Purkinje and myelination defects). | Candidate `HUMAN_MODEL_MISMATCH` / `KNOWLEDGE_GAP`: no GPAA1-specific mammalian model exists. |
| **Yeast gaa1Δ** | GAA1 is essential in *S. cerevisiae* [known biology; no cached citation] | Shows the subunit is essential and conserved. |

---

## Curation notes for the dismech entry

1. **Disease-specific evidence anchors** are PMIDs 29100095, 34703884, 37510348, 42001530 and 38112147. Their abstracts are cached and the quotes above are verbatim.
2. **Mechanism and structure** are covered by 34576938 (full text), 35165458 and 38963495. Xu 2022 (PMID:35551457) still needs `just fetch-reference`.
3. **Keep the vascular-anomaly paper (32533362) out of the GPIBD15 phenotypes.** It concerns a heterozygous, disputed claim. At most, record it as a `REFUTE`/discussion item quoting Castle's rebuttal.
4. **Pathophysiology node to conform to.** The current node should conform to an existing GPI-anchor-deficiency module if there is one; check with `just list-modules gpi`.
5. **Do not use PMID:20301507.** The retired GeneReviews N-linked CDG chapter is not GPIBD15-specific.
6. **GeneReviews baseline.** Run `just check-genereviews` to confirm that no GPIBD15 chapter exists.

---

### Sources

**Cached abstracts and full texts (all in `references_cache/`):**
- PMID:29100095 (Nguyen 2017)
- PMID:34703884 (Castle 2021)
- PMID:37510348 (Fontana 2023)
- PMID:42001530 (Ouyang 2026)
- PMID:38112147 (Chen 2023)
- PMID:39152716 (Bibi 2024)
- PMID:32533362 (Li 2020)
- PMID:34576938 (Liu 2021)
- PMID:35165458 (Zhang 2022)
- PMID:38963495 (Li 2024)

**Web:**
- [MedGen C4540520](https://ncbi.nlm.nih.gov/medgen/C4540520)
- [LOVD GPIBD15](https://databases.lovd.nl/shared/diseases/05364)
- [PanelApp GPAA1 (Genomics England)](https://panelapp.genomicsengland.co.uk/panels/402/gene/GPAA1/)
- [PanelApp Australia CDG](https://panelapp-aus.org/panels/68/gene/GPAA1/)
- [Xu et al. 2022 Nat Commun (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/pmid/35551457)
- [RCSB 7WLD](https://www.rcsb.org/structure/7WLD)
- [Zhang et al. 2022 NSMB](https://link.springer.com/article/10.1038/s41594-022-00726-6)
- [Liu et al. 2021 Molecules](https://www.mdpi.com/1420-3049/26/18/5462)
- [PMC7206848 (GPI mouse model review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206848)
- [bioRxiv Pigk Purkinje model](https://www.biorxiv.org/content/10.1101/2020.04.20.050591v3.full.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34703884`: "GPI anchoring deficiency due to biallelic variants in GPAA1"
  - closest text in source: "There is a case report of an individual with GPI deficiency due to variants in PIGM whose severe seizures were treated successfully with the histone deacetylase inhibitor sodium butyrate.30,31 However, this is likely not a feasible treatment for all GPI-related disorders, as the patient's specific pathogenic variant was in the PIGM promotor and led to decreased acetylation and therefore decreased gene expression"
- `PMID:34703884`: "Similar to the previous cohort, no homozygous loss-of-function variants were identified… suggestive of the importance of having residual functional gene product"
  - closest text in source: "Similar to the previous cohort, no homozygous loss-of-function variants were identified in this series of patients"
- `PMID:38963495` *(abstract only)*: "they suggest that unlike previously proposed, GPAA1 is not a catalytic subunit… most of the disease mutations occur near the active site or the subunit interfaces"
  - closest text in source: "Consistent with the assembly mechanisms and the active site architecture, most of the disease mutations occur near the active site or the subunit interfaces"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35551457` (2 mentions) - Molecular insights into biogenesis of glycosylphosphatidylinositol anchor proteins.
  - shared terms: gpi-ap, anchor
- `PMID:20301507` (1 mention) - Congenital Disorders of N-Linked Glycosylation and Multiple Pathway Overview – RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY.
  - shared terms: anchor

Weighed against this report's own most characteristic terms: `gpaa1`, `patient`, `seizure`, `cerebellar`, `variant`, `gpibd15`, `phenotype`, `atrophy`, `fever`, `epilepsy`, `gpi-ap`, `fibroblast`, `fontana`, `unverified`, `disease`, `year`, `delay`, `developmental`, `normal`, `anchor`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032794` (1 mention) - the report calls it "unverified"; HP calls it **Myoclonic seizure**
- `HP:0033052` (1 mention) - the report calls it "unverified"; HP calls it **Non-epileptic seizure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000384` (1 mention) - the report calls it "Preauricular and cheek skin tags"; HP calls it **Preauricular skin tag**, and lists "Preauricular skin tags" among its other names
- `CHEBI:50858` (1 mention) - the report calls it "Pharmacotherapy plus a corticosteroid agent"; CHEBI calls it **corticosteroid**, and lists "corticosteroides" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.