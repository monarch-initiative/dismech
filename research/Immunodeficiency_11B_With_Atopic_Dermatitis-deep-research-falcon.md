---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T02:47:43.063833'
end_time: '2026-09-06T02:58:57.725357'
duration_seconds: 674.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 11B with Atopic Dermatitis
  mondo_id: MONDO:0054697
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunodeficiency_11B_With_Atopic_Dermatitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 11B with Atopic Dermatitis
- **MONDO ID:** MONDO:0054697 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 11B with Atopic Dermatitis** covering all of the
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
- **Disease Name:** Immunodeficiency 11B with Atopic Dermatitis
- **MONDO ID:** MONDO:0054697 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 11B with Atopic Dermatitis** covering all of the
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


# Immunodeficiency 11B with Atopic Dermatitis (IMD11B/CADINS): Disease-Characteristics Report

## Executive summary and evidence scope

Immunodeficiency 11B with atopic dermatitis (IMD11B) is a rare, autosomal-dominant inborn error of immunity caused by heterozygous germline loss-of-function variants in **CARD11** that dominantly interfere with the wild-type protein. The preferred mechanistic name is **CARD11-associated atopy with dominant interference of NF-κB signaling (CADINS)**. It combines early-onset atopic disease—particularly dermatitis—with variably penetrant humoral and cellular immunodeficiency, recurrent respiratory or cutaneous infections, and occasional autoimmunity, neutropenia, gastrointestinal inflammation, or malignancy. It must not be conflated with autosomal-recessive complete CARD11 deficiency (OMIM 615206) or gain-of-function CARD11-associated BENTA syndrome. (pietzsch2022hyperigeandcarcinoma pages 1-2, urdinez2022expandingspectrumintrafamilial pages 1-2, garciamartinez2025fromsyndromicclues pages 1-2)

Published evidence remains limited to small, genetically heterogeneous cohorts, families, case reports, patient-cell experiments, and mouse models. A 2024 review table compiled 63 reported patients across approximately 25 families/case groups, but this is not a population registry and does not establish prevalence. The strongest aggregate estimates are approximately 89% with atopy, 75% with elevated IgE, 73% with atopic dermatitis, 68% with respiratory or viral infections, 20% with autoimmune manifestations, 15% each with neutropenia or oral ulcers, and fewer than 10% with lymphoma. These estimates are vulnerable to referral and ascertainment bias. (zhao2024anewdiseasecausingdominantnegative pages 8-9, pomerantz2022elevatedigefrom pages 4-6)

| Domain | Evidence-backed finding | Quantitative data | Suggested ontology terms | Evidence type / limitations |
|---|---|---:|---|---|
| Identity | Immunodeficiency 11B with atopic dermatitis, commonly called **CARD11-associated atopy with dominant interference of NF-κB signaling (CADINS)** | **OMIM 617638**; **MONDO:0054697** | MONDO:0054697; HP:0002721 Immunodeficiency | Aggregated disease-resource and human genetic evidence; distinct from autosomal-recessive complete CARD11 deficiency (OMIM 615206) and gain-of-function BENTA (OpenTargets Search: Immunodeficiency 11B with atopic dermatitis-CARD11, pietzsch2022hyperigeandcarcinoma pages 1-2) |
| Genetic cause | Heterozygous germline loss-of-function **CARD11** variants dominantly interfere with wild-type CARD11 signaling; inheritance is autosomal dominant, with de novo and familial cases | Literature review summarized **63 patients** across 25 families/case groups | CARD11; HGNC:16393; GO:0030154 cell differentiation | Human pedigrees plus in-vitro functional assays; penetrance is incomplete and expressivity highly variable (zhao2024anewdiseasecausingdominantnegative pages 8-9, pomerantz2022elevatedigefrom pages 8-10) |
| Onset | Usually infantile or early-childhood onset; severe dermatitis is commonly the first manifestation | Mean onset **5.9 months** in a 10-person CADINS cohort; dermatitis was initial in **7/10 (70%)** | HP:0003593 Infantile onset; HP:0007354 Atopic dermatitis | Single-center cohort; ascertainment favored symptomatic pediatric index cases (urdinez2022expandingspectrumintrafamilial pages 12-13) |
| Atopic disease | Multisystem atopy includes dermatitis, asthma, food allergy, allergic rhinitis, and sometimes eosinophilic gastrointestinal disease | Any atopy **89%**; atopic dermatitis **73%** | HP:0001047 Atopic dermatitis; HP:0002099 Asthma; HP:0500093 Food allergy; HP:0004403 Allergic rhinitis | International-cohort summary; denominators and manifestations vary across reports (pomerantz2022elevatedigefrom pages 8-10, pomerantz2022elevatedigefrom pages 4-6) |
| Laboratory allergy phenotype | Elevated IgE and eosinophilia are common but not obligatory | Elevated IgE **75%**; persistent eosinophilia **8/10 (80%)** in one cohort | HP:0003212 Elevated serum IgE; HP:0001880 Eosinophilia | Cohort-level observations; values vary with age and treatment (urdinez2022expandingspectrumintrafamilial pages 12-13, pomerantz2022elevatedigefrom pages 4-6) |
| Infection susceptibility | Recurrent respiratory and viral cutaneous infections reflect variable combined or humoral immunodeficiency; bronchiectasis may develop | Respiratory/viral infections approximately **68%** | HP:0002205 Recurrent respiratory infections; HP:0004429 Recurrent viral infections; HP:0002110 Bronchiectasis | Human cohorts and case reports; pathogen-specific frequencies are unavailable (pietzsch2022hyperigeandcarcinoma pages 2-4, pomerantz2022elevatedigefrom pages 4-6) |
| Immune dysregulation | Autoimmunity, neutropenia, oral ulcers, and rare lymphoma broaden the phenotype beyond allergy | Autoimmunity approximately **20%**; neutropenia approximately **15%**; oral ulcers approximately **15%**; lymphoma **<10%** | HP:0002960 Autoimmunity; HP:0001875 Neutropenia; HP:0000155 Oral ulcer; HP:0002665 Lymphoma | Small heterogeneous cohorts; malignancy association remains uncertain and may be variant- or infection-dependent (pomerantz2022elevatedigefrom pages 4-6, pietzsch2022hyperigeandcarcinoma pages 6-7) |
| Immunologic testing | T- and B-cell counts may be normal, but antigen/mitogen proliferation and specific-antibody production can be impaired; IgG may be reduced | PHA proliferation impaired in **5/6** tested in one cohort; about half of another cohort required immunoglobulin replacement | HP:0032130 Abnormal lymphocyte proliferation; HP:0004315 Decreased circulating antibody level; HP:0004432 Abnormality of specific antibody response | Functional abnormalities are variable; normal lymphocyte subsets do not exclude CADINS (urdinez2022expandingspectrumintrafamilial pages 12-13, izadi2021cadinsinan pages 1-3, urdinez2022expandingspectrumintrafamilial pages 15-17) |
| Molecular mechanism | Mutant CARD11 poisons mixed oligomers, impairing scaffold opening and CARD11–BCL10–MALT1 signalosome assembly; this reduces antigen-receptor-induced canonical NF-κB and usually JNK/mTORC1 signaling, glutamine uptake, proliferation, and IFN-γ, while favoring IL-4/GATA3-associated T-helper-2 skewing | All validated dominant-negative variants in the cited cohort impaired TCR-induced NF-κB; mTORC1 effects were variable | GO:0038063 collagen-activated signaling pathway; GO:0043123 positive regulation of IκB kinase/NF-κB signaling; GO:0007254 JNK cascade; GO:0031929 TOR signaling; GO:0042092 type 2 immune response; CL:0000624 CD4-positive alpha-beta T cell | Human cells, transfected cell lines, and mechanistic synthesis; relative contribution of each pathway differs by variant (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 4-6, pomerantz2022elevatedigefrom pages 8-10, izadi2021cadinsinan pages 3-4) |
| Diagnosis | Suspect CADINS with very-early-onset or treatment-resistant atopy plus recurrent/unusual infections, poor vaccine responses, autoimmunity, or family history. Confirm a heterozygous CARD11 variant by panel/WES/WGS and segregation testing; functional demonstration of dominant interference is important for novel variants | A 2024 case used trio WES, Sanger validation, NF-κB reporter/co-immunoprecipitation, and RNA sequencing | NCIT:C17607 Genetic Testing; NCIT:C101295 Whole Exome Sequencing; HP:0000005 Mode of inheritance | No consensus disease-specific criteria; sequence variants may remain VUS without functional validation (urdinez2022expandingspectrumintrafamilial pages 1-2, zhao2024anewdiseasecausingdominantnegative pages 8-9, izadi2021cadinsinan pages 3-4) |
| Treatment | Treat dermatitis conventionally; targeted IL-4/IL-13 blockade with dupilumab has produced marked benefit in case reports. Immunoglobulin replacement and antimicrobial prophylaxis are used for clinically significant antibody deficiency/infections. Glutamine partially rescued cellular defects in vitro but is not established clinical therapy | Dupilumab benefit reported at case level; no controlled response rate; immunoglobulin replacement reduced infections in one patient but did not prevent bronchiectasis | NCIT:C1576 Dupilumab; NCIT:C270 Immunoglobulin Therapy; NCIT:C1589 Tacrolimus; CHEBI:28300 glutamine | Observational reports and expert extrapolation; no disease-specific randomized trials, validated algorithm, or established HSCT indication for typical CADINS (pietzsch2022hyperigeandcarcinoma pages 2-4, izadi2021cadinsinan pages 3-4, giancotta2023tailoredtreatmentsin pages 5-6, giancotta2023tailoredtreatmentsin pages 4-5) |
| Prevention | Routine vaccination should be individualized after immune evaluation; HPV vaccination and surveillance have been proposed because HPV-positive carcinoma has occurred in affected families | HPV-positive squamous carcinoma reported in one family across the broader malignancy history | NCIT:C1746 HPV Vaccine; NCIT:C17139 Cancer Screening | Expert recommendation based on isolated familial malignancy observations, not prospective prevention studies (pietzsch2022hyperigeandcarcinoma pages 6-7, pietzsch2022hyperigeandcarcinoma pages 1-2) |
| R30W mouse model | Heterozygous **Card11 R30W/+** mice reproduce impaired T-, B-, and NK-cell signaling, reduced Treg numbers, reduced NK-cell IFN-γ, and age-dependent hyper-IgE, but not spontaneous dermatitis | Elevated IgE showed approximately **50% penetrance** and increased with age | CL:0000815 regulatory T cell; CL:0000623 natural killer cell; HP:0003212 Elevated serum IgE; GO:0032649 regulation of interferon-gamma production | Patient-variant knock-in model; failure to develop spontaneous dermatitis shows that high IgE alone is insufficient and limits direct phenotypic translation (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 8-10) |


*Table: Concise knowledge-base summary of IMD11B/CADINS identity, clinical frequencies, mechanism, diagnosis, management, and the Card11 R30W mouse model. Quantitative estimates derive from small, heterogeneous cohorts and should not be interpreted as population prevalence.*

## 1. Disease information

### Definition and identifiers

* **Disease:** Immunodeficiency 11B with atopic dermatitis.
* **Preferred synonym:** CARD11-associated atopy with dominant interference of NF-κB signaling (**CADINS**).
* **Other names:** CARD11-associated atopy; dominant-negative CARD11 deficiency; heterozygous CARD11 loss-of-function disease; CARD11-related hyper-IgE-like syndrome.
* **MONDO:** **MONDO:0054697**.
* **OMIM/MIM:** **617638**.
* **Causal gene:** **CARD11**, caspase recruitment domain family member 11; Ensembl **ENSG00000198286**. Open Targets identifies CARD11 as the sole associated target for MONDO:0054697, supported by five evidence records. (OpenTargets Search: Immunodeficiency 11B with atopic dermatitis-CARD11)
* **Orphanet:** A dedicated, confidently verified Orpha number was not identified in the retrieved evidence.
* **ICD-10/ICD-11:** No disease-specific code was identified. Cases generally require broader immunodeficiency and manifestation codes.
* **MeSH:** No disease-specific MeSH descriptor was identified; concepts such as primary immunodeficiency, atopic dermatitis, and CARD11 protein are used.

The evidence is primarily **aggregated disease-level literature**, supplemented by individual-patient and family data. It is not derived from a large EHR cohort or population registry.

### Disease-boundary warning

Monoallelic dominant-negative CADINS differs from: (1) **biallelic complete CARD11 deficiency**, an autosomal-recessive combined immunodeficiency/SCID-like disorder (OMIM 615206), and (2) **BENTA**, caused by activating CARD11 variants and characterized by B-cell expansion and lymphoproliferation. Variant zygosity and functional direction are therefore essential to classification. (pietzsch2022hyperigeandcarcinoma pages 1-2, urdinez2022expandingspectrumintrafamilial pages 1-2, garciamartinez2025fromsyndromicclues pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The established cause is a **germline heterozygous CARD11 variant with loss-of-function and dominant-interfering activity**. Mutant and wild-type CARD11 form dysfunctional mixed oligomers, impairing antigen-receptor-induced CARD11 opening, cofactor recruitment, and downstream signaling. Both inherited and de novo cases occur. A 2024 Chinese case carried de novo **NM_032415:c.2324C>T, p.Ser775Leu**; reporter, co-immunoprecipitation, and RNA-sequencing experiments showed dominant interference and reduced NF-κB transcriptional activity. (zhao2024anewdiseasecausingdominantnegative pages 8-9, pomerantz2022elevatedigefrom pages 8-10)

### Genetic risk and modifiers

Disease risk is determined principally by the causal allele. Functional severity differs among variants: R30W and R72Q have been characterized as stronger NF-κB inhibitors than variants such as N25Y or K83M. Nevertheless, no reliable genotype–phenotype correlation has been established, and marked variability occurs even within families. (zhao2024anewdiseasecausingdominantnegative pages 8-9)

No validated modifier genes, protective alleles, founder variants, carrier-frequency estimates, or epigenetic signatures are known. Formal penetrance is undefined; published families indicate incomplete or high-but-not-complete penetrance and markedly variable expressivity. A p.Arg75Trp family showed severe disease in the index patient but predominantly atopy without hypogammaglobulinemia in five relatives. (pietzsch2022hyperigeandcarcinoma pages 1-2, pietzsch2022hyperigeandcarcinoma pages 6-7)

### Environmental and infectious factors

No toxin, occupation, smoking pattern, diet, radiation exposure, or lifestyle factor has been shown to cause CADINS. Allergens and microbial exposure likely shape expression of eczema and infection burden, but CADINS-specific gene–environment studies are absent. Impaired CARD11-dependent upregulation of the glutamine transporter ASCT2 suggests that nutrient availability can modify lymphocyte signaling in vitro; supplemental glutamine partially rescued proliferation and IFN-γ production, but this has not established dietary prevention or clinical efficacy. (pomerantz2022elevatedigefrom pages 4-6, izadi2021cadinsinan pages 3-4)

Respiratory pathogens and cutaneous viruses—including herpesviruses, molluscum contagiosum, varicella-zoster virus, and HPV—are **complications or phenotypic probes of immunodeficiency**, not primary causes. Skin-barrier disruption and microbial colonization may amplify dermatitis, but CADINS-specific microbiome data are lacking. (pietzsch2022hyperigeandcarcinoma pages 2-4, (henry)2023definingthepathogenesis pages 75-79)

No proven genetic or environmental protective factor exists. Improvement of dermatitis with age in some patients is a natural-history observation, not evidence of protection. (zhao2024anewdiseasecausingdominantnegative pages 8-9, giancotta2023tailoredtreatmentsin pages 5-6)

## 3. Phenotypes

### Major clinical and laboratory manifestations

| Phenotype | Character/course and frequency | Suggested HPO term |
|---|---|---|
| Atopic dermatitis/eczema | Usually infantile, often severe or recalcitrant; approximately 73% overall. Initial manifestation in 7/10 patients in one cohort; may improve during childhood/adolescence. | HP:0001047 |
| Atopy, broadly defined | Approximately 89%; includes food allergy, asthma, rhinitis, and eosinophilic GI disease. | HP:0001026/individual manifestation terms |
| Elevated serum IgE | Approximately 75%; variable and not required. | HP:0003212 |
| Eosinophilia | Persistent in 8/10 in one cohort; one patient reached 5,900/µL. | HP:0001880 |
| Asthma | Common but less frequent than dermatitis; often early-onset. | HP:0002099 |
| Food allergy | Variable; immediate hypersensitivity may be prominent. | HP:0500093 |
| Allergic rhinitis | Variable. | HP:0004403 |
| Eosinophilic esophagitis/colitis | Uncommon but clinically important; may resemble IPEX-like disease. | HP:0002027 / HP:0100279 |
| Recurrent respiratory infection/pneumonia/sinusitis | Respiratory or viral infection in approximately 68%; may cause bronchiectasis. | HP:0002205, HP:0002110 |
| Viral skin infection/warts | HPV, herpesvirus, molluscum, VZV, eczema herpeticum reported. | HP:0004429, HP:0001070 |
| Hypogammaglobulinemia or impaired specific antibodies | Variable; total immunoglobulins may be normal. Poor vaccine antibody responses are diagnostically useful. | HP:0004315, HP:0004432 |
| Reduced lymphocyte proliferation | Counts can be normal despite impaired mitogen/antigen responses; PHA response abnormal in 5/6 tested in one cohort. | HP:0032130 |
| Neutropenia/agranulocytosis | Approximately 15%; sometimes transient and possibly autoimmune. | HP:0001875 |
| Autoimmunity/inflammation | Approximately 20%; colitis and other manifestations reported. | HP:0002960 |
| Oral ulcers | Approximately 15%. | HP:0000155 |
| Failure to thrive | 4/10 in one pediatric cohort. | HP:0001508 |
| Lymphoma/HPV-associated carcinoma | Rare; lymphoma under 10% in summaries. Causality and absolute risk remain uncertain. | HP:0002665 / HP:0030731 |

These frequency estimates derive from different cohorts and should not be combined as though they came from one prospective denominator. (urdinez2022expandingspectrumintrafamilial pages 12-13, pomerantz2022elevatedigefrom pages 4-6)

The mean onset in a 10-person CADINS cohort was **5.9 months**; mean age at assessment was 7.5 years, range 2–33 years. Severe dermatitis was the first manifestation in 70%. One 2024 case had severe eczema before 18 months that later resolved, illustrating a fluctuating or improving cutaneous course despite persistent genetic disease. (urdinez2022expandingspectrumintrafamilial pages 12-13, zhao2024anewdiseasecausingdominantnegative pages 8-9)

No CADINS-specific EQ-5D, SF-36, PROMIS, sleep, or dermatitis quality-of-life studies were found. Severe pruritus, food restriction, recurrent infections, repeated antibiotics, bronchiectasis, and chronic gastrointestinal disease plausibly impair daily functioning, but quantitative disease-specific quality-of-life effects remain unmeasured.

## 4. Genetic and molecular information

### Gene and variant classes

**CARD11** encodes a lymphocyte-enriched intracellular scaffold also called CARMA1. Pathogenic CADINS alleles are germline, heterozygous, and usually missense or in-frame changes; nonsense variants also occur. Dominant-negative variants are enriched in the N-terminal CARD, LATCH, and coiled-coil regions, although C-terminal MAGUK/GUK-domain variants are documented. Twelve of 14 variants in one early summary affected the CARD/coiled-coil region, with two in the C-terminal GUK region. (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 4-6)

Reported variants include **p.Arg30Gly, p.Arg30Gln, p.Arg30Trp, p.Thr43Arg, p.Arg47His, p.Ile52Thr, p.Glu57Asp, p.Arg72Gly/p.Arg72Leu, p.Arg75Gln/p.Arg75Trp, p.Glu96Lys, p.Leu92Trp, p.Lys143Ter, p.Arg187Pro, p.Leu194Pro, an in-frame alteration involving residues 183–196, p.Ser775Leu, p.Arg974Cys, and p.Arg975Trp**. This is not a definitive ClinVar catalog, and transcript normalization should precede database ingestion. (zhao2024anewdiseasecausingdominantnegative pages 8-9, (henry)2023definingthepathogenesis pages 75-79, izadi2021cadinsinan pages 3-4)

Examples with direct functional evidence include:

* **c.223C>T, p.Arg75Trp:** absent from gnomAD in the reported family; reduced CARD11 reporter activity even with wild-type co-expression, consistent with dominant interference. (pietzsch2022hyperigeandcarcinoma pages 2-4, pietzsch2022hyperigeandcarcinoma pages 6-7)
* **p.Arg72Leu:** failed to rescue NF-κB reporter activity or IL-2 secretion when coexpressed with wild-type CARD11; patient B cells showed absent PMA-induced IκBα degradation. (izadi2021cadinsinan pages 3-4)
* **c.2324C>T, p.Ser775Leu:** de novo and very rare; dominant interference shown by luciferase, co-immunoprecipitation, and RNA-seq. (zhao2024anewdiseasecausingdominantnegative pages 8-9)

Population allele frequencies should be obtained variant by variant from current gnomAD/ClinVar releases. The retrieved literature does not provide reliable frequencies for the full set. Variants are constitutional/germline, not somatic drivers. Novel variants should not be upgraded solely because CARD11 is plausible: functional demonstration of impaired signaling and dominant interference is particularly important. Multiplex functional work has assessed 2,542 CARD11 variants across residues 4–146, offering an important interpretation resource (PMID **33202260**). (pomerantz2022elevatedigefrom pages 10-12)

No recurrent chromosomal rearrangement, aneuploidy, methylation signature, histone abnormality, or established structural variant defines IMD11B. No validated modifier gene has been reported.

## 5. Environmental information

There is no evidence that pollution, toxins, occupational exposure, alcohol, tobacco, or physical activity modifies inherited disease penetrance. Standard avoidance of patient-specific allergens and skin irritants may reduce manifestations but cannot prevent the genetic disorder. Infectious organisms are opportunistic or recurrent complications. HPV deserves particular attention because persistent HPV infection and HPV-positive squamous carcinoma have occurred in affected families, although the magnitude of excess risk is unknown. (pietzsch2022hyperigeandcarcinoma pages 6-7, pietzsch2022hyperigeandcarcinoma pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A **heterozygous germline loss-of-function CARD11 variant** leads to production of mutant CARD11 capable of associating with wild-type CARD11.  
2. Mixed mutant/wild-type oligomers **lead to dominant “oligomer poisoning,”** defective signal-induced opening of CARD11, and impaired recruitment of BCL10, MALT1, HOIP and other cofactors. (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 8-10)  
3. Defective CARD11–BCL10–MALT1 signalosome assembly **leads to attenuated antigen-receptor-induced canonical NF-κB signaling** and, in most variants, impaired JNK and mTORC1 signaling. (pomerantz2022elevatedigefrom pages 4-6, izadi2021cadinsinan pages 3-4)  
4. Reduced mTORC1 activation and ASCT2-dependent glutamine uptake **lead to impaired lymphocyte metabolic activation, proliferation, and IFN-γ production**; the degree is variant dependent. (pomerantz2022elevatedigefrom pages 4-6)  
5. Impaired CARD11/JNK and IFN-γ signaling **leads to increased GATA3/IL-4-associated T-helper-2 differentiation**; the exact contribution of each branch is partly inferred from human cells and experimental systems. (bauman2025dominantinterferingcard11 pages 14-15, pomerantz2022elevatedigefrom pages 4-6)  
6A. Th2 bias **results in** IgE elevation, eosinophilia, food allergy, asthma, and inflamed/pruritic skin.  
6B. Impaired T-cell activation, B-cell help/specific-antibody formation, and NK-cell IFN-γ production **result in** recurrent respiratory and viral skin infections. (hutcherson2021pathwayspecificdefectsin pages 1-3, urdinez2022expandingspectrumintrafamilial pages 15-17)  
6C. Immune imbalance **may lead to** autoimmunity, neutropenia, inflammatory colitis, and possibly impaired HPV tumor surveillance; these downstream links are clinically associated but not fully demonstrated. (pietzsch2022hyperigeandcarcinoma pages 6-7)  
7. Recurrent airway infection and inflammation **can result in** chronic sinus disease and bronchiectasis, while epidermal inflammation and infection reinforce dermatitis. (pietzsch2022hyperigeandcarcinoma pages 2-4, izadi2021cadinsinan pages 1-3)

### Cells, pathways, metabolism, and tissue injury

Relevant cells include conventional CD4 T cells (**CL:0000624**), Th2 cells (**CL:0000546**), regulatory T cells (**CL:0000815**), B cells (**CL:0000236**), plasma cells (**CL:0000786**), and NK cells (**CL:0000623**). Human T- and B-cell numbers may be normal, emphasizing a functional rather than obligatory numerical defect. Human Treg findings are inconsistent; aggregate human data suggest generally preserved frequency/suppression, whereas the Card11-R30W mouse has reduced Treg numbers. (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 4-6)

Suggested GO terms include antigen receptor-mediated signaling (**GO:0050851**), positive regulation of IκB kinase/NF-κB signaling (**GO:0043123**), JNK cascade (**GO:0007254**), TOR signaling (**GO:0031929**), T-cell activation (**GO:0042110**), B-cell activation (**GO:0042113**), type 2 immune response (**GO:0042092**), regulation of IFN-γ production (**GO:0032649**), and glutamine transport (**GO:0006868**). CARD11 acts in a cytoplasmic/membrane-proximal signalosome rather than through a primary nuclear, mitochondrial, lysosomal, or extracellular defect.

### Molecular profiling and recent developments

The 2024 p.Ser775Leu study used RNA sequencing to confirm reduced downstream NF-κB transcriptional activity, representing disease-relevant transcriptomic evidence. Broad patient proteomics, metabolomics, lipidomics, single-cell, spatial-transcriptomic, and integrated multi-omic profiles have not been reported in the retrieved evidence. (zhao2024anewdiseasecausingdominantnegative pages 8-9)

A major subsequent mechanistic advance, published in March 2025, showed that CARD11 is required for TCR-induced JNK1/JNK2 activation; dominant-interfering variants attenuated this branch, and CADINS patient CD4 T cells showed increased GATA3 and NFAT2 after stimulation. This provides a direct mechanistic bridge from defective CARD11–JNK signaling to Th2 differentiation, but it postdates the requested 2023–2024 priority window. DOI: [10.1084/jem.20240272](https://doi.org/10.1084/jem.20240272), published March 2025. (bauman2025dominantinterferingcard11 pages 14-15)

## 7. Anatomical structures affected

* **Primary:** skin/epidermis (**UBERON:0002097**, skin; **UBERON:0001003**, epidermis), particularly diffuse rather than lateralized involvement.
* **Immune/lymphoid:** blood, lymphocytes, lymph nodes, spleen, and thymic immune development; abnormalities are primarily functional.
* **Respiratory:** upper airways/sinuses and lungs; recurrent sinusitis, pneumonia, asthma, and secondary bronchiectasis. Suggested terms include **UBERON:0002048** lung and **UBERON:0000004** nose.
* **Gastrointestinal:** esophagus and colon in eosinophilic esophagitis/colitis.
* **Secondary:** nails in fungal disease and anogenital/cutaneous epithelium in persistent HPV disease.

No consistent laterality is reported. At the subcellular level, the key compartment is the cytoplasmic CARD11–BCL10–MALT1 signaling complex assembled after antigen-receptor stimulation.

## 8. Temporal development

Onset is usually chronic and insidious in infancy, often beginning with dermatitis. The mean onset of 5.9 months in one cohort supports the HPO term **Infantile onset (HP:0003593)**. Infections, asthma, food allergy, antibody deficiency, gastrointestinal inflammation, or autoimmunity may emerge later. (urdinez2022expandingspectrumintrafamilial pages 12-13)

The disorder is lifelong genetically but clinically variable. Dermatitis may be severe in infancy and improve or remit during adolescence; immune defects and infection risk do not necessarily resolve in parallel. One patient developed hypogammaglobulinemia at age 5 and bronchiectasis at 13, illustrating the value of longitudinal immune and pulmonary surveillance. (pietzsch2022hyperigeandcarcinoma pages 2-4, zhao2024anewdiseasecausingdominantnegative pages 8-9, giancotta2023tailoredtreatmentsin pages 5-6)

There is no validated staging system, defined progression rate, or critical therapeutic window. Early recognition before irreversible bronchiectasis, nutritional impairment, or severe infection is the most plausible intervention opportunity.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Both familial transmission and de novo variants occur. Penetrance is incomplete or variably described as high in individual families, while expressivity ranges from isolated/severe atopy to combined immune dysfunction. Genetic anticipation has not been reported. Germline mosaicism remains theoretically possible but is not documented. No founder effect, geographic concentration, ethnic predisposition, sex bias, or carrier-frequency estimate is established. (pietzsch2022hyperigeandcarcinoma pages 6-7, zhao2024anewdiseasecausingdominantnegative pages 8-9)

No incidence or prevalence per 100,000 is available. The literature summary of approximately 63 affected individuals reflects reported cases rather than epidemiology. Men and women and multiple ancestry groups have been reported; the 2024 Chinese case broadens geographic representation. (zhao2024anewdiseasecausingdominantnegative pages 8-9)

## 10. Diagnostics

### Clinical suspicion and immunologic workup

Red flags are severe or treatment-resistant dermatitis beginning in infancy; multiple atopic manifestations; recurrent, severe, or unusual respiratory/viral infections; poor growth; hypogammaglobulinemia or poor vaccine responses; autoimmunity, neutropenia, oral ulcers, eosinophilic GI disease; and an affected parent or multiple generations.

Recommended baseline evaluation is CBC/differential, eosinophils, quantitative IgG/IgA/IgM/IgE, lymphocyte subsets, vaccine-specific antibodies, T-cell proliferation to mitogens/antigens, and directed infection assessment. Normal lymphocyte counts and Treg numbers do not exclude CADINS. One adult had absent Hib antibody despite vaccination and lacked baseline antibodies to 20/23 pneumococcal serotypes; only four serotypes became protective after PPSV23. (urdinez2022expandingspectrumintrafamilial pages 12-13, izadi2021cadinsinan pages 1-3, urdinez2022expandingspectrumintrafamilial pages 15-17)

Imaging is manifestation-directed: chest CT for recurrent pneumonia/bronchiectasis and sinus CT for refractory sinusitis. Endoscopy/biopsy may demonstrate eosinophilic esophagitis or colitis. No pathognomonic skin histology, metabolite, circulating protein biomarker, electrophysiologic test, or liquid biopsy exists.

### Genetic testing

An inborn-error-of-immunity/primary-atopy panel including **CARD11**, or early WES/WGS, is appropriate. Trio sequencing is especially valuable in apparently sporadic disease. Confirm variants by orthogonal sequencing and perform segregation/cascade testing. RNA-seq can clarify splice or transcriptional consequences, but it is not routine. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing have low expected yield unless another phenotype suggests them.

Novel CARD11 variants require cautious ACMG/AMP interpretation and ideally functional analysis: NF-κB reporter assays, IκBα degradation, IL-2/IFN-γ production, T-cell proliferation, mTORC1/JNK readouts, and coexpression with wild-type CARD11 to demonstrate dominant interference. Functional validation changed or excluded variant interpretation in a 15-person CARD11 cohort. (urdinez2022expandingspectrumintrafamilial pages 1-2, izadi2021cadinsinan pages 3-4)

### Differential diagnosis

Important alternatives include DOCK8 deficiency, STAT3-HIES, PGM3 deficiency, Wiskott–Aldrich syndrome, IPEX, Omenn syndrome, severe combined immunodeficiency, MALT1/BCL10 defects, CARD11 gain-of-function BENTA, CARD11 biallelic deficiency, common variable immunodeficiency, and common polygenic atopic dermatitis. DOCK8 deficiency can closely resemble CADINS through food allergy, asthma, viral skin infection, and recurrent respiratory infection but is usually autosomal recessive and often more severe. (izadi2021cadinsinan pages 3-4, pietzsch2022hyperigeandcarcinoma pages 1-2)

There are no validated disease-specific diagnostic criteria or population/newborn screening program. Cascade testing is appropriate after a familial pathogenic variant is established.

## 11. Outcome and prognosis

No 5- or 10-year survival, life-expectancy, mortality, disability, or standardized quality-of-life data exist. Many patients survive into adulthood, and dermatitis improves with age in a subset. Major morbidity includes severe eczema, food allergy, repeated infection, chronic sinusitis, bronchiectasis, gastrointestinal inflammation, treatment burden, and occasional autoimmunity or malignancy. (pietzsch2022hyperigeandcarcinoma pages 2-4, zhao2024anewdiseasecausingdominantnegative pages 8-9)

Poor prognostic indicators are inferred rather than validated: severe early infections, impaired T-cell proliferation, hypogammaglobulinemia/poor vaccine responses, persistent viral infection, bronchiectasis, inflammatory GI disease, and refractory dermatitis. In one patient, immunoglobulin reduced infections but did not prevent bronchiectasis. HPV-positive squamous carcinoma and cutaneous T-cell lymphoma have been reported, but absolute cancer risk is unknown. (pietzsch2022hyperigeandcarcinoma pages 2-4)

## 12. Treatment and current implementation

No curative, regulatory-approved CADINS-specific therapy or consensus algorithm exists. Treatment is individualized across dermatology, allergy, immunology, infectious disease, gastroenterology, and pulmonology.

1. **Skin-directed care:** emollients, trigger avoidance, topical corticosteroids, and topical calcineurin inhibitors are used as in conventional dermatitis, with infection surveillance. Topical tacrolimus controlled skin disease in one adult. Suggested NCIt concepts: **Topical Therapy**, **Corticosteroid Therapy**, and **Tacrolimus (NCIt:C1589)**. (izadi2021cadinsinan pages 1-3)
2. **Dupilumab:** IL-4Rα blockade targeting IL-4/IL-13 is mechanistically attractive. Marked eczema benefit has been reported in individual patients, apparently without reported adverse effects in the cited cases; controlled CADINS response rates are unavailable. Suggested NCIt: **Dupilumab (NCIt:C1576)**. (pietzsch2022hyperigeandcarcinoma pages 1-2, giancotta2023tailoredtreatmentsin pages 5-6)
3. **Other biologics:** mepolizumab and omalizumab have been proposed or reported in small experiences, but the retrieved evidence does not support a quantitative efficacy estimate or standard recommendation. (taietti2025inbornerrorsof pages 6-8)
4. **Immunoglobulin replacement:** indicated by clinically significant antibody deficiency, poor vaccine responses, and recurrent infections—not merely by genotype. Approximately half of one cohort had important humoral defects and required replacement. Benefit can be partial. Suggested NCIt: **Immunoglobulin Therapy (NCIt:C270)**. (izadi2021cadinsinan pages 1-3, urdinez2022expandingspectrumintrafamilial pages 15-17)
5. **Antimicrobials:** prompt treatment and, in selected patients, prophylaxis for persistent/severe infections. Evidence is expert practice rather than a CADINS trial. (izadi2021cadinsinan pages 3-4)
6. **Glutamine:** supplemental glutamine partially rescued mTORC1, proliferation, and IFN-γ defects in patient cells. This is in-vitro proof of correctability, not established dietary or pharmacologic therapy. Chemical ontology: **CHEBI:28300**. (pomerantz2022elevatedigefrom pages 4-6, izadi2021cadinsinan pages 3-4)
7. **HSCT:** not established for typical dominant-negative CADINS and was not listed as a standard CADINS option in a 2023 tailored-treatment summary. It may be considered only exceptionally for severe combined immune disease after specialist review; evidence from recessive CARD11 deficiency should not be extrapolated automatically. (giancotta2023tailoredtreatmentsin pages 4-5)

Allergen immunotherapy warrants caution: one adult stopped it because of frequent adverse reactions. No CARD11-directed gene therapy, CRISPR therapy, RNA therapy, or approved pharmacogenomic dosing guidance exists. Searches found no clearly relevant registered interventional CADINS trial; current implementation is therefore case-based precision management rather than trial-validated care.

## 13. Prevention

Primary prevention of the germline disorder is limited to reproductive options after molecular diagnosis: genetic counseling, familial cascade testing, prenatal diagnosis, and preimplantation genetic testing. For an affected heterozygous parent, the Mendelian transmission risk is 50% per pregnancy, although clinical severity cannot be predicted reliably because expressivity is variable.

Secondary/tertiary prevention includes early genomic diagnosis, periodic immunoglobulin and vaccine-antibody assessment, prompt infection treatment, pulmonary surveillance, skin-barrier care, nutritional/growth monitoring, and prevention of irreversible bronchiectasis. Live vaccines should be individualized according to measured cellular immune competence rather than prohibited solely because of the CARD11 genotype.

HPV vaccination, ideally with the 9-valent vaccine, plus age- and anatomy-appropriate HPV/cytology surveillance has been proposed after HPV-positive carcinoma in a CADINS family. This is expert precaution based on sparse observations, not prospective evidence. Suggested NCIt terms: **Human Papillomavirus Vaccine (NCIt:C1746)** and **Cancer Screening (NCIt:C17139)**. (pietzsch2022hyperigeandcarcinoma pages 6-7, pietzsch2022hyperigeandcarcinoma pages 1-2)

No lifestyle, dietary, environmental, or public-health measure can prevent inherited CADINS. Glutamine supplementation should not be represented as proven prophylaxis.

## 14. Other species and natural disease

No naturally occurring veterinary disorder confidently equivalent to human CADINS was identified. Accordingly, no affected breed, VBO term, animal incidence, zoonotic potential, or cross-species transmission applies. **Mus musculus** (NCBI Taxonomy **10090**) has the orthologous **Card11** gene and is used experimentally. The antigen-receptor/CBM signaling role is evolutionarily conserved, supporting comparative mechanistic inference, but mouse atopy does not fully reproduce human disease.

## 15. Model organisms and experimental systems

### Card11-R30W heterozygous mouse

A knock-in mouse expressing the patient-derived **Card11 R30W** allele models the dominant-negative state. It shows impaired T-, B-, and NK-cell signaling, a stronger signaling defect in T than B cells, reduced NK-cell IFN-γ with preserved cytotoxicity, reduced Treg numbers, and age-dependent elevated IgE with approximately 50% penetrance. It does **not** develop spontaneous atopic dermatitis or clear Th2 expansion, demonstrating that elevated IgE alone is insufficient for the complete human phenotype. Primary study: Hutcherson et al., *Journal of Immunology* 207:1150–1164, published August 2021; PMID **34341167**; DOI [10.4049/jimmunol.2001233](https://doi.org/10.4049/jimmunol.2001233). (hutcherson2021pathwayspecificdefectsin pages 1-3, pomerantz2022elevatedigefrom pages 8-10)

### Other models

Hypomorphic “unmodulated” Card11 mice develop pruritic dermatitis, elevated IgE, and allergy through differential impairment of Foxp3-positive Tregs versus Th2 effector cells. They are useful for studying signaling thresholds but do not model every human dominant-negative allele. Transfected Jurkat/JPM50.6 cells, primary patient T and B cells, reporter assays, and co-immunoprecipitation remain central for variant classification. Saturation functional assays provide scalable evidence for variant effects, although they cannot reproduce organism-level penetrance. (hutcherson2021pathwayspecificdefectsin pages 1-3, pietzsch2022hyperigeandcarcinoma pages 6-7, pomerantz2022elevatedigefrom pages 10-12)

No validated CADINS organoid, zebrafish, Drosophila, rat, iPSC, or humanized-mouse model was identified.

## Key primary sources and exact abstract excerpts

* **Ma et al., Nature Genetics, published June 2017; PMID 28628108; DOI [10.1038/ng.3898](https://doi.org/10.1038/ng.3898).** The discovery study reported: “*Through next-generation sequencing on a cohort of patients with severe atopic dermatitis with and without comorbid infections, we found eight individuals, from four families, with novel heterozygous mutations in CARD11*.” It further stated: “*The mTORC1 and IFN-γ production defects were partially rescued by supplementation with glutamine*.” (pomerantz2022elevatedigefrom pages 8-10)
* **Dorjbal et al., Journal of Allergy and Clinical Immunology, 2019; PMID 30170123.** The international cohort established that validated mutations disrupted TCR-induced NF-κB activation and that atopy occurred in approximately 89%. (pomerantz2022elevatedigefrom pages 8-10)
* **Hutcherson et al., Journal of Immunology, published August 2021; PMID 34341167; DOI [10.4049/jimmunol.2001233](https://doi.org/10.4049/jimmunol.2001233).** The abstract states: “*CARD11R30W/+ mice develop elevated serum IgE levels with 50% penetrance that becomes more pronounced with age, but do not develop spontaneous atopic dermatitis*.” (hutcherson2021pathwayspecificdefectsin pages 1-3)
* **Pietzsch et al., Frontiers in Immunology, published 16 May 2022; DOI [10.3389/fimmu.2022.878989](https://doi.org/10.3389/fimmu.2022.878989).** The abstract reports that the p.Arg75Trp variant had a dominant-negative effect and that “*one patient is under treatment with dupilumab, which has shown marked benefit in controlling severe eczema*.” (pietzsch2022hyperigeandcarcinoma pages 1-2)
* **Urdinez et al., Frontiers in Immunology, published 3 November 2022; DOI [10.3389/fimmu.2022.1020927](https://doi.org/10.3389/fimmu.2022.1020927).** This single-center series included 15 CARD11-associated cases—10 CADINS and 5 BENTA—and emphasized “*remarkable variability of disease expression…even within multiplex families*.” (urdinez2022expandingspectrumintrafamilial pages 1-2)
* **Zhao et al., Scientific Reports 14:24247, published October 2024; DOI [10.1038/s41598-024-71673-z](https://doi.org/10.1038/s41598-024-71673-z).** The abstract defines IMD11B as caused by germline dominant-negative CARD11 variants and reports that RNA sequencing “*confirmed that mutant CARD11 inhibited down-stream transcriptional activity of NF-κB*.” (zhao2024anewdiseasecausingdominantnegative pages 8-9)

## Knowledge gaps and curation cautions

The most important missing data are unbiased prevalence and incidence, prospective natural history, standardized penetrance, variant-level population frequencies, validated genotype–phenotype relationships, patient-reported outcomes, malignancy-risk estimates, controlled treatment trials, and single-cell/spatial/multi-omic profiling. Frequencies in this report should be encoded with their source cohort and denominator, not treated as universal. Variant classification should distinguish heterozygous dominant-negative CADINS from heterozygous activating BENTA and biallelic CARD11 deficiency. Finally, dupilumab is supported by case-level clinical benefit, whereas glutamine is principally an in-vitro mechanistic intervention; these evidence levels should remain separate in the knowledge base.

References

1. (pietzsch2022hyperigeandcarcinoma pages 1-2): Leonora Pietzsch, Julia Körholz, Felix Boschann, Mildred Sergon, Batsukh Dorjbal, Debra Yee, Vanessa Gilly, Eva Kämmerer, Diana Paul, Clemens Kastl, Martin W. Laass, Reinhard Berner, Eva Maria Jacobsen, Joachim Roesler, Daniela Aust, Min A. Lee-Kirsch, Andrew L. Snow, and Catharina Schuetz. Hyper-ige and carcinoma in cadins disease. Frontiers in Immunology, May 2022. URL: https://doi.org/10.3389/fimmu.2022.878989, doi:10.3389/fimmu.2022.878989. This article has 26 citations and is from a peer-reviewed journal.

2. (urdinez2022expandingspectrumintrafamilial pages 1-2): Luciano Urdinez, Lorenzo Erra, Alejandro M. Palma, María F. Mercogliano, Julieta Belén Fernandez, Emma Prieto, Verónica Goris, Andrea Bernasconi, Marianela Sanz, Mariana Villa, Carolina Bouso, Lucia Caputi, Belen Quesada, Daniel Solis, Anabel Aguirre Bruzzo, Maria Martha Katsicas, Laura Galluzzo, Christian Weyersberg, Marcela Bocian, Maria Marta Bujan, Matías Oleastro, María B. Almejun, and Silvia Danielian. Expanding spectrum, intrafamilial diversity, and therapeutic challenges from 15 patients with heterozygous card11-associated diseases: a single center experience. Frontiers in Immunology, Nov 2022. URL: https://doi.org/10.3389/fimmu.2022.1020927, doi:10.3389/fimmu.2022.1020927. This article has 27 citations and is from a peer-reviewed journal.

3. (garciamartinez2025fromsyndromicclues pages 1-2): Elena García-Martínez, María Teresa Schiaffino, Marisa Di Natale, María de las Mercedes Díaz Luna, Daniel Alejandro Viteri Álvarez, and María Alejandra Mejía González. From syndromic clues to diagnosis: understanding card11-driven disorders. Frontiers in Immunology, Jun 2025. URL: https://doi.org/10.3389/fimmu.2025.1626065, doi:10.3389/fimmu.2025.1626065. This article has 3 citations and is from a peer-reviewed journal.

4. (zhao2024anewdiseasecausingdominantnegative pages 8-9): Peiwei Zhao, Qingjie Meng, Yali Wu, Lei Zhang, Xiankai Zhang, Li Tan, Yan Ding, XiaoXia Lu, and Xuelian He. A new-disease-causing dominant-negative variant in card11 gene in a chinese case with recurrent fever. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-71673-z, doi:10.1038/s41598-024-71673-z. This article has 3 citations and is from a peer-reviewed journal.

5. (pomerantz2022elevatedigefrom pages 4-6): Joel L Pomerantz, Joshua D Milner, and Andrew L Snow. Elevated ige from attenuated card11 signaling: lessons from atopic mice and humans. Dec 2022. URL: https://doi.org/10.1016/j.coi.2022.102255, doi:10.1016/j.coi.2022.102255. This article has 13 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: Immunodeficiency 11B with atopic dermatitis-CARD11): Open Targets Query (Immunodeficiency 11B with atopic dermatitis-CARD11, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (pomerantz2022elevatedigefrom pages 8-10): Joel L Pomerantz, Joshua D Milner, and Andrew L Snow. Elevated ige from attenuated card11 signaling: lessons from atopic mice and humans. Dec 2022. URL: https://doi.org/10.1016/j.coi.2022.102255, doi:10.1016/j.coi.2022.102255. This article has 13 citations and is from a peer-reviewed journal.

8. (urdinez2022expandingspectrumintrafamilial pages 12-13): Luciano Urdinez, Lorenzo Erra, Alejandro M. Palma, María F. Mercogliano, Julieta Belén Fernandez, Emma Prieto, Verónica Goris, Andrea Bernasconi, Marianela Sanz, Mariana Villa, Carolina Bouso, Lucia Caputi, Belen Quesada, Daniel Solis, Anabel Aguirre Bruzzo, Maria Martha Katsicas, Laura Galluzzo, Christian Weyersberg, Marcela Bocian, Maria Marta Bujan, Matías Oleastro, María B. Almejun, and Silvia Danielian. Expanding spectrum, intrafamilial diversity, and therapeutic challenges from 15 patients with heterozygous card11-associated diseases: a single center experience. Frontiers in Immunology, Nov 2022. URL: https://doi.org/10.3389/fimmu.2022.1020927, doi:10.3389/fimmu.2022.1020927. This article has 27 citations and is from a peer-reviewed journal.

9. (pietzsch2022hyperigeandcarcinoma pages 2-4): Leonora Pietzsch, Julia Körholz, Felix Boschann, Mildred Sergon, Batsukh Dorjbal, Debra Yee, Vanessa Gilly, Eva Kämmerer, Diana Paul, Clemens Kastl, Martin W. Laass, Reinhard Berner, Eva Maria Jacobsen, Joachim Roesler, Daniela Aust, Min A. Lee-Kirsch, Andrew L. Snow, and Catharina Schuetz. Hyper-ige and carcinoma in cadins disease. Frontiers in Immunology, May 2022. URL: https://doi.org/10.3389/fimmu.2022.878989, doi:10.3389/fimmu.2022.878989. This article has 26 citations and is from a peer-reviewed journal.

10. (pietzsch2022hyperigeandcarcinoma pages 6-7): Leonora Pietzsch, Julia Körholz, Felix Boschann, Mildred Sergon, Batsukh Dorjbal, Debra Yee, Vanessa Gilly, Eva Kämmerer, Diana Paul, Clemens Kastl, Martin W. Laass, Reinhard Berner, Eva Maria Jacobsen, Joachim Roesler, Daniela Aust, Min A. Lee-Kirsch, Andrew L. Snow, and Catharina Schuetz. Hyper-ige and carcinoma in cadins disease. Frontiers in Immunology, May 2022. URL: https://doi.org/10.3389/fimmu.2022.878989, doi:10.3389/fimmu.2022.878989. This article has 26 citations and is from a peer-reviewed journal.

11. (izadi2021cadinsinan pages 1-3): Neema Izadi, Bradly M. Bauman, Gina Dabbah, Timothy J. Thauland, Manish J. Butte, Andrew L. Snow, and Joseph A. Church. Cadins in an adult with chronic sinusitis and atopic disease. Journal of Clinical Immunology, 41:256-258, Oct 2021. URL: https://doi.org/10.1007/s10875-020-00893-5, doi:10.1007/s10875-020-00893-5. This article has 12 citations and is from a domain leading peer-reviewed journal.

12. (urdinez2022expandingspectrumintrafamilial pages 15-17): Luciano Urdinez, Lorenzo Erra, Alejandro M. Palma, María F. Mercogliano, Julieta Belén Fernandez, Emma Prieto, Verónica Goris, Andrea Bernasconi, Marianela Sanz, Mariana Villa, Carolina Bouso, Lucia Caputi, Belen Quesada, Daniel Solis, Anabel Aguirre Bruzzo, Maria Martha Katsicas, Laura Galluzzo, Christian Weyersberg, Marcela Bocian, Maria Marta Bujan, Matías Oleastro, María B. Almejun, and Silvia Danielian. Expanding spectrum, intrafamilial diversity, and therapeutic challenges from 15 patients with heterozygous card11-associated diseases: a single center experience. Frontiers in Immunology, Nov 2022. URL: https://doi.org/10.3389/fimmu.2022.1020927, doi:10.3389/fimmu.2022.1020927. This article has 27 citations and is from a peer-reviewed journal.

13. (hutcherson2021pathwayspecificdefectsin pages 1-3): Shelby M Hutcherson, Jacquelyn R Bedsaul, and Joel L Pomerantz. Pathway-specific defects in t, b, and nk cells and age-dependent development of high ige in mice heterozygous for a cadins-associated dominant negative card11 allele. Journal of immunology (Baltimore, Md. : 1950), 207:1150-1164, Aug 2021. URL: https://doi.org/10.4049/jimmunol.2001233, doi:10.4049/jimmunol.2001233. This article has 23 citations.

14. (izadi2021cadinsinan pages 3-4): Neema Izadi, Bradly M. Bauman, Gina Dabbah, Timothy J. Thauland, Manish J. Butte, Andrew L. Snow, and Joseph A. Church. Cadins in an adult with chronic sinusitis and atopic disease. Journal of Clinical Immunology, 41:256-258, Oct 2021. URL: https://doi.org/10.1007/s10875-020-00893-5, doi:10.1007/s10875-020-00893-5. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (giancotta2023tailoredtreatmentsin pages 5-6): Carmela Giancotta, Nicole Colantoni, Lucia Pacillo, Veronica Santilli, Donato Amodio, Emma Concetta Manno, Nicola Cotugno, Gioacchino Andrea Rotulo, Beatrice Rivalta, Andrea Finocchi, Caterina Cancrini, Andrea Diociaiuti, May El Hachem, and Paola Zangari. Tailored treatments in inborn errors of immunity associated with atopy (ieis-a) with skin involvement. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1129249, doi:10.3389/fped.2023.1129249. This article has 20 citations.

16. (giancotta2023tailoredtreatmentsin pages 4-5): Carmela Giancotta, Nicole Colantoni, Lucia Pacillo, Veronica Santilli, Donato Amodio, Emma Concetta Manno, Nicola Cotugno, Gioacchino Andrea Rotulo, Beatrice Rivalta, Andrea Finocchi, Caterina Cancrini, Andrea Diociaiuti, May El Hachem, and Paola Zangari. Tailored treatments in inborn errors of immunity associated with atopy (ieis-a) with skin involvement. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1129249, doi:10.3389/fped.2023.1129249. This article has 20 citations.

17. ((henry)2023definingthepathogenesis pages 75-79): Yi-Chin (Henry) Lu. Defining the pathogenesis of human inborn errors of immunity affecting the card11-bcl10-malt1 complex. ArXiv, Jan 2023. URL: https://doi.org/10.14288/1.0394898, doi:10.14288/1.0394898. This article has 0 citations.

18. (pomerantz2022elevatedigefrom pages 10-12): Joel L Pomerantz, Joshua D Milner, and Andrew L Snow. Elevated ige from attenuated card11 signaling: lessons from atopic mice and humans. Dec 2022. URL: https://doi.org/10.1016/j.coi.2022.102255, doi:10.1016/j.coi.2022.102255. This article has 13 citations and is from a peer-reviewed journal.

19. (bauman2025dominantinterferingcard11 pages 14-15): Bradly M. Bauman, Jeffrey R. Stinson, Melissa A. Kallarakal, Lei Haley Huang, Andrew M. Frank, Gauthaman Sukumar, Nermina Saucier, Clifton L. Dalgard, Alice Y. Chan, Joshua D. Milner, Megan A. Cooper, and Andrew L. Snow. Dominant interfering card11 variants disrupt jnk signaling to promote gata3 expression in t cells. The Journal of experimental medicine, Mar 2025. URL: https://doi.org/10.1084/jem.20240272, doi:10.1084/jem.20240272. This article has 5 citations.

20. (taietti2025inbornerrorsof pages 6-8): Ivan Taietti, Francesco Catamerò, Lorenzo Lodi, Mattia Giovannini, and Riccardo Castagnoli. Inborn errors of immunity with atopic phenotypes in the allergy and immunology clinic: a practical review. Feb 2025. URL: https://doi.org/10.1097/aci.0000000000001059, doi:10.1097/aci.0000000000001059. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_11B_With_Atopic_Dermatitis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.
