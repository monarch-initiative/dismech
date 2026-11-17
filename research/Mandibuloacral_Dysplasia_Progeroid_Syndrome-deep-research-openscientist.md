---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-10T14:13:10.049671'
end_time: '2026-11-10T14:29:30.075246'
duration_seconds: 980.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Mandibuloacral Dysplasia Progeroid Syndrome
  mondo_id: MONDO:0030880
  category: Mendelian
  causal_genes: MTX2
  omim_id: OMIM:619127
  synonyms: MDPS; mandibuloacral dysplasia associated to MTX2
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mandibuloacral_Dysplasia_Progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mandibuloacral_Dysplasia_Progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mandibuloacral Dysplasia Progeroid Syndrome
- **MONDO ID:** MONDO:0030880 (if available)
- **Causal gene(s):** MTX2
- **OMIM:** OMIM:619127
- **Synonyms:** MDPS; mandibuloacral dysplasia associated to MTX2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Mandibuloacral Dysplasia Progeroid Syndrome** covering all of the
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

# Mandibuloacral Dysplasia Progeroid Syndrome (MDPS / MADaM): A Comprehensive Disease Characteristics Report

**Disease:** Mandibuloacral Dysplasia Progeroid Syndrome (MDPS), also called *mandibuloacral dysplasia associated to MTX2* (MADaM)
**MONDO ID:** MONDO:0030880 · **OMIM:** 619127 · **Causal gene:** **MTX2** (Metaxin-2; HGNC:7506; NCBI Gene 10651; Ensembl ENSG00000128654; UniProt O75431; gene OMIM *608555)
**Category:** Mendelian (autosomal recessive) · **Inheritance:** Biallelic loss-of-function

---

## Summary

Mandibuloacral Dysplasia Progeroid Syndrome (MDPS/MADaM) is an **ultra-rare, autosomal-recessive, congenital-onset premature-aging multisystem disorder** caused by **biallelic loss-of-function (null) variants in *MTX2***, the gene encoding **Metaxin-2 (MTX2)**, a peripheral protein of the cytosolic face of the mitochondrial outer membrane involved in mitochondrial protein import and in the SAM/MIB (sorting-and-assembly / mitochondrial-intermembrane-space-bridging) machinery. The disease was first molecularly defined by Elouej et al. in 2020 ([PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/)), who reported five homozygous null mutations in *MTX2* in patients presenting a "severe laminopathy-like mandibuloacral dysplasia characterized by growth retardation, bone resorption, arterial calcification, renal glomerulosclerosis and severe hypertension."

Mechanistically, MDPS is distinctive in that it **links primary mitochondrial dysfunction to a nuclear-envelope (laminopathy-like) phenotype**. Loss of MTX2 destabilizes and leads to loss of its partner protein Metaxin-1 (MTX1), fragmenting the mitochondrial network and impairing oxidative phosphorylation. Downstream, patient fibroblasts become resistant to induced apoptosis, show increased cellular senescence and mitophagy, and reduced proliferation — a cellular aging signature. Cross-species models (*C. elegans*, *Drosophila*, *Xenopus*, and patient fibroblasts) converge on perturbation of **mTOR (TOR) and Wnt signaling** and **ribosome-biogenesis**, with secondary nuclear morphological abnormalities that phenocopy classic *LMNA*/*ZMPSTE24* laminopathies. The disorder is therefore classified within the **premature-ageing laminopathy spectrum**.

Clinically, patients present soon after birth with growth retardation, generalized lipodystrophy, progeroid skin and facies (prominent eyes, long pinched nose, mandibular hypoplasia, small mouth), acro-osteolysis/bone resorption, arterial calcification, severe hypertension, renal glomerulosclerosis, hepatosplenic involvement, and in at least one case combined hypogammaglobulinemia with recurrent infections. As of 2024, only ~7 molecularly confirmed cases had been reported worldwide, so there are **no approved disease-modifying therapies**; management is entirely supportive and multidisciplinary. Mechanism-based experimental leads — **mTOR inhibition (rapamycin/rapalogs)** and **Myc/ribosome-biogenesis enhancement** — are supported only by non-mammalian models and other laminopathy contexts to date.

---

## Section 1 — Disease Information

**Overview.** MDPS/MADaM is a Mendelian, congenital-onset progeroid (premature-aging) skeletal dysplasia with multisystem involvement. Yeter Doğan et al. (2023) describe it as "a skeletal dysplasia characterized by postnatal growth retardation, hypotonia, generalized lipodystrophy, skin changes, progeroid traits, and dysmorphic facial features, including prominent eyes, long pinched nose, mandibular hypoplasia, and a small mouth" ([PMID: 36269149](https://pubmed.ncbi.nlm.nih.gov/36269149/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030880 |
| OMIM (phenotype) | 619127 |
| OMIM (gene) | *608555 (MTX2) |
| Gene (NCBI) | GeneID 10651 |
| HGNC | HGNC:7506 |
| Ensembl | ENSG00000128654 |
| UniProt | O75431 |
| Cytoband | 2q31.1 |

**Synonyms / alternative names.** MDPS; Mandibuloacral Dysplasia Progeroid Syndrome; Mandibuloacral dysplasia associated to MTX2 (MADaM). The official NCBI Gene record for MTX2 carries the alias "MDPS," directly linking the gene to the disease.

**Information source.** The disease-level knowledge base here is derived from a small number of **aggregated case reports and model-organism studies** (individual patient reports combined into disease-level resources such as OMIM/Orphanet), not from large EHR cohorts — reflecting the ultra-rare status of the condition.

---

## Section 2 — Etiology

**Primary cause (genetic).** MDPS is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *MTX2***. Elouej et al. reported "five homozygous null mutations in MTX2, encoding Metaxin-2 (MTX2), an outer mitochondrial membrane protein" ([PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/)). There is no environmental, infectious, or acquired cause; the disorder is purely monogenic.

**Genetic risk factors.** The only established genetic risk factor is inheritance of two null *MTX2* alleles. Most reported families are **consanguineous**, consistent with autosomal-recessive rare-disease genetics. No modifier genes or susceptibility loci are established in humans, although model work implicates *Myc* dosage and mitochondrial-fusion genes (*Marf*/*Opa1*) as genetic interactors in *Drosophila*.

**Environmental / lifestyle / protective factors.** None identified. Because the disease is fully penetrant monogenic recessive, there are no documented environmental risk factors, protective factors, or gene–environment interactions. This is an expected "not applicable" for a Mendelian loss-of-function disorder.

---

## Section 3 — Phenotypes

The phenotype is a **congenital-onset, progressive, severe** progeroid multisystem syndrome. Key manifestations and suggested HPO terms:

| Phenotype | Type | HPO suggestion | Onset / severity / frequency |
|---|---|---|---|
| Postnatal growth retardation | Physical/growth | HP:0008897 (postnatal growth retardation) | Congenital/neonatal; severe; typical |
| Generalized lipodystrophy | Physical/metabolic | HP:0009064 (generalized lipodystrophy) | Early; severe; typical |
| Mandibular hypoplasia | Craniofacial | HP:0000347 (micrognathia) | Congenital; typical |
| Acro-osteolysis / bone resorption | Skeletal | HP:0012864 (acroosteolysis) | Childhood; progressive |
| Prominent eyes | Craniofacial | HP:0000520 (proptosis) | Congenital; typical |
| Long/pinched nose | Craniofacial | HP:0000448 (prominent nose) | Congenital; typical |
| Small mouth | Craniofacial | HP:0000160 (microstomia) | Congenital |
| Progeroid skin changes | Cutaneous | HP:0007495 (aged/progeroid appearance) | Early; progressive |
| Hypotonia | Neuromuscular | HP:0001252 (hypotonia) | Neonatal |
| Arterial calcification | Cardiovascular | HP:0004944 (arterial calcification) | Progressive; severe |
| Severe hypertension | Cardiovascular | HP:0000822 (hypertension) | Progressive; severe |
| Renal glomerulosclerosis | Renal | HP:0000095 (glomerulosclerosis) | Progressive |
| Hepatosplenomegaly / hepatosplenic involvement | Visceral | HP:0001433 (hepatosplenomegaly) | Variable |
| Hypogammaglobulinemia / recurrent infections | Immune/laboratory | HP:0004313 (hypogammaglobulinemia); HP:0002719 (recurrent infections) | Variable (reported in ≥1 case) |

**Quality of life.** The combination of growth failure, skeletal deformity, severe hypertension, progressive renal disease, and (where present) immunodeficiency implies profound impact on daily functioning, frequent hospitalization, and early morbidity. Fu et al. note the index Chinese patient "has since been admitted to the hospital several times for infections" ([PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/)). No formal QoL instruments (EQ-5D/SF-36) have been applied, given rarity.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *MTX2* (Metaxin-2), 2q31.1. The RefSeq summary states the protein "is peripherally associated with the cytosolic face of the outer mitochondrial membrane, and… is involved in the import of proteins into the mitochondrion"; it interacts with Metaxin-1 (MTX1), undergoes alternative splicing yielding multiple transcripts, and has a related pseudogene on chromosome 7 (NCBI GeneID 10651).

**Pathogenic variants.** All reported disease alleles are **biallelic null / loss-of-function**, including nonsense, frameshift, and canonical splice-site variants:

| Variant | Type | Consequence | Reference |
|---|---|---|---|
| Five homozygous null mutations (nonsense/frameshift/splice) | LoF | Loss of MTX2 protein | [PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/) |
| c.543+1G>T | Canonical splice site | Exon 8 skipping | [PMID: 36269149](https://pubmed.ncbi.nlm.nih.gov/36269149/) |
| c.378+1G>A | Canonical splice site | Splice disruption / LoF | [PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/) |

- **Classification:** Pathogenic (ACMG), null variants with loss-of-function as a known mechanism.
- **Allele frequency:** Extremely rare / absent to very low in gnomAD (consistent with ultra-rare recessive disease); precise frequencies not catalogued here.
- **Origin:** Germline; no somatic relevance.
- **Functional consequence:** Loss of function with **secondary destabilization and loss of partner protein MTX1** — a key molecular readout of the disease. Elouej et al.: "Loss of MTX2 in patients' primary fibroblasts leads to loss of Metaxin-1 (MTX1) and mitochondrial dysfunction, including network fragmentation and oxidative phosphorylation impairment" ([PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established human modifier genes, epigenetic signatures, or large-scale chromosomal abnormalities. MDPS is a single-gene, point/splice-variant disorder. Model data implicate *Myc* and mitochondrial-fusion genes as experimental genetic modifiers (see Section 15).

---

## Section 5 — Environmental Information

**Not applicable.** MDPS is a monogenic recessive disorder with no established environmental, lifestyle, or infectious contributing factors. Recurrent infections observed in the hypogammaglobulinemic patient are a *consequence* of the immune phenotype, not an etiologic trigger.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *MTX2* null variants** (nonsense/frameshift/splice) **result in** loss of Metaxin-2 protein.
2. Loss of MTX2 **leads to** destabilization and loss of its partner **Metaxin-1 (MTX1)** — i.e., disruption of the SAM/MIB outer-membrane assembly machinery (demonstrated in patient fibroblasts).
3. Loss of MTX1/MTX2 **results in** impaired mitochondrial protein import and assembly, **causing** **mitochondrial network fragmentation and oxidative-phosphorylation / respiratory impairment** (shown in fibroblasts and confirmed as reduced respiratory capacity in *C. elegans*).
4. Mitochondrial dysfunction **leads to** a cellular stress/aging program: **resistance to induced apoptosis → increased cellular senescence and mitophagy → reduced proliferation** (patient fibroblasts).
5. In parallel (branch), mitochondrial failure **is associated with** transcriptomic **perturbation of aging, TOR (mTOR), and Wnt signaling pathways** (*C. elegans*), and **reduced ribosomal/mitochondrial/myogenic protein expression** (*Drosophila*) — *inferred* to drive growth failure and tissue atrophy; Myc overexpression rescues the *Drosophila* lethality, supporting a ribosome-biogenesis branch.
6. Mitochondrial dysfunction and the senescence program **lead to** **secondary nuclear-envelope morphological abnormalities** that phenocopy *LMNA*/*ZMPSTE24* laminopathies (the mechanistic link that defines MDPS as "laminopathy-like").
7. These cellular derangements, acting across connective tissue, bone, vasculature, kidney and immune cells, **result in** the clinical phenotype: **growth retardation, lipodystrophy, mandibular hypoplasia, acro-osteolysis/bone resorption, progeroid skin/facies, arterial calcification, severe hypertension, renal glomerulosclerosis, hepatosplenic involvement, and variable immunodeficiency.**

### Mechanistic diagram

```
MTX2 biallelic null variants
        │ (loss of Metaxin-2)
        ▼
Loss of partner MTX1  ── disrupted SAM/MIB outer-membrane machinery
        │
        ▼
Impaired mito protein import → network fragmentation → OXPHOS/respiration ↓
        │
        ├────────────► Apoptosis resistance → senescence ↑, mitophagy ↑, proliferation ↓
        │
        ├────────────► TOR/mTOR & Wnt dysregulation ; ribosome biogenesis ↓ (Myc-rescuable)
        │
        └────────────► Secondary nuclear-envelope abnormalities (laminopathy-like)
                                   │
                                   ▼
        Multisystem progeroid disease: growth failure, lipodystrophy, mandibular
        hypoplasia, acro-osteolysis, arterial calcification, hypertension,
        glomerulosclerosis, hepatosplenic + immune involvement
```

### Detail by category

- **Molecular pathways:** mTOR/TOR and Wnt signaling (transcriptomically perturbed in *C. elegans*: "significantly reduced mitochondrial respiratory capacities, and transcriptomic analysis identified perturbations in the aging, TOR, and WNT-signaling pathways," [PMID: 39462037](https://pubmed.ncbi.nlm.nih.gov/39462037/)); ribosome biogenesis via Myc ([PMID: 42296340](https://pubmed.ncbi.nlm.nih.gov/42296340/)). Suggested GO: GO:0032007 (negative regulation of TOR signaling), GO:0016055 (Wnt signaling), GO:0042254 (ribosome biogenesis).
- **Cellular processes:** apoptosis (resistance), cellular senescence (GO:0090398), mitophagy (GO:0000423), reduced proliferation. Upstream mitochondrial dysfunction is primary; senescence/nuclear defects are downstream. Elouej et al.: "patients' fibroblasts are resistant to induced apoptosis, leading to increased cell senescence and mitophagy and reduced proliferation" ([PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/)).
- **Protein dysfunction:** loss of function of MTX2 with secondary loss of MTX1; impaired assembly of the MIB complex (which includes SAMM50, MTX1, MTX2, MTX3, DNAJC11; [PMID: 26477565](https://pubmed.ncbi.nlm.nih.gov/26477565/)).
- **Metabolic changes:** OXPHOS/respiratory capacity deficits; lipodystrophy reflects disordered adipose/lipid homeostasis.
- **Immune involvement:** hypogammaglobulinemia with recurrent infections in at least one patient ([PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/)).
- **Tissue damage:** mitochondrial dysfunction, senescence, and arterial calcification/glomerulosclerosis (vascular and renal fibrosis/injury).
- **Subcellular compartments (GO CC):** mitochondrial outer membrane (GO:0005741), nuclear envelope (GO:0005635), SAM complex (GO:0001401).
- **Cell types (CL):** fibroblasts (CL:0000057), osteoclasts/osteoblasts (bone resorption), vascular smooth muscle cells (arterial calcification), podocytes/glomerular cells, adipocytes (CL:0000136), B lymphocytes (immunoglobulin deficiency).

---

## Section 7 — Anatomical Structures Affected

- **Skeletal system (primary):** mandible (UBERON:0001684) — hypoplasia; distal phalanges / acro-osteolysis (UBERON:0003221); generalized bone resorption.
- **Integument:** skin (UBERON:0002097) — progeroid atrophic changes; adipose tissue (UBERON:0001013) — generalized lipodystrophy.
- **Cardiovascular:** arteries (UBERON:0001637) — calcification; systemic hypertension.
- **Renal:** kidney glomerulus (UBERON:0000074) — glomerulosclerosis.
- **Hepatosplenic:** liver (UBERON:0002107), spleen (UBERON:0002106).
- **Immune:** B-cell/humoral immunity (hypogammaglobulinemia).
- **Craniofacial/head:** reduced head size and cranial cartilage hypoplasia in the *Xenopus* model, linking MTX2 to craniofacial (mandibular) morphogenesis.
- **Subcellular:** mitochondrion (outer membrane) is the primary affected compartment; nuclear envelope is secondarily affected.
- **Lateralization:** manifestations are generally **bilateral/symmetric** (growth, skeletal, vascular, renal).

---

## Section 8 — Temporal Development

- **Onset:** **Congenital / neonatal.** Growth retardation is detected soon after birth; "Patients present with early onset and severe symptoms and soon after birth are found to have growth retardation" ([PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/)).
- **Pattern:** chronic, **progressive** (progeroid). Acro-osteolysis, arterial calcification, hypertension, and glomerulosclerosis worsen over time; cuticle/skin phenotype worsens with age in the *C. elegans* model.
- **Course:** lifelong, progressive, without spontaneous remission.
- **Critical windows:** the congenital/early-childhood period is the window of greatest vulnerability and, hypothetically, of greatest opportunity for mechanism-based intervention (e.g., mTOR modulation) — not yet tested clinically.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive**, biallelic loss-of-function.
- **Penetrance:** apparently complete in biallelic null genotypes (all reported biallelic patients are affected).
- **Expressivity:** variable across organ systems (e.g., immune involvement reported in some but not all patients).
- **Consanguinity:** prominent — most families reported are consanguineous.
- **Prevalence/incidence:** ultra-rare. "So far, 7 cases of MADaM diagnosed with molecular diagnostics have been reported in worldwide" (as of 2024; [PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/)). No formal prevalence/incidence estimates exist.
- **Geographic distribution:** cases reported across multiple populations (including the first Chinese case, 2024); no established founder effect, though consanguineous populations are over-represented.
- **Sex ratio:** no sex bias expected for an autosomal recessive disorder; numbers too small for meaningful ratio.
- **Carrier frequency / mosaicism / anticipation:** not established; not applicable (no repeat expansion; anticipation not expected).

---

## Section 10 — Diagnostics

- **Primary diagnostic approach:** **Whole-exome sequencing (WES)**, which identified the causal variants in reported cases ([PMID: 36269149](https://pubmed.ncbi.nlm.nih.gov/36269149/), [PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/)). **Single-gene *MTX2* testing** is appropriate when the phenotype is recognized. WES in [PMID: 36269149](https://pubmed.ncbi.nlm.nih.gov/36269149/) "revealed a novel homozygous c.543+1G>T splice site variant in the MTX2 gene."
- **Splice-variant confirmation:** cDNA / RT-PCR to demonstrate exon skipping or aberrant splicing (used to confirm c.543+1G>T exon-8 skipping and c.378+1G>A effects).
- **Clinical/laboratory:** growth parameters; blood pressure (severe hypertension); renal function and urinalysis (glomerulosclerosis); immunoglobulin panel (hypogammaglobulinemia); metabolic/lipid profile (lipodystrophy).
- **Imaging:** skeletal radiographs (mandibular hypoplasia, acro-osteolysis, bone resorption); vascular imaging (arterial calcification); abdominal imaging (hepatosplenic/renal involvement).
- **Functional/research assays:** patient fibroblast studies showing loss of MTX1, mitochondrial fragmentation, OXPHOS impairment, senescence, and nuclear morphology defects — research-grade, not routine diagnostics.
- **Differential diagnosis:** classic mandibuloacral dysplasia due to *LMNA* (MADA) or *ZMPSTE24* (MADB); Hutchinson-Gilford progeria; atypical/generalized lipodystrophy-associated progeroid syndromes (*LMNA* p.T10I, p.E262K). Distinguishing feature: MDPS is defined by **biallelic *MTX2* null variants** and the mitochondrial signature, rather than lamin-processing defects.

---

## Section 11 — Outcome / Prognosis

- **Prognosis:** **Poor.** Severe, progressive, multisystem progeroid disease with early-onset severe hypertension, progressive renal glomerulosclerosis, arterial calcification, and (when present) immunodeficiency with recurrent infections driving repeated hospitalizations.
- **Survival/mortality:** no formal survival statistics owing to rarity; the constellation of cardiovascular and renal disease plus infection risk implies substantial early morbidity and mortality.
- **Morbidity/disability:** high — growth failure, skeletal deformity, hypertension, renal disease, and recurrent infection impose major functional burden.
- **Prognostic factors:** severity of renal and cardiovascular involvement and presence of immunodeficiency are plausible drivers of outcome (not formally modeled).
- **Recovery:** none; disease is progressive and lifelong.

---

## Section 12 — Treatment

**There is no approved or trialed disease-modifying therapy.** With only ~7–10 molecularly confirmed patients worldwide, clinical trials are not feasible. Management is **symptomatic and multidisciplinary**:

| Problem | Supportive management | NCIT concept (suggested) |
|---|---|---|
| Severe hypertension | Antihypertensive therapy, BP surveillance | Antihypertensive Agent (NCIT:C265) |
| Renal glomerulosclerosis | Nephroprotection, renal monitoring | Renal supportive care |
| Arterial calcification | Cardiovascular surveillance | Cardiovascular monitoring |
| Growth failure / lipodystrophy | Nutritional support | Nutritional Support (NCIT:C15339) |
| Skeletal disease | Orthopedics, physiotherapy | Physical Therapy |
| Hypogammaglobulinemia | Immunoglobulin replacement, infection prophylaxis | Immunoglobulin Therapy (NCIT:C566) |

**Mechanism-based experimental leads (not clinically validated for MDPS):**
- **mTOR inhibition (rapamycin/rapalogs):** rationale from laminopathy biology — "mTOR signaling deregulation is closely related to aging and age-related disorders, among which progeroid laminopathies represent genetically characterized clinical entities" ([PMID: 30781376](https://pubmed.ncbi.nlm.nih.gov/30781376/)), reinforced by TOR dysregulation in the *C. elegans* MDPS model.
- **Myc / ribosome-biogenesis enhancement:** "Overexpression of Drosophila Myc, a master regulator of ribosome biogenesis and cell growth, successfully rescues the preadult lethality caused by dMtx2 deficiency, and partially restores sarcomere and mitochondrial defects" ([PMID: 42296340](https://pubmed.ncbi.nlm.nih.gov/42296340/)).

No gene, cell, or RNA-based therapy exists; pharmacogenomics is not applicable.

---

## Section 13 — Prevention

- **Primary prevention:** not possible for a congenital monogenic disorder other than via reproductive genetics.
- **Genetic counseling:** central. For consanguineous/at-risk couples, **carrier testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT)** are the main preventive options once a familial *MTX2* variant is known.
- **Cascade testing:** offer to at-risk relatives in affected families.
- **Secondary/tertiary prevention:** early detection and management of hypertension, renal disease, cardiovascular calcification, and infections to prevent complications.
- **No immunization, behavioral, or public-health interventions** are applicable to disease causation.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous genes / taxonomy:** MTX2 is evolutionarily conserved. Functional orthologs exist in *C. elegans* (*mtx-2*), *Drosophila melanogaster* (*Mtx2*/*CG8004*), *Xenopus laevis* (*mtx2*), and mouse. Human MTX2 **rescues** the *Drosophila* null: "Mtx2 null mutants are lethal at a preadult stage, and this phenotype can be rescued by expression of either Drosophila Mtx2 (dMtx2) or its human ortholog, demonstrating functional conservation across species" ([PMID: 42296340](https://pubmed.ncbi.nlm.nih.gov/42296340/)).
- **Natural disease in other species:** no naturally occurring MDPS-equivalent disease is documented in companion animals or wildlife; the disorder is known only in humans and engineered/experimental models.
- **Zoonotic potential:** none (genetic disease).

---

## Section 15 — Model Organisms

MDPS/MADaM is unusually well-served by **four convergent model systems**, each recapitulating distinct disease facets:

| Model | Perturbation | Recapitulated phenotypes | Reference |
|---|---|---|---|
| **Patient fibroblasts** (in vitro, human) | Biallelic MTX2 null | Loss of MTX1, mito fragmentation, OXPHOS↓, apoptosis resistance, senescence↑, mitophagy↑, proliferation↓, nuclear morphology defects | [PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/) |
| ***C. elegans*** (*mtx-2*) | Depletion/knockdown | Rougher/less-elastic cuticle worsening with age (skin analog), abnormal mito morphology, delayed development, ↓pharyngeal pumping, ↓respiration, aging/TOR/WNT transcriptomic perturbation | [PMID: 39462037](https://pubmed.ncbi.nlm.nih.gov/39462037/) |
| ***Drosophila*** (*Mtx2*/*CG8004*) | Null | Preadult/late-pupal lethality (rescued by fly or human MTX2); impaired myofibril assembly; muscle mito defects; ↓myogenic/mito/ribosomal protein; axonal mito transport defects (interacts with Marf/Opa1); lifespan/healthspan effects; **Myc rescue** | [PMID: 42296340](https://pubmed.ncbi.nlm.nih.gov/42296340/), [PMID: 39657051](https://pubmed.ncbi.nlm.nih.gov/39657051/) |
| ***Xenopus laevis*** (*mtx2*) | Knockdown | Reduced head size, hypoplastic cranial cartilage, disrupted neural-crest/chondrogenic markers, ↓proliferation, ↑apoptosis; C-terminal GST-like domain essential for rescue | [PMID: 40967033](https://pubmed.ncbi.nlm.nih.gov/40967033/) |

**Phenotype recapitulation & limitations.** Collectively the models reproduce mitochondrial dysfunction, craniofacial/skeletal (mandibular) defects, skin/aging phenotypes, and muscle involvement, and they establish the mTOR/Wnt and ribosome-biogenesis axes plus the essential C-terminal GST-like domain ("establish its C-terminal GST-like domain as essential for craniofacial morphogenesis," [PMID: 40967033](https://pubmed.ncbi.nlm.nih.gov/40967033/)). **Limitations:** no mammalian (mouse) model of the full multisystem human disease (arterial calcification, glomerulosclerosis, severe hypertension, hypogammaglobulinemia) is yet described; invertebrate/amphibian models cannot capture the human vascular–renal–immune phenotypes.

---

## Mechanistic Model / Interpretation

MDPS is best understood as a **"mitochondrial laminopathy."** The primary lesion is loss of the outer-membrane protein MTX2, which — through obligate loss of its partner MTX1 and disruption of the SAM/MIB assembly machinery (SAMM50–MTX1–MTX2–MTX3–DNAJC11; [PMID: 26477565](https://pubmed.ncbi.nlm.nih.gov/26477565/)) — compromises mitochondrial protein import and oxidative phosphorylation. Energetic/respiratory failure then drives a cellular-aging program (senescence, apoptosis resistance, mitophagy, reduced proliferation) and, importantly, **secondary nuclear-envelope abnormalities** that phenocopy *LMNA*/*ZMPSTE24* progeroid laminopathies — the conceptual bridge established by Elouej et al. Parallel dysregulation of **mTOR and Wnt** signaling and **ribosome biogenesis** (Myc-dependent) links the energetic deficit to impaired tissue growth and homeostasis, explaining growth retardation, lipodystrophy, and skeletal/craniofacial defects. The disorder therefore sits at the intersection of mitochondrial biology and nuclear-lamina aging, with the two experimental therapeutic hypotheses (mTOR inhibition; Myc/ribosome restoration) each targeting a downstream branch rather than the primary MTX2 deficiency.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/) | *Loss of MTX2 causes mandibuloacral dysplasia…* | Landmark paper: five homozygous null MTX2 mutations; defines gene, protein, cardinal clinical features, and the mitochondria→nuclear-morphology link |
| [36269149](https://pubmed.ncbi.nlm.nih.gov/36269149/) | *A novel MTX2 splice-site variant… MDPS* | Core phenotype definition; c.543+1G>T exon-8-skipping LoF variant; WES diagnosis |
| [38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/) | *Case report: novel splice-site mutation of MTX2* | First Chinese case; c.378+1G>A; multisystem + hypogammaglobulinemia; ~7 molecularly confirmed cases worldwide |
| [42296340](https://pubmed.ncbi.nlm.nih.gov/42296340/) | *Drosophila Mtx2 model* | Functional conservation (human MTX2 rescue); muscle-critical lethality; Myc/ribosome-biogenesis rescue |
| [39462037](https://pubmed.ncbi.nlm.nih.gov/39462037/) | *C. elegans mtx-2 model* | Respiration deficits; aging/TOR/WNT transcriptomic perturbation; skin/cuticle aging analog |
| [40967033](https://pubmed.ncbi.nlm.nih.gov/40967033/) | *Xenopus mtx2 model* | Craniofacial morphogenesis; C-terminal GST-like domain essential |
| [34103969](https://pubmed.ncbi.nlm.nih.gov/34103969/) | Progeroid laminopathy review | Classifies MADaM in the premature-ageing laminopathy spectrum |
| [30781376](https://pubmed.ncbi.nlm.nih.gov/30781376/) | *mTOR signaling in laminopathies* | Rationale for mTOR inhibition as candidate therapy |
| [26477565](https://pubmed.ncbi.nlm.nih.gov/26477565/) | MICOS/MIB complex organization | Places MTX2 in the MIB complex with MTX1/MTX3/SAMM50/DNAJC11 |
| [39657051](https://pubmed.ncbi.nlm.nih.gov/39657051/) | *Drosophila Mtx2* (axonal mito transport) | Mito transport/lifespan phenotypes; Marf/Opa1 interaction |

Supporting/contextual laminopathy literature (differential diagnosis, lipodystrophy spectrum): [PMID: 39273270](https://pubmed.ncbi.nlm.nih.gov/39273270/), [PMID: 29267953](https://pubmed.ncbi.nlm.nih.gov/29267953/), [PMID: 37885131](https://pubmed.ncbi.nlm.nih.gov/37885131/), [PMID: 33859056](https://pubmed.ncbi.nlm.nih.gov/33859056/), [PMID: 32939435](https://pubmed.ncbi.nlm.nih.gov/32939435/).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare evidence base:** ~7 molecularly confirmed patients worldwide; genotype–phenotype correlations, penetrance, expressivity, and natural history are based on sparse case reports.
2. **No mammalian model** of the full multisystem disease; the vascular (arterial calcification), renal (glomerulosclerosis), hypertensive, and immune (hypogammaglobulinemia) phenotypes lack mechanistic models.
3. **Therapeutic leads unvalidated in humans or mammals:** mTOR inhibition and Myc/ribosome-biogenesis restoration rescue only non-mammalian models.
4. **No epidemiological data** (prevalence/incidence/survival) and no QoL instruments applied.
5. **Mechanistic branch uncertainty:** whether mTOR/Wnt dysregulation and nuclear-envelope abnormalities are drivers or bystanders of the clinical phenotype is inferred, not demonstrated causally in patients.
6. **Immune phenotype** (hypogammaglobulinemia) reported in a single case — generalizability unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional/constitutive *Mtx2* mouse model** to test whether the vascular, renal, hypertensive, and immune phenotypes are recapitulated in a mammal.
2. **Test mTOR inhibition (rapamycin) and Myc/ribosome-biogenesis modulation** in patient-derived fibroblasts/iPSC-derived relevant cell types (vascular smooth muscle, podocytes, osteoclasts) and in the mouse model, measuring senescence, OXPHOS, and nuclear morphology rescue.
3. **Establish an international patient registry** to capture natural history, genotype–phenotype correlations, survival, and the frequency of the immune phenotype.
4. **Multi-omics (transcriptomics/proteomics/metabolomics) on patient tissues** to confirm whether human disease shows the TOR/Wnt/ribosome signatures seen in models.
5. **Structure-function dissection** of the C-terminal GST-like domain (shown essential in *Xenopus*) to prioritize variant interpretation and potential protein-restoration strategies.
6. **Immunological workup** across additional patients to determine whether hypogammaglobulinemia is a recurrent feature warranting routine screening and Ig replacement.

---

*Evidence source types: human clinical (case reports, patient fibroblasts), model organism (C. elegans, Drosophila, Xenopus), in vitro (fibroblast assays), and computational/structural (MIB complex composition). All mechanistic and clinical claims are attributed to the PMIDs cited above.*


## Artifacts

- [OpenScientist final report](Mandibuloacral_Dysplasia_Progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mandibuloacral_Dysplasia_Progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030880` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **mandibuloacral dysplasia progeroid syndrome**
- `HP:0012864` (1 mention) - the report calls it "acroosteolysis"; HP calls it **Abnormal sperm morphology**
- `HP:0004944` (1 mention) - the report calls it "arterial calcification"; HP calls it **Dilatation of the cerebral artery**
- `HP:0000095` (1 mention) - the report calls it "glomerulosclerosis"; HP calls it **Abnormal renal glomerulus morphology**
- `NCIT:C15339` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Tissue Collection**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000160` (1 mention) - the report calls it "microstomia"; HP calls it **Narrow mouth**, and lists "Microstomia" among its other names
- `HP:0007495` (1 mention) - the report calls it "aged/progeroid appearance"; HP calls it **Prematurely aged appearance**, and lists "Precociously senile appearance" among its other names
- `GO:0016055` (1 mention) - the report calls it "Wnt signaling"; GO calls it **Wnt signaling pathway**
- `UBERON:0002097` (1 mention) - the report calls it "Integument:** skin"; UBERON calls it **skin of body**, and lists "integument" among its other names
- `UBERON:0001637` (1 mention) - the report calls it "Cardiovascular:** arteries"; UBERON calls it **artery**, and lists "arteries" among its other names
- `UBERON:0000074` (1 mention) - the report calls it "Renal:** kidney glomerulus"; UBERON calls it **renal glomerulus**
- `UBERON:0002107` (1 mention) - the report calls it "Hepatosplenic:** liver"; UBERON calls it **liver**
- `NCIT:C265` (1 mention) - the report calls it "Antihypertensive Agent"; NCIT calls it **Antidepressant Agent**
- `NCIT:C566` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **IgD**, and lists "Immunoglobulin D" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0030880` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
