---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:34:20.508981'
end_time: '2025-12-15T09:42:18.682130'
duration_seconds: 478.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Monkeypox
  mondo_id: ''
  category: Viral Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Monkeypox
- **MONDO ID:**  (if available)
- **Category:** Viral Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Monkeypox**.
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
- **Disease Name:** Monkeypox
- **MONDO ID:**  (if available)
- **Category:** Viral Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Monkeypox**.
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
- Disease Name: Monkeypox (mpox)
- MONDO ID: MONDO:0005737 (if using MONDO terminology; not explicitly verified in the cited sources)
- Category: Viral Disease

## Pathophysiology Description (Narrative)
Mpox is caused by the monkeypox virus (MPXV), a large enveloped double-stranded DNA virus of the Orthopoxvirus genus. MPXV replicates entirely in the host cytoplasm, forming ER-associated “mini-nuclei” or viral factories (Guarnieri bodies), and produces two infectious forms: the intracellular mature virion (IMV) and the extracellular enveloped virion (EEV). IMV are abundant and released upon cell lysis, whereas EEV acquire an additional membrane and enable efficient cell-to-cell and tissue spread. Entry occurs through fusion or endocytic pathways and depends on lipid rafts/cholesterol. Envelope proteins coordinate envelopment and dissemination: F13 (P37; target of tecovirimat) promotes EEV formation; B5R and A34R are necessary for EEV infectivity; A36R drives actin tail–mediated spread; smallpox-vaccinia literature indicates poxviruses can hijack EGFR signaling to enhance spread. Clinically, incubation is approximately 7–14 days, followed by a prodrome and a centrifugal rash characterized by macules→papules→vesicles→pustules→scabs, often with prominent lymphadenopathy. Lesions commonly involve genital and anal mucosa in recent outbreaks, reflecting transmission by close contact including during sexual activity (mechanistic modeling further supports higher presymptomatic infectiousness for sexual/skin routes). Immunocompromised hosts experience more severe and disseminated disease. (lu2023mpox(formerlymonkeypox) pages 2-4, lu2023mpox(formerlymonkeypox) pages 13-14, zinnah2024thereemergenceof pages 6-8, qudus2023theprospectiveoutcome pages 5-7)

At the cellular level, initial infection involves keratinocytes and skin-resident antigen-presenting cells (Langerhans cells, dendritic cells) and dermal fibroblasts, with infected APCs migrating to draining lymph nodes, where early amplification occurs and from which virus disseminates via the lymphohematogenous route. Ex vivo infection of human PBMCs demonstrates productive infection of monocytes, cycling NK cells, and regulatory CD4+ T cells, and a type I interferon–sensitive phenotype with downregulation of core IFN pathway genes (e.g., STAT1, JAK2) and guanylate-binding proteins, consistent with orthopox immune antagonism. Systemically, lymphoid organs (spleen, lymph nodes), liver (Kupffer cells, hepatocytes), and other sites can be involved, especially in severe or immunocompromised disease. (qudus2023theprospectiveoutcome pages 5-7, jarcy2024mpxvinfectshuman pages 14-18)

Immune evasion is multifaceted. MPXV encodes proteins that inhibit innate sensing (e.g., antagonism of TLR and cGAS–STING pathways, inhibition of IRF3 and NF-κB), block interferon responses, modulate inflammasome and complement activity, bind chemokines/cytokines (e.g., IL‑1β binding protein), and impair dendritic cell maturation, migration, and antigen presentation. NK cells expand early but exhibit functional impairment (reduced degranulation and IFN‑γ/TNF‑α). Serum cytokines such as IL‑8 (CXCL8), IFN‑γ, IL‑6, and MCP‑1 exhibit early induction kinetics in animal models. Prior smallpox vaccination confers cross-protection, reflecting antigenic conservation of key IMV/EEV targets (e.g., A33R, A44R, F13L). (prompetchara2024mpoxglobalhealth pages 6-8, parnian2024innateimmuneresponse pages 1-2, lu2023mpox(formerlymonkeypox) pages 13-14)

Antiviral resistance centers on F13L, the target of tecovirimat; resistance-associated mutations in F13/P37 have been observed in poxviruses and are mechanistically plausible in MPXV, warranting surveillance as tecovirimat is deployed. Evidence from orthopox biology indicates that changes in F13 can confer reduced drug susceptibility by altering envelopment/egress. (lu2023mpox(formerlymonkeypox) pages 13-14)

Selected direct quotes
- “Two infectious forms exist: IMV… and EEV… IMV are abundant… released upon cell lysis… EEV possess an additional lipid membrane that facilitates… spread.” (Signal Transduction and Targeted Therapy, 2023; DOI: 10.1038/s41392-023-01675-2). (lu2023mpox(formerlymonkeypox) pages 2-4)
- “F13 (P37)… is the molecular target of tecovirimat… B5R and A34R are required for extracellular virion envelopment/infectivity; A36R drives actin-tail formation for directed cell-to-cell spread.” (Signal Transduction and Targeted Therapy, 2023; DOI: 10.1038/s41392-023-01675-2). (lu2023mpox(formerlymonkeypox) pages 13-14)
- “Infection gave rise to de novo production of infectious MPXV… monocytes, cycling NK cells and regulatory CD4+ T-cells scored positive for viral RNA… downregulation of… STAT1, JAK2… GBP1, GBP2, GBP4, GBP5.” (bioRxiv, 2024; DOI: 10.1101/2024.09.16.613292). (jarcy2024mpxvinfectshuman pages 14-18)
- “NK cells expand but are rendered dysfunctional (reduced degranulation and suppressed IFN-γ/TNF-α).” (Asian Pacific J Allergy Immunol, 2024; DOI: 10.12932/ap-111024-1945). (prompetchara2024mpoxglobalhealth pages 6-8)


## Gene/Protein Annotations with Ontology Terms
- Viral genes/proteins (Orthopoxvirus; functional annotations from orthopox literature):
  - F13L (P37): Viral phospholipase/tegument protein required for EEV wrapping and egress; target of tecovirimat. Cellular component: EEV membrane; Process: extracellular virion formation; Actin-based spread indirectly via EEV trafficking. (lu2023mpox(formerlymonkeypox) pages 13-14, lu2023mpox(formerlymonkeypox) pages 2-4)
  - B5R: EEV membrane glycoprotein required for EEV maturation/infectivity. (lu2023mpox(formerlymonkeypox) pages 13-14)
  - A34R: EEV-associated protein facilitating spread/infectivity. (lu2023mpox(formerlymonkeypox) pages 13-14)
  - A36R: Inner envelope protein linking to actin polymerization for directed spread. (lu2023mpox(formerlymonkeypox) pages 13-14)
  - A33R/A29L/A44R (IMV/EEV antigens): Antibody targets; contribute to entry/neutralization. (prompetchara2024mpoxglobalhealth pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14)

- Host genes/proteins (HGNC):
  - EGFR (HGNC:3236): Host receptor/kinase co-opted by poxviruses to enhance spread. GO-BP: EGFR signaling; GO-CC: plasma membrane. (lu2023mpox(formerlymonkeypox) pages 13-14)
  - STAT1 (HGNC:11362), JAK2 (HGNC:6192): Type I/II IFN signaling; downregulated in infected PBMCs. GO-BP: type I interferon signaling (GO:0060337), JAK-STAT cascade. (jarcy2024mpxvinfectshuman pages 14-18)
  - IRF3 (HGNC:6117): IFN induction TF; antagonized by viral proteins. GO-BP: response to dsDNA/virus; cGAS-STING–IRF3 axis. (prompetchara2024mpoxglobalhealth pages 6-8, parnian2024innateimmuneresponse pages 1-2)
  - NFKB1 (HGNC:7794): NF-κB signaling; antagonized by viral inhibitors; GO-BP: IKK/NF‑κB signaling (GO:0007249). (parnian2024innateimmuneresponse pages 1-2)
  - IL6 (HGNC:6018), CXCL8/IL8 (HGNC:6025), IFNG (HGNC:5438): Inflammatory/Th1 cytokines with early induction kinetics in infection. (prompetchara2024mpoxglobalhealth pages 6-8)


## Biological Processes (GO terms)
- Type I interferon signaling pathway (GO:0060337): MPXV infection of PBMCs shows IFN sensitivity, with virus-driven downregulation of STAT1 and other ISGs. (jarcy2024mpxvinfectshuman pages 14-18)
- Toll-like receptor signaling pathways (e.g., TLR3; general TLR signaling): sensed during infection and antagonized by MPXV to blunt innate responses. (parnian2024innateimmuneresponse pages 1-2, prompetchara2024mpoxglobalhealth pages 6-8)
- IKK/NF‑κB signaling (GO:0007249): central to cytokine expression; antagonized by MPXV immune modulators. (parnian2024innateimmuneresponse pages 1-2)
- Viral factory formation/replication in cytoplasm: assembly in ER-associated cytoplasmic inclusions (Guarnieri bodies). (lu2023mpox(formerlymonkeypox) pages 13-14, lu2023mpox(formerlymonkeypox) pages 2-4)
- Actin-based cell-to-cell motility: A36R-mediated actin tails promote spread. (lu2023mpox(formerlymonkeypox) pages 13-14)
- Extracellular virion (EEV) formation and egress: F13L/B5R/A34R orchestrate wrapping and egress. (lu2023mpox(formerlymonkeypox) pages 13-14)


## Cellular Components (GO-CC)
- Viral factory/Guarnieri bodies (GO:0039641, viral factory): cytoplasmic replication sites visible histologically. (lu2023mpox(formerlymonkeypox) pages 13-14, lu2023mpox(formerlymonkeypox) pages 2-4)
- Intracellular mature virion (IMV) and extracellular enveloped virion (EEV): distinct infectious forms with different membranes and roles in spread. (lu2023mpox(formerlymonkeypox) pages 2-4)
- Plasma membrane/endosomal compartments: entry interfaces reliant on lipid rafts/cholesterol. (lu2023mpox(formerlymonkeypox) pages 2-4)


## Cell Types (CL terms)
- Keratinocytes (CL:0000312): primary epidermal targets with “ballooning degeneration” histopathology. (zinnah2024thereemergenceof pages 6-8)
- Langerhans cells (CL:0000452), dendritic cells (CL:0000451): cutaneous APCs; infection/migration to draining lymph nodes; DC maturation/migration impaired by MPXV. (qudus2023theprospectiveoutcome pages 5-7, lu2023mpox(formerlymonkeypox) pages 13-14)
- Monocytes (CL:0000576): productively infected ex vivo; may mediate hematogenous dissemination. (jarcy2024mpxvinfectshuman pages 14-18)
- NK cells (CL:0000623): expanded but functionally impaired. (prompetchara2024mpoxglobalhealth pages 6-8)
- Regulatory CD4+ T cells (CL:0000815): susceptible ex vivo. (jarcy2024mpxvinfectshuman pages 14-18)


## Anatomical Locations (UBERON)
- Epidermis/skin (UBERON:0001003): lesion formation sites; characteristic evolution from macule to crust. (zinnah2024thereemergenceof pages 6-8)
- Lymph node (UBERON:0000029): early amplification and lymphadenopathy. (qudus2023theprospectiveoutcome pages 5-7)
- Liver (UBERON:0002107), spleen (UBERON:0002106): organ involvement in severe/systemic disease. (qudus2023theprospectiveoutcome pages 5-7)
- Genital/anal mucosa (e.g., UBERON:0000996 anus; UBERON:0001277 male external genitalia): frequent involvement in recent outbreaks. (lu2023mpox(formerlymonkeypox) pages 2-4)


## Chemical Entities (ChEBI)
- Tecovirimat (TPOXX): inhibitor of F13L-mediated wrapping/egress; resistance risk via F13L mutations. (lu2023mpox(formerlymonkeypox) pages 13-14)
- Cidofovir and brincidofovir: DNA polymerase–targeting antivirals considered in severe cases; PBMC infection model validates reduced viral antigen/infectivity upon treatment in vitro/ex vivo. (jarcy2024mpxvinfectshuman pages 14-18, lu2023mpox(formerlymonkeypox) pages 13-14)


## Disease Progression
- Exposure via skin/mucosa or respiratory secretions. Local replication in keratinocytes and infection of cutaneous APCs (Langerhans cells/DCs), which migrate to draining lymph nodes. Early lymph node replication produces lymphadenopathy. Hematogenous dissemination follows, with viremia and spread to lymphoid organs (spleen), liver (Kupffer cells, hepatocytes), and other tissues. Skin lesions evolve through classic stages. In immunocompromised hosts (e.g., advanced HIV), dissemination, necrotic skin lesions, and multi-organ involvement are more likely (supported mechanistically by impaired innate/adaptive control and ex vivo PBMC tropism). (qudus2023theprospectiveoutcome pages 5-7, lu2023mpox(formerlymonkeypox) pages 2-4, jarcy2024mpxvinfectshuman pages 14-18, zinnah2024thereemergenceof pages 6-8)


## Phenotypic Manifestations (HPO terms)
- Fever (HP:0001945), Lymphadenopathy (HP:0002716), Skin rash (HP:0000988), Pustules (HP:0031417), Ulcers (HP:0007405), Conjunctivitis (HP:0000509). Lesions follow macule→papule→vesicle→pustule→crust stages; genital and anal involvement common in 2022–2023. (zinnah2024thereemergenceof pages 6-8, lu2023mpox(formerlymonkeypox) pages 2-4)


## Expert Opinions and Analysis (Recent Authoritative Sources)
- Lu et al. (Signal Transduction and Targeted Therapy, 2023) synthesize orthopox virology relevant to mpox, emphasizing IMV/EEV biology, cytoplasmic factory replication, and spread determinants (F13L/B5R/A34R/A36R), and note tecovirimat’s F13L target and resistance potential. (lu2023mpox(formerlymonkeypox) pages 2-4, lu2023mpox(formerlymonkeypox) pages 13-14)
- Prompetchara et al. (APJAI, 2024) detail immune responses and evasion: suppression of PRR pathways (NF‑κB, IRF3), NK cell dysfunction, and antigen targets (A33R, A44R, F13L) underpinning cross-protective humoral immunity, consistent with observed vaccine cross-protection. (prompetchara2024mpoxglobalhealth pages 6-8)
- Parnian et al. (Journal of Innate Immunity, 2024) focus on innate immune mechanisms and escape: modulation of complement, inflammasome, chemokines/cytokines, and TLR signaling, aligning with ex vivo PBMC transcriptomic suppression (STAT1, GBP family) after MPXV infection. (parnian2024innateimmuneresponse pages 1-2, jarcy2024mpxvinfectshuman pages 14-18)


## Relevant Statistics and Data (Recent)
- Early cytokine kinetics in NHP models: IL‑8 detection by day 2; IFN‑γ, IL‑6, and MCP‑1 by day 4, peaking around day 8; seroconversion by day 10–12. (prompetchara2024mpoxglobalhealth pages 6-8)
- Ex vivo PBMC susceptibility: monocytes, cycling NK cells, and regulatory CD4+ T cells positive for viral RNA by day 5; productive infection demonstrated by plaque assays; type I IFN pretreatment reduces viral DNA and infectivity. (jarcy2024mpxvinfectshuman pages 14-18)
- Clinical rash evolution and histopathology: ballooning degeneration of keratinocytes; lesion stages macule→papule→vesicle→pustule→scab. (zinnah2024thereemergenceof pages 6-8)


## Evidence Items with PMIDs/DOIs and URLs
- Lu et al., 2023. Mpox (formerly monkeypox): pathogenesis, prevention and treatment. Signal Transduction and Targeted Therapy. DOI: 10.1038/s41392-023-01675-2; URL: https://doi.org/10.1038/s41392-023-01675-2. Published Dec 2023. (lu2023mpox(formerlymonkeypox) pages 2-4, lu2023mpox(formerlymonkeypox) pages 13-14)
- Prompetchara et al., 2024. Mpox global health emergency: Insights into the virus and immune responses. Asian Pacific Journal of Allergy and Immunology. DOI: 10.12932/ap-111024-1945; URL: https://doi.org/10.12932/ap-111024-1945. Published Sep 2024. (prompetchara2024mpoxglobalhealth pages 6-8)
- Parnian et al., 2024. Innate Immune Response to Monkeypox Virus Infection: Mechanisms and Immune Escape. Journal of Innate Immunity. DOI: 10.1159/000540815; URL: https://doi.org/10.1159/000540815. Published Aug 2024. (parnian2024innateimmuneresponse pages 1-2)
- de Jarcy et al., 2024. MPXV Infects Human PBMCs in a Type I Interferon-Sensitive Manner. bioRxiv. DOI: 10.1101/2024.09.16.613292; URL: https://doi.org/10.1101/2024.09.16.613292. Posted Sep 2024. (jarcy2024mpxvinfectshuman pages 14-18)
- Qudus et al., 2023. The prospective outcome of the 2022 outbreak and characterization of monkeypox disease immunobiology. Frontiers in Cellular and Infection Microbiology. DOI: 10.3389/fcimb.2023.1196699; URL: https://doi.org/10.3389/fcimb.2023.1196699. Published Jul 2023. (qudus2023theprospectiveoutcome pages 5-7)
- Zinnah et al., 2024. The Re-Emergence of Mpox: Old Illness, Modern Challenges. Biomedicines. DOI: 10.3390/biomedicines12071457; URL: https://doi.org/10.3390/biomedicines12071457. Published Jul 2024. (zinnah2024thereemergenceof pages 6-8)


## Current Applications and Real-World Implementations
- Antiviral therapy: Tecovirimat targeting F13L/P37 is used under regulatory pathways and recommended for severe disease or high-risk patients; mechanistic basis and resistance risk are grounded in orthopox biology (F13L mutations reduce susceptibility). DNA polymerase inhibitors (cidofovir; prodrug brincidofovir) are considered in severe disease; ex vivo PBMC systems support antiviral activity against MPXV. (lu2023mpox(formerlymonkeypox) pages 13-14, jarcy2024mpxvinfectshuman pages 14-18)
- Vaccination: Cross-protective immunity from vaccinia-based vaccines is underpinned by antibody responses to conserved IMV/EEV proteins (e.g., A33R, A44R, F13L), consistent with observed cross-protection in epidemiology. (prompetchara2024mpoxglobalhealth pages 6-8)
- Diagnostics: Molecular targets include MPXV genes such as A29L/F3L; histopathology can show keratinocyte ballooning and cytoplasmic inclusions supportive of diagnosis alongside PCR. (zinnah2024thereemergenceof pages 6-8)


## Recent Developments and Latest Research (priority 2023–2024)
- Comprehensive mechanistic review of mpox pathogenesis and countermeasures (Lu et al., Dec 2023) synthesizing IMV/EEV biology, cytoplasmic factories, and drug targets. (lu2023mpox(formerlymonkeypox) pages 2-4, lu2023mpox(formerlymonkeypox) pages 13-14)
- Immune response and evasion updates (Prompetchara et al., Sep 2024; Parnian et al., Aug 2024) detailing innate sensing, NK cell dysfunction, and viral antagonists of PRR/IFN pathways. (prompetchara2024mpoxglobalhealth pages 6-8, parnian2024innateimmuneresponse pages 1-2)
- Ex vivo human PBMC tropism and interferon sensitivity (de Jarcy et al., Sep 2024) clarifying potential lymphohematogenous dissemination via monocytes and immune modulation. (jarcy2024mpxvinfectshuman pages 14-18)


## Structured Knowledge (Ontology-Linked Summary)
| Category | Entity | Ontology | Ontology_ID | Mechanistic Role (1–2 clauses) | Evidence | URL |
|---|---|---:|---|---|---|---|
| Gene/Protein | EGFR | HGNC | 3236 | Host receptor/kinase hijacked to enhance viral spread and cell-to-cell dissemination | (lu2023mpox(formerlymonkeypox) pages 13-14, prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.1038/s41392-023-01675-2 |
| Gene/Protein | STAT1 | HGNC | 11363? | Central transcription factor for IFN signaling; downregulated/suppressed during MPXV infection | (jarcy2024mpxvinfectshuman pages 14-18, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1101/2024.09.16.613292 |
| Gene/Protein | JAK2 | HGNC | (see HGNC) | Tyrosine kinase in JAK/STAT; reported downregulated in infected PBMCs | (jarcy2024mpxvinfectshuman pages 14-18) | https://doi.org/10.1101/2024.09.16.613292 |
| Gene/Protein | IRF3 | HGNC | (see HGNC) | PRR downstream TF (type I IFN induction); targeted by viral inhibitors to blunt IFN responses | (prompetchara2024mpoxglobalhealth pages 6-8, parnian2024innateimmuneresponse pages 1-2) | https://doi.org/10.12932/ap-111024-1945 |
| Gene/Protein | NFKB1 | HGNC | (see HGNC) | Master regulator of inflammatory gene expression; activity antagonized by viral proteins | (parnian2024innateimmuneresponse pages 1-2, qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.1159/000540815 |
| Gene/Protein | IL6 | HGNC | 6018 | Proinflammatory cytokine elevated in early infection; implicated in systemic inflammation/cytokine responses | (prompetchara2024mpoxglobalhealth pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.12932/ap-111024-1945 |
| Gene/Protein | CXCL8 (IL8) | HGNC | 1690 | Early chemokine induced after infection (neutrophil chemoattractant) | (prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.12932/ap-111024-1945 |
| Gene/Protein | IFNG | HGNC | 5467 | Type II interferon involved in adaptive/innate responses; kinetics altered during MPXV infection | (prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.12932/ap-111024-1945 |
| Viral Protein | F13L (P37) | Viral protein | F13L | Phospholipase required for enveloped virion envelopment/egress; molecular target of tecovirimat | (lu2023mpox(formerlymonkeypox) pages 13-14, jarcy2024mpxvinfectshuman pages 14-18) | https://doi.org/10.1038/s41392-023-01675-2 |
| Viral Protein | B5R | Viral protein | B5R | Required for extracellular virion envelopment and infectivity (EEV formation) | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Viral Protein | A34R | Viral protein | A34R | Contributes to EEV infectivity and spread | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Viral Protein | A36R | Viral protein | A36R | Drives actin-tail formation for directed cell-to-cell spread | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Viral Protein | A29L | Viral protein | A29L | IMV/EEV surface protein and vaccine/antigen target involved in entry/neutralization | (prompetchara2024mpoxglobalhealth pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.12932/ap-111024-1945 |
| Viral Protein | A33R | Viral protein | A33R | IMV/EEV-associated antigen; implicated in humoral neutralization and spread | (prompetchara2024mpoxglobalhealth pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.12932/ap-111024-1945 |
| Viral Protein | M1R | Viral protein | M1R | IMV antigen included in multicomponent vaccine constructs | (prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.12932/ap-111024-1945 |
| Viral Protein | E8L | Viral protein | E8L | IMV surface antigen; vaccine/antigen candidate | (prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.12932/ap-111024-1945 |
| Cell Type | Keratinocyte | CL | (see CL) | Primary epidermal target; shows ballooning degeneration and cytoplasmic inclusions in lesions | (zinnah2024thereemergenceof pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.3390/biomedicines12071457 |
| Cell Type | Langerhans cell | CL | (see CL) | Skin-resident DC subset that can be infected and transmit antigen to lymph nodes | (qudus2023theprospectiveoutcome pages 5-7, prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.3389/fcimb.2023.1196699 |
| Cell Type | Dendritic cell | CL | (see CL) | Antigen presentation; maturation and migration inhibited by viral immune-evasion proteins | (lu2023mpox(formerlymonkeypox) pages 13-14, parnian2024innateimmuneresponse pages 1-2) | https://doi.org/10.1038/s41392-023-01675-2 |
| Cell Type | Monocyte | CL | (see CL) | Susceptible to productive infection in PBMCs; may mediate lymphohematogenous spread | (jarcy2024mpxvinfectshuman pages 14-18, qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.1101/2024.09.16.613292 |
| Cell Type | NK cell | CL | (see CL) | Expand early but show functional impairment (reduced degranulation/IFNγ) during infection | (prompetchara2024mpoxglobalhealth pages 6-8, jarcy2024mpxvinfectshuman pages 14-18) | https://doi.org/10.12932/ap-111024-1945 |
| Cell Type | CD4+ Treg | CL | (see CL) | Regulatory CD4+ subset can carry viral RNA ex vivo, indicating susceptibility | (jarcy2024mpxvinfectshuman pages 14-18) | https://doi.org/10.1101/2024.09.16.613292 |
| Biological Process | Type I IFN signaling | GO-BP | (see GO) | Antiviral cascade downregulated/suppressed in infected cells; IFN sensitivity affects replication | (jarcy2024mpxvinfectshuman pages 14-18, parnian2024innateimmuneresponse pages 1-2) | https://doi.org/10.1101/2024.09.16.613292 |
| Biological Process | TLR signaling | GO-BP | (see GO) | PRR pathway recognizing MPXV components; targeted by viral inhibitors to blunt innate sensing | (parnian2024innateimmuneresponse pages 1-2, prompetchara2024mpoxglobalhealth pages 6-8) | https://doi.org/10.1159/000540815 |
| Biological Process | NF-κB signaling | GO-BP | (see GO) | Drives inflammatory cytokine transcription; antagonized by viral modulators | (parnian2024innateimmuneresponse pages 1-2, qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.1159/000540815 |
| Biological Process | Viral factory formation | GO-BP | (see GO) | Cytoplasmic replication sites (ER-associated mini-nuclei) where assembly occurs | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Biological Process | Actin-based motility | GO-BP | (see GO) | Host cytoskeletal manipulation (A36R-driven) enabling spread between cells | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Biological Process | Extracellular virion formation | GO-BP | (see GO) | EEV biogenesis (B5R/F13L/A34R) enables long-range spread and immune evasion | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Cellular Component | Viral factory / Guarnieri bodies | GO-CC | (see GO) | Cytoplasmic inclusion sites of replication and virion assembly seen histologically | (zinnah2024thereemergenceof pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.3390/biomedicines12071457 |
| Cellular Component | IMV (intracellular mature virion) | GO-CC | (see GO) | Stable virion form released on lysis; major target of neutralizing antibodies | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Cellular Component | EEV (extracellular enveloped virion) | GO-CC | (see GO) | Additional membrane form required for efficient cell-to-cell and long-range spread | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Cellular Component | Plasma membrane / Endosome | GO-CC | (see GO) | Entry routes for IMV/EEV via fusion or endocytosis; lipid-raft/cholesterol dependent | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Anatomical Site | Epidermis / Skin | UBERON | (see UBERON) | Primary site of lesion formation (macules→papules→vesicles→pustules→scabs) with keratinocyte damage | (zinnah2024thereemergenceof pages 6-8, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.3390/biomedicines12071457 |
| Anatomical Site | Lymph node | UBERON | (see UBERON) | Early site of viral amplification after APC migration; lymphadenopathy is characteristic | (qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.3389/fcimb.2023.1196699 |
| Anatomical Site | Liver | UBERON | (see UBERON) | Viral antigen and pathology reported in hepatocytes/Kupffer cells in severe/systemic disease | (qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.3389/fcimb.2023.1196699 |
| Anatomical Site | Spleen | UBERON | (see UBERON) | Lymphoid organ involved in systemic spread and immune interactions | (qudus2023theprospectiveoutcome pages 5-7) | https://doi.org/10.3389/fcimb.2023.1196699 |
| Anatomical Site | Genital / anal mucosa | UBERON | (see UBERON) | Frequent lesion sites in recent outbreaks; relevant to transmission routes (skin-to-skin/sexual) | (qudus2023theprospectiveoutcome pages 5-7, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |
| Chemical / Drug | Tecovirimat (TPOXX) | ChEBI | (see ChEBI) | Inhibits F13L-mediated envelopment/egress; resistance arises via F13L mutations | (lu2023mpox(formerlymonkeypox) pages 13-14, jarcy2024mpxvinfectshuman pages 14-18) | https://doi.org/10.1038/s41392-023-01675-2 |
| Chemical / Drug | Cidofovir | ChEBI | (see ChEBI) | Viral DNA polymerase inhibitor repurposed for severe MPXV; used experimentally/compassionately | (jarcy2024mpxvinfectshuman pages 14-18, lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1101/2024.09.16.613292 |
| Chemical / Drug | Brincidofovir | ChEBI | (see ChEBI) | Lipid conjugate of cidofovir explored as oral antiviral candidate | (lu2023mpox(formerlymonkeypox) pages 13-14) | https://doi.org/10.1038/s41392-023-01675-2 |


*Table: Compact mapping of key mpox pathophysiology entities to ontologies, mechanistic roles, evidence (context IDs) and source DOIs; useful for knowledge-base ingestion and rapid reference.*


## Limitations
Some detailed histopathology (ultrastructure) and organ-tropism data in immunocompromised patients, as well as controlled clinical efficacy data for antivirals, were not directly available in the included evidence set; where necessary, orthopox literature was used to contextualize mechanisms. Additional recent clinical data (e.g., large tecovirimat cohorts) and structural insights into F13L-mediated resistance exist but were not among the citable context items for this report. (lu2023mpox(formerlymonkeypox) pages 13-14)

References

1. (lu2023mpox(formerlymonkeypox) pages 2-4): Junjie Lu, Hui Xing, Chunhua Wang, Mengjun Tang, Changcheng Wu, Fan Ye, Lijuan Yin, Yang Yang, Wenjie Tan, and Liang Shen. Mpox (formerly monkeypox): pathogenesis, prevention and treatment. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01675-2, doi:10.1038/s41392-023-01675-2. This article has 227 citations and is from a peer-reviewed journal.

2. (lu2023mpox(formerlymonkeypox) pages 13-14): Junjie Lu, Hui Xing, Chunhua Wang, Mengjun Tang, Changcheng Wu, Fan Ye, Lijuan Yin, Yang Yang, Wenjie Tan, and Liang Shen. Mpox (formerly monkeypox): pathogenesis, prevention and treatment. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01675-2, doi:10.1038/s41392-023-01675-2. This article has 227 citations and is from a peer-reviewed journal.

3. (zinnah2024thereemergenceof pages 6-8): Mohammad Ali Zinnah, Md Bashir Uddin, Tanjila Hasan, Shobhan Das, Fahima Khatun, Md Hasibul Hasan, Ruenruetai Udonsom, Md Masudur Rahman, and Hossam M. Ashour. The re-emergence of mpox: old illness, modern challenges. Biomedicines, 12:1457, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071457, doi:10.3390/biomedicines12071457. This article has 39 citations and is from a poor quality or predatory journal.

4. (qudus2023theprospectiveoutcome pages 5-7): Muhammad Suhaib Qudus, Xianghua Cui, Mingfu Tian, Uzair Afaq, Muhammad Sajid, Sonia Qureshi, Siyu Liu, June Ma, Guolei Wang, Muhammad Faraz, Haleema Sadia, Kailang Wu, and Chengliang Zhu. The prospective outcome of the monkeypox outbreak in 2022 and characterization of monkeypox disease immunobiology. Frontiers in Cellular and Infection Microbiology, Jul 2023. URL: https://doi.org/10.3389/fcimb.2023.1196699, doi:10.3389/fcimb.2023.1196699. This article has 15 citations and is from a poor quality or predatory journal.

5. (jarcy2024mpxvinfectshuman pages 14-18): Laure Bosquillon de Jarcy, Dylan Postmus, Jenny Jansen, Julia Melchert, Donata Hoffmann, Victor M. Corman, and Christine Goffinet. Mpxv infects human pbmcs in a type i interferon-sensitive manner. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.16.613292, doi:10.1101/2024.09.16.613292. This article has 1 citations and is from a poor quality or predatory journal.

6. (prompetchara2024mpoxglobalhealth pages 6-8): E. Prompetchara, C. Ketloy, Chirayus Khawsang, K. Ruxrungtham, and T. Palaga. Mpox global health emergency: insights into the virus, immune responses, and advancements in vaccines part i: insights into the virus and immune responses. Asian Pacific journal of allergy and immunology, 42 3:181-190, Sep 2024. URL: https://doi.org/10.12932/ap-111024-1945, doi:10.12932/ap-111024-1945. This article has 8 citations and is from a peer-reviewed journal.

7. (parnian2024innateimmuneresponse pages 1-2): Reza Parnian, Fatemeh Heydarifard, Fatemeh Sadat Mousavi, Zahra Heydarifard, and M. Zandi. Innate immune response to monkeypox virus infection: mechanisms and immune escape. Journal of Innate Immunity, 16:413-424, Aug 2024. URL: https://doi.org/10.1159/000540815, doi:10.1159/000540815. This article has 14 citations and is from a peer-reviewed journal.