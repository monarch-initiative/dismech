---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T09:19:19.600131'
end_time: '2026-08-19T09:24:12.612246'
duration_seconds: 293.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypotonia, Infantile, with Psychomotor Retardation and Characteristic
    Facies 3
  mondo_id: ''
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
  web_search_requests: 17
  num_turns: 22
  total_cost_usd: 2.0994012000000004
  session_id: 86e8a80a-e969-5cd5-92d5-6c93657803a0
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3** covering all of the
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

I now have sufficient primary-literature grounding to write the report.

I have enough to compile a comprehensive, well-cited report now.

# Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3 (IHPRF3 / TBCK-Related Neurodevelopmental Disorder)

## 1. Disease Information

**Overview.** Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3 (IHPRF3) — now more commonly termed **TBCK-related neurodevelopmental disorder (TBCK-NDD)**, **TBCK-related intellectual disability syndrome**, or **TBCK syndrome** — is a severe, progressive, autosomal recessive neurodevelopmental and neurodegenerative disorder caused by biallelic loss-of-function pathogenic variants in **TBCK** (TBC1-domain-containing kinase), located at chromosome 4q24. Onset is at birth or in early infancy, with congenital/infantile hypotonia, profound global developmental delay/intellectual disability, characteristic coarsening facial features, and — in contrast to many static encephalopathies — a **progressive, multisystem, neurodegenerative course** with brain atrophy, motor neuronopathy, and lysosomal storage pathology ([GeneReviews, NBK615430](https://www.ncbi.nlm.nih.gov/books/NBK615430/); [OMIM #616900](https://omim.org/entry/616900)).

**Key identifiers:**
- **OMIM phenotype:** #616900 (IHPRF3); **OMIM gene:** *TBCK*, 616899
- **MONDO:** MONDO:0014823
- **Orphanet:** ORPHA:488632 — "TBCK-related encephalopathy-severe hypotonia-craniofacial dysmorphism syndrome"
- **Disease Ontology:** DOID:0060935
- **Gene:** HGNC symbol *TBCK*; chromosomal location 4q24
- **Inheritance:** Autosomal recessive

**Synonyms/alternative names:** TBCK-related neurodevelopmental disorder (TBCK-NDD, the current GeneReviews-preferred term); TBCK-related intellectual disability syndrome; TBCK deficiency disorder (TBCK-DD); TBCK syndrome; TBCK encephaloneuronopathy; proposed CLN15 (a candidate 15th subtype of neuronal ceroid lipofuscinosis, based on storage pathology — see below); "Boricua"/Puerto-Rican-founder TBCK encephalopathy (for the R126X founder-variant cohort).

**Evidence base.** Data derive from a mix of (a) individual case reports and small case series identified via clinical exome/genome sequencing, (b) a larger founder-variant cohort of Puerto Rican ("Boricua") patients enabling more systematic natural-history characterization, and (c) an aggregated GeneReviews clinical synthesis drawing on published cohorts. As of the most recent literature, roughly ~150–160 affected individuals have been reported worldwide, making this an ultra-rare disease (biorxiv 2026.02.18.706703).

---

## 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) **loss-of-function variants in TBCK** are the sole known cause. No environmental, infectious, or multifactorial etiology has been described; this is a monogenic Mendelian disorder.

**Genetic risk factors:**
- **Recurrent/founder pathogenic variants:**
  - **c.376C>T (p.Arg126Ter)** — a nonsense founder variant identified in individuals of **Puerto Rican ("Boricua") ancestry**; carrier frequency reported at roughly **0.5%** in the ExAC Latino reference population, consistent with a founder effect and no known consanguinity in the affected families (Ortiz‑González et al., 2018, PMID: [29283439](https://pubmed.ncbi.nlm.nih.gov/29283439/)).
  - **c.2060-9050_2235+26133del35359 (p.Glu687ValfsTer9)** — a recurrent single-exon (exon 23) deletion that can be **missed by standard exome sequencing** and requires targeted deletion/duplication or genome-sequencing analysis (GeneReviews, NBK615430).
  - **c.247C>T (p.Arg83Ter)** — a novel homozygous nonsense variant (exon 3) reported in a Chinese proband, the first non-Caucasian IHPRF3 case, with an extremely low ExAC frequency (0.0000082) (PMC9587582; PMID: [PMC9587582](https://pmc.ncbi.nlm.nih.gov/articles/PMC9587582/)).
  - **c.831_832insTA** — a homozygous 2-bp insertion causing a frameshift/premature stop, from the original Bhoj et al. cohort (PMID: [27040691](https://www.medchemexpress.com/mce_publications/27040691.html)).
- **Population risk:** Individuals of Puerto Rican descent carry a substantially elevated risk due to the R126X founder allele; overall disease prevalence is estimated at up to ~1:1,000,000 worldwide but roughly **fourfold higher in Admixed American populations** (GeneReviews, NBK615430).
- **No environmental risk factors** have been identified — this is a purely genetic (autosomal recessive) condition.
- **Protective factors:** None specifically identified genetically; heterozygous carriers are asymptomatic, consistent with recessive, loss-of-function biology and no reported carrier phenotype.
- **Gene–environment interaction:** None established. The one "environmental" modulator studied experimentally is **dietary leucine**, which can pharmacologically stimulate residual mTORC1 signaling in patient fibroblasts (see Mechanism, below) — this is a proposed therapeutic lever rather than an etiologic risk factor.

---

## 3. Phenotypes

TBCK-NDD phenotype data below are drawn primarily from the GeneReviews cross-cohort synthesis (NBK615430) supplemented by Chong et al. 2016 (AJHG, PMID 27040692), Bhoj et al. 2016 (AJHG, PMID: 27040691), and Ortiz-González et al. 2018 (PMID 29283439).

| Phenotype | Frequency | Onset/Course | Suggested HPO term |
|---|---|---|---|
| Severe/profound infantile hypotonia, decreased/absent reflexes | 100% | Congenital, progresses from central hypotonia to combined central hypotonia + peripheral spasticity | HP:0008947 (Infantile axial hypotonia) / HP:0001344 (Absent/diminished deep tendon reflexes) |
| Global developmental delay / profound intellectual disability, absent or minimal speech | 100% (severe in majority) | Congenital onset; most never progress beyond independent sitting; do not achieve ambulation or spoken language | HP:0012736 (Profound global developmental delay) |
| Seizures / epilepsy | ~60–77% (60% in Puerto Rican cohort; 76.7% in GeneReviews synthesis) | Onset ages 0–3 yr; often initially febrile-provoked, later multifocal/refractory in adolescence; high status epilepticus risk | HP:0032661 (Focal-onset seizure) / HP:0002373 (Febrile seizure) |
| Motor neuronopathy / progressive distal-then-proximal weakness | Majority | Progressive; electrophysiology suggests anterior horn cell/motor neuron involvement | HP:0007373 (Motor neuron atrophy) |
| Respiratory insufficiency | 84% | Progressive (not congenital); most require nocturnal noninvasive ventilation by age 5; ~75% of teenagers require tracheostomy | HP:0002093 (Respiratory insufficiency) |
| Craniofacial dysmorphism (coarse facial features, bitemporal narrowing, high-arched eyebrows, tented/exaggerated Cupid's-bow upper lip, high nasal bridge, anteverted nares, high palate) | 85.7% (head shape abnormalities) | Present from infancy; facial features coarsen with age | HP:0000280 (Coarse facial features) |
| Macroglossia | Up to 90% by age 10 | Progressive, generally does not require surgery | HP:0000158 (Macroglossia) |
| Dyslipidemia (hypercholesterolemia and/or hypertriglyceridemia) | 86.6% | Emerges in childhood; monitored q1–2 years | HP:0003119 (Abnormal circulating lipid concentration) |
| Osteopenia/osteoporosis, fractures | 84% | Progressive; DXA every 2–3 years | HP:0000939 (Osteoporosis) |
| Ophthalmologic abnormalities (strabismus, ptosis, nystagmus, optic atrophy, cortical visual impairment) | ~75% | Variable onset; some progressive | HP:0000486 (Strabismus) / HP:0000648 (Optic atrophy) / HP:0100704 (Cerebral visual impairment) |
| Genitourinary findings (UTIs, nephrolithiasis, neurogenic bladder, nephrocalcinosis) | 60% by age 15 | Often presents in adolescence | HP:0000107 (Renal cyst) is not correct — better: HP:0000800 (Nephrolithiasis, HP:0000800) |
| Brain volume loss / atrophy, ventriculomegaly, thin corpus callosum, cerebellar hypoplasia, white-matter disease/leukodystrophy | Common, progressive | Present early, "becomes more prominent with age" | HP:0002059 (Cerebral atrophy) / HP:0002079 (Hypoplasia of the corpus callosum) / HP:0002518 (Cerebral white matter atrophy) |
| Feeding difficulty / dysphagia, need for gastrostomy | Common | Infantile onset, often progressive due to bulbar weakness | HP:0011968 (Feeding difficulties) |
| Left ventricular hypertrophy | Emerges late adolescence/adulthood | Monitored by serial echocardiogram | HP:0001712 (Left ventricular hypertrophy) |
| Macrocephaly at birth, normalizing later / variable microcephaly, brachycephaly, turricephaly | Macrocephaly 32%; microcephaly 14%; brachycephaly 23%; turricephaly 14% | Head-shape trajectory can shift over infancy (a case report documented macrocephaly at birth [+2.91 SD] normalizing by 15 months; PMC9587582) | HP:0000256 (Macrocephaly) / HP:0000252 (Microcephaly) |
| Developmental regression / neurologic decompensation with illness | Common ("most individuals") | Often prompts work-up for mitochondrial disease | HP:0002376 (Developmental regression) |

**Quality-of-life impact:** Profound, lifelong dependency — most individuals never achieve independent ambulation, expressive speech, or self-feeding, and require multidisciplinary supportive technology (augmentative/alternative communication devices including eye-gaze systems, gastrostomy, and — commonly by the teen years — tracheostomy and chronic ventilatory support). Life-limiting complications (status epilepticus, aspiration/respiratory infection, urosepsis) contribute to premature mortality; the oldest reported affected individual is 34 years old (GeneReviews NBK615430).

---

## 4. Genetic/Molecular Information

**Causal gene:** *TBCK* (TBC1-domain-containing kinase); OMIM gene 616899; chromosome 4q24.

**Variant classification/type:** Virtually all reported pathogenic variants are predicted **loss-of-function** — nonsense (e.g., p.Arg126Ter, p.Arg83Ter), frameshift (e.g., c.831_832insTA), splice-site (e.g., c.1170+1G>A, per ClinVar RCV001251176), and a recurrent multi-exon (exon 23) deletion. This uniform loss-of-function spectrum, together with recessive segregation, strongly supports **haploinsufficiency/complete loss of TBCK function** as the disease mechanism (Chong et al. 2016, PMID 27040692; Bhoj et al. 2016, PMID 27040691).

**Allele frequency:** The Puerto Rican founder allele p.Arg126Ter was found at ~0.5% frequency in the ExAC Latino population (Ortiz-González et al. 2018, PMID 29283439), consistent with the elevated disease prevalence estimated in Admixed American populations.

**Somatic vs. germline:** Germline only; no somatic mosaicism reported to date.

**Functional consequence — GAP domain / mTORC1 link:** TBCK contains a Rab-GAP-like (TBC) domain and was initially proposed to act as a **Rab GTPase-activating protein** regulating **mTORC1 signaling** (Chong et al. titled it "Recessive Inactivating Mutations in TBCK, Encoding a Rab GTPase-Activating Protein…", PMID 27040692). Patient fibroblasts and iPSC-derived neuronal models show **decreased phosphorylation of ribosomal protein S6**, indicating reduced basal mTORC1 signaling, which can be partially rescued by exogenous leucine supplementation (Bhoj et al. 2016, PMID 27040691; PMC9587582).

**Newer molecular identity — the FERRY complex:** More recent structural and proteomic work has redefined TBCK as the core scaffolding subunit ("Fy-1") of the **FERRY (Five-subunit Endosomal Rab5 and RNA/ribosome intermediarY) complex**, together with PPP1R21 (Fy-2), C12orf4 (Fy-3), CRYZL1 (Fy-4), and GATD1 (Fy-5). FERRY is a Rab5 effector that binds mRNA directly and links early endosomes to mRNA/ribosome trafficking for local translation (Schuhmacher et al. 2023, *Molecular Cell*; structural papers reviewed in "Neurogenetic disorders associated with mutations in the FERRY complex" PMID 40062705). Notably, at least three of the five FERRY subunits (TBCK, PPP1R21, and others) are independently linked to severe pediatric neurodevelopmental disorders, defining a candidate **novel disease class** of "FERRYopathies."

**Modifier genes:** None established.

**Epigenetic information:** Not reported for this disorder.

**Chromosomal abnormalities:** Not a copy-number/aneuploidy disorder in the classic sense; however, the recurrent exon-23 deletion (c.2060-9050_2235+26133del35359) is itself a small structural (multi-exon) deletion, underscoring the need for deletion/duplication-sensitive testing.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been identified — TBCK-NDD is a fully penetrant monogenic autosomal recessive disorder. The only "environmental" lever studied is dietary/pharmacologic **leucine supplementation** as a potential mTORC1-signaling stimulant (investigational, not disease-causing/-protective in a population sense).

---

## 6. Mechanism / Pathophysiology

**Causal chain (best current model):**

1. **Biallelic TBCK loss-of-function** → loss of TBCK protein / disruption of the pentameric **FERRY complex** (TBCK–PPP1R21–C12orf4–CRYZL1–GATD1).
2. **Impaired FERRY-mediated endosome–mRNA trafficking**: recent iPSC-neuron work shows TBCK-deficient neurons have **reduced axonal mRNA content** and **reduced levels of the lysosomal dynein/dynactin adaptor JIP4**, producing **lysosomal axonal retrograde-trafficking defects** — i.e., TBCK mediates coupled endolysosomal trafficking of both mRNA and lysosomes (Flores-Mendez et al., bioRxiv 2025.03.02.641041 / PMC11908138; PMID 40093117).
3. **Downstream mTORC1 dysregulation**: loss of TBCK function is associated with **reduced basal mTORC1 signaling** (decreased phospho-S6), which can be partially rescued in vitro with leucine (Bhoj et al. 2016, PMID 27040691; Ortiz-González et al. 2018, PMID 29283439).
4. **Autophagic-lysosomal dysfunction**: mTORC1 inhibition together with primary trafficking defects produces **aberrant autophagy and impaired glycosylated-protein degradation**, with secondary **mitochondrial respiratory defects** hypothesized to reflect impaired mitochondrial quality control (mitophagy) downstream of lysosomal dysfunction (Ortiz-González et al. 2018, PMID 29283439).
5. **Lysosomal storage / neurodegeneration**: neuropathology from affected individuals demonstrates **intraneuronal lipofuscin storage material**, prompting the proposal to classify TBCK deficiency as a novel subtype of **neuronal ceroid lipofuscinosis (candidate CLN15)** — a lysosomal storage disease with a distinctive (non-single) storage-product profile (Bharath et al./Acta Neuropathol Commun 2018, PMID 30591081).
6. **Clinical manifestation**: the combination of motor neuronopathy, progressive white-matter/cortical volume loss, and multisystem lysosomal-storage-driven dysfunction (skeletal, ophthalmologic, hepatic/GI, cardiac) produces the progressive, multi-organ TBCK-NDD phenotype.

**Molecular pathways:** mTOR/mTORC1 signaling (KEGG mTOR signaling pathway); Rab5-dependent endosomal trafficking (Reactome "Rab regulation of trafficking"); autophagy/mitophagy pathways.

**Cellular processes:** endosome-to-lysosome trafficking; local axonal translation (mRNA transport); autophagosome–lysosome fusion; motor neuron maintenance.

**Protein dysfunction:** Loss of TBCK's TBC-domain-containing scaffolding function within FERRY; the pseudo-GAP status of the TBC domain remains debated (recent reviews frame TBCK as possibly a pseudo-kinase/pseudo-GAP acting primarily as a structural FERRY scaffold rather than a catalytically active Rab-GAP; see "Revisit TBCK—A Pseudo Kinase or a True…" review).

**Tissue damage mechanisms:** neurodegeneration via impaired autophagic clearance and lysosomal storage; motor neuron loss producing distal-predominant neuromuscular weakness; likely oxidative/metabolic stress from secondary mitochondrial dysfunction.

**Suggested GO terms:** GO:0007040 (lysosome organization); GO:0016237 (lysosomal microautophagy)/GO:0006914 (autophagy); GO:0032008 (positive regulation of TOR signaling) / GO:1904262 (negative regulation of TORC1 signaling); GO:0006417 (regulation of translation) for FERRY-mediated local translation; GO:0032418 (lysosome localization).

**Suggested CL terms:** CL:0000540 (neuron), CL:0011005 (GABAergic interneuron) or generically CL:0000030 (glioblast)/CL:0000127 (astrocyte) given astroglial perturbation reported in mouse models; CL:0000100 (motor neuron) for the anterior-horn-cell/motor-neuronopathy component.

**Molecular profiling/advanced technologies:**
- **Proteomics**: unbiased proteomics on TBCK-deficient iPSC-neurons confirmed physical interaction with PPP1R21, C12orf4, and CRYZL1, cementing the FERRY-complex model (PMID 40093117).
- **Structural biology**: cryo-EM structures of the human FERRY complex (Schuhmacher et al. 2023, *Molecular Cell*) define TBCK's clamp-like architectural role.
- **Single-cell/model-organism data**: a new **Tbck knockout mouse** shows early-onset, progressive neuronal and astroglial perturbation in vivo (bioRxiv 2026.05.07.723566) and a distinctive craniofacial/dental **mineralization defect** (reduced calcium/phosphorus, increased carbon, altered Mg/Fe) detected by microCT, nanoindentation, and Raman spectroscopy (bioRxiv 2026.02.18.706703) — the first hard-tissue phenotyping of a TBCK model.
- **Zebrafish model**: functional dissection shows that disrupting TBCK's golgin-97/245-binding activity (rather than its putative catalytic site) impairs neuronal growth and brain development, supporting a scaffolding/trafficking role over enzymatic GAP activity.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Central nervous system (brain — cortex, white matter, cerebellum, corpus callosum; motor neurons/anterior horn); peripheral/neuromuscular system (distal-predominant weakness).
**Secondary/complication-driven organ involvement:** Respiratory system (progressive insufficiency, need for tracheostomy); skeletal system (osteopenia, scoliosis, short stature/brachymelia, craniofacial bone mineralization defects); gastrointestinal system (dysphagia, GERD, constipation, pancreatitis); ophthalmologic system; cardiovascular system (left ventricular hypertrophy); genitourinary system (nephrolithiasis, neurogenic bladder, recurrent UTIs); hepatic/metabolic (dyslipidemia).

**Tissue/cell level:** Cortical and cerebellar neurons; motor neurons (anterior horn); glial cells (astroglial perturbation per mouse model); dental/craniofacial mineralizing tissue (enamel/dentin — newly described mouse phenotype).

**Subcellular level (GO Cellular Component):** Lysosome (GO:0005764) — primary storage-pathology site; early endosome (GO:0005769) — FERRY complex localization; axon (GO:0030424) — site of mRNA/lysosome trafficking defects; mitochondrion (GO:0005739) — secondary respiratory-chain dysfunction.

**Localization (UBERON):** UBERON:0000955 (brain); UBERON:0002037 (cerebellum); UBERON:0002298 (corpus callosum); UBERON:0000010 (peripheral nervous system) / anterior horn of spinal cord; UBERON:0002048 (lung, respiratory insufficiency); UBERON:0001474 (bone tissue, osteopenia).

**Lateralization:** No lateralization pattern reported — bilateral/symmetric involvement throughout (consistent with a systemic monogenic metabolic-trafficking disorder rather than a focal structural lesion).

---

## 8. Temporal Development

- **Onset:** Congenital or early infantile — hypotonia and feeding difficulty typically present from birth or the first months of life. Macrocephaly can be present at birth and normalize by infancy in some patients (PMC9587582).
- **Onset pattern:** Insidious/congenital for the core neuromuscular phenotype; more overtly progressive for respiratory, skeletal, ophthalmologic, cardiac, and renal complications, which emerge over childhood–adolescence.
- **Disease stages:** No formal staging system exists, but the natural history is broadly: (1) infantile hypotonia/feeding difficulty → (2) childhood seizure onset and progressive weakness/spasticity, with brain-imaging changes becoming more prominent → (3) adolescent multisystem complications (respiratory failure requiring tracheostomy in ~75% of teens, osteopenia/fractures, dyslipidemia, LV hypertrophy, nephrolithiasis) → (4) adult survivors (oldest reported case age 34) with cumulative multi-organ burden.
- **Progression rate:** Variable but generally progressive/degenerative — a departure from many "static" congenital hypotonia syndromes; facial coarsening, macroglossia, and neuroimaging abnormalities are explicitly described as worsening with age.
- **Course pattern:** Chronic-progressive, punctuated by acute **developmental regression/neurologic decompensation during intercurrent illness** — a recurring theme that often prompts (but does not confirm) evaluation for mitochondrial disease.
- **Remission:** None reported — this is a non-remitting neurodegenerative disorder.
- **Critical periods:** Early identification (ideally via genome/exome sequencing sensitive to the recurrent exon-23 deletion) is important for anticipatory multidisciplinary surveillance before major complications (respiratory failure, fractures, cardiac hypertrophy) manifest.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive. For carrier (heterozygous) parents: 25% recurrence risk per pregnancy for an affected child, 50% chance of an asymptomatic carrier, 25% chance unaffected/non-carrier (GeneReviews NBK615430).
- **Penetrance:** Complete, given biallelic loss-of-function variants (no reported incompletely penetrant carriers).
- **Expressivity:** Variable in severity and specific complication burden, but the core hypotonia/developmental delay phenotype is consistently severe/profound.
- **Genetic anticipation:** Not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented but a standard consideration in recessive disorder genetic counseling.
- **Founder effect:** Well documented — the p.Arg126Ter (R126X) variant is a **Puerto Rican ("Boricua") founder allele**, identified in multiple unrelated Puerto Rican families without known consanguinity, with ExAC Latino carrier frequency ~0.5% (Ortiz-González et al. 2018, PMID 29283439).
- **Consanguinity:** Contributes to some non-founder cases (compound heterozygosity/homozygosity in consanguineous families reported in the original Chong/Bhoj cohorts) but is explicitly **not** a feature of the Puerto Rican founder cohort.
- **Carrier frequency:** ~0.5% in Puerto Rican/Latino reference populations for the R126X allele; not separately quantified for other populations.
- **Prevalence:** Estimated as high as 1:1,000,000 worldwide, roughly fourfold higher in Admixed American populations; a 2026 preprint estimates ~159 affected individuals reported worldwide to date, an ultra-rare-disease classification (biorxiv 2026.02.18.706703; GeneReviews NBK615430).
- **Geographic distribution:** Global, but with a documented cluster/founder-driven excess in Puerto Rico; a case series has extended reporting to non-Caucasian populations, including the first reported Chinese patient (PMC9587582), indicating the disorder is pan-ethnic but was initially ascertained predominantly in individuals of European/Latino descent.
- **Sex ratio:** No sex predilection reported (autosomal recessive).
- **Age distribution:** Pediatric-predominant cohort with survival into adulthood documented (oldest reported patient 34 years).

---

## 10. Diagnostics

**No consensus formal clinical diagnostic criteria exist** — diagnosis requires identification of biallelic pathogenic TBCK variants plus a compatible clinical picture (GeneReviews NBK615430).

**Genetic testing:**
- **First-line:** Exome or genome sequencing, or a multigene neurodevelopmental-disorder panel that includes TBCK.
- **Critical caveat:** The recurrent single-exon-23 deletion can be **missed by standard exome sequencing**; if a multigene panel is non-diagnostic, targeted deletion/duplication analysis or genome sequencing is preferred.
- **Detection yield:** ~75% of pathogenic alleles identified by sequence analysis; ~25% require gene-targeted deletion/duplication analysis.
- **Single-gene TBCK testing** alone is "rarely useful" and not generally recommended as a first step (given phenotypic overlap with other conditions).
- **Chromosomal microarray/karyotype/FISH:** Not primary tools (this is not a classical CNV syndrome, aside from the specific recurrent intragenic deletion).
- **Carrier/prenatal/preimplantation testing:** Available once a family's pathogenic variants are known; recommended particularly for reproductive partners of known carriers of the same ancestry (e.g., Puerto Rican descent).

**Clinical/laboratory tests:**
- **Brain MRI:** Cerebral atrophy, ex vacuo ventriculomegaly, thin/dysgenetic corpus callosum, cerebellar hypoplasia, white-matter abnormalities ranging from nonspecific changes to overt leukodystrophy.
- **EMG/nerve conduction studies:** Support a motor neuronopathy pattern underlying the progressive weakness.
- **Lipid panel:** Recommended every 1–2 years given the high prevalence of dyslipidemia (86.6%).
- **DXA scan:** Every 2–3 years for osteopenia surveillance.
- **Echocardiogram:** Periodic surveillance for LV hypertrophy in adolescence/adulthood.
- **Neuropathology (when available, e.g., at autopsy or muscle/skin biopsy):** Intraneuronal lipofuscin-like storage material supporting the proposed CLN15 classification (PMID 30591081).

**Differential diagnosis (per GeneReviews):**
- **NALCN-related IHPRF1** (the entity giving this OMIM series its name) — distinguished by congenital contractures/arthrogryposis and distinct dysmorphic features.
- **PPP1R21-related neurodevelopmental disorder** — phenotypically very similar (same FERRY complex), distinguished by blue sclerae.
- **SPTBN4 disorder** — distinguished by auditory neuropathy, atypical for TBCK-NDD.
- Other severe congenital hypotonia/encephalopathy syndromes and lysosomal storage disorders given the coarse facial features and storage pathology.

**Screening:** No population newborn-screening program exists; targeted carrier screening is reasonable in populations with known founder-variant enrichment (Puerto Rican ancestry).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal actuarial survival curves published; the disorder carries **reduced survival**, with the oldest documented living individual reported at 34 years of age. Cause-of-death-associated complications include respiratory infections, status epilepticus, and recurrent urosepsis (GeneReviews NBK615430).
- **Morbidity/function:** Profound, essentially universal lifelong disability — the large majority never achieve independent ambulation or expressive spoken language; augmentative communication (including eye-gaze technology) is beneficial for some.
- **Complications:** Respiratory failure/tracheostomy dependence (by teens in ~75%), refractory epilepsy/status epilepticus, fractures from osteopenia, cardiac hypertrophy, recurrent UTIs/nephrolithiasis, aspiration, pancreatitis.
- **Recovery potential:** None — this is a progressive neurodegenerative disorder without a curative treatment; management is entirely supportive.
- **Prognostic factors:** The Puerto Rican founder R126X variant has been associated with a particularly severe, progressive phenotype including chronic respiratory failure and tracheostomy dependency, suggesting some genotype-severity correlation, though data across the full variant spectrum remain limited.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is entirely **multidisciplinary supportive care** (GeneReviews NBK615430):

- **Feeding/nutrition:** Feeding therapy, low threshold for gastrostomy tube placement (NCIT:C15447 Dietary Intervention as a general term; specific procedure would map to a gastrostomy/enteral-access NCIT term).
- **Respiratory:** Noninvasive ventilatory support progressing to tracheostomy/chronic ventilation; aggressive pulmonary clearance (NCIT:C49236 Therapeutic Procedure).
- **Seizure management:** Standard antiseizure medications; **caution with valproic acid and ketogenic diet** given evidence of secondary mitochondrial dysfunction; seizure action plans given high status-epilepticus risk (NCIT:C15986 Pharmacotherapy + therapeutic_agent per specific ASM).
- **Musculoskeletal:** Physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), orthopedic management of scoliosis/fractures (NCIT:C16186 Orthopedic Surgical Procedure); **caution advised with bisphosphonate infusions** due to reported adverse effects in this population.
- **Ophthalmologic:** Annual ophthalmology evaluation, low-vision services.
- **Developmental/educational:** Early intervention (0–3 yr), special education, individualized education plans, augmentative/alternative communication (AAC) evaluation.
- **Other organ-specific management:** Standard treatment per specialist for dyslipidemia, LV hypertrophy, recurrent UTIs/nephrolithiasis, neurogenic bladder, and pancreatitis; macroglossia typically requires no surgical intervention.
- **Investigational/mechanistic-hypothesis therapy:** **Leucine supplementation** has been proposed as a means to pharmacologically boost residual mTORC1 signaling, based on in vitro rescue of phospho-S6 signaling in patient fibroblasts (Bhoj et al. 2016, PMID 27040691; discussed further in PMC9587582); this remains **experimental/theoretical**, with no registered clinical trial identified for TBCK-NDD specifically and prognosis under current management still generally described as unfavorable.
- **Genetic counseling** (NCIT:C15240) is a core management component given the autosomal recessive inheritance and founder-variant carrier screening implications.

**Surveillance schedule (per GeneReviews):** growth/nutrition and constipation/pancreatitis assessment at each visit; annual ophthalmology; lipid panel q1–2 years; echocardiogram q1–2 years in adolescence/adulthood; DXA q2–3 years; sleep studies and urologic evaluation as clinically indicated.

---

## 13. Prevention

- **Primary prevention:** Carrier screening and genetic counseling in at-risk populations (notably Puerto Rican ancestry, given the R126X founder allele), with reproductive options including preimplantation genetic testing and prenatal diagnosis once familial variants are known.
- **Secondary prevention:** Early diagnosis (ideally via exome/genome sequencing sensitive to the recurrent exon-23 deletion) to enable anticipatory multidisciplinary surveillance before major complications manifest.
- **Tertiary prevention:** The structured surveillance protocol above (respiratory, skeletal, cardiac, lipid, ophthalmologic, renal) is explicitly aimed at preventing/mitigating downstream complications of a known progressive disease course.
- **Immunization:** No disease-specific vaccine strategy; standard immunization plus attention to respiratory-infection risk given neuromuscular respiratory compromise.
- **Public health/environmental interventions:** Not applicable — no environmental risk factor exists to modify.
- **Prophylaxis:** No specific pharmacologic prophylaxis established; seizure action plans function as a rescue-prophylaxis strategy given high status-epilepticus risk.

---

## 14. Other Species / Natural Disease

- **Taxonomy of models used:** *Mus musculus* (NCBITaxon:10090); *Danio rerio* (NCBITaxon:7955).
- **Naturally occurring disease in other species:** No naturally occurring veterinary TBCK-deficiency disease has been reported in the literature surveyed; all animal data derive from engineered (knockout) models rather than spontaneous veterinary disease.
- **Gene orthologs:** Mouse *Tbck* (MGI ortholog of human TBCK) and zebrafish *tbck* ortholog have both been used for functional modeling (see below); NCBI Gene IDs for mouse *Tbck* and zebrafish *tbck* orthologs are available via NCBI Gene/Alliance of Genome Resources.
- **Comparative biology:** The FERRY complex and its endosomal mRNA-trafficking function appear conserved across vertebrate models used to date (mouse, zebrafish), supporting translational relevance of these systems to human disease mechanism, though full comparative pathology (e.g., degree of neurodegeneration, storage pathology) across species has not yet been systematically benchmarked against human neuropathology.
- **Zoonotic potential:** Not applicable (non-infectious monogenic disorder).

---

## 15. Model Organisms

- **Mouse (knockout) — in vivo neurodevelopmental model:** A newly reported *Tbck*-knockout mouse (biorxiv 2026.05.07.723566) provides "the first in vivo evidence of early-onset, progressive neuronal and astroglial perturbation" in a Tbck-deficient vertebrate, establishing a tractable platform for interrogating the neurodevelopmental trajectory of TBCK syndrome.
- **Mouse (knockout) — craniofacial/hard-tissue model:** The same or a related *Tbck*-knockout mouse line was used to characterize a previously unrecognized **mineralization phenotype**: reduced calcium/phosphorus content, increased carbon (organic matrix retention), and stage-dependent magnesium/iron alterations in developing enamel, detected via microCT, histology, nanoindentation, energy-dispersive spectroscopy, and Raman spectroscopy (biorxiv 2026.02.18.706703) — establishing multimodal hard-tissue analysis as a sensitive approach for early craniofacial phenotyping in this and other rare genetic disorders.
- **Zebrafish (*Danio rerio*):** Functional studies show that disrupting TBCK's **golgin-97/245-binding activity** (rather than its putative catalytic/GAP site) impairs neuronal growth and brain development, supporting a scaffolding/trafficking-centric (rather than enzymatic) disease mechanism and demonstrating the zebrafish model's utility for TBCK neurodevelopmental studies.
- **Human iPSC-derived neuronal models:** Patient-derived iPSC neurons homozygous for the Boricua p.R126X variant show reduced axonal mRNA content, reduced levels of the lysosomal trafficking adaptor JIP4, and axonal lysosomal retrograde-trafficking defects — directly linking FERRY-complex loss to neuronal cell biology (Flores-Mendez et al. 2025, bioRxiv 2025.03.02.641041 / PMID 40093117).
- **Patient fibroblasts:** Used in the original discovery studies (Bhoj et al. 2016; Ortiz-González et al. 2018) to demonstrate reduced basal mTORC1 signaling (decreased phospho-S6), partial leucine-inducible rescue, aberrant autophagy, and mitochondrial respiratory chain defects.
- **Model limitations:** No model to date fully recapitulates the human multisystem phenotype (motor neuronopathy, seizures, skeletal, cardiac, renal, and lysosomal-storage components simultaneously); the mouse models are recent (2026 preprints) and longitudinal/behavioral phenotyping is still emerging. Translational fidelity between mouse/zebrafish neurodevelopmental phenotypes and the human progressive neurodegenerative course (e.g., extent of lipofuscin-like storage, degree of white-matter degeneration) has not yet been systematically validated — a candidate `HUMAN_MODEL_MISMATCH`-type consideration for future curation.
- **Resources:** MGI (for *Tbck* mouse allele records), ZFIN (for zebrafish *tbck* models), Alliance of Genome Resources (cross-species ortholog and phenotype aggregation).

---

## Key Primary Literature (PMID-cited)

1. Bhoj EJ et al. "Mutations in TBCK, Encoding TBC1-Domain-Containing Kinase, Lead to a Recognizable Syndrome of Intellectual Disability and Hypotonia." *Am J Hum Genet.* 2016. PMID: [27040691](https://www.medchemexpress.com/mce_publications/27040691.html)
2. Chong JX et al. "Recessive Inactivating Mutations in TBCK, Encoding a Rab GTPase-Activating Protein, Cause Severe Infantile Syndromic Encephalopathy." *Am J Hum Genet.* 2016;98:772-781. PMID: [27040692](https://pubmed.ncbi.nlm.nih.gov/27040692/)
3. Ortiz-González XR et al. "Homozygous boricua TBCK mutation causes neurodegeneration and aberrant autophagy." *Ann Neurol.* 2018;83(1):153-165. PMID: [29283439](https://pubmed.ncbi.nlm.nih.gov/29283439/)
4. [Author(s)]. "Homozygous TBC1 domain-containing kinase (TBCK) mutation causes a novel lysosomal storage disease – a new type of neuronal ceroid lipofuscinosis (CLN15)?" *Acta Neuropathol Commun.* 2018. PMID: [30591081](https://pubmed.ncbi.nlm.nih.gov/30591081/)
5. Identification of a novel pathogenic TBCK variant in a Chinese patient with IHPRF3: a case report. *BMC Pediatr.* 2022. PMC9587582.
6. Flores-Mendez M et al. "TBCK-deficiency leads to compartment-specific mRNA and lysosomal trafficking defects in patient-derived neurons." bioRxiv 2025.03.02.641041. PMID: [40093117](https://pubmed.ncbi.nlm.nih.gov/40093117/)
7. "Neurogenetic disorders associated with mutations in the FERRY complex: a novel disease class?" *Biol Open.* PMID: [40062705](https://pubmed.ncbi.nlm.nih.gov/40062705/)
8. "TBCK syndrome: a rare multi-organ neurodegenerative disease." PMID: [37455236](https://pubmed.ncbi.nlm.nih.gov/37455236/)
9. GeneReviews: "TBCK-Related Neurodevelopmental Disorder." NCBI Bookshelf NBK615430 (comprehensive clinical synthesis; frequencies cited throughout this report derive primarily from this source).
10. OMIM #616900 (IHPRF3) and #616899 (TBCK gene). https://omim.org/entry/616900

**Note on evidence gaps:** Several statistics in the GeneReviews synthesis (e.g., 76.7% seizures, 84% respiratory insufficiency, 86.6% dyslipidemia) are aggregate figures across the published cohort literature; the specific per-study denominators and exact primary-source attribution for each percentage were not independently re-verified against each underlying paper in this research pass and should be traced to primary sources (individually) before being encoded as frequency-qualified phenotype claims in a curated knowledge base, per standard evidence-verification practice.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.