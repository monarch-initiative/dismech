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

On identifiers: NCBITaxon is the sole vocabulary in use, and that is the right
call. It reaches serovar and serotype rank, so the unbound agents are curation
misses rather than ontology limits. GTDB and GenBank assembly accessions are
absent and should stay absent — GTDB classifies *Shigella* as *Escherichia coli*,
which would erase a distinction the KB depends on. The one thing no taxonomy can
carry is **pathotype**, which §4 rung 3a handles structurally instead.

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
| Life-cycle modelling is curated for one clade only | `agent_life_cycle:` **15/125** (12%). Where present it is well populated (`hosts` 15/15, `life_cycle_stages` 12/15, `vectors` 8/15) — but all 15 are vector-borne parasitic or arboviral entries. **At least 24 further zoonotic or vector-borne entries have no life-cycle block at all** (§2.6). `transmission:` 70/125 (56%) |
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

Note what makes this hard to audit: reservoir host and arthropod vector are
among the strongest arguments for splitting a genus lump, and the `agent_life_cycle`
block that carries them is populated on only 15 entries — none of them the ones in
dispute here. `Human_African_Trypanosomiasis` is one of the 15 and does record two
hosts and a vector, which is precisely why its split question is answerable at all.

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

### 2.6 Life-cycle modelling stops at the parasitology entries

`agent_life_cycle` — which carries `hosts` (with a `role` for definitive /
intermediate / reservoir / accidental / paratenic), `vectors`, and
`life_cycle_stages` (OPL-bound) — is present on 15 entries and well populated on
all 15: `Babesiosis`, `Chagas_Disease`, `Chikungunya`, `Dengue`,
`Human_African_Trypanosomiasis`, `Leishmaniasis`, `Lymphatic_Filariasis`,
`Malaria`, `Myiasis`, `Nipah_Virus_Disease`, `Onchocerciasis`, `Schistosomiasis`,
`Soil_Transmitted_Helminthiases`, `Taeniasis_Cysticercosis`, `Toxoplasmosis`.

The pattern is right and the block is not the problem. The problem is that it
stops at classical parasitology. At least 24 further entries with a non-human
reservoir or an arthropod vector carry none: `Plague` (flea, rodent),
`Rocky_Mountain_Spotted_Fever`, `Boutonneuse_Fever`, `Spotted_Fever_Rickettsiosis`,
`Scrub_Typhus`, `Murine_Typhus`, `Lone_Star_Virus_Infection`, `Tularemia`,
`Brucellosis`, `Leptospirosis`, both hantavirus entries, `Rabies`, `Monkeypox`,
`Ebola_Virus_Disease_EVD`, `Cat-Scratch_Disease`, `Glanders`, `Oroya_Fever`,
`Melioidosis`, `Dracunculiasis`, `Cutaneous_Larva_Migrans`,
`Polycystic_Echinococcosis`, `Hepatitis_E`, `Viral_Encephalitis`,
`Viral_Hemorrhagic_Fever` — plus `Lyme_Disease`, `Q_Fever`, `Psittacosis` and
`Southern_Tick-Associated_Rash_Illness`, which have no `infectious_agent` block
either.

This matters for the ladder specifically: reservoir host and vector are two of
the five axes rung 4 promotion is decided on. Where they are unrecorded, the
promotion question cannot be answered from the entry.

### 2.7 Identifier policy: NCBITaxon only, and that is mostly correct

**What is in use.** NCBITaxon, exclusively — 121 of the 125 flagged files, 411
occurrences, **165 distinct CURIEs**, of which 151 are binomial or finer and 14
sit at genus (*Aspergillus*, *Babesia*, *Brucella*, *Candida*, *Legionella*,
*Leptospira*, *Shigella*, *Norovirus*, …). It is properly wired: `OrganismDescriptor`
binds `term.id` to the `OrganismTerm` dynamic enum (`reachable_from` `NCBITaxon:1`
plus `NCBITaxon:10239` for viruses) at `obligation_level: REQUIRED`, validated
cache-first against `cache/ncbitaxon/terms.csv` and
`cache/enums/organismterm_*.csv`, with `NCBITaxon: ols:ncbitaxon` in
`conf/oak_config.yaml` (OLS rather than a local build — the SQLite is ~13.5 GB,
issue #5160).

**GTDB is not used anywhere.** No prefix in the schema, no adapter in
`oak_config.yaml`, zero occurrences in `kb/` or `src/`. Its only appearance in the
tree is a semsql registry file inside `.venv` — a dependency's ontology catalog,
not project configuration.

**GenBank / RefSeq genome identifiers are not used for microbes.** The
GenBank-shaped strings in `kb/` are all *human* reference sequences inside
evidence snippets and prose in Mendelian entries — `NM_007241.4`, `NC_000015.10`,
`NG_016284.1`, `NC_012920.1` (mtDNA) — and none are structured identifiers in a
slot. There are **zero** assembly accessions (`GCA_`/`GCF_`) anywhere in the
repository.

**Where NCBITaxon is sufficient.** It reaches well below species. Every one of
the seven unbound agent names in §1.3 resolves against NCBITaxon, including at
serovar and serotype rank:

| Unbound in the KB | Exists as |
|---|---|
| *Clostridium tetani* | `NCBITaxon:1513` |
| *Treponema carateum* | `NCBITaxon:3712027` |
| Human cytomegalovirus | `NCBITaxon:10359` (*Human betaherpesvirus 5*) |
| *S. enterica* serovar Paratyphi A | `NCBITaxon:54388` — **serovar rank** |
| *E. coli* O157:H7 | `NCBITaxon:83334` — **serotype rank** |

Those seven are therefore curation misses, not ontology limits, and the fix is
mechanical.

**Where NCBITaxon genuinely runs out: pathotype.** ETEC, EPEC and EAEC have no
NCBITaxon class — a search returns only individual sequenced isolates (e.g.
`Escherichia coli 042`, the EAEC reference strain). This is why all three
`Travelers_Diarrhea` pathotypes collapse onto `NCBITaxon:562`. It is not a fixable
gap in NCBITaxon: a pathotype is defined by **virulence gene content**, not by
phylogeny, so no taxonomy will ever carry it. Rung 3 of the ladder handles this
explicitly.

**GTDB would not fix this and would make things worse.** GTDB is a genome-based
taxonomy that re-splits and re-merges NCBI taxa on average nucleotide identity.
It has no pathotype concept either, and its species assignments diverge from the
clinical names the KB is built on. Queried live against the GTDB API:

```
Shigella dysenteriae 1012 → gtdbTaxonomy: … g__Escherichia; s__Escherichia coli
Shigella sonnei 53G       → gtdbTaxonomy: … g__Escherichia; s__Escherichia coli
```

GTDB classifies *Shigella* as *Escherichia coli*. Adopting it as a binding
vocabulary would collapse the agent of `Shigellosis` into *E. coli* and erase
exactly the distinction the ladder exists to preserve. GTDB is the right tool for
microbial phylogenomics and the wrong tool for naming what a patient has.

**A GenBank/RefSeq assembly accession names one isolate, not a stratum.**
Recording `GCA_000027125.1` for EAEC commits the KB to a single sequenced genome
standing in for a pathotype defined by a gene repertoire that varies across
isolates. That is a stronger claim than the evidence supports.

**Recommended policy.**

1. **NCBITaxon remains the sole binding vocabulary** for `infectious_agent_term`,
   `hosts`, and any organism reference. Bind the most specific NCBITaxon node that
   is *correct*, down to serovar or serotype where one exists.
2. **Do not add GTDB** as a prefix, adapter, or binding vocabulary. If a future
   need arises for genome-phylogenetic context, it belongs in a `notes:` line or a
   dedicated annotation, never in `term.id`.
3. **Do not add genome or assembly accessions** to `infectious_agent`. A specific
   sequenced isolate belongs in a `datasets:` record (where `bioproject:` /
   `sra:` prefixes already exist) or in an evidence `snippet`, not as the agent's
   identity.
4. **Pathotype is carried structurally, not by an identifier** — see rung 3.
   Leave `subtype_term` absent for a pathotype with no honest NCBITaxon node
   rather than binding the parent species. This is the `dismech-terms` rule that
   no term beats a bad one.
5. **Add a `pathotype:` slot to `InfectiousAgent`** (free text or a small
   controlled enum) so ETEC/EPEC/EAEC/EHEC and MRSA/MSSA are machine-queryable
   without a false ontology binding. `InfectiousAgent` currently carries only
   `name`, `infectious_agent_term`, `food_source`, `evidence`, `description`,
   `has_subtypes` — there is no `strain`, `serovar`, `serotype`, or `pathotype`
   slot anywhere in the schema.

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

> **Default level for a new microbial entry is the named clinical entity** — the
> pathogen–syndrome pair that infectious-disease practice names, diagnoses and
> treats as a unit (cholera, Legionnaires' disease, Pontiac fever, Buruli ulcer).
> Neither the organism alone nor the organ syndrome alone is the default.

The ladder has five rungs. Rung 2 is the default; you move off it only by meeting
that rung's stated test.

### Rung 0 — Out of scope

An ontology class too abstract to carry a mechanism: `MONDO:0005550` *infectious
disease*, *viral infectious disease*, *bacterial infectious disease*, *parasitic
infectious disease*.

**Requirement:** record as a stub with `entry_type: OUT_OF_SCOPE` and a `notes:`
line giving the reason, so the concept is not re-nominated. Never a Disease entry.

### Rung 1 — Grouping (`kb/groupings/`)

A curated union of Disease entries sharing an organism clade, a transmission
mode, or a clinical/programmatic category. *Treponematoses* is the reference
implementation.

| Requirement | Level |
|---|---|
| Explicit `members` — no ontology-closure substitute | required |
| `grouping_basis` | required |
| `grouping_rationale` stating **the axes on which the members were split**, not only what they share | required |
| `mappings.mondo_mappings` with an explicit `mapping_predicate` (`closeMatch` where the MONDO class is defined differently — see Treponematoses) | required |
| `membership_criteria` | recommended |
| Its own `pathophysiology` | **prohibited** — a grouping is a union, not a disease |

A grouping is also the correct home for an **organ syndrome spanning unrelated
organisms** (bacterial meningitis, infective endocarditis, endophthalmitis) when
the syndrome has no organism-independent mechanism of its own. Where it does have
one, prefer a `kb/modules/` module plus `conforms_to` on the member entries.

### Rung 2 — Disease entry: the named clinical entity  *(the default)*

| Requirement | Level |
|---|---|
| `disease_term` bound to MONDO, at the entry's **own** scope | required |
| — where no exact class exists, anchor to the nearest and record `mappings.mondo_mappings` with `skos:narrowMatch`; never reuse a broader parent term bare | required |
| `infectious_agent` — at least one, each with an NCBITaxon-bound `infectious_agent_term` | required |
| `transmission` — at least one route | required |
| `agent_life_cycle` with `hosts` (each carrying a `role`), **and `vectors` where an arthropod vector exists** | required whenever a non-human reservoir or vector exists |
| `life_cycle_stages` (OPL-bound) | required for helminth and protozoan agents; recommended otherwise |
| At least one `pathophysiology` node specific to this entity | required |
| `parents` drawn from the controlled list (see §5 item 7) | required |
| `classifications` | recommended |

**Test for being on this rung rather than rung 1:** the entity has a name the
field uses, a diagnostic pathway, and a treatment; and its `pathophysiology`
nodes are true of *every* case it covers. If a node has to be written vaguely
enough to cover two organisms with different mechanisms, the entry is a rung-1
grouping wearing a Disease costume.

### Rung 3 — `has_subtypes` within a Disease entry  *(the organism axis)*

Strata below the entry go here: **species → subspecies → serovar → serotype →
pathotype / strain**. This rung is deliberately generous. A stratum earns a
subtype when it differs from its siblings in **any one** of:

- clinical presentation or organ involvement
- diagnosis or diagnostic pathway
- first-line treatment or drug susceptibility
- prognosis or natural history
- transmission route, vector, or reservoir
- geography or at-risk population

One axis is enough for a subtype. (Two are needed to *promote* to a separate
entry — rung 4.) Recording a stratum as a subtype is cheap and reversible;
leaving it inside an undifferentiated lump is not.

| Requirement per subtype | Level |
|---|---|
| `name` — short and slug-friendly (`ETEC`, `RMSF`, `Type 1`); it is the foreign-key target for `subtype:` fields elsewhere in the file | required |
| `display_name` where the short name is too terse | recommended |
| `description` stating **what differs**, not just what the stratum is | required |
| `subtype_term` bound where an honest term exists — MONDO for a named disease variant, NCBITaxon for a species / subspecies / serovar / serotype | required *if a term exists* |
| `evidence` for the differentiating claim | required |
| `subtype_frequency`, `geography`, `genes` | recommended where known |

Only 29% of existing infectious subtypes carry a `subtype_term`; that is the
gap this rung's requirements close.

#### Rung 3a — Pathotypes and other non-phylogenetic strata

A **pathotype** is a stratum defined by virulence gene content rather than
phylogeny: ETEC / EPEC / EAEC / EHEC / EIEC / ExPEC / UPEC within *E. coli*,
MRSA / MSSA within *S. aureus*, toxigenic vs non-toxigenic *C. difficile* or
*C. diphtheriae*. Pathotypes are the concrete case of "subtype by variant where
it is clinically relevant" — and they usually *are* relevant, because they
determine the toxin, the syndrome, and often the therapy.

**No taxonomy carries them.** NCBITaxon has no ETEC or EPEC class; GTDB has none
either and would additionally collapse *Shigella* into *E. coli* (§2.7). So
pathotype is carried **structurally, not by an identifier**:

| Requirement | Level |
|---|---|
| A `has_subtypes` entry with `name` = the pathotype acronym | required |
| `description` naming the **defining virulence determinants** (LT/ST enterotoxin; bundle-forming pilus and the attaching-effacing lesion; Shiga toxin; *mecA*/SCC*mec*) | required |
| `subtype_term` bound **only** where a genuine node exists at serotype rank (`E. coli O157:H7` → `NCBITaxon:83334`) | conditional |
| `subtype_term` **omitted** where the only candidate is the parent species — binding *E. coli* to ETEC is a false grounding | required |
| The defining determinant modelled as a `pathophysiology` node where the mechanism is curated | recommended |
| A genome or assembly accession (`GCA_`/`GCF_`) as the stratum's identity | **prohibited** — see §2.7 |
| A `pathotype:` slot on `InfectiousAgent`, once added, populated in parallel | required after schema change |

The same shape covers other non-phylogenetic strata: **biotype** (*V. cholerae*
classical vs El Tor), **lineage** (*M. tuberculosis* L1–L9), **viral genotype**
(HCV 1–6, HBV A–H) and **clade** (mpox I vs II). Bind where NCBITaxon has a node;
otherwise carry it structurally and say so.

### Rung 4 — Promotion of a stratum to its own Disease entry

**The Treponematoses test.** Promote only when the stratum differs from its
siblings in **at least two** of: transmission route or vector; reservoir host;
natural history or tempo; organ systems ultimately involved; first-line therapy.

| Requirement | Level |
|---|---|
| Name the two-or-more satisfied axes explicitly, in the entry or in the covering grouping's `grouping_rationale` | required |
| Own `disease_term`; where no exact MONDO class exists, `skos:narrowMatch` to the parent | required |
| A rung-1 `Grouping` covering the promoted siblings | required |
| The parent entry **drops the promoted stratum from `has_subtypes`** | required — no double-modelling |
| Everything in rung 2 | required |

The last row is the rule `Spotted_Fever_Rickettsiosis` currently violates: RMSF
and boutonneuse fever are full entries *and* subtypes, carrying the same MONDO
IDs in both places.

### Orthogonal axes — never a rung

These are real distinctions that are modelled somewhere other than the taxonomy,
and reaching for a new entry for any of them is the error:

| Distinction | Belongs in |
|---|---|
| Phase of one infection (acute vs chronic; primary / latent / reactivated; colonisation vs invasive disease) | `progression:` / `stages:` on the single entry |
| Severity or stage | `stages:`, `severity` qualifiers |
| Organ syndrome across unrelated organisms | rung-1 Grouping, or a `kb/modules/` module |
| Post-infectious immune sequela (rheumatic heart disease, MIS-C, post-infectious vasculitis, ADEM) | its own Disease entry — the mechanism is host-immune, not microbial — cross-linked to the index infection via `parents` |
| Infection-attributed neoplasm | §3a cancer ladder; the pathogen is an `infectious_agent` annotation, never a granularity axis |
| Mechanism shared across diseases | `kb/modules/` + `conforms_to` |
| Antimicrobial resistance, where it does not change the syndrome | `treatments` / `notes` — but see rung 3a where it defines a pathotype (MRSA) |

### Decision procedure

1. Is the concept too abstract to carry a mechanism? → **rung 0**.
2. Is it a union of diseases the field already names separately? → **rung 1**.
3. Is it a named clinical entity with its own diagnosis and treatment? → **rung 2**. *(default)*
4. Is it an organism stratum below such an entity? → **rung 3**; check rung 3a if it is defined by gene content rather than phylogeny.
5. Does that stratum satisfy ≥2 Treponematoses axes? → **rung 4**, and add the covering grouping.
6. Is it a phase, stage, sequela, neoplasm, or mechanism? → not a rung; see the table above.

---

## 5. Recommended follow-up actions

Ordered by ratio of value to effort. Marked **[M]** where the work is
microbial-specific and **[G]** where the same defect exists across the whole KB
and should be tracked as a separate general issue.

| # | Action | Scope |
|---|---|---|
| 1 | **[M]** Ratify the rung ladder in §4 as design decisions **§3b** | 1 PR |
| 2 | **[M]** Backfill `infectious_agent:` (NCBITaxon-bound) on the 21+ microbial entries lacking it, starting with `COVID-19`, `Lyme_Disease`, `Legionnaires_Disease` and the nine respiratory-infection tranche entries | 21 entries |
| 3 | **[M]** Bind the 7 free-text pathogen names — all seven exist in NCBITaxon (§2.7) — and add `disease_term` to `Adenovirus_Respiratory_Infection` and `Lone_Star_Virus_Infection` | 9 entries |
| 4 | **[M]** Convert `Spotted_Fever_Rickettsiosis` and `Viral_Hemorrhagic_Fever` to `Grouping` records on the `Treponematoses` model (rung 1); keep RMSF and boutonneuse fever as the Disease entries they already are, and drop them from the parent's `has_subtypes` per rung 4 | 2 groupings, 2 entries edited |
| 5 | **[M]** Add rung-3 bound subtypes to `Bacterial_meningitis`, `Infective_Endocarditis`, `Endophthalmitis`, `Chorioamnionitis`, `Travelers_Diarrhea`, `Choroiditis`, `Folliculitis` — or convert them to rung-1 groupings | 7 entries |
| 6 | **[M]** Add a `pathotype:` slot to `InfectiousAgent`, then populate the rung-3a strata: ETEC / EAEC / EPEC in `Travelers_Diarrhea`, MRSA/MSSA where *S. aureus* is the agent, toxigenic vs non-toxigenic *C. difficile* | 1 schema PR + ~6 entries |
| 7 | **[M]** Re-anchor the 10 over-broad `disease_term` bindings, adding `skos:narrowMatch` mappings where no exact MONDO class exists | 10 entries |
| 8 | **[M]** Add `agent_life_cycle` (with `hosts`, and `vectors` where an arthropod vector exists) to the ~24 zoonotic and vector-borne entries lacking it, since rung-4 promotion turns on reservoir and vector | ~24 entries |
| 9 | **[M]** Decide `entry_type` on the 40 infectious stubs, and seed the coverage gaps in §2.5 (typhoid fever, herpes zoster, anthrax, diphtheria, sepsis, UTI and the rest) | queue work |
| 10 | **[M]** Retire `Infectious_Disease` (`MONDO:0005550`) under rung 0, recording the reasoning so the concept is not re-nominated | 1 entry |
| 11 | **[M]** Add rung-1 groupings: *Rickettsioses*, *Viral hepatitides*, *Soil-transmitted helminthiases*, *Enteric fevers*, *Arboviral haemorrhagic fevers* | ~5 groupings |
| 12 | **[G]** Normalise `parents:` to a controlled vocabulary and decide whether it should be ontology-bound rather than `range: string`. The microbial set alone uses 131 distinct strings for 125 entries, but 2,366 entries KB-wide use the slot | KB-wide |
| 13 | **[G]** Raise `subtype_term` binding rates KB-wide. 29% in the microbial set; measure and target the rest | KB-wide |
| 14 | **[G]** Audit for grouping-shaped Disease entries outside infection — the `Spotted_Fever_Rickettsiosis` pattern is the same one §3a found in cancer organ-umbrella entries | KB-wide |

Items 2, 3 and 7 are mechanical and independently verifiable; item 1 should land
first so items 4, 5, 6 and 9 have a rule to cite. Items 12–14 belong in a separate
general issue so the microbial work is not blocked behind KB-wide refactors.

### Two questions for a human

**1. Does the ladder or MONDO win when they disagree?** The orthogonal-axes table
says phase is `progression:`, not an entry — which implies merging
`Acute_Hepatitis_C_Virus_Infection` into `Hepatitis_C`. Both are substantial
curated entries with their own MONDO classes, and MONDO itself distinguishes
them. The alternative reading is that MONDO's split should be honoured and the
rule narrowed to phases MONDO does *not* separately class. Settle this before
item 5 begins.

**2. How far down does rung 3 go before it becomes noise?** The rung is
deliberately generous — one differentiating axis earns a subtype. For *M.
tuberculosis* lineages or HCV genotypes that is clearly right; for the ~2,000
*Salmonella* serovars it clearly is not. The working answer is that a stratum
earns a subtype when the difference is *documented in the literature for this
disease*, not merely nomenclaturally available, but that is a judgement the
curation community should confirm.

---

## Provenance

Generated by Claude Code on 2026-08-29 against `main` at 2,476 disorder entries,
99 groupings, 164 modules, 1,385 stubs. The microbial set was identified by the
presence of an `infectious_agent:` block (125 entries) plus a keyword sweep of
entry headers reviewed by hand (≥21 further entries). All counts in §1.3 were
computed from the YAML, not estimated; the scripts are one-off and are not
committed. No KB content was modified.

NCBITaxon term existence in §2.7 was checked live against the EBI OLS4 API; the
GTDB *Shigella* placement was checked live against `gtdb-api.ecogenomic.org`. The
vector-borne/zoonotic classification behind the “≥24 entries” figure in §2.6 was
made by hand from the entry descriptions, not by a rule.

A first revision of this report stated that `hosts:`, `vectors:` and
`life_cycle_stages:` were unused KB-wide. That was measured at the wrong nesting
level — all three are slots of `AgentLifeCycle`, not of `Disease`, and are well
populated on the 15 entries that carry an `agent_life_cycle` block. §1.3, §2.2 and
§2.6 carry the corrected finding, which is one of partial coverage rather than
disuse.
