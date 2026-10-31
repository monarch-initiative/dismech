---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T18:17:42.822542'
end_time: '2026-10-29T18:23:20.774414'
duration_seconds: 337.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: FOXP2-Related Speech and Language Disorder
  mondo_id: MONDO:0011184
  category: Mendelian
  causal_genes: FOXP2
  omim_id: OMIM:602081
  synonyms: CAS; developmental verbal dyspraxia; speech and language disorder with
    orofacial dyspraxia; speech-language disorder type 1
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
  num_turns: 30
  total_cost_usd: 2.6468859
  session_id: d766227f-70b4-5440-ab6b-6f5a6ed9d934
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 7
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 17
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:14555953
  relevance_assessed: 39
  on_topic: 37
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 47
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0111275
    reported_labels:
    - Disease Ontology
    ontology_label: speech-language disorder-1
  - term_id: HP:0000750
    reported_labels:
    - Near-universal
    ontology_label: Delayed speech and language development
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
- **Disease Name:** FOXP2-Related Speech and Language Disorder
- **MONDO ID:** MONDO:0011184 (if available)
- **Causal gene(s):** FOXP2
- **OMIM:** OMIM:602081
- **Synonyms:** CAS; developmental verbal dyspraxia; speech and language disorder with orofacial dyspraxia; speech-language disorder type 1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **FOXP2-Related Speech and Language Disorder** covering all of the
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

I'm looking up the key FOXP2 papers to get PMIDs. Running the PubMed script needs approval, so I'm switching to web search and fetch.

I've confirmed most of the PMIDs. A few landmark papers are still missing (the 1998 localisation study, the 2002 brain MRI study, the 2006 functional and deletion studies). I'm fetching those now.

# FOXP2-Related Speech and Language Disorder (FOXP2-SLD; SPCH1): research report

**Causal gene:** *FOXP2* (forkhead box P2), chromosome 7q31.1. The OMIM gene entry is 605317; the phenotype entry is OMIM:602081, "Speech-language disorder 1; SPCH1". The disorder is caused by heterozygous loss of function of *FOXP2*. This can be a sequence variant, a deletion of all or part of the gene, a structural rearrangement, or, at the 7q31 level, maternal uniparental disomy of chromosome 7. Every claim below concerns this gene and MONDO ID.

**How to read this report.** The bibliographic details of every PMID below were pulled from NCBI E-utilities and checked. Quoted snippets came back from abstract text through an automated extraction step. Several are deliberately short fragments, and each must be re-checked against the `references_cache/` copy before it is used as an evidence `snippet:`. Snippets from PMIDs 7846081, 2332125 and 11872605 are especially fragmentary. No ontology CURIE in this report has been looked up in a source yet; all are leads to verify with `runoak` or the caches before binding.

---

## 1. Disease information

**Overview.** FOXP2-SLD is an autosomal dominant neurodevelopmental disorder. Its core feature is **childhood apraxia of speech (CAS)**, a disorder of planning and programming speech movements. It usually occurs with dysarthria, impaired expressive (and often receptive) language, literacy difficulties, and impaired orofacial praxis. Nonverbal cognition is usually relatively spared.

The GeneReviews chapter (Morgan, Fisher, Scheffer & Hildebrand; posted 2016-06-23, updated 2023-01-26; PMID:27336128, NBK368474) defines the disorder as caused by heterozygous *FOXP2* pathogenic variants, including whole- or partial-gene deletions. It names CAS as the core feature, notes autistic features in some individuals, and states that there is no cure and that care is supportive.

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0011184 (per MedGen C0750927) |
| OMIM (phenotype) | 602081, SPCH1 |
| OMIM (gene) | 605317, *FOXP2* |
| Orphanet | ORPHA:209908 (per MedGen and the OMIM cross-references) |
| Disease Ontology | DOID:0111275 |
| GARD | 12889 |
| SNOMED CT | 229703009 (OMIM cross-reference) |
| HGNC | *FOXP2* is HGNC:13875, which in this repo would be written `hgnc:13875`. I have not checked this against `cache/hgnc/terms.csv`; verify it. |
| GeneReviews | NBK368474 / PMID:27336128 |
| ICD-10 / ICD-11 | No specific code. The phenotype falls under the developmental speech disorder codes (ICD-10 F80.x; ICD-11 6A01.0 developmental speech sound disorder). These are lead codes only. |

**Synonyms.** FOXP2-SLD; SPCH1; speech-language disorder type 1; developmental verbal dyspraxia (DVD); childhood apraxia of speech, FOXP2-related; speech and language disorder with orofacial dyspraxia; "KE family disorder".

**Data provenance.** Knowledge of this disorder comes from family and cohort studies (the KE pedigree, other multiplex families, case series) and aggregated resources (OMIM, GeneReviews, Orphanet). None of it comes from EHR data.

---

## 2. Etiology

**Causal factors (genetic).**
- **The KE family.** In this three-generation family, about half the members have a severe speech disorder. It was first described by Hurst et al. 1990 (PMID:2332125): "in which 16 members have a severe…"; "Intelligence and hearing are normal." The locus (SPCH1) was later mapped to 7q31.
- **Gene discovery.** Lai et al. 2001 (PMID:11586359) identified *FOXP2*:
  - "a severe speech and language disorder is transmitted as an autosomal-dominant monogenic trait"
  - The gene "is directly disrupted by the translocation breakpoint in CS", an unrelated child with a t(5;7) translocation.
  - The KE family carries the missense variant p.Arg553His (R553H) in the forkhead DNA-binding domain.
- **First truncating variant.** MacDermot et al. 2005 (PMID:15877281) screened probands with verbal dyspraxia and found "a heterozygous nonsense mutation that yields a dramatically truncated protein product" (p.Arg328Ter), segregating with speech difficulties.
- **Other mechanisms:**
  - **7q31 deletions that include *FOXP2***: Zeesman et al. 2006 (PMID:16470794): "Her deletion is on the paternally inherited chromosome and includes the FOXP2 gene". Morison et al. 2025 (PMID:40714749): "Deletion size ranged from 6.8 to 15.2 Mb."
  - **Maternal uniparental disomy of chromosome 7, or paternal deletion.** Feuk et al. 2006 (PMID:17033973): "Of these individuals with DVD, all 12 for whom parental DNA was available showed absence of a paternal copy of FOXP2."
  - **Small intragenic deletions**: Turner et al. 2013 (PMID:23918746).

**Genetic risk factors.** In a monogenic sense, the risk factor is a pathogenic *FOXP2* variant. Common *FOXP2* variation does not reliably predict language phenotypes (Hoogman et al. 2014, PMID:25013396, on brain structure). Rare missense variants are often non-functional: Estruch et al. 2016 (PMID:27933109) tested several and "only one showed functional effects". The authors concluded that some variation "is unlikely to be a highly penetrant cause of speech/language disorder". This matters for variant interpretation.

**Environmental risk factors.** None documented. I found no evidence of environmental causation.

**Protective factors.** No genetic or environmental protective factors are documented. Early, intensive speech-language therapy improves outcomes but is treatment, not protection.

**Gene–environment interactions.** None documented.

---

## 3. Phenotypes

Frequencies come mainly from Morison et al. 2023 (PMID:36328423): 28 individuals from 17 families, 12 loss-of-function and 5 missense variants, ages 2–62. Snippets from that abstract:
- "Speech disorders were prevalent (23/25, 92%) and CAS was most common (22/25, 88%)"
- Language impairment in 21/25 (84%).
- "seven participants with severe language disorder had average non-verbal cognition."
- "Comorbidities included feeding difficulties in infancy (10/26, 38%)". Fine and gross motor impairment were each 13/26 (50%), anxiety 5/27 (19%), depression 6/27 (22%), and sleep disturbance 10/24 (42%).

The HPO terms are leads and must be verified.

| Phenotype | Type | Onset / course | Frequency | Suggested HPO (verify) |
|---|---|---|---|---|
| Childhood apraxia of speech | Clinical sign | Toddler; lifelong. Persists into adulthood, and some sounds ("th", "r", "ch", "j") are never acquired (PMID:36328423) | 88% (22/25) | HP:0011098 Speech apraxia |
| Speech disorder, any | Sign | Childhood | 92% (23/25) | HP:0002167 Abnormality of speech or vocalization (coarse; needs a `coarse_binding_basis`) |
| Dysarthria | Sign | Childhood; persistent | Common (GeneReviews) | HP:0001260 Dysarthria |
| Oral / orofacial dyspraxia (non-speech movements) | Sign | Childhood | Core finding in the KE family (PMID:7846081); "unable to cough, sneeze, or laugh spontaneously" in a 7q31 deletion case (PMID:16470794) | Search HPO for "oral motor dyspraxia" |
| Expressive language impairment | Sign | Childhood | Included in the 84% with language impairment | HP:0002474 Expressive language delay |
| Receptive language impairment | Sign | Childhood | Variable | Search for the "Receptive language delay" term |
| Delayed speech and language development | Sign | Infancy/toddler | Near-universal | HP:0000750 |
| Literacy and spelling difficulty | Sign | School age | Frequent (GeneReviews/OMIM) | HP:0010522 Dyslexia |
| Feeding difficulties in infancy | Symptom | Infancy | 38% (10/26) | HP:0011968 Feeding difficulties |
| Fine motor impairment | Sign | Childhood | 50% (13/26) | HP:0010862 Delayed fine motor development |
| Gross motor impairment | Sign | Childhood | 50% (13/26) | HP:0002194 Delayed gross motor development |
| Mild intellectual disability or low verbal IQ | Sign | Childhood | Variable. Reuter et al. 2017: "Mild cognitive impairment was reported for most individuals." (PMID:27572252) | HP:0001256 Intellectual disability, mild |
| Autistic features / ASD | Behavioural | Childhood | Some individuals. In the UPD7/deletion series, "Four of the patients with DVD also meet criteria for autism spectrum disorder." (PMID:17033973) | HP:0000729 Autistic behavior; HP:0000717 Autism |
| Anxiety | Behavioural | Childhood to adult | 19% | HP:0000739 Anxiety |
| Depression | Behavioural | Adolescent/adult | 22% | HP:0000716 Depressivity |
| Sleep disturbance | Symptom | Childhood | 42% | HP:0002360 Sleep abnormality |
| Phonological working memory deficit (nonword repetition) | Neurocognitive | Childhood to adult | KE family and later work (PMID:29174050; PMID:11872604) | No HPO term found yet. Record that the search was done in `notes`. |

**Severity and progression.** Severity runs from mild to severe. The course is stable or slowly improving with therapy; the disorder is not neurodegenerative.

**Quality-of-life impact.** The main burden is on communication, education and social participation. Some people rely on augmentative and alternative communication (AAC): in 7q31 deletions, AAC included key word sign in 5/8 (63%) (PMID:40714749). Adaptive functioning across monogenic neurodevelopmental disorders, including *FOXP2*, was profiled in PMID:39846212. I found no EQ-5D or SF-36 data specific to this disorder.

---

## 4. Genetic and molecular information

**Gene.** *FOXP2*, a FOX-family (P subfamily) transcription factor. It has a polyglutamine tract, a zinc finger, a leucine zipper (which mediates homo- and heterodimerisation with FOXP1 and FOXP4), and a C-terminal forkhead DNA-binding domain.

**Variant classes**
- **Missense in the forkhead domain.** R553H (KE family) and others: Reuter et al. 2017 (PMID:27572252): "two novel missense mutations within the forkhead domain". R553H is the residue equivalent to FOXP1 R514H, which causes a different disorder (Sollis et al. 2017, PMID:28741757).
- **Nonsense and frameshift.** For example R328X (PMID:15877281). Reuter et al. 2017 reported "four different truncating mutations".
- **Deletions.** Intragenic (PMID:23918746) or multi-megabase 7q31 deletions (PMID:40714749, PMID:16470794).
- **Translocations** disrupting the gene (PMID:11586359).
- **Maternal UPD7** (PMID:17033973).

**Classification.** Truncating variants and deletions are typically classed pathogenic or likely pathogenic. Missense variants need functional assessment, because many rare variants are neutral (PMID:27933109). ClinGen gene-disease validity: I did not find a CGGV record during this search. Check `cache/` and the ClinGen export before recording `gene_disease_validity`, and never assign a tier yourself.

**Allele frequency.** *FOXP2* is depleted of loss-of-function variants in gnomAD (high pLI/LOEUF constraint). I did not retrieve exact metrics here; pathogenic variants are absent or ultra-rare.

**Origin.** Germline. Variants are either de novo or inherited from an affected parent: "Mutations occurred de novo in four families and were inherited from an affected parent in the other four." (PMID:27572252)

**Functional consequence.** Loss of function, i.e. haploinsufficiency. Vernes et al. 2006 (PMID:16984964):
- R553H "severely affects FOXP2 function, chiefly by disrupting nuclear localization and DNA-binding properties."
- R328X "yields an unstable, predominantly cytoplasmic product that lacks transactivation capacity."
- Q17L "did not have any detectable functional effect in the present study."

A dominant-negative effect of R553H through dimerisation with wild-type protein has been proposed but not established. Haploinsufficiency is the consensus model, supported by deletions and UPD causing a similar phenotype.

**Imprinting.** Imprinting has been raised because of the paternal-absence finding (PMID:17033973: "we show the maternally inherited FOXP2 to be comparatively underexpressed"). However, "The speech gene FOXP2 is not imprinted." (Thomas et al. 2012, PMID:23033221). Maternally inherited point variants also cause the disorder, so treat parent-of-origin effects as unresolved.

**Modifier genes.** None established.

**Epigenetics.** FOXP2 is post-translationally SUMOylated: "FOXP2 is SUMOylated at a single major site" (PMID:26867680). No disease-associated methylation signature has been reported.

**Chromosomal abnormalities.** 7q31 deletions (6.8–15.2 Mb), t(5;7)(q22;q31.2), and maternal UPD7, which overlaps with Silver-Russell syndrome.

---

## 5. Environmental information
Not applicable. There are no environmental, lifestyle or infectious causes. Leave the `environmental:` section empty, or record the absence with a `Left deliberately uncited.` `review_notes` waiver if the section is populated.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain
1. **A heterozygous *FOXP2* pathogenic variant** (truncating, deletion, or forkhead-domain missense) **leads to** loss of functional FOXP2 protein. Truncated proteins are unstable or cytoplasmic; R553H fails to bind DNA and mislocalises (PMID:16984964, in vitro). The functional effect is haploinsufficiency.
2. **Reduced FOXP2 dosage results in** altered transcriptional regulation of neural target genes. FOXP2 "has dual functionality, acting to either repress or activate gene expression" (PMID:17999362). It "binds to and dramatically down-regulates CNTNAP2" (PMID:18987363). Fetal brain targets regulate neurite outgrowth (PMID:21765815). These are in vitro and mouse-tissue ChIP data; the target dysregulation in human patient neurons is inferred.
3. **Altered target-gene networks lead to** abnormal development and function of cortico-striatal and cortico-cerebellar circuits. Foxp2 "modulates neuronal network formation" (PMID:21765815), and FOXP2 interacts with cortical transcription factors (PMID:29365100).
   - **3a, striatum.** In R552H heterozygous mice (the murine equivalent of R553H): "abnormal synaptic plasticity in striatal and cerebellar neural circuits" (PMID:18328704); "abnormally high ongoing striatal activity" (PMID:21876543).
   - **3b, cerebellum.** "Homozygous R552H mice show severe reductions in cerebellar growth" (PMID:18328704). In humans, Crus I grey matter is reduced and hypoactive (PMID:30460543).
   - **3c, cortex and dorsal language stream.** Children show "white matter reductions in the arcuate fasciculus (dorsal language…" (PMID:30796815).
4. **Circuit dysfunction results in** structural and functional brain anomalies in affected humans. KE family MRI shows bilateral changes, including a smaller caudate, and "Several of these regions were abnormal bilaterally" (PMID:11872605). fMRI shows "significant underactivation … in Broca's area" (PMID:14555953).
5. **Impaired cortico-basal ganglia-cerebellar sensorimotor learning leads to** deficient acquisition and sequencing of orofacial motor programs. The mouse data show motor-skill learning deficits (PMID:18328704). In songbirds, Area X knockdown impairs vocal imitation: "normal auditory-guided vocal motor learning requires FoxP2" (PMID:18052609). Applying this to human speech is a cross-species inference.
6. **This manifests as** CAS, oral dyspraxia and dysarthria. Downstream of the speech-motor deficit, and possibly through partly separate cortical pathways, come language and literacy impairment and phonological working-memory deficits (PMID:7846081, PMID:29174050).
   - **Branch (inferred).** Effects of *FOXP2* in other organs (lung, gut, bone, islets, studied in mice: PMID:27341756, 25527076, 26021489) do not produce a recognised clinical phenotype in heterozygous humans.

### Detail checklist (all CURIEs to verify)
- **Molecular function:** DNA-binding transcription repressor activity (GO:0001217); sequence-specific DNA binding (GO:0043565); protein homo- and heterodimerisation (GO:0042803 / GO:0046982).
- **Biological processes:** regulation of transcription by RNA polymerase II (GO:0006357); vocal learning (GO:0042297); vocalization behavior (GO:0071625); regulation of synaptic plasticity (GO:0048167); neuron projection development (GO:0031175); cerebellum development (GO:0021549); striatum development (GO:0021756); motor learning (GO:0061743).
- **Cell types:** medium spiny neuron (CL:1001474); Purkinje cell (CL:0000121); cerebral cortex layer 6 neurons / corticothalamic neurons (search CL); deep cerebellar nuclei neurons (search CL).
- **Subcellular location:** nucleus (GO:0005634). Truncated mutants mislocalise to the cytoplasm (GO:0005737).
- **Not involved:** metabolic, immune and tissue-damage mechanisms; no evidence for any of them.
- **Omics:** ChIP-chip and expression arrays in human neuron-like cells and mouse fetal brain (PMID:17999362, 21765815); a co-expression network linking CAS genes in embryonic brain (Eising et al. 2019, PMID:29463886). I found no single-cell or spatial data from patients.

---

## 7. Anatomical structures affected
- **Organ and system:** brain (nervous system). The functional effect falls on the speech apparatus (orofacial musculature, larynx), but those structures are themselves normal.
- **Regions (verify UBERON IDs):**
  - caudate nucleus (UBERON:0001873), bilaterally smaller
  - putamen (UBERON:0001874)
  - inferior frontal gyrus / Broca's area (UBERON:0002980 or the inferior frontal gyrus term)
  - cerebellum, Crus I (UBERON:0002037 plus a lobule term)
  - arcuate fasciculus (search UBERON)
  - sensorimotor cortex
- **Laterality:** bilateral abnormalities (PMID:11872605; PMID:30460543).
- **Cells:** see the CL list in section 6.

---

## 8. Temporal development
- **Onset:** congenital and developmental. Delays in babbling and first words are often noted in infancy; CAS becomes apparent at 2–4 years. Onset is insidious.
- **Course:** lifelong and stable to slowly improving. It is not progressive. Speech impairment persists into adulthood (PMID:36328423).
- **Critical period:** early childhood, when speech-motor learning is most plastic and intensive therapy is likely most effective. This is an inference from general CAS practice; I found no FOXP2-specific trial.
- **Remission:** none. Function improves with therapy.

---

## 9. Inheritance and population
- **Inheritance:** autosomal dominant (HP:0000006). Variants are de novo or inherited.
- **Penetrance:** high or complete for clear loss-of-function variants (KE family; PMID:27572252).
- **Expressivity:** variable, ranging from mild speech disorder to minimal verbal output, with variable cognition and autism features (PMID:36328423).
- **Anticipation:** none. **Germline mosaicism:** possible in principle; I found no specific data. **Founder effects, carrier frequency, consanguinity:** not applicable or not documented.
- **Prevalence:** unknown. FOXP2-SLD is rare. Genetic diagnoses are found in roughly a third of CAS cases ("a remarkable one in three children have a genetic variant that explains their CAS", Morgan et al. 2024, PMID:38366112), and *FOXP2* is one of many genes involved. Use `prevalence_class: NOT_YET_DOCUMENTED` or a qualitative `RARE` with `measure_type: UNKNOWN`.
- **Sex ratio:** roughly equal (14 of 28 male in PMID:36328423). **Geography:** cases are reported worldwide; I found no population enrichment.

---

## 10. Diagnostics
- **Clinical:** a speech-language pathology assessment for CAS (inconsistent errors, disrupted transitions between sounds and syllables, inappropriate prosody), oral-motor assessment, and language and literacy testing. Neuropsychological testing shows that nonverbal IQ is usually relatively preserved.
- **Imaging:** clinical MRI is usually unremarkable for an individual. In the framing of Morgan & Webster 2018 (PMID:30294994), "clinical MRI scans fail to reveal overt neural anomalies in individual cases with CAS". Group-level research MRI shows caudate, cerebellar and arcuate abnormalities (PMID:11872605, 30460543, 30796815, 27734906).
- **Laboratory and biomarkers:** none.
- **Genetic testing:** a positive genetic diagnosis is the basis for confirming the disorder.
  - **Exome or genome sequencing** with CNV calling is recommended for CAS, because the yield is about 1 in 3 (PMID:38366112). Morgan & Webster 2018: "a genetic aetiology should increasingly be pursued" (PMID:30294994).
  - **Chromosomal microarray** detects 7q31 deletions.
  - **Methylation or SNP-based testing for maternal UPD7** if the clinical picture overlaps with Silver-Russell syndrome.
  - **Single-gene or panel testing** (CAS and speech panels).
  - Karyotype, FISH or long-read sequencing to detect translocations.
  - Testing for mitochondrial DNA and repeat expansions is not indicated.
- **Differential diagnosis:** other monogenic CAS genes, including *GRIN2A*, *SETBP1*, *CHD3*, *SETD1A*, *WDR5*, *KAT6A*, *ZFHX4*, *TNRC6B*, *MKL2* (PMID:29463886), *FOXP1* syndrome (PMID:28741757), *ELP4*/16p11.2 deletion, *DDX3X*, *BRPF1*, *KANSL1*. Also idiopathic CAS, dysarthria from other neurological causes, hearing loss, and autism spectrum disorder.
- **Screening:** no population screening. Testing is offered to relatives (cascade testing) and prenatally when the familial variant is known.

---

## 11. Outcome and prognosis
- **Survival:** normal life expectancy. There is no disease-specific mortality.
- **Morbidity:** lifelong communication disability, educational difficulties, possible reliance on AAC, and psychiatric comorbidity (anxiety 19%, depression 22%; PMID:36328423).
- **Prognostic factors:** larger 7q31 deletions are associated with more severe and broader phenotypes, including ID and minimal verbal ability (PMID:40714749). Intragenic loss-of-function variants and missense variants show overlapping severity. I found no prognostic biomarkers.

---

## 12. Treatment
There is no disease-modifying therapy. Care is supportive (GeneReviews, PMID:27336128).

| Intervention | Notes | Suggested NCIT term (verify) |
|---|---|---|
| Intensive, motor-based speech therapy for CAS (for example ReST, DTTC, PROMPT, Nuffield Dyspraxia Programme) | Mainstay of treatment. Evidence comes from general CAS trials, not from FOXP2-specific studies. | NCIT:C159273 Speech-Language Therapy; `therapeutic_modality: BEHAVIORAL` |
| Augmentative and alternative communication (key word sign, devices) | Used in severe cases (PMID:40714749) | Search NCIT. A device term cannot be the `treatment_term`; use the device qualifier pattern in CLAUDE.md. |
| Language and literacy intervention, educational support | | NCIT:C15315 Rehabilitation (broad) |
| Occupational and physical therapy for fine and gross motor issues | Motor impairment in 50% | NCIT:C121351 Occupational Therapy; NCIT:C15302 Physical Therapy |
| Feeding therapy in infancy | 38% have feeding difficulties | Search NCIT |
| Psychological and psychiatric care for anxiety, depression, sleep | | Supportive Care NCIT:C15747 |
| Genetic counselling | | NCIT:C15240 Genetic Counseling |

- No pharmacotherapy, gene therapy or RNA therapy exists. I found no FOXP2-specific clinical trials on ClinicalTrials.gov, and no pharmacogenomic issues.

---

## 13. Prevention
- **Primary:** not applicable.
- **Secondary:** genetic diagnosis early in CAS enables early, intensive therapy.
- **Tertiary:** monitor and treat feeding, motor and mental-health comorbidities, and support literacy.
- **Counselling:** each child of an affected person has a 50% risk. After a de novo variant, recurrence risk is low but above zero because of possible germline mosaicism. Prenatal or preimplantation testing is possible when the familial variant is known (GeneReviews).

---

## 14. Other species
- *FOXP2* is highly conserved across vertebrates. Two amino acid substitutions arose on the human lineage: "FOXP2 is the first gene relevant to the human ability to develop language", and "this gene has been the target of selection during recent human evolution" (Enard et al. 2002, PMID:12192408). Later genomic analyses have questioned the recent-selective-sweep interpretation; this report does not cover those.
- **Orthologs (IDs to verify):**
  - mouse *Foxp2* (NCBI Taxon 10090; NCBI Gene 114142)
  - zebra finch *FoxP2* (Taxon 59729)
  - zebrafish *foxp2* (Taxon 7955)
  - *Drosophila* FoxP (Taxon 7227)
- **Natural disease in animals:** none known. I found no OMIA entry.
- **Zoonotic potential:** not applicable.

---

## 15. Model organisms

| Model | Genotype | Recapitulation | Limitations | PMID |
|---|---|---|---|---|
| Mouse *Foxp2*-R552H knock-in (KE-equivalent) | Heterozygous | "Heterozygous R552H mice are overtly normal in brain structure"; deficits in motor-skill learning; abnormal striatal and cerebellar plasticity. The same mutation causes "abnormally high ongoing striatal activity" (PMID:21876543). | Mice have no speech, so circuit-level motor learning is a proxy quantity for speech-motor programming. Homozygotes (non-human genotype) have "severe reductions in cerebellar growth". | 18328704; 21876543 |
| Mouse *Foxp2* disruption | Homozygous or heterozygous | "Disruption of both copies … caused severe motor impairment, premature death"; altered ultrasonic vocalisations; cerebellar abnormalities | Ultrasonic vocalisation is innate, not learned, so a poor proxy for speech | 15983371 |
| Conditional *Foxp2* null (floxed) | Region-specific knockout | "Foxp2 loss in each region impacted behaviour differently"; cell-autonomous increase in intrinsic excitability | Circuit-specific; supraphysiological total loss | 17619227; 30108312 |
| Humanised *Foxp2* mouse | Human T303N/N325S knock-in | "medium spiny neurons have increased dendrite lengths and increased synaptic plasticity"; faster procedural learning (PMID:25225386) | Models evolution, not disease | 19490899; 25225386 |
| Zebra finch Area X knockdown | Lentiviral shRNA | "Knockdown of FoxP2 resulted in an incomplete and inaccurate imitation of tutor song." This is a vocal-learning model. | Avian song circuit; knockdown, not a germline variant | 18052609 |
| Cell models (SH-SY5Y, HEK293) | Overexpression of variants | Localisation, DNA binding, transactivation, dimerisation and interactome assays | In vitro, overexpression | 16984964; 27933109; 29365100 |

Reviews: French & Fisher 2014 (PMID:25048596); White 2006 (PMID:17035521). I found no patient iPSC-derived neuron model in this search; this is a knowledge gap and a candidate `HUMAN_MODEL_MISMATCH` discussion.

---

## Key evidence (bibliographic details checked)

| PMID | Citation | Evidence source |
|---|---|---|
| 2332125 | Hurst 1990, Dev Med Child Neurol, KE family | Human clinical |
| 7846081 | Vargha-Khadem 1995, PNAS, praxic and nonverbal deficits | Human clinical |
| 11586359 | Lai 2001, Nature, *FOXP2* gene discovery | Human clinical |
| 11872604, 11872605 | Watkins 2002, Brain, behavioural and MRI studies | Human clinical |
| 14555953 | Liégeois 2003, Nat Neurosci, fMRI | Human clinical |
| 15877281 | MacDermot 2005, AJHG, R328X | Human clinical |
| 16984964 | Vernes 2006, HMG, variant function | In vitro |
| 17033973 | Feuk 2006, AJHG, paternal absence and UPD7 | Human clinical |
| 16470794 | Zeesman 2006, AJMG-A, 7q31 deletion | Human clinical |
| 17999362, 21765815, 18987363 | Vernes 2007/2011/2008, targets and CNTNAP2 | In vitro / model organism |
| 27572252 | Reuter 2017, J Med Genet, 14 individuals | Human clinical |
| 27933109 | Estruch 2016, J Neurodev Disord, rare variants | In vitro |
| 36328423 | Morison 2023, J Med Genet, 28-person cohort | Human clinical |
| 40714749 | Morison 2025, AJMG-A, 7q31 deletions | Human clinical |
| 38366112 | Morgan 2024, Mol Psychiatry, review of CAS genetic architecture | Review synthesis |
| 30294994 | Morgan & Webster 2018, clinical practice update | Review synthesis |
| 30460543, 30796815, 27734906 | Cerebellar and dorsal-stream imaging studies | Human clinical |
| 18328704, 21876543, 15983371, 30108312, 19490899, 25225386 | Mouse models | Model organism |
| 18052609 | Haesler 2007, songbird | Model organism |
| 12192408 | Enard 2002, Nature, evolution | Computational / other |
| 27336128 | GeneReviews (Morgan et al. 2016, updated 2023) | Review synthesis |

**Gaps to flag for curation:**
- The prevalence of FOXP2-SLD itself has not been measured.
- I did not find a ClinGen validity record; check the cache.
- No patient iPSC or organoid model was found.
- No FOXP2-specific treatment trials exist.
- Whether R553H acts as a dominant negative in vivo is unresolved.
- Parent-of-origin effects (UPD7 versus point variants) are unresolved.

**Sources**
- [GeneReviews: FOXP2-Related Speech and Language Disorder (PubMed 27336128)](https://pubmed.ncbi.nlm.nih.gov/27336128/)
- [NCBI Bookshelf NBK368474](https://www.ncbi.nlm.nih.gov/books/NBK368474/)
- [MedGen C0750927 (MONDO/OMIM/Orphanet cross-references)](https://ncbi.nlm.nih.gov/medgen/C0750927)
- [OMIM 602081 mirror](https://https.ncbi.nlm.nih.gov/omim/602081)
- [MedlinePlus Genetics: FOXP2-related speech and language disorder](https://medlineplus.gov/genetics/condition/foxp2-related-speech-and-language-disorder)
- [Morison et al. 2023 (University of Melbourne record)](https://findanexpert.unimelb.edu.au/scholarlywork/1711728-in-depth-characterisation-of-a-cohort-of-individuals-with-missense-and-loss-of-function-variants-disrupting-foxp2)
- [LOVD disease #05569 (SPCH1)](https://databases.lovd.nl/shared/diseases/05569)
- NCBI E-utilities (esearch, esummary, efetch), used for all PMID metadata and abstract snippets

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 39 |
| On topic | 37 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:14555953` *(abstract only)*: "significant underactivation … in Broca's area"
  - closest text in source: "Consistent with previously reported bilateral morphological abnormalities, the affected members showed significant underactivation relative to the unaffected members in Broca's area and its right homolog, as well as in other cortical language-related regions and in the putamen"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0111275` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **speech-language disorder-1**
- `HP:0000750` (1 mention) - the report calls it "Near-universal"; HP calls it **Delayed speech and language development**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001217` (1 mention) - the report calls it "Molecular function:** DNA-binding transcription repressor activity"; GO calls it **DNA-binding transcription repressor activity**
- `CL:1001474` (1 mention) - the report calls it "Cell types:** medium spiny neuron"; CL calls it **medium spiny neuron**
- `GO:0005634` (1 mention) - the report calls it "Subcellular location:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.