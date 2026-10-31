---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-23T14:03:24.754576'
end_time: '2026-10-23T14:04:33.931735'
duration_seconds: 69.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ACBD5 Deficiency
  mondo_id: MONDO:0100112
  category: Mendelian
  causal_genes: ACBD5
  omim_id: not recorded
  synonyms: Retinal dystrophy with leukodystrophy; RDLKD; Acyl-CoA binding domain
    containing protein 5 deficiency
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
  num_turns: 7
  total_cost_usd: 0.8232822000000001
  session_id: ba849568-e665-5205-8995-e1d1f294fec3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 5
  verified: 5
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
- **Disease Name:** ACBD5 Deficiency
- **MONDO ID:** MONDO:0100112 (if available)
- **Causal gene(s):** ACBD5
- **OMIM:** not recorded
- **Synonyms:** Retinal dystrophy with leukodystrophy; RDLKD; Acyl-CoA binding domain containing protein 5 deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ACBD5 Deficiency** covering all of the
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

# ACBD5 Deficiency (Retinal Dystrophy with Leukodystrophy, RDLKD): Research Report

**Causal gene: ACBD5** (acyl-CoA binding domain containing 5, HGNC `hgnc:23338`; the CURIE comes from memory and needs a lookup before use). It encodes a peroxisomal tail-anchored membrane protein. The disease is MONDO:0100112, as given in the brief.

**Method and reliability.** I ran three web searches and one PubMed listing. I did not read any abstract in full. Statements marked *(search summary)* come from search-engine summaries and need an exact-quote check with `just fetch-reference` before use as snippets. Statements marked *(background, unverified)* come from my own background knowledge and have no source. PMIDs are only those returned by the PubMed listing. I did not find a zebrafish model, so the model-organism section covers mouse only.

## 1. Disease information

- ACBD5 deficiency is an autosomal recessive peroxisomal disorder. Patients have retinal dystrophy, progressive white-matter disease, and in some cases ataxia, cleft palate, and other features.
- It was first described by Ferdinandusse et al. (J Med Genet 2017, PMID:27799409). The patient was a girl with progressive leukodystrophy, cleft palate, ataxia and retinal dystrophy. She had a homozygous ACBD5 indel with complete loss of the protein *(search summary)*.
- The same year, Yagita et al. (J Biol Chem 2017, PMID:27899449) reported the retinal dystrophy-associated ACBD5 defect in cells.
- Identifiers: OMIM 616618, as seen in a search-result URL, whose content I did not check. The brief says OMIM "not recorded", so confirm it. The glycosmos page maps the disease to DOID:0080946. I did not look up Orphanet, ICD or MeSH identifiers.
- Synonyms: retinal dystrophy with leukodystrophy (RDLKD); ACBD5 deficiency; acyl-CoA binding domain containing protein 5 deficiency.
- The data are individual patient reports and case series, not aggregate resources. About 7 cases had been reported when the Australian case report was written, and the later literature adds more *(search summary)*.

## 2. Etiology

- **Cause:** biallelic loss-of-function variants in ACBD5. No environmental causes, risk factors, protective factors or gene–environment interactions are documented. No modifier genes are documented in the sources I saw.
- **Reported variants:** Ferdinandusse 2017 (indel, complete protein loss); Gorukmez 2021 (PMID:34668366); Rudaks 2024 (PMID:37789430, novel mutations); Hasturk 2024 (PMID:38841324, novel homozygous variant); and the Omani series, Al Shamsi (PMID:42343915). I did not extract the HGVS descriptions, so pull them from the primary papers or ClinVar.

## 3. Phenotypes (candidate HPO terms need lookup)

| Phenotype | Notes | Candidate HPO term (from memory, unverified) |
|---|---|---|
| Retinal dystrophy / cone-rod dystrophy | Infantile presentation with nystagmus and photophobia, progressing to legal blindness; severe cone-rod dystrophy on ERG (Omani series) *(search summary)* | Cone-rod dystrophy; Nystagmus; Photophobia |
| Leukodystrophy | Diffuse T2 signal abnormality in deep white matter, with corticospinal tract involvement *(search summary)* | Leukodystrophy |
| Ataxia | Index patient | Ataxia |
| Cleft palate | Index patient | Cleft palate |
| Mildly raised plasma VLCFA | Mild elevation of C26 and the C26/C22 ratio, so plasma testing can be unremarkable *(search summary)* | Abnormal circulating very long-chain fatty acid concentration |

Frequencies per phenotype are not available because the cohorts are small. Onset is infantile or childhood, and the disease is progressive. One patient was diagnosed in adulthood by exome sequencing *(search summary)*. Quality-of-life data were not found.

## 4. Genetic and molecular information

- **Gene and protein:** ACBD5 is a peroxisomal membrane protein with an N-terminal cytosolic acyl-CoA binding domain. It also has an FFAT-like motif that binds the ER protein VAPB.
- **Variants and consequence:** reported variants are loss-of-function. Ferdinandusse reported complete protein loss. I did not obtain gnomAD frequencies, ClinGen validity or ACMG classifications.
- **Not applicable or not found:** epigenetic and chromosomal data.
- **Related gene:** ACBD4 paralogue work is in Kors 2024 (PMID:39271061). ACBD6 variants cause a distinct neurodevelopmental syndrome (Kaiyrzhanov 2024, PMID:37951597) and should not be confused with this disease.

## 5. Environmental information

No environmental, lifestyle or infectious factors have been reported.

## 6. Mechanism and pathophysiology

**Causal chain.**

1. Biallelic loss-of-function variants in ACBD5 abolish the protein (demonstrated; Ferdinandusse 2017).
2. This leads to impaired peroxisomal β-oxidation of VLCFA. Knockout of ACBD5 in HeLa cells showed that ACBD5 binds VLC-CoAs and mediates their peroxisomal β-oxidation *(search summary)*. Peroxisome biogenesis is unaffected in patient fibroblasts *(search summary)*.
3. A mechanistic explanation is proposed: ACBD5 holds C26-CoA in the cytosol so that it can reach the peroxisome *(search summary)*. The authors describe this as a proposal, and the Exeter abstract says the precise role is not yet established.
4. Loss of ACBD5 also reduces peroxisome–ER contacts, because ACBD5 tethers peroxisomes to the ER through VAPB (Hua et al. and Costello et al., J Cell Biol 2017; PMIDs not confirmed). Loss of the tether increases peroxisome motility *(search summary)*. This step is demonstrated in cells. Whether the loss of contacts or the VLCFA defect matters more for disease is inferred and not settled.
5. VLCFA and ultra-long-chain lipids accumulate in tissues. In mice, C>32 species accumulate in cerebellar phosphocholines but not in liver (Darwisch 2020, PMID:33244184) *(search summary)*.
6. In the retina, very long-chain polyunsaturated fatty acids accumulate in the plexiform layers, not the photoreceptor outer segments. The authors link this to photoreceptor synapse degeneration and neuroinflammation (Merz 2025, PMID:41324649) *(search summary)*.
7. The result is retinal degeneration with glial activation, and cerebellar and white-matter disease (inferred from the mouse and patient data).

**Where the mechanism branches:** the retinal branch (VLC-PUFA, synapse loss, neuroinflammation) and the neural branch (cerebellar and corticospinal pathology, axonopathy). Both start at the VLCFA and contact-site defect.

**Suggested GO terms (from memory, unverified):**
- peroxisomal fatty acid β-oxidation, very-long-chain fatty acid metabolic process, and peroxisome–ER membrane contact site organization.
- Cell types: photoreceptor, bipolar cell, retinal ganglion cell, RPE cell, Müller glia, Purkinje cell, oligodendrocyte.

The Frontiers 2025 review (Dawes, PMID:40672445) covers patients and mouse models together. I did not find omics datasets.

## 7. Anatomical structures affected

- **Eye:** retina (photoreceptors, inner retina, RPE).
- **Brain:** deep white matter, corticospinal tracts, cerebellum.
- **Palate:** cleft palate in the index patient.
- **Subcellular:** peroxisomal membrane, ER contact sites.
- Bilateral involvement is the likely pattern, but I did not find a source for it.

## 8. Temporal development

Onset is in infancy to childhood, with progression to legal blindness. White-matter disease is progressive. The course is chronic and lifelong. I did not find staging, remission patterns or critical periods.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Consanguinity:** it plays a role in the Omani series, which is homozygous and from one population *(search summary)*. The Omani cases may point to a founder effect, but I did not verify this.
- **Frequency:** the disease is ultra-rare. I found no prevalence, incidence, carrier frequency, penetrance or sex-ratio data.

## 10. Diagnostics

- **Plasma VLCFA:** changes are only mild (C26 and the C26/C22 ratio), so a normal or near-normal profile does not exclude the disease *(search summary)*.
- **Patient fibroblasts:** they show reduced peroxisomal β-oxidation and elevated VLCFA (Ferdinandusse 2017; Herzog 2018, PMID:28849344, on lipidomics of fibroblasts).
- **Genetic testing:** exome or genome sequencing, or a leukodystrophy or retinal dystrophy gene panel including ACBD5. One adult was diagnosed by exome *(search summary)*.
- **Other tests:** ERG (cone-rod pattern) and brain MRI (white-matter signal change).
- **Differential diagnosis:** other peroxisomal disorders, X-linked adrenoleukodystrophy, and other leukodystrophies with retinopathy (*background, unverified*).

## 11. Prognosis

The disease is progressive, with visual loss to legal blindness. Long-term neurological data and survival data are not available. I did not find quality-of-life data.

## 12. Treatment

- **No approved disease-specific treatment was found.**
- **Preclinical:** Granadeiro et al. (Brain 2024, PMID:38066620) report ataxia with giant axonopathy in Acbd5-deficient mice, halted by adeno-associated virus gene therapy. This is model-organism evidence only.
- **Supportive care:** low-vision services, rehabilitation, and neurological follow-up (*background, unverified*).
- **Not found:** clinical trials (NCT) and NCIT intervention terms.
- **Suggested NCIT terms (from memory, unverified):** gene therapy NCIT:C15238; supportive care NCIT:C15747; genetic counseling NCIT:C15240.

## 13. Prevention

Genetic counseling is appropriate for an autosomal recessive disorder, with carrier testing in families and prenatal or preimplantation testing where requested (*background, unverified*). I found no newborn screening or immunization data.

## 14. Other species and natural disease

I found no natural disease in other species and did not search OMIA. Orthologs exist, with the mouse gene being Acbd5 (a commercial knockout is listed for C57BL/6J) *(search summary)*.

## 15. Model organisms

- **Mouse (Acbd5-deficient)** (Darwisch 2020, PMID:33244184):
  - Raised VLCFA and a progressive cerebellar pathology.
  - The liver has more peroxisomes but fewer peroxisome–ER contacts.
  - Ultra-long-chain fatty acids accumulate in the cerebellum but not the liver.
  - This model recapitulates the neurological features, but I did not confirm retinal and white-matter parity.
- **Retinal findings in mice:** moderate degeneration of photoreceptor, bipolar, ganglion and RPE cells with prominent glial activation; accumulation of VLC-PUFA in the plexiform layers (Merz 2025, PMID:41324649) *(search summary)*.
- **Axonopathy and gene therapy:** Granadeiro 2024, PMID:38066620.
- **Cell models:** HeLa knockout cells and patient fibroblasts. Peroxisome biogenesis is intact in patient fibroblasts *(search summary)*.
- **Zebrafish and other models:** none found.
- **Limitation:** the mouse phenotype is dominated by cerebellar and axonal pathology. Fidelity to human leukodystrophy and cone-rod dystrophy is uncertain.

## Reference list

PMIDs below come from the PubMed listing.

- 27799409 – Ferdinandusse S et al., J Med Genet 2017: first patient report.
- 27899449 – Yagita Y et al., J Biol Chem 2017: ACBD5 deficiency in cells.
- 28849344 – Herzog K et al., J Inherit Metab Dis 2018: fibroblast lipidomics.
- 33244184 – Darwisch W et al., Commun Biol 2020: mouse cerebellum and liver.
- 34668366 – Gorukmez O et al., J Pediatr Endocrinol Metab 2021: new patient.
- 37789430 – Rudaks LI et al., Am J Med Genet A 2024: novel mutations.
- 38841324 – Hasturk BA et al., Mol Syndromol 2024: novel homozygous variant.
- 38066620 – Granadeiro L et al., Brain 2024: AAV gene therapy in mice.
- 39271061 – Kors S et al., BBA Mol Cell Res 2024: ACBD4/5-like proteins.
- 40672445 – Dawes ML et al., Front Mol Neurosci 2025: review.
- 41324649 – Merz J et al., Cell Mol Life Sci 2025: retinal VLC-PUFA.
- 42343915 – Al Shamsi B et al., Oman Med J 2026: Omani case series.

**Sources:** [Exeter repository: Ferdinandusse 2017](https://ore.exeter.ac.uk/repository/handle/10871/23869) · [Frontiers review 2025](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2025.1602343/pdf) · [Mouse paper, PMC7691522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7691522/) · [JCB 2022 on ACBD5 regulation](https://rupress.org/jcb/article/221/3/e202003143/212956/Regulating-peroxisome-ER-contacts-via-the-ACBD5) · [JCB 2017 ACBD5 and VAPB](https://rupress.org/jcb/article-split/216/2/331/46166/ACBD5-and-VAPB-mediate-membrane-associations) · [OMIM 616618](https://https.ncbi.nlm.nih.gov/omim/616618) · [PubMed listing](https://pubmed.ncbi.nlm.nih.gov/?term=ACBD5+deficiency&sort=date&size=50)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.