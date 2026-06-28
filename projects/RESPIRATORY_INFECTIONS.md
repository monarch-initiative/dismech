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

High-value respiratory infections **not yet in the KB**, roughly priority-ordered:

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

**Other viral**
- MERS-CoV
- Parainfluenza virus infection
- Human metapneumovirus infection
- Adenovirus respiratory infection

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
5. Add the new slug to the `diseases:` frontmatter list here.

## Related

- [`ANTIMICROBIAL`](ANTIMICROBIAL.md), [`ANTIVIRAL`](ANTIVIRAL.md), [`ANTIFUNGAL`](ANTIFUNGAL.md) — treatment-mechanism layer.
- [`COMORBIDITIES`](COMORBIDITIES.md) — respiratory-infection comorbidity/trajectory signals (e.g. RSV → asthma, influenza → bacterial superinfection).
