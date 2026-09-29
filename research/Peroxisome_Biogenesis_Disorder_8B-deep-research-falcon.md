---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T14:30:04.631064'
end_time: '2026-09-16T14:42:27.038065'
duration_seconds: 742.41
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: PEX16 deficiency (peroxisome biogenesis disorder 8B, the mild non-Zellweger
    end of the PEX16 spectrum)
  mondo_id: MONDO:0013943
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 34
  not_found: 1
  obsolete: 1
  unverifiable: 7
  confabulation_rate: 0.028
  labels_checked: 5
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013943
    reported_labels:
    - if available
    ontology_label: peroxisome biogenesis disorder 8B
  - term_id: HP:0032312
    reported_labels:
    - abnormal very-long-chain fatty-acid level
    ontology_label: Decreased circulating globulin concentration
  labels_variant: 2
  unresolved_terms:
  - HP:000
  obsolete_terms:
  - term_id: HP:0040083
    ontology_label: obsolete Toe walking
    replaced_by: HP:0030051
  unresolvable_prefixes:
  - OMIM
  - Taxon
  - ClinicalTrials.gov
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_8B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PEX16 deficiency (peroxisome biogenesis disorder 8B, the mild non-Zellweger end of the PEX16 spectrum)
- **MONDO ID:** MONDO:0013943 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PEX16 deficiency (peroxisome biogenesis disorder 8B, the mild non-Zellweger end of the PEX16 spectrum)** covering all of the
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
- **Disease Name:** PEX16 deficiency (peroxisome biogenesis disorder 8B, the mild non-Zellweger end of the PEX16 spectrum)
- **MONDO ID:** MONDO:0013943 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PEX16 deficiency (peroxisome biogenesis disorder 8B, the mild non-Zellweger end of the PEX16 spectrum)** covering all of the
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


# PEX16 Deficiency / Peroxisome Biogenesis Disorder 8B

## Executive summary

PEX16 deficiency is an ultra-rare, autosomal-recessive peroxisome-biogenesis disorder caused by biallelic pathogenic variants in **PEX16**. The historical label **peroxisome biogenesis disorder 8B (PBD8B)** denotes the milder, non-classic-Zellweger end of the PEX16 phenotypic continuum. Its best-documented presentation is a childhood-onset, slowly progressive spastic-ataxia/leukodystrophy syndrome that may include dystonia, tremor, dysarthria, neuropathy, hearing or visual disease, while cognition and plasma very-long-chain fatty acids (VLCFAs) can be relatively preserved. This is not a separate biochemical mechanism from PEX16-related Zellweger spectrum disorder (ZSD), but a severity category generally associated with residual PEX16 function. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2, rayana2026polyunsaturatedfattyacid pages 14-15)

The evidence base is unusually small. Many statements below derive either from individual PEX16 patients, patient-derived cells, or aggregate ZSD guidance rather than PBD8B-specific cohorts. Consequently, frequencies, penetrance, incidence, survival, and treatment-response estimates cannot presently be calculated reliably.

| Domain | PEX16-specific finding | Evidence strength/type | Suggested ontology identifiers |
|---|---|---|---|
| Identity | Mild **PEX16 deficiency / peroxisome biogenesis disorder 8B (PBD8B)** is the non-neonatal, milder end of the PEX16-related Zellweger-spectrum continuum. **OMIM 614877**; PEX16-related severe PBD8A/Zellweger phenotype is OMIM 614876. (rayana2026polyunsaturatedfattyacid pages 14-15) | Authoritative disease classification; human disease literature | OMIM:614877; MONDO:0013943 **user supplied—verify against current MONDO release**; MeSH/Orphanet/ICD exact mappings: verify |
| Causal gene | **PEX16**, encoding peroxisomal biogenesis factor 16; gene **OMIM 603360**. (rayana2026polyunsaturatedfattyacid pages 14-15) | Curated gene–disease and functional evidence | HGNC:8857 **verify current HGNC record**; OMIM:603360; GO:0005777 (peroxisome) |
| Inheritance | Biallelic germline PEX16 variants cause disease through an **autosomal-recessive** mechanism; the reported mild adult had compound-heterozygous variants inherited from the parents. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2) | Strong human segregation plus functional evidence | HP:0000007 (autosomal recessive inheritance) |
| Cardinal phenotype | A slowly progressive **spastic-ataxia/leukodystrophy phenotype** may begin in childhood with toe walking and falls and evolve into marked lower-limb spasticity, cerebellar ataxia/dysarthria, tremor, dystonia, white-matter abnormalities, and wheelchair dependence; cognition may remain substantially preserved. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2) | PEX16-specific human case evidence; very small sample | HP:0001257 (spasticity); HP:0001251 (ataxia); HP:0001260 (dysarthria); HP:0001332 (dystonia); HP:0002415 (leukodystrophy); HP:0002352 (white-matter abnormality) |
| Other possible manifestations | Across PEX16-related disease, reported ocular findings include cataract, optic atrophy, and abnormal retinal pigmentation; atypical cases require surveillance for hearing, vision, liver, adrenal, renal, skeletal, and neurologic complications. (rayana2026polyunsaturatedfattyacid pages 14-15, NCT01668186 chunk 1) | PEX16 ocular summary plus broader ZSD natural-history protocol; frequencies unknown | HP:0000518 (cataract); HP:0000648 (optic atrophy); HP:0007703 (abnormal retinal pigmentation); additional exact terms: verify |
| Biochemical caveat | Plasma VLCFAs may be **normal or only mildly abnormal** in mild PEX16 disease; normal VLCFAs therefore do not exclude PBD8B. Broader testing includes C26:0/C26:1 and C24:0/C22:0 and C26:0/C22:0 ratios, phytanic/pristanic acids, erythrocyte plasmalogens, pipecolic acid, and DHCA/THCA. (kumar2018expandingthespectrum pages 2-3, braverman2016peroxisomebiogenesisdisorders pages 3-4) | Direct PEX16 case observation plus expert diagnostic review | HP:0032312 (abnormal very-long-chain fatty-acid level)—exact applicability may be absent in mild disease; CHEBI identifiers for individual analytes: verify |
| Molecular mechanism | PEX16 is an integral peroxisomal membrane biogenesis factor and PEX3 docking component. Biallelic dysfunction disrupts early membrane assembly and protein trafficking, producing fewer, enlarged, or absent functional peroxisomes and downstream impairment of VLCFA/branched-chain fatty-acid oxidation, ether-lipid synthesis, bile-acid metabolism, and redox homeostasis. (kumar2018expandingthespectrum pages 1-2, wangler2017peroxisomalbiogenesisis pages 3-6, chen2024hepatocytespecificpex16abrogation pages 1-2) | Human patient-cell evidence supported by fly and mouse functional studies; some downstream tissue links remain inferred | GO:0007031 (peroxisome organization); GO:0016558 (protein import into peroxisome matrix); GO:0033540 (fatty-acid beta-oxidation using acyl-CoA oxidase); GO:0005777 (peroxisome); GO:0005783 (endoplasmic reticulum) |
| Diagnostic approach | Confirm with biallelic PEX16 variants using a peroxisomal-disorder/leukodystrophy panel, exome, or genome sequencing, with deletion/duplication analysis as needed. Pair genetics with multianalyte peroxisomal biochemistry and, when results are equivocal, cultured-fibroblast assays of catalase localization, peroxisome number/morphology, VLCFA oxidation, and plasmalogen synthesis. (kumar2018expandingthespectrum pages 2-3, braverman2016peroxisomebiogenesisdisorders pages 3-4, braverman2016peroxisomebiogenesisdisorders pages 4-6) | Expert-review/technical-standard approach plus PEX16 patient-cell validation | NCIT:C15709 (genetic testing); NCIT:C101295 (whole-exome sequencing)—verify current NCIT labels; LOINC assay identifiers: laboratory-specific/verify |
| Treatment status | No approved PEX16-specific disease-modifying treatment is established. Management is multidisciplinary and supportive: physical/occupational/speech therapy, mobility and spasticity management, hearing/vision support, nutritional or gastrostomy support when needed, seizure treatment, and surveillance of liver, adrenal, renal, bone, dental, and neurologic status. (braverman2016peroxisomebiogenesisdisorders pages 4-6, braverman2016peroxisomebiogenesisdisorders pages 10-12) | Expert consensus extrapolated from Zellweger-spectrum care; no PEX16-specific response rates | NCIT:C15329 (supportive care); NCIT intervention identifiers for individual therapies: verify |
| Prognosis | PBD8B can permit survival into adulthood but is generally chronic and neurologically progressive; one individual progressed from childhood gait disturbance to wheelchair dependence while retaining near-normal cognition at age 41. Gene-specific survival rates, life expectancy, and validated prognostic biomarkers are unavailable. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2) | Direct longitudinal history from one adult plus major evidence gaps | HP:0003676 (progressive disorder); survival/prognosis ontology mapping: verify |
| Model evidence | Pex16-null Drosophila show reduced peroxisomes, locomotor impairment, bang sensitivity, and markedly shortened lifespan; human reference PEX16 rescues organelle and behavioral phenotypes, whereas variant rescue distinguishes severe from hypomorphic alleles. Hepatocyte-specific Pex16-knockout mice lack hepatic peroxisomes and show enlarged liver, hepatocyte proliferation, altered serum lipids/bile acids, and resistance to diet-induced steatosis. (gomez2024distinguishingpexgene pages 16-21, gomez2024distinguishingpexgene pages 32-39, chen2024hepatocytespecificpex16abrogation pages 1-2) | Strong experimental loss-of-function/rescue evidence; organismal models do not fully reproduce mild human neurologic disease | NCBI Taxon:7227 (Drosophila melanogaster); NCBI Taxon:10090 (Mus musculus); CL:0000182 (hepatocyte) |
| Current research/registries | The recruiting longitudinal PBD natural-history study **NCT01668186** targets 244 participants with annual multisystem, imaging, biochemical, and genotype–phenotype follow-up; the recruiting ZSD retinopathy study **NCT06190626** targets 30 participants. Neither provides PEX16-specific outcomes yet. (NCT01668186 chunk 1, NCT06190626 chunk 2) | Active observational research; no efficacy inference | ClinicalTrials.gov:NCT01668186; ClinicalTrials.gov:NCT06190626 |
| Key evidence gaps | No reliable PEX16/PBD8B prevalence, incidence, penetrance estimate, sex ratio, carrier frequency, founder effect, protective allele, environmental modifier, validated quality-of-life measure, genotype-specific treatment response, natural veterinary counterpart, or proven epigenomic/single-cell/spatial signature has been established. | Absence of adequate PEX16-specific cohorts; do not infer from aggregate ZSD data | Ontology mappings unavailable or not applicable; mark as **unknown** rather than negative where systematic study is lacking |


*Table: Compact knowledge-base summary of mild PEX16 deficiency/PBD8B, integrating human, cellular, animal-model, diagnostic, and clinical-management evidence. Unverified or unavailable ontology mappings and major evidence gaps are explicitly identified.*

## 1. Disease information

### Definition and scope

PEX16 is required early in peroxisomal membrane assembly. Biallelic dysfunction reduces the formation of competent peroxisomes and secondarily disrupts several lipid-metabolic and redox functions. PEX16-related disease spans severe neonatal Zellweger syndrome through atypical childhood/adult neurodegenerative disease. PBD8B should therefore be modeled as the **mild end of a continuous PEX16-related ZSD spectrum**, not as an entirely independent disorder. Historical labels such as neonatal adrenoleukodystrophy and infantile Refsum disease likewise describe severity positions rather than cleanly separable entities. (rayana2026polyunsaturatedfattyacid pages 14-15, braverman2016peroxisomebiogenesisdisorders pages 1-3)

### Identifiers and synonyms

- **Preferred name:** peroxisome biogenesis disorder 8B.
- **Synonyms:** PBD8B; mild PEX16 deficiency; atypical PEX16-related Zellweger spectrum disorder; PEX16-related spastic ataxia; mild PEX16-related peroxisome-biogenesis disorder.
- **OMIM disease:** **614877** (PBD8B).
- **Related severe allelic disorder:** **OMIM 614876**, PBD8A/Zellweger syndrome.
- **Gene:** **PEX16**, OMIM **603360**. (rayana2026polyunsaturatedfattyacid pages 14-15)
- **MONDO:** the supplied **MONDO:0013943** should be retained provisionally but verified against the current MONDO release; the retrieved Open Targets query did not resolve a PBD8B–PEX16 association. (OpenTargets Search: peroxisome biogenesis disorder 8B-PEX16)
- **Orphanet, MeSH, ICD-10/ICD-11:** no confidently PBD8B-specific identifiers were recovered. Coding usually occurs under broader peroxisomal-disorder/Zellweger-spectrum categories; database-specific verification is required.

The present entry is an **aggregated disease-level synthesis**, but much of the PEX16-specific clinical evidence originates from case reports or small case series rather than EHR-scale datasets. The 2022 PEX16 atypical-ZSD case series was published online February 2, 2022 (Neurogenetics 23:115–127; **PMID 35106698**; DOI: [10.1007/s10048-022-00684-7](https://doi.org/10.1007/s10048-022-00684-7)). (NCT01668186 chunk 2)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **biallelic germline loss-of-function or hypomorphic variation in PEX16**. The inheritance pattern is autosomal recessive. Severe null-like alleles are expected to abolish peroxisome formation more extensively, whereas residual-function missense or in-frame alleles may support survival into childhood or adulthood. Humanized-fly experiments support an allele-severity continuum rather than a simple variant-class rule. (kumar2018expandingthespectrum pages 1-2, gomez2024distinguishingpexgene pages 16-21)

A well-characterized 41-year-old woman carried compound-heterozygous variants **NM_004813.2:c.658G>A, p.(Ala220Thr)** and **c.830G>A, p.(Arg277Gln)**. Both were absent or extremely rare in gnomAD, affected conserved residues, were computationally predicted to be damaging, segregated from the parents, and were accompanied by abnormal peroxisome morphology and function in patient-derived neural stem-like cells. These observations support pathogenicity, although current ClinVar classifications should be checked independently before clinical reporting. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)

The atypical allele **PEX16 p.Phe332del** showed substantial rescue in humanized Drosophila, consistent with a hypomorphic effect. By contrast, **p.Arg176Ter** failed to rescue major phenotypes and behaved as a severe allele. This is experimental variant-functional evidence, not by itself an ACMG clinical classification. (gomez2024distinguishingpexgene pages 16-21, gomez2024distinguishingpexgene pages 32-39)

### Other risk factors

- **Family history/consanguinity:** increase the prior probability of inheriting two pathogenic alleles but are not necessary; an affected individual may be the first recognized case.
- **Sex:** both sexes are expected to be affected equally because the locus is autosomal. No reliable PBD8B sex-ratio data exist.
- **Age:** age modifies clinical expression, not genetic susceptibility; manifestations can accumulate over decades.
- **Modifier genes, founder alleles, germline mosaicism, anticipation:** no PEX16-specific evidence sufficient for quantitative conclusions was identified. Anticipation is not expected for a recessive non-repeat disorder.

### Environmental, protective, and gene–environment factors

No toxin, infection, lifestyle, occupational exposure, or dietary pattern is established as a cause of PBD8B. No protective PEX16 allele or validated environmental protective factor is known. Nutritional state can, however, alter **biomarker detectability**: phytanic and pristanic acids may be normal in breastfed neonates because dietary exposure is limited. This is a diagnostic interaction, not evidence that diet prevents the genetic disease. (braverman2016peroxisomebiogenesisdisorders pages 3-4)

Fly data show disproportionate sensitivity to starvation and glucose deprivation, suggesting that systemic metabolic stress can modify phenotype after peroxisome loss. That observation remains preclinical and does not justify a PBD8B-specific high-carbohydrate regimen. (wangler2017peroxisomalbiogenesisis pages 1-2)

## 3. Phenotypes

### Core mild-PEX16 phenotype

The most informative longitudinal case began toe-walking and falling frequently at age three. Gait impairment progressed to wheelchair dependence. Tremor, fine-motor impairment, and involuntary facial movements emerged around age 19; speech disturbance appeared in the mid-thirties. At 41 years, findings included severe lower-limb spasticity, upper-limb ataxia, cerebellar dysarthria, cervical dystonia, head tremor, and Meige-like orofacial movements. Cognition was nearly preserved (MMSE 29/30). MRI demonstrated confluent white-matter abnormalities and atrophy, and MR spectroscopy showed raised myoinositol. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)

Suggested phenotype annotations include:

- Childhood-onset gait abnormality — **HP:000 gait abnormality; exact child term should be verified**.
- Frequent falls — **HP:0002527**.
- Toe walking — **HP:0040083**.
- Progressive spastic paraplegia/spasticity — **HP:0001257**.
- Cerebellar ataxia — **HP:0001251**.
- Dysarthria — **HP:0001260**.
- Tremor — **HP:0001337**.
- Dystonia — **HP:0001332**.
- Leukodystrophy/white-matter abnormality — **HP:0002415 / HP:0002352**.
- Cerebral or cerebellar atrophy — select the site-specific HPO term from imaging.
- Preserved cognition should be stored as an observed negative/qualifier rather than a phenotype.

The same adult had no seizures, known liver disease, or adrenal insufficiency; VLCFAs, nerve-conduction studies, and needle EMG were normal. These are case-specific negative findings and must not be interpreted as universal exclusions. (kumar2018expandingthespectrum pages 2-3)

### Broader PEX16/ZSD manifestations

Reported PEX16-associated ocular manifestations include cataract, optic atrophy, and abnormal retinal pigmentation. Suggested HPO terms are **HP:0000518**, **HP:0000648**, and **HP:0007703**, respectively. Across ZSD, hearing loss, retinal degeneration, peripheral neuropathy, seizures, hypotonia, feeding difficulty, liver dysfunction, adrenal insufficiency, renal cortical cysts or oxalate stones, low bone density, fractures, and enamel defects may occur; their frequency specifically in PBD8B is unknown. (rayana2026polyunsaturatedfattyacid pages 14-15, braverman2016peroxisomebiogenesisdisorders pages 20-20)

Laboratory abnormalities may include elevated C26:0/C26:1, abnormal C24:0/C22:0 or C26:0/C22:0 ratios, elevated phytanic/pristanic acids, DHCA/THCA and pipecolic acid, and reduced erythrocyte plasmalogens. Mild PEX16 disease can have normal plasma VLCFAs; the finding therefore has incomplete sensitivity. (braverman2016peroxisomebiogenesisdisorders pages 3-4)

### Severity, progression, and quality of life

The characteristic course is chronic and slowly progressive, but expressivity is broad. Mobility, speech, fine-motor function, vision, and hearing can substantially impair education, employment, independence, and caregiver burden. No PEX16-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life dataset was identified. Aggregate ZSD caregiver work exists, but it cannot provide a PBD8B-specific estimate. (bose2020zellwegerspectrumdisorder pages 7-8)

## 4. Genetic and molecular information

**PEX16** encodes an integral peroxisomal membrane protein. It provides a docking context for PEX3; PEX3 recruits PEX19 and supports delivery of newly synthesized peroxisomal membrane proteins. PEX16 participates in early membrane designation and de novo organelle formation associated with the endoplasmic reticulum. (wangler2017peroxisomalbiogenesisis pages 3-6, chen2024hepatocytespecificpex16abrogation pages 1-2)

Pathogenic variants are germline and biallelic. Reported disease alleles include missense, nonsense, and in-frame-deletion classes. The likely mechanism is loss or reduction of function, not gain of function or dominant negativity. Population frequencies are generally extremely low, but variant-level gnomAD values were not recoverable from the source set and should be queried against the current genome build and transcript.

No validated modifier gene, PEX16-specific methylation signature, histone abnormality, chromosomal rearrangement, or recurrent copy-number syndrome was identified. Chromosomal microarray may detect an exon-spanning or whole-gene deletion but is not the primary test for typical sequence-level PEX16 disease.

## 5. Environmental information

PEX16 deficiency is a Mendelian organelle-biogenesis disorder, not an infectious, toxic, radiation-associated, or lifestyle-acquired condition. Smoking, alcohol, physical activity, and pollution have not been shown to alter penetrance. General health maintenance remains appropriate, but it should not be represented as disease prevention. No infectious trigger or zoonotic process applies.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic or hypomorphic PEX16 variants lead to** absent or reduced functional PEX16 at early peroxisomal membranes. (kumar2018expandingthespectrum pages 1-2, chen2024hepatocytespecificpex16abrogation pages 1-2)
2. **Reduced PEX16 activity leads to** defective PEX3 docking, peroxisomal membrane-protein recruitment, and de novo peroxisome assembly. (wangler2017peroxisomalbiogenesisis pages 3-6, chen2024hepatocytespecificpex16abrogation pages 1-2)
3. **Defective assembly results in** fewer, enlarged, absent, or import-incompetent peroxisomes; this is directly demonstrated in patient-derived cells, flies, and conditional mouse hepatocytes. (kumar2018expandingthespectrum pages 2-3, wangler2017peroxisomalbiogenesisis pages 3-6, chen2024hepatocytespecificpex16abrogation pages 1-2)
4. **Loss of competent peroxisomes leads to** impaired VLCFA β-oxidation, branched-chain fatty-acid oxidation, ether-lipid/plasmalogen synthesis, bile-acid maturation, and redox handling. (rayana2026polyunsaturatedfattyacid pages 14-15, wangler2017peroxisomalbiogenesisis pages 3-6)
5. **These metabolic defects result in** substrate accumulation and product deficiency. In mild disease this biochemical disturbance may be tissue-restricted or below the sensitivity of plasma VLCFA testing; that interpretation is plausible but not fully demonstrated in every PBD8B patient. (kumar2018expandingthespectrum pages 2-3, braverman2016peroxisomebiogenesisdisorders pages 3-4)
6. **Neural branch:** altered membrane lipids, redox homeostasis, and metabolic support are inferred to cause axonal, myelin, cerebellar, and white-matter dysfunction, leading to progressive spasticity, ataxia, dystonia, dysarthria, and leukodystrophy. Human cellular and clinical associations are strong, but the contribution of each metabolite is unresolved. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2, wangler2017peroxisomalbiogenesisis pages 2-3)
7. **Hepatic branch:** hepatocyte peroxisome loss causes altered lipid and bile-acid metabolism and abnormal proliferative control; conditional Pex16-null mice directly show absent hepatic peroxisomes, hepatocyte proliferation, and hepatomegaly. Translation of these findings to mild human PEX16 deficiency is incomplete. (chen2024hepatocytespecificpex16abrogation pages 1-2)
8. **Systemic branch:** broader disturbances of glycolysis, glycogen metabolism, and the pentose-phosphate pathway may amplify energetic vulnerability; this is supported by fly metabolomics and mouse transcriptional correlations but remains inferential in human PBD8B. (wangler2017peroxisomalbiogenesisis pages 1-2)

Relevant biological-process terms include **GO:0007031 peroxisome organization**, **GO:0016558 protein import into peroxisome matrix**, fatty-acid β-oxidation, ether-lipid biosynthesis, bile-acid biosynthesis, and cellular redox homeostasis. Relevant compartments are **GO:0005777 peroxisome** and **GO:0005783 endoplasmic reticulum**.

Suggested cell annotations are neuron (**CL:0000540**), oligodendrocyte (**CL:0000128**), astrocyte (**CL:0000127**), hepatocyte (**CL:0000182**), retinal pigment epithelial cell, photoreceptor, and peripheral myelinating Schwann cell. Direct PEX16-specific evidence is strongest for patient-derived olfactory neurosphere cells and mouse hepatocytes; involvement of other named cells is based mainly on anatomy and broader PBD models.

### Molecular profiling

Patient-derived olfactory-neurosphere cells had reduced peroxisome density, increased organelle size, reduced catalase activity, and an altered hydrogen-peroxide response. Lower measured oxidative stress after H₂O₂ exposure was interpreted as possible compensation by other peroxide-metabolizing enzymes, not evidence that PEX16 loss is antioxidative. (kumar2018expandingthespectrum pages 1-2)

Drosophila pex16 mutants accumulated long-chain species including C24:0–C30:0, had decreased plasmalogen, and displayed changes in glycolysis, glycogen metabolism, and the pentose-phosphate pathway. No disease-specific human single-cell, spatial-transcriptomic, epigenomic, or integrated multi-omic atlas was identified. (wangler2017peroxisomalbiogenesisis pages 3-6, wangler2017peroxisomalbiogenesisis pages 1-2)

## 7. Anatomical structures affected

The **central nervous system** is the dominant organ system in mild disease: corticospinal tracts, cerebral white matter, cerebellar systems, and likely long axons are clinically implicated. The peripheral nervous system may be affected in the broader spectrum, although electrophysiology can remain normal. Other organs requiring surveillance include retina/optic nerve, inner ear, liver, adrenal glands, kidneys, skeleton, teeth, and gastrointestinal/nutritional systems. (kumar2018expandingthespectrum pages 2-3, NCT01668186 chunk 1, braverman2016peroxisomebiogenesisdisorders pages 20-20)

Suggested anatomy terms include brain (**UBERON:0000955**), cerebral white matter, cerebellum (**UBERON:0002037**), spinal cord (**UBERON:0002240**), liver (**UBERON:0002107**), retina (**UBERON:0000966**), optic nerve, kidney (**UBERON:0002113**), and adrenal gland (**UBERON:0002369**). Disease manifestations are generally bilateral/systemic rather than consistently lateralized.

## 8. Temporal development

Onset may be congenital in severe PEX16 deficiency, but PBD8B often has childhood or occasionally later recognition. The documented adult case had insidious motor onset at three years, later extrapyramidal/cerebellar manifestations, and decades-long progression. PBD8B is lifelong; spontaneous remission has not been described. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)

Critical periods are plausible during fetal neuronal migration, postnatal myelination, and retinal development, but the relative importance of developmental injury versus ongoing degeneration is unresolved. Early molecular diagnosis is valuable because hearing, vision, adrenal, nutritional, orthopedic, and renal complications may be treatable even when the primary biogenesis defect is not.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. When both parents are confirmed heterozygous carriers, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier child, and 25% probability of inheriting neither familial allele. Expression is variable and depends partly on residual allelic function. Penetrance for clearly pathogenic biallelic genotypes is presumed high but has not been quantified for hypomorphic combinations.

No defensible PBD8B-specific prevalence, incidence, carrier frequency, founder effect, geographic concentration, ethnic enrichment, sex ratio, or age distribution was found. The absence of estimates reflects extreme rarity and ascertainment bias, not proof of equal worldwide frequency. Consanguinity can increase occurrence of homozygous genotypes but is not required.

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** consider PEX16/PBD8B in unexplained childhood- or adult-onset spastic ataxia, leukodystrophy, dystonia, neuropathy, retinal/hearing disease, or a multisystem peroxisomal phenotype.
2. **Biochemistry:** fasting plasma C26:0/C26:1 and C24:0/C22:0 and C26:0/C22:0 ratios; phytanic and pristanic acids; erythrocyte plasmalogens; plasma/urine pipecolic acid; plasma/urine DHCA and THCA. A normal VLCFA profile does **not** exclude mild PEX16 deficiency. (braverman2016peroxisomebiogenesisdisorders pages 3-4)
3. **Molecular confirmation:** sequencing and deletion/duplication analysis of PEX16 through a peroxisomal-disorder, leukodystrophy, hereditary-spastic-paraplegia, or ataxia panel. Exome or genome sequencing is appropriate for nonspecific or panel-negative cases; WGS identified the two variants in the key adult case. (kumar2018expandingthespectrum pages 2-3)
4. **Functional resolution:** cultured fibroblast or other patient-cell assays can assess catalase localization, peroxisome number/morphology, VLCFA oxidation/accumulation, phytanic/pristanic oxidation, and plasmalogen synthesis. These are particularly important with VUSs or mild biochemical findings. (braverman2016peroxisomebiogenesisdisorders pages 3-4)
5. **Phenotypic staging:** brain MRI, ophthalmologic examination/OCT/FAF, audiology, liver and adrenal testing, renal function/urine oxalate and ultrasound, bone density, dental review, neurologic examination, and developmental/functional assessment. (NCT01668186 chunk 1, braverman2016peroxisomebiogenesisdisorders pages 20-20)

The ACMG-aligned technical framework is represented by the 2020 laboratory standard, while the major clinical overview is Braverman et al., published online December 23, 2015 and in March 2016 (**PMID 26750748**; DOI: [10.1016/j.ymgme.2015.12.009](https://doi.org/10.1016/j.ymgme.2015.12.009)). (NCT06190626 chunk 2)

### Differential diagnosis

Important alternatives include other PEX-related ZSDs; single-enzyme peroxisomal disorders such as ACOX1 or HSD17B4 deficiency; X-linked adrenoleukodystrophy; Refsum disease; complicated hereditary spastic paraplegias; mitochondrial leukodystrophies; metachromatic leukodystrophy; Krabbe disease; cerebrotendinous xanthomatosis; and adult-onset genetic ataxias. Approximately 10–15% of suspected patients with elevated VLCFAs may instead have a single-enzyme defect, reinforcing the need for multianalyte and molecular confirmation. (braverman2016peroxisomebiogenesisdisorders pages 3-4)

CMA, karyotyping, FISH, mitochondrial-DNA testing, and repeat-expansion assays are not first-line PEX16 tests unless the phenotype or sequencing data indicate an alternative mechanism. RNA sequencing can help resolve suspected splice variants, but no validated PEX16 transcriptomic diagnostic signature exists.

### Screening

Population newborn screening specifically for PBD8B is not established. X-ALD newborn-screening assays based on elevated VLCFAs may incidentally detect many ZSD cases but can miss biochemically mild PEX16 disease. Cascade testing of relatives is appropriate after familial variants are established. (braverman2016peroxisomebiogenesisdisorders pages 4-6)

## 11. Outcome and prognosis

PBD8B is compatible with survival into adulthood. It is nevertheless potentially progressive and disabling: the most detailed patient advanced from early-childhood gait difficulty to wheelchair dependence while retaining near-normal cognition at 41. No PEX16-specific five- or ten-year survival, mortality rate, median life expectancy, or validated prognostic model exists. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)

Likely prognostic factors include residual PEX16 function, age at onset, severity of developmental brain disease, rate of white-matter progression, sensory loss, liver/adrenal involvement, and nutritional/respiratory complications. These are biologically and clinically plausible but have not been quantified for PBD8B. Recovery of established neurodegeneration is not documented; rehabilitation may preserve function and prevent secondary complications.

## 12. Treatment and current implementation

No approved pharmacologic, gene, RNA, cell, or genome-editing therapy corrects PEX16 deficiency. Care is individualized and multidisciplinary:

- physical and occupational therapy, stretching, orthotics, mobility devices, and fall prevention;
- speech/swallow therapy and augmentative communication;
- standard antispasticity, dystonia, tremor, pain, and antiseizure therapies when clinically indicated;
- audiologic aids or cochlear-implant assessment and low-vision/ophthalmic care;
- nutrition assessment, treatment of fat-soluble-vitamin deficiency, and gastrostomy when safe oral intake is inadequate;
- surveillance and standard treatment of liver disease, adrenal insufficiency, renal oxalate stones, reduced bone density/fracture, and dental enamel disease. (braverman2016peroxisomebiogenesisdisorders pages 20-20, braverman2016peroxisomebiogenesisdisorders pages 4-6, braverman2016peroxisomebiogenesisdisorders pages 10-12)

These are expert ZSD recommendations rather than therapies proven in PEX16-specific trials. No reliable response percentages or PEX16 pharmacogenomic associations exist. Suggested NCIT intervention concepts include supportive care, physical therapy, occupational therapy, speech-language therapy, hearing aid, cochlear implantation, gastrostomy, anticonvulsant therapy, and genetic counseling; exact NCIT codes should be validated in the target terminology release.

AAV9 gene augmentation for ZSD-associated visual disease has been discussed preclinically, but no human PEX16 gene-replacement trial or efficacy result was identified. (braverman2016peroxisomebiogenesisdisorders pages 10-12)

### Trials and recent real-world research

- **NCT01668186**, recruiting natural-history study, targets **244** participants and follows clinical, imaging, biochemical, and genotype–phenotype outcomes annually; estimated completion is 2031. It is relevant to PEX16 but has not reported PEX16-specific outcomes. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT01668186) (NCT01668186 chunk 1)
- **NCT06190626**, recruiting prospective ZSD-retinopathy study, targets **30** participants. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06190626) (NCT06190626 chunk 2)
- Completed aggregate-PBD studies include betaine (**NCT01838941**, phase 3, 12 participants) and hydroxychloroquine/pexophagy reduction (**NCT03856866**, phase 2, 3 participants). The retrieved records did not supply efficacy results or show PEX16-specific enrollment; neither should be described as an established treatment.
- The 2023 ophthalmic natural-history/scoping review was published August 2, 2023 (**PMID 37541626**; DOI: [10.1016/j.ophtha.2023.07.026](https://doi.org/10.1016/j.ophtha.2023.07.026)). It supports systematic retinal surveillance but is not PEX16-specific. (NCT01668186 chunk 2, NCT06190626 chunk 2)

## 13. Prevention

The inherited biochemical defect cannot be prevented by vaccination, lifestyle modification, or environmental avoidance.

- **Primary/reproductive prevention:** carrier testing, genetic counseling, preimplantation genetic testing, and prenatal diagnosis after familial variants are known.
- **Prenatal testing:** targeted variant analysis using chorionic-villus sampling or amniocentesis; biochemical prenatal testing may also be possible in specialist laboratories. (braverman2016peroxisomebiogenesisdisorders pages 4-6)
- **Secondary prevention:** cascade testing and early diagnosis of mildly affected relatives; newborn VLCFA screening alone is not sufficiently sensitive for all PEX16 cases.
- **Tertiary prevention:** early hearing/vision support, nutritional care, rehabilitation, vaccination according to routine schedules, fall/contracture prevention, and surveillance for adrenal, renal, hepatic, skeletal, and dental complications.

There is no PEX16-specific prophylactic medication.

## 14. Other species and natural disease

No well-established naturally occurring PEX16-deficiency syndrome in companion animals, livestock, or wildlife was identified, and there is no zoonotic transmission. Orthologues are conserved in **Mus musculus** (NCBI Taxon 10090), **Drosophila melanogaster** (7227), and other model species. Veterinary breed/VBO associations and natural-disease prevalence are unavailable.

## 15. Model organisms and advanced experimental developments

### Drosophila

Pex16-null flies have markedly reduced peroxisomal puncta, locomotor impairment, bang sensitivity, and shortened lifespan. In the 2024 humanized-fly preprint, null females and males lived on average **13.2 and 8.5 days**, versus approximately **49–51 days** in controls. Human reference PEX16 partially rescued lifespan to **26.2 and 23 days**; p.Phe332del rescued to **26.3 and 26.2 days**, whereas p.Arg176Ter did not meaningfully rescue. Human PEX16 also restored peroxisome number and nerve-fiber morphology. These data provide functional evidence for an allele-severity spectrum. (gomez2024distinguishingpexgene pages 16-21, gomez2024distinguishingpexgene pages 32-39)

Earlier fly studies demonstrated loss of punctate GFP-SKL localization, reduced Pex3 staining, increased C24:0–C30:0 species, decreased plasmalogen, locomotor dysfunction, and altered carbohydrate metabolism. Rescue constructs restored organelle markers, strongly linking the phenotype to Pex16 loss. (wangler2017peroxisomalbiogenesisis pages 3-6, wangler2017peroxisomalbiogenesisis pages 1-2)

### Mouse

In a 2024 hepatocyte-specific Pex16 knockout, hepatocyte peroxisomes were absent, hepatocytes proliferated, and liver mass increased. Basal serum triglycerides, free fatty acids, and cholesterol decreased, whereas bile acids increased. Unlike controls and adipocyte-specific knockouts, hepatocyte knockouts resisted high-fat-diet-induced obesity and hepatic steatosis. This is valuable tissue-specific mechanistic evidence but does not recapitulate the mild human neurologic phenotype. DOI: [10.3390/biomedicines12050988](https://doi.org/10.3390/biomedicines12050988), April 2024. (chen2024hepatocytespecificpex16abrogation pages 1-2)

### Cellular models and limitations

Patient-derived olfactory neurosphere cells reproduce reduced peroxisome density, increased organelle size, reduced catalase activity, and altered oxidative-stress handling. They are useful for variant validation and candidate-drug testing, but they do not reproduce whole-body pharmacology or decades-long tract degeneration. (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)

No validated PEX16 patient iPSC-derived organoid, single-cell atlas, spatial-transcriptomic study, or CRISPR therapeutic correction study was identified in the retrieved literature.

## Evidence interpretation and research gaps

The strongest PBD8B evidence comprises biallelic human genotypes with segregation, cellular peroxisome abnormalities, and conserved rescue in model organisms. The most important unresolved questions are the number and spectrum of living patients; variant-level penetrance; tissue-specific biochemical signatures when plasma VLCFAs are normal; longitudinal MRI, vision, hearing, and mobility trajectories; disease-specific quality of life; and whether early restoration of PEX16 can prevent rather than reverse neurologic injury.

Exact abstract quotations were not reproduced where the retrieved full-text evidence did not provide the original abstract wording. This avoids presenting reconstructed summaries as verbatim quotations. The key contemporary experimental conclusion is nevertheless quantitative: hypomorphic and null-like human PEX16 alleles separate in rescue assays, while the major current clinical conclusion is that **normal plasma VLCFAs cannot exclude mild PEX16 disease**. (braverman2016peroxisomebiogenesisdisorders pages 3-4, gomez2024distinguishingpexgene pages 16-21)

## Selected primary and authoritative references

1. Kumar KR et al. *Expanding the spectrum of PEX16 mutations and novel insights into disease mechanisms.* Molecular Genetics and Metabolism Reports. September 2018. DOI: [10.1016/j.ymgmr.2018.07.003](https://doi.org/10.1016/j.ymgmr.2018.07.003). (kumar2018expandingthespectrum pages 2-3, kumar2018expandingthespectrum pages 1-2)
2. Cheung A et al. *Clinical, neuroradiological, and molecular characterization of patients with atypical Zellweger spectrum disorder caused by PEX16 mutations: a case series.* Neurogenetics. Online February 2, 2022. **PMID 35106698**. DOI: [10.1007/s10048-022-00684-7](https://doi.org/10.1007/s10048-022-00684-7). (NCT01668186 chunk 2)
3. Braverman NE et al. *Peroxisome biogenesis disorders in the Zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines.* Molecular Genetics and Metabolism. March 2016. **PMID 26750748**. DOI: [10.1016/j.ymgme.2015.12.009](https://doi.org/10.1016/j.ymgme.2015.12.009). (braverman2016peroxisomebiogenesisdisorders pages 20-20, braverman2016peroxisomebiogenesisdisorders pages 3-4, braverman2016peroxisomebiogenesisdisorders pages 4-6)
4. Wangler MF et al. *Peroxisomal biogenesis is genetically and biochemically linked to carbohydrate metabolism in Drosophila and mouse.* PLOS Genetics. June 2017. DOI: [10.1371/journal.pgen.1006825](https://doi.org/10.1371/journal.pgen.1006825). (wangler2017peroxisomalbiogenesisis pages 2-3, wangler2017peroxisomalbiogenesisis pages 3-6, wangler2017peroxisomalbiogenesisis pages 1-2)
5. Gomez VA et al. *Distinguishing PEX gene variant severity for mild, severe, and atypical peroxisome biogenesis disorders in Drosophila.* bioRxiv. November 2024. DOI: [10.1101/2024.11.14.623590](https://doi.org/10.1101/2024.11.14.623590). Preprint at the time represented in the retrieved evidence. (gomez2024distinguishingpexgene pages 16-21, gomez2024distinguishingpexgene pages 32-39)
6. Chen X et al. *Hepatocyte-Specific PEX16 Abrogation in Mice Leads to Hepatocyte Proliferation, Alteration of Hepatic Lipid Metabolism, and Resistance to High-Fat Diet-Induced Hepatic Steatosis and Obesity.* Biomedicines. April 2024. DOI: [10.3390/biomedicines12050988](https://doi.org/10.3390/biomedicines12050988). (chen2024hepatocytespecificpex16abrogation pages 1-2)

References

1. (kumar2018expandingthespectrum pages 2-3): Kishore R. Kumar, Gautam Wali, Ryan L. Davis, Amali C. Mallawaarachchi, Elizabeth E. Palmer, Velimir Gayevskiy, Andre E. Minoche, David Veivers, Marcel E. Dinger, Alan Mackay-Sim, Mark J. Cowley, and Carolyn M. Sue. Expanding the spectrum of pex16 mutations and novel insights into disease mechanisms. Sep 2018. URL: https://doi.org/10.1016/j.ymgmr.2018.07.003, doi:10.1016/j.ymgmr.2018.07.003. This article has 16 citations.

2. (kumar2018expandingthespectrum pages 1-2): Kishore R. Kumar, Gautam Wali, Ryan L. Davis, Amali C. Mallawaarachchi, Elizabeth E. Palmer, Velimir Gayevskiy, Andre E. Minoche, David Veivers, Marcel E. Dinger, Alan Mackay-Sim, Mark J. Cowley, and Carolyn M. Sue. Expanding the spectrum of pex16 mutations and novel insights into disease mechanisms. Sep 2018. URL: https://doi.org/10.1016/j.ymgmr.2018.07.003, doi:10.1016/j.ymgmr.2018.07.003. This article has 16 citations.

3. (rayana2026polyunsaturatedfattyacid pages 14-15): Naga Pradeep Rayana, Navdeep Gogna, Mark P. Krebs, Gayle B. Collin, Jürgen K. Naggert, and Patsy M. Nishina. Polyunsaturated fatty acid metabolism in the retinal pigment epithelium and its association with outer retinal disease. Mammalian Genome, May 2026. URL: https://doi.org/10.1007/s00335-026-10239-y, doi:10.1007/s00335-026-10239-y. This article has 0 citations and is from a peer-reviewed journal.

4. (NCT01668186 chunk 1): Nancy Braverman. Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD). McGill University Health Centre/Research Institute of the McGill University Health Centre. 2012. ClinicalTrials.gov Identifier: NCT01668186

5. (braverman2016peroxisomebiogenesisdisorders pages 3-4): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 353 citations and is from a peer-reviewed journal.

6. (wangler2017peroxisomalbiogenesisis pages 3-6): Michael F. Wangler, Yu-Hsin Chao, Vafa Bayat, Nikolaos Giagtzoglou, Abhijit Babaji Shinde, Nagireddy Putluri, Cristian Coarfa, Taraka Donti, Brett H. Graham, Joseph E. Faust, James A. McNew, Ann Moser, Marco Sardiello, Myriam Baes, and Hugo J. Bellen. Peroxisomal biogenesis is genetically and biochemically linked to carbohydrate metabolism in drosophila and mouse. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006825, doi:10.1371/journal.pgen.1006825. This article has 58 citations and is from a domain leading peer-reviewed journal.

7. (chen2024hepatocytespecificpex16abrogation pages 1-2): Xue Chen, Long Wang, Krista L. Denning, Anna Mazur, Yujuan Xu, Kesheng Wang, Logan M. Lawrence, Xiaodong Wang, and Yongke Lu. Hepatocyte-specific pex16 abrogation in mice leads to hepatocyte proliferation, alteration of hepatic lipid metabolism, and resistance to high-fat diet (hfd)-induced hepatic steatosis and obesity. Biomedicines, 12(5):988, Apr 2024. URL: https://doi.org/10.3390/biomedicines12050988, doi:10.3390/biomedicines12050988. This article has 11 citations.

8. (braverman2016peroxisomebiogenesisdisorders pages 4-6): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 353 citations and is from a peer-reviewed journal.

9. (braverman2016peroxisomebiogenesisdisorders pages 10-12): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 353 citations and is from a peer-reviewed journal.

10. (gomez2024distinguishingpexgene pages 16-21): Vanessa A. Gomez, Oguz Kanca, Sharayu V. Jangam, Saurabh Srivastav, Jonathan C. Andrews, and Michael F. Wangler. Distinguishing pex gene variant severity for mild, severe, and atypical peroxisome biogenesis disorders in drosophila. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.14.623590, doi:10.1101/2024.11.14.623590. This article has 1 citations.

11. (gomez2024distinguishingpexgene pages 32-39): Vanessa A. Gomez, Oguz Kanca, Sharayu V. Jangam, Saurabh Srivastav, Jonathan C. Andrews, and Michael F. Wangler. Distinguishing pex gene variant severity for mild, severe, and atypical peroxisome biogenesis disorders in drosophila. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.14.623590, doi:10.1101/2024.11.14.623590. This article has 1 citations.

12. (NCT06190626 chunk 2): Nancy Braverman. Longitudinal Prospective Natural History Study of Retinopathy in Zellweger Spectrum Disorder. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2023. ClinicalTrials.gov Identifier: NCT06190626

13. (braverman2016peroxisomebiogenesisdisorders pages 1-3): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 353 citations and is from a peer-reviewed journal.

14. (OpenTargets Search: peroxisome biogenesis disorder 8B-PEX16): Open Targets Query (peroxisome biogenesis disorder 8B-PEX16, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

15. (NCT01668186 chunk 2): Nancy Braverman. Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD). McGill University Health Centre/Research Institute of the McGill University Health Centre. 2012. ClinicalTrials.gov Identifier: NCT01668186

16. (wangler2017peroxisomalbiogenesisis pages 1-2): Michael F. Wangler, Yu-Hsin Chao, Vafa Bayat, Nikolaos Giagtzoglou, Abhijit Babaji Shinde, Nagireddy Putluri, Cristian Coarfa, Taraka Donti, Brett H. Graham, Joseph E. Faust, James A. McNew, Ann Moser, Marco Sardiello, Myriam Baes, and Hugo J. Bellen. Peroxisomal biogenesis is genetically and biochemically linked to carbohydrate metabolism in drosophila and mouse. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006825, doi:10.1371/journal.pgen.1006825. This article has 58 citations and is from a domain leading peer-reviewed journal.

17. (braverman2016peroxisomebiogenesisdisorders pages 20-20): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 353 citations and is from a peer-reviewed journal.

18. (bose2020zellwegerspectrumdisorder pages 7-8): Mousumi Bose, David D. Cuthbertson, Marsha A. Fraser, Jean-Baptiste Roullet, K. Michael Gibson, Dana R. Schules, Kelly M. Gawron, Melissa B. Gamble, Kathryn M. Sacra, Melisa J. Lopez, and William B. Rizzo. Zellweger spectrum disorder: a cross-sectional study of symptom prevalence using input from family caregivers. Molecular Genetics and Metabolism Reports, 25:100694, Dec 2020. URL: https://doi.org/10.1016/j.ymgmr.2020.100694, doi:10.1016/j.ymgmr.2020.100694. This article has 4 citations.

19. (wangler2017peroxisomalbiogenesisis pages 2-3): Michael F. Wangler, Yu-Hsin Chao, Vafa Bayat, Nikolaos Giagtzoglou, Abhijit Babaji Shinde, Nagireddy Putluri, Cristian Coarfa, Taraka Donti, Brett H. Graham, Joseph E. Faust, James A. McNew, Ann Moser, Marco Sardiello, Myriam Baes, and Hugo J. Bellen. Peroxisomal biogenesis is genetically and biochemically linked to carbohydrate metabolism in drosophila and mouse. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006825, doi:10.1371/journal.pgen.1006825. This article has 58 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_8B-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 7 |
| Terms whose name was checked | 5 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013943` (3 mentions) - the report calls it "if available"; MONDO calls it **peroxisome biogenesis disorder 8B**
- `HP:0032312` (1 mention) - the report calls it "abnormal very-long-chain fatty-acid level"; HP calls it **Decreased circulating globulin concentration**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:000` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0040083` (obsolete Toe walking) (1 mention) - replaced by `HP:0030051`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15329` (1 mention) - the report calls it "supportive care"; NCIT calls it **Surgical Procedure**, and lists "Surgical" among its other names
- `HP:0003676` (1 mention) - the report calls it "progressive disorder"; HP calls it **Progressive**, and lists "Progressive disorder" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Taxon`, `ClinicalTrials.gov`.
