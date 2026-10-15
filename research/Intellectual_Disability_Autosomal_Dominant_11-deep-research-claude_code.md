---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-09-28T12:55:40.497930'
end_time: '2026-09-28T12:59:01.165950'
duration_seconds: 200.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability, Autosomal Dominant 11
  mondo_id: MONDO:0013658
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
  web_search_requests: 3
  num_turns: 21
  total_cost_usd: 1.9612924
  session_id: a3307180-5d0e-476b-86f6-92470b0ec55d
  stop_reason: end_turn
  permission_denials: 3
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
citation_count: 8
reference_validation:
  total_references: 13
  verified: 12
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.077
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:11050113
  relevance_assessed: 12
  on_topic: 8
  unresolved_references:
  - PMID:25572454
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 10
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013658
    reported_labels:
    - MONDO
    ontology_label: intellectual disability, autosomal dominant 11
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, Autosomal Dominant 11
- **MONDO ID:** MONDO:0013658 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Autosomal Dominant 11** covering all of the
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

I've read the cached sources; now I'm pulling the patient phenotype table and checking for any later EPB41L1 case reports.

Found a ClinGen assertion in the local cache; reading it, then writing the report.

# Intellectual Disability, Autosomal Dominant 11 (MRD11; EPB41L1-related): research report

**Target:** Intellectual disability, autosomal dominant 11 · MONDO:0013658 · Mendelian
**Report date:** 2026-09-28

**Sourcing.** Quotes marked *[cached]* were read from the full texts or abstracts already fetched into this worktree's `references_cache/`. Items marked *[web]* came from search-result snippets that I could not open in full and need checking against the primary source. Ontology CURIEs in this report were not looked up. Treat them as leads and resolve each one with `runoak` or the term cache before binding it, as the repo's term contract requires.

---

## Summary

- **The disease rests on one patient.** MRD11 is defined by a single de novo missense variant, EPB41L1 c.2560C>T / p.Pro854Ser, found in one boy with severe nonsyndromic intellectual disability (ID) in a candidate-gene screen (Hamdan et al., 2011, PMID:21376300).
- **The mechanism is inferred from cell culture.** The variant halves 4.1N binding to the AMPA receptor subunit GluR1 and lowers GluR1 at the neuronal surface. That fits established 4.1N biology in AMPA receptor trafficking (PMID:11050113, PMID:19503082).
- **Mouse data point in different directions:**
  - A combined 4.1N/4.1G hypomorph showed no defect in glutamatergic transmission or LTP (PMID:19225127).
  - Knocking down 4.1N in rat dentate gyrus granule neurons did reduce synapse number and function (PMID:37845032).
  - The complete 4.1N knockout mouse has a hypothalamic–pituitary–gonadal phenotype and not a reported cognitive one (PMID:33046791).
- **The gene–disease link is weak.** It should be curated as a single-case, limited-evidence association. The one PubMed-indexed human report is the original one. A second de novo missense (p.Glu619Asp), described in a pediatric nephrology report, is not in PubMed and could not be verified.

---

## 1. Disease information

**Overview.** MRD11 is an autosomal dominant, nonsyndromic intellectual developmental disorder caused by a heterozygous (de novo) variant in EPB41L1. EPB41L1 encodes protein 4.1N, a neuron-enriched FERM-domain scaffold that links membrane receptors to the spectrin–actin cytoskeleton.

The index case is described in PMID:21376300 *[cached]*: "The p.Pro854Ser in EPB41L1 was found in a male with severe ID (Table 3). EPB41L1 encodes a neuronal cytoskeletal protein known as 4.1N, which binds to AMPAR subunits through its C-terminal domain and regulates their expression at the synaptic membrane."

**Identifiers**

| Resource | ID | Note |
|---|---|---|
| MONDO | MONDO:0013658 | label "intellectual disability, autosomal dominant 11" (confirmed in `cache/mondo/terms.csv`) |
| OMIM phenotype | 614257 (MRD11) | from memory; verify |
| OMIM gene | 602879 (EPB41L1) | Hamdan 2011 cites "EPB4L1 (MIM 602879)" *[cached]* |
| Gene locus | 20q11.23 *[web: OMIM/GeneCards]* | |
| Orphanet | No disorder-specific entry is known. MRD11 probably sits under ORPHA:178469 "Autosomal dominant non-syndromic intellectual disability" | verify; a grouping-level class, not an exact match |
| ICD-10 / ICD-11 | F79 / 6A00 (nonspecific ID codes only) | no disease-specific code |
| MeSH | Intellectual Disability (D008607) | nonspecific |

**Synonyms:** mental retardation, autosomal dominant 11; intellectual developmental disorder, autosomal dominant 11; EPB41L1-related intellectual disability.

**Data provenance:** a single published proband from a research cohort (French-Canadian nonsyndromic ID cohort, Montreal). No EHR or registry data exist.

## 2. Etiology

- **Cause:** a heterozygous germline de novo missense variant in EPB41L1. It is the only published variant in PubMed.
- **The screen that found it** *[cached, PMID:21376300]*: "we sequenced 197 genes encoding glutamate receptors and a large subset of their known interacting proteins in 95 sporadic cases of NSID. We found 11 DNMs … De novo missense mutations were found in KIF1A, GRIN1, CACNG2, and EPB41L1. Functional studies showed that all these missense mutations affect protein function in cell culture systems, suggesting that they may be pathogenic."
- **The authors' own caveat** *[cached]*: "Although sequencing these genes in larger cohorts is needed to further ascertain their involvement in NSID, genetic and functional evidence argue in favor of this possibility." This is the key evidentiary limit for the entry.
- **Cohort exclusions.** The cohort excluded dysmorphic features, abnormal growth, abnormal head circumference at birth, and perinatal or teratogenic risk factors. By design, the phenotype is "pure" ID.
- **Environmental, protective, and gene–environment factors:** none known. Record as not applicable.
- **Copy-number context.** EPB41L1 lies inside the proposed 1.62 Mb minimal critical region of the 20q11.2 microdeletion syndrome, together with GDF5 and SAMHD1 (Jedraszak 2015, PMID:25572454; Bensaid 2024, PMID:38511524). That syndrome is a separate, contiguous-gene disorder (ID, skeletal/brachydactyly and facial features). Its ID has been attributed to EPB41L1 haploinsufficiency as a candidate, not proven. Keep it distinct from MRD11, or cite it only as indirect support for dosage sensitivity.

## 3. Phenotypes

Only one proband is described, so every frequency is 1/1. Use `SOURCE_UNSPECIFIED` caution and do not state population frequencies.

| Phenotype | Details | Source | HPO lead (verify) |
|---|---|---|---|
| Severe intellectual disability | male; "severe ID" | PMID:21376300 *[cached]* | HP:0010864 Intellectual disability, severe |
| Global developmental delay | implied by the childhood ID diagnosis made on standardized tests | PMID:21376300 (cohort definition) | HP:0001263 |
| Hypotonia | reported in the OMIM clinical synopsis | *[web: OMIM 602879]* "The patient had hypotonia, no evidence of epilepsy, and normal brain imaging by MRI" | HP:0001252 Hypotonia |
| **Absent** seizures | negative finding | *[web: OMIM]* | record in `notes`, do not add as a phenotype |
| **Normal** brain MRI | negative finding | *[web: OMIM]* | as above |
| Nonsyndromic: no dysmorphism, normal growth, normal OFC at birth | cohort inclusion criteria | PMID:21376300 *[cached]* | n/a |

**Ages.** OMIM describes the patient as a 6-year-old boy *[web]*.

**Caution about the MRI footnote.** The Hamdan Table 3 footnotes "Mild atrophy of the vermian region of the cerebellum on the MRI" and the "ADOS not suggestive of autism at 15 years" refer to *other* probands in that table. The EPB41L1 patient was about 6 years old with a normal MRI. Do not attach those footnotes to MRD11.

**Onset and course:** onset in infancy or childhood (developmental); non-progressive, as expected for a neurodevelopmental disorder; lifelong. No quality-of-life data exist.

## 4. Genetic and molecular information

- **Gene:** EPB41L1 (erythrocyte membrane protein band 4.1 like 1); protein 4.1N (UniProt Q9H4G0). The HGNC ID is believed to be hgnc:3378; verify against `cache/hgnc/terms.csv` and use the lowercase `hgnc:` prefix.
- **Protein structure:** "The 879 amino acid protein shares 70, 36, and 46% identity with 4.1R in the defined membrane-binding, spectrin-actin-binding, and C-terminal domains" (PMID:10414974 *[cached]*). The domains are FERM, SAB (spectrin-actin-binding) and CTD (C-terminal domain), separated by the unique regions U1–U3 (PMID:34589518 *[cached]*).

**Pathogenic variant**

| Field | Value |
|---|---|
| Variant | c.2560C>T / p.Pro854Ser, in the C-terminal domain. Transcript not stated in the paper; OMIM uses NM_012156 |
| Origin | germline, de novo, heterozygous |
| Type | missense |
| Classification | functionally damaging in vitro; no ClinVar or ClinGen classification verified here |
| Predicted effect | reduced GluR1 binding, i.e. hypomorphic / partial loss of function; dominant negative has not been tested |

- **Primary finding** *[cached, PMID:21376300]*: "Coimmunoprecipitation (coIP) studies showed that p.Pro854Ser reduces the binding of 4.1N to GluR1 by 50% in these cells … insertion of the AMPAR subunit GluR1 at the synaptic membrane was significantly decreased in transfected hippocampal neurons producing mutant 4.1N."
- **Other variants:**
  - p.Glu619Asp (c.1857G>C, NM_012156.2), de novo, is reported in an *Asian Journal of Pediatric Nephrology* case, "Kidney Involvement in EPB41L1-associated MRD11" (about 2024). It is not PubMed-indexed and the full text is paywalled (HTTP 402). **Unverified; do not cite until fetched.**
  - No population allele frequency for p.Pro854Ser is reported in the source.
- **Gene–disease validity:** not confirmed. No ClinGen `CGGV:` assertion for EPB41L1 exists in the local cache (a grep hit turned out to be RAB7A). With one proband, a curation would most plausibly be *Limited*.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none known, apart from the 20q11.2 deletion context described in section 2.

## 5. Environmental information

None known: no environmental, lifestyle or infectious factors. Not applicable.

## 6. Mechanism and pathophysiology

**Ordered causal chain.** Steps 1–3 are shown for the variant in vitro; steps 4–6 are inferred.

1. **Initiating lesion.** A heterozygous de novo EPB41L1 p.Pro854Ser variant changes a conserved residue in the 4.1N C-terminal domain. *[human genetic; PMID:21376300]*
2. **Loss of GluR1 binding.** This roughly halves 4.1N binding to the AMPA receptor GluR1 C-terminus. *[in vitro, HEK293 co-IP; PMID:21376300]* In normal biology, the 4.1N CTD binds a membrane-proximal region of the GluR1 C-terminus and links AMPA receptors to actin: "4.1N can associate with GluR1 in vivo and colocalizes with AMPA receptors at excitatory synapses. Disruption of the interaction … decreased the surface expression of GluR1" (PMID:11050113 *[cached]*).
3. **Reduced surface GluR1.** Impaired binding reduces activity-dependent insertion of GluR1 into the plasma membrane, lowering surface and synaptic GluR1. *[in vitro, cultured hippocampal neurons; PMID:21376300]* The normal step, from PMID:19503082 *[cached]*: "the protein 4.1N was required for activity-dependent GluR1 insertion. Protein kinase C (PKC) phosphorylation of the serine 816 (S816) and S818 residues of GluR1 enhanced 4.1N binding to GluR1 … disrupting 4.1N-dependent GluR1 insertion decreased surface expression of GluR1 and the expression of long-term potentiation."
4. **Weaker excitatory transmission and plasticity.** This leads to weakened AMPA-receptor-mediated excitatory transmission and impaired LTP. *[inferred for the variant; shown for 4.1N disruption in rodent neurons]*
   - **Branch, cell-type specificity:** "reducing 4.1N expression in rat DG granule neurons … results in a significant reduction in glutamatergic synapse function that is caused by a decrease in the number of glutamatergic synapses … reduction of 4.1N expression in hippocampal CA1 pyramidal neurons has no impact on basal glutamatergic neurotransmission." The FERM domain, not the CTD, was essential there (PMID:37845032 *[cached]*). This partly conflicts with the CTD-centred variant model, so record it as a caveat.
   - **Contrary evidence:** mice lacking 4.1G with 4.1N at 22% of wild type showed "no change in basic glutamatergic synaptic transmission and long-term potentiation in the hippocampus" (PMID:19225127 *[cached]*). Record this as a REFUTE or `HUMAN_MODEL_MISMATCH` discussion.
5. **Circuit dysfunction.** Impaired synaptic plasticity and excitatory synapse maintenance in hippocampal and cortical circuits lead to defective learning and memory circuit development. *[inferred]*
6. **Clinical outcome:** severe intellectual disability and developmental delay. *[human, single case]*

**Other 4.1N partners that could contribute (speculative).** The review PMID:34589518 *[cached]* lists GluK1–3 kainate receptors, mGluR8, KCC2, IP3R1, D2/D3 receptors, CASK, βII-spectrin and others. None is linked to the variant.

**Mechanistic leads (GO and CL terms need lookup)**
- AMPA receptor trafficking / neurotransmitter receptor localization to the postsynaptic membrane: search GO "neurotransmitter receptor transport to postsynaptic membrane" and "regulation of AMPA receptor activity".
- Long-term synaptic potentiation (GO:0060291).
- Actin cytoskeleton organization (GO:0030036).
- Protein localization to plasma membrane (GO:0072659).
- Cell types: excitatory neuron / hippocampal neuron; dentate gyrus granule cell (search CL "granule cell"); CL:0000540 neuron.
- Suggested `biological_scale` tags: MOLECULAR for the binding loss, CELLULAR for the trafficking defect, TISSUE/ORGANISM for circuit and cognition.
- Candidate module: check `just list-modules synap` for an existing glutamatergic synaptopathy module before creating one.

**Omics:** no transcriptomic, proteomic, metabolomic or single-cell data specific to MRD11.

## 7. Anatomical structures

- **Organ and system:** brain; central nervous system (UBERON:0000955 brain).
- **Regions:** hippocampus, especially dentate gyrus (UBERON:0001885, verify) and cerebral cortex, based on 4.1N expression and function, not human pathology.
- **Normal expression** *[cached, PMID:10414974]*: "4.1N is expressed in almost all central and peripheral neurons … detected in embryonic neurons at the earliest stage of postmitotic differentiation." It shows punctate synaptic staining in cerebellar and dentate granule layers.
- **Subcellular:** postsynaptic density and postsynaptic membrane of excitatory synapses; cortical actin cytoskeleton. It colocalizes with PSD-95 and GluR1 (PMID:10414974). GO CC leads: postsynaptic density (GO:0014069), cortical actin cytoskeleton (GO:0030864).
- **Kidney involvement:** raised only by the unverified AJPN report. Do not curate without the source.

## 8. Temporal development

- **Onset:** congenital or neurodevelopmental, recognised in early childhood.
- **Course:** static and lifelong. No stages, remission, natural-history or critical-period data exist.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006), de novo in the reported case. Recurrence risk is low apart from germline mosaicism, which has not been assessed.
- **Penetrance and expressivity:** unknown, since n = 1.
- **Prevalence:** unknown. Use `measure_type: CASES_IN_LITERATURE`, roughly 1 in PubMed, or 2 if the AJPN case is verified.
- **Sex:** the index case is male. No founder effect, anticipation or ethnic predilection is known; the index cohort was mostly French-Canadian.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, or an ID gene panel, with trio analysis to establish de novo status. EPB41L1 is on some ID panels (see [GTR gene 2036](https://www.ncbi.nlm.nih.gov/gtr/genes/2036/)).
- **Chromosomal microarray:** first tier, to exclude 20q11.2 deletions that include EPB41L1.
- **Other tests:** no biomarkers or specific laboratory, imaging or EEG findings. The index MRI and seizure history were normal *[web: OMIM]*.
- **Differential diagnosis:** other glutamatergic nonsyndromic ID genes from the same screen (SYNGAP1, GRIN1, CACNG2/MRD10, SHANK3, STXBP1, KIF1A); the 20q11.2 microdeletion syndrome; EPB41L3-related disorders, which are biallelic with seizures and myelination defects (Brain 2024, doi:10.1093/brain/awae299). The last are a paralog disorder, not the same disease.
- **Screening:** none.

## 11. Outcome and prognosis

No data on survival, life expectancy or complications. Expected lifelong severe cognitive disability; the index case had no epilepsy.

## 12. Treatment

No disease-specific or experimental therapy, and no clinical trials (none found on ClinicalTrials.gov). Care is supportive. NCIT leads to verify:
- Supportive Care (NCIT:C15747)
- Rehabilitation (NCIT:C15315)
- Physical Therapy (NCIT:C15302), for hypotonia
- Speech Language Therapy (NCIT:C159273)
- Occupational Therapy (NCIT:C121351)
- Genetic Counseling (NCIT:C15240)

These are all generic; mark `therapeutic_modality: BEHAVIORAL` where appropriate.

## 13. Prevention

No primary prevention. Genetic counseling is the main measure: for a de novo case, low recurrence risk with a small mosaicism caveat. Prenatal or preimplantation testing is possible once a familial variant is known. No screening programs exist.

## 14. Other species

No naturally occurring disease is recorded in OMIA. The EPB41L1 ortholog is conserved in vertebrates, including mouse Epb41l1 (MGI) and rat.

## 15. Model organisms

| Model | Key finding | Recapitulation | Source |
|---|---|---|---|
| 4.1N⁻/⁻ mouse (Epb41l1 KO) | "born at a significantly reduced Mendelian ratio and exhibited high mortality between 3 to 5 weeks of age"; small; gonadal atrophy; reduced pituitary secretory granules; GnRH absent from hypothalamic axons | Does not model ID: homozygous null, cognition not reported. Suggested link: `FAILS_TO_RECAPITULATE` or `PARTIALLY_RECAPITULATES` with `SPECIES_MISMATCH` and `POPULATION_MISMATCH` (null vs heterozygous missense) caveats | PMID:33046791 *[cached]* |
| 4.1G-null / 4.1N-hypomorph mouse (22% 4.1N) | Moderate reduction in synaptosomal GluR1 at 3 weeks; normal basal transmission and LTP | Negative for the synaptic mechanism; candidate `HUMAN_MODEL_MISMATCH` | PMID:19225127 *[cached]* |
| Rat DG granule neuron 4.1N knockdown | Fewer glutamatergic synapses and weaker AMPA receptor function; CA1 unaffected | Partial support for the mechanism (`PERTURBS`, CELLULAR scale) | PMID:37845032 *[cached]* |
| Cultured hippocampal neurons, rat 4.1N-P852S (equivalent to human P854S) | Reduced surface GluR1 | Direct variant model (IN_VITRO) | PMID:21376300 *[cached]* |
| Hippocampal neurons, 4.1N disruption | Required for activity-dependent GluR1 insertion and LTP | Mechanistic (IN_VITRO / ex vivo) | PMID:19503082 *[cached]* |

No knock-in mouse carrying the patient variant has been reported. Only generic resources apply (MGI, IMPC).

---

## Curation cautions for the KB entry

1. **Single-proband disease.** Every phenotype is n = 1, so state frequencies as 1/1 or omit them. Consider a `KNOWLEDGE_GAP` discussion on replication.
2. **Evidence-source classification:**
   - Hamdan co-IP and neuron experiments: IN_VITRO.
   - Proband phenotype: HUMAN_CLINICAL.
   - Mouse papers: MODEL_ORGANISM.
   - Split Hamdan into separate evidence items for each source.
3. **Conflicting mouse evidence.** The PMID:19225127 negative result and the PMID:37845032 finding that the FERM domain, not the CTD, is essential in dentate gyrus neurons should be recorded, not dropped.
4. **Hypotonia, normal MRI and no seizures** currently rest on OMIM, not a quotable abstract. Look for the text in Hamdan Table 3 (the table body is not in the cache) before binding HP:0001252.
5. **Do not cite the p.Glu619Asp nephrology report** until its full text has been obtained.

## Sources

- Hamdan FF et al. *Am J Hum Genet* 2011. PMID:21376300. https://doi.org/10.1016/j.ajhg.2011.02.001
- Walensky LD et al. *J Neurosci* 1999. PMID:10414974
- Shen L et al. *J Neurosci* 2000. PMID:11050113
- Lin DT et al. *Nat Neurosci* 2009. PMID:19503082
- Wozny C et al. *J Cell Sci* 2009. PMID:19225127
- Wang H et al. *Sci Rep* 2020. PMID:33046791
- Yang Q et al. *Front Mol Biosci* 2021 (review). PMID:34589518
- Pushkin AN et al. *J Neurosci* 2023. PMID:37845032
- Jedraszak G et al. *Am J Med Genet A* 2015. PMID:25572454
- Bensaid S et al. *Am J Med Genet A* 2024. PMID:38511524
- [OMIM 602879 – EPB41L1](https://omim.org/entry/602879)
- [MalaCards – MRD11](https://www.malacards.org/card/autosomal_dominant_intellectual_developmental_disorder_11)
- [GeneCards – EPB41L1](https://www.genecards.org/card/EPB41L1)
- [NCBI GTR – EPB41L1](https://www.ncbi.nlm.nih.gov/gtr/genes/2036/)
- [Kidney involvement in EPB41L1-associated MRD11 (AJPN; unverified, paywalled)](https://www.ovid.com/jnls/ajpn/fulltext/10.4103/ajpn.ajpn_20_24~kidney-involvement-in-erythrocyte-membrane-protein-band)
- [Biallelic EPB41L3 variants, *Brain* 2024 (paralog differential)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11733690/)
- [ClinGen gene-validity search](https://search.clinicalgenome.org/kb/gene-validity)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:25572454` (2 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:11050113`: "4.1N can associate with GluR1 in vivo and colocalizes with AMPA receptors at excitatory synapses. Disruption of the interaction … decreased the surface expression of GluR1"
  - closest text in source: "Protein 4.1N also associates with GluR1 in vivo and colocalizes with AMPA receptors in excitatory synapses"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013658` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual disability, autosomal dominant 11**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.