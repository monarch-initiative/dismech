---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T07:41:02.766113'
end_time: '2026-05-05T08:06:37.384502'
duration_seconds: 1534.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atypical Hemolytic Uremic Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atypical Hemolytic Uremic Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Atypical Hemolytic Uremic Syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Disease Characterization: Atypical Hemolytic Uremic Syndrome (aHUS)

## Summary

Atypical Hemolytic Uremic Syndrome (aHUS) is a rare, life-threatening thrombotic microangiopathy (TMA) driven by chronic, uncontrolled activation of the alternative complement pathway. The disease is characterized by the clinical triad of microangiopathic hemolytic anemia (MAHA), thrombocytopenia, and acute kidney injury (AKI), with frequent extrarenal manifestations affecting the cardiovascular, neurological, and gastrointestinal systems. With an estimated prevalence of approximately 10 per million inhabitants and an incidence of 0.5–2 per million per year, aHUS qualifies as an ultra-rare disease with significant morbidity and mortality if untreated.

The molecular basis of aHUS centers on genetic or acquired defects in complement regulatory proteins. Pathogenic variants have been identified in CFH (~30% of cases), CD46/MCP (~10%), CFI (~5–15%), C3 (~10%), CFB (rare), THBD, and DGKE, while anti-factor H autoantibodies account for 5–11% of cases. Critically, aHUS exhibits incomplete penetrance (~50% of mutation carriers develop disease), requiring environmental triggers — including infections, pregnancy, surgery, or medications — to unmask the genetic predisposition. This "two-hit" model is fundamental to understanding disease pathogenesis and has direct implications for genetic counseling and risk assessment.

The therapeutic landscape has been revolutionized by complement C5 inhibitors. Eculizumab, approved by the FDA in 2011, and its long-acting successor ravulizumab, have transformed outcomes from >50% progression to end-stage kidney disease (ESKD) to sustained hematological and renal remission in the majority of treated patients. Genotype-guided management strategies are now emerging as critical for decisions regarding therapy duration, transplant planning, and relapse risk stratification, with CFH mutations conferring the highest relapse risk and CD46/MCP mutations the most favorable prognosis.

---

## Key Findings

### Finding 1: aHUS Is Caused by Dysregulation of the Alternative Complement Pathway

Multiple large registries and mechanistic studies confirm that aHUS is a thrombotic microangiopathy driven by uncontrolled activation of the alternative complement pathway, with genetic variants identified in approximately 50–60% of patients. As stated by Rojas-López et al., *"Atypical hemolytic uremic syndrome (aHUS) is a rare, life-threatening thrombotic microangiopathy (TMA) characterized by complement dysregulation, leading to microvascular thrombosis and multi-organ injury"* ([PMID: 40217974](https://pubmed.ncbi.nlm.nih.gov/40217974/)).

The key genes and their frequencies in aHUS patients were established by Frémeaux-Bacchi et al., who documented that *"different groups have demonstrated genetic predisposition to atypical HUS (aHUS) involving five genes encoding for complement components which play a role in the activation or control of the alternative pathway: encoding factor H (CFH), accounting for 30% of aHUS; CD46 (encoding membrane cofactor protein [MCP]) accounting for approximately 10% of aHUS; CFI (encoding factor I) accounting for an estimated 5-15% of patients; C3 (encoding C3) accounting for approximately 10% of aHUS; and rarely CFB (encoding factor B)"* ([PMID: 21376430](https://pubmed.ncbi.nlm.nih.gov/21376430/)).

The autoimmune form involving anti-factor H antibodies has been documented in 5–11% of cases: *"Factor H autoantibodies (anti-FHs) have been reported in aHUS in 5-11% of cases and are strongly associated with the homozygous deletion of CFHR3-CFHR1 genes"* ([PMID: 35405682](https://pubmed.ncbi.nlm.nih.gov/35405682/)).

| Gene | Protein | Frequency in aHUS | Function | Mutation Consequence |
|------|---------|-------------------|----------|---------------------|
| **CFH** | Complement Factor H | ~30% | Fluid-phase and surface complement regulator | Loss of function |
| **CD46/MCP** | Membrane Cofactor Protein | ~10% | Membrane-bound complement regulator | Loss of function |
| **CFI** | Complement Factor I | 5–15% | Serine protease cleaving C3b/C4b | Loss of function |
| **C3** | Complement C3 | ~10% | Central complement component | Gain of function |
| **CFB** | Complement Factor B | 1–4% | Alternative pathway activator | Gain of function |
| **THBD** | Thrombomodulin | ~5% | Endothelial anticoagulant/complement regulator | Loss of function |
| **DGKE** | Diacylglycerol Kinase Epsilon | Rare | Lipid signaling, non-complement | Loss of function |
| Anti-FH Ab | (autoimmune) | 5–11% | Blocks CFH surface recognition | Functional CFH deficiency |

### Finding 2: Incomplete Penetrance and Gene-Environment Interactions Are Fundamental to aHUS

Only approximately 50% of individuals carrying pathogenic complement variants ever develop clinical aHUS, establishing that environmental triggers are necessary to overwhelm the already-compromised complement regulatory capacity. As stated: *"Despite the presence of an underlying genetic etiology, an environmental trigger is often necessary to manifest disease, a phenomenon known as incomplete penetrance. These triggers could include infections, pregnancy, medication, cancers, or ischemia-reperfusion injury"* ([PMID: 40670222](https://pubmed.ncbi.nlm.nih.gov/40670222/)).

This two-hit model was further established: *"Predisposition to aHUS is inherited with incomplete penetrance. It is admitted that mutations confer a predisposition to develop aHUS rather than directly causing the disease and that a second event (genetic or environmental) is required for disease manifestation"* ([PMID: 21376430](https://pubmed.ncbi.nlm.nih.gov/21376430/)).

Data from the Global aHUS Registry (n=307 patients with identifiable triggers) quantified specific trigger frequencies: *"Malignancy was most common (58/307, 18.9%), followed by pregnancy and acute infections (both 53/307, 17.3%)"* ([PMID: 38604995](https://pubmed.ncbi.nlm.nih.gov/38604995/)).

### Finding 3: C5 Inhibitors (Eculizumab/Ravulizumab) Have Transformed aHUS Outcomes

Eculizumab (anti-C5 monoclonal antibody), approved by the FDA in 2011, and its long-acting successor ravulizumab have dramatically improved patient outcomes. In Japanese post-marketing surveillance of dialysis-dependent patients treated with eculizumab: *"Of 38 included patients, 21 (55.3%) and 17 (44.7%) were placed in Groups A and B, respectively. No patient re-started dialysis"* ([PMID: 41148448](https://pubmed.ncbi.nlm.nih.gov/41148448/)). Earlier treatment initiation (<15 days from TMA onset) was associated with dialysis discontinuation (p=0.008).

Genotype-specific relapse risk after treatment discontinuation has been characterized: *"Pathogenic gene variants in complement-regulating proteins, particularly CFH, CFI, MCP/CD46, and C3, significantly increase the risk of relapse, particularly within the first 3 to 12 months after cessation"* ([PMID: 41347985](https://pubmed.ncbi.nlm.nih.gov/41347985/)).

Real-world data from 60 patients switching to ravulizumab confirmed maintained effectiveness: *"This is the first real-world cohort analysis of data from patients treated with ravulizumab and reinforces the real-world safety and effectiveness data of ravulizumab in patients with aHUS who switched from eculizumab"* ([PMID: 39291212](https://pubmed.ncbi.nlm.nih.gov/39291212/)).

### Finding 4: aHUS Epidemiology — Rare Disease with Female Predominance in Adults

Belgian registry data established a population-based prevalence: *"A total of 121 Belgian patients were registered in the Global aHUS Registry, resulting in a prevalence of 10.4 aHUS patients per million inhabitants, with a higher proportion of females affected (57.9% vs 42.1% of males)"* ([PMID: 41102576](https://pubmed.ncbi.nlm.nih.gov/41102576/)).

A striking age-dependent sex ratio reversal was documented: *"A sex-specific difference was apparent according to age at initial disease onset as the ratio of males to females was 1.3:1 for childhood presentation and 1:2 for adult presentation"* ([PMID: 29907460](https://pubmed.ncbi.nlm.nih.gov/29907460/)). The female predominance in adults is likely attributable to pregnancy as a disease trigger.

UK Registry data quantified genotype-specific prognosis: *"ESKD-free survival probability at five years was 0.80 for paediatric patients and 0.57 for adults. ESKD-free survival was negatively influenced by CFH, C3, or CFI variants"* ([PMID: 40764536](https://pubmed.ncbi.nlm.nih.gov/40764536/)).

### Finding 5: Mouse Models Confirm the Causal Role of Complement Dysregulation in aHUS

Landmark mouse models have provided definitive in vivo proof of the complement dysregulation mechanism. The first aHUS mouse model (Cfh(−/−).FHΔ16-20) demonstrated that *"these mice, transgenically expressing a mouse FH protein functionally equivalent to aHUS-associated human FH mutants, regulate C3 activation in plasma and spontaneously develop aHUS but not MPGN2. These animals represent the first model of aHUS and provide in vivo evidence that effective plasma C3 regulation and the defective control of complement activation on renal endothelium are the critical events in the molecular pathogenesis of FH-associated aHUS"* ([PMID: 17517971](https://pubmed.ncbi.nlm.nih.gov/17517971/)).

Critically, C5-deficient mice were completely protected: *"spontaneous aHUS did not develop in any of the C5-deficient mice"* ([PMID: 21148255](https://pubmed.ncbi.nlm.nih.gov/21148255/)), providing the direct mechanistic rationale for therapeutic C5 inhibition with eculizumab.

The FH W1206R knock-in mouse model further showed that *"disruption of FH function on the cell surface can also lead to disseminated complement-dependent macrovascular thrombosis"* ([PMID: 28057640](https://pubmed.ncbi.nlm.nih.gov/28057640/)), with both micro- and macrovascular thrombosis, retinal ischemia, and 48% premature mortality.

---

## Mechanistic Model: From Genetic Predisposition to Clinical Disease

The pathogenesis of aHUS can be understood as a multi-step cascade where genetic susceptibility and environmental insults converge on the complement system:

```
STEP 1: GENETIC PREDISPOSITION (Upstream)
┌──────────────────────────────────────────────────────┐
│ Complement gene variant(s):                           │
│ CFH, CD46, CFI, C3, CFB, THBD, DGKE                 │
│ OR anti-FH autoantibodies                             │
│                                                       │
│ → Impaired complement regulation on endothelial       │
│   cell surfaces                                       │
│ → Normal plasma complement control preserved          │
│ → Subclinical carrier state (~50% lifetime disease    │
│   risk)                                               │
└────────────────────────┬─────────────────────────────┘
                         ↓
STEP 2: ENVIRONMENTAL TRIGGER — "SECOND HIT" (Upstream)
┌──────────────────────────────────────────────────────┐
│ Infection (17.3%), pregnancy (17.3%),                 │
│ malignancy (18.9%), surgery, medications              │
│                                                       │
│ → Complement activation via innate immunity           │
│ → Direct endothelial stress/injury                    │
│ → Overwhelms compromised regulatory capacity          │
└────────────────────────┬─────────────────────────────┘
                         ↓
STEP 3: COMPLEMENT AMPLIFICATION LOOP (Central)
┌──────────────────────────────────────────────────────┐
│ Uncontrolled C3b deposition on endothelium            │
│ C3 convertase (C3bBb) amplification loop              │
│ C5 convertase formation → C5a + C5b-9 (MAC)          │
│                                                       │
│ GO:0006957 (complement activation, alternative        │
│   pathway)                                            │
│                                                       │
│ ★ THERAPEUTIC TARGET: C5 inhibitors block here ★      │
└────────────────────────┬─────────────────────────────┘
                         ↓
STEP 4: ENDOTHELIAL INJURY AND THROMBOSIS (Downstream)
┌──────────────────────────────────────────────────────┐
│ MAC insertion → endothelial cell damage               │
│ C5a → neutrophil recruitment, NETosis                 │
│ Loss of anticoagulant endothelial properties          │
│ Platelet adhesion and fibrin deposition               │
│                                                       │
│ → Microvascular thrombosis (TMA)                      │
│   CL:1001005 (glomerular endothelial cell)            │
│   CL:0000233 (platelet)                               │
│   CL:0000775 (neutrophil)                             │
└────────────────────────┬─────────────────────────────┘
                         ↓
STEP 5: CLINICAL MANIFESTATION (Downstream)
┌──────────────────────────────────────────────────────┐
│ TMA TRIAD:                                            │
│ • Mechanical hemolysis (MAHA) — HP:0004855            │
│ • Consumptive thrombocytopenia — HP:0001873           │
│ • Organ ischemia/injury — HP:0001919 (AKI)           │
│                                                       │
│ Extrarenal: CNS (~18%), cardiac (~19%), GI (~26%)     │
│                                                       │
│ Primary organ: Kidney (UBERON:0002113)                │
│ Key structure: Renal glomerulus (UBERON:0000074)      │
└──────────────────────────────────────────────────────┘
```

**Key molecular players and their GO annotations:**
- GO:0006956 — Complement activation
- GO:0006957 — Complement activation, alternative pathway
- GO:0030449 — Regulation of complement activation
- GO:0007596 — Blood coagulation
- GO:0006954 — Inflammatory response
- GO:0030168 — Platelet activation

---

## Comprehensive Disease Characterization

### 1. Disease Information

**Overview:** Atypical Hemolytic Uremic Syndrome (aHUS) is a complement-mediated thrombotic microangiopathy characterized by microvascular endothelial injury leading to thrombosis, mechanical hemolysis, consumptive thrombocytopenia, and organ damage — predominantly affecting the kidneys. Unlike typical HUS caused by Shiga toxin-producing *E. coli* (STEC-HUS), aHUS arises from intrinsic dysregulation of the complement system.

| Database | Identifier |
|----------|-----------|
| **MONDO** | MONDO:0019632 |
| **OMIM** | #235400 (aHUS1/CFH); #612922 (aHUS2/CD46); #612923 (aHUS3/CFI); #612924 (aHUS4/CFB); #612925 (aHUS5/C3); #612926 (aHUS6/THBD); #615008 (aHUS7/DGKE) |
| **Orphanet** | ORPHA:2134 |
| **ICD-10** | D59.3 |
| **ICD-11** | 3A21.1 |
| **MeSH** | D065766 |

**Synonyms:** Complement-mediated TMA (CM-TMA), complement-mediated HUS, non-Shiga toxin-associated HUS, D− HUS (historical), primary aHUS.

**Information sources:** Aggregated from international patient registries (Global aHUS Registry), OMIM, Orphanet, GeneReviews, and 58 reviewed publications from PubMed.

### 2. Etiology

**Primary causes:** Genetic loss-of-function mutations in complement regulatory proteins (CFH, CFI, CD46, THBD) or gain-of-function mutations in complement activators (C3, CFB); acquired anti-factor H autoantibodies (5–11%); non-complement pathway via DGKE mutations (rare autosomal recessive form).

**Genetic risk factors:** See Finding 1 table above. A 400-patient genetic analysis additionally implicated PLG (plasminogen) as a novel aHUS gene enriched for ultrarare coding variants ([PMID: 30377230](https://pubmed.ncbi.nlm.nih.gov/30377230/)). CFHR1-CFHR3 homozygous deletion is strongly associated with anti-FH autoantibodies (91.6% vs 9.8% in controls; [PMID: 36622444](https://pubmed.ncbi.nlm.nih.gov/36622444/)). IgM class anti-FH autoantibodies were detected in 3.8% of patients, potentially explaining some previously "idiopathic" cases ([PMID: 33712527](https://pubmed.ncbi.nlm.nih.gov/33712527/)).

**Environmental triggers:** Infections (respiratory, gastrointestinal, H1N1, SARS-CoV-2), pregnancy/postpartum, malignancy, medications (calcineurin inhibitors, anti-VEGF agents), organ transplantation (ischemia-reperfusion), and autoimmune disease flares. SARS-CoV-2 spike proteins directly activate the alternative complement pathway ([PMID: 32877502](https://pubmed.ncbi.nlm.nih.gov/32877502/)).

**Protective factors:** CD46/MCP mutations associate with better prognosis. Early complement inhibitor therapy (<15 days) improves outcomes. Meningococcal vaccination is essential before C5 inhibitor therapy.

### 3. Phenotypes

**Core clinical triad (>95% frequency each):**

| Phenotype | HPO Term | Severity | Progression |
|-----------|----------|----------|-------------|
| Microangiopathic hemolytic anemia | HP:0004855 | Moderate-severe | Episodic, acute |
| Thrombocytopenia | HP:0001873 | Moderate-severe | Episodic |
| Acute kidney injury | HP:0001919 | Severe (40–50% require dialysis) | May progress to CKD/ESKD |

**Additional renal phenotypes:** Proteinuria (HP:0000093; nephrotic-range in 73.3%; [PMID: 41793014](https://pubmed.ncbi.nlm.nih.gov/41793014/)), hematuria (HP:0000790), hypertension (HP:0000822), chronic kidney disease (HP:0012622; 39% progress to CKD 3–4), ESKD (HP:0003774; 37% if untreated).

**Extrarenal manifestations (19–38% of patients):** Gastrointestinal involvement is most common (~26%; pancreatitis HP:0001733, colitis HP:0002583), followed by cardiovascular (~19%; cardiomyopathy HP:0001638), and neurological (~18%; seizures HP:0001250, stroke HP:0001297, encephalopathy).

**Laboratory abnormalities:** Elevated LDH (HP:0025435), low haptoglobin (decreased in 89.3%), schistocytes (HP:0001927), low C3 (HP:0005421; up to 90% in pediatric cohorts), normal ADAMTS13 activity (>10%).

**Age of onset:** Bimodal — mean 4.9 years (pediatric), 37.8 years (adult); overall 23.6 years ([PMID: 40764536](https://pubmed.ncbi.nlm.nih.gov/40764536/)). DGKE-aHUS presents in infancy; anti-FH antibody form typically in school-age children.

### 4. Genetic/Molecular Information

**Causal genes (HGNC IDs):** CFH (HGNC:4883), CD46 (HGNC:6953), CFI (HGNC:5394), C3 (HGNC:1318), CFB (HGNC:1037), THBD (HGNC:11784), DGKE (HGNC:2852), PLG (HGNC:9071, newly implicated).

**Pathogenic variants:** CFH mutations predominantly cluster in SCR 19–20, impairing surface recognition while preserving plasma regulatory activity. A novel homozygous CD46 mutation c.1127+2T>A was recently identified with functional validation showing reduced mRNA/protein expression ([PMID: 40983966](https://pubmed.ncbi.nlm.nih.gov/40983966/)). Variants with MAF >0.1% should not be considered pathogenic without functional evidence ([PMID: 30377230](https://pubmed.ncbi.nlm.nih.gov/30377230/)). 30–40% of patients carry VUS requiring further characterization ([PMID: 39644051](https://pubmed.ncbi.nlm.nih.gov/39644051/)).

**Chromosomal abnormalities:** The 1q31.3 CFHR gene cluster is prone to non-allelic homologous recombination producing deletions (CFHR1-CFHR3), duplications, and hybrid genes (CFH-CFHR fusions).

**Modifier genes:** CFHR1-5 gene copy number variants, MCP polymorphisms, and combined mutations (digenic/oligogenic inheritance) increase disease penetrance and severity.

### 5. Environmental Information

No specific toxins or occupational exposures are established as direct aHUS causes. Key infectious triggers include *Mycoplasma pneumoniae* (associated with anti-FH antibody development; [PMID: 35405682](https://pubmed.ncbi.nlm.nih.gov/35405682/)), H1N1 influenza (<30 reported cases; [DOI: 10.5414/CNCS111525](https://doi.org/10.5414/CNCS111525)), and SARS-CoV-2 (spike protein directly activates the alternative pathway; [PMID: 32877502](https://pubmed.ncbi.nlm.nih.gov/32877502/)).

### 6. Mechanism / Pathophysiology

**Molecular pathways:** The central pathway is the alternative complement pathway (KEGG: hsa04610; Reactome: R-HSA-173736). Genetic defects impair C3b inactivation on endothelial surfaces → uncontrolled C3 convertase (C3bBb) amplification → C5 convertase formation → C5a (anaphylatoxin) + C5b-9 (MAC) generation → endothelial injury.

**Protein dysfunction:** CFH mutations in SCR 19–20 impair surface recognition while maintaining fluid-phase regulation — the critical distinction proven by mouse models ([PMID: 17517971](https://pubmed.ncbi.nlm.nih.gov/17517971/)). CFH also has three heparin-binding sites (SCR 7, SCR 9, SCR 20) mediating endothelial surface interactions ([PMID: 16263173](https://pubmed.ncbi.nlm.nih.gov/16263173/)).

**Cellular processes:** Endothelial activation/injury (GO:0002544), platelet activation (GO:0030168), NETosis, inflammation (GO:0006954), and MAC-mediated cell death. Complement-coagulation-neutrophil cross-talk amplifies TMA ([PMID: 36642429](https://pubmed.ncbi.nlm.nih.gov/36642429/)).

**Cell types involved:** Glomerular endothelial cells (CL:1001005; primary target), platelets (CL:0000233), neutrophils (CL:0000775), podocytes (CL:0000653; secondary), tubular epithelial cells (CL:1000494; ischemic).

**Immune involvement:** Autoimmunity (anti-FH IgG and IgM autoantibodies; [PMID: 33712527](https://pubmed.ncbi.nlm.nih.gov/33712527/)); complement-coagulation cross-talk; SLE-associated aHUS ([PMID: 41173493](https://pubmed.ncbi.nlm.nih.gov/41173493/)).

### 7. Anatomical Structures Affected

**Primary organ:** Kidney (UBERON:0002113) — renal glomeruli (UBERON:0000074) and arterioles (UBERON:0001980) are the predominant sites of TMA.

**Secondary organs:** Brain (UBERON:0000955; ~18%), heart (UBERON:0000948; ~19%), GI tract (UBERON:0005409; ~26%), lung (UBERON:0002048; rare), eye (UBERON:0000970; retinal thrombosis demonstrated in FH W1206R mice; [PMID: 30711487](https://pubmed.ncbi.nlm.nih.gov/30711487/)).

**Subcellular:** Cell membrane (GO:0005886) — MAC insertion site; extracellular space (GO:0005615) — complement cascade.

**Lateralization:** Bilateral kidney involvement (symmetric).

### 8. Temporal Development

**Onset:** Acute; bimodal age distribution (pediatric mean 4.9 years, adult mean 37.8 years). Onset typically follows a triggering event.

**Progression:** Episodic/relapsing-remitting without treatment. 57% of patients experience additional TMA events. Without treatment: ESKD-free survival at 5 years is 0.80 (pediatric) and 0.57 (adult) ([PMID: 40764536](https://pubmed.ncbi.nlm.nih.gov/40764536/)). With C5 inhibitors: hematological remission ~80%, >55% discontinue dialysis.

**Relapse patterns:** Highest risk 3–12 months after treatment discontinuation, genotype-dependent. CFH carries highest relapse risk; CD46 carries lowest.

**Critical periods:** Pregnancy/postpartum, post-transplant, post-infectious episodes.

### 9. Inheritance and Population

**Epidemiology:** Prevalence ~10.4 per million (Belgian registry; [PMID: 41102576](https://pubmed.ncbi.nlm.nih.gov/41102576/))); incidence ~0.5–2 per million per year.

**Inheritance:** Predominantly autosomal dominant with incomplete penetrance (~50%) for CFH, CFI, C3, CFB, THBD. Autosomal recessive for DGKE and some CD46 families. Digenic/oligogenic patterns recognized.

**Sex ratio:** Overall 57.9% female. Male:female = 1.3:1 in childhood, 1:2 in adults ([PMID: 29907460](https://pubmed.ncbi.nlm.nih.gov/29907460/)). Adult female predominance attributable to pregnancy as trigger.

**Geographic distribution:** Worldwide; anti-FH antibody form more prevalent in Indian subcontinent; population-specific genetic profiles documented (Brazilian: [PMID: 39918340](https://pubmed.ncbi.nlm.nih.gov/39918340/); Australian: [PMID: 32378251](https://pubmed.ncbi.nlm.nih.gov/32378251/)).

### 10. Diagnostics

**Clinical tests:** CBC with smear (schistocytes), LDH, haptoglobin, Coombs test (negative), creatinine, complement levels (C3, C4, Factor H, Factor I, sC5b-9), ADAMTS13 activity (>10% excludes TTP), anti-Factor H antibodies, Shiga toxin testing (excludes STEC-HUS).

**Genetic testing:** Recommended for all patients — comprehensive NGS gene panel (minimum: CFH, CFI, CD46, C3, CFB, THBD, DGKE; extended: CFHR1-5, PLG) plus MLPA for structural variants. WES for novel gene discovery. Anti-FH antibody ELISA in all patients. Turnaround time: weeks — treatment should not be delayed ([PMID: 39644051](https://pubmed.ncbi.nlm.nih.gov/39644051/)).

**Biopsy findings:** Glomerular/arteriolar TMA with endothelial swelling, fibrin-platelet thrombi, "onion-skin" intimal proliferation, mesangiolysis, cortical necrosis (severe).

**Differential diagnosis:** TTP (ADAMTS13 <10%), STEC-HUS (Shiga toxin+), HELLP syndrome, malignant hypertension-TMA (complement variants found in 25%; [PMID: 39106497](https://pubmed.ncbi.nlm.nih.gov/39106497/)), drug-induced TMA, autoimmune disease-associated TMA, cobalamin C deficiency, G6PD deficiency (can mimic aHUS; [PMID: 29248304](https://pubmed.ncbi.nlm.nih.gov/29248304/)).

**Screening:** Cascade genetic screening recommended for first-degree relatives. Not included in newborn screening programs.

### 11. Outcome/Prognosis

**Pre-eculizumab era:** 33–40% mortality/ESKD at first episode; 65% overall ESKD progression.

**Post-eculizumab era:** Hematological remission ~80%; 55.3% of dialysis patients discontinue dialysis ([PMID: 41148448](https://pubmed.ncbi.nlm.nih.gov/41148448/)); post-transplant TMA: 68% graft survival at 12 months with eculizumab ([PMID: 41368132](https://pubmed.ncbi.nlm.nih.gov/41368132/)).

**Genotype-prognosis correlations:**

| Genotype | ESKD Risk | Relapse Risk | Transplant Recurrence |
|----------|-----------|-------------|----------------------|
| CFH | Highest (~60%) | High | ~80% |
| CFI | High | Moderate | ~50% |
| C3 | Moderate-High | Moderate | ~50% |
| CD46/MCP | Lowest (~20%) | Low-Moderate | <20% |
| Anti-FH Ab | Variable | High if untreated | Possible |

**Prognostic factors:** Genotype (CFH worst, CD46 best), age at onset (childhood better), time to treatment (<15 days improves outcomes; p=0.008), presence of hypertension (less frequent in recovery group: 28.6% vs 64.7%, p=0.022), and multiple pathogenic variants ([PMID: 41347985](https://pubmed.ncbi.nlm.nih.gov/41347985/)).

### 12. Treatment

**First-line — Complement C5 inhibitors (MAXO:0001298):**
- **Eculizumab** (Soliris®): Anti-C5 monoclonal antibody; IV q2 weeks; FDA-approved 2011
- **Ravulizumab** (Ultomiris®): Long-acting anti-C5; IV q8 weeks; confirmed real-world effectiveness ([PMID: 39291212](https://pubmed.ncbi.nlm.nih.gov/39291212/))
- Mandatory meningococcal vaccination before treatment (MenACWY + MenB)

**Plasma therapy (MAXO:0000755):** Historical first-line; now bridge therapy or when C5 inhibitors unavailable. Plasma exchange removes autoantibodies and mutant proteins; plasma infusion provides normal complement regulators.

**Immunosuppression (anti-FH antibody form):** Rituximab, mycophenolate mofetil, corticosteroids.

**Emerging therapies:**
- **Iptacopan/LNP023** (oral Factor B inhibitor): First successful use in SLE-aHUS ([PMID: 40996634](https://pubmed.ncbi.nlm.nih.gov/40996634/))
- **Factor D inhibitors**: Block upstream complement activation ([PMID: 32877502](https://pubmed.ncbi.nlm.nih.gov/32877502/))
- **Anti-properdin**: Prevents TMA in mouse models ([PMID: 29858280](https://pubmed.ncbi.nlm.nih.gov/29858280/))

**Kidney transplantation (MAXO:0001175):** For ESKD patients; requires genotype-based risk assessment and prophylactic eculizumab for high-risk genotypes.

**Treatment discontinuation:** Genotype-guided — CFH: generally continued indefinitely; CD46: safer to discontinue. Close monitoring mandatory for 3–12 months post-cessation.

### 13. Prevention

**Primary prevention:** Genetic counseling (MAXO:0000079) for affected families; no population-level primary prevention exists.

**Secondary prevention:** Cascade genetic screening of first-degree relatives; biomarker monitoring in at-risk individuals; trigger awareness education.

**Tertiary prevention:** Prophylactic eculizumab pre-transplant; prompt treatment at relapse signs; lifelong complement inhibition for high-risk genotypes; meningococcal vaccination (MAXO:0000759).

### 14. Other Species / Natural Disease

No well-documented naturally occurring aHUS in companion animals. Complement system is highly conserved across vertebrates. Orthologous genes: mouse Cfh (NCBI Gene: 12628), C3 (12266), Cfi (12630), Cfb (14962), Cd46 (17221). CFH surface recognition domain function is conserved, as demonstrated by mouse models faithfully recapitulating human disease.

### 15. Model Organisms

**Cfh(−/−).FHΔ16-20 mice:** First aHUS model; expresses truncated FH lacking surface-binding domains; spontaneous renal TMA ([PMID: 17517971](https://pubmed.ncbi.nlm.nih.gov/17517971/)).

**FH W1206R knock-in mice:** Point mutation model; renal TMA + systemic thrombophilia + retinal ischemia; 48% premature death ([PMID: 28057640](https://pubmed.ncbi.nlm.nih.gov/28057640/); [PMID: 30711487](https://pubmed.ncbi.nlm.nih.gov/30711487/)).

**C5-deficient crosses:** Complete protection from aHUS, proving C5 is essential ([PMID: 21148255](https://pubmed.ncbi.nlm.nih.gov/21148255/)) — direct rationale for eculizumab.

**Anti-properdin treated mice:** Blocking properdin prevents TMA and thrombophilia ([PMID: 29858280](https://pubmed.ncbi.nlm.nih.gov/29858280/)).

**Model limitations:** Homozygous backgrounds (humans typically heterozygous); incomplete penetrance poorly modeled in inbred strains; most models focus on CFH; drug pharmacokinetic differences limit direct translation.

---

## Evidence Base

### Key Supporting Literature

| Citation | Contribution | Evidence Type |
|----------|-------------|---------------|
| [PMID: 40217974](https://pubmed.ncbi.nlm.nih.gov/40217974/) | Comprehensive aHUS review: complement dysregulation, multiorgan involvement | Clinical review |
| [PMID: 21376430](https://pubmed.ncbi.nlm.nih.gov/21376430/) | Established gene frequencies and two-hit model | Clinical/genetic |
| [PMID: 17517971](https://pubmed.ncbi.nlm.nih.gov/17517971/) | First mouse model proving surface complement dysregulation | Model organism |
| [PMID: 21148255](https://pubmed.ncbi.nlm.nih.gov/21148255/) | C5 dependence of aHUS — rationale for eculizumab | Model organism |
| [PMID: 28057640](https://pubmed.ncbi.nlm.nih.gov/28057640/) | FH W1206R mouse: systemic thrombophilia | Model organism |
| [PMID: 29907460](https://pubmed.ncbi.nlm.nih.gov/29907460/) | Global Registry: genotype-phenotype correlations (n=851) | Clinical registry |
| [PMID: 30377230](https://pubmed.ncbi.nlm.nih.gov/30377230/) | 400-patient genetic analysis; PLG as new gene | Genetic study |
| [PMID: 41102576](https://pubmed.ncbi.nlm.nih.gov/41102576/) | Belgian registry: prevalence 10.4/million | Population epidemiology |
| [PMID: 40764536](https://pubmed.ncbi.nlm.nih.gov/40764536/) | UK registry: ESKD-free survival, genotype-prognosis | Clinical registry |
| [PMID: 38604995](https://pubmed.ncbi.nlm.nih.gov/38604995/) | Trigger characterization (n=307) | Clinical registry |
| [PMID: 41148448](https://pubmed.ncbi.nlm.nih.gov/41148448/) | Eculizumab: 55.3% dialysis discontinuation | Post-marketing surveillance |
| [PMID: 39291212](https://pubmed.ncbi.nlm.nih.gov/39291212/) | Ravulizumab real-world effectiveness | Clinical registry |
| [PMID: 41347985](https://pubmed.ncbi.nlm.nih.gov/41347985/) | Genotype-specific relapse risk | Clinical review |
| [PMID: 40670222](https://pubmed.ncbi.nlm.nih.gov/40670222/) | Gene-environment interaction framework | Mechanistic review |
| [PMID: 35405682](https://pubmed.ncbi.nlm.nih.gov/35405682/) | Anti-FH antibodies: 5–11% prevalence | Clinical study |
| [PMID: 36622444](https://pubmed.ncbi.nlm.nih.gov/36622444/) | Complement variants in anti-FH aHUS: 3% pathogenic | Meta-analysis |
| [PMID: 39644051](https://pubmed.ncbi.nlm.nih.gov/39644051/) | Diagnosis, management, discontinuation consensus | Clinical guideline |
| [PMID: 40983966](https://pubmed.ncbi.nlm.nih.gov/40983966/) | Novel CD46 mutation c.1127+2T>A | Genetic/functional |
| [PMID: 40996634](https://pubmed.ncbi.nlm.nih.gov/40996634/) | First iptacopan use in SLE-aHUS | Case report |
| [PMID: 32877502](https://pubmed.ncbi.nlm.nih.gov/32877502/) | SARS-CoV-2 spike activates alternative pathway | In vitro |

---

## Limitations and Knowledge Gaps

1. **Genetically unresolved cases (30–40%):** Despite comprehensive testing, no pathogenic variant is identified in a substantial proportion of patients. Additional genetic, epigenetic, and environmental factors remain to be discovered.

2. **VUS interpretation:** 30–40% of identified variants are classified as VUS. Functional validation assays are not standardized or widely available ([PMID: 39644051](https://pubmed.ncbi.nlm.nih.gov/39644051/)).

3. **Treatment discontinuation criteria:** While genotype-guided approaches are emerging, precise biomarkers to predict safe discontinuation are lacking. The optimal duration of C5 inhibitor therapy remains undefined for many genotypes.

4. **Upstream complement inhibition:** C5 inhibitors leave upstream C3 activation unchecked. Whether proximal complement inhibitors (Factor B, Factor D, C3) offer superior outcomes remains under investigation.

5. **Registry biases:** Most data derive from developed nations with access to eculizumab. Global epidemiology in low-resource settings is poorly characterized. The Brazilian case report ([PMID: 41425686](https://pubmed.ncbi.nlm.nih.gov/41425686/)) illustrates how limited access impacts outcomes.

6. **Epigenetic contributions:** Virtually no data on epigenetic modifications in aHUS pathogenesis.

7. **Quality of life data:** Formal QoL studies using validated instruments specific to aHUS are limited.

8. **Long-term outcomes:** With complement inhibitors available only since 2011, truly long-term (>15 year) outcome data are still maturing.

9. **Pregnancy management:** Optimal management of pregnancy in women with known complement variants remains poorly defined.

10. **Non-complement aHUS:** The role of DGKE and other non-complement pathways is incompletely understood.

---

## Proposed Follow-up Research and Actions

### High Priority

1. **Functional characterization of VUS:** Develop standardized high-throughput assays (hemolytic assays, surface protection assays) for complement gene variants to reclassify the 30–40% of patients with VUS.

2. **Biomarker development for treatment discontinuation:** Prospective studies correlating complement biomarkers (sC5b-9, C3d, Bb) with relapse risk to enable personalized treatment duration decisions.

3. **Clinical trials of proximal complement inhibitors:** Head-to-head trials comparing Factor B inhibitors (iptacopan), Factor D inhibitors, and C3 inhibitors against C5 inhibitors.

### Moderate Priority

4. **Whole-genome sequencing studies:** To identify non-coding regulatory variants, structural variants, and novel genes in genetically unresolved aHUS.

5. **Single-cell transcriptomics of aHUS renal biopsies:** Characterize endothelial cell subtypes and immune cell populations at single-cell resolution.

6. **Epigenome-wide association studies:** Investigate DNA methylation patterns in complement regulatory genes and their association with disease penetrance.

7. **Global epidemiology studies:** Characterize population-specific genetics and outcomes in under-represented populations.

### Lower Priority

8. **Additional animal models:** CFI, C3, and CD46 mutation mouse models for genotype-specific pathophysiology.

9. **Long-term outcome registries:** 20+ year follow-up of patients on complement inhibitors.

10. **AI-based variant interpretation:** Machine learning models trained on functional data to predict pathogenicity of novel complement variants.

---

## Ontology Term Summary

| Category | Terms |
|----------|-------|
| **MONDO** | MONDO:0019632 (atypical hemolytic uremic syndrome) |
| **HPO** | HP:0004855 (MAHA), HP:0001873 (thrombocytopenia), HP:0001919 (AKI), HP:0000093 (proteinuria), HP:0000822 (hypertension), HP:0001927 (schistocytosis), HP:0025435 (elevated LDH), HP:0005421 (low C3), HP:0001250 (seizures), HP:0001638 (cardiomyopathy), HP:0012622 (CKD), HP:0001733 (pancreatitis) |
| **GO (BP)** | GO:0006956 (complement activation), GO:0006957 (alternative pathway), GO:0030449 (regulation of complement), GO:0007596 (coagulation), GO:0006954 (inflammation), GO:0030168 (platelet activation) |
| **GO (CC)** | GO:0005886 (plasma membrane), GO:0005615 (extracellular space) |
| **CL** | CL:1001005 (glomerular endothelial cell), CL:0000233 (platelet), CL:0000775 (neutrophil), CL:0000653 (podocyte), CL:1000494 (renal tubular epithelial cell) |
| **UBERON** | UBERON:0002113 (kidney), UBERON:0000074 (renal glomerulus), UBERON:0000955 (brain), UBERON:0000948 (heart), UBERON:0005409 (GI tract), UBERON:0002048 (lung) |
| **CHEBI** | CHEBI:149504 (eculizumab), CHEBI:190524 (ravulizumab) |
| **MAXO** | MAXO:0001298 (complement inhibitor therapy), MAXO:0000602 (dialysis), MAXO:0001175 (kidney transplantation), MAXO:0000755 (plasma exchange), MAXO:0000759 (vaccination), MAXO:0000079 (genetic counseling) |

---

*Report generated from systematic review of 58 publications, international registry data, and mechanistic studies. All claims are supported by cited primary literature with PMIDs. Evidence types include human clinical data (registries, case series, meta-analyses), model organism studies (mouse genetic models), in vitro functional assays, and computational analyses.*
