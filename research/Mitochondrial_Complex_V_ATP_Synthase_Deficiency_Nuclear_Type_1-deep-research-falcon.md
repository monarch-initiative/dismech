---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T03:44:40.801719'
end_time: '2026-09-16T03:58:50.427871'
duration_seconds: 849.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1
  mondo_id: MONDO:0011421
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 64
  verified: 59
  not_found: 0
  obsolete: 3
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011421
    reported_labels:
    - if available
    ontology_label: mitochondrial complex V (ATP synthase) deficiency, nuclear type
      1
  obsolete_terms:
  - term_id: GO:0000275
    ontology_label: obsolete mitochondrial proton-transporting ATP synthase complex,
      catalytic sector F(1)
    replaced_by: GO:0045259
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  - term_id: GO:0000276
    ontology_label: obsolete mitochondrial proton-transporting ATP synthase complex,
      coupling factor F(o)
    replaced_by: GO:0045259
  unresolvable_prefixes:
  - Taxon
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1
- **MONDO ID:** MONDO:0011421 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1** covering all of the
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
- **Disease Name:** Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1
- **MONDO ID:** MONDO:0011421 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1** covering all of the
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


# Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 1

## Executive summary and evidence limits

Mitochondrial complex V deficiency, nuclear type 1 is an exceptionally rare, severe, autosomal-recessive mitochondrial encephalopathy caused by biallelic loss of function of **ATPAF2**, historically named **ATP12**. ATPAF2 is not a structural ATP-synthase subunit; it is a mitochondrial assembly factor required to construct the catalytic F1 sector. The defining variant is homozygous **NM_?*:c.280T>A, p.(Trp94Arg)**, reported in one Moroccan girl. The 2024 systematic review still recognized only this single genetically confirmed patient. Consequently, phenotype “frequencies” below mean observations in **1/1 reported patient**, not stable population estimates. (tauchmannova2024variabilityofclinical pages 17-19)

The evidence base comprises one human case report, biochemical studies of patient tissues and fibroblasts, conserved yeast assembly-factor experiments, and disease-group reviews. No ATPAF2-specific cohort, registry, natural-history study, clinical trial, validated biomarker, treatment-response study, patient-derived multi-omics dataset, or mammalian disease model was identified.

| Domain | ATPAF2-specific finding | Evidence type/strength | Ontology-ready annotation |
|---|---|---|---|
| Disease scope | **Mitochondrial complex V (ATP synthase) deficiency, nuclear type 1** is exceptionally rare; only **one genetically confirmed patient** was retained in the 2024 systematic review. (tauchmannova2024variabilityofclinical pages 17-19) | Human case, **n=1**; very-low-certainty frequency and natural-history evidence | MONDO:0011421; mitochondrial respiratory-chain complex V deficiency |
| Gene and variant | The index patient was homozygous for **ATPAF2 c.280T>A (p.Trp94Arg; W94R)**. ATPAF2 was historically called **ATP12** and encodes an ATP-synthase F1 assembly factor. (tauchmannova2024variabilityofclinical pages 17-19, franco2020humanmitochondrialpathologies pages 17-19, meirleir2004respiratorychaincomplex pages 2-3) | Human molecular diagnosis plus mechanistic/model support; strong plausibility but one human genotype | ATPAF2; OMIM *608918; SO:0001583 missense_variant |
| Inheritance | The affected girl was born to healthy consanguineous Moroccan parents; both parents and one healthy sibling were heterozygous. The variant was absent from 50 Moroccan controls, supporting **autosomal-recessive germline inheritance**. (meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 2-3) | Familial segregation in one pedigree; moderate case-level support | HP:0000007 Autosomal recessive inheritance |
| Core phenotype | Congenital/early-infantile severe encephalopathy with hypertonia, poor sucking, profound developmental delay, seizures, failure to thrive, contractures/camptodactyly, hepatomegaly, hypoplastic kidneys, large mouth, prominent nasal bridge, micrognathia, and rocker-bottom feet. (meirleir2004respiratorychaincomplex pages 1-2) | Direct observation in one patient; frequencies cannot be generalized beyond **1/1** | HP:0001298 Encephalopathy; HP:0001276 Hypertonia; HP:0011968 Feeding difficulties; HP:0001263 Global developmental delay; HP:0001250 Seizure; HP:0001508 Failure to thrive; HP:0002803 Congenital contracture; HP:0012385 Camptodactyly; HP:0002240 Hepatomegaly; HP:0000089 Renal hypoplasia; HP:0000347 Micrognathia |
| Metabolic findings | Urine showed increased lactate, fumarate, methylglutaconic acid, and amino acids. CSF lactate was **2.9 mmol/L** (reference **<2**); plasma lactate fluctuated from **2.7–10 mmol/L** (reference **<2.2**). (meirleir2004respiratorychaincomplex pages 1-2) | Quantitative human laboratory evidence, n=1 | HP:0003128 Lactic acidosis; HP:0003535 3-methylglutaconic aciduria; HP:0003355 Aminoaciduria; CHEBI:24996 lactate |
| Complex V enzymology | Complex V activity was **30 nmol substrate/min/mg protein in liver** versus control median **87** (5th–95th percentile **35–108**), and **119** in skeletal muscle versus control median **209** (range **97–754**). Complex IV was also reduced in liver. (meirleir2004respiratorychaincomplex pages 2-3) | Direct patient-tissue biochemistry; strong evidence for a predominant complex V defect with tissue variability | GO:0000275 Mitochondrial proton-transporting ATP synthase complex; GO:0042776 Mitochondrial ATP synthesis coupled proton transport |
| Complex assembly | BN-PAGE/catalytic staining showed severe complex V reduction in liver and fibroblasts, with greater residual staining in skeletal muscle. Immunoblotting showed markedly reduced complex V α, β, d, and OSCP subunits; other OXPHOS complexes were comparatively preserved in principal assembly assays. (meirleir2004respiratorychaincomplex pages 2-3, meirleir2004respiratorychaincomplex pages 3-4) | Direct biochemical/protein evidence from tissues and fibroblasts; strong case-level functional support | GO:0033615 Mitochondrial proton-transporting ATP synthase complex assembly; GO:0005743 Mitochondrial inner membrane |
| MRI | MRI demonstrated marked cortical–subcortical atrophy, corpus-callosum dysgenesis with absent anterior genu and rostrum, and white-matter hypoplasia; basal ganglia and thalami became atrophic within months. (meirleir2004respiratorychaincomplex pages 1-2) | Serial human imaging, n=1; demonstrates progression | HP:0002120 Cerebral cortical atrophy; HP:0007370 Corpus callosum abnormality; HP:0002506 Diffuse cerebral atrophy; HP:0007007 Abnormality of the basal ganglia; UBERON:0000955 brain |
| Pathology | Muscle light microscopy showed increased lipid content without ragged-red fibers. (meirleir2004respiratorychaincomplex pages 2-3) | Direct biopsy evidence, n=1; absence of ragged-red fibers does not exclude mitochondrial disease | HP:0003555 Muscle fiber lipid accumulation; UBERON:0001134 skeletal muscle tissue; CL:0000187 muscle cell |
| Course and outcome | Severe developmental impairment, seizures, and growth failure progressed during infancy; the child died from an intercurrent infection at **14 months**. No disease-specific survival estimates exist. (meirleir2004respiratorychaincomplex pages 1-2) | Single-patient natural history; very low certainty for population prognosis | HP:0003593 Infantile onset; HP:0003676 Progressive; HP:0003811 Lethal in infancy |
| Molecular mechanism | ATPAF2/Atp12 binds the ATP-synthase F1 **α subunit**, prevents nonproductive aggregation, and supports formation of the catalytic **α3β3 hexamer**. W94R is inferred to impair this function, causing loss of assembled complex V and reduced ATP synthesis. (tauchmannova2024variabilityofclinical pages 1-3, meirleir2004respiratorychaincomplex pages 3-4, meirleir2004respiratorychaincomplex pages 4-5) | Protein-biogenesis studies plus concordant human biochemistry; direct W94R details partly model-derived | GO:0033615 ATP-synthase-complex assembly; GO:0051082 Unfolded-protein binding; GO:0006457 Protein folding; GO:0000276 Mitochondrial ATP-synthase coupling factor F1 |
| Downstream pathophysiology | Reduced complex V assembly leads to impaired oxidative phosphorylation and ATP availability. Diversion of pyruvate toward lactate and energy failure in brain, muscle, liver, and kidney is plausible; links to malformations, seizures, and neurodegeneration remain **inferred**, not directly demonstrated in ATPAF2 tissues. (tauchmannova2024variabilityofclinical pages 17-19, meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 2-3) | Human biochemical concordance plus inference; ATPAF2-specific ROS, apoptosis, and immune mechanisms unproven | GO:0006119 Oxidative phosphorylation; GO:0006096 Glycolytic process; CL:0000540 neuron; CL:0000187 muscle cell; CL:0000182 hepatocyte |
| Yeast evidence | Human ATP12 cDNA complements a yeast **Δatp12** mutant. Yeast Atp12 deficiency causes F1/β-subunit aggregation, respiratory deficiency, failure to grow on non-fermentable carbon sources, and reduced ATPase activity; later reviews list W94R as confirmed in yeast. (franco2020humanmitochondrialpathologies pages 17-19, meirleir2004respiratorychaincomplex pages 3-4) | Conserved functional model; strong support for assembly-factor function but cannot reproduce human neurodevelopmental disease | NCBI Taxon:4932 *Saccharomyces cerevisiae*; GO:0033615; genetic loss-of-function/complementation model |
| Treatment and trials | No ATPAF2-specific drug, gene/RNA therapy, response rate, approved therapy, or interventional trial was identified. Care is supportive and phenotype-directed; vitamins and cofactors lack ATPAF2-specific efficacy data. | Evidence gap; no disease-specific clinical-trial evidence | NCIT:C15747 Supportive Care; NCIT:C15313 Physical Therapy; NCIT:C15290 Genetic Counseling |
| Extrapolated management | **General mitochondrial-disease guidance—not ATPAF2-specific:** avoid fasting and metabolic stress; provide prompt calories and fluids during illness; monitor neurologic, nutritional, cardiac, hepatic, renal, auditory, visual, and endocrine status; obtain MRI for new neurologic deterioration; consider rehabilitation and antiseizure therapy. (coelho2026apersonalizedmedicine pages 225-226, mickelssonUnknownyearclinicalandneuroimaginga pages 21-24, coelho2026apersonalizedmedicine pages 56-59) | Expert-consensus extrapolation; benefit in ATPAF2 deficiency unknown | NCIT:C16269 Disease Management; NCIT:C17888 Nutritional Support; NCIT:C15747 Supportive Care |
| 2024 review status | The 2024 review still listed only **one ATPAF2 patient**, with homozygous p.Trp94Arg, encephalopathy, 3-methylglutaconic aciduria, lactic acidosis, dysmorphism, markedly reduced complex V abundance, and reduced ATP-hydrolytic activity. No expanded cohort, natural-history study, or disease-specific omics analysis was reported. (tauchmannova2024variabilityofclinical pages 17-19) | Recent authoritative disease-group review confirming persistent extreme rarity and major evidence gaps | Evidence status: single-case Mendelian disorder; phenotype frequencies not estimable |


*Table: Compact evidence map for ATPAF2-related mitochondrial complex V deficiency, separating direct findings from the single confirmed human case and model evidence from extrapolated mitochondrial-disease management.*

## 1. Disease information

### Definition

The disorder is a primary mitochondrial oxidative-phosphorylation disease in which deficient ATPAF2-mediated assembly causes a marked reduction of assembled and functional mitochondrial F-type ATP synthase (respiratory-chain complex V). Complex V normally uses proton flow from the intermembrane space into the matrix to convert ADP and inorganic phosphate into ATP. (meirleir2004respiratorychaincomplex pages 1-2)

### Identifiers and synonyms

- **Preferred name:** mitochondrial complex V (ATP synthase) deficiency, nuclear type 1.
- **MONDO:** **MONDO:0011421**, as specified in the query; database mappings should be locally verified before release.
- **Causal gene:** **ATPAF2**, ATP synthase mitochondrial F1 complex assembly factor 2; **OMIM gene *608918**.
- **Historical gene/protein names:** **ATP12**, ATP12 homolog, ATP12p/Atp12p.
- **Disease synonyms:** ATPAF2-related mitochondrial disease; ATP12-related complex V deficiency; nuclear-encoded ATP-synthase assembly deficiency; mitochondrial complex V deficiency due to ATP12 mutation.
- **Broader mappings:** mitochondrial respiratory-chain complex deficiency (**MONDO:0000066**) and Orphanet’s broader “mitochondrial disorder due to a defect in assembly or maturation of respiratory-chain complexes” (**Orphanet:309136**) are broader, not equivalent, categories. Open Targets maps ATPAF2 (ENSG00000171953) to mitochondrial respiratory-chain complex deficiency but provides no underlying association evidence in the returned record. (OpenTargets Search: mitochondrial complex V deficiency nuclear type 1-ATPAF2)
- **OMIM disease, Orphanet disease-specific, ICD-10, ICD-11, and MeSH identifiers:** no confidently verified disease-specific codes were available in the retrieved evidence. Broad mitochondrial-metabolism codes should not be represented as exact equivalents.

The original evidence is **individual-patient research data**, not an EHR cohort. Later reviews aggregate that case at disease level but do not add patients. The foundational article was published February 2004 in *Journal of Medical Genetics*, 41:120–124, DOI [10.1136/jmg.2003.012047](https://doi.org/10.1136/jmg.2003.012047); a PMID was not displayed in the retrieved full text and therefore is not asserted here. (meirleir2004respiratorychaincomplex pages 1-2)

## 2. Etiology

### Causal factor and genetic risk

The only established cause is germline biallelic ATPAF2 dysfunction. The index patient was homozygous for **c.280T>A, p.Trp94Arg (W94R)**. Both healthy parents and one healthy sibling were heterozygous, establishing recessive segregation; the family was consanguineous and of Moroccan origin. W94R was absent from 50 ethnically matched controls. (meirleir2004respiratorychaincomplex pages 2-3)

The published notation should be normalized against the current MANE transcript before knowledge-base ingestion because the 2004 report predates current HGVS conventions and contains typographic inconsistency elsewhere (“W84R”). The 2024 review uses **c.280T>A (p.Trp94Arg)**. (tauchmannova2024variabilityofclinical pages 17-19, meirleir2004respiratorychaincomplex pages 2-3)

**Variant interpretation:** the case-level evidence supports a pathogenic/likely pathogenic classification—homozygosity in an affected child, recessive segregation, absence from limited controls, severe complex V assembly deficiency, evolutionary conservation, and concordant yeast functional evidence. A current ClinVar assertion and current gnomAD allele frequency were not retrieved and should be checked directly rather than inferred. The variant is a germline missense allele; no somatic involvement is known.

### Other risk, protective, and modifying factors

- **Family history/consanguinity:** consanguinity increased the probability of homozygosity in the reported family, although family history was otherwise unremarkable. (meirleir2004respiratorychaincomplex pages 1-2)
- **Sex, ancestry, age:** no evidence establishes these as biological susceptibility factors; the only patient happened to be a Moroccan girl.
- **Environmental, occupational, lifestyle, toxic, or infectious causes:** none established.
- **Protective variants or modifier genes:** none reported.
- **Epigenetic modifiers:** none reported.
- **Gene–environment interaction:** infection probably acted as a metabolic stressor in the terminal event—the child died during an intercurrent infection—but it did not cause the Mendelian disorder. The broader principle that fever, fasting, dehydration, and surgery can precipitate mitochondrial decompensation is general mitochondrial-disease evidence, not ATPAF2-specific evidence. (meirleir2004respiratorychaincomplex pages 1-2, coelho2026apersonalizedmedicine pages 56-59)

## 3. Phenotypes

All disease-specific frequencies are **1/1** unless stated otherwise.

- **Congenital microcephaly/small head size:** head circumference 30.5 cm at full term. Suggested HPO: **HP:0000252 Microcephaly**.
- **Dysmorphism:** large mouth, prominent nasal bridge, micrognathia, and rocker-bottom feet. HPO suggestions: **HP:0000154 Wide mouth**, **HP:0000426 Prominent nasal bridge**, **HP:0000347 Micrognathia**, **HP:0001838 Rocker-bottom foot**.
- **Musculoskeletal manifestations:** congenital limb-flexion contractures and camptodactyly. HPO: **HP:0002803 Congenital contracture**, **HP:0012385 Camptodactyly**.
- **Neurologic manifestations:** neonatal hypertonia, severe developmental delay, encephalopathy, and seizures. HPO: **HP:0001276 Hypertonia**, **HP:0001263 Global developmental delay**, **HP:0001298 Encephalopathy**, **HP:0001250 Seizure**.
- **Feeding/growth:** poor sucking and subsequent failure to thrive. HPO: **HP:0011968 Feeding difficulties**, **HP:0001508 Failure to thrive**.
- **Hepatic/renal:** hepatomegaly and hypoplastic kidneys. HPO: **HP:0002240 Hepatomegaly**, **HP:0000089 Renal hypoplasia**.
- **Metabolic laboratory abnormalities:** urinary lactate, fumarate, methylglutaconic acid, and amino acids were increased. CSF lactate was **2.9 mmol/L** (reference <2); plasma lactate fluctuated between **2.7 and 10 mmol/L** (reference <2.2). HPO: **HP:0003128 Lactic acidosis**, **HP:0003535 3-methylglutaconic aciduria**, **HP:0003355 Aminoaciduria**. (meirleir2004respiratorychaincomplex pages 1-2)
- **Neuroimaging:** marked cortical–subcortical atrophy, corpus-callosum dysgenesis with absent anterior genu and rostrum, and white-matter hypoplasia; basal ganglia and thalami became atrophic over ensuing months. HPO: **HP:0002120 Cerebral cortical atrophy**, **HP:0007370 Abnormality of the corpus callosum**, **HP:0007007 Abnormality of the basal ganglia**, and an appropriate white-matter abnormality term. (meirleir2004respiratorychaincomplex pages 1-2)
- **Muscle pathology:** increased lipid content without ragged-red fibers. HPO: **HP:0003555 Muscle fiber lipid accumulation**. The absence of ragged-red fibers is important because these are often absent in pediatric mitochondrial disease. (meirleir2004respiratorychaincomplex pages 2-3, coelho2026apersonalizedmedicine pages 53-56)

The presentation resembled cerebro-oculo-facio-skeletal/Pena–Shokeir type II syndrome but lacked microphthalmia and cataracts. No behavioral or psychiatric phenotype was separately assessed. No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data exist. Profound developmental, feeding, motor, and seizure burdens imply severe impairment of daily function, but this is a clinical inference rather than a measured patient-reported outcome.

## 4. Genetic and molecular information

**ATPAF2** lies at **17p11.2** and encodes a broadly expressed, nuclear-encoded mitochondrial protein. Its product is imported into the mitochondrial matrix and acts specifically in ATP-synthase biogenesis rather than as a general HSP60-family chaperone. (meirleir2004respiratorychaincomplex pages 3-4)

The F1 sector contains α, β, γ, δ, and ε subunits. ATPAF2/Atp12 interacts with the F1 α subunit, while ATPAF1/Atp11 interacts with β; these interactions prevent nonproductive aggregation and permit assembly of the catalytic **α3β3** module. The 2024 review describes ATPAF2 as required for formation of this hexamer. (tauchmannova2024variabilityofclinical pages 1-3, meirleir2004respiratorychaincomplex pages 3-4)

The W94R substitution lies adjacent to a strongly conserved residue. The original authors inferred that replacing a neutral residue with basic arginine severely compromises ATPAF2 activity and proper F1 assembly. This is a **loss-of-function assembly defect**, not demonstrated gain of function or dominant-negative action. (meirleir2004respiratorychaincomplex pages 4-5)

No additional pathogenic ATPAF2 alleles, structural variants, chromosomal abnormalities, modifier genes, disease-associated methylation signature, or chromatin abnormality were identified. Current population frequency, ClinVar status, HGNC identifier, and transcript-specific HGVS should be added only after direct database verification.

## 5. Environmental information

No toxin, radiation, pollution, occupation, diet, smoking, alcohol exposure, lifestyle behavior, or infectious agent is etiologic. Intercurrent infection can increase energy demand and precipitate deterioration in mitochondrial disease; the reported child died during an infection, but causality for the terminal outcome cannot be disentangled from severe baseline disease. (meirleir2004respiratorychaincomplex pages 1-2)

There is no evidence that a diet, supplement, exercise pattern, or environmental exposure prevents ATPAF2 disease. Avoidance of prolonged fasting and prompt management of illness are tertiary risk-reduction measures extrapolated from general mitochondrial medicine, not primary prevention of the genotype. (coelho2026apersonalizedmedicine pages 56-59)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous ATPAF2 c.280T>A (p.Trp94Arg) leads to** defective ATPAF2/Atp12 assembly-factor function in the mitochondrial matrix.  
2. **Defective ATPAF2–F1 α-subunit handling leads to** failure to prevent nonproductive α/β aggregation and impaired α3β3 F1-module assembly; the W94R-specific molecular interaction is supported by conserved-model evidence but not structurally demonstrated in patient cells. (tauchmannova2024variabilityofclinical pages 1-3, meirleir2004respiratorychaincomplex pages 3-4, meirleir2004respiratorychaincomplex pages 4-5)  
3. **Impaired F1 assembly leads to** markedly reduced mature complex V abundance and loss of multiple associated subunits (α, β, d, and OSCP). (meirleir2004respiratorychaincomplex pages 2-3, meirleir2004respiratorychaincomplex pages 3-4)  
4. **Reduced mature complex V leads to** decreased ATP-hydrolytic/synthase activity and impaired oxidative phosphorylation. (tauchmannova2024variabilityofclinical pages 17-19, meirleir2004respiratorychaincomplex pages 2-3)  
5. **Impaired oxidative phosphorylation results in** inadequate ATP supply and redox imbalance; diversion of pyruvate toward lactate plausibly causes hyperlactatemia/lactic acidosis. This metabolic link is strongly biologically supported but was not flux-measured in this patient.  
6. **Energy failure branches into:**  
   a. **neuronal/developmental injury**, leading to encephalopathy, seizures, severe delay, and progressive cerebral, basal-ganglia, and thalamic atrophy;  
   b. **skeletal-muscle dysfunction**, leading to abnormal lipid accumulation, hypertonia/contractures, and impaired motor function;  
   c. **hepatic and renal dysfunction/developmental involvement**, associated with hepatomegaly, aminoaciduria, and renal hypoplasia. These organ-level links are inferred from phenotype and bioenergetics rather than demonstrated histologically. (meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 2-3)  
7. **Systemic low bioenergetic reserve leads to** vulnerability during infection or catabolic stress, culminating in progressive failure to thrive and infant death in the reported case. (meirleir2004respiratorychaincomplex pages 1-2)

### Quantitative biochemical evidence

Complex V activity was **30 nmol substrate/min/mg protein in liver**, versus control median 87 (5th–95th percentile 35–108), and **119 in skeletal muscle**, versus control median 209 (97–754). Liver complex IV was also reduced, while principal BN-PAGE assays showed comparative preservation of complexes I, II, and IV and normal complex III cross-reacting material. This supports a predominant complex V assembly defect with tissue variability rather than an absolutely isolated defect in every assay. (meirleir2004respiratorychaincomplex pages 2-3, meirleir2004respiratorychaincomplex pages 3-4)

BN-PAGE/catalytic staining showed severe complex V reduction in liver and fibroblasts but greater residual staining in skeletal muscle. Immunoblots demonstrated markedly reduced or undetectable assembled complex V and reduced α, β, d, and OSCP subunits. (meirleir2004respiratorychaincomplex pages 2-3, meirleir2004respiratorychaincomplex pages 3-4)

### Pathways, processes, cells, and ontology suggestions

- **GO biological process:** GO:0033615 mitochondrial proton-transporting ATP-synthase-complex assembly; GO:0042776 mitochondrial ATP synthesis coupled proton transport; GO:0006119 oxidative phosphorylation; GO:0006457 protein folding.
- **GO cellular component:** GO:0005739 mitochondrion; GO:0005759 mitochondrial matrix; GO:0005743 mitochondrial inner membrane; GO:0000275 mitochondrial proton-transporting ATP synthase complex; GO:0000276 F1 sector.
- **Likely vulnerable cells:** neurons (**CL:0000540**), skeletal myocytes (**CL:0000187**), hepatocytes (**CL:0000182**), and renal tubular epithelial cells. These are phenotype-driven suggestions; cell-specific ATPAF2 pathology has not been measured.
- **Metabolic entities:** ATP (**CHEBI:15422**), ADP (**CHEBI:16761**), phosphate, pyruvate (**CHEBI:15361**), and lactate (**CHEBI:24996**).

ATPAF2-specific ROS generation, apoptosis, autophagy, mitophagy, mTOR/MAPK/PI3K signaling, inflammation, or immune activation has not been demonstrated. A 2024 CRISPR-based PMF-seq study found that ATPAF2 loss sensitized cells to acute tBID action, suggesting a relationship between complex V state and mitochondrial apoptosis, but this was a functional-genomics screen rather than evidence from patients with W94R disease.

No patient transcriptomics, proteomics beyond targeted immunoblotting, metabolomics beyond clinical organic-acid testing, lipidomics, single-cell analysis, spatial transcriptomics, or integrated multi-omics study has been published.

## 7. Anatomical structures affected

**Primary system:** central nervous system—cerebral cortex/subcortical structures, cerebral white matter, corpus callosum, basal ganglia, and thalamus. Suggested UBERON terms include **UBERON:0000955 brain**, **UBERON:0001893 telencephalon**, **UBERON:0002421 hippocampal formation only if independently demonstrated—not currently**, **UBERON:0002420 basal ganglion**, and **UBERON:0001897 dorsal thalamus**. (meirleir2004respiratorychaincomplex pages 1-2)

**Additional organs/tissues:** skeletal muscle, liver, kidney, and skin fibroblasts used for biochemical testing. Suggested UBERON: **UBERON:0001134 skeletal muscle tissue**, **UBERON:0002107 liver**, **UBERON:0002113 kidney**, and **UBERON:0002097 skin**. (meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 2-3)

**Subcellular localization:** mitochondrial matrix and inner-membrane ATP-synthase assembly machinery. No lateralization was reported; brain abnormalities were described as diffuse/central rather than unilateral.

## 8. Temporal development

Onset was congenital/neonatal: dysmorphism, microcephaly, contractures, hypertonia, impaired sucking, hepatomegaly, and renal hypoplasia were recognized at birth or initial evaluation. During infancy, severe developmental delay, seizures, failure to thrive, and radiographic progression from cortical/subcortical atrophy to basal-ganglia and thalamic atrophy occurred. The course was rapidly progressive and fatal at 14 months. (meirleir2004respiratorychaincomplex pages 1-2)

No standardized stages, remission pattern, recovery episodes, or intervention-responsive window are known. Infection, fasting, fever, dehydration, and surgery should be treated as periods of heightened metabolic vulnerability based on general mitochondrial-disease practice. (coelho2026apersonalizedmedicine pages 56-59)

## 9. Inheritance and population

The demonstrated pattern is **autosomal recessive**. For two heterozygous parents, each pregnancy has the standard theoretical probabilities of 25% affected, 50% heterozygous carrier, and 25% unaffected non-carrier, assuming the same parental genotypes and no unusual mosaicism.

Penetrance for biallelic W94R cannot be estimated from one affected child. Heterozygous parents and a sibling were clinically healthy, arguing against a dominant phenotype. Expressivity, anticipation, germline mosaicism, and founder effects are unknown. Consanguinity was present in the sole pedigree. (meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 2-3)

No prevalence, incidence, carrier frequency, geographic distribution, ethnic enrichment, or sex ratio can be calculated. “One reported patient” is the most defensible statistic. The broader prevalence of all mitochondrial diseases must not be assigned to this ATPAF2 subtype.

## 10. Diagnostics

### Recommended diagnostic workflow

1. **Clinical recognition:** congenital/infantile encephalopathy with dysmorphism, contractures, feeding failure, seizures, progressive atrophy, hyperlactatemia, and 3-methylglutaconic aciduria should prompt mitochondrial evaluation.
2. **Initial biochemistry:** blood lactate and pyruvate with careful collection, blood gas/acid–base status, glucose, electrolytes, ammonia, liver enzymes, CK, plasma amino acids, acylcarnitines, and urine organic acids. CSF lactate/pyruvate/alanine may be informative with neurologic disease. A lactate/pyruvate ratio >20 may suggest respiratory-chain dysfunction but is neither sensitive nor specific. (coelho2026apersonalizedmedicine pages 220-222)
3. **Imaging:** brain MRI; MRS may detect a lactate peak. Repeat MRI with new neurologic deterioration or seizures. General mitochondrial patterns include cortical/cerebellar atrophy and white-matter, basal-ganglia, thalamic, or brainstem lesions. (coelho2026apersonalizedmedicine pages 53-56, mickelssonUnknownyearclinicalandneuroimaging pages 21-24)
4. **Molecular testing:** trio WES or WGS with ATPAF2 included, concurrent analysis of nuclear OXPHOS/ATP-synthase genes, and mtDNA sequencing/deletion analysis because phenotypes overlap. Confirm candidate variants by an orthogonal method and test parents. WGS is preferable when exome/panel testing is negative because it can detect noncoding, copy-number, and structural variants; this is general genomic reasoning, not ATPAF2-specific validation.
5. **Functional confirmation:** patient fibroblasts or muscle/liver tissue can undergo BN-PAGE with complex V in-gel activity, immunoblotting/complexome profiling, spectrophotometric activity normalized to citrate synthase, ATP-production assays, and oxygen-consumption studies. Muscle activity below 20% of controls is strongly indicative in general practice, although normal tissue testing does not exclude mitochondrial disease. (coelho2026apersonalizedmedicine pages 53-56)
6. **RNA sequencing:** useful for suspected splice/noncoding variants or unresolved cases, but no ATPAF2 diagnostic RNA-seq signature exists.

The original case demonstrates that conventional muscle microscopy may show only lipid accumulation without ragged-red fibers; therefore, a nondiagnostic biopsy morphology cannot exclude the disorder. (meirleir2004respiratorychaincomplex pages 2-3)

### Biomarkers

Lactate and 3-methylglutaconic acid are clues, not specific biomarkers. General pediatric PMD studies support FGF21 and GDF15, but neither has been validated in ATPAF2 deficiency. In one pediatric PMD cohort of 51 patients, median GDF15 was 919.46 pg/mL versus 294.86 in non-mitochondrial neuromuscular disease and 221.21 in healthy controls; GDF15 AUC was 0.891, with a 606.369-pg/mL cutoff giving 74.5% sensitivity and 100% specificity. These values should not be treated as ATPAF2 performance estimates.

### Differential diagnosis

- Other nuclear complex V assembly/subunit disorders: **TMEM70, ATP5F1A, ATP5F1B, ATP5F1D, ATP5F1E**, and other ATP-synthase genes.
- mtDNA complex V disorders: **MT-ATP6** and **MT-ATP8**.
- Other causes of 3-methylglutaconic aciduria and mitochondrial membrane dysfunction.
- Leigh/Leigh-like spectrum and other respiratory-chain deficiencies.
- Pyruvate dehydrogenase deficiency, especially when lactate/pyruvate ratio is low.
- COFS/Pena–Shokeir spectrum, congenital disorders of glycosylation, and neuromuscular fetal-akinesia syndromes.

A 2024 Leigh-spectrum framework recommends parallel amino acids, acylcarnitines, and urinary organic acids because rapidly available biochemical testing characterized 80% of its cohort and enabled specific intervention in 10%; those figures concern Leigh-spectrum diagnosis broadly, not ATPAF2 disease.

### Screening

There is no population or newborn screening program. Once familial variants are known, cascade carrier testing, targeted prenatal diagnosis, and preimplantation genetic testing are technically feasible. CMA, karyotype, FISH, and repeat-expansion testing are not first-line unless another diagnosis is suspected. mtDNA testing remains important in the differential but will not detect a nuclear ATPAF2 variant.

## 11. Outcome and prognosis

The only genetically confirmed patient developed profound neurologic disability, seizures, feeding/growth failure, and progressive brain atrophy and died during infection at **14 months**. No 5- or 10-year survival, life-expectancy distribution, mortality rate, recovery proportion, or validated prognostic model exists. (meirleir2004respiratorychaincomplex pages 1-2)

Potential poor-prognosis indicators—congenital onset, severe hyperlactatemia, extensive brain atrophy, seizures, feeding failure, and multiorgan involvement—are clinically plausible but unvalidated. Residual tissue-specific complex V activity could influence severity, as skeletal muscle retained more activity than liver in the index patient, but no genotype–biochemistry–outcome series exists. (meirleir2004respiratorychaincomplex pages 2-3)

## 12. Treatment

### Disease-specific status

There is **no ATPAF2-specific approved pharmacotherapy, gene therapy, RNA therapy, cell therapy, surgery, or evidence-based treatment algorithm**. No ATPAF2-targeted interventional clinical trial or NCT identifier was identified. Treatment response rates and ATPAF2-specific adverse-event data are unavailable.

### Current real-world care—extrapolated from general mitochondrial practice

- **Metabolic crisis prevention and treatment:** avoid prolonged fasting; provide prompt hydration and calories during illness; monitor glucose, acid–base status, lactate, ammonia, electrolytes, liver enzymes, CK, ketones, and renal status. Perioperative plans should minimize fasting and temperature instability. (coelho2026apersonalizedmedicine pages 225-226, coelho2026apersonalizedmedicine pages 56-59)
- **Neurology:** standard seizure treatment guided by epilepsy specialists. Levetiracetam and benzodiazepines are commonly considered safer general options. Valproate should be approached cautiously in mitochondrial disease—especially when POLG disease has not been excluded—and drug choice individualized. (coelho2026apersonalizedmedicine pages 225-226)
- **Nutrition:** swallowing assessment, calorie optimization, treatment of reflux/constipation, and enteral feeding when necessary. NCIT suggestions: **NCIT:C17888 Nutritional Support**, **NCIT:C15747 Supportive Care**.
- **Rehabilitation:** physical, occupational, speech/feeding, and respiratory therapy tailored to tolerance. NCIT: **NCIT:C15313 Physical Therapy**, occupational therapy, speech therapy.
- **Surveillance:** neurologic/developmental assessment, EEG as indicated, growth/nutrition, ECG/echocardiography, liver and renal tests, ophthalmology, hearing, endocrine/glucose/thyroid evaluation, and repeat MRI with clinical change. These are general PMD recommendations. (mickelssonUnknownyearclinicalandneuroimaginga pages 21-24, mickelssonUnknownyearclinicalandneuroimaging pages 21-24)
- **Vitamins/cofactors:** coenzyme Q10, riboflavin, thiamine, alpha-lipoic acid, and folinic acid are sometimes used empirically; L-carnitine should generally be reserved for documented deficiency. Controlled evidence is limited and no efficacy has been shown for ATPAF2 disease. (hynynen2019statusepilepticusin pages 51-54)
- **Exercise:** supervised, gradually progressive aerobic and resistance activity may benefit stable mitochondrial patients, but the congenital severe ATPAF2 phenotype has no exercise study and may permit only supportive positioning and therapy.

Gene replacement is conceptually attractive because ATPAF2 is nuclear encoded, but delivery to brain and multiple organs, developmental timing, natural-history scarcity, and absence of a mammalian model are major barriers. CRISPR editing, mRNA/ASO therapy, mitochondrial transplantation, and metabolic modulators remain speculative for this condition.

## 13. Prevention

**Primary prevention of sporadic occurrence is not possible through lifestyle modification.** For known carrier couples, genetic counseling is the principal evidence-based preventive strategy. Options include targeted carrier testing of adult relatives, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and preimplantation genetic testing for the familial ATPAF2 variant. NCIT suggestion: **NCIT:C15290 Genetic Counseling**.

**Secondary prevention:** no newborn or biochemical population screen exists. Early genomic testing in a symptomatic infant or an at-risk pregnancy can shorten diagnosis and enable anticipatory metabolic and supportive care, but there is no proof that presymptomatic treatment changes ATPAF2 outcomes.

**Tertiary prevention:** avoid fasting and dehydration, institute illness plans, vaccinate according to routine schedules to reduce preventable infections, maintain nutrition, and monitor neurologic, cardiac, hepatic, renal, endocrine, hearing, and visual complications. Vaccination prevents infection-related stress, not the genetic disease itself.

## 14. Other species and natural disease

ATPAF2/ATP12 function is evolutionarily conserved across eukaryotes. The best-characterized comparative system is **Saccharomyces cerevisiae** (NCBI Taxon **4932**), in which Atp12 deficiency causes F1/β-subunit aggregation, respiratory deficiency, failure to grow on non-fermentable carbon sources, and reduced ATPase activity. Human ATP12 cDNA complements yeast Δatp12, demonstrating conserved function. (meirleir2004respiratorychaincomplex pages 3-4)

No naturally occurring ATPAF2-equivalent veterinary disease, breed predisposition, wildlife syndrome, zoonotic transmission, or cross-species infectious susceptibility was identified. The disorder is inherited and noncommunicable.

## 15. Model organisms and experimental systems

### Yeast

Yeast is the principal mechanistic model. Its strengths are conserved ATP12 function, tractable respiratory growth assays, direct analysis of F1 assembly, and complementation by human ATP12. Reviews list human W94R as functionally confirmed in yeast. (franco2020humanmitochondrialpathologies pages 17-19, meirleir2004respiratorychaincomplex pages 3-4)

Its limitations are lack of human brain development, organ-specific disease, seizures, dysmorphism, and mammalian metabolic physiology. It therefore validates the assembly defect but not the full clinical phenotype.

### Cellular systems

Patient fibroblasts demonstrated severely reduced complex V by BN-PAGE/catalytic staining and are the most disease-proximal model available. Modern applications could include ATPAF2 correction/rescue, complexome profiling, Seahorse respirometry, isotope tracing, mitochondrial membrane-potential assays, and stress-challenge studies. (meirleir2004respiratorychaincomplex pages 2-3)

A 2024 PMF-seq CRISPR screen identified ATPAF2 loss as a genetic sensitizer to acute tBID-induced mitochondrial injury. This is a valuable functional-genomics observation but not a W94R model and not proof that apoptosis drives the human phenotype.

### Mammalian and advanced models

No ATPAF2-W94R knock-in mouse, conditional knockout, zebrafish line, Drosophila model, patient iPSC-derived neuron/cardiomyocyte, organoid, or humanized model was identified. No ATPAF2-specific single-cell or spatial atlas exists. Developing a viable hypomorphic or tissue-specific mammalian model is a high priority because complete disruption may be developmentally lethal and because yeast cannot model neurodevelopmental anatomy.

## Recent developments and expert assessment, 2023–2024

The most important disease-specific update is negative but informative: the August 2024 systematic review, *Variability of Clinical Phenotypes Caused by Isolated Defects of Mitochondrial ATP Synthase*, DOI [10.33549/physiolres.935407](https://doi.org/10.33549/physiolres.935407), still found only one ATPAF2 patient and summarized the phenotype as encephalopathy, 3-methylglutaconic aciduria, lactic acidosis, dysmorphism, markedly reduced complex V abundance, and reduced ATP-hydrolytic activity. (tauchmannova2024variabilityofclinical pages 17-19)

A useful direct statement from that review is its table entry: **“ATPAF2 c.280T>A Hm (p.Trp94Arg) … encephalopathy, 3-MGA, LA, DF … [one] patient.”** (tauchmannova2024variabilityofclinical pages 17-19)

The original report’s key conclusion was: **“To our knowledge, this is the first report of a pathogenic mutation in a human nuclear encoded ATPase assembly gene.”** It also concluded that **“lactic acidosis, dysmorphic features, and methyl glutaconic aciduria can be major clues in the diagnosis.”** (meirleir2004respiratorychaincomplex pages 1-2, meirleir2004respiratorychaincomplex pages 4-5)

Broader 2024 advances include multi-omic diagnostic frameworks, improved Leigh-spectrum pipelines, and scalable mitochondrial functional-genomics assays. Their current application to ATPAF2 is diagnostic prioritization and experimental design—not an established therapy. The chief expert-level conclusion is that mechanistic confidence is substantially stronger than clinical generalizability: ATPAF2’s role in F1 assembly is well supported, but virtually every statement about penetrance, phenotype frequency, prognosis, management efficacy, and population burden remains limited by **n=1**.

## Priority knowledge gaps

1. Independent ATPAF2 cases and standardized deposition of variants in ClinVar/LOVD.
2. Current transcript-normalized HGVS, population-frequency, and ACMG/AMP curation.
3. Prospective natural history and patient-reported quality-of-life data.
4. ATPAF2-W94R rescue in patient cells and structural measurement of altered α-subunit binding.
5. iPSC-neuron, organoid, and mammalian models.
6. Patient complexomics, transcriptomics, metabolomics, and stress-response profiling.
7. Disease-specific biomarkers and quantitative outcome measures.
8. Preclinical testing of nuclear ATPAF2 gene replacement or mRNA delivery.

**Knowledge-base confidence:** high for the ATPAF2–complex V assembly relationship and recessive W94R pedigree; moderate for W94R pathogenicity based on integrated segregation/biochemistry/model evidence; very low for phenotype frequencies, epidemiology, prognosis, and treatment effectiveness because only one genetically confirmed patient has been reported.

References

1. (tauchmannova2024variabilityofclinical pages 17-19): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 19 citations and is from a peer-reviewed journal.

2. (franco2020humanmitochondrialpathologies pages 17-19): Leticia V. R. Franco, Luca Bremner, and Mario H. Barros. Human mitochondrial pathologies of the respiratory chain and atp synthase: contributions from studies of saccharomyces cerevisiae. Nov 2020. URL: https://doi.org/10.3390/life10110304, doi:10.3390/life10110304. This article has 20 citations.

3. (meirleir2004respiratorychaincomplex pages 2-3): L. Meirleir, S. Seneca, W. Lissens, I. D. Clercq, F. Eyskens, E. Gerlo, J. Smet, and R. Coster. Respiratory chain complex v deficiency due to a mutation in the assembly gene atp12. Journal of Medical Genetics, 41:120-124, Feb 2004. URL: https://doi.org/10.1136/jmg.2003.012047, doi:10.1136/jmg.2003.012047. This article has 274 citations and is from a domain leading peer-reviewed journal.

4. (meirleir2004respiratorychaincomplex pages 1-2): L. Meirleir, S. Seneca, W. Lissens, I. D. Clercq, F. Eyskens, E. Gerlo, J. Smet, and R. Coster. Respiratory chain complex v deficiency due to a mutation in the assembly gene atp12. Journal of Medical Genetics, 41:120-124, Feb 2004. URL: https://doi.org/10.1136/jmg.2003.012047, doi:10.1136/jmg.2003.012047. This article has 274 citations and is from a domain leading peer-reviewed journal.

5. (meirleir2004respiratorychaincomplex pages 3-4): L. Meirleir, S. Seneca, W. Lissens, I. D. Clercq, F. Eyskens, E. Gerlo, J. Smet, and R. Coster. Respiratory chain complex v deficiency due to a mutation in the assembly gene atp12. Journal of Medical Genetics, 41:120-124, Feb 2004. URL: https://doi.org/10.1136/jmg.2003.012047, doi:10.1136/jmg.2003.012047. This article has 274 citations and is from a domain leading peer-reviewed journal.

6. (tauchmannova2024variabilityofclinical pages 1-3): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 19 citations and is from a peer-reviewed journal.

7. (meirleir2004respiratorychaincomplex pages 4-5): L. Meirleir, S. Seneca, W. Lissens, I. D. Clercq, F. Eyskens, E. Gerlo, J. Smet, and R. Coster. Respiratory chain complex v deficiency due to a mutation in the assembly gene atp12. Journal of Medical Genetics, 41:120-124, Feb 2004. URL: https://doi.org/10.1136/jmg.2003.012047, doi:10.1136/jmg.2003.012047. This article has 274 citations and is from a domain leading peer-reviewed journal.

8. (coelho2026apersonalizedmedicine pages 225-226): MMP Coelho. A personalized medicine approach for mitochondrial respiratory chain disorders in childhood in the new era of genome sequence. Unknown journal, 2026.

9. (mickelssonUnknownyearclinicalandneuroimaginga pages 21-24): N Mickelsson. Clinical and neuroimaging features in primary mitochondrial diseases–a cohort study incorporating quantitative mri. Unknown journal, Unknown year.

10. (coelho2026apersonalizedmedicine pages 56-59): MMP Coelho. A personalized medicine approach for mitochondrial respiratory chain disorders in childhood in the new era of genome sequence. Unknown journal, 2026.

11. (OpenTargets Search: mitochondrial complex V deficiency nuclear type 1-ATPAF2): Open Targets Query (mitochondrial complex V deficiency nuclear type 1-ATPAF2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (coelho2026apersonalizedmedicine pages 53-56): MMP Coelho. A personalized medicine approach for mitochondrial respiratory chain disorders in childhood in the new era of genome sequence. Unknown journal, 2026.

13. (coelho2026apersonalizedmedicine pages 220-222): MMP Coelho. A personalized medicine approach for mitochondrial respiratory chain disorders in childhood in the new era of genome sequence. Unknown journal, 2026.

14. (mickelssonUnknownyearclinicalandneuroimaging pages 21-24): N Mickelsson. Clinical and neuroimaging features in primary mitochondrial diseases–a cohort study incorporating quantitative mri. Unknown journal, Unknown year.

15. (hynynen2019statusepilepticusin pages 51-54): J Hynynen. Status epilepticus in mitochondrial diseases and the role of polg1 variants in the valproic-acid induced hepatotoxicity. Unknown journal, 2019.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 64 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011421` (3 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex V (ATP synthase) deficiency, nuclear type 1**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0000275` (obsolete mitochondrial proton-transporting ATP synthase complex, catalytic sector F(1)) (2 mentions) - replaced by `GO:0045259`
- `GO:0051082` (obsolete unfolded protein binding) (1 mention)
- `GO:0000276` (obsolete mitochondrial proton-transporting ATP synthase complex, coupling factor F(o)) (2 mentions) - replaced by `GO:0045259`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`, `Orphanet`.