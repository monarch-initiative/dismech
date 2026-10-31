---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T14:54:54.855469'
end_time: '2026-10-15T14:59:15.264627'
duration_seconds: 260.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Interstitial Lung Disease 1
  mondo_id: MONDO:0030608
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 55
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 52
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: DOID:0060941
    reported_labels:
    - DOID
    ontology_label: interstitial lung disease 1
  - term_id: CL:0002063
    reported_labels:
    - Primary SFTPA1-producing and injured cell
    - Alveolar epithelial type II cell
    ontology_label: pulmonary alveolar type 2 cell
  - term_id: CL:0002062
    reported_labels:
    - Secondary impairment through architectural destruction
    ontology_label: pulmonary alveolar type 1 cell
  - term_id: CL:0000583
    reported_labels:
    - Surfactant clearance, innate immunity and inflammation
    ontology_label: alveolar macrophage
  - term_id: CL:0000186
    reported_labels:
    - Contractile collagen-producing effector
    ontology_label: myofibroblast cell
  obsolete_terms:
  - term_id: GO:0045045
    ontology_label: obsolete secretory pathway
    replaced_by: GO:0032940
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Interstitial Lung Disease 1
- **MONDO ID:** MONDO:0030608 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Interstitial Lung Disease 1** covering all of the
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

# Interstitial Lung Disease 1  
## Disease-characteristics research report

**Disease:** Interstitial lung disease 1 (**ILD1**)  
**MONDO:** **MONDO:0030608**  
**Defining gene:** **SFTPA1**  
**OMIM phenotype:** **619611**  
**Inheritance:** Usually autosomal dominant with incomplete, age-dependent penetrance; one autosomal-recessive family is established  
**Evidence base reviewed through:** **15 October 2026**

> **Scope note.** ILD1 is the specific Mendelian surfactant-protein-A1 disorder caused by pathogenic germline variants in **SFTPA1**. It should not be conflated with the broad clinical category “interstitial lung disease,” with SFTPA2-associated ILD2, or with all familial pulmonary fibrosis.

---

## Executive summary

Interstitial lung disease 1 is an exceptionally rare, predominantly lung-limited surfactant disorder whose clinical spectrum ranges from fatal infantile fibrosing interstitial pneumonia to adult-onset idiopathic interstitial pneumonia, usual interstitial pneumonia/idiopathic pulmonary fibrosis, respiratory failure, and lung adenocarcinoma. The phenotype can be absent in young carriers and is highly variable even within a family. OMIM maps ILD1 to **SFTPA1 at 10q22.3** and recognizes both autosomal-dominant and autosomal-recessive inheritance. [1][31]

Disease-associated missense variants cluster in exon 6, which encodes the C-terminal carbohydrate-recognition domain of surfactant protein A1. The best-established variants are **p.Val178Met, p.Tyr208His, p.Trp211Arg, and p.Val225Met**. Functional studies consistently find preserved intracellular protein production but markedly reduced or absent extracellular secretion. In the recessive p.Tyr208His model, retained mutant protein activates an **IRE1α–JNK–RIPK3–MLKL necroptosis pathway** in alveolar type II cells, leading to epithelial loss, inflammation, collagen deposition, impaired gas exchange, and progressive fibrosis. Influenza A infection markedly accelerates this process in knock-in mice. [53][78][83]

No therapy is approved specifically for SFTPA1-associated ILD. Current practice extrapolates from IPF and progressive pulmonary fibrosis: avoidance of inhalational injury, vaccination, pulmonary rehabilitation, oxygen when indicated, antifibrotic therapy according to the radiologic/clinical phenotype, early lung-transplant referral, and unusually careful surveillance for lung cancer. In a 2023 transplant cohort, 20 adults with surfactant-gene ILD—including five with SFTPA1 variants—had a median post-transplant survival of **8.6 years**, and none of the five SFTPA1 recipients died during reported follow-up. [91][92]

---

# 1. Disease information

## 1.1 Definition

ILD1 is a monogenic disorder caused by germline pathogenic variants in **SFTPA1**, encoding surfactant protein A1, a collectin produced mainly by alveolar epithelial type II cells. Its defining pathology is progressive remodeling and fibrosis of the distal lung, variably expressed as idiopathic interstitial pneumonia, nonspecific interstitial pneumonia, usual interstitial pneumonia, or clinical IPF. Dyspnea, restrictive physiology, ground-glass or reticular abnormalities, reduced gas transfer, clubbing, respiratory failure, and lung adenocarcinoma may occur. [31]

The original molecular report described phenotypes “ranging from severe respiratory insufficiency occurring early in life to the association of lung fibrosis and cancer in adult patients.” The same study showed that p.Trp211Arg impairs SP-A1 secretion and alters SP-A distribution in alveolar epithelium (Nathan et al., **15 April 2016**, PMID **26792177**, DOI: [10.1093/hmg/ddw014](https://doi.org/10.1093/hmg/ddw014)). [46][47]

## 1.2 Identifiers and terminology

| Resource | Identifier/name | Qualification |
|---|---|---|
| MONDO | **MONDO:0030608 — interstitial lung disease 1** | Preferred disease ontology identifier |
| OMIM phenotype | **#619611 — Interstitial lung disease 1; ILD1** | Gene–phenotype relation to SFTPA1 |
| OMIM gene | **\*178630 — SFTPA1** | Surfactant protein A1 |
| DOID | **DOID:0060941** | Interstitial lung disease 1 |
| MedGen | **C5562021**, UID 1794231 | ILD1; associated gene SFTPA1 |
| Orphanet cross-reference | **ORPHA:2032** | Orphanet’s broader “idiopathic pulmonary fibrosis” entry, not a perfectly specific ILD1 concept |
| ICD-10 | **J84.1** | Other interstitial pulmonary diseases with fibrosis; phenotype-level code, not gene-specific |
| ICD-11 | **CB03.4** | Idiopathic pulmonary fibrosis; phenotype-level code |
| MeSH | **D054990 — Idiopathic Pulmonary Fibrosis** | Includes familial idiopathic pulmonary fibrosis as a narrower concept |
| MeSH broader term | **D011658 — Pulmonary Fibrosis** | Useful when phenotype is not formally IPF |
| UMLS/MedGen synonym | **ILD1; Interstitial lung disease 1** | Specific disease synonyms |

OMIM explicitly records SFTPA1-associated ILD1 as autosomal dominant or autosomal recessive. Orphanet/ICD/MeSH cross-references generally point to the broader IPF phenotype and therefore have lower specificity than MONDO:0030608 or OMIM:619611. [166][168][173][176]

**Common names:** ILD1; SFTPA1-associated interstitial lung disease; SP-A1–related interstitial lung disease; SFTPA1-related pulmonary fibrosis; familial idiopathic interstitial pneumonia due to SFTPA1; familial IPF due to SFTPA1.

## 1.3 Information provenance

The evidence is chiefly **aggregated disease-level evidence** from:

- multigenerational pedigrees;
- rare-disease sequencing cohorts;
- patient HRCT, pathology and transplant cohorts;
- ClinVar/OMIM/MedGen;
- in-vitro protein-expression studies;
- genetically engineered mice.

It is not primarily an EHR-defined disease. The foundational literature comprises small, deeply phenotyped families rather than population-scale clinical records.

---

# 2. Etiology

## 2.1 Primary causal factor

The primary cause is a **germline pathogenic SFTPA1 variant**. Most reported disease is associated with a heterozygous missense variant and dominant inheritance; homozygous p.Tyr208His produced severe recessive disease in one consanguineous Japanese family. [16][76]

SFTPA1 encodes a calcium-dependent C-type lectin/collectin involved in:

- pulmonary-surfactant organization and homeostasis;
- binding of phospholipids;
- pathogen recognition and opsonization;
- regulation of alveolar macrophages and pulmonary inflammation.

Expression is strongly enriched in **alveolar type II cells**. [153][154]

## 2.2 Genetic risk factors

| Factor | Evidence and interpretation |
|---|---|
| Heterozygous pathogenic SFTPA1 variant | Principal cause of dominant ILD1; penetrance is incomplete and age dependent |
| Biallelic pathogenic SFTPA1 variant | Established for p.Tyr208His; associated with earlier, severe progressive IPF |
| Variant location in CRD | All variants in the major functional series occurred in exon 6 encoding the carbohydrate-recognition domain |
| Family history of ILD/IPF | Strong indication for testing; 11/14 probands in one SP-A cohort had a first-degree ILD history |
| Personal/family lung cancer | Particularly important for SFTPA1/SFTPA2 disorders |
| Age | Risk rises with age, although infantile disease is possible |
| Other familial pulmonary-fibrosis genes | TERT, TERC, RTEL1, PARN, SFTPA2, SFTPC, ABCA3 and others are differential causes, not proven ILD1 modifiers |

No reproducible ILD1-specific modifier gene has yet been established.

## 2.3 Environmental and acquired risk modifiers

Evidence is suggestive rather than sufficient to calculate exposure-specific relative risks.

- Reported carriers had exposures to **tobacco, silica, occupational dust, birds, barge work, and cannabis**, while other affected carriers had no recognized exposure.
- Cigarette smoke and fibrogenic dust plausibly increase alveolar epithelial stress but are **not required** for disease.
- Respiratory infection may accelerate disease: influenza A caused striking worsening in Sftpa1^Y208H/Y208H^ mice without increasing viral titers or delaying clearance. [78]
- Aging is a major biological cofactor in the knock-in model; fibrosis, hypoxemia, and death emerged progressively with age.

## 2.4 Protective factors

No ILD1-specific genetic or environmental protective factor is validated.

Reasonable risk-reduction measures include:

- never smoking and avoiding secondhand smoke;
- respiratory protection against silica, metal, wood and other fibrogenic dusts;
- minimizing avian/mold antigen exposure if sensitization or hypersensitivity is suspected;
- influenza, pneumococcal, COVID-19 and age-appropriate vaccination;
- prompt treatment of respiratory infection;
- avoidance of unnecessary pneumotoxic drugs.

These measures reduce additional lung injury but have not been shown to prevent disease in genetically susceptible carriers.

## 2.5 Gene–environment interaction

The strongest experimental interaction is:

**SFTPA1 p.Tyr208His → latent epithelial vulnerability → influenza A exposure → amplified IRE1α/JNK/RIPK3 signaling → accelerated alveolar type II-cell necroptosis and fibrosis.**

In the human p.Trp211Arg family, marked variability among relatives exposed to tobacco or occupational environments led the authors to propose environmental contributions, but causality could not be separated from age-dependent penetrance and other genetic modifiers. [47]

---

# 3. Phenotypes

Frequencies below are based on very small ascertainment-biased cohorts. The most detailed mixed SFTPA1/SFTPA2 cohort contained 28 carriers, so these figures are informative but not ILD1 population estimates.

| Phenotype | Type, onset and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Interstitial lung disease | Clinical/radiologic disease; infancy through late adulthood; usually chronic progressive | Defining feature in symptomatic carriers | **HP:0006530 Abnormal pulmonary interstitial morphology** |
| Pulmonary fibrosis | Imaging/pathologic manifestation; progressive, variable severity | Core phenotype; listed for SFTPA1 | **HP:0002206 Pulmonary fibrosis** |
| Idiopathic pulmonary fibrosis/UIP | Clinical/pathologic subtype, predominantly adult | Seen in dominant and recessive families | HP:0002206; consider disease-level MONDO annotation |
| Dyspnea | Symptom; exertional initially, potentially at rest in advanced disease | Present in the recessive family and expected in progressive ILD | **HP:0002094 Dyspnea** |
| Chronic cough | Symptom; often dry | Typical fibrotic-ILD symptom, but not quantified specifically in ILD1 | **HP:0012735 Cough** |
| Restrictive ventilatory defect | Functional sign; progressive | Characteristic of fibrotic ILD; individual ILD1 values sparsely reported | **HP:0002091 Restrictive ventilatory defect** |
| Reduced diffusing capacity | Physiologic abnormality | Likely common in clinically manifest fibrosis; frequency unavailable | **HP:0045051 Reduced pulmonary diffusing capacity** |
| Hypoxemia | Laboratory/physiologic abnormality; advanced disease | Demonstrated in the mouse model and clinically expected with respiratory failure | **HP:0012418 Hypoxemia** |
| Ground-glass opacity | HRCT sign | 7/10 centrally reviewed SFTPA1/SFTPA2 probands, 70% | **HP:0025179 Ground-glass opacification** |
| Reticulation/interlobular septal thickening | HRCT sign | Reported across patients | **HP:0030878 Interstitial pulmonary abnormality** |
| Honeycombing | HRCT/pathology sign; advanced fibrosis | Reported but not universal | **HP:0025180 Honeycomb lung** |
| Bronchiectasis/traction bronchiectasis | Imaging manifestation | Reported in the SP-A cohort | **HP:0002110 Bronchiectasis** |
| Digital clubbing | Physical sign | Included in the ILD1 clinical definition; no reliable percentage | **HP:0001217 Clubbing** |
| Respiratory insufficiency/failure | Severe clinical manifestation | Fatal at nine months in one p.Trp211Arg infant; severe in advanced adults | **HP:0002878 Respiratory failure** |
| Recurrent bronchitis/infection | Symptom/complication | Seen in some carriers; SP-A has innate immune function | **HP:0002837 Recurrent respiratory infections** |
| Lung adenocarcinoma | Neoplastic complication | Strongly enriched in SFTPA1/SFTPA2 families | **HP:0030358 Lung adenocarcinoma** |
| Acute exacerbation | Complication | Documented cause of death in the broader SP-A cohort | **HP:0033678 Acute exacerbation of interstitial lung disease** |
| Asymptomatic carrier state | Clinical status | Seven of 28 SFTPA1/SFTPA2 carriers were asymptomatic; some had subclinical CT/PFT abnormalities | **HP:0000001 All** plus explicit “asymptomatic carrier” qualifier |

The 2020 SP-A cohort reported the following exact abstract statement:

> “Among the 28 SFTPA1 or SFTPA2 mutation carriers, the mean age at ILD onset was 45 years (range 0.6–65 years) and 48% underwent lung transplantation.”

Seven carriers were asymptomatic. Ground-glass opacity and fibrosis were each present in **7/10** centrally reviewed CT scans; UIP, indeterminate-UIP, NSIP, hypersensitivity-pneumonitis-like, and pleuroparenchymal fibroelastosis patterns all occurred. [74][83]

### Quality-of-life burden

No disease-specific EQ-5D, SF-36 or PROMIS study has been reported for ILD1. Expected burdens are those of progressive fibrotic ILD:

- exertional limitation and loss of employment capacity;
- oxygen dependence;
- fatigue and cough;
- anxiety related to progression, transplantation and cancer;
- major caregiver burden;
- genetic and reproductive uncertainty.

Pulmonary rehabilitation is used to improve exercise tolerance, symptoms and emotional well-being, although it does not reverse fibrosis. [129]

---

# 4. Genetic and molecular information

## 4.1 Gene annotation

| Attribute | Value |
|---|---|
| Gene | **SFTPA1** |
| Full name | Surfactant protein A1 |
| HGNC | **HGNC:10798** |
| NCBI Gene | **653509** |
| Ensembl | **ENSG00000122852** |
| OMIM gene | **178630** |
| UniProt | **P07714** |
| Cytogenetic location | **10q22.3** |
| Major disease transcript used in initial reports | **NM_005411.4** |
| Protein class | Secreted C-type lectin/collectin |
| Principal producing cell | Alveolar epithelial type II cell |
| Key domain | C-terminal carbohydrate-recognition domain |

## 4.2 Established and reported variants

| Variant | Origin/inheritance | Classification/evidence | Population frequency | Functional consequence |
|---|---|---|---|---|
| **NM_005411.4:c.532G>A, p.(Val178Met)**, rs1215316727 | Germline, heterozygous AD | Reported as likely pathogenic; segregated in familial IIP | 1/250,994 alleles in the 2020 gnomAD analysis | Preserved cellular production, abolished secretion |
| **c.622T>C, p.(Tyr208His)** | Germline, homozygous AR; parents heterozygous | Pathogenic based on segregation, absence from reference databases and strong functional/model evidence | Absent from 1000 Genomes and ExAC in the discovery report | Secretion failure; IRE1α/JNK/RIPK3/MLKL necroptosis |
| **NM_005411.4:c.631T>C, p.(Trp211Arg)** | Germline, heterozygous AD | Pathogenic; cosegregation, conservation and functional secretion defect | Not reported in 1000 Genomes, EVS or ExAC at discovery | Absent extracellular secretion; abnormal lung SP-A staining |
| **c.673G>A, p.(Val225Met)** | Germline, heterozygous AD | Likely pathogenic in the 2020 functional series | Not described in gnomAD in that report | Preserved production, abolished secretion |
| **c.655C>T, p.(Arg219Trp), rs4253527** | Germline polymorphism | Benign/common; was in cis with p.Trp211Arg but did not segregate independently with disease | Approximately 2–25% across older databases/populations | No detectable secretion defect; modifier role unproven |

Nathan et al. identified nine heterozygous p.Trp211Arg carriers in one extended pedigree. Disease onset ranged from **7 months to 69 years**, and unaffected carriers demonstrated incomplete penetrance (PMID **26792177**). [46][50]

Doubková et al. identified heterozygous **c.532G>A, p.Val178Met** by WES and Sanger confirmation in a three-generation Czech family (published **5 March 2019**, PMID **30854216**, DOI: [10.1038/s41439-019-0044-z](https://doi.org/10.1038/s41439-019-0044-z)). Its abstract states: “This variant encodes the substitution p.(Val178Met), localized within the carbohydrate recognition domain.” [61][64]

Takezaki et al. identified homozygous p.Tyr208His in three brothers from a consanguineous family (published **10 October 2019**, PMID **31601679**, DOI: [10.1084/jem.20182351](https://doi.org/10.1084/jem.20182351)). [78]

### Variant interpretation cautions

- A missense VUS in SFTPA1 is not sufficient for diagnosis.
- Useful pathogenic evidence includes extreme rarity, CRD location, segregation, preserved production with failed secretion, abnormal tissue localization, and phenotype compatibility.
- Testing should report transcript, genome build, read quality, allele balance, zygosity and ACMG/AMP criteria.
- All proven human variants are **germline**, not somatic driver mutations.

## 4.3 Molecular consequence and mode of action

For dominant alleles, the precise mechanism may combine:

1. reduced extracellular SP-A1 dosage;
2. intracellular retention/misfolding;
3. ER stress and epithelial toxicity;
4. possible interference with SP-A1/SP-A2 oligomer secretion.

A universal dominant-negative mechanism has **not** been directly proven. In p.Tyr208His experiments, mutant SP-A1 associated intracellularly with wild-type SP-A1 or SP-A2, but these complexes were scarcely secreted, supporting a potential retention effect. [78]

## 4.4 Modifier genes, epigenetics and chromosome abnormalities

- **Modifier genes:** none validated for ILD1.
- **Epigenetic signature:** no diagnostic ILD1 methylation or chromatin signature is established.
- **Structural variants/CNVs:** no recurrent ILD1-specific deletion, duplication, inversion or translocation has been demonstrated.
- **Somatic changes:** lung cancers arising in carriers may acquire conventional somatic cancer alterations, but these do not define ILD1.

---

# 5. Environmental information

| Category | Relevance to ILD1 |
|---|---|
| Tobacco smoke | Plausible accelerator and major independent lung-cancer risk; not necessary for disease |
| Silica, metal, cement, wood or mixed dust | Potential additive epithelial/fibrogenic injury; reported in individual carriers |
| Birds/avian antigen and mold | May complicate the radiologic differential with hypersensitivity pneumonitis |
| Air pollution | General fibrotic-lung-disease concern; no ILD1-specific effect size |
| Influenza A | Experimental accelerator of Sftpa1 p.Tyr208His fibrosis |
| Other viruses | No specific causal pathogen established |
| Diet/alcohol/exercise | No evidence that these cause ILD1; exercise training can preserve function but is not disease-preventive |
| Radiation/pneumotoxic drugs | Potential superimposed lung injury; no ILD1-specific susceptibility estimate |

ILD1 is **not infectious** and is not transmitted between people. Infection is a potential trigger or accelerator, not the Mendelian cause.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **A germline SFTPA1 missense lesion in the carbohydrate-recognition domain leads to structurally or electrostatically abnormal SP-A1.**

2. **Abnormal SP-A1 leads to failure of secretion from alveolar epithelial type II cells**, despite preserved intracellular protein synthesis.

3. **Failed secretion leads to reduced/abnormally distributed SP-A at the alveolar surface and intracellular retention in type II pneumocytes.**

4. **Intracellular retention leads to ER stress and IRE1α phosphorylation**; this step is demonstrated for p.Tyr208His in mice and inferred for several dominant variants.

5. **Phosphorylated IRE1α leads to JNK activation, which leads to increased RIPK3 expression.**

6. **RIPK3 activation leads to MLKL phosphorylation and membrane-disruptive necroptosis of alveolar epithelial type II cells.**

7. **Type II-cell necroptosis leads to loss of epithelial integrity and regenerative capacity, release of inflammatory/damage signals, macrophage recruitment and fibroblast activation.**

8. **Fibroblast/myofibroblast activation leads to excessive extracellular-matrix and collagen deposition, alveolar-wall thickening, architectural distortion and honeycombing.**

9. **Fibrotic remodeling leads to restrictive physiology, reduced diffusion capacity, hypoxemia, dyspnea and respiratory failure.**

10. **Chronic epithelial injury and compensatory proliferation lead—by an incompletely demonstrated branch—to increased lung-adenocarcinoma risk.**

11. **A respiratory viral insult such as influenza A can branch at steps 4–7 and leads to accelerated ER stress, necroptosis and fibrosis in the p.Tyr208His mouse model.**

## 6.2 Protein and surfactant biology

SP-A is a multimeric collectin. Its carbohydrate-recognition domain binds microbial and lipid ligands in a calcium-dependent manner. SP-A participates in tubular-myelin/surfactant organization and innate immune defense. SFTPA1 is strongly enriched in alveolar type II cells, whereas secreted protein is present at the alveolar air–liquid interface and in alveolar macrophages. [153][154]

Normal pulmonary surfactant is predominantly lipid, with a smaller protein fraction. SP-A is not the principal surface-tension-lowering component—that function depends strongly on phospholipids and hydrophobic surfactant proteins—but it organizes surfactant and regulates host defense.

## 6.3 Cellular processes

| Mechanism | Evidence level | Suggested ontology annotation |
|---|---|---|
| Defective protein secretion | Human cells, patient tissue | GO:0009306 protein secretion; GO:0046903 secretion |
| ER stress/unfolded-protein response | Mouse and cultured cells; inferred in dominant human disease | GO:0034976 response to endoplasmic reticulum stress; GO:0006986 response to unfolded protein |
| IRE1-mediated UPR | Mouse p.Tyr208His model | GO:0036498 IRE1-mediated unfolded protein response |
| JNK/MAPK signaling | Mouse intervention evidence | GO:0007254 JNK cascade; GO:0000165 MAPK cascade |
| RIPK3–MLKL necroptosis | Human tissue marker plus genetic mouse rescue | GO:0070266 necroptotic process |
| Type II pneumocyte death | Human and mouse | GO:0012501 programmed cell death |
| Inflammation and macrophage activation | Mouse/pathology evidence | GO:0006954 inflammatory response |
| Fibroblast activation/ECM deposition | Histology and mouse model | GO:0048144 fibroblast proliferation; GO:0030198 extracellular matrix organization |
| Collagen accumulation | Human fibrosis and mouse hydroxyproline/Col1a1 | GO:0032963 collagen metabolic process |
| Impaired gas exchange | Clinical downstream effect | GO:0007585 respiratory gaseous exchange |

### Relevant cell types

| Cell type | Role | Suggested CL term |
|---|---|---|
| Alveolar epithelial type II cell | Primary SFTPA1-producing and injured cell | **CL:0002063** |
| Alveolar epithelial type I cell | Secondary impairment through architectural destruction | **CL:0002062** |
| Alveolar macrophage | Surfactant clearance, innate immunity and inflammation | **CL:0000583** |
| Lung fibroblast | ECM synthesis and fibrosis | **CL:0000057 fibroblast** |
| Myofibroblast | Contractile collagen-producing effector | **CL:0000186** |
| Pulmonary epithelial progenitor/transitional cell | Likely repair response; ILD1-specific single-cell evidence limited | Appropriate epithelial progenitor term |

## 6.4 Experimental proof of the necroptosis pathway

The p.Tyr208His study supplied unusually strong causal evidence:

- increased phosphorylated MLKL in an affected human lung;
- increased IRE1α and JNK phosphorylation and Ripk3 expression in mutant mice;
- absence of increased active caspase-3, arguing against apoptosis as the primary death mechanism;
- **Ripk3 deletion** improved survival, oxygenation and fibrosis;
- **Mlkl deletion** protected against post-influenza fibrosis;
- JNK inhibitor **SP600125** reduced Ripk3 expression and fibrosis;
- IRE1α inhibitor **KIRA6** reduced JNK activation and fibrosis;
- forced Ripk3 expression partially reversed JNK-inhibitor benefit.

The authors’ abstract states that p.Tyr208His “promotes necroptosis of AEII cells through JNK-mediated up-regulation of Ripk3.” These are model-system findings, not an established human therapy. [78]

## 6.5 Immune involvement

SP-A binds carbohydrates on microorganisms and modulates phagocytosis, cytokine production and reactive-oxygen responses. Loss or mislocalization may therefore alter innate immunity. Sftpa1-null mice show reduced resistance to respiratory infection and exaggerated inflammatory responses to lipopolysaccharide. [158]

No evidence supports a primary autoimmune etiology. Rheumatoid arthritis occurred in a minority of the combined SFTPA1/SFTPA2 cohort, but causality is uncertain.

## 6.6 Molecular profiling and advanced technologies

- **Transcriptomics:** The p.Tyr208His model demonstrated increased **Ripk3** and **Col1a1** expression. A disease-specific human ILD1 transcriptomic signature has not been validated.
- **Proteomics:** No diagnostic plasma or BAL proteomic signature specific to ILD1.
- **Metabolomics/lipidomics:** No reproducible ILD1-specific signature. Altered surfactant lipid organization is biologically plausible but not adequately quantified.
- **Single-cell analysis:** SFTPA1 is a canonical alveolar type II-cell marker; general IPF atlases demonstrate epithelial-state heterogeneity, but no sufficiently powered single-cell ILD1 cohort exists.
- **Spatial transcriptomics:** No ILD1-specific spatial atlas.
- **CRISPR:** CRISPR-Cas9 insertion of p.Tyr208His reproduced fibrosis in mice, supporting variant causality.
- **Organoids/iPSC:** Potentially useful for individualized secretion and rescue studies, but not established diagnostic tools.

---

# 7. Anatomical structures affected

| Scale | Affected structure | Suggested ontology |
|---|---|---|
| Organ | Lung, usually bilateral and diffuse | **UBERON:0002048 lung** |
| Functional unit | Pulmonary alveolus | **UBERON:0002299 pulmonary alveolus** |
| Tissue | Alveolar epithelium | **UBERON:0003215 alveolar epithelium** |
| Tissue | Pulmonary interstitium/alveolar septum | **UBERON:0004893 lung interstitium** where supported |
| Distal airway | Respiratory bronchiole; may show bronchiolar metaplasia | UBERON respiratory bronchiole term |
| Pleura/subpleural lung | In UIP/PPFE patterns | UBERON pleura/subpleural region |
| Cell | Alveolar epithelial type II cell | **CL:0002063** |
| Subcellular | Endoplasmic reticulum | **GO:0005783** |
| Subcellular | ER lumen/secretory pathway | **GO:0005788**, GO:0045045 |
| Subcellular | Extracellular/alveolar surfactant layer | **GO:0005576 extracellular region** |
| Subcellular | Plasma membrane during MLKL necroptosis | **GO:0005886 plasma membrane** |

Disease is normally **bilateral**, not unilateral. Secondary structures include pulmonary vasculature and the right ventricle if chronic hypoxemia causes pulmonary hypertension/cor pulmonale. Lung cancer represents a secondary but major organ-level complication.

---

# 8. Temporal development

## 8.1 Onset

Onset is exceptionally broad:

- fatal infantile respiratory disease beginning at **7 months**;
- young-adult recessive IPF diagnosed at **24 and 27 years**;
- dominant disease commonly emerging in the fourth to sixth decades;
- latest reported onset in the original pedigree: **69 years**.

The combined SP-A cohort’s mean/median onset was approximately **45 years**, range **0.6–65 years**. [83]

## 8.2 Course and stages

| Stage | Typical manifestations |
|---|---|
| Genetically at risk/subclinical | No symptoms; normal or subtle HRCT/PFT findings |
| Early disease | Exertional dyspnea, cough, ground glass or fine reticulation; mild DLCO/FVC reduction |
| Established fibrotic ILD | Progressive reticulation, traction bronchiectasis, UIP/NSIP/indeterminate pattern |
| Advanced disease | Honeycombing, severe restriction, exertional/resting hypoxemia, oxygen dependence |
| End-stage | Respiratory failure, acute exacerbation, transplantation or death |
| Cancer branch | Lung adenocarcinoma may arise during fibrotic disease or occasionally dominate presentation |

The course is generally chronic and progressive but highly variable. Spontaneous durable remission is not documented. Treatment may slow progression but does not reverse established fibrosis.

The recessive family showed severe progression: two brothers diagnosed in their twenties died at **32 and 34**, while the third developed dyspnea at 40. [76]

## 8.3 Critical intervention windows

- Before irreversible FVC/DLCO decline and extensive honeycombing.
- Before severe frailty or pulmonary hypertension limits transplantation.
- At the first evidence of cancer, given the high cancer burden.
- During family-based presymptomatic surveillance, although the ideal CT interval remains unknown.

---

# 9. Inheritance, penetrance and population

## 9.1 Inheritance

- **Autosomal dominant:** most established families.
- **Autosomal recessive:** homozygous p.Tyr208His family.
- **Penetrance:** incomplete and age dependent.
- **Expressivity:** extremely variable.
- **Anticipation:** not demonstrated.
- **Germline mosaicism:** not reported, though theoretically possible.
- **Founder effect:** none established.
- **Consanguinity:** relevant to the recessive Japanese family.
- **Sex ratio:** no clear sex-limited effect; combined SP-A cohort male:female ratio was 0.65.

A 2025 penetrance analysis of combined SFTPA1/SFTPA2 pathogenic-variant carriers estimated **89.3% penetrance by age 80 for either ILD or lung cancer**. This is not a pure ILD1 estimate and should not be applied uncritically to every SFTPA1 variant. [84]

## 9.2 Epidemiology

No reliable prevalence, incidence or carrier-frequency estimate exists specifically for ILD1.

- It is likely **far below 1 per 100,000** and is represented by a small number of reported families.
- Surfactant-gene variants collectively account for approximately **1–3% of familial pulmonary-fibrosis families**, but this includes SFTPA1, SFTPA2, SFTPC, ABCA3 and NKX2-1. [115][117]
- No ethnicity is known to have consistently elevated ILD1 prevalence.
- Published pedigrees include European/French, Czech, Japanese and North African ancestry, indicating worldwide potential distribution.
- Reported variants are generally ultra-rare rather than common founder alleles.

---

# 10. Diagnostics

## 10.1 Clinical diagnostic approach

A diagnosis requires integration of:

1. phenotype compatible with fibrotic ILD;
2. detailed three-generation family history of ILD and lung cancer;
3. HRCT;
4. pulmonary function and oxygenation assessment;
5. exclusion of autoimmune, exposure-related, drug-induced and infectious ILD;
6. identification and classification of a germline SFTPA1 variant;
7. segregation/functional evidence where necessary.

### Recommended clinical tests

| Test | Purpose/findings |
|---|---|
| HRCT chest | Ground glass, reticulation, septal thickening, traction bronchiectasis, honeycombing, UIP/NSIP/PPFE patterns and lung nodules/cancer |
| Spirometry | FVC decline and restrictive physiology |
| Lung volumes | Reduced total lung capacity |
| DLCO | Often reduced before severe restriction |
| Rest/exercise oximetry | Detect hypoxemia |
| Six-minute walk | Functional capacity and exertional desaturation |
| Arterial blood gas | Advanced respiratory failure |
| Echocardiography | Screen for pulmonary hypertension/right-heart strain |
| Autoimmune serology | ANA, ENA, RF/anti-CCP, myositis testing as clinically indicated |
| Exposure assessment | Smoking, occupational dust, birds, mold and drugs |
| Bronchoscopy/BAL | Selected cases; exclude infection or alternative diagnoses |
| Surgical/cryobiopsy | Only if imaging/genetics do not establish diagnosis and result would alter care |
| Histology | UIP, fibrosing NSIP or indeterminate fibrosis; hyperplastic pneumocytes with abnormal intracellular/discontinuous SP-A staining |

Routine serum SP-A, SP-D, KL-6 or MMP-7 may reflect epithelial injury in some jurisdictions but are not validated as specific ILD1 diagnostics.

## 10.2 Genetic testing strategy

The **2023 ERS familial pulmonary fibrosis statement** recommends offering sequencing to patients with fibrotic ILD plus an affected first- or second-degree relative, a relative with a known pathogenic variant, suspected short-telomere syndrome, or idiopathic fibrosing ILD before age 50 (published **16 March 2023**, PMID **36549714**). Telomere- and surfactant-related genes should generally be included. [109][113]

Preferred workflow:

1. **Pre-test genetic counseling.**
2. Test an **affected proband first**.
3. Use a comprehensive familial pulmonary-fibrosis/childhood-ILD panel including at least:
   - SFTPA1, SFTPA2, SFTPB, SFTPC, ABCA3, NKX2-1;
   - TERT, TERC, RTEL1, PARN, DKC1, TINF2, NAF1, POT1 and other validated telomere genes;
   - additional syndromic ILD genes according to age/phenotype.
4. Include **CNV analysis**.
5. If panel testing is negative, consider **WES or WGS**, preferably family-based.
6. Confirm clinically important variants by an orthogonal method where appropriate.
7. Offer **targeted cascade testing** only after a familial pathogenic/likely pathogenic variant is identified.

### Utility by test type

| Test | ILD1 utility |
|---|---|
| Single-gene SFTPA1 sequencing | Appropriate when a familial SFTPA1 variant is known or phenotype is highly specific |
| Multigene panel | Preferred first-line assay in most familial ILD |
| WES | Useful for panel-negative Mendelian disease; may miss deep intronic and some structural variants |
| WGS | Broadest SNV, indel, intronic and structural-variant coverage; interpretation remains limiting |
| CMA | Low yield unless syndromic developmental findings suggest a CNV |
| Karyotype/FISH | Not routinely indicated |
| mtDNA testing | Not routinely indicated |
| Repeat-expansion testing | Not relevant to known ILD1 |
| RNA sequencing | Research/variant-resolution role; potentially demonstrates altered splicing |
| Protein secretion assay | Research-level functional evidence for a missense VUS |

## 10.3 Differential diagnosis

| Disorder | Distinguishing points |
|---|---|
| SFTPA2-associated ILD2 | Similar fibrosis/cancer phenotype; pathogenic variant in SFTPA2 |
| SFTPC-associated ILD | More frequent pediatric disease; pro-SP-C misfolding/processing abnormalities |
| ABCA3 deficiency | Usually recessive; neonatal respiratory distress or childhood ILD; lamellar-body defect |
| Telomere biology disorder | Premature greying, marrow failure, liver disease, short telomeres |
| Hermansky–Pudlak syndrome | Albinism and bleeding diathesis |
| Autoimmune ILD | Serologic/systemic rheumatologic features |
| Hypersensitivity pneumonitis | Relevant antigen exposure, air trapping/mosaic attenuation and BAL lymphocytosis |
| Occupational pneumoconiosis | Specific dust exposure and characteristic imaging/pathology |
| Sarcoidosis | Granulomas, nodal disease, extrapulmonary manifestations |
| Infection | Microbiologic evidence and acute/subacute course |
| Lymphangitic cancer | Nodular septal thickening and primary malignancy |
| Sporadic IPF | No pathogenic Mendelian variant or informative family history |

## 10.4 Screening of relatives

- A known familial pathogenic variant permits predictive testing in competent adults after counseling.
- Baseline history, examination, PFT/DLCO and HRCT should be considered for adult carriers.
- The ERS statement supports CT and PFT screening particularly for symptomatic first-degree relatives; evidence for intervals in asymptomatic relatives remains limited. [118]
- Testing minors for an adult-onset disorder is generally deferred, but pediatric testing may be justified when the family includes childhood disease or a biallelic risk.

---

# 11. Outcome and prognosis

## 11.1 Prognostic variability

Prognosis ranges from lifelong asymptomatic carriage to fatal infantile disease or rapidly progressive adult IPF. Poor prognostic factors likely include:

- biallelic pathogenic variants;
- early onset;
- rapid FVC/DLCO decline;
- UIP/honeycombing;
- oxygen requirement;
- acute exacerbation;
- pulmonary hypertension;
- lung cancer;
- inability to undergo transplantation.

No validated SFTPA1-specific prognostic calculator or biomarker exists.

## 11.2 Mortality and transplantation

In the combined 2020 SFTPA1/SFTPA2 cohort:

- **11/23 symptomatic patients (48%)** underwent lung transplantation;
- median transplant age was **51 years**;
- median diagnosis-to-transplant interval was **5 years**;
- **9/28 carriers (32%)** died;
- median death age was **51 years**.

These results are affected by referral and severity ascertainment. [83]

The 2023 French transplant study included 20 surfactant-gene patients—SFTPA1 n=5, SFTPA2 n=7, SFTPC n=8:

- diagnosis age: median **45 years**;
- transplant age: median **51 years**;
- median post-transplant survival: **8.6 years**;
- eight patients died overall;
- none of the five SFTPA1 recipients died during follow-up.

The investigators concluded that transplantation “may be a valid therapeutic option” and emphasized cancer screening before and after transplant (PMID **38020562**, published **20 November 2023**). [91][92]

## 11.3 Lung-cancer risk

The latest major 2024 cohort of 99 carriers of surfactant-related variants found:

- 82/99 (**82.8%**) had ILD at diagnosis;
- 13 had lung cancer;
- 27 (**32.9%**) underwent transplantation;
- 15-year cancer-free survival was **0.43** for SFTPA1/SFTPA2 carriers versus **0.85** for non-SFTPA surfactant-gene carriers;
- 28 (**28.3%**) died during follow-up.

The authors called for specific ILD and lung-cancer surveillance in this relatively young population (published **2 May 2024**). [97][100]

---

# 12. Treatment

There is no genotype-specific approved treatment and no randomized trial confined to ILD1. Management should occur in a multidisciplinary ILD/genetics center.

## 12.1 Clinical treatment framework

| Intervention | Role and evidence | Suggested NCIT annotation |
|---|---|---|
| **Pirfenidone** | Standard antifibrotic for an IPF phenotype; ILD1-specific response unknown | NCIT: Pirfenidone; antifibrotic agent |
| **Nintedanib** | Antifibrotic for IPF and conditionally recommended for progressive pulmonary fibrosis after standard management | NCIT: Nintedanib; tyrosine kinase inhibitor |
| Supplemental oxygen | Resting or exertional hypoxemia | NCIT: Oxygen Therapy |
| Pulmonary rehabilitation | Exercise capacity, dyspnea coping and quality of life | NCIT: Pulmonary Rehabilitation |
| Vaccination | Reduce respiratory-infection burden | NCIT: Vaccination |
| Smoking cessation | Reduces additive epithelial and cancer injury | NCIT: Smoking Cessation |
| Lung transplantation | Definitive organ-replacement treatment for eligible end-stage disease | NCIT: Lung Transplantation |
| Palliative/supportive care | Dyspnea, anxiety, cough and advance-care planning | NCIT: Palliative Care |
| Cancer-directed treatment | Stage- and genotype-specific surgery/systemic/radiation therapy | Appropriate NCIT oncologic intervention terms |

The 2022 ATS/ERS/JRS/ALAT guideline conditionally recommends **nintedanib for non-IPF progressive pulmonary fibrosis after failure of standard management** and calls for further pirfenidone research in non-IPF PPF. Both pirfenidone and nintedanib remain appropriate for a patient meeting standard IPF indications, irrespective of SFTPA1 status, absent contraindication. [121][122]

In the 2020 SP-A cohort, some SFTPA1 patients received pirfenidone, nintedanib or unspecified antifibrotic therapy, but the sample was too small for a genotype-specific response rate. [83]

### Adverse effects and monitoring

- **Nintedanib:** diarrhea, nausea, weight loss, elevated liver enzymes, bleeding risk; monitor liver function and interactions.
- **Pirfenidone:** nausea, anorexia, photosensitivity, rash and hepatotoxicity; monitor liver function and counsel regarding sun protection.
- **Oxygen:** fire risk and mobility burden.
- **Transplantation:** rejection, infection, malignancy, renal/metabolic toxicity and chronic allograft dysfunction.

## 12.2 Experimental and advanced therapeutics

No approved gene, cell, RNA or CRISPR therapy exists for ILD1.

Potential research strategies include:

- correcting SFTPA1 variants by genome/base editing;
- allele-specific suppression of toxic dominant transcripts;
- mRNA or protein replacement;
- pharmacologic enhancement of folding and secretion;
- IRE1α, JNK, RIPK3 or MLKL inhibition;
- alveolar type II-cell regenerative therapy.

IRE1α/JNK/necroptosis interventions are supported only by the p.Tyr208His mouse model. They should not currently be used clinically outside a properly regulated trial. [78]

A 2023 review of personalized therapies for surfactant disorders emphasized gene-, RNA-, protein- and cell-based possibilities but did not identify an approved SFTPA1-directed therapy. [104]

## 12.3 Treatment algorithm

1. Confirm ILD pattern and SFTPA1 pathogenicity.
2. Eliminate smoking and relevant inhalational exposures.
3. Vaccinate and treat infection promptly.
4. Monitor symptoms, FVC, DLCO, exercise oxygenation and HRCT.
5. If IPF criteria are met, offer approved antifibrotic therapy.
6. If non-IPF fibrotic ILD becomes progressive, consider nintedanib under PPF guidance.
7. Add pulmonary rehabilitation, oxygen and symptom-directed care.
8. Intensify lung-cancer surveillance.
9. Refer early for transplant evaluation when decline is evident.
10. Offer clinical-trial participation and family genetic counseling.

No clinically actionable pharmacogenomic variant is established for antifibrotic choice in ILD1.

---

# 13. Prevention

## 13.1 Primary prevention

The inherited variant cannot currently be prevented after conception. Risk-reduction includes:

- smoking avoidance/cessation;
- dust and aerosol controls;
- respiratory protection at work;
- vaccination;
- minimizing avoidable pneumotoxic exposures;
- reproductive counseling.

## 13.2 Secondary prevention

- cascade genetic testing after a familial variant is established;
- baseline and longitudinal PFT/DLCO;
- low-threshold HRCT for symptoms or physiologic changes;
- careful review of CT for nodules and early cancer;
- early antifibrotic and transplant assessment where indicated.

There is no proven population-wide screening program because ILD1 is ultra-rare.

## 13.3 Tertiary prevention

- oxygen and rehabilitation to limit disability;
- infection prevention;
- management of reflux, sleep-disordered breathing and cardiovascular comorbidity;
- surveillance for pulmonary hypertension and malignancy;
- early transplant referral;
- palliative-care integration.

## 13.4 Reproductive options

After identification of a familial pathogenic variant:

- natural conception with prenatal diagnosis;
- preimplantation genetic testing for monogenic disease;
- donor gametes;
- adoption;
- conception without testing.

For dominant disease, each child of a heterozygous carrier generally has a **50% transmission probability**, but disease severity cannot be predicted reliably. For two heterozygous carriers of a recessive pathogenic allele, the classic per-pregnancy risks are 25% affected, 50% carrier and 25% non-carrier.

---

# 14. Other species and natural disease

## 14.1 Comparative biology

| Species | Taxon | Ortholog/model relevance |
|---|---:|---|
| Human | **NCBI Taxon 9606** | Natural ILD1; SFTPA1 NCBI Gene 653509 |
| House mouse | **10090** | Sftpa1 knockout and p.Tyr208His knock-in models; MGI:109518 |
| Norway rat | **10116** | Sftpa1 ortholog; surfactant and collectin biology |
| Dog | **9615** | Conserved SP-A biology; no established natural SFTPA1-ILD1 counterpart |
| Cat | **9685** | No established natural orthologous ILD1 |
| Other mammals | Various | SP-A structure and innate immune function are evolutionarily conserved |

MGI reports that homozygous Sftpa1-null mice have impaired responses to lung stress, reduced resistance to pulmonary infection and enhanced LPS-induced inflammation. [158]

## 14.2 Naturally occurring veterinary disease

Idiopathic pulmonary fibrosis occurs naturally in animals—most notably West Highland White Terriers—but a direct causal **SFTPA1** ortholog variant equivalent to human ILD1 has not been established. Consequently:

- no VBO breed term should be assigned specifically to SFTPA1-related ILD1;
- natural canine/feline fibrosis is comparative pathology, not a confirmed orthologous Mendelian disease;
- ILD1 has no zoonotic potential and no cross-species transmission.

---

# 15. Model organisms and experimental systems

| Model | Construction | Phenotype recapitulation | Main application | Limitation |
|---|---|---|---|---|
| **Sftpa1 p.Tyr208His knock-in mouse** | Targeted knock-in and independently CRISPR-generated line | Age-dependent spontaneous fibrosis, collagen accumulation, type II-cell loss, hypoxemia and mortality | Causal pathway and therapeutic-target studies | Models one recessive allele, not all dominant ILD1 |
| Influenza-challenged p.Tyr208His mouse | H3N2 exposure at 20 weeks | Rapid fibrosis and ∼70% mortality by day 28 despite similar viral titers | Gene–environment interaction | Acute experimental infection differs from human exposure history |
| Ripk3- or Mlkl-deficient knock-in mouse | Genetic epistasis | Rescue of fibrosis, oxygenation and survival | Establishes necroptosis causality | Whole-animal deletion; cell-specific effects incompletely resolved |
| JNK/IRE1α inhibitor mouse | SP600125 or KIRA6 | Reduced signaling and fibrosis | Preclinical pathway targeting | Compounds are not established ILD1 treatments |
| Sftpa1 knockout mouse | Targeted null | Infection susceptibility, exaggerated inflammation; enhanced fibrosis after injury | SP-A immune/homeostatic function | Does not reproduce secretion-defective missense toxicity |
| HEK293T expression system | Wild-type/mutant constructs | Preserved production, absent secretion | Variant functional classification | Non-pulmonary transformed cell line |
| A549 alveolar-like cells | Co-expression of SP-A1/SP-A2 constructs | Intracellular complex formation but failed mutant-complex secretion | Oligomerization/retention studies | Cancer line, not primary type II cells |
| Patient lung tissue | Biopsy/explant | Hyperplastic pneumocytes, intracellular/discontinuous SP-A, fibrosis; pMLKL in p.Tyr208His case | Human validation | Very limited number of samples |
| Future iPSC/organoid model | Patient-derived or engineered | Not yet standardized | Precision rescue and drug screening | Maturity and surfactant physiology limitations |

The central model paper’s abstract directly reports:

> “Sftpa1 knock-in (Sftpa1-KI) mice that harbored the same mutation as patients spontaneously developed pulmonary fibrosis that was accelerated by influenza virus infection.”

It further reports that JNK inhibition ameliorated fibrosis and that RIPK3 overexpression worsened it (Takezaki et al., PMID **31601679**). [78]

Useful model resources are **MGI**, **IMSR/MMRRC**, **IMPC**, GEO/SRA for expression datasets, and patient-derived repositories maintained by ILD reference centers.

---

# Recent developments, 2023–2024

| Publication/date | Development | Relevance |
|---|---|---|
| Borie et al., ERS familial pulmonary fibrosis statement, **16 March 2023**, PMID **36549714** | Formal expert guidance on who should receive genetic sequencing and family screening | Supports surfactant-gene testing in familial and early-onset ILD [113] |
| Bermudez et al., **20 November 2023**, PMID **38020562** | First multicenter transplant-outcome study focused on adult surfactant-gene ILD | Median post-transplant survival 8.6 years; transplant is a valid option [91] |
| “Towards personalized therapies…,” **22 November 2023** | Review of gene/RNA/protein/cell strategies | Frames future disease-modifying approaches; none yet approved [104] |
| Luyapan et al., 2023 | Surfactant-pathway genetics and lung-cancer susceptibility research | Supports broader surfactant-pathway involvement; not a new monogenic ILD1 determinant [72] |
| Legendre/Nathan-group cohort, **2 May 2024** | Quantified cancer burden among surfactant-gene variant carriers | 15-year cancer-free survival 0.43 for SFTPA1/SFTPA2 vs 0.85 for other surfactant genes [97][100] |
| Rare genetic ILD pictorial review, **13 November 2024** | Updated radiologic synthesis | Reinforces adult-onset ILD and lung-cancer association for heterozygous SFTPA1/SFTPA2 variants [87] |

---

# Knowledge-base conclusions

1. **ILD1 is a specific SFTPA1-related Mendelian disorder**, not a generic synonym for all interstitial lung disease.
2. The most defensible core annotation is:  
   **germline SFTPA1 CRD missense variant → deficient SP-A1 secretion/retention in alveolar type II cells → epithelial stress and death → progressive fibrosis ± lung adenocarcinoma.**
3. **Autosomal dominant, incompletely penetrant disease is usual**, but severe **autosomal-recessive** disease is proven.
4. Phenotypic onset extends from **infancy to late adulthood**, with marked intrafamilial variability.
5. **Lung-cancer surveillance is a central management issue**, particularly for SFTPA1/SFTPA2 carriers.
6. No ILD1-specific drug exists; management uses standard IPF/PPF pathways, supportive care and timely lung transplantation.
7. The **p.Tyr208His knock-in mouse** is the strongest mechanistic model, but its necroptosis pathway should not automatically be generalized to every dominant SFTPA1 allele.
8. Disease-specific prevalence, variant-specific penetrance, treatment-response rates, validated biomarkers, epigenetic signatures and human single-cell datasets remain major evidence gaps.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0060941` (1 mention) - the report calls it "DOID"; DOID calls it **interstitial lung disease 1**
- `CL:0002063` (2 mentions) - the report calls it "Primary SFTPA1-producing and injured cell", "Alveolar epithelial type II cell"; CL calls it **pulmonary alveolar type 2 cell**
- `CL:0002062` (1 mention) - the report calls it "Secondary impairment through architectural destruction"; CL calls it **pulmonary alveolar type 1 cell**
- `CL:0000583` (1 mention) - the report calls it "Surfactant clearance, innate immunity and inflammation"; CL calls it **alveolar macrophage**
- `CL:0000186` (1 mention) - the report calls it "Contractile collagen-producing effector"; CL calls it **myofibroblast cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0045045` (obsolete secretory pathway) (1 mention) - replaced by `GO:0032940`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0002063` - called "Primary SFTPA1-producing and injured cell", "Alveolar epithelial type II cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`.