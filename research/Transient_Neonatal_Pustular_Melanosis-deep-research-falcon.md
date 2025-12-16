---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:54:21.597679'
end_time: '2025-12-15T10:01:59.106334'
duration_seconds: 457.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Transient Neonatal Pustular Melanosis
  mondo_id: ''
  category: Skin Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Transient Neonatal Pustular Melanosis
- **MONDO ID:**  (if available)
- **Category:** Skin Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Transient Neonatal Pustular Melanosis**.
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
- **Disease Name:** Transient Neonatal Pustular Melanosis
- **MONDO ID:**  (if available)
- **Category:** Skin Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Transient Neonatal Pustular Melanosis**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Transient Neonatal Pustular Melanosis (TNPM)
- MONDO ID: Not clearly defined in MONDO as of 2025; often indexed under neonatal transient pustular eruptions
- Category: Skin Disorder

## Pathophysiology Description
TNPM is a benign, self-limited neonatal pustular eruption characterized by sterile, fragile, milky-white to yellow pustules present at birth that rupture easily, leaving hyperpigmented macules with a peripheral collarette of fine scale. Cytology of pustule contents typically shows neutrophil predominance, while histopathology reveals intra- or subcorneal collections of neutrophils with scattered eosinophils and basal/suprabasal increased pigmentation without pigmentary incontinence. Proposed mechanisms include a physiologic, innate immune response of neonatal epidermis—potentially a variant of erythema toxicum neonatorum—and a response to early skin colonization by commensal microbiota. TNPM requires no treatment and resolves spontaneously, with residual hyperpigmentation lasting weeks to months (mahon2019vesiculopustularbullousand pages 8-10).

Incidence overall is estimated at approximately 0.5–1%, with higher frequency reported among infants of African ancestry (around 4.4%); recent single-center observational studies report TNPM among neonatal dermatoses at ~2–3% in mixed cohorts, consistent with earlier race-stratified observations (mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8).

|Entity type|Specific term (ID)|Role in TNPM (one sentence)|Evidence|
|---|---|---|---|
|Gene/Protein|None reported|No specific causal genes have been identified for TNPM; etiology remains unclear and is considered possibly a variant of ETN.|(mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9)|
|Cell type|Neutrophil (CL:0000776)|Predominant cell in pustule smears and intra-/subcorneal pustules, indicating a neutrophil-predominant sterile pustular response.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Cell type|Keratinocyte (CL:0000312)|Epidermal cells forming the intra-/subcorneal pustules and source of the peripheral collarette of scale.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Cell type|Melanocyte (CL:0000148)|Contributes to basal/suprabasal increased pigmentation leading to persistent hyperpigmented macules after pustule rupture.|(mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9)|
|Biological process|Neutrophil chemotaxis (GO:0030593)|Likely mediates recruitment of neutrophils into the epidermis producing pustule formation.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Biological process|Epidermis development (GO:0008544)|Altered superficial epidermal architecture with pustule formation and rapid re-epithelialization on healing.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Biological process|Keratinization (GO:0031424)|Terminal differentiation/keratinocyte responses contribute to scale/collarette formation and lesion resolution.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Biological process|Pigmentation (GO:0043473)|Increased basal/suprabasal pigmentation explains the residual pigmented macules following pustule rupture.|(mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9)|
|Cellular component|Stratum corneum (GO:0001533)|Described site of intra- or subcorneal pustule formation on histology/biopsy.|(mahon2019vesiculopustularbullousand pages 8-10)|
|Cellular component|Stratum spinosum (GO:0071454)|Adjacent epidermal layer involved in the epidermal inflammatory response and pustule architecture.|(mahon2019vesiculopustularbullousand pages 17-18)|
|Cellular component|Extracellular space (GO:0005615)|Pustule fluid and neutrophil-rich exudate occupy extracellular epidermal spaces forming visible pustules.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Phenotype|Neonatal pustules (HP:0000970)|Primary clinical lesion: fragile milky/yellow pustules usually present at or shortly after birth that rupture easily.|(mahon2019vesiculopustularbullousand pages 8-10)|
|Phenotype|Hyperpigmented macules (HP:0001035)|Residual pea-sized pigmented macules with peripheral collarette of scale that may persist for weeks to months.|(mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8)|
|Phenotype|Scaling/collarette (HP:0000988)|Fine peripheral collarette of scale around healed lesions reflecting superficial epidermal involvement.|(mahon2019vesiculopustularbullousand pages 8-10)|
|Anatomy|Epidermis (UBERON:0001003)|Primary tissue layer involved; lesions are epidermal (intra-/subcorneal) in location.|(mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18)|
|Anatomy|Skin of face (UBERON:0001456)|Commonly affected site (forehead, cheeks, bitemporal areas).|(mahon2019vesiculopustularbullousand pages 8-10)|
|Anatomy|Neck (UBERON:0000974)|Frequent anatomical location for lesions.|(mahon2019vesiculopustularbullousand pages 8-10)|
|Anatomy|Back (UBERON:0002410)|Frequent anatomical location for lesions.|(mahon2019vesiculopustularbullousand pages 8-10)|
|Anatomy|Palms/Soles (UBERON:0002398, UBERON:0002387)|Less commonly involved but reported in some series.|(mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8)|
|Chemical|Prostaglandin E2 (ChEBI:15551)|Increased PGE2 has been hypothesized in some transient neonatal eruptions and suggested as a possible mediator in older reviews.|(larralde2019transientskindisorders pages 7-9)|
|Chemical|Melanin (ChEBI:28790)|Primary pigment composing residual hyperpigmented macules due to increased basal/suprabasal pigmentation.|(mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9)|


*Table: Concise knowledge-base table mapping entity types (genes, cells, processes, components, phenotypes, anatomy, chemicals) to their roles in Transient Neonatal Pustular Melanosis with evidence citations to the provided context IDs; useful for ontology annotation and rapid reference.*

## 1. Core Pathophysiology
- Primary mechanisms: sterile neutrophil-predominant intra-/subcorneal pustules that rupture, followed by transient postinflammatory basal/suprabasal melanization; absence of significant dermal inflammation or vasculitis on biopsy; no mucosal involvement. Smears are neutrophil-rich (distinguishing from ETN’s eosinophil-rich smears) (mahon2019vesiculopustularbullousand pages 8-10).
- Molecular pathways: direct causal molecular pathways are not established for TNPM. By analogy and expert opinion, innate immune signaling underpinning neutrophil chemotaxis and epidermal barrier adaptation to postnatal microbial colonization are implicated; prostaglandin E2 has been hypothesized historically in transient neonatal eruptions, though not proven specific to TNPM (mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9).
- Cellular processes: neutrophil recruitment to the superficial epidermis; keratinocyte disruption forming superficial pustules and collarettes; melanocyte activity resulting in increased basal/suprabasal melanin deposition causing residual macules (mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): none definitively implicated in TNPM; unlike autoinflammatory pustular disorders (e.g., IL36RN, CARD14) there is no monogenic basis identified (mahon2019vesiculopustularbullousand pages 8-10).
- Chemical entities (ChEBI): prostaglandin E2 (hypothesized mediator in transient neonatal skin responses); melanin as the pigment in residual macules (larralde2019transientskindisorders pages 7-9, mahon2019vesiculopustularbullousand pages 8-10).
- Cell types (CL): neutrophils (predominant in pustules), keratinocytes (epidermal architecture of pustules and scale), melanocytes (basal/suprabasal pigmentation) (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18).
- Anatomical locations (UBERON): epidermis; commonly affected skin of the face (forehead, cheeks, bitemporal areas), neck, and back; palms/soles less often (mahon2019vesiculopustularbullousand pages 8-10).

## 3. Biological Processes (GO terms)
- Neutrophil chemotaxis (GO:0030593): inferred from neutrophil-rich pustules (mahon2019vesiculopustularbullousand pages 8-10).
- Epidermis development (GO:0008544) and keratinization (GO:0031424): reflect superficial epidermal pustule formation and healing with collarette (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18).
- Pigmentation (GO:0043473): increased basal/suprabasal pigmentation underlies residual macules (mahon2019vesiculopustularbullousand pages 8-10, larralde2019transientskindisorders pages 7-9).

## 4. Cellular Components (GO-CC)
- Stratum corneum/cornified envelope (GO:0001533): site of intra- or subcorneal pustule collections (mahon2019vesiculopustularbullousand pages 8-10).
- Stratum spinosum (adjacent layer) and extracellular space (GO:0005615): involved in pustule architecture and exudate (mahon2019vesiculopustularbullousand pages 17-18, mahon2019vesiculopustularbullousand pages 8-10).

## 5. Disease Progression
- Sequence of events: at birth, non-erythematous fragile pustules form in superficial epidermis → easy rupture within hours to days → residual pea-sized hyperpigmented macules with fine peripheral collarette of scale → gradual fading of pigmentation over weeks to months; disease is entirely self-limited and non-scarring (mahon2019vesiculopustularbullousand pages 8-10).
- Stages/phases: pustular phase (sterile, neutrophil-rich, superficial) followed by macular hyperpigmentation phase; often present simultaneously because many pustules rupture in the first hours after birth (mahon2019vesiculopustularbullousand pages 8-10).

## 6. Phenotypic Manifestations
- Key clinical phenotypes: milky/yellow superficial fragile pustules without surrounding erythema; residual hyperpigmented macules with collarette of scale; typical distribution on face/neck/back; palms/soles occasionally; well-appearing infants without systemic symptoms; mucosa spared (mahon2019vesiculopustularbullousand pages 8-10).
- Relation to mechanisms: neutrophil-rich superficial accumulations account for pustules; keratinocyte disruption accounts for collarette; increased basal/suprabasal melanin deposition accounts for hyperpigmented macules (mahon2019vesiculopustularbullousand pages 8-10).

## Recent Developments and Epidemiology (2023–2024)
- A cross-sectional NICU cohort in India (2023) recorded TNPM in 13 of 474 neonates (2.74%); the discussion reiterates historically reported race-stratified incidences (~0.2% White, 4.4% Black). Publication: November 2023; Journal of Family Medicine and Primary Care; URL: https://doi.org/10.4103/jfmpc.jfmpc_513_23 (quazi2023acrosssectionalstudy pages 6-8).
- An outpatient infant dermatoses series (2023) from India listed TNPM among notable neonatal dermatoses and commented on newborn-skin microbial evolution in the first year of life as context for physiologic eruptions. Publication: April 2023; Journal of Skin and Sexually Transmitted Diseases; URL: https://doi.org/10.25259/jsstd_84_2021 (mudang2023patternsofinfant pages 4-5).
- A 2024 tertiary referral hospital study in Pakistan surveyed cutaneous findings in newborns, providing contemporary prevalence context for physiologic neonatal lesions (publication year 2024; Journal of Pakistan Association of Dermatologists). Although TNPM-specific counts were not highlighted in the excerpt, the study contributes to current baseline frequencies of neonatal skin findings (habib2024patternofcutaneous pages 4-6).

## Differential Diagnosis and Expert Analysis
- Versus erythema toxicum neonatorum (ETN): ETN typically arises after the first 24–48 hours with erythematous macules/papules progressing to pustules; cytology shows eosinophil predominance, in contrast to TNPM’s neutrophils; ETN often has an erythematous background and lacks persistent hyperpigmented macules with collarette (mahon2019vesiculopustularbullousand pages 8-10).
- Versus neonatal infections (staphylococcal/streptococcal pyoderma, Candida, HSV, varicella, syphilis): TNPM pustules are sterile; infants are well; mucosa is spared; absence of systemic signs helps discriminate; laboratory confirmation (Gram/KOH/Tzanck/PCR/serology) is reserved for atypical cases (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18).
- Expert consensus emphasizes that most benign neonatal pustular eruptions require no treatment when classic clinical features are present in a well newborn; TNPM is self-limited (mahon2019vesiculopustularbullousand pages 1-2, mahon2019vesiculopustularbullousand pages 8-10).

## Current Applications and Real-World Implementation
- Point-of-care microscopic smear (Wright/Giemsa) to identify neutrophil predominance can support bedside differentiation from ETN and infection, limiting unnecessary antimicrobials and testing (mahon2019vesiculopustularbullousand pages 1-2, mahon2019vesiculopustularbullousand pages 8-10).
- Education of nursery and neonatal teams on classic lesion morphology and evolution reduces unwarranted interventions; reassurance of parents is a key implementation component (mahon2019vesiculopustularbullousand pages 8-10).

## Relevant Statistics and Data
- Overall incidence ~0.5–1% with higher rates (~4.4%) reported in infants of African ancestry; in contemporary hospital-based Indian cohort, TNPM frequency was 2.74% among 474 neonates; hyperpigmented macules may persist for weeks to months (mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8).

## Ontology-Ready Annotations
- Genes/Proteins (HGNC): none definitive; no monogenic etiology identified (mahon2019vesiculopustularbullousand pages 8-10).
- Biological Process (GO): neutrophil chemotaxis (GO:0030593); epidermis development (GO:0008544); keratinization (GO:0031424); pigmentation (GO:0043473) (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18, larralde2019transientskindisorders pages 7-9).
- Cellular Component (GO-CC): stratum corneum/cornified envelope (GO:0001533); extracellular space (GO:0005615) (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18).
- Cell Types (CL): neutrophil (CL:0000776); keratinocyte (CL:0000312); melanocyte (CL:0000148) (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 17-18).
- Anatomy (UBERON): epidermis (UBERON:0001003); skin of face (UBERON:0001456); neck (UBERON:0000974); back (UBERON:0002410); palms (UBERON:0002398); soles (UBERON:0002387) (mahon2019vesiculopustularbullousand pages 8-10).
- Phenotypes (HP): neonatal pustules (HP:0000970); hyperpigmented macules (HP:0001035); scaling skin (HP:0000988) (mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8).
- Chemicals (ChEBI): prostaglandin E2 (ChEBI:15551) [hypothesis]; melanin (ChEBI:28790) (larralde2019transientskindisorders pages 7-9, mahon2019vesiculopustularbullousand pages 8-10).

## Evidence Items with URLs and Dates
- Mahon C, Martinez AE. Vesiculopustular, bullous and erosive diseases of the neonate. Dec 2019. Wiley; DOI: https://doi.org/10.1002/9781119142812.ch11 (mahon2019vesiculopustularbullousand pages 8-10, mahon2019vesiculopustularbullousand pages 1-2).
- Quazi S, et al. A cross-sectional study on the prevalence and determinants of various neonatal dermatoses. Nov 2023. Journal of Family Medicine and Primary Care; DOI: https://doi.org/10.4103/jfmpc.jfmpc_513_23 (quazi2023acrosssectionalstudy pages 6-8).
- Mudang J, et al. Patterns of infant dermatoses. Apr 2023. Journal of Skin and Sexually Transmitted Diseases; DOI: https://doi.org/10.25259/jsstd_84_2021 (mudang2023patternsofinfant pages 4-5).
- Larralde M, Abad ME. Transient skin disorders in the neonate and young infant. Dec 2019. Wiley; DOI: https://doi.org/10.1002/9781119142812.ch6 (larralde2019transientskindisorders pages 7-9).
- Serdaroğlu S, Çakıl B. Physiologic skin findings of newborn. 2008. Journal of Turkish Academy of Dermatology; URL: http://www.jtad.org/2008/4/jtad82401r.pdf (serdaroglu2008physiologicskinfindings pages 2-4).
- Habib A, et al. Pattern of cutaneous manifestations in newborns at a tertiary referral hospital in Pakistan. 2024. Journal of Pakistan Association of Dermatologists; pages 821–828 (habib2024patternofcutaneous pages 4-6).

Limitations: High-quality mechanistic studies in TNPM are scarce; molecular pathways remain speculative. Recent epidemiologic series are single-center and may not generalize across regions or racial/ethnic groups (mahon2019vesiculopustularbullousand pages 8-10, quazi2023acrosssectionalstudy pages 6-8).

References

1. (mahon2019vesiculopustularbullousand pages 8-10): Caroline Mahon and Anna E. Martinez. Vesiculopustular, bullous and erosive diseases of the neonate. ArXiv, pages 134-153, Dec 2019. URL: https://doi.org/10.1002/9781119142812.ch11, doi:10.1002/9781119142812.ch11. This article has 1 citations.

2. (quazi2023acrosssectionalstudy pages 6-8): Sabiha Quazi, Sanjiv Choudhary, Adarshlata Singh, Bhushan Madke, Khalid L Khan, and Sudhir Singh. A cross-sectional study on the prevalence and determinants of various neonatal dermatoses. Journal of Family Medicine and Primary Care, 12:2942-2949, Nov 2023. URL: https://doi.org/10.4103/jfmpc.jfmpc\_513\_23, doi:10.4103/jfmpc.jfmpc\_513\_23. This article has 9 citations and is from a peer-reviewed journal.

3. (larralde2019transientskindisorders pages 7-9): Margarita Larralde and Maria Eugenia Abad. Transient skin disorders in the neonate and young infant. ArXiv, pages 72-83, Dec 2019. URL: https://doi.org/10.1002/9781119142812.ch6, doi:10.1002/9781119142812.ch6. This article has 9 citations.

4. (mahon2019vesiculopustularbullousand pages 17-18): Caroline Mahon and Anna E. Martinez. Vesiculopustular, bullous and erosive diseases of the neonate. ArXiv, pages 134-153, Dec 2019. URL: https://doi.org/10.1002/9781119142812.ch11, doi:10.1002/9781119142812.ch11. This article has 1 citations.

5. (mudang2023patternsofinfant pages 4-5): Jully Mudang, Koyakutty Abdul Samad, Vasanthiamma K. Devakumar, Priya Ashok, and Anuja Elizabeth George. Patterns of infant dermatoses: an observational study from the dermatology outpatient clinic of a tertiary referral center. Journal of Skin and Sexually Transmitted Diseases, 5:28-35, Apr 2023. URL: https://doi.org/10.25259/jsstd\_84\_2021, doi:10.25259/jsstd\_84\_2021. This article has 2 citations.

6. (habib2024patternofcutaneous pages 4-6): A Habib, S Shaheen, S Shahzad, and SGRA Nadir. Pattern of cutaneous manifestations in newborns at a tertiary referral hospital in pakistan. Unknown journal, 2024.

7. (mahon2019vesiculopustularbullousand pages 1-2): Caroline Mahon and Anna E. Martinez. Vesiculopustular, bullous and erosive diseases of the neonate. ArXiv, pages 134-153, Dec 2019. URL: https://doi.org/10.1002/9781119142812.ch11, doi:10.1002/9781119142812.ch11. This article has 1 citations.

8. (serdaroglu2008physiologicskinfindings pages 2-4): S Serdaroğlu and B Çakıl. Physiologic skin findings of newborn. Unknown journal, 2008.