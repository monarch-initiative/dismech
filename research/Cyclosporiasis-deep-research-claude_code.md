---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-09T14:09:45.015037'
end_time: '2026-07-09T14:13:35.160669'
duration_seconds: 230.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cyclosporiasis
  mondo_id: ''
  category: Infectious Disease
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 22
  total_cost_usd: 2.1671602000000005
  session_id: db903cd5-6264-56d5-9a4c-20a915dd00d2
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cyclosporiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Cyclosporiasis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Cyclosporiasis (*Cyclospora cayetanensis* infection): Comprehensive Research Report

## 1. Disease Information

**Overview:** Cyclosporiasis is a foodborne/waterborne diarrheal illness caused by *Cyclospora cayetanensis*, a coccidian (apicomplexan) protozoan parasite. Humans are the only known host — no animal reservoir has been identified — and transmission occurs via ingestion of sporulated oocysts contaminating fresh produce or water; there is no direct person-to-person transmission because freshly passed oocysts require days-to-weeks of environmental sporulation before becoming infectious (CDC DPDx; PMC6780905, *Cyclospora cayetanensis and Cyclosporiasis: An Update*).

**Key identifiers:**
- **ICD-10-CM:** A07.4 (Cyclosporiasis)
- **MONDO:** MONDO:0005725
- **Disease Ontology:** DOID:12750
- **Orphanet:** ORPHA210
- **SNOMED CT:** 240372001
- **UMLS:** C0343398
- **NCBI Taxonomy (organism):** *Cyclospora cayetanensis*, txid88456
- **MeSH:** Cyclosporiasis (D019022); Organism: *Cyclospora* (D019081)

**Synonyms:** Cyclospora infection, *Cyclospora cayetanensis* infection, "cyanobacterium-like body" (CLB) diarrhea (historical name before speciation in 1993-94), coccidian-associated diarrhea.

**Evidence basis:** Aggregated disease-level knowledge (case series, outbreak investigations, systematic reviews) predominates; some individual pathologic/histologic case reports exist (e.g., PMID:9395371).

---

## 2. Etiology

**Causal agent:** Infection is caused by ingestion of sporulated oocysts of *C. cayetanensis* (an obligate intracellular coccidian parasite of the family Eimeriidae). This is an infectious, not genetic, disease — there is no known Mendelian susceptibility locus, though host immune status strongly modulates severity.

**A newly recognized taxonomic wrinkle (2023):** CDC researchers demonstrated that clinical "*C. cayetanensis*" cyclosporiasis is actually caused by **at least three genetically distinct species/lineages** — the classic *C. cayetanensis* (with lineages A and B distinguished at the CDS3 and 360i2 nuclear loci) plus two novel species, ***Cyclospora ashfordi* sp. nov.** and ***Cyclospora henanensis* sp. nov.** (isolated from a Henan, China strain), all causing indistinguishable human cyclosporiasis (PMC10090632, *Parasitology* 2023, "Cyclospora cayetanensis comprises at least 3 species that cause human cyclosporiasis"; CDC AMD success story).

**Risk factors:**
- *Environmental/behavioral:* Consumption of imported fresh produce (basil, cilantro, raspberries, snow peas, mesclun/salad mix, broccoli), especially from Guatemala, Mexico, Peru; travel to or residence in endemic regions (Guatemala, Peru, Nepal, Haiti, Indonesia, parts of Africa); warm/rainy season exposure — "prevalence...rises during periods of elevated rainfall and warm weather in Guatemala, Honduras, Mexico, Jordan, Nepal, and China" (search synthesis of PMC10536660).
- *Age:* Children in endemic areas show higher susceptibility/prevalence than adults.
- *Immune status:* HIV/AIDS and other immunocompromising conditions (transplant recipients, chemotherapy patients) markedly increase risk of severe, prolonged, and relapsing disease and of extraintestinal (biliary) involvement.
- *Socioeconomic:* Low-income, endemic, or disease-endemic settings with poor water/sanitation infrastructure.
- No confirmed genetic risk variants have been described; no GWAS hits are catalogued for cyclosporiasis susceptibility.

**Protective factors:** No specific genetic protective alleles known. Environmentally, thorough cooking of produce (heat, not chemical disinfection) destroys oocysts; adequate irrigation-water treatment (microfiltration, ozone, UV) reduces field contamination (FDA Cyclospora page; PMC10536660). Repeated natural exposure in endemic areas may confer partial age-related immunity (older residents of endemic areas often show milder/asymptomatic infection versus travelers/children).

**Gene-environment interactions:** Not established as a specific mechanistic pathway in the literature; the dominant modifiers are host immune competence (HIV, immunosuppression) interacting with environmental oocyst exposure dose/frequency, rather than a defined host genetic polymorphism.

---

## 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Notes/Frequency |
|---|---|---|---|
| Watery diarrhea | Symptom | HP:0002014 (Diarrhea) | Hallmark; profuse, often explosive |
| Abdominal cramping/pain | Symptom | HP:0002027 (Abdominal pain) | Common |
| Nausea | Symptom | HP:0002018 (Nausea) | Common |
| Vomiting | Symptom | HP:0002013 (Vomiting) | Occasional |
| Anorexia/loss of appetite | Symptom | HP:0002039 (Poor appetite) | Common, notable |
| Weight loss | Sign | HP:0001824 (Weight loss) | Can exceed 20 lb untreated |
| Fatigue | Symptom | HP:0012378 (Fatigue) | Prominent, often disproportionate |
| Low-grade fever | Sign | HP:0025336 (Low-grade fever) / HP:0001945 (Fever) | Less common than diarrhea |
| Bloating/flatulence | Symptom | HP:0002583 (Bowel obstruction) not ideal; consider HP:0030765 (Abdominal bloating) | Common |
| Myalgias | Symptom | HP:0003326 (Myalgia) | Reported |
| Malabsorption | Sign | HP:0002024 (Malabsorption) | Documented pathologically |
| Relapsing/remitting course | Clinical course | (course qualifier, not HP term) | Symptoms wax and wane; may relapse days-weeks after apparent resolution |
| Guillain-Barré syndrome (rare sequela) | Sign | HP:0002878 (Guillain-Barré syndrome) | Reported post-infectious complication |
| Reactive arthritis / Reiter syndrome (rare sequela) | Sign | HP:0100558 (Reactive arthritis, if available) | Reported post-infectious complication |
| Acalculous cholecystitis / biliary disease | Sign | HP:0005375 (Cholecystitis) | Reported in immunocompromised (AIDS) patients |

**Onset/severity:** Incubation averages ~1 week (range 2 days–2+ weeks) (CDC Clinical Overview). Disease is "often mild or asymptomatic" in endemic populations but can be severe in infants, the elderly, and profoundly immunocompromised patients (PMC8471761). Untreated illness can last from several days to a month or longer, with some patients relapsing one or more times.

**Quality of life impact:** Chronic/relapsing diarrhea with substantial weight loss and fatigue can significantly impair daily functioning, particularly in immunocompromised or pediatric malnourished populations; explicit EQ-5D/SF-36 data specific to cyclosporiasis were not identified in the literature searched.

---

## 4. Genetic/Molecular Information

This is an infectious disease with **no human causal gene** — genetic material of interest belongs to the pathogen itself.

**Pathogen genome:** The *C. cayetanensis* nuclear genome is ~44 Mbp, 52% GC content, ~7,500 genes (PMC4851813, comparative genomics study). It also carries a **mitochondrial genome** (PMID for complete mitochondrial genome: PMC4455993/PLOS ONE 2015) and an **apicoplast genome** (a relict non-photosynthetic plastid; PMC5129617) — both used as multicopy targets for sensitive detection and geographic traceback.

**Comparative genomics:** *C. cayetanensis* shows "coccidia-like metabolism and invasion components but unique surface antigens," with overall genome organization and invasion machinery closely resembling *Eimeria tenella*, but differing in amino acid metabolism, propanoyl-CoA degradation, GPI-anchor biosynthesis, and N-glycosylation; unlike *Eimeria* spp., no active LTR-retrotransposons have been identified (PMC4851813).

**Genotyping/molecular epidemiology tools** (used for outbreak traceback rather than clinical variant calling):
- Original MLST panel: five microsatellite loci (CYC3, CYC13, CYC15, CYC21, CYC22) — successful in <60% of stool specimens (search synthesis, PMC8506454).
- Newer **targeted amplicon deep sequencing (TADS)/targeted amplicon sequencing (TAS)** schemes: six nuclear loci (Nu_CDS1–4, Nu_378, Nu_360i2) + two mitochondrial markers (Mt_MSR, Mt_Cmt) (PMID:37396378, PMC10311907, 2023; PMID:38792677, 2024 evaluation of increased genetic resolution).
- **Mitochondrial junction region typing:** successfully typed 132/134 samples into 14 sequence types, matching epidemiologic clusters in 7/10 outbreaks (Emerging Infectious Diseases, 2019).
- CDC's ensemble clustering method accounts for sexual recombination in the parasite's life cycle, achieving 90–94% sensitivity/99% specificity for 2019 outbreak clustering.

**Species/lineage delineation (2023):** Two nuclear loci (CDS3, 360i2) distinguish lineage A vs. B within *C. cayetanensis*, and a genetically distinct Chinese isolate was elevated to a new species, *C. henanensis*, alongside *C. ashfordi* (PMC10090632).

**Epigenetics, somatic/germline distinction, chromosomal abnormalities:** Not applicable — this is a parasitic infection, not a heritable human genetic disease.

---

## 5. Environmental Information

- **Primary environmental vehicle:** Sporulated oocysts contaminating fresh produce (basil, cilantro, raspberries, snow peas, mesclun mix, broccoli) and water. Sporulation requires days-to-weeks at 22–30°C outside the host (PMC8779055).
- **Infectious agent classification:** Protozoan parasite, NCBI Taxonomy ID 88456, phylum Apicomplexa, family Eimeriidae.
- **Environmental persistence:** The oocyst wall confers marked resistance to routine chemical disinfectants, **including chlorine** — "Cyclospora may be resistant to routine chemical disinfection methods such as those using chlorine" and "routine chemical sanitizers and household produce washes are generally ineffective against Cyclospora oocysts" (FDA Cyclospora page; search synthesis). Only heat (cooking/boiling) reliably destroys oocysts in food; water treatment via microfiltration, ozone, or UV can reduce irrigation-water contamination.
- **Seasonality:** Marked seasonal peaks associated with warm, rainy periods in endemic countries (Guatemala, Honduras, Mexico, Jordan, Nepal, China) and a well-documented May–August seasonal peak in U.S. outbreaks tied to imported produce.
- **Lifestyle factors:** International travel to endemic regions and dietary consumption of imported raw produce are the dominant lifestyle risk factors in non-endemic countries (e.g., U.S., Canada, Europe).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Ingestion of sporulated oocysts** (via contaminated produce/water) →
2. **Excystation in the gut lumen:** sporozoites are released from sporocysts (each sporulated oocyst contains 2 sporocysts, each with 2 elongated sporozoites) →
3. **Invasion of small intestinal (and occasionally biliary) epithelial cells:** sporozoites transform into schizonts within a parasitophorous vacuole in the apical cytoplasm, above the host cell nucleus, most numerous at villus tips (PMC8779055; PMID:9395371) →
4. **Asexual schizogony (merogony):**
   - **Type I meronts** contain 8–12 merozoites (~3–4 µm) that perpetuate autoinfection/amplification within the host intestine.
   - **Type II meronts** contain 4 merozoites (~12–15 µm) that differentiate into the sexual stages.
5. **Gametogony:** Type II merozoites form microgametocytes (male, flagellated microgametes ~6.6 × 5.2 µm) and macrogametocytes (female, containing eosinophilic wall-forming bodies) →
6. **Fertilization and oocyst formation:** unsporulated oocysts (8–10 µm, spheroidal) are shed in feces, non-infectious until environmental sporulation (7–14 days at 22–30°C) completes the cycle →
7. **Local tissue injury:** histopathology shows acute-to-chronic inflammatory infiltration of the lamina propria (lymphocytes, plasma cells, eosinophils), surface epithelial disarray, loss of brush border, villous blunting/flattening, crypt hyperplasia, diffuse edema, and vascular dilatation in jejunal biopsies (PMID:9395371; PMC8471761) →
8. **Functional consequence:** disruption of the absorptive epithelium produces **malabsorptive, secretory watery diarrhea**, confirmed pathologically as malabsorption in biopsy-proven cases; inflammatory changes may persist beyond parasitologic clearance, potentially explaining post-infectious relapsing symptoms.
9. **Rare post-infectious immune-mediated sequelae:** Guillain-Barré syndrome and reactive arthritis/Reiter syndrome have been reported following cyclosporiasis, suggesting a molecular-mimicry or immune-activation mechanism analogous to other enteric-infection-triggered autoimmune sequelae, though the precise immunologic pathway is not well characterized in the literature reviewed.
10. **Immunocompromised host divergence:** in AIDS/transplant patients, parasite burden and tissue spread (including biliary epithelium, producing acalculous cholecystitis and biliary disease) are markedly increased, and clearance requires prolonged/higher-dose antimicrobial therapy.

**Cell types involved:** small intestinal (jejunal) enterocytes/epithelial cells (CL:0000584 enterocyte; CL:0002250 intestinal crypt cell), biliary epithelial cells (CL:1000343 epithelial cell of intrahepatic bile duct) in immunocompromised hosts, lamina propria lymphocytes and plasma cells (CL:0000542 lymphocyte, CL:0000786 plasma cell).

**Biological processes (GO terms):**
- GO:0044409 (entry into host) / GO:0075732 (viral penetration into host cell, N/A — better: GO:0044412 or general "invasion of host epithelial cell")
- GO:0006955 (immune response)
- GO:0002526 (acute inflammatory response)
- GO:0022415 (viral process — N/A for parasite; use GO:0044403 symbiotic process / host-parasite interaction terms)
- GO:0007586 (digestion) — disrupted
- GO:0006811 (ion transport) — disrupted absorptive function underlying malabsorption

**Protein dysfunction / biochemical abnormalities:** Not a host-protein-defect disease; the pathogen's own invasion-related surface antigens are apicomplexan-family unique (distinct from *Eimeria*), a focus of ongoing genomic characterization (PMC4851813) but not yet resolved to specific therapeutic targets.

**Omics/advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR functional-genomics datasets specific to *C. cayetanensis* host-response were identified — a direct consequence of the field's central research bottleneck (see Model Organisms, below): there is **no cell-culture or animal model system** to propagate the parasite, severely limiting mechanistic/omics studies (PMC10536660; PMC9608778 "Hastening Progress in Cyclospora Requires Studying Eimeria Surrogates").

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary target — small intestine (jejunum predominantly). Secondary/complication-level involvement — biliary tract (gallbladder, bile ducts) in immunocompromised hosts. Body system: digestive/gastrointestinal system; secondary neurological (Guillain-Barré) and musculoskeletal/rheumatologic (reactive arthritis) involvement as rare post-infectious sequelae.
- **UBERON terms:** UBERON:0002115 (jejunum), UBERON:0002108 (small intestine), UBERON:0002110 (gallbladder), UBERON:0002394 (bile duct), UBERON:0001007 (digestive system).
- **Tissue/cell level:** Intestinal epithelium (villus and crypt enterocytes), lamina propria (inflammatory infiltrate: lymphocytes, plasma cells, occasional eosinophils), biliary epithelium.
- **Cell Ontology terms:** CL:0000584 (enterocyte), CL:0009017 (intestinal crypt stem cell / crypt epithelial cell), CL:1000343 (epithelial cell of intrahepatic bile duct), CL:0000542 (lymphocyte), CL:0000786 (plasma cell).
- **Subcellular level:** Parasites reside within a **parasitophorous vacuole** in the apical cytoplasm of host epithelial cells, above the nucleus — GO Cellular Component: GO:0020009 (parasitophorous vacuole membrane) / GO:0033664 (host parasitophorous vacuole).
- **Localization:** Villus tips most heavily parasitized; no clear lateralization pattern (diffuse small-bowel process).

---

## 8. Temporal Development

- **Onset:** Incubation averages ~1 week (range 2 days to ≥2 weeks) after ingestion of sporulated oocysts; can affect any age but more severe in infants, elderly, and immunocompromised.
- **Onset pattern:** Acute onset of watery diarrhea and systemic symptoms.
- **Progression/course:** Highly variable — "some patients experience a single self-limited episode, whereas others have waxing and waning symptoms" (PMC8471761). Untreated illness may last days to a month or longer; **relapsing course** is characteristic, with symptoms resolving then recurring days to a week later, sometimes multiple cycles.
- **Duration:** Self-limited in many immunocompetent hosts over weeks; can become chronic/relapsing in immunocompromised patients (case report of chronic Cyclospora infection with intestinal malabsorption in a heart transplant recipient, PMC12584178).
- **Remission:** Both spontaneous (immunocompetent) and treatment-induced (TMP-SMX) remission occur; inflammatory changes on biopsy may outlast parasitologic cure.
- **Critical periods:** No defined developmental critical window; risk of severe/prolonged disease is driven by immune status rather than age-specific biological windows (though pediatric and elderly hosts trend toward more severe presentations).

---

## 9. Inheritance and Population

**Not a genetic disease** — no Mendelian inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, or carrier frequency applies.

**Epidemiology:**
- **Global prevalence:** Pooled worldwide human prevalence estimated at **3.55%** in a 2024 systematic review/meta-analysis/meta-regression (*Acta Tropica*, ScienceDirect, S0001706X24000597); prevalence is markedly higher in low-income/endemic countries and among individuals with diarrhea, particularly in Africa.
- **Geographic distribution:** At least **54 countries** have documented *C. cayetanensis* infections, with outbreaks recorded in 13; high-endemicity regions include Guatemala, Honduras, Peru, Nepal, Haiti, Indonesia, Madagascar, and parts of the Middle East/Asia (Jordan, China).
- **U.S. burden:** In 2023, 4 of 24 (17%) major FDA-investigated foodborne outbreaks were attributed to *C. cayetanensis*; a June 2023 restaurant-associated outbreak in Limestone County, Alabama produced 47 cases linked to cilantro (PMC12005484; MMWR-style report). 2022 and 2024 showed similar patterns, with the majority of outbreak food-source investigations remaining inconclusive (only broccoli was conclusively confirmed in one 2023 outbreak) (NACMCF 2023 report, FSIS).
- **Age distribution:** Children in endemic countries show higher susceptibility/prevalence than adults; in non-endemic countries, cases cluster among travelers and consumers of imported produce across all ages.
- **Sex ratio:** No strong sex predilection reported in the literature reviewed.
- **Travelers:** *C. cayetanensis* is a recognized cause of traveler's diarrhea, especially among travelers returning to industrialized countries from endemic regions.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Microscopy:** Stool ova-and-parasite exam with **modified acid-fast (Kinyoun) staining** — oocysts stain bright pinkish-red, though staining is variable (some mottled, some non-refractile "glassy" and unstained); **modified safranin staining** offers improved sensitivity and faster turnaround than modified acid-fast; **UV autofluorescence microscopy** — oocysts autofluoresce blue/green under UV, considered more reliable than acid-fast staining alone.
- **Molecular (PCR/NAAT):** *C. cayetanensis*-specific PCR assays (e.g., PMC2493149, highly sensitive/specific PCR) and multiplex syndromic **gastrointestinal panels** (e.g., FilmArray GI Panel) that include *Cyclospora* targets are increasingly used clinically; molecular methods avoid the sporulation-dependent morphologic ambiguity of microscopy.
- **Biopsy:** Small intestinal (jejunal) biopsy can show diagnostic intracellular parasite stages within parasitophorous vacuoles, though rarely required given stool-based diagnostics.
- **LOINC:** relevant test panels exist for ova-and-parasite exam and GI PCR panels (specific LOINC codes for *Cyclospora* antigen/PCR are laboratory-specific; Mayo Clinic Labs test CYCL — "Cyclospora Stain, Feces" — is a representative clinical order).

**Genetic/molecular epidemiologic testing (not for individual diagnosis but outbreak investigation):** targeted amplicon sequencing (TAS/TADS) genotyping panels (nuclear + mitochondrial loci) used by CDC and public health labs for traceback (PMID:37396378; PMID:38792677).

**Screening:** No population-based or newborn screening programs exist (this is an acute infectious, not congenital/genetic, disease); case-based surveillance and outbreak cluster detection (via PulseNet-style genotyping) function as the "screening" analog at the public-health level.

**Differential diagnosis:** Other causes of infectious watery diarrhea/traveler's diarrhea — *Cryptosporidium*, *Giardia*, *Cystoisospora (Isospora) belli*, enterotoxigenic *E. coli*, norovirus, and in immunocompromised hosts, microsporidiosis.

---

## 11. Outcome/Prognosis

- **Mortality:** Generally low in immunocompetent hosts; cyclosporiasis is rarely fatal but can cause significant morbidity, especially in malnourished children and severely immunocompromised patients where prolonged, high-volume diarrhea and malabsorption can be life-threatening ("prolonged diarrhea that could be life threatening in immunocompromised patients," search synthesis of clinical reviews).
- **Morbidity:** Significant weight loss (reportedly >20 lb in some untreated cases), fatigue, and malabsorption; chronic cases in immunocompromised hosts (e.g., transplant recipients) can produce sustained intestinal malabsorption (PMC12584178 case report).
- **Recovery:** Excellent with appropriate TMP-SMX treatment (>90% cure rates in immunocompetent patients per PMC8471761); without treatment, illness resolves over days to a month (occasionally longer) but relapse is common.
- **Complications:** Acalculous cholecystitis/biliary disease (especially AIDS patients), Guillain-Barré syndrome, reactive arthritis/Reiter syndrome as rare post-infectious sequelae.
- **Prognostic factors:** Immune status is the dominant prognostic determinant — HIV/AIDS, transplant immunosuppression, and extremes of age (infancy, elderly) predict more severe/prolonged/relapsing disease and treatment courses of longer duration or need for secondary prophylaxis.

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **Trimethoprim-sulfamethoxazole (TMP-SMX):** treatment of choice. Standard adult regimen: one double-strength tablet (TMP 160 mg/SMX 800 mg) orally twice daily for 7–10 days, achieving >90% cure rates in immunocompetent patients (PMC8471761). In a randomized controlled trial in HIV-infected patients, diarrhea ceased in all 19 TMP-SMX-treated patients, with 18/19 (95%) stool-negative by day 7 (PMID:10836915, comparing TMP-SMX vs. ciprofloxacin for *Isospora belli* and *C. cayetanensis* in HIV).
- **HIV-infected/immunocompromised patients:** may require longer treatment courses and, in some cases, secondary (chronic suppressive) prophylaxis to prevent relapse.
- **Alternatives for sulfa allergy:** **Ciprofloxacin** (less effective than TMP-SMX but an acceptable alternative) and **nitazoxanide** are used when TMP-SMX cannot be tolerated, though treatment failures are more common with these agents; "no highly effective alternatives have been identified for persons who are allergic to or intolerant of TMP-SMX."

**MAXO terms:**
- MAXO:0000647 (chemotherapy) — not applicable; better: generic pharmacotherapy term
- Use `treatment_term`: NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent`: CHEBI term for trimethoprim/sulfamethoxazole combination (CHEBI:45924 co-trimoxazole), or individual components CHEBI:45963 (trimethoprim), CHEBI:9328 (sulfamethoxazole); ciprofloxacin — CHEBI:100241; nitazoxanide — CHEBI:7580.
- MAXO:0000950 (supportive care) for oral rehydration/fluid-electrolyte management.

**Advanced therapeutics:** None applicable — no gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy is used or in development for this parasitic infection.

**Surgical/interventional:** Not typically required except for management of complications (e.g., cholecystectomy in rare severe acalculous cholecystitis cases).

**Supportive care:** Oral or IV rehydration and electrolyte repletion for volume losses, nutritional support for malabsorption/weight loss.

**Experimental treatments:** No dedicated *Cyclospora*-specific clinical trials were identified as currently active (search of trial-focused sources returned no *Cyclospora*-specific NCT-registered interventional trials); most evidence base derives from older HIV-era comparative drug trials (e.g., PMID:10836915).

**Treatment algorithm:** Confirm diagnosis (stool microscopy/PCR) → first-line TMP-SMX 7–10 days → reassess for immunocompromised status (consider extended course/secondary prophylaxis) → for sulfa allergy, ciprofloxacin or nitazoxanide as second-line with counseling on lower efficacy.

---

## 13. Prevention

- **Primary prevention:** No vaccine exists. Key strategies: (1) thorough cooking of high-risk imported produce (only heat reliably destroys oocysts, since chlorine and standard produce washes are largely ineffective against the resistant oocyst wall); (2) safe drinking-water practices, especially for travelers to endemic regions; (3) improved agricultural practices — sanitized irrigation water, water treatment via microfiltration/ozone/UV in growing regions (FDA; PMC10536660).
- **Secondary prevention (screening/early detection):** No population screening program exists; clinical suspicion in returning travelers or after implicated produce exposure prompts stool testing; **outbreak surveillance and genotyping-based traceback** (CDC's TAS/mitochondrial-junction methods) functions as public-health-level early detection to halt ongoing exposures.
- **Tertiary prevention:** Prompt TMP-SMX treatment to prevent complications (biliary disease, prolonged malabsorption) and, in immunocompromised patients, secondary prophylaxis to prevent relapse.
- **Public health interventions:** FDA/CDC foodborne-outbreak investigation infrastructure (PulseNet-style genotype clustering), import controls/testing on high-risk produce commodities from endemic-growing regions, and grower-level Good Agricultural Practices (GAP) guidance (2023 NACMCF report on *Cyclospora* in produce).
- **Traveler's health counseling:** Avoid unpeeled/unwashed raw produce and untreated water in endemic destinations.
- **Genetic counseling:** Not applicable (non-genetic disease).

---

## 14. Other Species / Natural Disease

- **Host range:** Humans are the **only known definitive host** for *C. cayetanensis* sensu stricto; extensive experimental attempts to infect a wide variety of animal models (including non-human primates) have failed (PMC8779055; PMC10536660).
- **Related organisms in animals:** Numerous other *Cyclospora* species infect non-human hosts (reptiles, rodents, other mammals) but do not cause human disease; a molecular survey found *Cyclospora* spp. in cattle in Shanxi Province, China (PMC11274234), raising open questions about environmental/zoonotic overlap that remain unresolved for human-infective genotypes specifically.
- **Newly named species (2023):** *Cyclospora ashfordi* sp. nov. and *Cyclospora henanensis* sp. nov., both shown to cause human cyclosporiasis alongside classic *C. cayetanensis* lineages A/B (PMC10090632) — an important taxonomic/comparative-biology update.
- **Transmission/zoonotic potential:** No confirmed zoonotic transmission cycle for the human-infective *Cyclospora* species/lineages; the human-only host cycle is a key epidemiologic feature distinguishing cyclosporiasis from cryptosporidiosis (which does have zoonotic reservoirs).
- **Comparative biology:** Genomically and morphologically, *C. cayetanensis* is closely allied with *Eimeria* (94–98% SSU rRNA sequence similarity), particularly avian-infecting *Eimeria* species, and shares coccidia-like metabolic and invasion machinery with *Eimeria tenella* despite unique surface antigens (PMC4851813).

---

## 15. Model Organisms

**This is the single greatest research bottleneck for the disease:**

- **No validated animal model exists.** "Researchers have been unable to establish *C. cayetanensis* infection in a wide variety of animal models," and there is no in vitro/tissue-culture propagation system either (PMC10536660; PMC9608778).
- **Human challenge study:** A CDC pilot human-challenge study (PMID:15200870, *Emerging Infectious Diseases* 2004) dosed 7 healthy volunteers with 200–49,000 oocysts; **none developed clinical or parasitologic evidence of infection** over 16 weeks of follow-up — underscoring major unknowns in infectious dose, host susceptibility factors, and possibly reduced oocyst viability by the time of the challenge inoculum.
- **Surrogate model strategy:** Given the impasse, researchers have proposed using the genomically and biologically related genus ***Eimeria*** (which does have established animal infection models, e.g., *E. tenella* in chickens, *E. falciformis* in mice) as a tractable surrogate system to model coccidian biology relevant to *Cyclospora* — see PMC9608778, "Hastening Progress in Cyclospora Requires Studying Eimeria Surrogates."
- **Available research material:** Investigators must rely entirely on oocysts recovered from naturally infected human stool specimens, which are scarce, variably viable, and logistically difficult to standardize — severely constraining functional genomics, drug-screening, vaccine development, and mechanistic host-response studies.
- **Resources:** No dedicated *Cyclospora* model-organism repository/database exists analogous to MGI/ZFIN/FlyBase for this pathogen; genomic resources are housed in general databases (NCBI Taxonomy txid88456, GenBank genome assemblies referenced in PMC4851813, PMC4455993, PMC5129617).

---

## Summary of Key Ontology Term Suggestions

| Category | Term |
|---|---|
| Disease | MONDO:0005725; ICD-10-CM A07.4; DOID:12750; ORPHA210 |
| Organism | NCBITaxon:88456 (*Cyclospora cayetanensis*) |
| Phenotypes (HP) | HP:0002014 Diarrhea; HP:0002027 Abdominal pain; HP:0002018 Nausea; HP:0002039 Poor appetite; HP:0001824 Weight loss; HP:0012378 Fatigue; HP:0002024 Malabsorption; HP:0002878 Guillain-Barré syndrome; HP:0005375 Cholecystitis |
| Cell types (CL) | CL:0000584 enterocyte; CL:1000343 intrahepatic bile duct epithelial cell; CL:0000542 lymphocyte; CL:0000786 plasma cell |
| Anatomy (UBERON) | UBERON:0002115 jejunum; UBERON:0002108 small intestine; UBERON:0002110 gallbladder; UBERON:0002394 bile duct |
| Chemicals (CHEBI) | CHEBI:45963 trimethoprim; CHEBI:9328 sulfamethoxazole; CHEBI:100241 ciprofloxacin; CHEBI:7580 nitazoxanide |
| Treatment (MAXO/NCIT) | NCIT:C15986 Pharmacotherapy; MAXO:0000950 supportive care |

---

## Sources

- [CDC - DPDx - Cyclosporiasis](https://www.cdc.gov/dpdx/cyclosporiasis/index.html)
- [Clinical Overview of Cyclosporiasis | CDC](https://www.cdc.gov/cyclosporiasis/hcp/clinical-overview/index.html)
- [Clinical Guidance for Cyclosporiasis | CDC](https://www.cdc.gov/cyclosporiasis/hcp/clinical-guidance/index.html)
- [Cyclospora cayetanensis and Cyclosporiasis: An Update - PMC (PMID:35056567)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6780905/)
- [Cyclospora cayetanensis: A Perspective (2020–2023) with Emphasis on Epidemiology and Detection Methods - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10536660/)
- [Life Cycle and Transmission of Cyclospora cayetanensis: Knowns and Unknowns - PMC (PMID:35056567)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8779055/)
- [Cyclospora cayetanensis infection in humans: biological characteristics, clinical features, epidemiology, detection method and treatment - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10317703/)
- [Cyclosporiasis—Updates on Clinical Presentation, Pathology, Clinical Diagnosis, and Treatment - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8471761/)
- [Pathologic and clinical findings in patients with cyclosporiasis - PubMed (PMID:9395371)](https://pubmed.ncbi.nlm.nih.gov/9395371/)
- [Outbreak of Cyclosporiasis Among Patrons of a Mexican-Style Restaurant — Limestone County, Alabama, May–June 2023 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12005484/)
- [Cyclospora cayetanensis in Produce (NACMCF 2023 Report)](https://www.fsis.usda.gov/sites/default/files/media_file/documents/NACMCF_Cyclospora_Report_2023_Final.pdf)
- [Cyclospora | FDA](https://www.fda.gov/food/foodborne-pathogens/cyclospora)
- [Trimethoprim-sulfamethoxazole compared with ciprofloxacin... - PubMed (PMID:10836915)](https://pubmed.ncbi.nlm.nih.gov/10836915/)
- [Highly Sensitive and Specific PCR Assay for Reliable Detection of Cyclospora cayetanensis Oocysts - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2493149/)
- [Mitochondrial Junction Region as Genotyping Marker for Cyclospora cayetanensis - EID/CDC](https://wwwnc.cdc.gov/eid/article/25/7/18-1447_article)
- [Investigation of US Cyclospora cayetanensis outbreaks in 2019... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8506454/)
- [Genotyping Cyclospora cayetanensis From Multiple Outbreak Clusters... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9200147/)
- [Development of a targeted amplicon sequencing method for genotyping Cyclospora cayetanensis - PubMed (PMID:37396378)](https://pubmed.ncbi.nlm.nih.gov/37396378/)
- [Evaluation of the Increased Genetic Resolution... - PubMed (PMID:38792677)](https://pubmed.ncbi.nlm.nih.gov/38792677/)
- [Cyclospora cayetanensis comprises at least 3 species that cause human cyclosporiasis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10090632/)
- [Three of a Kind: CDC Researchers Find Cyclospora is Not Just a Single Species | CDC AMD](https://www.cdc.gov/advanced-molecular-detection/php/success-stories/cyclospora.html)
- [The Complete Mitochondrial Genome of the Foodborne Parasitic Pathogen Cyclospora cayetanensis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4455993/)
- [Comparative sequence analysis of Cyclospora cayetanensis apicoplast genomes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5129617/)
- [Comparative genomics reveals Cyclospora cayetanensis possesses coccidia-like metabolism and invasion components but unique surface antigens - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4851813/)
- [Human Challenge Pilot Study with Cyclospora cayetanensis - EID/CDC (PMID:15200870)](https://wwwnc.cdc.gov/eid/article/10/4/03-0356_article)
- [Hastening Progress in Cyclospora Requires Studying Eimeria Surrogates - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9608778/)
- [Chronic Cyclospora infection in a heart transplant patient with intestinal malabsorption - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12584178/)
- [The global prevalence of Cyclospora cayetanensis infection: A systematic review, meta-analysis, and meta-regression - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0001706X24000597)
- [Cyclospora Cayetanensis—Major Outbreaks from Ready to Eat Fresh Fruits and Vegetables - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7699734/)
- [Cyclosporiasis - MalaCards](https://www.malacards.org/card/cyclosporiasis)
- [2026 ICD-10-CM Diagnosis Code A07.4: Cyclosporiasis](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A00-A09/A07-/A07.4)
- [Molecular Identification and Survey of Cyclospora spp. in Cattle in Shanxi Province, North China - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11274234/)