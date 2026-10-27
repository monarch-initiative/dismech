---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T23:23:00.247090'
end_time: '2026-09-03T23:33:22.703319'
duration_seconds: 622.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chondrodysplasia Blomstrand Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 48
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.02
  unresolved_terms:
  - HP:0002796
  obsolete_terms:
  - term_id: GO:0019933
    ontology_label: obsolete cAMP-mediated signaling
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Chondrodysplasia_Blomstrand_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chondrodysplasia Blomstrand Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chondrodysplasia Blomstrand Type** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chondrodysplasia Blomstrand Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chondrodysplasia Blomstrand Type** covering all of the
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


# Chondrodysplasia Blomstrand Type: Disease-Characteristics Report

## Executive summary

Chondrodysplasia Blomstrand type—more commonly **Blomstrand osteochondrodysplasia (BOCD)** or **Blomstrand lethal chondrodysplasia (BLC)**—is an exceptionally rare, autosomal-recessive, prenatal-onset skeletal dysplasia caused by biallelic severe loss-of-function variants in **PTH1R**, encoding parathyroid hormone/parathyroid hormone-related peptide receptor type 1. Loss of fetal PTHrP–PTH1R signaling prematurely drives growth-plate chondrocytes from proliferation into hypertrophy and mineralization. The resulting generalized advanced ossification, shortened bones, narrow thorax, and pulmonary hypoplasia usually cause stillbirth or death minutes to hours after delivery. There is no disease-modifying treatment or validated population prevalence estimate. The strongest evidence comes from a small number of fetal case reports/series, receptor-functional studies, knockout mice, and zebrafish experiments; quantitative phenotype frequencies should therefore be interpreted cautiously. (portalescastillo2025humandiseasescaused pages 1-2, hoogendam2007novelmutationsin pages 1-2)

---

## 1. Disease information

### Definition and nomenclature

BOCD is a lethal sclerosing skeletal dysplasia characterized by **accelerated endochondral ossification and advanced skeletal maturation**, rather than delayed mineralization. The literature uses *Blomstrand osteochondrodysplasia*, *Blomstrand chondrodysplasia*, *Blomstrand lethal osteochondrodysplasia*, *Blomstrand lethal chondrodysplasia*, and occasionally *Blomstrand syndrome*. Historical publications distinguish **type I**, with complete PTH1R inactivation and extremely short malformed bones, from the somewhat less severe but still lethal **type II**, associated with small amounts of residual receptor activity. (portalescastillo2025humandiseasescaused pages 8-8, portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 1-2)

**Suggested identifiers—verify against the current release before database ingestion:**

- **OMIM:** 215045, *Blomstrand chondrodysplasia*.
- **Orphanet:** commonly indexed as *Blomstrand lethal chondrodysplasia*; the current ORPHA numerical record should be release-validated.
- **MONDO:** map through the current MONDO cross-reference to OMIM:215045; a stable MONDO number was not present in the retrieved primary literature and should not be inferred from text-mining alone.
- **MeSH:** no clearly disease-specific MeSH descriptor was found; indexing generally falls under osteochondrodysplasias/chondrodysplasia.
- **ICD-10:** no dedicated code; typically falls under **Q77.8**, other osteochondrodysplasia with defects of growth of tubular bones and spine.
- **ICD-11:** use the current rare skeletal-dysplasia hierarchy; no disease-specific leaf code was verified in the retrieved evidence.

The evidence is predominantly **aggregated disease-level literature derived from individually described fetuses**, postmortem examinations, family segregation, and experimental models—not EHR-derived population data. Hoogendam et al. studied two type-I and three type-II families using clinical examination, imaging, histology, sequencing, RNA analysis, and receptor assays. (hoogendam2007novelmutationsin pages 1-2)

**Landmark source:** Hoogendam et al., published online 12 December 2006 and in March 2007, DOI: https://doi.org/10.1210/jc.2006-0300. The abstract concludes: **“type I BOCD is caused by a complete inactivation of the PTHR1, whereas low levels of residual activity … result in the relatively milder presentation of type II BOCD.”** (hoogendam2007novelmutationsin pages 1-2)

---

## 2. Etiology

### Causal factor

The primary cause is **germline biallelic PTH1R loss of function**. PTH1R is a class-B G-protein-coupled receptor activated by PTH and PTHrP. In fetal growth plates, its critical ligand is PTHrP. Severe receptor loss disrupts PTHrP-dependent maintenance of proliferating chondrocytes, causing premature hypertrophic differentiation and ossification. (martin2016parathyroidhormonerelatedprotein pages 19-20, portalescastillo2025humandiseasescaused pages 1-2, portalescastillo2025humandiseasescaused pages 2-4)

### Risk factors

- **Genetic:** two pathogenic PTH1R alleles are required for classic BOCD. Reported lesions include nonsense, frameshift, missense, and splice-altering variants. Consanguinity increases the probability that both parents carry the same rare allele, but affected offspring have also occurred in nonconsanguineous families. (hoogendam2007novelmutationsin pages 1-2)
- **Family history:** affected siblings and recurrent fetal losses are important clues. One Asian first-cousin couple had three similarly affected fetuses. (hoogendam2007novelmutationsin pages 1-2, hoogendam2007novelmutationsin pages 2-3)
- **Sex:** both male and female fetuses are reported; no sex-linked difference is established.
- **Environmental, infectious, lifestyle, occupational, maternal-age, or toxicant risks:** none established.

### Protective factors and gene–environment interaction

No protective PTH1R allele, diet, medication, lifestyle factor, or reproducible gene–environment interaction has been reported. Because BOCD is a highly penetrant developmental receptor-null phenotype, environmental modification is not expected to prevent the skeletal lesion once an affected fetal genotype is present. This is an inference, not evidence from intervention studies.

---

## 3. Phenotypes

All manifestations are congenital/prenatal, generally severe, and nonremitting. Frequencies below are qualitative unless a study supplied a number; the literature is too small and ascertainment-biased for robust percentages.

| Phenotype | Character and course | Suggested HPO term |
|---|---|---|
| Advanced skeletal maturation/generalized premature ossification | Defining radiographic sign; severe and prenatal | Accelerated skeletal maturation **HP:0005616**; abnormality of ossification **HP:0000135** |
| Generalized osteosclerosis/increased bone density | Common radiographic manifestation | Osteosclerosis **HP:0002796**; increased bone mineral density **HP:0004340** |
| Micromelia/short limbs and short tubular bones | Severe, symmetric, prenatal | Micromelia **HP:0002983**; short long bones **HP:0003026** |
| Metaphyseal broadening | Tubular bones short with widened metaphyses | Metaphyseal widening **HP:0003016** |
| Narrow/small thorax and short ribs | Severe; directly compromises lung development | Narrow chest **HP:0000774**; short ribs **HP:0000773** |
| Pulmonary hypoplasia/respiratory failure | Major lethal complication | Pulmonary hypoplasia **HP:0002089**; neonatal respiratory distress **HP:0002643** |
| Micrognathia, small viscerocranium, protruding tongue, flat/hypoplastic nasal bridge | Characteristic craniofacial pattern | Micrognathia **HP:0000347**; tongue protrusion **HP:0010808**; depressed nasal bridge **HP:0005280** |
| Macrocephaly or relatively large head | Prenatal ultrasound/clinical sign in some cases | Macrocephaly **HP:0000256** |
| Polyhydramnios | Prenatal complication in reported pregnancies | Polyhydramnios **HP:0001561** |
| Fetal hydrops/generalized edema | Reported in several fetuses | Hydrops fetalis **HP:0001789**; generalized edema **HP:0000969** |
| Premature ossification of patella, carpal/tarsal and laryngeal cartilage | Highly distinctive evidence of accelerated maturation | Premature ossification **HP:0005616**; abnormal laryngeal cartilage morphology, closest HPO mapping |
| Reduced resting/proliferative growth-plate zones | Histopathologic abnormality | Abnormal epiphyseal morphology **HP:0005930**; abnormal chondrocyte morphology, ontology mapping recommended |
| Absent nipples/mammary glands | Extraskeletal developmental manifestation | Athelia **HP:0002550**; mammary-gland aplasia **HP:0010615** |
| Tooth-development/eruption abnormality | Demonstrated through the shared PTH1R pathway; often not clinically observable because of lethality | Failure of tooth eruption **HP:0006291** |
| Aortic coarctation | Variable; one review of historical reports and a zebrafish study cited approximately 50% of described infants, but this estimate is based on very few selected cases | Coarctation of the aorta **HP:0001680** |
| Cataract/possible hypocalcemia | Cataracts reported in at least two fetuses; hypocalcemia was suggested, not consistently measured | Congenital cataract **HP:0000519**; hypocalcemia **HP:0002901** |

A well-characterized 32-week fetus had polyhydramnios, a relatively large head, small thorax, lung hypoplasia, and very short dense tubular bones. Examination showed severe micrognathia, protruding tongue, narrow thorax, absent nipples, and symmetric limb shortening; imaging showed generalized osteosclerosis, advanced skeletal maturation, short ribs, ossified laryngeal cartilage and patella, metaphyseal broadening, and extensive carpal/tarsal ossification. (hoogendam2007novelmutationsin pages 2-3)

Histology demonstrated reduced epiphyses and resting/proliferative zones, near absence of columnar proliferating chondrocytes, disordered hypertrophic columns, and an irregular growth-plate–primary-spongiosa boundary. A 2023 reanalysis further identified ectopic calcified islands, disordered trabeculae, and AGGRECAN-positive ectopic chondrocytes in diaphyseal trabecular-like structures. (csukasi2023skeletaldiseasescaused pages 2-5, hoogendam2007novelmutationsin pages 2-3)

**Quality of life:** validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data do not exist. The disorder is usually incompatible with postnatal survival; family burden centers on fetal loss, reproductive decision-making, and perinatal bereavement.

---

## 4. Genetic and molecular information

- **Gene:** **PTH1R**, parathyroid hormone 1 receptor; chromosome 3p21 region; HGNC-approved symbol PTH1R.
- **Protein:** PTH/PTHrP receptor type 1, a seven-transmembrane class-B GPCR.
- **Origin:** constitutional/germline, not somatic.
- **Inheritance:** autosomal recessive.
- **Functional class:** severe or complete loss of receptor signaling. Type-II disease can retain a small amount of correctly spliced transcript or residual receptor function. (portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 1-2, hoogendam2007novelmutationsin pages 3-5)

The established severe alleles and functional interpretation are summarized below.

| Nucleotide change | Protein consequence | Variant class | Zygosity | Review-reported rsID / allele-frequency field | Functional effect | Phenotype and nomenclature notes |
|---|---|---|---|---|---|---|
| `c.1049+27C&gt;T` | `p.G350fsX351` | Intronic aberrant splice-donor creation; frameshift and truncation | Homozygous | rs2107055197; none reported | Preferential aberrant splicing produces a truncated receptor lacking transmembrane domains 5–7 and the cytoplasmic C-terminus; low-level normal transcript remains; severe loss of function | Type II BOCD, consistent with residual transcript. The 2007 legacy designation was “intron M4 +27C&gt;T”; the 2025 review maps it as `c.1049+27C&gt;T`, `p.G350fsX351` (hoogendam2007novelmutationsin pages 7-8, portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 3-5) |
| `c.1148G&gt;A` | `p.L373_R383del` | Splice-acceptor alteration causing an in-frame deletion | Compound heterozygous | rs398122843; 0.7 | Severe receptor loss of function | Severe Blomstrand chondrodysplasia; the nucleotide change has also been reported in PTH1R-related primary failure of tooth eruption, indicating genotype–phenotype overlap (risom2013identificationofsix pages 7-7, portalescastillo2025humandiseasescaused pages 2-4) |
| `c.310C&gt;T` | `p.R104X` | Nonsense; premature termination | Homozygous | rs121434604; 0.14 | Produces only the signal peptide and first 79 amino acids, eliminating functional extracellular, transmembrane, and intracellular domains; complete or severe loss of function | Classical severe type I BOCD. The 2007 legacy description gives `338C&gt;T` with `R104X`; the 2025 review uses `c.310C&gt;T`, `p.R104X` (hoogendam2007novelmutationsin pages 1-2, portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 3-5) |
| `c.395C&gt;T` | `p.P132L` | Missense | Homozygous | rs121434599; 0.36 | Markedly impaired PTHrP binding and signaling with low residual activity; classified as severe loss of function | Recurrently associated with relatively milder type II BOCD, supporting a residual-activity–severity relationship (hoogendam2007novelmutationsin pages 7-8, martin2016parathyroidhormonerelatedprotein pages 19-20, hoogendam2007novelmutationsin pages 1-2, portalescastillo2025humandiseasescaused pages 2-4) |
| `c.1093delG` | `p.V365CfsX141` | Single-nucleotide deletion; frameshift and premature termination | Homozygous | rs1304201852; 0.44 | Severe receptor loss of function | Severe lethal Blomstrand chondrodysplasia; type assignment was not specified in the extracted review table (portalescastillo2025humandiseasescaused pages 2-4, portalescastillo2025humandiseasescaused pages 8-8) |
| Interpretation note | — | — | — | Values above are transcribed from the 2025 review’s field labeled “allele frequency” | These values are review-reported and are not necessarily validated population allele frequencies or percentages | Verify against the underlying population database and version before reuse (portalescastillo2025humandiseasescaused pages 2-4) |


*Table: Knowledge-base summary of five established severe PTH1R loss-of-function alleles associated with lethal Blomstrand chondrodysplasia. It records functional and phenotype evidence while flagging legacy nomenclature and uncertain review-reported frequency values.*

The numeric values reproduced in the artifact from the 2025 review’s “allele frequency” field are **not credible as unqualified population frequencies for a lethal recessive disorder** and may reflect database formatting or very-low-frequency units. They must be checked directly in the current gnomAD/ClinVar records before knowledge-base import. Absence or extreme rarity in population databases is expected for pathogenic BOCD alleles.

The 2007 functional work showed that p.R104X eliminates essentially all receptor domains. The intronic allele created a preferred aberrant splice boundary and a truncated receptor lacking transmembrane helices 5–7 and the cytoplasmic tail, although a small amount of normal transcript remained. Patient fibroblasts failed to accumulate cAMP after high-dose PTH or PTHrP. (hoogendam2007novelmutationsin pages 3-5)

No validated **modifier gene**, disease-specific methylation signature, histone-mark abnormality, recurrent chromosomal rearrangement, or pathogenic copy-number syndrome has been established. DEPTOR, DVL2, TAZ, HDAC4/5, MEF2, RUNX2, SOX9, and IHH are mechanistic pathway components, not proven human BOCD modifier genes.

---

## 5. Environmental information

No toxin, radiation, pollution, occupation, smoking, alcohol, nutrition, exercise pattern, medication, infection, or microbiome exposure is known to cause or trigger BOCD. It is not contagious and has no zoonotic transmission. Environmental-factor and prophylactic-vaccine fields are therefore **not applicable**.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic severe PTH1R variants lead to** absent or markedly reduced functional receptor at fetal growth-plate cells. (portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 3-5)
2. **Loss of receptor function leads to** failure of PTHrP-stimulated Gαs–adenylyl-cyclase–cAMP–PKA signaling; some variants also abolish phosphoinositide signaling. (guasto2021signalingpathwaysin pages 7-8, lai2008generegulationin pages 19-24)
3. **Reduced PTHrP signaling leads to** failure to maintain resting/proliferating chondrocytes and failure to delay hypertrophic differentiation. (martin2016parathyroidhormonerelatedprotein pages 19-20, portalescastillo2025humandiseasescaused pages 1-2)
4. **Loss of this restraint leads to** reduced SOX9-associated proliferative/chondrogenic activity and release of HDAC4/5–MEF2–RUNX2-mediated hypertrophic programs; the full downstream chain is demonstrated mainly in mouse growth plates and is mechanistically inferred for BOCD. (guasto2021signalingpathwaysin pages 7-8, nishimori2019pthrptargetshdac4 pages 17-17)
5. **Premature chondrocyte hypertrophy leads to** early cartilage mineralization, growth-plate exhaustion/disorganization, and accelerated endochondral bone formation throughout the skeleton. (portalescastillo2025humandiseasescaused pages 1-2, hoogendam2007novelmutationsin pages 2-3)
6. **Growth-plate disruption leads to** short malformed tubular bones, micromelia, osteosclerosis, advanced epiphyseal/carpal/tarsal/patellar ossification, and loss of normal bone–cartilage boundaries. (hoogendam2007novelmutationsin pages 2-3, csukasi2023skeletaldiseasescaused pages 2-5)
7. **Accelerated rib-cage ossification and short ribs lead to** a small rigid thorax, pulmonary hypoplasia, inability to ventilate, and perinatal death. (portalescastillo2025humandiseasescaused pages 1-2, hoogendam2007novelmutationsin pages 2-3)
8. **Parallel branch:** loss of PTHrP–PTH1R signaling during vascular development may lead to reduced local Notch signaling and endothelial loss, resulting in aortic obstruction/coarctation; this is supported by zebrafish knockdown and remains incompletely demonstrated in humans. (gray2013lossoffunction pages 5-6, gray2013lossoffunction pages 1-2)
9. **Exploratory branch:** PTH1R loss may dysregulate DEPTOR–DVL2–TAZ/mTOR-linked skeletal-progenitor fate, leading to ectopic chondrocytes and disordered osteogenic/chondrogenic differentiation; direct BOCD patient-cell validation is lacking. (csukasi2023skeletaldiseasescaused pages 6-8, csukasi2023skeletaldiseasescaused pages 8-9, csukasi2023skeletaldiseasescaused pages 2-5)

### Pathways and cells

The normal IHH–PTHrP feedback loop spaces hypertrophic differentiation: prehypertrophic chondrocytes produce IHH, which promotes periarticular PTHrP; PTHrP then acts on PTH1R-positive proliferating/prehypertrophic chondrocytes to delay hypertrophy. Cells moving away from the PTHrP source differentiate and re-express IHH. (martin2016parathyroidhormonerelatedprotein pages 19-20, guasto2021signalingpathwaysin pages 18-19)

PTH1R can couple to **Gαs/cAMP/PKA**, **Gαq/PLCβ/DAG/IP3/Ca²⁺**, and β-arrestin pathways. Gαs signaling supports proliferation and SOX9 while suppressing hypertrophic MEF2/RUNX2 activity via nuclear HDAC4. By contrast, PLC/Ca²⁺ signaling can favor hypertrophic differentiation. BOCD-causing receptor-null variants remove the coordinated response rather than selectively increasing one branch. (guasto2021signalingpathwaysin pages 7-8, portalescastillo2025humandiseasescaused pages 1-2)

The 2023 study found absent/low DEPTOR in BOCD ectopic chondrocytes and proposed that DEPTOR interactions with PTH1R, DVL2, and TAZ regulate TAZ localization and osteogenic/adipogenic/chondrogenic fate. However, most molecular experiments used immortalized mesenchymal cells, DEPTOR knockdown, HEK293T cells, or Jansen cells; BOCD patient cells were unavailable. These results are promising pathway refinement, not a validated therapeutic target. (csukasi2023skeletaldiseasescaused pages 6-8, csukasi2023skeletaldiseasescaused pages 5-6, csukasi2023skeletaldiseasescaused pages 8-9)

**Suggested GO biological-process terms:** endochondral ossification (GO:0001958); cartilage development (GO:0051216); chondrocyte differentiation (GO:0002062); regulation of chondrocyte differentiation (GO:0032330); bone mineralization (GO:0030282); cAMP-mediated signaling (GO:0019933); adenylate-cyclase-activating GPCR signaling (GO:0007189); skeletal-system development (GO:0001501); blood-vessel development (GO:0001568); Notch signaling (GO:0007219).

**Suggested Cell Ontology terms:** chondrocyte **CL:0000138**; hypertrophic chondrocyte (current CL child term should be release-checked); osteoblast **CL:0000062**; mesenchymal stem cell **CL:0000134**; vascular endothelial cell **CL:0000115**.

**Subcellular components:** plasma membrane (GO:0005886), receptor complex (GO:0043235), cytoplasm (GO:0005737), nucleus (GO:0005634). There is no evidence that BOCD is primarily mitochondrial, lysosomal, ER-storage, inflammatory, autoimmune, or metabolic.

---

## 7. Anatomical structures affected

**Primary:** appendicular and axial skeleton, fetal growth plates, epiphyseal cartilage, ribs, craniofacial skeleton, laryngeal cartilage, carpal/tarsal elements, patellae, and developing teeth. Suggested UBERON mappings include growth plate cartilage **UBERON:0004766**, cartilage tissue **UBERON:0002418**, bone tissue **UBERON:0002481**, rib **UBERON:0002228**, lung **UBERON:0002048**, mandible **UBERON:0001684**, and aorta **UBERON:0000947**.

**Secondary:** lungs are hypoplastic because of thoracic restriction; the aorta may show preductal coarctation; mammary glands/nipples may be absent; congenital cataracts are occasional. (portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 2-3)

The skeletal involvement is generalized and usually symmetric; no consistent lateralization is described.

---

## 8. Temporal development

- **Onset:** embryonic/fetal, during endochondral skeletal development.
- **Prenatal recognition:** possible in the first trimester in recurrent families and later through ultrasound evidence of short dense bones, small thorax, and polyhydramnios; historical literature contains a first-trimester diagnosis report. (portalescastillo2025humandiseasescaused pages 8-8)
- **Course:** continuously developmental rather than episodic or relapsing. Ossification becomes excessively advanced with gestation.
- **End stage:** miscarriage, termination after prenatal diagnosis, stillbirth, or death shortly after delivery from respiratory failure/pulmonary hypoplasia.
- **Remission/recovery:** none known.
- **Critical period:** early fetal growth-plate development. Intervention after severe thoracic and pulmonary maldevelopment would be unlikely to reverse anatomy; no prenatal molecular therapy has been tested.

---

## 9. Inheritance and population

BOCD is **autosomal recessive**. If both parents carry pathogenic alleles in the same gene, each pregnancy has the conventional Mendelian probabilities of 25% affected, 50% carrier, and 25% unaffected/noncarrier, assuming confirmed parental carrier status and no unusual allele behavior.

Penetrance of severe biallelic null genotypes appears high, but a formal penetrance estimate is impossible. Expressivity varies with residual receptor function: complete inactivation is associated with type I, whereas hypomorphic alleles can produce type II. Much milder biallelic PTH1R phenotypes—Eiken syndrome, PTH resistance, and tooth-eruption failure—show that genotype–phenotype prediction must incorporate functional severity rather than merely “biallelic versus monoallelic.” (portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 7-8, hoogendam2007novelmutationsin pages 1-2)

No anticipation, established germline-mosaicism series, founder effect, carrier frequency, ethnic enrichment, geographic endemicity, incidence, or prevalence per 100,000 has been established. Cases include European/Caucasian, Asian, and Turkish families and both sexes. Published case numbers remain only in the low tens; this is a literature impression, not a registry-derived statistic. Consanguinity is recurrent but not obligatory. (hoogendam2007novelmutationsin pages 1-2)

---

## 10. Diagnostics

### Clinical and prenatal approach

1. **Detailed fetal ultrasound:** assess long-bone length and density, thoracic size, ribs, craniofacial proportions, lungs, polyhydramnios, edema/hydrops, and associated cardiac anatomy.
2. **Fetal radiography or low-dose CT where clinically justified:** demonstrates generalized osteosclerosis and markedly advanced ossification, including unusually early carpal, tarsal, patellar, and laryngeal-cartilage mineralization.
3. **Fetal echocardiography:** evaluate the aortic arch because coarctation is reported.
4. **Molecular confirmation:** sequence **PTH1R** and perform deletion/duplication analysis if sequencing is negative. Parental testing establishes phase and recurrence risk.
5. **Postmortem examination:** skeletal survey, lung and cardiovascular examination, and growth-plate histology are valuable for definitive diagnosis and counseling.

The primary series explicitly combined “clinical, radiographical, histological, and biochemical” criteria with PTH1R analysis. (hoogendam2007novelmutationsin pages 1-2, hoogendam2007novelmutationsin pages 2-3)

### Genetic-test selection

- **Known familial variant:** targeted testing by chorionic-villus sampling or amniocentesis is preferred.
- **Strong BOCD phenotype:** single-gene PTH1R testing or a lethal skeletal-dysplasia panel with copy-number analysis.
- **Uncertain skeletal dysplasia:** trio WES/WGS can identify PTH1R and phenocopies. WGS is useful for deep-intronic/structural lesions; a 2007 type-I case had no coding or splice-boundary variant detected, illustrating that standard exon sequencing can miss a causal lesion. (hoogendam2007novelmutationsin pages 1-2, hoogendam2007novelmutationsin pages 3-5)
- **CMA/karyotype:** useful for a broader fetal-anomaly differential, but not the primary assay for this single-gene disorder.
- **FISH, mitochondrial testing, repeat-expansion testing, RNA-omics, proteomics, metabolomics, epigenomics, and liquid biopsy:** not routine BOCD tests.
- **RNA studies:** useful when a splice variant is suspected; RT-PCR demonstrated preferential aberrant splicing and residual normal transcript for intron M4+27C>T. (hoogendam2007novelmutationsin pages 7-8, hoogendam2007novelmutationsin pages 3-5)

### Differential diagnosis

Important alternatives include other lethal skeletal dysplasias—thanatophoric dysplasia, achondrogenesis, osteogenesis imperfecta type II, hypophosphatasia, short-rib thoracic dysplasias, campomelic dysplasia, and perinatal hypophosphatasia. **Advanced generalized ossification/osteosclerosis**, premature patellar/carpal/tarsal/laryngeal ossification, reduced growth-plate proliferation, and biallelic PTH1R loss distinguish BOCD. PTH1R-related differentials include Eiken syndrome, which has delayed rather than accelerated ossification; activating-PTH1R Jansen metaphyseal chondrodysplasia; and heterozygous PTH1R-associated primary failure of tooth eruption. (hoogendam2007novelmutationsin pages 1-2, risom2013identificationofsix pages 7-7, portalescastillo2025humandiseasescaused pages 2-4)

There are no consensus society diagnostic criteria, newborn screening, biochemical screening biomarker, or validated prenatal risk calculator.

---

## 11. Outcome and prognosis

Prognosis is uniformly grave for classic BOCD. A 32-week infant did not breathe and died within minutes; autopsy showed pulmonary hypoplasia and preductal aortic coarctation. The literature’s first described infant was delivered at 22 weeks and died shortly afterward. (portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 2-3)

No five- or ten-year survival statistics exist because classic disease is prenatal/perinatal lethal. The proximate mechanism is restrictive thoracic maldevelopment and lung hypoplasia; cardiovascular abnormalities may add risk. Type II is radiographically less severe but remains lethal. No validated prognostic biomarker exists beyond genotype/function and the severity of thoracic/pulmonary involvement. (portalescastillo2025humandiseasescaused pages 1-2, hoogendam2007novelmutationsin pages 1-2)

---

## 12. Treatment

No approved pharmacotherapy, gene therapy, cell therapy, RNA therapy, surgery, or disease-modifying prenatal intervention exists. A search of ClinicalTrials.gov retrieved **no relevant BOCD-specific interventional trial or NCT identifier**.

Management is therefore:

- multidisciplinary prenatal diagnosis and counseling;
- fetal echocardiographic and obstetric assessment;
- discussion of pregnancy options according to local law and family values;
- delivery planning that avoids futile traumatic intervention where lethality is certain;
- neonatal comfort care/palliative respiratory support when appropriate;
- autopsy/tissue preservation and molecular confirmation;
- psychological and bereavement support.

Suggested NCIT intervention concepts include **Genetic Counseling**, **Prenatal Genetic Testing**, **Palliative Care**, **Supportive Care**, and **Whole Exome Sequencing**; exact NCIT codes should be mapped in the current release.

PTH or PTHrP replacement is not an established therapy: severe receptor-null disease cannot be corrected simply by supplying more ligand. Experimental PTH1R inverse agonists developed for activating Jansen disease address the opposite signaling defect and are not applicable to BOCD. The 2023 DEPTOR–TAZ findings remain preclinical and do not constitute a treatment. (csukasi2023skeletaldiseasescaused pages 6-8, csukasi2023skeletaldiseasescaused pages 8-9)

---

## 13. Prevention

- **Primary prevention:** no lifestyle or environmental prevention is possible.
- **Reproductive prevention/choice:** carrier testing for relatives after identification of the familial alleles; preimplantation genetic testing for monogenic disease; targeted prenatal diagnosis by CVS or amniocentesis; early expert ultrasound.
- **Secondary prevention:** early fetal diagnosis prevents diagnostic uncertainty and permits informed pregnancy and delivery planning, but does not prevent disease progression.
- **Tertiary prevention:** comfort-focused perinatal care can reduce suffering; there is no way to prevent the lethal skeletal/pulmonary complication after it is established.
- **Immunization, public-health sanitation, exposure reduction, and medication prophylaxis:** not applicable.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart or breed predisposition was identified. Therefore, OMIA/VBO breed mapping and veterinary prevalence cannot presently be supplied. PTH1R signaling is evolutionarily conserved across vertebrates, but experimental phenocopies should not be labeled naturally occurring disease. There is no zoonotic potential or cross-species transmission.

---

## 15. Model organisms and experimental systems

### Mouse

**Pth1r-null** and **Pthlh/PTHrP-null** mice die neonatally and show shortened bones, abbreviated proliferative zones, disrupted growth-plate organization, premature hypertrophy and accelerated ossification, closely phenocopying human BOCD. Transgenic PTHrP expression in proliferating chondrocytes partially rescues Pthlh-null lethality, establishing tissue-specific pathway causality. Limitations include species-specific anatomy and the absence of human allelic heterogeneity. (martin2016parathyroidhormonerelatedprotein pages 19-20, portalescastillo2025humandiseasescaused pages 1-2, portalescastillo2025humandiseasescaused pages 2-4)

### Zebrafish

Morpholino knockdown of either pthr1 or pthrp caused a localized mid-aortic occlusion from endothelial loss, preceded by defective hypochordal Notch signaling; inducible Notch upregulation rescued the lesion. The abstract states: **“Loss of function of either PTHR1 or PTHrP leads to a localized aortic defect that is Notch dependent.”** This supports, but does not prove, a direct mechanism for human BOCD-associated coarctation. Morpholino partial knockdown and differences between fish aortic occlusion and human coarctation are major limitations. Gray et al., June 2013, DOI: https://doi.org/10.1161/ATVBAHA.112.300590. (gray2013lossoffunction pages 5-6, gray2013lossoffunction pages 1-2)

### Human tissue and cellular systems

Patient fetal growth plates provide the most disease-proximal pathology evidence. Patient dermal fibroblasts and transfected COS-7 cells established loss of PTH/PTHrP-induced cAMP signaling and residual activity for hypomorphic variants. These cells are useful for receptor pharmacology but do not fully reproduce growth-plate differentiation. (hoogendam2007novelmutationsin pages 2-3, hoogendam2007novelmutationsin pages 3-5)

The 2023 DEPTOR study used BOCD tissue, immortalized mesenchymal stem cells, HEK293T interaction assays, and Jansen fibroblasts. It linked DEPTOR–DVL2–TAZ to skeletal lineage choice, but lacked BOCD patient-derived progenitor cells and direct rescue of the lethal phenotype. Csukasi et al., January 2023, DOI: https://doi.org/10.3389/fcell.2022.963389. (csukasi2023skeletaldiseasescaused pages 6-8, csukasi2023skeletaldiseasescaused pages 5-6, csukasi2023skeletaldiseasescaused pages 8-9)

No validated BOCD iPSC, organoid, single-cell atlas, spatial-transcriptomic dataset, CRISPR screen, or integrated disease-specific proteomic/metabolomic/lipidomic signature was identified.

---

## Recent developments, 2023–2024, and expert assessment

The most disease-relevant 2023 advance was the identification of abnormal BOCD skeletal-progenitor patterning and low DEPTOR in ectopic chondrocytes, with a proposed DEPTOR–DVL2–TAZ mechanism. It expands BOCD biology beyond a simple “premature hypertrophy” model, but remains partly extrapolative because BOCD living cells were unavailable. (csukasi2023skeletaldiseasescaused pages 6-8, csukasi2023skeletaldiseasescaused pages 2-5, csukasi2023skeletaldiseasescaused pages 1-2)

A 2024 PTH1R family study concerned a heterozygous allele and incomplete penetrance in a broader PTH1R phenotype, not classic recessive lethal BOCD. Its relevance is chiefly interpretive: **PTH1R variant effect, zygosity, receptor domain, and residual signaling—not gene name alone—determine phenotype**. No 2023–2024 BOCD therapeutic trial, epidemiologic cohort, single-cell study, or survival improvement was identified.

The current expert view is consequently stable: classic BOCD is a receptor-loss developmental disorder in which complete PTH1R inactivation produces type-I disease, while residual activity can soften skeletal morphology to type II without reliably restoring viability. Recent mechanistic work refines downstream lineage biology, but diagnosis and family planning—not treatment—remain the principal real-world applications. (csukasi2023skeletaldiseasescaused pages 8-9, portalescastillo2025humandiseasescaused pages 2-4, hoogendam2007novelmutationsin pages 1-2)

## Evidence limitations

The evidence base comprises very few fetuses, heterogeneous historical reports, postmortem ascertainment, and model systems. Apparent frequencies—including the approximately 50% estimate for aortic coarctation—must not be treated as population estimates. There are no registries large enough to establish incidence, penetrance, sex ratio, carrier frequency, survival curves, quality-of-life scores, or treatment-response rates. Primary-study PMIDs were not consistently present in the retrieved full texts; DOI URLs have therefore been supplied rather than inventing unverified PMID mappings.

References

1. (portalescastillo2025humandiseasescaused pages 1-2): Ignacio Portales-Castillo, Jakob Höppner, Harald Jüppner, and Thomas J. Gardella. Human diseases caused by homozygous pth1r mutations. Frontiers in Endocrinology, Aug 2025. URL: https://doi.org/10.3389/fendo.2025.1641292, doi:10.3389/fendo.2025.1641292. This article has 4 citations.

2. (hoogendam2007novelmutationsin pages 1-2): J. Hoogendam, H. Farih‐Sips, L. C. Wÿnaendts, Clemens W.G.M. Löwik, J. Wit, and Marcel Karperien. Novel mutations in the parathyroid hormone (pth)/pth-related peptide receptor type 1 causing blomstrand osteochondrodysplasia types i and ii. The Journal of clinical endocrinology and metabolism, 92 3:1088-95, Mar 2007. URL: https://doi.org/10.1210/jc.2006-0300, doi:10.1210/jc.2006-0300. This article has 62 citations.

3. (portalescastillo2025humandiseasescaused pages 8-8): Ignacio Portales-Castillo, Jakob Höppner, Harald Jüppner, and Thomas J. Gardella. Human diseases caused by homozygous pth1r mutations. Frontiers in Endocrinology, Aug 2025. URL: https://doi.org/10.3389/fendo.2025.1641292, doi:10.3389/fendo.2025.1641292. This article has 4 citations.

4. (portalescastillo2025humandiseasescaused pages 2-4): Ignacio Portales-Castillo, Jakob Höppner, Harald Jüppner, and Thomas J. Gardella. Human diseases caused by homozygous pth1r mutations. Frontiers in Endocrinology, Aug 2025. URL: https://doi.org/10.3389/fendo.2025.1641292, doi:10.3389/fendo.2025.1641292. This article has 4 citations.

5. (martin2016parathyroidhormonerelatedprotein pages 19-20): T. John Martin. Parathyroid hormone-related protein, its regulation of cartilage and bone development, and role in treating bone diseases. Physiological reviews, 96 3:831-71, Jul 2016. URL: https://doi.org/10.1152/physrev.00031.2015, doi:10.1152/physrev.00031.2015. This article has 203 citations and is from a highest quality peer-reviewed journal.

6. (hoogendam2007novelmutationsin pages 2-3): J. Hoogendam, H. Farih‐Sips, L. C. Wÿnaendts, Clemens W.G.M. Löwik, J. Wit, and Marcel Karperien. Novel mutations in the parathyroid hormone (pth)/pth-related peptide receptor type 1 causing blomstrand osteochondrodysplasia types i and ii. The Journal of clinical endocrinology and metabolism, 92 3:1088-95, Mar 2007. URL: https://doi.org/10.1210/jc.2006-0300, doi:10.1210/jc.2006-0300. This article has 62 citations.

7. (csukasi2023skeletaldiseasescaused pages 2-5): Fabiana Csukasi, Michaela Bosakova, Tomas Barta, Jorge H. Martin, Jesus Arcedo, Maya Barad, Gustavo A. Rico-Llanos, Jennifer Zieba, Jose Becerra, Pavel Krejci, Ivan Duran, and Deborah Krakow. Skeletal diseases caused by mutations in pth1r show aberrant differentiation of skeletal progenitors due to dysregulation of deptor. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.963389, doi:10.3389/fcell.2022.963389. This article has 5 citations.

8. (hoogendam2007novelmutationsin pages 3-5): J. Hoogendam, H. Farih‐Sips, L. C. Wÿnaendts, Clemens W.G.M. Löwik, J. Wit, and Marcel Karperien. Novel mutations in the parathyroid hormone (pth)/pth-related peptide receptor type 1 causing blomstrand osteochondrodysplasia types i and ii. The Journal of clinical endocrinology and metabolism, 92 3:1088-95, Mar 2007. URL: https://doi.org/10.1210/jc.2006-0300, doi:10.1210/jc.2006-0300. This article has 62 citations.

9. (hoogendam2007novelmutationsin pages 7-8): J. Hoogendam, H. Farih‐Sips, L. C. Wÿnaendts, Clemens W.G.M. Löwik, J. Wit, and Marcel Karperien. Novel mutations in the parathyroid hormone (pth)/pth-related peptide receptor type 1 causing blomstrand osteochondrodysplasia types i and ii. The Journal of clinical endocrinology and metabolism, 92 3:1088-95, Mar 2007. URL: https://doi.org/10.1210/jc.2006-0300, doi:10.1210/jc.2006-0300. This article has 62 citations.

10. (risom2013identificationofsix pages 7-7): Lotte Risom, Line Christoffersen, Jette Daugaard-Jensen, Hanne Dahlgaard Hove, Henriette Skovgaard Andersen, Brage Storstein Andresen, Sven Kreiborg, and Morten Duno. Identification of six novel pth1r mutations in families with a history of primary failure of tooth eruption. PLoS ONE, 8:e74601, Sep 2013. URL: https://doi.org/10.1371/journal.pone.0074601, doi:10.1371/journal.pone.0074601. This article has 76 citations and is from a peer-reviewed journal.

11. (guasto2021signalingpathwaysin pages 7-8): Alessandra Guasto and Valérie Cormier-Daire. Signaling pathways in bone development and their related skeletal dysplasia. International Journal of Molecular Sciences, 22:4321, Apr 2021. URL: https://doi.org/10.3390/ijms22094321, doi:10.3390/ijms22094321. This article has 106 citations.

12. (lai2008generegulationin pages 19-24): LP Lai. Gene regulation in growth plate chondrocytes by the parathyroid hormone 1 receptor and the beta2-adrenergic receptor. Unknown journal, 2008.

13. (nishimori2019pthrptargetshdac4 pages 17-17): Shigeki Nishimori, Forest Lai, Mieno Shiraishi, Tatsuya Kobayashi, Elena Kozhemyakina, Tso-Pang Yao, Andrew B. Lassar, and Henry M. Kronenberg. Pthrp targets hdac4 and hdac5 to repress chondrocyte hypertrophy. JCI insight, Mar 2019. URL: https://doi.org/10.1172/jci.insight.97903, doi:10.1172/jci.insight.97903. This article has 64 citations and is from a domain leading peer-reviewed journal.

14. (gray2013lossoffunction pages 5-6): Caroline Gray, David Bratt, Julie Lees, Marc daCosta, Karen Plant, Oliver J. Watson, Sara Solaymani-Kohal, Simon Tazzyman, Jovana Serbanovic-Canic, David C. Crossman, Bernard D. Keavney, Andrea Haase, Kathryn McMahon, Martin Gering, Henry Roehl, Paul C. Evans, and Timothy J.A. Chico. Loss of function of parathyroid hormone receptor 1 induces notch-dependent aortic defects during zebrafish vascular development. Arteriosclerosis, Thrombosis, and Vascular Biology, 33:1257–1263, Jun 2013. URL: https://doi.org/10.1161/atvbaha.112.300590, doi:10.1161/atvbaha.112.300590. This article has 16 citations and is from a domain leading peer-reviewed journal.

15. (gray2013lossoffunction pages 1-2): Caroline Gray, David Bratt, Julie Lees, Marc daCosta, Karen Plant, Oliver J. Watson, Sara Solaymani-Kohal, Simon Tazzyman, Jovana Serbanovic-Canic, David C. Crossman, Bernard D. Keavney, Andrea Haase, Kathryn McMahon, Martin Gering, Henry Roehl, Paul C. Evans, and Timothy J.A. Chico. Loss of function of parathyroid hormone receptor 1 induces notch-dependent aortic defects during zebrafish vascular development. Arteriosclerosis, Thrombosis, and Vascular Biology, 33:1257–1263, Jun 2013. URL: https://doi.org/10.1161/atvbaha.112.300590, doi:10.1161/atvbaha.112.300590. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (csukasi2023skeletaldiseasescaused pages 6-8): Fabiana Csukasi, Michaela Bosakova, Tomas Barta, Jorge H. Martin, Jesus Arcedo, Maya Barad, Gustavo A. Rico-Llanos, Jennifer Zieba, Jose Becerra, Pavel Krejci, Ivan Duran, and Deborah Krakow. Skeletal diseases caused by mutations in pth1r show aberrant differentiation of skeletal progenitors due to dysregulation of deptor. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.963389, doi:10.3389/fcell.2022.963389. This article has 5 citations.

17. (csukasi2023skeletaldiseasescaused pages 8-9): Fabiana Csukasi, Michaela Bosakova, Tomas Barta, Jorge H. Martin, Jesus Arcedo, Maya Barad, Gustavo A. Rico-Llanos, Jennifer Zieba, Jose Becerra, Pavel Krejci, Ivan Duran, and Deborah Krakow. Skeletal diseases caused by mutations in pth1r show aberrant differentiation of skeletal progenitors due to dysregulation of deptor. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.963389, doi:10.3389/fcell.2022.963389. This article has 5 citations.

18. (guasto2021signalingpathwaysin pages 18-19): Alessandra Guasto and Valérie Cormier-Daire. Signaling pathways in bone development and their related skeletal dysplasia. International Journal of Molecular Sciences, 22:4321, Apr 2021. URL: https://doi.org/10.3390/ijms22094321, doi:10.3390/ijms22094321. This article has 106 citations.

19. (csukasi2023skeletaldiseasescaused pages 5-6): Fabiana Csukasi, Michaela Bosakova, Tomas Barta, Jorge H. Martin, Jesus Arcedo, Maya Barad, Gustavo A. Rico-Llanos, Jennifer Zieba, Jose Becerra, Pavel Krejci, Ivan Duran, and Deborah Krakow. Skeletal diseases caused by mutations in pth1r show aberrant differentiation of skeletal progenitors due to dysregulation of deptor. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.963389, doi:10.3389/fcell.2022.963389. This article has 5 citations.

20. (csukasi2023skeletaldiseasescaused pages 1-2): Fabiana Csukasi, Michaela Bosakova, Tomas Barta, Jorge H. Martin, Jesus Arcedo, Maya Barad, Gustavo A. Rico-Llanos, Jennifer Zieba, Jose Becerra, Pavel Krejci, Ivan Duran, and Deborah Krakow. Skeletal diseases caused by mutations in pth1r show aberrant differentiation of skeletal progenitors due to dysregulation of deptor. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.963389, doi:10.3389/fcell.2022.963389. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Chondrodysplasia_Blomstrand_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002796` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019933` (obsolete cAMP-mediated signaling) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.