---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-02-01T09:19:51.997859'
end_time: '2026-02-01T09:21:37.455716'
duration_seconds: 105.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Transverse Myelitis
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 40
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Transverse Myelitis
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Transverse Myelitis**.
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

# Comprehensive Pathophysiology of Transverse Myelitis: Molecular and Cellular Mechanisms of Spinal Cord Inflammation and Demyelination

Transverse myelitis (TM) represents a focal inflammatory disorder of the spinal cord characterized by immune-mediated demyelination and axonal injury that results in acute neurological dysfunction affecting sensorimotor and autonomic systems[1][33][37]. The condition demonstrates significant pathobiological heterogeneity, with multiple etiological pathways converging on a final common pathway of spinal cord inflammation, myelin destruction, and neuronal injury. This report synthesizes current understanding of the molecular and cellular mechanisms underlying TM pathophysiology, emphasizing the dysregulated immune processes, pathogenic molecular mediators, and the sequence of events leading from initial trigger to clinical manifestation and potential recovery.

## Primary Pathophysiological Mechanisms Underlying Spinal Cord Inflammation

The fundamental pathophysiological process in transverse myelitis involves dysregulated immune responses targeting components of the central nervous system, particularly the myelin sheath and associated glial cells within the spinal cord[1][2]. Rather than representing a pure demyelinating disorder, TM emerges as a mixed inflammatory condition involving multiple cellular and tissue compartments. The histopathophysiology varies considerably depending on the underlying etiology, but classical presentations are characterized by **perivascular infiltration, demyelination, and axonal injury mediated by monocytes and lymphocytes at lesion sites**[1][2][13]. The heterogeneous nature of TM pathology, manifested by involvement of both gray and white matter with variable degrees of inflammation across different cases, demonstrates that multiple immunological mechanisms can produce the characteristic clinical syndrome of acute spinal cord dysfunction[1][2].

The initial trigger for this inflammatory cascade differs markedly across TM etiologies but frequently involves either direct pathogenic infection or molecular mimicry following viral or bacterial infection[3][22]. In idiopathic cases, which represent the majority of TM presentations, the immune system mounts an abnormal and excessive response against the spinal cord in the absence of any identifiable external trigger[2][4]. The body's inflammatory response, which normally functions to eliminate infectious agents or repair injured tissue, becomes pathologically dysregulated and targets the healthy myelin insulation covering nerve fibers in the spinal cord[2][4]. This aberrant immune activation represents a fundamental departure from normal immune homeostasis, wherein protective inflammatory mechanisms become destructive to host tissue.

## Molecular Pathways and Dysregulated Inflammatory Processes

Multiple interconnected molecular pathways drive the inflammatory cascade in transverse myelitis, with distinct patterns emerging depending on the underlying etiology. The dysregulated pathways encompass classical and alternative complement activation, T cell and B cell mediated autoimmunity, cytokine-driven inflammation, and blood-brain barrier disruption. Understanding these pathways provides crucial insight into disease mechanisms and identifies potential therapeutic targets.

### Interleukin-6 and Astrocyte-Driven Inflammation

Recent investigations have identified interleukin-6 (IL-6) as a particularly critical mediator in TM pathogenesis. Research examining cerebrospinal fluid (CSF) from TM patients revealed that IL-6 levels are **selectively and dramatically elevated, with approximately 300-fold mean induction relative to control patients**[17]. Remarkably, IL-6 levels in CSF were 262-fold higher in acute TM cases compared to controls, whereas serum IL-6 did not differ significantly, suggesting that IL-6 is generated within the central nervous system rather than entering from peripheral circulation[17]. Immunohistochemical analysis of spinal cord autopsy specimens from deceased TM patients demonstrated that astrocytes constitute the predominant source of IL-6 production within inflammatory lesions, with microglial cells and infiltrating immune cells contributing less robustly to IL-6 secretion[17].

The cytopathic effects of IL-6 operate through STAT3 phosphorylation at Tyr705 in microglial cells, which is critical for mediating IL-6-induced neural injury[17]. Critically, IL-6 demonstrates both necessity and sufficiency for inducing the characteristic spinal cord injury observed in TM patients, as demonstrated through organotypic spinal cord cultures and animal models of TM[17]. IL-6 directly correlates with markers of tissue injury and sustained clinical disability in TM patients, establishing this cytokine as a key pathogenic effector linking inflammation to neurological dysfunction[17]. The mechanism involves IL-6 stimulation of astrocyte IL-6 production through a positive feedback loop, amplifying the inflammatory signal within the lesion microenvironment[17].

### Interleukin-17 and Th17-Driven Autoimmunity

Interleukin-17 (IL-17) production from peripheral blood mononuclear cells is markedly elevated in TM patients compared to healthy controls, multiple sclerosis patients, and other neurological diseases[14]. TM patients demonstrate approximately 8.4-fold higher IL-17 levels compared to MS patients and substantially higher levels compared to controls and other neurological diseases, with mean IL-17 levels of 302.6 pg/ml in TM versus 36.1 pg/ml in controls[14]. This elevated IL-17 production parallels and likely amplifies IL-6 levels, as IL-17 regulates the production of proinflammatory cytokines including TNF-α, IL-1β, and IL-6, all of which stimulate IL-6 production by astrocytes[14]. The relationship between IL-17 and IL-6 suggests that Th17 cell differentiation and IL-17 production represent critical events in TM immunopathogenesis, with IL-17 functioning as an amplifier of the inflammatory cascade already initiated by IL-6.

### Complement Cascade Activation

The complement system, particularly in antibody-mediated TM presentations such as neuromyelitis optica spectrum disorder (NMOSD), drives pathogenic astrocyte destruction and neuroinflammation[31][34]. When pathogenic aquaporin-4 (AQP4) immunoglobulin G antibodies bind to AQP4 on astrocyte membranes, they initiate complement activation through the classical pathway[31]. This cascade culminates in the enzymatic cleavage of complement component C5 into two highly active fragments: C5a, a potent anaphylatoxin, and C5b, which initiates assembly of the terminal complement complex C5b-9, also termed the membrane attack complex (MAC)[31][34]. The MAC functions as a pore-forming structure that inserts into the astrocyte membrane, causing osmotic dysregulation and rapid astrocyte death through complement-dependent cytotoxicity[31][34].

C5a operates as a powerful chemotactic factor recruiting and activating inflammatory cells, particularly neutrophils, driving a robust inflammatory infiltrate into CNS lesions[34]. C5aR and C3aR signaling involve the pertussis-toxin-sensitive G-protein G_αi with downstream activation of intracellular calcium, PI3K, Akt, and MAPK pathways, resulting in production of reactive oxygen species, pro-inflammatory mediators including IL-6 and TNF-α, histamine, and adhesion molecules[31]. Beyond direct complement-mediated astrocytolysis, bystander injury mechanisms contribute to tissue damage, wherein local diffusion of soluble C5b67 complexes produced by complement activation on astrocytes results in MAC formation on nearby bystander cells[31]. Antibody-dependent cellular cytotoxicity (ADCC) mechanisms also participate, with leukocytes activated by IgG binding to AQP4 on astrocytes causing targeted injury to adjacent cells through exocytosis of toxic granule contents[31].

The biological effects of complement activation extend beyond cytotoxicity to encompass leukocyte chemotaxis and recruitment of inflammatory cells. Bystander injury and complement-mediated leukocyte recruitment suggest that complement-targeted therapeutics may offer particular value in antibody-mediated TM presentations. C5 inhibition through monoclonal antibodies such as eculizumab and ravulizumab acts as a "circuit breaker," immediately blocking the final common pathway of tissue destruction by preventing C5 cleavage and thereby abolishing both C5a generation and MAC formation[31][34].

### Molecular Mimicry and Superantigen-Mediated Disease

Alternative histopathologic mechanisms in TM include molecular mimicry and superantigen-mediated disease, both operating through immune cross-reactivity mechanisms[1][19]. Molecular mimicry occurs when an infectious agent displays molecular structures that resemble epitopes within the spinal cord or myelin[22]. When the body mounts an immune response to the invading pathogen, it simultaneously responds to spinal cord molecules sharing structural characteristics with pathogen epitopes, leading to misdirected immune attack on host CNS tissue[22]. This mechanism has particular relevance in post-infectious TM presentations, wherein TM develops following recovery from a primary infection, suggesting that pathogen clearance has occurred while misdirected autoimmune responses persist.

Superantigen-mediated mechanisms bypass conventional MHC-peptide-TCR interactions by directly cross-linking MHC class II molecules on antigen-presenting cells with T cell receptors, causing massive polyclonal T cell activation independent of specific antigen recognition[1][3]. This leads to robust pro-inflammatory cytokine production and autoreactive T cell expansion. These alternative mechanisms likely operate alongside classical antigen-specific immune responses in various TM etiologies and contribute to the heterogeneous pathobiological features observed across the TM disease spectrum.

## Blood-Brain Barrier Disruption and Immune Cell Trafficking

The blood-brain barrier (BBB) dysfunction represents a critical early pathological event enabling immune cell infiltration into the spinal cord parenchyma. The BBB comprises endothelial cells interconnected by tight junctions, with pericytes and astrocyte endfeet forming the neurovascular unit (NVU). Breakdown of BBB integrity occurs through both paracellular and transcellular pathways[15]. Paracellular permeability increases via breakdown of tight junctions when inflammatory cytokines including TNF-α and IFN-γ activate BBB endothelial cells by upregulating proinflammatory signals such as NF-κB, resulting in decreased tight junction protein expression[15].

Transcellular leukocyte migration across the BBB occurs via coordinated activation of cell adhesion molecules on endothelial cells and their corresponding ligands on lymphocytes. Lymphocytes express very late antigen-4 (VLA-4) and lymphocyte function-associated antigen-1 (LFA-1), which couple with endothelial cell receptors VCAM-1 and ICAM-1, respectively, to mediate leukocyte arrest and transmigration[15]. VCAM-1 upregulation in BBB endothelial cells around active or inactive lesions suggests that endothelial activation precedes demyelination formation[15]. Additional adhesion molecules including melanoma cell adhesion molecule (MCAM), activated leukocyte cell adhesion molecule (ALCAM), and diapedesis-promoting integrin and costimulatory molecule (DICAM) orchestrate trafficking of specific immune cell subsets, particularly pathogenic Th1 and Th17 cells[15].

Endothelial cells can be directly targeted by pathogenic autoantibodies, as demonstrated in NMOSD where autoantibodies against glucose-regulated protein 78 (GRP78) on brain microvascular endothelial cells activate these cells and induce claudin-5 downregulation and enhanced macromolecule transit[18]. These mechanisms collectively represent a fundamental shift in BBB function from a protective barrier to a gateway facilitating CNS immune infiltration.

## Glial Cell Activation and Astrocyte-Microglia Interactions

Astrocytes and microglial cells play pivotal roles in TM pathophysiology beyond their role as IL-6 producers. Astrocyte activation and microglial activation represent hallmark features of TM histopathology[12][25]. In NMOSD-associated TM, astrocytes activated by AQP4-IgG binding undergo loss of AQP4 expression yet remain initially viable, establishing a "precytolytic" phase wherein astrocytes are activated but not yet lysed[26]. During this precytolytic phase, astrocytes signal to microglia via complement fragment C3a, derived from upregulated astrocytic complement C3 protein[26].

Microglial C3a receptor (C3aR) signaling emerges as critical for progression beyond the precytolytic phase, with C3aR-deficient mice showing attenuated microglial activation and motor impairment despite ongoing astrocyte activation and AQP4 downregulation[26]. Confocal imaging reveals striking physical coalescence of astrocytes and microglia following NMO-IgG-mediated astrocyte activation, with microglial processes converging toward activated astrocytes[26]. This astrocyte-microglia crosstalk thus represents a previously underappreciated mechanism driving disease progression and motor deficits in NMO-associated TM, suggesting that microglia serve as critical effectors of neuronal dysfunction following astrocyte activation.

The microglial contribution to TM extends beyond astrocyte-microglia interactions to include direct effects on neurons and axons. Microglial-derived pro-inflammatory mediators, reactive oxygen species, and proteases can directly damage neuronal structures. Additionally, microglial phagocytic activity may contribute to myelin and axonal debris clearance but can also result in excess neural tissue destruction if uncontrolled.

## Key Molecular Players: Antigens, Antibodies, and Autoreactive Cell Populations

### Aquaporin-4: The Prototype AQP4-Associated Autoimmune TM

Aquaporin-4 (AQP4), a water channel protein localized to astrocyte plasma membranes particularly at perivascular endfeet, represents the primary autoantigen in approximately 40% of neuromyelitis optica spectrum disorder (NMOSD) cases and a substantial subset of severe TM presentations[1][7][10]. The AQP4 protein mediates water transport across astrocyte membranes, essential for osmoregulation and astrocyte volume control[7]. Circulating anti-AQP4 immunoglobulin G autoantibodies directly initiate astrocyte injury upon binding to extracellular epitopes of AQP4, triggering complement-dependent cytotoxicity and antibody-dependent cellular cytotoxicity mechanisms[7][31]. The presence of anti-AQP4 antibodies in serum demonstrates robust specificity for NMOSD, with nearly perfect positive predictive value for the diagnosis when combined with appropriate clinical and imaging findings.

Longitudinally extensive transverse myelitis (LETM), defined as spinal cord lesions extending over three or more vertebral segments with more than two-thirds of cord thickness involvement, shows particularly high association with anti-AQP4 seropositivity. In one study examining recurrent TM patients, anti-AQP4 antibody positivity increased from 26.9% overall to 41.2% among LETM cases[7]. The presence of anti-AQP4 antibodies in LETM predicts higher disability scores and increased likelihood of disease recurrence and conversion to NMO[7][10]. While anti-AQP4 seropositivity predicts recurrent disease course, it does not necessarily predict long-term disability outcome, suggesting that multiple pathogenic mechanisms contribute to final clinical outcomes beyond AQP4-IgG activity.

### Myelin Oligodendrocyte Glycoprotein (MOG) and MOG Antibody-Associated Disease

Myelin oligodendrocyte glycoprotein (MOG) represents an alternative primary autoantigen in a subset of TM cases, particularly in MOG antibody-associated disease (MOGAD)[8][11]. MOG comprises an extracellular domain on the outer surface of oligodendrocyte myelin sheaths and is exposed on cell surfaces of both oligodendrocytes and myelin-producing cells. Anti-MOG antibodies in MOGAD patients target these exposed epitopes, leading to demyelination and CNS inflammation[8]. MOGAD presents as the second most common presentation of MOG antibody disease overall, occurring in approximately 26% of affected patients[8].

Importantly, TM in MOGAD typically presents with better neurological outcomes compared to AQP4-IgG-positive NMOSD, with MOGAD TM patients demonstrating lower average expanded disability status scale (EDSS) scores than AQP4-Ab positive NMOSD patients[8]. However, MOGAD-associated TM frequently involves the conus medullaris, predisposing to persistent bladder dysfunction with up to 59% experiencing long-term bladder symptoms compared to 48% in AQP4-positive NMOSD[8]. A major diagnostic challenge in MOGAD-associated TM involves fluctuating MOG antibody seropositivity, with antibody levels varying over time, occasionally disappearing and reappearing, and the possibility of initially normal MRI in up to 10% of patients[8].

### T Cell and B Cell Responses in TM Pathogenesis

Both CD4+ and CD8+ T cells contribute substantially to TM pathophysiology through multiple mechanisms. Th17 cells, differentiated through the combined action of TGF-β plus IL-6, with IL-21 and IL-23 enhancing their precursor frequency and stabilizing their phenotype, represent particularly pathogenic T cell subsets in TM[38]. Th17 cells express the transcription factor RORC and produce IL-17, IL-21, and IL-22, all of which promote endothelial activation, increase trans-endothelial migration of neutrophils and eosinophils, and amplify local inflammation[15][38]. Compared to MS patients, TM patients display higher proportions of Th17 cells and IL-17-producing CD8+ T cells in peripheral blood, suggesting that TM represents a Th17-driven autoimmune disease[38].

The relationship between T cells and B cells in TM involves critical cross-talk in both directions[38]. B cells, beyond their role as antibody producers, serve as antigen-presenting cells and produce IL-6, potentially skewing T cells toward a Th17 response[38]. Conversely, Th17 cells provide very effective help to B cells, facilitating germinal center formation and autoantibody production[38]. In AQP4-IgG seropositive NMOSD, NMO-IgG is produced peripherally rather than intrathecally, with antibody-producing plasmablasts and plasma cells not recruited to the subarachnoid space[38]. This peripheral generation of pathogenic antibodies indicates that T cell help occurs in secondary lymphoid organs rather than within the CNS, representing a fundamental distinction from MS wherein intrathecal antibody production occurs.

## Genetic Factors and Host Susceptibility

Genetic predisposition significantly influences TM susceptibility and clinical manifestations. Specific human leukocyte antigen (HLA) alleles confer risk for NMOSD-associated TM, with HLA-DRB1*08:02 and HLA-DRB1*16:02 identified as risk alleles while HLA-DRB1*09:01 confers protection[20][23]. The potassium channel gene KCNMA1, which encodes large-conductance calcium-activated potassium channel alpha 1 subunit, associates with disability and transverse myelitis in NMOSD, with immunohistochemical detection in perivascular endfeet of astrocytes and markedly diminished immunoreactivity in active spinal cord lesions[20][23]. This suggests that KCNMA1-mediated potassium channel dysfunction in astrocytes may impair osmoregulation and contribute to cellular injury.

MS genetic risk alleles outside the major histocompatibility complex region also contribute to NMOSD susceptibility, though with lesser effect sizes than in MS[20]. The MS genetic burden score in NMOSD patients is significantly higher than in healthy controls, suggesting that genetic factors conferring MS risk partially overlap with those for TM and NMOSD[20].

## Cellular Components and Site-Specific Pathological Processes

### Perivascular Inflammation and Gray Matter Involvement

The characteristic histopathological distribution of TM lesions, with perivascular infiltration of inflammatory cells, reflects the predilection for vascular-associated immune infiltration[1][3][6]. Monocyte and lymphocyte infiltration concentrates around small blood vessels within the spinal cord, establishing inflammatory foci that subsequently spread to involve adjacent parenchyma. The involvement of both gray and white matter in TM lesions represents a departure from classical demyelinating patterns and indicates that neurons and neuronal cell bodies are targeted alongside myelin-producing oligodendrocytes.

Gray matter involvement in TM produces distinctive lower motor neuron (LMN) features, urinary retention, and a more devastating but often monophasic clinical course, distinct from white matter myelitis with upper motor neuron (UMN) features and more indolent but potentially recurrent courses[35][40]. This distinction suggests fundamentally different pathological processes target motor neurons directly versus corticospinal tract axons. Anterior horn cell dysfunction, as detected through electromyography, predicts poor long-term recovery prognosis, indicating that neuronal loss carries particular prognostic significance[40].

### Oligodendrocyte and Myelin Vulnerability

Oligodendrocytes and myelin sheaths represent primary targets of TM pathogenic mechanisms. Demyelination in TM arises from both direct oligodendrocyte injury through antibody-mediated and T cell-mediated mechanisms and from bystander demyelination secondary to inflammatory mediator release. The heterogeneous histopathology, with variable degrees of demyelination, axonal injury, and astroglial and microglial activation, indicates multiple potentially overlapping mechanisms of oligodendrocyte and myelin injury operating across different TM etiologies.

Oligodendrocyte progenitor cells (OPCs) represent potential therapeutic targets for remyelination, with research demonstrating that human glial restricted progenitor cells can integrate into spinal cord-demyelinated lesions and remyelinate lesions while supporting damaged axons[6][21]. The capacity for endogenous remyelination exists within the injured spinal cord but is frequently insufficient to fully restore myelin or neurological function, suggesting that therapeutic enhancement of remyelination capacity may improve long-term outcomes.

## Disease Progression: Sequence of Events from Trigger to Clinical Manifestation

The temporal progression of transverse myelitis follows a relatively stereotyped pattern despite variable etiologies, with symptom onset ranging from acute onset within hours to subacute progression over four weeks[2][25][41]. The characteristic progression to nadir occurs between 4 hours and 21 days after symptom onset, representing a critical diagnostic feature[1][2][13][25]. This rapid progression reflects the acute inflammatory nature of the disorder and contrasts sharply with the much slower progression in many other myelopathies.

The sequence of pathophysiological events likely proceeds as follows: initial trigger (infection, molecular mimicry, or unknown factors in idiopathic cases) activates innate and adaptive immune responses; BBB disruption allows immune cell infiltration into the spinal cord; activated T cells and B cells, along with innate immune cells, infiltrate the cord parenchyma; astrocytes become activated by direct contact with immune cells and exposure to pro-inflammatory cytokines; complement and antibody-mediated mechanisms target antigens on astrocytes and oligodendrocytes; IL-6 and IL-17 production drives amplification of inflammation; microglia become activated and interact with astrocytes in AQP4-IgG-mediated disease; myelin destruction proceeds through demyelination; axonal injury and neuronal dysfunction occur; and clinical manifestations emerge reflecting the spinal cord level and degree of tissue injury.

The rapid clinical progression to nadir likely reflects the acute inflammatory and demyelinating processes overwhelming the spinal cord's limited capacity for compensatory adaptation. Demyelination blocks action potential propagation along axons, leading to immediate functional deficit. Axonal injury and cell death may accumulate rapidly during the acute inflammatory phase.

## Distinct Etiological Pathways Leading to TM

### Idiopathic TM: Immune Dysregulation Without Identifiable Trigger

Idiopathic transverse myelitis, comprising the majority of TM cases, occurs in the absence of identifiable external triggers yet demonstrates clear evidence of immune-mediated tissue injury[1][2][4]. The underlying pathophysiological mechanism in idiopathic TM is postulated to involve an immune response to a virus that the body has cleared and is no longer detectable, with the immune system remaining activated and mistakenly attacking the spinal cord wiring[2]. This scenario implies that initial viral infection triggers immune activation through pattern recognition and provides antigenic epitopes; the virus is subsequently cleared from the body; yet the activated immune response persists and becomes redirected against self-antigens through molecular mimicry or epitope spreading mechanisms; and immune attack on the myelin sheath ensues.

### Post-Infectious and Parainfectious TM

Post-infectious TM develops following recovery from viral or bacterial infection, suggesting that immune responses initiated against pathogens become misdirected to the spinal cord[1][22][37]. Numerous infectious agents associate with TM, including enteroviruses, West Nile virus, herpes viruses, HIV, HTLV-1, Zika virus, neuroborreliosis from Lyme disease, Mycoplasma, and Treponema pallidum[1][4][37]. The temporal relationship between infection and TM onset, with TM developing days to weeks after infectious symptom resolution, supports post-infectious rather than direct viral infection of the spinal cord as the primary mechanism in many cases[22].

Molecular mimicry represents the leading proposed mechanism in post-infectious TM, wherein pathogenic epitopes share structural features with CNS antigens[22]. When immune responses target the pathogenic epitope, cross-reactivity with self-antigens ensues. Viral superantigens represent an alternative mechanism, causing polyclonal T cell expansion independent of specific antigen recognition and generating a pool of autoreactive T cells that secondarily attack CNS tissue[3].

### Systemic Autoimmune Disease-Associated TM

Multiple systemic inflammatory autoimmune disorders associate with TM, including systemic lupus erythematosus (SLE), Sjögren syndrome (SS), Behçet disease, sarcoidosis, antiphospholipid syndrome, and others[1][35][40][43]. In these contexts, TM arises from dysregulated systemic autoimmunity with secondary CNS involvement. SLE-associated TM typically presents with longitudinally extensive lesions and more severe clinical courses requiring aggressive immunosuppression[43]. The presence of oligoclonal bands in CSF and elevated IgG index in SLE-related TM indicates intrathecal immunoglobulin synthesis, suggesting active CNS autoimmunity within the spinal cord microenvironment[40].

Sjögren syndrome-associated TM frequently affects the cervical cord and may manifest as LETM[43]. Spinal cord involvement occurs in 20-35% of SS patients and may represent the initial disease manifestation in approximately 20%[35]. SS-associated TM often proves refractory to corticosteroid monotherapy, requiring more aggressive immunosuppressive approaches including intravenous cyclophosphamide[43].

Antiphospholipid antibody syndrome-associated TM likely involves interactions between circulating antiphospholipid antibodies and spinal cord phospholipids, with resulting thrombotic or inflammatory complications[43]. CSF findings typically reveal neutrophilic pleocytosis with elevated protein and occasionally elevated IgG index[35].

Paraneoplastic TM occurs as a remote neurological complication of malignancy, particularly in association with specific paraneoplastic antibodies such as anti-CRMP-5 (collapsin response mediator protein-5) in small cell lung carcinoma[35][40]. These antibodies target CNS antigens cross-reactive with tumor antigens, and remission of the underlying malignancy may lead to TM improvement.

### Vaccine-Associated TM

Rare cases of TM have been anecdotally reported following vaccination, including vaccinations against rabies, diphtheria-tetanus-polio, pertussis, MMR, influenza, hepatitis B, and recently COVID-19[4][42]. One theory suggests that vaccination may jumpstart an autoimmune process in genetically susceptible individuals, though the exact mechanisms remain unclear[4]. Importantly, extensive research has demonstrated that vaccines are safe, and any association with TM may be coincidental or represent an exceptionally rare complication[4]. The temporal association between vaccination and TM onset, occurring within days to three months, suggests that if a causal relationship exists, it likely involves vaccine-triggered immune activation rather than vaccine components causing direct CNS injury[4].

## Phenotypic Manifestations and Their Relationship to Pathophysiology

### Acute Motor Deficits: Paraparesis and Paralysis

Motor weakness, typically progressing rapidly and reaching peak deficit within days to weeks, reflects damage to corticospinal tracts and gray matter motor neurons[2][33][37][41]. At peak deficit, 50% of patients present with complete paraplegia, illustrating the severity of motor pathway disruption[2][19]. Upper motor neuron signs predominate when white matter lesions damage corticospinal tracts, while lower motor neuron signs emerge when lesions directly involve anterior horn cells in gray matter[40][43]. The progression from initial flaccidity to subsequent spasticity reflects evolving stages of spinal shock and neuronal reorganization.

The lesion level determines which motor systems are affected, with thoracic lesions (affecting 70% of cases) causing lower extremity weakness and gait disturbance, cervical lesions (20% of cases) potentially affecting upper extremities and breathing through phrenic nerve involvement, and lumbosacral lesions (10% of cases) causing lower extremity weakness[1][2][13]. The rapid development and severity of motor deficits reflect the acute inflammatory demyelination and axonal injury mechanisms rather than gradual progressive myelin loss or neurodegeneration typical of chronic disorders.

### Sensory Level and Sensory Dysfunction

The sensory level, defined as a clearly demarcated boundary below which sensation is reduced or absent, represents a hallmark physical finding in TM and emerges from spinal cord transection or near-transection of sensory pathways[1][2][4][35]. Approximately 80% of TM patients present with a clearly defined sensory level[25]. Sensory symptoms generally affect the lesion level or 1-2 levels above or below the lesion, reflecting the anatomical distribution of the inflammatory lesion. Abnormal sensations including dysesthesia (unpleasant, burning sensation), paresthesia (tingling, "pins and needles" sensation), and allodynia (pain from light touch normally non-painful) occur in 80-94% of TM patients[4][25][47].

The pathophysiological basis for sensory dysfunction involves demyelination of spinothalamic and dorsal column fibers, disrupting the normal transmission of pain, temperature, and proprioceptive information to the brain. The distinctive band-like sensation wrapping around the torso reflects the transverse nature of the spinal cord lesion affecting both sides, creating a level boundary at the lesion rostral margin[4][47].

### Autonomic Dysfunction: Bladder, Bowel, and Sexual Dysfunction

Autonomic dysfunction represents an almost universal finding in acute TM, with virtually all patients experiencing some degree of bladder or bowel dysfunction at peak deficit[2][19]. The acute phase features urinary retention due to spinal shock affecting parasympathetic sacral autonomic fibers, followed by development of hyperreflexic, spastic bladder or flaccid atonic bladder depending on the stage of spinal shock resolution[22]. Bowel dysfunction typically manifests as constipation acutely and may progress to incontinence. Sexual dysfunction occurs frequently, with men experiencing erectile dysfunction and both genders experiencing difficulty achieving orgasm[36][48].

The pathophysiology involves damage to autonomic nerve fibers within the spinal cord, particularly at the conus medullaris where sacral parasympathetic fibers concentrate[40][43]. Conus-localized lesions produce particularly prominent early and severe sphincter and sexual dysfunction[40][43]. The presence of prominent bladder dysfunction at presentation may paradoxically indicate central cord involvement where autonomic fibers are concentrated, thus potentially predicting worse neurological outcomes[22].

### Back Pain and Radicular Symptoms

Back pain, occurring in 80-95% of TM patients, typically precedes or accompanies motor and sensory symptoms[6][25]. The pain frequently localizes to the thoracic or lumbar region corresponding to the lesion location. The pathophysiological basis for pain in TM likely involves several mechanisms: inflammatory irritation of spinal nerve roots or meningeal structures, ischemia from impaired spinal cord blood flow, and dysfunction of pain-processing systems following demyelination. Sharp, radiating pain shooting down extremities or wrapping around the trunk suggests root involvement or sensory pathway irritation.

### Spinal Shock and Long-Term Disability

Immediately after acute TM onset, spinal shock develops over approximately three weeks, a period of transient depression of neural activity below the lesion producing flaccid paralysis, absent reflexes, and suppressed autonomic function[22]. Following spinal shock resolution, gradual recovery of reflex function occurs, often accompanied by transition to spastic paralysis with hyperreflexia. The distinction between these phases has prognostic significance, with patients demonstrating persistent lower motor neuron features beyond the expected spinal shock duration showing poor long-term recovery prognosis[43].

Long-term disability outcomes vary dramatically across the TM spectrum: approximately 33% recover with little to no lasting deficits, 33% develop moderate permanent disability, and 33% experience severe permanent disability[2][13][19][24]. Pain and spasticity represent the most frequent long-term complications, affecting quality of life substantially even in patients with otherwise good motor recovery[36]. Persistent sexual dysfunction, depression, anxiety, and social isolation constitute additional long-term consequences of TM with significant impact on patient wellbeing[36][48].

## Differential Diagnosis and Disease Mimics

Recognition that TM represents a syndrome rather than a disease entity with single etiology necessitates careful differential diagnosis to exclude other myelopathies that mimic TM clinically and radiographically. Conditions that must be excluded include compressive myelopathy from herniated discs, vertebral body compression fractures, epidural abscesses or masses, and spondylitis[1][37]. Vascular causes including spinal cord infarction from anterior spinal artery occlusion must be excluded, as these require distinct management strategies. Metabolic and nutritional causes such as vitamin B12 deficiency or copper deficiency present with similar clinical features but have entirely different pathophysiology and treatment approaches[35][40]. Neoplasms, both primary intramedullary and metastatic, may present acutely with myelitic features. Radiation myelitis from prior spinal cord radiation represents another important mimic. Guillain-Barré syndrome, an ascending motor paralysis from peripheral nerve involvement, must be distinguished from TM through clinical examination and electrodiagnostic testing[1].

## Contemporary Understanding of Recovery Mechanisms

Recovery from acute TM proceeds through multiple mechanisms encompassing natural resolution of inflammation, remyelination, axonal regeneration, and plastic reorganization of spinal cord circuits. Most recovery occurs within the first three months after symptom onset, though improvements continue for up to two years[1][2][13][21]. Intensive physical and occupational therapy initiated early maximizes functional recovery by promoting activity-dependent neural repair mechanisms[21][53].

Myelin repair through oligodendrocyte progenitor cell (OPC) proliferation and differentiation into new myelinating oligodendrocytes represents an important endogenous repair mechanism, though it frequently occurs incompletely. Emerging therapeutic approaches including stem cell transplantation and remyelination-promoting therapies aim to enhance these natural repair processes[27][30]. Mesenchymal stem cells and neural progenitor cells secrete neurotrophic growth factors, modulate inflammation, and promote axonal regeneration and remyelination when delivered to lesion sites[27][30].

Neuroplasticity mechanisms, whereby preserved neural circuits reorganize and develop new functional connections to bypass damage, contribute substantially to functional recovery even without histological myelin repair[21][53]. Spinal cord reorganization can redirect motor commands through alternative pathways, permitting recovery of function despite persistent demyelination.

## Conclusion

Transverse myelitis emerges as a pathophysiologically diverse yet clinically recognizable syndrome of acute spinal cord inflammation and demyelination. Multiple molecular and cellular mechanisms converge from distinct etiological pathways to produce the characteristic clinical manifestations of rapidly progressive motor, sensory, and autonomic dysfunction. Dysregulated immune responses targeting components of the myelin-glia-neuronal complex result from both identifiable external triggers and intrinsic immune dysregulation in idiopathic cases. The heterogeneous histopathology reflecting variable involvement of gray and white matter, different cell types, and multiple pathogenic mechanisms indicates that TM encompasses multiple disease entities with overlapping clinical presentations. Understanding these underlying pathophysiological mechanisms provides a foundation for developing targeted therapeutic interventions aimed at suppressing pathogenic immune responses while promoting endogenous repair processes.