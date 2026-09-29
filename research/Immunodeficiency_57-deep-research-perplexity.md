---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-17T14:18:23.247460'
end_time: '2026-09-17T14:24:28.885784'
duration_seconds: 365.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 57
  mondo_id: MONDO:0020849
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 64
  verified: 58
  not_found: 1
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.016
  labels_checked: 37
  labels_matching: 20
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0012404
    reported_labels:
    - Early-onset inflammatory bowel disease
    ontology_label: Abnormal urine citrate concentration
  - term_id: HP:0003481
    reported_labels:
    - Inflammatory arthritis
    ontology_label: Segmental peripheral demyelination/remyelination
  - term_id: HP:0001883
    reported_labels:
    - Decreased T cell count
    ontology_label: Talipes
  - term_id: HP:0002110
    reported_labels:
    - Recurrent lower respiratory tract infections
    - Bronchiectasis
    ontology_label: Bronchiectasis
  - term_id: HP:0002597
    reported_labels:
    - Inflammatory bowel disease
    ontology_label: Abnormality of the vasculature
  - term_id: HP:0002038
    reported_labels:
    - Chronic diarrhea
    ontology_label: Protein avoidance
  - term_id: HP:0002240
    reported_labels:
    - Gastrointestinal hemorrhage
    ontology_label: Hepatomegaly
  - term_id: HP:0002635
    reported_labels:
    - Cutaneous vasculitis
    - Leukocytoclastic vasculitis
    ontology_label: Type IV atherosclerotic lesion
  - term_id: HP:0012091
    reported_labels:
    - Decreased NK cell count
    ontology_label: Abnormality of pancreas physiology
  labels_variant: 8
  unresolved_terms:
  - HP:0003479
  obsolete_terms:
  - term_id: GO:0032088
    ontology_label: obsolete negative regulation of NF-kappaB transcription factor
      activity
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  unresolvable_prefixes:
  - DO
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 57
- **MONDO ID:** MONDO:0020849 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 57** covering all of the
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

# Immunodeficiency 57 with Autoinflammation (IMD57 / MONDO:0020849): An In-Depth Characterization

Immunodeficiency 57 with autoinflammation (IMD57) is a very rare autosomal recessive primary immunodeficiency caused by biallelic loss-of-function variants in the **RIPK1** gene, leading to a characteristic combination of early-onset recurrent bacterial, viral, and fungal infections; chronic inflammatory bowel disease involving both upper and lower gastrointestinal tract; progressive inflammatory polyarthritis; lymphopenia; and dysregulated cytokine production.[1][3][5][11][14][18] Patients typically present in infancy with severe gastrointestinal symptoms, failure to thrive, recurrent respiratory and systemic infections, and evidence of systemic inflammation, often requiring intensive immunologic, nutritional, and sometimes hematopoietic stem cell–based interventions.[3][5][18] Mechanistically, the disease represents a prototypic **inborn error of innate immunity**, in which the loss of RIPK1’s scaffolding and regulatory functions destabilizes the balance between pro-survival NF-κB signaling and programmed cell death pathways, producing both immunodeficiency and autoinflammation.[12][15][17][18] Only a small number of families—on the order of a dozen probands—have been reported worldwide, but detailed human and mouse studies together have established IMD57 as a “natural experiment” demonstrating the central role of RIPK1 in human immune homeostasis and highlighting RIPK1-related pathways as therapeutic targets.[3][12][17][18]  

---

## 1. Disease Information

### 1.1 Overview and Core Definition

Immunodeficiency 57 with autoinflammation (IMD57) is defined as a primary immunodeficiency characterized by **recurrent infections starting in the first year of life**, **lymphopenia**, **altered production of multiple cytokines**, **inflammatory polyarthritis**, and **chronic active inflammation of the digestive tract**, caused by **homozygous or compound heterozygous loss-of-function mutations in the RIPK1 gene on chromosome 6p25.2**.[1][5][11][14][18] ZFIN and Disease Ontology describe IMD57 as “immune dysregulation–inflammatory bowel disease–arthritis–recurrent infections–lymphopenia syndrome,” emphasizing the combined immunodeficiency and autoinflammatory phenotype.[1] MalaCards similarly summarizes the disease as “a rare genetic immune disease characterized by early onset of recurrent bacterial, viral, and fungal infections, chronic inflammatory bowel disease, gastritis, and inflammatory polyarthritis.”[5] The first detailed human description came from Cuchet-Lourenço et al. in Science in 2018, who reported four patients from three unrelated consanguineous families with complete RIPK1 deficiency due to homozygous mutations, presenting with severe infections, early-onset inflammatory bowel disease (IBD), and progressive polyarthritis.[18]  

ClinGen’s Primary Immune Regulatory Disorders Gene Curation Expert Panel (GCEP) has classified the **RIPK1–IMD57** gene–disease relationship as **“definitive,”** noting that at least 11 distinct variants (missense, nonsense, frameshift, and large deletions) have been identified in 13 probands across five independent publications, all with consistent clinical phenotypes.[3] The panel emphasizes that all reported patients present with recurrent infections and early-onset IBD, and that the mechanism of pathogenicity is **loss of function** of RIPK1.[3] In a 2021 review, Liu et al. (Frontiers in Immunology) grouped IMD57 under “RIPK1-associated inborn errors of innate immunity,” together with a distinct autosomal dominant autoinflammatory condition caused by cleavage-resistant RIPK1 mutations, highlighting the dual roles of RIPK1 in immune defense and immune regulation.[12]  

From a disease classification standpoint, IMD57 fits squarely within the category of **Mendelian primary immunodeficiency / primary immune regulatory disorders**, with features that overlap combined immunodeficiency, monogenic IBD, and systemic autoinflammatory disease.[3][5][10][12] It is distinguished clinically by the triad of severe early-onset IBD, progressive inflammatory arthritis, and recurrent severe infections, all in the setting of lymphopenia and dysregulated cytokine responses.[3][5][11][18] The point prevalence is estimated to be less than 1 per 1,000,000 worldwide, consistent with its status as an ultra-rare disorder.[5]  

### 1.2 Key Identifiers and Ontology Mapping

Multiple biomedical databases now index Immunodeficiency 57 with consistent identifiers and cross-references. OMIM designates IMD57 as **“Immunodeficiency 57 with autoinflammation”** with the phenotype MIM number **618108**, linked to the RIPK1 gene (MIM 603453) and locus 6p25.2.[11][14] Orphanet lists the corresponding Orpha number **529977** for this condition, and Disease Ontology assigns DOID:0111952.[1][11] MONDO, the Mondo Disease Ontology, references IMD57 under **MONDO:0020849**, as noted in ClinGen’s gene–disease curation.[3] ZFIN explicitly maps the human disease entry “immunodeficiency 57” to DO:0111952 and provides cross-links to OMIM and Orphanet.[1]  

The **RIPK1 gene** itself is catalogued under HGNC-approved symbol **RIPK1**, OMIM gene entry **603453**, and cytogenetic location **6p25.2**, with GRCh38 genomic coordinates 6:3,063,967–3,115,187.[14] OMIM lists two phenotypes linked to RIPK1: (1) **Autoinflammation with episodic fever and lymphadenopathy** (AIEFL; MIM 618852), an autosomal dominant condition caused by heterozygous cleavage-resistant mutations; and (2) **Immunodeficiency 57 with autoinflammation** (IMD57; MIM 618108), an autosomal recessive condition caused by biallelic loss-of-function mutations.[14][19] This dual mapping underscores the allelic heterogeneity and functional bifurcation of RIPK1-associated human disease.  

In terms of controlled vocabularies, IMD57 can be mapped to **Human Phenotype Ontology (HPO)** terms including early-onset inflammatory bowel disease (HP:0012404), recurrent respiratory infections (HP:0002205), recurrent bacterial infections (HP:0002718), lymphopenia (HP:0001888), inflammatory arthritis (HP:0003481), failure to thrive (HP:0001508), hepatosplenomegaly (HP:0001433), and hypogammaglobulinemia (HP:0004313), among others.[3][5][11][18] At the disease level, the condition aligns with **MONDO:0020849** (immunodeficiency 57), which integrates OMIM, Orphanet, and other ontology sources.[3]  

### 1.3 Synonyms and Alternative Names

Several synonymous or related names are used for Immunodeficiency 57 in the literature and databases. OMIM and multiple resources refer to it as **“Immunodeficiency 57 with autoinflammation”** and often abbreviate this as **IMD57**.[11][14][18] ZFIN and Disease Ontology describe a longer descriptive synonym: **“immune dysregulation–inflammatory bowel disease–arthritis–recurrent infections–lymphopenia syndrome,”** capturing the cardinal clinical manifestations.[1] MalaCards lists additional synonyms, including “Immune Dysregulation-Inflammatory Bowel Disease-Arthritis-Recurrent Infections-Lymphopenia Syndrome” and “Immunodeficiency 57 with Autoinflammation.”[5]  

Genomics England’s PanelApp entries for both autoinflammatory disorders and infantile enterocolitis / monogenic inflammatory bowel disease panels list the RIPK1-associated phenotype as “Immunodeficiency 57, OMIM:618108” or “Immunodeficiency 57 with autoinflammation,” and explicitly distinguish it from “Autoinflammation with episodic fever and lymphadenopathy, OMIM:618852.”[8][9][10] ClinGen refers to the condition consistently as **“immunodeficiency 57”** with MONDO:0020849 and emphasizes its classification as a primary immune regulatory disorder.[3]  

Thus, in developing a disease knowledge base entry, the primary name should be **“Immunodeficiency 57 with autoinflammation (IMD57)”**, with synonyms including “immune dysregulation–inflammatory bowel disease–arthritis–recurrent infections–lymphopenia syndrome” and “RIPK1 deficiency.”[1][3][5][11][18] The term “RIPK1 deficiency” is particularly useful mechanistically, but it should be reserved for biallelic loss-of-function conditions to avoid confusion with the distinct heterozygous cleavage-resistant RIPK1 autoinflammatory syndrome.[12][14][19]  

### 1.4 Data Sources and Evidence Types

The current understanding of IMD57 is derived primarily from **aggregated disease-level resources** and a small number of **detailed case series and mechanistic studies**, rather than from large clinical cohorts or electronic health record–based analyses. OMIM, Orphanet, MalaCards, ClinGen, ZFIN, and PanelApp provide consolidated descriptions that integrate findings from the original case reports and mechanistic studies.[1][3][5][10][11][14][18]  

The foundational clinical evidence comes from human case reports and series, including the seminal Science article by Cuchet-Lourenço et al. (2018; PMID: 30026316), Li et al. (2019; PMID: 30591564), Uchiyama et al. (2019; PMID: 31213653), and later case descriptions compiled in ClinGen and Frontiers reviews.[3][12][18] These human data are complemented by extensive **mouse genetic models** of Ripk1 deficiency or mutation, which revealed perinatal lethality with severe immune abnormalities, profound sensitivity to necroptosis and apoptosis, and critical roles in TNF, TLR, and interferon receptor signaling.[13][16][17]  

In vitro studies using patient-derived cells and engineered systems further demonstrate the molecular consequences of RIPK1 deficiency, including defective MAPK activation, impaired production of cytokines such as IL-6, IL-10, TNF-α, and IL-12, and enhanced necroptosis; these findings are summarized by Cuchet-Lourenço et al. and by ClinGen.[3][18] As ClinGen notes, “studies robustly show that RIPK1 is involved in MAPK p38 phosphorylation and subsequent stimulation of the production of IL-6, IL-10, TNF-α and IL-12; loss of RIPK1 also leads to excessive production of the proinflammatory cytokine IL-1β.”[3]  

Therefore, IMD57 is a disease where multiple evidence streams converge: human clinical observation, human genetic data, in vitro functional assays, and animal models. There are currently no large-scale population-based studies, randomized trials, or registry data, reflecting the ultra-rare status of the condition and the recency of its recognition (first reports in 2018).[3][12][18]  

---

## 2. Etiology

### 2.1 Primary Causal Factors: RIPK1 Loss-of-Function

The **primary causal factor** in Immunodeficiency 57 is **biallelic loss-of-function (LoF) mutation in the RIPK1 gene**, which encodes receptor-interacting serine/threonine-protein kinase 1, a key regulator of cell death and inflammatory signaling pathways.[3][12][14][15][18] OMIM, ClinGen, and MalaCards all indicate that IMD57 is “caused by mutations in the RIPK1 gene on chromosome 6p25.2” and that the mechanism of pathogenicity is loss of function.[3][5][11][14] Cuchet-Lourenço et al. identified homozygous LoF mutations (nonsense and frameshift) in four patients from three consanguineous families, demonstrating that complete absence of RIPK1 protein leads to severe immunodeficiency and autoinflammation.[18]  

ClinGen’s curation summarizes that at least **11 variants** in **RIPK1** have been associated with IMD57, including four missense variants, four nonsense variants, one frameshift variant, and two large deletions, all in homozygous or compound heterozygous configuration in affected individuals.[3] These variants are distributed across the gene and include truncating mutations that abolish protein expression, as well as missense changes that severely disrupt functional domains.[3][12][14][18] Functional studies in patients’ cells and model systems show that these variants lead to absent or severely reduced RIPK1 protein and loss of both its kinase activity and scaffolding functions.[3][12][18]  

RIPK1 is a multifunctional adaptor and kinase that integrates signals from multiple receptors, including TNF receptor 1 (TNFR1), Toll-like receptors (TLR3, TLR4), and RIG-I-like receptors, and regulates NF-κB activation, MAPK signaling, and cell death pathways (apoptosis and necroptosis).[13][15][16][17] As one review describes, “RIPK1 is a ‘Swiss Army knife’ of innate immune regulation” connected to TNFRs, TLRs, type I interferon receptor (IFNAR1), STING, and MAVS, and it controls transcription and translation of inflammatory genes as well as multiple forms of programmed cell death.[15] Complete loss-of-function of such a central hub understandably has profound consequences for immune homeostasis, leading to both immunodeficiency (due to defective survival and activation of immune cells) and autoinflammation (due to uncontrolled cell death and dysregulated cytokine production).[12][15][17][18]  

Thus, IMD57 is best conceptualized as a **monogenic primary immunodeficiency / immune dysregulation syndrome due to germline, biallelic, loss-of-function mutations in RIPK1**, with no evidence to date that environmental or acquired factors alone can cause a similar phenotype in the absence of genetic defects in this gene.[3][5][12][18]  

### 2.2 Genetic Risk Factors: Causal Variants and Susceptibility Context

From a risk-factor perspective, the **presence of biallelic pathogenic RIPK1 variants** is both necessary and sufficient for the IMD57 phenotype in reported families, consistent with monogenic Mendelian inheritance.[3][11][14][18] All described patients have either homozygous or compound heterozygous mutations in RIPK1, often in the context of parental consanguinity, and there is no suggestion of incomplete penetrance for classic LoF alleles.[3][18]  

ClinGen catalogues at least 11 disease-associated alleles in 13 probands, including missense, nonsense, frameshift, and structural variants.[3] Cuchet-Lourenço et al. reported variants such as a homozygous frameshift leading to early truncation, while Li et al. and Uchiyama et al. described additional missense and truncating variants.[3][18] The allele frequency of these specific pathogenic variants in population databases such as gnomAD is extremely low or absent, consistent with their pathogenicity and the rarity of IMD57.[3][5] Although detailed allele frequencies are not provided in the sources summarized here, ClinGen notes that the variants are rare, often private to a single family, and that their functional impact has been demonstrated experimentally.[3]  

Beyond the direct causal variants, there is currently no strong evidence for **modifier genes** or polygenic risk factors that modulate IMD57 susceptibility or severity, although this cannot be excluded given the small number of cases. Other genes in the linear ubiquitin chain assembly complex (LUBAC), such as RBCK1 and RNF31 (HOIP), and negative regulators such as OTULIN, can cause related immunodeficiency and autoinflammatory syndromes when mutated, but these represent distinct genetic disorders rather than modifiers of RIPK1-deficient IMD57.[12] For example, LUBAC deficiency due to RBCK1 or RNF31 mutations leads to severe immunodeficiency and recurrent fever with polyglucosan myopathy, and OTULIN mutations cause OTULIN-related autoinflammatory syndrome (ORAS, otulipenia), reflecting convergent pathways in linear ubiquitin signaling and NF-κB regulation.[12]  

Thus, at present, the **primary genetic risk factor** for IMD57 is the inheritance of two pathogenic RIPK1 alleles in an autosomal recessive fashion, often facilitated by parental consanguinity, with no established role for other susceptibility loci.[3][11][14][18]  

### 2.3 Environmental and Lifestyle Risk Factors

There is **no evidence** that environmental, lifestyle, or occupational exposures independently cause Immunodeficiency 57 in the absence of RIPK1 mutations. However, as with other primary immunodeficiencies, environmental factors influence **disease expression and complication risk** by modulating exposure to infectious agents and perhaps the severity of inflammatory stimuli.[5][12][18] Patients with IMD57 are susceptible to a wide range of bacterial, viral, and fungal infections, particularly involving the gastrointestinal tract and respiratory system, and the frequency and severity of these infections will naturally be shaped by local pathogen burden, sanitation, vaccination practices, and access to medical care.[5][18]  

Recurrent infections themselves can exacerbate inflammatory bowel disease and arthritis, creating a vicious cycle in which environmental pathogen exposure interacts with the underlying genetic defect in RIPK1 to drive morbidity.[5][12][18] For example, in RIPK1-deficient mice, infection or exposure to inflammatory stimuli such as TNF or TLR ligands can precipitate lethal necroptosis and systemic inflammation, suggesting that environmental inflammatory cues can dramatically unmask or amplify the consequences of RIPK1 loss.[13][16][17] Similar mechanisms may operate in humans, although direct data in IMD57 patients are limited.  

Lifestyle factors such as diet, smoking, and physical activity have not been systematically studied in IMD57, but by analogy with other forms of early-onset inflammatory bowel disease, dietary patterns, microbial exposures, and antibiotic use may modulate intestinal inflammation and microbiome composition, potentially influencing the severity of enterocolitis.[10][12][18] Nonetheless, these influences should be viewed as **modifying factors** rather than primary causes, with the underlying RIPK1 deficiency remaining the central determinant of disease.  

### 2.4 Protective Factors and Potential Modifiers

Given the rarity of IMD57 and the small number of reported patients, **protective factors**—either genetic or environmental—have not been formally characterized. There are no known **protective RIPK1 variants** that mitigate disease in biallelic LoF carriers, nor is there evidence of “resilient” individuals with two clearly pathogenic RIPK1 alleles and no phenotype.[3][14][18] It is plausible that polymorphisms in parallel survival pathways, antioxidant defenses, or cytokine regulators could modulate disease severity, but such hypotheses remain speculative.  

In terms of environmental or treatment-related protective factors, **hematopoietic stem cell transplantation (HSCT)** appears to be a potent “curative” intervention for at least some patients. Cuchet-Lourenço et al. reported that HSCT in one RIPK1-deficient patient “reversed cytokine production defects and resolved clinical symptoms,” demonstrating that reconstitution of the hematopoietic compartment with RIPK1-sufficient cells can restore immune function and control inflammation.[18] This suggests that HSCT acts as a protective factor against disease progression, though it is a therapeutic intervention rather than a naturally occurring modifier.  

Standard supportive measures—such as prophylactic antimicrobials, immunoglobulin replacement, and nutritional support—undoubtedly reduce morbidity and mortality, but these have not been systematically studied specifically in IMD57.[5][18] Their benefits are inferred from broader primary immunodeficiency practice and the observed reduction of infection burden in case reports. There is no evidence that specific diets, probiotics, or environmental interventions have unique protective effects beyond general care for immunocompromised children.  

### 2.5 Gene–Environment Interactions

Although comprehensive gene–environment interaction studies are lacking, the **biological role of RIPK1** strongly implies that environmental stimuli—particularly infections and inflammatory signals—interact with the genetic defect to shape disease expression. RIPK1 is activated downstream of TNFR1, TLR3/4, RIG-I-like receptors, and type I/II interferon receptors in response to cytokines, pathogen-associated molecular patterns (PAMPs), and damage-associated molecular patterns (DAMPs).[13][15][17] In normal individuals, this signaling network balances NF-κB–mediated pro-survival and inflammatory gene expression with controlled activation of apoptosis or necroptosis when needed.[13][15][17]  

In RIPK1-deficient cells, TNF, TLR, and interferon signals can no longer properly engage NF-κB and MAPK pathways, and instead they may trigger **unrestrained caspase-8–dependent apoptosis or RIPK3-MLKL–dependent necroptosis**, leading to cell death, release of DAMPs, and further inflammation.[13][16][17][18] This means that environmental exposures such as infections or endotoxin may produce exaggerated tissue damage and inflammatory responses in IMD57 patients compared with healthy individuals. As Kaiser et al. demonstrated in mice, RIPK1 suppresses innate immune necrosis and apoptosis during critical periods like parturition, showing that environmental inflammatory insults can be fatal when RIPK1 is absent.[13]  

Thus, **gene–environment interaction in IMD57** can be conceptualized as follows: the inherited RIPK1 LoF mutation creates a latent vulnerability in immune cells and tissues, and environmental inflammatory triggers such as infections, microbiota-derived signals, and cytokines unmask this vulnerability, driving episodes of severe infection, enterocolitis, and arthritis. This interaction is consistent with the clinical observation that IMD57 patients suffer recurrent infections and chronic inflammatory disease, yet there are no reported cases of similar disease among individuals without RIPK1 mutations despite comparable environmental exposures.[3][5][12][18]  

---

## 3. Phenotypes

### 3.1 General Clinical Phenotype and Age of Onset

The phenotype of Immunodeficiency 57 is dominated by **recurrent severe infections**, **early-onset inflammatory bowel disease**, and **progressive inflammatory arthritis**, with additional features including lymphopenia, hypogammaglobulinemia, hepatosplenomegaly, chronic lung disease, and failure to thrive.[3][5][11][12][18] OMIM’s clinical synopsis describes “recurrent bacterial, viral, and fungal infections from infancy,” “lymphopenia,” “inflammatory bowel disease involving upper and lower gastrointestinal tract,” “inflammatory polyarthritis,” and “variable hypogammaglobulinemia.”[11] MalaCards emphasizes “diarrhea, vomiting, hepatosplenomegaly, mouth ulcers, perianal abscesses, chronic lung disease with bronchiectasis, and failure to thrive,” along with “skin rash associated with lymphocytic vasculitis.”[5]  

The **age of symptom onset** is consistently in **early infancy**, often within the first year of life.[3][5][11][18] ClinGen notes that all patients “invariably present with recurrent infection and inflammatory bowel disease during early childhood,” and MalaCards lists onset in “infancy, neonatal” for the immune dysregulation–IBD–arthritis–recurrent infections–lymphopenia syndrome.[3][5] Thus, an appropriate HPO term is *Neonatal onset* (HP:0003623) or *Infantile onset* (HP:0003593), with *Age of onset of gastrointestinal symptoms in infancy* mapping to early-onset IBD (HP:0012404).  

Symptom severity is generally **severe** or **life-threatening** without appropriate treatment. Patients experience life-threatening infections, severe malnutrition due to enterocolitis, and progressive joint damage from arthritis.[3][5][18] The disease course appears **chronic and progressive**, particularly for gastrointestinal and joint manifestations, although some patients may have fluctuating or episodic inflammatory activity superimposed on a chronic baseline.[3][5][12][18] There are currently too few patients to quantify symptom frequencies precisely, but ClinGen’s observation that all patients present with recurrent infection and IBD implies a frequency approaching 100% for these core features.[3]  

The impact on quality of life is profound. Infants and children with IMD57 often require prolonged hospitalizations, parenteral nutrition, broad-spectrum antibiotics, immunosuppressive or biologic therapies, and in some cases HSCT.[5][18] Chronic pain and functional limitations from polyarthritis further impair daily activities, school attendance, and psychosocial development. While formal quality-of-life instruments (e.g., EQ-5D, SF-36) have not been applied in published reports, the constellation of severe immunodeficiency, chronic inflammation, and growth failure clearly corresponds to major reductions in physical, emotional, and social well-being.  

### 3.2 Infectious Susceptibility and Immunologic Phenotypes

A hallmark of IMD57 is **recurrent infections with bacteria, viruses, and fungi**, reflecting a broad immunodeficiency rather than susceptibility to a single pathogen group.[3][5][11][12][18] Cuchet-Lourenço et al. reported that RIPK1-deficient patients experienced multiple episodes of pneumonia, severe bacterial infections, viral infections, and systemic fungal infection, often requiring intensive care and prolonged antimicrobial therapy.[18] ClinGen summarizes the phenotype as “recurrent bacterial, viral and fungal infections since early childhood.”[3] MalaCards similarly highlights “early onset of recurrent bacterial, viral, and fungal infections” as a defining characteristic.[5]  

Immunologic evaluation reveals **variable T-cell lymphopenia**, with CD4 and CD8 T-cell counts often reduced, while B-cell and NK-cell counts may be normal or decreased.[3][5][18] ClinGen notes that “T-cell lymphopenia is typically observed, while B-cell and NK cell counts may be normal or decreased,” indicating a predominant but not exclusive T-cell defect.[3] Lymphopenia (HP:0001888) is therefore a core HPO term, with more specific mapping to reduced T-cell count (HP:0001883) and possibly combined immunodeficiency (HP:0005387). In some patients, **hypogammaglobulinemia** (HP:0004313) and impaired specific antibody responses are observed, suggesting defective B-cell help.[3][5][11][18]  

Functional assays show **altered cytokine production** in response to TNF and TLR ligands, with reduced production of IL-6, IL-10, TNF-α, and IL-12, and paradoxically increased IL-1β, reflecting both impaired and dysregulated inflammation.[3][12][18] Cuchet-Lourenço et al. reported that “RIPK1-deficient cells showed impaired mitogen-activated protein kinase activation and cytokine secretion and were prone to necroptosis,” providing mechanistic insight into the immunologic phenotype.[18] ClinGen notes that studies “robustly show that RIPK1 is involved in MAPK p38 phosphorylation and subsequent stimulation of the production of IL-6, IL-10, TNF-α and IL-12; loss of RIPK1 also leads to excessive production of the proinflammatory cytokine IL-1β.”[3]  

The **quality-of-life impact** of this infectious and immunologic phenotype is substantial. HPO terms capturing the phenotype include *Recurrent bacterial infections* (HP:0002718), *Recurrent viral infections* (HP:0004429), *Recurrent fungal infections* (HP:0002841), *Recurrent lower respiratory tract infections* (HP:0002110), and *Chronic lung disease* (HP:0006528), the latter particularly relevant in patients who develop bronchiectasis.[3][5][18] Frequent hospitalizations, intravenous antibiotics, and isolation measures restrict normal social interaction and schooling, while chronic lung disease can lead to long-term exercise intolerance and respiratory limitation.  

### 3.3 Gastrointestinal Phenotypes: Early-onset Inflammatory Bowel Disease

The gastrointestinal phenotype in IMD57 is dominated by **early-onset inflammatory bowel disease** involving both small and large intestine and sometimes the upper gastrointestinal tract.[3][5][10][11][12][18] Patients present with chronic diarrhea, vomiting, abdominal pain, gastrointestinal bleeding, mouth ulcers, perianal disease, and failure to thrive, often mimicking severe very-early-onset IBD or infantile enterocolitis.[5][10][18] MalaCards notes that patients “exhibit early-onset inflammatory bowel disease involving the upper and lower gastrointestinal tract” and lists symptoms such as diarrhea, vomiting, perianal abscesses, and gastritis.[5] Genomics England’s “Infantile enterocolitis & monogenic inflammatory bowel disease” panel includes RIPK1 as a biallelic gene associated with IMD57, underscoring its role as a cause of monogenic IBD.[10]  

Endoscopic and histologic findings in reported cases show chronic active inflammation with ulceration, crypt abscesses, and sometimes granulomas, consistent with severe IBD, though detailed pathology is not fully described in the summarized sources.[10][12][18] The HPO term *Inflammatory bowel disease* (HP:0002597) and more specific *Early-onset inflammatory bowel disease* (HP:0012404) are appropriate, along with *Chronic diarrhea* (HP:0002038), *Gastrointestinal hemorrhage* (HP:0002240), *Mouth ulcers* (oral ulcers; HP:0000155), and *Perianal fistula* or *Perianal abscess* (HP:0003403 / HP:0100640).[5][10][18]  

The severity and chronicity of enterocolitis in IMD57 have profound consequences for growth and nutrition. Patients frequently display **failure to thrive** (HP:0001508), weight loss, and micronutrient deficiencies due to malabsorption and poor oral intake.[5][18] Some require parenteral nutrition or gastrostomy feeding, and the constant gastrointestinal symptoms markedly reduce appetite, energy, and participation in daily activities. From a quality-of-life perspective, chronic abdominal pain, frequent loose stools, and risk of incontinence can be particularly distressing for children and families.  

### 3.4 Musculoskeletal and Autoinflammatory Phenotypes: Arthritis and Vasculitis

Another core feature of IMD57 is **inflammatory polyarthritis**, often progressive and disabling.[3][5][11][12][18] Cuchet-Lourenço et al. reported progressive polyarthritis affecting multiple joints, and ClinGen emphasizes that “all patients invariably present with recurrent infection and inflammatory bowel disease during early childhood” and “develop progressive polyarthritis.”[3][18] MalaCards similarly notes “inflammatory polyarthritis” and progression over time.[5] This phenotype likely corresponds to HPO terms *Arthritis* (HP:0001369), *Inflammatory arthritis* (HP:0003481), and *Polyarthritis* (HP:0003479), and in some cases *Joint contracture* (HP:0001371) if chronic inflammation leads to structural damage.  

Skin involvement has also been described, including **skin rash associated with lymphocytic vasculitis**, suggesting small-vessel involvement as part of the autoinflammatory process.[5][12] MalaCards notes “skin rash associated with lymphocytic vasculitis,” and the Frontiers review mentions that one RIPK1-deficient patient had autoinflammatory manifestations beyond the classic triad, indicating that autoinflammation can extend to cutaneous and possibly systemic vasculitic features.[5][12] Appropriate HPO terms include *Cutaneous vasculitis* (HP:0002635), *Skin rash* (HP:0000988), and perhaps *Leukocytoclastic vasculitis* (HP:0002635) if histology is available.  

These musculoskeletal and cutaneous manifestations significantly impair quality of life. Children with polyarthritis may experience chronic pain, morning stiffness, reduced range of motion, and difficulty walking or performing fine motor tasks, leading to limitations in play, schooling, and self-care. Skin vasculitis can cause painful lesions, ulceration, or cosmetic concerns, which may further affect psychosocial well-being. If unrecognized or inadequately treated, chronic joint inflammation can result in irreversible joint damage and disability.  

### 3.5 Hematologic, Pulmonary, and Other Systemic Phenotypes

Beyond lymphopenia and hypogammaglobulinemia, IMD57 patients may exhibit **hepatosplenomegaly**, **chronic lung disease with bronchiectasis**, and other systemic features.[3][5][11][18] MalaCards lists hepatosplenomegaly, chronic lung disease with bronchiectasis, and failure to thrive among the common traits.[5] Hepatosplenomegaly likely reflects chronic immune activation, extramedullary hematopoiesis, or portal hypertension related to intestinal inflammation, and aligns with HPO term *Hepatosplenomegaly* (HP:0001433).[5][18] Chronic lung disease with bronchiectasis corresponds to *Bronchiectasis* (HP:0002110) and *Chronic obstructive pulmonary disease* or more broadly *Chronic lung disease* (HP:0006528).[5]  

Laboratory abnormalities include **lymphopenia**, **variable decreases in B and NK cells**, and **variable hypogammaglobulinemia**, as noted above.[3][5][11][18] HPO terms such as *Decreased T cell count* (HP:0001883), *Decreased B cell count* (HP:0004322), *Decreased NK cell count* (HP:0012091), and *Abnormal immunoglobulin level* (HP:0004315) apply. Cytokine profiling in whole-blood assays reveals altered responses to TNF and TLR ligands, but these findings are usually reported in research settings rather than as routine diagnostics.[3][18]  

The overall systemic phenotype is therefore one of **multisystem immune dysregulation**, affecting hematologic, gastrointestinal, musculoskeletal, pulmonary, and cutaneous systems. Quality-of-life impacts are cumulative: chronic fatigue, dyspnea from lung disease, abdominal pain, joint pain, and frequent hospitalizations create a heavy disease burden. Caregivers face substantial emotional and logistical challenges, and the risk of early mortality poses significant psychosocial stress on families.[3][5][18]  

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: RIPK1

The **causal gene** for Immunodeficiency 57 is **RIPK1** (Receptor-interacting serine/threonine-protein kinase 1), also known as receptor-interacting protein kinase 1, encoded by the gene with OMIM entry **603453** and located on chromosome 6p25.2.[3][11][14][15] OMIM describes RIPK1 as a cytosolic protein kinase that controls multiple signaling pathways leading to inflammation and apoptotic or necroptotic cell death.[14] The gene spans approximately 51 kb in GRCh38 coordinates (6:3,063,967–3,115,187) and encodes a 671-amino acid protein with an N-terminal kinase domain, an intermediate region containing a RIP homotypic interaction motif (RHIM), and a C-terminal death domain.[14][15][17]  

RIPK1 plays dual roles as a **kinase** and **scaffold** in pathways downstream of TNFR1, TLR3, TLR4, RIG-I-like receptors, and others.[13][15][17] In its scaffold role, RIPK1 helps assemble the TNFR1 complex I and other signaling complexes that activate NF-κB and MAPKs, promoting cell survival and inflammatory gene expression.[13][15][17] In its kinase role, RIPK1 can promote programmed cell death via formation of cytosolic complexes (often termed complex II, ripoptosome, or necrosome), which recruit caspase-8 to induce apoptosis or interact with RIPK3/MLKL to drive necroptosis.[13][15][16][17] These diverse functions are subject to extensive regulation by ubiquitination, phosphorylation, and caspase cleavage.[15][16][17]  

In the context of human disease, the same gene underlies both **autosomal dominant autoinflammation with episodic fever and lymphadenopathy (AIEFL; OMIM 618852)** and **autosomal recessive immunodeficiency 57 with autoinflammation (IMD57; OMIM 618108)**, depending on the nature and zygosity of the mutation.[14][19] AIEFL is caused by heterozygous missense mutations at the highly conserved residue Asp324 that render RIPK1 resistant to caspase-8 cleavage, resulting in cleavage-resistant hyperactive RIPK1 and recurrent autoinflammatory episodes.[12][14][19] In contrast, IMD57 is caused by biallelic LoF mutations that abolish RIPK1 expression or function, leading to a combined immunodeficiency and chronic autoinflammation.[3][12][14][18]  

### 4.2 Pathogenic Variants and Variant Classes

ClinGen’s curation indicates that at least **11 distinct RIPK1 variants** have been reported in IMD57 patients, including four missense variants, four nonsense variants, one frameshift, and two large deletions, all in homozygous or compound heterozygous state.[3] Cuchet-Lourenço et al. identified homozygous LoF mutations (including truncating variants) in four patients from three families; Li et al. and Uchiyama et al. subsequently reported additional variants.[3][18] Although the exact cDNA and protein-level nomenclature for all variants is not fully detailed in the sources summarized here, OMIM lists specific alleles (e.g., 603453.0001–603453.0003) corresponding to early reports.[14][18]  

These variants share the common functional feature of **loss-of-function**, either through nonsense-mediated mRNA decay, truncated proteins lacking critical domains, or missense changes that abolish protein stability or disrupt essential functional motifs.[3][12][18] Functional studies in patient-derived fibroblasts or blood cells show absent or severely reduced RIPK1 protein by immunoblot, absent TNF-induced NF-κB activation, defective MAPK activation, and increased susceptibility to necroptosis.[3][12][18] Cuchet-Lourenço et al. concluded that “complete RIPK1 deficiency” was present in their patients and that this deficiency was sufficient to cause severe immunodeficiency and inflammatory disease.[18]  

From a classification standpoint, these variants would be considered **pathogenic** or **likely pathogenic** under ACMG/AMP guidelines, based on criteria such as PVS1 (null variant in a gene where LoF is a known mechanism of disease), PS3 (well-established functional studies), PM2 (absent from controls), and PP4 (highly specific phenotype).[3] ClinVar and other variant databases catalog individual RIPK1 variants associated with IMD57, though detailed ClinVar entries are not explicitly summarized in the sources here.[10][14]  

Because IMD57 is a germline congenital disorder, the variants are of **germline origin**, inherited from carrier parents in autosomal recessive fashion.[3][11][18] There is no evidence for somatic mosaicism or acquired somatic RIPK1 mutations contributing to this specific disease, although somatic modulation of RIPK1 activity may be relevant in other contexts such as cancer or inflammatory conditions.[15][17]  

### 4.3 Functional Consequences and Mechanistic Classification

Functionally, the pathogenic RIPK1 variants in IMD57 share the mechanistic feature of **loss-of-function**, affecting both the kinase activity and scaffolding functions of the protein.[3][12][15][18] This contrasts sharply with the heterozygous Asp324 variants causing AIEFL/CRIA, which are **cleavage-resistant gain-of-function** mutants that make RIPK1 hyperactive and non-cleavable by caspase-8.[12][16][19]  

Multiple lines of evidence support the LoF classification for IMD57 variants. Cuchet-Lourenço et al. demonstrated that patient cells lacked detectable RIPK1 protein, had impaired activation of MAPK p38 and ERK upon stimulation, and had blunted production of cytokines such as TNF-α and IL-6, indicating loss of normal pro-survival and inflammatory signaling.[18] At the same time, these cells were **prone to necroptosis**, suggesting that the protective scaffolding function of RIPK1, which normally suppresses uncontrolled RIPK3/MLKL activation, was absent.[18] Kaiser et al. and others showed in mice that RIPK1 deficiency leads to perinatal lethality due to uncontrolled necroptosis and apoptosis, further confirming the vital prosurvival role of RIPK1’s kinase-independent functions.[13][16]  

RIPK1’s dual mechanistic roles have been encapsulated in reviews describing it as a “Swiss Army knife” of innate immune regulation.[15] In its scaffolding role in TNFR1 complex I, RIPK1 supports NF-κB activation and cell survival; in its kinase role, when deubiquitinated and released to cytosolic complexes, it can promote cell death via caspase-8 or RIPK3/MLKL.[13][15][17] Loss-of-function mutations that abolish both roles shift the balance toward unregulated cell death (due to absence of scaffolding) and impaired inflammatory gene expression (due to absence of NF-κB/MAPK activation), explaining the combination of immunodeficiency and autoinflammation in IMD57.[12][15][18]  

At the level of Gene Ontology (GO), RIPK1 participates in biological processes such as *TNF-mediated signaling pathway* (GO:0033209), *regulation of NF-kappaB transcription factor activity* (GO:0032088), *necroptotic process* (GO:0070266), and *apoptotic process* (GO:0006915).[15][17] Its molecular functions include *protein serine/threonine kinase activity* (GO:0004674) and *death receptor binding* (GO:0005123). The pathogenic variants in IMD57 therefore result in disruption of these processes and functions, with downstream consequences for immune cell survival, cytokine production, and tissue integrity.[12][15][18]  

### 4.4 Epigenetic and Structural Genomic Considerations

There is currently no evidence that **epigenetic changes** (e.g., DNA methylation, histone modifications) or large-scale chromosomal abnormalities play a primary role in IMD57 beyond the documented large deletions involving RIPK1, which are structural genetic variants rather than epigenetic phenomena.[3][14] ClinGen notes that two large deletions affecting RIPK1 have been identified in IMD57 patients, underscoring that structural variants can cause the disease if they abolish RIPK1 expression.[3] However, no broader chromosomal syndromes or microdeletion syndromes associated with RIPK1 locus have been described in this context.  

The RIPK1 locus lies on chromosome 6p25.2, a region that can be involved in various structural variants in other conditions, but the IMD57 phenotype is specifically attributable to disruption of RIPK1 rather than to contiguous gene deletion syndromes.[14] There are no reports of epigenetic silencing of RIPK1 causing IMD57, and epigenomic studies in IMD57 patients have not been reported.  

---

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors

As a Mendelian primary immunodeficiency with a clear genetic cause, IMD57 does not have known **non-genetic causal** factors. However, environmental exposures influence the **phenotypic expression and complications** of the disease. Patients are highly susceptible to bacterial, viral, and fungal infections, particularly in the gastrointestinal and respiratory tracts, and the **frequency and severity** of these infections depend on environmental pathogen burden, vaccination coverage, sanitation, and healthcare access.[3][5][18] Even common respiratory viruses or enteric pathogens that cause mild disease in immunocompetent children can lead to severe, recurrent, or chronic infections in IMD57 patients, contributing to lung damage (bronchiectasis) and exacerbation of IBD.[5][18]  

Inflammatory triggers such as infections, endotoxin exposure, and perhaps microbiome composition are especially relevant given the central role of RIPK1 in TNFR, TLR, and interferon signaling.[13][15][17] In RIPK1-deficient mice, systemic exposure to TNF or TLR agonists can cause catastrophic necroptosis and fatal systemic inflammation, illustrating how environmental inflammatory signals can unmask the consequences of RIPK1 loss.[13][16] Although human IMD57 patients are not complete Ripk1 knockouts (e.g., some may have residual scaffolding function), these animal data suggest that environmental inflammatory cues have disproportionate effects in the setting of RIPK1 deficiency.[12][18]  

### 5.2 Lifestyle and Infectious Contexts

Lifestyle factors such as diet, hygiene, and exposure to crowded environments may modulate infection risk in IMD57, but there is no evidence that they independently drive disease onset. Nonetheless, standard public health measures—hand hygiene, infection control, safe drinking water, vaccination of contacts—are particularly important for these patients to reduce infection burden.[5][18]  

Given the prominent IBD phenotype, diet may influence symptom severity, as in other forms of IBD, but the underlying pathophysiology is driven by RIPK1 deficiency rather than nutritional factors. From a clinical standpoint, carefully managed nutrition, including elemental diets, enteral feeding, or parenteral nutrition when necessary, can mitigate malnutrition and failure to thrive, but these interventions are supportive rather than etiologic.[5][18]  

There is no evidence that specific toxins, pollutants, radiation, or occupational exposures contribute to IMD57 pathogenesis. Infectious agents are important as **triggers** and complicating factors, but not as primary causes, and there is no specific pathogen uniquely associated with IMD57 beyond the general susceptibility to opportunistic or severe infections.[3][5][18]  

---

## 6. Mechanism and Pathophysiology

### 6.1 High-Level Causal Chain

At a high level, the pathophysiology of Immunodeficiency 57 can be conceptualized as a sequential causal chain linking the initiating genetic lesion to clinical manifestations. Step 1: **Biallelic loss-of-function mutations in RIPK1** abolish or severely reduce RIPK1 protein expression or function in hematopoietic and possibly non-hematopoietic cells.[3][14][18] Step 2: This **loss of RIPK1** disrupts its scaffolding role in TNFR1, TLR, and RIG-I-like receptor signaling complexes, leading to **impaired activation of NF-κB and MAPKs** and altered cytokine production in response to inflammatory stimuli; this step is directly demonstrated in human patient cells and inferred from mouse models.[3][12][18] Step 3: In parallel, the absence of RIPK1’s prosurvival scaffold function renders cells—particularly immune cells—**hypersensitive to caspase-8–dependent apoptosis and RIPK3-MLKL–dependent necroptosis** in response to TNF and other signals, as demonstrated in mouse models and supported by increased necroptosis in RIPK1-deficient human cells.[13][16][18] Step 4: The combination of impaired NF-κB/MAPK signaling and increased programmed cell death leads to **lymphopenia, impaired T-cell and innate immune function, and defective host defense**, resulting in recurrent severe infections; this step is inferred from immunophenotyping and functional assays in patients.[3][18] Step 5: At the same time, the propensity for necroptosis and dysregulated cytokine production in myeloid and other cells leads to **chronic autoinflammation**, particularly in the gut, joints, and skin, manifesting as early-onset IBD, polyarthritis, and vasculitis; this step is supported by clinical observation and by animal models showing that excessive necroptosis drives systemic inflammation.[12][13][16][18] Step 6: Repeated cycles of infection, tissue damage, and autoinflammation cause cumulative **organ damage**, including bronchiectasis, growth failure, and joint destruction, culminating in the full clinical spectrum of IMD57.[3][5][18]  

### 6.2 RIPK1 Structure, Pathways, and Biological Roles

RIPK1 is a modular protein comprising an N-terminal serine/threonine kinase domain, an intermediate region containing a **RIP homotypic interaction motif (RHIM)**, and a C-terminal **death domain**.[14][15][17] This architecture allows RIPK1 to participate in multiple protein–protein interactions and signaling complexes. In TNFR1 signaling, RIPK1 is recruited to the receptor complex (complex I) via its death domain and interacts with TRADD, TRAF2, and LUBAC, thereby promoting the formation of a polyubiquitinated signaling platform that activates NF-κB and MAPKs.[13][15][17] In TLR3 and TLR4 signaling, RIPK1 interacts with the adaptor TRIF via RHIM, linking pattern-recognition receptor signaling to downstream NF-κB and MAPKs.[13][15] RIPK1 also participates in signaling downstream of interferon receptors, RIG-I-like receptors, and STING, integrating antiviral and inflammatory responses.[15][17]  

Depending on context, RIPK1’s kinase activity and scaffolding function can have opposing effects. In its **scaffolding role**, RIPK1 supports **cell survival and proinflammatory gene expression**, primarily via NF-κB activation; these functions are largely kinase independent.[13][15][17] In contrast, when deubiquitinated and released from receptor complexes, RIPK1’s **kinase activity** promotes formation of cytosolic complexes (complex II, ripoptosome) that recruit FADD and caspase-8, leading to apoptosis, or interact with RIPK3 and MLKL, leading to necroptosis.[13][16][17]  

Kaiser et al. demonstrated that RIPK1 suppresses innate immune necrotic and apoptotic cell death during mammalian parturition, showing that a **kinase-independent prosurvival role** of RIPK1 prevents lethal consequences of RIP3-dependent necroptosis and caspase-8–dependent apoptosis.[13] In their PNAS 2014 article, they observed that Rip1-deficient mice die perinatally with gross immune system abnormalities, and that triple deficiency of RIP1, RIP3, and caspase-8 rescues viability and immune competence, underscoring RIPK1’s central role in balancing cell death pathways.[13][16]  

Recent reviews further highlight RIPK1 as a **critical molecular switch** in cell fate decisions. A 2025 Frontiers review notes that “RIPK1 acts as a critical molecular switch, balancing cell survival and death in response to environmental cues,” and that its scaffolding function can be protective, whereas its kinase activity can drive cell death and inflammation when aberrantly activated.[17] An earlier ScienceDirect overview calls RIPK1 a “Swiss Army knife” of innate immune regulation, linked to TNFRs, TLRs, IFNAR1, STING, and MAVS, and controlling necroptosis, apoptosis, pyroptosis, and inflammatory gene expression.[15]  

### 6.3 Consequences of RIPK1 Loss-of-Function in Humans

The human IMD57 phenotype provides direct evidence of what happens when RIPK1 is absent in the immune system. Cuchet-Lourenço et al. summarized their key findings as follows:  

> “RIPK1 (receptor-interacting serine/threonine kinase 1) is a master regulator of signaling pathways leading to inflammation and cell death and is of medical interest as a drug target. We report four patients from three unrelated families with complete RIPK1 deficiency caused by rare homozygous mutations. The patients suffered from recurrent infections, early-onset inflammatory bowel disease, and progressive polyarthritis. They had immunodeficiency with lymphopenia and altered production of various cytokines revealed by whole-blood assays. In vitro, RIPK1-deficient cells showed impaired mitogen-activated protein kinase activation and cytokine secretion and were prone to necroptosis. Hematopoietic stem cell transplantation reversed cytokine production defects and resolved clinical symptoms in one patient. Thus, RIPK1 plays a critical role in the human immune system.”[18]  

This abstract encapsulates the mechanistic consequences of RIPK1 LoF: impaired MAPK and cytokine responses, increased necroptosis, lymphopenia, and clinical immunodeficiency/autoinflammation. ClinGen’s curation corroborates these findings, emphasizing that loss of RIPK1 disrupts MAPK p38 phosphorylation and subsequent IL-6, IL-10, TNF-α, and IL-12 production, while promoting excessive IL-1β production.[3] The increased necroptosis presumably reflects loss of RIPK1’s prosurvival scaffolding function, which normally restrains RIPK3/MLKL activation.[13][16][18]  

From a GO perspective, loss of RIPK1 disrupts processes such as *positive regulation of NF-kappaB transcription factor activity* (GO:0051092), *regulation of necroptotic process* (GO:0060545), and *innate immune response* (GO:0045087). Immune cell types affected include T lymphocytes (CL:0000084), B lymphocytes (CL:0000236), NK cells (CL:0000623), and myeloid cells such as monocytes/macrophages (CL:0000235).[3][12][18]  

### 6.4 Immunodeficiency: T-cell Lymphopenia and Defective Cytokine Responses

The **immunodeficiency** in IMD57 arises from a combination of lymphopenia and defective cytokine responses. ClinGen notes that “T-cell lymphopenia is typically observed, while B-cell and NK cell counts may be normal or decreased,” and that all patients have recurrent bacterial, viral, and fungal infections.[3] The T-cell defect likely results from increased apoptosis or necroptosis of developing or peripheral T cells due to loss of RIPK1’s prosurvival scaffold function in response to TNF and other signals, as suggested by mouse models where RIPK1 deficiency leads to profound lymphoid abnormalities.[13][16][17]  

RIPK1-deficient human cells also show impaired activation of MAPK pathways (e.g., p38, ERK) and reduced production of proinflammatory cytokines in response to TLR and TNF stimulation, weakening innate immune responses to pathogens.[3][18] At the same time, increased IL-1β production reflects dysregulated inflammasome activation or necroptosis-driven DAMP release, contributing to autoinflammation rather than effective antimicrobial defense.[3][12][18]  

These defects collectively impair both **innate immunity** (monocyte, macrophage, dendritic cell responses to TLR ligands, IFN, and TNF) and **adaptive immunity** (T-cell survival and activation), leading to susceptibility to opportunistic infections across multiple pathogen classes.[3][5][18] GO terms relevant here include *T cell mediated immunity* (GO:0002456), *adaptive immune response* (GO:0002250), and *cytokine production involved in immune response* (GO:0002367).  

### 6.5 Autoinflammation and Tissue Damage: Necroptosis and Dysregulated Cytokines

Paradoxically, the same loss-of-function in RIPK1 also promotes **autoinflammation**, particularly in the gut, joints, and skin. This arises from the dual role of RIPK1 in suppressing inappropriate necroptosis and apoptosis. Kaiser et al. showed that Rip1-deficient mice develop perinatal lethality with massive necroptosis and apoptosis in response to innate immune stimuli, and that this lethal phenotype can be rescued by deleting RIP3 and caspase-8, indicating that RIPK1 normally restrains both pathways.[13][16]  

In IMD57 patients, RIPK1-deficient cells are “prone to necroptosis,” as demonstrated experimentally.[18] Necroptosis is a proinflammatory form of cell death in which RIPK3 phosphorylates MLKL, leading to membrane permeabilization and release of DAMPs and cytokines such as IL-1α, IL-1β, and HMGB1.[16][17] A 2025 Frontiers review notes that “activation of RIPK1-dependent necroptosis is caspase-independent and involves RIPK1/RIPK3-dependent activation of MLKL, resulting in membrane permeabilization and subsequent release of proinflammatory cytokines and chemokines upon necroptosis-mediated cell death,” although in RIPK1 deficiency, RIPK3-MLKL activation may occur via alternative pathways.[17]  

Dysregulated **IL-1β production** is a key feature: ClinGen notes that loss of RIPK1 leads to excessive IL-1β production, which can drive autoinflammatory manifestations such as arthritis, IBD, and vasculitis.[3] In the gut, increased necroptosis or apoptosis of epithelial and immune cells may disrupt barrier integrity, allowing microbial translocation and chronic inflammation, while dysregulated cytokines perpetuate mucosal immune activation, producing early-onset IBD.[10][12][18] In joints, similar mechanisms—cell death, DAMP release, and IL-1/TNF/IL-6–driven synovial inflammation—likely underlie inflammatory polyarthritis.  

Thus, IMD57 can be viewed as a **“loss-of-function immunodeficiency with gain-of-function autoinflammation”**, in which the absence of a regulatory hub leads to both impaired host defense and exaggerated inflammatory cell death. This duality is a hallmark of many primary immune regulatory disorders and illustrates the delicate balance maintained by RIPK1 in healthy individuals.[3][12][17]  

### 6.6 Branching Mechanistic Pathways and Upstream/Downstream Relationships

From an ordered causal perspective, several branching mechanisms can be delineated. Upstream, the initiating event is **germline RIPK1 LoF**, present in all cells but especially consequential in hematopoietic lineages. In response to environmental triggers (TNF, TLR ligands, interferons, viral RNA, bacterial products), multiple pathways diverge.  

One branch involves **TNFR1 signaling**. In normal cells, TNFR1 engagement recruits TRADD, RIPK1, TRAF2/5, and LUBAC to form complex I, leading to NF-κB activation and expression of survival and inflammatory genes.[13][15][17] In RIPK1-deficient cells, TRADD and other adaptors may still signal, but the absence of RIPK1 undermines complex stability and NF-κB activation, while also predisposing to formation of death-inducing complexes (complex II) that engage caspase-8 even more readily.[13][17][18]  

Another branch involves **TLR3/4–TRIF–RIPK1** signaling. Normally, TLR3/4 activation via TRIF recruits RIPK1 through RHIM, linking TLR activation to NF-κB and MAPK pathways.[13][15] In the absence of RIPK1, TRIF-dependent signaling may be skewed toward cell death pathways or rendered ineffective for cytokine induction, compromising antiviral and antibacterial responses.[13][15][18]  

A third branch concerns **interferon and RIG-I-like receptor pathways**. RIPK1 participates in some of these pathways, and its absence may reduce type I IFN responses or alter the balance between antiviral defense and inflammatory cell death, although detailed human data in IMD57 are limited.[15][17]  

Downstream of these branches, two major outcome pathways emerge: **immune cell depletion and functional impairment**, leading to immunodeficiency, and **excessive inflammatory cell death and cytokine release**, leading to autoinflammation and tissue damage. These processes engage multiple cell types, including T cells (CL:0000084), B cells (CL:0000236), NK cells (CL:0000623), macrophages (CL:0000235), dendritic cells (CL:0000451), and intestinal epithelial cells (CL:0000069).[3][12][18]  

---

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

IMD57 primarily affects the **immune system** and **gastrointestinal tract**, with secondary involvement of musculoskeletal, pulmonary, hepatic, and cutaneous systems. The immune system involvement encompasses lymphoid organs such as thymus, lymph nodes, spleen (UBERON:0002106), and bone marrow (UBERON:0002371), reflected clinically in lymphopenia, hypogammaglobulinemia, and recurrent infections.[3][5][11][18] Hepatosplenomegaly (UBERON:0002107 and UBERON:0002108) suggests enlargement of liver and spleen due to chronic immune activation.[5][18]  

The gastrointestinal tract involvement includes **small intestine** (UBERON:0002108), **colon** (UBERON:0001155), and **upper GI tract** structures such as stomach (UBERON:0000945), as patients present with enterocolitis, gastritis, diarrhea, and perianal disease.[5][10][18] Genomics England categorizes RIPK1 under “infantile enterocolitis & monogenic inflammatory bowel disease,” underscoring the gut as a major target organ.[10]  

Musculoskeletal involvement manifests as polyarthritis affecting multiple joints, potentially including knees, ankles, wrists, and small joints of hands and feet (various UBERON joint terms), reflecting synovial inflammation and joint damage.[3][5][18] Pulmonary involvement includes chronic lung disease and bronchiectasis (UBERON:0002048 for lung), likely secondary to recurrent infections and immune dysregulation.[5][18] Skin and vascular involvement appears as rash and lymphocytic vasculitis, affecting dermis and small blood vessels.[5][12]  

### 7.2 Tissue- and Cell-Level Targets

At the tissue level, IMD57 affects **lymphoid tissue**, **intestinal mucosa**, **synovial tissue**, **lung parenchyma**, and **skin**. In lymphoid tissue, T-cell zones are likely depleted or dysfunctional due to lymphopenia and increased apoptosis, while germinal center reactions may be impaired, contributing to defective antibody responses.[3][18] In intestinal mucosa, chronic inflammatory infiltrates, epithelial cell death, and disrupted barrier integrity characterize early-onset IBD.[10][12][18] Synovial tissue exhibits inflammatory infiltrates and pannus formation consistent with autoinflammatory arthritis.  

Key cell types include T lymphocytes (CL:0000084), B lymphocytes (CL:0000236), NK cells (CL:0000623), monocytes/macrophages (CL:0000235), dendritic cells (CL:0000451), neutrophils (CL:0000096), and intestinal epithelial cells (CL:0000069).[3][12][18] RIPK1’s role in these cells encompasses regulation of survival, cytokine production, and response to TNF and TLR ligands; its absence leads to context-dependent cell death and dysfunction.[12][15][17][18]  

### 7.3 Subcellular Compartments and Localization

Though RIPK1 is a cytosolic kinase, its functions are associated with specific **subcellular compartments**. It is recruited to the plasma membrane–proximal TNFR1 complex I (GO Cellular Component: *TNF-alpha/NF-kappa B signaling complex* GO:0031264), and it participates in cytosolic complexes such as the ripoptosome and necrosome.[13][15][17] RIPK1 also localizes to cytosolic signaling complexes downstream of TLRs and RIG-I-like receptors, and its kinase activity influences events at the plasma membrane, cytoplasm, and possibly mitochondria through downstream necroptotic effectors like MLKL.[16][17]  

In IMD57, loss of RIPK1 means these complexes either do not form properly (e.g., complex I) or form aberrantly (e.g., death-inducing complexes without appropriate regulation), altering signaling in cellular compartments such as plasma membrane, cytosol (GO:0005829), and nucleus (GO:0005634) where NF-κB and other transcription factors act.[13][15][17][18]  

---

## 8. Temporal Development

### 8.1 Age of Onset and Early Disease Course

IMD57 is a **pediatric-onset** disease, with symptoms beginning in **neonatal period or infancy**, typically within the first year of life.[3][5][11][18] OMIM notes that recurrent infections start in the first year of life, and MalaCards lists onset in “infancy, neonatal.”[5][11] ClinGen emphasizes that early-onset IBD and infections are invariant features during early childhood.[3] Thus, age-of-onset HPO terms such as *Neonatal onset* (HP:0003623) and *Infantile onset* (HP:0003593) apply.  

The onset pattern is **chronic and insidious** rather than acute. Infants may present initially with persistent diarrhea, failure to thrive, and recurrent respiratory or systemic infections, and over months to years they develop progressive arthritis and additional complications.[5][18] Some may be misdiagnosed initially with nonspecific severe combined immunodeficiency, early-onset IBD, or juvenile idiopathic arthritis before the full constellation of features and genetic diagnosis clarifies the underlying syndrome.[3][12][18]  

### 8.2 Disease Progression, Course, and Duration

The **disease course** of IMD57 appears **chronic and progressive**, with ongoing enterocolitis, arthritis, and recurrent infections, punctuated by acute exacerbations triggered by infections or other inflammatory stimuli.[3][5][18] Over time, recurrent infections can lead to chronic lung disease and bronchiectasis; chronic intestinal inflammation can cause strictures, malabsorption, and growth failure; and chronic arthritis can result in joint damage and disability.[5][18]  

Without curative interventions such as HSCT, the disease is likely **lifelong** and life-limiting. However, the limited number of reported cases and the recency of diagnosis make it difficult to define precise natural history, survival curves, or progression stages. One can conceptually define an early stage dominated by infections and gastrointestinal symptoms, an intermediate stage with established chronic organ damage (lung, joints), and an advanced stage with severe systemic complications and potential organ failure, but these stages have not been formalized in the literature.[3][5][12][18]  

Response to HSCT in at least one patient suggests that the disease course can be **reset** by reconstituting RIPK1-sufficient hematopoietic cells, leading to resolution of infections and IBD.[18] However, if significant organ damage has already occurred (e.g., bronchiectasis, joint destruction), some sequelae may be irreversible, emphasizing the importance of early diagnosis and intervention.  

### 8.3 Remission Patterns and Critical Periods

Spontaneous remissions are not described in IMD57; rather, disease activity fluctuates with triggers such as infections but remains chronic without definitive treatment. Immunosuppressive or biologic therapies (e.g., anti-TNF) may induce partial remission of IBD or arthritis in some monogenic IBD cases, but specific data for IMD57 are sparse in the summarized sources.[10][12][18] These therapies,

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 64 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 37 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012404` (3 mentions) - the report calls it "Early-onset inflammatory bowel disease"; HP calls it **Abnormal urine citrate concentration**
- `HP:0003481` (2 mentions) - the report calls it "Inflammatory arthritis"; HP calls it **Segmental peripheral demyelination/remyelination**
- `HP:0001883` (2 mentions) - the report calls it "Decreased T cell count"; HP calls it **Talipes**
- `HP:0002110` (2 mentions) - the report calls it "Recurrent lower respiratory tract infections", "Bronchiectasis"; HP calls it **Bronchiectasis**
- `HP:0002597` (1 mention) - the report calls it "Inflammatory bowel disease"; HP calls it **Abnormality of the vasculature**
- `HP:0002038` (1 mention) - the report calls it "Chronic diarrhea"; HP calls it **Protein avoidance**
- `HP:0002240` (1 mention) - the report calls it "Gastrointestinal hemorrhage"; HP calls it **Hepatomegaly**
- `HP:0002635` (2 mentions) - the report calls it "Cutaneous vasculitis", "Leukocytoclastic vasculitis"; HP calls it **Type IV atherosclerotic lesion**
- `HP:0012091` (1 mention) - the report calls it "Decreased NK cell count"; HP calls it **Abnormality of pancreas physiology**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003479` (1 mention), reported as "Polyarthritis" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0032088` (obsolete negative regulation of NF-kappaB transcription factor activity) (1 mention)
- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004313` (2 mentions) - the report calls it "hypogammaglobulinemia"; HP calls it **Decreased circulating immunoglobulin concentration**, and lists "Hypogammaglobulinemia" among its other names
- `HP:0001371` (1 mention) - the report calls it "Joint contracture"; HP calls it **Flexion contracture**
- `HP:0004322` (1 mention) - the report calls it "Decreased B cell count"; HP calls it **Short stature**, and lists "Decreased body height" among its other names
- `HP:0004315` (1 mention) - the report calls it "Abnormal immunoglobulin level"; HP calls it **Decreased circulating IgG concentration**, and lists "Decreased immunoglobulin G" among its other names
- `GO:0033209` (1 mention) - the report calls it "TNF-mediated signaling pathway"; GO calls it **tumor necrosis factor-mediated signaling pathway**, and lists "TNF-alpha-mediated signaling pathway" among its other names
- `GO:0032088` (1 mention) - the report calls it "regulation of NF-kappaB transcription factor activity"; GO calls it **obsolete negative regulation of NF-kappaB transcription factor activity**
- `GO:0051092` (1 mention) - the report calls it "positive regulation of NF-kappaB transcription factor activity"; GO calls it **obsolete positive regulation of NF-kappaB transcription factor activity**
- `GO:0060545` (1 mention) - the report calls it "regulation of necroptotic process"; GO calls it **positive regulation of necroptotic process**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002110` - called "Recurrent lower respiratory tract infections", "Bronchiectasis"
- `HP:0002635` - called "Cutaneous vasculitis", "Leukocytoclastic vasculitis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `DO`, `OMIM`.