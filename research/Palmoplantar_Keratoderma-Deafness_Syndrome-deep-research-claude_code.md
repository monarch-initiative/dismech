---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-01T23:20:01.574527'
end_time: '2026-10-01T23:21:05.757011'
duration_seconds: 64.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Palmoplantar Keratoderma-Deafness Syndrome
  mondo_id: MONDO:0007852
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
  - claude-sonnet-5-5
  web_search_requests: 2
  num_turns: 4
  total_cost_usd: 0.7651502000000001
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
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
citation_count: 9
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Palmoplantar Keratoderma-Deafness Syndrome
- **MONDO ID:** MONDO:0007852 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Palmoplantar Keratoderma-Deafness Syndrome** covering all of the
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

# Palmoplantar Keratoderma-Deafness Syndrome: Research Report

**Verification status.** I ran two searches. The evidence base is the OMIM, GeneReviews, Bedoukian 2021 and PMC pages those searches returned, plus a PubMed E-utilities query. I did not open full texts. PMIDs that I did not retrieve are marked **[PMID not verified]**. Run `just fetch-reference` on them and quote snippets from the cached files. Do not copy snippets or CURIEs from this report. Every HP, GO, CL, UBERON, NCIT and CHEBI suggestion below is a lead from memory and must be looked up before binding. I have included no CURIEs for that reason.

**Scope.** I did not confirm that MONDO:0007852 is the right ID for this concept. Check it with `runoak` before using it. The OMIM entry is #148350 (autosomal dominant, GJB2). A mitochondrial form is associated with MT-TS1 and sits partly in the separate OMIM mitochondrial-deafness entries. See the lump/split note at the end.

## 1. Disease Information

- **Overview.** PPK with deafness is an autosomal dominant condition with sensorineural hearing loss and progressive hyperkeratosis of the palms and soles ([OMIM #148350](https://omim.org/entry/148350)). The hearing loss is slowly progressive and high-frequency.
- **Identifiers.**
  - OMIM #148350.
  - MGI/Disease Ontology DOID:0111505 ([MGI](https://informatics.jax.org/disease/148350)).
  - GenCC curates GJB2 against OMIM:148350 ([GenCC](https://search.thegencc.org/submissions/GENCC_000104-HGNC_4284-OMIM_148350-HP_0000006-GENCC_100002)).
  - Not verified: Orphanet, ICD and MeSH IDs.
- **Synonyms.** "Keratoderma, palmoplantar, with deafness" is the OMIM title. The related term "Bart-Pumphrey syndrome" is not the same entity. It is a GJB2-associated condition with knuckle pads and leukonychia, and I did not verify it.
- **Data source.** The data are aggregated disease-level and case-report resources, not EHR-derived.

## 2. Etiology

- **Causes.** The condition can be caused by mutation in GJB2 (connexin 26) or in the mitochondrial MT-TS1 gene (OMIM, above).
- **Genetic risk factors.**
  - GJB2 mutations are confined to a narrow spectrum. The affected codons are 59, 73 and 75 (OMIM, above).
  - Known variants: p.Gly59Ser (c.175G>A, also reported in a de novo Vohwinkel case, [PMC11745274](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11745274/)), p.Arg75Gln/Trp, and p.Asp50Asn (reported in KID syndrome, [PMC3750395](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3750395/)).
  - A GJB2 frameshift plus a novel missense variant gave a variable PPK-with-deafness phenotype ([Bedoukian 2021, Mol Genet Genomic Med](https://onlinelibrary.wiley.com/doi/10.1002/mgg3.1574)).
- **Environmental and protective factors.** None are established. Aminoglycoside exposure is a recognized modifier for MT-TS1 and mtDNA hearing loss in general, but I did not verify it for this entity.
- **Gene-environment interaction.** None documented here.

## 3. Phenotypes

Frequencies were not retrieved. Suggested HPO terms are to be looked up, not recalled.

| Phenotype | Notes | HPO term to look up |
|---|---|---|
| Palmoplantar keratoderma | Progressive. Mitochondrial form is described as scaling, hyperkeratosis and a honeycomb appearance of palms, soles and heels ([GeneReviews NBK1422](https://www.ncbi.nlm.nih.gov/sites/books/NBK1422/)). | "Palmoplantar keratoderma" |
| Sensorineural hearing impairment | Slowly progressive, high-frequency. MT-TS1 variants are usually childhood-onset. | "Sensorineural hearing impairment" |
| Variable additional features | Reported with GJB2 variants, including KID-spectrum overlap (see lump/split below). | Look up only if sourced |

Onset, severity and quality-of-life data were not retrieved.

## 4. Genetic/Molecular Information

- **GJB2 (HGNC symbol GJB2).** The CURIE is to be looked up, in lowercase `hgnc:` form. Inheritance is autosomal dominant. Variants are missense at codons 59, 73 and 75. The functional consequence is generally described as a dominant-negative or gain-of-function effect on connexin 26 hemichannels or gap junctions. I did not verify this here.
- **MT-TS1 m.7445A>G (mitochondrial tRNA-Ser(UCN)).**
  - Many relatives in one family had PPK plus deafness with m.7445A>G (OMIM, above).
  - In vitro studies indicate an endonucleolytic processing defect, caused by a non-cleavable C at the processing junction ([GeneReviews NBK1422](https://www.ncbi.nlm.nih.gov/sites/books/NBK1422/)).
  - A Portuguese family with deafness and PPK carried A7445G ([ResearchGate listing](https://www.researchgate.net/publication/7757245_A7445G_mtDNA_mutation_present_in_a_Portuguese_family_exhibiting_hereditary_deafness_and_palmoplantar_keratoderma)). [PMID not verified]
- **Modifier genes, epigenetics, chromosomal abnormalities.** None documented in what I retrieved.

## 5. Environmental Information

Nothing disease-specific was found. No infectious agents are implicated.

## 6. Mechanism / Pathophysiology (causal chains)

**GJB2 form**
1. A dominant missense variant (codon 59, 73 or 75) alters connexin 26. The change in channel behavior is inferred and not demonstrated here.
2. This leads to disrupted gap-junction or hemichannel function in the cochlea and epidermis.
3. In the cochlea, disrupted potassium and metabolite recycling leads to progressive hair-cell and supporting-cell dysfunction. This step is inferred.
4. The result is slowly progressive high-frequency sensorineural hearing loss.
5. In the epidermis, impaired keratinocyte differentiation and barrier function leads to progressive palmoplantar hyperkeratosis. Palms and soles are affected because GJB2 is highly expressed there. This is inferred.

**MT-TS1 form**
1. m.7445A>G places a non-cleavable C at the tRNA processing junction.
2. This results in an endonucleolytic processing defect in the mitochondrial tRNA-Ser(UCN) transcript.
3. This is inferred to impair mitochondrial translation and lower oxidative phosphorylation capacity in high-energy tissues. The cochlea is the best-documented target.
4. The result is childhood-onset sensorineural hearing loss.
5. Why only some families develop PPK is unexplained. It may reflect heteroplasmy or nuclear modifiers (speculative).

Candidate GO and CL concepts to look up: gap junction, connexin complex, mitochondrial tRNA processing, keratinocyte differentiation, inner ear hair cell, keratinocyte.

## 7. Anatomical Structures Affected

- **Organs.** Skin of the palms and soles (epidermis) and the inner ear (cochlea).
- **Cells.** Keratinocytes and cochlear hair cells or supporting cells.
- **Subcellular.** Plasma membrane gap junctions (GJB2) and mitochondria (MT-TS1).
- **Lateralization.** Bilateral, though I did not verify this.

## 8. Temporal Development

- Hearing loss is slowly progressive.
- PPK is progressive.
- Detailed natural-history data were not retrieved.

## 9. Inheritance and Population

- GJB2 form: autosomal dominant. Mitochondrial form: maternal inheritance.
- Prevalence, penetrance and founder data were not retrieved. The disorder is rare.
- The Cameroonian KID cases and the Portuguese mtDNA family show that both forms occur in different populations.

## 10. Diagnostics

- **Approach.** Audiometry plus dermatological examination, followed by genetic testing.
- **Genetic testing.** Sequence GJB2 first. Then test mtDNA MT-TS1, including m.7445A>G, which is offered as a clinical test ([Saint Francis lab listing](https://www.saintfrancis.com/physicians/laboratory-testing/molecular-genetics/available-tests/mitochondrial-hearing-loss-mtts1-gene)). Hearing-loss gene panels also cover both.
- **Differential.** Vohwinkel syndrome, KID syndrome and Bart-Pumphrey syndrome (all GJB2-related), and other PPK syndromes. I did not verify distinguishing features beyond this.

## 11. Outcome/Prognosis

No survival or quality-of-life data were retrieved. The hearing loss is progressive.

## 12. Treatment

I found no disease-specific trials. Management is supportive:

- **Hearing.** Hearing aids and, if needed, cochlear implantation. In dismech, bind the surgical action rather than the device term, per CLAUDE.md.
- **Skin.** Keratolytics and emollients. Oral retinoids are sometimes used for PPK. I did not verify this for this entity.
- **Aminoglycosides.** Avoid them in the mitochondrial form. This is a standard precaution for mtDNA hearing loss and is not verified for this entity.
- **Counseling.** Genetic counseling.
- NCIT terms need lookup. Candidates are the generic supportive-care and surgical-procedure terms already listed in CLAUDE.md.

## 13. Prevention

Genetic counseling with maternal-lineage counseling for the mitochondrial form. No primary prevention exists.

## 14. Other Species / Natural Disease

Not evaluated. Check OMIA before asserting any naturally occurring animal disease.

## 15. Model Organisms

Not evaluated. Mouse Gjb2 models exist, but I did not verify any that reproduce this dominant PPK-with-deafness phenotype. Check MGI.

## Curation Notes (lump/split)

- **GJB2 variants span several allelic syndromes.** Vohwinkel, KID, Bart-Pumphrey and PPK-with-deafness are all linked to GJB2, and the case reports above show phenotypic overlap. Apply the CLAUDE.md lump/split rules. A possible outcome is a `Grouping` of GJB2 keratoderma-deafness syndromes, with PPK-deafness as its own entry.
- **The mitochondrial form may need its own entry.** It differs on inheritance and mechanism, which meets the two-axis promotion rule. Alternatively, record it as a `has_subtypes` row with a pointer.
- **Remaining work.**
  1. Fetch the primary literature for the classic GJB2 PPK-deafness reports, the Portuguese m.7445A>G family paper and the GeneReviews chapter.
  2. Resolve the MONDO ID.
  3. Fill the missing sections (frequencies, epidemiology, models) before drafting the entry.

## Sources

- [OMIM #148350](https://omim.org/entry/148350)
- [GeneReviews: Nonsyndromic Hearing Loss and Deafness, Mitochondrial (NBK1422)](https://www.ncbi.nlm.nih.gov/sites/books/NBK1422/)
- [Bedoukian et al. 2021, Mol Genet Genomic Med](https://onlinelibrary.wiley.com/doi/10.1002/mgg3.1574)
- [Vohwinkel syndrome with de novo GJB2 p.Gly59Ser (PMC11745274)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11745274/)
- [GJB2 p.Asp50Asn in KID syndrome (PMC3750395)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3750395/)
- [GenCC GJB2–OMIM:148350 submission](https://search.thegencc.org/submissions/GENCC_000104-HGNC_4284-OMIM_148350-HP_0000006-GENCC_100002)
- [MGI disease page for 148350](https://informatics.jax.org/disease/148350)
- [Portuguese A7445G family (ResearchGate)](https://www.researchgate.net/publication/7757245_A7445G_mtDNA_mutation_present_in_a_Portuguese_family_exhibiting_hereditary_deafness_and_palmoplantar_keratoderma)
- PubMed query for "palmoplantar keratoderma deafness GJB2": 52 hits, 20 returned, including PMIDs 40667477, 35938034, 34916582, 33443819 and 31408183. I did not open or verify them.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007852` (2 mentions) - the report calls it "if available"; MONDO calls it **palmoplantar keratoderma-deafness syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.
