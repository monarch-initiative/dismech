# Microbial disease granularity review (2026-08-29)

**Question.** Cancer entries got a ratified granularity ladder in August 2026
(design decisions §3a, from `cancer-taxonomy-granularity-review-2026-08-28.md`).
Mendelian disease has one too (§3, issues #306/#7082). Infectious disease has
neither. This report reviews how the ~146 microbial entries currently in the KB
are split and lumped, identifies where the implicit practice is inconsistent,
and proposes a decision ladder for ratification.

**TL;DR.** The KB is splitting microbial disease along **six different axes at
once** — organism taxonomy, organ syndrome, clinical eponym, phase of infection,
transmission setting, and neoplastic sequela — with no recorded rule saying
which one wins. Most individual calls are defensible; the problem is that
nothing says *why*, so the same situation is resolved two different ways in
different parts of the KB. Concretely: `Legionella` is split by syndrome
(Legionnaires' disease / Pontiac fever) while `Neisseria`, `Streptococcus`,
`Haemophilus` and `Listeria` are lumped by syndrome into one
`Bacterial_meningitis` entry with no subtypes; Rocky Mountain spotted fever and
boutonneuse fever exist simultaneously as full standalone entries *and* as
subtypes of `Spotted_Fever_Rickettsiosis`, both carrying the same MONDO IDs; and
ten lumped entries anchor to a MONDO term far broader than the entry
(`Travelers_Diarrhea` → `MONDO:0001673` *diarrheal disease*). The single
exemplary artifact in the whole area is the `Treponematoses` grouping, which
does record its lump/split reasoning explicitly — and it is the **only one of 99
groupings** covering infectious disease.

---

## 1. What the KB does today

### 1.1 The set

| Set | Count |
|---|---|
| Disorder entries carrying an `infectious_agent:` block | **125** |
| Further entries whose etiology is a transmissible agent but which carry **no** `infectious_agent:` block | **≥21** |
| Total microbial entries (working figure) | **~146** |
| Groupings over any of them | **1** (`Treponematoses`) of 99 |
| Modules for infection biology | ~15 (`intracellular_pathogen_persistence`, `granuloma_formation`, `innate_antiviral_interferon_response`, the antibiotic/antiviral target modules, …) |
| Infectious stubs still queued | 40, **all** `entry_type: UNDECIDED` |

The 21+ entries missing `infectious_agent:` are not edge cases. They include
`COVID-19`, `Lyme_Disease`, `Pertussis`, `Legionnaires_Disease`, `Q_Fever`,
`Psittacosis`, `Middle_East_Respiratory_Syndrome`, `Paralytic_Poliomyelitis`,
`Congenital_Zika_Syndrome`, `Mycetoma`, `Noma`, `Dental_Caries`,
`Pelvic_Inflammatory_Disease` and all five pneumonia entries. Nine of them share
the parent strings `Bacterial Respiratory Infection` / `Viral Respiratory
Infection` / `Fungal Respiratory Infection` — a coherent curation tranche that
simply never populated the pathogen slot. **The causative organism is therefore
not machine-queryable for roughly one microbial entry in seven, including the
most-read entry in the KB.**

### 1.2 Six granularity axes, none declared

| Axis | Examples | Consistent? |
|---|---|---|
| **Organism** (1 species ↔ 1 disease) | `Cholera`, `Measles`, `Rabies`, `Tetanus`, `Buruli_Ulcer`, `Melioidosis`, `Trachoma` | yes — the stable core |
| **Organism genus/complex, lumped** | `Babesiosis` (5 taxa), `Brucellosis` (3), `Leptospirosis` (2), `Aspergillosis`, `Leishmaniasis`, `Human_African_Trypanosomiasis` (2 subspecies) | inconsistent — see §2.2 |
| **Organ syndrome across unrelated pathogens** | `Bacterial_meningitis` (4 taxa), `Infective_Endocarditis` (3), `Endophthalmitis` (4), `Folliculitis` (4), `Choroiditis` (4), `Chorioamnionitis` (6), `Travelers_Diarrhea` (8), `Viral_Encephalitis` (5), `Viral_Hemorrhagic_Fever` | inconsistent — see §2.1 |
| **Clinical eponym / syndrome from one organism** | `Legionnaires_Disease` vs `Pontiac_Fever`; `Hantavirus_HFRS` vs `Hantavirus_Pulmonary_Syndrome`; `Scarlet_Fever` vs `Toxic_Shock_Syndrome` | inconsistent — see §2.3 |
| **Phase of one infection** | `Acute_Hepatitis_C_Virus_Infection` vs `Hepatitis_C`; `Acquired_Immunodeficiency_Syndrome` with no HIV-infection entry; `Long_COVID` vs `COVID-19` | inconsistent — see §2.4 |
| **Infection-attributed neoplasm** | `Cervical_Cancer`, `HPV_Positive_Head_and_Neck_Cancer`, `EBV_Associated_Gastric_Cancer`, `Burkitt_Lymphoma`, `Kaposi_Sarcoma`, `Merkel_Cell_Carcinoma`, `Adult_T_Cell_Leukemia_Lymphoma`, `Aflatoxin_Related_HCC` | governed by §3a, not by any infection rule |

### 1.3 Measurable symptoms

| Symptom | Measurement |
|---|---|
| Hierarchy is free text, not a foreign key | `parents:` is `multivalued: true, range: string`. The 125 flagged entries use **131 distinct parent strings** — more distinct strings than entries |
| …and it is not even case-normalised | `Bacterial Infection` (17) / `Bacterial infection` (2) / `Bacterial infectious disease` (2) / `bacterial infectious disease` (2) / `primary bacterial infectious disease` (2) are five spellings of one concept |
| Microbial-specific slots are unused | `hosts:` **0/125**, `vectors:` **0/125**, `life_cycle_stages:` **0/125**, `agent_life_cycle:` 15/125 (12%), `transmission:` 70/125 (56%) |
| Subtypes are mostly unbound | 181 subtypes across the infectious set, **only 54 (29%)** carry a `subtype_term` ontology binding |
| Over-broad MONDO anchoring on lumps | 10 entries have ≥3 agents and 0 subtypes; several anchor above their own scope — `Travelers_Diarrhea` → *diarrheal disease*, `Soil_Transmitted_Helminthiases` → *helminthiasis*, `Lymphatic_Filariasis` → *filariasis*, `Rhinovirus_Infection` → *common cold* |
| Mapping discipline is nearly absent | 17 `mondo_mappings` entries total across 125 files (12 exactMatch, 3 narrowMatch, 1 broadMatch, 1 closeMatch) |
| No `disease_term` at all | `Adenovirus_Respiratory_Infection`, `Lone_Star_Virus_Infection` |
| Unbound pathogen taxa | 7 entries name an agent with no NCBITaxon binding (`Tetanus` → *Clostridium tetani*, `Pinta` → *Treponema carateum*, `Cytomegalovirus_Retinitis` → *Human cytomegalovirus*, …) |
| One entry is the ontology root | `Infectious_Disease` is a 184-line Disease entry anchored to `MONDO:0005550` *infectious disease*, with one generic pathophysiology node ("Pathogen Invasion and Replication") |

---

## 2. Specific defects

### 2.1 Organ-syndrome entries lump unrelated pathogens with no internal structure

`Bacterial_meningitis` (1,352 lines) names *Neisseria meningitidis*,
*Streptococcus pneumoniae*, *Haemophilus influenzae* and *Listeria
monocytogenes* as its four agents and carries **zero subtypes**. These four
organisms differ in age distribution, vaccine availability, capsular vs
listerial pathogenesis, empiric antibiotic choice (ampicillin is added
specifically for *Listeria*), and MONDO identity — each has its own MONDO class.
The entry's pathograph therefore has to describe a mechanism generic enough to
cover all four, which is exactly the failure mode the cancer review identified
for organ-umbrella entries.

The same pattern holds for `Infective_Endocarditis` (3 agents / 3 unbound
subtypes), `Endophthalmitis` (4 / 6 unbound), `Folliculitis` (4 / 8 unbound),
`Choroiditis` (4 agents, none NCBITaxon-bound, 10 subtypes), `Chorioamnionitis`
(6 / 3) and `Travelers_Diarrhea` (8 agents, 0 subtypes, anchored to *diarrheal
disease*).

`Travelers_Diarrhea` also exposes a representation limit worth recording: its
three *E. coli* pathotypes (ETEC, EAEC, EPEC) all bind to `NCBITaxon:562`
*Escherichia coli*, because NCBITaxon has no pathotype rank. Pathotype is a
real mechanistic distinction (heat-labile/heat-stable enterotoxin vs aggregative
adherence vs attaching-effacing lesion) that the current binding cannot carry.

### 2.2 Genus-level lumps are decided ad hoc

`Coccidioidomycosis` lumps *C. immitis* and *C. posadasii* — correct; they are
clinically indistinguishable. `Human_African_Trypanosomiasis` lumps *T. b.
gambiense* and *T. b. rhodesiense* — questionable; they differ in reservoir
(anthroponotic vs zoonotic), tempo (chronic West African vs acute East African),
and staging/treatment pathway, which is precisely the profile the
`Treponematoses` grouping used to justify *splitting* four near-identical
organisms. `Malaria` lumps *P. falciparum* and *P. vivax*, which differ in
hypnozoite biology and therefore in radical-cure requirements. Nothing records
which way the call went or why.

Note what makes this hard to audit: `hosts:` and `vectors:` are used **zero**
times. Reservoir host and arthropod vector are among the strongest arguments for
splitting a genus lump, and the KB currently cannot express either.

### 2.3 Rocky Mountain spotted fever is modelled twice, at two levels

| Concept | As standalone entry | As subtype of `Spotted_Fever_Rickettsiosis` |
|---|---|---|
| Rocky Mountain spotted fever | `Rocky_Mountain_Spotted_Fever.yaml`, 2,119 lines, `MONDO:0019359` | subtype `RMSF`, `subtype_term` `MONDO:0019359` |
| Boutonneuse fever | `Boutonneuse_Fever.yaml`, 1,273 lines, `MONDO:0024472` | subtype `MSF`, `subtype_term` `MONDO:0024472` |

`Spotted_Fever_Rickettsiosis` (1,714 lines, `MONDO:0001195` *spotted fever*) is
in substance a **grouping** curated as a Disease: its six subtypes are six named
diseases, two of which are already full entries. Under §3a's rule for promoted
strata, this should be a `Grouping` with the members as Disease entries — the
`Treponematoses` shape exactly. The same test flags `Viral_Hemorrhagic_Fever`
(8 unbound subtypes, one of which duplicates the standalone
`Hantavirus_Hemorrhagic_Fever_with_Renal_Syndrome` entry).

### 2.4 Phase-of-infection and pathogen-syndrome splits disagree with each other

- **`Legionella`** is split by syndrome into two entries (`Legionnaires_Disease`,
  `Pontiac_Fever`) — reasonable, they are genuinely different illnesses. But
  `Pontiac_Fever` carries `infectious_agent:` and `Legionnaires_Disease` does
  not, so the shared etiology is invisible to any query.
- **HCV** is split by phase: `Acute_Hepatitis_C_Virus_Infection`
  (`MONDO:0100371`) and `Hepatitis_C` (`MONDO:0005231`). The schema already has
  `progression:` (keyed on `phase`) and `stages:` for exactly this.
- **HIV** is split the other way: `Acquired_Immunodeficiency_Syndrome` exists,
  but there is **no HIV-infection entry**, so untreated chronic HIV infection has
  nowhere to live except inside the AIDS entry.
- **SARS-CoV-2** spreads over four entries — `COVID-19`, `Long_COVID`,
  `Multisystem_Inflammatory_Syndrome_in_Children_MIS-C`,
  `Seasonal_Coronavirus_Infection` — of which only the middle two declare the
  virus.

### 2.5 Coverage gaps that follow from having no ladder

Because nothing says what level a microbial entry sits at, the queue has been
filled opportunistically. Absent from both `kb/` and `stubs/`:

**typhoid fever** (while `Paratyphoid_Fever` *is* curated), **herpes zoster /
shingles** (while `Chickenpox` is), **anthrax**, **diphtheria**, **amebiasis**,
**histoplasmosis**, **listeriosis**, **salmonellosis**, **West Nile fever**,
**yellow fever**, **rotavirus** and **norovirus gastroenteritis**, **sepsis**,
**urinary tract infection**, **cellulitis**, **infectious osteomyelitis**.
`Cryptosporidiosis` and `Zika` exist only as stubs. All 40 infectious stubs are
`entry_type: UNDECIDED`, meaning the lump/split call — the curator's *first*
job per the stub queue rules — has not been made for any of them.

---

## 3. Assessment

**What is already right and should be preserved.**

- The organism-defined core (cholera, measles, rabies, leprosy, tetanus, Buruli
  ulcer, the hepatitides A–E) is at the level the field actually uses, and is
  stable.
- Infection *mechanism* is correctly handled as modules, not taxa —
  `intracellular_pathogen_persistence`, `granuloma_formation`,
  `innate_antiviral_interferon_response`, `molecular_mimicry_autoimmunity`, the
  antibiotic/antiviral target modules. This mirrors the hallmark-module pattern
  §3a praised for cancer.
- Post-infectious sequelae are already separate entries with distinct mechanisms
  (`Rheumatic_Heart_Disease`, `Postinfectious_Vasculitis`, `MIS-C`,
  `Postpoliomyelitis_Syndrome`, `Acute_Disseminated_Encephalomyelitis`). That is
  the right call — the mechanism is host-immune, not microbial.
- `Treponematoses` is a model artifact. It states in its `grouping_rationale`
  exactly which axes justified splitting (transmission route, vertical
  transmission, organ systems, second-line drug susceptibility) and why the
  membership criterion is "a pathogenic treponeme" rather than "a *T. pallidum*
  subspecies". Every contested cluster in §2 needs a paragraph like that.

**The three systematic deviations** (deliberately parallel to §3a's three):

1. **Syndrome-level entries used as taxa.** Organ syndromes spanning unrelated
   organisms (`Bacterial_meningitis`, `Infective_Endocarditis`, `Endophthalmitis`,
   `Choroiditis`, `Folliculitis`, `Chorioamnionitis`, `Travelers_Diarrhea`,
   `Viral_Encephalitis`, `Viral_Hemorrhagic_Fever`) are curated as single
   diseases, most with no per-pathogen subtypes.
2. **Grouping-shaped entries curated as Disease.** `Spotted_Fever_Rickettsiosis`
   and `Viral_Hemorrhagic_Fever` list named diseases as subtypes, two of which
   are simultaneously standalone entries with the same MONDO IDs.
3. **No recorded rule**, hence: 131 parent strings for 125 entries, 0% use of
   `hosts`/`vectors`, 29% subtype binding, 17 MONDO mappings total, and 40
   `UNDECIDED` stubs.

---

## 4. Proposed decision ladder (draft for design-decisions.md §3b)

> **Default level for a new microbial entry is the named clinical entity as
> infectious-disease practice names it** — the pathogen–syndrome pair that has
> its own name, diagnosis, and treatment pathway (cholera, Legionnaires'
> disease, Pontiac fever, Buruli ulcer). Neither the organism alone nor the
> organ syndrome alone is the default.

1. **Below that level — organism strata (species, subspecies, serotype,
   genotype, pathotype) are `has_subtypes`**, not entries. Promote a stratum to
   its own entry only when it meets the *Treponematoses test*: it differs from
   its siblings in **at least two** of — transmission route or vector,
   reservoir host, natural history/tempo, organ systems involved, or first-line
   therapy. Record which two in the entry, and cover the promoted siblings with
   a `Grouping`. A promoted stratum with no MONDO term of its own anchors to the
   parent with `mapping_predicate: skos:narrowMatch`, never by bare parent-term
   reuse.
2. **An organ syndrome spanning unrelated organisms is a `Grouping`, not a
   Disease** — unless the syndrome itself has a conserved mechanism independent
   of which organism causes it (in which case prefer a `kb/modules/` module and
   `conforms_to`). Where such an entry is retained as a Disease for clinical
   reasons, every named agent must appear as an ontology-bound `has_subtypes`
   entry.
3. **Phase of a single infection is `progression:` / `stages:`, never a separate
   entry.** Acute vs chronic hepatitis C, primary vs latent vs reactivated
   herpesvirus, and colonisation vs invasive disease are phases.
4. **Post-infectious immune sequelae remain separate Disease entries** — the
   mechanism is host-immune, not microbial — but must name the index infection
   in `parents` and link to its entry.
5. **Infection-attributed neoplasms follow §3a.** The pathogen is an *etiologic
   annotation* (`infectious_agent`), not a granularity axis; it never promotes a
   cancer stratum to an entry on its own.
6. **The ontology root is not an entry.** `MONDO:0005550` *infectious disease*,
   and comparably abstract classes (*viral infectious disease*, *bacterial
   infectious disease*), are `OUT_OF_SCOPE` — too abstract to carry a mechanism.
7. **Every microbial entry declares its agent.** `infectious_agent` with an
   NCBITaxon binding is required; `transmission` is required; `hosts` and
   `vectors` are required wherever a non-human reservoir or arthropod vector
   exists, because those are the axes rules 1 and 2 are decided on.

---

## 5. Recommended follow-up actions

Ordered by ratio of value to effort.

| # | Action | Scope |
|---|---|---|
| 1 | Ratify the ladder above as design decisions **§3b** | 1 PR |
| 2 | Backfill `infectious_agent:` (NCBITaxon-bound) on the 21+ microbial entries lacking it, starting with `COVID-19`, `Lyme_Disease`, `Legionnaires_Disease` and the nine respiratory-infection tranche entries | 21 entries |
| 3 | Bind the 7 free-text pathogen names that have no NCBITaxon term, and add `disease_term` to `Adenovirus_Respiratory_Infection` and `Lone_Star_Virus_Infection` | 9 entries |
| 4 | Convert `Spotted_Fever_Rickettsiosis` and `Viral_Hemorrhagic_Fever` to `Grouping` records on the `Treponematoses` model; keep RMSF and boutonneuse fever as the Disease entries they already are | 2 groupings, 2 entries edited |
| 5 | Add per-pathogen bound subtypes to `Bacterial_meningitis`, `Infective_Endocarditis`, `Endophthalmitis`, `Chorioamnionitis`, `Travelers_Diarrhea`, `Choroiditis`, `Folliculitis` — or convert them to groupings under rule 2 | 7 entries |
| 6 | Re-anchor the 10 over-broad `disease_term` bindings, adding `skos:narrowMatch` mappings where no exact MONDO class exists | 10 entries |
| 7 | Normalise `parents:` to a controlled vocabulary. 131 strings collapse to roughly a dozen; case variants alone account for five spellings of "bacterial infection". Consider whether `parents` should become ontology-bound rather than free text | KB-wide, scriptable |
| 8 | Populate `hosts:` and `vectors:` on the zoonotic and vector-borne entries — currently 0% — since rules 1 and 2 turn on them | ~40 entries |
| 9 | Decide `entry_type` on the 40 infectious stubs, and seed the coverage gaps in §2.5 (typhoid fever, herpes zoster, anthrax, diphtheria, sepsis, UTI and the rest) | queue work |
| 10 | Retire `Infectious_Disease` (`MONDO:0005550`) under rule 6, recording the reasoning so the concept is not re-nominated | 1 entry |
| 11 | Add groupings mirroring the ladder: *Rickettsioses*, *Viral hepatitides*, *Soil-transmitted helminthiases*, *Enteric fevers*, *Arboviral haemorrhagic fevers* | ~5 groupings |

Items 2, 3 and 6 are mechanical and independently verifiable; item 1 should land
first so items 4, 5 and 9 have a rule to cite.

### Open question for a human

Rule 3 (phase is not an entry) implies merging `Acute_Hepatitis_C_Virus_Infection`
into `Hepatitis_C` as a `progression` phase. Both are substantial curated
entries with their own MONDO classes, and MONDO itself distinguishes them. The
alternative reading is that MONDO's own split should be honoured and rule 3
narrowed to phases MONDO does *not* separately class. This is a judgement call
about whether the ladder or the ontology is authoritative when they disagree,
and it should be settled before item 5 begins.

---

## Provenance

Generated by Claude Code on 2026-08-29 against `main` at 2,476 disorder entries,
99 groupings, 164 modules, 1,385 stubs. The microbial set was identified by the
presence of an `infectious_agent:` block (125 entries) plus a keyword sweep of
entry headers reviewed by hand (≥21 further entries). All counts in §1.3 were
computed from the YAML, not estimated; the scripts are one-off and are not
committed. No KB content was modified.
