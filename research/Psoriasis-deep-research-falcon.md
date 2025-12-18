---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:57:24.344938'
end_time: '2025-12-17T19:02:33.119965'
duration_seconds: 308.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Psoriasis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Psoriasis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Psoriasis**.
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
- **Disease Name:** Psoriasis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Psoriasis**.
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


Disease Pathophysiology Research Report: Psoriasis

Target Disease
- Disease Name: Psoriasis
- MONDO ID: MONDO:0005301 (psoriasis)
- Category: Complex

Pathophysiology description
Psoriasis is a chronic, immune-mediated inflammatory disease of the skin with systemic manifestations driven by a self-amplifying cytokine network centered on the IL-23/IL-17 axis, keratinocyte–immune cell feedback loops, and genetically primed dysregulation of innate and adaptive immunity. Dendritic cells, mononuclear phagocytes, and keratinocytes orchestrate Th17/Tc17 responses that sustain epidermal hyperproliferation and barrier dysfunction; in parallel, IL-36–mediated innate inflammation underlies pustular variants. Single-cell and translational studies highlight the persistence of tissue-resident memory T cells and circuit-level reinforcement of inflammation that guide current targeted therapies against IL‑23, IL‑17, and TYK2 signaling (deucravacitinib), with emerging modulators of AHR and other pathways under investigation (krueger2024il23pastpresent pages 5-5, yao2025skinimmunemicroenvironment pages 6-7, li2025interventionsincytokine pages 5-6, shirley2024pathogenesisofinflammation pages 7-9).

1) Core Pathophysiology
- Central cytokine axis and feedback: Antigen-presenting cells in lesional skin produce IL‑23 (p19/p40) and TNF-α, driving Th17/Tc17 effectors that secrete IL‑17A/F and IL‑22; IL‑17 acts on keratinocytes to induce chemokines, AMPs, and further cytokines, establishing a positive feedback loop that sustains chronic inflammation and epidermal hyperplasia. Selective IL‑23p19 and IL‑17 inhibitors achieve high and durable clinical clearance in moderate–severe plaque psoriasis, underscoring the axis’ pathogenic dominance (URL: https://doi.org/10.3389/fimmu.2024.1331217; Apr 2024) (krueger2024il23pastpresent pages 5-5). Single-cell and microenvironment-focused reviews emphasize that keratinocyte exposure to IL‑17/IL‑22 triggers additional IL‑23/Th17 axis signaling and tissue-resident memory T-cell persistence that predisposes to recurrence (URL: https://doi.org/10.3389/fimmu.2025.1643418; Aug 2025) (yao2025skinimmunemicroenvironment pages 6-7).
- Keratinocyte signaling programs: Keratinocyte hyperproliferation and aberrant differentiation are potentiated by STAT3 and NF‑κB activation downstream of IL‑22/IL‑17/TNF; genetic and pharmacologic evidence link TYK2/JAK signaling to Th17 biology and keratinocyte responses. Loss-of-function TYK2 variants reduce risk, and JAK/TYK2 inhibitors show efficacy. AHR dysregulation modulates epidermal hyperplasia and cytokine balance, indicating a role for xenobiotic and photometabolic pathways in epidermal control (URL: https://doi.org/10.3390/ijms251810152; Sep 2024) (shirley2024pathogenesisofinflammation pages 7-9). Oxidative stress and cGAS–STING/type I IFN pathways can augment these signals and couple innate sensing to Th17 responses (URL: https://doi.org/10.3389/fimmu.2025.1573905; Apr 2025) (li2025interventionsincytokine pages 5-6).
- Dendritic cell–T cell crosstalk: Plasmacytoid DCs release type I IFNs that activate myeloid DCs, which produce IL‑12 and IL‑23 to drive Th1/Th17 polarization; the resulting IL‑17/IL‑22 milieu drives keratinocyte proliferation and neutrophil recruitment, with LL37/AMPs further amplifying DC activation (URL: https://doi.org/10.3389/fimmu.2025.1573905; Apr 2025; URL: https://doi.org/10.7759/cureus.68569; Sep 2024) (li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).
- Innate IL‑36 pathway in pustular disease: Keratinocyte‑derived IL‑36 cytokines activate IL‑36R→NF‑κB signaling to induce chemokines, inhibit differentiation, and recruit neutrophils. Genetic or functional imbalance between IL‑36 agonists and IL‑36RN (IL‑36Ra) is a hallmark of pustular psoriasis; clinical targeting of IL‑36R has shown benefit in generalized pustular psoriasis (URL: https://doi.org/10.3389/fimmu.2025.1643418; Aug 2025) (yao2025skinimmunemicroenvironment pages 6-7).

2) Key Molecular Players
- Genes/Proteins (HGNC symbols):
  - IL23A (IL‑23p19), IL12B (p40), IL23R: genetic and mechanistic contributors to Th17 maintenance; protective and risk alleles identified across GWAS; central therapeutic targets (krueger2024il23pastpresent pages 5-5, radu2025naturallyderivedbioactive pages 3-5).
  - IL17A/IL17F, IL17RA: effector cytokines/receptor mediating keratinocyte activation and neutrophil mobilization (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6).
  - TYK2: kinase transducing IL‑23/IL‑12 signals; LoF variants protective; therapeutic target of deucravacitinib (shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6).
  - CARD14: keratinocyte NF‑κB adaptor; rare variants cause PSORS2 and promote keratinocyte‑intrinsic inflammation (radu2025naturallyderivedbioactive pages 3-5).
  - TRAF3IP2 (Act1): adaptor for IL‑17 receptor signaling; GWAS locus for Th17 signaling (radu2025naturallyderivedbioactive pages 3-5).
  - IL36RN, IL1RL2 (IL‑36R), IL1RAP, AP1S3: IL‑36 pathway and autophagy adaptor genes implicated in pustular forms and innate amplification (yao2025skinimmunemicroenvironment pages 6-7, radu2025naturallyderivedbioactive pages 3-5, li2025interventionsincytokine pages 5-6).
  - HLA‑C*06:02 (PSORS1): strongest MHC class I risk allele; associated with early-onset/guttate phenotypes and treatment response heterogeneity (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).
  - LCE3B/C deletions, ERAP1, IFIH1: barrier and antigen processing/IFN pathway contributors (radu2025naturallyderivedbioactive pages 3-5).
- Chemical entities/classes:
  - Biologics targeting IL‑23 (risankizumab, guselkumab, tildrakizumab) and IL‑17/IL‑17RA (secukinumab, ixekizumab, brodalumab) demonstrate high clearance rates and durable control; IL‑23 inhibitors often provide superior long-term durability with slower onset versus IL‑17A inhibitors (krueger2024il23pastpresent pages 5-5).
  - Oral TYK2 inhibitor deucravacitinib modulates IL‑23/IL‑12 signaling; benefits reported in plaque psoriasis (li2025interventionsincytokine pages 5-6).
  - AHR pathway modulators under investigation; AHR dysregulation affects epidermal hyperplasia and cytokines (shirley2024pathogenesisofinflammation pages 7-9).
- Cell types (CL terms):
  - Keratinocytes (epidermal): primary responders/amplifiers of IL‑17/IL‑22/TNF; source of IL‑36 and AMPs (shirley2024pathogenesisofinflammation pages 7-9, yao2025skinimmunemicroenvironment pages 6-7).
  - Dendritic cells: plasmacytoid and myeloid DCs initiate and sustain Th17 responses (li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).
  - Th17/Tc17 cells and tissue-resident memory T cells: key effectors and persistence drivers (yao2025skinimmunemicroenvironment pages 6-7, krueger2024il23pastpresent pages 5-5).
  - Neutrophils: downstream of IL‑17/IL‑36, prominent in pustular forms (yao2025skinimmunemicroenvironment pages 6-7, li2025interventionsincytokine pages 5-6).
- Anatomical locations (UBERON): epidermis and dermis of skin; lesional niches enriched for DCs and TRM T cells with keratinocyte–immune crosstalk (krueger2024il23pastpresent pages 5-5, yao2025skinimmunemicroenvironment pages 6-7).

3) Biological Processes (candidate GO terms; evidence-linked)
- Th17 cell differentiation and maintenance by IL‑23 signaling; JAK/TYK2–STAT pathways (krueger2024il23pastpresent pages 5-5, shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6).
- Response to interleukin‑17; chemokine-mediated neutrophil chemotaxis; antimicrobial peptide production by keratinocytes (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).
- NF‑κB signaling in keratinocytes; regulation of keratinocyte proliferation and differentiation; STAT3 activation by IL‑22 (shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6).
- IL‑36 signaling and neutrophil recruitment; innate immune activation (yao2025skinimmunemicroenvironment pages 6-7).
- Type I interferon signaling and cGAS–STING activation downstream of oxidative DNA damage (li2025interventionsincytokine pages 5-6).

4) Cellular Components (candidate GO-CC terms)
- Plasma membrane/cytokine receptor complexes (IL‑23R/IL‑12R/IL‑17RA complexes) in T cells and keratinocytes (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6).
- Cytosol and nucleus for STAT3/NF‑κB transcriptional programs in keratinocytes (shirley2024pathogenesisofinflammation pages 7-9).
- Extracellular space for cytokines/chemokines and antimicrobial peptides; epidermal/dermal interstitial microenvironment of lesions (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).

5) Disease Progression
- Initiation: Environmental triggers (infection, trauma, stress) and genetic predisposition activate innate sensors (TLRs, cGAS–STING) and plasmacytoid DCs → type I IFN and TNF; myeloid DC activation produces IL‑23/IL‑12 (shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6).
- Amplification: IL‑23 sustains Th17/Tc17; IL‑17A/F and IL‑22 drive keratinocyte proliferation, AMP and chemokine release; keratinocytes feed back to immune cells, reinforcing IL‑23/Th17 axis; TRM cells persist and predispose to relapse after therapy (yao2025skinimmunemicroenvironment pages 6-7, krueger2024il23pastpresent pages 5-5).
- Chronicity: Circuit-level reinforcement via NF‑κB/STAT3 in keratinocytes, oxidative stress/type I IFN, and continued DC–T cell crosstalk sustains plaques; in pustular forms, IL‑36 dysregulation produces neutrophilic inflammation (li2025interventionsincytokine pages 5-6, yao2025skinimmunemicroenvironment pages 6-7).

6) Phenotypic Manifestations and Comorbidities
- Clinical phenotypes (HP terms):
  - Chronic plaque psoriasis (erythematous scaly plaques; acanthosis; neutrophils in stratum corneum) linked to IL‑23/IL‑17 dominance (krueger2024il23pastpresent pages 5-5, jauregui2024sharedpathophysiologyof pages 3-5).
  - Guttate psoriasis often associated with HLA‑Cw6 and heightened Th17 signatures (li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5).
  - Generalized pustular psoriasis characterized by IL‑36 pathway activation, keratinocyte-derived IL‑36, and neutrophilia (yao2025skinimmunemicroenvironment pages 6-7, li2025interventionsincytokine pages 5-6).
- Systemic inflammation and comorbidities: Psoriasis is systemic with links to psoriatic arthritis, IBD, and cardiovascular/metabolic disease; IL‑23/Th17 biology and chronic inflammation are implicated. IL‑23 inhibitors show durable efficacy and systemic benefits in psoriatic disease management frameworks (URL: https://doi.org/10.3389/fimmu.2024.1331217; Apr 2024) (krueger2024il23pastpresent pages 5-5).

7) Microbiome in Pathogenesis
- Gut–skin axis: Psoriasis associates with gut dysbiosis, including Firmicutes/Bacteroidetes imbalance and SCFA depletion; dysbiosis modulates immune tone (Th17/Treg balance) and may exacerbate systemic inflammation and lesions (URL: https://doi.org/10.7759/cureus.68569; Sep 2024) (jauregui2024sharedpathophysiologyof pages 3-5). Narrative mechanistic synthesis reports increased Prevotella and reduced SCFAs in psoriasis, and highlights adjunctive microbiome-modulating strategies as areas of investigation (URL: https://doi.org/10.3389/fimmu.2025.1573905; Apr 2025) (li2025interventionsincytokine pages 5-6).
- Skin microbiome: Dysbiosis with increased streptococci and decreased commensals reported; keratinocyte AMP overexpression (LL37/β-defensins/S100s) links microbial signals to DC activation and type I IFN (URL: https://doi.org/10.7759/cureus.68569; Sep 2024) (jauregui2024sharedpathophysiologyof pages 3-5).

8) Current Applications and Therapeutic Implications (2023–2024 priority)
- IL‑23 selective inhibition: Guselkumab, risankizumab, and tildrakizumab are approved for moderate–severe plaque psoriasis; head‑to‑head trials and long-term extensions show superior durability to TNF and some IL‑17 agents, with potential for sustained responses after withdrawal, although onset can be slower than IL‑17A blockers (URL: https://doi.org/10.3389/fimmu.2024.1331217; Apr 2024) (krueger2024il23pastpresent pages 5-5).
- IL‑17 pathway inhibition: IL‑17A (secukinumab, ixekizumab) and IL‑17RA (brodalumab) rapidly suppress keratinocyte inflammatory programs and neutrophilic signatures; highly effective for plaque disease (krueger2024il23pastpresent pages 5-5).
- TYK2 inhibition: Deucravacitinib (selective TYK2 allosteric inhibitor) addresses IL‑23/IL‑12 signaling with demonstrated efficacy in plaque psoriasis; genetic TYK2 LoF supports target validity (URL: https://doi.org/10.3399/fimmu.2025.1573905; Apr 2025; URL: https://doi.org/10.3390/ijms251810152; Sep 2024) (li2025interventionsincytokine pages 5-6, shirley2024pathogenesisofinflammation pages 7-9).
- IL‑36 pathway targeting: The IL‑36 axis is pivotal in generalized pustular psoriasis; clinical proof-of-concept with IL‑36R blockade aligns with mechanistic role (yao2025skinimmunemicroenvironment pages 6-7).
- AHR modulators: AHR dysregulation contributes to epidermal hyperplasia and cytokine balance; antagonists/ligands are under investigation as keratinocyte-directed therapies (URL: https://doi.org/10.3390/ijms251810152; Sep 2024) (shirley2024pathogenesisofinflammation pages 7-9).

Expert opinions and analysis
- “IL‑23…is a hierarchically dominant regulatory cytokine in a cluster of immune-mediated inflammatory diseases (IMIDs), including psoriasis…Selective IL‑23p19 inhibitors…are approved…show superior efficacy versus adalimumab, secukinumab, and ustekinumab in head‑to‑head trials, achieve high durable responses… and can maintain benefit after treatment withdrawal” (Krueger et al., 2024; URL: https://doi.org/10.3389/fimmu.2024.1331217) (krueger2024il23pastpresent pages 5-5).
- “IL‑17A/F are pivotal effectors and IL‑23 (p19/p40) drives Th17/Tc17 populations…TRM cells are long-lived pathogenic drivers…The IL‑36 family…links to pustular phenotypes” (Yao et al., 2025; URL: https://doi.org/10.3389/fimmu.2025.1643418) (yao2025skinimmunemicroenvironment pages 6-7).
- “JAK–STAT pathway is central: IL‑22 activates TYK2/JAK1, IL‑23 activates JAK2/TYK2…TYK2 loss‑of‑function decreases disease risk…AHR dysregulation…modulates epidermal hyperplasia and cytokine balance” (Shirley et al., 2024; URL: https://doi.org/10.3390/ijms251810152) (shirley2024pathogenesisofinflammation pages 7-9).

Relevant statistics and data
- Dominant therapeutic axis: Multiple head-to-head clinical comparisons summarized in expert roadmap show IL‑23 inhibitors’ superior durability and high PASI90/100 rates vs TNF and some IL‑17 agents in moderate–severe plaque psoriasis, with responses maintained up to 5 years and post-withdrawal durability in subsets (Krueger et al., 2024) (krueger2024il23pastpresent pages 5-5).
- Genetic architecture: GWAS and exome studies implicate HLA‑C*06:02 (PSORS1), IL23/IL12 pathways (IL12B, IL23A/IL23R), TYK2, TRAF3IP2, CARD14, barrier genes (LCE3B/C), ERAP1, and interferon signaling (IFIH1), consistent with Th17/keratinocyte–NF‑κB biology (Radu et al., 2025) (radu2025naturallyderivedbioactive pages 3-5).
- Microbiome patterns: Reviews synthesize Firmicutes/Bacteroidetes imbalance, increased Streptococcus on skin, and reduced SCFAs in gut, collectively supporting a Th17‑skewing milieu (Jauregui et al., 2024; Li et al., 2025) (jauregui2024sharedpathophysiologyof pages 3-5, li2025interventionsincytokine pages 5-6).

Evidence items (primary texts; URLs and dates)
- Krueger JG et al. IL‑23 past, present, and future: a roadmap… Frontiers in Immunology. Apr 2024. https://doi.org/10.3389/fimmu.2024.1331217 (krueger2024il23pastpresent pages 5-5)
- Yao Y et al. Skin immune microenvironment in psoriasis: from bench to bedside. Frontiers in Immunology. Aug 2025. https://doi.org/10.3389/fimmu.2025.1643418 (yao2025skinimmunemicroenvironment pages 6-7)
- Shirley SN et al. Pathogenesis of inflammation in skin disease: IJMS. Sep 2024. https://doi.org/10.3390/ijms251810152 (shirley2024pathogenesisofinflammation pages 7-9)
- Li L et al. Interventions in cytokine signaling: novel horizons… Frontiers in Immunology. Apr 2025. https://doi.org/10.3389/fimmu.2025.1573905 (li2025interventionsincytokine pages 5-6)
- Radu A et al. Naturally derived bioactives… Inflammopharmacology. Nov 2025. https://doi.org/10.1007/s10787-024-01602-z (radu2025naturallyderivedbioactive pages 3-5)
- Jauregui W et al. Shared pathophysiology of IBD and psoriasis. Cureus. Sep 2024. https://doi.org/10.7759/cureus.68569 (jauregui2024sharedpathophysiologyof pages 3-5)
- Shokoufa P, Aghaei M. Advances in molecular pathogenesis and therapy. GMJ. May 2025. https://doi.org/10.31661/gmj.vi.3854 (shokoufa2025advancesinthe pages 1-3)
- Dascălu RC et al. Contemporary insight into psoriasis pathogenesis. J Pers Med. May 2024. https://doi.org/10.3390/jpm14050535 (dascalu2024reviewacontemporary pages 14-16)

Structured annotations for knowledge-base integration
- Genes/proteins (HGNC): IL23A; IL12B; IL23R; IL17A/IL17F; IL17RA; TYK2; CARD14; TRAF3IP2; IL36RN; IL1RL2; IL1RAP; AP1S3; HLA‑C (krueger2024il23pastpresent pages 5-5, radu2025naturallyderivedbioactive pages 3-5, li2025interventionsincytokine pages 5-6, yao2025skinimmunemicroenvironment pages 6-7, jauregui2024sharedpathophysiologyof pages 3-5).
- Biological processes (GO BP): Th17 cell differentiation; response to interleukin‑17; keratinocyte proliferation; NF‑κB signaling; JAK–STAT cascade; cytokine-mediated signaling; neutrophil chemotaxis; type I interferon signaling; IL‑36 signaling pathway (krueger2024il23pastpresent pages 5-5, shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6, yao2025skinimmunemicroenvironment pages 6-7).
- Cellular components (GO CC): plasma membrane cytokine receptor complexes (IL‑23R/IL‑12R/IL‑17RA); cytosol and nucleus (STAT3/NF‑κB transcriptional machinery); extracellular space (cytokines/chemokines/AMPs) (shirley2024pathogenesisofinflammation pages 7-9, krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6).
- Cell types (CL): keratinocyte; plasmacytoid dendritic cell; conventional/myeloid dendritic cell; Th17/Tc17 cell; tissue-resident memory T cell; neutrophil (yao2025skinimmunemicroenvironment pages 6-7, li2025interventionsincytokine pages 5-6, jauregui2024sharedpathophysiologyof pages 3-5, krueger2024il23pastpresent pages 5-5).
- Anatomical locations (UBERON): skin epidermis and dermis; lesional microenvironments enriched for DCs/TRM (krueger2024il23pastpresent pages 5-5, yao2025skinimmunemicroenvironment pages 6-7).
- Chemical entities (classes; CHEBI mapping where appropriate): IL‑23/IL‑17 biological antagonists; TYK2 inhibitor (deucravacitinib); experimental AHR modulators (krueger2024il23pastpresent pages 5-5, li2025interventionsincytokine pages 5-6, shirley2024pathogenesisofinflammation pages 7-9).
- Phenotypes (HP): psoriasiform dermatitis; chronic plaque psoriasis; guttate psoriasis; generalized pustular psoriasis; nail and scalp involvement (mechanistic mapping emphasized for plaque/pustular) (yao2025skinimmunemicroenvironment pages 6-7, li2025interventionsincytokine pages 5-6, krueger2024il23pastpresent pages 5-5, jauregui2024sharedpathophysiologyof pages 3-5).

Quotable excerpts supporting key statements
- “IL‑23…is a hierarchically dominant regulatory cytokine in…psoriasis…Selective IL‑23p19 inhibitors…show superior efficacy…achieve high durable responses…and can maintain benefit after treatment withdrawal” (krueger2024il23pastpresent pages 5-5).
- “IL‑17A/F are pivotal effectors and IL‑23 (p19/p40) drives Th17/Tc17…TRM cells are long-lived pathogenic drivers…The IL‑36 family…links to pustular phenotypes” (yao2025skinimmunemicroenvironment pages 6-7).
- “The JAK–STAT pathway is central: IL‑22 activates TYK2/JAK1, IL‑23 activates JAK2/TYK2…TYK2 loss-of-function decreases disease risk…AHR dysregulation…modulates epidermal hyperplasia” (shirley2024pathogenesisofinflammation pages 7-9).
- “pDCs release TNF and type I IFNs and activate mDCs to produce IL‑12/IL‑23 that drive Th1/Th17 responses” with oxidative stress and cGAS–STING augmenting type I IFN and Th17 pathways (li2025interventionsincytokine pages 5-6).
- “Genome-wide…link susceptibility to…HLA‑C, ERAP1…Th17 activation (TRAF3IP2, IL12B, IL23R, IL23A)… and type I interferon signaling (IFIH1, TYK2)” (radu2025naturallyderivedbioactive pages 3-5).

Limitations and evidence gaps
- While single-cell and spatial studies are rapidly refining stromal/immune states and lesion dynamics, high-resolution fibroblast-state data and early on-treatment cellular kinetics—crucial for precision stratification—are still being generalized from limited cohorts and were only partially represented in the sources reviewed here (yao2025skinimmunemicroenvironment pages 6-7, shokoufa2025advancesinthe pages 1-3). Additional integration with large longitudinal scRNA-seq/spatial datasets will improve cellular ontologies and therapeutic response prediction.

Summary
Psoriasis pathophysiology centers on an IL‑23→Th17→IL‑17/IL‑22 axis that drives keratinocyte NF‑κB/STAT3 activation, epidermal hyperproliferation, and multi-cellular feedback involving DCs, TRM T cells, and neutrophils; pustular variants feature IL‑36–dominated innate cascades. Genetic architecture maps strongly to MHC class I (HLA‑C*06:02), Th17 signaling (IL12B/IL23A/IL23R/TYK2/TRAF3IP2), keratinocyte NF‑κB (CARD14), and innate IL‑36/autophagy circuits (IL36RN, AP1S3). Dysbiosis of skin and gut microbiota likely skews immune tone toward Th17. These insights rationalize current first-line targeted interventions (IL‑23/IL‑17 biologics, TYK2 inhibition) and motivate investigation of keratinocyte‑directed AHR modulation and IL‑36 blockade for pustular disease (krueger2024il23pastpresent pages 5-5, yao2025skinimmunemicroenvironment pages 6-7, shirley2024pathogenesisofinflammation pages 7-9, li2025interventionsincytokine pages 5-6, radu2025naturallyderivedbioactive pages 3-5, jauregui2024sharedpathophysiologyof pages 3-5).

References

1. (krueger2024il23pastpresent pages 5-5): J. G. Krueger, K. Eyerich, Vijay K. Kuchroo, C. Ritchlin, M. T. Abreu, M. M. Elloso, Anne M. Fourie, S. Fakharzadeh, Jonathan P Sherlock, Ya-Wen Yang, Daniel J. Cua, Iain B. McInnes, Soren Skov, Daniella Schwartz, and Maria N. Navarro. Il-23 past, present, and future: a roadmap to advancing il-23 science and therapy. Frontiers in immunology, 15:1331217, Apr 2024. URL: https://doi.org/10.3389/fimmu.2024.1331217, doi:10.3389/fimmu.2024.1331217. This article has 85 citations and is from a peer-reviewed journal.

2. (yao2025skinimmunemicroenvironment pages 6-7): Yi Yao, Li-Qing Chen, Yi-Bo Lv, Shun-Li Tang, Wei Shen, Hui Sun, and Hua-Jie Zhong. Skin immune microenvironment in psoriasis: from bench to bedside. Frontiers in Immunology, Aug 2025. URL: https://doi.org/10.3389/fimmu.2025.1643418, doi:10.3389/fimmu.2025.1643418. This article has 1 citations and is from a peer-reviewed journal.

3. (li2025interventionsincytokine pages 5-6): Lisha Li, Jun Liu, Jiaye Lu, Junchao Wu, Xinyue Zhang, Tianyou Ma, Xiying Wu, Quangang Zhu, Zhongjian Chen, and Zongguang Tai. Interventions in cytokine signaling: novel horizons for psoriasis treatment. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1573905, doi:10.3389/fimmu.2025.1573905. This article has 5 citations and is from a peer-reviewed journal.

4. (shirley2024pathogenesisofinflammation pages 7-9): Simona N. Shirley, Abigail E. Watson, and Nabiha Yusuf. Pathogenesis of inflammation in skin disease: from molecular mechanisms to pathology. International Journal of Molecular Sciences, 25:10152, Sep 2024. URL: https://doi.org/10.3390/ijms251810152, doi:10.3390/ijms251810152. This article has 29 citations and is from a poor quality or predatory journal.

5. (jauregui2024sharedpathophysiologyof pages 3-5): Walter Jauregui, Yozahandy A Abarca, Yasmin Ahmadi, Vaishnavi B Menon, Daniela A Zumárraga, Maria Camila Rojas Gomez, Aleeza Basri, Rohitha S Madala, Peter Girgis, and Zahra Nazir. Shared pathophysiology of inflammatory bowel disease and psoriasis: unraveling the connection. Cureus, Sep 2024. URL: https://doi.org/10.7759/cureus.68569, doi:10.7759/cureus.68569. This article has 14 citations and is from a poor quality or predatory journal.

6. (radu2025naturallyderivedbioactive pages 3-5): Ada Radu, Delia Mirela Tit, Laura Maria Endres, Andrei-Flavius Radu, Cosmin Mihai Vesa, and Simona Gabriela Bungau. Naturally derived bioactive compounds as precision modulators of immune and inflammatory mechanisms in psoriatic conditions. Inflammopharmacology, 33:527-549, Nov 2025. URL: https://doi.org/10.1007/s10787-024-01602-z, doi:10.1007/s10787-024-01602-z. This article has 24 citations and is from a peer-reviewed journal.

7. (shokoufa2025advancesinthe pages 1-3): Parivash Shokoufa and Mahsa Aghaei. Advances in the molecular pathogenesis and targeted therapy of psoriasis. Galen Medical Journal, pages e3854, May 2025. URL: https://doi.org/10.31661/gmj.vi.3854, doi:10.31661/gmj.vi.3854. This article has 0 citations.

8. (dascalu2024reviewacontemporary pages 14-16): Rucsandra Cristina Dascălu, Andreea Lili Bărbulescu, Loredana Elena Stoica, Ștefan Cristian Dinescu, Cristina Elena Biță, Horațiu Valeriu Popoviciu, Răzvan Adrian Ionescu, and Florentin Ananu Vreju. Review: a contemporary, multifaced insight into psoriasis pathogenesis. Journal of Personalized Medicine, 14:535, May 2024. URL: https://doi.org/10.3390/jpm14050535, doi:10.3390/jpm14050535. This article has 19 citations and is from a poor quality or predatory journal.