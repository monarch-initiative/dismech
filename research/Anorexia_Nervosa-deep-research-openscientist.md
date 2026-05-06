---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T03:55:07.426084'
end_time: '2026-05-05T04:23:40.601442'
duration_seconds: 1713.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anorexia Nervosa
  mondo_id: ''
  category: Psychiatric
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
citation_count: 71
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anorexia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Anorexia Nervosa** covering all of the
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

# Comprehensive Disease Characterization Report: Anorexia Nervosa

---

## Summary

**Anorexia nervosa (AN)** is a severe metabo-psychiatric disorder characterized by persistent energy intake restriction, intense fear of gaining weight, and disturbance in self-perceived body weight or shape. It carries the highest mortality rate of any mental illness, with a standardized mortality ratio (SMR) of 5.52 (95% CI: 4.47–6.82) compared with the general population and a suicide-related mortality risk ratio of 9.86 (95% CI: 5.63–17.27) ([PMID: 41536100](https://pubmed.ncbi.nlm.nih.gov/41536100/)). The disorder affects approximately 0.48–1.4% of women and 0.2% of men over their lifetime, with typical onset during adolescence. The landmark 2019 genome-wide association study identified eight significant risk loci and established AN as a disorder with both psychiatric and metabolic genetic origins, with heritability estimated at 48–74% from twin studies and SNP-based heritability of approximately 11–17% ([PMID: 31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/); [PMID: 39988782](https://pubmed.ncbi.nlm.nih.gov/39988782/)).

AN produces devastating multi-organ effects including the largest brain structural deficits of any psychiatric disorder (Cohen's d up to 0.95 for cortical thickness reductions), global endocrine dysregulation with hypothalamic-pituitary axis dysfunction, osteoporosis in up to 50% of patients, and cardiovascular complications. Treatment relies primarily on family-based therapy (FBT) for adolescents, with remission rates of 29–49% at 12-month follow-up, and cognitive behavioral therapy for adults. No pharmacological treatments are currently approved specifically for AN, though olanzapine shows promise as an adjunctive treatment. Long-term follow-up studies indicate approximately 50–60% of patients achieve full recovery, while 10–20% develop chronic illness and mortality remains significant even decades after diagnosis.

Emerging research avenues—including gut microbiome interventions, epigenetic biomarkers for disease status, polygenic risk scoring, and novel pharmacological targets such as GLP-1 receptor agonists—offer promising future therapeutic directions. This report synthesizes evidence from 89 reviewed publications to provide a comprehensive characterization across all major disease dimensions.

---

## 1. Disease Information

### Overview

Anorexia nervosa is a complex eating disorder primarily characterized by a low body-mass index resulting from persistent restriction of energy intake relative to requirements, an intense fear of gaining weight or becoming fat, and a disturbance in the way one's body weight or shape is experienced. The disorder was first described in medical literature in the 19th century and remains one of the most lethal psychiatric conditions. As stated in the landmark GWAS publication: *"Characterized primarily by a low body-mass index, anorexia nervosa is a complex and serious illness"* ([PMID: 31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/)).

### Key Identifiers

| Database | Identifier |
|----------|------------|
| MONDO | MONDO:0005351 |
| OMIM | 606788 |
| Orphanet | ORPHA:36297 |
| ICD-10 | F50.0 (Anorexia nervosa), F50.1 (Atypical anorexia nervosa) |
| ICD-11 | 6B80 |
| MeSH | D000856 |
| DSM-5 | 307.1 |

### Synonyms and Alternative Names

- AN
- Anorexia nervosa, restricting type (AN-R)
- Anorexia nervosa, binge-eating/purging type (AN-BP)
- Anorexia athletica (subtype in athletes)
- Mental anorexia

### Information Sources

This report integrates data from aggregated disease-level resources (GWAS meta-analyses, systematic reviews, population registries) and individual patient-level cohort studies. Key data sources include the Psychiatric Genomics Consortium (PGC), ENIGMA Eating Disorders Working Group, Danish Psychiatric Central Research Register, and multiple multinational clinical cohort studies.

---

## 2. Etiology

### Disease Causal Factors

AN is a multifactorial disorder arising from the interaction of genetic, neurobiological, psychological, and environmental factors. It is now recognized as a **metabo-psychiatric** disorder, reflecting the discovery that genetic risk factors span both psychiatric liability and metabolic/anthropometric traits ([PMID: 31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/); [PMID: 38431502](https://pubmed.ncbi.nlm.nih.gov/38431502/)).

### Genetic Risk Factors

**Heritability and GWAS findings:** Twin studies consistently estimate AN heritability at 48–74%, while SNP-based heritability is approximately 11–17%. As reported: *"Genetic studies, particularly genome-wide association studies (GWAS), have identified key loci associated with ED susceptibility, with heritability estimates for these disorders ranging between 48% and 74%"* ([PMID: 39988782](https://pubmed.ncbi.nlm.nih.gov/39988782/)).

The 2019 PGC-ED GWAS meta-analysis of approximately 17,000 AN cases and 55,000 controls identified **eight genome-wide significant loci**, implicating genes involved in both psychiatric and metabolic pathways ([PMID: 31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/)).

**Key susceptibility loci and candidate genes:**

| Gene/Locus | Chromosome | Function | Evidence |
|------------|------------|----------|----------|
| *FOXP1* | 3p13 | Transcription factor; neurodevelopment | GWAS locus; poly-T STR in 3'UTR identified |
| *CADM1* | 11q23.3 | Cell adhesion; synapse formation | GWAS significant |
| *IP6K2/PRKAR2A* | 3p21.31 | Kinase signaling | GWAS locus; polymorphic SVA-D element |
| *NCKIPSD* | 3p21.31 | Cytoskeleton regulation | GWAS significant |
| *PTBP2* | 1p21.3 | RNA processing; neuronal | GWAS significant |
| *BDNF* | 11p14.1 | Neurotrophin; feeding regulation | Candidate gene; Val66Met polymorphism |
| *HTR2A* (5-HT2A) | 13q14.2 | Serotonin receptor | Candidate gene meta-analyses |

Targeted nanopore sequencing has identified additional poorly characterized variants in GWAS regions, including a polymorphic SINE-VNTR-Alu element (SVA-D) near *IP6K2/PRKAR2A* and a poly-T short tandem repeat in the 3'UTR of *FOXP1*, which may affect post-transcriptional processing ([PMID: 39741260](https://pubmed.ncbi.nlm.nih.gov/39741260/)).

**Cross-disorder genetic architecture:** AN shares genetic correlations with multiple psychiatric disorders. Genomic structural equation modeling places AN within a "compulsive disorders" factor alongside OCD and Tourette syndrome ([PMID: 39009701](https://pubmed.ncbi.nlm.nih.gov/39009701/)). Cross-disorder meta-analysis has identified 109 loci associated with at least two psychiatric disorders, with pleiotropic loci showing heightened brain expression beginning prenatally ([PMID: 31835028](https://pubmed.ncbi.nlm.nih.gov/31835028/)).

AN is **negatively** genetically correlated with body fat percentage and fat-free mass, and Mendelian randomization identifies AN as potentially causal for decreased fat mass ([PMID: 31852892](https://pubmed.ncbi.nlm.nih.gov/31852892/)).

### Environmental Risk Factors

- **Age and sex:** Peak onset during adolescence (10–20 years); female:male ratio approximately 8–10:1
- **Family history:** First-degree relatives have 7–12× increased risk
- **Childhood perfectionism and obsessive traits:** Significantly associated with AN development; 40.4% of restrictive eaters display obsessive traits ([PMID: 20179406](https://pubmed.ncbi.nlm.nih.gov/20179406/))
- **Weight/shape teasing:** Established risk factor across severity levels ([PMID: 38212857](https://pubmed.ncbi.nlm.nih.gov/38212857/))
- **Childhood obesity:** History of overweight predisposes to eating disorder development
- **Relational factors:** Unmet emotional needs, feelings of non-belonging, exposure to conditional worth messaging about body/eating ([PMID: 41236167](https://pubmed.ncbi.nlm.nih.gov/41236167/))
- **Athletic participation:** Athletes in aesthetic sports have significantly higher prevalence ([PMID: 37528996](https://pubmed.ncbi.nlm.nih.gov/37528996/))
- **Cultural factors:** Western cultural idealization of thinness plays a salient role in rising incidence

### Protective Factors

- Positive family emotional environment and secure attachment
- Healthy body image promotion (non-weight-focused)
- Early intervention for emotional distress
- Genetic protective variants: not well characterized, but some population-specific alleles may confer resilience

### Gene-Environment Interactions

Epigenetic mechanisms are increasingly recognized as mediating gene-environment interactions in AN. Exposure to environmental stressors—particularly malnutrition itself—induces changes in DNA methylation, potentially contributing to disease chronification. Epigenome-wide association studies suggest potential reversibility of malnutrition-induced epigenetic changes upon recovery ([PMID: 38849516](https://pubmed.ncbi.nlm.nih.gov/38849516/); [PMID: 30353170](https://pubmed.ncbi.nlm.nih.gov/30353170/)).

---

## 3. Phenotypes

### Core Behavioral and Psychological Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Restrictive eating / food refusal | HP:0011968 (Feeding difficulties) | ~100% | Adolescence | Variable to severe |
| Intense fear of weight gain | HP:0000831 | ~100% | Adolescence | Moderate to severe |
| Body image distortion | — | ~100%; delusional intensity in 23.6% | Adolescence | Variable |
| Excessive exercise | HP:0000752 (Hyperactivity) | 31–80% | Adolescence | Variable |
| Amenorrhea | HP:0000141 | ~70–90% in females | After weight loss | Reversible with weight restoration |
| Depressed mood | HP:0000716 | ~45% comorbid depression/dysthymia | Variable | Variable |
| Obsessive-compulsive features | HP:0000722 (OCD) | 40.4% (restrictive subtype) | Premorbid or concurrent | Variable |
| Anhedonia | HP:0000746 | Common | During illness | Moderate to severe |

Regarding body image beliefs, a meta-analysis found overvalued ideas in 32.5% and delusional-like beliefs in 23.6% of AN patients, with greater belief rigidity correlating with poorer insight ([PMID: 41707619](https://pubmed.ncbi.nlm.nih.gov/41707619/)).

### Physical Manifestations and Clinical Signs

| Phenotype | HPO Term | Frequency | Clinical Significance |
|-----------|----------|-----------|----------------------|
| Low BMI / Emaciation | HP:0004325 (Decreased body weight) | ~100% | Defining feature |
| Hypothermia | HP:0002045 | Common | Adaptive to starvation |
| Bradycardia | HP:0001662 | Common | Cardiovascular complication |
| Lanugo hair | HP:0002232 | ~30% | Physical sign |
| Acrocyanosis | HP:0001063 (Acrocyanosis) | Common | Peripheral vascular |
| Osteopenia/Osteoporosis | HP:0000939 / HP:0000938 | Up to 50% | Potentially irreversible |
| Purpura | — | Occasional | Bleeding diathesis |

### Laboratory Abnormalities

| Finding | HPO/LOINC | Frequency | Notes |
|---------|-----------|-----------|-------|
| Hypokalemia | HP:0002900 | Common (purging subtype) | aOR 1.98 for ED diagnosis |
| Hyponatremia | HP:0002902 | Less common | aOR 5.26 for ED diagnosis |
| Hypophosphatemia | HP:0002148 | Common, especially refeeding | aOR 2.83 for ED diagnosis |
| Hypomagnesemia | HP:0002917 | Common | Monitor during refeeding |
| Metabolic alkalosis | — | Common (purging) | aOR 2.60 for ED diagnosis |
| Hypercholesterolemia | HP:0003124 | 13–18% | Paradoxical; associated with lower BMI |
| Elevated cortisol | HP:0003118 | Common | Adaptive hypercortisolaemia |
| Low leptin | — | Common | Suppressed adipokine |
| Elevated ghrelin | — | Common | Orexigenic compensation |
| Elevated peptide YY | — | Common | Paradoxically elevated |
| Low estradiol | HP:0008214 | Common | Hypogonadotropic hypogonadism |
| Low IGF-1 | — | Common | Growth hormone resistance |

Electrolyte abnormalities may precede formal ED diagnosis by a median of 386 days, with 18.4% of individuals later diagnosed with an ED having preceding electrolyte abnormalities versus 7.5% of controls (aOR 2.12, 95% CI: 1.86–2.41) ([PMID: 36346630](https://pubmed.ncbi.nlm.nih.gov/36346630/)).

### Quality of Life Impact

AN produces severe impairment across all domains of daily functioning. Role impairment and comorbidity with other mental disorders are highly common ([PMID: 19427647](https://pubmed.ncbi.nlm.nih.gov/19427647/)). Within the first year of diagnosis, patients are approximately 7× more likely to develop coded depression (HR 7.3, 95% CI: 6.6–8.1) and 9× more likely to engage in self-harm (HR 9.4, 95% CI: 8.2–10.7) compared to matched controls ([PMID: 41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/)).

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

AN is a **polygenic disorder** without single causal gene mutations. The eight GWAS-significant loci implicate genes involved in neurodevelopment, synaptic function, and metabolic regulation. An estimated ~11,500 genetic variants are thought to contribute to the full heritability landscape ([PMID: 31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/)).

**Candidate genes with robust evidence:**

- **BDNF** (Brain-Derived Neurotrophic Factor): Reduced circulating levels in AN patients; Val66Met polymorphism associated with worse outcomes in humans, though not confirmed in rat ABA models ([PMID: 35625351](https://pubmed.ncbi.nlm.nih.gov/35625351/))
- **HTR2A** (Serotonin 2A Receptor): Meta-analytic support as a susceptibility gene for both AN and bulimia nervosa ([PMID: 24202964](https://pubmed.ncbi.nlm.nih.gov/24202964/))
- **FOXP1**: Transcription factor involved in neurodevelopment; poly-T STR in 3'UTR may affect post-transcriptional processing ([PMID: 39741260](https://pubmed.ncbi.nlm.nih.gov/39741260/))

### Genetic Correlations with Other Traits

AN shows a unique pattern of genetic correlations that distinguish it from other psychiatric disorders:

| Trait | Genetic Correlation Direction | Significance |
|-------|------------------------------|--------------|
| OCD | Positive | Compulsive disorders cluster |
| Schizophrenia | Positive (moderate) | Shared psychiatric liability |
| Major depression | Positive | Shared internalizing factor |
| BMI / Body fat % | **Negative** | Metabo-psychiatric origins |
| Type 2 diabetes | **Negative** | Metabolic component |
| HDL cholesterol | Positive | Metabolic component |
| Physical activity | Positive | Metabolic component |
| Education years | Positive | Cognitive component |

### Epigenetic Information

Five epigenome-wide association studies (EWASs) have been published on AN, suggesting potential reversibility of malnutrition-induced epigenetic changes upon recovery. Differential DNA methylation may serve as a biomarker for disease status or early diagnosis and may be involved in disease chronification ([PMID: 38849516](https://pubmed.ncbi.nlm.nih.gov/38849516/)). The field remains nascent, with most studies limited by small sample sizes and candidate gene approaches ([PMID: 30353170](https://pubmed.ncbi.nlm.nih.gov/30353170/)).

### Chromosomal Abnormalities

No specific chromosomal abnormalities are causally linked to AN. Linkage studies have suggested susceptibility loci on chromosomes 1 and 10 for eating disorders broadly ([PMID: 24340712](https://pubmed.ncbi.nlm.nih.gov/24340712/)).

---

## 5. Environmental Information

### Environmental Factors

- **Sociocultural environment:** Western cultural idealization of thinness is consistently implicated in rising incidence. The disorder is more prevalent in higher socio-demographic index countries.
- **Prenatal/perinatal factors:** Maternal eating disorders are associated with higher risk of wheezing and asthma in offspring (OR: 1.25, 95% CI: 1.06–1.47), suggesting intergenerational effects ([PMID: 41330642](https://pubmed.ncbi.nlm.nih.gov/41330642/)).

### Lifestyle Factors

- **Dieting behavior:** Dietary restriction is the most proximal behavioral risk factor
- **Excessive exercise:** Both a symptom and perpetuating factor; athletes in aesthetic sports are at markedly elevated risk ([PMID: 37528996](https://pubmed.ncbi.nlm.nih.gov/37528996/))
- **Sleep disruption:** Bidirectional causal relationships between insomnia/sleep traits and AN identified via Mendelian randomization ([PMID: 38703603](https://pubmed.ncbi.nlm.nih.gov/38703603/))

### Infectious Agents

AN is not caused by infectious agents. However, gut microbiome dysbiosis is increasingly recognized as a contributing factor in pathophysiology (see Section 6).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**Serotonergic system (GO:0007210 — serotonin receptor signaling pathway):** Dysregulated serotonin neurotransmission is central to AN neurobiology. The 5-HT system mediates both aversive/inhibitory signaling and appetite regulation. As described: *"Restricted eating may be a means of reducing negative mood caused by skewed interactions between serotonin aversive or inhibitory and dopamine reward systems"* ([PMID: 23333342](https://pubmed.ncbi.nlm.nih.gov/23333342/)).

**Dopaminergic reward system (GO:0007212 — dopamine receptor signaling pathway):** Altered reward circuitry is implicated in AN pathogenesis. Hyperdopaminergic mice show augmented vulnerability to activity-based anorexia (ABA), and reward deficits may underlie the paradoxical food avoidance seen in AN ([PMID: 33768216](https://pubmed.ncbi.nlm.nih.gov/33768216/); [PMID: 28475260](https://pubmed.ncbi.nlm.nih.gov/28475260/)).

**Opioid system:** β-endorphin (a POMC gene product) is elevated in female mice undergoing ABA, and mu opioid receptor activation promotes food anticipatory activity, a key ABA feature ([PMID: 33661571](https://pubmed.ncbi.nlm.nih.gov/33661571/)).

**Adrenergic system:** Catecholamine dysregulation is involved in AN pathophysiology; catecholamine levels may be higher in AN patients than in healthy controls, with higher norepinephrine concentrations in adipose tissue suggesting local sympathetic nervous system dominance ([PMID: 37691603](https://pubmed.ncbi.nlm.nih.gov/37691603/); [PMID: 38310530](https://pubmed.ncbi.nlm.nih.gov/38310530/)).

**Endocannabinoid system:** Peripheral cannabinoid signaling is disrupted in AN, affecting both central appetite regulation and peripheral metabolic processes in adipose tissue, liver, pancreas, and skeletal muscle ([PMID: 29437028](https://pubmed.ncbi.nlm.nih.gov/29437028/)).

### Endocrine Dysregulation

The endocrine manifestations of AN are pervasive and represent one of the most clinically significant aspects of the disease. As comprehensively reviewed: *"Dysfunction of the hypothalamic-pituitary axis includes hypogonadotropic hypogonadism with relative oestrogen and androgen deficiency, growth hormone resistance, hypercortisolaemia, non-thyroidal illness syndrome, hyponatraemia and hypooxytocinaemia. Serum levels of leptin, an anorexigenic adipokine, are suppressed and levels of ghrelin, an orexigenic gut peptide, are elevated in women with anorexia nervosa; however, levels of peptide YY, an anorexigenic gut peptide, are paradoxically elevated"* ([PMID: 27811940](https://pubmed.ncbi.nlm.nih.gov/27811940/)).

**Causal chain:**
```
Chronic energy restriction
    → Reduced adipose tissue → Suppressed leptin (CHEBI:81571)
    → Hypothalamic dysfunction
        → Decreased GnRH → Hypogonadotropic hypogonadism → Amenorrhea + Bone loss
        → Increased CRH → Hypercortisolaemia → Bone loss + Immune suppression
        → GH resistance → Low IGF-1 → Growth impairment
        → Decreased T3 → Non-thyroidal illness → Reduced metabolic rate
    → Gut peptide dysregulation → Elevated ghrelin + Paradoxical elevated PYY
    → Autonomic dysfunction → Sympathetic dysregulation in adipose tissue
```

### Gut Microbiome

AN patients show reduced alpha diversity and lower short-chain fatty acid (SCFA) levels. Dysbiosis affects immune system responses, intestinal permeability, and neurotransmitter production via the gut-brain axis ([PMID: 33416044](https://pubmed.ncbi.nlm.nih.gov/33416044/); [PMID: 33652962](https://pubmed.ncbi.nlm.nih.gov/33652962/)). Interestingly, recent evidence challenges the "leaky gut" concept in adolescent AN: zonulin and lipopolysaccharide-binding protein (LBP) levels are decreased rather than increased, suggesting reduced rather than increased paracellular intestinal permeability, and these alterations persist despite weight recovery ([PMID: 40789230](https://pubmed.ncbi.nlm.nih.gov/40789230/)).

Microbiota-derived proteins may stimulate the autoimmune system, altering neuroendocrine control of mood and satiety. Microbial richness increases upon weight regain or fecal microbiota transplantation ([PMID: 33416044](https://pubmed.ncbi.nlm.nih.gov/33416044/)).

### Metabolic Changes

- **Energy metabolism:** Resting energy expenditure is very low in underweight patients but increases dramatically early in refeeding ([PMID: 16721178](https://pubmed.ncbi.nlm.nih.gov/16721178/))
- **Lipid metabolism:** Paradoxical hypercholesterolemia in acute illness; cholesterol levels are higher in females than males and correlate with severity of malnutrition ([PMID: 37864342](https://pubmed.ncbi.nlm.nih.gov/37864342/))
- **Bone metabolism:** Decreased bone formation, increased bone resorption; osteoporosis affects up to 50% of patients and may be irreversible ([PMID: 38380189](https://pubmed.ncbi.nlm.nih.gov/38380189/))

### Brain Structure and Function

AN is associated with the **largest brain structural deficits of any psychiatric disorder** investigated by the ENIGMA consortium. A coordinated analysis of 685 AN patients and 963 controls revealed: *"In AN, reductions in cortical thickness, subcortical volumes, and, to a lesser extent, cortical surface area were sizable (Cohen's d up to 0.95), widespread, and colocalized with hub regions"* ([PMID: 36031441](https://pubmed.ncbi.nlm.nih.gov/36031441/)).

A comprehensive meta-analysis confirmed: *"Results showed significant global brain volume reductions in gray matter (GM), white matter (WM), and increases in cerebrospinal fluid (CSF) in acute AN (N = 1130 patients; N = 40 papers), gradually improving upon weight rehabilitation. However, even after 1.5 years of recovery, significantly lower global GM volume compared to healthy controls was found"* ([PMID: 41619402](https://pubmed.ncbi.nlm.nih.gov/41619402/)).

Key affected brain regions include the bilateral anterior and median cingulate cortex, with decreased both gray matter volume and resting-state functional activity ([PMID: 34296492](https://pubmed.ncbi.nlm.nih.gov/34296492/)). The hippocampus shows volumetric and functional impairments contributing to memory and learning deficits ([PMID: 33176113](https://pubmed.ncbi.nlm.nih.gov/33176113/)).

**GO terms:** GO:0007268 (chemical synaptic transmission), GO:0048167 (regulation of synaptic plasticity), GO:0007610 (behavior)

**Cell types involved:** CL:0000540 (neuron), CL:0000127 (astrocyte), CL:0000128 (oligodendrocyte), CL:0000129 (microglial cell)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organs:**
- **Brain** (UBERON:0000955): Gray matter volume reduction, cortical thinning, white matter changes
- **Bone** (UBERON:0001474): Osteopenia/osteoporosis; up to 50% of patients affected
- **Heart** (UBERON:0000948): Bradycardia, arrhythmias, QTc prolongation
- **Endocrine glands** (hypothalamus, pituitary, thyroid, adrenal, gonads): Global endocrine dysregulation

**Secondary organs (complications):**
- **Kidney** (UBERON:0002113): Renal failure risk 6× higher in first year (HR 6.0, 95% CI: 4.2–8.5) ([PMID: 41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/))
- **Liver** (UBERON:0002107): Liver disease risk 6.7× higher in first year (HR 6.7, 95% CI: 3.8–11.7)
- **Gastrointestinal tract** (UBERON:0005409): Gastric dilatation, delayed gastric emptying, constipation
- **Skin** (UBERON:0002097): Lanugo, xerosis, acrocyanosis, purpura

**Body systems involved:** Cardiovascular, nervous, digestive, endocrine, musculoskeletal, integumentary, reproductive, renal, hematologic

### Tissue and Cell Level

- Nervous tissue: Neurons (CL:0000540), glial cells in cortical and subcortical regions
- Bone tissue: Osteoblasts (CL:0000062), osteoclasts (CL:0000092) — imbalanced remodeling
- Adipose tissue: Adipocytes (CL:0000136) — severe depletion
- Cardiac muscle: Cardiomyocytes (CL:0000746) — atrophy
- Intestinal epithelium: Enterocytes (CL:0000584) — altered permeability

### Brain Localization (UBERON terms)

- Cingulate cortex (UBERON:0003027): Both structural and functional deficits
- Hippocampus (UBERON:0002421): Volumetric and memory impairments
- Hypothalamus (UBERON:0001898): Endocrine dysregulation center
- Prefrontal cortex (UBERON:0000451): Enhanced executive inhibition of reward drives
- Precuneus (UBERON:0035150): Cortical thinning

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Adolescence (10–20 years); cumulative lifetime prevalence analysis shows the majority of eating disorders have initial onset in this window ([PMID: 19427647](https://pubmed.ncbi.nlm.nih.gov/19427647/))
- **Onset pattern:** Usually insidious, beginning with dietary restriction that progressively intensifies
- **Prolonged emotional distress** typically precedes symptom onset, with opportunities for early prevention/intervention often missed ([PMID: 41236167](https://pubmed.ncbi.nlm.nih.gov/41236167/))

### Progression

- **Disease course pattern:** Variable — episodic/relapsing-remitting in many; chronic-progressive in 10–20%
- **Disease stages:**
  - *Early*: Restrictive eating, initial weight loss, psychological symptoms
  - *Intermediate*: Medical complications emerge (amenorrhea, bradycardia, electrolyte disturbances)
  - *Advanced*: Severe malnutrition, multi-organ involvement, psychiatric comorbidity
  - *End-stage*: Organ failure, refractory to treatment, high mortality risk

### Long-term Outcomes

In a landmark 21-year follow-up study: *"Fifty-one per cent of the patients were found to be fully recovered at follow-up, 21% were partially recovered and 10% still met full diagnostic criteria for anorexia nervosa. Sixteen per cent were deceased, due to causes related to anorexia nervosa. The standardized mortality rate was 9.8"* ([PMID: 11459385](https://pubmed.ncbi.nlm.nih.gov/11459385/)).

A 13-year follow-up of 484 patients found 60.3% recovered, 25.8% relatively good outcome, and 6.4% each with bad and severe outcomes. Recovery rate increased with elapsing relapse-free time (p=0.02) ([PMID: 21317006](https://pubmed.ncbi.nlm.nih.gov/21317006/)).

### Critical Periods

- **Adolescence (10–19 years):** Primary window of vulnerability and optimal intervention
- **Transition from adolescent to adult services:** Risk of discontinuity in care ([PMID: 33223229](https://pubmed.ncbi.nlm.nih.gov/33223229/))
- **First 2 years of illness:** Key predictors of long-term outcome established; early response to treatment predicts better outcomes

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---------|-------|--------|
| Lifetime prevalence (women) | 0.48–1.4% | [PMID: 19427647](https://pubmed.ncbi.nlm.nih.gov/19427647/); [PMID: 41366465](https://pubmed.ncbi.nlm.nih.gov/41366465/) |
| Lifetime prevalence (men) | ~0.2% | [PMID: 41366465](https://pubmed.ncbi.nlm.nih.gov/41366465/) |
| Incidence | Increasing globally | Multiple sources |
| Sex ratio (F:M) | ~8–10:1 | Population registries |

### Inheritance Pattern

AN follows a **multifactorial/polygenic** inheritance pattern. Key genetic architecture features:

- **Heritability:** 48–74% (twin studies); moderate heritability confirmed in population-level register data from Denmark and Sweden covering >67,000 individuals with eating disorders ([PMID: 40615413](https://pubmed.ncbi.nlm.nih.gov/40615413/))
- **Penetrance:** Incomplete and age-dependent
- **Expressivity:** Highly variable — spectrum from subclinical features to life-threatening illness
- **Polygenicity:** Estimated ~11,500 variants explain 90% of genetic heritability

### Population Demographics

- **Sex distribution:** Predominantly female; however, male cases are likely underdiagnosed and males with EDs have unmet needs ([PMID: 34246009](https://pubmed.ncbi.nlm.nih.gov/34246009/))
- **Ethnic/racial disparities:** Latinx and Asian patients are half as likely as White patients to receive recommended treatment (aOR 0.49 and 0.55, respectively) ([PMID: 36694235](https://pubmed.ncbi.nlm.nih.gov/36694235/))
- **Geographic distribution:** Higher prevalence in Western/high-income countries, but increasingly recognized globally
- **Insurance disparities:** Publicly insured patients are one-third as likely to receive recommended treatment ([PMID: 36694235](https://pubmed.ncbi.nlm.nih.gov/36694235/))

---

## 10. Diagnostics

### Clinical Criteria

**DSM-5 Diagnostic Criteria (307.1):**
1. Restriction of energy intake relative to requirements, leading to significantly low body weight
2. Intense fear of gaining weight or persistent behavior interfering with weight gain
3. Disturbance in the way body weight or shape is experienced

**Subtypes:**
- Restricting type (AN-R)
- Binge-eating/purging type (AN-BP)

**Severity based on BMI:**
- Mild: BMI ≥ 17 kg/m²
- Moderate: BMI 16–16.99 kg/m²
- Severe: BMI 15–15.99 kg/m²
- Extreme: BMI < 15 kg/m²

Latent class analysis has empirically identified four phenotypic classes, with obsessive-compulsive features differentiating among restricting AN subgroups ([PMID: 14757596](https://pubmed.ncbi.nlm.nih.gov/14757596/)).

### Laboratory Tests

| Test | Purpose | Key Findings |
|------|---------|--------------|
| Complete metabolic panel | Electrolyte screening | Hypokalemia, hyponatremia, hypophosphatemia |
| Magnesium, phosphate | Refeeding syndrome risk | Often depleted |
| CBC | Hematologic status | Anemia, leukopenia, thrombocytopenia |
| Thyroid function | Endocrine assessment | Low T3 (non-thyroidal illness) |
| Gonadotropins, estradiol | Reproductive function | Low (hypogonadotropic hypogonadism) |
| Cortisol | HPA axis assessment | Elevated |
| IGF-1 | Growth/nutritional status | Low (GH resistance) |
| ECG | Cardiac monitoring | Bradycardia, QTc prolongation |
| DXA / REMS | Bone density | Osteopenia/osteoporosis |

REMS (Radiofrequency echographic multispectrometry) shows good agreement with DXA for BMD assessment in AN and may be particularly useful during fertile age and pregnancy ([PMID: 35896857](https://pubmed.ncbi.nlm.nih.gov/35896857/)).

### Imaging Studies

- **Brain MRI:** May reveal gray matter volume reductions and cortical thinning; lower brain volumes of the cerebellum and subcortical gray matter at admission predict worse outcomes ([PMID: 37263169](https://pubmed.ncbi.nlm.nih.gov/37263169/))
- **PET/SPECT:** Research tools for serotonergic and dopaminergic receptor density mapping; clinical utility not established ([PMID: 32234640](https://pubmed.ncbi.nlm.nih.gov/32234640/))

### Screening Tools

- **SCOFF questionnaire:** Brief 5-question screening tool
- **EAT-26 (Eating Attitudes Test):** 26-item self-report measure
- **EDI-2 (Eating Disorder Inventory):** Comprehensive psychometric assessment
- **Electrolyte monitoring:** Otherwise unexplained electrolyte abnormalities may identify individuals who benefit from ED screening ([PMID: 36346630](https://pubmed.ncbi.nlm.nih.gov/36346630/))

### Genetic Testing

Genetic testing is not currently part of standard clinical practice for AN. However, the Eating Disorders Genetics Initiative 2 (EDGI2) is advancing polygenic risk scoring that may eventually enable risk stratification ([PMID: 40419993](https://pubmed.ncbi.nlm.nih.gov/40419993/)).

### Differential Diagnosis

- Bulimia nervosa (binge-purge without low weight)
- Avoidant/restrictive food intake disorder (ARFID) (no body image distortion)
- Binge eating disorder
- Major depressive disorder with appetite loss
- Medical conditions causing weight loss (malignancy, Crohn's disease, hyperthyroidism, Addison's disease)
- Body dysmorphic disorder (significantly higher delusionality than AN) ([PMID: 41707619](https://pubmed.ncbi.nlm.nih.gov/41707619/))

---

## 11. Outcome/Prognosis

### Mortality

AN has the **highest mortality rate of all mental disorders**:

| Measure | Value | Source |
|---------|-------|--------|
| All-cause mortality RR vs. general population | 5.52 (95% CI: 4.47–6.82) | [PMID: 41536100](https://pubmed.ncbi.nlm.nih.gov/41536100/) |
| Suicide-related mortality RR | 9.86 (95% CI: 5.63–17.27) | [PMID: 41536100](https://pubmed.ncbi.nlm.nih.gov/41536100/) |
| Mortality at 21-year follow-up | 16% | [PMID: 11459385](https://pubmed.ncbi.nlm.nih.gov/11459385/) |
| All-cause mortality HR (first year) | 4.6 (95% CI: 3.1–7.0) | [PMID: 41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/) |
| Suicide HR (first year) | 13.7 (95% CI: 4.8–38.8) | [PMID: 41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/) |

Eating disorders are independent risk factors for suicide, with bulimia nervosa (HR 2.59) and other eating disorders (HR 2.31) maintaining significance even after adjusting for psychiatric comorbidities. For AN specifically, the association became non-significant after adjustment for comorbid psychiatric conditions ([PMID: 40280427](https://pubmed.ncbi.nlm.nih.gov/40280427/)).

Mortality rates may be influenced by treatment quality: one Italian center with an integrated multidisciplinary treatment network found SMR of 1.19 (95% CI: 0.79–1.81), not significantly different from the general population ([PMID: 36062404](https://pubmed.ncbi.nlm.nih.gov/36062404/)).

### Recovery and Long-term Outcomes

| Timeframe | Full Recovery | Partial Recovery | Active AN | Deceased |
|-----------|--------------|------------------|-----------|----------|
| 13-year follow-up (N=484) | 60.3% | 25.8% | 6.4% (bad) + 6.4% (severe) | 1.2% |
| 21-year follow-up | 51% | 21% | 10% | 16% |

### Prognostic Factors

**Poor prognostic factors:**
- Low BMI at discharge
- Low energy and fat intake
- High drive for excessive exercise
- High perfectionism and interpersonal distrust
- High anxiety
- Psychiatric comorbidity
- Binge/purge subtype transition
- Higher levels of depression and compulsivity ([PMID: 17628126](https://pubmed.ncbi.nlm.nih.gov/17628126/))
- Lower brain volumes at admission ([PMID: 37263169](https://pubmed.ncbi.nlm.nih.gov/37263169/))
- Older age at onset

**Favorable prognostic factors:**
- Adolescent age at treatment
- Early symptom improvement
- Maintaining contact with mother
- Shorter duration of illness before treatment
- Higher pre-treatment BMI ([PMID: 37697396](https://pubmed.ncbi.nlm.nih.gov/37697396/))

### Complications

Within 10 years of diagnosis, patients experience excess adverse outcomes ([PMID: 41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/)):
- 110 excess renal failure events per 10,000 individuals
- 26 excess liver disease events per 10,000 individuals
- 95 excess all-cause deaths per 10,000 individuals
- 341 excess unnatural deaths per 100,000 individuals

---

## 12. Treatment

### Psychotherapy (First-line)

**Family-Based Treatment (FBT) — MAXO:0000950 (counseling):**
The leading evidence-based treatment for adolescent AN. *"In 5 randomized controlled trials (RCTs) in anorexia nervosa (N=560) remission rates were between 21.2-42% at end of treatment, between 21.8-40% at 6-month follow-up, and between 29-49% at 12-month follow-up"* ([PMID: 31466116](https://pubmed.ncbi.nlm.nih.gov/31466116/)).

In a naturalistic Finnish study, 61.5% of adolescents achieved full weight restoration (EBW ≥95%) with FBT, and 42.3% required no further treatment ([PMID: 37697396](https://pubmed.ncbi.nlm.nih.gov/37697396/)).

**Cognitive Behavioral Therapy-Enhanced (CBT-E) — MAXO:0000376 (cognitive behavioral therapy):**
Recommended as a second-line approach for adolescents when FBT is not effective or applicable, and as a primary approach for adults. CBT-E shows moderate to large effect sizes regardless of previous FBT failure ([PMID: 30829421](https://pubmed.ncbi.nlm.nih.gov/30829421/); [PMID: 33223229](https://pubmed.ncbi.nlm.nih.gov/33223229/)).

### Pharmacotherapy

**No medications are currently FDA-approved specifically for AN.** Key pharmacological considerations:

| Medication | Evidence | Notes |
|------------|----------|-------|
| Olanzapine | Weekly weight gain 0.898 vs. 0.677 kg (p=0.004) | Promising adjunctive treatment; *"The OLZ group achieved greater weekly weight gain (0.898 vs. 0.677 kg, p = 0.004)"* ([PMID: 40879610](https://pubmed.ncbi.nlm.nih.gov/40879610/)) |
| Fluoxetine | Limited evidence for relapse prevention | Not effective for acute weight restoration |
| Dronabinol | Promising preliminary results | Cannabinoid receptor agonist |
| SSRIs | For comorbid depression | Not for core AN symptoms |
| Teriparatide | Trends in improved bone structure (IT cortical thickness +13%) | For AN-related osteoporosis ([PMID: 41591404](https://pubmed.ncbi.nlm.nih.gov/41591404/)) |
| Romosuzumab | Significant BMD increase in case report | Novel anti-sclerostin antibody for AN osteoporosis ([PMID: 39314548](https://pubmed.ncbi.nlm.nih.gov/39314548/)) |

### Nutritional Rehabilitation (MAXO:0001298 — dietary modification)

Weight gain of 2.2–4.4 lb per week stabilizes cardiovascular health ([PMID: 33382560](https://pubmed.ncbi.nlm.nih.gov/33382560/)). Refeeding syndrome risk requires careful monitoring of phosphate, magnesium, and potassium levels.

### Hospitalization (MAXO:0010363 — inpatient care)

Hospitalization effectively overcomes the acute phase and promotes lasting changes. A multidisciplinary approach comprising clinical/nutritional, psychotherapeutic, family, occupational, and body therapy components is recommended ([PMID: 12452251](https://pubmed.ncbi.nlm.nih.gov/12452251/)).

### Treatment Strategy and Future Directions

- **Integrated multidisciplinary networks** may significantly reduce mortality ([PMID: 36062404](https://pubmed.ncbi.nlm.nih.gov/36062404/))
- **GLP-1 receptor agonists** are being investigated via Mendelian randomization for potential effects on AN ([PMID: 40141382](https://pubmed.ncbi.nlm.nih.gov/40141382/))
- **Psychedelic-assisted therapy**, novel monoaminergic drugs, and hormone analogues are emerging areas of investigation ([PMID: 32858054](https://pubmed.ncbi.nlm.nih.gov/32858054/))
- **Probiotics and microbiome-targeted therapies** show early promise for restoring gut-brain axis function ([PMID: 33652962](https://pubmed.ncbi.nlm.nih.gov/33652962/))

---

## 13. Prevention

### Primary Prevention

- **Media literacy programs** to counter thin-ideal internalization
- **Body image education** emphasizing positive body focus rather than weight/dieting ([PMID: 33382560](https://pubmed.ncbi.nlm.nih.gov/33382560/))
- **Family support programs** for building healthy emotion regulation skills
- **Athlete screening:** Targeted prevention in aesthetic sports populations ([PMID: 37528996](https://pubmed.ncbi.nlm.nih.gov/37528996/))

### Secondary Prevention (Early Detection)

- **Electrolyte screening:** Unexplained electrolyte abnormalities in adolescents should prompt ED assessment ([PMID: 36346630](https://pubmed.ncbi.nlm.nih.gov/36346630/))
- **BMI trend monitoring:** Subtle weight changes should be investigated in primary care ([PMID: 33382560](https://pubmed.ncbi.nlm.nih.gov/33382560/))
- **Web-based parent interventions:** The E@T program showed significant increase in expected body weight at 12-month follow-up (Cohen d=0.42), though parent adherence was low ([PMID: 30552078](https://pubmed.ncbi.nlm.nih.gov/30552078/))

### Tertiary Prevention

- Long-term psychiatric monitoring, as 6% of treated patients attempt suicide even years after initial treatment ([PMID: 35142161](https://pubmed.ncbi.nlm.nih.gov/35142161/))
- Ongoing bone density monitoring and treatment
- Relapse prevention through continued therapeutic support; relapse risk declines after 4 years symptom-free ([PMID: 9054777](https://pubmed.ncbi.nlm.nih.gov/9054777/))

### Genetic Counseling

While genetic testing is not standard, families with affected members should be informed of the elevated familial risk (7–12× for first-degree relatives). The EDGI2 initiative may eventually enable polygenic risk-based screening ([PMID: 40419993](https://pubmed.ncbi.nlm.nih.gov/40419993/)).

---

## 14. Other Species / Natural Disease

### Animal Models of Relevance

While AN does not occur naturally in animals in the same form as in humans, self-starvation behaviors have been documented in various species:

- **Activity-based anorexia (ABA) in rodents:** The most widely used animal model, in which rats or mice with unlimited running wheel access and restricted food availability develop paradoxical hypophagia, hyperactivity, and life-threatening weight loss, recapitulating key features of human AN including hypothermia and anhedonia ([PMID: 28475260](https://pubmed.ncbi.nlm.nih.gov/28475260/); [PMID: 38103992](https://pubmed.ncbi.nlm.nih.gov/38103992/))

### Comparative Biology

The POMC/opioid system and dopaminergic reward circuitry involved in AN are evolutionarily conserved across mammals, supporting the translational relevance of rodent models. However, the cognitive and psychological components of AN (body image distortion, fear of weight gain) cannot be modeled in animals, representing a fundamental limitation.

---

## 15. Model Organisms

### Activity-Based Anorexia (ABA) Model

**Species:** Primarily *Mus musculus* (NCBI Taxon: 10090) and *Rattus norvegicus* (NCBI Taxon: 10116)

**Protocol:** Combining limited food access with unlimited running wheel access produces paradoxical decrease in food intake, hyperactivity, and life-threatening weight loss ([PMID: 34124309](https://pubmed.ncbi.nlm.nih.gov/34124309/)).

**Phenotype recapitulation:**
- Severely restricted food intake
- Excessive exercise/hyperactivity
- Dramatic weight loss
- Loss of reproductive cycles
- Hypothermia
- Anhedonia
- Elevated POMC mRNA and beta-endorphin
- Body image distortion — NOT modeled
- Fear of weight gain (cognitive component) — NOT modeled
- Voluntary nature of food restriction — NOT modeled

### Genetic Models

| Model | Key Finding | Reference |
|-------|------------|-----------|
| Hyperdopaminergic mice | Increased dopamine augments ABA vulnerability | [PMID: 33768216](https://pubmed.ncbi.nlm.nih.gov/33768216/) |
| MOR knockout mice | Blunted food anticipatory activity in both sexes | [PMID: 33661571](https://pubmed.ncbi.nlm.nih.gov/33661571/) |
| BDNF Val68Met rats | No effect on ABA susceptibility or feeding behavior | [PMID: 35625351](https://pubmed.ncbi.nlm.nih.gov/35625351/) |
| C57BL/6 vulnerability/resilience | Resilient mice show adaptive food intake increase and weight stabilization | [PMID: 34124309](https://pubmed.ncbi.nlm.nih.gov/34124309/) |

**Research applications:** The ABA model enables investigation of neurobiological mechanisms, pharmacological interventions, genetic susceptibility factors, and the distinction between vulnerable and resilient phenotypes ([PMID: 38103992](https://pubmed.ncbi.nlm.nih.gov/38103992/)).

---

## Key Findings — Detailed Evidence

### Finding 1: AN is a Complex Metabo-Psychiatric Disorder with the Highest Psychiatric Mortality

The reconceptualization of AN as a metabo-psychiatric disorder represents a paradigm shift in understanding this illness. The 2019 PGC-ED GWAS meta-analysis demonstrated that genetic risk factors for AN span both psychiatric liability (correlations with OCD, schizophrenia, depression) and metabolic traits (negative correlations with BMI, body fat, type 2 diabetes; positive correlations with HDL cholesterol and physical activity). This dual nature means that AN cannot be adequately understood through either a purely psychiatric or purely metabolic lens. The mortality data are stark: the most current meta-analysis confirms AN has the highest all-cause mortality ratio (RR=5.52) and suicide-related mortality (RR=9.86) of all eating disorders and indeed all mental illnesses.

### Finding 2: Global Endocrine Dysregulation

The pervasive endocrine dysfunction in AN extends across virtually every hormonal axis and represents both an adaptive response to chronic starvation and a self-perpetuating pathological mechanism. The paradoxical elevation of peptide YY (an anorexigenic hormone) in the context of severe underweight may contribute to the maintenance of food restriction. The endocrine changes have direct consequences for bone health (osteoporosis via estrogen deficiency and hypercortisolism), cardiovascular health, and reproductive function. Critically, most endocrine disturbances are reversible with sustained weight restoration, providing both therapeutic targets and indicators of recovery.

### Finding 3: Brain Structural Deficits

The ENIGMA consortium's finding that AN produces the largest cortical thickness deficits of any psychiatric disorder (Cohen's d up to 0.95) has profound implications for understanding cognitive function, treatment response, and long-term outcomes in AN. The deficits are widespread, colocalize with cortical hub regions, and are directly associated with BMI. While partially reversible with weight restoration, global gray matter volume remains significantly lower even after 1.5 years of recovery, suggesting some degree of lasting neural impact. Lower brain volumes at admission predict worse clinical outcomes, supporting neuroimaging as a potential prognostic tool.

### Finding 4: Family-Based Treatment Efficacy and Treatment Landscape

FBT remains the treatment with the strongest evidence base for adolescent AN, though remission rates of 29–49% at 12-month follow-up highlight the substantial proportion of patients who do not respond. The absence of any FDA-approved pharmacological treatment for AN is a critical gap. Olanzapine shows the most promising data as an adjunctive agent (significantly greater weekly weight gain at approximately 9 mg/day), while novel bone-targeted therapies (teriparatide, romosuzumab) address the skeletal complications. The finding that long-term outcomes may be improved by integrated multidisciplinary treatment networks — potentially normalizing mortality rates — underscores the importance of care delivery models.

---

## Mechanistic Model

```
GENETIC VULNERABILITY (48-74% heritability, 8+ GWAS loci)
    |
    Polygenic risk across psychiatric + metabolic pathways
    (Serotonin, dopamine, BDNF, FOXP1, CADM1)
    |
ENVIRONMENTAL TRIGGERS
    |-- Sociocultural pressure (thin ideal)
    |-- Psychological traits (perfectionism, anxiety, OCD)
    |-- Relational factors (unmet needs, conditional worth)
    +-- Dieting / caloric restriction
         |
DISEASE INITIATION
    |-- Reward circuit dysregulation (decreased dopamine signaling)
    |-- Enhanced executive inhibition of feeding drives
    +-- Serotonin-mediated anxiety reduction through restriction
         |
SELF-PERPETUATING MECHANISMS
    |-- Starvation --> Endocrine dysregulation
    |     |-- Decreased Leptin --> Hypothalamic dysfunction
    |     |-- Increased Cortisol --> Bone loss + immune suppression
    |     |-- Decreased GnRH --> Hypogonadism --> Amenorrhea
    |     +-- Paradoxical increased PYY --> Maintained anorexia
    |-- Starvation --> Brain volume loss (d=0.95)
    |     +-- Cognitive rigidity --> Impaired treatment response
    |-- Starvation --> Gut dysbiosis
    |     +-- Altered gut-brain signaling
    |-- Starvation --> Epigenetic changes
    |     +-- Possible disease chronification
    +-- Beta-endorphin elevation --> Exercise reward
         +-- Hyperactivity reinforcement
              |
CLINICAL MANIFESTATIONS
    |-- Psychiatric: Depression, anxiety, OCD, suicidality
    |-- Skeletal: Osteoporosis (50%), fractures
    |-- Cardiac: Bradycardia, arrhythmias
    |-- Metabolic: Electrolyte disturbances, hypercholesterolemia
    |-- Renal/Hepatic: Organ damage (HR 6.0-6.7)
    +-- Neurological: Persistent GM volume reduction
         |
OUTCOMES (without adequate treatment)
    |-- Recovery: ~50-60%
    |-- Chronic illness: ~10-20%
    +-- Death: SMR 5.52 (highest of all psychiatric disorders)
```

---

## Evidence Base

### Landmark Studies

| Study | PMID | Contribution |
|-------|------|-------------|
| PGC-ED GWAS (Watson et al., 2019) | [31308545](https://pubmed.ncbi.nlm.nih.gov/31308545/) | Identified 8 risk loci; established metabo-psychiatric paradigm |
| ENIGMA-ED Brain Structure (2022) | [36031441](https://pubmed.ncbi.nlm.nih.gov/36031441/) | Largest cortical thickness deficits of any psychiatric disorder |
| Mortality Meta-Analysis (2025) | [41536100](https://pubmed.ncbi.nlm.nih.gov/41536100/) | Definitive mortality data: SMR 5.52, suicide RR 9.86 |
| Endocrine Review (Misra and Klibanski, 2014) | [27811940](https://pubmed.ncbi.nlm.nih.gov/27811940/) | Comprehensive endocrine characterization |
| FBT Systematic Review (2019) | [31466116](https://pubmed.ncbi.nlm.nih.gov/31466116/) | Treatment efficacy data: remission 29-49% at 12 months |
| 21-Year Follow-up (Zipfel et al., 2000) | [11459385](https://pubmed.ncbi.nlm.nih.gov/11459385/) | Long-term outcomes: 51% recovery, 16% mortality |
| Brain Volume Meta-Analysis (2025) | [41619402](https://pubmed.ncbi.nlm.nih.gov/41619402/) | Persistent GM volume reduction after 1.5 years recovery |
| Adverse Outcomes Cohort (2025) | [41282513](https://pubmed.ncbi.nlm.nih.gov/41282513/) | Multi-organ adverse outcome quantification |
| Cross-Disorder Genetics (2019) | [31835028](https://pubmed.ncbi.nlm.nih.gov/31835028/) | 109 shared loci across 8 psychiatric disorders |
| Genetic Correlations with Body Composition (2019) | [31852892](https://pubmed.ncbi.nlm.nih.gov/31852892/) | AN causal for decreased fat mass via MR |

---

## Limitations and Knowledge Gaps

1. **Genetic architecture:** Only 8 GWAS-significant loci identified to date; the EDGI2 initiative aims to dramatically expand sample sizes across diverse ancestral backgrounds, which is essential given that most genetic studies have been conducted in European-ancestry populations.

2. **Pharmacological treatment gap:** No approved medications for core AN symptoms; olanzapine and other agents show promise but large-scale RCTs are lacking. The network meta-analysis protocol (EfaNosa, [PMID: 41366465](https://pubmed.ncbi.nlm.nih.gov/41366465/)) will provide the first systematic comparison of all available treatments.

3. **Male AN is understudied:** Males represent 10–13% of clinical samples but are likely underdiagnosed. Mortality and morbidity data for males are limited due to small sample sizes ([PMID: 34246009](https://pubmed.ncbi.nlm.nih.gov/34246009/)).

4. **Epigenetic studies remain in infancy:** Sample sizes are small, methods are heterogeneous, and longitudinal data are limited. Whether epigenetic changes are causes, consequences, or biomarkers of illness remains unclear ([PMID: 38849516](https://pubmed.ncbi.nlm.nih.gov/38849516/)).

5. **Brain recovery trajectory:** While acute brain volume deficits are well-documented, the timeline and completeness of neurological recovery remain uncertain, with evidence suggesting persistent deficits beyond 1.5 years of recovery.

6. **Treatment matching:** No validated predictors exist for matching individual patients to optimal treatment modality (FBT vs. CBT-E vs. other approaches).

7. **Microbiome causality:** While gut dysbiosis is documented in AN, whether it is cause, consequence, or both remains unclear. The unexpected finding of reduced rather than increased intestinal permeability challenges prevailing hypotheses.

8. **Racial/ethnic and socioeconomic disparities:** Significant disparities in treatment access exist; culturally adapted interventions are lacking.

---

## Proposed Follow-up Experiments/Actions

1. **Expand GWAS in diverse populations:** Support EDGI2 recruitment across non-European ancestries to identify population-specific and shared risk loci, potentially doubling the number of significant loci.

2. **Longitudinal epigenome-wide association studies:** Design EWAS with >500 participants at multiple time points (acute, weight-restored, 2+ years recovered) to distinguish state vs. trait epigenetic markers and identify biomarkers for relapse risk.

3. **RCT comparing FBT vs. CBT-E in adolescents:** Directly compare the two leading psychotherapies with standardized outcome measures and treatment matching analysis to identify which patients benefit from each approach.

4. **Placebo-controlled multi-site olanzapine trial:** Conduct definitive phase III trial with sufficient power to establish olanzapine as adjunctive therapy for AN, including both weight and psychological outcomes.

5. **Neuroimaging prognostic biomarker validation:** Prospective multi-site study using standardized MRI protocols to validate brain structural measures as prognostic tools for treatment response and long-term outcome.

6. **Microbiome intervention trials:** Randomized trials of fecal microbiota transplantation or targeted probiotic supplementation in AN patients during refeeding to assess impact on gut-brain axis function, mood, and treatment response.

7. **Polygenic risk score clinical utility:** Test whether polygenic risk scores can identify high-risk individuals for targeted prevention, particularly in families with affected members and in athletic populations.

8. **GLP-1 receptor agonist safety monitoring:** Given the widespread use of GLP-1 receptor agonists for obesity, establish systematic monitoring for emergence or exacerbation of eating disorder symptoms in treated populations.

9. **Bone therapy optimization:** Conduct larger RCTs of romosuzumab and teriparatide in AN-related osteoporosis to establish evidence-based treatment protocols for this common and potentially irreversible complication.

10. **Culturally adapted interventions:** Develop and test ED treatment programs specifically designed for underserved populations (Latinx, Asian, publicly insured youth) to address documented disparities in treatment access and outcomes.

---

*Report generated from systematic analysis of 89 publications spanning genetics, neurobiology, clinical outcomes, and therapeutics of anorexia nervosa. All citations verified against PubMed abstracts.*
