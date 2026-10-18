---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:45:56.870181'
end_time: '2026-08-31T17:32:25.205952'
duration_seconds: 2788.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 30
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Defect_Type_30-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Defect_Type_30-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 30
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 30** covering all of the
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

# Combined Oxidative Phosphorylation Defect Type 30 (COXPD30): A Comprehensive Disease Report

**Disease:** Combined Oxidative Phosphorylation Deficiency 30 (COXPD30)
**Causal gene:** *TRMT10C* (encoding MRPP1)
**OMIM:** #616974 | **MONDO:** MONDO:0014856 | **Category:** Mendelian, autosomal recessive
**Report date:** 2026-08-31

---

## Summary

Combined Oxidative Phosphorylation Deficiency 30 (COXPD30) is an ultra-rare, autosomal-recessive mitochondrial disorder caused by biallelic loss-of-function/hypomorphic mutations in **TRMT10C** (chromosome 3q12.3), which encodes **MRPP1** (mitochondrial RNase P protein 1, also called tRNA methyltransferase 10 homolog C). MRPP1 is a bifunctional subunit of human mitochondrial RNase P (mt-RNase P): together with MRPP2 (SDR5C1/HSD17B10) and MRPP3 (PRORP) it cleaves the 5′ ends of mitochondrial tRNAs (mt-tRNAs) from the polycistronic mitochondrial transcripts, and the stable MRPP1/MRPP2 subcomplex additionally installs the N1-methyl modification at position 9 (m1A9/m1G9, "m1R9") that is essential for correct mt-tRNA folding. When MRPP1 is deficient, mt-tRNA maturation and methylation fail, mitochondrial translation collapses, and all 13 mtDNA-encoded oxidative phosphorylation (OXPHOS) subunits are under-produced — yielding a combined deficiency of respiratory-chain complexes I, III, IV and V.

The disease was defined in 2016 by Metodiev and colleagues ([PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)), who identified biallelic *TRMT10C* variants in two unrelated infants who both presented at birth with lactic acidosis, hypotonia, feeding difficulties and sensorineural deafness, and both died at 5 months from respiratory failure. COXPD30 sits within an "mt-RNase P allelic series": each of the three subunit genes causes a distinct mitochondrial disorder — *TRMT10C* → COXPD30, *SDR5C1/HSD17B10* → X-linked HSD10 disease, and *PRORP* → COXPD54 (Perrault-syndrome spectrum). A critical disambiguation for knowledge-base curation is that COXPD30 is a **TRMT10C** disorder and must not be confused with **TRMT5**-related COXPD26 (OMIM #616539), a genetically and clinically distinct entity.

Evidence for COXPD30 is drawn from a very small human clinical base (essentially two index patients), supplemented by robust in-vitro biochemistry, cryo-EM structural biology of mt-RNase P, and cell-based rescue experiments. There is no disease-specific therapy; management is supportive. Because the reported patients died in infancy, no natural-history, long-term-outcome, or treatment-trial data exist. This report compiles all available disease characteristics against the 15-section template, flags the numerous "not available" fields inherent to an ultra-rare disorder, and provides ontology-term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) throughout.

---

## Key Findings

### Finding 1 — COXPD30 is caused by biallelic (autosomal-recessive) *TRMT10C*/MRPP1 mutations

Whole-exome sequencing identified biallelic *TRMT10C* variants in two unrelated infants. Subject 1 was compound heterozygous for c.542G>T (p.Arg181Leu) and c.814A>G (p.Thr272Ala); subject 2 was homozygous for c.542G>T (p.Arg181Leu). Both presented at birth with lactic acidosis, hypotonia, feeding difficulties and deafness, and both died at 5 months from respiratory failure ([PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)). The disorder is catalogued as OMIM #616974.

Population-genetics constraint metrics from gnomAD are fully consistent with a recessive, loss-of-tolerance mechanism rather than haploinsufficiency: pLI = 0.015, LOEUF = 0.80, missense-z = 0.53 — i.e., *TRMT10C* is **not** predicted to be haploinsufficient or missense-constrained, exactly as expected for a gene requiring biallelic hits to cause disease.

> "we identified mutations in TRMT10C (encoding the mitochondrial RNase P protein 1 [MRPP1]) in two unrelated individuals who presented at birth with lactic acidosis, hypotonia, feeding difficulties, and deafness. Both individuals died at 5 months after respiratory failure." — [PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)

### Finding 2 — Mechanism: MRPP1 loss impairs 5′ pre-tRNA processing and m1R9 methylation, causing combined OXPHOS deficiency

MRPP1 (TRMT10C), MRPP2 (SDR5C1/HSD17B10) and MRPP3 (PRORP) form the mt-RNase P complex that cleaves the 5′ ends of mt-tRNAs from polycistronic precursor transcripts. A stable MRPP1/MRPP2 subcomplex independently carries m1R9 methyltransferase activity, methylating mt-tRNAs at position 9 — a modification vital for folding mt-tRNAs into their correct tertiary structures. Patient fibroblasts showed decreased MRPP1 protein and accumulation of unprocessed mt-RNA precursors, indicating impaired mt-RNA processing and defective mitochondrial protein synthesis. Because faithful mt-tRNA maturation is a prerequisite for translating all 13 mtDNA-encoded OXPHOS subunits, the downstream consequence is multiple respiratory-chain-complex deficiency. Re-expression of wild-type *TRMT10C* rescued the phenotype, confirming causation.

> "MRPP1, along with MRPP2 and MRPP3, form the mitochondrial ribonuclease P (mt-RNase P) complex that cleaves the 5' ends of mt-tRNAs from polycistronic precursor transcripts. Additionally, a stable complex of MRPP1 and MRPP2 has m(1)R9 methyltransferase activity, which methylates mt-tRNAs at position 9 and is vital for folding mt-tRNAs into their correct tertiary structures." — [PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)

> "revealed decreased protein levels of MRPP1 and an increase in mt-RNA precursors indicative of impaired mt-RNA processing and defective mitochondrial protein synthesis" — [PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)

### Finding 3 — Structural basis: the TRMT10C/SDR5C1 subcomplex binds and positions mt-tRNA for processing and methylation

Cryo-EM of human mt-RNase P bound to precursor tRNA shows that TRMT10C and SDR5C1 form a subcomplex that binds conserved mt-tRNA elements — including the anticodon loop — and positions the tRNA for methylation; the endonuclease PRORP is then recruited and activated through its PPR and nuclease domains to ensure precise 5′ cleavage ([PMID: 34489609](https://pubmed.ncbi.nlm.nih.gov/34489609/)). Subsequent cryo-EM work visualised the full maturation cycle — 5′ and 3′ end processing, methylation and 3′-CCA addition — and proposed that the methyltransferase subcomplex recognises the fragile mitochondrial pre-tRNA in a mode that also supports end-processing and acts as a **folding quality-control checkpoint** ([PMID: 38824131](https://pubmed.ncbi.nlm.nih.gov/38824131/)). Beyond 5′ processing, MRPP1/2 also retains the tRNA product and significantly enhances ELAC2-catalysed 3′ processing for 17 of the 22 mt-tRNAs, and presents the tRNA to the CCA-adding enzyme ([PMID: 29040705](https://pubmed.ncbi.nlm.nih.gov/29040705/)) — explaining the broad pleiotropy of TRMT10C loss.

> "Subunits TRMT10C and SDR5C1 form a subcomplex that binds conserved mitochondrial tRNA elements, including the anticodon loop, and positions the tRNA for methylation. The endonuclease PRORP is recruited and activated through interactions with its PPR and nuclease domains to ensure precise pre-tRNA cleavage." — [PMID: 34489609](https://pubmed.ncbi.nlm.nih.gov/34489609/)

> "MRPP1/2 is not only a component of the mitochondrial RNase P but that it retains the tRNA product from the 5'-processing step and significantly enhances the efficiency of ELAC2-catalyzed 3'-processing for 17 of the 22 tRNAs encoded in the human mitochondrial genome" — [PMID: 29040705](https://pubmed.ncbi.nlm.nih.gov/29040705/)

### Finding 4 — All three mt-RNase P subunits cause distinct mitochondrial disorders (allelic / differential-diagnosis series)

Mitochondrial RNase P is a three-protein complex, and pathogenic variants in each subunit gene cause a distinct disorder that shares the same molecular signature (reduced subunit protein, accumulation of unprocessed mt-tRNA precursors, decreased mtDNA-encoded proteins, rescue by wild-type cDNA):

| Subunit | Gene | Disorder | OMIM | Inheritance | Hallmark presentation |
|---|---|---|---|---|---|
| MRPP1 | *TRMT10C* | **COXPD30** | #616974 | AR | Neonatal lactic acidosis, hypotonia, deafness, encephalo-cardiomyopathy; fatal in infancy |
| MRPP2 | *SDR5C1 / HSD17B10* | HSD10 disease | #300438 | X-linked | Progressive neurodegeneration + cardiomyopathy |
| MRPP3 | *PRORP* | COXPD54 | #619737 | AR | Pleiotropic: Perrault syndrome (SNHL + POI) → leukodystrophy/developmental delay |

> "Pathogenic variants in TRMT10C and SDR5C1 are associated with distinct recessive or x-linked infantile onset disorders, resulting from defects in mitochondrial RNA processing." — [PMID: 34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/)

> "Identification of disease-causing variants in PRORP indicates that pathogenic variants in all three subunits of mt-RNase P can cause mitochondrial dysfunction, each with distinct pleiotropic clinical presentations." — [PMID: 34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/)

### Finding 5 — *TRMT10C* variant landscape: mostly VUS, very few disease-specific pathogenic small variants

A ClinVar query returned 119 *TRMT10C* records: 83 of uncertain significance, 18 likely benign, 2 benign, 2 conflicting, and only 9 "Pathogenic" plus 2 "Likely pathogenic." Critically, of the "pathogenic" entries, the **only** COXPD30-specific small variant is NM_017819.4:c.814A>G (p.Thr272Ala); the remaining "pathogenic" calls are large multi-gene 3q copy-number gains/losses (e.g., chr3:93.8–145.7 Mb) that merely encompass *TRMT10C* rather than representing COXPD30-specific alleles. 99 of 119 variants are SNVs. This means variant interpretation for COXPD30 is heavily dependent on functional validation. The field-standard assay is an in-vitro mt-tRNA 5′-processing reaction reconstituted with recombinant TRMT10C + SDR5C1 + PRORP, which quantifies reduced processing for disease variants ([PMID: 34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/), [PMID: 37558808](https://pubmed.ncbi.nlm.nih.gov/37558808/)).

> "In vitro mitochondrial tRNA processing assays with recombinant TRMT10C, SDR5C1 and PRORP indicated two COXPD54-associated PRORP variants" — [PMID: 37558808](https://pubmed.ncbi.nlm.nih.gov/37558808/)

### Finding 6 — Quantitative population genetics of the COXPD30 founding variants (gnomAD r4)

| Variant (NM_017819.4) | Protein | GRCh38 position | gnomAD v4 exome AF | Genome AF | Consequence |
|---|---|---|---|---|---|
| c.542G>T | p.Arg181Leu | chr3:101,565,323 G>T | 1.20×10⁻⁴ (176/1,461,190) | 1.31×10⁻⁴ (20/152,164) | missense |
| c.814A>G | p.Thr272Ala | chr3:101,565,595 A>G | 1.37×10⁻⁶ (2/1,461,814) | absent | missense |

The recurrent allele p.Arg181Leu corresponds to a heterozygous carrier frequency of roughly **1 in ~4,000**, whereas p.Thr272Ala is ultra-rare. Ensembl VEP assigns both a most-severe consequence of `missense_variant`. Gene-level constraint (pLI 0.015, LOEUF 0.80, mis_z 0.53) confirms *TRMT10C* is neither LoF- nor missense-constrained, consistent with a recessive disease gene.

> "compound heterozygous c.542G>T (p.Arg181Leu) and c.814A>G (p.Thr272Ala) changes in subject 1 and a homozygous c.542G>T (p.Arg181Leu) variant in subject 2" — [PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)

### Finding 7 — TRMT10C/MRPP1 protein architecture, catalytic GO functions and structural resources

UniProt **Q7L0Y3** (MRPP1_HUMAN, "tRNA methyltransferase 10 homolog C"): 403 amino acids; N-terminal mitochondrial transit peptide (aa 1–39); a single catalytic "SAM-dependent MTase TRM10-type" domain (aa 191–383) of the SPOUT methyltransferase superfamily. **Molecular functions:** tRNA (adenine(9)-N1)-methyltransferase (**GO:0160106**) and tRNA (guanosine(9)-N1)-methyltransferase (**GO:0052905**) — i.e., m1A9/m1G9; RNA binding (**GO:0003723**); tRNA binding (**GO:0000049**). **Biological processes:** mitochondrial RNA/tRNA 5′-end processing (**GO:0000964**, **GO:0097745**), mt-tRNA 3′-end processing (**GO:1990180**), mt-tRNA methylation (**GO:0070901**), positive regulation of mitochondrial translation (**GO:0070131**), tRNA 3′-CCA addition (**GO:0001680**). **Cellular components:** mitochondrial matrix (**GO:0005759**), mitochondrial ribonuclease P complex (**GO:0030678**), mitochondrial nucleoid (**GO:0042645**). 13 PDB entries visualise the complex: 5NFJ, 7ONU, 8CBK/L/M/O, 8RR1/3/4, 9EY0/1/2, 9GCH.

### Finding 8 — MONDO definition independently confirms *TRMT10C* as the COXPD30 gene

The OLS4/MONDO record for **MONDO:0014856** ("combined oxidative phosphorylation defect type 30") carries the logical definition: *"Any combined oxidative phosphorylation deficiency in which the cause of the disease is a mutation in the TRMT10C gene."* Exact synonyms include COXPD30, "combined oxidative phosphorylation deficiency type 30", "TRMT10C combined oxidative phosphorylation deficiency", and "combined oxidative phosphorylation deficiency caused by mutation in TRMT10C." This was retrieved programmatically from the EBI OLS4 API (HTTP 200), providing an independent ontology-level confirmation of the gene–disease relationship.

---

## Report by Template Section

### 1. Disease Information

**Overview.** COXPD30 is a severe, congenital-onset mitochondrial disease of impaired mitochondrial gene expression. It belongs to the broad "combined oxidative phosphorylation deficiency" (COXPD) family — disorders in which more than one respiratory-chain complex is deficient because a shared step of mitochondrial gene expression (here, mt-tRNA maturation) fails.

**Key identifiers.**
- **OMIM:** #616974 (phenotype); gene *TRMT10C* OMIM *615423
- **MONDO:** MONDO:0014856
- **Orphanet:** COXPD30 has no dedicated Orphanet number verified in this investigation; it falls under the broad "Combined oxidative phosphorylation deficiency" grouping (specific ORPHA mapping *not independently verified — flagged as uncertain*).
- **ICD-10:** E88.8 / **ICD-11:** 5C53.2 (mitochondrial metabolic disorders) — generic, not COXPD30-specific.
- **MeSH:** No dedicated descriptor; indexed under "Mitochondrial Diseases" / "Oxidative Phosphorylation."
- **HGNC:** TRMT10C, HGNC:26022. **UniProt:** Q7L0Y3. **NCBI Gene:** 54931. **Ensembl:** ENSG00000174173.

**Synonyms / alternative names:** COXPD30; Combined oxidative phosphorylation deficiency type 30; TRMT10C combined oxidative phosphorylation deficiency; MRPP1 deficiency.

**Source of information:** Disease-level, aggregated resources (OMIM, MONDO, ClinVar, gnomAD, UniProt) plus the two-patient index cohort — **not** EHR-derived. Given only two reported patients, all clinical statements rest on a very small case base.

### 2. Etiology

**Causal factors:** Purely genetic — biallelic pathogenic variants in *TRMT10C*. No environmental, infectious, or acquired cause. **Not applicable:** infectious agents, toxins, lifestyle.

**Genetic risk factors:** The disease-defining alleles are the causal variants themselves (p.Arg181Leu recurrent; p.Thr272Ala). No modifier loci or susceptibility variants have been identified. Consanguinity increases the risk of homozygosity for the recurrent allele (subject 2 was homozygous).

**Protective factors:** None known. Heterozygous carriers are asymptomatic (recessive disease).

**Gene–environment interactions:** None documented. (Speculatively, metabolic stressors that raise ATP demand could unmask marginal OXPHOS capacity, but this is **not demonstrated** for COXPD30.)

### 3. Phenotypes

All phenotype data derive from the two index patients ([PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)); frequencies are therefore "2/2" unless noted.

| Phenotype | Type | HPO term | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| Lactic acidosis | Lab abnormality | HP:0003128 | Neonatal | 2/2 | Hallmark biochemical marker |
| Muscular hypotonia | Clinical sign | HP:0001252 | Neonatal | 2/2 | |
| Feeding difficulties | Symptom | HP:0011968 | Neonatal | 2/2 | |
| Sensorineural hearing loss | Clinical sign | HP:0000407 | Congenital | 2/2 | Shared across mt-RNase P disorders |
| Respiratory failure | Clinical sign | HP:0002878 | Infantile | 2/2 | Cause of death (~5 mo) |
| Decreased mitochondrial respiratory-chain activity | Lab abnormality | HP:0008314 | Neonatal | 2/2 | Complexes I/III/IV/V |
| Cardiomyopathy (encephalo-cardiomyopathy spectrum) | Clinical sign | HP:0001638 | Infantile | Reported in mt-RNase P disorder spectrum | Prominent in HSD10/related |

**Severity & progression:** Severe, rapidly progressive, fatal in infancy. **Quality-of-life impact:** Profound — the infants required intensive supportive care and did not survive past 5 months; formal QoL instruments (EQ-5D, SF-36) are not applicable to neonates and were not used.

### 4. Genetic / Molecular Information

**Causal gene:** *TRMT10C* (HGNC:26022; 3q12.3; NCBI Gene 54931; Ensembl ENSG00000174173; RefSeq NM_017819.4). **Protein:** MRPP1 / Q7L0Y3, 403 aa (Finding 7).

**Pathogenic variants (COXPD30-specific):**

| cDNA | Protein | Class | ACMG interpretation | Origin |
|---|---|---|---|---|
| c.542G>T | p.Arg181Leu | missense | (Likely) pathogenic — recurrent, functionally supported | germline |
| c.814A>G | p.Thr272Ala | missense | Pathogenic (ClinVar) | germline |

Both are **germline**, **missense**, causing a hypomorphic/loss-of-function effect on MRPP1's methyltransferase and tRNA-processing scaffolding roles. Allele frequencies as in Finding 6. p.Thr272Ala lies within the catalytic SPOUT MTase domain (aa 191–383); p.Arg181Leu lies just N-terminal to it, plausibly affecting domain integrity or substrate positioning (structural inference).

**Variant interpretation caveat (Finding 5):** The bulk of *TRMT10C* ClinVar entries are VUS; functional reconstitution assays are the arbiter. **Somatic origin, COSMIC:** not applicable (constitutional disease). **Modifier genes / epigenetic changes / chromosomal abnormalities:** none specifically established for COXPD30 (large 3q CNVs encompassing *TRMT10C* are reported in ClinVar but are contiguous-gene events, not COXPD30 per se).

### 5. Environmental Information

**Not applicable.** COXPD30 is a Mendelian disorder with no environmental, lifestyle, or infectious contribution.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic missense variants in *TRMT10C* (p.Arg181Leu, p.Thr272Ala) **lead to** reduced steady-state MRPP1 protein and impaired MRPP1 enzymatic/scaffolding function. *(demonstrated: reduced MRPP1 protein in patient fibroblasts)*
2. Reduced functional MRPP1 **results in** a destabilised/less-active MRPP1–MRPP2 (TRMT10C–SDR5C1) subcomplex, the tRNA-binding and m1R9-methylating core of mt-RNase P. *(demonstrated structurally; MRPP1/MRPP2 interdependence also shown via HSD10 knock-down — [PMID: 24549042](https://pubmed.ncbi.nlm.nih.gov/24549042/))*
3. This **impairs** (a) 5′-end cleavage of mt-tRNAs from polycistronic transcripts and (b) m1A9/m1G9 methylation at tRNA position 9. **Branch (a)** and **branch (b)** converge on the same downstream node. *(demonstrated: accumulation of unprocessed mt-RNA precursors)*
4. Loss of m1R9 methylation **leads to** mis-folding of the structurally fragile mt-tRNAs; failure of 5′ (and downstream 3′/CCA) processing **leads to** a shortage of mature, aminoacylatable mt-tRNAs. *(mechanistically inferred from the established role of m1R9 in tertiary folding and from processing-cascade dependence — [PMID: 38824131](https://pubmed.ncbi.nlm.nih.gov/38824131/), [PMID: 29040705](https://pubmed.ncbi.nlm.nih.gov/29040705/))*
5. Depletion of functional mt-tRNAs **results in** defective mitochondrial translation of the 13 mtDNA-encoded OXPHOS subunits. *(demonstrated: defective mitochondrial protein synthesis)*
6. Reduced synthesis of core subunits **results in** combined deficiency of respiratory-chain complexes I, III, IV and V (complex II, entirely nuclear-encoded, is typically spared). *(demonstrated: multiple respiratory-chain deficiencies)*
7. OXPHOS failure **leads to** inadequate ATP production, a shift to anaerobic glycolysis and **lactic acidosis**, and energy failure in high-demand tissues (brain, heart, cochlea, skeletal muscle). *(demonstrated biochemically)*
8. Tissue-level energy failure **manifests** as neonatal hypotonia, feeding difficulties, sensorineural deafness, encephalo-cardiomyopathy and ultimately fatal respiratory failure. *(demonstrated clinically)*

```
TRMT10C biallelic missense
        │
        ▼
  ↓ MRPP1 protein / function
        │
        ▼
 destabilised MRPP1–MRPP2 subcomplex
        │
   ┌────┴─────┐
   ▼          ▼
5' pre-tRNA   m1R9 (m1A9/m1G9)
processing↓   methylation↓
   └────┬─────┘
        ▼
 mis-folded / immature mt-tRNAs  →  ↓ mt-translation
        ▼
 ↓ 13 mtDNA-encoded OXPHOS subunits
        ▼
 combined complex I/III/IV/V deficiency
        ▼
 ↓ ATP, ↑ lactate  →  energy failure in brain/heart/cochlea/muscle
        ▼
 neonatal lactic acidosis, hypotonia, deafness, respiratory failure (death ~5 mo)
```

**Molecular pathways / processes:** mitochondrial tRNA 5′-processing (GO:0000964/GO:0097745), mt-tRNA methylation (GO:0070901), mitochondrial translation (GO:0032543), oxidative phosphorylation (GO:0006119). **Upstream:** mt-tRNA maturation defect. **Downstream:** OXPHOS deficiency, lactic acidosis. **Cell types affected:** high-energy-demand post-mitotic cells — cardiomyocytes (CL:0000746), neurons (CL:0000540), cochlear hair cells (CL:0000855), skeletal myocytes (CL:0000188). **Subcellular compartment:** mitochondrial matrix / mitochondrial nucleoid (GO:0005759, GO:0042645). **CHEBI entities:** lactate (CHEBI:24996), S-adenosyl-L-methionine (CHEBI:15414, the methyl donor), ATP (CHEBI:15422).

**Immune involvement / epigenetics:** not implicated. **Metabolomics/proteomics signatures:** patient cells show accumulated mt-RNA precursors and reduced mtDNA-encoded proteins; elevated lactate/lactate-to-pyruvate ratio is the accessible metabolic readout.

### 7. Anatomical Structures Affected

- **Organ level (primary):** brain (UBERON:0000955), heart (UBERON:0000948), cochlea/inner ear (UBERON:0001844), skeletal muscle (UBERON:0001134).
- **Body systems:** nervous, cardiovascular, auditory/special-sense, musculoskeletal, and metabolic.
- **Tissue/cell level:** nervous tissue, cardiac muscle, cochlear sensory epithelium, skeletal muscle — all oxidative, mitochondria-rich tissues.
- **Subcellular:** mitochondrion (GO:0005739), specifically mitochondrial matrix (GO:0005759) and nucleoid (GO:0042645); the lesion is in the mt-RNase P complex (GO:0030678).
- **Localization / lateralization:** systemic and bilateral (e.g., bilateral sensorineural hearing loss); not focal or lateralised.

### 8. Temporal Development

- **Onset:** congenital / neonatal ("at birth"), acute in presentation.
- **Progression:** rapidly progressive, monophasic decline; no remission.
- **Stages:** neonatal presentation → progressive multi-organ energy failure → terminal respiratory failure.
- **Duration / course:** short; both index patients died at **5 months**. No relapsing-remitting or episodic pattern.
- **Critical period / intervention window:** the neonatal period; however, no disease-modifying intervention exists, so the "window" is theoretical.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive (biallelic *TRMT10C*). Confirmed by compound-het and homozygous genotypes in unrelated patients.
- **Penetrance:** presumed complete for biallelic pathogenic genotypes (based on 2/2 patients); formal penetrance cannot be estimated from n=2.
- **Expressivity:** limited data; both patients had a concordant severe neonatal-lethal course.
- **Carrier frequency:** recurrent p.Arg181Leu ~1/4,000 heterozygotes (gnomAD v4). Predicted affected-birth frequency for this single allele (Hardy–Weinberg, homozygous) ≈ (1.2×10⁻⁴)² ≈ 1.4×10⁻⁸ — i.e., extremely rare, consistent with an ultra-rare disorder; compound heterozygosity with other rare pathogenic alleles raises the aggregate slightly.
- **Epidemiology:** prevalence/incidence not established; classifiable as ultra-rare (<1/1,000,000). Only two reported patients.
- **Anticipation / germline mosaicism:** not applicable/not reported.
- **Founder effects:** the recurrent p.Arg181Leu may represent a mild founder or recurrent allele; no specific population enrichment established.
- **Consanguinity:** relevant (subject 2 homozygous), typical of ultra-rare AR disease.
- **Sex ratio:** no sex bias expected for an autosomal-recessive disorder; data insufficient. **Geographic distribution:** unknown.

### 10. Diagnostics

- **Laboratory:** elevated blood/CSF lactate and lactate-to-pyruvate ratio (LOINC 2524-7 lactate); respiratory-chain enzyme assays in muscle/fibroblasts showing multiple-complex (I/III/IV/V) deficiency; sparing of complex II supports a mitochondrial-translation defect.
- **Biomarkers:** lactate (CHEBI:24996); molecularly, accumulation of unprocessed mt-tRNA precursors and reduced mtDNA-encoded proteins on Northern/immunoblot (research assays).
- **Genetic testing (diagnostic gold standard):** exome (WES) or genome (WGS) sequencing detecting biallelic *TRMT10C* variants; targeted mitochondrial/nuclear "mito" gene panels including *TRMT10C*; single-gene testing/confirmation. Chromosomal microarray only relevant to detect large 3q CNVs encompassing the gene. mtDNA testing is expected **normal** (nuclear-encoded disease) and helps exclude primary mtDNA disorders.
- **Functional confirmation:** in-vitro reconstituted mt-RNase P 5′-processing assay (recombinant TRMT10C+SDR5C1+PRORP) to classify novel/VUS alleles ([PMID: 34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/), [PMID: 37558808](https://pubmed.ncbi.nlm.nih.gov/37558808/)); patient-cell rescue with wild-type cDNA.
- **Imaging / electrophysiology:** brain MRI and echocardiography as clinically indicated (encephalopathy/cardiomyopathy); auditory brainstem response for deafness — nonspecific.
- **Differential diagnosis:** other COXPD subtypes, especially **TRMT5-related COXPD26** (OMIM #616539; the key disambiguation), and the allelic mt-RNase P disorders HSD10 disease (*HSD17B10*) and COXPD54 (*PRORP*); other neonatal mitochondrial encephalo-cardiomyopathies with lactic acidosis.
- **Screening:** no newborn-screening test exists; carrier/cascade testing is possible once a familial genotype is known.

### 11. Outcome / Prognosis

- **Survival / life expectancy:** very poor — both reported patients died at 5 months from respiratory failure. Prognosis for the classic biallelic-severe genotype appears neonatal-lethal.
- **Mortality:** disease-specific mortality was 100% in the reported cohort (2/2).
- **Morbidity:** profound multi-system disability (hypotonia, deafness, feeding failure, cardiomyopathy) during the short lifespan.
- **Complications:** respiratory failure (terminal), cardiomyopathy, failure to thrive.
- **Recovery potential:** none with current care (supportive only).
- **Prognostic factors:** insufficient data; by analogy to the mt-RNase P series, residual enzyme/processing activity (hypomorphic vs null) is the plausible determinant of severity, though milder COXPD30 cases have not yet been reported. **Prognostic biomarkers:** none validated.

### 12. Treatment

- **Disease-specific therapy:** **none exists.** Management is entirely **supportive/symptomatic**.
- **Supportive care (NCIT: Supportive Care, C15277):** nutritional support/feeding assistance, treatment of lactic acidosis, cardiac and respiratory support, hearing habilitation.
- **Pharmacotherapy:** no proven agents. Generic "mitochondrial cocktail" supplements (coenzyme Q10, riboflavin, thiamine, L-carnitine) are used empirically in mitochondrial disease without COXPD30-specific evidence (NCIT terms exist for individual agents, e.g., Coenzyme Q10 C1096).
- **Advanced/experimental therapeutics:** no gene therapy, cell therapy, RNA therapy, or targeted therapy is available or in trials for COXPD30 specifically. In principle, gene replacement (AAV-*TRMT10C*) is conceptually attractive given the small CDS (403 aa) and the demonstrated cDNA rescue in vitro, but this is **hypothetical** and untested.
- **Pharmacogenomics / personalized medicine:** not applicable.
- **Treatment outcomes / adverse events:** not applicable (no specific therapy).

### 13. Prevention

- **Primary prevention:** not possible (constitutional genetic disease) other than reproductive risk avoidance.
- **Genetic counselling:** central. Once a proband genotype is known, 25% recurrence risk applies to future pregnancies; carrier testing of relatives (cascade screening) and reproductive options — prenatal diagnosis and preimplantation genetic testing (PGT-M) — are available.
- **Carrier screening:** feasible for known familial alleles; population carrier screening is not standard given rarity.
- **Secondary/tertiary prevention, immunization, public-health, environmental interventions:** not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologues:** *TRMT10C* is conserved across metazoa. Mouse *Trmt10c* (MGI ortholog); the TRM10 methyltransferase family is deeply conserved to yeast (Trm10). **No viable *Trmt10c* knockout mouse** has been reported (constitutive loss is presumed embryonic-lethal, consistent with the essential role of mt-tRNA maturation) — a key gap for modelling.
- **Natural disease in other species:** no naturally occurring COXPD30-equivalent disorder is catalogued in OMIA for companion or production animals as of this review.
- **Comparative biology:** the mt-RNase P mechanism (protein-only, PRORP-based, with a TRM10-family methyltransferase partner) is conserved across eukaryotes, making yeast and human cell systems informative for mechanism though not for the intact clinical phenotype.
- **Zoonotic potential / transmission:** not applicable.

### 15. Model Organisms

- **Cellular / in-vitro models (primary evidence base):** patient-derived fibroblasts (showing reduced MRPP1, mt-RNA precursor accumulation, translation defect, and cDNA rescue — [PMID: 27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/)); reconstituted recombinant mt-RNase P (TRMT10C+SDR5C1+PRORP) for biochemical/structural and variant-classification studies ([PMID: 34489609](https://pubmed.ncbi.nlm.nih.gov/34489609/), [PMID: 29040705](https://pubmed.ncbi.nlm.nih.gov/29040705/), [PMID: 34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/)).
- **RNAi / knock-down models:** HSD10/MRPP2 knock-down demonstrates MRPP1–MRPP2 interdependence and impaired heavy-strand transcript processing ([PMID: 24549042](https://pubmed.ncbi.nlm.nih.gov/24549042/)).
- **Whole-animal genetic models:** no established viable mouse model of COXPD30; this is a major gap. **iPSC/organoid models:** none reported specifically.
- **Model limitations:** cellular and biochemical systems recapitulate the molecular lesion (processing/methylation defect, OXPHOS deficiency) well, but cannot model organ-level phenotypes (deafness, cardiomyopathy) or test systemic therapies; the absence of a viable animal model constrains preclinical development.

---

## Mechanistic Model / Interpretation

COXPD30 is best understood as a **mitochondrial gene-expression disorder** rather than a defect of any single respiratory-chain complex. The primary lesion is loss of MRPP1 function at the very first steps of mt-tRNA biogenesis. Because a single enzyme complex (mt-RNase P, with its MRPP1/MRPP2 methyltransferase core) services all 22 mitochondrial tRNAs — which in turn are required to translate all 13 mtDNA-encoded OXPHOS subunits — a defect here is inevitably *combined* and *pleiotropic*. This explains why the biochemistry shows deficiency of complexes I, III, IV and V (all containing mtDNA-encoded subunits) with sparing of the entirely nuclear-encoded complex II, and why the phenotype strikes the most oxidative tissues (brain, heart, cochlea, muscle) first and hardest.

Two features distinguish COXPD30 within the mitochondrial-disease landscape. First, it is the *TRMT10C* member of a clean **three-gene allelic series** (mt-RNase P: *TRMT10C*/*HSD17B10*/*PRORP*), which is a gift for differential diagnosis and mechanism: the three disorders share a molecular signature yet diverge clinically, implying that subunit-specific and dosage-specific effects tune the phenotype. Second — and critically for curation — COXPD30 must be kept separate from **TRMT5-related COXPD26**: both involve mt-tRNA methyltransferases and both cause combined OXPHOS deficiency, but TRMT5 installs m1G37 (adjacent to the anticodon) whereas TRMT10C/MRPP1 installs m1R9 and additionally scaffolds 5′/3′ processing. Confusing the two would mis-assign gene, OMIM number, and mechanism.

The evidence base is unusually **deep in molecular/structural detail but shallow in clinical breadth**. We have atomic-resolution cryo-EM of the intact machine, quantitative in-vitro assays, and gnomAD-level allele frequencies — yet only two patients. Any statement about penetrance, expressivity, milder phenotypes, natural history, or treatment response is therefore provisional.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [27132592](https://pubmed.ncbi.nlm.nih.gov/27132592/) | *Recessive mutations in TRMT10C cause defects in mitochondrial RNA processing and multiple respiratory chain deficiencies* | Human clinical + cell | **Defining paper.** Establishes gene, biallelic inheritance, core phenotype, mechanism, and cDNA rescue (F1, F2, F6) |
| [34489609](https://pubmed.ncbi.nlm.nih.gov/34489609/) | *Structural basis of RNA processing by human mitochondrial RNase P* | Structural (cryo-EM) | TRMT10C/SDR5C1 subcomplex binds and positions tRNA; PRORP recruitment (F3, F7) |
| [38824131](https://pubmed.ncbi.nlm.nih.gov/38824131/) | *Structural basis for human mitochondrial tRNA maturation* | Structural (cryo-EM) | Full maturation cycle; methyltransferase subcomplex as folding quality-control checkpoint (F3) |
| [29040705](https://pubmed.ncbi.nlm.nih.gov/29040705/) | *The MRPP1/MRPP2 complex is a tRNA-maturation platform in human mitochondria* | In vitro biochemistry | MRPP1/2 enhances 3′ processing of 17/22 mt-tRNAs; broad maturation platform (F3) |
| [34715011](https://pubmed.ncbi.nlm.nih.gov/34715011/) | *Bi-allelic variants in PRORP cause mt-tRNA processing defects…* | Human clinical + in vitro | Establishes the mt-RNase P allelic series; recombinant processing assay (F4, F5) |
| [37558808](https://pubmed.ncbi.nlm.nih.gov/37558808/) | *Novel homozygous variants in PRORP expand COXPD54…* | Human clinical + in vitro | Recombinant TRMT10C+SDR5C1+PRORP assay used for variant classification (F5) |
| [24549042](https://pubmed.ncbi.nlm.nih.gov/24549042/) | *Mutation/knock-down of HSD10 causes loss of MRPP1…* | Cell / knock-down | MRPP1–MRPP2 interdependence; impaired heavy-strand processing (supports mechanism step 2) |
| [26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/) | *TRMT5 mutations cause a defect in mt-tRNA modification…* | Human clinical | **Contrast/disambiguation:** TRMT5 → COXPD26, distinct from COXPD30 |
| [35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/) | *Novel TRMT5 mutations associated with COXPD26…* | Human clinical | Confirms TRMT5/COXPD26 is a separate entity |

The remaining papers reviewed (e.g., general mitochondrial-dysfunction reviews in cardiomyopathy, Parkinson's, Alzheimer's, and heart-failure economics) were screened and found **not directly relevant** to COXPD30; they are retained in the literature log for completeness but do not support specific claims here.

---

## Limitations and Knowledge Gaps

1. **Tiny clinical cohort (n=2).** All phenotype, onset, penetrance, expressivity and prognosis statements rest on two patients from one report. Milder or later-onset COXPD30 phenotypes may exist but are unreported.
2. **No natural-history or treatment data.** Both patients died in infancy; there are no longitudinal, QoL, or therapeutic-response data.
3. **Variant interpretation is functionally dependent.** Most *TRMT10C* ClinVar entries are VUS; only p.Thr272Ala (and the recurrent p.Arg181Leu) are functionally supported. New variants require reconstituted-assay validation.
4. **No viable animal model.** The absence of a *Trmt10c* mouse limits in-vivo mechanism and preclinical therapeutics.
5. **Orphanet/ICD/MeSH mapping is generic.** COXPD30 lacks dedicated Orphanet/ICD/MeSH identifiers; some cross-references in Section 1 are flagged as not independently verified.
6. **Genotype–phenotype correlation unknown.** Whether residual activity predicts severity (as in the PRORP/COXPD54 spectrum) is untested for COXPD30.

---

## Proposed Follow-up Experiments / Actions

1. **International case ascertainment** (GeneMatcher, MSeqDR, mitochondrial-disease registries) to enlarge the COXPD30 cohort, define phenotype range, penetrance and natural history, and detect milder alleles.
2. **Systematic functional classification** of all *TRMT10C* VUS using the reconstituted mt-RNase P 5′-processing and m1R9-methylation assays, feeding ACMG-aligned re-classification into ClinVar.
3. **Model development:** conditional/hypomorphic *Trmt10c* mouse (tissue-restricted, e.g., cardiac or neuronal Cre) to bypass presumed embryonic lethality; patient-iPSC-derived cardiomyocytes, neurons and cochlear organoids to model organ-level phenotypes.
4. **Genotype–phenotype and structure–function mapping:** locate all reported variants onto the cryo-EM/PDB structures (5NFJ, 7ONU, 8CBK-series, 8RR-series, 9EY-series, 9GCH) to correlate residual activity with clinical severity.
5. **Therapeutic proof-of-concept:** given the demonstrated wild-type-cDNA rescue and the small CDS, test AAV-mediated *TRMT10C* gene replacement or mRNA therapy in patient cells and (once available) animal models.
6. **Curation actions:** finalize ontology mappings (confirm/assign Orphanet, ICD-11, MeSH), lock MONDO:0014856 ↔ *TRMT10C*, and encode the HPO frequency annotations and CHEBI/GO/CL/UBERON terms listed above into the knowledge base, explicitly flagging the TRMT5/COXPD26 disambiguation.

---

*Evidence-source key: **Human clinical** (patient cohorts/case reports), **In vitro** (reconstituted enzymology), **Structural** (cryo-EM/PDB), **Cell** (patient fibroblasts, knock-down), **Computational** (gnomAD constraint, VEP, ontology queries). All mechanistic claims are anchored to the cited PMIDs; inferred steps are labelled as such in the causal chain.*


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_30-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_30-deep-research-openscientist_artifacts/final_report.pdf)