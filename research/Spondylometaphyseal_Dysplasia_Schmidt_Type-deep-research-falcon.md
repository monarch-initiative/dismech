---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:31:22.411515'
end_time: '2026-09-09T11:39:03.579127'
duration_seconds: 461.17
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Spondylometaphyseal dysplasia Algerian type (SMD-A), also called spondylometaphyseal
    dysplasia Schmidt type and SMD with severe genu valgum, OMIM 184253, ORPHA 93316
    - an autosomal dominant type II collagenopathy caused by heterozygous COL2A1 glycine
    substitutions, not Schmidt syndrome (autoimmune polyglandular syndrome type II)
    and not the TRPV4-related SMD Kozlowski type
  mondo_id: MONDO:0008478
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 8
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008478
    reported_labels:
    - if available
    ontology_label: spondylometaphyseal dysplasia, Schmidt type
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spondylometaphyseal_Dysplasia_Schmidt_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondylometaphyseal dysplasia Algerian type (SMD-A), also called spondylometaphyseal dysplasia Schmidt type and SMD with severe genu valgum, OMIM 184253, ORPHA 93316 - an autosomal dominant type II collagenopathy caused by heterozygous COL2A1 glycine substitutions, not Schmidt syndrome (autoimmune polyglandular syndrome type II) and not the TRPV4-related SMD Kozlowski type
- **MONDO ID:** MONDO:0008478 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondylometaphyseal dysplasia Algerian type (SMD-A), also called spondylometaphyseal dysplasia Schmidt type and SMD with severe genu valgum, OMIM 184253, ORPHA 93316 - an autosomal dominant type II collagenopathy caused by heterozygous COL2A1 glycine substitutions, not Schmidt syndrome (autoimmune polyglandular syndrome type II) and not the TRPV4-related SMD Kozlowski type** covering all of the
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
- **Disease Name:** Spondylometaphyseal dysplasia Algerian type (SMD-A), also called spondylometaphyseal dysplasia Schmidt type and SMD with severe genu valgum, OMIM 184253, ORPHA 93316 - an autosomal dominant type II collagenopathy caused by heterozygous COL2A1 glycine substitutions, not Schmidt syndrome (autoimmune polyglandular syndrome type II) and not the TRPV4-related SMD Kozlowski type
- **MONDO ID:** MONDO:0008478 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondylometaphyseal dysplasia Algerian type (SMD-A), also called spondylometaphyseal dysplasia Schmidt type and SMD with severe genu valgum, OMIM 184253, ORPHA 93316 - an autosomal dominant type II collagenopathy caused by heterozygous COL2A1 glycine substitutions, not Schmidt syndrome (autoimmune polyglandular syndrome type II) and not the TRPV4-related SMD Kozlowski type** covering all of the
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


# Spondylometaphyseal dysplasia, Algerian type (SMD-A): research report

## Executive summary

Spondylometaphyseal dysplasia, Algerian type (SMD-A) is an exceptionally rare, nonlethal, autosomal-dominant skeletal dysplasia and type II collagenopathy. Its characteristic combination is disproportionate short stature with a short trunk, severe bilateral genu valgum, moderate platyspondyly—especially posterior/dorsal vertebral flattening—short ilia with narrow greater sciatic notches, and generalized metaphyseal dysplasia of the long bones. The disorder was delineated in five members of an Algerian family in 1988; a phenotypically concordant 7-year-old Japanese boy reported in 2013 carried heterozygous **COL2A1** NM_001844.4:c.2582G>T, p.(Gly861Val), linking SMD-A to defective type II collagen. The disease literature remains limited to very small case reports, so prevalence, penetrance, phenotype frequencies, natural history, surgical outcomes, and life expectancy cannot be estimated reliably. (zhang2020integratedanalysisof pages 21-24, zhang2020integratedanalysisof pages 10-14)

The strongest evidence is summarized below.

| Evidence domain | Direct SMD-A finding | Evidence type/publication | Confidence and limitations |
|---|---|---|---|
| Original delineation | SMD-A was introduced after evaluation of five affected individuals from an Algerian family. | Human case series: Kozlowski et al., *Pediatric Radiology* (1988), DOI: [10.1007/BF02390399](https://doi.org/10.1007/BF02390399) (zhang2020integratedanalysisof pages 21-24) | **Moderate:** Foundational disease-specific evidence, but only five related cases; detailed individual-level data were unavailable in the retrieved text. |
| Defining phenotype | Core findings are short trunk and severe genu valgum, with moderate platyspondyly—especially dorsal vertebral flattening—short ilia, narrow greater sciatic notches, and generalized metaphyseal dysplasia of the long bones. | Disease-specific synthesis of the original phenotype: Zhang et al., *Clinical Genetics* (2020), DOI: [10.1111/cge.13680](https://doi.org/10.1111/cge.13680) (zhang2020integratedanalysisof pages 10-14) | **Moderate:** The clinicoradiographic pattern is characteristic, but frequencies, penetrance, and longitudinal progression cannot be estimated from the very small cohort. |
| Molecular etiology | A 7-year-old Japanese boy with an SMD-A-matching phenotype carried heterozygous **COL2A1** NM_001844.4:c.2582G>T, p.(Gly861Val), supporting classification as an autosomal-dominant type II collagenopathy. | Human molecular case report: Matsubayashi et al., *Molecular Syndromology* (2013), 4:148–151 (barathouari2016mutationupdatefor pages 7-8, zhang2020integratedanalysisof pages 10-14) | **Moderate:** Disease-specific genotype–phenotype evidence, but based on one molecularly characterized case; no SMD-A-specific functional assay was reported, and the 2020 review described the classification as supportive rather than definitive. |
| Overlapping phenotype context | Six patients with a related **COL2A1** phenotype shared disproportionate short stature, platyspondyly, shortened long bones, epiphyseal and hip dysplasia, metaphyseal dappling and corner-fracture lesions, and genu varum or valgum. Reported substitutions were Gly154Arg in two patients, Gly181Arg, Gly922Arg, Gly861Val, and Gly546Ser. | Human comparative case synthesis: Chen et al., *BMC Pediatrics* (2017), DOI: [10.1186/s12887-017-0930-9](https://doi.org/10.1186/s12887-017-0930-9) (chen2017recurrentc.g1636a(p.g546s) pages 3-5, chen2017recurrentc.g1636a(p.g546s) pages 5-6) | **Low for strict SMD-A assignment; moderate for phenotypic overlap:** The authors classified this pattern as an SEMD-Strudwick variant; corner-fracture and dappling findings should not automatically be equated with classic SMD-A. |
| Broader COL2A1 evidence | Across 663 probands, investigators catalogued 460 distinct **COL2A1** variants and 21 disorders; 488 of 663 variants (73.6%) were substitutions, 439 of 539 coding-region variants lay in the triple-helical domain, and 140 substitutions replaced glycine. | Aggregated literature and LOVD analysis: Zhang et al., *Clinical Genetics* (2020), DOI: [10.1111/cge.13680](https://doi.org/10.1111/cge.13680) (zhang2020integratedanalysisof pages 6-10, zhang2020integratedanalysisof pages 1-6) | **High for the broader type II collagenopathy spectrum, not SMD-A prevalence:** Database ascertainment and phenotype-label uncertainty limit genotype–phenotype inference; these statistics are not SMD-A-specific. |
| Glycine-substitution mechanism | Glycine substitutions in Gly-X-Y repeats commonly destabilize the collagen-II triple helix and are generally interpreted as dominant-negative structural variants; glycine replacement accounted for 142 of 415 (34%) catalogued variants. | Mutation review and database synthesis: Barat-Houari et al., *Human Mutation* (published online October 7, 2015; issue 2016), DOI: [10.1002/humu.22915](https://doi.org/10.1002/humu.22915) (barathouari2016mutationupdatefor pages 2-4, barathouari2016mutationupdatefor pages 1-2) | **High as a general collagen-II model; inferred for p.Gly861Val:** Variant position does not reliably predict phenotype, and genetic, epigenetic, or environmental modifiers remain possible. |
| Contemporary mechanistic model | A human isogenic iPSC-cartilage model of another dominant **COL2A1** glycine substitution, p.Gly1170Ser, showed slow procollagen-II folding and secretion with intracellular ER accumulation but no coupled unfolded-protein response. | Human in-vitro preprint, version posted March 9, 2024: Yammine et al., bioRxiv, DOI: [10.1101/2023.10.19.562780](https://doi.org/10.1101/2023.10.19.562780) (yammine2023erprocollagenstorage pages 1-5) | **Indirect and hypothesis-generating only:** This is a different variant and phenotype, and the cited version was not peer reviewed. It does not establish ER storage or absent UPR activation in p.Gly861Val SMD-A; reviews emphasize mutation-, collagen-, and cell-specific responses (bateman2022collagenmisfoldingmutations pages 14-15, bateman2022collagenmisfoldingmutations pages 1-2). |


*Table: Evidence tiers supporting the clinical definition and COL2A1 association of SMD-A, while distinguishing direct disease observations from overlapping phenotypes and indirect mechanistic models.*

## 1. Disease information

### Definition and classification

SMD-A is a Mendelian chondrodysplasia affecting vertebral bodies and long-bone metaphyses. It belongs to the **COL2A1/type II collagenopathy spectrum**, in which defective cartilage extracellular matrix impairs endochondral bone growth. The original publication was Kozlowski *et al.*, “A new type of spondylo-metaphyseal dysplasia—Algerian type,” *Pediatric Radiology*, published April 1988, DOI: https://doi.org/10.1007/BF02390399; it described five cases. Molecular support came from Matsubayashi *et al.*, “COL2A1 mutation in spondylometaphyseal dysplasia Algerian type,” *Molecular Syndromology* 4:148–151 (2013), DOI: https://doi.org/10.1159/000346644. (zhang2020integratedanalysisof pages 21-24, barathouari2016mutationupdatefor pages 7-8, zhang2020integratedanalysisof pages 10-14)

**Identifiers and names**

- OMIM phenotype: **184253**.
- Orphanet: **ORPHA:93316**.
- MONDO: **MONDO:0008478**, as supplied in the target specification; this should be revalidated against the current MONDO release before automated ingestion.
- Gene: **COL2A1**, OMIM **120140/108300** in historical literature; HGNC symbol COL2A1.
- Synonyms: *spondylometaphyseal dysplasia, Algerian type*; *SMD Algerian type*; *SMD-A*; *spondylometaphyseal dysplasia with severe genu valgum*; and historically *Schmidt type*.
- No disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence. Coding generally falls under broader osteochondrodysplasia/skeletal-dysplasia categories; local coding systems should not substitute “Schmidt syndrome.”

**Critical disambiguation:** this is not autoimmune polyglandular syndrome type II (“Schmidt syndrome”), and it is not **TRPV4**-related SMD Kozlowski type. It should also not be conflated automatically with **FN1**-related SMD corner-fracture/Sutcliffe type or COL2A1-related SEMD Strudwick type.

The evidence is principally **aggregated disease-level literature derived from individual pedigrees and case reports**, not EHR-scale or registry data. The 2020 COL2A1 synthesis reviewed 170 publications, 663 independent probands, 1,678 affected individuals, 460 distinct variants, and 21 COL2A1-associated disorders, but only one molecularly characterized case was assigned specifically to SMD-A. (zhang2020integratedanalysisof pages 10-14, zhang2020integratedanalysisof pages 1-6)

## 2. Etiology

### Causal factor

The demonstrated cause is a constitutional heterozygous missense alteration in **COL2A1**, specifically c.2582G>T, p.(Gly861Val), in the molecularly characterized Japanese case. This replaces an invariant glycine in the Gly-X-Y repeat of the collagen-II triple-helical domain. Type II procollagen is a homotrimer of three α1(II) chains and is the major fibrillar collagen of cartilage; after secretion and propeptide cleavage, molecules assemble into a cross-linked extracellular fibrillar network. (zhang2020integratedanalysisof pages 10-14, zhang2020integratedanalysisof pages 1-6)

Glycine substitutions are a major pathogenic class: a 2016 mutation review found them in 142/415 variants (34%), while a later dataset found 140 glycine substitutions among 488 substitutions and 439/539 coding-region variants in the triple-helical domain. Such substitutions generally act through a **dominant-negative structural mechanism**, destabilizing helix folding and/or fibril assembly rather than simple haploinsufficiency. (barathouari2016mutationupdatefor pages 2-4, barathouari2016mutationupdatefor pages 1-2, zhang2020integratedanalysisof pages 6-10)

### Risk, protective, and modifying factors

- **Genetic risk:** carrying a pathogenic heterozygous COL2A1 allele is the primary risk. An affected heterozygous individual ordinarily has a 50% transmission probability per conception.
- **Family history:** relevant because of dominant inheritance, although de novo COL2A1 variants occur elsewhere in the collagenopathy spectrum.
- **Modifiers:** none are validated for SMD-A. Broader COL2A1 studies show marked inter- and intrafamilial variability and suggest unidentified genetic, epigenetic, age-dependent, or environmental modifiers. This remains hypothesis-level evidence. (chen2017recurrentc.g1636a(p.g546s) pages 5-6, barathouari2016mutationupdatefor pages 5-6)
- **Environmental risk or protective factors:** none are known to cause or prevent SMD-A. Mechanical loading may influence symptoms and progression of deformity or secondary osteoarthritis, but it does not cause the germline disorder.
- **Gene–environment interaction:** not studied directly.
- **Protective alleles, diet, supplements, toxins, infections, occupational exposures, smoking, or alcohol effects:** no SMD-A-specific evidence.

## 3. Phenotypes

The cardinal phenotype is based on a handful of patients; therefore, “characteristic” does not mean that a population frequency is known.

| Phenotype | Characteristics | Suggested HPO term |
|---|---|---|
| Disproportionate short stature/short trunk | Pediatric developmental manifestation; chronic and likely lifelong | Short stature, **HP:0004322**; Disproportionate short stature; Short trunk |
| Severe genu valgum | Cardinal, usually bilateral lower-limb angular deformity; may impair gait and knee mechanics | Genu valgum, **HP:0002857** |
| Platyspondyly | Moderate, with characteristic dorsal/posterior vertebral flattening | Platyspondyly, **HP:0000926** |
| Generalized metaphyseal dysplasia | Long-bone metaphyseal irregularity/remodeling defect | Metaphyseal dysplasia, **HP:0000944** |
| Short ilia and narrow greater sciatic notches | Pelvic radiographic hallmark | Short ilium; Abnormality of the greater sciatic notch |
| Short-trunk skeletal dysplasia | Combined axial and appendicular growth disturbance | Abnormality of the vertebral column; Abnormality of long-bone morphology |
| Possible myopia/hearing loss in overlapping COL2A1 cases | Not established as cardinal or frequent in strict SMD-A | Myopia, **HP:0000545**; Sensorineural hearing impairment, **HP:0000407** |

The 2020 review describes SMD-A as presenting with “short trunk, severe genu valgum,” and the radiographic hallmarks listed above. The 2013 molecular case was diagnosed at age seven, supporting childhood recognition. (zhang2020integratedanalysisof pages 10-14)

A related six-patient COL2A1 series with metaphyseal “dappling” and “corner-fracture” lesions reported disproportionate short stature, platyspondyly, short long bones, femoral-head/neck and hip dysplasia, and genu varum/valgum in all six tabulated patients. However, those authors classified the phenotype as an SEMD-Strudwick variant; these frequencies must **not** be imported as SMD-A frequencies. (chen2017recurrentc.g1636a(p.g546s) pages 3-5, chen2017recurrentc.g1636a(p.g546s) pages 5-6)

**Quality of life:** no SMD-A-specific EQ-5D, SF-36, PROMIS, pain, mobility, educational, or employment study exists in the retrieved literature. Severe knee malalignment, short stature, gait disturbance, pain, reduced mobility, and later degenerative joint disease are plausible functional burdens, but quantitative estimates are unavailable.

## 4. Genetic and molecular information

- **Gene:** COL2A1, encoding collagen α1(II); 54 coding exons were described in the 2020 analysis.
- **Disease-associated variant:** NM_001844.4:c.2582G>T, p.(Gly861Val), heterozygous missense; germline/constitutional in the reported child. (zhang2020integratedanalysisof pages 10-14)
- **Protein domain:** triple-helical Gly-X-Y repeat.
- **Functional class:** inferred dominant-negative structural allele. No p.Gly861Val-specific secretion, thermal-stability, fibrillogenesis, cartilage histology, or animal functional assay was retrieved.
- **ACMG/AMP status:** the human phenotype, invariant glycine substitution, dominant mechanism, and rarity support pathogenicity, but an up-to-date ClinVar assertion and criterion-level ACMG classification were not available in the retrieved documents and should be checked directly before database deposition.
- **Population frequency:** no allele count was available from gnomAD, TOPMed, ExAC, or 1000 Genomes in the retrieved evidence. A causal ultra-rare dominant skeletal-dysplasia allele is expected to be absent or exceptionally rare, but this must not be recorded as a measured frequency without a current database query.
- **Somatic variants:** not etiologic. Somatic and germline mosaicism occur elsewhere in COL2A1 disease, but neither was demonstrated in SMD-A. (barathouari2016mutationupdatefor pages 5-6, barathouari2016mutationupdatefor pages 6-7)
- **Modifier genes/epigenetics/chromosomal abnormalities:** none established. SMD-A is not known to result from aneuploidy, translocation, repeat expansion, mitochondrial mutation, or a recurrent copy-number abnormality.

The broader genotype–phenotype relationship is weak. The 2020 abstract states: “a well-defined genotype-phenotype correlation has not been established,” and the 2017 report similarly notes that identical COL2A1 mutations can produce different metaphyseal phenotypes. (chen2017recurrentc.g1636a(p.g546s) pages 1-3, zhang2020integratedanalysisof pages 1-6)

## 5. Environmental information

SMD-A is not an infectious, toxic, nutritional, radiation-induced, occupational, or lifestyle disease. No pathogen, toxin, pollutant, dietary deficiency, smoking exposure, alcohol exposure, or medication has been shown to initiate it. Exercise, body weight, and joint loading could modify pain or mechanical complications but are downstream management considerations, not etiologic factors. No vaccine or anti-infective intervention is relevant beyond routine preventive care.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous **COL2A1 c.2582G>T** lesion **leads to** p.Gly861Val substitution at an obligatory glycine in the α1(II) triple helix. (zhang2020integratedanalysisof pages 10-14)
2. Incorporation of mutant α1(II) chains into homotrimeric procollagen **is inferred to lead to** delayed or abnormal triple-helix folding and reduced molecular stability; this has not been demonstrated directly for p.Gly861Val. (barathouari2016mutationupdatefor pages 2-4, barathouari2016mutationupdatefor pages 1-2)
3. Abnormal procollagen-II **is inferred to result in** one or both of two branches: **(A)** defective secretion/ER retention and proteostasis disturbance; **(B)** secretion of structurally abnormal collagen that disrupts extracellular fibrillogenesis. Branch B has stronger general support for dominant glycine substitutions, but neither branch has been tested in SMD-A cartilage. (bateman2022collagenmisfoldingmutations pages 14-15, bateman2022collagenmisfoldingmutations pages 1-2)
4. Qualitatively or structurally defective collagen-II matrix **leads to** impaired cartilage tensile architecture, growth-plate organization, and chondrocyte differentiation/signaling during endochondral ossification. Broader COL2A1 studies report sparse matrix, irregular/short collagen fibrils, and altered hypertrophic differentiation markers. (zhang2020integratedanalysisof pages 14-18)
5. Growth-plate dysfunction **results in** generalized metaphyseal dysplasia and abnormal longitudinal/remodeling growth of long bones.
6. Abnormal endochondral growth at vertebral and pelvic sites **results in** platyspondyly, short trunk, short ilia, and narrow sciatic notches.
7. Disordered growth and load transmission across the lower extremities **result in** severe genu valgum and likely gait limitation, with a plausible downstream risk of pain and early degenerative joint disease.

**Important expert caveat:** ER stress must not be asserted as proven. A 2022 authoritative review concluded that evidence for a canonical cytotoxic unfolded-protein response in collagen types other than collagen X is incomplete and mutation- and cell-type-specific. It states that “while it is tempting to implicate UPR activation,” the evidence is mixed. (bateman2022collagenmisfoldingmutations pages 14-15, bateman2022collagenmisfoldingmutations pages 1-2)

A 2024 human iPSC-cartilage preprint involving a different variant, p.Gly1170Ser, found that mutant procollagen-II was slow to fold and secrete and accumulated intracellularly, but “this accumulation is not recognized by the unfolded protein response.” This is an important contemporary model of collagen-II proteostasis, not direct SMD-A evidence. (yammine2023erprocollagenstorage pages 1-5)

**Suggested annotations:** GO: collagen fibril organization; extracellular-matrix organization; cartilage development; chondrocyte differentiation; endochondral ossification; skeletal-system development; protein folding in ER; response to ER stress. Cell types: growth-plate chondrocyte, proliferative chondrocyte, prehypertrophic chondrocyte, hypertrophic chondrocyte, articular chondrocyte, and osteoblast. Cellular components: collagen-containing extracellular matrix, collagen trimer, endoplasmic-reticulum lumen, Golgi apparatus, and extracellular fibril.

No SMD-A-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics study was identified.

## 7. Anatomical structures affected

**Primary structures:** vertebral bodies, ilia/pelvis, long-bone metaphyses, growth plates, and knee alignment. The dominant tissue is hyaline cartilage—especially growth-plate cartilage—and its collagen-II extracellular matrix. Type II collagen is also present in articular cartilage, intervertebral discs, and vitreous, but ocular disease is not established as a defining SMD-A feature. (zhang2020integratedanalysisof pages 1-6)

Suggested UBERON labels include vertebral body, vertebral column, ilium, greater sciatic notch, femur, tibia, humerus, long-bone metaphysis, epiphyseal growth plate, articular cartilage, knee joint, and intervertebral disc. Suggested GO cellular components include collagen-containing extracellular matrix, collagen type-II trimer, ER lumen, and collagen fibril. Genu valgum is expected to be bilateral; no characteristic unilateral or asymmetric distribution is established.

## 8. Temporal development

SMD-A is congenital in genetic origin, with skeletal manifestations becoming clinically/radiographically evident during growth. The molecularly confirmed case was recognized at seven years. The course is chronic and lifelong rather than episodic or remitting. Deformity may become more apparent as growth and weight-bearing proceed, but no prospective natural-history cohort defines progression rate, stages, or critical intervention windows. (zhang2020integratedanalysisof pages 10-14)

The practical period of greatest vulnerability is childhood growth, when angular deformity may progress and growth-modulation surgery—if indicated—remains possible. This is orthopedic inference, not a measured SMD-A treatment effect. There is no spontaneous or pharmacologic remission.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant.
- **Recurrence:** 50% per pregnancy for an affected heterozygous parent, assuming ordinary Mendelian segregation.
- **Penetrance:** not quantified; apparently high in the original family, but the sample is too small to claim complete penetrance.
- **Expressivity:** likely variable across COL2A1 disease, but strict SMD-A variability is poorly measured.
- **Anticipation:** no evidence.
- **Founder effect:** the original Algerian pedigree does not by itself prove a founder allele. No founder haplotype is established.
- **Consanguinity:** not etiologically important for a dominant disorder.
- **Carrier frequency:** unknown and not meaningfully estimable.
- **Sex ratio:** unknown; no sex bias can be inferred from a few cases.
- **Prevalence/incidence:** no population estimate. It should be described as **ultra-rare**, not assigned a numerical prevalence.
- **Geography:** first reported in Algeria, followed by a molecularly concordant Japanese case; therefore, it is not known to be geographically restricted. (zhang2020integratedanalysisof pages 21-24, zhang2020integratedanalysisof pages 10-14)

## 10. Diagnostics

### Clinical and imaging diagnosis

Initial evaluation should combine pedigree, growth proportions, limb alignment, gait, joint range of motion, and a skeletal survey. The key radiographic constellation is severe genu valgum plus moderate dorsal platyspondyly, generalized long-bone metaphyseal dysplasia, short ilia, and narrow greater sciatic notches. Detailed clinical and radiographic assessment remains essential because COL2A1 phenotypes overlap extensively. (zhang2020integratedanalysisof pages 10-14, zhang2020integratedanalysisof pages 1-6)

Recommended real-world assessments include standing long-leg radiographs for mechanical-axis deviation; spine and pelvis radiographs; targeted cervical-spine imaging before anesthesia or if instability/neurologic symptoms are suspected; and MRI when cartilage, spinal cord, or joint complications require clarification. There is no diagnostic serum enzyme, metabolite, inflammatory marker, biopsy signature, electrophysiologic test, or liquid-biopsy biomarker.

### Genetic testing

1. Use a skeletal-dysplasia/type II collagenopathy multigene panel including **COL2A1**, **TRPV4**, **FN1**, and phenotype-directed differential genes; ensure coding exons and splice junctions are covered.
2. If the phenotype is classic, sequence and deletion/duplication analysis of COL2A1 is reasonable.
3. Confirm candidate variants by an orthogonal method and test parents/affected relatives for segregation.
4. WES or WGS is useful when panel testing is negative or phenotype overlap is substantial. A 2017 COL2A1 family illustrates successful WES followed by Sanger confirmation and segregation testing. (chen2017recurrentc.g1636a(p.g546s) pages 3-5)
5. RNA analysis may clarify suspected splice variants. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion assays are not first-line tests for classic SMD-A.

### Differential diagnosis

- **TRPV4-related SMD Kozlowski type:** distinguish genetically and by its own radiographic spectrum.
- **FN1-related SMD corner-fracture/Sutcliffe type:** corner-fracture-like metaphyseal lesions with relative epiphyseal sparing; COL2A1 cases can phenotypically overlap. (zhang2020integratedanalysisof pages 10-14)
- **COL2A1 SEMD Strudwick type:** dappled metaphyses, scoliosis, pectus carinatum, disproportionate short stature; overlap is substantial. (zhang2020integratedanalysisof pages 10-14)
- **SEDC, Kniest dysplasia, and other type II collagenopathies:** assess epiphyseal disease, ocular/hearing features, cleft palate, joint enlargement, and molecular findings.
- **Metaphyseal dysplasia and other genu-valgum skeletal dysplasias:** distinguish by vertebral/pelvic pattern and gene testing.
- **Autoimmune Schmidt syndrome:** unrelated endocrine-autoimmune condition, not a skeletal dysplasia.

No universally accepted SMD-A diagnostic criteria, newborn screening, or population screening program exists. Cascade testing is appropriate after identifying a familial pathogenic variant.

## 11. Outcome and prognosis

SMD-A is considered nonlethal, but no survival curve, mortality rate, or disease-specific life-expectancy estimate exists. Available reports do not establish cardiopulmonary, renal, hepatic, neurologic, or immune-system failure. Expected morbidity centers on short stature, progressive lower-limb malalignment, gait impairment, joint pain, restricted mobility, secondary osteoarthritis, and possible need for corrective orthopedic procedures. These complications are biologically and clinically plausible but lack SMD-A-specific rates.

No validated prognostic biomarker or prediction model exists. Potential clinical prognostic factors include baseline mechanical-axis deviation, remaining growth, hip/spine involvement, pain, joint degeneration, and functional status. Molecular position alone is not a reliable severity predictor because COL2A1 genotype–phenotype correlation is weak. (chen2017recurrentc.g1636a(p.g546s) pages 5-6, barathouari2016mutationupdatefor pages 5-6)

## 12. Treatment

There is **no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, or SMD-A-specific clinical trial** in the retrieved evidence. No response-rate or adverse-event series exists.

Current care is multidisciplinary and supportive:

- pediatric skeletal-dysplasia/genetics follow-up;
- pediatric orthopedic surveillance of genu valgum, hips, spine, gait, and mechanical axis;
- physical therapy emphasizing safe mobility, muscle strength, balance, and preservation of range of motion;
- occupational therapy and school/work accommodations where required;
- weight management and low-impact activity to reduce excessive joint load without restricting healthy participation;
- standard age-appropriate analgesia for pain, individualized to comorbidity and age;
- hearing and ophthalmologic assessment at baseline because other COL2A1 disorders can involve these organs, although their frequency in strict SMD-A is unknown;
- corrective surgery—guided growth/hemiepiphysiodesis during growth or osteotomy for established deformity—when progressive malalignment, pain, gait dysfunction, or joint overload warrants it. SMD-A-specific outcome data are absent.

Suggested NCIT intervention labels include Genetic Counseling; Physical Therapy; Occupational Therapy; Pain Management; Hemiepiphysiodesis; Corrective Osteotomy; and Orthopedic Surgery. Exact NCIT codes should be resolved against the current ontology release.

The 2024 iPSC-cartilage work provides a platform for future testing of collagen folding, quality-control, and secretion therapies, but it studied another COL2A1 allele and is not a clinical implementation. (yammine2023erprocollagenstorage pages 1-5)

## 13. Prevention

Primary prevention by lifestyle change, vaccination, or medication is not possible for a germline dominant disorder. Secondary/tertiary prevention includes early molecular diagnosis, growth-period orthopedic surveillance, timely management of angular deformity, preservation of mobility, and monitoring for joint degeneration.

After molecular confirmation, genetic counseling should cover dominant transmission, variable expression, cascade testing, prenatal diagnosis, and preimplantation genetic testing for the known familial allele. Broader COL2A1 guidance supports antenatal or preimplantation testing and presymptomatic testing of at-risk relatives once the causal variant is identified. (barathouari2016mutationupdatefor pages 5-6)

Population newborn screening and universal carrier screening are not justified because the condition is ultra-rare, dominant, and lacks an established newborn-screening intervention. Germline mosaicism cannot be excluded absolutely after an apparently de novo case, although it has not been documented for SMD-A.

## 14. Other species and natural disease

No naturally occurring animal disease specifically homologous to human SMD-A or carrying orthologous p.Gly861Val was identified. COL2A1 is evolutionarily conserved across vertebrates and collagen-II disorders occur in experimental and naturally occurring contexts, but these should not be labeled SMD-A without variant and phenotype concordance. There is no infectious transmission, zoonotic potential, or cross-species contagion.

Relevant comparative taxa include *Mus musculus* (NCBI Taxon 10090) and *Danio rerio* (7955), both useful for endochondral-bone and cartilage biology. No breed-specific VBO annotation is justified from current evidence.

## 15. Model organisms and experimental systems

No SMD-A-specific knock-in mouse, zebrafish, organoid, or patient-derived iPSC line was identified. Broader COL2A1-mutant mice show dilated rough ER/Golgi, fewer and thinner matrix fibrils, poor matrix organization, and altered growth-plate differentiation, but heterozygous mice may under-recapitulate human disease whereas homozygous animals may be excessively severe. (yammine2023erprocollagenstorage pages 1-5, zhang2020integratedanalysisof pages 14-18)

The most relevant recent development is isogenic human iPSC-derived cartilage. In the p.Gly1170Ser model, RNA sequencing, interactomics, microscopy, and biochemical assays demonstrated slow folding/secretion and ER storage without canonical UPR activation. Its strengths are human genotype, chondrocyte context, expandable tissue-like matrix, and suitability for drug screening; its limitations are a different allele/phenotype and, for the cited March 9, 2024 version, preprint status. (yammine2023erprocollagenstorage pages 1-5)

A high-value future SMD-A model would introduce c.2582G>T into an isogenic human iPSC line, differentiate it into growth-plate and articular chondrocytes, and measure triple-helix folding, secretion, collagen-II fibril architecture, matrix mechanics, ER proteostasis, chondrocyte-zone differentiation, and response to allele-selective silencing or proteostasis modulators.

## Evidence limitations and knowledge-base recommendation

The disease assignment is credible but rests on **five original familial cases plus one molecularly characterized phenocopy/concordant case**. The most defensible knowledge-base entry is therefore: “autosomal-dominant COL2A1-related spondylometaphyseal dysplasia characterized by severe genu valgum,” with p.Gly861Val recorded as disease-associated and its dominant-negative mechanism marked **inferred**, not experimentally demonstrated. Frequencies, penetrance, natural history, prognosis, treatment outcomes, environmental modifiers, and molecular profiling should be entered as **unknown**, rather than extrapolated numerically from other type II collagenopathies. (zhang2020integratedanalysisof pages 21-24, zhang2020integratedanalysisof pages 10-14)

### Key source dates and URLs

- Kozlowski K, *et al.* *Pediatric Radiology*. April 1988. DOI: https://doi.org/10.1007/BF02390399.
- Matsubayashi S, *et al.* *Molecular Syndromology*. 2013;4:148–151. DOI: https://doi.org/10.1159/000346644.
- Barat-Houari M, *et al.* Published online October 7, 2015; *Human Mutation* 2016;37:7–15. DOI: https://doi.org/10.1002/humu.22915. (barathouari2016mutationupdatefor pages 1-2)
- Chen J, *et al.* *BMC Pediatrics*. July 2017;17:175. DOI: https://doi.org/10.1186/s12887-017-0930-9. (chen2017recurrentc.g1636a(p.g546s) pages 1-3)
- Zhang B, *et al.* *Clinical Genetics*. 2020;97:383–395. DOI: https://doi.org/10.1111/cge.13680. (zhang2020integratedanalysisof pages 1-6)
- Bateman JF, *et al.* *Connective Tissue Research*. May 2022;63:210–227. DOI: https://doi.org/10.1080/03008207.2022.2036735. (bateman2022collagenmisfoldingmutations pages 1-2)
- Yammine KM, *et al.* bioRxiv version posted March 9, 2024. DOI: https://doi.org/10.1101/2023.10.19.562780. (yammine2023erprocollagenstorage pages 1-5)

References

1. (zhang2020integratedanalysisof pages 21-24): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 63 citations and is from a peer-reviewed journal.

2. (zhang2020integratedanalysisof pages 10-14): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 63 citations and is from a peer-reviewed journal.

3. (barathouari2016mutationupdatefor pages 7-8): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 179 citations and is from a domain leading peer-reviewed journal.

4. (chen2017recurrentc.g1636a(p.g546s) pages 3-5): Jing Chen, Xiaomin Ma, Yulin Zhou, Guimei Li, and Qiwei Guo. Recurrent c.g1636a (p.g546s) mutation of col2a1 in a chinese family with skeletal dysplasia and different metaphyseal changes: a case report. BMC Pediatrics, Jul 2017. URL: https://doi.org/10.1186/s12887-017-0930-9, doi:10.1186/s12887-017-0930-9. This article has 6 citations and is from a peer-reviewed journal.

5. (chen2017recurrentc.g1636a(p.g546s) pages 5-6): Jing Chen, Xiaomin Ma, Yulin Zhou, Guimei Li, and Qiwei Guo. Recurrent c.g1636a (p.g546s) mutation of col2a1 in a chinese family with skeletal dysplasia and different metaphyseal changes: a case report. BMC Pediatrics, Jul 2017. URL: https://doi.org/10.1186/s12887-017-0930-9, doi:10.1186/s12887-017-0930-9. This article has 6 citations and is from a peer-reviewed journal.

6. (zhang2020integratedanalysisof pages 6-10): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 63 citations and is from a peer-reviewed journal.

7. (zhang2020integratedanalysisof pages 1-6): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 63 citations and is from a peer-reviewed journal.

8. (barathouari2016mutationupdatefor pages 2-4): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 179 citations and is from a domain leading peer-reviewed journal.

9. (barathouari2016mutationupdatefor pages 1-2): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 179 citations and is from a domain leading peer-reviewed journal.

10. (yammine2023erprocollagenstorage pages 1-5): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

11. (bateman2022collagenmisfoldingmutations pages 14-15): John F. Bateman, Matthew D. Shoulders, and Shireen R. Lamandé. Collagen misfolding mutations: the contribution of the unfolded protein response to the molecular pathology. Connective Tissue Research, 63:210-227, Feb 2022. URL: https://doi.org/10.1080/03008207.2022.2036735, doi:10.1080/03008207.2022.2036735. This article has 38 citations and is from a peer-reviewed journal.

12. (bateman2022collagenmisfoldingmutations pages 1-2): John F. Bateman, Matthew D. Shoulders, and Shireen R. Lamandé. Collagen misfolding mutations: the contribution of the unfolded protein response to the molecular pathology. Connective Tissue Research, 63:210-227, Feb 2022. URL: https://doi.org/10.1080/03008207.2022.2036735, doi:10.1080/03008207.2022.2036735. This article has 38 citations and is from a peer-reviewed journal.

13. (barathouari2016mutationupdatefor pages 5-6): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 179 citations and is from a domain leading peer-reviewed journal.

14. (barathouari2016mutationupdatefor pages 6-7): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 179 citations and is from a domain leading peer-reviewed journal.

15. (chen2017recurrentc.g1636a(p.g546s) pages 1-3): Jing Chen, Xiaomin Ma, Yulin Zhou, Guimei Li, and Qiwei Guo. Recurrent c.g1636a (p.g546s) mutation of col2a1 in a chinese family with skeletal dysplasia and different metaphyseal changes: a case report. BMC Pediatrics, Jul 2017. URL: https://doi.org/10.1186/s12887-017-0930-9, doi:10.1186/s12887-017-0930-9. This article has 6 citations and is from a peer-reviewed journal.

16. (zhang2020integratedanalysisof pages 14-18): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 63 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Spondylometaphyseal_Dysplasia_Schmidt_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 8 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008478` (3 mentions) - the report calls it "if available"; MONDO calls it **spondylometaphyseal dysplasia, Schmidt type**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
