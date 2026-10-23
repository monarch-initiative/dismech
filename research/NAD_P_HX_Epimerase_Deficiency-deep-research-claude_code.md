---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T19:14:31.464534'
end_time: '2026-10-15T19:15:24.268059'
duration_seconds: 52.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: NAD(P)HX Epimerase Deficiency
  mondo_id: MONDO:0020781
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.6912183999999999
  session_id: a4618dfa-d284-5dfb-b077-0a3b19b97962
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NAD(P)HX Epimerase Deficiency
- **MONDO ID:** MONDO:0020781 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **NAD(P)HX Epimerase Deficiency** covering all of the
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

# NAD(P)HX Epimerase Deficiency (NAXE deficiency; PEBEL1): research report

**Scope and provenance.** I ran three standard web searches: one on the disease, one on NAXD, and one on Kremer 2016. I did not fetch any full text.
- Claims tagged **[search]** come from search-result summaries. Those summaries were generated by the search tool, and I did not open the primary papers.
- Claims tagged **[memory]** are from my recall. They are leads, not verified.
- Sections 6–15 are mostly thin. Where I found nothing, I say so rather than substitute adjacent material.
- **No identifier was checked in this session.** That includes the MONDO ID in your template (`MONDO:0020781`), HP/GO/CL/UBERON/NCIT CURIEs and OMIM/ORPHA numbers. Look each one up (`runoak`, caches) before binding.

## 1. Disease information

- NAXE deficiency is an autosomal recessive neurometabolic disorder caused by biallelic variants in *NAXE* (formerly *APOA1BP*). It is also called PEBEL1, early-onset progressive encephalopathy with brain edema and/or leukoencephalopathy 1 [search: [KEGG H02262](https://www.kegg.jp/entry/H02262), [Zhu 2026](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1766864/full)].
- It is a metabolite-repair disorder. The NAD(P)HX repair pathway has two enzymes, NAXE (epimerase) and NAXD (dehydratase). Deficiency of either one causes a distinct disease.
- Fewer than 40 cases had been reported by a 2026 report [search: Zhu 2026]. A 2021 review counted 18 [search: [PMC8542128](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8542128/)].
- **Identifiers not verified:** OMIM (I recall 617186 for PEBEL1 [memory]), Orphanet, MeSH and the ICD codes.
- **Lump/split call to make:** NAXE deficiency (PEBEL1) and NAXD deficiency are separate genes and separate entities. The NAXD paper (Van Bergen 2019, DOI 10.1093/brain/awy310) describes its own disease [search: [ORBilu](https://orbilu.uni.lu/handle/10993/37920)]. I recall NAXD being PEBEL2 [memory, unverified]. I recommend separate entries, possibly with a shared mechanism module for NAD(P)HX repair failure.
- Check whether `MONDO:0020781` is the NAXE entity before using it.

## 2. Etiology

- **Cause:** Biallelic *NAXE* variants cause loss of NAD(P)HX epimerase activity [search: [Kremer 2016, AJHG, PMC5065653](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065653)].
- **Environmental trigger:** Febrile infection triggers onset and each episode of deterioration (Kremer 2016 summary, below).
- **Risk and protective factors:** No other data found.
  - Heat or fever as a damage-promoting stressor comes from the NAXD paper [search: Van Bergen 2019]. It is plausible for NAXE but not demonstrated here.
  - No protective variants or modifier genes were found.
  - Niacin and nicotinamide are covered under treatment.

## 3. Phenotypes

From Kremer 2016 (human clinical, 4 families) [search]:
- Onset in the second year of life, with (sub)acute ataxia.
- Cerebellar edema, spinal myelopathy and skin lesions.
- Deterioration triggered by febrile infection.
- A rapidly progressive course leading to coma, global brain atrophy and death in all affected individuals.

Other reports:
- Respiratory failure, seizures and neurodevelopmental regression [search: Zhu 2026].
- A milder, long-surviving phenotype: a 24-year-old man with infant-onset decompensations during infections, then improvement and residual cerebellar dysfunction [search: [Almudhry 2024](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1204848/full)].

**Frequencies, QoL data and HPO term assignment were not retrieved.** The skin lesion type, which I recall as ichthyosiform or erythematous [memory], needs confirmation. Do not assign HPO terms from this report without lookup.

## 4. Genetic/molecular information

- **Gene:** *NAXE* (HGNC symbol; the CURIE is not verified, so use the `hgnc:` lowercase form after lookup).
- **Variants:** Kremer 2016 and the later reports describe homozygous or compound-heterozygous variants. The 2024 milder case carried a homozygous missense variant [search]. I did not retrieve specific variants, ClinVar classifications, gnomAD frequencies or a ClinGen validity tier. Check ClinGen and cache a `CGGV:` record if one exists. I did not check whether one does.
- **Functional consequence:** Loss of function. In fibroblasts from two families, NAXE was undetectable and cyclic-NADHX was highly elevated [search: Kremer 2016].
- **Modifier genes, epigenetics, chromosomal abnormalities:** Nothing found.

## 5. Environmental information

- **Febrile illness** is the one documented trigger (Kremer 2016; Zhu 2026) [search].
- No toxin, lifestyle or infectious-agent data was found. The triggering infections are non-specific.

## 6. Mechanism / pathophysiology

1. Biallelic *NAXE* variants cause loss of NAD(P)HX epimerase [search: Kremer 2016].
2. Heat or metabolic stress spontaneously converts NADH and NADPH to the damaged forms S-NADHX and S-NADPHX. These forms are normally epimerized to the R form and then dehydrated back to NAD(P)H by NAXD. This is the pathway biochemistry [memory]. The NAXD paper states it for NAXD [search].
3. Without the epimerase, the S-epimers accumulate. Cyclic-NADHX is the elevated marker in patient fibroblasts [search: Kremer 2016].
4. Accumulated NAD(P)HX derivatives are toxic. For NAXD, the authors state that the accumulation "likely" damages the brain and heart [search]. Inferred for NAXE; mitochondrial impairment is demonstrated in NAXD fibroblasts, not in NAXE here.
5. Fever raises the rate of damage formation, which would explain acute decompensation. This is an inference. I did not retrieve any direct measurement showing that fever increases NAD(P)HX formation in NAXE patients.
6. Brain edema, leukoencephalopathy and cerebellar involvement follow, with myelopathy, then coma and death [search: Kremer 2016].

I did not find molecular profiling, single-cell data or screen data. The cell types for the CL terms are not established here. Likely GO and CHEBI candidates are NAD(P)HX epimerase activity and NADHX, but these are unverified.

## 7. Anatomical structures affected

- Cerebellum (edema), spinal cord (myelopathy), global brain (atrophy) and skin [search: Kremer 2016].
- NAXD deficiency also affects the heart [search]. A cardiac phenotype for NAXE is not established here.
- Subcellular localization (cytosol or mitochondria): not retrieved.
- Lateralization: not found. Bilateral CNS involvement is reported, but I did not verify it.

## 8. Temporal development

- Onset is typically in infancy or early childhood. Kremer 2016 reports the second year of life [search].
- The course is episodic decompensation after infection with incomplete recovery.
- The classic course is fatal in early childhood (coma and death, within 3 years in one source) [search].
- Longer survival with stable residual cerebellar dysfunction has been reported [search: Almudhry 2024].
- The "first 3 years of life" figure comes from a search summary and may not match the primary source.

## 9. Inheritance and population

- Autosomal recessive.
- Prevalence and incidence are not established. Fewer than 40 reported cases indicates an ultra-rare disease [search].
- I found no data on founder variants, consanguinity, carrier frequency or sex ratio. Kremer's families are said to be of varied origin [memory, unverified].

## 10. Diagnostics

- **Biochemical:** The elevated cyclic-NADHX in fibroblasts is research-level. A clinical metabolite assay was not found.
- **Genetic:** Exome or genome sequencing. One abstract urges early genome testing because niacin may improve outcomes [search: AAN abstract, Hanna].
- **Imaging:** MRI shows cerebellar edema and leukoencephalopathy (the PEBEL name).
- **Differential diagnosis:** Post-infectious cerebellar ataxia, which one 2025 AAN case report found it masquerading as [search: [AAN 2025](https://index.mirasmart.com/AAN2025/PDFfiles/AAN2025-004442.html)]. Other metabolic encephalopathies are also possible.
- Newborn and carrier screening: not found. LOINC and test-registry data were not searched.

## 11. Prognosis

- The classic course is fatal in childhood. This rests on 4 families in Kremer 2016 [search].
- Survival into adulthood is reported in milder cases [search: Almudhry 2024].
- No registry or QoL data was found.

## 12. Treatment

- **Disease-specific:** No approved therapy was found.
- **Niacin or nicotinamide:** Case-level reports only.
  - One abstract reports symptom stabilization after niacin [search: AAN abstract].
  - A 2024 case report suggests niacin as supportive therapy [search: Almudhry 2024].
  - High-dose nicotinamide has been reported to improve two patients [search], but I did not identify those publications.
  - Treat these as uncontrolled, low-grade evidence (single cases or small series).
- **Immunomodulatory plus mitochondrial cofactor therapy:** One 2026 case report describes near-complete motor recovery [search: Zhu 2026]. It is a single case, and the recovery cannot be attributed to a specific component.
- **Fever management and supportive care:** Plausible given the mechanism, but I found no source recommending a specific protocol.
- No trials (NCT) were searched. Check ClinicalTrials.gov before stating that none exist.
- NCIT terms for these treatments were not looked up.

## 13. Prevention

- Genetic counseling and carrier testing follow from autosomal recessive inheritance. This is general reasoning, not a sourced finding.
- Early fever control and prompt treatment of infections would follow from the mechanism, but no source I retrieved recommends it.

## 14. Other species

Not searched: OMIA, orthologs and veterinary reports.

## 15. Model organisms

Not searched. I did not retrieve any mouse, zebrafish or other model for *NAXE*. Do not assume one exists.

## Gaps and verification list

1. Fetch the Kremer 2016 full text ([PMC5065653](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065653)). Take the PMID, variants and exact snippets from the cached `just fetch-reference` file.
2. Fetch Van Bergen 2019 (Brain, DOI 10.1093/brain/awy310). A bibliographic database record gave "30576410", which is probably its PMID but is not stated in the results I saw. Confirm it. Use it only for the NAXD sibling entry.
3. Spiegel et al. 2016 is reported to have described NAXE variants as well. My search could not confirm it, so I cite nothing from it. Locate it by PubMed search.
4. Confirm the following in structured sources, with a quote from each: OMIM and Orphanet entries, the HPO annotations and frequencies, ClinGen gene-disease validity, the GeneReviews situation (`just check-genereviews`), and the MONDO ID.
5. Locate the primary papers behind the nicotinamide claims. Until then they are leads.

## Sources

- [Kremer et al. 2016, AJHG (PMC5065653)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065653)
- [NAXE case report and review (PMC8542128)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8542128/)
- [Almudhry et al. 2024, Front Neurol](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1204848/full)
- [Zhu et al. 2026, Front Pediatr](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1766864/full)
- [KEGG H02262](https://www.kegg.jp/entry/H02262)
- [AAN 2025 abstract](https://index.mirasmart.com/AAN2025/PDFfiles/AAN2025-004442.html)
- [Van Bergen 2019 NAXD record (ORBilu)](https://orbilu.uni.lu/handle/10993/37920)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.