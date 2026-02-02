---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T17:08:46.917809'
end_time: '2026-01-31T17:15:34.688558'
duration_seconds: 407.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemophilia B
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hemophilia B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hemophilia B**.
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
- **Disease Name:** Hemophilia B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hemophilia B**.
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


Disease Pathophysiology Research Report: Hemophilia B (Factor IX Deficiency)

Target Disease
- Disease Name: Hemophilia B (Christmas disease)
- MONDO ID: —
- Category: Genetic (X-linked recessive)

Pathophysiology description
Hemophilia B (HB) is an X‑linked recessive bleeding disorder caused by pathogenic variants in the F9 gene leading to reduced or absent factor IX (FIX) activity, impairing intrinsic tenase formation (FVIIIa–FIXa complex) and downstream thrombin generation. Disease severity correlates with residual FIX activity: severe <1%, moderate 1–5%, mild 5–40% of normal; prevalence is approximately 1 in 30,000 males worldwide (clinical phenotype typically includes mucocutaneous bleeding, post‑procedural hemorrhage, hemarthroses) (baniamer2024understandinginheritedbleeding pages 2-4). FVIII/FIX function can be conceptualized through tenase biology; notably, the approved bispecific antibody emicizumab “mimic[s] the function of FVIII by bringing together Factor IXa and Factor X,” illustrating the centrality of FIXa–FX complex assembly for effective intrinsic tenase activity (quote from review summarizing non‑factor approaches) (linari2025hemophiliachangesand pages 4-5), and perioperative guidance reiterates emicizumab “bridging activated factor IX and factor X” (quote) (lowell2024perioperativemanagementof pages 4-5). Large F9 deletions are associated with high inhibitor risk and allergic reactions in HB; these risks are highlighted clinically in infants presenting with severe bleeding such as intracranial hemorrhage (ICH) (lassandro2024intracranialhemorrhagein pages 1-2, wroblewska2025genetherapyas pages 1-2).

Key concepts and definitions (current understanding)
- Etiology: Pathogenic F9 variants (missense, nonsense, splice, indels, large deletions/duplications) reduce FIX antigen/activity; X‑linked inheritance (wroblewska2025genetherapyas pages 1-2, baniamer2024understandinginheritedbleeding pages 2-4).
- Severity thresholds: Severe <1% FIX activity; moderate 1–5%; mild 5–40% (baniamer2024understandinginheritedbleeding pages 2-4, wroblewska2025genetherapyas pages 1-2).
- Core mechanism: Impaired intrinsic tenase (FVIIIa–FIXa) assembly/activity results in deficient propagation of thrombin generation and unstable fibrin formation (supported by emicizumab mechanism mimicking FVIII cofactor to bring FIXa and FX together) (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Clinical manifestations: Spontaneous/joint bleeds in severe disease; post‑trauma/procedural bleeding in mild/moderate; ICH can be an initial presentation in infancy (baniamer2024understandinginheritedbleeding pages 2-4, lassandro2024intracranialhemorrhagein pages 1-2).

Recent developments and latest research (priority 2023–2024)
AAV gene therapy (adult severe–moderately severe HB)
- Fidanacogene elaparvovec (AAV) Phase 3 (BENEGENE‑2; NEJM 2024): annualized bleeding rate (ABR) decreased by 71% (from 4.42 to 1.28) 12–15 months post‑infusion vs prophylaxis lead‑in; mean FIX activity 26.9% at 15 months (median 22.9%; one‑stage SynthASil); 62% received glucocorticoids for transaminitis or decreased FIX; no thrombotic events or inhibitors (data‑cutoff Aug 30, 2023) (URL: https://doi.org/10.1056/NEJMoa2302982; published Sep 2024) (cuker2024genetherapywith pages 11-11).
- Cross‑program summaries (2023–2024) report sustained FIX expression with mean values in the mid‑20s to mid‑30s percent and large reductions in bleeding and factor use (e.g., median ABR 12→0; FIX infusions 53.5→0), alongside frequent but manageable ALT elevations and steroid use; anti‑AAV neutralizing antibodies exclude many candidates (chernyi2024recentadvancesin pages 17-18).
- Lancet 2025 review emphasizes real‑world considerations: pre‑existing AAV antibodies in ~25–40%, immune transaminase elevations requiring corticosteroids (weeks to months), variable durability, exclusion of children/inhibitor patients, and long‑term integration risk monitoring, while confirming multi‑year expression and cessation of prophylaxis for most recipients (URL: https://doi.org/10.1016/S0140-6736(24)02139-1; Mar 2025) (chowdary2025haemophilia pages 10-11).

Rebalancing (non‑factor) therapies (2023–2024 evidence base)
- Anti‑TFPI monoclonal antibodies (concizumab, marstacimab): Mechanism restores initiation pathway by relieving TFPI inhibition to enhance FXa/thrombin generation. Phase 3 programs progressed; concizumab experienced thrombotic events (associated with concomitant hemostatic therapies) prompting protocol adjustments; marstacimab showed efficacy with superiority signals vs prior factor prophylaxis in patients without inhibitors (Lancet 2025 review) (chowdary2025haemophilia pages 9-10). A 2024 Cochrane review confirms the development status and comparative intent versus standard care (search last updated Aug 16, 2023) ().
- Antithrombin siRNA (fitusiran): Monthly subcutaneous dosing lowers hepatic antithrombin mRNA to rebalance thrombin generation. Phase 3 data show significant ABR reductions but safety signals (thrombosis when antithrombin levels too low and when high‑dose concomitant hemostatics used; some hepatobiliary AEs). Risk‑mitigation includes antithrombin targets of ~15–35% and careful management of on‑demand agents (chowdary2025haemophilia pages 9-10). Perioperative guidance highlights a prior program hold after a fatal sinus thrombosis with concurrent high‑dose FVIII and notes reversibility with antithrombin supplementation (lowell2024perioperativemanagementof pages 4-5).

Extended half‑life (EHL) FIX products and inhibitor risk
- EHL rFIXFc and rIX‑FP reduce infusion frequency and improve adherence; in pediatrics, weekly rFIXFc prophylaxis is feasible. Inhibitor formation and allergic reactions can occur, with large F9 deletions conferring elevated risk and potential nephrotic syndrome; a 2024 case demonstrates continued rFIXFc prophylaxis with pre‑medication after low‑titer inhibitor emergence, avoiding nephrotic progression (URL: https://doi.org/10.1186/s13052-024-01819-2; Nov 2024) (lassandro2024intracranialhemorrhagein pages 1-2). Reviews also reinforce that immune tolerance induction is less effective in HB inhibitor patients and that anaphylaxis/nephrotic syndrome risks are higher than in HA (wroblewska2025genetherapyas pages 1-2).

Current applications and real‑world implementations
- Standard prophylaxis: Regular FIX replacement per severity is the global standard; even modest increases in factor activity can improve phenotype and reduce bleeds; humanitarian programs expand access (baniamer2024understandinginheritedbleeding pages 2-4).
- Gene therapy: One‑time IV AAV delivery enabling cessation of routine prophylaxis in many adults; real‑world implementation requires screening for AAV antibodies, liver monitoring, steroid management, and long‑term follow‑up (cuker2024genetherapywith pages 11-11, chowdary2025haemophilia pages 10-11).
- Non‑factor therapies: Emicizumab widely adopted for HA; in HB, rebalancing approaches (concizumab, marstacimab, fitusiran) are in late development or approved in some regions, with careful risk mitigation and guidance evolving (chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5, linari2025hemophiliachangesand pages 4-5).
- Perioperative management: Emicizumab interferes with aPTT‑based assays; use appropriate chromogenic or viscoelastic assays; avoid or limit aPCC due to thrombotic/TMA risks; rFVIIa preferred if needed (lowell2024perioperativemanagementof pages 4-5).

Expert opinions and authoritative analyses
- Lancet 2025 review (international experts) synthesizes gene therapy implementation challenges (antibody exclusion, transaminitis, durability), and non‑factor therapy risk–benefit considerations; underscores individualized selection and registry data needs (chowdary2025haemophilia pages 10-11).
- Perioperative experts highlight assay interference and thrombosis risk management with non‑factor agents, recommending tailored perioperative plans and judicious use of bypassing agents (lowell2024perioperativemanagementof pages 4-5).
- Cochrane 2024 review catalogs the evidence base and uncertainties around non‑factor prophylaxis in congenital hemophilia ().

Relevant statistics and data from recent studies
- Prevalence: ~1 in 30,000 males; severity thresholds severe <1%, moderate 1–5%, mild 5–40% FIX (baniamer2024understandinginheritedbleeding pages 2-4).
- AAV gene therapy (fidanacogene elaparvovec, NEJM 2024): ABR −71% vs lead‑in; mean FIX 26.9% at 15 months; 62% on steroids for transaminase/FIX declines; 0 inhibitors/thromboses in the report (cuker2024genetherapywith pages 11-11).
- AAV programs meta‑summary (2023–2024): FIX levels often mid‑20s to mid‑30s percent; high proportions without bleeding and cessation of factor use; ALT elevations common; anti‑AAV antibodies exclude many candidates (chernyi2024recentadvancesin pages 17-18).
- Pediatric severe HB ICH case (2024): severe FIX deficiency (<1%) due to large F9 deletions; low‑titer inhibitor (0.6–1.0 BU) after EHL rFIXFc; premedication immunotolerance allowed continued weekly prophylaxis without nephrotic syndrome (lassandro2024intracranialhemorrhagein pages 1-2).

Molecular and cellular mechanisms
- Molecular pathways dysregulated: intrinsic pathway propagation (defective FVIIIa–FIXa tenase assembly and function) leading to insufficient thrombin burst; rebalancing strategies target endogenous anticoagulants (TFPI, antithrombin) to restore thrombin generation (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5, chowdary2025haemophilia pages 9-10).
- Cellular processes affected: Hepatocyte synthesis of FIX (secreted plasma zymogen); platelet‑surface and activated endothelium‑supported assembly of intrinsic tenase; impaired clot stability manifesting as clinical bleeding. Mechanistic surrogates from emicizumab’s action reinforce the requirement for colocalizing FIXa and FX (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Tissues/organs: Liver (FIX synthesis), synovial joints and muscles (target bleeding sites), CNS (ICH risk in infants) (lassandro2024intracranialhemorrhagein pages 1-2, baniamer2024understandinginheritedbleeding pages 2-4).

Key molecular players
- Genes/Proteins: F9 (HGNC:3551) encoding factor IX; interacting factors: FVIII (cofactor), FX, thrombin; endogenous anticoagulants targeted by non‑factor therapies: TFPI (anti‑TFPI mAbs), antithrombin (siRNA) (linari2025hemophiliachangesand pages 4-5, chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5).
- Chemical entities (CHEBI):
  - Anti‑TFPI monoclonal antibodies: concizumab, marstacimab (therapeutic biologics) (chowdary2025haemophilia pages 9-10).
  - siRNA: fitusiran (subcutaneous RNAi drug) (chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5).
  - AAV gene therapy products: fidanacogene elaparvovec (AAV vector delivering FIX‑Padua) (cuker2024genetherapywith pages 11-11).
- Cell types (CL): Hepatocytes (CL:0000182) – FIX production; platelets (CL:0000233) – tenase surface; endothelial cells (CL:0000115) – hemostatic interface. (Mechanistic context supported by emicizumab’s effect on bringing FIXa and FX together) (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Anatomical locations (UBERON): Liver (UBERON:0002107); synovial joint (UBERON:0000982); brain/CNS (UBERON:0000955) (lassandro2024intracranialhemorrhagein pages 1-2, baniamer2024understandinginheritedbleeding pages 2-4).

Biological processes (GO) disrupted
- Blood coagulation (GO:0007596) and intrinsic pathway of blood coagulation (GO:0007597): impaired FIX activation/function within intrinsic tenase (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Regulation of thrombin generation (part of coagulation cascade): diminished in HB; therapeutically enhanced by anti‑TFPI and antithrombin‑lowering strategies (chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5).
- Response to wounding/hemostasis (GO:0009611/GO:0007599): abnormal bleeding phenotype (baniamer2024understandinginheritedbleeding pages 2-4).

Cellular components (GO)
- Extracellular region/plasma (GO:0005576): circulating FIX zymogen.
- Plasma membrane surfaces (platelets/endothelium) for intrinsic tenase assembly (protein complex at membrane) inferred from emicizumab’s bridging of FIXa and FX (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).

Disease progression (sequence of events)
1) F9 pathogenic variant → reduced/absent functional FIX antigen/activity (wroblewska2025genetherapyas pages 1-2, baniamer2024understandinginheritedbleeding pages 2-4).
2) Impaired intrinsic tenase assembly/activity (FVIIIa–FIXa–phospholipid–Ca2+) → reduced FX activation and thrombin burst (supported by emicizumab mechanism that rescues tenase-like function by colocalizing FIXa and FX) (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
3) Inadequate fibrin generation/stability → bleeding after minimal trauma; in severe disease, spontaneous hemarthroses/muscle bleeds; infants can present with ICH (baniamer2024understandinginheritedbleeding pages 2-4, lassandro2024intracranialhemorrhagein pages 1-2).
4) Treatment modifies trajectory: EHL FIX increases trough levels; gene therapy can restore FIX into mild range; rebalancing therapies elevate thrombin potential but require thrombosis risk management (cuker2024genetherapywith pages 11-11, chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5).

Phenotypic manifestations with mechanistic links (HP terms)
- Recurrent hemarthrosis (HP:0003257) and chronic arthropathy (HP:0001362): due to inadequate tenase‑mediated thrombin generation during joint microtrauma (baniamer2024understandinginheritedbleeding pages 2-4).
- Easy bruising (HP:0000978), epistaxis (HP:0000421), post‑procedural hemorrhage (HP:0001892) (baniamer2024understandinginheritedbleeding pages 2-4).
- Intracranial hemorrhage (HP:0002170) in infancy/severe deficiency (lassandro2024intracranialhemorrhagein pages 1-2).
- Inhibitor formation (alloantibodies) with allergic reactions/nephrotic syndrome risk in HB, especially with large F9 deletions (HP:0025354; mechanistic: anti‑FIX neutralization; immune complex complications) (lassandro2024intracranialhemorrhagein pages 1-2, wroblewska2025genetherapyas pages 1-2).

Evidence items (PMIDs/DOIs, URLs, dates)
- NEJM 2024 (BENEGENE‑2; fidanacogene elaparvovec): ABR −71%; FIX ~27% at 15 months; steroid use 62%; no inhibitors/thromboses. DOI: 10.1056/NEJMoa2302982. URL: https://doi.org/10.1056/NEJMoa2302982. Published Sep 2024 (cuker2024genetherapywith pages 11-11).
- Biomolecules 2024 review: summarizes AAV HB programs (AMT‑061/etranacogene dezaparvovec and others) with sustained FIX levels (mid‑20s to mid‑30s %) and substantial ABR/infusion reductions; notes ALT elevations and AAV antibody exclusions. DOI: 10.3390/biom14070854. URL: https://doi.org/10.3390/biom14070854. Published Jul 2024 (chernyi2024recentadvancesin pages 17-18).
- Lancet 2025 review: gene therapy implementation (eligibility, immune toxicity, durability) and non‑factor therapies (anti‑TFPI, fitusiran) with risk–benefit framing. DOI: 10.1016/S0140-6736(24)02139-1. URL: https://doi.org/10.1016/S0140-6736(24)02139-1. Published Mar 2025 (chowdary2025haemophilia pages 10-11).
- Italian J Pediatr 2024 case: infant ICH; rFIXFc prophylaxis, low‑titer inhibitor, immunotolerance premedication avoided nephrotic syndrome. DOI: 10.1186/s13052-024-01819-2. URL: https://doi.org/10.1186/s13052-024-01819-2. Published Nov 2024 (lassandro2024intracranialhemorrhagein pages 1-2).
- Journal of Applied Genetics 2025 review: HB genetics (F9, Xq27.1), severity thresholds, EHL FIX, gene therapy approval context, inhibitor risks. DOI: 10.1007/s13353-025-00952-w. URL: https://doi.org/10.1007/s13353-025-00952-w. Published Apr 2025 (wroblewska2025genetherapyas pages 1-2).
- Journal of Hematology & Oncology Research 2024 review: prevalence (~1/30,000 males), severity thresholds, standard prophylaxis rationale. DOI: 10.14302/issn.2372-6601.jhor-24-5108. URL: https://doi.org/10.14302/issn.2372-6601.jhor-24-5108. Published Aug 2024 (baniamer2024understandinginheritedbleeding pages 2-4).
- Current Anesthesiology Reports 2024: perioperative management, emicizumab assay interference, aPCC thrombosis/TMA risks, rFVIIa preference; fitusiran program hold after fatal sinus thrombosis with high‑dose FVIII, reversibility with AT. DOI: 10.1007/s40140-024-00635-y. URL: https://doi.org/10.1007/s40140-024-00635-y. Published Jun 2024 (lowell2024perioperativemanagementof pages 4-5).
- Cochrane Database of Systematic Reviews 2024: non‑factor therapies for congenital hemophilia A/B (concizumab, marstacimab, fitusiran) (search through Aug 16, 2023). DOI: 10.1002/14651858.CD014544.pub2. URL: https://doi.org/10.1002/14651858.CD014544.pub2. Published Feb 2024 ().
- Frontiers in Medicine 2025 narrative review: HB mutation spectrum; intrinsic pathway pathophysiology; EHL, gene therapy, non‑factor strategies; global access issues. DOI: 10.3389/fmed.2025.1618464. URL: https://doi.org/10.3389/fmed.2025.1618464. Published Sep 2025 (dushimova2025therapeuticadvancesin pages 2-3).

Ontology‑style annotations
- Gene/protein (HGNC): F9 (HGNC:3551) → Factor IX (serine protease zymogen) (wroblewska2025genetherapyas pages 1-2).
- GO Biological Processes: blood coagulation (GO:0007596); intrinsic pathway of blood coagulation (GO:0007597); regulation of thrombin generation (supported by non‑factor strategies) (linari2025hemophiliachangesand pages 4-5, chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5).
- GO Cellular Components: extracellular region (GO:0005576); membrane‑bound tenase at activated platelet/endothelial surfaces (supported mechanistically by emicizumab bridging FIXa and FX) (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Phenotype (HP): hemarthrosis (HP:0003257), arthropathy (HP:0001362), epistaxis (HP:0000421), easy bruising (HP:0000978), post‑procedural bleeding (HP:0001892), intracranial hemorrhage (HP:0002170), inhibitor formation (HP:0025354) (baniamer2024understandinginheritedbleeding pages 2-4, lassandro2024intracranialhemorrhagein pages 1-2, wroblewska2025genetherapyas pages 1-2).
- Cell types (CL): hepatocytes (CL:0000182), platelets (CL:0000233), endothelial cells (CL:0000115) (mechanistic support via tenase/emicizumab bridging) (linari2025hemophiliachangesand pages 4-5, lowell2024perioperativemanagementof pages 4-5).
- Anatomical locations (UBERON): liver (UBERON:0002107), synovial joint (UBERON:0000982), brain/CNS (UBERON:0000955) (lassandro2024intracranialhemorrhagein pages 1-2, baniamer2024understandinginheritedbleeding pages 2-4).

Direct quotes (selected)
- “mimic the function of FVIII by bringing together Factor IXa and Factor X” (emicizumab mechanism) (linari2025hemophiliachangesand pages 4-5).
- Emicizumab acts by “bridging activated factor IX and factor X,” with perioperative cautions on assay interference and thrombotic risk management (lowell2024perioperativemanagementof pages 4-5).

Plan status update
- Core mechanisms, recent developments (2023–2024), applications, expert analyses, and statistics compiled from recent high‑quality sources (NEJM 2024; Cochrane 2024; perioperative review 2024; Lancet 2025 synthesis) and clinically relevant case evidence (ICH in infant) (cuker2024genetherapywith pages 11-11, lowell2024perioperativemanagementof pages 4-5, chowdary2025haemophilia pages 10-11, lassandro2024intracranialhemorrhagein pages 1-2).

Citations: (baniamer2024understandinginheritedbleeding pages 2-4, cuker2024genetherapywith pages 11-11, lassandro2024intracranialhemorrhagein pages 1-2, chernyi2024recentadvancesin pages 17-18, chowdary2025haemophilia pages 10-11, wroblewska2025genetherapyas pages 1-2, dushimova2025therapeuticadvancesin pages 2-3, chowdary2025haemophilia pages 9-10, lowell2024perioperativemanagementof pages 4-5, linari2025hemophiliachangesand pages 4-5)

References

1. (baniamer2024understandinginheritedbleeding pages 2-4): Ansam Zakaria Baniamer, Aya Mohannad Hamdan, Mohammad Raed AlGhzawi, Mohammad Tareq Alfaqeh, Sadeen Yaser Yaseen, Shama Mohammad Alshtawi, Hala Yasin Alomush, and Rand Mahdi Olimat. Understanding inherited bleeding disorders: genetic mutations in blood coagulation factors and regulatory proteins. Journal of Hematology and Oncology Research, 4:1-23, Aug 2024. URL: https://doi.org/10.14302/issn.2372-6601.jhor-24-5108, doi:10.14302/issn.2372-6601.jhor-24-5108. This article has 2 citations.

2. (linari2025hemophiliachangesand pages 4-5): Silvia Linari and Giancarlo Castaman. Hemophilia: changes and new achievements in management and care. International Journal of Bone Fragility, 5:66-71, Oct 2025. URL: https://doi.org/10.57582/ijbf.250502.066, doi:10.57582/ijbf.250502.066. This article has 0 citations.

3. (lowell2024perioperativemanagementof pages 4-5): Aliena E. Lowell, Michael P. Calgi, Joseph J. Caruso, Louise M. Man, and John S. McNeil. Perioperative management of hemophilia patients. Current Anesthesiology Reports, 14:354-365, Jun 2024. URL: https://doi.org/10.1007/s40140-024-00635-y, doi:10.1007/s40140-024-00635-y. This article has 7 citations and is from a peer-reviewed journal.

4. (lassandro2024intracranialhemorrhagein pages 1-2): Giuseppe Lassandro, Valentina Palladino, and Paola Giordano. Intracranial hemorrhage in an infant leads to the diagnosis and treatment of severe hemophilia b: a case report. Italian Journal of Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s13052-024-01819-2, doi:10.1186/s13052-024-01819-2. This article has 0 citations and is from a peer-reviewed journal.

5. (wroblewska2025genetherapyas pages 1-2): Kinga Wróblewska, Dominika Bieszczad, Magdalena Popławska, Karolina Joanna Ziętara, Monika Zajączkowska, and Agata Filip. Gene therapy as an innovative approach to the treatment of hemophilia b-a review. Journal of applied genetics, Apr 2025. URL: https://doi.org/10.1007/s13353-025-00952-w, doi:10.1007/s13353-025-00952-w. This article has 0 citations and is from a peer-reviewed journal.

6. (cuker2024genetherapywith pages 11-11): Adam Cuker, Kaan Kavakli, Laurent Frenzel, Jiaan-Der Wang, Jan Astermark, Monica H. Cerqueira, Alfonso Iorio, Olga Katsarou-Fasouli, Robert Klamroth, Amy D. Shapiro, Cédric Hermans, Akira Ishiguro, Andrew D. Leavitt, Johannes B. Oldenburg, Margareth C. Ozelo, Jerome Teitel, Francesca Biondo, Annie Fang, Joanne Fuiman, John McKay, Pengling Sun, John E.J. Rasko, and Jeremy Rupon. Gene therapy with fidanacogene elaparvovec in adults with hemophilia b. The New England journal of medicine, 391 12:1108-1118, Sep 2024. URL: https://doi.org/10.1056/nejmoa2302982, doi:10.1056/nejmoa2302982. This article has 74 citations and is from a highest quality peer-reviewed journal.

7. (chernyi2024recentadvancesin pages 17-18): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Biomolecules, 14:854, Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 33 citations and is from a poor quality or predatory journal.

8. (chowdary2025haemophilia pages 10-11): Pratima Chowdary, Manuel Carcao, Gili Kenet, and Steven W Pipe. Haemophilia. The Lancet, 405:736-750, Mar 2025. URL: https://doi.org/10.1016/s0140-6736(24)02139-1, doi:10.1016/s0140-6736(24)02139-1. This article has 33 citations and is from a highest quality peer-reviewed journal.

9. (chowdary2025haemophilia pages 9-10): Pratima Chowdary, Manuel Carcao, Gili Kenet, and Steven W Pipe. Haemophilia. The Lancet, 405:736-750, Mar 2025. URL: https://doi.org/10.1016/s0140-6736(24)02139-1, doi:10.1016/s0140-6736(24)02139-1. This article has 33 citations and is from a highest quality peer-reviewed journal.

10. (dushimova2025therapeuticadvancesin pages 2-3): Zaure Dushimova, Marat Pashimov, Jamilya Kaibullayeva, Laura Danyarova, Elmira Kultanova, Gulnara Abdilova, and Nagima Mustapayeva. Therapeutic advances in hemophilia: from molecular innovation to patient-centered global care. Frontiers in Medicine, Sep 2025. URL: https://doi.org/10.3389/fmed.2025.1618464, doi:10.3389/fmed.2025.1618464. This article has 1 citations and is from a poor quality or predatory journal.