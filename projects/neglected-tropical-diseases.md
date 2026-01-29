# Neglected Tropical Diseases Curation Project

## Overview
Curate the WHO-recognized neglected tropical diseases (NTDs) in the Disorder Mechanisms Knowledge Base, with emphasis on pathogen life cycles, transmission routes, immune evasion, and chronic morbidity mechanisms. The current WHO list includes 21 diseases or disease groups, which maps to 22 KB files when splitting the dengue/chikungunya group.

## Goals
- Create or enhance NTD YAML files in `kb/disorders/`
- Capture vector/reservoir/host interactions
- Annotate phenotypes with HPO terms and treatments with MAXO terms
- Provide PMID-supported evidence for core mechanisms

## Existing NTD Entries in KB (2)
| Disease | File | Status |
|---------|------|--------|
| Dengue | Dengue.yaml | Exists |
| Echinococcosis (polycystic) | Polycystic_Echinococcosis.yaml | Exists |

## NTDs to Curate (WHO List, 21 groups)
The WHO list below is used as the project scope. Some WHO groups are split into multiple files for clarity (e.g., dengue + chikungunya).

### Bacterial NTDs
| Disease | Planned File | Notes | Status |
|---------|--------------|-------|--------|
| Buruli ulcer | Buruli_Ulcer.yaml | Mycobacterium ulcerans | [x] |
| Leprosy (Hansen's disease) | Leprosy.yaml | M. leprae/ lepromatosis | [x] |
| Trachoma | Trachoma.yaml | Chlamydia trachomatis | [x] |
| Noma (cancrum oris) | Noma.yaml | Added to WHO list in 2023 | [x] |
| Yaws and other endemic treponematoses | Yaws.yaml | Bejel.yaml and Pinta.yaml added | [x] |

### Protozoal NTDs
| Disease | Planned File | Notes | Status |
|---------|--------------|-------|--------|
| Chagas disease | Chagas_Disease.yaml | Trypanosoma cruzi | [x] |
| Human African trypanosomiasis | Human_African_Trypanosomiasis.yaml | T. brucei; stage 1/2 | [x] |
| Leishmaniasis | Leishmaniasis.yaml | Visceral/cutaneous/mucosal | [x] |

### Viral NTDs
| Disease | Planned File | Notes | Status |
|---------|--------------|-------|--------|
| Dengue | Dengue.yaml | Existing | [x] |
| Chikungunya | Chikungunya.yaml | Often paired with dengue in WHO list | [x] |
| Rabies | Rabies.yaml | Neurotropic lyssavirus | [x] |

### Helminth NTDs
| Disease/Group | Planned File | Notes | Status |
|---------------|--------------|-------|--------|
| Dracunculiasis (Guinea-worm disease) | Dracunculiasis.yaml | Eradication focus | [x] |
| Lymphatic filariasis | Lymphatic_Filariasis.yaml | Wuchereria/Brugia | [x] |
| Onchocerciasis (river blindness) | Onchocerciasis.yaml | O. volvulus | [x] |
| Schistosomiasis | Schistosomiasis.yaml | S. haematobium/mansoni/japonicum | [x] |
| Soil-transmitted helminthiases | Soil_Transmitted_Helminthiases.yaml | Ascaris, Trichuris, hookworm | [x] |
| Foodborne trematodiases | Foodborne_Trematodiases.yaml | Clonorchis, Opisthorchis, Fasciola, Paragonimus | [x] |
| Taeniasis/cysticercosis | Taeniasis_Cysticercosis.yaml | Taenia solium | [x] |
| Echinococcosis | Cystic_Echinococcosis.yaml | Cystic form added; polycystic file exists | [x] |

### Fungal NTDs
| Disease/Group | Planned File | Notes | Status |
|---------------|--------------|-------|--------|
| Mycetoma, chromoblastomycosis and other deep mycoses | Mycetoma.yaml | Chromoblastomycosis.yaml added | [x] |

### Ectoparasites, Other, and Envenoming
| Disease/Group | Planned File | Notes | Status |
|---------------|--------------|-------|--------|
| Scabies and other ectoparasitoses | Scabies.yaml | Consider Tungiasis.yaml | [x] |
| Snakebite envenoming | Snakebite_Envenoming.yaml | Toxin-mediated | [x] |

## Cross-Cutting Mechanisms to Capture
1. **Vector biology**: insect/arthropod vectors, seasonality, geographic range
2. **Reservoirs**: zoonotic cycles, domestic/wild animal hosts
3. **Immune evasion**: antigenic variation, intracellular persistence, Th1/Th2 skewing
4. **Chronic inflammation**: granulomas, fibrosis, lymphatic damage, neuroinvasion
5. **Tissue tropism**: skin, CNS, liver, lymphatics, eye, bone
6. **Coinfections and comorbidity**: HIV, malnutrition, helminth co-burden
7. **Public health interfaces**: WASH, mass drug administration, vector control

## Suggested Curation Order
1. **High-burden, high-impact**: dengue, schistosomiasis, soil-transmitted helminthiases, lymphatic filariasis
2. **Vector-borne protozoa**: leishmaniasis, Chagas, HAT
3. **Skin NTDs**: leprosy, Buruli ulcer, yaws, scabies, mycetoma/chromoblastomycosis
4. **Zoonotic and toxin-mediated**: rabies, echinococcosis, snakebite
5. **Elimination targets**: dracunculiasis, trachoma

---

# STATUS

## New NTD Disease Files (20/20)
- [x] Buruli ulcer
- [x] Chagas disease
- [x] Chikungunya
- [x] Dracunculiasis
- [x] Foodborne trematodiases
- [x] Human African trypanosomiasis
- [x] Leishmaniasis
- [x] Leprosy
- [x] Lymphatic filariasis
- [x] Mycetoma / chromoblastomycosis
- [x] Noma
- [x] Onchocerciasis
- [x] Rabies
- [x] Scabies and other ectoparasitoses
- [x] Schistosomiasis
- [x] Snakebite envenoming
- [x] Soil-transmitted helminthiases
- [x] Taeniasis/cysticercosis
- [x] Trachoma
- [x] Yaws and other endemic treponematoses

## Existing NTD Diseases (2/2)
- [x] Dengue
- [x] Echinococcosis (polycystic file exists; cystic form added)

# NOTES

## 2026-01-26
- Added Schistosomiasis.yaml with PMID-supported evidence for transmission, granulomatous pathology, and praziquantel treatment.
- Added Lymphatic_Filariasis.yaml with OPL life-cycle stages and PMID evidence for mosquito transmission, lymphatic pathology, and MDA treatments.
- Added Leishmaniasis.yaml with OPL life-cycle stages, sand fly transmission, and clinical form subtypes.
- Added Chagas_Disease.yaml with OPL life-cycle stages, triatomine transmission, and cardiomyopathy evidence.
- Added Human_African_Trypanosomiasis.yaml with OPL life-cycle stages, tsetse transmission, and staged CNS involvement.
- Added Soil_Transmitted_Helminthiases.yaml with species coverage, helminth transmission, and deworming treatments.
- Added Onchocerciasis.yaml with black fly transmission, pruritus/ocular disease, and ivermectin therapy.
- Added Chikungunya.yaml with Aedes transmission, fever/arthralgia phenotypes, and symptomatic care.
- Added Taeniasis_Cysticercosis.yaml with Taenia solium lifecycle context and neurocysticercosis seizure evidence.
- Added Rabies.yaml with lyssavirus etiology, bite transmission, and post-exposure prophylaxis.
- Added Buruli_Ulcer.yaml with mycolactone-mediated tissue destruction and antimicrobial/surgical treatment notes.
- Added Dracunculiasis.yaml with waterborne copepod transmission and Dracunculus medinensis etiology.
- Added Trachoma.yaml with conjunctival C. trachomatis infection, scarring, and SAFE strategy antibiotic MDA.
- Refreshed Dengue.yaml with updated MONDO term, Aedes vector transmission, and severe plasma leakage pathophysiology.
- Added Leprosy.yaml with M. leprae etiology, nasal droplet transmission, neuropathy, and multidrug therapy evidence.
- Added Scabies.yaml with Sarcoptes scabiei etiology, contact transmission, pruritus/lesions, and first-line therapy evidence.
- Added Snakebite_Envenoming.yaml with venom toxicity, clinical features, and antivenom treatment evidence.
- Added Foodborne_Trematodiases.yaml with major liver, lung, and intestinal fluke agents and food-borne transmission evidence.
- Added Mycetoma.yaml with fungal/bacterial etiologies and classic subcutaneous swelling evidence.
- Added Noma.yaml with polymicrobial necrotizing pathology and gangrenous phenotype evidence.
- Added Yaws.yaml with T. pallidum subsp. pertenue etiology, direct-contact transmission, ulcers, and azithromycin therapy evidence.
- Added Cystic_Echinococcosis.yaml with E. granulosus etiology, dog-associated transmission, hepatic cysts, and benzimidazole/surgical treatments.
- Added Chromoblastomycosis.yaml with common etiologic agents, traumatic inoculation, and verrucous lesion phenotypes.
- Added Bejel.yaml with T. pallidum subsp. endemicum etiology evidence.
- Added Pinta.yaml with T. carateum etiology evidence.

## 2026-01-25
- Project initialized using WHO's current NTD list (21 diseases/groups).
