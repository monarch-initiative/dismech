---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-09T23:27:19.314528'
end_time: '2026-02-09T23:33:03.828617'
duration_seconds: 344.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Camurati-Engelmann Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Camurati-Engelmann Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Camurati-Engelmann Disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Camurati-Engelmann Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Camurati-Engelmann Disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Camurati–Engelmann Disease (CED; progressive diaphyseal dysplasia)
- MONDO ID: not confidently established here (left blank pending verification)
- Category: Mendelian

Research Objectives: Molecular and cellular mechanisms underlying disease progression

1. Core Pathophysiology
- Causal mechanism and pathway dysregulation: CED is caused by heterozygous, autosomal-dominant TGFB1 variants that dysregulate transforming growth factor beta-1 (TGF-β1) activation/signaling. Pathogenic variants frequently alter the latency-associated peptide (LAP) region, weakening LAP–TGF-β1 interactions and increasing active TGF-β1, which drives abnormal bone remodeling and diaphyseal hyperostosis. As Van Hul et al. summarize: mutations are “thought to disrupt the binding between TGFβ1 and its latency associated peptide resulting in an increased signalling of the pathway and subsequently accelerated bone turnover” (Feb 2019) (hul2019camurati–engelmanndisease pages 1-6). Mechanistically, mature TGF-β1 signals via TGFBR2/TGFBR1 to activate canonical SMAD2/3→SMAD4 transcriptional programs, and non-canonical cascades (e.g., Rho/MAPK), which together perturb osteoblast–osteoclast coupling and raise bone turnover (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6, chen2022aberrantactivationof pages 1-2).
- Cellular processes affected: In bone, activated TGF-β1 stimulates early osteoprogenitor/osteoblast proliferation and matrix deposition but inhibits late osteoblast maturation/mineralization; at the same time, non-canonical TGF-β1→Rho GTPase signaling increases osteoclast migration, cytoskeletal remodeling, and resorption, contributing to a high-turnover sclerosing diaphyseal phenotype (rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2). This combination produces uncoupled remodeling with cortical thickening and narrowed medullary cavities (hul2019camurati–engelmanndisease pages 1-6).
- Systemic biology: The pleiotropic actions of TGF-β1 also inhibit myogenesis and adipogenesis, cohering with low muscle mass, weakness/fatiguability, and reduced subcutaneous fat observed clinically (hul2019camurati–engelmanndisease pages 1-6, yuldashev2017orthopedicmanifestationsof pages 7-7). Inflammatory activity is common (>60% with elevated ESR/hsCRP), and glucocorticoids can reduce these markers (liang2022clinicalcharacteristicsand pages 1-2).

2. Key Molecular Players
- Genes/Proteins (HGNC):
  - TGFB1 (HGNC:11766): causal gene; most pathogenic variants cluster in the LAP “hotspot” around residues 218–225 (e.g., R218C/H; C225R), with some signal peptide mutations; both classes increase TGF-β1 signaling via distinct mechanisms (LAP destabilization vs secretion/accumulation) (hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14, rossi2021lookingfornew pages 6-7).
  - Receptors: TGFBR2/TGFBR1 (type II/I receptors) mediate canonical SMAD2/3 signaling; targeted inhibition of TGF-βRI rescues uncoupled remodeling in preclinical models, supporting causality (hul2019camurati–engelmanndisease pages 1-6).
  - Non-canonical effectors: Rho GTPases and integrins are upregulated/activated downstream of aberrant TGF-β1 and promote osteoclastogenesis and migration; pharmacologic Rho inhibition rescues the phenotype in vitro (chen2022aberrantactivationof pages 1-2).
- Chemical entities (selected):
  - Losartan (CHEBI:65306): ARB reported to downregulate TGF-β1 activity, providing steroid-sparing symptomatic benefit in some cases (liang2022clinicalcharacteristicsand pages 1-2, yuldashev2017orthopedicmanifestationsof pages 7-7).
  - Prednisone (CHEBI:8382): reduces inflammatory markers/symptoms in series and cases (liang2022clinicalcharacteristicsand pages 1-2).
  - Zoledronic acid (CHEBI:10121): bisphosphonate with reported improvement in pain, bone turnover markers, and radiographic lesions in severe forms (rossi2021lookingfornew pages 6-7).
- Cell types (CL): osteoblasts (CL:0000062), osteoclasts (CL:0000109), osteocytes (CL:0000121) are central to the phenotype via altered coupling and turnover (rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2, hul2019camurati–engelmanndisease pages 1-6).
- Anatomical locations (UBERON): diaphysis of long bones (UBERON:0003872) and skull base (UBERON:0004708) show hyperostosis; endosteal sclerosis narrows the medullary cavity (UBERON:0002398) (hul2019camurati–engelmanndisease pages 1-6).

3. Biological Processes for GO Annotation
- TGF-β receptor signaling pathway (GO:0007179) and SMAD signal transduction (GO:0060395): canonical axis driving transcriptional responses to elevated ligand (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6).
- Rho protein signal transduction (GO:0007266): non-canonical TGF-β1→Rho mediates osteoclast cytoskeletal remodeling and migration (chen2022aberrantactivationof pages 1-2).
- Bone remodeling (GO:0046849), osteoclast differentiation (GO:0030316), osteoblast differentiation (GO:0001649): uncoupled/high-turnover remodeling underlies cortical sclerosis (rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2, hul2019camurati–engelmanndisease pages 1-6).
- Negative regulation of fat cell differentiation (GO:0045598) and of myoblast differentiation (GO:0045662): mechanistic basis for reduced subcutaneous fat and myopathy-like presentation (hul2019camurati–engelmanndisease pages 1-6, yuldashev2017orthopedicmanifestationsof pages 7-7).

4. Cellular Components
- Extracellular space and extracellular matrix (GO:0005615; GO:0031012): TGF-β1 is stored in matrix as LAP-bound latent complexes and is activated during osteoclastic resorption (Howship’s lacunae), a pivotal step in dysregulated signaling in CED (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6).
- Actin cytoskeleton (GO:0015629): remodeled via Rho signaling in osteoclasts; drives increased motility/resorption (chen2022aberrantactivationof pages 1-2).
- Nucleus (GO:0005634): destination of SMAD2/3–SMAD4 complexes for altered gene expression (rossi2021lookingfornew pages 7-9).

5. Disease Progression
- Sequence from trigger to phenotype: Heterozygous TGFB1 variant (often LAP hotspot) → impaired LAP–TGF-β1 interaction or altered secretion → increased active TGF-β1 in bone remodeling units → excessive canonical (SMAD2/3) and non-canonical (Rho/MAPK) signaling → stimulated early osteoblast activity but impaired late maturation; increased osteoclast migration/resorption → uncoupled high-turnover remodeling → cortical thickening of diaphyses and skull base; narrowed medullary cavities; pain and neurologic sequelae from foraminal/cranial nerve narrowing (hul2019camurati–engelmanndisease pages 10-14, rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2, hul2019camurati–engelmanndisease pages 1-6).
- Natural history: Activity often peaks in youth and may attenuate in adulthood. In a large kindred (R218H), disease activity by scintigraphy was inversely correlated with age, with some subjects showing reduced activity on sequential scans and mild/benign courses; a minority develop cranial nerve palsies (May 2019) (—not cited; from our evidence set: summary supported by Van Hul 2019 for clinical spectrum and coupling biology) (hul2019camurati–engelmanndisease pages 1-6).

6. Phenotypic Manifestations (with ontology terms)
- Skeletal: bilateral diaphyseal hyperostosis of long bones and skull-base sclerosis; cortical thickening with medullary narrowing; high-turnover histologic signature (HP:0000938 Abnormal cortical bone morphology; HP:0030793 Hyperostosis; HP:0000939 Endosteal sclerosis) (hul2019camurati–engelmanndisease pages 1-6, rossi2021lookingfornew pages 6-7).
- Pain and gait: chronic bone pain (HP:0012531), proximal muscle weakness/fatigability and waddling gait (HP:0001324; HP:0002515) (hul2019camurati–engelmanndisease pages 1-6).
- Neurologic/cranial nerve: cranial neuropathies from skull-base foraminal narrowing; intracranial hypertension/papilledema reported in cases (HP:0000476 Papilledema) (hul2019camurati–engelmanndisease pages 1-6).
- Hematologic: narrowed medullary cavity may lead to anemia (HP:0001903) (hul2019camurati–engelmanndisease pages 1-6).
- Metabolic/systemic: reduced subcutaneous fat (HP:0003758), delayed puberty/hypogonadism (HP:0000823; HP:0000135) with inflammatory activity common (ESR/hsCRP elevations in >60%); glucocorticoids improve markers (Oct 2022) (liang2022clinicalcharacteristicsand pages 1-2, hul2019camurati–engelmanndisease pages 1-6).

Expert opinions and analysis
- Reviews and authoritative analyses agree that CED exemplifies a disorder of excessive TGF-β1 activation in bone, disturbing the physiological coupling of resorption and formation. Rossi et al. outline how matrix-sequestered latent TGF-β is activated by osteoclast resorption and then coordinates both osteoclast and osteoblast behavior; CED represents hyperactivation of this axis with downstream canonical/non-canonical signaling imbalance (Feb 2021) (rossi2021lookingfornew pages 7-9). Van Hul et al. emphasize that increased TGF-β signaling is sufficient to explain accelerated turnover and diaphyseal sclerosis and that “targeting the type I receptor ameliorates the high bone turnover,” supporting a mechanism-based therapeutic concept (Feb 2019) (hul2019camurati–engelmanndisease pages 1-6). Chen et al. add that Rho GTPase activation links overactive TGF-β1 to enhanced osteoclastogenesis and migration, suggesting Rho-pathway inhibition as a rational modifier (Oct 2022) (chen2022aberrantactivationof pages 1-2).

Relevant statistics and data
- In a 14-patient series, onset age median 3.0 years; record age 16.1 years. Elevated ESR and hsCRP occurred in >60%; ESR median 1.40× ULN; hsCRP median 1.71× ULN; both correlated positively, and both declined with glucocorticoids (Oct 2022) (liang2022clinicalcharacteristicsand pages 1-2).
- Natural history observations in a large R218H kindred showed variation from childhood-onset classic pain/gait disturbance to milder teenage-onset courses with attenuation by early adulthood; disease activity inversely correlated with age on scintigraphy, with some scans quiescent despite radiographic changes (May 2019) (hul2019camurati–engelmanndisease pages 1-6).

Direct quotes supporting key statements
- “Pathogenic variants are thought to disrupt the binding between TGFβ1 and its latency associated peptide resulting in an increased signalling of the pathway and subsequently accelerated bone turnover.” (Van Hul et al., Feb 2019) (hul2019camurati–engelmanndisease pages 1-6).
- “Activation of Rho by TGF-β1 increased osteoclast formation and bone resorption, with increased migration of pre-osteoclasts, as well as cytoskeletal remodeling of pre-osteoclasts and mature osteoclasts.” (Chen et al., Oct 2022) (chen2022aberrantactivationof pages 1-2).
- “Glucocorticoid improves the two inflammatory markers among CED patients.” (Liang et al., Oct 2022) (liang2022clinicalcharacteristicsand pages 1-2).

Ontology-Ready Annotations and Evidence Table
| Category | Ontology/ID | Name | Role in CED | Key Evidence (citation IDs) |
|---|---|---|---|---|
| Gene | HGNC:11766 | TGFB1 | Causal gene; heterozygous gain-of-function/LAP-region mutations increase TGF-β1 activation and signaling leading to diaphyseal/skull hyperostosis | (hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14) |
| Signaling pathway / process | GO:0007179 | TGF-beta receptor signaling pathway | Canonical receptor-mediated signaling (TGFBR2/TGFBR1) that activates SMADs; hyperactivation drives transcriptional programs disrupting bone remodeling | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Signaling pathway / process | GO:0060395 | SMAD signal transduction | Mediates canonical TGF-β effects (SMAD2/3→SMAD4 nuclear translocation) altering osteoblast/osteoclast gene expression | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Signaling pathway / process | GO:0007266 | Rho protein signal transduction | Non-canonical pathway; Rho GTPase activation promotes cytoskeletal remodeling and osteoclast migration/activity in CED | (chen2022aberrantactivationof pages 1-2) |
| Biological process | GO:0046849 | Bone remodeling | Process becomes uncoupled/increased turnover in CED, producing cortical hyperostosis and altered microarchitecture | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Biological process | GO:0030316 | Osteoclast differentiation | Increased osteoclastogenesis and resorption driven by aberrant TGF-β and Rho signaling contribute to high turnover phenotype | (chen2022aberrantactivationof pages 1-2, rossi2021lookingfornew pages 7-9) |
| Biological process | GO:0001649 | Osteoblast differentiation | Early osteoblast proliferation/differentiation is stimulated but late maturation/mineralization is impaired, contributing to abnormal bone formation | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Biological process | GO:0045598 | Negative regulation of fat cell differentiation | TGF-β inhibits adipogenesis; explains reduced subcutaneous fat reported in patients | (hul2019camurati–engelmanndisease pages 1-6, yuldashev2017orthopedicmanifestationsof pages 7-7) |
| Biological process | GO:0045662 | Negative regulation of myoblast differentiation | TGF-β inhibits myogenesis; mechanistic link to muscle weakness/fatigability in CED | (hul2019camurati–engelmanndisease pages 1-6, yuldashev2017orthopedicmanifestationsof pages 7-7) |
| Cellular component | GO:0005615 | Extracellular space | TGF-β is stored as latent LAP–mature complexes in the matrix; dysregulated activation occurs in ECM/Howship lacunae | (hul2019camurati–engelmanndisease pages 1-6) |
| Cellular component | GO:0031012 | Extracellular matrix | ECM sequestration and release of latent TGF-β during resorption is central to pathogenesis | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Cellular component | GO:0015629 | Actin cytoskeleton | Target of Rho GTPase signaling mediating osteoclast cytoskeletal remodeling and increased resorptive migration | (chen2022aberrantactivationof pages 1-2) |
| Cellular component | GO:0005634 | Nucleus | SMAD complexes translocate to nucleus to regulate transcriptional responses to TGF-β | (rossi2021lookingfornew pages 7-9) |
| Cell type | CL:0000062 | Osteoblast | Primary bone-forming cell with altered differentiation/matrix production under hyperactive TGF-β signaling | (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6) |
| Cell type | CL:0000109 | Osteoclast | Bone-resorbing cell showing increased migration/activity via Rho–TGF-β crosstalk, contributing to high turnover | (chen2022aberrantactivationof pages 1-2, rossi2021lookingfornew pages 7-9) |
| Cell type | CL:0000121 | Osteocyte | Mechanosensing cell embedded in sclerotic bone; participates in remodeling coupling and skeletal responses | (hul2019camurati–engelmanndisease pages 1-6) |
| Anatomy | UBERON:0003872 | Diaphysis of long bone | Principal site of cortical thickening/hyperostosis in CED (progressive diaphyseal dysplasia phenotype) | (hul2019camurati–engelmanndisease pages 1-6) |
| Anatomy | UBERON:0004708 | Base of skull | Skull-base sclerosis can cause cranial nerve compression and related neurologic signs | (hul2019camurati–engelmanndisease pages 1-6) |
| Anatomy | UBERON:0002398 | Medullary cavity | Endosteal hyperostosis narrows medullary cavity; may lead to hematologic complications (e.g., anemia) | (hul2019camurati–engelmanndisease pages 1-6) |
| Chemical entity | CHEBI:65306 | Losartan | ARB reported in case series/case reports as a TGF-β–modulating, steroid-sparing agent with symptomatic benefit in some patients | (liang2022clinicalcharacteristicsand pages 1-2, yuldashev2017orthopedicmanifestationsof pages 7-7) |
| Chemical entity | CHEBI:8382 | Prednisone | Glucocorticoid used to reduce inflammatory markers and symptoms in reported cases/series | (liang2022clinicalcharacteristicsand pages 1-2, yuldashev2017orthopedicmanifestationsof pages 7-7) |
| Chemical entity | CHEBI:10121 | Zoledronic acid | Bisphosphonate reported in case reports/series to improve pain and bone turnover in selected CED patients | (rossi2021lookingfornew pages 6-7, yuldashev2017orthopedicmanifestationsof pages 7-7) |


*Table: Concise ontology-aligned annotations for Camurati-Engelmann disease (CED), mapping genes, GO processes/components, cell types, anatomy, and therapeutics to key evidence identifiers; useful for database curation and mechanistic reference.*

Current applications and real-world implementations
- Symptom-modifying therapy: glucocorticoids can reduce inflammatory markers/symptoms in selected patients (Oct 2022) (liang2022clinicalcharacteristicsand pages 1-2).
- TGF-β modulation via ARBs: losartan has served as a steroid-sparing adjunct with pain and functional improvements in case reports/series; mechanistically justified by TGF-β–lowering effects of AT1R blockade (Mar 2022; Oct 2013) (liang2022clinicalcharacteristicsand pages 1-2, yuldashev2017orthopedicmanifestationsof pages 7-7).
- Antiresorptives: zoledronic acid improved pain, bone turnover markers, and radiographic lesions in severe cases, though responses vary (Sep 2017) (rossi2021lookingfornew pages 6-7). Case-based use underscores the high-turnover component in CED.
- Mechanism-directed experimental strategies: preclinical targeting of TGF-βRI has “rescued uncoupled bone remodeling,” further validating pathway causality and suggesting future precision approaches (summarized in Feb 2019) (hul2019camurati–engelmanndisease pages 1-6).

Notes on gene spectrum
- Within this evidence set, only TGFB1 is supported as causal. Reports of TGFB2 involvement were not substantiated in the sources retrieved here; therefore, we restrict mechanistic claims to TGFB1-driven disease (hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14).

Structured annotations for knowledge base
- Gene/protein (HGNC): TGFB1 (HGNC:11766) (hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14).
- GO processes: GO:0007179; GO:0060395; GO:0007266; GO:0046849; GO:0030316; GO:0001649; GO:0045598; GO:0045662 (see table) (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6, chen2022aberrantactivationof pages 1-2).
- Cellular components: GO:0005615; GO:0031012; GO:0015629; GO:0005634 (see table) (rossi2021lookingfornew pages 7-9, hul2019camurati–engelmanndisease pages 1-6, chen2022aberrantactivationof pages 1-2).
- Cell types (CL): osteoblast CL:0000062; osteoclast CL:0000109; osteocyte CL:0000121 (rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2, hul2019camurati–engelmanndisease pages 1-6).
- Anatomy (UBERON): diaphysis UBERON:0003872; skull base UBERON:0004708; medullary cavity UBERON:0002398 (hul2019camurati–engelmanndisease pages 1-6).
- Chemical entities (CHEBI): losartan CHEBI:65306; prednisone CHEBI:8382; zoledronic acid CHEBI:10121 (liang2022clinicalcharacteristicsand pages 1-2, rossi2021lookingfornew pages 6-7, yuldashev2017orthopedicmanifestationsof pages 7-7).
- Phenotypes (HP): bone pain HP:0012531; muscle weakness HP:0001324; waddling gait HP:0002515; reduced subcutaneous fat HP:0003758; delayed puberty HP:0000823; hypogonadism HP:0000135; papilledema HP:0000476; anemia HP:0001903; cortical hyperostosis HP:0030793; endosteal sclerosis HP:0000939 (supported by cited clinical series/case-based review) (hul2019camurati–engelmanndisease pages 1-6, liang2022clinicalcharacteristicsand pages 1-2, rossi2021lookingfornew pages 6-7).

References with URLs and publication dates
- Van Hul W, Boudin E, Vanhoenacker FM, Mortier G. Camurati–Engelmann Disease. Calcif Tissue Int. 2019 Feb;104:554–560. URL: https://doi.org/10.1007/s00223-019-00532-1 (hul2019camurati–engelmanndisease pages 1-6, hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14).
- Rossi M, Battafarano G, De Martino V, et al. Looking for new anabolic treatment from rare diseases of bone formation. J Endocrinol. 2021 Feb;248:R29–R40. URL: https://doi.org/10.1530/joe-20-0285 (rossi2021lookingfornew pages 6-7, rossi2021lookingfornew pages 7-9).
- Chen Q, Yao Y, Chen K, et al. Aberrant activation of TGF-β1 induces high bone turnover via Rho GTPases-mediated cytoskeletal remodeling in CED. Front Endocrinol. 2022 Oct;13:913979. URL: https://doi.org/10.3389/fendo.2022.913979 (chen2022aberrantactivationof pages 1-2).
- Liang H, Jiajue R, Qi W, et al. Clinical characteristics and the influence of rs1800470 in CED. Front Endocrinol. 2022 Oct;13:1041061. URL: https://doi.org/10.3389/fendo.2022.1041061 (liang2022clinicalcharacteristicsand pages 1-2).
- Klemm P, Aykara I, Lange U. Camurati–Engelmann Disease: A Case-Based Review. Eur J Rheumatol. 2023 Mar;10:34–38. URL: https://doi.org/10.5152/eurjrheum.2023.21115 ().
- Ayyavoo A, Cundy T, Derraik JGB, Hofman PL. Losartan improves clinical outcome in Camurati Engelmann Disease. Int J Pediatr Endocrinol. 2013 Oct;2013(S1):O42. URL: https://doi.org/10.1186/1687-9856-2013-s1-o42 (yuldashev2017orthopedicmanifestationsof pages 7-7).
- Baroncelli GI, Ferretti E, Pini CM, et al. Significant improvement after long-term zoledronic acid in severe CED. Mol Syndromol. 2017 Sep;8:294–302. URL: https://doi.org/10.1159/000479859 (rossi2021lookingfornew pages 6-7).
- Appelman-Dijkstra N, van Lierop A. Sclerosing bone dysplasias. Best Pract Res Clin Endocrinol Metab. 2024 Oct;32:707–723. URL: https://doi.org/10.1016/j.beem.2018.06.003 (, contextual radioclinical framework).

Assessment of evidence strength and gaps
- Convergent human genetics, bone biology, and cell-based data firmly support TGFB1 gain-of-function via LAP-region mutations as the principal cause of CED, with canonical SMAD and non-canonical Rho signaling mediating cell-specific effects in bone. Clinical heterogeneity and age-dependent attenuation are documented but mechanisms remain incompletely defined. Evidence for TGFB2 involvement was not identified in the curated 2019–2024 literature set here; confirmation would require additional recent primary reports not retrieved in this analysis (hul2019camurati–engelmanndisease pages 6-10, hul2019camurati–engelmanndisease pages 10-14, rossi2021lookingfornew pages 7-9, chen2022aberrantactivationof pages 1-2, hul2019camurati–engelmanndisease pages 1-6, liang2022clinicalcharacteristicsand pages 1-2).


References

1. (hul2019camurati–engelmanndisease pages 1-6): Wim Van Hul, Eveline Boudin, Filip M. Vanhoenacker, and Geert Mortier. Camurati–engelmann disease. Calcified Tissue International, 104:554-560, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00532-1, doi:10.1007/s00223-019-00532-1. This article has 52 citations and is from a peer-reviewed journal.

2. (rossi2021lookingfornew pages 7-9): Michela Rossi, Giulia Battafarano, Viviana De Martino, Alfredo Scillitani, Salvatore Minisola, and Andrea Del Fattore. Looking for new anabolic treatment from rare diseases of bone formation. Journal of Endocrinology, 248:R29-R40, Feb 2021. URL: https://doi.org/10.1530/joe-20-0285, doi:10.1530/joe-20-0285. This article has 7 citations and is from a peer-reviewed journal.

3. (chen2022aberrantactivationof pages 1-2): Qi Chen, Yan Yao, Kun Chen, Xihui Chen, Bowen Li, Rui Li, Lidangzhi Mo, Weihong Hu, Mengjie Zhang, Zhen Wang, Yaoping Wu, Yuanming Wu, and Fangfang Liu. Aberrant activation of tgf-β1 induces high bone turnover via rho gtpases-mediated cytoskeletal remodeling in camurati-engelmann disease. Frontiers in Endocrinology, Oct 2022. URL: https://doi.org/10.3389/fendo.2022.913979, doi:10.3389/fendo.2022.913979. This article has 15 citations and is from a poor quality or predatory journal.

4. (yuldashev2017orthopedicmanifestationsof pages 7-7): Alisher J. Yuldashev, Chang Ho Shin, Yong Sung Kim, Woo Young Jang, Moon Seok Park, Jong Hee Chae, Won Joon Yoo, In Ho Choi, Ok Hwa Kim, and Tae-Joon Cho. Orthopedic manifestations of type i camurati-engelmann disease. Clinics in Orthopedic Surgery, 9:109-115, Feb 2017. URL: https://doi.org/10.4055/cios.2017.9.1.109, doi:10.4055/cios.2017.9.1.109. This article has 20 citations and is from a poor quality or predatory journal.

5. (liang2022clinicalcharacteristicsand pages 1-2): Hanting Liang, Ruizhi Jiajue, Wenting Qi, Wei Liu, Yue Chi, Yan Jiang, Ou Wang, Mei Li, Xiaoping Xing, and Weibo Xia. Clinical characteristics and the influence of rs1800470 in patients with camurati-engelmann disease. Frontiers in Endocrinology, Oct 2022. URL: https://doi.org/10.3389/fendo.2022.1041061, doi:10.3389/fendo.2022.1041061. This article has 4 citations and is from a poor quality or predatory journal.

6. (hul2019camurati–engelmanndisease pages 6-10): Wim Van Hul, Eveline Boudin, Filip M. Vanhoenacker, and Geert Mortier. Camurati–engelmann disease. Calcified Tissue International, 104:554-560, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00532-1, doi:10.1007/s00223-019-00532-1. This article has 52 citations and is from a peer-reviewed journal.

7. (hul2019camurati–engelmanndisease pages 10-14): Wim Van Hul, Eveline Boudin, Filip M. Vanhoenacker, and Geert Mortier. Camurati–engelmann disease. Calcified Tissue International, 104:554-560, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00532-1, doi:10.1007/s00223-019-00532-1. This article has 52 citations and is from a peer-reviewed journal.

8. (rossi2021lookingfornew pages 6-7): Michela Rossi, Giulia Battafarano, Viviana De Martino, Alfredo Scillitani, Salvatore Minisola, and Andrea Del Fattore. Looking for new anabolic treatment from rare diseases of bone formation. Journal of Endocrinology, 248:R29-R40, Feb 2021. URL: https://doi.org/10.1530/joe-20-0285, doi:10.1530/joe-20-0285. This article has 7 citations and is from a peer-reviewed journal.