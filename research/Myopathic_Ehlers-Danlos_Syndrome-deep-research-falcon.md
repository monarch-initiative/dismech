---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T17:46:14.687929'
end_time: '2026-09-16T18:01:27.816552'
duration_seconds: 913.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Myopathic Ehlers-Danlos Syndrome
  mondo_id: MONDO:0034022
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 40
  not_found: 1
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.023
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0034022
    reported_labels:
    - if available
    ontology_label: Bethlem myopathy 2
  unresolved_terms:
  - HP:0002802
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myopathic_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopathic Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0034022 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myopathic Ehlers-Danlos Syndrome** covering all of the
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
- **Disease Name:** Myopathic Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0034022 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myopathic Ehlers-Danlos Syndrome** covering all of the
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


# Myopathic Ehlers–Danlos Syndrome (mEDS): Disease-Characteristics Report

**Target:** Myopathic Ehlers–Danlos syndrome / COL12A1-related myopathy  
**Category:** Mendelian extracellular-matrix disorder  
**Knowledge cut-off emphasized:** 2024, with a clearly labeled 2025 cohort included because it materially changes the recessive natural-history evidence.

## Executive summary

Myopathic Ehlers–Danlos syndrome is an exceptionally rare, usually congenital disorder caused by germline pathogenic variants in **COL12A1**, combining congenital myopathy with connective-tissue manifestations. The characteristic pattern is congenital hypotonia and muscle weakness, delayed motor development, distal joint hypermobility, proximal or large-joint contractures, spinal deformity, and variably soft skin, atrophic scars, or impaired wound healing. Dominant-negative glycine substitutions and in-frame exon-skipping alleles usually cause milder, ambulant disease, sometimes evolving into adult distal myopathy. Biallelic loss-of-function generally causes a more severe congenital phenotype, although independent ambulation and improvement over time are possible. The primary lesion is defective collagen XII organization around collagen-I fibrils, disrupting extracellular-matrix architecture, mechanics, cell–cell organization, and force transmission rather than the muscle contractile apparatus itself. (delbaere2020noveldefectsin pages 2-3, zou2014recessiveanddominant pages 1-2, mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 7-9)

The 2023 authoritative review states: **“Mutations in the collagen XII gene cause myopathic Ehlers-Danlos syndrome (mEDS), an early-onset disease characterized by overlapping connective tissue abnormalities and muscle weakness.”** It further describes delayed motor development, weakness, laxity, hypermobility, contractures, and abnormal wound healing. (izu2023collagenxiimediated pages 1-2)

---

## 1. Disease information

### Definition and nomenclature

mEDS is one of the monogenic EDS types recognized in the 2017 international classification. It is also described as **COL12A1-related myopathy**, **COL12A1-related myopathic EDS**, **EDS/myopathy overlap syndrome**, **collagen XII–related disease**, **Bethlem myopathy 2/Bethlem-like myopathy**, and, for severe recessive presentations, **Ullrich congenital muscular dystrophy 2/UCMD2-like disease**. The terminology reflects a continuous collagen-XII disease spectrum rather than proven discrete biological entities. (delbaere2020noveldefectsin pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9, merlini2025myopathicehlersdanlossyndrome pages 1-2)

### Identifiers

- **MONDO:0034022**: Open Targets currently labels this entity **Bethlem myopathy 2** and associates it with **COL12A1/ENSG00000111799**. Thus, the supplied MONDO identifier is available, but its preferred label is not exactly “myopathic EDS.” (OpenTargets Search: myopathic Ehlers-Danlos syndrome-COL12A1)
- **OMIM:** COL12A1-related dominant and recessive phenotypes are commonly indexed under Bethlem myopathy 2 and Ullrich congenital muscular dystrophy 2, respectively; a single unambiguous mEDS-only OMIM identifier was not established in the retrieved evidence.
- **Orphanet:** mEDS is recognized as an ultra-rare EDS subtype, but a disease-specific ORPHA number was not verified from the retrieved primary evidence.
- **ICD-10/ICD-11 and MeSH:** no validated mEDS-specific code or descriptor was identified. Implementations generally require an umbrella EDS/heritable connective-tissue-disorder code plus molecular annotation.
- **Gene:** **COL12A1**, collagen type XII alpha-1 chain; Ensembl **ENSG00000111799**. (OpenTargets Search: myopathic Ehlers-Danlos syndrome-COL12A1)

This report represents **aggregated disease-level evidence** from published patients, families, fibroblast assays, and animal models—not individual EHR-derived data.

---

## 2. Etiology

### Causal factor

The cause is a **germline pathogenic COL12A1 variant**. Collagen XII is a homotrimeric fibril-associated collagen with interrupted triple helices (FACIT) that organizes collagen-I-rich extracellular matrices. Both autosomal-dominant and autosomal-recessive disease occur. (izu2023collagenxiimediated pages 1-2, chiquet2014collagenxiiprotecting pages 1-3, delbaere2020noveldefectsin pages 1-2)

### Genetic risk

- **Dominant disease:** usually heterozygous glycine substitutions in the triple-helical region or in-frame exon-skipping alleles. These interfere with secretion or assembly of homotrimeric collagen XII and act predominantly through **dominant-negative** effects. (punetha2017novelcol12a1variant pages 3-4, mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 2-3)
- **Recessive disease:** biallelic loss-of-function or severely hypomorphic alleles cause marked reduction or absence of collagen XII. (mccarty2025clinicalcharacterizationof pages 1-2)
- The first discovery study included two severely affected siblings with homozygous loss of function and one milder patient with a de novo dominant missense variant. (zou2014recessiveanddominant pages 1-2)

Variants supported in retrieved primary reports include **c.8329G>C (p.Gly2777Arg)**, absent from ExAC and NHLBI ESP in the 2017 report; heterozygous exon-skipping defects designated **Δ52, Δ53, Δ54, and Δ56**; and biallelic **p.Ile1393Phefs*11/p.Ala1110Asp** in one family. A 2024 report identified homozygous **c.8903C>T (p.Pro2968Leu)** but treated its disease classification cautiously because functional and segregation evidence remained limited. (delbaere2020noveldefectsin pages 1-2, punetha2017novelcol12a1variant pages 3-4, ipek2024col12a1genevariant pages 5-6, mccarty2025clinicalcharacterizationof pages 1-2)

All established mEDS alleles are **germline**. Somatic COL12A1 variants reported in cancers do not establish mEDS.

### Non-genetic, protective, and gene–environment factors

No environmental toxin, infection, lifestyle exposure, susceptibility locus, protective allele, modifier gene, or validated gene–environment interaction has been demonstrated to cause or prevent mEDS. Mechanical loading regulates normal collagen-XII expression—tensile/cyclic strain induces it in fibroblastic cells—but this is mechanobiology, not evidence that exercise or occupation causes Mendelian disease. (izu2023collagenxiimediated pages 1-2, chiquet2014collagenxiiprotecting pages 3-4)

Family history increases prior probability in inherited cases but may be absent with de novo dominant variants. Consanguinity can increase the probability of recessive disease; no quantified attributable risk or established founder allele was found.

---

## 3. Phenotypes

The core genotype–phenotype distinction is summarized below.

| Domain | Autosomal-dominant COL12A1 disease | Autosomal-recessive/biallelic COL12A1 disease | Ontology suggestions |
|---|---|---|---|
| Onset | Usually congenital or childhood hypotonia/motor delay; adolescent presentation and symptomatic distal weakness beginning in the fourth decade also occur. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 2-3) | Congenital onset; reduced fetal movement, hypotonia, hip dysplasia, and delayed milestones occurred in all eight individuals in the 2025 cohort; arthrogryposis occurred in 4/8. (mccarty2025clinicalcharacterizationof pages 2-3) | HP:0002808 Abnormal fetal movements; HP:0001252 Hypotonia; HP:0001263 Global developmental delay; HP:0002751 Kyphosis |
| Severity and course | Generally mild, with retained ambulation and slowly progressive weakness; childhood function may be relatively preserved before adult distal weakness. Rare severe neonatal respiratory presentations occur. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9) | Variable but usually more severe: 5/8 had profound congenital weakness, minimal milestones, respiratory insufficiency, and feeding difficulty; 3/8 had mild-to-moderate weakness and walked independently. Motor ability often improved slowly without regression. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3) | HP:0003701 Proximal muscle weakness; HP:0002460 Distal muscle weakness; HP:0002376 Developmental regression—typically absent |
| Motor function and weakness | Axial, proximal, or distal weakness; adult disease may selectively involve anterior lower-leg muscles, finger extensors, and intrinsic hand muscles. In a later review, 31/33 reported dominant cases remained ambulant. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9) | Proximal and distal lower-limb weakness ranging from isolated hip-flexor weakness to profound generalized weakness. Five of 15 literature cases never walked; some ambulant children walked at 15 months, 16 months, or 3 years. (mccarty2025clinicalcharacterizationof pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9) | HP:0003324 Generalized muscle weakness; HP:0008948 Pelvic-girdle muscle weakness; HP:0009055 Distal lower-limb muscle weakness; HP:0002355 Difficulty walking |
| Joints and spine | Joint hyperlaxity in 5/6 patients in a 2019 series; pes planus common, with occasional ankle contractures. Distal hypermobility may coexist with proximal contractures; kyphoscoliosis can progress. (punetha2017novelcol12a1variant pages 3-4, mohassel2019dominantcollagenxii pages 2-3) | Distal laxity in all eight recent patients; contractures in 6/8, often involving finger flexors and knees. Progressive scoliosis requiring surgery occurred in 3/8 and thoracic kyphoscoliosis in 2/8. (mccarty2025clinicalcharacterizationof pages 2-3) | HP:0001382 Joint hypermobility; HP:0001371 Flexion contracture; HP:0001763 Pes planus; HP:0002650 Scoliosis; HP:0002751 Kyphosis; HP:0002802 Arthrogryposis multiplex congenita |
| Skin, wound healing, and craniofacial findings | Soft/doughy skin, atrophic scarring, abnormal wound healing, and high-arched palate have been reported; reliable frequencies are unavailable. (delbaere2020noveldefectsin pages 2-3, punetha2017novelcol12a1variant pages 3-4, izu2023collagenxiimediated pages 1-2) | Dysmorphic features were universal in the recent cohort; gingival hypertrophy occurred in 6/8, with micrognathia and dental abnormalities also reported. Velvety palms/soles occurred, whereas keloid scarring was absent; skin-feature frequencies otherwise unavailable. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3) | HP:0000974 Hyperextensible skin; HP:0001075 Atrophic scars; HP:0000278 Retrognathia; HP:0000212 Gingival overgrowth; HP:0000164 Abnormality of the dentition; HP:0000218 High-arched palate |
| Respiratory, feeding, and cardiac involvement | No cardiac or pulmonary disease was detected in the six-patient 2019 series; reported FVC values in later compiled cases ranged approximately 58–115% predicted. Rare severe dominant neonatal respiratory failure is reported. Feeding frequencies unavailable. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9, merlini2025myopathicehlersdanlossyndrome pages 2-3) | Seven of eight required nasogastric or gastrostomy feeding. Respiratory involvement ranged from absent to ventilator dependence from birth; cardiac findings occurred in 4/8. Exact lesion-specific frequencies are unavailable. (mccarty2025clinicalcharacterizationof pages 2-3) | HP:0002093 Respiratory insufficiency; HP:0002020 Gastroesophageal reflux; HP:0008872 Feeding difficulties in infancy; HP:0011968 Feeding by nasogastric tube; HP:0011471 Gastrostomy tube feeding; HP:0001627 Abnormal heart morphology |
| Laboratory and electrophysiology | CK is usually normal or mildly elevated, although compiled values ranged from about 42–1,310 U/L. One congenital case had normal CK, EMG, and nerve-conduction studies. (punetha2017novelcol12a1variant pages 3-4, merlini2025myopathicehlersdanlossyndrome pages 2-3) | CK was normal in four and mildly elevated in two reported patients. EMG/nerve-conduction evidence was unavailable in the extracted cohort. (mccarty2025clinicalcharacterizationof pages 2-3) | HP:0003236 Elevated serum creatine kinase; HP:0003458 EMG abnormality—variable/not established |
| Biopsy and imaging | Muscle biopsy may show mild, nonspecific, non-dystrophic myopathy with fiber-size variation and increased connective tissue. Imaging can demonstrate rectus-femoris, posterior-thigh, neck, and lumbar muscle involvement. (punetha2017novelcol12a1variant pages 3-4, merlini2025myopathicehlersdanlossyndrome pages 7-9, merlini2025myopathicehlersdanlossyndrome pages 1-2) | Four biopsies showed mild myopathic changes without dystrophic necrosis/regeneration. MRI ranged from normal to severe diffuse atrophy and fatty replacement; posterior-thigh and rectus-femoris involvement may be selective. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 3-4) | HP:0003199 Decreased muscle mass; HP:0003712 Abnormal muscle fiber morphology; HP:0003808 Abnormal muscle biopsy finding; UBERON:0001383 skeletal muscle tissue |
| Molecular mechanism | Glycine substitutions and in-frame exon-skipping variants affecting the triple-helical region typically exert dominant-negative effects, causing intracellular retention, impaired secretion, or abnormal fibril-associated collagen-XII deposition. Mutant-allele siRNA restored ECM localization in exon-52-deletion fibroblasts. (punetha2017novelcol12a1variant pages 3-4, mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 2-3) | Usually biallelic loss of function, producing markedly reduced or absent collagen XII. Fibroblast collagen-XII abundance correlated with clinical severity in the eight-patient cohort. (mccarty2025clinicalcharacterizationof pages 1-2) | GO:0030198 extracellular matrix organization; GO:0030199 collagen fibril organization; GO:0005201 extracellular matrix structural constituent; GO:0062023 collagen-containing extracellular matrix; CL:0000057 fibroblast |
| Prognosis and function | Most patients retain ambulation; weakness may remain mild for years but can progress in adulthood. No genotype-specific survival, mortality, or validated quality-of-life statistics are available. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9) | Lifelong congenital disease with severity ranging from ventilator-dependent profound disability to independent walking. Improvement without motor regression is documented, but survival rates, life expectancy, and validated quality-of-life outcomes are unavailable. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3) | HP:0002355 Difficulty walking; HP:0003547 Shoulder-girdle muscle weakness; ICF mobility and self-care domains |


*Table: Evidence-based comparison of autosomal-dominant and biallelic COL12A1-related myopathic Ehlers-Danlos syndrome across clinical, diagnostic, molecular, and prognostic domains. Frequencies are reported only where available, and evidence gaps are explicitly marked.*

### Principal phenotype annotations

- Congenital hypotonia — **HP:0001252**; usually neonatal/congenital, variable severity.
- Generalized, proximal, axial, or distal weakness — **HP:0003324**, **HP:0003701**, **HP:0002460**; mild and slowly progressive in many dominant cases, profound congenitally in severe recessive disease.
- Delayed motor milestones — **HP:0001270/HP:0001263**; walking may be delayed to early childhood, never achieved in severe cases, or retained into adulthood.
- Distal/generalized joint hypermobility — **HP:0001382**; a major recurring feature and present in 5/6 patients in one dominant series and all eight patients in the recent biallelic cohort. (mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 2-3)
- Proximal or large-joint/finger/knee contractures — **HP:0001371**; present in 6/8 of the recent biallelic cohort. (mccarty2025clinicalcharacterizationof pages 2-3)
- Arthrogryposis — **HP:0002802**; 4/8 in that cohort. (mccarty2025clinicalcharacterizationof pages 2-3)
- Scoliosis/kyphoscoliosis — **HP:0002650**, **HP:0002751**; may progress and require surgery.
- Pes planus — **HP:0001763**; common in dominant distal-myopathy presentations. (mohassel2019dominantcollagenxii pages 2-3)
- Soft/doughy or hyperextensible skin and atrophic scarring — **HP:0000974**, **HP:0001075**; frequencies remain poorly quantified. (delbaere2020noveldefectsin pages 2-3)
- Gingival hypertrophy and dental abnormalities — **HP:0000212**, **HP:0000164**; gingival hypertrophy occurred in 6/8 biallelic patients. (mccarty2025clinicalcharacterizationof pages 2-3)
- Feeding difficulty/enteral feeding — **HP:0011968**, **HP:0011471**; 7/8 biallelic patients required nasogastric or gastrostomy feeding. (mccarty2025clinicalcharacterizationof pages 2-3)
- Respiratory insufficiency — **HP:0002093**; ranges from absent to neonatal ventilator dependence in biallelic disease; uncommon in typical dominant disease.
- Patellar instability — suggested **HP:0002999** or a more specific HPO patellar-dislocation term; human imaging and Col12a1-null mice support inclusion. (zhu2021ablationofthe pages 16-20)

### Quality of life

No disease-specific EQ-5D, SF-36, PROMIS, or validated patient-reported-outcome study was found. Functional burden plausibly arises from delayed walking, falls, weakness, spinal deformity, feeding or ventilatory dependence, surgery, and mobility-aid requirements, but quantitative quality-of-life effects remain unknown.

---

## 4. Genetic and molecular information

### Gene and protein

**COL12A1** encodes three identical α1(XII) chains that assemble as collagen-XII homotrimers. Each chain contains two short collagenous domains and non-collagenous domains, including a large NC3 region with fibronectin type-III repeats, von Willebrand factor-A modules, and a thrombospondin N-terminal module. Alternative splicing produces large XIIA and smaller XIIB isoforms; mixed XIIA/XIIB trimers can form. The short isoform predominates in many mature tissues, while long collagen XII remains prominent in bone, tendon, and dermis. (chiquet2014collagenxiiprotecting pages 1-3, delbaere2020noveldefectsin pages 1-2, izu2023collagenxiimediated pages 1-2)

### Variant classes and consequences

- **Missense glycine substitutions:** disturb the Gly-X-Y triple-helical motif; p.Gly2777Arg caused intracellular retention and reduced deposited matrix, supporting dominant-negative interference. (punetha2017novelcol12a1variant pages 3-4)
- **Canonical splice/in-frame exon-skipping variants:** preserve the reading frame but alter critical extracellular domains; Δ52/53/54/56 alleles caused variant-specific intracellular accumulation, abnormal long-isoform processing, near-absence of short collagen XII, and altered decorin/tenascin-X. (delbaere2020noveldefectsin pages 1-2)
- **Frameshift/nonsense/canonical loss-of-function variants:** generally biallelic and cause absent or markedly reduced collagen XII, with protein abundance broadly tracking severity. (mccarty2025clinicalcharacterizationof pages 1-2)
- **VUS:** p.Arg1863Cys and p.Pro2968Leu illustrate the need not to diagnose mEDS from rarity or computational prediction alone. Functional evidence, segregation, phenotype concordance, and ACMG/AMP assessment are necessary. (delbaere2020noveldefectsin pages 1-2, ipek2024col12a1genevariant pages 5-6)

Exact gnomAD frequencies were not available for every allele. Disease-causing alleles are expected to be absent or extremely rare; the p.Gly2777Arg report documented absence from the then-current ExAC/ESP databases. (punetha2017novelcol12a1variant pages 3-4)

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene, disease-specific methylation signature, histone alteration, recurrent CNV, translocation, inversion, aneuploidy, or germline-mosaicism rate is established. Parental mosaicism should nevertheless be considered when counseling apparently de novo cases.

---

## 5. Environmental information

mEDS is not infectious, toxic, nutritional, occupational, or lifestyle-induced. No pathogen or environmental exposure is implicated. Sensible activity modification may reduce secondary joint injury, fatigue, or falls but does not alter the initiating genotype. Smoking, alcohol, diet, pollutants, and radiation have not been shown to modify penetrance.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A pathogenic germline COL12A1 allele leads to** production of a structurally abnormal collagen-XII chain or reduced/absent protein.
2. **Dominant glycine/exon-skipping alleles lead to** intracellular retention, defective secretion, and incorporation of abnormal chains into homotrimers; **biallelic loss-of-function leads to** quantitative collagen-XII deficiency. (delbaere2020noveldefectsin pages 1-2, punetha2017novelcol12a1variant pages 3-4, mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 1-2)
3. **Defective collagen XII leads to** impaired association with collagen-I fibrils and disturbed interactions with decorin, tenascin-X, fibromodulin, COMP, and potentially collagen VI. (izu2021collagenxiimediated pages 15-19, chiquet2014collagenxiiprotecting pages 9-11, chiquet2014collagenxiiprotecting pages 3-4)
4. **Disrupted molecular bridging leads to** abnormal collagen-fibril spacing, assembly, bundling, and pericellular matrix organization. (izu2021collagenxiimediated pages 15-19, izu2023collagenxiimediated pages 1-2, chiquet2014collagenxiiprotecting pages 9-11)
5. **Abnormal ECM architecture leads to** altered tissue stiffness, elasticity, passive-force transmission, mechanotransduction, and cell shape/cell–cell communication. The force-transmission interpretation is strongly supported by mouse physiology but remains partly inferred for human muscle. (izu2021collagenxiimediated pages 15-19, izu2023collagenxiimediated pages 1-2, zou2014recessiveanddominant pages 1-2)
6. **In muscle, these defects lead to** reduced passive force and grip strength, delayed fiber-type maturation, weakness, hypotonia, and delayed motor development. (zou2014recessiveanddominant pages 1-2)
7. **In tendons, ligaments, joints, bone, skin, and periodontium, the defects lead to** laxity and dislocation, contractures from abnormal muscle–tendon development, scoliosis/kyphosis, bone fragility, skin/scar abnormalities, and gingival/dental manifestations. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3, izu2021collagenxiimediated pages 15-19, zhu2021ablationofthe pages 16-20)
8. **Severe congenital weakness and bulbar/respiratory involvement lead to** delayed or absent milestones, feeding-tube dependence, respiratory insufficiency, and major disability in the most severe recessive cases. (mccarty2025clinicalcharacterizationof pages 2-3)

### Pathways and processes

The central pathway is **extracellular-matrix organization**, not a canonical oncogenic signaling cascade. Relevant GO annotations include:

- **GO:0030198** extracellular matrix organization
- **GO:0030199** collagen fibril organization
- **GO:0062023** collagen-containing extracellular matrix
- **GO:0005201** extracellular matrix structural constituent
- collagen trimer and extracellular/pericellular matrix cellular-component terms
- connective-tissue development, tendon development, skeletal-system development, cell–matrix adhesion, cell–cell communication, mechanotransduction, and muscle force transmission.

TGF-β1 and mechanical strain induce collagen-XII expression in normal fibroblastic cells, but a disease-driving TGF-β, MAPK, PI3K–AKT, mTOR, Wnt, immune, apoptotic, autophagic, oxidative-stress, or metabolic pathway has not been demonstrated in mEDS. (izu2023collagenxiimediated pages 1-2, chiquet2014collagenxiiprotecting pages 3-4)

### Cells and tissues

Candidate Cell Ontology concepts are **fibroblast (CL:0000057)**, tenocyte, osteoblast, osteocyte, skeletal-muscle fiber/myocyte, chondrocyte, and mesenchymal stromal cell. In mice, single-cell analysis identified Col12a1-positive populations including **Tnmd+ tenocytes, Myod1+ myoblasts, and Col2a1+ chondrocytes**, with altered matrisome expression in the tenocyte population. This is model-organism evidence, not a human single-cell atlas. (zhu2021ablationofthe pages 16-20)

### Molecular profiling

Patient-fibroblast immunocytochemistry, RT-PCR, qPCR, and extracellular-matrix staining show variant-specific collagen-XII defects. No validated human blood biomarker, metabolomic/lipidomic signature, epigenomic signature, spatial transcriptomic study, organoid model, or disease-specific CRISPR screen was found. Allele-specific siRNA rescued extracellular collagen-XII localization in exon-52-deletion fibroblasts, constituting proof of mechanism rather than a clinical therapy. (mohassel2019dominantcollagenxii pages 2-3)

---

## 7. Anatomical structures affected

Primary structures are the musculoskeletal and connective-tissue systems:

- **Skeletal muscle**—axial, proximal, and distal muscles; rectus femoris and posterior thigh can show selective imaging abnormalities.
- **Tendon and ligament**—including patellar/quadriceps tendon and cruciate ligaments.
- **Joints**—distal joints, hips, knees, ankles, fingers, and patellofemoral articulation.
- **Spine and bone**—scoliosis, kyphosis, malformed patellar groove, and model-supported bone fragility.
- **Skin and scar tissue**, **gingiva/periodontium**, and dentition.
- Secondary involvement may include respiratory muscles, swallowing/feeding function, and variably the heart. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3, mccarty2025clinicalcharacterizationof pages 3-4, zhu2021ablationofthe pages 16-20)

Suggested UBERON mappings include skeletal muscle tissue (**UBERON:0001383**), tendon, ligament, dermis, periosteum, periodontium, femur, tibia, patella, knee joint, vertebral column, gingiva, and respiratory muscle. The defect is usually bilateral/generalized; asymmetry may occur on imaging but is not a defining lateralized phenotype.

At the subcellular level, relevant compartments are the **endoplasmic-reticulum/secretory pathway** for retained dominant-mutant protein and the extracellular/collagen-containing matrix for defective deposition. (punetha2017novelcol12a1variant pages 3-4)

---

## 8. Temporal development

Onset is usually prenatal, neonatal, or early childhood: reduced fetal movement, congenital hypotonia, hip dysplasia, arthrogryposis, and motor delay may be the first manifestations. Dominant disease can remain mild through youth and present as slowly progressive distal weakness in the fourth decade; adolescent onset also occurs. (mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 2-3)

The course is chronic and lifelong but not uniformly degenerative. Severe recessive disease produces early disability, respiratory or feeding dependence, and spinal progression. Nonetheless, motor function in the recent recessive cohort often improved slowly without regression. Dominant distal myopathy may progress gradually in adulthood. There are no validated clinical stages, remission pattern, or critical pharmacologic treatment window. Early recognition is important for preventing orthopedic deformity, nutritional compromise, and respiratory complications. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3)

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant and autosomal recessive.
- **Recurrence:** approximately 50% per pregnancy for a heterozygous affected parent, subject to penetrance and variant interpretation; 25% affected, 50% carrier, and 25% unaffected per pregnancy when both parents carry the same recessive disease allele.
- **Penetrance:** not quantified; dominant expressivity is clearly variable.
- **Anticipation:** not reported.
- **Founder effects/carrier frequency:** none established.
- **Sex ratio:** no reproducible sex bias.
- **Ethnic/geographic enrichment:** none established.

The late-2024 clinical review estimated prevalence at **<1 per 1,000,000** and reported **25 individuals from 16 families**, including two recessive families. A 2023 review similarly counted 16 families. These are literature counts, not population-based prevalence studies. (dijk2024clinicaldiagnosisof pages 3-4, izu2023collagenxiimediated pages 1-2)

A later 2025 review—outside the requested priority window but informative—compiled approximately **30 dominant patients in 18 families and 15 recessive patients in 13 families**, illustrating rapid ascertainment growth and continuing underdiagnosis. (merlini2025myopathicehlersdanlossyndrome pages 1-2)

---

## 10. Diagnostics

### Clinical recognition

Suspect mEDS when congenital or childhood hypotonia/weakness and motor delay coexist with **distal joint hypermobility plus proximal contractures**, scoliosis/kyphosis, pes planus, soft skin or abnormal scars, gingival hypertrophy, or a Bethlem/UCMD-like phenotype without a COL6 diagnosis. Minimal clinical criteria in the 2017 EDS framework require congenital muscle hypotonia and/or muscle atrophy that improves with age, plus proximal contractures and/or distal joint hypermobility; molecular confirmation is essential because of overlap. The 2020 cohort used major/minor criteria and included soft doughy skin, atrophic scarring, motor delay, and biopsy-proven myopathy among supporting features. (delbaere2020noveldefectsin pages 2-3)

### Testing strategy

1. Detailed prenatal, developmental, neuromuscular, joint, skin, scar, dental/gingival, respiratory, feeding, cardiac, and three-generation family history.
2. Physical examination including Beighton score, muscle strength, contractures, spine, patellar stability, skin/scars, palate, and gingiva.
3. Serum CK—often normal or mildly elevated; a normal result does not exclude disease. (mccarty2025clinicalcharacterizationof pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 2-3)
4. Pulmonary function testing when developmentally possible; sleep study or blood-gas assessment if respiratory weakness is suspected.
5. Echocardiography/ECG at baseline where clinically appropriate because cardiac findings occurred in some recessive patients, although dominant-series evidence does not establish routine progressive cardiomyopathy. (mohassel2019dominantcollagenxii pages 2-3, mccarty2025clinicalcharacterizationof pages 2-3)
6. Muscle MRI can show rectus-femoris, posterior-thigh, neck, lumbar, or diffuse muscle involvement; normal imaging does not exclude mEDS. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 3-4, merlini2025myopathicehlersdanlossyndrome pages 1-2)
7. EMG/NCS may be normal. Biopsy, if performed, usually shows mild non-dystrophic myopathy, fiber-size variation, and interstitial connective tissue without prominent necrosis/regeneration. It is supportive rather than diagnostic. (punetha2017novelcol12a1variant pages 3-4, merlini2025myopathicehlersdanlossyndrome pages 7-9)
8. **Molecular confirmation:** a comprehensive congenital-myopathy/muscular-dystrophy or heritable-connective-tissue panel including **COL12A1, COL6A1, COL6A2, COL6A3, FKBP14, PLOD1, COL5A1/2, TNXB**, and other phenotype-relevant genes. Monogenic EDS reviews regard massively parallel gene-panel testing as current gold standard. (dijk2024clinicaldiagnosisof pages 3-4, mccarty2025clinicalcharacterizationof pages 7-9)
9. If panel testing is negative, use exome or genome sequencing with exon-level CNV and splice analysis. RNA sequencing from fibroblasts may clarify suspected splice variants. Single-gene sequencing is reasonable when the phenotype and familial allele are known.

CMA, karyotype, FISH, mitochondrial-DNA analysis, and repeat-expansion tests are not first-line unless independent clinical findings suggest those mechanisms.

### Variant interpretation

Classification should follow ACMG/AMP principles and incorporate rarity, segregation/de novo status, phenotype specificity, predicted effect, RNA evidence, and collagen-XII immunostaining or secretion assays where available. A COL12A1 VUS alone is not diagnostic. (delbaere2020noveldefectsin pages 1-2, ipek2024col12a1genevariant pages 5-6)

### Differential diagnosis

Principal differentials are collagen-VI-related Ullrich congenital muscular dystrophy and Bethlem myopathy, FKBP14- and PLOD1-related kyphoscoliotic EDS, classical EDS, TNXB-related classical-like EDS, other congenital myopathies/dystrophies, and congenital contractural disorders. Distal hypermobility plus proximal contractures and mild non-dystrophic biopsy can resemble collagen-VI disease; molecular testing is decisive. (mccarty2025clinicalcharacterizationof pages 7-9, merlini2025myopathicehlersdanlossyndrome pages 1-2)

There is no newborn biochemical screen. Cascade molecular testing is appropriate after identifying a familial pathogenic variant.

---

## 11. Outcome and prognosis

No population-based survival, 5- or 10-year survival, life-expectancy, or mortality estimate exists. Typical dominant disease is compatible with prolonged ambulation and often no recognized cardiac or pulmonary disease, although slowly progressive adult weakness occurs. In one literature synthesis, **31/33 dominant cases were ambulant**. (mohassel2019dominantcollagenxii pages 2-3, merlini2025myopathicehlersdanlossyndrome pages 7-9)

Recessive disease spans profound neonatal weakness with ventilator/feeding dependence to mild weakness with independent walking. In the recent eight-person biallelic cohort, **5/8 were severe and 3/8 mild-to-moderate**; motor improvement without regression was documented. Progressive scoliosis, contractures, joint instability, respiratory failure, feeding impairment, and reduced mobility are major morbidity drivers. (mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3)

No prognostic circulating biomarker is validated. Broadly, biallelic null alleles and absent fibroblast collagen XII correlate with greater severity, whereas residual expression is associated with milder disease; variant-level prediction remains imperfect. (mccarty2025clinicalcharacterizationof pages 1-2)

---

## 12. Treatment

### Current standard of care

There is **no approved disease-modifying pharmacotherapy** and no evidence-based mEDS-specific treatment algorithm. Management is individualized and multidisciplinary, usually involving clinical genetics, neurology/neuromuscular medicine, rehabilitation, orthopedics, pulmonology, cardiology where indicated, gastroenterology/nutrition, dentistry, pain services, and wound/surgical teams. Evidence is predominantly expert extrapolation from EDS and congenital myopathy rather than controlled mEDS trials. (fajardojimenez2022ehlersdanlosaliterature pages 3-4, islam2021ehlersdanlossyndromeimmunologic pages 23-28, malfait2020theehlers–danlossyndromes pages 15-16)

- **Physical/occupational therapy:** low-impact strengthening, motor training, balance/fall prevention, preservation of range while avoiding aggressive stretching of unstable joints, pacing, and adaptive equipment. Suggested NCIT concepts: *Physical Therapy*, *Occupational Therapy*, *Exercise Therapy*.
- **Orthoses and mobility aids:** braces for unstable joints, ankle-foot orthoses where helpful, and wheelchair/scooter support for severe weakness or pain. Suggested NCIT: *Orthotic Device*, *Assistive Device*. (islam2021ehlersdanlossyndromeimmunologic pages 23-28)
- **Orthopedic care:** monitor hip dysplasia, contractures, patellar instability, scoliosis, and kyphosis. Surgery is considered for progressive deformity or failed conservative care; one reported patient’s scoliosis improved after surgery. Tissue fragility and wound healing must be considered. (punetha2017novelcol12a1variant pages 3-4, islam2021ehlersdanlossyndromeimmunologic pages 23-28)
- **Respiratory care:** serial clinical/FVC assessment, cough support, sleep evaluation, and noninvasive or invasive ventilation when required.
- **Nutrition/feeding:** swallowing assessment, nutritional support, and nasogastric/gastrostomy feeding when oral intake is unsafe or insufficient; this is common in severe recessive disease. (mccarty2025clinicalcharacterizationof pages 2-3)
- **Pain:** individualized non-pharmacological and pharmacological management; no mEDS-specific analgesic or pharmacogenomic recommendation exists.
- **Skin/wounds:** minimize trauma and tension; general EDS guidance recommends deep sutures and longer retention where dehiscence is a concern. (islam2021ehlersdanlossyndromeimmunologic pages 23-28)
- **Dental/periodontal care:** surveillance is rational given gingival hypertrophy and dental abnormalities.
- **Anesthesia:** no COL12A1-specific protocol was found; preoperative respiratory, airway, cervical/spinal, joint-positioning, and tissue-fragility assessment is prudent.

### Experimental therapy and trials

No relevant registered interventional clinical trial was returned by the ClinicalTrials.gov search, and no approved gene, cell, CRISPR, antisense, siRNA, mRNA, or protein-replacement therapy exists. Allele-specific siRNA restored extracellular collagen-XII distribution in patient fibroblasts carrying an exon-52 deletion, demonstrating targetability but not clinical efficacy or safety. (mohassel2019dominantcollagenxii pages 2-3)

---

## 13. Prevention

Primary prevention through lifestyle or vaccination is not applicable to a germline collagenopathy. Immunization follows routine schedules; no infectious prophylaxis is disease-specific.

Secondary prevention consists of early molecular diagnosis, cascade testing, early developmental/rehabilitation services, and surveillance for contractures, scoliosis, respiratory insufficiency, feeding problems, joint instability, and cardiac abnormalities when clinically indicated.

Tertiary prevention includes fall and injury reduction, joint stabilization, careful wound management, contracture/spinal monitoring, nutritional support, and timely ventilatory intervention. General EDS evidence supports conservative strengthening and braces but is not mEDS trial evidence. (islam2021ehlersdanlossyndromeimmunologic pages 23-28)

Genetic counseling should explain dominant and recessive recurrence risks, variable expressivity, and VUS limitations. Once familial pathogenic variant(s) are known, prenatal diagnosis and preimplantation genetic testing are technically possible. Carrier testing is relevant to recessive families; presymptomatic/cascade testing is relevant to dominant families. (malfait2020theehlers–danlossyndromes pages 15-16)

---

## 14. Other species and natural disease

No well-established naturally occurring COL12A1-mEDS homolog in companion animals, livestock, or wildlife was identified, and there is no zoonotic or transmissible component. Orthologous collagen-XII genes are conserved across vertebrates, supporting comparative model use, but veterinary prevalence and breed-specific VBO associations are unavailable.

---

## 15. Model organisms and experimental systems

### Mouse

The principal model is the **Col12a1-null mouse** (*Mus musculus*, NCBI Taxon **10090**). It recapitulates reduced grip strength, impaired passive muscle force, delayed fiber-type transition, skeletal abnormalities, short stature, kyphosis/kyphoscoliosis, bone fragility, tendon disorganization, patellar subluxation/dislocation, malformed femoral patellar groove, rectus-femoris abnormalities, central nuclei, and fiber-size variation. (delbaere2020noveldefectsin pages 2-3, zou2014recessiveanddominant pages 1-2, zhu2021ablationofthe pages 16-20)

Tendon studies show defective cellular columns and matrix compartmentalization, abnormal fibril masses/spacing, altered cross-sectional area and mechanics, establishing collagen XII as a regulator of hierarchical tendon development. (izu2021collagenxiimediated pages 15-19)

**Applications:** ECM assembly, mechanotransduction, muscle passive-force transmission, tendon development, patellar stability, bone development, and preclinical target validation.

**Limitations:** a null mouse best models recessive deficiency, not every dominant-negative human allele; feeding/respiratory severity and human long-term functional variability are incompletely reproduced.

### Cellular models

Primary patient dermal fibroblasts are the main human model. They reveal intracellular retention, secretion defects, altered fibril-associated deposition, isoform abnormalities, and secondary decorin/tenascin-X changes. Mutant-allele siRNA rescue provides functional validation. (delbaere2020noveldefectsin pages 1-2, punetha2017novelcol12a1variant pages 3-4, mohassel2019dominantcollagenxii pages 2-3)

No validated mEDS iPSC, organoid, zebrafish, Drosophila, or C. elegans model was established in the retrieved literature.

---

## Recent developments and evidence appraisal

1. **2023 mechanistic synthesis:** Izu and Birk integrated extracellular fibrillogenesis with collagen-XII-dependent regulation of cell shape and communication, framing mEDS as both an ECM-structural and cellular-organization disorder. Published 2 March 2023; DOI: https://doi.org/10.3389/fcell.2023.1129000. (izu2023collagenxiimediated pages 1-2)
2. **2023–2024 case expansion:** additional recessive splice and nonsense alleles continued to broaden severity, while a 2024 p.Pro2968Leu report emphasized the difficulty of assigning pathogenicity without functional confirmation. DOI for the latter: https://doi.org/10.1159/000536344. (ipek2024col12a1genevariant pages 5-6)
3. **2024 diagnostic consensus:** monogenic EDS diagnosis increasingly relies on phenotype-guided massively parallel panel testing rather than clinical labeling alone. Published November 2024; DOI: https://doi.org/10.1515/medgen-2024-2060. (dijk2024clinicaldiagnosisof pages 3-4)
4. **Accepted in 2024/published 2025 recessive cohort:** eight additional patients showed that biallelic disease is not uniformly lethal or nonambulant: 3/8 walked independently and motor improvement without regression occurred, while 5/8 had severe congenital disease. DOI: https://doi.org/10.1002/acn3.52225. (mccarty2025clinicalcharacterizationof pages 1-2, mccarty2025clinicalcharacterizationof pages 7-9, mccarty2025clinicalcharacterizationof pages 2-3)

### Landmark primary sources

- Zou et al., *Human Molecular Genetics*, May 2014, **PMID 24334604**, DOI: https://doi.org/10.1093/hmg/ddt627. The title itself captures the central finding: **“Recessive and dominant mutations in COL12A1 cause a novel EDS/myopathy overlap syndrome in humans and mice.”** (zou2014recessiveanddominant pages 1-2)
- The parallel 2014 discovery evidence is indexed under **PMID 24334769** in the disease–target association record. (OpenTargets Search: myopathic Ehlers-Danlos syndrome-COL12A1)
- Delbaere et al., *Genetics in Medicine*, January 2020, DOI: https://doi.org/10.1038/s41436-019-0599-6; four novel pathogenic heterozygous exon-skipping defects were found in six patients from four families among 78 unresolved clinically selected individuals. (delbaere2020noveldefectsin pages 1-2, delbaere2020noveldefectsin pages 2-3)

## Major knowledge gaps

Reliable incidence, population prevalence, penetrance, carrier frequency, sex ratio, life expectancy, mortality, validated quality-of-life outcomes, longitudinal respiratory/cardiac risk, variant-specific prognosis, biomarkers, and controlled treatment outcomes are unavailable. Likewise absent are disease-specific immune, metabolic, epigenetic, spatial-omics, and advanced human single-cell studies. Published frequencies derive from very small, ascertainment-biased cohorts and should not be interpreted as population estimates.

References

1. (delbaere2020noveldefectsin pages 2-3): Sarah Delbaere, Tibbe Dhooge, Delfien Syx, Florence Petit, Nathalie Goemans, Anne Destrée, Olivier Vanakker, Riet De Rycke, Sofie Symoens, and Fransiska Malfait. Novel defects in collagen xii and vi expand the mixed myopathy/ehlers–danlos syndrome spectrum and lead to variant-specific alterations in the extracellular matrix. Jan 2020. URL: https://doi.org/10.1038/s41436-019-0599-6, doi:10.1038/s41436-019-0599-6. This article has 66 citations and is from a highest quality peer-reviewed journal.

2. (zou2014recessiveanddominant pages 1-2): Yaqun Zou, Daniela Zwolanek, Yayoi Izu, Shreya Gandhy, Gudrun Schreiber, Knut Brockmann, Marcella Devoto, Zuozhen Tian, Ying Hu, Guido Veit, Markus Meier, Jörg Stetefeld, Debbie Hicks, Volker Straub, Nicol C. Voermans, David E. Birk, Elisabeth R. Barton, Manuel Koch, and Carsten G. Bönnemann. Recessive and dominant mutations in col12a1 cause a novel eds/myopathy overlap syndrome in humans and mice. Human molecular genetics, 23 9:2339-52, May 2014. URL: https://doi.org/10.1093/hmg/ddt627, doi:10.1093/hmg/ddt627. This article has 105 citations and is from a domain leading peer-reviewed journal.

3. (mohassel2019dominantcollagenxii pages 2-3): Payam Mohassel, Teerin Liewluck, Ying Hu, Daniel Ezzo, Tracy Ogata, Dimah Saade, Sarah Neuhaus, Véronique Bolduc, Yaqun Zou, Sandra Donkervoort, Livija Medne, Charlotte J. Sumner, P. James B. Dyck, Klaas J. Wierenga, Gihan Tennekoon, Richard S. Finkel, Jiani Chen, Thomas L. Winder, Nathan P. Staff, A. Reghan Foley, Manuel Koch, and Carsten G. Bönnemann. Dominant collagen xii mutations cause a distal myopathy. Annals of Clinical and Translational Neurology, 6:1980-1988, Sep 2019. URL: https://doi.org/10.1002/acn3.50882, doi:10.1002/acn3.50882. This article has 30 citations and is from a peer-reviewed journal.

4. (mccarty2025clinicalcharacterizationof pages 7-9): Riley M. McCarty, Dimah Saade, Pinki Munot, Chamindra G. Laverty, Hailey Pinz, Yaqun Zou, Meghan McAnally, Pomi Yun, Cuixia Tian, Ying Hu, Lucy Feng, Rahul Phadke, Sophia Ceulemans, Pilar Magoulas, Andrew J. Skalsky, Jennifer R. Friedman, Stephen R. Braddock, Sarah B. Neuhaus, Denise M. Malicki, Matthew N. Bainbridge, Shareef Nahas, David P. Dimmock, Stephen F. Kingsmore, Timothy E. Lotze, A. Reghan Foley, Francesco Muntoni, Volker Straub, Sandra Donkervoort, and Carsten G. Bönnemann. Clinical characterization of collagen xii‐related disease caused by biallelic col12a1 variants. Annals of Clinical and Translational Neurology, 12:602-614, Feb 2025. URL: https://doi.org/10.1002/acn3.52225, doi:10.1002/acn3.52225. This article has 4 citations and is from a peer-reviewed journal.

5. (izu2023collagenxiimediated pages 1-2): Yayoi Izu and David E. Birk. Collagen xii mediated cellular and extracellular mechanisms in development, regeneration, and disease. Frontiers in Cell and Developmental Biology, Mar 2023. URL: https://doi.org/10.3389/fcell.2023.1129000, doi:10.3389/fcell.2023.1129000. This article has 58 citations.

6. (merlini2025myopathicehlersdanlossyndrome pages 7-9): Luciano Merlini, Patrizia Sabatelli, Vittoria Cenni, Mariateresa Zanobio, Alberto Di Martino, Francesco Traina, Cesare Faldini, Vincenzo Nigro, and Annalaura Torella. Myopathic ehlers-danlos syndrome (meds) related to col12a1: two novel families and literature review. Jun 2025. URL: https://doi.org/10.3390/ijms26115387, doi:10.3390/ijms26115387. This article has 3 citations.

7. (merlini2025myopathicehlersdanlossyndrome pages 1-2): Luciano Merlini, Patrizia Sabatelli, Vittoria Cenni, Mariateresa Zanobio, Alberto Di Martino, Francesco Traina, Cesare Faldini, Vincenzo Nigro, and Annalaura Torella. Myopathic ehlers-danlos syndrome (meds) related to col12a1: two novel families and literature review. Jun 2025. URL: https://doi.org/10.3390/ijms26115387, doi:10.3390/ijms26115387. This article has 3 citations.

8. (OpenTargets Search: myopathic Ehlers-Danlos syndrome-COL12A1): Open Targets Query (myopathic Ehlers-Danlos syndrome-COL12A1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (chiquet2014collagenxiiprotecting pages 1-3): Matthias Chiquet, David E. Birk, Carsten G. Bönnemann, and Manuel Koch. Collagen xii: protecting bone and muscle integrity by organizing collagen fibrils. Aug 2014. URL: https://doi.org/10.1016/j.biocel.2014.04.020, doi:10.1016/j.biocel.2014.04.020. This article has 131 citations.

10. (delbaere2020noveldefectsin pages 1-2): Sarah Delbaere, Tibbe Dhooge, Delfien Syx, Florence Petit, Nathalie Goemans, Anne Destrée, Olivier Vanakker, Riet De Rycke, Sofie Symoens, and Fransiska Malfait. Novel defects in collagen xii and vi expand the mixed myopathy/ehlers–danlos syndrome spectrum and lead to variant-specific alterations in the extracellular matrix. Jan 2020. URL: https://doi.org/10.1038/s41436-019-0599-6, doi:10.1038/s41436-019-0599-6. This article has 66 citations and is from a highest quality peer-reviewed journal.

11. (punetha2017novelcol12a1variant pages 3-4): Jaya Punetha, Akanchha Kesari, Eric P. Hoffman, Monika Gos, Anna Kamińska, Anna Kostera‐Pruszczyk, Irena Hausmanowa‐Petrusewicz, Ying Hu, Yaqun Zou, Carsten G. Bönnemann, and Maria JȨdrzejowska. Novel col12a1 variant expands the clinical picture of congenital myopathies with extracellular matrix defects. Muscle & Nerve, 55:277-281, Feb 2017. URL: https://doi.org/10.1002/mus.25232, doi:10.1002/mus.25232. This article has 48 citations and is from a peer-reviewed journal.

12. (mccarty2025clinicalcharacterizationof pages 2-3): Riley M. McCarty, Dimah Saade, Pinki Munot, Chamindra G. Laverty, Hailey Pinz, Yaqun Zou, Meghan McAnally, Pomi Yun, Cuixia Tian, Ying Hu, Lucy Feng, Rahul Phadke, Sophia Ceulemans, Pilar Magoulas, Andrew J. Skalsky, Jennifer R. Friedman, Stephen R. Braddock, Sarah B. Neuhaus, Denise M. Malicki, Matthew N. Bainbridge, Shareef Nahas, David P. Dimmock, Stephen F. Kingsmore, Timothy E. Lotze, A. Reghan Foley, Francesco Muntoni, Volker Straub, Sandra Donkervoort, and Carsten G. Bönnemann. Clinical characterization of collagen xii‐related disease caused by biallelic col12a1 variants. Annals of Clinical and Translational Neurology, 12:602-614, Feb 2025. URL: https://doi.org/10.1002/acn3.52225, doi:10.1002/acn3.52225. This article has 4 citations and is from a peer-reviewed journal.

13. (mccarty2025clinicalcharacterizationof pages 1-2): Riley M. McCarty, Dimah Saade, Pinki Munot, Chamindra G. Laverty, Hailey Pinz, Yaqun Zou, Meghan McAnally, Pomi Yun, Cuixia Tian, Ying Hu, Lucy Feng, Rahul Phadke, Sophia Ceulemans, Pilar Magoulas, Andrew J. Skalsky, Jennifer R. Friedman, Stephen R. Braddock, Sarah B. Neuhaus, Denise M. Malicki, Matthew N. Bainbridge, Shareef Nahas, David P. Dimmock, Stephen F. Kingsmore, Timothy E. Lotze, A. Reghan Foley, Francesco Muntoni, Volker Straub, Sandra Donkervoort, and Carsten G. Bönnemann. Clinical characterization of collagen xii‐related disease caused by biallelic col12a1 variants. Annals of Clinical and Translational Neurology, 12:602-614, Feb 2025. URL: https://doi.org/10.1002/acn3.52225, doi:10.1002/acn3.52225. This article has 4 citations and is from a peer-reviewed journal.

14. (ipek2024col12a1genevariant pages 5-6): Rojan İpek, Büşra Eser Çavdartepe, Sevcan Tuğ Bozdoğan, and Uluç Yiş. Col12a1 gene variant and a review of the literature: a case report of ullrich congenital muscular dystrophy. Molecular Syndromology, 15:311-316, Feb 2024. URL: https://doi.org/10.1159/000536344, doi:10.1159/000536344. This article has 3 citations and is from a peer-reviewed journal.

15. (chiquet2014collagenxiiprotecting pages 3-4): Matthias Chiquet, David E. Birk, Carsten G. Bönnemann, and Manuel Koch. Collagen xii: protecting bone and muscle integrity by organizing collagen fibrils. Aug 2014. URL: https://doi.org/10.1016/j.biocel.2014.04.020, doi:10.1016/j.biocel.2014.04.020. This article has 131 citations.

16. (merlini2025myopathicehlersdanlossyndrome pages 2-3): Luciano Merlini, Patrizia Sabatelli, Vittoria Cenni, Mariateresa Zanobio, Alberto Di Martino, Francesco Traina, Cesare Faldini, Vincenzo Nigro, and Annalaura Torella. Myopathic ehlers-danlos syndrome (meds) related to col12a1: two novel families and literature review. Jun 2025. URL: https://doi.org/10.3390/ijms26115387, doi:10.3390/ijms26115387. This article has 3 citations.

17. (mccarty2025clinicalcharacterizationof pages 3-4): Riley M. McCarty, Dimah Saade, Pinki Munot, Chamindra G. Laverty, Hailey Pinz, Yaqun Zou, Meghan McAnally, Pomi Yun, Cuixia Tian, Ying Hu, Lucy Feng, Rahul Phadke, Sophia Ceulemans, Pilar Magoulas, Andrew J. Skalsky, Jennifer R. Friedman, Stephen R. Braddock, Sarah B. Neuhaus, Denise M. Malicki, Matthew N. Bainbridge, Shareef Nahas, David P. Dimmock, Stephen F. Kingsmore, Timothy E. Lotze, A. Reghan Foley, Francesco Muntoni, Volker Straub, Sandra Donkervoort, and Carsten G. Bönnemann. Clinical characterization of collagen xii‐related disease caused by biallelic col12a1 variants. Annals of Clinical and Translational Neurology, 12:602-614, Feb 2025. URL: https://doi.org/10.1002/acn3.52225, doi:10.1002/acn3.52225. This article has 4 citations and is from a peer-reviewed journal.

18. (zhu2021ablationofthe pages 16-20): Mengjie Zhu, Fabian Metzen, Janina Betz, Mark Hopkinson, Juliane Heilig, Thomas Imhof, Anja Niehoff, David E. Birk, Yayoi Izu, Andrew A. Pitsillides, Janine Altmüller, Gudrun Schreiber, Mats Paulsson, Manuel Koch, and Bent Brachvogel. Ablation of the facit collagen xii disturbs musculoskeletal ecm organization and causes patella dislocation and myopathy. bioRxiv, Dec 2021. URL: https://doi.org/10.1101/2021.12.29.474475, doi:10.1101/2021.12.29.474475. This article has 0 citations.

19. (izu2021collagenxiimediated pages 15-19): Yayoi Izu, Sheila M. Adams, Brianne K. Connizzo, David P. Beason, Louis J. Soslowsky, Manuel Koch, and David E. Birk. Collagen xii mediated cellular and extracellular mechanisms regulate establishment of tendon structure and function. Jan 2021. URL: https://doi.org/10.1016/j.matbio.2020.10.004, doi:10.1016/j.matbio.2020.10.004. This article has 48 citations and is from a domain leading peer-reviewed journal.

20. (chiquet2014collagenxiiprotecting pages 9-11): Matthias Chiquet, David E. Birk, Carsten G. Bönnemann, and Manuel Koch. Collagen xii: protecting bone and muscle integrity by organizing collagen fibrils. Aug 2014. URL: https://doi.org/10.1016/j.biocel.2014.04.020, doi:10.1016/j.biocel.2014.04.020. This article has 131 citations.

21. (dijk2024clinicaldiagnosisof pages 3-4): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 4 citations.

22. (fajardojimenez2022ehlersdanlosaliterature pages 3-4): María José Fajardo-Jiménez, Johanna A. Tejada-Moreno, Alejandro Mejía-García, Andrés Villegas-Lanau, Wildeman Zapata-Builes, Jorge E. Restrepo, Gina P. Cuartas, and Juan C. Hernandez. Ehlers-danlos: a literature review and case report in a colombian woman with multiple comorbidities. Nov 2022. URL: https://doi.org/10.3390/genes13112118, doi:10.3390/genes13112118. This article has 2 citations.

23. (islam2021ehlersdanlossyndromeimmunologic pages 23-28): Mareesa Islam, Christopher Chang, and M. Eric Gershwin. Ehlers-danlos syndrome: immunologic contrasts and connective tissue comparisons. Jan 2021. URL: https://doi.org/10.1016/j.jtauto.2020.100077, doi:10.1016/j.jtauto.2020.100077. This article has 40 citations and is from a peer-reviewed journal.

24. (malfait2020theehlers–danlossyndromes pages 15-16): Fransiska Malfait, Marco Castori, Clair A. Francomano, Cecilia Giunta, Tomoki Kosho, and Peter H. Byers. The ehlers–danlos syndromes. Jul 2020. URL: https://doi.org/10.1038/s41572-020-0194-9, doi:10.1038/s41572-020-0194-9. This article has 294 citations.

## Artifacts

- [Edison artifact artifact-00](Myopathic_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0034022` (2 mentions) - the report calls it "if available"; MONDO calls it **Bethlem myopathy 2**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002802` (2 mentions) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (2 mentions) - replaced by `HP:0001288`
- `GO:0062023` (obsolete collagen-containing extracellular matrix) (2 mentions) - replaced by `GO:0031012`