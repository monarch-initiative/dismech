# Citations for Research Query

**Query:** # Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Hypermobile Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007523 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Candidate extracellular matrix remodeling abnormalities (cultured hEDS/HSD dermal fibroblasts: disorganised collagen and fibronectin ECM, loss of alpha2beta1/alpha5beta1 integrin organisation, preferential alphavbeta3 integrin; CELLULAR, hypothetical); 2. Myofibroblast-like fibroblast transition (alphavbeta3 integrin/ILK/Snail1 signalling, alpha-SMA stress fibres, cadherin-11, MMP9 - in vitro patient-fibroblast evidence only; CELLULAR, provisional); 3. Joint instability and recurrent soft-tissue injury (TISSUE; currently the only node wired to phenotypes: Joint dislocation, Chronic pain, Arthralgia)

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Joint hypermobility; Joint dislocation; Chronic pain; Arthralgia; Myalgia; Fatigue; Sleep disturbance; Migraine; Peripheral neuropathy (including small-fiber neuropathy); Orthostatic tachycardia (postural tachycardia syndrome); Acrocyanosis; Gastrointestinal dysmotility; Gastroesophageal reflux; Nausea; Constipation; Mitral valve prolapse; Aortic root dilatation; Hyperextensible skin; Soft skin; Atrophic scars; Striae distensae; Easy bruising; Pelvic organ prolapse; Abdominal wall hernia; Dental crowding; High, narrow palate; Sleep apnea; Anxiety; Depression

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Hypermobile EDS (2017 criteria) is a clinically diagnosed heritable connective tissue disorder with autosomal dominant transmission in families and NO confirmed causal gene; the 2017 criteria deliberately separate it from hypermobility spectrum disorder, and the entry already records the genetics controversy, the proposed KLK15, ACKR3 and complement/proteomic candidates (2025, unreplicated), and the TNXB-associated hypermobility disorder as separate open discussions. Do NOT re-survey the causal-gene question, the hEDS-versus-HSD boundary debate, or the diagnostic criteria. Treat generalised connective-tissue laxity with a candidate fibroblast ECM-remodeling/myofibroblast-transition phenotype as the given upstream context, and concentrate entirely on how that context produces each listed clinical manifestation.

## Research Objective

The missing layer is the **causal wiring between the mechanism nodes and the
clinical phenotypes**: which pathophysiological process produces which clinical
manifestation, through what intermediates. For **each phenotype listed above**,
report:

1. **The mechanistic chain** from the established disease process to that
   phenotype, as an ordered sequence of steps, one per line, with explicit
   causal verbs ("leads to", "results in"). Start each chain from whichever of
   the existing mechanism nodes is the true proximal upstream step.
2. **Missing intermediate processes**: where the chain passes through a
   process that is NOT in the mechanism node list above (for example a
   malabsorption step, a distinct autoantibody specificity, a clonal expansion
   step), name it explicitly and flag it as a proposed new node.
3. **Primary human evidence** for each causal step: PMIDs with exact quotes
   from the abstracts. Prefer human clinical and interventional studies
   (dietary-withdrawal reversal counts as interventional evidence for a causal
   link). Distinguish evidence source types: human clinical, model organism,
   in vitro, computational.
4. **An evidence grade for the chain as a whole**, one of:
   - ESTABLISHED — causal chain demonstrated in humans, widely accepted
   - SUPPORTED — plausible chain with direct human evidence for most steps
   - PROPOSED — hypothesis in the literature, key steps not demonstrated
   - NOT_ESTABLISHED — the association is documented but no mechanistic chain
     has been demonstrated; competing explanations remain open
5. **Non-causal alternatives** where they are live: if the phenotype may be
   associated through shared genetic background (for example shared HLA
   haplotypes), coincident autoimmunity, or ascertainment rather than through
   downstream causation, say so explicitly.

**Honesty requirement:** "NOT_ESTABLISHED, mechanism unknown" is a correct and
valuable answer. Do NOT manufacture a mechanistic chain to satisfy the request.
A phenotype with no settled mechanism should be reported as exactly that, with
the competing hypotheses named and graded. It is expected that several
phenotypes in the list will end up NOT_ESTABLISHED.

## Priority Hubs

The following convergence hubs are anticipated to route several phenotypes and
must NOT be given shallow treatment. For each, report the full mechanistic
detail and per-branch citations:

(a) PAIN HUB: how hEDS chronic pain arises beyond acute mechanical injury - central sensitisation / nociplastic pain (lowered pressure and thermal pain thresholds, temporal summation), small-fiber neuropathy (reduced intraepidermal nerve fibre density on skin biopsy), proprioceptive deficit and muscle weakness from joint laxity, and their contribution to arthralgia, myalgia, migraine, fatigue and sleep disturbance; give human quantitative-sensory-testing and skin-biopsy studies as primary evidence. (b) AUTONOMIC HUB: the proposed routes from connective-tissue laxity to postural tachycardia / orthostatic intolerance - venous pooling from distensible vessel walls and reduced preload, autonomic small-fiber neuropathy, hyperadrenergic state, deconditioning, and mast-cell mediator release; say which have direct human measurement (tilt-table, catecholamines, venous compliance) and which are inference; include acrocyanosis as a vasomotor manifestation. (c) GASTROINTESTINAL HUB: gut-wall connective tissue laxity, autonomic dysfunction, visceral hypersensitivity and mast-cell activation as competing or additive explanations for dysmotility, reflux, nausea and constipation; report manometry, gastric-emptying and disorders-of-gut-brain-interaction cohort data. (d) TISSUE LAXITY HUB: the direct mechanical consequences of lax connective tissue in each site - joint capsule and ligament (hypermobility, dislocation), dermis (hyperextensible and soft skin, atrophic scars, striae, easy bruising from vessel-wall and perivascular support fragility), pelvic floor (prolapse), abdominal wall (hernia), cardiac valve and aortic root (mitral valve prolapse, aortic root dilatation - including the longitudinal data showing hEDS aortic dilatation is usually mild and non-progressive), and craniofacial/upper-airway structures (dental crowding, high narrow palate, obstructive sleep apnea). (e) PSYCHIATRIC HUB: whether anxiety and depression in hEDS are downstream of chronic pain, dysautonomia and interoceptive sensitivity, share a neurodevelopmental or autonomic substrate, or are ascertainment effects; name the cohort and imaging studies and treat non-causal explanations as live.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as listed
  above, containing: the numbered causal chain, the evidence grade, PMIDs with
  exact abstract quotes per step, and suggested ontology terms (GO for
  biological processes, CL for cell types, HP for the phenotype itself).
- A final section titled **Proposed New Mechanism Nodes** listing every
  intermediate process flagged in item 2, each with: a suggested node name, its
  upstream node (from the existing list or another proposed node), its
  downstream phenotypes, and the strongest single citation for its causal
  placement.
- A final section titled **Unwired Phenotypes** listing every phenotype graded
  NOT_ESTABLISHED, with one sentence each on what evidence would settle it.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make

**Provider:** openscientist
**Generated:** 2026-11-12T13:10:16.287134

1. PMID:7283686
2. PMID:31498548
3. PMID:26919608
4. PMID:27306637
5. PMID:19878973
6. PMID:20579833
7. PMID:42417930
8. PMID:42437376
9. PMID:42640494
10. PMID:28073787
11. PMID:32434316
12. PMID:28986003
13. PMID:12010910
14. PMID:38747032
15. PMID:41432355
16. PMID:40387691
17. PMID:21193204
18. PMID:42099513
19. PMID:6806400
20. PMID:15566352
21. PMID:19592142
22. PMID:26658756
23. PMID:42979294
24. PMID:34213599
25. PMID:40609249
26. PMID:22539777
27. PMID:25089514
28. PMID:35449490