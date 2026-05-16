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
| Acute Disseminated Encephalomyelitis (ADEM) | Acute_Disseminated_Encephalomyelitis.yaml | [x] Curated | Post-infectious CNS demyelination, mainly children |
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
| CNS Vasculitis | CNS_Vasculitis.yaml | [x] Curated - 95.7% compliance | Primary angiitis of the CNS |
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

## New Diseases to Curate (4/15)
- [x] Neuromyelitis Optica Spectrum Disorder (NMOSD) - 70.6% compliance
- [x] MOG Antibody Disease (MOGAD) - 91.9% compliance
- [x] Acute Disseminated Encephalomyelitis (ADEM) - 94.6% weighted compliance
- [x] Transverse Myelitis - 100.0% weighted compliance
- [x] Anti-NMDA Receptor Encephalitis - 100.0% weighted compliance
- [ ] Limbic Encephalitis
- [ ] Hashimoto Encephalopathy (SREAT)
- [x] CNS Vasculitis - 95.7% compliance
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

## 2026-05-16

**CNS Vasculitis curated**:
- Created `kb/disorders/CNS_Vasculitis.yaml` focused on primary angiitis of the CNS / PCNSV
- Deep research completed with Falcon and OpenScientist providers
- 95.7% weighted compliance achieved
- MONDO and Orphanet grounding: `MONDO:0015374` and `ORPHA:140989`
- Key evidence from:
  - ORPHA:140989 - rare-disease definition, incidence band, and HPO phenotype frequencies
  - PMID:3275856 - classic Calabrese-Mallek diagnostic criteria
  - PMID:17924545, PMID:26020379, PMID:25708615, and PMID:32062032 - Mayo incidence, subtypes, outcomes, relapse, and maintenance therapy
  - DOI:10.1177/23969873231190431 - ESO 2023 PACNS guideline
  - PMID:36264136 - PCNSV brain transcriptomic immune activation
  - PMID:40546217 - 2025 multicenter German outcome and cyclophosphamide relapse data
  - PMID:40643487 - serum and CSF neurofilament light chain biomarker study
- ClinicalTrials.gov entries documented for vessel-wall MRI, ferumoxytol MRI in CNS inflammation, and refractory non-ANCA vasculitis biologics
- Ontology terms: MONDO/ORPHA disease IDs, UBERON CNS vascular anatomy, CL immune-cell subsets, GO inflammatory and antigen-presentation processes, HPO neurologic/CSF/MRI phenotypes, MAXO diagnosis/treatment terms

**Transverse Myelitis enhanced/reviewed**:
- Enhanced existing `kb/disorders/Transverse_Myelitis.yaml`
- Falcon, Perplexity, and Cyberian research artifacts were already present; OpenScientist was attempted for the required second provider pass but produced no artifact after ~20 minutes and was terminated as hung
- 100.0% weighted compliance achieved after adding subtype grounding, progression, LETM/spinal movement/back pain/spasticity phenotypes, serum NfL/GFAP biomarkers, COVID-associated outcome evidence, CSF inflammatory marker recurrence evidence, IVIG clinical-trial metadata, and NCIT treatment grounding for plasmapheresis/IVIG
- Checked MONDO and Orphanet context: MONDO:0021553 lacks direct Orphanet xrefs, but MONDO acute/idiopathic/MOG-IgG acute TM subtype terms map to ORPHA:139417, ORPHA:139423, and ORPHA:592873; local Orphadata XML is absent, so ORPHA caches could not be regenerated for direct YAML evidence
- Key evidence from:
  - PMID:12045735 - immunopathogenesis and focal spinal cord inflammation
  - PMID:32644728 - 2025 StatPearls clinical presentation and outcome summary
  - PMID:25340060 - recurrence risk after initial transverse myelitis
  - PMID:23999580 - LETM AQP4-IgG cohort and differential diagnosis context
  - PMID:38977461 - 2024 prospective spinal movement disorders cohort
  - PMID:34171586, PMID:26351447, PMID:29270309, and PMID:35246251 - back pain and spasticity phenotype coverage added during review
  - PMID:36894677 and PMID:37688927 - serum NfL/GFAP biomarker studies in idiopathic and seropositive transverse myelitis
  - PMID:41349230 - 2026 post-COVID-19 infection/vaccination TM outcomes and imaging comparison
  - PMID:42003147 - 2026 retrospective TM outcomes cohort
  - PMID:26009577 and NCT02398994 - STRIVE IVIG trial protocol and registration
- Ontology terms: MONDO (acute, idiopathic, MOG-IgG acute TM), HP (myelitis with EXTENSIVE spatial qualifier, back pain, spasticity, tonic spasms, focal dystonia), CL (monocyte), GO (humoral immune response), NCIT (plasmapheresis, IVIG therapy)

**Anti-NMDA receptor encephalitis curated**:
- Created `kb/disorders/Anti-NMDA_Receptor_Encephalitis.yaml`
- Deep research via falcon provider; Asta retrieval run added as a second literature pass
- 99.4% global compliance and 100.0% weighted compliance achieved
- Modeled teratoma-associated and post-herpes simplex encephalitis subtypes, Graus-style clinical criteria, racial/ethnic and geographic incidence variation, CSF anti-GluN1/NMDAR IgG biomarkers, NEOS prognostic variables, relapse/recovery trajectory, first-line immunotherapy, second-line rituximab/cyclophosphamide, plasma exchange, IVIG, corticosteroids, and tumor removal
- Key evidence from:
  - PMID:18851928 - original case series and antibody effects on synaptic NMDAR clusters
  - PMID:23290630 - 577-patient treatment/outcome cohort
  - PMID:26906964 and PMID:28972277 - autoimmune encephalitis and anti-NMDAR diagnostic criteria
  - PMID:31326280 - Lancet Neurology mechanism and clinical update
  - PMID:31619447 and PMID:33589542 - large Chinese longitudinal cohorts for phenotypes, treatment, outcomes, and relapse
  - PMID:30578370 - NEOS score prognostic predictors
  - PMID:37371620 and PMID:38728608 - geographic/climatic and US race/ethnicity incidence studies
  - PMID:38145121 - blood-brain barrier and anti-NMDAR antibody review
  - PMID:39147951 - post-herpes simplex encephalitis anti-NMDAR encephalitis cohort
  - PMID:39566012 - long-term cognitive, functional, and patient-reported outcomes
- ClinicalTrials.gov entries documented for immunoadsorption therapy, prolonged recovery-stage biomarkers/rehabilitation, and NEOSII prediction modeling
- Ontology terms: MONDO (anti-NMDA receptor encephalitis), CL (B cell, plasma cell, neuron), GO (B cell mediated immunity, immunoglobulin production, receptor internalization, glutamate receptor signaling, synaptic plasticity, blood-brain barrier maintenance), HP (psychosis, seizure, dyskinesia, memory impairment, coma, autonomic dysfunction, hypoventilation, EEG abnormality, CSF pleocytosis), UBERON (brain, hippocampal formation, blood-brain barrier), MAXO/NCIT/CHEBI treatment terms

**MOGAD curated**:
- Created `kb/disorders/MOGAD.yaml`
- Deep research via falcon provider; OpenScientist provider run added for second-pass literature review
- 91.9% weighted compliance achieved
- Local Orphanet cache, current Orphanet web search, and MONDO cross-reference check found no ORPHA disease mapping for `MONDO:1040024`; Orphanet diagnostic-test listings currently point to acute disseminated encephalomyelitis with anti-MOG antibodies rather than a MOGAD disease entry
- Key evidence from:
  - PMID:36706773 - International MOGAD Panel diagnostic criteria
  - PMID:34418402 - Lancet Neurology clinical/pathogenesis review
  - PMID:40088708 - 2025 pathogenesis and biomarker review
  - PMID:29695592 - MOGADOR adult cohort relapse and phenotype data
  - PMID:32048003 and PMID:32412053 - MOGAD neuropathology, histopathology, and immunopathology
  - PMID:32629363 - International rituximab treatment cohort
  - PMID:34634625 and PMID:35377395 - maintenance IVIG meta-analysis and adult cohort
  - PMID:40708693 - Current treatment principles review
  - PMID:41657079 and PMID:41865559 - South Wales and Denmark epidemiology
- ClinicalTrials.gov entries documented for satralizumab, rozanolixizumab, azathioprine, and tocilizumab MOGAD trials
- Ontology terms: MONDO (MOGAD), CL (oligodendrocyte, T cell), GO (complement activation, ADCC, myelination), HP (optic neuritis, myelitis, CNS demyelination, spinal cord lesion), MAXO/NCIT/CHEBI treatment terms

**Acute Disseminated Encephalomyelitis curated**:
- Created `kb/disorders/Acute_Disseminated_Encephalomyelitis.yaml`
- Reviewed MONDO/Orphanet context: MONDO:0019383, Orphanet:83597
- Documented IPMSSG-style clinical definition, monophasic/multiphasic/MOG-IgG-associated subtypes, pediatric incidence, adult outcome burden, postinfectious autoimmunity, blood-brain barrier disruption, molecular mimicry, perivenous demyelination, MOG-IgG/complement mechanisms, clinical phenotypes, CSF findings, acute immunotherapies, and active/relevant clinical trials
- Added evidence from contemporary reviews, pediatric and adult cohorts, pathology studies, MOG-IgG relapse-risk data, and ClinicalTrials.gov records
- Achieved 94.6% weighted compliance

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
