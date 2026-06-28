---
title: Respiratory Infections Curation Project
status: PLANNED
description: >-
  Anatomy/syndrome-oriented curation of infections of the respiratory tract
  (upper and lower), complementing the drug-mechanism-oriented ANTIMICROBIAL,
  ANTIVIRAL, and ANTIFUNGAL projects. Seeds the existing respiratory-infection
  entries and tracks the major coverage gaps (bacterial pneumonia, atypical
  pneumonias, pertussis, fungal pneumonias, croup, sinusitis/pharyngitis).
tags: [DISEASE_DOMAIN, INFECTIOUS_DISEASE, RESPIRATORY]
diseases:
- Influenza
- COVID-19
- Long_COVID
- Respiratory_Syncytial_Virus_Infection
- Rhinovirus_Infection
- Tuberculosis
- Coccidioidomycosis
- Hantavirus_Pulmonary_Syndrome
- Pontiac_Fever
- Plague
- Tularemia
- Glanders
- Scarlet_Fever
- Chickenpox
- Bronchiectasis
---

# Respiratory Infections Curation Project

## Overview

This project organizes dismech curation of **infections of the respiratory
tract** — by anatomical site and clinical syndrome rather than by drug class.
It is the disease-domain complement to the three drug-mechanism projects:

- [`ANTIMICROBIAL`](ANTIMICROBIAL.md) — antibacterial drug–bug mechanism modules
- [`ANTIVIRAL`](ANTIVIRAL.md) — antiviral drug–virus mechanism modules
- [`ANTIFUNGAL`](ANTIFUNGAL.md) — antifungal mechanism modules

Where those projects ask "how does the drug work against the pathogen," this
project asks "what is the pathophysiology of infection at this site, in this
host." A respiratory-infection entry should still `conforms_to` the relevant
drug-mechanism module(s) for its treatments; this project tracks the *clinical
entities* and their coverage, and the drug-mechanism projects track the
treatment wiring.

## Funding alignment: the Intercept initiative

[Intercept](https://www.interceptfund.com/) is a $500M philanthropic fund whose
stated goal is to *radically reduce and ultimately eliminate endemic respiratory
infections* — pushing the effective reproduction number below 1 for viruses with
R₀ < 3. Its scientific thesis directly shapes the priorities of this project.

Intercept's **four core target viruses are all already curated in dismech** and
seeded above: Influenza, COVID-19 (SARS-CoV-2), Respiratory_Syncytial_Virus_Infection,
and Rhinovirus_Infection. So Intercept-aligned work here is primarily about
**deepening mechanism and treatment coverage**, not creating the core entries.

Intercept funds two product classes:

1. **Broad-Spectrum Preventatives (BSPs)** across five mechanistic tracks:
   - *Adaptive immunity* — universal vaccines, broadly-neutralizing antibodies,
     tissue-resident CD8 T cells (dismech: `VACCINE` / `MONOCLONAL_ANTIBODY` modalities)
   - *Direct-acting antivirals* — siRNA, broad-spectrum RdRp inhibitors, mAbs,
     receptor decoys (dismech: existing `viral_polymerase_inhibition`,
     `viral_entry_fusion_inhibition` modules)
   - *Innate-immunity modulators* — engineered interferon, cGAS/RIG-I agonists
     (**module gap** — see below)
   - *Host-directed antivirals* — targeting host dependency factors
     (**module gap** — see below)
   - *Physical-barrier formulations* — lectin/mucin nasal sprays (a treatment modality)
2. **Air Cleaning Technologies** (far-UVC, filtration, antimicrobial vapors) —
   environmental interventions, **out of dismech's disease-mechanism scope**.

### Intercept-aligned module gaps

dismech already has seven *direct-acting* antiviral mechanism modules (polymerase,
protease, entry/fusion, integrase, assembly/release, latency, PARP-macrodomain).
Two of Intercept's BSP tracks have **no module yet** and are genuinely conserved
cross-virus mechanisms worth a `kb/modules/` design pattern:

- **`host_directed_antiviral_dependency`** (proposed) — host dependency factors a
  virus requires (ACE2/TMPRSS2 for SARS-CoV-2, sialic-acid receptors / α2,6-linkage
  for influenza, etc.). Target of the host-directed and receptor-decoy tracks; high
  broad-spectrum value because host factors are conserved where viral proteins are not.
- **`innate_antiviral_interferon_response`** (proposed) — type I/III interferon,
  cGAS-STING, and RIG-I/MDA5 signaling. Target of the innate-immunity-modulator track.

## Scope

**In scope:** infections whose primary disease is in the respiratory tract —
upper (rhinitis/common cold, pharyngitis, sinusitis, laryngitis, croup,
epiglottitis) and lower (bronchitis, bronchiolitis, pneumonia, empyema, lung
abscess, pulmonary TB and fungal pneumonias). Systemic or zoonotic infections
are in scope when a respiratory form is a principal manifestation (e.g.
pneumonic plague, pneumonic tularemia, pulmonary glanders, varicella
pneumonia), and post-acute respiratory sequelae (Long COVID).

**Out of scope (cross-referenced, not owned here):**
- Non-infectious airway/parenchymal disease — Asthma, COPD,
  Hypersensitivity_Pneumonitis / Bird_Fanciers_Lung, Hereditary_Pulmonary_Alveolar_Proteinosis,
  Pulmonary_Hemosiderosis (these are immune/structural, not infections).
- Structural/developmental lung disease — Congenital_Pulmonary_Airway_Malformation,
  Scimitar_Syndrome, Laryngotracheoesophageal_Cleft.
- Host susceptibility entries (immunodeficiencies, Primary Ciliary Dyskinesia,
  Cystic Fibrosis) that predispose to recurrent respiratory infection — these
  belong to their own domains but are relevant comorbidity links.

Bronchiectasis is included as a **boundary case**: it is a chronic suppurative
airway disease driven by a vicious cycle of infection and inflammation, often
post-infectious, and is the structural endpoint many of these infections feed
into.

## Existing entries (seed set)

### Viral
| Entry | Pathogen / note |
|---|---|
| Influenza | Influenza A/B; LRTI + URTI |
| COVID-19 | SARS-CoV-2 acute infection |
| Long_COVID | Post-acute SARS-CoV-2 sequelae |
| Respiratory_Syncytial_Virus_Infection | RSV bronchiolitis/pneumonia |
| Rhinovirus_Infection | Common cold (URTI) |
| Hantavirus_Pulmonary_Syndrome | Hantavirus (HPS) |
| Chickenpox | VZV; respiratory-droplet transmission, varicella pneumonia |

### Bacterial / mycobacterial
| Entry | Pathogen / note |
|---|---|
| Tuberculosis | *Mycobacterium tuberculosis*; pulmonary + extrapulmonary |
| Pontiac_Fever | *Legionella* (mild, self-limited febrile form) |
| Scarlet_Fever | Group A *Streptococcus* pharyngitis (URT portal) |
| Plague | *Yersinia pestis* — pneumonic form |
| Tularemia | *Francisella tularensis* — pneumonic form |
| Glanders | *Burkholderia mallei* — pulmonary nodular disease |

### Fungal
| Entry | Pathogen / note |
|---|---|
| Coccidioidomycosis | *Coccidioides* — pulmonary mycosis |

## Coverage gaps (curation backlog)

High-value respiratory infections **not yet in the KB**, roughly priority-ordered.
Items tagged **[Intercept]** broaden coverage of Intercept's endemic-respiratory-virus
thesis (broad-spectrum protection across viral families) and are prioritized accordingly.

**Endemic respiratory viruses [Intercept] — highest priority**
- Human metapneumovirus infection [Intercept]
- Parainfluenza virus infection [Intercept]
- Seasonal/endemic coronaviruses (229E, OC43, NL63, HKU1) [Intercept]
- Adenovirus respiratory infection [Intercept]
- MERS-CoV (pandemic-potential coronavirus) [Intercept]

**Bacterial pneumonia & atypicals**
- Community-acquired pneumonia / pneumococcal pneumonia (*Streptococcus pneumoniae*)
- Legionnaires' disease (*Legionella pneumophila* pneumonia — the severe sibling of Pontiac_Fever)
- *Mycoplasma pneumoniae* pneumonia (atypical)
- *Chlamydophila pneumoniae* / psittacosis (*C. psittaci*)
- *Haemophilus influenzae* and *Moraxella catarrhalis* LRTI
- Hospital-acquired / ventilator-associated pneumonia
- Q fever (*Coxiella burnetii*) pulmonary form

**Vaccine-preventable / classic URT & airway**
- Pertussis (whooping cough)
- Diphtheria
- Acute bacterial/viral bronchitis
- Acute sinusitis / rhinosinusitis
- Streptococcal pharyngitis (as an entity distinct from Scarlet_Fever)
- Croup (laryngotracheobronchitis), epiglottitis

**Fungal & opportunistic**
- *Pneumocystis jirovecii* pneumonia (PCP)
- Pulmonary aspergillosis
- Histoplasmosis
- Blastomycosis
- Pulmonary cryptococcosis

## Workflow

1. Pick a gap entry above (or claim via the priority dashboard / `/claim-disease`).
2. Curate with `/curate`, anchoring pathophysiology on the host–pathogen
   interaction at the respiratory site.
3. Wire treatments to the appropriate drug-mechanism module(s) via
   `target_mechanisms` / `conforms_to` (see ANTIMICROBIAL / ANTIVIRAL /
   ANTIFUNGAL).
4. Validate: `just validate`, `just validate-references`, `just validate-terms-file`.

### Intercept-aligned deepening track (core 4 already curated)

Beyond filling gaps, deepen the already-curated core viruses along Intercept's thesis:

- **Build the two proposed modules** (`host_directed_antiviral_dependency`,
  `innate_antiviral_interferon_response`) and add `conforms_to` edges from the
  core virus entries.
- **Enrich broad-spectrum-preventative treatments** on Influenza, COVID-19,
  Respiratory_Syncytial_Virus_Infection, and Rhinovirus_Infection — tag each with
  the right `therapeutic_modality` (`VACCINE`, `MONOCLONAL_ANTIBODY`, `SIRNA`,
  `SMALL_MOLECULE`) and wire via `target_mechanisms` (e.g. RSV nirsevimab + RSVpreF
  vaccine; influenza baloxavir cap-dependent-endonuclease inhibitor).
5. Add the new slug to the `diseases:` frontmatter list here.

## Related

- [`ANTIMICROBIAL`](ANTIMICROBIAL.md), [`ANTIVIRAL`](ANTIVIRAL.md), [`ANTIFUNGAL`](ANTIFUNGAL.md) — treatment-mechanism layer.
- [`COMORBIDITIES`](COMORBIDITIES.md) — respiratory-infection comorbidity/trajectory signals (e.g. RSV → asthma, influenza → bacterial superinfection).
