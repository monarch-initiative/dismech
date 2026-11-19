---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T07:18:31.594454'
end_time: '2026-11-11T07:33:48.151962'
duration_seconds: 916.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Jaberi-Elahi Syndrome
  mondo_id: MONDO:0060711
  category: Mendelian
  causal_genes: GTPBP2
  omim_id: OMIM:617988
  synonyms: JABELS
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Jaberi-Elahi_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Jaberi-Elahi_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jaberi-Elahi Syndrome
- **MONDO ID:** MONDO:0060711 (if available)
- **Causal gene(s):** GTPBP2
- **OMIM:** OMIM:617988
- **Synonyms:** JABELS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Jaberi-Elahi Syndrome** covering all of the
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

# Jaberi-Elahi Syndrome (JABELS): A Comprehensive Disease Characterization

**Disease:** Jaberi-Elahi Syndrome (JABELS)
**Causal gene:** **GTPBP2** (GTP-binding protein 2; HGNC, chromosome 6p21.1; UniProt Q9BX10)
**Identifiers:** OMIM #617988 · MONDO:0060711 · Category: Mendelian, autosomal recessive

---

## Summary

**Jaberi-Elahi syndrome is an ultra-rare autosomal-recessive neurodevelopmental and neurodegenerative disorder caused by biallelic loss-of-function variants in the gene GTPBP2.** GTPBP2 encodes a 602-amino-acid translational (tr-type) GTPase that partners with PELO (Pelota) to rescue stalled ribosomes as part of the ribosome-associated quality-control / no-go decay machinery. The disorder was first delineated in 2016 in a consanguineous Iranian family (Jaberi, Elahi, and colleagues) in which three affected siblings presented with neurodegeneration accompanied by brain iron accumulation, and it has since been confirmed and broadened by multiple independent families worldwide. Fewer than ~30 patients had been reported in the literature as of 2024, making this one of the rarest Mendelian neurodevelopmental disorders characterized to date.

The clinical picture is dominated by early motor developmental delay (≈93% of patients), sparse hair (≈93%), speech disorder (≈86%), intellectual disability (≈82%), hypotonia (≈82%), skeletal anomalies (≈82%), and visual/retinal impairment (≈64%), with additional features including microcephaly (which may be severe and congenital), progressive spasticity, choreoathetoid movements, refractory epilepsy, facial dysmorphism, cerebral/cerebellar atrophy, and—in a subset of families—agenesis of the corpus callosum and brain iron accumulation. Expressivity is notably variable and some features (ectodermal/iron abnormalities) are non-obligate and appear family-specific.

The mechanistic basis is well-supported by mouse and invertebrate models. GTPBP2 loss causes codon-specific ribosome stalling (demonstrated at AGA/Arg codons when a CNS-specific tRNA is also limiting), which triggers the GCN2–eIF2α–ATF4 integrated stress response (ISR). Paradoxically, this ISR is neuroprotective and *attenuates* rather than drives the neurodegeneration, implying that unresolved stalling and downstream proteostatic collapse are the primary injurious events. The closely related paralog GTPBP1 produces an essentially identical syndrome and acts non-redundantly in the same pathway. There is no disease-specific therapy; management is entirely supportive, and diagnosis rests on exome/genome sequencing demonstrating biallelic GTPBP2 variants.

---

## Key Findings

### Finding 1 — JABELS is an autosomal-recessive neurodevelopmental/neurodegenerative disorder caused by biallelic GTPBP2 loss-of-function (F001)

The disorder was first reported by Jaberi et al. (2016) in a consanguineous Iranian family with three affected siblings. Using linkage analysis plus exome sequencing, they identified a homozygous splice-site mutation in **GTPBP2** that deletes exon 9 and produces a truncated protein lacking conserved C-terminal domains. The authors state: *"A splice site mutation in GTPBP2 that encodes GTP-binding protein 2 was identified in the patients and considered possible cause of their disease"* and note that *"Iron accumulation in the brain of the patients was a notable phenotypic feature"* ([PMID: 26675814](https://pubmed.ncbi.nlm.nih.gov/26675814/)).

Independent confirmation came from Bertoli-Avella et al. (2018), who reported three unrelated families with homozygous nonsense variants—**c.430C>T p.(Arg144\*)**, **c.1219C>T p.(Gln407\*)**, and **c.1408C>T p.(Arg470\*)**—establishing pathogenicity beyond the index family: *"whole-exome sequencing identified the homozygous non-sense variants c.430[C>T];[C>T] p.(Arg144\*), c.1219[C>T];[C>T] p.(Gln407\*) and c.1408[C>T];[C>T] p.(Arg470\*) in GTPBP2"* ([PMID: 29449720](https://pubmed.ncbi.nlm.nih.gov/29449720/)). Together these establish a recessive loss-of-function mechanism. **Identifiers:** OMIM #617988; MONDO:0060711; gene GTPBP2 (6p21.1); synonym JABELS.

### Finding 2 — Core phenotype spectrum and frequencies (28-patient review) (F002)

The most comprehensive phenotype tabulation comes from Manoochehri et al. (2024), who reviewed 28 reported individuals. The dominant features and their frequencies are summarized below:

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Motor developmental delay | 26/28 (93%) | HP:0001270 Motor delay |
| Sparse hair | 26/28 (93%) | HP:0008070 Sparse hair |
| Speech disorder | 24/28 (86%) | HP:0000750 Delayed speech / HP:0002167 Speech articulation difficulties |
| Intellectual disability | 23/28 (82%) | HP:0001249 Intellectual disability |
| Hypotonia | 23/28 (82%) | HP:0001252 Hypotonia |
| Skeletal problems | 23/28 (82%) | HP:0000924 Abnormality of the skeletal system |
| Visual impairment | 18/28 (64%) | HP:0000505 Visual impairment |

Additional reported features include abnormal reflexes, facial dysmorphism, poor growth, microcephaly (HP:0000252), progressive spasticity (HP:0002061), choreoathetoid movements (HP:0001266), refractory epilepsy (HP:0001250 Seizure), brain atrophy (HP:0012444), agenesis of the corpus callosum (HP:0001274), and variable brain iron accumulation (HP:0011392 Abnormal cerebral iron deposition). The authors summarize: *"A large numbers of patients manifest motor development delay (26/28), sparse hair (26/28), and speech disorder (24/28). Moreover, a significant fraction of patients suffer from intellectual disability (23/28), hypotonia (23/28), skeletal problems (23/28), and visual impairment (18/28)"* ([PMID: 38852771](https://pubmed.ncbi.nlm.nih.gov/38852771/)).

### Finding 3 — Mechanism: GTPBP2 is a ribosome-rescue factor; its loss causes codon-specific ribosome stalling and neurodegeneration (F003)

The pivotal mechanistic work came from Ishimura et al. (2014), who showed in mice that **loss of GTPBP2—a binding partner of the ribosome-recycling protein Pelota—combined with mutation of a CNS-specific tRNA gene (n-Tr20) causes ribosome stalling and widespread neurodegeneration**: *"loss of GTPBP2, a novel binding partner of the ribosome recycling protein Pelota, in mice with a mutation in a tRNA gene that is specifically expressed in the central nervous system causes ribosome stalling and widespread neurodegeneration"* ([PMID: 25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/)).

This paradigm was reinforced by Terrey et al. (2020) studying the paralog GTPBP1: *"Loss of a tRNA gene leads to ribosomal pausing that is resolved by the translational GTPase GTPBP2, and in its absence causes neuron death"* ([PMID: 33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/)), indicating that GTPBP1 and GTPBP2 act non-redundantly in the same ribosome-rescue pathway. Salpietro et al. (2024) added that human disease variants are loss-of-function with ribosome-profiling abnormalities, and that *Drosophila* knockdown of the ortholog CG2017 recapitulates the defects ([PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)).

**GO terms:** GO:0072344 rescue of stalled ribosome; GO:0006412 translation; GO:0003924 GTPase activity. **CL terms:** CL:0000540 neuron; CL:0000210 photoreceptor cell (retinal degeneration).

### Finding 4 — GTPBP1 and GTPBP2 produce an identical syndrome; both are translational GTPases related to eEF1A/eRF3/Hbs1 (F004)

Salpietro et al. (2024) described 20 individuals from 16 families with biallelic GTPBP1 **or** GTPBP2 variants sharing *"microcephaly, profound neurodevelopmental impairment, pathognomonic craniofacial features, and ectodermal defects"*, together with abnormal vision/hearing, progressive spasticity, choreoathetoid movements, refractory epilepsy, and brain atrophy; all variants were loss-of-function ([PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)).

Zinoviev et al. (2018) classified these proteins biochemically: *"GTP-binding protein 1 (GTPBP1) and GTPBP2 comprise a divergent group of translational GTPases with obscure functions, which are most closely related to eEF1A, eRF3, and Hbs1"* ([PMID: 30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/)). GTPBP1 has eEF1A-like aminoacyl-tRNA delivery activity and stimulates exosomal mRNA degradation, implicating both paralogs in mRNA surveillance and ribosome-associated quality control (RQC).

### Finding 5 — Downstream mechanism: AGA-codon stalling activates the neuroprotective GCN2–eIF2α–ATF4 integrated stress response (F005)

Ishimura et al. (2016) dissected the downstream signaling in *Gtpbp2(nmf205)* mice: *"neuronal elongation complexes are stalled at AGA codons due to deficiencies in a tRNA(Arg)UCU tRNA and GTPBP2, a mammalian ribosome rescue factor. Increased levels of phosphorylation of eIF2α (Ser51) were detected prior to neurodegeneration"* ([PMID: 27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/)). Transcriptomics showed ATF4 activation—the hallmark of the integrated stress response (ISR). Critically, the authors found that *"this pathway was activated by the eIF2α kinase, GCN2, in an apparent deacylated tRNA-independent fashion. Further we found that the ISR attenuates neurodegeneration"* ([PMID: 27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/)).

This is a mechanistically important nuance: the ISR is a **protective, compensatory** response, not the proximate cause of neuron death. Neurodegeneration therefore reflects the failure/insufficiency of ribosome rescue and proteostasis, with the ISR buffering—but not preventing—the injury. **GO terms:** GO:0140469 GCN2-mediated ISR signaling; GO:0034198 cellular response to amino acid starvation.

### Finding 6 — Model organisms and epidemiology (F006)

**Mouse:** The *Gtpbp2(nmf205)* mouse on the B6J background (which carries the n-Tr20 tRNA^Arg mutation) develops progressive neurodegeneration, retinal degeneration, and ribosome stalling ([PMID: 25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/); [PMID: 27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/)). **Invertebrate:** *Drosophila* knockdown of the ortholog **CG2017** recapitulates defects: *"we also investigated the effect of reducing expression of CG2017, an ortholog of human GTPBP1/2, in the fruit fly Drosophila melanogaster"* ([PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)).

**Epidemiology:** JABELS is ultra-rare, with ~28 individuals reported as of 2024 ([PMID: 38852771](https://pubmed.ncbi.nlm.nih.gov/38852771/)). GTPBP2 is listed among autosomal-recessive NBIA (neurodegeneration with brain iron accumulation) genes with a very low combined lifetime risk. Kolarova et al. (2022) estimated: *"The combined estimated lifetime risk of all 13 investigated NBIA disorders is 0.88 (95% confidence interval 0.70-1.10) per 100,000 based on the global gnomAD dataset"*, with GTPBP2 individually far below the top contributors (PLA2G6/PANK2/COASY) ([PMID: 35180557](https://pubmed.ncbi.nlm.nih.gov/35180557/)).

### Finding 7 — Expanded phenotypic spectrum: severe congenital microcephaly, early seizures, white-matter and cardiac anomalies (F007)

Soğukpınar et al. (2026) reported a 4-month-old female of consanguineous parents with a novel homozygous frameshift GTPBP2 variant: *"presenting with severe microcephaly, developmental delay, hypotonia, and craniofacial features. Additional findings included left-sided pes equinovarus, secundum atrial septal defect, and periventricular white matter abnormalities on brain magnetic resonance imaging (MRI). No overt ectodermal abnormalities were observed"* ([PMID: 42553919](https://pubmed.ncbi.nlm.nih.gov/42553919/)). This broadens the spectrum to include **cardiac (secundum ASD) and limb (pes equinovarus) anomalies** and highlights that ectodermal features are non-obligate.

Bertoli-Avella et al. (2018) similarly emphasized family-specific expressivity: *"Notable differences include structural brain abnormalities (e.g., agenesis of the corpus callosum, exclusive to our patients), and evidence for brain iron accumulation (exclusive to the previously described family)"* ([PMID: 29449720](https://pubmed.ncbi.nlm.nih.gov/29449720/)). **HPO terms:** HP:0001631 Atrial septal defect; HP:0001762 Talipes equinovarus; HP:0002500 Abnormal cerebral white matter morphology; HP:0000252 Microcephaly.

### Finding 8 — GTPBP2 protein architecture (F008)

Per UniProt Q9BX10, human GTPBP2 is a **602-amino-acid** protein containing a tr-type (translational) G domain (≈residues 170–398) with GTP-binding/P-loop motifs (binding sites ~179–186, 260–264, 316–319) and an N-terminal disordered region (16–64). Functionally it is involved in the rescue of ribosome stalling due to the presence of non-functional tRNA and has very low GTP-binding activity; it interacts with PELO (Pelota). The weak/context-dependent GTP binding is supported by Zinoviev et al.: *"Although GTPBP2's binding to GTP was stimulated by Phe-tRNA"* ([PMID: 30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/)). Tissue expression is highest in thymus, spleen, and testis, with lower expression in brain, lung, kidney, and ovary. Disease-causing truncating variants (p.Arg144\*, p.Gln407\*, p.Arg470\*, exon-9 splice deletion) remove or disrupt the G domain and/or C-terminal effector region. **GO cellular component:** GO:0005737 cytoplasm; GO:0022626 cytosolic ribosome (associated).

### Finding 9 — gnomAD constraint confirms a recessive loss-of-function gene with strong missense intolerance (F009)

Population constraint metrics for GTPBP2 (ENSG00000172432, chr6:43,605,316–43,629,264) are consistent with a recessive disease gene:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.0002 | NOT haploinsufficient — heterozygous LoF tolerated |
| LOEUF (oe_lof upper) | 0.68 | Moderate LoF constraint |
| observed/expected LoF | 0.51 (obs 32 / exp 63); LoF Z = 3.31 | Depleted for LoF |
| missense Z | 4.61 | **Strong** missense constraint |
| oe_mis | 0.62 | Missense depleted |

The low pLI indicates heterozygous loss-of-function alleles are tolerated in the general population (carriers are unaffected), consistent with recessive inheritance, whereas the high missense Z shows the coding sequence—especially the G domain—is under strong purifying selection.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in GTPBP2** (nonsense, frameshift, or splice) → **absent or truncated, non-functional GTPBP2 protein** lacking the tr-type G domain and/or C-terminal effector region (*demonstrated*; PMID 26675814, 29449720, 42553919).
2. Loss of functional GTPBP2 → **failure of PELO-dependent rescue of stalled/paused ribosomes** (ribosome-associated quality control / no-go decay) (*demonstrated in mouse*; PMID 25061210).
3. Impaired rescue, when combined with limiting tissue-specific tRNA supply (e.g., CNS-enriched tRNA^Arg_UCU), → **codon-specific ribosome stalling at cognate codons (AGA/Arg)** and accumulation of stalled elongation complexes (*demonstrated in mouse*; PMID 27085088).
4. Ribosome stalling → **GCN2 (eIF2α kinase) activation → eIF2α-Ser51 phosphorylation → ATF4-driven integrated stress response (ISR)** (*demonstrated*; PMID 27085088). **Branch:** the ISR is **neuroprotective** and *attenuates* degeneration, so it is a compensatory side-arm, not the injurious main path.
5. Persistent unresolved stalling, aberrant/truncated nascent peptides, and proteostatic stress (*inferred* for human disease from model data) → **progressive neuronal and retinal cell death** (*demonstrated in mouse*; PMID 25061210, 27085088).
6. Neurodegeneration + abnormal neurodevelopment → **clinical phenotype**: motor delay, intellectual disability, speech disorder, hypotonia, spasticity, choreoathetosis, epilepsy, visual impairment, microcephaly, brain atrophy (*demonstrated in humans*; PMID 38852771, 38118446, 29449720).
7. **Parallel/variable branches** (family-specific, mechanism *inferred*): brain iron accumulation (NBIA-spectrum), ectodermal defects (sparse hair), skeletal/cardiac/limb anomalies—reflecting broader roles of translational quality control in development.

```
GTPBP2 biallelic LoF
        │
        ▼
 Loss of ribosome-rescue (PELO partner) ──► ribosome stalling (AGA/Arg codons)
        │                                            │
        │                                            ▼
        │                               GCN2 ─► p-eIF2α ─► ATF4 (ISR)
        │                                            │
        │                                 [PROTECTIVE — attenuates death]
        ▼
 Proteostatic stress / aberrant nascent peptides
        │
        ▼
 Neuronal + retinal degeneration ──► NDD/neurodegeneration phenotype
        │
        ├─► (variable) brain iron accumulation (NBIA spectrum)
        ├─► (variable) ectodermal: sparse hair
        └─► (variable) skeletal / cardiac (ASD) / limb (pes equinovarus)
```

**Upstream vs downstream:** The mutation and loss of ribosome rescue are upstream; stalling is the central lesion; the GCN2/ISR arm and neuronal death are downstream. The ISR is best understood as a downstream *buffer*. **Cell types:** neurons (CL:0000540), retinal photoreceptors (CL:0000210), cerebellar/cortical neurons. **Processes:** GO:0072344 (rescue of stalled ribosome), GO:0006412 (translation), GO:0140469 (GCN2-mediated ISR).

---

## Section-by-Section Knowledge Base Content

### 1. Disease Information
JABELS is an autosomal-recessive neurodevelopmental/neurodegenerative syndrome. **Identifiers:** OMIM #617988; MONDO:0060711; gene GTPBP2 (HGNC). A robust ICD-10/ICD-11, MeSH, and dedicated Orphanet code are not well established for this ultra-rare entity (information not well-indexed). **Synonyms:** JABELS; Jaberi-Elahi syndrome; GTPBP2-related neurodegeneration with brain iron accumulation (NBIA-spectrum). Information is derived from aggregated, disease-level case reports and small family series (not EHR-scale cohorts).

### 2. Etiology
**Causal factor:** purely genetic—biallelic (homozygous or compound-heterozygous) loss-of-function variants in GTPBP2. **Genetic risk factor:** consanguinity (most reported families are consanguineous, enriching for homozygous recessive alleles). **Environmental/protective factors and gene–environment interactions:** none established (not applicable for a monogenic recessive disorder). No protective variants are known.

### 3. Phenotypes
See Finding 2 table for core phenotypes and frequencies. Phenotype **types** span clinical signs (hypotonia, spasticity), physical manifestations (sparse hair, microcephaly, dysmorphism, skeletal/cardiac/limb anomalies), behavioral/cognitive changes (intellectual disability, speech disorder), and neuroimaging/laboratory abnormalities (brain atrophy, white-matter changes, brain iron accumulation). **Onset:** neonatal to infantile; developmental delay is typically apparent in the first months of life. **Severity:** moderate to severe. **Progression:** progressive/neurodegenerative with spasticity and sometimes refractory epilepsy. **QoL impact:** profound—most affected individuals have severe intellectual and motor disability requiring full-time care.

### 4. Genetic / Molecular Information
**Causal gene:** GTPBP2 (6p21.1). **Reported pathogenic variants:** c.430C>T p.(Arg144\*); c.1219C>T p.(Gln407\*); c.1408C>T p.(Arg470\*) (all nonsense, PMID 29449720); exon-9 splice-site deletion (PMID 26675814); novel homozygous frameshift (PMID 42553919). **Variant types:** nonsense, frameshift, splice-site—all truncating/LoF. **Classification:** pathogenic/likely pathogenic per ACMG (PVS1 loss-of-function + recessive segregation). **Allele frequency:** individually absent/ultra-rare in gnomAD. **Origin:** germline. **Functional consequence:** loss of function. **Modifier genes:** tissue-specific tRNA abundance (e.g., n-Tr20 tRNA^Arg in mouse) is a demonstrated genetic modifier of ribosome stalling; GTPBP1 is a non-redundant paralog. **Epigenetics/chromosomal abnormalities:** none reported.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors. Not applicable.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above (Findings 3–5, 8).

### 7. Anatomical Structures Affected
**Primary:** central nervous system—cerebral cortex (UBERON:0000956), cerebellum (UBERON:0002037), basal ganglia (iron deposition; UBERON:0002420), white matter (UBERON:0002316), corpus callosum (UBERON:0002336, agenesis in some). **Secondary/other systems:** retina/eye (UBERON:0000970), integument/hair follicle (ectodermal: sparse hair; UBERON:0002073), skeletal system (UBERON:0001434), heart (atrial septum; UBERON:0002085). **Cells:** neurons (CL:0000540), photoreceptors (CL:0000210). **Subcellular:** cytoplasmic translation machinery / ribosome (GO:0022626); abnormal iron handling implicates mitochondria/lysosomes (inferred). **Lateralization:** generally bilateral/symmetric CNS involvement; one patient had left-sided pes equinovarus (asymmetric limb finding).

### 8. Temporal Development
**Onset:** congenital/infantile (developmental delay in first months). **Course:** chronic, progressive/neurodegenerative, lifelong. **Stages:** early developmental delay → progressive spasticity, movement disorder, epilepsy → advanced neurodegeneration with brain atrophy. No remission. Critical period for any future therapy would plausibly be early, before irreversible neuronal loss (inferred).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears complete in biallelic LoF carriers. **Expressivity:** variable—iron accumulation, corpus callosum agenesis, ectodermal, and cardiac/limb features are family-specific. **Consanguinity:** strong role; most families are consanguineous. **Carrier frequency:** very low (gnomAD; low pLI = heterozygotes tolerated). **Epidemiology:** ultra-rare, ~28 patients reported; part of the recessive NBIA group whose combined lifetime risk is ~0.88/100,000 (PMID 35180557). **Geography:** reported in Iranian, Middle Eastern/North African, and other consanguineous populations; no clear sex predilection.

### 10. Diagnostics
**Genetic testing is the diagnostic cornerstone:** whole-exome or whole-genome sequencing (often with homozygosity mapping in consanguineous pedigrees) identifying biallelic GTPBP2 LoF variants; single-gene/panel testing (NBIA or intellectual-disability panels including GTPBP2) is an alternative. **Imaging:** brain MRI shows atrophy, white-matter abnormalities, possible corpus callosum agenesis, and T2\*/SWI signal consistent with iron accumulation in a subset. **Supportive studies:** EEG for epilepsy; ophthalmologic/retinal evaluation; echocardiography if cardiac anomaly suspected. **No specific biochemical biomarker** exists. **Differential diagnosis:** other NBIA disorders (PKAN/PANK2, PLAN/PLA2G6, MPAN/C19orf12, BPAN/WDR45), GTPBP1-related disorder (phenotypically identical), and other recessive neurodevelopmental/microcephaly syndromes.

### 11. Outcome / Prognosis
Prognosis is poor: severe, lifelong intellectual and motor disability with progressive neurologic decline. Formal survival/mortality statistics are unavailable given the small cohort, but refractory epilepsy and severe neurodisability imply increased morbidity and likely reduced life expectancy. No recovery potential; management is palliative/supportive.

### 12. Treatment
**No disease-specific or disease-modifying therapy exists.** Management is **supportive and multidisciplinary:** anti-seizure medications for epilepsy; physical/occupational/speech therapy; management of spasticity; nutritional support; ophthalmologic and orthopedic/cardiac care as needed. The protective role of the GCN2/ISR arm (PMID 27085088) suggests ISR modulation as a *theoretical* future target, and tRNA-supplementation strategies (cf. tRNA overexpression rescuing related tRNA/translation disorders, PMID 34516840) are conceptual avenues—none clinically available. **NCIT terms:** NCIT:C15313 Supportive Care; NCIT:C15329 Rehabilitation Therapy; NCIT:C98015 Antiepileptic Agent.

### 13. Prevention
Primary prevention is limited to **genetic counseling** for consanguineous/at-risk families, carrier testing, and reproductive options including prenatal diagnosis and preimplantation genetic testing once the familial variant is known. No vaccines, behavioral, or public-health interventions apply.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal or wildlife disease is documented. **Orthologs:** mouse *Gtpbp2*, *Drosophila* CG2017. The mechanism (ribosome rescue/RQC) is deeply evolutionarily conserved. No zoonotic potential.

### 15. Model Organisms
- **Mouse:** *Gtpbp2(nmf205)* loss-of-function on the B6J background (which harbors the modifier n-Tr20 tRNA^Arg mutation) models progressive neurodegeneration, retinal degeneration, AGA-codon ribosome stalling, and GCN2/ISR activation (PMID 25061210, 27085088). **Recapitulation:** strong for neurodegeneration, retinal involvement, and the core molecular mechanism; the requirement for a co-occurring tRNA modifier is a caveat for direct human translation.
- **Invertebrate:** *Drosophila* CG2017 knockdown recapitulates GTPBP1/2 defects (PMID 38118446).
- **Databases:** MGI (mouse Gtpbp2), FlyBase (CG2017), Alliance of Genome Resources.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [26675814](https://pubmed.ncbi.nlm.nih.gov/26675814/) | Mutation in GTPBP2 in family w/ neurodegeneration + brain iron | Human clinical | Original description; causal gene; iron phenotype (F001) |
| [29449720](https://pubmed.ncbi.nlm.nih.gov/29449720/) | Biallelic inactivating GTPBP2 variants cause NDD | Human clinical | Independent confirmation; 3 nonsense variants; variable expressivity (F001, F007) |
| [38852771](https://pubmed.ncbi.nlm.nih.gov/38852771/) | Novel GTPBP2 mutation + literature review | Human clinical review | 28-patient phenotype frequencies; epidemiology (F002, F006) |
| [25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/) | Ribosome stalling from tRNA mutation causes neurodegeneration | Mouse model | Core mechanism: GTPBP2 = ribosome rescue factor (F003) |
| [27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/) | GCN2 activation by ribosome stalling | Mouse model | AGA stalling; eIF2α/ATF4 ISR; protective (F005) |
| [33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/) | GTPBP1 resolves paused ribosomes | Mouse model | Paralog; non-redundant pathway (F003, F004) |
| [38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/) | GTPBP1/GTPBP2 cause identical NDD syndrome | Human + Drosophila | Syndrome definition; LoF; fly model (F004, F006) |
| [30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/) | Functions of GTPBP1/GTPBP2 | In vitro/biochemical | Protein family (eEF1A/eRF3/Hbs1); weak GTP binding (F004, F008) |
| [35180557](https://pubmed.ncbi.nlm.nih.gov/35180557/) | Lifetime risk of recessive NBIA disorders | Computational/genetic | Epidemiology context (F006) |
| [42553919](https://pubmed.ncbi.nlm.nih.gov/42553919/) | Novel homozygous frameshift GTPBP2 | Human clinical | Expanded phenotype: cardiac/limb; no ectodermal (F007) |
| [39419454](https://pubmed.ncbi.nlm.nih.gov/39419454/) | Metabolic alterations in MPAN/NBIA fibroblasts | In vitro | Places GTPBP2 in NBIA iron/lipid-metabolism context |
| [34516840](https://pubmed.ncbi.nlm.nih.gov/34516840/) | tRNA overexpression rescues neuropathy | Mouse model | Conceptual therapeutic analogy (tRNA supplementation) |
| [29096076](https://pubmed.ncbi.nlm.nih.gov/29096076/) | Regulation of mRNA translation in neurons | Review | Broader context: translation dysregulation in neurodegeneration |
| [25061188](https://pubmed.ncbi.nlm.nih.gov/25061188/) | Ribosome rescue and neurodegeneration | Commentary | Contextual commentary on PMID 25061210 |

Evidence strength is high for the causal gene, LoF mechanism, core phenotype, and ribosome-rescue pathway (concordant human genetics + mouse + invertebrate data). The GCN2/ISR arm is directly demonstrated in mouse; its exact role in human patients is inferred.

---

## Limitations and Knowledge Gaps

- **Very small human cohort (~28 patients).** Frequency estimates, natural-history staging, survival, and genotype–phenotype correlations are statistically fragile.
- **Model caveat:** the pivotal mouse neurodegeneration phenotype required a *co-occurring* CNS-tRNA modifier (n-Tr20). Whether analogous tissue-specific tRNA limitations drive the human phenotype is unproven; it is an attractive but inferred bridge.
- **Mechanism of secondary features** (brain iron accumulation, ectodermal/sparse hair, skeletal/cardiac/limb anomalies) is not mechanistically explained and is family-variable.
- **No validated biomarker** for diagnosis, severity, or progression monitoring.
- **No human therapeutic data**; ISR-modulating or tRNA-based strategies are purely conceptual.
- **Ontology/registry indexing** (ICD-11, MeSH, Orphanet code) for JABELS is incomplete.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to pool genotype–phenotype data, natural history, and survival from the dispersed case reports.
2. **Patient-derived models:** generate iPSC-derived neurons and cerebral organoids from GTPBP2-null patients to test whether codon-specific stalling and ISR activation occur in human cells without an engineered tRNA modifier.
3. **Ribosome profiling in human GTPBP2-deficient neurons** to map stall sites and compare with the mouse AGA-codon signature.
4. **Test ISR modulators** (e.g., ISRIB, GCN2 agonists/antagonists) in patient neurons/organoids and the *Gtpbp2* mouse to determine whether enhancing the protective ISR or clearing stalled ribosomes is beneficial.
5. **tRNA-supplementation / AAV gene-replacement proof-of-concept** in the *Gtpbp2* mouse, leveraging the analogy to tRNA rescue of tRNA-synthetase neuropathy (PMID 34516840).
6. **Mechanistic study of brain iron accumulation** in GTPBP2 deficiency to clarify its link (if any) to impaired translational quality control and to position JABELS within the NBIA spectrum.
7. **Formal ClinVar/ClinGen curation** and ACMG classification of all reported GTPBP2 variants, plus submission of an Orphanet/ICD-11 entry to improve indexing.

---

*Report compiled from 5 discovery iterations, 9 confirmed findings, and 14 reviewed papers.*


## Artifacts

- [OpenScientist final report](Jaberi-Elahi_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Jaberi-Elahi_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0060711` (4 mentions) - the report calls it "if available"; MONDO calls it **Jaberi-Elahi syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0072344` (2 mentions) - the report calls it "rescue of stalled ribosome"; GO calls it **rescue of stalled cytosolic ribosome**
- `GO:0140469` (2 mentions) - the report calls it "GCN2-mediated ISR"; GO calls it **GCN2-mediated signaling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
