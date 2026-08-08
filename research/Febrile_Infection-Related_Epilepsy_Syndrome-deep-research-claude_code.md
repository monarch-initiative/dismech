---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-24T08:10:33.513720'
end_time: '2026-07-24T08:16:29.109515'
duration_seconds: 355.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Febrile Infection-Related Epilepsy Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 10
  num_turns: 18
  total_cost_usd: 2.83275775
  session_id: ad1def07-260d-4201-8e1b-f255bcc97419
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Febrile Infection-Related Epilepsy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Febrile Infection-Related Epilepsy Syndrome** covering all of the
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

Alright, I've got a solid evidence base. Here's the full report.

---

# Research Report: Febrile Infection-Related Epilepsy Syndrome (FIRES)

**Category:** Complex (immune-inflammatory epileptic encephalopathy) · **MONDO:0015584**

> **A curator's up-front warning:** FIRES is *not* a classic Mendelian disorder, and this whole template is built assuming a gene-first disease. Treating FIRES like it has a "causal gene" is like looking for the single ant that started the anthill — it's the wrong altitude. FIRES is best modeled as a **downstream clinical-inflammatory convergence syndrome** riding on top of a normal genome that got tipped over by a fever. I've flagged throughout where the gene-centric sections of this template genuinely don't apply. Where I cite a paper by DOI rather than PMID, I couldn't independently confirm the exact PMID from search — those are marked **(verify PMID before curating a snippet)**, per the anti-hallucination SOP.

---

## 1. Disease Information

FIRES is a rare, catastrophic epileptic encephalopathy in which a previously healthy person — usually a school-age child — develops explosive, drug-resistant **status epilepticus** a few days after a banal, self-limited febrile illness (a cold, a stomach bug). The fever itself is gone or fading by the time the brain catches fire. There's no tumor, no stroke, no obvious infection *in* the brain, no metabolic crash to explain it. The seizures just won't stop, often for weeks to months, and survivors are almost always left with lasting epilepsy and cognitive damage.

The clean way to think about the naming, settled by the **2018 international consensus** (Hirsch et al., *Epilepsia* 2018;59:739–744, [doi:10.1111/epi.14016](https://onlinelibrary.wiley.com/doi/10.1111/epi.14016), **verify PMID**):

- **NORSE** (New-Onset Refractory Status Epilepticus) is the umbrella — a *clinical presentation*, not a diagnosis: refractory SE with no readily identifiable acute structural, toxic, or metabolic cause, in someone without active epilepsy or a relevant prior neurological disorder.
- **FIRES is the subtype of NORSE that requires a preceding febrile infection**, with fever starting **between 2 weeks and 24 hours before** the refractory SE onset. Fever need not be present at SE onset. **FIRES applies to any age** (the consensus deliberately removed the old pediatric-only restriction).
- **Cryptogenic NORSE/FIRES** = the ~50% where no cause is found even after full workup. Most FIRES ends up here.

> Quote (consensus framing, per NORSE Institute summary of Hirsch 2018): *"FIRES is a subtype of NORSE that involves a prior febrile infection, with fever starting between 2 weeks and 24 hours prior to the onset of refractory status epilepticus."*

**Key identifiers:**

| System | ID |
|---|---|
| MONDO | **MONDO:0015584** |
| Orphanet | **ORPHA:163703** |
| ICD-10 | G40.5 (special epileptic syndromes) |
| ICD-11 | 8A63.Y (other specified status epilepticus) |
| GARD | 11005 |
| OMIM | **none** — no Mendelian OMIM entry (consistent with its non-Mendelian nature) |

**Common synonyms / historical names** (worth carrying as `synonyms`, because the older names encode obsolete assumptions):
- Fever-Induced Refractory Epileptic Encephalopathy in School-age children (**FIRES** — the original Nabbout acronym)
- Acute Encephalitis with Refractory Repetitive Partial Seizures (**AERRPS**, Japanese literature)
- Devastating Epileptic Encephalopathy in School-age Children (**DESC**)
- Idiopathic catastrophic epileptic encephalopathy; "new-onset cryptogenic febrile SE"

**Data provenance:** almost entirely **disease-level aggregated** from case reports and small case series — there is no large individual-patient EHR registry, and worldwide only ~on the order of 100+ well-characterized cases have been published. This scarcity is itself a load-bearing fact for every "frequency" and "prevalence" claim below.

Sources: [Orphanet 163703](https://www.orpha.net/en/disease/detail/163703), [NORD](https://rarediseases.org/mondo-disease/febrile-infection-related-epilepsy-syndrome/), [Hirsch 2018 consensus](https://onlinelibrary.wiley.com/doi/10.1111/epi.14016), [Lit review PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/).

---

## 2. Etiology

**Causal factors — the honest answer is "unknown trigger, stereotyped response."** The leading model is that a **nonspecific febrile infection acts as a trigger, not a cause**, unmasking a runaway **innate-immune / autoinflammatory** cascade in the brain. Think of the fever as the match and a primed neuroinflammatory system as the dry grass — the fire's character comes from the grass, not the match. Most likely, per Orphanet, *"FIRES is an immune-inflammatory-mediated epileptic encephalopathy, with a vicious circle of inflammation and hyperexcitability."*

- **Infectious triggers:** many pathogens have been reported preceding FIRES (influenza, HHV-6, enteroviruses, Mycoplasma, respiratory/GI viruses), but **no single organism is consistently found**, and virus is generally *not* recoverable from CSF/brain — arguing against direct viral encephalitis and for a **para-/post-infectious immune mechanism**.
- **Not classic autoimmune encephalitis:** neuronal autoantibodies (anti-NMDAR, etc.) are usually **absent** in cryptogenic FIRES; this distinguishes it from antibody-mediated NORSE, which is a separate branch of the NORSE tree.

**Genetic risk factors:** No causal Mendelian gene. The candidate-gene study by **Appenzeller et al. (2012, *Dev Med Child Neurol*; PMID:23066759)** explicitly showed *"FIRES is not caused by SCN1A, POLG, PCDH19 mutations or rare copy number variations."* What *does* recur is **susceptibility in innate-immune / cytokine genes**:
- **IL1RN** (IL-1 receptor antagonist gene) — a VNTR allele and a risk haplotype were over-represented in FIRES patients vs controls; the index anakinra-responder carried multiple *IL1RN* variants with reduced intracellular IL-1RA expression (**Clarkson et al. 2019, *Ann Neurol*; PMID:30779222**).
- Emerging single reports of rare de novo variants in innate-immune/microglial genes — e.g., a **de novo pathogenic *CSF1R* variant implicating microglial dysfunction** (Fisher et al. 2025, *Epilepsia*, [doi:10.1111/epi.18538](https://onlinelibrary.wiley.com/doi/10.1111/epi.18538), **verify PMID**). These are individual leads, not established causes.

**Environmental / demographic risk factors:** young school age (peak ~7–10 yr), possibly slight male predominance, and simply *having a recent febrile infection*. No occupational/toxic exposures implicated.

**Protective factors:** none established genetically or environmentally. Suggestively, the *IL1RN* findings imply that **adequate endogenous IL-1RA function is protective** and its functional deficiency is permissive — an inverted-protection framing rather than a discovered protective allele.

**Gene–environment interaction** is arguably the *core* of FIRES: a permissive innate-immune genotype (e.g., low-functioning IL-1RA) + a common febrile infection → uncontrolled IL-1β-driven neuroinflammation. This G×E convergence is the single most curation-worthy mechanistic claim.

Sources: [Appenzeller 2012 PMID:23066759](https://pubmed.ncbi.nlm.nih.gov/23066759/), [Clarkson 2019 PMID:30779222](https://pubmed.ncbi.nlm.nih.gov/30779222/), ["Fighting autoinflammation in FIRES" PMID:35356746](https://pubmed.ncbi.nlm.nih.gov/35356746/), [Fisher 2025 CSF1R](https://onlinelibrary.wiley.com/doi/10.1111/epi.18538).

---

## 3. Phenotypes

Clinical course runs in three phases (per lit review PMC9756623):

**Prodromal phase** — mild febrile illness (URI or GI), 1–2 days, then a symptom-free interval of 24 h–2 weeks.

**Acute phase** — the defining catastrophe:
- **Status epilepticus, refractory / super-refractory** — HP:0002133 (Status epilepticus), with **focal seizures with impaired awareness** (HP:0002384) evolving to **bilateral tonic-clonic seizures** (HP:0002069); often multifocal with migrating perisylvian/fronto-temporal foci. Frequency: **~100% (defining feature)**.
- **Seizures** broadly — HP:0001250. Frequency: obligate.
- **Encephalopathy / impaired consciousness** — HP:0002383 (Focal-onset) / HP:0001259 (Coma) during barbiturate suppression. Frequency: very frequent.
- **Fever** preceding — HP:0001945. Frequency: obligate by definition (in the preceding window).
- **Dysautonomia** (tachycardia, blood pressure lability) during ICU course — HP:0011448 (Abnormal autonomic nervous system physiology). Occasional.

**Chronic phase** — near-universal in survivors:
- **Refractory/pharmacoresistant epilepsy** — HP:0011171 (Refractory status is upstream) / **HP:0002197** is not right; use **HP:0001250 + intractability noted**; **Drug-resistant epilepsy** maps well to HP:0011097 (Epileptic encephalopathy) as the overarching descriptor. Per PMC9756623: *"among 66 of the 68 survived, 63 of them continued to have epilepsy refractory to any type of treatment."* Frequency: **~90–95% of survivors**.
- **Intellectual disability** — HP:0001249. Roughly *one-third normal/borderline, one-third mild–moderate ID, one-third severe ID/vegetative*. Frequency: **~66–100% of survivors**.
- **Cognitive/memory impairment** — HP:0100543 (Cognitive impairment), esp. **memory impairment** HP:0002354 (mesial temporal injury). Very frequent.
- **Language impairment / regression** — HP:0002463; **speech regression** HP:0001344. Frequent.
- **Behavioral / neuropsychiatric changes** — HP:0000708 (Behavioral abnormality), including autistic features, ADHD-like symptoms, mood/psychiatric sequelae. Frequent.
- **Motor deficits** — HP:0001324 (Muscle weakness) / **HP:0002071** (Abnormality of extrapyramidal motor function); spasticity/ataxia in severe cases. Variable.

**Laboratory phenotype:**
- **CSF pleocytosis** — mild lymphocytic, in >50% of patients (HP:0012229, Abnormal CSF protein/cellular content). 
- **Elevated CSF & serum pro-inflammatory cytokines/chemokines** (IL-6, IL-1β, IL-1RA, IL-8, CXCL/CCL chemokines) — the biochemical signature.
- Usually **normal glucose, negative viral PCR/cultures**, negative or nonspecific autoantibodies.

**Onset/severity/progression:** onset **acute/explosive**, pediatric predominant (but any age per consensus); severity **severe** essentially by definition; acute phase **episodic-to-continuous** SE lasting weeks–months, then a **chronic, often progressive-then-static** deficit. **QoL impact is profound** — survivors frequently need lifelong care, special education, and have high caregiver burden; no FIRES-specific validated QoL instrument exists (generic pediatric epilepsy/QOLCE tools apply).

Sources: [PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/), [Orphanet](https://www.orpha.net/en/disease/detail/163703).

---

## 4. Genetic / Molecular Information

**This section is where the template's gene-centric framing mostly does not apply, and that absence is itself the finding.**

- **Causal genes:** *none established.* FIRES is **not Mendelian**; there is no OMIM number. Prime epilepsy candidates were formally excluded (*SCN1A, POLG, PCDH19*, CNVs; Appenzeller 2012, PMID:23066759).
- **Susceptibility / modifier loci:**
  - **IL1RN** (IL-1 receptor antagonist; HGNC gene *IL1RN*) — risk VNTR allele + haplotype; **functional deficiency of endogenous IL-1RA** demonstrated. This is the strongest molecular lead. *"FIRES is associated with reduced expression of intracellular IL1RA isoforms and a functional deficiency in IL1RA inhibitory activity"* (Clarkson 2019, PMID:30779222).
  - Polymorphisms in other **cytokine genes** reported (small studies) — collectively point to genetically-tuned innate-immune reactivity, not a single locus.
  - **CSF1R** de novo variant — a 2025 single-case lead implicating **microglia** (Fisher 2025).
- **Variant classification / allele frequency / somatic vs germline:** Not applicable in the ACMG/ClinVar sense — there is no recurrent pathogenic variant to classify. The *IL1RN* signals are **germline common-variant susceptibility**, characterized by association, not pathogenicity calls. gnomAD/ClinVar have no FIRES-defining variant.
- **Epigenetics / chromosomal abnormalities:** none characterized; karyotype/CMA are normal (part of the diagnostic exclusion).
- **Functional consequence framing:** the operative molecular defect is a **functional loss of anti-inflammatory braking (IL-1RA)** rather than a coding change in a neuronal channel — a "loss of the brakes," not a "stuck accelerator."

Ontology handles: gene **IL1RN**; process **GO:0032611** (interleukin-1 beta production), **GO:0004908** (interleukin-1 receptor activity), **GO:0070498** (interleukin-1-mediated signaling pathway).

Sources: [Clarkson 2019 PMID:30779222](https://pubmed.ncbi.nlm.nih.gov/30779222/), [Appenzeller 2012 PMID:23066759](https://pubmed.ncbi.nlm.nih.gov/23066759/).

---

## 5. Environmental Information

- **Infectious agents (trigger):** a **preceding nonspecific febrile infection is obligatory** — but no consistent pathogen. Reported antecedents include respiratory and GI viral illnesses, influenza, HHV-6/HHV-7, enterovirus, adenovirus, *Mycoplasma pneumoniae*. Crucially, the CNS is usually **culture/PCR-negative**, so these are **triggers of an immune response, not brain-invasive pathogens** (NCBI Taxonomy is applicable only as "reported antecedent," not causal agent).
- **Toxic / occupational / pollution factors:** none implicated (and toxic causes are an exclusion criterion for NORSE/FIRES).
- **Lifestyle factors:** not applicable — this strikes previously healthy children with no lifestyle contribution.

The environmental story is thin *by design*: FIRES is defined partly by the **absence** of a clear structural/toxic/metabolic cause.

---

## 6. Mechanism / Pathophysiology

This is the heart of the entry and where the causal chain lives. Best current model — a **self-amplifying innate-immune ↔ hyperexcitability loop**:

**Causal chain (upstream → downstream):**

1. **Febrile infection primes the innate immune system** → systemic + CNS cytokine surge. (trigger)
2. **Failure of anti-inflammatory braking** — functionally deficient **IL-1 receptor antagonist (IL-1RA)** cannot restrain **IL-1β** signaling (Clarkson 2019). *This is the pivotal node.*
3. **Microglial and astrocyte activation** (GO:0001774 microglial cell activation; GO:0048143 astrocyte activation) → local release of **IL-1β, IL-6, TNF, IL-8, and chemokines** (GO:0032635 IL-6 production; GO:0032611 IL-1β production).
4. **IL-1β → IL-1R1 signaling on neurons** enhances excitability: potentiates **NMDA-receptor** currents (via Src-family kinase phosphorylation of GluN2B) and suppresses GABAergic inhibition → shifts the **excitation/inhibition balance** toward excitation (GO:0051968 positive regulation of synaptic transmission, glutamatergic).
5. **Blood–brain barrier breakdown** — IL-6/IL-1 increase BBB permeability, letting peripheral immune cells and mediators in, further stoking inflammation (a positive-feedback door propped open).
6. **Seizures themselves drive more inflammation** — seizure activity upregulates cytokines → the **"vicious circle of inflammation and hyperexcitability"** (Orphanet) → **super-refractory status epilepticus**.
7. **Downstream tissue injury** — excitotoxic + inflammatory neuronal death, especially in **hippocampus / mesial temporal structures** and neocortex → chronic **mesial temporal sclerosis**, atrophy, and the permanent epilepsy + cognitive phenotype.

> Supporting quotes:
> - *"Elevated IL-6 levels in the central nervous system worsen neuroinflammation by activating microglia and astrocytes, releasing pro-inflammatory cytokines, and weakening the blood-brain barrier."*
> - *"FIRES is associated with reduced expression of intracellular IL1RA isoforms and a functional deficiency in IL1RA inhibitory activity"* (Clarkson 2019, PMID:30779222).

**Cell types (CL):** microglial cell **CL:0000129**; astrocyte **CL:0000127**; central nervous system neuron / glutamatergic neuron **CL:0000679**; hippocampal pyramidal neuron; peripheral monocyte/macrophage **CL:0000235** (infiltrating).

**Biological processes (GO):** **GO:0006954** (inflammatory response); **GO:0002526** (acute inflammatory response); **GO:0070498** (IL-1-mediated signaling); **GO:0032635/GO:0032611** (IL-6 / IL-1β production); **GO:0001774** (microglial activation); **GO:0060291**/excitatory synaptic plasticity; **GO:0007268** (chemical synaptic transmission); BBB dysfunction (GO:0043114 regulation of vascular permeability).

**Immune involvement:** predominantly **innate/autoinflammatory** (IL-1/IL-6 axis, microglia), *not* classic adaptive autoimmunity — antibodies usually absent. This is why **IL-1 blockade (anakinra)** and **IL-6R blockade (tocilizumab)** are mechanistically rational and empirically the most promising immunotherapies.

**Molecular profiling:** the reproducible signal is a **CSF/serum cytokine-chemokine signature** (↑IL-6, ↑IL-1RA, ↑IL-1β, ↑IL-8, ↑CXCL10, ↑CCL chemokines). No robust FIRES-specific transcriptomic/proteomic/metabolomic dataset yet — a genuine knowledge gap worth a `discussions: KNOWLEDGE_GAP` note.

Sources: ["Fighting autoinflammation in FIRES" PMID:35356746](https://pubmed.ncbi.nlm.nih.gov/35356746/), [Clarkson 2019 PMID:30779222](https://pubmed.ncbi.nlm.nih.gov/30779222/), [IL-6 neuro review PMC11249726](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11249726/), [NORSE immune dysregulation review](https://www.sciencedirect.com/science/article/pii/S0387760425000889).

---

## 7. Anatomical Structures Affected

- **Primary organ / system:** **brain / central nervous system** (UBERON:0000955 brain; UBERON:0001017 CNS). Bilateral, often with **fronto-temporal / perisylvian predominance** initially.
- **Most consistently injured region:** **hippocampus / mesial temporal lobe** (UBERON:0002421 hippocampal formation; UBERON:0002771 medial temporal lobe → chronic **mesial temporal sclerosis**). Also neocortical (frontal, temporal, insular/perisylvian; UBERON:0016525 insular cortex).
- **Chronic structural change:** diffuse **cerebral atrophy** with ventriculomegaly (~49% of chronic cases) and **bilateral hippocampal/temporal atrophy** (~half) on follow-up MRI (PMC9756623).
- **Secondary organ involvement:** systemic ICU complications of prolonged SE + anesthesia — **respiratory** (ventilator dependence, pneumonia), **cardiovascular** (dysautonomia, propofol-related issues), **metabolic/hepatic** (from ketogenic diet + anesthetics), immobility complications. These are downstream of critical illness, not primary FIRES targets.
- **Tissue/cell level:** gray-matter neurons (hippocampal pyramidal, neocortical), reactive **astrocytes** and **microglia**; **BBB endothelium** (UBERON:0001986 endothelium) with increased permeability.
- **Subcellular (GO cellular component):** synapse **GO:0045202** (NMDA-receptor-bearing postsynaptic membrane, GO:0014069); microglial inflammasome machinery (cytoplasm); mitochondria in excitotoxic neurons (GO:0005739).
- **Lateralization:** typically **bilateral**, may be asymmetric; hallmark EEG shows multifocal seizures with **shifting/migrating foci across both hemispheres**.

Sources: [PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/).

---

## 8. Temporal Development

- **Onset:** **acute / explosive**, in a previously healthy person, **24 h–2 weeks after** the febrile prodrome resolves. Peak pediatric onset ~**7–10 years** (any age per 2018 consensus).
- **Stages:** (1) **prodromal** febrile illness → (2) **acute** refractory/super-refractory SE lasting **weeks to months** (the ICU phase) → (3) **chronic** drug-resistant epilepsy + neurocognitive sequelae, typically **lifelong**.
- **Progression rate:** acute phase is **rapid and severe**; there is frequently **no latent seizure-free "honeymoon"** between acute and chronic phases — the epilepsy is continuous.
- **Course pattern:** acute **super-refractory (continuous)** → chronic **relapsing/refractory** epilepsy that is usually **static-to-slowly-progressive** cognitively.
- **Remission:** spontaneous remission of the *acute* SE can occur but is unpredictable; **treatment-induced** seizure reduction is the goal, rarely full seizure-freedom. Chronic epilepsy generally **does not remit**.
- **Critical window for intervention:** strong emerging theme that **early immunotherapy (first-line within ~72 h; escalate to anakinra/tocilizumab early)** and **early ketogenic diet** improve outcomes — the therapeutic window is **days, not weeks**. This "treat early or lose the brain" window is a key actionable claim.

Sources: [Wickstrom 2022 consensus PMID:35951466](https://pubmed.ncbi.nlm.nih.gov/35951466/), [PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/).

---

## 9. Inheritance and Population

- **Epidemiology:** rare. In Germany, **prevalence ≈ 1/100,000** and **annual incidence ≈ 1/1,000,000** in children/adolescents (Orphanet). Roughly **~100+ cases** published worldwide; global data sparse. 
  - For dismech `Prevalence`: `measure_type: POINT_PREVALENCE`, `prevalence_class: BAND_1_9_PER_1000000` or `BELOW_1_IN_1000000` depending on framing; **rate_per_100000 ≈ 1.0** (prevalence) — and a **separate** `ANNUAL_INCIDENCE` record at **rate_per_100000 ≈ 0.1** (1/1,000,000). Do **not** conflate the two.
- **Inheritance pattern:** **not heritable / not Mendelian.** No AD/AR/X-linked/mitochondrial pattern; sporadic. Susceptibility is **multifactorial** with innate-immune (*IL1RN*) modifiers. Penetrance/expressivity/anticipation/founder/consanguinity/carrier-frequency fields are **not applicable**.
- **Demographics:** predominantly **school-age children**, with reports across all ages since the consensus broadened it. Possible **male predominance** (modest, per case series). No strong ethnic/geographic clustering established (AERRPS literature is Japanese, likely ascertainment rather than true predisposition).

Sources: [Orphanet](https://www.orpha.net/en/disease/detail/163703), [Dovepress prevalence/impact review](https://www.dovepress.com/febrile-infection-related-epilepsy-syndrome-fires-prevalence-impact-an-peer-reviewed-fulltext-article-NDT).

---

## 10. Diagnostics

**FIRES is fundamentally a diagnosis of exclusion + a compatible clinical picture** (refractory SE after recent fever, no cause found). Consensus (Wickstrom 2022, PMID:35951466) emphasizes broad, rapid workup.

- **EEG (essential):** early **fronto-temporal spike-and-wave**; evolving to **multifocal seizures with migrating foci**, diffuse delta-theta slowing; may show the **extreme delta brush** pattern (shared with anti-NMDAR encephalitis). Continuous EEG monitoring is mandatory to track (super-)refractory SE. (LOINC-codable; electrophysiology.)
- **MRI:** **often normal early** (~61% normal at presentation — PMC9756623), which supports the diagnosis; later shows **hippocampal T2/FLAIR signal → mesial temporal sclerosis**, and progressive atrophy/ventriculomegaly. (RadLex/Radiopaedia.)
- **CSF:** mild **lymphocytic pleocytosis** (>50%), usually normal glucose, **negative infectious PCR/culture**, and **elevated pro-inflammatory cytokines/chemokines** (research/specialty assays). Send **autoimmune encephalitis antibody panel** (serum + CSF) — usually negative, but must exclude antibody-mediated NORSE.
- **Blood:** inflammatory markers; rule out systemic infection, HLH/macrophage-activation (ferritin, triglycerides — a reported FIRES mimic/overlap), metabolic and toxicologic causes.
- **Genetic testing:** **epilepsy gene panel / WES/WGS** is recommended in the NORSE/FIRES workup to **exclude monogenic mimics** (e.g., *PCDH19, POLG, SCN1A*, mitochondrial disease) — *not* because a FIRES gene exists, but to rule out a look-alike. Mitochondrial testing where indicated. CMA/karyotype normal.
- **Differential diagnosis (must rule out):** infectious/viral encephalitis; **anti-NMDAR and other autoimmune encephalitides**; mitochondrial encephalopathy (POLG, MELAS); genetic epileptic encephalopathies (Dravet/*SCN1A*, *PCDH19*); CNS vasculitis; toxic/metabolic SE; **HLH/MAS**-associated SE. FIRES's distinguishing features: **normal prior development, obligate preceding fever, absence of identified cause, and the innate-cytokine signature**.
- **Screening:** no population screening — too rare, no biomarker with predictive value pre-onset.

Sources: [Wickstrom 2022 PMID:35951466](https://pubmed.ncbi.nlm.nih.gov/35951466/), [PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/).

---

## 11. Outcome / Prognosis

Blunt truth: FIRES is one of the worst outcomes in pediatric neurology.

- **Mortality:** up to **~12–30%** (acute-phase death, often from super-refractory SE and its ICU complications).
- **Epilepsy:** near-universal in survivors — *"among 66 of the 68 survived, 63 continued to have epilepsy refractory to any type of treatment"* (PMC9756623). So **>90% of survivors → chronic drug-resistant epilepsy**.
- **Cognition:** roughly a **thirds distribution** — ~1/3 normal-to-borderline, ~1/3 mild–moderate intellectual disability, ~1/3 severe ID / vegetative. Overall **~66–100% of survivors are left developmentally disabled** (Orphanet/NORD).
- **Prognostic factors (emerging):** **longer/deeper barbiturate coma and longer SE duration → worse cognitive outcome**; **earlier immunotherapy and earlier ketogenic diet → better outcome**. Higher/earlier cytokine burden may portend worse course. No validated prognostic biomarker yet.
- **Morbidity / QoL:** severe — lifelong care needs, special education, motor/language deficits, behavioral/psychiatric comorbidity, and high family/caregiver burden.

Sources: [Orphanet](https://www.orpha.net/en/disease/detail/163703), [NORD](https://rarediseases.org/mondo-disease/febrile-infection-related-epilepsy-syndrome/), [PMC9756623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/).

---

## 12. Treatment

No cure; management is a two-front war — **stop the seizures** and **cool the inflammation** — with early, aggressive escalation. The 2022 international consensus (Wickstrom et al., PMID:35951466, 85 consensus statements) is the anchor.

**A. Anti-seizure / anesthetic (acute SE control)**
- Standard SE ladder: benzodiazepines → IV ASMs (levetiracetam, valproate, phenytoin/fosphenytoin) → **anesthetic/burst-suppression coma** (midazolam, **barbiturates/pentobarbital**, ketamine, propofol). *Caveat:* **prolonged barbiturate coma correlates with worse cognition** — a therapy whose cure edges into harm.
  - MAXO: **MAXO:0000058** (pharmacotherapy) / antiseizure pharmacotherapy; anesthesia.
- **Cannabidiol (Epidiolex):** promising in both phases — case series of 7 children, **6/7 improved** in seizure frequency/duration (Gofshteyn et al. 2017, *J Child Neurol*; **PMID:27655472**); acute-phase reports of SE resolution within days (Fetta 2023, *Epilepsia Open*, [doi:10.1002/epi4.12740](https://onlinelibrary.wiley.com/doi/10.1002/epi4.12740), **verify PMID**). CHEBI: cannabidiol **CHEBI:69478**.
- Other ASMs reported ad hoc (cenobamate, perampanel, topiramate) in the chronic phase — anecdotal.

**B. Ketogenic diet (KD) — a signature FIRES therapy**
- Landmark: **Nabbout et al. 2010, *Epilepsia*** ([doi:10.1111/j.1528-1167.2010.02703.x](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2010.02703.x), **verify PMID**) — 4:1 KD in 9 FIRES children, **efficacious in 7**, with seizure cessation **2–4 days after ketonuria / 4–6 days after diet onset**. Now a recommended early adjunct (watch for propofol interaction → propofol infusion syndrome). MAXO: **MAXO:0000088** (dietary intervention) / ketogenic diet.

**C. Immunotherapy (mechanistically the most rational)**
- **First-line, start within ~72 h:** high-dose **corticosteroids** (MAXO/CHEBI corticosteroid), **IVIG**, and/or **plasma exchange**. MAXO: **MAXO:0000759** (immunosuppressive therapy); plasmapheresis.
- **Second-line, escalate early in cryptogenic FIRES:**
  - **Anakinra** (recombinant **IL-1 receptor antagonist**) — the most evidence-backed targeted therapy, born from the mechanism itself. First reported by **Kenney-Jung et al. 2016, *Ann Neurol*** ([doi:10.1002/ana.24806](https://onlinelibrary.wiley.com/doi/10.1002/ana.24806), **verify PMID**): CSF cytokines normalized on treatment. In one series, **11/15 children had >50% seizure reduction at 1 week** (PMC9756623); early use → shorter ICU stay. Long-term neuropsych outcomes can still be poor despite anakinra (Frontiers Neurol 2023). 
  - **Tocilizumab** (**IL-6 receptor** monoclonal antibody) — effective in some **anakinra-refractory** cases (Stredny et al. 2020, *Child Neurol Open*, [doi:10.1177/2329048X20979253](https://journals.sagepub.com/doi/10.1177/2329048X20979253), **verify PMID**); and vice versa — **anakinra works in some tocilizumab-refractory cases even with normal IL-1β** (Frontiers Immunol 2026). MAXO: **MAXO:0000759** immunomodulation; therapeutic_modality: MONOCLONAL_ANTIBODY for tocilizumab.
  - Chronic-phase case series: anakinra/tocilizumab gave **partial seizure reduction (20–50%) in some, no seizure-freedom** ([Seizure 2022, PMID:35759951](https://pubmed.ncbi.nlm.nih.gov/35759951/)).
  - Others (rituximab, tacrolimus, canakinumab, cyclophosphamide) — inconsistent/unclear benefit.

**D. Other / experimental:** vagus nerve stimulation and epilepsy surgery in selected chronic drug-resistant cases; therapeutic hypothermia (largely abandoned); intrathecal/other anti-cytokine strategies under study. Active clinical trials exist (e.g., KD for SRSE, NCT07496749 — verify) — search ClinicalTrials.gov for current anakinra/tocilizumab/KD FIRES trials.

**Pharmacogenomics:** none FIRES-specific; the closest thing to "genotype-guided therapy" is the **conceptual match of IL-1RA-deficiency → anakinra**, i.e., mechanism-guided rather than pharmacogenomic.

Sources: [Wickstrom 2022 PMID:35951466](https://pubmed.ncbi.nlm.nih.gov/35951466/), [Kenney-Jung 2016](https://onlinelibrary.wiley.com/doi/10.1002/ana.24806), [Nabbout 2010 KD](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2010.02703.x), [Gofshteyn 2017 CBD PMID:27655472](https://pubmed.ncbi.nlm.nih.gov/27655472/), [Anakinra long-term outcomes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10030614/), [Chronic-phase series PMID:35759951](https://pubmed.ncbi.nlm.nih.gov/35759951/).

---

## 13. Prevention

Largely **not applicable / not feasible** — you can't screen for or vaccinate against a syndrome whose trigger is "some ordinary fever" in a genetically-unpredictable host.

- **Primary prevention:** none. No way to identify at-risk children pre-onset; routine childhood vaccination reduces some febrile infections generally but isn't a FIRES-specific strategy.
- **Secondary prevention (early detection/treatment):** the real lever — **early recognition of NORSE/FIRES and rapid escalation to immunotherapy + KD within days** is effectively "secondary prevention" of the devastating chronic phase. This is the consensus's central practical message.
- **Tertiary prevention:** manage chronic epilepsy, rehab (PT/OT/speech), neuropsychology, avoid prolonged barbiturate coma, prevent ICU complications.
- **Genetic counseling / carrier / prenatal screening:** **not applicable** — sporadic, non-Mendelian; recurrence risk to siblings is not meaningfully elevated.

Sources: [Wickstrom 2022 PMID:35951466](https://pubmed.ncbi.nlm.nih.gov/35951466/).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** described in **humans (NCBITaxon:9606)** only.
- **Natural animal disease:** **none reported** — there is no recognized spontaneous FIRES equivalent in companion animals or wildlife (OMIA has no FIRES entry). Veterinary relevance: nil.
- **Comparative biology:** the *mechanistic* pieces (fever → IL-1β/IL-6 neuroinflammation → seizure) are evolutionarily conserved and studied in rodent **inflammation-induced seizure / epileptogenesis** models, but no animal *naturally* develops the FIRES syndrome.
- **Zoonosis / cross-species transmission:** not applicable (FIRES is not transmissible; the antecedent infections may be common human pathogens but FIRES itself is a host immune response).

---

## 15. Model Organisms

**No faithful animal model of FIRES exists** — a genuine translational gap, and worth a `discussions: HUMAN_MODEL_MISMATCH` entry rather than a claim of recapitulation.

- **Closest surrogates (mechanistic, not disease-faithful):**
  - Rodent **inflammation-driven seizure / epileptogenesis** models — systemic or intracerebral **LPS**, **IL-1β**, or **poly(I:C)** to model fever/infection-triggered hyperexcitability; **kainate/pilocarpine SE** models with an inflammatory "second hit." These reproduce the **IL-1β → NMDA-potentiation → seizure** node but **not** the explosive, super-refractory, previously-healthy-child syndrome.
  - **IL1RN-related** manipulations (IL-1RA knockout / IL-1β overexpression) speak to the anti-inflammatory-braking hypothesis but are not "FIRES mice."
- **Genetic models:** none purpose-built for FIRES (no causal gene to knock in). *Il1rn*-null mice exist for autoinflammation broadly and are conceptually relevant to the IL-1RA-deficiency hypothesis.
- **In vitro / patient-derived:** patient **CSF cytokine assays** and **cell-based IL-1R signaling assays** (as in Clarkson 2019) are the main experimental system; iPSC-derived neuron/microglia co-cultures are a logical but not-yet-established avenue.
- **Model limitation (the crux):** no model captures the **whole-syndrome convergence** — the specific human host-susceptibility + common-infection trigger + super-refractory course. Applications are limited to dissecting the **cytokine-hyperexcitability loop**, not the syndrome.

Resources: MGI (*Il1rn*, *Il6* alleles), rodent SE/neuroinflammation literature.

---

## Curation notes & flagged gaps for the dismech entry

- **Model this as an immune/inflammatory epileptic encephalopathy, not a gene disorder.** The natural `conforms_to` target is the epilepsy convergence module — **`epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`** — with FIRES supplying the *upstream inflammatory driver* (IL-1β/IL-6 → NMDA potentiation + GABA suppression) rather than a channel variant. Consider whether a dedicated **neuroinflammation/autoinflammatory-seizure** module is warranted; if one is ever built, FIRES + antibody-mediated NORSE would be natural conformers.
- **Pivotal node to curate:** *functional IL-1RA deficiency → unopposed IL-1β signaling* (Clarkson 2019, PMID:30779222) — this is the mechanistic hinge and the therapeutic rationale for anakinra, so it deserves its own pathophysiology node with the anakinra treatment linked via `target_mechanisms`.
- **Two separate `Prevalence` records** (point prevalence ~1/100,000 vs annual incidence ~1/1,000,000) — don't merge; different `measure_type`.
- **Evidence-source tagging:** most treatment evidence is small **HUMAN_CLINICAL** case series (low N); the IL-1RA functional work is **IN_VITRO** cell-based assay + human samples; rodent inflammation-seizure work is **MODEL_ORGANISM**. Split accordingly.
- **PMIDs to verify before quoting** (I could confirm the paper but not independently pin the PMID via search): Hirsch 2018 consensus (doi:10.1111/epi.14016), Kenney-Jung 2016 (doi:10.1002/ana.24806), Nabbout 2010 KD (doi:10.1111/j.1528-1167.2010.02703.x), Fetta 2023 CBD (doi:10.1002/epi4.12740), Stredny 2020 tocilizumab (doi:10.1177/2329048X20979253), Fisher 2025 CSF1R (doi:10.1111/epi.18538). **Confirmed PMIDs:** 30779222 (Clarkson), 35951466 (Wickstrom), 23066759 (Appenzeller), 27655472 (Gofshteyn CBD), 35356746 (autoinflammation review), 35759951 (chronic-phase anakinra/tocilizumab series). Run `just fetch-reference` on each and verify snippets before committing.

**Primary sources cited:**
[Hirsch 2018 consensus (Epilepsia)](https://onlinelibrary.wiley.com/doi/10.1111/epi.14016) · [Wickstrom 2022 management consensus (PMID:35951466)](https://pubmed.ncbi.nlm.nih.gov/35951466/) · [Clarkson 2019 IL-1RA deficiency (PMID:30779222)](https://pubmed.ncbi.nlm.nih.gov/30779222/) · [Appenzeller 2012 gene-negative (PMID:23066759)](https://pubmed.ncbi.nlm.nih.gov/23066759/) · [Kenney-Jung 2016 anakinra](https://onlinelibrary.wiley.com/doi/10.1002/ana.24806) · [Nabbout 2010 ketogenic diet](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2010.02703.x) · [Gofshteyn 2017 cannabidiol (PMID:27655472)](https://pubmed.ncbi.nlm.nih.gov/27655472/) · [Chronic-phase anakinra/tocilizumab series (PMID:35759951)](https://pubmed.ncbi.nlm.nih.gov/35759951/) · ["Fighting autoinflammation in FIRES" (PMID:35356746)](https://pubmed.ncbi.nlm.nih.gov/35356746/) · [Fisher 2025 CSF1R (Epilepsia)](https://onlinelibrary.wiley.com/doi/10.1111/epi.18538) · [Lit review + 2 cases (PMC9756623)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9756623/) · [Orphanet 163703](https://www.orpha.net/en/disease/detail/163703) · [NORD/MONDO FIRES](https://rarediseases.org/mondo-disease/febrile-infection-related-epilepsy-syndrome/).

---

That's the whole map, Harry. The one-sentence version if you're skimming: **FIRES is a fever that lights a match in a brain whose anti-inflammatory fire extinguisher (IL-1RA) is functionally busted — so the innate-immune blaze and the seizures feed each other into weeks of unstoppable status epilepticus, and the survivors pay for it for life.** The whole thing points at IL-1/IL-6 blockade as the rational therapy, which is exactly where the anakinra/tocilizumab evidence is pooling. Curate it as an inflammatory epileptic encephalopathy hanging off the E/I-imbalance module, not as a gene disorder — there is no gene.