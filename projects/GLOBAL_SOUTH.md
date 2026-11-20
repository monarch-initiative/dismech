---
title: "Global South Disease Burden: Pathograph Depth"
status: IN_PROGRESS
description: Bring the 64 knowledge-base entries that carry most of the disease burden in low- and middle-income countries up to a usable pathograph standard. The entries all exist; their causal graphs are thin, and five have no causal edges at all. This project tracks depth rather than coverage.
tags:
- INFECTIOUS_DISEASE
- IMMUNOLOGY
- TOXICOLOGY
- VACCINES
diseases:
- Acquired_Immunodeficiency_Syndrome
- Aflatoxicosis
- Aflatoxin_Related_HCC
- Alpha_Thalassemia
- Anthrax
- Arsenic_Poisoning
- Arsenic_Related_Cancers
- Beta_Thalassemia
- Bubonic_Plague
- Buruli_Ulcer
- Chagas_Disease
- Chikungunya
- Cholera
- Congenital_Zika_Syndrome
- Cryptococcal_Meningitis
- Cystic_Echinococcosis
- Dengue
- Diphtheria
- Dracunculiasis
- Ebola_Virus_Disease_EVD
- Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency
- Hepatitis_B
- Human_African_Trypanosomiasis
- Invasive_Non-Typhoidal_Salmonellosis
- Konzo
- Lassa_Fever
- Lead_Poisoning
- Leishmaniasis
- Leprosy
- Leptospirosis
- Lymphatic_Filariasis
- Malaria
- Measles
- Melioidosis
- Meningeal_Tuberculosis
- Mycetoma
- Noma
- Nontuberculous_Mycobacterial_Lung_Disease
- Onchocerciasis
- Organophosphate_Poisoning
- Paralytic_Poliomyelitis
- Paratyphoid_Fever
- Pertussis
- Plague
- Podoconiosis
- Polycystic_Echinococcosis
- Rabies
- Rheumatic_Heart_Disease
- Rotaviral_Enteritis
- Scabies
- Schistosomiasis
- Scrub_Typhus
- Sickle_Cell_Disease
- Silicosis
- Snakebite_Envenoming
- Soil_Transmitted_Helminthiases
- Taeniasis_Cysticercosis
- Tetanus
- Tetanus_Neonatorum
- Trachoma
- Tuberculosis
- Typhoid_Fever
- Yaws
- Yellow_Fever
---

# Global South Disease Burden: Pathograph Depth

> **GitHub Epic**: https://github.com/monarch-initiative/dismech/issues/16706

## Why this project exists

Every one of the 64 diseases below already has an entry, so coverage is not the problem. Depth is. Together these entries hold 487 mechanism nodes and 726 causal edges, but five have mechanism nodes and **no causal edges at all**, 18 have no phenotype connected to any mechanism, and 28 render as more than one disconnected component. Across the set, 320 of 580 phenotypes (55%) are explained by an edge.

Nothing in the validation stack measures this. An entry whose nodes were never joined up passes `just validate`, `just validate-terms` and `just validate-disorders`, and scores high on `just compliance`, which counts filled slots rather than connected mechanism. That blind spot is tracked separately in #7855, #9789 and #16699; this project is the content work.

## Relationship to the other projects

[NTD](NTD.md) owns the WHO list and tracks whether each disease **has an entry** — on that measure it is complete, 20 of 20. This project asks a different question of 22 of those same diseases, plus 42 more, and the answers differ: Trachoma, Lymphatic filariasis and Polycystic echinococcosis are all ticked off in NTD and all have zero causal edges. [VACCINES](VACCINES.md) overlaps on the vaccine-preventable entries and owns the `target_mechanisms` wiring there.

## Scope

| Group | Entries | What it covers |
|---|--:|---|
| Other high-burden infection | 25 | high-burden infections outside the NTD list, including the vaccine-preventable childhood diseases |
| WHO NTD | 22 | the WHO neglected tropical disease list |
| Poverty / environmental | 9 | non-infectious diseases of poverty, where the exposure is the intervention point |
| Big three | 4 | malaria, tuberculosis, HIV/AIDS |
| Host genetic / malaria-linked | 4 | host-genetic conditions shaped by malaria selection |

## Status by tier

Tiers come from a structural audit: mechanism nodes, causal edges, nodes with no edge in or out, connected components, phenotype inlinks, ontology bindings, treatment wiring, and `just check-granularity`.

**The tables are a snapshot taken on 2026-11-06 and will go stale as the issues below close.** Nothing regenerates them, so treat a figure here as the state when the audit ran, not as current. Each column can be recomputed per entry:

| Column | Where it comes from |
|---|---|
| Nodes, Edges | `pathophysiology[]` and its `downstream[].target` entries |
| Floating | nodes with no edge in or out; no recipe reports these yet, which is #7855 |
| Phenotypes wired | `just list-disconnected-phenotypes kb/disorders/<Entry>.yaml` |
| Main gaps | `just check-granularity kb/disorders/<Entry>.yaml`, plus the graph columns above |

### Tier 1 — no usable pathograph (5)

| Disease | Nodes | Edges | Floating | Phenotypes wired | Issue |
|---|--:|--:|--:|--:|---|
| Lymphatic Filariasis | 4 | 0 | 4 | 0/4 | #16712 |
| Polycystic Echinococcosis | 3 | 0 | 3 | 0/3 | #16713 |
| Trachoma | 1 | 0 | 1 | 0/1 | #16714 |
| Ebola Virus Disease EVD | 5 | 0 | 5 | 0/18 | #16715 |
| Tetanus | 3 | 0 | 3 | 0/6 | #16716 |

### Tier 2 — broken or badly incomplete (12)

| Disease | Nodes | Edges | Floating | Phenotypes wired | Issue |
|---|--:|--:|--:|--:|---|
| Mycetoma | 4 | 2 | 1 | 0/8 | #16718 |
| Plague | 8 | 6 | 1 | 0/10 | #16719 |
| Dracunculiasis | 4 | 7 | 1 | 7/7 | #16720 |
| Tuberculosis | 8 | 6 | 1 | 0/10 | #16721 |
| Schistosomiasis | 5 | 3 | 2 | 1/6 | #16722 |
| Noma | 2 | 1 | 0 | 0/10 | #16723 |
| Buruli Ulcer | 2 | 1 | 1 | 1/1 | #16724 |
| Paratyphoid Fever | 6 | 5 | 1 | 0/6 | #16725 |
| Konzo | 4 | 3 | 0 | 0/6 | #16726 |
| Measles | 6 | 5 | 1 | 1/9 | #16727 |
| Malaria | 13 | 10 | 4 | 3/10 | #16728 |
| Paralytic Poliomyelitis | 6 | 5 | 0 | 0/8 | #16729 |

### Tier 3 — works, gaps around it (24)

| Disease | Nodes | Edges | Floating | Phenotypes wired | Issue |
|---|--:|--:|--:|--:|---|
| Congenital Zika Syndrome | 12 | 13 | 0 | 0/15 | #16730 |
| Leptospirosis | 21 | 25 | 2 | 6/16 | #16731 |
| Soil Transmitted Helminthiases | 5 | 5 | 1 | 3/4 | #16732 |
| Cholera | 9 | 5 | 3 | 1/12 | #16733 |
| Invasive Non-Typhoidal Salmonellosis | 7 | 11 | 2 | 7/8 | #16734 |
| Onchocerciasis | 4 | 12 | 0 | 8/8 | #16735 |
| Hepatitis B | 8 | 18 | 1 | 10/10 | #16736 |
| Human African Trypanosomiasis | 2 | 2 | 0 | 1/1 | #16737 |
| Rabies | 11 | 11 | 0 | 0/12 | #16738 |
| Pertussis | 7 | 6 | 0 | 0/7 | #16739 |
| Scrub Typhus | 13 | 13 | 0 | 0/25 | #16740 |
| Yaws | 7 | 20 | 1 | 16/16 | #16741 |
| Podoconiosis | 13 | 14 | 0 | 0/5 | #16742 |
| Silicosis | 9 | 11 | 0 | 0/9 | #16743 |
| Cystic Echinococcosis | 5 | 9 | 0 | 5/5 | #16744 |
| Taeniasis Cysticercosis | 4 | 7 | 0 | 4/4 | #16745 |
| Dengue | 12 | 7 | 6 | 3/5 | #16746 |
| Cryptococcal Meningitis | 7 | 7 | 2 | 3/5 | #16747 |
| Leprosy | 12 | 7 | 6 | 4/5 | #16748 |
| Melioidosis | 10 | 18 | 2 | 12/12 | #16749 |
| Typhoid Fever | 9 | 17 | 2 | 9/9 | #16750 |
| Beta Thalassemia | 6 | 23 | 0 | 18/18 | #16751 |
| Diphtheria | 16 | 15 | 0 | 1/22 | #16752 |
| Lassa Fever | 7 | 22 | 0 | 15/15 | #16753 |

### Tier 4 — minor, tracked in the epic (13)

Alpha Thalassemia, Anthrax, Bubonic Plague, Chikungunya, Glucose-6-Phosphate Dehydrogenase G6PD Deficiency, Lead Poisoning, Leishmaniasis, Nontuberculous Mycobacterial Lung Disease, Organophosphate Poisoning, Scabies, Sickle Cell Disease, Snakebite Envenoming, Yellow Fever.

### Tier 5 — no findings (10)

Acquired Immunodeficiency Syndrome, Aflatoxicosis, Aflatoxin Related HCC, Arsenic Poisoning, Arsenic Related Cancers, Chagas Disease, Meningeal Tuberculosis, Rheumatic Heart Disease, Rotaviral Enteritis, Tetanus Neonatorum.

`Chagas_Disease` is the model for an infectious entry: 6 mechanism nodes, 13 edges, nothing floating, 8 of 9 phenotypes explained, and one intracellular node branching to both the cardiac and the enteric syndrome.

## Order of work

1. Tier 1, because an entry with no edges renders as a row of disconnected boxes.
2. The 18 entries where no phenotype is wired, which is what makes a page read as two unrelated lists.
3. Tier 2 floating nodes and missing stages.
4. Tier 3, mostly ontology bindings and treatment links.

## Curation standard for this project

- Every new causal edge carries its own evidence with an exact-quote snippet. An edge added to clear a report is worse than no edge.
- A phenotype may legitimately stay unconnected when its mechanism is genuinely unknown or it is a laboratory readout. Say so in `notes:` rather than inventing an edge.
- A bare `downstream` target must match a `pathophysiology` or `phenotypes` name exactly. A subtype name does not resolve and renders as a phantom node.
- Each entry gets a `history/` record with its PR.

```bash
just list-disconnected-phenotypes kb/disorders/<Entry>.yaml
just check-causal-targets kb/disorders/<Entry>.yaml
just check-granularity kb/disorders/<Entry>.yaml
just validate-disorders kb/disorders/<Entry>.yaml
```

# NOTES

## 2026-11-06
- Project created from a structural audit of all 64 entries. Epic #16706 opened with per-disease issues #16712-#16753 for tiers 1-3.
- The audit found the same blind spot twice: the NTD project marks a disease complete when an entry exists, and `just compliance` scores an entry on filled slots. Trachoma satisfies both and has one node and no edges.
