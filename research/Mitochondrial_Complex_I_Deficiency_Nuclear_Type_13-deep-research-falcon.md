---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T17:04:18.959349'
end_time: '2026-09-03T17:16:37.843503'
duration_seconds: 738.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13), caused
    by biallelic NDUFA2 variants
  mondo_id: MONDO:0032618
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 45
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032618
    reported_labels:
    - if available
    ontology_label: mitochondrial complex I deficiency, nuclear type 13
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_13-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13), caused by biallelic NDUFA2 variants
- **MONDO ID:** MONDO:0032618 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13), caused by biallelic NDUFA2 variants** covering all of the
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
- **Disease Name:** Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13), caused by biallelic NDUFA2 variants
- **MONDO ID:** MONDO:0032618 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13), caused by biallelic NDUFA2 variants** covering all of the
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


# Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13)

## Executive summary and evidence limits

MC1DN13 is an ultra-rare autosomal-recessive mitochondrial disorder caused by biallelic pathogenic variants in **NDUFA2**, which encodes a nuclear-derived accessory subunit of respiratory-chain complex I. The documented clinical spectrum extends from severe congenital/infantile Leigh syndrome with cardiomyopathy and early death to infantile-onset cystic leukoencephalopathy with chronic motor and cognitive disability. The disease-specific literature found for this report comprises only **three molecularly characterized patients**—one published in 2008 and two in 2018—so percentages calculated from this denominator must not be interpreted as population frequencies. No additional disease-specific patient series from 2023–2024 was identified. Open Targets maps NDUFA2 (ENSG00000131495) as the sole associated target for MONDO:0032618 and links the association to PMID **18513682** and **28857146**. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 13-NDUFA2)

| MC1DN13 evidence snapshot | Evidence summary | Evidence status |
|---|---|---|
| Disease/gene | Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13; MONDO:0032618), caused by biallelic **NDUFA2** variants; NDUFA2 encodes an accessory subunit in the distal matrix/N module of respiratory-chain complex I. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 13-NDUFA2, hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 1-5) | Established disease–gene relationship |
| Known published patients | Disease-specific human evidence consists of **three molecularly characterized individuals**: one reported in 2008 and two in 2018. No larger NDUFA2-specific cohort was identified. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 1-5, perrier2018recessivemutationsin pages 5-8) | Direct human evidence; extremely small sample |
| Variants | Homozygous **c.208+5G>A** causing exon-2 skipping and truncation; homozygous **c.134A>C (p.Lys45Thr)**; and compound-heterozygous **c.134A>C (p.Lys45Thr)/c.225del (p.Asn76Metfs*4)**. The latter deletion was predicted loss-of-function; the 2018 report listed dbSNP rs757982865/rs863224084 and ClinVar submissions SCV000584198/SCV000584199. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 1-5, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14) | Direct genotype evidence; classifications should be rechecked against current ClinVar/ACMG criteria |
| Phenotypic spectrum | Severe congenital/infantile **Leigh disease** with neonatal cardiomyopathy, developmental impairment, optic atrophy, seizures, apnea, acidosis and death at 11 months; or infantile-onset **cystic leukoencephalopathy** with regression, spasticity/upper-motor-neuron signs, dystonia, epilepsy, intellectual disability, feeding/growth impairment and loss of ambulation. White-matter disease could be stable or progressive. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14) | Direct human evidence; frequencies are descriptive only (n=3) |
| Direct functional evidence | Patient muscle/fibroblasts showed isolated complex-I deficiency; for c.208+5G>A, activity was **20% and 36% of the lowest control value** in muscle and fibroblasts, respectively. Studies demonstrated reduced NDUFA2/NDUFA9, accumulation of complex-I subcomplexes, impaired assembly, mitochondrial depolarization and reduced pyruvate-linked ATP production. Wild-type NDUFA2 complementation partially rescued complex-I expression/activity and depolarization. (hoefs2008ndufa2complexi pages 4-5, hoefs2008ndufa2complexi pages 3-4, hoefs2008ndufa2complexi pages 2-3) | Direct biochemical and cellular evidence |
| Inheritance | **Autosomal recessive**; homozygous cases occurred in consanguineous Turkish and Pakistani families, while one non-consanguineous Asian-Indian patient was compound heterozygous. Parents tested were heterozygous carriers. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8) | Direct segregation evidence |
| Diagnosis | Genomic confirmation by NDUFA2-inclusive mitochondrial/Leigh panel, WES or WGS, with segregation and RNA analysis for splice variants; supportive evaluation includes lactate/metabolic testing, brain MRI/MRS, respiratory-chain enzyme assays, and BN-PAGE when needed. A 2024 French cohort supports WES/WGS over panels in diagnostically uncertain primary mitochondrial disease, but this is not NDUFA2-specific. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14, rouzier2024primarymitochondrialdisorders pages 1-2) | NDUFA2 testing is direct; broader diagnostic strategy partly inferred from mitochondrial-disease practice |
| Treatment/trials | No curative or NDUFA2-targeted clinical therapy and no relevant registered MC1DN13 trial were identified. Current care is supportive and multidisciplinary—management of seizures, feeding/nutrition, tone and mobility, cardiomyopathy, respiratory crises, and metabolic decompensation. Experimental complementation establishes biological plausibility for gene replacement but is not a clinical treatment. (hoefs2008ndufa2complexi pages 6-8, hoefs2008ndufa2complexi pages 4-5) | Supportive care inferred from broader mitochondrial/Leigh practice; gene rescue is preclinical in patient cells |
| Key evidence gaps | No disease-specific prevalence/incidence, penetrance estimate, prospective natural history, validated phenotype frequencies, treatment-response rates, quality-of-life measures, prognostic biomarkers, pharmacogenomics, dedicated animal/iPSC/organoid model, or single-cell/spatial/multi-omics study. ROS-mediated injury and precise cell-type vulnerability remain plausible complex-I mechanisms rather than demonstrated MC1DN13 mechanisms. (dang2020analysisofhuman pages 1-3, yin2024structuralinsightsinto pages 1-2, dang2020analysisofhuman pages 28-30) | Major uncertainty due to only three published individuals |


*Table: Compact summary of the direct human, biochemical, and genetic evidence for biallelic NDUFA2 disease. It highlights the three published individuals and separates demonstrated findings from broader complex-I or mitochondrial-disease inference.*

## 1. Disease information

### Definition

MC1DN13 is a Mendelian oxidative-phosphorylation disorder in which biallelic NDUFA2 variants reduce the assembly, stability, and activity of mitochondrial NADH:ubiquinone oxidoreductase, or respiratory-chain complex I. Complex I normally oxidizes NADH, transfers electrons to ubiquinone, and couples this reaction to proton translocation across the inner mitochondrial membrane, generating the electrochemical gradient used for ATP synthesis. NDUFA2 lies in the matrix-facing distal/N-module region and has a thioredoxin-like/ferredoxin-like fold. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 1-5)

### Identifiers and synonyms

- **MONDO:** MONDO:0032618.
- **Disease name:** mitochondrial complex I deficiency, nuclear type 13.
- **Abbreviation:** MC1DN13.
- **Causal gene:** **NDUFA2**, “NADH:ubiquinone oxidoreductase subunit A2”; Ensembl **ENSG00000131495**; OMIM gene **602137**. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 13-NDUFA2, hoefs2008ndufa2complexi pages 1-2)
- **Broader phenotype terms:** NDUFA2-related mitochondrial disease; NDUFA2-related complex I deficiency; NDUFA2-related Leigh disease; NDUFA2-related mitochondrial leukoencephalopathy.
- **Broader biochemical disease:** isolated mitochondrial complex I deficiency, historically OMIM **252010**. The Leigh phenotype is historically OMIM **256000**. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 1-5)
- **Orphanet:** a disease-specific Orphanet number was not established from the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific code or heading for MC1DN13 was identified; coding generally falls under mitochondrial metabolism disorders/mitochondrial disease or Leigh syndrome. These broader codes should not be represented as MC1DN13-specific identifiers.

The evidence is principally **patient-level primary literature**, subsequently aggregated by resources such as MONDO/Open Targets. It is not derived from EHR-scale cohorts or registries. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 13-NDUFA2, hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 1-5)

## 2. Etiology

### Causal factors and genetic risk

The necessary causal factor is biallelic germline NDUFA2 dysfunction. Three disease-associated genotypes were reported:

1. Homozygous **c.208+5G>A**, impairing the splice donor after exon 2, causing near-complete exon-2 skipping, frameshift, and a predicted 48-amino-acid truncated product rather than the normal 99-amino-acid protein. A small amount of correctly spliced transcript remained. The mutant protein was not detected and was inferred to be unstable and degraded. (hoefs2008ndufa2complexi pages 4-5, hoefs2008ndufa2complexi pages 3-4)
2. Homozygous **c.134A>C (p.Lys45Thr)**. The 2018 report regarded this conserved-residue substitution as damaging and found it once in heterozygous state in ExAC, reported as MAF 0.0008 in that paper. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)
3. Compound heterozygous **c.134A>C (p.Lys45Thr)** and **c.225del (p.Asn76Metfs*4)**. The deletion was absent from databases examined by the authors and predicted to be loss-of-function. The variants were deposited as dbSNP rs757982865/rs863224084 and ClinVar submissions SCV000584198/SCV000584199, although current ClinVar assertions and contemporary gnomAD frequencies should be rechecked before clinical use. (perrier2018recessivemutationsin pages 1-5, perrier2018recessivemutationsin pages 5-8)

The 2020 structural review also listed p.Glu57Ala and p.Asp50Asn among NDUFA2 substitutions, but the retrieved disease-specific primary reports do not establish these as additional MC1DN13 patient genotypes; they should therefore not be entered as definitively pathogenic without source-level reassessment. (dang2020analysisofhuman pages 1-3)

All established variants are **germline**, not somatic. Consanguinity increased homozygosity risk in the Turkish and Pakistani families. The two families carrying p.Lys45Thr shared a surrounding haplotype, suggesting a possible common ancestor, but no population-wide founder effect or carrier frequency has been demonstrated. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

### Environmental, protective, and gene–environment factors

No environmental exposure, infection, toxin, diet, lifestyle, sex, or age factor is known to cause MC1DN13. Febrile illness, varicella infection, vomiting, and likely catabolic stress temporally preceded decompensation in reported patients; these are plausible **triggers of metabolic crisis in genetically affected individuals**, not primary causes. One child deteriorated after two days of vomiting and recent varicella; both leukoencephalopathy cases presented around febrile illness. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8)

No validated genetic or environmental protective factor, modifier gene, epigenetic modifier, or gene–environment interaction has been demonstrated. Avoidance of fasting and prompt management of illness are precautionary mitochondrial-disease practices rather than proven MC1DN13-specific protective interventions.

## 3. Phenotypes

### Patient-level spectrum

**Patient 1, Hoefs et al. 2008:** Turkish boy, first-cousin parents, homozygous c.208+5G>A. Hypertrophic cardiomyopathy appeared on day 5; development was impaired from birth. MRI at four months showed cerebral atrophy and corpus-callosum hypoplasia, followed by optic atrophy. At 7.5 months, after vomiting and recent varicella, he developed severe acidosis, generalized tonic-clonic seizures, coma, and prolonged ventilatory dependence. Later MRI demonstrated corticospinal-tract demyelination and subacute necrotizing encephalomyelopathy consistent with Leigh syndrome. Recurrent apnea, bradycardia, seizures, and asystole culminated in death from cardiovascular arrest at 11 months. (hoefs2008ndufa2complexi pages 1-2)

**Patient 2, Perrier et al. 2018:** Pakistani girl, first-cousin parents, homozygous p.Lys45Thr, plus an independent homozygous SLC22A5 diagnosis. At eight months she had encephalopathy, hepatomegaly, hyperammonemia, and severe carnitine deficiency. Despite carnitine treatment she regressed until 12 months, then stabilized. Findings included severe leg-predominant spasticity and other upper-motor-neuron signs, cerebellar features, generalized dystonia, moderate intellectual disability, focal epilepsy from age six, and wheelchair dependence from age nine. MRI at age two showed periventricular/deep white-matter T2 abnormalities with cystic change involving corpus callosum and posterior internal capsule; imaging was stable at 12 years. Because SLC22A5 disease did not explain the leukodystrophy, WES established dual molecular diagnoses. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

**Patient 3, Perrier et al. 2018:** Asian-Indian girl of non-consanguineous parents, compound heterozygous p.Lys45Thr/p.Asn76Metfs*4. She presented at eight months with fever, failure to thrive, regression, feeding impairment requiring nasogastric feeding, severe irritability, absent purposeful hand use, and upper-motor-neuron signs. MRI showed confluent periventricular/subcortical cystic white-matter abnormalities involving posterior internal capsule, middle cerebellar peduncle, and cerebellar white matter. MRS showed a large lipid/lactate peak and low N-acetylaspartate. Disease and volume loss progressed by 13 months, while basal ganglia, thalami, and corpus callosum were spared. At four years she was small and microcephalic, used short sentences, walked with a walker, and used a wheelchair over longer distances. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

### Suggested phenotype ontology annotations

High-confidence HPO suggestions include:

- Global developmental delay — **HP:0001263**
- Developmental regression — **HP:0002376**
- Intellectual disability — **HP:0001249**
- Spasticity — **HP:0001257**
- Dystonia — **HP:0001332**
- Seizure — **HP:0001250**; generalized tonic-clonic seizure — **HP:0002069**; focal-onset seizure — **HP:0007359**
- Cerebral white-matter abnormality/leukoencephalopathy — **HP:0002500/HP:0002415**; cystic white-matter degeneration should additionally be recorded in free text because ontology specificity may vary by HPO release
- Cerebral atrophy — **HP:0002059**
- Hypoplasia of corpus callosum — **HP:0002079**
- Optic atrophy — **HP:0000648**
- Hypertrophic cardiomyopathy — **HP:0001639**
- Lactic acidosis/metabolic acidosis — **HP:0003128/HP:0001942**
- Apnea — **HP:0002104**; bradycardia — **HP:0001662**
- Failure to thrive — **HP:0001508**; feeding difficulties — **HP:0011968**
- Microcephaly — **HP:0000252**
- Hepatomegaly — **HP:0002240**; hyperammonemia — **HP:0001987**
- Elevated lactate on MRS — use abnormal brain MR spectroscopy/lactate annotation according to the current HPO release.

Apparent sample proportions are informative only as case descriptors: onset by eight months in 3/3; neurodevelopmental impairment/regression in 3/3; major neuroimaging abnormalities in 3/3; seizures in 2/3; major loss of mobility in both surviving leukoencephalopathy cases; cardiomyopathy and death in 1/3. These are not validated disease frequencies. Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been reported; nevertheless, feeding support, walker/wheelchair dependence, epilepsy, cognitive disability, and ventilatory crises imply profound functional burden. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8)

## 4. Genetic and molecular information

**NDUFA2** is a nuclear gene encoding a small imported mitochondrial accessory subunit. It belongs to the N module of complex I and contacts NDUFS1; p.Lys45Thr lies in a conserved residue in this structurally constrained region. Mammalian complex I has 45 subunits—14 core catalytic/proton-translocating and 31 accessory subunits—with NDUFA2 participating in the late-added N-module region. (dang2020analysisofhuman pages 1-3, yin2024structuralinsightsinto pages 1-2)

The established disease mechanism is recessive loss or severe impairment of function through abnormal splicing/protein instability, truncation, or damaging missense change. The c.208+5G>A allele markedly reduced NDUFA2 protein; NDUFA9 was also reduced, holo-complex I was depleted, and inactive subcomplexes accumulated. p.Lys45Thr-associated fibroblasts showed reduced complex-I activity and an approximately 750-kDa subcomplex, interpreted as an advanced assembly defect. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

There is no evidence for dominant-negative or gain-of-function disease, somatic mutation, a recurrent chromosomal rearrangement, large-scale copy-number syndrome, modifier gene, or disease-specific epigenetic signature. The coexisting SLC22A5 disorder in one patient is a **dual diagnosis**, not a demonstrated NDUFA2 modifier. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol use, diet, or infectious organism is an etiologic agent. Intercurrent infection, fever, vomiting, reduced intake, and fasting can increase energy demand or catabolism and may precipitate decompensation in mitochondrial disease; the reported temporal associations support clinical caution but do not prove a specific molecular interaction with NDUFA2. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic NDUFA2 variants lead to** abnormal transcript splicing, truncated protein, unstable protein, or dysfunctional p.Lys45Thr protein. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 5-8)
2. **Loss or dysfunction of NDUFA2 leads to** impaired late-stage N-module incorporation and/or stability of respiratory complex I, demonstrated by reduced NDUFA2/NDUFA9, diminished holoenzyme, and accumulated subcomplexes. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 8-14)
3. **Defective assembly leads to** isolated reduction of complex-I catalytic activity; in the splice-variant patient, activity was 20% of the lowest control value in muscle and 36% in fibroblasts, while complexes II–IV were preserved. (hoefs2008ndufa2complexi pages 3-4, hoefs2008ndufa2complexi pages 2-3)
4. **Reduced NADH oxidation/proton pumping leads to** loss of mitochondrial membrane potential and deficient oxidative ATP generation; patient muscle had markedly reduced pyruvate oxidation and ATP-plus-phosphocreatine production. (hoefs2008ndufa2complexi pages 1-2, hoefs2008ndufa2complexi pages 2-3)
5. **Bioenergetic failure results in** lactate accumulation/acidosis and inadequate energy supply, especially in brain, heart, optic pathways, and long motor tracts. The tissue-selective vulnerability is clinically supported, while the precise cell-type thresholds are inferred rather than directly measured. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8)
6. **Branch A—central nervous system:** energy failure **leads to** developmental impairment/regression, white-matter degeneration or Leigh-type necrotizing encephalomyelopathy, then spasticity, dystonia, seizures, cognitive impairment, and loss of ambulation. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)
7. **Branch B—cardiorespiratory system:** energy failure **leads to** cardiomyopathy and central/neuromuscular respiratory instability, then apnea, bradycardia/asystole, and potentially early death. This branch is demonstrated in only one patient. (hoefs2008ndufa2complexi pages 1-2)
8. **Possible oxidative-stress branch:** defective complex I **may lead to** increased ROS and oxidative injury. This is biologically plausible and supported for complex-I perturbation generally, but ROS was not directly quantified in MC1DN13 patients and should be marked **inferred**. (dang2020analysisofhuman pages 1-3, yin2024structuralinsightsinto pages 1-2)

Wild-type NDUFA2 complementation increased complex-I expression/activity and improved membrane depolarization in patient fibroblasts, strongly supporting causality and loss of function. It did not correct an unrelated NDUFS7-deficient line, supporting gene-specific rescue. (hoefs2008ndufa2complexi pages 6-8, hoefs2008ndufa2complexi pages 4-5)

Relevant pathway/ontology suggestions are mitochondrial electron-transport chain complex I assembly (**GO:0032981**), mitochondrial electron transport from NADH to ubiquinone (**GO:0006120**), oxidative phosphorylation (**GO:0006119**), ATP synthesis coupled electron transport (**GO:0042773**), proton motive force-driven ATP synthesis (**GO:0015986**), mitochondrial membrane-potential maintenance (**GO:0051881**), and—only as inferred—response to oxidative stress (**GO:0006979**). Cellular components include mitochondrial respiratory-chain complex I (**GO:0005747**), mitochondrial inner membrane (**GO:0005743**), mitochondrial matrix-facing peripheral arm, and respiratory-chain supercomplex (**GO:0098803**).

No MC1DN13-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics patient study was identified. The 2024 Ndufs4-null cryo-EM study is a major recent advance in general complex-I assembly: it places the NDUFA2-containing N module in the final assembly stage and shows loose N-module association in another Leigh model, but it is **not an NDUFA2 model**. (yin2024structuralinsightsinto pages 1-2)

## 7. Anatomical structures affected

Directly observed organs and sites include:

- **Central nervous system:** cerebral white matter, periventricular/deep and subcortical white matter, corticospinal tracts, corpus callosum, posterior limb of internal capsule, middle cerebellar peduncle, cerebellar white matter, and Leigh-type encephalomyelopathic regions. Suggested annotations include brain **UBERON:0000955**, cerebral white matter **UBERON:0002437**, corpus callosum **UBERON:0002336**, internal capsule **UBERON:0002199**, corticospinal tract, cerebellar white matter, and middle cerebellar peduncle according to current UBERON release. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)
- **Visual system:** optic nerve/optic pathways, evidenced by optic atrophy; optic nerve **UBERON:0000962**. (hoefs2008ndufa2complexi pages 1-2)
- **Heart:** myocardium, evidenced by neonatal hypertrophic cardiomyopathy; heart **UBERON:0000948**, cardiac muscle tissue **UBERON:0001133**. (hoefs2008ndufa2complexi pages 1-2)
- **Liver/metabolic system:** hepatomegaly and hyperammonemia occurred in one patient but are confounded by proven SLC22A5 deficiency and should not be assigned confidently to NDUFA2. (perrier2018recessivemutationsin pages 5-8)

Plausible vulnerable cell types include neurons (**CL:0000540**), oligodendrocytes (**CL:0000128**), astrocytes (**CL:0000127**), optic-nerve retinal ganglion-cell axons, and cardiomyocytes (**CL:0000746**). These cell-specific assignments are inferred from anatomy; no MC1DN13 single-cell pathology establishes the primary target population. The fundamental subcellular lesion is in mitochondria (**GO:0005739**) and the inner-membrane respiratory complex I (**GO:0005747**). Lesions were bilateral/diffuse where described; no consistent lateralization was reported.

## 8. Temporal development

Onset was neonatal in the severe Leigh case and at eight months in both leukoencephalopathy cases. The disease can therefore be congenital or infantile. Course was heterogeneous:

- Rapid neonatal/infantile progression with cardiomyopathy, crisis at 7.5 months, coma, recurrent respiratory/cardiac arrest, and death at 11 months. (hoefs2008ndufa2complexi pages 1-2)
- Regression between eight and 12 months followed by relative neurologic stabilization, although epilepsy and mobility loss emerged later; MRI remained stable between ages two and 12. (perrier2018recessivemutationsin pages 5-8)
- Progressive white-matter disease and volume loss over five months, followed by survival with major disability at age four. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

No formal stages, remission definition, progression rate, or prospective natural-history data exist. Early infancy and catabolic illness appear to be periods of high vulnerability. Lifelong disease should be expected in survivors; spontaneous cure has not been described.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For carrier parents, the standard Mendelian recurrence estimate is 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy, assuming both variants are confirmed in trans and no exceptional mechanism. Parents tested in the reports were heterozygous carriers. (hoefs2008ndufa2complexi pages 4-5, perrier2018recessivemutationsin pages 5-8)

Penetrance appears high for individuals with the reported biallelic genotypes, but only three patients are known and penetrance cannot be quantified. Expressivity is markedly variable, from fatal Leigh disease to chronic cystic leukoencephalopathy. There is no evidence of anticipation, sex linkage, sex bias, germline mosaicism, or a quantified founder effect. Both sexes are theoretically equally susceptible; the published sample includes one boy and two girls.

No MC1DN13-specific prevalence, incidence, carrier-frequency, ethnic-risk, or geographic-distribution estimate exists. The three patients came from Turkish, Pakistani, and Asian-Indian families; this does not establish population enrichment. For context only, a 2024 French study cites an estimated combined lifetime risk of 48.4 per 100,000 for 249 autosomal-recessive mitochondrial disorders and a broad primary mitochondrial disease prevalence near or above 20 per 100,000; these figures must not be assigned to MC1DN13. (rouzier2024primarymitochondrialdisorders pages 1-2)

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** infantile regression/delay, spastic-dystonic movement disorder, seizures, optic atrophy, cardiomyopathy, respiratory crises, or cystic white-matter disease should raise suspicion for mitochondrial/complex-I disease.
2. **MRI/MRS:** evaluate basal ganglia/brainstem for Leigh lesions and white matter for confluent, cystic, internal-capsule, callosal, and cerebellar involvement. A lactate peak and low NAA support metabolic injury but are not specific. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 8-14)
3. **Metabolic testing:** blood/CSF lactate, pyruvate, acid–base status, glucose, ammonia, plasma amino acids, acylcarnitines, urine organic acids, CK, liver indices, and carnitine. Normal or nonspecific results do not exclude disease.
4. **Genomic testing:** trio WES or WGS with both nuclear mitochondrial genes and mtDNA analysis is preferred for an undiagnosed Leigh/leukoencephalopathy phenotype; a comprehensive mitochondrial/Leigh/complex-I panel including NDUFA2 is an alternative. The 2024 MitoDiag cohort of more than 2,000 referrals found 397 nuclear-gene diagnoses spanning 172 genes and concluded that WES/WGS was more valuable than panels in “possible” mitochondrial disease, while also revealing many mimics. (rouzier2024primarymitochondrialdisorders pages 1-2)
5. **Variant confirmation:** Sanger confirmation, parental segregation, copy-number analysis, and RNA/cDNA analysis for suspected splice variants. The c.208+5G>A diagnosis required demonstration of exon-2 skipping. (hoefs2008ndufa2complexi pages 4-5, hoefs2008ndufa2complexi pages 3-4)
6. **Functional confirmation when needed:** respiratory-chain spectrophotometry in fibroblasts or muscle, oxygen-consumption analysis, BN-PAGE/in-gel activity, and immunoblotting for complex-I abundance/assembly. Reduced complex I in both muscle and fibroblasts and a 750-kDa subcomplex are directly documented. (hoefs2008ndufa2complexi pages 3-4, perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

WGS can detect coding, noncoding, mtDNA, and some structural variants concurrently. CMA, karyotype, and FISH are not first-line tests for a sequence-level recessive disorder but may be appropriate if copy-number or chromosomal disease is suspected. Repeat-expansion and liquid-biopsy testing are not relevant. RNA sequencing may resolve splice effects but has not been specifically reported for MC1DN13 beyond targeted RT-PCR.

### Differential diagnosis

Differentials include other nuclear or mtDNA complex-I deficiencies; other Leigh-spectrum genes; POLG and mitochondrial translation disorders; pyruvate-dehydrogenase deficiency; biotin-thiamine-responsive basal-ganglia disease; organic acidemias; primary leukodystrophies with cystic degeneration; and treatable metabolic mimics. The dual SLC22A5/NDUFA2 diagnosis illustrates why unexplained features should not automatically be attributed to an existing diagnosis. (perrier2018recessivemutationsin pages 5-8, perrier2018recessivemutationsin pages 8-14)

No validated MC1DN13 diagnostic criteria, newborn biochemical screen, or population-screening program exists. Cascade testing of relatives and targeted prenatal/preimplantation testing become possible after familial variants are established.

## 11. Outcome and prognosis

No survival curves, five- or ten-year survival rates, or life-expectancy estimates are available. One of three reported individuals died at 11 months; two survived to at least four and 12 years with substantial neurologic disability. This cannot support a mortality-rate estimate. (hoefs2008ndufa2complexi pages 1-2, perrier2018recessivemutationsin pages 5-8)

Morbidity includes epilepsy, spasticity, dystonia, cognitive disability, feeding support, impaired hand function, walker/wheelchair dependence, optic atrophy, cardiomyopathy, and respiratory crises. Potential complications include metabolic acidosis, aspiration/feeding complications, contractures, scoliosis, malnutrition, status epilepticus, cardiomyopathy/arrhythmia, and respiratory failure, although not all were observed in the three cases.

Possible poor-prognosis indicators—congenital onset, neonatal cardiomyopathy, severe residual complex-I deficiency, coma, apnea, and diffuse Leigh injury—are clinically plausible but unvalidated. The relatively prolonged courses with p.Lys45Thr suggest possible residual function, yet the sample is too small and one patient had a second metabolic disorder. No prognostic biomarker or treatment-response predictor exists.

## 12. Treatment

There is no approved disease-modifying or NDUFA2-specific treatment and no relevant registered MC1DN13 clinical trial was found. Current management is extrapolated from primary mitochondrial and Leigh-spectrum practice and should be coordinated by metabolic genetics, neurology, cardiology, pulmonology, nutrition, rehabilitation, and palliative-care teams as appropriate.

- **Acute illness:** rapid assessment; avoid prolonged fasting; provide glucose-containing fluids when appropriate while monitoring lactate, glucose, electrolytes, acid–base balance, ammonia, cardiac rhythm, and respiratory status. Treat infection, vomiting, dehydration, seizures, and acidosis according to cause and specialist guidance.
- **Epilepsy:** standard antiseizure treatment individualized for mitochondrial safety and comorbidities; avoid valproate when POLG disease has not been excluded or when hepatic risk is substantial.
- **Cardiorespiratory:** echocardiography/ECG surveillance, guideline-directed cardiomyopathy care, sleep/respiratory assessment, airway-clearance support, and ventilatory support when needed.
- **Nutrition:** swallowing evaluation, dietitian input, aspiration prevention, enteral feeding when necessary, and individualized avoidance of catabolic fasting.
- **Tone and disability:** physiotherapy, occupational and speech/communication therapy, mobility devices, orthoses, and treatment of spasticity/dystonia.
- **Vision/hearing and multisystem surveillance:** ophthalmology, audiology, renal, endocrine, hepatic, and developmental assessments based on phenotype.
- **Supplements:** thiamine, riboflavin, coenzyme Q10, carnitine, antioxidants, or “mitochondrial cocktails” are sometimes used empirically, but no MC1DN13 response rate or controlled evidence exists. Carnitine was specifically indicated for the separate SLC22A5 disorder in one patient and should not be interpreted as NDUFA2 therapy. (perrier2018recessivemutationsin pages 5-8)

Suggested NCIt intervention concepts include Genetic Counseling, Whole Exome Sequencing, Whole Genome Sequencing, Physical Therapy, Occupational Therapy, Speech Therapy, Enteral Nutrition, Anticonvulsant Therapy, Mechanical Ventilation, and Palliative Care; exact NCIt codes should be resolved against the current thesaurus release.

Wild-type NDUFA2 complementation rescued patient-cell defects and therefore provides proof-of-mechanism for eventual gene replacement, but the baculovirus experiment was a laboratory assay, not a therapeutic protocol. No NDUFA2 AAV, CRISPR, RNA therapy, cell therapy, or human pharmacogenomic strategy is available. (hoefs2008ndufa2complexi pages 6-8, hoefs2008ndufa2complexi pages 4-5)

## 13. Prevention

Primary lifestyle prevention is not possible because the disorder is inherited. Effective genetic prevention options after variant identification include carrier testing, cascade testing, reproductive counseling, preimplantation genetic testing for monogenic disease, chorionic-villus or amniotic-fluid prenatal diagnosis, and use of donor gametes. Because this is a **nuclear autosomal-recessive** disorder, mitochondrial replacement therapy does not address the causal variants.

Secondary prevention consists of early molecular diagnosis, anticipatory cardiac/respiratory/feeding surveillance, and rapid intervention during illness. Tertiary prevention targets seizures, aspiration, contractures, malnutrition, mobility loss, and metabolic crises. Vaccination is not disease-specific but routine immunization, including seasonal infection prevention where appropriate, may reduce catabolic illness exposure. No prophylactic medication has proven MC1DN13 efficacy.

## 14. Other species and natural disease

NDUFA2 and the architecture of respiratory complex I are evolutionarily conserved. Relevant comparative taxa include human (**NCBI Taxonomy 9606**), mouse (**10090**), zebrafish (**7955**), fruit fly (**7227**), and *Caenorhabditis elegans* (**6239**). However, no naturally occurring veterinary disease conclusively attributable to biallelic orthologous NDUFA2 variants was identified, and no breed-specific VBO annotation is warranted. The disorder is noninfectious and has no zoonotic or cross-species transmission.

Comparative structural work supports conservation of the complex-I N module, but species differ in assembly and active/deactive-state regulation. Consequently, ortholog conservation supports pathogenic plausibility but does not guarantee faithful reproduction of the human white-matter phenotype. (yin2024structuralinsightsinto pages 1-2)

## 15. Model organisms and experimental models

The disease-specific experimental models reported are **patient-derived skin fibroblasts** and patient muscle biochemical material. Fibroblasts reproduced reduced complex-I abundance/activity, subcomplex accumulation, and mitochondrial depolarization; re-expression of wild-type NDUFA2 partially rescued these abnormalities. This is the strongest available functional model. (hoefs2008ndufa2complexi pages 4-5, hoefs2008ndufa2complexi pages 3-4)

CRISPR knockout studies in human cells reported in broader complex-I work indicate that NDUFA2 loss destabilizes the N module and can eliminate complex-I activity, but these are generic engineered models rather than knock-ins of the human MC1DN13 variants. Structural reviews conclude that accessory-subunit loss commonly disrupts inter-subunit networks and assembly. (dang2020analysisofhuman pages 1-3, dang2020analysisofhuman pages 28-30)

No dedicated Ndufa2 knockout/knock-in mouse, zebrafish, Drosophila, worm, yeast, patient iPSC, neural organoid, or humanized model recapitulating MC1DN13 was identified. Ndufs4-null mice are extensively used for complex-I Leigh syndrome but model a different gene. A 2024 cryo-EM analysis of Ndufs4-null mouse heart demonstrated loose N-module association and refined the late-assembly framework that includes NDUFA2; it supplies valuable mechanistic analogy, not phenotype validation for MC1DN13. (yin2024structuralinsightsinto pages 1-2)

## Recent developments and expert assessment

The most important 2023–2024 developments are **indirect** rather than disease-specific. First, the 2024 MitoDiag study demonstrated real-world implementation of WES/WGS across a national mitochondrial diagnostic network and emphasized broad genomic testing because clinically suspected mitochondrial disease is genetically heterogeneous and frequently mimicked by other disorders. This strongly supports genome-wide testing for patients with an MC1DN13-like presentation. (rouzier2024primarymitochondrialdisorders pages 1-2)

Second, the 2024 cryo-EM study of Ndufs4-null complex I resolved defective N-module attachment at molecular scale and places the NDUFA2-containing module in the final stage of mammalian complex-I assembly. This sharpens interpretation of the subcomplex accumulation observed in NDUFA2 patient cells, but it does not establish an NDUFA2-specific treatment. (yin2024structuralinsightsinto pages 1-2)

The principal expert conclusion is therefore one of **high-confidence disease–gene causality but low-confidence phenotype frequencies and prognosis**. Complementation, segregation, splicing, enzyme assays, and BN-PAGE make the molecular diagnosis compelling. Conversely, only three published individuals preclude robust epidemiology, genotype–phenotype correlations, penetrance estimates, outcome prediction, or treatment evaluation.

## Key primary sources and quotations

1. **Hoefs et al.**, “NDUFA2 Complex I Mutation Leads to Leigh Disease,” *American Journal of Human Genetics* 82:1306–1315, **June 2008**; PMID **18513682**; DOI/URL: https://doi.org/10.1016/j.ajhg.2008.05.007. Abstract quote: “The mutation in this accessory subunit causes reduced activity and disturbed assembly of complex I,” and the abnormalities were “(partially) rescued with a baculovirus system expressing the NDUFA2 gene.” (hoefs2008ndufa2complexi pages 1-2)
2. **Perrier et al.**, “Recessive Mutations in NDUFA2 Cause Mitochondrial Leukoencephalopathy,” *Clinical Genetics* 93:396–400, **February 2018**; PMID **28857146**; DOI/URL: https://doi.org/10.1111/cge.13126. Abstract quote: “We report two patients with cystic leukoencephalopathy and complex I deficiency with recessive mutations in NDUFA2.” (perrier2018recessivemutationsin pages 1-5)
3. **Yin et al.**, “Structural insights into respiratory complex I deficiency and assembly from the mitochondrial disease-related ndufs4−/− mouse,” *EMBO Journal* 43:225–249, published online **2 January 2024**; DOI/URL: https://doi.org/10.1038/s44318-023-00001-4. This is indirect mechanistic evidence; the authors report “a loose association of the NADH-dehydrogenase module” and propose that NDUFAF2 recruits that module during assembly. (yin2024structuralinsightsinto pages 1-2)
4. **Rouzier et al.**, “Primary mitochondrial disorders and mimics: Insights from a large French cohort,” *Annals of Clinical and Translational Neurology* 11:1478–1491, received 26 February and accepted **23 March 2024**; DOI/URL: https://doi.org/10.1002/acn3.52062. The study evaluated more than 2,000 referrals and concluded that WES/WGS was more valuable than panels for genetically resolving “possible” primary mitochondrial disease. (rouzier2024primarymitochondrialdisorders pages 1-2)

### Knowledge-base caution

All phenotype-frequency fields should be entered as **unknown** or “reported in case(s), n=3 total,” rather than percentages. Variant classifications and population frequencies should be refreshed from current ClinVar/gnomAD records before clinical deployment. ROS injury, particular vulnerable cell populations, dietary benefit, mitochondrial cocktails, and gene therapy remain inferred or experimental—not established MC1DN13 characteristics.

References

1. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 13-NDUFA2): Open Targets Query (mitochondrial complex I deficiency nuclear type 13-NDUFA2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (hoefs2008ndufa2complexi pages 1-2): Saskia J.G. Hoefs, Cindy E.J. Dieteren, Felix Distelmaier, Rolf J.R.J. Janssen, Andrea Epplen, Herman G.P. Swarts, Marleen Forkink, Richard J. Rodenburg, Leo G. Nijtmans, Peter H. Willems, Jan A.M. Smeitink, and Lambert P. van den Heuvel. Ndufa2 complex i mutation leads to leigh disease. American journal of human genetics, 82 6:1306-15, Jun 2008. URL: https://doi.org/10.1016/j.ajhg.2008.05.007, doi:10.1016/j.ajhg.2008.05.007. This article has 175 citations and is from a highest quality peer-reviewed journal.

3. (perrier2018recessivemutationsin pages 1-5): S. Perrier, L. Gauquelin, Martine Tétreault, L. Tran, N. Webb, Myriam Srour, John Mitchell, Catherine Brunel-Guitton, Jacek Majewski, Long, Stephanie Keller, M. Gambello, Cas Simons, A. Vanderver, and Geneviève Bernard. Recessive mutations in ndufa2 cause mitochondrial leukoencephalopathy. Clinical Genetics, 93:396-400, Feb 2018. URL: https://doi.org/10.1111/cge.13126, doi:10.1111/cge.13126. This article has 22 citations and is from a peer-reviewed journal.

4. (perrier2018recessivemutationsin pages 5-8): S. Perrier, L. Gauquelin, Martine Tétreault, L. Tran, N. Webb, Myriam Srour, John Mitchell, Catherine Brunel-Guitton, Jacek Majewski, Long, Stephanie Keller, M. Gambello, Cas Simons, A. Vanderver, and Geneviève Bernard. Recessive mutations in ndufa2 cause mitochondrial leukoencephalopathy. Clinical Genetics, 93:396-400, Feb 2018. URL: https://doi.org/10.1111/cge.13126, doi:10.1111/cge.13126. This article has 22 citations and is from a peer-reviewed journal.

5. (hoefs2008ndufa2complexi pages 4-5): Saskia J.G. Hoefs, Cindy E.J. Dieteren, Felix Distelmaier, Rolf J.R.J. Janssen, Andrea Epplen, Herman G.P. Swarts, Marleen Forkink, Richard J. Rodenburg, Leo G. Nijtmans, Peter H. Willems, Jan A.M. Smeitink, and Lambert P. van den Heuvel. Ndufa2 complex i mutation leads to leigh disease. American journal of human genetics, 82 6:1306-15, Jun 2008. URL: https://doi.org/10.1016/j.ajhg.2008.05.007, doi:10.1016/j.ajhg.2008.05.007. This article has 175 citations and is from a highest quality peer-reviewed journal.

6. (perrier2018recessivemutationsin pages 8-14): S. Perrier, L. Gauquelin, Martine Tétreault, L. Tran, N. Webb, Myriam Srour, John Mitchell, Catherine Brunel-Guitton, Jacek Majewski, Long, Stephanie Keller, M. Gambello, Cas Simons, A. Vanderver, and Geneviève Bernard. Recessive mutations in ndufa2 cause mitochondrial leukoencephalopathy. Clinical Genetics, 93:396-400, Feb 2018. URL: https://doi.org/10.1111/cge.13126, doi:10.1111/cge.13126. This article has 22 citations and is from a peer-reviewed journal.

7. (hoefs2008ndufa2complexi pages 3-4): Saskia J.G. Hoefs, Cindy E.J. Dieteren, Felix Distelmaier, Rolf J.R.J. Janssen, Andrea Epplen, Herman G.P. Swarts, Marleen Forkink, Richard J. Rodenburg, Leo G. Nijtmans, Peter H. Willems, Jan A.M. Smeitink, and Lambert P. van den Heuvel. Ndufa2 complex i mutation leads to leigh disease. American journal of human genetics, 82 6:1306-15, Jun 2008. URL: https://doi.org/10.1016/j.ajhg.2008.05.007, doi:10.1016/j.ajhg.2008.05.007. This article has 175 citations and is from a highest quality peer-reviewed journal.

8. (hoefs2008ndufa2complexi pages 2-3): Saskia J.G. Hoefs, Cindy E.J. Dieteren, Felix Distelmaier, Rolf J.R.J. Janssen, Andrea Epplen, Herman G.P. Swarts, Marleen Forkink, Richard J. Rodenburg, Leo G. Nijtmans, Peter H. Willems, Jan A.M. Smeitink, and Lambert P. van den Heuvel. Ndufa2 complex i mutation leads to leigh disease. American journal of human genetics, 82 6:1306-15, Jun 2008. URL: https://doi.org/10.1016/j.ajhg.2008.05.007, doi:10.1016/j.ajhg.2008.05.007. This article has 175 citations and is from a highest quality peer-reviewed journal.

9. (rouzier2024primarymitochondrialdisorders pages 1-2): Cécile Rouzier, Emmanuelle Pion, Annabelle Chaussenot, Céline Bris, Samira Ait‐El‐Mkadem Saadi, Valérie Desquiret‐Dumas, Naïg Gueguen, Konstantina Fragaki, Patrizia Amati‐Bonneau, Giulia Barcia, Pauline Gaignard, Julie Steffann, Alessandra Pennisi, Jean‐Paul Bonnefont, Elise Lebigot, Sylvie Bannwarth, Bruno Francou, Benoit Rucheton, Damien Sternberg, Marie‐Laure Martin‐Negrier, Aurélien Trimouille, Gaëlle Hardy, Stéphane Allouche, Cécile Acquaviva‐Bourdain, Cécile Pagan, Anne‐Sophie Lebre, Pascal Reynier, Mireille Cossee, Shahram Attarian, Véronique Paquis‐Flucklinger, and Vincent Procaccio. Primary mitochondrial disorders and mimics: insights from a large french cohort. Annals of Clinical and Translational Neurology, 11:1478-1491, May 2024. URL: https://doi.org/10.1002/acn3.52062, doi:10.1002/acn3.52062. This article has 16 citations and is from a peer-reviewed journal.

10. (hoefs2008ndufa2complexi pages 6-8): Saskia J.G. Hoefs, Cindy E.J. Dieteren, Felix Distelmaier, Rolf J.R.J. Janssen, Andrea Epplen, Herman G.P. Swarts, Marleen Forkink, Richard J. Rodenburg, Leo G. Nijtmans, Peter H. Willems, Jan A.M. Smeitink, and Lambert P. van den Heuvel. Ndufa2 complex i mutation leads to leigh disease. American journal of human genetics, 82 6:1306-15, Jun 2008. URL: https://doi.org/10.1016/j.ajhg.2008.05.007, doi:10.1016/j.ajhg.2008.05.007. This article has 175 citations and is from a highest quality peer-reviewed journal.

11. (dang2020analysisofhuman pages 1-3): Quynh-Chi L. Dang, Duong H. Phan, Abigail N. Johnson, Mukund Pasapuleti, Hind A. Alkhaldi, Fang Zhang, and Steven B. Vik. Analysis of human mutations in the supernumerary subunits of complex i. Life, 10:296, Nov 2020. URL: https://doi.org/10.3390/life10110296, doi:10.3390/life10110296. This article has 26 citations.

12. (yin2024structuralinsightsinto pages 1-2): Zhan Yin, Ahmed-Noor A Agip, Hannah R Bridges, and Judy Hirst. Structural insights into respiratory complex i deficiency and assembly from the mitochondrial disease-related ndufs4−/− mouse. Jan 2024. URL: https://doi.org/10.1038/s44318-023-00001-4, doi:10.1038/s44318-023-00001-4. This article has 39 citations.

13. (dang2020analysisofhuman pages 28-30): Quynh-Chi L. Dang, Duong H. Phan, Abigail N. Johnson, Mukund Pasapuleti, Hind A. Alkhaldi, Fang Zhang, and Steven B. Vik. Analysis of human mutations in the supernumerary subunits of complex i. Life, 10:296, Nov 2020. URL: https://doi.org/10.3390/life10110296, doi:10.3390/life10110296. This article has 26 citations.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_13-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
| Terms checked | 46 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032618` (4 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 13**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (2 mentions) - replaced by `GO:0045271`