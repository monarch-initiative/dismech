---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-11T12:44:52.975434'
end_time: '2026-09-11T12:49:23.397419'
duration_seconds: 270.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Osteootohepatoenteric Syndrome
  mondo_id: MONDO:0859164
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 30
  total_cost_usd: 1.7371946000000003
  session_id: 30472749-cc0b-5982-8425-d65a5081b928
  stop_reason: end_turn
  assistant_text_blocks: 4
fell_back: true
requested_provider: perplexity
provider_attempts:
- provider: perplexity
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 20
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC9868473
  relevance_assessed: 12
  on_topic: 8
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  - term_id: GO:0032313
    ontology_label: GO_0032313
    replaced_by: GO:0043087
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteootohepatoenteric Syndrome
- **MONDO ID:** MONDO:0859164 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteootohepatoenteric Syndrome** covering all of the
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

I'll research this condition now using web search tools.

Now let me fetch the foundational Esteve 2018 AJHG paper, the MVID-mechanism paper, and the recent JCI Insight paper for deeper molecular/mechanistic detail.

I now have sufficient material to compile the comprehensive report.

# Osteootohepatoenteric Syndrome (OOHE / O2HE) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Osteootohepatoenteric syndrome (OOHE, also styled O2HE or "osteo-oto-hepato-enteric syndrome") is an ultra-rare autosomal recessive multisystem disorder first delineated in 2018. It is defined by a variable combination of four core features reflected in its name: bone fragility (osteo-), sensorineural hearing loss (oto-), cholestasis (hepato-), and congenital/severe diarrhea (enteric-), sometimes accompanied by mild developmental delay and intellectual disability. It is caused by biallelic (compound heterozygous or homozygous) loss-of-function variants in **UNC45A** (Unc-45 Myosin Chaperone A), a myosin co-chaperone gene on chromosome 15q26.1 [OMIM #619377](https://omim.org/entry/619377); [PMID:29429573](https://pubmed.ncbi.nlm.nih.gov/29429573/).

**Key identifiers:**
- **OMIM:** #619377 (phenotype), *611219 (UNC45A gene)
- **MONDO:** MONDO:0859164
- **MedGen:** C5543557 (UID 1785846)
- **Gene:** UNC45A, HGNC gene ID 55898 approx. (NCBI Gene 55898), 15q26.1
- Orphanet-specific numeric entry was not retrievable through available search (not confirmed in this session — treat as unresolved rather than fabricate an ORPHA code)

**Synonyms:** O2HE syndrome; OOHE; osteo-oto-hepato-enteric syndrome; UNC45A-related disorder / UNC45A deficiency syndrome. A related but phenotypically distinct allelic entity — **Aagenaes syndrome (cholestasis-lymphedema syndrome)** presenting with neonatal cholestasis and lymphedema — has recently been linked to a UNC45A 5′-UTR regulatory variant (c.-88G>A) in combination with a loss-of-function allele, suggesting an expanding UNC45A-related allelic/phenotypic spectrum distinct from classic OOHE ([PMID:39887522](https://pubmed.ncbi.nlm.nih.gov/39887522/)).

**Evidence basis.** Nearly all published data derive from individual case reports and small case series (aggregated literature review, not a large disease registry), supplemented by patient-derived cellular/organoid models and animal (zebrafish) studies. As of the most recent literature review (2025), **13 cases have been reported worldwide** ([PMC12516782](https://pmc.ncbi.nlm.nih.gov/articles/PMC12516782/)), making this one of the rarest entries in the dismech Mendelian category.

---

## 2. Etiology

**Disease causal factor:** Purely monogenic/genetic — biallelic loss-of-function (missense, nonsense, frameshift, small in-frame deletion, and splice) variants in *UNC45A*. No environmental, infectious, or mechanistic non-genetic cause has been described.

**Genetic risk factors:**
- Compound heterozygosity is more common than homozygosity in reported cases (most patients are compound heterozygotes for two different UNC45A alleles) [PMID:29429573].
- Recurrent variant: **c.710T>C (p.Leu237Pro)**, located in the central domain, is the most frequently reported pathogenic allele across unrelated families and has been mechanistically characterized as a distinctive "gain-of-interaction" rather than simple loss-of-function variant ([PMC11949031](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949031/); [PMID:40125554](https://pubmed.ncbi.nlm.nih.gov/40125554/)).
- Other reported variants: c.292C>T (p.Arg98Trp) (recurrent, found in ≥2 unrelated families — [PMC9868473](https://pmc.ncbi.nlm.nih.gov/articles/PMC9868473/), [PMC13019544](https://pmc.ncbi.nlm.nih.gov/articles/PMC13019544/)); c.2534-2545del (p.Leu845-Met848del); c.592C>T (p.Gln198*); c.2455C>T (p.Arg819Ter); c.2581C>T; c.2633C>T; c.2734T>G; p.Val423Asp (destabilizing/proteasomal-degradation mechanism, [PMC9218578](https://pmc.ncbi.nlm.nih.gov/articles/PMC9218578/)).
- Variants segregate with disease and are absent or present at very low frequency in gnomAD, consistent with a highly penetrant recessive Mendelian mechanism [OMIM #619377].
- No specific gnomAD constraint (pLI/LOEUF) figure for UNC45A could be independently confirmed from search results in this session; this should be verified directly against the gnomAD browser before citing a number.

**Environmental/lifestyle risk factors:** None established — this is a fully genetically determined disease with no known environmental trigger, though it may contribute to non-genetic risk of prematurity (4 of 12 reported cases were premature, suggesting UNC45A dysfunction may itself predispose to preterm birth) [PMC12516782].

**Protective factors:** None identified in the literature.

**Gene-environment interactions:** None reported; disease expression is governed by allele-specific molecular mechanism (see §6) rather than external modifiers, although intra-familial phenotypic discordance despite identical genotype has been documented (see §9, Penetrance/Expressivity), implying unidentified modifying factors (genetic or environmental) exist.

---

## 3. Phenotypes

Phenotype frequencies below are drawn from the aggregated 13-case literature review ([PMC12516782](https://pmc.ncbi.nlm.nih.gov/articles/PMC12516782/)) unless otherwise cited.

| Phenotype | Frequency | Type | Onset | Suggested HPO term |
|---|---|---|---|---|
| Congenital/severe secretory diarrhea | 13/13 (100%) | GI symptom | Neonatal (within days of birth) | HP:0002014 Diarrhea / consider HP:0410030 Congenital diarrhea |
| Neonatal cholestasis / prolonged jaundice | 9/13 (69%) | Lab/clinical sign | Neonatal | HP:0200034 Cholestasis; HP:0006579 Prolonged neonatal jaundice |
| Bone fragility / recurrent fractures | 6/13 (46%) | Skeletal sign | Infancy–childhood | HP:0002659 Recurrent fractures; HP:0004349 Reduced bone mineral density |
| Sensorineural hearing loss | 6/13 (46%) | Sensory sign | Congenital/early | HP:0000407 Sensorineural hearing impairment |
| Premature delivery | 4/13 (31%) | Perinatal | Birth | HP:0001622 Premature birth |
| Villous atrophy / MVID-like enteropathy | Reported in multiple cases | Histopathology | Neonatal | HP:0011471 Villous atrophy |
| Hepatomegaly | Reported | Clinical sign | Infancy | HP:0002240 Hepatomegaly |
| Hepatic fibrosis | Reported (MedGen) | Histopathology | Variable | HP:0001395 Hepatic fibrosis |
| Mild developmental delay / intellectual disability | Subset of cases | Cognitive | Childhood | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability |
| Osteoporosis (DEXA-confirmed) | Individual cases documented longitudinally (ages 14 and 25 in one patient) | Skeletal | Childhood onward | HP:0000939 Osteoporosis |
| Developmental dysplasia of the hip | Reported (MedGen) | Skeletal | Congenital | HP:0001385 Hip dysplasia |
| Pruritus (cholestasis-associated, episodic) | Reported in ≥1 case, severe (7-month episode) | Symptom | Variable | HP:0000989 Pruritus |
| Brain injury (neonatal) | Reported in neonatal cases | Neurological | Neonatal | Not further specified in sources retrieved |
| Recurrent miscarriage association | Suggested in literature review | Reproductive/perinatal | — | Not an HPO-codeable phenotype per se; notable epidemiological association |

**Severity/progression:** Highly variable — from near-complete clinical and biochemical recovery by 12 months in a milder Chinese case (normal hearing, no bone fragility) [PMC9868473] to severe secretory diarrhea requiring **complete enterectomy** and **early mortality in 2 of 4 patients** carrying the p.Leu237Pro variant in one cohort [PMC11949031]. Cholestasis can be relapsing/recurrent (benign recurrent intrahepatic cholestasis-like pattern) over decades, as documented in a 33-year-old patient followed from birth [PMC13019544].

**Quality of life impact:** Diarrhea and cholestasis drive substantial infancy/childhood morbidity (dehydration, growth failure, need for parenteral nutrition); hearing loss affects language development; bone fragility causes recurrent fractures affecting mobility. No formal EQ-5D/SF-36 data are available given the extreme rarity of the condition.

---

## 4. Genetic/Molecular Information

**Causal gene:** UNC45A (Unc-45 Myosin Chaperone A), OMIM *611219, chromosome 15q26.1. Suggest HGNC binding via lowercase `hgnc:` CURIE once confirmed via lookup (do not fabricate the numeric HGNC ID — verify via `runoak`/HGNC lookup before curation).

**Variant classification and types (per ACMG/ClinVar framework, as reported in source papers):**
- Missense: p.Arg98Trp, p.Leu237Pro, p.Val423Asp
- Nonsense/stop-gain: p.Gln198*, p.Arg819Ter
- In-frame deletion: p.Leu845_Met848del (4 amino acids)
- Regulatory (5′-UTR): c.-88G>A (associated with the related Aagenaes-syndrome-like phenotype, not classic OOHE) [PMID:39887522]

**Zygosity:** Predominantly compound heterozygous (biallelic, two different pathogenic variants); occasional homozygosity reported in consanguineous or founder contexts (not confirmed with a specific PMID in this session).

**Functional consequence — allele-specific mechanisms (important for `functional_impact_category` curation):**
1. **Classic loss-of-function** (e.g., nonsense/frameshift/most missense alleles): reduced UNC45A protein expression/stability, loss of chaperone activity for myosin folding [PMID:29429573].
2. **p.Val423Asp:** causes protein instability and proteasomal degradation rather than direct loss of chaperone catalytic function [PMC9218578].
3. **p.Leu237Pro (c.710T>C):** a distinctive **non-classical, dominant-negative-like mechanism** — the mutant *retains* chaperone/folding activity and still supports myosin filament assembly, but forms **abnormally stable oligomeric chaperone-myosin complexes** that fail to dissociate normally, thereby trapping and inhibiting nonmuscle myosin II (NMII) function and impairing transferrin/cargo recycling through endocytic compartments [PMC11949031]. This is a mechanistically distinct "trapping" gain-of-interaction phenotype layered on an overall loss-of-function disease, and is a strong candidate for `functional_impact_category: DOMINANT_NEGATIVE` at the `GeneticContext` level in a dismech curation, with careful attention to differentiating this from simple `LOSS_OF_FUNCTION` framing used for other alleles in the same gene.

**Modifier genes:** None formally established, though MYO5B is functionally (not genetically) linked — see mechanism section below — as UNC45A and MYO5B mutations converge on the same enterocyte apical-trafficking pathway causing overlapping enteropathy phenotypes between OOHE and microvillus inclusion disease (MVID) [PMC9218578].

**Epigenetic information:** No epigenetic mechanism has been reported for this disease.

**Chromosomal abnormalities:** None reported; disease is caused by point mutations/small indels, not large structural rearrangements.

**Population frequency:** All reported variants are rare or absent in gnomAD, consistent with a fully penetrant, ultra-rare recessive disorder; no specific allele frequency percentages could be confirmed from available sources in this session.

---

## 5. Environmental Information

No environmental, toxin, occupational, dietary, or infectious contributing factors have been identified for OOHE — it is a fully monogenic disorder. The only quasi-environmental association reported is that UNC45A dysfunction itself may be a *cause* (not consequence) of prematurity and possibly recurrent miscarriage, based on the observation that 4 of 12 literature cases were born prematurely [PMC12516782] — this is a mechanistic/reproductive association rather than an external environmental risk factor and should not be modeled as an `environmental:` exposure entry.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic loss-of-function (or, for p.Leu237Pro, altered-function) variants in *UNC45A* **lead to** impaired UNC45A co-chaperone activity in the HSP90–UNC45A–myosin folding axis.
2. Impaired chaperone function **results in** misfolding, aggregation, or (for the p.Leu237Pro allele) pathological over-stabilization of myosin motor proteins that are UNC45A clients — principally **nonmuscle myosin II (NMII)** and **myosin Vb (MYO5B)** in enterocytes [PMC9106349; PMC11949031].
3. Myosin Vb misfolding/loss of function **leads to** impaired **Rab11A-dependent apical recycling-endosome trafficking** in intestinal epithelial cells — evidenced directly: Rab11 vesicles mislocalize away from the apical membrane in patient-derived organoids and duodenal tissue [PMC9106349].
4. Disrupted apical trafficking **causes** mislocalization of key absorptive apical membrane transporters — notably **NHE3** (sodium-hydrogen exchanger) and **DRA** (chloride-bicarbonate exchanger) — into intracellular compartments rather than the brush border, while secretory transporters such as **CFTR** remain correctly localized (and one recent organoid study implicates CFTR itself as contributing to the intestinal phenotype — [PMC12780477], not independently confirmed in full detail here).
5. This selective loss of absorptive capacity with preserved/relatively enhanced secretory capacity **produces** a net secretory/osmotic diarrhea phenotype — the dominant and fully penetrant (100% of cases) clinical feature.
6. In parallel, myosin misfolding **disrupts brush-border microvillar architecture**, producing sparse, disorganized, shortened microvilli, subapical accumulation of pleomorphic vesicles and PAS-positive secretory granules, and formation of **microvillus inclusions** — a histopathological phenocopy of **microvillus inclusion disease (MVID)**, which is itself caused by MYO5B mutations, establishing OOHE and MVID as mechanistically convergent, allelic-pathway-related disorders rather than incidentally similar diseases [PMC9218578].
7. Independently, UNC45A dysfunction in **cholangiocytes/hepatocytes leads to** aberrant localization of the **bile salt export pump (BSEP)**, as directly demonstrated by immunofluorescence showing reduced UNC45A expression and aberrant BSEP localization in a patient liver biopsy [PMC13019544], **resulting in** impaired canalicular bile acid export and a low-GGT cholestasis phenotype (present in 69% of cases) — mechanistically parallel to other low-GGT familial intrahepatic cholestasis syndromes (e.g., BSEP/FIC1 deficiency), even though BSEP itself is not mutated.
8. UNC45A's broader chaperone role for **myosin-dependent processes in bone (osteoblast/osteoclast function is myosin-cytoskeleton-dependent) and inner-ear hair cells (myosin motors are essential for stereocilia and hair-cell mechanotransduction) plausibly explains** the bone fragility (46%) and sensorineural hearing loss (46%) components of the syndrome, though the cell-type-specific mechanistic studies for bone and cochlea (as opposed to the well-characterized enterocyte/hepatocyte mechanisms) are less developed in the literature reviewed here — this should be flagged as an inferred/less-directly-demonstrated step if curated into a pathograph.
9. The p.Leu237Pro allele additionally **impairs transferrin receptor recycling** through altered NMII-dependent endocytic trafficking, broadening the cell-biological consequences beyond the apical/enterocyte compartment and potentially contributing to the multisystem nature of severe cases [PMC11949031].

### Molecular pathways / cellular processes
- **HSP90–UNC45A co-chaperone pathway**: UNC45A has an N-terminal TPR domain (HSP90 interaction), a central domain (function less well defined, but is the site of the p.Leu237Pro mutation), and a C-terminal UCS domain critical for myosin motor-domain folding [GeneCards; PMID search — JBC].
- **Myosin-dependent apical vesicular trafficking** (Rab11A recycling endosome pathway) in enterocytes.
- **Nonmuscle myosin II (NMII)-dependent endocytic recycling** (transferrin pathway).
- **Bile canalicular transporter trafficking** (BSEP localization) in hepatocytes.

### Protein dysfunction
Myosin Vb (MYO5B) and nonmuscle myosin II are the principal UNC45A "client" motor proteins; their misfolding/mistrafficking is the proximate lesion. Suggested GO terms: **GO:0051082** (unfolded protein binding), **GO:0051291** (protein heterooligomerization), **GO:0016459** (myosin complex), **GO:0090161** (Golgi ribbon formation — likely not directly relevant, verify), and most centrally **GO:0032313** (regulation of Rab GTPase activity) and **GO:0006892** (post-Golgi vesicle-mediated transport)/**GO:1904776** (regulation of protein localization to apical plasma membrane) — these should be independently verified via OAK lookup before binding, per dismech's term-contract rules.

### Cell types and biological processes involved
- **Enterocytes** (small intestinal absorptive epithelial cells) — primary site of the enteropathy; suggested CL term: **CL:0000584** (enterocyte) — verify via lookup.
- **Hepatocytes / cholangiocytes** — cholestasis mechanism.
- **Cochlear hair cells** (inferred, not directly demonstrated in the sources retrieved) — hearing loss.
- **Osteoblasts/osteoclasts** (inferred) — bone fragility.

### Advanced/omics findings
- **Organoid models:** Patient-derived and CRISPR-engineered UNC45A-knockout intestinal organoids (2D and 3D, including iPSC-derived) recapitulate MVID-like architecture: dense cellular aggregates lacking a central lumen, large F-actin-positive intracellular inclusions, and abnormal brush border differentiation [PMC9106349].
- **Proteomics:** Mass spectrometry of UNC45A immunoprecipitates identified myosin Vb among nine myosin proteins significantly enriched, together with HSP90 and actin, establishing the direct chaperone-client physical interaction [PMC9106349].
- **Model organism (zebrafish):** *unc45a* mutant zebrafish larvae display microvillus shortening and MVI-like intracellular compartments plus Rab11 mislocalization, confirming in vivo relevance of the enterocyte trafficking defect [PMC9106349]. Notably, *unc45a* (unlike the paralog *unc45b*) is **not required for zebrafish myogenesis** and *unc45a*/*unc45b* double mutants show no muscle phenotype beyond that of *unc45b* alone — indicating functional divergence between the two UNC45 paralogs, with UNC45A's disease-relevant role being epithelial/non-muscle rather than sarcomeric.

---

## 7. Anatomical Structures Affected

- **Primary organs:** Small intestine (enterocytes/brush border), liver (hepatocytes, bile canaliculi), inner ear (cochlea), skeleton (bone).
- **Secondary/complication-related:** Growth/nutritional status (secondary to chronic diarrhea and malabsorption); potentially CNS (developmental delay in a subset; neonatal brain injury reported in some neonatal cases).
- **Body systems:** Gastrointestinal, hepatobiliary, auditory/sensory, skeletal, and (in a subset) neurodevelopmental.
- **Tissue/cell level:** Intestinal villus/crypt epithelium (enterocytes); hepatocyte canalicular membrane; cochlear hair cells (inferred); osteoblast/osteoclast lineage (inferred).
- **Subcellular level:** Apical recycling endosomes (Rab11A-positive compartments), brush-border microvilli, subapical secretory vesicles, lysosomes (enlarged in villus enterocytes), and — for the p.Leu237Pro mechanism — transferrin-receptor endocytic recycling compartments. Suggested GO Cellular Component terms: **GO:0031526** (brush border membrane), **GO:0055038** (recycling endosome membrane) — verify via lookup.
- **Localization:** No lateralization pattern reported (systemic/bilateral disease, e.g., bilateral sensorineural hearing loss).

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal for the cardinal features — diarrhea typically manifests within the first days to weeks of life (one case: loose stools 3–5×/day starting shortly after birth; another: acholic diarrhea within 10 days of birth). Cholestasis/jaundice is also neonatal-onset in most reported cases.
- **Onset pattern:** Acute/severe at presentation in the neonatal period for GI and hepatic features; bone fragility and hearing loss may not become apparent/diagnosed until later childhood (e.g., osteoporosis confirmed by DEXA at ages 14 and 25 in one longitudinally followed patient).
- **Progression:** Highly variable. Some patients show progressive/relapsing cholestasis over decades with episodic pruritic flares (one patient's cholestasis recurred at age 10 with a 7-month pruritus episode and bilirubin up to 270 μmol/L, then again requiring treatment as an adult). Others show near-complete resolution of diarrhea/cholestasis by 12 months with only mild residual biochemical abnormality. The most severe reported outcomes (associated with p.Leu237Pro) included complete enterectomy in one patient and early mortality in two of four patients in that cohort.
- **Disease course pattern:** Can be relapsing-remitting (cholestasis, described as "benign recurrent intrahepatic cholestasis"-like) or chronic/progressive (osteoporosis, hearing loss).
- **Critical periods:** The neonatal period is the critical window for diagnosis and life-threatening complications (severe diarrhea, cholestasis, need for parenteral nutrition); later childhood/adolescence is when skeletal and residual hepatic sequelae become apparent.

---

## 9. Inheritance and Population

- **Epidemiology:** Extremely rare — 13 cases reported worldwide as of the most recent literature review [PMC12516782]. No formal prevalence/incidence estimate exists (would fall in `prevalence_class: BELOW_1_IN_1000000` / `measure_type: CASES_IN_LITERATURE` per dismech conventions, given the literature explicitly frames this as a cumulative case count rather than a population-based rate).
- **Inheritance pattern:** Autosomal recessive (AR) — confirmed in all reported cases (compound heterozygous or homozygous biallelic variants segregating with disease) [OMIM #619377]. Suggested HP inheritance term: **HP:0000007** (Autosomal recessive inheritance).
- **Penetrance:** Appears to be high/complete for compound heterozygous null combinations, but **intrafamilial phenotypic discordance has been documented**: two siblings carrying the identical UNC45A genotype (a 5′-UTR variant c.-88G>A plus a loss-of-function allele p.Arg531Ter) both presented with neonatal cholestasis and lymphedema, but only one developed severe liver failure requiring transplantation, while the other did not — demonstrating variable expressivity/incomplete penetrance for severity even with identical genotype [PMID:39887522]. This is directly relevant to any `Inheritance.penetrance` or expressivity annotation.
- **Expressivity:** Markedly variable, spanning from mild, self-resolving disease (Chinese case, near-complete recovery by 12 months, no bone or hearing involvement) [PMC9868473] to severe multisystem disease with enterectomy and early death [PMC11949031].
- **Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported in retrieved sources.
- **Founder effects / consanguinity:** Not confirmed with specific data in this session; several published families appear non-consanguineous (e.g., the Chinese case explicitly notes "healthy, non-consanguineous parents").
- **Carrier frequency:** Not established; variants are individually rare/private in gnomAD.
- **Population demographics:** Cases reported from multiple ancestries including French/European (original 2018 description), Chinese Han (2022/2023 case), and others in the aggregated 13-case series; no specific ethnic enrichment has been established. No sex-ratio data could be confirmed from available sources.

---

## 10. Diagnostics

**Laboratory tests:**
- Liver panel: elevated total and direct bilirubin (e.g., total bilirubin 136.75 μmol/L, direct bilirubin 104.38 μmol/L in one infant), elevated total bile acids (TBA up to 217.3 μmol/L), **low GGT** pattern of cholestasis (consistent with a BSEP-trafficking-type mechanism despite BSEP being genetically normal) [PMC9868473; PMC13019544].
- Stool studies: consistent with secretory diarrhea.

**Imaging:**
- Abdominal ultrasound/imaging: hepatomegaly.
- DEXA scan: reduced bone mineral density/osteoporosis, performed longitudinally in at least one patient (ages 14, 25).

**Functional tests:**
- Auditory brainstem response (ABR): used to assess hearing (one case had normal ABR wave V threshold 25 dBHL; another had moderate bilateral sensorineural hearing loss confirmed via audiometry).

**Biopsy/histopathology:**
- Intestinal biopsy: villous atrophy, microvillus inclusion disease-like features (sparse/disorganized/shortened microvilli, microvillus inclusions, enlarged lysosomes in villus enterocytes).
- Liver biopsy: immunofluorescence showing reduced UNC45A protein expression and aberrant BSEP canalicular mislocalization [PMC13019544].

**Genetic testing:**
- **Whole exome sequencing (WES)** is the diagnostic modality used in essentially all reported cases (identifying compound heterozygous UNC45A variants); given the syndrome's rarity and nonspecific overlapping presentation with other congenital diarrhea/cholestasis syndromes (e.g., MVID/MYO5B, other PFIC genes), a single-gene UNC45A panel is unlikely to be first-line — WES/WGS with a congenital-diarrhea or cholestasis gene panel is the practical approach.
- No dedicated GTR/gene panel curated name could be confirmed from sources retrieved in this session.

**Differential diagnosis:** Microvillus inclusion disease (MYO5B, STX3, STXBP2 mutations) — overlapping enteropathy and even shared histopathology; other low-GGT progressive familial intrahepatic cholestasis syndromes (FIC1/ATP8B1, BSEP/ABCB11); congenital chloride/sodium diarrhea; other syndromic hearing-loss/bone-fragility overlap syndromes (e.g., osteogenesis imperfecta — noted as a differential in amedes-genetics resource). The related UNC45A allelic entity, Aagenaes/cholestasis-lymphedema syndrome, should also be distinguished.

**Screening:** No newborn screening or population carrier screening program exists for this ultra-rare condition.

---

## 11. Outcome/Prognosis

- **Mortality:** Documented in the most severe genotype-phenotype subgroup — 2 of 4 patients carrying the p.Leu237Pro variant in one cohort had early mortality [PMC11949031]. Formal survival statistics (5-year, 10-year) do not exist given the small case numbers; the broader 13-case literature review noted insufficient data to establish a population-level mortality rate, though neonatal brain injury was reported in some cases [PMC12516782].
- **Morbidity/complications:** Severe secretory diarrhea can necessitate long-term parenteral nutrition or, in the most severe case, complete enterectomy. Recurrent cholestatic flares with severe pruritus can persist into adulthood (one patient followed to age 33). Chronic bone fragility with recurrent fractures and confirmed osteoporosis on DEXA. One documented case of severe liver failure requiring liver transplantation in a UNC45A-mutant sibling pair.
- **Recovery potential:** Some patients (notably milder allele combinations) show near-complete clinical and biochemical recovery in infancy with treatment and can discontinue medication [PMC9868473]. Others require lifelong management.
- **Prognostic factors:** The specific UNC45A allele appears to be an important prognostic determinant — e.g., p.Leu237Pro is associated with a more severe/potentially lethal phenotype via its distinctive dominant-negative-like mechanism, while other missense combinations (e.g., p.Arg98Trp-containing genotypes) have been associated with milder, more treatable disease courses. However, the documented sibling discordance with identical genotype (§9) shows genotype alone does not fully predict severity.

---

## 12. Treatment

No disease-specific approved therapy or standardized treatment guideline exists; management is supportive/symptomatic, targeting each organ system.

**Pharmacotherapy for cholestasis:**
- **Ursodeoxycholic acid (UDCA)**, oral, e.g., 50 mg/day in an infant, used for cholestasis management [PMC9868473]. Suggested NCIT term: `NCIT:C15986` (Pharmacotherapy) + `therapeutic_agent` CHEBI ursodeoxycholic acid (verify CURIE via lookup).
- **Compound glycyrrhizin (IV)** — reported to "relieve cholestasis by regulating bile acid transporters" [PMC9868473].
- **Ademetionine 1,4-butanedisulfonate (S-adenosylmethionine)** — hepatoprotective adjunct used alongside UDCA.
- **Odevixibat** — an **ileal bile acid transporter (IBAT) inhibitor**, used via compassionate use in a 31-year-old patient at 38.5 μg/kg/day; over 2.5 years of follow-up the patient experienced no further episodes of pruritus or weight loss, with sustained low bilirubin/bile acid levels — the first reported targeted pharmacologic intervention for recurrent UNC45A-associated cholestasis and notable because IBAT inhibitors are otherwise approved/studied for other genetic cholestatic diseases (e.g., PFIC, Alagille syndrome) [PMC13019544]. This represents a genuine `therapeutic_modality: SMALL_MOLECULE` candidate treatment worth curating with an NCIT/CHEBI binding for odevixibat if available.
- **Fat-soluble vitamin supplementation** (A, D, E, K) — standard supportive care for cholestasis-associated malabsorption.

**Nutritional/supportive management for diarrhea:**
- Combination of **parenteral nutrition** and **enteral nutrition**, individualized; some patients improve with oral formula feeding and gain weight over time [PMC12516782].
- In the most severe case, **complete enterectomy** was performed [PMC11949031] — an NCIT surgical-procedure term (`NCIT:C15329` Surgical Procedure) would apply, with `preferred_term` specifying enterectomy.

**Hearing loss management:**
- **Hearing aids** — reported for moderate bilateral sensorineural hearing loss [PMC13019544]. Suggested NCIT device pattern per dismech convention: bind the clinical action term with a `qualifiers` device sub-binding rather than binding the device term directly to `treatment_term` (per the dismech Treatment Terms guidance on devices).
- No cochlear implantation has been specifically reported for this syndrome in the sources retrieved (unlike some other syndromic hearing-loss entries in the KB).

**Bone fragility management:**
- No bisphosphonate use for OOHE specifically was confirmed in this session's searches (a bisphosphonate result returned was for an unrelated condition, MPS IVA) — do not assume bisphosphonate use without a direct primary-source citation; this is a plausible but currently unconfirmed treatment avenue for curation purposes.

**Liver transplantation:**
- Reported as a rescue intervention in at least one sibling with severe liver failure, though specific to the related/overlapping Aagenaes-like phenotype rather than confirmed in classic OOHE cohorts [context from sibling-discordance search; PMID:39887522 general topic].

**Experimental/investigational:** No registered clinical trials specific to UNC45A/OOHE were identified in this session's searches; odevixibat use above was compassionate/off-label rather than a formal trial.

**Treatment outcomes:** Response to UDCA + supportive hepatoprotective regimen was associated with "complete clinical and biochemical recovery" at 12 months in a milder case [PMC9868473]. Odevixibat's 2.5-year efficacy signal (no pruritus/weight-loss recurrence) in a single adult patient is the strongest treatment-response data currently available, though it derives from a single case and should be treated as preliminary.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies exist beyond standard genetic counseling for known carrier couples (given full autosomal recessive inheritance) and, where a familial pathogenic variant is known, prenatal or preimplantation genetic testing could theoretically be offered — no specific literature on this practice for UNC45A/OOHE was identified in this session. No immunization, screening program, or public-health intervention is applicable to this monogenic disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring UNC45A-deficient disease has been reported in non-human species (companion animals, livestock, or wildlife) in the sources retrieved — OMIA and veterinary literature searches were not performed in this session and should be checked separately before asserting a negative finding definitively.

**Orthologous gene:** UNC45A has zebrafish (*unc45a*) and *Drosophila*, *C. elegans* orthologs (the UNC-45/CRO1/She4p — "UCS" — protein family is deeply conserved from yeast to human); vertebrates have duplicated into two paralogs, UNC45A (general/non-muscle) and UNC45B (striated-muscle-specific).

**Comparative biology:** The UCS-domain myosin-chaperone function is evolutionarily ancient and highly conserved (from the yeast She4 protein through *C. elegans* UNC-45 to human UNC45A/B), supporting strong translational validity of model-organism mechanistic findings, though the disease-specific epithelial/hepatocyte trafficking phenotype appears to be a vertebrate/mammalian-relevant elaboration rather than a universally conserved disease mechanism.

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*):** *unc45a* loss-of-function/mutant larvae recapitulate key enterocyte phenotypes — microvillus shortening, MVI-like (microvillus-inclusion-like) intracellular compartments, and Rab11 mislocalization — providing solid in vivo confirmation of the apical-trafficking mechanism [PMC9106349]. Notably, *unc45a* mutants do **not** show a muscle phenotype (unlike *unc45b* mutants), so zebrafish *unc45a* models are specifically useful for the epithelial/enteric arm of the disease, not for bone or hearing phenotypes, which remain less modeled.
- **Human iPSC-derived and CRISPR-engineered intestinal organoids (2D/3D):** UNC45A-knockout Caco-2 cells and patient-derived organoids are the best-characterized disease models, recapitulating MVID-like architecture (dense aggregates lacking central lumen, F-actin-positive inclusions, mislocalized apical transporters NHE3/DRA, disorganized brush border) [PMC9106349]. A more recent study used **primary human intestinal organoids from patients carrying biallelic UNC45A variants** to implicate CFTR in the pathogenesis of the intestinal phenotype [PMC12780477] — this paper's full methodological/quantitative detail could not be extracted in this session due to access restrictions and should be independently verified before citing specific findings.
- **Cell lines:** Caco-2 (intestinal epithelial) cells with CRISPR UNC45A knockout, plus MG132 proteasome-inhibitor treatment used to demonstrate myosin Vb aggregate formation upon UNC45A loss.
- **Model limitations:** No mouse model of UNC45A-related disease was identified in this session's searches (searches focused on zebrafish and organoid systems); bone- and cochlea-specific animal or cellular models of OOHE were not identified, representing a translational gap between the well-modeled enteric/hepatic mechanism and the less-mechanistically-explained skeletal/auditory phenotypes.
- **Research applications:** Organoid and zebrafish models are primarily used to dissect the myosin-chaperone-trafficking mechanism in enterocytes and to test candidate therapeutics (e.g., relevance to the CFTR-implicating organoid study, which may point toward CFTR-modulating drugs as a novel therapeutic avenue, though this requires direct verification of that paper's content).

---

## Notes on Evidence Gaps and Curation Caveats

Consistent with dismech's evidence-discipline requirements, the following should be **independently verified via primary-source fetch and exact-quote extraction** before being curated into a KB entry, since access restrictions in this session prevented full-text confirmation of several details:
1. The original 2018 Esteve et al. AJHG paper (PMID:29429573) abstract could not be directly fetched (ScienceDirect/PubMed blocked) — its exact founding cohort size, ages, and full phenotype table should be re-confirmed directly.
2. The OMIM entry and clinical synopsis (#619377) returned 403 errors and were reconstructed from MedGen/search-snippet cross-references only — the full OMIM clinical synopsis categories should be fetched directly (e.g., via an authenticated OMIM API key) before use as a curation source.
3. The CFTR-organoid paper (PMC12780477) content could not be extracted past a bot-check page; only its title/topic is confirmed.
4. No confirmed Orphanet (ORPHA) code was found for this entry in this session.
5. gnomAD constraint metrics (pLI/LOEUF) for UNC45A were not independently confirmed and should be pulled directly from the gnomAD browser.

## Sources

- [OMIM #619377 — Osteootohepatoenteric Syndrome](https://omim.org/entry/619377)
- [OMIM Clinical Synopsis #619377](https://www.omim.org/clinicalSynopsis/619377)
- [OMIM *611219 — UNC45A](https://omim.org/entry/611219)
- [MedGen C5543557 — Osteootohepatoenteric syndrome](https://www.ncbi.nlm.nih.gov/medgen/1785846)
- [MalaCards — Osteootohepatoenteric Syndrome](https://www.malacards.org/card/osteootohepatoenteric_syndrome)
- [Esteve et al. 2018 — Loss-of-Function Mutations in UNC45A Cause a Syndrome Associating Cholestasis, Diarrhea, Impaired Hearing, and Bone Fragility, AJHG, PMID:29429573](https://pubmed.ncbi.nlm.nih.gov/29429573/)
- [Esteve et al. bioRxiv preprint (2018)](https://www.biorxiv.org/content/10.1101/208942v1.full)
- [Case report: Osteo-oto-hepato-enteric syndrome caused by UNC45A deficiency (Chinese neonate), PMID:36699472, PMC9868473](https://pmc.ncbi.nlm.nih.gov/articles/PMC9868473/)
- [UNC45A deficiency causes microvillus inclusion disease–like phenotype by impairing myosin VB–dependent apical trafficking, PMC9106349](https://pmc.ncbi.nlm.nih.gov/articles/PMC9106349)
- [A Functional Relationship Between UNC45A and MYO5B Connects Two Rare Diseases With Shared Enteropathy, PMC9218578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9218578/)
- [Altered chaperone–nonmuscle myosin II interactions drive pathogenicity of the UNC45A c.710T>C variant in osteo-oto-hepato-enteric syndrome, JCI Insight, PMID:40125554, PMC11949031](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949031/)
- [Odevixibat treatment for recurrent cholestasis in a patient with biallelic UNC45A variants causing osteo-oto-hepato-enteric syndrome, PMC13019544](https://pmc.ncbi.nlm.nih.gov/articles/PMC13019544/)
- [A Case Report and Literature Review on Osteo‐Oto‐Hepato‐Enteric Syndrome in Premature Infants Caused by UNC45A Deficiency, PMC12516782](https://pmc.ncbi.nlm.nih.gov/articles/PMC12516782/)
- [A New UNC45A 5'UTR Variant in Patients with Aagenaes Syndrome, PMID:39887522](https://pubmed.ncbi.nlm.nih.gov/39887522/)
- [Primary human intestinal organoids with biallelic UNC45A variants suggest role of CFTR in pathogenesis of UNC45A‐related intestinal disorder, PMC12780477](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12780477/)
- [GeneCards — UNC45A](https://www.genecards.org/card/UNC45A)
- [Lack of Developmental Redundancy between Unc45 Proteins in Zebrafish Muscle Development, PMC3492250](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3492250/)
- [thegencc.org — UNC45A gene-disease submission](https://thegencc.org/submissions/SGC-114732.1)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9868473` *(abstract only)*: "relieve cholestasis by regulating bile acid transporters"
  - closest text in source: "Laboratory tests revealed highly elevated levels of total serum bilirubin (TB), direct bilirubin (DB), and total bile acid (TBA)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051082` (obsolete unfolded protein binding) (1 mention)
- `GO:0032313` (GO_0032313) (1 mention) - replaced by `GO:0043087`

28 of 30 terms resolved to a current term; the rest could not be looked up either way.