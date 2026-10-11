---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:47:45.670496'
end_time: '2026-10-01T10:52:57.021233'
duration_seconds: 311.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: OGT-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0030907
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
  web_search_requests: 4
  num_turns: 23
  total_cost_usd: 2.393312
  session_id: c717d6d1-5225-4ab4-8c68-50b7a77b7279
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
citation_count: 7
reference_validation:
  total_references: 30
  verified: 29
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.033
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 29
  on_topic: 23
  unresolved_references:
  - PMID:41651253
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 50
  verified: 49
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0080240
    reported_labels:
    - DOID
    ontology_label: non-syndromic X-linked intellectual disability 106
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** OGT-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0030907 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **OGT-Congenital Disorder of Glycosylation** covering all of the
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

I'm still gathering sources. The `curl` call needed approval, so I'm switching to WebFetch against the Europe PMC API.

I have the core primary literature. Next I'm checking candidate ontology IDs against the repo's local term caches, then I'll write the report.

# OGT-Congenital Disorder of Glycosylation (OGT-CDG): research report for a dismech entry

**Target:** OGT-CDG / X-linked intellectual disability 106 (MRX106). MONDO:0030907 (`intellectual disability, X-linked 106`, confirmed against the local MONDO cache in the draft entry). Category: Mendelian.
**Date:** 2026-10-01

## Sources and how to treat this report

- **Abstract quotes are verbatim.** Every quote below comes from an abstract retrieved through the Europe PMC REST API. Before any of them is used as a KB snippet, run `just fetch-reference PMID:…` and `just count-verified-snippets`.
- **Two review summaries were extracted by a secondary tool and can't be quoted.** The patient tables and phenotype frequencies from the Pravata 2020 *Eur J Hum Genet* review (PMC7253464) and the Mayfield 2024 *J Biol Chem* review (PMC11381892) came from a model reading the full-text XML.
  - Use those numbers as leads only.
  - In the Mayfield extraction, the per-variant OGA and HCF1 table carried author attributions ("Makroglou 2020", "Stephen 2024") that I could not confirm. Treat that table as unverified.
- **Some sources were not reached.** OMIM returned HTTP 403, the PMC HTML pages served a CAPTCHA, and there is no OGT row in the local Orphanet or ClinGen caches (`references_cache/ORPHA_*`, `CGGV_*`). The OMIM, Orphanet and ClinGen identifiers below are therefore not confirmed.
- **Ontology IDs are tagged by provenance.**
  - **[cache]** means the ID and label were read from this repo's `cache/*/terms.csv` during this session.
  - **[verify]** means the ID was not found locally and must be looked up before binding. This follows the CLAUDE.md rule that a CURIE is never written from memory.

---

## 1. Disease information

**Overview.** OGT-CDG is a syndromic X-linked neurodevelopmental disorder caused mainly by missense variants in *OGT* (Xq13.1). *OGT* encodes O-GlcNAc transferase, which is the only enzyme that adds O-linked β-N-acetylglucosamine (O-GlcNAc) to serine and threonine residues of nuclear and cytosolic proteins.

- In 2020, Pravata and colleagues proposed classifying the condition as a congenital disorder of glycosylation. PMID:32080367 (review): *"we compile the work from the last few years that clearly delineates a new syndromic form of ID, which we propose to classify as a novel Congenital Disorder of Glycosylation (OGT-CDG)."*
- Mayfield 2024 summarises the phenotype. PMID:39059494: *"This disorder primarily presents with global developmental delay and intellectual disability (ID), alongside other variable neurological features and subtle facial dysmorphisms in patients."*

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0030907 *intellectual disability, X-linked 106* | in the local cache |
| OMIM (phenotype) | 300997, MRX106 | from LOVD and the search results; omim.org returned 403 |
| OMIM (gene) | *OGT* 300255 | from search results |
| DOID | DOID:0080240 | from search results |
| HGNC | *OGT*: not in `cache/hgnc/terms.csv` | **[verify]** with `runoak`; it is commonly given as HGNC:8127, which needs confirming |
| Orphanet / ICD-10 / ICD-11 / MeSH | none found | the search returned no ORPHA code specific to OGT-CDG |

**Synonyms:** OGT-CDG; OGT-XLID (used in PMID:33329753 and PMID:42107645); OGT-ID (PMID:42770280); MRX106; X-linked intellectual disability 106; mental retardation, X-linked 106.

**Data provenance:** everything here comes from aggregated case reports and family studies plus model systems, not from EHR data.

## 2. Etiology

- **Cause.** Germline variants in *OGT*, mostly missense. The first OGT-CDG families were all hemizygous males, but heterozygous females with de novo catalytic-domain variants have since been reported.
  - The first variant, p.L254F, was found in an X-exome screen of XLID families. PMID:25679214 (Niranjan 2015) is the screen; PMID:28302723 (Vaidyanathan 2017) characterised the variant.
  - PMID:28302723: *"An X-chromosome exome screen identified a missense mutation, which encodes an amino acid in the tetratricopeptide repeat, in OGT (759G>T (p.L254F)) that segregates with X-linked intellectual disability (XLID) in an affected family."*
- **Risk factors.** The only established risk factor is being male and carrying a pathogenic *OGT* allele, with family history of X-linked intellectual disability as the practical marker. No environmental risk factors are known.
- **Modifiers and protection.**
  - No modifier genes or protective alleles have been established.
  - The level of OGA compensation is a candidate *biochemical* modifier (see Section 6).
  - Skewed X-inactivation is relevant in heterozygous females (PMID:31296563).
- **Gene–environment interaction.** None documented. Because OGT is a nutrient sensor fed by the hexosamine biosynthetic pathway (UDP-GlcNAc), a metabolic interaction is plausible but has not been studied (reviewed in PMID:33329753).

## 3. Phenotypes

**Frequencies.** The figures come from the Pravata 2020 *EJHG* review summary (13 patients in 7 families). They were extracted by the secondary tool, so confirm them against the published table before use. Figures in the "~" form are approximate; denominators are the number of patients assessed.

| Phenotype | Frequency | HPO term | Notes |
|---|---|---|---|
| Intellectual disability | 13/13 (100%) | HP:0001249 Intellectual disability **[cache]** | IQ well below 70 |
| Developmental delay | 13/13 | HP:0001263 Global developmental delay **[cache]** | |
| Speech/language delay | 8/8 assessed | HP:0000750 Delayed speech and language development **[cache]** | FCDGC: "often impacting development of speech and language" |
| Dysmorphic facial features | 12/13 | Specific terms: HP:0000154 Wide mouth, HP:0000219 Thin upper lip vermilion, HP:0000179 Thick lower lip vermilion, HP:0000319 Smooth philtrum, HP:0000337 Broad forehead, HP:0000268 Dolichocephaly, HP:0000218 High palate **[all cache]** | Described as "wide mouth, thin upper lip, full lower lip, smooth philtrum" |
| Eye abnormalities | 10/13 | HP:0000545 Myopia, HP:0000483 Astigmatism, HP:0000540 Hypermetropia, HP:0000646 Amblyopia, HP:0000486 Strabismus **[all cache]** | High hypermetropia and amblyopia are listed in the MRX106 synopsis |
| 5th-finger clinodactyly / long fingers | 9/13 | HP:0004209 Clinodactyly of the 5th finger; HP:0100807 Long fingers **[cache]** | |
| Behavioural problems (ASD, ADHD) | 7/11 | HP:0000717 Autism; HP:0007018 Attention deficit hyperactivity disorder **[cache]** | |
| Short stature | 6/10 | HP:0004322 **[cache]** | Recapitulated in mice (PMID:38566589) |
| Low birth weight | 6/9 | **[verify]**, not in cache | |
| Hypotonia | 4/5 assessed | HP:0001252 **[cache]** | Also noted in PMID:41030119 |
| Brain abnormalities (e.g. corpus callosum hypoplasia) | 5/10 | HP:0002079 Hypoplasia of the corpus callosum **[cache]** | Recapitulated in the C921Y mouse (PMID:42770280) |
| Hearing or ear anomalies | 5/11 | HP:0000365 Hearing impairment **[cache]** | |
| Genital anomalies | 3/8 | HP:0000028 Cryptorchidism, HP:0000047 Hypospadias **[cache]** | Which of these is reported needs confirming |
| Microcephaly | 3/13 | HP:0000252 **[cache]** | Seen in both mouse models (PMID:38566589, PMID:42770280) |
| Seizures / epilepsy | ~1/10 in early cohort | HP:0001250 Seizure **[cache]** | C921Y "co-segregates with XLID and epileptic seizures" (PMID:37334838) |
| Drooling, coarse facies | qualitative | HP:0002307 Drooling **[cache]** | "resembles storage disorders" |
| Hepatoblastoma | 1 case | HP:0002884 **[cache]** | Possibly coincidental (PMID:41030119) |
| Ulcerative colitis, connective-tissue features | anecdotal | — | FCDGC patient page only |

**Onset and course.** Onset is congenital or in infancy and presents as developmental delay. The course is a static neurodevelopmental disorder; no regression has been reported. Severity ranges from mild to severe ID.

**Quality of life.** No QoL instrument data have been published. The functional burden comes from lifelong ID, language impairment and behavioural comorbidity.

## 4. Genetics and molecular information

**Gene.** *OGT* (Xq13.1) has an N-terminal tetratricopeptide-repeat (TPR) domain that handles substrate and partner recognition, and a C-terminal glycosyltransferase domain split into two catalytic lobes. OGT also proteolytically matures HCF1 (*HCFC1*, hgnc:4839 **[cache]**), which is itself an XLID gene. OGT's counter-enzyme is OGA (gene *OGA*, formerly *MGEA5*; HGNC ID **[verify]**).

**Reported variants** (from the primary abstracts and the EJHG review table)

| Variant | Domain | Sex / inheritance | Source |
|---|---|---|---|
| p.L254F (c.759G>T as written in the abstract; c.762G>C in the review table) | TPR | males, segregating in a family | PMID:28302723 |
| p.R284P | TPR | hemizygous male | PMID:28584052 |
| c.463-6T>G (splice) | TPR | hemizygous male; aberrant splicing, no stable truncated protein | PMID:28584052 |
| p.A259T (c.775G>A) | TPR | males, family | PMID:29769320 |
| p.E339G (c.1016A>G) | TPR | males, family | PMID:29769320 |
| p.A319T | TPR | males, family (per review table) | Selvan 2018 per the review table; this variant is not in the PMID:29769320 abstract, so source it in the full text first |
| p.N567K | catalytic | monozygotic **female** twins, skewed X-inactivation | PMID:31296563 |
| p.N648Y | catalytic | male, de novo (per review table) | probably PMID:31627256; the abstract does not name the variant, so confirm |
| p.C921Y | catalytic | co-segregates with XLID and seizures | PMID:37334838 |
| new missense variant, de novo | — | male with hepatoblastoma | PMID:41030119 |

The 2026 OGT/OGA variant catalogue (PMID:42107645, `oglcnac.mcw.edu/ogtoga/ogt/`) now lists **101** pathogenic OGT-XLID variants curated with clinicians: *"we partnered directly with clinicians and researchers to curate the most comprehensive and up-to-date collection of pathogenic OGT-XLID variants (n = 101)."*

**Variant class and functional effect**
- Variants are mostly missense, with one splice variant. They are hypomorphic (partial loss of function). Null alleles are expected to be lethal because OGT is essential for vertebrate embryogenesis (PMID:31296563).
- TPR variants cause modest instability. PMID:29769320: *"modest declines in thermodynamic stability and/or activities."*
- Catalytic-domain variants cause loss of activity. PMID:31296563: *"decreased OGT stability and disruption of the substrate binding site, resulting in loss of catalytic activity."*

**Other genetic features**
- Variants are germline; none are somatic.
- Population frequency: pathogenic variants are absent or ultra-rare. gnomAD OGT variants trigger a stronger homeostatic feedback response than OGT-CDG variants (PMID:39706180).
- Curation status: Genomics England PanelApp lists *OGT* Green (high evidence) for intellectual disability. No ClinGen gene–disease validity record is in the local cache. Because no classification was retrieved, `gene_disease_validity` should be left empty.
- Epigenetics: none in patients. Mechanistic links run through OGT–TET complexes (PMID:41033462) and through chromatin and Polycomb roles (reviewed in PMID:33329753).
- No chromosomal abnormalities are associated with the disorder.

## 5. Environmental information

None known. There is no infectious agent, toxin or lifestyle factor. For a dismech entry, leave `environmental:` empty rather than inventing a hexosamine or nutrient link.

## 6. Mechanism and pathophysiology

### Causal chain

1. A **germline hypomorphic *OGT* variant** in the TPR or catalytic domain **leads to** reduced OGT protein stability, reduced catalytic activity, or altered substrate and partner recognition (PMID:28302723, PMID:28584052, PMID:29606577, PMID:31296563).
   - *Branch A, catalytic variants (N567K, N648Y, C921Y):* catalytic activity is lost, which **results in** global hypo-O-GlcNAcylation in stem cells and in brain (PMID:31627256, PMID:37334838, PMID:38566589).
   - *Branch B, TPR variants (L254F, R284P, A259T, E339G):* global O-GlcNAc is near normal. L254F distorts the TPR helix (PMID:29606577). R284P also impairs HCF1 proteolysis (PMID:28584052).
2. Reduced OGT function **triggers homeostatic compensation**: OGA expression falls, through an OGT/mSin3A-HDAC1 repressor complex at the OGA promoter. This keeps global O-GlcNAc roughly stable, but imperfectly (PMID:28302723, PMID:28584052).
   - PMID:28302723: *"lymphoblastoids from affected individuals displayed a marked decrease in steady-state OGA protein and mRNA levels."*
   - PMID:28584052: *"Our data suggest that mutant cells attempt to maintain global O-GlcNAcylation by down-regulating O-GlcNAcase expression."*
   - The step from compensation to disease is supported by a screen. PMID:39706180 found reduced feedback across OGT-CDG variants, which "points to reduced disruption of O-GlcNAc homeostasis as a common mechanism." In the paper's terms, that means a blunted homeostatic response.
3. This **O-GlcNAc dyshomeostasis leads to** altered gene expression in pluripotent and early neural cells. Reported changes include:
   - cell-fate and LXR/RXR signalling genes (PMID:29769320);
   - reduced Oct4/Sox2 and self-renewal (PMID:37334838);
   - Zscan4 upregulation through the OGT–TET complex (PMID:41033462);
   - delayed neuronal differentiation (PMID:31296563);
   - altered neural stem cell morphology (PMID:38759397).
   - *The link from these changes to the human brain phenotype is inferred.*
4. Disrupted early neurodevelopment **results in** microcephaly, thinner cortex, superficial-layer cortical dysplasia and corpus callosum hypoplasia. This is shown in mouse (PMID:42770280, PMID:38566589).
5. Together with **synaptic and neuronal circuit defects**, this **leads to** ID, learning deficits and behavioural phenotypes.
   - Flies show impaired NMJ synaptogenesis and habituation learning, plus sleep instability (PMID:35500025, PMID:39535175).
   - Mice show hyperactivity and impulsivity (PMID:42770280).
6. A separate branch acts on **growth**: lower body weight and fat mass and short stature (mouse, PMID:38566589). This is the counterpart of short stature and low birth weight in patients. *The underlying mechanism is not established.*

**Parallel hypotheses that are not resolved.** These include TPR-interactome disruption (PMID:33356293, PMID:39059494), hypo-O-GlcNAcylation of specific neuronal substrates (22 candidates involved in Ras/MAPK signalling, translational repression, cytoskeleton and chromatin; PMID:35863433), and HCF1 misprocessing, which affects only some variants (PMID:28584052, PMID:31296563). These map naturally to `mechanistic_hypotheses` with `status: EMERGING`.

### Detail

- **Pathways:** O-GlcNAc cycling; hexosamine-pathway nutrient sensing; HCF1 maturation (the HCF-1:OGT axis in neurogenesis, PMID:41651253); TET-dependent DNA demethylation; Ras/MAPK.
- **GO terms:**
  - GO:7770074 *protein O-linked glycosylation via N-acetylglucosamine* **[cache]**
  - GO:0006493 *protein O-linked glycosylation* **[cache]**
  - GO:0030182 *neuron differentiation* **[cache]**
  - GO:0007420 *brain development* **[cache]**
  - GO:0007416 *synapse assembly* **[cache]**
  - GO:0019827 *stem cell population maintenance* **[cache]**
  - GO:0006338 *chromatin remodeling* **[cache]**
  - Molecular function "protein O-GlcNAc transferase activity" **[verify]**
- **Cell types:**
  - CL:0002322 embryonic stem cell **[cache]**
  - CL:0000047 neural stem cell **[cache]**
  - CL:0011020 neural progenitor cell **[cache]**
  - CL:0000540 neuron **[cache]**
- **Cellular compartments:** nucleus and cytosol (GO CC IDs **[verify]**).
- **Structural biology:** L254F TPR helix distortion (PMID:29606577); TPR α-solenoid dynamics (PMID:31628985); OGT dimer cryo-EM structure (PMID:34764280).
- **Omics:**
  - hESC transcriptomes (PMID:29769320)
  - mESC quantitative proteomics (PMID:41033462)
  - mouse brain proteomics (PMID:42770280)
  - TPR BioID interactome, MassIVE MSV000085626 (PMID:33356293)
  - No single-cell or spatial studies were found.

## 7. Anatomical structures affected

- **Primary:** brain, especially the cerebral cortex (superficial layers of the cingulate cortex in mouse) and the corpus callosum.
- **Other:** eye (refractive errors, amblyopia), skeleton and growth (short stature, clinodactyly), face, external genitalia, ear.
- UBERON IDs **[verify]** for: brain, cerebral cortex, corpus callosum, eye.
- **Subcellular:** nucleus and cytoplasm, where OGT and its substrates are located.
- **Lateralization:** not applicable.

## 8. Temporal development

- **Onset:** congenital, with prenatal growth effects (low birth weight). Developmental delay is evident in infancy.
- **Course:** a static, lifelong neurodevelopmental disorder. No stages and no remission.
- **Critical period:** stem cell and mouse data point to embryonic and early neurodevelopmental windows (PMID:37334838, PMID:38759397, PMID:41033462). Intervention in adulthood partially rescues fly synaptic and sleep phenotypes (PMID:39535175), which suggests some postnatal plasticity. *The human relevance is inferred.*

## 9. Inheritance and population

- **Inheritance:** X-linked, with HP:0001419 X-linked recessive inheritance **[cache]** for the familial male cases.
  - Heterozygous females are usually unaffected carriers (FCDGC).
  - Exceptions are de novo catalytic variants in affected females with skewed X-inactivation (PMID:31296563). A second inheritance block or a note may be warranted. HP:0001423 X-linked dominant inheritance **[cache]** should only be used if the de novo female cases are curated as such.
- **Prevalence:** unknown. About 101 pathogenic variants have been catalogued by 2026 (PMID:42107645). Use `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `RARE`; do not invent a rate.
- **Other features:**
  - Sex ratio: strongly male-predominant.
  - Penetrance: complete in hemizygous males as reported. Expressivity is variable.
  - No anticipation and no founder effects.
  - Consanguinity is not relevant.
  - Carrier frequency is unknown.

## 10. Diagnostics

- **Genetic testing is the diagnosis.** Exome or genome sequencing, or ID/XLID gene panels including *OGT* (PanelApp Green). FCDGC: *"OGT-CDG is ultimately diagnosed through genetic testing in blood."*
- **Glycosylation screening does not help.** Standard CDG screening (transferrin isoelectric focusing) assesses N-glycans, so it is not expected to detect O-GlcNAc defects. *I could not find a source that says this explicitly; it is my inference and needs one before it goes in the entry.*
- **Functional confirmation:**
  - patient fibroblast western blot for O-GlcNAc and OGA levels (PMID:28584052, PMID:41030119);
  - recombinant enzyme activity assays (PMID:41030119);
  - an mESC double-fluorescence feedback assay that separates pathogenic from benign VUS (PMID:39706180).
  - A blood Ogt/Oga mRNA ratio has been proposed as a monitoring biomarker (mouse, PMID:42209020).
- **Imaging:** brain MRI (corpus callosum hypoplasia, microcephaly).
- **Differential diagnosis:** other syndromic XLID, including *HCFC1*-related cblX and XLID, and *DDX3X*; storage disorders because of the coarse facies and drooling; other CDGs.
- **Screening:** no newborn screening. Carrier and cascade testing of mothers and female relatives; prenatal or preimplantation testing once the familial variant is known.

## 11. Outcome and prognosis

No natural-history data exist. FCDGC: *"Due to the rarity of the disease, there is no clear prognosis."* Life expectancy is not reported to be shortened. Morbidity is lifelong ID, language impairment, and behavioural and visual issues. A single report of hepatoblastoma (PMID:41030119) raises an unproven question about cancer risk.

## 12. Treatment

- **There is no disease-specific therapy.** FCDGC: *"There are no known treatments for OGT-CDG."*
- **Supportive and rehabilitative care.** Suggested NCIT terms, all **[verify]**:
  - Supportive Care (CLAUDE.md lists NCIT:C15747)
  - Physical Therapy (NCIT:C15302)
  - Speech-language therapy (NCIT:C159273)
  - Occupational therapy (NCIT:C121351)
  - Genetic Counseling (NCIT:C15240)
  - Corrective lenses or ophthalmology care, and antiseizure medication where seizures occur.
- **Experimental: OGA inhibition (preclinical only).**
  - *Drosophila*: PMID:35500025: *"The habituation deficit can be corrected by blocking O-GlcNAc hydrolysis… blocking O-GlcNAc hydrolysis is a potential strategy to treat OGT-CDG."* PMID:39535175: phenotypes *"can be partially rescued by genetically or chemically targeting OGA."*
  - *Mouse*: crossing with catalytically dead OGA *"partially restored O-GlcNAc homeostasis in brain and blood"* (PMID:42209020).
  - Brain-penetrant OGA inhibitors such as Thiamet-G, and clinical-stage compounds developed for tauopathy, are candidate agents (review PMID:39509538).
  - No OGT-CDG clinical trial (NCT) was found.

## 13. Prevention

- **Primary prevention:** genetic counselling, carrier testing of at-risk females, and prenatal or preimplantation diagnosis.
- **Tertiary prevention:** early developmental intervention, eye surveillance, and seizure monitoring.
- No vaccines or environmental interventions apply.

## 14. Other species and natural disease

- No naturally occurring animal disease has been reported (no OMIA search was done).
- OGT is highly conserved:
  - *Drosophila* *super sex combs* (*sxc*, a Polycomb-group gene);
  - *C. elegans* *ogt-1*, which modulates seizure susceptibility (PMID:34797853);
  - zebrafish ortholog listed on ZFIN (ZDB-GENE-030131-9631).

## 15. Model organisms

| Model | Variant | Recapitulation | Ref |
|---|---|---|---|
| Mouse (*Mus musculus*) | catalytically impaired OGT-CDG knock-in | decreased brain O-GlcNAc, OGT and OGA; low body weight and fat mass, short stature, microcephaly | PMID:38566589 |
| Mouse | C921Y | hyperactivity, impulsivity, associative-learning deficits; microcephaly, thin cortex, corpus callosum hypoplasia, cingulate dysplasia; proteomic dyshomeostasis | PMID:42770280 |
| Mouse | OGT-CDG × OGA-dead cross | microcephaly and motor deficits; partial genetic rescue of homeostasis | PMID:42209020 |
| *Drosophila* | patient missense variants (CRISPR) in *sxc* | locomotor and habituation-learning deficits rescued by OGA blockade; reduced NMJ synaptogenesis and sleep stability, partially rescued | PMID:35500025, PMID:39535175 |
| *Drosophila* | N567K | global O-GlcNAc proteome changes | PMID:31296563 |
| mESC | N567K, N648Y(?), C921Y, others | loss of OGA, delayed neuronal differentiation; reduced self-renewal (Oct4/Sox2); Zscan4/TET dysregulation | PMID:31296563, PMID:31627256, PMID:37334838, PMID:41033462 |
| hESC (CRISPR) | five TPR variants | transcriptome deregulation of cell-fate and LXR/RXR genes; no gross O-GlcNAc change | PMID:29769320 |
| Human iPSC plus isogenic control | OGT-CDG variant | reduced OGT and OGA; altered neuroectoderm and NSC morphology | PMID:38759397 |
| Patient fibroblasts and LCLs | L254F, R284P, splice, novel | reduced OGA, near-normal global O-GlcNAc | PMID:28302723, PMID:28584052, PMID:41030119 |

**Limitations.**
- Mouse models reproduce growth and structural brain features, but cognitive testing in rodents only approximates human ID.
- Fly models lack cortical architecture.
- Stem cell compensation may mask phenotypes in early stages (PMID:38759397).
- TPR-variant mouse models have not been reported.

**For dismech:** curate the mouse models under `animal_models:` and the cell models under `experimental_models:`. Use `modeled_mechanisms` targeted at nodes such as "O-GlcNAc Dyshomeostasis", "Impaired Neuronal Differentiation" and "Cortical Malformation", with `PARTIALLY_RECAPITULATES` where appropriate.

---

## Key references

| PMID | Citation |
|---|---|
| 25679214 | Niranjan 2015 *PLoS One*: X-exome XLID screen |
| 28302723 | Vaidyanathan 2017 *JBC*: L254F |
| 28584052 | Willems 2017 *JBC*: R284P and c.463-6T>G |
| 29606577 | Gundogdu 2018 *Cell Chem Biol*: L254F structure |
| 29769320 | Selvan 2018 *JBC*: A259T, E339G; hESC |
| 31296563 | Pravata 2019 *PNAS*: N567K, female twins |
| 31627256 | Pravata 2020 *FEBS Lett*: catalytic-domain variant |
| 32080367 | Pravata 2020 *Eur J Hum Genet*: OGT-CDG review and proposal |
| 33329753 | Konzman 2020 *Front Genet*: review |
| 33356293 | Stephen 2021 *J Proteome Res*: TPR interactome |
| 35500025 | Fenckova 2022 *PLoS Genet*: *Drosophila* |
| 35863433 | Mitchell 2022 *JBC*: candidate conveyor proteins |
| 37334838 | Omelková 2023 *DMM*: C921Y |
| 38566589 | Authier 2024 *DMM*: mouse |
| 38759397 | Murray 2024 *Mol Genet Metab*: iPSC |
| 39059494 | Mayfield 2024 *JBC*: review |
| 39535175 | Czajewski 2024 *eLife*: *Drosophila* rescue |
| 39706180 | Yuan 2025 *Stem Cell Rep*: variant screen |
| 41033462 | Pravata 2025 *MCP*: Zscan4/TET |
| 41030119 | D'Alessio 2026 *AJMG A*: hepatoblastoma case |
| 41651253 | Ayushma 2026 *Neurobiol Dis*: HCF-1:OGT axis |
| 42107645 | Kimi 2026 *JBC*: variant catalogue (n=101) |
| 42209020 | Authier 2026 *eNeuro*: OGA genetic rescue |
| 42770280 | Authier 2026 *eLife*: C921Y mouse |

**Web sources:** [FCDGC OGT-CDG page](https://fcdgc.rarediseasesnetwork.org/diseases-studied/ogt-cdg) · [LOVD MRX106](https://databases.lovd.nl/shared/diseases/05737) · [PanelApp OGT](https://panelapp.genomicsengland.co.uk/panels/285/gene/OGT/) · [DOID:0080240](https://disease-ontology.org/term/DOID:0080240) · [Mayfield 2024, JBC](https://www.jbc.org/article/S0021-9258(24)02100-8/fulltext) · [Czajewski 2024, eLife](https://elifesciences.org/articles/90376) · [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 29 |
| On topic | 23 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:41651253` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080240` (4 mentions) - the report calls it "DOID"; DOID calls it **non-syndromic X-linked intellectual disability 106**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0030907` (2 mentions) - the report calls it "intellectual disability, X-linked 106`, confirmed against the local MONDO cache in the draft entry"; MONDO calls it **intellectual disability, X-linked 106**