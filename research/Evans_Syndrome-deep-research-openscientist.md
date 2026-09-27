---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-10T09:27:50.211198'
end_time: '2026-09-10T09:42:57.945125'
duration_seconds: 907.73
template_file: /tmp/evans_prompt.md
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Evans_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Evans_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Evans syndrome
- **MONDO ID:** MONDO:0016030 (if available)
- **Category:** Autoimmune cytopenia / immune dysregulation

## Research Objectives

Please provide a comprehensive research report on **Evans syndrome** covering all of the
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

# Evans Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** Evans syndrome
**MONDO ID:** MONDO:0016030 · **Orphanet:** ORPHA:1959 · **Category:** Autoimmune cytopenia / immune dysregulation
**Report type:** Literature-based disease knowledge-base entry (no primary datasets provided; all content derived from aggregated disease-level literature and cohort studies).

---

## Summary

Evans syndrome (ES) is a rare autoimmune disorder defined by the **concurrent or sequential occurrence of autoimmune hemolytic anemia (AIHA)** — proven by a positive direct antiglobulin (Coombs) test with hemolysis — **and immune thrombocytopenia (ITP)**, sometimes accompanied by autoimmune neutropenia. It is a diagnosis of exclusion, established with a complete blood count, blood smear, and Coombs test after secondary causes have been ruled out. The final common effector mechanism is production of **warm IgG autoantibodies** against erythrocyte antigens and anti-platelet glycoprotein antibodies, leading to **Fc-receptor– and complement-mediated destruction of red cells and platelets, predominantly in the spleen**.

The central insight consolidated across this investigation is that Evans syndrome is best understood **not as an isolated blood disorder but as a phenotype of systemic immune dysregulation**. In children especially, ES is frequently the presenting manifestation of an underlying **inborn error of immunity (IEI)** — with monogenic or immune-dysregulation causes identified in roughly 50–60% of pediatric autoimmune-cytopenia cohorts (ALPS/FAS pathway, CTLA4, LRBA, PIK3CD/APDS, NFKB1, SASH3, partial DiGeorge syndrome). It may also be secondary to systemic lupus erythematosus (SLE), lymphoproliferative disease, or common variable immunodeficiency. ANA positivity in childhood ES is a strong predictor of progression to SLE.

The clinical course is **chronic and relapsing with substantial morbidity and mortality**. Nationwide registry data give an adult incidence approaching ~1.8 per million person-years and a median survival of ~7 years overall (dramatically worse — ~1.7 years — for secondary ES). Pediatric-onset disease carries ~16% mortality at 15 years, most often from infection or bleeding, with a very high treatment burden. Management escalates from corticosteroids/IVIG (first-line) to rituximab and sirolimus (steroid-sparing second-line), with genotype-directed targeted immunotherapy (abatacept, leniolisib, JAK inhibitors) increasingly important. This report details all 15 disease-characteristic domains, flagging where evidence is robust versus where it is sparse or not applicable.

---

## Key Findings

### F001 — Definition: coexistence of AIHA and ITP

Evans syndrome is consistently defined across cohorts as the **simultaneous or sequential association of AIHA (positive direct antiglobulin/Coombs test with hemolysis) and ITP**. The two events may occur at the same time or one may follow the other. Diagnosis relies on a full blood count/film and a Coombs test, and is a diagnosis of exclusion after secondary causes are ruled out. In the French OBS'CEREVANCE pediatric AIHA cohort (n=265), Evans syndrome was present in **37%** of childhood AIHA cases.

> "There is a coexistence of Immune thrombocytopenia (ITP) with Autoimmune haemolytic anaemia (AIHA) and both of these events may occur simultaneously or one follows the other." — [PMID: 31983745](https://pubmed.ncbi.nlm.nih.gov/31983745/)
> "Evans' syndrome was diagnosed in 37% of cases." — [PMID: 21228033](https://pubmed.ncbi.nlm.nih.gov/21228033/)

### F002 — Frequently the presenting sign of an inborn error of immunity (IEI)

In a Tampa Bay prospective autoimmune cytopenia (AIC) cohort (n=104), **51% showed evidence of IEI and 26% had monogenic disorders**; IEI prevalence was highest in Evans syndrome (61.5%) and AIHA (62.5%). The most common monogenic causes were **partial DiGeorge syndrome (pDGS)**, followed by variants in **NFKB1, CTLA4, and FAS**. A germline **SASH3** nonsense mutation (c.862C>T; p.Arg288Ter) has been identified as a specific monogenic cause. By contrast, an adult chronic ITP/Evans cohort (n=44) screened with an NGS panel of >370 IEI genes found **no fully penetrant IEI**, though 18.2% carried heterozygous pathogenic IEI variants — establishing that the diagnostic yield of IEI testing is far higher in pediatric than adult-onset disease.

> "Among 104 AIC patients, 53 (51%) showed evidence of IEI, including 27 (26%) with monogenic disorders-most commonly partial DiGeorge syndrome (pDGS), followed by variants in NFKB1, CTLA4, and FAS." — [PMID: 41560547](https://pubmed.ncbi.nlm.nih.gov/41560547/)
> "No cases of IEI were identified despite a high representation of subjects with a personal history of autoimmunity" — [PMID: 37792884](https://pubmed.ncbi.nlm.nih.gov/37792884/)
> "identified a germline mutation in SASH3 (c.862C>T;p.Arg288Ter), indicating a recently identified IEI" — [PMID: 37646304](https://pubmed.ncbi.nlm.nih.gov/37646304/)

### F003 — Chronic, relapsing, multisystem course with ~16% pediatric mortality at 15 years

In the French OBS'CEREVANCE cohort of 151 pediatric-onset ES patients with >5 years follow-up (median 11.3 years): at 10 years, ITP and AIHA were in sustained complete remission in **54.5%** and **78.4%** respectively; by age 20, **74% had ≥1 clinical immunopathological manifestation** (lymphoproliferation, dermatological, GI/hepatic, pulmonary). **Survival at 15 years was 84% (~16% mortality)**; death occurred at a median age of 18 years, most often from infection. The **number of second-line treatments and severe/recurrent infections were independently associated with mortality**. In an earlier cohort (n=156), 5-year ITP and AIHA relapse-free survival were 25% and 61%, and 69% required ≥1 second-line treatment.

> "At 10 years, ITP and AIHA were in sustained complete remission in 54.5% and 78.4% of patients, respectively." — [PMID: 33440924](https://pubmed.ncbi.nlm.nih.gov/33440924/)
> "Survival at 15 years after diagnosis was 84%." — [PMID: 33440924](https://pubmed.ncbi.nlm.nih.gov/33440924/)
> "Overall, 69% of children required one or more second-line immune treatments" — [PMID: 26484337](https://pubmed.ncbi.nlm.nih.gov/26484337/)

### F004 — Treatment: corticosteroids/IVIG first-line; rituximab and sirolimus effective second-line

Standard first-line therapy is **corticosteroids ± IVIG**, but relapse on taper is common. **Rituximab** (anti-CD20): in a prospective French pediatric AIHA/Evans cohort (n=61), 75% responded and rituximab allowed steroid withdrawal in 72%; 6-year relapse-free survival was 48% (higher in isolated AIHA than in ES, P<0.05). **Sirolimus** (mTOR inhibitor): in a multicenter prospective trial of 30 refractory AICs, all 12 ALPS children achieved durable complete response and most patients with Evans syndrome/CVID/SLE responded. **Genotype-directed targeted agents** are emerging (abatacept for CTLA4/LRBA; sirolimus/leniolisib for ALPS/APDS; ruxolitinib/baricitinib). **Splenectomy** is effective but its benefit is diminished by immunopathological manifestations and carries infection/thrombosis risk.

> "Forty-six patients responded (75%) and the 6-year relapse-free survival (RFS) was 48%." — [PMID: 28444729](https://pubmed.ncbi.nlm.nih.gov/28444729/)
> "sirolimus led to CR and durable responses in a majority of children with refractory multilineage autoimmune cytopenias" — [PMID: 26504182](https://pubmed.ncbi.nlm.nih.gov/26504182/)

### F005 — ANA-positive childhood ES is a strong risk factor for progression to SLE

In the OBS'CEREVANCE cohort, ANA were positive in 20% (355/1803) of children with AIC; 22% of ANA-positive patients developed SLE at a median age of 14.5 years. **Progression to SLE occurred in 45% of ANA-positive Evans syndrome patients** (vs 20% chronic ITP, 19% AIHA); no ANA-negative patient developed SLE. Independent risk factors were **age >10 years at AIC diagnosis (RR 3.67, 95% CI 1.18–11.4, P=.024)** and **ANA titer >1/160 (RR 5.28, 95% CI 1.20–23.17, P=.027)**.

> "20% of chronic immune thrombocytopenic purpura, 19% of autoimmune hemolytic anemia, and 45% of Evans syndrome" — [PMID: 38227934](https://pubmed.ncbi.nlm.nih.gov/38227934/)

### F006 — Very rare, rising incidence; secondary ES has markedly worse survival

Danish nationwide registry data. **Adults (n=242, 1977–2017):** mean age at diagnosis 58.5 years, 51.2% women, 27.3% secondary; incidence rose to **1.8 per million person-years** and prevalence to **21.3 per million persons** by 2016. Median survival was **7.2 years overall (primary 10.9 years; secondary only 1.7 years; secondary 5-year survival 38%)**; leading causes of death were bleeding, infections, and hematological cancer. **Children <13 years (n=21):** incidence 0.5–1.2 per million person-years; prevalence rose from 6.7 (1990) to 19.3 (2015) per million; hazard ratio for death was **22-fold** higher than matched general-population children.

> "The annual Evans syndrome incidence and prevalence rose significantly during the study period, to 1.8 per million person-years and 21.3 per million persons, respectively, in 2016." — [PMID: 31292991](https://pubmed.ncbi.nlm.nih.gov/31292991/)
> "The median survival with Evans syndrome was 7.2 years (primary Evans syndrome: 10.9 years; secondary Evans syndrome: 1.7 years)." — [PMID: 31292991](https://pubmed.ncbi.nlm.nih.gov/31292991/)
> "Hazard ratio for death was 22 fold higher for children with ES compared to matched children from general population" — [PMID: 32271826](https://pubmed.ncbi.nlm.nih.gov/32271826/)

### F007 — Mechanism: defective lymphocyte apoptosis / broken tolerance → autoantibody-mediated cytopenias

A large subset of ES — particularly **ALPS** — results from defective **FAS-mediated extrinsic apoptosis** of lymphocytes (germline/somatic **FAS, FASLG, CASP10**), leading to lymphoproliferation, expansion of **TCRαβ+ CD4−CD8− double-negative T (DNT) cells**, and autoimmune cytopenias. ALPS biomarkers include elevated DNT cells and elevated **soluble FAS ligand (sFASL)**. Other monogenic causes disrupt tolerance at distinct nodes: **CTLA4/LRBA** (impaired Treg checkpoint), **PIK3CD** (APDS, PI3K-δ hyperactivation), **NFKB1** (haploinsufficiency), and **SASH3** (lymphocyte adaptor; germinal-center hypoplasia). The final common step is warm IgG anti-erythrocyte and anti-platelet-glycoprotein autoantibody production causing Fc-receptor/complement-mediated splenic destruction.

> "Autoimmune lymphoproliferative syndrome (ALPS) is a disorder of disrupted lymphocyte homeostasis, resulting from mutations in the Fas apoptotic pathway." — [PMID: 22157362](https://pubmed.ncbi.nlm.nih.gov/22157362/)
> "sFASL level can efficiently discriminate patients with ALPS when using the appropriate thresholds" — [PMID: 38700373](https://pubmed.ncbi.nlm.nih.gov/38700373/)
> "LRBA protein deficiency was shown to be responsible for different types of inborn errors of immunity, such as common variable immunodeficiency (CVID) and autoimmune lymphoproliferative syndrome (ALPS)" — [PMID: 31432443](https://pubmed.ncbi.nlm.nih.gov/31432443/)

### F008 — Clinical phenotype and diagnostic laboratory profile

The phenotype combines features of both cytopenias. **AIHA component** (HP:0004808): pallor (HP:0000980), fatigue (HP:0012378), jaundice (HP:0000952), dark urine, splenomegaly (HP:0001744); labs show positive DAT (warm IgG±C3d — **74% IgG/IgG+C3d** in the pediatric cohort), reticulocytosis, elevated LDH and indirect bilirubin, low haptoglobin. **ITP component** (HP:0001973): petechiae (HP:0000967), purpura/bruising (HP:0000979), mucosal/GI bleeding (HP:0011897). When ES reflects immune dysregulation, organomegaly is prominent — in LRBA deficiency **splenomegaly occurred in 93.3% (14/15)**. Some patients also have neutropenia (HP:0001875), hypogammaglobulinemia (HP:0004313), and recurrent infections (HP:0002719).

> "In 74% of cases the direct antiglobulin test was IgG/IgG+C3d." — [PMID: 21228033](https://pubmed.ncbi.nlm.nih.gov/21228033/)
> "Splenomegaly was seen in 93.3% (14/15) of the patients on admission." — [PMID: 31432443](https://pubmed.ncbi.nlm.nih.gov/31432443/)

### F009 — Natural disease in dogs; FAS-pathway (Fas^lpr) mouse model

**Natural disease:** ES (concurrent immune-mediated hemolytic anemia + immune-mediated thrombocytopenia) is a recognized spontaneous entity in the domestic dog (*Canis lupus familiaris*, NCBI:txid9615), reported across breeds including Rottweiler, Miniature Schnauzer, and Dachshund; canine cases are DAT-positive, glucocorticoid/immunosuppressant-responsive, and can be complicated by thrombosis and opportunistic infection — paralleling human disease. **Model organism:** the FAS pathway underlying ALPS-type human ES is modeled by the **MRL/lpr (Fas^lpr) and gld (Faslg)** mouse, which develop lymphoproliferation, TCRαβ+ DNT-cell accumulation, autoantibodies, and autoimmune cytopenias; leniolisib reduced lymphoproliferation in murine ALPS.

> "presumptively diagnosed with Evans' syndrome (ES)" — [PMID: 19411652](https://pubmed.ncbi.nlm.nih.gov/19411652/)
> "Leniolisib reduced lymphoproliferative disease in murine autoimmune lymphoproliferative syndrome" — [PMID: 41608120](https://pubmed.ncbi.nlm.nih.gov/41608120/)

---

## The 15-Section Disease Characteristics Report

### 1. Disease Information

**Overview.** Evans syndrome is a rare, chronic autoimmune disorder characterized by the combination of AIHA and ITP (± autoimmune neutropenia), occurring simultaneously or sequentially (F001). It is a diagnosis of exclusion made after ruling out secondary causes (SLE, lymphoproliferative disease, IEI, drugs, infection).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0016030 |
| Orphanet | ORPHA:1959 |
| ICD-10 | D69.3 (ITP component) / D59.1 (AIHA component) — no single dedicated code |
| ICD-11 | 3B51.0 / 3A20 (component-based) |
| MeSH | Anemia, Hemolytic, Autoimmune; Thrombocytopenia (no unique ES MeSH heading) |
| OMIM | No single OMIM entry; monogenic causes have their own (e.g., ALPS 601859; CTLA4 haploinsufficiency 616100; APDS 615513) |

**Synonyms:** Evans-Fisher syndrome; autoimmune hemolytic anemia with immune thrombocytopenia; combined autoimmune hemolytic anemia and thrombocytopenia.

**Information source.** Evidence in this report derives from aggregated disease-level resources: national prospective cohorts (French OBS'CEREVANCE), nationwide registries (Danish), and case series/reports — not from a single EHR extract.

### 2. Etiology

**Causal factors.** ES is heterogeneous. It may be **primary (idiopathic)** or **secondary** to another disorder. A dominant paradigm is that ES is often the hematologic expression of an **underlying inborn error of immunity** (F002, F007). Documented monogenic/genetic causes: **FAS, FASLG, CASP10** (ALPS), **CTLA4, LRBA** (Treg checkpoint defects), **PIK3CD** (APDS), **NFKB1** (haploinsufficiency), **SASH3**, and **partial DiGeorge syndrome (22q11.2 deletion)**. Secondary causes include SLE, common variable immunodeficiency, and lymphoproliferative disease.

**Genetic risk factors.** Germline loss-of-function variants in the genes above; somatic FAS variants in ALPS; the 22q11.2 microdeletion (pDGS). ANA positivity marks a susceptibility state for SLE-associated ES (F005).

**Environmental risk factors.** Age (bimodal: pediatric and older-adult peaks), female sex (adult 51.2% women), family/personal history of autoimmunity. No established toxin, occupational, or dietary cause. Some secondary cases follow infection or lymphoma.

**Protective factors.** None specifically established. ANA-negativity predicts against SLE progression (F005). No protective genetic alleles are defined for ES.

**Gene–environment interactions.** In ANA-positive children, age >10 years plus high ANA titer (>1/160) multiplicatively raise SLE risk (F005), illustrating interaction between an autoantibody "environment" and host age/genetic background. Not otherwise well characterized.

### 3. Phenotypes

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Autoimmune hemolytic anemia | Lab/clinical | HP:0004808 | Defining; DAT+ in ~all; 74% IgG/IgG+C3d |
| Autoimmune thrombocytopenia | Lab/clinical | HP:0001973 | Defining |
| Pallor | Sign | HP:0000980 | Common (anemia) |
| Fatigue | Symptom | HP:0012378 | Common |
| Jaundice | Sign | HP:0000952 | Hemolysis |
| Splenomegaly | Sign | HP:0001744 | Very common in immune-dysregulation ES; 93.3% in LRBA deficiency |
| Petechiae | Sign | HP:0000967 | Thrombocytopenic bleeding |
| Purpura/bruising | Sign | HP:0000979 | Common |
| Mucosal/GI bleeding | Sign | HP:0011897 | Variable severity |
| Lymphadenopathy | Sign | HP:0002716 | ALPS-type ES |
| Neutropenia | Lab | HP:0001875 | Subset (triple cytopenia) |
| Hypogammaglobulinemia | Lab | HP:0004313 | IEI-associated |
| Recurrent infections | Clinical | HP:0002719 | IEI-associated; major cause of death |

**Characteristics.** Onset spans neonatal to geriatric; pediatric-onset disease is typically chronic and relapsing (F003), adult disease often chronic. Severity is **variable to severe** (life-threatening anemia or bleeding possible). Progression is **episodic/relapsing-remitting**. By age 20, 74% of pediatric-onset patients have ≥1 additional immunopathological manifestation (F003).

**Quality-of-life impact.** High treatment burden, chronic relapses, transfusion dependence in flares, immunosuppression-related infection risk, and cumulative organ involvement substantially impair QoL; formal EQ-5D/SF-36/PROMIS data specific to ES were not identified (knowledge gap).

### 4. Genetic / Molecular Information

**Causal genes** (in monogenic/IEI-associated ES): **FAS** (OMIM 134637), **FASLG**, **CASP10**, **CTLA4**, **LRBA**, **PIK3CD**, **NFKB1**, **SASH3**; chromosomal **22q11.2 deletion** (partial DiGeorge) (F002, F007).

**Pathogenic variants.** Documented examples include the **SASH3** nonsense variant **c.862C>T (p.Arg288Ter)** (F002). Variant classes span nonsense/frameshift (loss of function; NFKB1, LRBA, SASH3), missense (gain of function in PIK3CD/APDS), and structural (22q11.2 deletion). ALPS may involve **somatic** FAS variants restricted to DNT cells as well as germline variants. Functional consequences: **loss of function** (FAS apoptosis, LRBA/CTLA4 checkpoint, NFKB1), **gain of function** (PIK3CD/PI3K-δ hyperactivation).

**Modifier genes.** Not formally established for ES; disease expression is modified by the specific IEI genotype and by secondary triggers (SLE, lymphoma).

**Epigenetic information.** No ES-specific DNA-methylation or histone-modification signature was identified in the literature reviewed (knowledge gap).

**Chromosomal abnormalities.** 22q11.2 deletion (partial DiGeorge) is the single most common monogenic-level cause in one large pediatric AIC cohort (F002).

### 5. Environmental Information

**Environmental factors.** No established chemical, radiation, or occupational cause. **Infectious agents** may act as triggers in secondary ES, and infections are a leading complication/cause of death, but no single pathogen is causal. **Lifestyle factors** are not established causes; comorbidities such as diabetes and heavy smoking appear in case reports of thrombotic complications but are not disease causes. ES itself is autoimmune, not infectious or transmissible.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline (or somatic) genetic lesion in a tolerance/apoptosis gene — e.g., **FAS/FASLG/CASP10, CTLA4, LRBA, PIK3CD, NFKB1, SASH3** — **leads to** defective lymphocyte homeostasis or a broken immune checkpoint (upstream; demonstrated for these IEIs). *In primary/idiopathic ES without an identified gene, this step is inferred.*
2. **Branch A (ALPS-type):** defective FAS-mediated extrinsic apoptosis **results in** failure to delete autoreactive lymphocytes → lymphoproliferation and **accumulation of TCRαβ+ CD4−CD8− double-negative T (DNT) cells** (demonstrated; DNT cells and elevated soluble FASL are diagnostic biomarkers).
3. **Branch B (checkpoint-type):** CTLA4/LRBA loss, PI3K-δ hyperactivation (APDS), or NFKB1 haploinsufficiency **results in** impaired regulatory T-cell function and dysregulated B/T-cell activation.
4. Both branches **converge on** loss of B-cell tolerance and **results in** activation of autoreactive B cells / plasma cells.
5. This **leads to** production of **warm IgG autoantibodies** against red-cell antigens and anti-platelet glycoprotein (e.g., GPIIb/IIIa) antibodies (demonstrated effector step).
6. Autoantibody opsonization **results in** **Fc-receptor– and complement-mediated phagocytosis/destruction of erythrocytes and platelets, predominantly by splenic macrophages** (downstream effector).
7. This **leads to** the clinical manifestations: hemolytic anemia (pallor, jaundice, reticulocytosis, low haptoglobin, high LDH/bilirubin) and thrombocytopenia (petechiae, purpura, bleeding) (F007, F008).

```
 Genetic lesion (FAS/CTLA4/LRBA/PIK3CD/NFKB1/SASH3 or unknown)
          │
   ┌──────┴───────────┐
   ▼                   ▼
 Defective FAS       Impaired Treg / checkpoint
 apoptosis (ALPS)    (CTLA4, LRBA, APDS, NFKB1)
   │  DNT-cell         │
   │  expansion        │
   └──────┬────────────┘
          ▼
  Loss of B-cell tolerance → autoreactive plasma cells
          ▼
  Warm IgG anti-RBC + anti-platelet autoantibodies
          ▼
  Fc-receptor / complement-mediated splenic destruction
          ▼
  AIHA + ITP  (Evans syndrome)
```

**Molecular pathways:** FAS/FASLG extrinsic apoptosis (caspase-8/10); PI3K-AKT-mTOR (APDS; rationale for sirolimus/leniolisib); CTLA4–CD80/86 costimulation checkpoint; NF-κB signaling. **Cellular processes:** defective apoptosis, lymphoproliferation, breakdown of self-tolerance, complement activation, macrophage phagocytosis. **Immune involvement:** combined autoimmunity + immunodeficiency (recurrent infection). **GO terms:** apoptotic process (GO:0006915), regulation of immune response (GO:0050776), complement activation (GO:0006956), phagocytosis (GO:0006909). **Cell types (CL):** double-negative T cell, regulatory T cell (CL:0000815), B cell/plasma cell (CL:0000786), macrophage (CL:0000235), erythrocyte (CL:0000232), platelet/thrombocyte (CL:0000233).

### 7. Anatomical Structures Affected

**Organ level.** Primary: **spleen** (UBERON:0002106; principal site of destruction and often enlarged), **bone marrow** (UBERON:0002371; compensatory hyperplasia), **blood** (UBERON:0000178). Secondary/associated: **lymph nodes** (UBERON:0000029; lymphoproliferation), **liver** (UBERON:0002107; hepatomegaly, associated autoimmune hepatitis), lungs and GI tract in multisystem ES. Body systems: hematopoietic/immune (primary), with cardiovascular (thrombosis risk), hepatic, pulmonary, and GI involvement in immune-dysregulation subtypes.

**Tissue/cell level.** Targets: **erythrocytes** (CL:0000232) and **platelets** (CL:0000233); effectors: splenic **macrophages** (CL:0000235), dysregulated **T cells** (including DNT cells) and **B cells/plasma cells**.

**Subcellular level.** Death-inducing signaling complex at the plasma membrane (FAS/FADD/caspase); autoantibody targets are red-cell membrane proteins and platelet-surface glycoproteins. GO cellular components: plasma membrane (GO:0005886), death-inducing signaling complex (GO:0031264).

**Localization.** Systemic; splenic destruction is central. Lateralization not applicable (systemic hematologic disease).

### 8. Temporal Development

**Onset.** Bimodal — pediatric (childhood) and older-adult (mean 58.5 years in the Danish adult cohort). Onset pattern is typically **subacute to chronic/insidious**, though acute severe hemolytic or bleeding crises occur. The two cytopenias may present simultaneously or years apart (F001).

**Progression.** **Relapsing-remitting/episodic**, chronic lifelong course (F003). Pediatric 5-year relapse-free survival: ITP 25%, AIHA 61%. At 10 years, sustained CR in 54.5% (ITP) and 78.4% (AIHA). Multisystem immunopathology accrues over time (74% by age 20).

**Patterns.** Remissions are usually **treatment-induced**; spontaneous durable remission is uncommon in pediatric-onset disease. Critical windows: early diagnosis of an underlying IEI opens the door to genotype-targeted therapy; monitoring for immunopathological manifestations refines splenectomy risk–benefit.

### 9. Inheritance and Population

**Epidemiology (F006).** Adult incidence ~**1.8 per million person-years**, prevalence ~**21.3 per million** (Denmark, 2016). Pediatric incidence 0.5–1.2 per million person-years; pediatric prevalence rising (6.7→19.3 per million, 1990→2015). Adult mean age at diagnosis 58.5 years; 51.2% women; 27.3% secondary.

**Genetic etiology.** Inheritance depends on the underlying IEI: **autosomal dominant** (ALPS/FAS, CTLA4 haploinsufficiency, NFKB1, PIK3CD GOF), **autosomal recessive** (LRBA), **X-linked** (SASH3), or **de novo/structural** (22q11.2 deletion). Penetrance is **incomplete and age-dependent** (e.g., CTLA4 haploinsufficiency). Expressivity is variable. Somatic mosaicism occurs in ALPS (somatic FAS variants). Anticipation, founder effects, and consanguinity are not general features of ES, though consanguinity increases recessive-IEI (LRBA) risk. Most "primary" ES has no identified single gene and behaves as a multifactorial/polygenic autoimmune trait.

**Population demographics.** No strong ethnic predilection established; adult female predominance is modest (~51%). Geographic distribution is worldwide; rising recorded incidence likely reflects better ascertainment.

### 10. Diagnostics

**Clinical/laboratory tests (F008).** CBC with **blood smear** (spherocytes, polychromasia, low platelets); **direct antiglobulin (Coombs) test** (warm IgG ± C3d; 74% IgG/IgG+C3d); reticulocyte count (elevated); **LDH** (elevated), **indirect/unconjugated bilirubin** (elevated), **haptoglobin** (low); platelet count (low). LOINC-codable analytes: hemoglobin, platelet count, reticulocytes, LDH, bilirubin, haptoglobin, DAT.

**Biomarkers.** For underlying ALPS: elevated **TCRαβ+ DNT cells** and **soluble FAS ligand (sFASL)**; also elevated vitamin B12 and IL-10 in ALPS. ANA (SLE risk marker). Immunoglobulin levels (hypogammaglobulinemia in IEI).

**Genetic testing.** Given the high IEI yield in pediatric ES (F002), **NGS gene panels (>370 IEI genes), whole-exome sequencing, and increasingly whole-genome sequencing** are recommended, especially in children, early-onset, syndromic, or treatment-refractory cases. **Chromosomal microarray/FISH** for 22q11.2 deletion (partial DiGeorge). Targeted single-gene testing when a specific IEI is suspected. Adult isolated ES has lower monogenic yield.

**Clinical criteria & differential diagnosis.** Diagnosis is clinical + laboratory (coexistent AIHA and ITP with positive DAT) after exclusion of: **thrombotic thrombocytopenic purpura / thrombotic microangiopathy** (check ADAMTS13; <10 IU/dL indicates iTTP), SLE, drug-induced cytopenias, lymphoproliferative disease, DIC, and hemophagocytic syndrome. Microangiopathic hemolysis with schistocytes distinguishes TMA from the warm-antibody hemolysis of ES.

**Screening.** No population screening. **Cascade genetic screening** of relatives is appropriate when a monogenic IEI is identified. No newborn screening for ES.

### 11. Outcome / Prognosis

**Survival/mortality (F003, F006).** Adult median survival **7.2 years** (primary 10.9 years; **secondary only 1.7 years**, 5-year survival 38%). Pediatric survival at 15 years **84%** (~16% mortality), death at median age 18 years; pediatric HR for death 22× the general population. Leading causes of death: **infection, bleeding, and hematological cancer**.

**Morbidity/function.** High — chronic relapses, transfusion dependence during flares, cumulative multisystem immunopathology, and immunosuppression-related complications. Disease-specific QoL instruments were not identified (gap).

**Complications.** Recurrent/severe infections (major driver of mortality), thrombosis (including reports of Buerger's disease and spontaneous echocardiographic contrast), hematological malignancy, and progression to SLE.

**Prognostic factors.** Independent predictors of mortality: **number of second-line treatments** and **severe/recurrent infections** (F003). **Secondary etiology** predicts markedly worse survival (F006). ANA positivity + age >10 + high titer predicts SLE progression (F005). Immunopathological manifestations reduce splenectomy benefit.

### 12. Treatment

| Line | Intervention | Evidence / notes | NCIT |
|---|---|---|---|
| First | **Corticosteroids** (prednisone/prednisolone) ± **IVIG** | Standard; relapse common on taper (F004) | NCIT:C305 (steroid); NCIT:C555 (IVIG) |
| Second | **Rituximab** (anti-CD20) | 75% response, 72% steroid withdrawal, 6-yr RFS 48% (F004) | NCIT:C1702 |
| Second | **Sirolimus** (mTOR inhibitor) | Durable CR in refractory multilineage AIC, all ALPS children (F004) | NCIT:C1212 |
| Second/other | Mycophenolate mofetil, azathioprine | Effective in ES + autoimmune hepatitis case reports | NCIT:C2005 / NCIT:C264 |
| Targeted | **Abatacept** (CTLA4-Ig) | For CTLA4/LRBA defects | NCIT:C65483 |
| Targeted | **Leniolisib** / sirolimus | For APDS/ALPS (PI3K-δ pathway); leniolisib validated in murine ALPS | — |
| Targeted | **Ruxolitinib / baricitinib** (JAK inhibitors) | Immune dysregulation subtypes | — |
| Complement/other | Iptacopan (factor B inhibitor) | Refractory C3d-positive AIHA flares (case reports) | — |
| Surgical | **Splenectomy** | Effective but benefit reduced by immunopathological manifestations; infection/thrombosis risk | NCIT:C51915 |
| Cellular | Hematopoietic stem cell transplant | For severe monogenic IEI-associated ES | NCIT:C15431 |

**Pharmacogenomics/personalized medicine.** Genotype-directed therapy is a defining trend: abatacept for CTLA4/LRBA, sirolimus/leniolisib for ALPS/APDS, JAK inhibitors for interferon/JAK-STAT–driven dysregulation. **Treatment strategy:** escalate from steroids/IVIG → rituximab/sirolimus → genotype-targeted agents; reserve splenectomy for selected cases; support with transfusion, infection prophylaxis, and thrombosis awareness.

### 13. Prevention

**Primary prevention:** none (no modifiable cause). **Secondary prevention:** early recognition of coexistent cytopenias and prompt immunosuppression; **early IEI genetic diagnosis** enables targeted therapy and family counseling. **Tertiary prevention:** infection prophylaxis (vaccination, especially before/after splenectomy — encapsulated-organism vaccines; antibiotic prophylaxis post-splenectomy), thrombosis vigilance, monitoring for SLE progression and malignancy, and surveillance for accruing immunopathological manifestations. **Genetic counseling** is indicated when a monogenic IEI is found (variable inheritance patterns). No immunization prevents ES itself.

### 14. Other Species / Natural Disease

**Taxonomy.** Naturally occurring ES is well documented in the **domestic dog** (*Canis lupus familiaris*, **NCBI:txid9615**) — concurrent immune-mediated hemolytic anemia and immune-mediated thrombocytopenia (F009). Reported breeds: **Rottweiler, Miniature Schnauzer, Dachshund**. Canine cases are DAT-positive and glucocorticoid/immunosuppressant-responsive, and can be complicated by thrombosis and opportunistic infection during immunosuppression — closely paralleling human disease.

**Orthologous genes.** *FAS*, *FASLG*, *CTLA4*, *LRBA*, *PIK3CD* orthologs are conserved across mammals. **Comparative biology:** the FAS apoptosis mechanism is evolutionarily conserved, underpinning both canine natural disease and rodent models. **Zoonotic potential:** none (autoimmune, non-transmissible).

### 15. Model Organisms

**Model type.** Mammalian (mouse) genetic models of the FAS pathway recapitulate ALPS-type ES (F009). **Specific systems:** **MRL/lpr (Fas^lpr)** mouse (Fas loss of function) and **gld (Faslg)** mouse (FAS ligand defect) — both develop **lymphoproliferation, TCRαβ+ DNT-cell accumulation, autoantibodies, and autoimmune cytopenias**.

**Applications.** These models study the apoptosis-defect mechanism, DNT-cell biology, and therapeutics — e.g., **leniolisib reduced lymphoproliferative disease in murine ALPS** (F009), validating targeted therapy translation. **Limitations:** lpr/gld mice best model the ALPS/FAS subtype and background-dependent lupus-like autoimmunity; they do not capture the full heterogeneity of human ES (CTLA4, LRBA, APDS, NFKB1, SASH3, secondary ES). **Resources:** MGI, IMSR for Fas/Faslg alleles.

---

## Mechanistic Model / Interpretation

Evans syndrome should be conceptualized as a **shared downstream phenotype produced by many upstream lesions of immune tolerance**. The unifying "trunk" is autoantibody-mediated, Fc-receptor/complement-driven splenic destruction of red cells and platelets. The "roots" are diverse: defective apoptosis (ALPS/FAS pathway), failed Treg checkpoints (CTLA4/LRBA), signaling hyperactivation (PIK3CD/APDS), transcriptional haploinsufficiency (NFKB1), adaptor loss (SASH3), or a structural syndrome (22q11.2/pDGS) — and, in a large fraction, no identifiable single gene (polygenic/multifactorial autoimmunity), or a secondary driver (SLE, lymphoma).

This model explains the clinical behavior: because the root cause is systemic immune dysregulation, ES is rarely "just" a blood disease — it tends to recruit additional autoimmune and lymphoproliferative manifestations over time (74% by age 20), progresses to SLE in high-risk ANA-positive children, relapses despite treatment, and kills primarily through infection (reflecting the immunodeficiency side of the dysregulation) and bleeding. It also explains why therapy is migrating from broad immunosuppression toward **mechanism-matched targeted agents** (abatacept, sirolimus/leniolisib, JAK inhibitors), which requires molecular diagnosis via genomic sequencing.

---

## Evidence Base

| PMID | Study | Supports |
|---|---|---|
| [31983745](https://pubmed.ncbi.nlm.nih.gov/31983745/) | ES case report/review | Definition, autoantibody mechanism (F001, F008) |
| [21228033](https://pubmed.ncbi.nlm.nih.gov/21228033/) | French AIHA cohort (n=265) | 37% ES frequency; 74% IgG/IgG+C3d DAT (F001, F008) |
| [41560547](https://pubmed.ncbi.nlm.nih.gov/41560547/) | Prospective AIC biomarker study (n=104) | 51% IEI, 26% monogenic; pDGS/NFKB1/CTLA4/FAS (F002) |
| [37792884](https://pubmed.ncbi.nlm.nih.gov/37792884/) | Adult ITP/Evans IEI screen (n=44) | Low adult monogenic yield (F002) |
| [37646304](https://pubmed.ncbi.nlm.nih.gov/37646304/) | SASH3 case | Novel monogenic cause (F002) |
| [33440924](https://pubmed.ncbi.nlm.nih.gov/33440924/) | OBS'CEREVANCE long-term (n=151) | Remission rates, 84% 15-yr survival, mortality factors (F003) |
| [26484337](https://pubmed.ncbi.nlm.nih.gov/26484337/) | OBS'CEREVANCE cohort (n=156) | High treatment burden (F003) |
| [28444729](https://pubmed.ncbi.nlm.nih.gov/28444729/) | Rituximab pediatric cohort (n=61) | 75% response, 72% steroid withdrawal (F004) |
| [26504182](https://pubmed.ncbi.nlm.nih.gov/26504182/) | Sirolimus prospective trial (n=30) | Sirolimus efficacy in refractory AIC (F004) |
| [38227934](https://pubmed.ncbi.nlm.nih.gov/38227934/) | ANA-associated AIC study | 45% ES→SLE; risk factors (F005) |
| [31292991](https://pubmed.ncbi.nlm.nih.gov/31292991/) | Danish adult registry (n=242) | Incidence/prevalence; primary vs secondary survival (F006) |
| [32271826](https://pubmed.ncbi.nlm.nih.gov/32271826/) | Danish pediatric cohort (n=21) | Pediatric incidence; 22× mortality HR (F006) |
| [22157362](https://pubmed.ncbi.nlm.nih.gov/22157362/) | ALPS review | FAS apoptosis mechanism (F007) |
| [38700373](https://pubmed.ncbi.nlm.nih.gov/38700373/) | ALPS biomarker study | sFASL/DNT biomarkers (F007) |
| [31432443](https://pubmed.ncbi.nlm.nih.gov/31432443/) | LRBA defect series | LRBA tolerance mechanism; 93.3% splenomegaly (F007, F008) |
| [19411652](https://pubmed.ncbi.nlm.nih.gov/19411652/) | Canine ES case | Natural disease in dog (F009) |
| [41608120](https://pubmed.ncbi.nlm.nih.gov/41608120/) | Murine ALPS + leniolisib | Mouse model + targeted therapy (F009) |
| [35443028](https://pubmed.ncbi.nlm.nih.gov/35443028/) | Splenectomy outcomes | Immunopathological manifestations reduce splenectomy benefit |
| [40809448](https://pubmed.ncbi.nlm.nih.gov/40809448/) | Microangiopathic anemia review | TTP/TMA differential (ADAMTS13) |

---

## Limitations and Knowledge Gaps

- **No dedicated OMIM/ICD entry:** ES is coded by its components; identifiers are inherited from underlying IEIs, complicating standardized annotation.
- **Adult vs pediatric divergence:** monogenic IEI yield is high in children but low in adults; conclusions from pediatric cohorts may not transfer to adult-onset disease.
- **QoL data absent:** no ES-specific EQ-5D/SF-36/PROMIS evidence was identified.
- **Epigenetics unstudied:** no ES-specific methylation/histone or single-cell/spatial multi-omics signature was found in the reviewed literature.
- **Primary/idiopathic ES mechanism inferred:** for the large fraction lacking an identified gene, the tolerance-defect chain is extrapolated from monogenic cases, not directly demonstrated.
- **Two citation snippets were flagged "mismatch"** in the knowledge state (PMID 37008642, 41608120 — title-based); their claims (canine ES; murine ALPS + leniolisib) are corroborated by companion verified citations but should be re-verified against full text.
- **Treatment evidence** is largely from cohorts, single-arm trials, and case reports; randomized comparative data are scarce given rarity.

## Proposed Follow-up Experiments / Actions

1. **Systematic genomic testing study** stratified by age of onset to define IEI yield thresholds and cost-effectiveness of WES/WGS in adult vs pediatric ES.
2. **Prospective biomarker panel** (DNT cells, sFASL, ANA titer, IL-10, immunoglobulins) to build a validated risk-stratification model for SLE progression, malignancy, and mortality.
3. **Genotype-stratified therapeutic trials** matching targeted agents to mechanism (abatacept for CTLA4/LRBA; leniolisib for APDS; JAK inhibitors for interferonopathy-like dysregulation).
4. **Single-cell and spatial immune profiling** of spleen/marrow/blood to map the autoreactive B-cell and DNT-cell compartments and identify novel targets.
5. **ES-specific QoL/PRO instrument development** and longitudinal capture within existing registries (OBS'CEREVANCE, Danish).
6. **Comparative canine studies** leveraging naturally occurring canine ES as a translational large-animal model for therapeutics.

---

*Report compiled from 9 confirmed findings and 34 reviewed papers across 5 investigation iterations. Evidence source types: predominantly human clinical (national cohorts, registries, case series), with model-organism (Fas^lpr/gld mouse) and natural-disease (canine) corroboration.*


## Artifacts

- [OpenScientist final report](Evans_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Evans_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31983745
2. PMID:21228033
3. PMID:41560547
4. PMID:37792884
5. PMID:37646304
6. PMID:33440924
7. PMID:26484337
8. PMID:28444729
9. PMID:26504182
10. PMID:38227934
11. PMID:31292991
12. PMID:32271826
13. PMID:22157362
14. PMID:38700373
15. PMID:31432443
16. PMID:19411652
17. PMID:41608120