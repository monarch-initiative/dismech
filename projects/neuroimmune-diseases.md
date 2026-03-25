# Neuroimmune Diseases Curation Project

## Overview
Comprehensive curation of neuroimmune diseases for the dismech knowledge base. Neuroimmune diseases are conditions where the immune system attacks components of the nervous system (CNS or PNS), causing inflammation, demyelination, or neuronal damage.

## Existing Neuroimmune Diseases in KB (7)
These are already in the knowledge base and may benefit from enhancement:

| Disease | File | Status | Notes |
|---------|------|--------|-------|
| Multiple Sclerosis | Multiple_Sclerosis.yaml | High quality | CNS demyelination, autoimmune |
| Guillain-Barré Syndrome | Guillain_Barre_Syndrome.yaml | Moderate | PNS molecular mimicry |
| CIDP | Chronic_Inflammatory_Demyelinating_Polyneuropathy.yaml | Moderate | Chronic PNS demyelination |
| Myasthenia Gravis | Myasthenia_Gravis.yaml | High quality | NMJ autoantibodies |
| Stiff Person Syndrome | Stiff_Person_Syndrome.yaml | 100% compliance | Anti-GAD65 autoimmune |
| Narcolepsy | Narcolepsy.yaml | High quality | Likely autoimmune (hypocretin neurons) |
| ME/CFS | Myalgic_Encephalomyelitis_Chronic_Fatigue_Syndrome.yaml | High quality | Immune dysfunction, neuroinflammation |

## New Neuroimmune Diseases to Curate (15)

### Priority 1: CNS Demyelinating Disorders
| Disease | File | Status | Description |
|---------|------|--------|-------------|
| Neuromyelitis Optica Spectrum Disorder (NMOSD) | Neuromyelitis_Optica_Spectrum_Disorder.yaml | [ ] To curate | Anti-AQP4/MOG antibodies target optic nerves and spinal cord |
| MOG Antibody Disease (MOGAD) | MOG_Antibody_Disease.yaml | [ ] To curate | Anti-MOG antibodies, distinct from MS and NMOSD |
| Acute Disseminated Encephalomyelitis (ADEM) | Acute_Disseminated_Encephalomyelitis.yaml | [ ] To curate | Post-infectious CNS demyelination, mainly children |
| Transverse Myelitis | Transverse_Myelitis.yaml | [ ] To curate | Immune-mediated spinal cord inflammation |

### Priority 2: Autoimmune Encephalitis
| Disease | File | Status | Description |
|---------|------|--------|-------------|
| Anti-NMDA Receptor Encephalitis | Anti-NMDA_Receptor_Encephalitis.yaml | [ ] To curate | Most common autoimmune encephalitis, psychiatric + movement |
| Limbic Encephalitis | Limbic_Encephalitis.yaml | [ ] To curate | Memory loss, seizures, psychiatric symptoms |
| Hashimoto Encephalopathy (SREAT) | Hashimoto_Encephalopathy.yaml | [ ] To curate | Steroid-responsive encephalopathy with anti-thyroid antibodies |

### Priority 3: CNS Inflammatory Disorders
| Disease | File | Status | Description |
|---------|------|--------|-------------|
| CNS Vasculitis | CNS_Vasculitis.yaml | [ ] To curate | Primary angiitis of the CNS |
| Neurosarcoidosis | Neurosarcoidosis.yaml | [ ] To curate | Granulomatous inflammation of nervous system |
| Susac Syndrome | Susac_Syndrome.yaml | [ ] To curate | Microangiopathy affecting brain, retina, inner ear |

### Priority 4: Other Neuroimmune Conditions
| Disease | File | Status | Description |
|---------|------|--------|-------------|
| Optic Neuritis | Optic_Neuritis.yaml | [ ] To curate | Inflammation of optic nerve |
| Acute Flaccid Myelitis (AFM) | Acute_Flaccid_Myelitis.yaml | [ ] To curate | Enterovirus-associated anterior horn cell syndrome |
| Neuropsychiatric SLE | Neuropsychiatric_SLE.yaml | [ ] To curate | CNS manifestations of lupus |
| Autoimmune Autonomic Ganglionopathy | Autoimmune_Autonomic_Ganglionopathy.yaml | [ ] To curate | Anti-ganglionic AChR antibodies |
| Paraneoplastic Neurological Syndromes | Paraneoplastic_Neurological_Syndromes.yaml | [ ] To curate | Cancer-associated autoimmune neurological disorders |

## Key Neuroimmune Mechanisms to Cover
1. **Antibody-mediated** - autoantibodies targeting neural antigens (AQP4, MOG, NMDAR, VGCC, GAD65)
2. **T cell-mediated** - autoreactive T cells attacking CNS/PNS components
3. **Molecular mimicry** - cross-reactivity between pathogens and neural antigens
4. **Complement activation** - complement-mediated tissue destruction
5. **Blood-brain barrier disruption** - immune cell infiltration into CNS
6. **Microglial activation** - CNS innate immune response
7. **Paraneoplastic** - cancer-driven autoimmunity against neural tissue

## Target Autoantibodies to Document
- Anti-AQP4 (aquaporin-4) - NMOSD
- Anti-MOG (myelin oligodendrocyte glycoprotein) - MOGAD, ADEM
- Anti-NMDAR - Anti-NMDA receptor encephalitis
- Anti-LGI1, Anti-CASPR2 - Limbic encephalitis
- Anti-GAD65 - Stiff Person Syndrome, cerebellar ataxia
- Anti-AChR - Myasthenia Gravis
- Anti-ganglioside (GM1, GD1a, GQ1b) - GBS variants
- Anti-Hu, Anti-Yo, Anti-Ri - Paraneoplastic syndromes
- Anti-TPO - Hashimoto encephalopathy

## Deep Research Provider
Default: falcon

---

# STATUS

## New Diseases to Curate (1/15)
- [x] Neuromyelitis Optica Spectrum Disorder (NMOSD) - 70.6% compliance
- [ ] MOG Antibody Disease (MOGAD)
- [ ] Acute Disseminated Encephalomyelitis (ADEM)
- [ ] Transverse Myelitis
- [ ] Anti-NMDA Receptor Encephalitis
- [ ] Limbic Encephalitis
- [ ] Hashimoto Encephalopathy (SREAT)
- [ ] CNS Vasculitis
- [ ] Neurosarcoidosis
- [ ] Susac Syndrome
- [ ] Optic Neuritis
- [ ] Acute Flaccid Myelitis (AFM)
- [ ] Neuropsychiatric SLE
- [ ] Autoimmune Autonomic Ganglionopathy
- [ ] Paraneoplastic Neurological Syndromes

## Existing Diseases to Review/Enhance (0/7)
- [ ] Multiple Sclerosis - check compliance
- [ ] Guillain-Barré Syndrome - add treatment evidence
- [ ] CIDP - add treatment evidence
- [ ] Myasthenia Gravis - verify compliance
- [ ] Stiff Person Syndrome - complete (100%)
- [ ] Narcolepsy - verify compliance
- [ ] ME/CFS - verify compliance

# NOTES

## 2026-01-06

**NMOSD curated (first disease complete)**:
- Created `kb/disorders/Neuromyelitis_Optica_Spectrum_Disorder.yaml`
- Deep research via falcon provider
- 70.6% compliance achieved
- Key evidence from:
  - PMID:26092914 - International diagnostic criteria (2015)
  - PMID:35454180 - AQP4 pathophysiology review
  - PMID:31050279 - Eculizumab PREVENT trial
  - PMID:31495497 - Inebilizumab N-MOmentum trial
  - PMID:36933107 - Satralizumab review
  - PMID:33420337 - HLA-DRB1*03:01 association meta-analysis
- Ontology terms: CL (astrocyte, neutrophil, eosinophil, oligodendrocyte), GO (complement activation), HP (optic neuritis, nausea/vomiting), MAXO (pharmacotherapy)
- Three approved targeted therapies documented: eculizumab (C5 inhibitor), inebilizumab (anti-CD19), satralizumab (IL-6R blocker)

Project initiated. Identified 7 existing neuroimmune diseases in KB:
- Multiple Sclerosis, Guillain-Barré Syndrome, CIDP, Myasthenia Gravis - classic autoimmune
- Stiff Person Syndrome - rare but well-curated (100% compliance)
- Narcolepsy - increasingly recognized autoimmune (hypocretin neuron loss)
- ME/CFS - immune dysfunction with neuroinflammation

Identified 15 candidate diseases to add, prioritized by:
1. CNS demyelinating (NMOSD, MOGAD, ADEM, TM) - closely related to MS
2. Autoimmune encephalitis (Anti-NMDAR, Limbic, Hashimoto) - emerging field
3. CNS inflammatory (Vasculitis, Neurosarcoidosis, Susac) - important differentials
4. Other neuroimmune conditions - paraneoplastic, autonomic, etc.

Key distinguishing features:
- NMOSD vs MS: AQP4 antibodies, longitudinally extensive TM, severe optic neuritis
- MOGAD: distinct from both MS and NMOSD, better prognosis
- Anti-NMDAR encephalitis: often associated with ovarian teratoma, good response to immunotherapy
