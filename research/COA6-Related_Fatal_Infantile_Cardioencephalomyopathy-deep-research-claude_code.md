---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T13:24:23.720892'
end_time: '2026-09-10T13:28:58.881505'
duration_seconds: 275.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: COA6-Related Fatal Infantile Cardioencephalomyopathy
  mondo_id: MONDO:0014668
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
  web_search_requests: 23
  num_turns: 30
  total_cost_usd: 1.5888039999999997
  session_id: 9e69cc81-c7bf-5849-9c45-54bef1e4f4c3
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COA6-Related Fatal Infantile Cardioencephalomyopathy
- **MONDO ID:** MONDO:0014668 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COA6-Related Fatal Infantile Cardioencephalomyopathy** covering all of the
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

I'll research this now using web search and fetch tools, then compile the full report inline.

I now have comprehensive material. Compiling the full research report.

# COA6-Related Fatal Infantile Cardioencephalomyopathy — Comprehensive Research Report

## 1. Disease Information

**Overview:** COA6-related fatal infantile cardioencephalomyopathy is an ultra-rare, autosomal recessive mitochondrial disease caused by biallelic pathogenic variants in *COA6* (Cytochrome C Oxidase Assembly Factor 6). It belongs to the family of isolated mitochondrial complex IV (cytochrome c oxidase, COX) deficiencies and manifests in the neonatal period with severe hypertrophic cardiomyopathy (often with left ventricular non-compaction), lactic acidosis, and hypotonia, typically progressing to death within the first weeks of life ([OMIM #616501](https://www.omim.org/entry/616501)).

**Key identifiers:**
- **OMIM disease entry:** #616501 — Mitochondrial Complex IV Deficiency, Nuclear Type 13 (MC4DN13)
- **OMIM gene entry:** *614772 — CYTOCHROME c OXIDASE ASSEMBLY FACTOR 6; COA6
- **MONDO:** MONDO:0014668
- **Orphanet:** The gene page [Orphanet: COA6](https://www.orpha.net/en/disease/gene/COA6) links COA6 to "Fatal infantile cytochrome C oxidase deficiency" (ORPHA:1561), the broader clinical category shared with SCO2, COX15, and related genes
- **MedGen concept:** related concepts include C3554534 ("Cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency 2") — note that different databases (OMIM, MedGen, ClinVar) use slightly inconsistent numeric suffixes ("2" vs "4") for this entity across sources; curators should not over-interpret the exact ordinal without cross-checking the specific database version
- **HGNC:** HGNC:18025
- **Entrez/NCBI Gene ID:** 388753
- **Cytogenetic location:** 1q42.2 (GRCh38 chr1:234,373,456–234,385,080)
- **Gene aliases:** *C1orf31*

**Synonyms for the disease:** Mitochondrial complex IV deficiency, nuclear type 13 (MC4DN13); COX deficiency due to COA6 mutation; COA6-related cardiomyopathy; cytochrome c oxidase deficiency, COA6-related.

**Evidence basis:** Nearly all clinical knowledge derives from two published index families (individual case reports with segregating genetics, functional cell/model validation) rather than large aggregated cohorts — this is a genuinely ultra-rare, single-gene Mendelian disorder with only a handful of molecularly confirmed patients in the literature.

---

## 2. Etiology

**Primary cause:** Biallelic (homozygous or compound heterozygous) loss-of-function pathogenic variants in *COA6*, which disrupt the copper-dependent biogenesis of mitochondrial complex IV subunit COX2 (MT-CO2), causing isolated complex IV (cytochrome c oxidase) deficiency.

**Genetic risk factors:**
- Autosomal recessive inheritance — both parents are obligate heterozygous carriers, typically clinically unaffected.
- **Consanguinity** is a documented risk factor: the second reported family (Baertling et al., 2015) involved "a female infant born of consanguineous parents of Arab descent" with a homozygous *COA6* variant, illustrating the classic recessive-disease enrichment pattern in consanguineous unions.
- No modifier genes have yet been identified, though functional work shows genetic/biochemical interaction with *SCO1* and *SCO2* (see Mechanism), raising the theoretical possibility that variation in these interacting genes could modulate phenotype severity, though this has not been demonstrated clinically.

**Environmental/other risk factors:** None established; this is a purely monogenic disorder with no known environmental, infectious, or lifestyle contribution to disease causation.

**Protective factors:** None specifically documented for COA6 deficiency. By analogy to the related disorder SCO2 deficiency, **copper** has been explored as a potential ameliorating cofactor at the cellular level (see Treatment/Mechanism sections), but this is a pharmacological/therapeutic avenue rather than a naturally occurring protective factor.

**Gene-environment interactions:** None reported. Disease penetrance and severity in the reported cases appear to be driven by variant type (truncating/null vs. specific missense) rather than by environmental modifiers.

---

## 3. Phenotypes

### Cardiac phenotypes
- **Hypertrophic cardiomyopathy** — onset in the neonatal period (birth to first days of life), severe, biventricular. Described in both index families as the dominant and life-limiting feature.
  - HPO: **Hypertrophic cardiomyopathy (HP:0001639)**; **Biventricular hypertrophy (HP:0001725)** as applicable
- **Left ventricular non-compaction** — echocardiography in the Baertling et al. patient showed "severe hypertrophic cardiomyopathy affecting both ventricles with some areas of noncompaction in the left ventricle."
  - HPO: **Left ventricular noncompaction cardiomyopathy (HP:0006955)**
- **Valvular insufficiency** — mitral, tricuspid, and pulmonic insufficiency reported on echocardiography.
  - HPO: **Mitral regurgitation (HP:0031628)**; **Tricuspid regurgitation (HP:0025166)**; **Pulmonic regurgitation** (as applicable)
- Onset: **congenital/neonatal**, present at birth or emerging within the first days of life. Severity: **severe**, rapidly progressive, fatal.

### Systemic/metabolic phenotypes
- **Lactic acidosis** — severe, appearing soon after birth in both families; a core biochemical hallmark of the mitochondrial respiratory chain defect.
  - HPO: **Lactic acidosis (HP:0003128)**
- **Hypothermia** and **tachypnea** — reported in the neonatal presentation.
  - HPO: **Hypothermia (HP:0002045)**; **Tachypnea (HP:0002789)**
- **Metabolic/muscular hypotonia** — "muscular hypotonia" was described in the Baertling patient; systemic floppiness consistent with mitochondrial myopathy.
  - HPO: **Hypotonia (HP:0001252)**; **Neonatal hypotonia (HP:0001319)**
- **Failure to thrive / weakness** — general OMIM clinical synopsis notes "hypotonia, weakness, and failure to thrive, resulting in death in infancy."
  - HPO: **Failure to thrive (HP:0001508)**

### Neurologic/encephalopathic phenotypes ("encephalo-" component)
- Encephalopathic features are part of the disease name ("cardioencephalomyopathy"), reflecting CNS involvement alongside the cardiac and muscular phenotype, consistent with generalized mitochondrial energy failure affecting high-energy-demand tissues (brain, heart, skeletal muscle).
  - HPO candidate terms: **Encephalopathy (HP:0001298)**

### Other/dysmorphic
- **Mild dysmorphic features** and **systolic murmur** noted at birth in at least one patient.
  - HPO: **Systolic murmur (HP:0033553_or similar)**; **dysmorphic features** (nonspecific, general term)

### Phenotype characteristics
- **Age of onset:** Neonatal (birth to first days of life) in both reported families — this is a uniformly neonatal-onset, not later-onset, disorder based on current literature.
- **Severity:** Uniformly severe/fatal in the reported cases; no attenuated or later-onset COA6 phenotype has yet been published (contrast with the related gene *COX6B1* or milder complex IV deficiencies).
- **Progression:** Rapidly progressive — both index patients died in infancy/early weeks of life.
- **Frequency among affected individuals:** Because only two molecularly confirmed families have been published, frequency estimates for individual phenotypes (e.g., "X% have LVNC") cannot be reliably calculated; the phenotypes above were present in the majority/all of the very small number of reported cases.
- **Quality of life impact:** Given the fatal, rapidly progressive neonatal course, quality-of-life impact is profound but of very short duration (days to weeks); no structured QOL instrument data (EQ-5D, etc.) exist for this ultra-rare condition.

---

## 4. Genetic/Molecular Information

**Causal gene:** *COA6* (HGNC:18025; Entrez Gene 388753; chromosome 1q42.2; OMIM *614772).

**Reported pathogenic variants (both from the two founding case reports):**

| Family | Variant(s) | Zygosity | Predicted consequence | Reference |
|---|---|---|---|---|
| Ghosh et al. 2014 (male infant) | c.177G>C (p.Trp59Cys, **W59C**) + c.259G>T (p.Glu87Ter, **E87X**) | Compound heterozygous | W59C: missense at a conserved residue causing mistargeting to the mitochondrial matrix and disruption of SCO2/COX2 interactions; E87X: nonsense/truncating, producing a truncated protein lacking the fourth cysteine of the conserved twin CX9C cysteine motif | PMID:25339201 |
| Baertling et al. 2015 (female infant, consanguineous, Arab descent) | c.196T>C (p.Trp66Arg, **W66R**) | Homozygous | Missense substitution at a conserved tryptophan; results in absence of COA6 protein in patient fibroblasts and reduced complex IV | (OMIM #616501; described via PMID search) |
| Additional ClinVar entry | c.373-8dup | — | Listed under "Cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency" in ClinVar (RCV001584195) | ClinVar |

**Variant classification:** All reported disease-causing variants are classified as pathogenic per functional and segregation evidence (ACMG/AMP framework implied by ClinVar submissions), though formal multi-lab ClinVar consensus classification data for each variant were not independently retrieved in this search.

**Allele frequency in population databases:** *COA6* is not listed among genes with notable population allele frequency data readily surfaced by general search; given the extreme rarity of the disease (only 2 published families) and the severity of the phenotype (fatal in infancy), pathogenic *COA6* alleles are expected to be present at very low frequency in gnomAD, consistent with a severe recessive lethal disorder. Direct gnomAD constraint metrics (o/e, pLI) for *COA6* were not confirmed in this search and should be verified directly at gnomad.broadinstitute.org before citation in a KB entry.

**Somatic vs. germline:** All reported variants are germline (inherited, biallelic); no somatic/postzygotic mosaic cases have been reported.

**Functional consequences — loss of function is the unifying mechanism:**
- Both the W59C+E87X compound heterozygous genotype and the homozygous W66R genotype behave as **loss-of-function** alleles.
- Functional/yeast complementation: mutant *COA6* alleles "were unable to rescue mitochondrial respiratory growth defect in Coa6-null yeast, consistent with a loss of function" (functional_impact_category candidate: `LOSS_OF_FUNCTION` / `PARTIAL_LOSS_OF_FUNCTION` depending on variant).
- The W59C variant specifically causes **protein mistargeting** — instead of localizing correctly to the mitochondrial intermembrane space, mutant COA6 is mistargeted to the mitochondrial matrix, disrupting its normal interactions with SCO2 and newly synthesized COX2 (a distinct, more complex loss-of-function mechanism beyond simple protein instability).
- Patient fibroblasts (W66R) show **complete absence of COA6 protein**, consistent with a null/amorphic allele via nonsense-mediated decay or protein instability.

**Modifier genes:** None formally established in patients; however, cell-based studies show a direct biochemical/genetic interaction between COA6 and *SCO2* — “Mitochondrial disease genes COA6, COX6B and SCO2 have overlapping roles in COX2 biogenesis” (PMID:26669719) and "Cooperation between COA6 and SCO2 in COX2 Maturation... Links Two Mitochondrial Cardiomyopathies" (Pacheu-Grau et al., 2015, *Cell Metabolism* 21:823-833, PMID:25959673), suggesting SCO2 variants could theoretically modify COA6-disease expressivity, though this is not clinically demonstrated.

**Epigenetic information:** No epigenetic (DNA methylation, histone modification) contribution to COA6-related disease has been reported; this is a straightforward loss-of-function Mendelian gene defect.

**Chromosomal abnormalities:** None reported; disease is caused by point mutations (missense, nonsense) rather than large structural/copy-number changes.

---

## 5. Environmental Information

No environmental factors, toxins, lifestyle exposures, or infectious triggers have been implicated in COA6-related disease causation or exacerbation. This is consistent with its status as a pure monogenic mitochondrial disorder. (Note for curation: given the KB's environmental-evidence discipline, this section should likely remain unpopulated or explicitly noted as "no evidence of environmental contribution identified in literature search" rather than speculatively populated.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic *COA6* variants** (e.g., homozygous W66R, or compound heterozygous W59C/E87X) → **loss of functional COA6 protein** in the mitochondrial intermembrane space (via mistargeting, truncation, or instability/absence).
2. Loss of COA6 → **failure of COA6's thiol-reductase/copper-relay function** — COA6 normally acts as a thiol-disulfide oxidoreductase that reduces cysteine residues on COX2 and on the copper metallochaperone SCO1, enabling Cu(I) binding in the otherwise oxidizing intermembrane-space environment (PMID:32061935, *J Mol Biol* / *Cell Reports* structural studies).
3. This reductase failure → **impaired copper (CuA site) metallation of newly synthesized COX2** (mtDNA-encoded core subunit of complex IV), because COA6 cooperates with SCO1 and SCO2 in a sequential copper-delivery pathway to the CuA binuclear copper center of COX2 (Pacheu-Grau et al. 2015, PMID:25959673; "COA6 interacts transiently with the copper-containing catalytic domain of newly synthesized COX2").
4. Failure of COX2 maturation → **rapid proteolytic turnover of unassembled/unmetallated COX2** and accumulation of stalled complex IV assembly intermediates (involving the COX20–TMEM177–COA6 intermediate complex described by Soma et al. 2019, *Cell Reports* 29:4114-4126, PMID:31851937).
5. Loss of mature COX2 → **failure of cytochrome c oxidase (complex IV) holoenzyme assembly**, producing **isolated (biochemically selective) complex IV deficiency** on respiratory chain enzymology, demonstrated in patient fibroblasts and muscle.
6. Complex IV deficiency → **impaired terminal electron transport and oxidative phosphorylation (OXPHOS)**, most severely affecting the highest-energy-demand postmitotic tissues: cardiomyocytes, neurons, and skeletal muscle.
7. In cardiomyocytes → **energy failure drives compensatory/maladaptive hypertrophic remodeling and disordered myocardial compaction**, producing the clinical **hypertrophic cardiomyopathy** and **left ventricular non-compaction** seen on echocardiography. (Inferred mechanistic step — the direct causal link from OXPHOS failure to LVNC morphogenesis is inferred from the general biology of energy-deficient cardiomyopathies rather than directly demonstrated for COA6 specifically.)
8. Systemically → impaired OXPHOS drives **anaerobic glycolytic compensation**, producing **lactic acidosis**, and generalized energy deficit in skeletal muscle and CNS produces **hypotonia** and **encephalopathic features** (the "encephalo-" component of cardioencephalomyopathy). (Inferred/generalized mitochondrial-disease mechanism, consistent with but not uniquely demonstrated for COA6.)
9. The combined burden of severe cardiac pump failure, systemic metabolic acidosis, and multi-organ energy failure in the neonatal period → **early infantile death**, typically within the first weeks of life.

### Molecular pathway / process detail
- **Pathway:** Mitochondrial complex IV (cytochrome c oxidase) biogenesis / assembly pathway; copper-relay/metallochaperone pathway (SCO1–SCO2–COA6–COX2 axis); MIA40/ERV1 disulfide-relay mitochondrial intermembrane-space protein import pathway (COA6 is itself a substrate of this import machinery, oxidized/folded upon import via its twin CX9C motif).
  - GO: **mitochondrial respiratory chain complex IV assembly (GO:0033617)**; **cytochrome complex assembly (GO:0017004)**; **protein import into mitochondrial intermembrane space (GO:0045041)**; **copper ion transport (GO:0006825)**
- **Cellular process:** Failure of oxidative phosphorylation complex assembly; compensatory metabolic shift toward anaerobic glycolysis; likely activation of the mitochondrial unfolded protein/integrated stress response (not directly demonstrated for COA6 but general to severe OXPHOS defects).
- **Protein structure/function:** COA6 is a small (14.1 kDa, 125 amino acid) soluble mitochondrial intermembrane-space protein with a **CX9CXnCX10C** twin cysteine motif forming a coiled-coil-helix-coiled-coil-helix (CHCH) domain — a redox-active fold. It is imported and oxidatively folded by the **MIA40 (CHCHD4)/ERV1(ALR)** disulfide-relay pathway. Structural/biochemical studies characterize COA6 as a **thiol-disulfide oxidoreductase** (not a copper metallochaperone per se) that reduces cysteines on COX2 and SCO1 to permit copper loading (Bourens & Barrientos-type structural work; PMC6743065, PMC8773535, and the ScienceDirect papers on "COA6 Facilitates Cytochrome c Oxidase Biogenesis as Thiol-reductase" PMID:32061935, and "COA6 Is Structurally Tuned to Function as a Thiol-Disulfide Oxidoreductase").
- **Metabolic changes:** Reduced oxidative ATP generation; elevated blood lactate (glycolytic compensation); consistent with generalized mitochondrial energy metabolism failure rather than a specific isolated metabolite defect.
- **Immune system involvement:** None described; not an immune-mediated disease.
- **Tissue damage mechanisms:** Energy failure/ischemia-like injury in high-demand tissues (heart, brain, muscle) secondary to OXPHOS insufficiency, rather than classic oxidative-stress-driven fibrosis (though secondary oxidative stress from an inefficient/uncoupled respiratory chain is plausible and typical of complex IV disorders generally).
- **Biochemical abnormality:** **Isolated cytochrome c oxidase (complex IV) enzymatic deficiency**, demonstrated biochemically in patient fibroblasts/muscle, with normal or relatively preserved activity of complexes I, II, III, and V — the classic "isolated COX deficiency" biochemical signature that first directs genetic testing toward the COX-assembly-factor gene set (*SURF1*, *SCO1*, *SCO2*, *COX10*, *COX15*, *COA5*, *COA6*, *COA7*, etc.).

### Molecular/cell-type involvement for annotation
- **Cell types affected:** cardiomyocyte (CL:0000746); skeletal myocyte; neuron (generalized)
- **Subcellular localization (GO Cellular Component):** mitochondrial intermembrane space (GO:0005758); mitochondrial inner membrane (associated, via interaction with COX2/COX20/TMEM177)

### Molecular profiling / advanced technologies
- No transcriptomic, proteomic, or single-cell datasets specific to human COA6-deficient tissue were identified in this search (consistent with the extreme rarity of the disease and the reliance on classic biochemical/genetic case-report methodology plus model-organism validation).
- **Model-system profiling that has been done:** yeast complementation assays (Coa6-null yeast strain rescue experiments); zebrafish morphant (knockdown) assays with cardiac phenotyping; human patient fibroblast biochemical and immunoblot studies (complex IV activity, COA6/COX2/SCO1/SCO2 protein levels); *in vitro* biophysical/structural characterization of recombinant COA6 protein (NMR/crystallography-adjacent structural biology, e.g., Life Science Alliance 2019, PMC6743065).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (myocardium — both ventricles); central nervous system/brain (encephalopathic component)
- **Secondary:** Skeletal muscle (hypotonia/weakness); broader multisystem involvement typical of mitochondrial disease
- **Body systems:** Cardiovascular system (primary); nervous system (primary — "encephalo-"); musculoskeletal system (hypotonia); metabolic/endocrine (lactic acidosis)
- UBERON: **heart (UBERON:0000948)**; **brain (UBERON:0000955)**; **skeletal muscle tissue (UBERON:0001134)**

**Tissue and cell level:**
- Myocardial tissue — both ventricles, with specific left ventricular non-compaction morphology
- CL: **cardiac muscle cell / cardiomyocyte (CL:0000746)**

**Subcellular level:**
- Mitochondria generally; specifically the **mitochondrial intermembrane space** (site of COA6 localization and function) and the **mitochondrial inner membrane** (site of complex IV/COX2 assembly)
- GO Cellular Component: **mitochondrial intermembrane space (GO:0005758)**; **mitochondrial respiratory chain complex IV (GO:0045277)**

**Localization:** Bilateral/systemic — biventricular cardiac hypertrophy (not lateralized); CNS involvement is generalized/encephalopathic rather than focal.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal — clinical features (hypotonia, systolic murmur, mild dysmorphism) present at birth, with severe lactic acidosis, hypothermia, and tachypnea developing "soon after birth."
- **Onset pattern:** Acute-to-subacute, rapidly evolving within the first days of life.
- **Progression:** Rapidly progressive to fatal cardiac and metabolic decompensation.
- **Disease stages:** No formal staging system exists (ultra-rare, no natural-history study); informally: (1) birth with subtle findings → (2) acute neonatal metabolic/cardiac crisis (lactic acidosis, hypothermia, tachypnea) → (3) progressive hypertrophic cardiomyopathy with LVNC and valvular regurgitation → (4) fatal cardiac/multiorgan failure in early infancy.
- **Progression rate:** Rapid — fatal course documented within the first weeks of life ("fatal course in the first weeks of life," per OMIM clinical synopsis).
- **Disease course pattern:** Progressive, non-remitting; no relapsing-remitting pattern described.
- **Disease duration:** Not self-limited — uniformly fatal in infancy in all reported cases to date.
- **Remission:** None reported; no spontaneous or treatment-induced remission documented for COA6 deficiency specifically (contrast with the unusual single case report of partial cardiac reversal with copper-histidine in *SCO2* deficiency, PMID:14970747 — an analogous but genetically distinct disorder).
- **Critical periods:** The neonatal period itself is the critical window — given the rapidity of decompensation, any intervention (e.g., experimental copper therapy) would need to be initiated essentially at or before symptom onset to have a plausible chance of benefit, though this remains theoretical for COA6 specifically.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence/incidence:** Not formally estimated in any registry; this is an ultra-rare condition with only two independently ascertained, molecularly confirmed families published in the primary literature (Ghosh et al. 2014; Baertling et al. 2015), plus scattered additional ClinVar variant submissions. No population-based prevalence or incidence figures exist. For KB purposes this would be classified under `prevalence_class: NOT_YET_DOCUMENTED` or an ultra-rare qualitative band, given the case-report-level evidence base (fewer than 5 published, distinctly ascertained cases as of this search).

**Inheritance pattern:** **Autosomal recessive (AR)** — confirmed by compound heterozygosity in one family and homozygosity (with consanguineous parents) in the second.
- HPO mode of inheritance: **Autosomal recessive inheritance (HP:0000007)**

**Penetrance:** Presumed complete/high penetrance given the severity and consistency of the phenotype across the (small number of) reported biallelic cases; formal penetrance estimates are not calculable from case-report-level data.

**Expressivity:** Appears relatively consistent (severe, neonatal-onset, cardiac-predominant) across the two published families, though the specific variant (missense mistargeting vs. compound het with a null allele) may plausibly affect severity/tissue-specificity nuances — insufficient data to formally characterize variable expressivity.

**Genetic anticipation:** Not applicable — this is not a repeat-expansion or anticipation-prone disorder.

**Germline mosaicism:** Not reported for COA6.

**Founder effects:** Not established; the two published pathogenic missense variants (W59C, W66R) and the nonsense variant (E87X) each occurred in unrelated/distinct families without evidence yet compiled for a specific population founder effect, though the consanguineous "Arab descent" family raises the possibility that region-specific carrier screening could be informative in populations with high consanguinity rates — this has not been formally studied.

**Consanguinity role:** Directly documented as relevant in the second reported family (homozygous W66R in a consanguineous Arab-descent family), consistent with the general pattern for ultra-rare autosomal recessive disorders.

**Carrier frequency:** Not established in the literature retrieved; gnomAD-based carrier-frequency estimation would need to be performed directly against the gnomAD browser for a KB entry (not confirmed in this search).

**Population demographics:**
- **Affected populations:** Insufficient case numbers to identify ethnic/demographic enrichment beyond the documented consanguineous Arab-descent family.
- **Geographic distribution:** No geographic clustering established; cases reported from at least two distinct, unrelated ascertainments (implying no single-population restriction, though sample size is far too small to draw firm conclusions).
- **Sex ratio:** The two published index cases comprise one male infant (Ghosh et al.) and one female infant (Baertling et al.) — consistent with expected 1:1 autosomal recessive inheritance, not X-linked.
- **Age distribution:** Exclusively neonatal/early infantile in all reported cases; no juvenile-, adult-, or late-onset COA6 phenotype has been published.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Serum lactate** — elevated, reflecting lactic acidosis; LOINC-codable analyte.
- **Respiratory chain enzymology** (muscle or fibroblast biopsy) — demonstrates **isolated complex IV (cytochrome c oxidase) deficiency**, with relatively preserved activity of other OXPHOS complexes — the classic biochemical signature directing genetic workup toward the COX-assembly-factor gene panel.
- **Echocardiography** — primary imaging modality; shows biventricular hypertrophic cardiomyopathy with regional left ventricular non-compaction and valvular (mitral, tricuspid, pulmonic) regurgitation.

**Genetic testing:**
- **Whole-exome sequencing (WES)** was the diagnostic modality used in both published families (trio-based approach identifying compound heterozygous or homozygous *COA6* variants), consistent with the standard modern diagnostic pathway for suspected isolated mitochondrial complex IV deficiency in a neonate, given the large number of candidate nuclear COX-assembly genes.
- **Gene panel testing** for "Nuclear Mitochondrial Disorders" (e.g., commercial panels such as Invitae's Nuclear Mitochondrial Disorders Panel) include *COA6* as a covered gene.
- **Single-gene Sanger sequencing** was used for confirmation/segregation analysis in both families following variant identification.
- **Muscle/fibroblast biopsy with biochemical complex IV assay and immunoblotting** for COA6, COX2, SCO1, SCO2 protein levels — used as functional confirmation in both published cases (showing absent/reduced COA6 protein and reduced complex IV assembly).

**Differential diagnosis:** Other genetic causes of isolated/severe complex IV deficiency with cardiomyopathy, most importantly:
- ***SCO2*-related cardioencephalomyopathy** — the closest biochemical/mechanistic relative (shares the copper-relay pathway with COA6; "links two mitochondrial cardiomyopathies," per Pacheu-Grau et al.)
- ***SCO1***-related hepatoencephalopathy/COX deficiency
- ***COX15***, ***COX10***, ***SURF1***, ***COA5***, ***COA7***, ***COX16***, ***COX20*** and other nuclear COX-assembly-factor genes causing overlapping fatal infantile cardioencephalomyopathy/COX-deficiency phenotypes (e.g., a 2021 report of a novel *COX16* variant causing "severe fatal neonatal lactic acidosis, encephalopathy, cardiomyopathy, and liver dysfunction," Wintjes et al. 2021, *Human Mutation*)
- Other causes of neonatal hypertrophic cardiomyopathy: sarcomeric gene defects (e.g., *MYBPC3* compound heterozygous truncating variants causing fatal neonatal HCM), Noonan-spectrum RASopathies, glycogen storage disease (Pompe disease), Barth syndrome (*TAZ*, associated with LVNC specifically).

**Screening:** No specific newborn screening test exists for COA6 deficiency (not amenable to standard metabolic newborn screening panels); diagnosis relies on clinical suspicion in a neonate with unexplained hypertrophic cardiomyopathy plus lactic acidosis, triggering biochemical and genetic workup.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Uniformly fatal in early infancy in both published cases — described as a disorder with "a fatal course in the first weeks of life" (OMIM clinical synopsis for MC4DN13). No long-term survivors have been reported in the primary literature retrieved.
- **Life expectancy:** Days to a few weeks from birth, based on the two published cases.
- **Complications:** Progressive hypertrophic cardiomyopathy leading to cardiac pump failure; severe refractory lactic acidosis; hypotonia/weakness contributing to respiratory compromise.
- **Recovery potential:** None described in COA6-specific cases; contrast with the single reported case of partial, transient hypertrophic cardiomyopathy reversal in a *SCO2*-deficient patient treated with subcutaneous copper-histidine (PMID:14970747) — this is a mechanistically related but genetically distinct disorder, and no equivalent reversal has been reported for COA6.
- **Prognostic factors:** Severity of cardiac hypertrophy/non-compaction and degree of lactic acidosis at presentation appear to correlate with the uniformly poor outcome across the small case series; insufficient data to formally identify prognostic biomarkers.

---

## 12. Treatment

**No disease-modifying or curative therapy exists for COA6-related fatal infantile cardioencephalomyopathy.** Management to date has been supportive/palliative given the rapidly fatal neonatal course.

**Pharmacotherapy — investigational/mechanistic rationale (cell-based, not yet clinically validated for COA6):**
- **Copper supplementation:** *In vitro* studies on patient fibroblasts are the strongest treatment-relevant finding in the literature: "Copper supplementation restores cytochrome c oxidase assembly defect in a mitochondrial disease model of COA6 deficiency" (Ghosh et al. 2014, *Human Molecular Genetics*, PMID:24549041) — "treatment of patient fibroblasts with copper led to a stable increase of complex IV and its subunits, suggesting a possible therapeutic option." This has been replicated at the cell-biology level but **has not been reported as a clinical intervention in an actual COA6 patient** (unlike the analogous *SCO2* case, PMID:14970747, where subcutaneous copper-histidine was administered to a living patient with transient cardiac benefit).
  - NCIT candidate term: **NCIT:C15986 (Pharmacotherapy)**; therapeutic_agent: copper (CHEBI, elemental/ionic copper — specific CHEBI ID would need verification, e.g., copper(II) chloride or copper-histidine complex depending on formulation)
- **Bezafibrate + copper combination** (studied in *SCO2* cellular models, not COA6 directly) achieved more complete rescue of COX activity than copper alone in related-gene cell models, suggesting a plausible but untested combination approach for COA6.
- **Elesclomol** has been explored as a copper-ionophore restoring mitochondrial function in genetic models of copper deficiency broadly (PNAS, PMID not retrieved directly) — a theoretical, unvalidated-for-COA6 avenue.

**Supportive/rehabilitative care:**
- **Supportive care** — symptom management, nutritional support, and cardiac supportive management (e.g., diuretics, inotropic support as clinically indicated) in the acute neonatal setting, though no COA6-specific treatment protocol has been published.
  - NCIT: **NCIT:C15747 (Supportive Care)**

**Advanced/experimental therapeutics:** No gene therapy, cell therapy, or RNA-based therapeutic approach has been reported for COA6-related disease specifically. No registered clinical trials (ClinicalTrials.gov) targeting COA6 deficiency were identified in this search.

**Genetic counseling:** Recommended for families of affected infants given confirmed autosomal recessive inheritance, with 25% recurrence risk per pregnancy for parents of an affected child; prenatal diagnosis via chorionic villus sampling/amniocentesis for known familial variants would be technically feasible once the causative variants are identified in a family, though no specific published experience with prenatal diagnosis for COA6 was found.
  - NCIT: **NCIT:C15240 (Genetic Counseling)**

**Treatment outcomes:** No systematic treatment-response, side-effect, or adverse-event data exist for COA6-directed therapy in humans, since no clinical (as opposed to cell-culture) therapeutic intervention has been reported.

---

## 13. Prevention

- **Primary prevention:** Genetic counseling and carrier testing in families with a known affected child or in populations with elevated consanguinity, to inform reproductive decision-making. No population-level primary prevention program exists given the extreme rarity of the condition.
- **Secondary prevention/screening:** Prenatal genetic testing (once familial variants are known) and/or preimplantation genetic diagnosis (PGD) are theoretically applicable standard approaches for a known autosomal recessive lethal disorder, though no published experience specific to COA6 was identified.
- **Tertiary prevention:** Not applicable in the classic sense, given the rapidly fatal neonatal course precludes long-term complication management; acute supportive cardiac/metabolic management in the immediate neonatal period represents the only available "tertiary" intervention window.
- **Immunization:** Not applicable — no infectious/immune component to this disease.
- **Public health/environmental interventions:** Not applicable — purely monogenic disorder with no environmental prevention target.
- **Prophylaxis:** None established; investigational copper supplementation (see Treatment) has not been validated as prophylactic therapy in at-risk newborns (e.g., a sibling known to carry the familial genotype prenatally) and is not standard of care.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease caused by spontaneous *COA6* mutation has been reported in this search (contrast with many other mitochondrial disease genes that have recognized veterinary analogs); COA6 biology has been studied primarily through **engineered/induced models** (yeast complementation, zebrafish morpholino knockdown) rather than naturally occurring animal disease.
- **Orthologous gene:** Yeast *Ymr244c-a*/*COA6* ortholog (used for functional complementation studies); zebrafish *coa6* ortholog (used for morphant knockdown cardiac phenotyping); mouse *Coa6* ortholog, **MGI:1915142**, located on an autosome in mouse, with entries in [IMPC](https://mousephenotype.org/data/genes/MGI:1915142) and [MGI](https://informatics.jax.org/marker/MGI:1915142) — a systematic knockout-phenotype dataset exists at IMPC, though detailed cardiac-specific phenotype results were not extracted in this search and should be checked directly at the IMPC gene page for a KB `animal_models` entry.
- **Comparative biology:** COA6 function (thiol-reductase-mediated copper delivery to COX2 for complex IV assembly) is deeply evolutionarily conserved from yeast to zebrafish to humans — demonstrated directly by the cross-species complementation and knockdown experiments in the founding Ghosh et al. 2014 paper, which used "an integrative approach based on clues from evolutionary history, protein localization and human genetics" spanning all three systems.
- **Zoonotic potential/cross-species susceptibility:** Not applicable — this is a cell-autonomous, non-infectious, genetically determined mitochondrial disorder.

---

## 15. Model Organisms

**Yeast (*Saccharomyces cerevisiae*):**
- **Model type:** Cellular/unicellular eukaryotic model.
- **Coa6-null yeast strain** used for functional complementation assays: wild-type human *COA6* rescues the respiratory growth defect of Coa6-null yeast, while patient-derived mutant alleles (W59C, E87X, W66R) fail to rescue, directly demonstrating loss-of-function pathogenicity (Ghosh et al. 2014, PMID:24549041).
- **Application:** Structure-function dissection of the conserved CX9CXnCX10C cysteine motif; rapid, genetically tractable system for variant-effect functional validation.
- **Resource:** [SGD - Saccharomyces Genome Database entry](https://yeastgenome.org/reference/S000174898)

**Zebrafish (*Danio rerio*):**
- **Model type:** Vertebrate, induced (morpholino knockdown) model.
- ***coa6* knockdown (morphant) zebrafish embryos** display **reduced heart rate and cardiac developmental defects**, "recapitulating the observed pathology in the human mitochondrial disease patient who died of neonatal hypertrophic cardiomyopathy" (Ghosh et al. 2014).
- **Phenotype recapitulation:** High-fidelity for the cardiac/developmental phenotype at a gross morphological/functional level (heart rate, cardiac structure); the conserved residue corresponding to the human patient mutation was shown to be essential for COA6 function in this system, directly supporting pathogenicity of the human variant.
- **Limitations:** Morpholino knockdown (rather than a stable genetic knockout/knock-in mutant line) has inherent limitations (potential off-target/incomplete knockdown effects, transient embryonic-stage-only assessment) — this should be recorded as a `fidelity: MODERATE` or similar caveat if curated as a `modeled_mechanisms` link, with `limitations` noting the morpholino (vs. genetic mutant) nature of the model.
- **Resource:** [ZFIN](https://zfin.org) (zebrafish model organism database) — specific ZFIN accession not retrieved in this search.

**Mouse (*Mus musculus*):**
- **Model type:** Mammalian, genetic (knockout) model — via the International Mouse Phenotyping Consortium.
- **Gene:** *Coa6*, MGI:1915142.
- **Resource:** [IMPC gene page](https://mousephenotype.org/data/genes/MGI:1915142) and [MGI marker page](https://informatics.jax.org/marker/MGI:1915142) — systematic phenotyping data are cataloged there; specific cardiac/lethality phenotype results were not extracted in this search pass and should be directly reviewed before KB curation (IMPC knockout-mouse embryonic lethality is common for essential mitochondrial assembly-factor genes and would be an important data point to confirm/record).

**Human cell-based models:**
- **Patient-derived fibroblasts** (from both published families) — the primary human cellular model, used for: complex IV enzymatic activity assays, COA6/COX2/SCO1/SCO2 immunoblotting, and copper-supplementation rescue experiments.
- **HEK293/HeLa cell overexpression and knockdown/knockout systems** — used extensively in the mechanistic follow-up literature (Pacheu-Grau et al. 2015; Soma et al. 2019; structural biology papers) to dissect the COA6–SCO1–SCO2–COX2–COX20–TMEM177 interaction network.

**Research applications enabled by these models:** Variant-effect functional classification (yeast complementation); cardiac developmental phenotyping (zebrafish); systemic/embryonic phenotyping and potential lethality assessment (mouse knockout, via IMPC); detailed biochemical/structural dissection of the copper-relay assembly pathway and therapeutic (copper supplementation) proof-of-concept (human fibroblasts and human cell lines).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Term |
|---|---|
| Gene | HGNC gene: `hgnc:18025` (COA6) |
| Disease | MONDO:0014668 |
| Inheritance | HP:0000007 (Autosomal recessive inheritance) |
| Phenotype | HP:0001639 (Hypertrophic cardiomyopathy) |
| Phenotype | HP:0006955 (Left ventricular noncompaction cardiomyopathy) |
| Phenotype | HP:0003128 (Lactic acidosis) |
| Phenotype | HP:0001252 / HP:0001319 (Hypotonia / Neonatal hypotonia) |
| Phenotype | HP:0002045 (Hypothermia) |
| Phenotype | HP:0002789 (Tachypnea) |
| Phenotype | HP:0001508 (Failure to thrive) |
| Phenotype | HP:0031628 (Mitral regurgitation) |
| GO Process | GO:0033617 (mitochondrial respiratory chain complex IV assembly) |
| GO Process | GO:0045041 (protein import into mitochondrial intermembrane space) |
| GO Cellular Component | GO:0005758 (mitochondrial intermembrane space) |
| GO Cellular Component | GO:0045277 (mitochondrial respiratory chain complex IV) |
| Cell type | CL:0000746 (cardiac muscle cell) |
| Anatomy | UBERON:0000948 (heart), UBERON:0000955 (brain), UBERON:0001134 (skeletal muscle tissue) |
| Treatment (investigational) | NCIT:C15986 (Pharmacotherapy) — copper supplementation, cell-based evidence only |

---

## Citation Requirements — Key Primary Literature

1. Ghosh A, Trivedi PP, Timbalia SA, Griffin AT, Rahn JJ, Chan SS, Gohil VM. "Copper supplementation restores cytochrome c oxidase assembly defect in a mitochondrial disease model of COA6 deficiency." *Hum Mol Genet.* 2014;23(13):3596-3606. PMID: [24549041](https://pubmed.ncbi.nlm.nih.gov/24549041/)
2. (Companion clinical report) "Mutations in COA6 cause cytochrome c oxidase deficiency and neonatal hypertrophic cardiomyopathy." PMID: [25339201](https://pubmed.ncbi.nlm.nih.gov/25339201/)
3. Baertling F, et al. (2015) — homozygous COA6 W66R in consanguineous family; described in [OMIM #616501](https://www.omim.org/entry/616501)
4. Pacheu-Grau D, et al. "Cooperation between COA6 and SCO2 in COX2 Maturation during Cytochrome c Oxidase Assembly Links Two Mitochondrial Cardiomyopathies." *Cell Metab.* 2015;21(6):823-833. PMID: [25959673](https://www.ncbi.nlm.nih.gov/pubmed/25959673)
5. "Mitochondrial disease genes COA6, COX6B and SCO2 have overlapping roles in COX2 biogenesis." PMID: [26669719](https://pubmed.ncbi.nlm.nih.gov/26669719/)
6. Soma S, et al. "COA6 Is Structurally Tuned to Function as a Thiol-Disulfide Oxidoreductase in Copper Delivery to Mitochondrial Cytochrome c Oxidase." *Cell Rep.* 2019;29(12):4114-4126. PMID: [31851937](https://pubmed.ncbi.nlm.nih.gov/31851937/)
7. "COA6 Facilitates Cytochrome c Oxidase Biogenesis as Thiol-reductase for Copper Metallochaperones in Mitochondria." PMID: [32061935](https://pubmed.ncbi.nlm.nih.gov/32061935/)
8. Structural/functional characterization: "Structural and functional characterization of the mitochondrial complex IV assembly factor Coa6." *Life Sci Alliance.* 2019. PMC: [PMC6743065](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6743065)
9. "The Role of COA6 in the Mitochondrial Copper Delivery Pathway to Cytochrome c Oxidase." PMC: [PMC8773535](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773535/)
10. OMIM #616501 — Mitochondrial Complex IV Deficiency, Nuclear Type 13: [omim.org/entry/616501](https://www.omim.org/entry/616501)
11. OMIM *614772 — COA6 gene: [omim.org/entry/614772](https://www.omim.org/entry/614772)
12. Orphanet gene page: [orpha.net/en/disease/gene/COA6](https://www.orpha.net/en/disease/gene/COA6)
13. Reference (analogous SCO2 copper therapy case): "Reversion of hypertrophic cardiomyopathy in a patient with deficiency of the mitochondrial copper binding protein Sco2." PMID: [14970747](https://pubmed.ncbi.nlm.nih.gov/14970747/)

**Note on evidence completeness for KB curation:** This report was assembled from web search and fetched summaries rather than full-text verbatim abstract retrieval for every source (several PubMed/OMIM pages returned cookie-consent/403 blocks rather than raw text during this session). **Before entering any `snippet:` evidence field into the dismech KB, each citation above must be independently re-fetched via `just fetch-reference <PMID>` and the exact quoted text verified against the cached abstract/full text**, per the project's evidence-integrity requirements — none of the quotations reproduced above should be treated as pre-verified exact-source substrings.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25959673` *(abstract only)*: "Cooperation between COA6 and SCO2 in COX2 Maturation... Links Two Mitochondrial Cardiomyopathies"
  - closest text in source: "Our analyses define COA6 as a constituent of the mitochondrial copper relay system, linking defects in COX2 metallation to cardiac cytochrome c oxidase deficiency."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 20 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014668` (3 mentions) - the report calls it "if available", "Disease"; MONDO calls it **cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency 4**
- `HP:0006955` (2 mentions) - the report calls it "HPO: **Left ventricular noncompaction cardiomyopathy", "Left ventricular noncompaction cardiomyopathy"; HP calls it **Olivopontocerebellar hypoplasia**
- `HP:0031628` (2 mentions) - the report calls it "HPO: **Mitral regurgitation", "Mitral regurgitation"; HP calls it **Aborted sudden cardiac death**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001725` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001639` (2 mentions) - the report calls it "HPO: **Hypertrophic cardiomyopathy", "Hypertrophic cardiomyopathy"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0003128` (2 mentions) - the report calls it "HPO: **Lactic acidosis", "Lactic acidosis"; HP calls it **Lactic acidosis**
- `HP:0002045` (2 mentions) - the report calls it "HPO: **Hypothermia", "Hypothermia"; HP calls it **Hypothermia**
- `HP:0001252` (2 mentions) - the report calls it "HPO: **Hypotonia"; HP calls it **Hypotonia**
- `HP:0001508` (2 mentions) - the report calls it "HPO: **Failure to thrive", "Failure to thrive"; HP calls it **Failure to thrive**
- `HP:0001298` (1 mention) - the report calls it "HPO candidate terms: **Encephalopathy"; HP calls it **Encephalopathy**
- `GO:0033617` (2 mentions) - the report calls it "GO: **mitochondrial respiratory chain complex IV assembly", "mitochondrial respiratory chain complex IV assembly"; GO calls it **mitochondrial respiratory chain complex IV assembly**
- `CL:0000746` (3 mentions) - the report calls it "Cell types affected:** cardiomyocyte", "CL: **cardiac muscle cell / cardiomyocyte", "cardiac muscle cell"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `GO:0005758` (3 mentions) - the report calls it "GO Cellular Component: **mitochondrial intermembrane space", "mitochondrial intermembrane space"; GO calls it **mitochondrial intermembrane space**
- `UBERON:0000948` (2 mentions) - the report calls it "UBERON: **heart"; UBERON calls it **heart**, and lists "chambered heart" among its other names
- `GO:0045277` (2 mentions) - the report calls it "mitochondrial respiratory chain complex IV"; GO calls it **respiratory chain complex IV**
- `HP:0000007` (2 mentions) - the report calls it "HPO mode of inheritance: **Autosomal recessive inheritance", "Autosomal recessive inheritance"; HP calls it **Autosomal recessive inheritance**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014668` - called "if available", "Disease"
- `HP:0001639` - called "HPO: **Hypertrophic cardiomyopathy", "Hypertrophic cardiomyopathy"
- `HP:0006955` - called "HPO: **Left ventricular noncompaction cardiomyopathy", "Left ventricular noncompaction cardiomyopathy"
- `HP:0031628` - called "HPO: **Mitral regurgitation", "Mitral regurgitation"
- `HP:0003128` - called "HPO: **Lactic acidosis", "Lactic acidosis"
- `HP:0002045` - called "HPO: **Hypothermia", "Hypothermia"
- `HP:0001508` - called "HPO: **Failure to thrive", "Failure to thrive"
- `GO:0033617` - called "GO: **mitochondrial respiratory chain complex IV assembly", "mitochondrial respiratory chain complex IV assembly"
- `CL:0000746` - called "Cell types affected:** cardiomyocyte", "CL: **cardiac muscle cell / cardiomyocyte", "cardiac muscle cell"
- `GO:0005758` - called "GO Cellular Component: **mitochondrial intermembrane space", "mitochondrial intermembrane space"
- `HP:0000007` - called "HPO mode of inheritance: **Autosomal recessive inheritance", "Autosomal recessive inheritance"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
