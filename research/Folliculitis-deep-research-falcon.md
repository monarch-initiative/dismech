---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-01T17:49:10.204619'
end_time: '2026-03-01T18:02:17.542643'
duration_seconds: 787.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Folliculitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Folliculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Folliculitis**.
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
- **Disease Name:** Folliculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Folliculitis**.
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


## Comprehensive Research Report: Folliculitis Pathophysiology (Molecular & Cellular Mechanisms)

### Scope note and definition
Folliculitis is a clinicopathologic syndrome defined by inflammation centered on the hair follicle (pilosebaceous unit), presenting as follicular papules and/or pustules. In practice, “folliculitis” includes multiple entities with distinct etiologies and immune programs (e.g., bacterial folliculitis/furunculosis, Malassezia folliculitis, eosinophilic pustular folliculitis/Ofuji disease, and folliculitis decalvans), which share a folliculocentric inflammatory pattern but differ in triggers, dominant effector cells, and risk of scarring.

**Current understanding:** across subtypes, folliculitis emerges when (i) follicular barrier/immune homeostasis is perturbed (e.g., occlusion, altered keratinocyte differentiation, immunosuppression), enabling (ii) microbial overgrowth and/or dysbiosis or noninfectious inflammatory triggers, which then (iii) activate epithelial innate immune programs and (iv) recruit granulocytes (neutrophils or eosinophils) that create pustules and can destroy follicular epithelium. Malassezia folliculitis highlights a type-17 program (IL‑23/IL‑17 axis), eosinophilic pustular folliculitis is typically type-2 skewed (eosinophils, PGD2–CRTH2), and folliculitis decalvans is a neutrophilic scarring alopecia with microbiome/immune dysregulation and frequent Staphylococcus aureus associations. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5, morenoarrones2023folliculitisdecalvanshas pages 8-8, li2023clinicalandpathological pages 5-6, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

### Disease identifiers
A MONDO identifier was not retrieved in the accessible evidence for “folliculitis” as a parent concept in this run.

---

## 1) Core pathophysiology

### 1.1 Bacterial folliculitis and furunculosis (S. aureus-centric)
**Trigger/initiating event.** Bacterial folliculitis commonly follows microinjury, maceration, friction, shaving, or occlusion that enables follicular invasion by bacteria; deep folliculitis/furunculosis represents follicle rupture with dermal/hypodermal abscess formation.

**Microbe and virulence determinants.** Staphylococcus aureus employs cytolytic toxins, immune evasion, and abscess-promoting factors in follicular infections. In a highly cited 2023 review, Panton–Valentine leukocidin (PVL) is described as “a cytotoxic virulence factor” with **PVL positivity rates of 40–90% in furunculosis**. (linz2023clinicalimpactof pages 3-5) S. aureus alpha-hemolysin (Hla) contributes to epithelial injury; Hla “induces keratinocyte necrosis” and is “required for infection in keratinocytes,” and Hla binds ADAM10 and can disrupt epithelial adhesion via E‑cadherin cleavage. (linz2023clinicalimpactof pages 10-11, linz2023clinicalimpactof pages 5-7)

**Innate immune recognition and cytokine programs.** Cutaneous pattern-recognition receptor (PRR) signaling contributes to early inflammation. The same review notes PRRs “including TLR2 and NOD2,” and that NOD2 loss in models increases bacterial burden and NF‑κB activity. (linz2023clinicalimpactof pages 10-11) The host response is initially neutrophil-dominant with inflammatory mediators (e.g., IL‑6, IL‑1β, chemokines) and later shifts toward IL‑17A/F–associated programs. (linz2023clinicalimpactof pages 10-11)

**Cellular processes affected.** Key processes include keratinocyte activation, neutrophil recruitment/activation (including neutrophil extracellular traps, NETs), abscess organization, and (in deep disease) tissue destruction and scarring. (linz2023clinicalimpactof pages 10-11, linz2023clinicalimpactof pages 3-5)

**Quantitative recent context (SSTIs as a folliculitis-adjacent umbrella).** Recurrent SSTIs occur in ~16–19% of patients (most within 3 months) and MRSA SSTI hospitalization rates decreased over time (e.g., 1.72 per 1000 in 2016 to 1.32 per 1000 by 2019 in the US). (linz2023clinicalimpactof pages 1-2)

### 1.2 Malassezia (Pityrosporum) folliculitis
**Trigger/initiating event.** Malassezia are lipid-dependent commensal yeasts; disease reflects **follicular overgrowth** in sebum-rich areas promoted by humidity, occlusion, antibiotic exposure, and immunosuppression. (chalupczak2025malasseziafolliculitisan pages 1-2)

**Dysregulated pathways: keratinocyte innate immunity + type 17 axis.** A mechanistic review notes that Malassezia can induce keratinocytes to produce cytokines including **IL‑1α, IL‑6, IL‑8, IL‑12, TNF‑α**, and also IL‑4 and IL‑10 “via Toll-like receptor 2 (TLR2),” with complement activation via classical and alternative pathways. (chalupczak2025malasseziafolliculitisan pages 1-2) In addition, murine epicutaneous infection models report Malassezia “selectively induce interleukin-17 (IL-17) and related cytokines,” and cell profiling found “neutrophils, and Langerhans cells were found to express the highest levels of IL-23 transcripts,” supporting an **IL‑23/IL‑17 axis** with innate myeloid/antigen-presenting cell involvement. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)

**Cellular processes affected.** Follicular plugging/occlusion and folliculocentric inflammation are emphasized, consistent with a sequence of (i) follicular environment changes (lipids, humidity, occlusion) → (ii) yeast proliferation in the follicle → (iii) keratinocyte PRR activation and complement engagement → (iv) recruitment of inflammatory leukocytes (including neutrophils in type-17–skewed responses) → pustule formation. (chalupczak2025malasseziafolliculitisan pages 1-2, martinezortega2024malasseziafolliculitispathogenesis pages 4-5)

**Quantitative data (recent cohorts/reviews).** A 2023 systematic review aggregating **1,238 immunocompetent patients** found mean age ~24.3 years, male predominance ~64%, common sites chest (~70%) and back/shoulders (~69%), and pruritus in ~71.7%. (green2023clinicalcharacteristicsand pages 2-4) Diagnostic performance and treatment outcomes include KOH smear sensitivity/specificity “up to 84.6% and 100%,” and high response rates to antifungals (oral ~92% improvement; topical ~81.6%). (green2023clinicalcharacteristicsand pages 1-2) Another review reports Wood’s lamp “low sensitivity (65.3%) for MF diagnosis.” (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)

### 1.3 Eosinophilic pustular folliculitis (EPF; Ofuji disease)
**Core lesion biology.** EPF is characterized histologically by eosinophil-rich folliculocentric inflammation and microabscess formation. In a 10-patient clinicopathologic series (2023), histopathology included “intraepithelial spongiform oedema with eosinophil migration into hair follicles,” and “eosinophilic and neutrophilic abscesses in hair follicles,” with eosinophilic microabscesses around appendages and perivascular regions. (li2023clinicalandpathological pages 1-2)

**Mechanistic model (cell trafficking and follicular destruction).** The same study frames EPF as eosinophil recruitment into sebaceous follicles, mixing with neutrophils and promoting “fragmentation of follicular epithelium” with “small abscesses” and mucinosis-like changes. (li2023clinicalandpathological pages 5-6)

**Type 2–skewed pathways (current literature).** A recent review-level summary highlights prostaglandin D2 (PGD2) chemotaxis via CRTH2 (PTGDR2) implicating recruitment of Th2 cells, eosinophils, and basophils. (li2025successfultreatmentof pages 8-8) Additional mechanistic framing supports Th2 cytokines (IL‑4/IL‑5/IL‑13) and eosinophil biology in EPF. (danielson2025dermatologiclesionswith pages 3-4)

**Quantitative data (10-case series + image table).** In Li et al. 2023, EPF cases spanned ages 22–45 with 5 male/5 female, and pruritus occurred in 7/10. Peripheral eosinophil counts were reported per case (one normal; others elevated). (li2023clinicalandpathological pages 1-2) Table 1 visually summarizes these patient characteristics and eosinophil counts. (li2023clinicalandpathological media 4cdf4055)

### 1.4 Folliculitis decalvans (FD)
**Core lesion biology.** FD is a chronic neutrophilic folliculitis of the scalp that leads to scarring alopecia. It is often linked clinically to S. aureus, but emerging data support broader dysbiosis/microbiome heterogeneity.

**Microbiome + immune dysfunction concept.** A 2023 cross-sectional study using trichoscopy-guided biopsies is explicitly framed as showing a “heterogeneous microbiological signature and impaired immunological response,” and targeted staphylococcal virulence markers (e.g., pvl, mecA) were assessed. (morenoarrones2023folliculitisdecalvanshas pages 2-3)

**Immune privilege collapse and lichenoid phase hypothesis.** The same FD study proposes that microbiota perturbation could cause “a collapse of follicular immune privilege,” exposing follicular antigens and “triggering a lichenoid response against the hair follicle.” (morenoarrones2023folliculitisdecalvanshas pages 8-8)

**Drug-induced implementation: EGFR inhibitor–associated FD.** In oncology, EGFR inhibitors can precipitate FD-like scarring folliculitis; the mechanistic framing is that EGFR inhibitor adverse reactions arise from “disturbances in keratinocyte differentiation, cytokine secretion, and neutrophil chemotaxis,” producing sterile folliculitis with frequent secondary bacterial superinfection; S. aureus is “frequently cultured” and its superantigens “may contribute to pathogenesis.” (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

---

## 2) Key molecular players (genes/proteins), chemical entities, cell types, and anatomical locations

### 2.1 Genes/proteins and pathways (HGNC-style names where applicable)
**Innate sensors / signaling**
- **TLR2**: implicated in Malassezia-induced keratinocyte cytokine responses and in bacterial skin infection PRR recognition. (chalupczak2025malasseziafolliculitisan pages 1-2, linz2023clinicalimpactof pages 10-11)
- **NOD2**: PRR implicated in bacterial skin infection models; loss increases bacterial burden/NF‑κB activity. (linz2023clinicalimpactof pages 10-11)
- **MYD88** and **IL36R** (IL1RL2 / IL‑36 receptor axis): cited as mediating “Malassezia-induced IL-17-dependent skin inflammation.” (martinezortega2024malasseziafolliculitispathogenesis pages 6-7)

**Cytokines/chemokines (examples strongly represented in evidence)**
- **IL1A, IL6, CXCL8 (IL-8), IL12, TNF**: induced in keratinocytes by Malassezia via TLR2 (as described in review evidence). (chalupczak2025malasseziafolliculitisan pages 1-2)
- **IL23** (IL23A as a component of IL‑23): IL‑23 transcripts highest in neutrophils/Langerhans cells in Malassezia skin model. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)
- **IL17 axis** (e.g., IL17A/IL17F conceptually): Malassezia “selectively induce IL‑17 and related cytokines.” (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)
- **IL33**: promotes NETs via NADPH oxidase in S. aureus skin infection context. (linz2023clinicalimpactof pages 10-11)

**Host targets / epithelial injury**
- **ADAM10**: Hla binds ADAM10 and disrupts epithelial adhesion (E‑cadherin cleavage). (linz2023clinicalimpactof pages 5-7)
- **PTGS2 (COX2)** and **IL8**: protein A can induce keratinocyte proinflammatory genes including COX2 and IL8. (linz2023clinicalimpactof pages 10-11)

**Microbial virulence factors**
- **PVL (lukS-PV/lukF-PV; toxin concept)**: associated with furunculosis; PVL positivity 40–90% in furunculosis. (linz2023clinicalimpactof pages 3-5)
- **Hla (alpha-hemolysin)**: keratinocyte necrosis and epithelial disruption. (linz2023clinicalimpactof pages 10-11, linz2023clinicalimpactof pages 5-7)
- **Protein A (spa; virulence concept)**: immune evasion and keratinocyte activation. (linz2023clinicalimpactof pages 10-11)
- **Coagulase (coa) / vWbp**: implicated in abscess formation. (linz2023clinicalimpactof pages 10-11)

### 2.2 Chemical entities (CHEBI-style)
- **Prostaglandin D2 (PGD2)**: chemotaxis via CRTH2 described for EPF. (li2025successfultreatmentof pages 8-8)
- **Indomethacin**: commonly effective/first-line in EPF with rapid responses in case series experience. (li2023clinicalandpathological pages 5-6)
- **Itraconazole, ketoconazole**: key antifungals for Malassezia folliculitis; strong response rates across cohorts. (martinezortega2024malasseziafolliculitispathogenesis pages 1-3, green2023clinicalcharacteristicsand pages 2-4)
- **Tetracyclines/doxycycline**: used for FD (including EGFR inhibitor–associated FD) with both antibacterial and anti-inflammatory roles; typical durations 4–16 weeks cited. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 5-5)

### 2.3 Cell types (CL-style)
- **Keratinocytes**: central epithelial responders producing cytokines after microbial sensing. (chalupczak2025malasseziafolliculitisan pages 1-2, linz2023clinicalimpactof pages 10-11)
- **Neutrophils**: dominant effector cells in bacterial folliculitis/furunculosis and FD; implicated in IL‑23 transcripts in Malassezia model; drive pustules and scarring follicular destruction in FD. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5, linz2023clinicalimpactof pages 10-11)
- **Eosinophils**: dominant effector cells in EPF; migrate into follicles and form microabscesses. (li2023clinicalandpathological pages 1-2)
- **Langerhans cells**: implicated as IL‑23 transcript-high cells in Malassezia model; also recognize S. aureus via langerin in SSTI review. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5, linz2023clinicalimpactof pages 10-11)
- **Plasma cells**: part of FD infiltrate in EGFR inhibitor-associated FD histopathology (“rich in neutrophils and plasma cells”). (nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

### 2.4 Anatomical locations (UBERON-style)
- **Pilosebaceous unit / hair follicle**: primary inflammatory compartment across folliculitis entities. (li2023clinicalandpathological pages 1-2, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)
- **Sebaceous-rich truncal skin (chest/back/shoulders)**: common distribution for Malassezia folliculitis. (green2023clinicalcharacteristicsand pages 2-4)
- **Scalp hair follicles**: primary site for FD and EGFR inhibitor-associated FD. (morenoarrones2023folliculitisdecalvanshas pages 2-3, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

---

## 3) Biological processes disrupted (GO-oriented)
Representative processes, with evidence linkage:
- **Innate immune response / PRR signaling (TLR2, NOD2)** (chalupczak2025malasseziafolliculitisan pages 1-2, linz2023clinicalimpactof pages 10-11)
- **Cytokine-mediated signaling pathways** (IL‑1/IL‑6/IL‑8/TNF; IL‑23/IL‑17) (chalupczak2025malasseziafolliculitisan pages 1-2, martinezortega2024malasseziafolliculitispathogenesis pages 4-5, linz2023clinicalimpactof pages 10-11)
- **Granulocyte chemotaxis and activation**: neutrophil chemotaxis in FD (drug-induced model) and bacterial folliculitis; eosinophil migration in EPF. (li2023clinicalandpathological pages 1-2, nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3, linz2023clinicalimpactof pages 10-11)
- **Complement activation** in Malassezia folliculitis. (chalupczak2025malasseziafolliculitisan pages 1-2)
- **Epithelial cell death and barrier disruption** (keratinocyte necrosis; epithelial adhesion disruption). (linz2023clinicalimpactof pages 5-7)

---

## 4) Cellular components (subcellular/compartment focus)
- **Follicular lumen and follicular epithelium**: site of Malassezia overgrowth, follicular plugging, and inflammatory infiltration. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5, li2023clinicalandpathological pages 1-2)
- **Perifollicular dermis / perivascular spaces**: common inflammatory distribution in EPF and FD, including mixed infiltrates and microabscesses. (morenoarrones2023folliculitisdecalvanshas pages 8-8, li2023clinicalandpathological pages 1-2)

---

## 5) Disease progression: sequence of events (by subtype)

### 5.1 Malassezia folliculitis progression (conceptual)
1. Environmental/host predisposition (humidity, occlusion, antibiotic exposure) promotes yeast overgrowth in sebum-rich follicles. (chalupczak2025malasseziafolliculitisan pages 1-2)
2. Keratinocytes sense Malassezia via TLR2 and produce inflammatory mediators (IL‑1α, IL‑6, IL‑8, IL‑12, TNF‑α), with complement activation. (chalupczak2025malasseziafolliculitisan pages 1-2)
3. Type-17–linked inflammation emerges; Malassezia induces IL‑17, with IL‑23 transcripts in neutrophils/Langerhans cells in model systems. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)
4. Clinical manifestation: monomorphic pruritic follicular papules/pustules and a chronic-relapsing course. (chalupczak2025malasseziafolliculitisan pages 1-2)

### 5.2 EPF progression (clinicopathologic)
1. Triggering antigenic stimuli (often unclear) with preferential involvement of sebaceous areas. (li2023clinicalandpathological pages 2-5)
2. Eosinophil recruitment into follicles → spongiosis and eosinophil migration into follicular epithelium. (li2023clinicalandpathological pages 1-2)
3. Formation of eosinophilic (and often mixed eosinophilic/neutrophilic) follicular abscesses with follicular destruction. (li2023clinicalandpathological pages 2-5)
4. Clinical plaques/pustules; typically heal with post-inflammatory hyperpigmentation without scarring in the case series experience. (li2023clinicalandpathological pages 5-6)

### 5.3 FD progression (conceptual + drug-induced model)
1. Microbiome perturbation/dysbiosis may collapse follicular immune privilege → antigen exposure → lichenoid response. (morenoarrones2023folliculitisdecalvanshas pages 8-8)
2. Neutrophilic perifollicular inflammation leads to follicular destruction and permanent scarring alopecia. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)
3. In EGFR inhibitor-associated FD: keratinocyte differentiation defects and neutrophil chemotaxis contribute to sterile folliculitis with frequent S. aureus superinfection, amplifying inflammation. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

---

## 6) Phenotypic manifestations (HP-oriented)
- **Follicular papules/pustules** (common across subtypes) (chalupczak2025malasseziafolliculitisan pages 1-2, li2023clinicalandpathological pages 1-2)
- **Pruritus** (notable in Malassezia folliculitis; common in EPF) (green2023clinicalcharacteristicsand pages 2-4, li2023clinicalandpathological pages 1-2)
- **Scarring alopecia** (FD; deep folliculitis) (nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5, linz2023clinicalimpactof pages 3-5)

---

## 7) Recent developments and latest research emphasis (prioritizing 2023–2024)

### 7.1 2023–2024 highlights
- **FD microbiome + immune response framing (2023):** FD characterized by “heterogeneous microbiological signature and impaired immunological response,” with a mechanistic hypothesis of immune privilege collapse and lichenoid response. (morenoarrones2023folliculitisdecalvanshas pages 2-3, morenoarrones2023folliculitisdecalvanshas pages 8-8)
- **Malassezia folliculitis immunology axis (2024):** epicutaneous model evidence supports Malassezia-driven IL‑17 responses and IL‑23 production by myeloid/Langerhans subsets, and provides diagnostic quantification (Wood’s lamp sensitivity 65.3%). (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)
- **EPF clinicopathology (2023):** detailed histopathology and patient-level eosinophil counts in a 10-case series provide a contemporary phenotype/biology anchor for EPF. (li2023clinicalandpathological pages 1-2, li2023clinicalandpathological media 4cdf4055)
- **EGFR inhibitor-associated FD (2023):** mechanistic linkage to keratinocyte differentiation/cytokine secretion/neutrophil chemotaxis, with practical prevention/management guidance (pre-emptive tetracyclines/topical steroids). (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3, nowaczyk2023egfrinhibitorinducedfolliculitis pages 5-6)

---

## 8) Current applications and real-world implementations

### 8.1 Diagnostic implementation
- **Malassezia folliculitis:** KOH smear and histopathology are widely used. In the 2023 systematic review, KOH sensitivity/specificity reported up to **84.6%/100%**. (green2023clinicalcharacteristicsand pages 1-2) Wood’s lamp has **65.3% sensitivity** in one report. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5) Misdiagnosis is common: ~40.5% had prior unsuccessful treatments (often acne-directed). (green2023clinicalcharacteristicsand pages 2-4)
- **EPF:** biopsy is central; Table 1 in Li et al. 2023 summarizes clinical features and eosinophil counts for 10 cases. (li2023clinicalandpathological media 4cdf4055)
- **FD:** trichoscopy-guided biopsy and microbiologic evaluation; EGFR inhibitor-associated FD emphasizes trichoscopy as a key noninvasive diagnostic tool and highlights the need to identify/treat superinfection to prevent severe complications in immunocompromised patients. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)

### 8.2 Therapeutic implementation (mechanism-aligned)
- **Malassezia folliculitis:** antifungals are highly effective; 2023 aggregated data indicate oral antifungals ~92% success and topical ~81.6%. (green2023clinicalcharacteristicsand pages 1-2)
- **EPF:** indomethacin is commonly effective and described as a preferred/first-line option; in one cohort segment, responses are often within weeks. (li2023clinicalandpathological pages 5-6)
- **FD (including EGFR inhibitor-associated):** systemic tetracyclines and topical steroids/antibiotics are used; tetracyclines “should be continued for 4 up to 16 weeks,” then tapered to anti-inflammatory doses for maintenance. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 5-5)

---

## 9) Evidence items with identifiers (PMIDs preferred)
PMIDs were not available in the extracted evidence snippets during this tool run; therefore, below are DOI-based evidence anchors (each is a peer-reviewed article unless otherwise noted):
- Linz MS et al. *Antibiotics* (Mar 2023). DOI: 10.3390/antibiotics12030557. (linz2023clinicalimpactof pages 1-2)
- Moreno-Arrones OM et al. *Dermatology* (Jan 2023). DOI: 10.1159/000529301. (morenoarrones2023folliculitisdecalvanshas pages 2-3)
- Nowaczyk J et al. *Anti-Cancer Drugs* (Jan 2023). DOI: 10.1097/CAD.0000000000001494. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3)
- Green M et al. *Archives of Dermatological Research* (Dec 2023). DOI: 10.1007/s00403-022-02506-0. (green2023clinicalcharacteristicsand pages 2-4)
- Li Y et al. *Clinical, Cosmetic and Investigational Dermatology* (Sep 2023). DOI: 10.2147/CCID.S427718. (li2023clinicalandpathological pages 1-2)
- Martínez-Ortega JI et al. *Cureus* (Nov 2024). DOI: 10.7759/cureus.73429. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)

---

## 10) Key direct-quote excerpts supporting major mechanistic claims
- Malassezia folliculitis model evidence: Malassezia spp. “selectively induce interleukin-17 (IL-17) and related cytokines,” and “neutrophils, and Langerhans cells were found to express the highest levels of IL-23 transcripts.” (martinezortega2024malasseziafolliculitispathogenesis pages 4-5)
- FD immune-privilege hypothesis: microbiota perturbation may cause “a collapse of follicular immune privilege,” exposing follicular antigens and “triggering a lichenoid response against the hair follicle.” (morenoarrones2023folliculitisdecalvanshas pages 8-8)
- EGFR inhibitor-associated FD mechanism: adverse reactions originate from “disturbances in keratinocyte differentiation, cytokine secretion, and neutrophil chemotaxis.” (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3)
- Furunculosis PVL association: PVL reported positive in **40–90%** of furunculosis. (linz2023clinicalimpactof pages 3-5)

---

## Conclusion
Folliculitis comprises mechanistically distinct folliculocentric inflammatory disorders unified by follicular barrier disruption and innate immune activation. Recent 2023–2024 literature emphasizes (i) microbiome heterogeneity and impaired immunity in folliculitis decalvans with a proposed immune-privilege collapse/lichenoid phase; (ii) Malassezia-driven keratinocyte innate activation coupled to an IL‑23/IL‑17 (type-17) axis involving neutrophils and Langerhans cells; and (iii) eosinophilic pustular folliculitis as an eosinophil-dominant, often type-2–skewed disorder with characteristic follicular eosinophilic microabscesses and clinically meaningful response to indomethacin. (morenoarrones2023folliculitisdecalvanshas pages 2-3, martinezortega2024malasseziafolliculitispathogenesis pages 4-5, li2023clinicalandpathological pages 1-2, nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5)


References

1. (martinezortega2024malasseziafolliculitispathogenesis pages 4-5): Jesús Iván Martínez-Ortega, Jacqueline E Mut Quej, and Samantha Franco González. Malassezia folliculitis: pathogenesis and diagnostic challenges. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73429, doi:10.7759/cureus.73429. This article has 8 citations.

2. (morenoarrones2023folliculitisdecalvanshas pages 8-8): Oscar M. Moreno-Arrones, Carlota Garcia-Hoz, Rosa del Campo, Garbiñe Roy, David Saceda-Corralo, Juan Jimenez-Cauhe, Manuel Ponce-Alonso, Sergio Serrano-Villar, Pedro Jaen, John Paoli, and Sergio Vano-Galvan. Folliculitis decalvans has a heterogeneous microbiological signature and impaired immunological response. Dermatology, 239:454-461, Jan 2023. URL: https://doi.org/10.1159/000529301, doi:10.1159/000529301. This article has 14 citations and is from a peer-reviewed journal.

3. (li2023clinicalandpathological pages 5-6): Yuan Li, Gaihe Chen, Xin Zhou, Xiaole Zheng, Ming Zhang, Xiaojuan Yao, Jiejie Lu, and Xiaohuan Hu. Clinical and pathological analysis of 10 cases of eosinophilic pustular folliculitis. Clinical, Cosmetic and Investigational Dermatology, 16:2467-2472, Sep 2023. URL: https://doi.org/10.2147/ccid.s427718, doi:10.2147/ccid.s427718. This article has 4 citations and is from a peer-reviewed journal.

4. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 3-5): Joanna Nowaczyk, Kamil Fret, Grazyna Kaminska-Winciorek, Lidia Rudnicka, and Joanna Czuwara. Egfr inhibitor-induced folliculitis decalvans: a case series and management guidelines. Anti-Cancer Drugs, 34:942-948, Jan 2023. URL: https://doi.org/10.1097/cad.0000000000001494, doi:10.1097/cad.0000000000001494. This article has 9 citations and is from a peer-reviewed journal.

5. (linz2023clinicalimpactof pages 3-5): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 279 citations.

6. (linz2023clinicalimpactof pages 10-11): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 279 citations.

7. (linz2023clinicalimpactof pages 5-7): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 279 citations.

8. (linz2023clinicalimpactof pages 1-2): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 279 citations.

9. (chalupczak2025malasseziafolliculitisan pages 1-2): Natalia V. Chalupczak and Shari R. Lipner. Malassezia folliculitis: an underdiagnosed mimicker of acneiform eruptions. Journal of Fungi, 11:662, Sep 2025. URL: https://doi.org/10.3390/jof11090662, doi:10.3390/jof11090662. This article has 2 citations.

10. (green2023clinicalcharacteristicsand pages 2-4): Maxwell Green, Aileen M. Feschuk, Nadia Kashetsky, and Howard I. Maibach. Clinical characteristics and treatment outcomes of pityrosporum folliculitis in immunocompetent patients. Archives of Dermatological Research, 315:1-13, Dec 2023. URL: https://doi.org/10.1007/s00403-022-02506-0, doi:10.1007/s00403-022-02506-0. This article has 13 citations and is from a peer-reviewed journal.

11. (green2023clinicalcharacteristicsand pages 1-2): Maxwell Green, Aileen M. Feschuk, Nadia Kashetsky, and Howard I. Maibach. Clinical characteristics and treatment outcomes of pityrosporum folliculitis in immunocompetent patients. Archives of Dermatological Research, 315:1-13, Dec 2023. URL: https://doi.org/10.1007/s00403-022-02506-0, doi:10.1007/s00403-022-02506-0. This article has 13 citations and is from a peer-reviewed journal.

12. (li2023clinicalandpathological pages 1-2): Yuan Li, Gaihe Chen, Xin Zhou, Xiaole Zheng, Ming Zhang, Xiaojuan Yao, Jiejie Lu, and Xiaohuan Hu. Clinical and pathological analysis of 10 cases of eosinophilic pustular folliculitis. Clinical, Cosmetic and Investigational Dermatology, 16:2467-2472, Sep 2023. URL: https://doi.org/10.2147/ccid.s427718, doi:10.2147/ccid.s427718. This article has 4 citations and is from a peer-reviewed journal.

13. (li2025successfultreatmentof pages 8-8): Wanni Li, Xiaohuan Hu, Yuan Li, and Gaihe Chen. Successful treatment of eosinophilic pustular folliculitis with secondary follicular mucin deposition using indomethacin: an atypical case and literature review. Clinical, Cosmetic and Investigational Dermatology, 18:1063-1070, May 2025. URL: https://doi.org/10.2147/ccid.s520968, doi:10.2147/ccid.s520968. This article has 0 citations and is from a peer-reviewed journal.

14. (danielson2025dermatologiclesionswith pages 3-4): David T. Danielson, Ian Lagerstrom, Zachary Wary, Aaron Auerbach, and David S. Cassarino. Dermatologic lesions with eosinophilia in the head and neck. Head and Neck Pathology, Feb 2025. URL: https://doi.org/10.1007/s12105-025-01757-3, doi:10.1007/s12105-025-01757-3. This article has 1 citations and is from a peer-reviewed journal.

15. (li2023clinicalandpathological media 4cdf4055): Yuan Li, Gaihe Chen, Xin Zhou, Xiaole Zheng, Ming Zhang, Xiaojuan Yao, Jiejie Lu, and Xiaohuan Hu. Clinical and pathological analysis of 10 cases of eosinophilic pustular folliculitis. Clinical, Cosmetic and Investigational Dermatology, 16:2467-2472, Sep 2023. URL: https://doi.org/10.2147/ccid.s427718, doi:10.2147/ccid.s427718. This article has 4 citations and is from a peer-reviewed journal.

16. (morenoarrones2023folliculitisdecalvanshas pages 2-3): Oscar M. Moreno-Arrones, Carlota Garcia-Hoz, Rosa del Campo, Garbiñe Roy, David Saceda-Corralo, Juan Jimenez-Cauhe, Manuel Ponce-Alonso, Sergio Serrano-Villar, Pedro Jaen, John Paoli, and Sergio Vano-Galvan. Folliculitis decalvans has a heterogeneous microbiological signature and impaired immunological response. Dermatology, 239:454-461, Jan 2023. URL: https://doi.org/10.1159/000529301, doi:10.1159/000529301. This article has 14 citations and is from a peer-reviewed journal.

17. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 1-3): Joanna Nowaczyk, Kamil Fret, Grazyna Kaminska-Winciorek, Lidia Rudnicka, and Joanna Czuwara. Egfr inhibitor-induced folliculitis decalvans: a case series and management guidelines. Anti-Cancer Drugs, 34:942-948, Jan 2023. URL: https://doi.org/10.1097/cad.0000000000001494, doi:10.1097/cad.0000000000001494. This article has 9 citations and is from a peer-reviewed journal.

18. (martinezortega2024malasseziafolliculitispathogenesis pages 6-7): Jesús Iván Martínez-Ortega, Jacqueline E Mut Quej, and Samantha Franco González. Malassezia folliculitis: pathogenesis and diagnostic challenges. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73429, doi:10.7759/cureus.73429. This article has 8 citations.

19. (martinezortega2024malasseziafolliculitispathogenesis pages 1-3): Jesús Iván Martínez-Ortega, Jacqueline E Mut Quej, and Samantha Franco González. Malassezia folliculitis: pathogenesis and diagnostic challenges. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73429, doi:10.7759/cureus.73429. This article has 8 citations.

20. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 5-5): Joanna Nowaczyk, Kamil Fret, Grazyna Kaminska-Winciorek, Lidia Rudnicka, and Joanna Czuwara. Egfr inhibitor-induced folliculitis decalvans: a case series and management guidelines. Anti-Cancer Drugs, 34:942-948, Jan 2023. URL: https://doi.org/10.1097/cad.0000000000001494, doi:10.1097/cad.0000000000001494. This article has 9 citations and is from a peer-reviewed journal.

21. (li2023clinicalandpathological pages 2-5): Yuan Li, Gaihe Chen, Xin Zhou, Xiaole Zheng, Ming Zhang, Xiaojuan Yao, Jiejie Lu, and Xiaohuan Hu. Clinical and pathological analysis of 10 cases of eosinophilic pustular folliculitis. Clinical, Cosmetic and Investigational Dermatology, 16:2467-2472, Sep 2023. URL: https://doi.org/10.2147/ccid.s427718, doi:10.2147/ccid.s427718. This article has 4 citations and is from a peer-reviewed journal.

22. (nowaczyk2023egfrinhibitorinducedfolliculitis pages 5-6): Joanna Nowaczyk, Kamil Fret, Grazyna Kaminska-Winciorek, Lidia Rudnicka, and Joanna Czuwara. Egfr inhibitor-induced folliculitis decalvans: a case series and management guidelines. Anti-Cancer Drugs, 34:942-948, Jan 2023. URL: https://doi.org/10.1097/cad.0000000000001494, doi:10.1097/cad.0000000000001494. This article has 9 citations and is from a peer-reviewed journal.