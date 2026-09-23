---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T07:02:22.176787'
end_time: '2026-09-01T07:43:07.567280'
duration_seconds: 2445.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia Type 2
  mondo_id: ''
  category: Mendelian
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 33
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hereditary_Hemorrhagic_Telangiectasia_Type_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Hemorrhagic_Telangiectasia_Type_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia Type 2** covering all of the
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

# Hereditary Hemorrhagic Telangiectasia Type 2 (HHT2): Comprehensive Disease Characteristics Report

**Disease:** Hereditary Hemorrhagic Telangiectasia Type 2
**MONDO ID:** MONDO:0010880
**OMIM:** #600376 (phenotype); *601284 (ACVRL1 gene)
**Orphanet:** ORPHA:774 (parent HHT) | **ICD-10:** I78.0 | **MeSH:** D013683
**Category:** Mendelian (autosomal dominant)

---

## Summary

Hereditary Hemorrhagic Telangiectasia Type 2 (HHT2, Rendu–Osler–Weber syndrome, type 2) is an autosomal dominant vascular dysplasia caused by germline heterozygous **loss-of-function mutations in *ACVRL1*** (also called *ALK1*, on chromosome 12q13), which encodes the endothelial type I TGF-β/BMP receptor **activin receptor-like kinase 1 (ALK1)**. ALK1 binds the circulating ligands **BMP9 and BMP10** with high affinity and signals through **SMAD1/5/8** to maintain vascular quiescence and arterial identity. Haploinsufficiency of ALK1 de-represses angiogenesis, producing the two clinical hallmarks of HHT: fragile mucocutaneous **telangiectases** and larger visceral **arteriovenous malformations (AVMs)** that shunt blood directly from arteries to veins, bypassing capillary beds ([PMID: 33513792](https://pubmed.ncbi.nlm.nih.gov/33513792/), [PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/)).

HHT2 has a **distinct genotype–phenotype profile** compared with *ENG*-associated HHT1: epistaxis begins later and is less penetrant, pulmonary and cerebral AVMs are fewer, but hepatic AVMs, gastrointestinal bleeding, and pulmonary arterial hypertension (PAH, ~20% of *ACVRL1* carriers) are more common ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/), [PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/), [PMID: 42516693](https://pubmed.ncbi.nlm.nih.gov/42516693/)). The combined clinical prevalence of HHT is roughly **1 in 5,000**, though genomic-database analyses suggest the true genetic prevalence is 1.5–4-fold higher, indicating substantial underdiagnosis ([PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)).

Diagnosis combines the four clinical **Curaçao criteria** with molecular confirmation by *ACVRL1* sequencing, and management follows the **Second International HHT Guidelines** (2020): AVM screening and embolization, hematologic support for anemia, and disease-modifying **antiangiogenic therapies** (bevacizumab, pazopanib, thalidomide, and—newly validated in a randomized trial—**pomalidomide**) ([PMID: 32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/), [PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/), [PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)). Notably, *ACVRL1*/HHT2 genotype trends toward a **less robust pomalidomide response**, a first hint of genotype-guided therapy in HHT ([PMID: 41719457](https://pubmed.ncbi.nlm.nih.gov/41719457/)).

---

## 1. Disease Information

**Overview.** HHT2 is one subtype of hereditary hemorrhagic telangiectasia, a systemic autosomal dominant fibrovascular dysplasia characterized by the absence of normal capillary beds between arterioles and venules, leading to direct artery-to-vein connections. Small superficial lesions present as **telangiectases** (skin, lips, oral/nasal mucosa, fingers); larger lesions form visceral **AVMs** (lungs, liver, brain, GI tract, spinal cord). Lesions are fragile and prone to hemorrhage, producing recurrent epistaxis and internal bleeding ([PMID: 37695357](https://pubmed.ncbi.nlm.nih.gov/37695357/)).

**Key identifiers (machine-verified via EBI OLS4 and MyGene.info):**

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0010880** ("telangiectasia, hereditary hemorrhagic, type 2") |
| OMIM (phenotype) | **#600376** |
| OMIM (gene) | *601284 (ACVRL1) |
| Orphanet | ORPHA:774 (HHT, parent) |
| ICD-10 | I78.0 |
| MeSH | D013683 |
| Parent term | MONDO:0019180 (hereditary hemorrhagic telangiectasia) |

**Related subtypes:** HHT1 (MONDO:0008535, *ENG*), HHT3 (MONDO:0010996), HHT4 (MONDO:0012532), HHT5 (MONDO:0014217, *GDF2*/BMP9), and juvenile polyposis–HHT (MONDO:0008278, *SMAD4*).

**Synonyms:** HHT type 2; Osler–Weber–Rendu syndrome type 2; Rendu–Osler–Weber disease type 2; ACVRL1-related HHT; ALK1-related HHT.

**Information source.** This report is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, curated genotype–phenotype cohort studies, and international registries such as Cure HHT and the Danish HHT Database), supplemented by cohort-level clinical studies rather than individual EHR records.

---

## 2. Etiology

**Primary cause.** HHT2 is a monogenic Mendelian disorder caused by **germline heterozygous loss-of-function mutations in *ACVRL1***. ALK1 and endoglin (ENG) are transmembrane receptors on endothelial cells that bind circulating BMP9/BMP10 and activate SMAD1/5/8; *ACVRL1* haploinsufficiency reduces this signaling and is the root cause of HHT2 ([PMID: 33513792](https://pubmed.ncbi.nlm.nih.gov/33513792/)).

> "HHT is primarily associated with a reduction in endoglin (ENG) or ACVRL1 activity due to loss-of-function mutations. ENG and ACVRL1 transmembrane receptors are expressed on endothelial cells (ECs) and bind to circulating ligands BMP9 and BMP10 with high affinity. Ligand binding to the receptor complex leads to activation of the SMAD1/5/8 signalling pathway to regulate downstream gene expression." — [PMID: 33513792](https://pubmed.ncbi.nlm.nih.gov/33513792/)

**Genetic risk factors.** The causal variant is a heterozygous *ACVRL1* mutation. Mutations cluster largely in **exons 7 and 8**, which encode the intracellular serine/threonine kinase domain ([PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/)). Family history is the single strongest risk factor: almost all cases are inherited, with a 50% transmission risk to offspring. **Truncating *ACVRL1* mutations** are associated with a higher frequency of epistaxis and telangiectasis ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)).

**Environmental / lifestyle risk factors.** HHT is not caused by environmental exposures, but physiological factors modulate expression. **Blood flow / fluid shear stress** is a key mechanistic modifier—AVMs develop preferentially at sites of altered flow, and *acvrl1* transcription itself is flow- and ligand-dependent ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)). **Pregnancy** is a high-risk period (peripheral vasodilation, increased cardiac output) with reported heart failure, intracranial/pulmonary hemorrhage, and stroke ([PMID: 28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/)). Age increases lesion burden and epistaxis severity.

**Protective factors.** No validated genetic or environmental protective alleles are established for HHT2. Mechanistically, **restoring or enhancing ALK1 signaling** (e.g., ACVRL1 overexpression, BMP9/BMP10 supplementation) is protective in models—overexpression of *Acvrl1* prevents AVM development in both *Acvrl1*- and *Eng*-null mice ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)).

**Gene–environment interactions.** The dominant GxE axis is **flow × genotype**: physiological shear stress synergizes with BMP9/BMP10–ALK1–SMAD signaling to maintain vessel stability; ALK1 haploinsufficiency lowers this protective set point, so hemodynamic stress precipitates AVM formation ([PMID: 37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/), [PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)). A "second hit" (somatic mutation, injury, inflammation, angiogenic stimulus) is thought to convert focal haploinsufficiency into a discrete lesion, explaining the sporadic, focal nature of AVMs on a uniformly heterozygous genetic background.

---

## 3. Phenotypes

HHT2 phenotypes span symptoms, clinical signs, physical manifestations, and laboratory abnormalities. Frequencies below are drawn primarily from the French–Italian HHT network (93 HHT1, 250 HHT2), a Dutch cohort, and international QoL studies.

| Phenotype | Type | HPO term | Onset | Frequency / severity in HHT2 |
|---|---|---|---|---|
| Recurrent epistaxis | Symptom/sign | HP:0000421 (epistaxis) | Later than HHT1; incomplete penetrance | Most common symptom; **92%** in large QoL cohort ([PMID: 40055726](https://pubmed.ncbi.nlm.nih.gov/40055726/)); occurs later with incomplete penetrance (P<0.0001) ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)) |
| Mucocutaneous telangiectases | Physical sign | HP:0000562 (telangiectasia of the skin) | Progressive with age | Characteristic sites: lips, tongue, fingers, nasal mucosa |
| Hepatic AVM / liver involvement | Clinical sign | HP:0100761 (visceral AVM); hepatic | Adult; silent in children | **More common in HHT2**; symptomatic hepatic involvement seen only in HHT2 ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)); silent in 35% of HHT2 children by imaging ([PMID: 28248153](https://pubmed.ncbi.nlm.nih.gov/28248153/)) |
| GI bleeding | Symptom | HP:0002239 (GI hemorrhage) | Adult/late-onset | **16.4%** in HHT2 vs 6.5% HHT1 (P=0.017) ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)) |
| Pulmonary AVM | Clinical sign | HP:0002110 (pulmonary AVM) | Variable | **Less frequent/smaller** than HHT1: symptomatic PAVM 5.2% vs 34.4% (P<0.001) ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)) |
| Cerebral AVM | Clinical sign | HP:0002408 (CNS AVM) | Congenital/variable | Less common than HHT1; cerebral abscess 0.8% vs 7.5% ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)) |
| Spinal AVM | Clinical sign | HP:0002435 | — | **Seen only in HHT2** ([PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/)) |
| Pulmonary arterial hypertension | Clinical sign/lab | HP:0002092 (PAH) | Adult (occasionally infant) | ~**20%** of *ACVRL1* carriers ([PMID: 42516693](https://pubmed.ncbi.nlm.nih.gov/42516693/)) |
| Iron-deficiency anemia | Lab abnormality | HP:0001891 | Secondary to bleeding | 28.9% vs 15.1% in inpatients ([PMID: 33779866](https://pubmed.ncbi.nlm.nih.gov/33779866/)) |
| Fatigue | Symptom | HP:0012378 | Chronic | **79%** in QoL cohort ([PMID: 40055726](https://pubmed.ncbi.nlm.nih.gov/40055726/)) |

**Severity and progression.** Manifestations are typically **progressive** (telangiectases and epistaxis worsen with age) with **episodic** bleeding. Expressivity is highly variable even within families.

**Quality-of-life impact.** HHT imposes a substantial QoL burden driven chiefly by epistaxis and fatigue, with strong links to anxiety, depression, and reduced SF-36 scores. In the international Cure HHT study (n=565 completers), Epistaxis Severity Score (ESS) correlated positively with anxiety, depression, and fatigue and negatively with SF-36 (ESS vs SF-36 −26.4 [95% CI −33 to −19.9]) ([PMID: 40055726](https://pubmed.ncbi.nlm.nih.gov/40055726/)).

> "The most common symptoms were epistaxis 521/565 (92%) and fatigue 446/565 (79%)." — [PMID: 40055726](https://pubmed.ncbi.nlm.nih.gov/40055726/)

In the Danish HHT Database (n=124), ESS negatively correlated with SF-36 General Health (−4.14 [−6.01; −2.27], p<0.001), with age the only ESS predictor and **no association of ESS with sex, HHT type, or anticoagulation** ([PMID: 42419030](https://pubmed.ncbi.nlm.nih.gov/42419030/)). Comorbid liver and GI AVMs—prominent in HHT2—further reduce physical QoL scores ([PMID: 34857410](https://pubmed.ncbi.nlm.nih.gov/34857410/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***ACVRL1*** (activin A receptor-like type 1 / ALK1). HGNC:175; NCBI Gene 94; Ensembl ENSG00000139567; cytoband **12q13.13**; UniProt **P37023**; gene OMIM *601284. Protein-coding; the encoded ALK1 is a 503-amino-acid endothelial type I TGF-β/BMP receptor.

**Pathogenic variants.**
- **Variant types:** missense (dominant in the kinase domain), nonsense, frameshift, splice-site, and small in-frame indels; large deletions/duplications also occur (detected by MLPA/del-dup analysis).
- **Location:** mutations cluster largely in **exons 7 and 8**, encoding the serine/threonine kinase domain, whereas *ENG* (HHT1) mutations are widely distributed ([PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/)).

> "Mutations in ACVRL1 cluster largely in exons 7 and 8, but ENG mutations were widely distributed within that gene." — [PMID: 16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/)

- **Classification (ACMG/AMP):** the majority of reported disease alleles are pathogenic or likely pathogenic; VUS are common for novel missense variants and can be resolved by functional assays and cosegregation.
- **Origin:** germline (heterozygous). **De novo** cases and **mosaicism** are uncommon but documented—mosaic *ENG*/*ACVRL1* mutations may be present at ≤25% allele fraction and can be missed by Sanger, requiring high-depth NGS ([PMID: 21415079](https://pubmed.ncbi.nlm.nih.gov/21415079/), [PMID: 29243366](https://pubmed.ncbi.nlm.nih.gov/29243366/)).
- **Functional consequence:** **loss of function / haploinsufficiency** (reduced ALK1 signaling); some missense kinase-domain variants may act in a dominant-negative fashion on the receptor complex.

**Allele frequency.** Individually rare; genomic-database analysis (gnomAD, All of Us, Regeneron Million Exome) estimates combined *ENG*+*ACVRL1* pathogenic/likely-pathogenic genetic prevalence at **1.753–2.555 per 5,000**, rising to 2.874–4.327 per 5,000 including potentially pathogenic variants ([PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)).

**Domain architecture (why exon 7–8 mutations abolish function; UniProt P37023, verified).** ALK1 comprises: an **extracellular ligand-binding domain** (aa 22–118; cysteine-rich snake-toxin-like fold with disulfides C34–C51, C36–C41, C46–C69, C77–C89, C90–C95; N-glycosylation at N98; residues 73–76 confer BMP-ligand specificity); a single **transmembrane helix** (aa 119–141); and a cytoplasmic region (aa 142–503) containing the regulatory **GS domain** (aa 172–201; regulatory phosphoserines S155/S160/S161) and the **serine/threonine kinase domain** (aa 202–492; ATP site aa 208–216 and K229; catalytic aspartate D330). Kinase-domain (exon 7–8) mutations abolish SMAD1/5/8 phosphorylation. InterPro/Pfam: GS domain (IPR003605/PF08515), kinase domain (IPR000719/PF07714), TGFB_receptor (IPR000333). Experimental structures: extracellular domain (PDB 2LCR NMR; 4FAO, 6SF1/6SF2/6SF3, 7PPC including BMP9/BMP10 complexes) and intracellular kinase domain (PDB 3MY0, 2.65 Å, aa 195–497).

**Modifier genes.** The HHT phenotype is modified by other pathway members; the *ENG*/*ACVRL1*/*SMAD4*/*GDF2* network shapes severity. *SMAD4* (downstream of ALK1) loss recapitulates AVM formation and defines the JP-HHT overlap. Formal quantitative modifier loci for HHT2 severity remain incompletely defined.

**Epigenetic / chromosomal information.** No recurrent epigenetic signature or large-scale chromosomal abnormality is established as causal for HHT2. Large *ACVRL1* deletions are detectable by MLPA/CMA but are a minority of alleles.

---

## 5. Environmental Information

HHT2 is a **monogenic disorder without an infectious or toxic etiology**. Environmental and lifestyle factors act only as **modifiers/triggers**:

- **Hemodynamic stress / blood flow:** the principal physiological modifier; flow regulates *acvrl1* transcription and AVMs arise at sites of abnormal shear ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/), [PMID: 37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/)).
- **Pregnancy:** raises risk of hemorrhagic and cardiovascular complications ([PMID: 28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/)).
- **Angiogenic stimuli / injury / inflammation:** proposed "second hits" that focalize AVM development.
- **Infectious agents:** none cause HHT2. However, pulmonary AVMs create right-to-left shunts that predispose to **paradoxical septic embolization and brain abscess**, so infection is a downstream complication—HHT is overrepresented among cerebral-abscess patients ([PMID: 28578477](https://pubmed.ncbi.nlm.nih.gov/28578477/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline heterozygous loss-of-function mutation in *ACVRL1*** (often exon 7–8, kinase domain) **results in** reduced functional ALK1 receptor on endothelial cells (haploinsufficiency).
2. Reduced ALK1 **leads to** diminished high-affinity binding of circulating **BMP9/BMP10** and **decreased phosphorylation of SMAD1/5/8** (loss of downstream transcriptional output). *(Demonstrated in vitro and in patient endothelium.)*
3. Loss of ALK1–SMAD signaling **removes the anti-angiogenic brake**: ALK1–SMAD normally synergizes with **Notch** in stalk cells to induce **HEY1/HEY2**, repressing VEGF signaling, tip-cell formation, and sprouting. Its loss **de-represses VEGF-driven angiogenesis** ([PMID: 22421041](https://pubmed.ncbi.nlm.nih.gov/22421041/)). *(Demonstrated in mouse retina; rescued by BMP9.)*
4. In parallel, the **fluid-shear-stress (FSS) set point** that keeps vessels quiescent is **lowered**. Loss of SMAD4 (downstream node) **disinhibits flow-mediated KLF4–TIE2–PI3K/Akt signaling**, driving cell-cycle progression, excessive EC proliferation, and **loss of arterial identity** via KLF4 repression of CDKN2A/CDKN2B ([PMID: 37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/)). *(Demonstrated in *Smad4*-deletion models.)*
5. ALK1 loss **induces a KIT⁺ angiogenic endothelial-cell population** with tip-cell markers and **PI3K/KRAS activation**; **KIT is directly repressed by BMP9–ALK1–SMAD4**, so its de-repression drives AVM-like transcriptional reprogramming ([PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)). *(Demonstrated in inducible endothelial *Alk1*-knockout mice; KIT inhibition reduced malformations.)*
6. Excessive, mis-patterned angiogenesis with loss of arterial/venous identity **produces direct artery-to-vein connections** — **telangiectases** (small) and **AVMs** (large) lacking intervening capillaries.
7. These fragile, high-flow lesions **rupture and shunt**, **causing** epistaxis, GI bleeding, iron-deficiency anemia, and organ-specific sequelae (pulmonary shunt/hypoxemia/paradoxical embolism; hepatic AVM/high-output cardiac failure; cerebral/spinal AVM; PAH).

**Branch point:** Downstream of steps 3–5 the mechanism branches by **organ and hemodynamic context**, generating the HHT2-specific distribution (more hepatic AVM, GI bleeding, and PAH; fewer pulmonary/cerebral AVM than HHT1).

Supporting quotes:

> "ALK1-dependent SMAD signaling synergizes with activated Notch in stalk cells to induce expression of the Notch targets HEY1 and HEY2, thereby repressing VEGF signaling, tip cell formation, and endothelial sprouting." — [PMID: 22421041](https://pubmed.ncbi.nlm.nih.gov/22421041/)

> "loss of SMAD4 disinhibits flow-mediated KLF4-TIE2-PI3K/Akt signaling, leading to cell cycle progression-mediated loss of arterial identity due to KLF4-mediated repression of cyclin dependent Kinase (CDK) inhibitors CDKN2A and CDKN2B." — [PMID: 37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/)

> "This process is driven by the emergence of a KIT+ angiogenic EC population with human AVM-like transcriptional features, including tip-cell markers and activation of PI3K and KRAS signaling pathways… Kit is directly repressed by BMP9-ALK1-SMAD4 signaling." — [PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)

### Supporting detail

- **Molecular pathways:** BMP9/BMP10–ALK1–SMAD1/5/8 (canonical); cross-talk with **Notch–HEY1/HEY2**, **PI3K–AKT**, **KRAS/MAPK**, and **KLF4–TIE2** flow signaling. Suggested GO terms: BMP signaling pathway (GO:0030509), SMAD protein signal transduction (GO:0060395), angiogenesis (GO:0001525), regulation of sprouting angiogenesis (GO:1903670), endothelial cell proliferation (GO:0001935), arterial endothelial cell differentiation (GO:0060842), response to fluid shear stress (GO:0034405).
- **Cellular processes:** endothelial-cell proliferation, loss of arterial identity, altered tip/stalk-cell selection, and emergence of an aberrant arterial-lymphatic-like EC state that contributes to vascular leakage and AVMs ([PMID: 39429196](https://pubmed.ncbi.nlm.nih.gov/39429196/)).
- **Protein dysfunction:** loss of ALK1 kinase catalytic activity (D330, K229 ATP site) → failure to transphosphorylate R-SMADs; extracellular-domain variants impair BMP9/BMP10 binding.
- **Cell types (CL terms):** endothelial cell (CL:0000115), blood vessel endothelial cell (CL:0000071), arterial endothelial cell (CL:1000413); mural cells/pericytes contribute to vessel-wall fragility.
- **Immune / tissue-damage mechanisms:** the primary injury is hemorrhagic (mechanical rupture of fragile shunts) rather than autoimmune; chronic blood loss drives iron-deficiency anemia; pulmonary shunts enable septic paradoxical embolism.
- **Molecular profiling:** single-cell/transcriptomic work identifies discrete pathogenic EC states (KIT⁺ angiogenic ECs; arterial-lymphatic-like ECs) as tractable therapeutic nodes ([PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/), [PMID: 39429196](https://pubmed.ncbi.nlm.nih.gov/39429196/)).

```
ACVRL1 LOF (exon 7-8 kinase domain)
        │  haploinsufficiency
        ▼
 ↓ ALK1 receptor  ──►  ↓ BMP9/BMP10 binding  ──►  ↓ SMAD1/5/8-P
        │                                              │
        ▼                                              ▼
 ↓ Notch/HEY1-2 brake                 ↓ FSS set point (SMAD4)
   → de-repressed VEGF/sprouting        → KLF4-TIE2-PI3K/AKT, ↓CDKN2A/B
        │                                              │
        └──────────────►  KIT+ angiogenic EC state  ◄──┘
                          (PI3K/KRAS, tip-cell program)
                                   │
                                   ▼
              Excess/mis-patterned angiogenesis, loss of arterial identity
                                   │
                                   ▼
                  Telangiectases + AVMs (no capillary bed)
                                   │
                ┌──────────────┬───┴────────┬───────────────┐
             Epistaxis     Hepatic AVM   GI bleed / anemia   PAH
             (nasal)       (HHT2 ↑)      (HHT2 ↑)           (~20%)
```

---

## 7. Anatomical Structures Affected

**Organ level (primary):** nasal mucosa (epistaxis), skin/oral mucosa (telangiectases), **liver** (hepatic AVM—prominent in HHT2), **lungs** (pulmonary AVM), **brain** and **spinal cord** (cerebral/spinal AVM—spinal AVM seen only in HHT2), **gastrointestinal tract** (telangiectases, bleeding).
**Secondary/complication organs:** heart (high-output failure from hepatic shunting; PAH), brain (paradoxical embolic stroke, abscess), bone marrow/hematologic (iron-deficiency anemia).
**Body systems:** cardiovascular (primary), respiratory, digestive, nervous, integumentary.

**Suggested UBERON terms:** blood vessel (UBERON:0001981), endothelium of blood vessel (UBERON:0001982), nasal mucosa (UBERON:0001825), liver (UBERON:0002107), lung (UBERON:0002048), brain (UBERON:0000955), spinal cord (UBERON:0002240), gastrointestinal tract (UBERON:0001555), skin (UBERON:0002097).

**Tissue and cell level:** vascular endothelium (primary), with mural cell/pericyte and smooth-muscle involvement in vessel-wall remodeling. **CL terms:** endothelial cell (CL:0000115), blood vessel endothelial cell (CL:0000071), arterial endothelial cell (CL:1000413), pericyte (CL:0000669).

**Subcellular level (GO Cellular Component):** plasma membrane receptor complex (GO:0098802), integral component of plasma membrane (GO:0005887); intracellular signaling occurs in the cytoplasm/nucleus (SMAD nuclear translocation, GO:0005634).

**Localization / lateralization:** telangiectases are **multifocal and bilateral**; AVMs are typically focal and can be unilateral (e.g., a single dominant PAVM) or multiple/bilateral.

---

## 8. Temporal Development

**Onset.** Insidious and age-dependent. In HHT2, **epistaxis begins later** than in HHT1 and is incompletely penetrant ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)). Telangiectases and visceral lesions accumulate with age; hepatic involvement is largely **silent in childhood** (detectable by imaging in ~35% of HHT2 children but clinically silent) and becomes symptomatic in adults ([PMID: 28248153](https://pubmed.ncbi.nlm.nih.gov/28248153/)). PAH can rarely present in infancy ([PMID: 42516693](https://pubmed.ncbi.nlm.nih.gov/42516693/)).

**Progression.** Chronic, lifelong, and **progressive** with **episodic** bleeding. Epistaxis severity increases with age (age is the only consistent ESS predictor) ([PMID: 42419030](https://pubmed.ncbi.nlm.nih.gov/42419030/)). No formal disease "stages" exist; burden is quantified by lesion number/size and ESS.

**Patterns / critical periods.** Bleeding is **relapsing/episodic**; spontaneous remission of established lesions is uncommon, but antiangiogenic therapy induces telangiectasia regression. **Pregnancy** is a critical window of heightened risk ([PMID: 28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/)); childhood is a window for presymptomatic screening and prophylactic PAVM management.

---

## 9. Inheritance and Population

**Epidemiology.** Combined HHT clinical prevalence ~**1 in 5,000** (range 1:5,000–10,000). Genetic prevalence is likely higher: **1.75–2.56 per 5,000** (pathogenic/likely-pathogenic *ENG*+*ACVRL1*), up to 2.87–4.33 per 5,000 including potentially pathogenic variants, indicating underdiagnosis ([PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)). Regional studies: Argentina HMO 3.2/10,000 ([PMID: 38683506](https://pubmed.ncbi.nlm.nih.gov/38683506/)); Alberta 1 in 3,800 with a **3.25:1 female preponderance** and elevated stroke incidence (450 vs 260/100,000; rate ratio 1.73, 95% CI 1.05–2.84) ([PMID: 30520389](https://pubmed.ncbi.nlm.nih.gov/30520389/)).

> "The genetic prevalence of HHT ranged from 1.753 to 2.555 in 5000 individuals, when considering only pathogenic and likely pathogenic variants, and from 2.874 to 4.327 in 5000 individuals, when also potentially pathogenic variants were considered." — [PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)

**Inheritance and genetic parameters.**
- **Pattern:** autosomal dominant.
- **Penetrance:** age-dependent and high but incomplete—epistaxis penetrance in HHT2 is notably lower/later than HHT1 ([PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)).
- **Expressivity:** highly variable, even within families.
- **Genetic anticipation:** not a feature (not a repeat-expansion disorder).
- **De novo / mosaicism:** rare; ~90% present with detectable heterozygous variant and nearly all have a family history; mosaicism (≤25% allele fraction) requires high-depth NGS ([PMID: 29243366](https://pubmed.ncbi.nlm.nih.gov/29243366/), [PMID: 21415079](https://pubmed.ncbi.nlm.nih.gov/21415079/)).
- **Founder effects/consanguinity:** *ACVRL1* mutations are highly allelic and family-specific; consanguinity is not relevant to a dominant disorder.

**Population demographics.** Occurs worldwide across ethnicities; specific regional founder mutations exist for HHT generally. Diagnosed cases show a **female predominance** (~3:1 in some registries), and inpatients have elevated anemia, congestive heart failure, liver disease, and cerebrovascular malformations (OR 11.04) ([PMID: 33779866](https://pubmed.ncbi.nlm.nih.gov/33779866/), [PMID: 30520389](https://pubmed.ncbi.nlm.nih.gov/30520389/)).

---

## 10. Diagnostics

**Clinical criteria — Curaçao criteria (4):** (1) spontaneous recurrent **epistaxis**; (2) mucocutaneous **telangiectases** at characteristic sites; (3) **visceral AVM** (pulmonary, hepatic, cerebral, spinal, GI); (4) **first-degree relative** with HHT. **≥3 = definite; 2 = possible/suspected; <2 = unlikely.** In children the criteria have low early sensitivity (only 41% met ≥3 at median 8.4 y; 63% over follow-up), so **genetic testing is important pediatrically** ([PMID: 37572862](https://pubmed.ncbi.nlm.nih.gov/37572862/)).

> "In children <6 years at presentation, only 23% fulfilled at least 3 criteria initially." — [PMID: 37572862](https://pubmed.ncbi.nlm.nih.gov/37572862/)

**Genetic testing.** Molecular confirmation by ***ACVRL1* sequencing plus deletion/duplication analysis**, typically via an **HHT gene panel** (*ENG*, *ACVRL1*, *SMAD4*, *GDF2*/BMP9). Single-gene testing is appropriate when a familial variant is known (cascade testing). WES/WGS are useful for atypical/negative cases. High-depth NGS is needed to detect **mosaicism** missed by Sanger ([PMID: 29243366](https://pubmed.ncbi.nlm.nih.gov/29243366/)).

**Imaging / functional screening:**
- **Pulmonary AVM:** contrast (agitated-saline) **transthoracic echocardiography** to detect right-to-left shunt, followed by **chest CT** ([PMID: 37132738](https://pubmed.ncbi.nlm.nih.gov/37132738/)).
- **Cerebral/spinal AVM:** **MRI**.
- **Hepatic AVM:** **Doppler ultrasound** / CT / MRA (common-hepatic-artery dilation is an early HHT2 sign) ([PMID: 28248153](https://pubmed.ncbi.nlm.nih.gov/28248153/)).
- **GI bleeding:** endoscopy.

**Laboratory:** CBC/iron studies for chronic blood-loss anemia (HP:0001891). No single circulating biomarker is diagnostic; ESS and NOSE-HHT are validated **severity** instruments.

**Differential diagnosis:** *GDF2*/BMP9-related vascular-anomaly syndrome (phenotypic overlap; ~15% of clinically suspected HHT lack *ENG*/*ACVRL1*/*SMAD4* mutations) ([PMID: 23972370](https://pubmed.ncbi.nlm.nih.gov/23972370/)); RASA1-related capillary malformation–AVM syndrome; CREST/systemic sclerosis; isolated PAVM; other causes of GI angiodysplasia.

**Screening/cascade testing:** once a familial *ACVRL1* variant is identified, **cascade genetic screening** of at-risk relatives enables presymptomatic surveillance and prophylactic PAVM embolization.

---

## 11. Outcome / Prognosis

**Survival/mortality.** Life expectancy is near-normal with modern surveillance and treatment, but HHT carries excess morbidity and preventable mortality from hemorrhage, high-output cardiac failure (hepatic AVM), stroke, and brain abscess (paradoxical embolism through PAVM). HHT patients have elevated **stroke** incidence (rate ratio 1.73) ([PMID: 30520389](https://pubmed.ncbi.nlm.nih.gov/30520389/)) and higher inpatient rates of congestive heart failure, liver disease, and cerebrovascular malformations ([PMID: 33779866](https://pubmed.ncbi.nlm.nih.gov/33779866/)).

**Morbidity/function.** Chronic epistaxis, iron-deficiency anemia (frequently transfusion-dependent), and fatigue drive disability and reduced QoL; abnormal cerebral MRI findings can independently worsen depressive symptoms (BDI-II β=9.69, p=0.003) ([PMID: 41950724](https://pubmed.ncbi.nlm.nih.gov/41950724/)).

**Complications:** paradoxical embolic stroke and **brain abscess** (PAVM), high-output heart failure and portal hypertension (hepatic AVM), PAH (~20% of *ACVRL1* carriers), hemorrhage (GI, pulmonary, intracranial), pregnancy-related events.

**Prognostic factors.** Higher baseline ESS, older age, extent of visceral AVM involvement, and PAH worsen prognosis. Presymptomatic **PAVM embolization** improves quality-adjusted survival (decision analysis favored immediate embolotherapy for feeding arteries ≥3 mm: 37.2 vs 32.6 QALYs) ([PMID: 19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/)). Genotype is prognostic for organ distribution (HHT2 → hepatic/GI/PAH) and hints at differential drug response.

---

## 12. Treatment

Management follows the **Second International HHT Guidelines** (2020; AGREE II/GRADE methodology, 15 countries) covering epistaxis, GI bleeding, anemia, pediatric care, pregnancy, and pulmonary/hepatic/cerebral VM management ([PMID: 32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/)).

> "The goal of the Second International HHT Guidelines process was to develop evidence-based consensus guidelines for the management and prevention of HHT-related symptoms and complications." — [PMID: 32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/)

**Local / interventional:**
- **Epistaxis:** humidification, topical therapies, laser/ablative treatment, septodermoplasty; nasal closure in refractory cases.
- **Pulmonary AVM:** **transcatheter embolization** (coils/plugs); presymptomatic embolization recommended for feeding arteries ≥3 mm ([PMID: 19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/)); antibiotic prophylaxis before procedures to prevent brain abscess ([PMID: 37132738](https://pubmed.ncbi.nlm.nih.gov/37132738/)).
- **Hepatic AVM:** medical management first; liver transplantation for refractory high-output failure.

**Systemic antiangiogenic pharmacotherapy** (NCIT: antiangiogenesis agents). Three established agents target VEGF-driven angiogenesis and vessel maturation:

> "Intravenous bevacizumab, oral pazopanib, and oral thalidomide are the three targeted primary angiogenesis inhibitors, with multiple studies describing both reassuring safety and impressive effectiveness in the treatment of moderate-to-severe HHT-associated bleeding." — [PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/)

| Drug | Class / target | NCIT (suggested) | Evidence |
|---|---|---|---|
| **Bevacizumab** | Anti-VEGF monoclonal antibody | NCIT:C2039 | Reduces epistaxis/GI bleeding and high-output cardiac failure ([PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/)) |
| **Pazopanib** | Multikinase (VEGFR) inhibitor | NCIT:C45386 | Reduces bleeding ([PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/)) |
| **Thalidomide** | Antiangiogenic / vessel maturation | NCIT:C716 | Bolsters vessel maturation, reduces bleeding ([PMID: 28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/)) |
| **Pomalidomide** | Immunomodulatory antiangiogenic | NCIT:C79809 | **RCT-proven** (see below) |

**Pomalidomide — level-1 evidence (PATH-HHT, NCT03910244).** Randomized placebo-controlled trial, 144 patients (95 pomalidomide 4 mg/day, 49 placebo, 24 weeks): mean difference in ESS change vs placebo **−0.94 points (95% CI −1.57 to −0.31)**, exceeding the 0.71-point clinically meaningful threshold; the trial was **stopped early for efficacy** ([PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)).

> "At 24 weeks, the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was -0.94 points (95% confidence interval [CI], -1.57 to -0.31;" — [PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)

The ATLAS extension (n=62, up to 4.4 y) confirmed durable ESS improvement (5.55→2.80, P<0.0001) and reduced hematologic support (9.11→5.73 red-cell/iron units, P=0.0056), though it was less effective for GI bleeding ([PMID: 41512167](https://pubmed.ncbi.nlm.nih.gov/41512167/)).

> "Significant, durable improvements in mean epistaxis severity score (5.55 points [baseline] to 2.80 points [month 12]; P< .0001)" — [PMID: 41512167](https://pubmed.ncbi.nlm.nih.gov/41512167/)

**Pharmacogenomics / genotype-guided therapy.** In a PATH-HHT response analysis, a **less robust pomalidomide response** was associated with older age (per 10 y, P=0.02) and **underlying *ACVRL1* (HHT2) germline mutation** (+0.62 ESS [95% CI −0.04 to 1.27] vs *ENG*/*SMAD4*/unknown, P=0.06), the first genotype signal for treatment stratification in HHT ([PMID: 41719457](https://pubmed.ncbi.nlm.nih.gov/41719457/)).

> "Characteristics associated with a less robust response were older age (0.29 [95% CI, 0.05-0.53] per 10 years older, P = .02) and underlying ACVRL1 germ line mutation (0.62 [95% CI, -0.04 to 1.27] vs ENG, SMAD4, or mutation not known, P = .06]" — [PMID: 41719457](https://pubmed.ncbi.nlm.nih.gov/41719457/)

**Supportive care:** oral/IV **iron replacement** and transfusion for anemia; antifibrinolytics (tranexamic acid) as adjuncts; antibiotic prophylaxis for PAVM.

**Emerging targeted approaches (preclinical):** **KIT inhibition** (KIT⁺ angiogenic ECs), ALK1-activating therapeutics, and pathway modulators (PI3K/AKT) are under investigation ([PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/), [PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)).

---

## 13. Prevention

**Primary prevention** of the genetic disease is not possible, but reproductive options (genetic counseling, **preimplantation genetic testing**, prenatal diagnosis) can prevent transmission.

**Secondary prevention (early detection):** **cascade genetic testing** of first-degree relatives once a familial *ACVRL1* variant is identified, followed by organ screening—contrast echocardiography/chest CT for PAVM, MRI for cerebral AVM, Doppler/CT for hepatic AVM. Presymptomatic **PAVM embolization** prevents stroke and brain abscess ([PMID: 19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/)).

**Tertiary prevention:** **antibiotic prophylaxis** before dental/surgical procedures in patients with PAVM to prevent brain abscess ([PMID: 37132738](https://pubmed.ncbi.nlm.nih.gov/37132738/)); avoidance of anticoagulation where feasible; iron-status monitoring; high-risk pregnancy management ([PMID: 28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/)); mental-health support given the psychological impact of screening ([PMID: 41950724](https://pubmed.ncbi.nlm.nih.gov/41950724/)).

**Counseling.** Genetic counseling is central: 50% offspring risk, variable expressivity, importance of cascade screening, and reproductive options. **Immunization/public-health/environmental** interventions are not applicable to this Mendelian disorder.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** *ACVRL1* is conserved across vertebrates: human *ACVRL1* (NCBI Gene 94); mouse *Acvrl1* (NCBI Gene 11482; NCBI Taxon 10090); zebrafish *acvrl1* (NCBI Taxon 7955). ALK1 signaling and its flow/BMP dependence are evolutionarily conserved—zebrafish and mouse recapitulate core AVM biology ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)).

**Natural disease in other species.** No well-characterized naturally occurring HHT2 analog is established in companion animals or wildlife (no prominent OMIA entry). HHT is essentially a human Mendelian disorder; animal involvement is via **engineered models** (Section 15) rather than spontaneous disease.

**Comparative biology.** The **conservation of the BMP9/BMP10–ALK1–SMAD pathway** and its flow-coupling across zebrafish and mice underpins the translational value of these models. **Zoonotic/cross-species transmission:** not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

**Mouse (Mus musculus, NCBI Taxon 10090).** The workhorse model. **Inducible endothelial-specific *Alk1* (Acvrl1) knockouts** develop AVMs and reveal the KIT⁺ angiogenic EC mechanism; KIT inhibition rescued malformations ([PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)). *Acvrl1*-null and *Eng*-null mice develop AVMs preventable by *Acvrl1* overexpression ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)). Endothelial *Alk1* deletion also produces aberrant arterial-lymphatic-like ECs driving leakage/AVMs ([PMID: 39429196](https://pubmed.ncbi.nlm.nih.gov/39429196/)); *Smad4*-deletion models define the FSS-set-point mechanism ([PMID: 37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/)). Available genetic tools: conditional/floxed alleles, endothelial Cre drivers, and neonatal-retina AVM assays.

**Zebrafish (Danio rerio, NCBI Taxon 7955).** *acvrl1* mutants and *acvrl1:egfp* reporters demonstrate blood-flow- and Bmp10-dependent *acvrl1* transcription and cranial AVM formation—ideal for studying flow–ligand coupling ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)). A *bmp9*-deficient zebrafish model supported the angiogenic role of BMP9 ([PMID: 23972370](https://pubmed.ncbi.nlm.nih.gov/23972370/)).

**Cellular / iPSC models.** A **CRISPR-engineered isogenic hiPSC line carrying heterozygous *ACVRL1* c.143G>A (p.Gly48Glu)** provides a human in-vitro platform for HHT2 disease modeling and drug testing; the line retained normal karyotype, pluripotency, and trilineage differentiation ([PMID: 41905104](https://pubmed.ncbi.nlm.nih.gov/41905104/)). Human endothelial cells under defined shear stress reproduce flow-dependent ALK1 regulation ([PMID: 38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/)).

**Phenotype recapitulation and limitations.** Models faithfully reproduce **AVM formation, flow-dependence, and the angiogenic EC reprogramming** central to HHT. Limitations: they may not capture the **stochastic, focal, late-onset** nature of human lesions on a heterozygous background, the full organ-distribution differences of HHT2 vs HHT1, or long-term hemorrhagic morbidity; complete knockouts are embryonic-lethal, requiring conditional/inducible strategies.

**Resources:** MGI (mouse *Acvrl1*), ZFIN (zebrafish *acvrl1*), IMPC/IMSR, Cellosaurus/hiPSC repositories.

---

## Mechanistic Model / Interpretation

HHT2 is best understood as a disease of **lost endothelial angiogenic restraint**. In healthy vessels, circulating BMP9/BMP10 engage ALK1 (with endoglin) on endothelial cells and, together with physiological shear stress, activate SMAD1/5/8 to hold vessels in a quiescent, arterialized state—partly by cooperating with Notch to induce HEY1/HEY2 and repress VEGF-driven sprouting, and partly by maintaining a high fluid-shear-stress "set point" that limits proliferation. A single loss-of-function *ACVRL1* allele halves this signal. The consequences converge on **de-repressed, mis-patterned angiogenesis**: VEGF/tip-cell programs are unleashed, PI3K–AKT and KRAS pathways activate, a pathological **KIT⁺ angiogenic endothelial state** emerges, and arterial identity is lost through KLF4-mediated repression of cell-cycle inhibitors. The end result is direct artery-to-vein shunts without capillaries—telangiectases and AVMs—that are fragile and bleed.

The **HHT2-specific clinical fingerprint** (later/less-penetrant epistaxis; fewer pulmonary/cerebral AVMs; more hepatic AVMs, GI bleeding, and PAH) reflects how this common upstream lesion plays out differently across organ-specific hemodynamic and molecular contexts. This model has therapeutic corollaries realized in the clinic: **anti-VEGF and immunomodulatory antiangiogenics** (bevacizumab, pazopanib, thalidomide, pomalidomide) counteract the de-repressed angiogenesis, while emerging strategies aim upstream (ALK1-activating agents; enhancing *ACVRL1* expression) or at newly identified downstream nodes (**KIT inhibition**).

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [33513792](https://pubmed.ncbi.nlm.nih.gov/33513792/) | Defines LOF mechanism and BMP9/BMP10–ALK1–SMAD1/5/8 signaling |
| [16470787](https://pubmed.ncbi.nlm.nih.gov/16470787/) | *ACVRL1* mutation clustering (exons 7–8); organ-specific AVM distribution |
| [17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/) | French–Italian genotype–phenotype cohort; HHT2 quantitative differences |
| [42516693](https://pubmed.ncbi.nlm.nih.gov/42516693/) | ACVRL1–PAH association (~20%) |
| [41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/) | Genomic-database genetic prevalence; underdiagnosis |
| [30520389](https://pubmed.ncbi.nlm.nih.gov/30520389/) | Population prevalence, female preponderance, elevated stroke risk |
| [33779866](https://pubmed.ncbi.nlm.nih.gov/33779866/) | Cerebrovascular/cardiovascular comorbidity burden (NIS) |
| [37490341](https://pubmed.ncbi.nlm.nih.gov/37490341/) | SMAD4/FSS set point; KLF4–TIE2–PI3K/Akt; loss of arterial identity |
| [22421041](https://pubmed.ncbi.nlm.nih.gov/22421041/) | ALK1–Notch/HEY anti-angiogenic mechanism |
| [42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/) | KIT⁺ angiogenic EC state; PI3K/KRAS; KIT as therapeutic target |
| [38727966](https://pubmed.ncbi.nlm.nih.gov/38727966/) | Flow- and Bmp10-dependent *acvrl1* transcription |
| [39429196](https://pubmed.ncbi.nlm.nih.gov/39429196/) | Arterial-lymphatic-like ECs contributing to leakage/AVM |
| [32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/) | Second International HHT Guidelines |
| [35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/) | Antiangiogenic therapies (bevacizumab, pazopanib, thalidomide) |
| [39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/) | PATH-HHT pomalidomide RCT (primary efficacy) |
| [41512167](https://pubmed.ncbi.nlm.nih.gov/41512167/) | ATLAS long-term pomalidomide durability |
| [41719457](https://pubmed.ncbi.nlm.nih.gov/41719457/) | ACVRL1/HHT2 trend toward weaker pomalidomide response |
| [37572862](https://pubmed.ncbi.nlm.nih.gov/37572862/) | Low Curaçao sensitivity in children |
| [40055726](https://pubmed.ncbi.nlm.nih.gov/40055726/) | International QoL burden (epistaxis, fatigue) |
| [42419030](https://pubmed.ncbi.nlm.nih.gov/42419030/) | Danish ESS–QoL correlation; no difference by HHT type |
| [34857410](https://pubmed.ncbi.nlm.nih.gov/34857410/) | Visceral AVMs reduce physical QoL |
| [41950724](https://pubmed.ncbi.nlm.nih.gov/41950724/) | Psychological impact of cerebral MRI screening |
| [21415079](https://pubmed.ncbi.nlm.nih.gov/21415079/) / [29243366](https://pubmed.ncbi.nlm.nih.gov/29243366/) | Mosaicism detection |
| [23972370](https://pubmed.ncbi.nlm.nih.gov/23972370/) | BMP9/GDF2 differential diagnosis |
| [19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/) | PAVM embolization decision analysis |
| [41905104](https://pubmed.ncbi.nlm.nih.gov/41905104/) | hiPSC HHT2 model (p.Gly48Glu) |
| [28248153](https://pubmed.ncbi.nlm.nih.gov/28248153/) | Pediatric hepatic involvement in HHT2 |
| [28578477](https://pubmed.ncbi.nlm.nih.gov/28578477/) | HHT overrepresentation in cerebral abscess |
| [28603431](https://pubmed.ncbi.nlm.nih.gov/28603431/) | Pregnancy risk and therapeutics |
| [37132738](https://pubmed.ncbi.nlm.nih.gov/37132738/) | PAVM update; screening and antibiotic prophylaxis |
| [16155196](https://pubmed.ncbi.nlm.nih.gov/16155196/) | Genotype–phenotype: HAVM more frequent in HHT2, distinct milder phenotype |
| [36504622](https://pubmed.ncbi.nlm.nih.gov/36504622/) | Brain AVM cellular/molecular mechanisms review |
| [37695357](https://pubmed.ncbi.nlm.nih.gov/37695357/) | 14th HHT conference; disease overview and incidence ~1:5000 |

---

## Limitations and Knowledge Gaps

- **HHT2-specific data are limited.** Much mechanistic evidence derives from pan-HHT or *Eng*/*Smad4* models; direct *Acvrl1*-heterozygous studies and HHT2-only clinical trials are fewer.
- **Modifier genes** driving the striking variable expressivity of HHT2 are largely unidentified; the "second hit" hypothesis is plausible but incompletely proven in human tissue.
- **Pomalidomide genotype effect** for *ACVRL1* is a **trend (P=0.06)**, not a definitive result, and requires prospective, genotype-stratified confirmation.
- **Penetrance and prevalence** estimates are complicated by underdiagnosis; genetic-prevalence figures assume variant pathogenicity that may be imperfect.
- **No naturally occurring animal disease** and no HHT2 newborn-screening program exist; diagnosis remains clinical/genetic and often delayed.
- **Epigenetic contributions** to HHT2 are essentially unstudied.

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified antiangiogenic trials** — prospectively test whether *ACVRL1*/HHT2 patients respond less to pomalidomide/thalidomide and better to alternative agents (e.g., anti-VEGF or upstream ALK1 activators), converting the PATH-HHT signal into actionable precision medicine.
2. **KIT-directed therapy translation** — evaluate KIT inhibitors (or KIT-pathway modulators) in *Acvrl1*-mutant models and early-phase human studies, building on the KIT⁺ angiogenic EC discovery.
3. **ALK1-enhancing strategies** — test ligand supplementation (BMP9/BMP10 mimetics) and approaches that raise residual *ACVRL1* expression, exploiting the flow-dependent positive-feedback loop.
4. **HHT2 single-cell/spatial atlas** — define organ-specific endothelial states (hepatic vs pulmonary vs nasal) to explain the HHT2 clinical fingerprint and identify organ-tailored targets.
5. **Modifier-gene GWAS/exome analysis** within large HHT2 registries to explain variable expressivity and identify protective alleles.
6. **Pediatric genetic-diagnosis pathways** — formalize early molecular testing given low childhood Curaçao sensitivity, coupled with structured mental-health support for screening-detected findings.

---

*Report compiled from 9 confirmed findings and 35 reviewed papers across 5 investigation iterations. Evidence types: predominantly human clinical/cohort and model-organism (mouse, zebrafish, hiPSC), with computational database verification of identifiers.*


## Artifacts

- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_Type_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_Type_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 35 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42579368` *(abstract only)*: "This process is driven by the emergence of a KIT+ angiogenic EC population with human AVM-like transcriptional features, including tip-cell markers and activation of PI3K and KRAS signaling pathways… Kit is directly repressed by BMP9-ALK1-SMAD4 signaling."
  - closest text in source: "This process is driven by the emergence of a KIT+ angiogenic EC population with human AVM-like transcriptional features, including tip-cell markers and activation of PI3K and KRAS signaling pathways"
- `PMID:39292928`: "At 24 weeks, the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was -0.94 points (95% confidence interval [CI], -1.57 to -0.31;"
  - closest text in source: "At 24 weeks, the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was -0.94 points (95% confidence interval [CI], -1.57 to -0.31;"
- `PMID:41512167` *(abstract only)*: "Significant, durable improvements in mean epistaxis severity score (5.55 points [baseline] to 2.80 points [month 12]; P< .0001)"
  - closest text in source: "Significant, durable improvements in mean epistaxis severity score (5.55 points [baseline] to 2.80 points [month 12]; P< .0001)"
- `PMID:41719457` *(abstract only)*: "Characteristics associated with a less robust response were older age (0.29 [95% CI, 0.05-0.53] per 10 years older, P = .02) and underlying ACVRL1 germ line mutation (0.62 [95% CI, -0.04 to 1.27] vs ENG, SMAD4, or mutation not known, P = .06]"
  - closest text in source: "Characteristics associated with a less robust response were older age (0.29 [95% CI, 0.05-0.53] per 10 years older, P = .02) and underlying ACVRL1 germ line mutation (0.62 [95% CI, -0.04 to 1.27] vs ENG, SMAD4, or mutation not known, P = .06]"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002110` (1 mention) - the report calls it "pulmonary AVM"; HP calls it **Bronchiectasis**
- `HP:0002408` (1 mention) - the report calls it "CNS AVM"; HP calls it **Cerebral arteriovenous malformation**
- `HP:0002435` (1 mention) - the report calls it "Clinical sign"; HP calls it **Meningocele**
- `HP:0002092` (1 mention) - the report calls it "PAH"; HP calls it **Pulmonary arterial hypertension**
- `HP:0001891` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Iron deficiency anemia**
- `HP:0012378` (1 mention) - the report calls it "Symptom"; HP calls it **Fatigue**
- `NCIT:C45386` (1 mention) - the report calls it "Multikinase (VEGFR) inhibitor"; NCIT calls it **Carcinogenic Chlorinated Hydrocarbon**
- `NCIT:C716` (1 mention) - the report calls it "Antiangiogenic / vessel maturation"; NCIT calls it **Omeprazole**
- `NCIT:C79809` (1 mention) - the report calls it "Immunomodulatory antiangiogenic"; NCIT calls it **Defactinib**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000562` (1 mention), reported as "telangiectasia of the skin" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005887` (GO_0005887) (1 mention) - replaced by `GO:0005886`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100761` (1 mention) - the report calls it "visceral AVM"; HP calls it **Visceral angiomatosis**
- `NCIT:C2039` (1 mention) - the report calls it "Anti-VEGF monoclonal antibody"; NCIT calls it **Bevacizumab**, and lists "Anti-VEGF Monoclonal Antibody SIBP04" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:774` - called "parent HHT", "HHT, parent"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
