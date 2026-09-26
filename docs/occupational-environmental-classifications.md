# Occupational and environmental classifications

This page covers the sanctioned classification systems dismech encodes for
**occupational disease** and for **environmental exposures and their agents**,
and — the part that most often trips curators up — *which of the two things
each system actually classifies*.

## The load-bearing distinction: disease vs agent

There are two families here, and they attach to different places in the schema.

| | Classifies | Lives on | Examples |
|---|---|---|---|
| **Disease-level** | the disease entry | `Disease.classifications` | ILO list (two axes), European schedule |
| **Agent/exposure-level** | the agent or the exposure event | `Environmental.exposure_classifications` | IARC group, GHS class, route, duration, hazard type, exposome domain |

"Benzene is an IARC Group 1 carcinogen" is a statement about **benzene**, not
about any disease benzene causes. Putting it in `Disease.classifications` would
assert — wrongly — that the disease itself carries the hazard classification.
That is why the exposure axes hang off the `environmental:` entry, mirroring the
separation dismech already maintains between the disease and its exposures.

The same disorder normally carries both families:

```yaml
# Disease-level: what occupational nosologies recognise this disease as
classifications:
  harrisons_chapter:
  - classification_value: RESPIRATORY
  ilo_disease_category:            # section 2 -> disease-category axis
  - classification_value: pneumoconiosis_from_fibrogenic_mineral_dust
    notes: 'ILO List of Occupational Diseases (revised 2010), item 2.1.1.'
  eu_occupational_category:
  - classification_value: silicosis
    notes: 'European schedule Annex I item 301.11 "Silicosis".'

# Agent-level: what the exposure itself is
environmental:
- name: Occupational Respirable Crystalline Silica Exposure
  exposure_term:
    preferred_term: exposure to respirable crystalline silica
    term:
      id: ECTO:7000030
      label: exposure to silica dust
  exposure_classifications:
    hazard_agent_type:
    - classification_value: CHEMICAL
    exposure_route:
    - classification_value: INHALATION
    exposure_duration:
    - classification_value: CHRONIC
    iarc_carcinogen_group:
      classification_value: GROUP_1
      notes: 'Quartz/cristobalite; hazard identification, not a risk statement.'
```

These annotations **do not replace ECTO grounding**. `exposure_term` still
post-composes the exposure event itself; the axes make the regulatory and
toxicological facts queryable without parsing a term label.

## Disease-level: the two occupational nosologies

### ILO List of Occupational Diseases (`ilo_agent_category`, `ilo_disease_category`)

From the **List of occupational diseases (revised
2010)** annexed to the ILO's List of Occupational Diseases Recommendation, 2002
(No. 194). Approved by the ILO Governing Body on 25 March 2010 (307th Session)
after two tripartite Meetings of Experts. This is the closest thing to a globally
sanctioned nosology of work-related disease: Recommendation No. 194 asks member
States to build national schedules comprising, to the extent possible, these
diseases, so it is the common denominator across national lists.

118 values — 4 sections, 8 subsections, 106 items — hierarchical via `is_a`.

**The list is biaxial, so it is two enums reached by two slots.**

| Axis | Sections | Slot | Enum | Items name |
|---|---|---|---|---|
| causative agent | 1 (chemical/physical/biological), 3 (cancer) | `ilo_agent_category` | `ILOCausativeAgentEnum` (84 values) | the *agent* — "Diseases caused by benzene or its homologues" |
| disease category | 2 (by target organ system), 4 (other) | `ilo_disease_category` | `ILODiseaseCategoryEnum` (34 values) | the *disease* — "Asthma caused by recognized sensitizing agents" |

So occupational asthma from isocyanates is legitimately both `isocyanates`
(1.1.35, agent slot) and `occupational_asthma` (2.1.7, disease slot). **Do not
carry the ISDS "assign exactly one group" habit over to this instrument** — ISDS
lists each disorder once by construction; the ILO list does not, and both slots
stay multivalued because more than one item from a single axis is normal
(silicosis takes 2.1.1 *and* 2.1.2).

**Why two enums rather than two slots over one enum.** Two slots sharing one
enum would be enforcement theatre: nothing would stop a section-2 value being
put in the agent slot. Separate enums are what actually make the axis binding.
The two slots additionally share a LinkML `slot_group`
(`occupational_classification`), but that is **presentational only** — the spec
is explicit that "slot groups do not change the semantics of a model" — so it
groups the slots for display and enforces nothing. Each axis enum also declares
`in_subset` (`ilo_causative_agent_axis` / `ilo_disease_category_axis`) so the
axis is machine-readable rather than inferred from the enum name.

**Two caveats the split creates**, both recorded in the module description:

- The ILO's contiguous numbering is now spread across two enums (1.x and 3.x in
  one, 2.x and 4.x in the other). Every value still carries its item number
  verbatim at the head of its `description`, so number lookup works.
- Placing sections 3 and 4 on an axis is **dismech's reading, not the ILO's**.
  The instrument presents four sections, not two axes. Section 3.1 goes on the
  agent axis because its own title is "Cancer caused by the following agents";
  section 4 goes on the disease axis because its one named item (miners'
  nystagmus) is a clinical entity. Section 1.3 is a further wrinkle — its items
  are disease names (Brucellosis, Tetanus) despite sitting under section 1 — and
  it stays on the agent axis because that is where the ILO puts it.

Worked examples in the KB:

| Entry | ILO items | Slot | What it demonstrates |
|---|---|---|---|
| `Silicosis` | 2.1.1 + 2.1.2 | `ilo_disease_category` | Two items from one axis |
| `Asbestosis` | 2.1.1 | `ilo_disease_category` | Disease axis for the non-malignant outcome |
| `Malignant_Mesothelioma` | 3.1.1 | `ilo_agent_category` | Agent axis, *same exposure* as Asbestosis |
| `Noise_Induced_Hearing_Loss` | 1.2.1 | `ilo_agent_category` | Agent-only: no hearing organ-system subsection exists |

**Open items.** Every subsection ends in one (1.1.41, 1.2.7, 1.3.9, 2.1.12,
2.2.4, 2.3.8, 2.4.2, 3.1.21, 4.2) permitting recognition of a disease the list
does not name. They are real permissible values but a weak assignment: prefer a
specific item, and when you must use one, say in `notes` what the agent or
disease actually was. COVID-19 in health workers falls under 1.3.9, the list
predating the pandemic.

### European schedule of occupational diseases (`eu_occupational_category`)

The European schedule is **not** biaxial — it indexes by agent or route through
all five chapters — so it stays one enum on one slot, and joins the ILO slots in
the `occupational_classification` display group.

`EUOccupationalScheduleEnum`, from **Commission Recommendation 2003/670/EC**, in
its current consolidated form. Two amendments have changed it:

- **Recommendation (EU) 2022/2337** (28 Nov 2022) added Annex I item **408**,
  COVID-19 contracted through work in disease prevention, health and social care
  and domiciliary assistance, or in a pandemic context in sectors with a proven
  outbreak risk.
- **Recommendation (EU) 2025/2609** (18 Dec 2025) added four asbestos-related
  diseases to Annex I — **311** laryngeal cancer, **312** ovarian cancer, **313**
  pleural plaques with functional impairment, **314** non-malignant pleural
  effusion — and three suspected asbestos-related cancers to Annex II (**2.309**
  colon, **2.310** rectum, **2.311** stomach). In the same revision Annex II item
  2.308 (laryngeal cancer from asbestos) was **removed**, having been promoted to
  Annex I as 311, so it is not a permissible value. Member States were asked to
  report implementation by 31 December 2026.

177 values — 2 annexes, 10 chapters, 165 items.

**The two annexes mean different things.** Annex I is the recognised schedule
(liable for compensation, subject to prevention measures). Annex II is the
*additional list of diseases suspected of being occupational in origin* —
notifiable, and candidates for later promotion. Annex II keys are prefixed
`suspected_` so the tiers cannot be confused at a glance, they render with an
explicit "(Annex II — suspected)" badge, and an Annex II assignment must say so
in `notes`.

### ILO or EU — which?

**Both, when both apply.** They are separate instruments over the same subject
matter, not substitutes, and neither implies the other. The differences that
matter in practice:

- The European schedule is **finer-grained** where the ILO list is generic. It
  names silicosis (301.11), asbestosis (301.21) and mesothelioma (301.22) as
  distinct items; the ILO list folds the first two into one fibrogenic-mineral-dust
  item (2.1.1) and routes mesothelioma to the cancer section (3.1.1).
- The European schedule is organised **throughout** by causative agent or route;
  only the ILO list has the target-organ-system axis.
- The European schedule uniquely carries COVID-19 and the 2025 asbestos
  additions; the ILO list has not been revised since 2010.

### Numbering, and why it is not in the keys

Item numbers are stable *within* a revision and are what national law and
statistical reporting cite, so every number is recorded verbatim at the head of
its `description`. Provenance identifiers, though, live in LinkML metaslots
rather than prose: each module and enum carries `source:` (and `see_also:`), and
the eight European-schedule items introduced by the 2022 and 2025 amendments
carry their **own** per-value `source:` pointing at the amending recommendation
— so a per-value `source` is itself the signal that an item is a recent
addition, while everything else inherits the enum-level consolidated source. They are **not** stable across revisions (the 2002 ILO list
numbered differently), so — following the convention set by
`ISDSNosologyGroupEnum` — numbers are not part of any permissible-value key. A
future renumbering therefore cannot invalidate stored assignments.

The published EU numbering has genuine gaps (no 115.03, 134, 304.03, 305.02,
501, 2.131–2.139, 2.302, 2.306) and in two places prints sub-items out of numeric
order (201.01/201.03/201.02/201.04, and 304.05/305.01/304.06). Both are
reproduced faithfully. **Do not "repair" either.**

### When to assign at all

Assign only when the disease is genuinely recognised as occupational in origin —
the European schedule requires that it "must be linked directly to the
occupation". An exposure existing is not enough: lead poisoning from a
contaminated water supply is not ILO 1.1.8; lead poisoning in a smelter worker
is.

A disease with both occupational and non-occupational forms (asthma, COPD,
mesothelioma, hearing loss) **still takes the item** — the assignment records
that an occupational form is recognised, not that every case is occupational.
Say which in `notes`.

As with ICIMD and ISDS, a placement is a *definitional taxonomy* mapping, not an
empirical disease claim, so prefer `notes:` over a manufactured evidence
`snippet:`.

## Agent-level: the six exposure axes

All six live under `Environmental.exposure_classifications`. They are separate
enums rather than one blended vocabulary because an exposure has a value on
several at once — "chronic + inhalation + chemical + IARC Group 1" is a normal,
non-redundant description of occupational benzene.

| Slot | Enum | Source |
|---|---|---|
| `hazard_agent_type` | `HazardAgentTypeEnum` | Occupational-hygiene scheme (chemical / physical / biological / ergonomic / psychosocial / safety) |
| `exposure_route` | `ExposureRouteEnum` | Standard toxicological route axis (ATSDR, EPA, GHS, ECTO) |
| `exposure_duration` | `ExposureDurationEnum` | ATSDR Minimal Risk Level durations |
| `iarc_carcinogen_group` | `IARCCarcinogenGroupEnum` | IARC Monographs, Preamble as amended January 2019 |
| `ghs_health_hazard_class` | `GHSHealthHazardClassEnum` | UN GHS health hazard classes (EU CLP, OSHA HCS) |
| `exposome_domain` | `ExposomeDomainEnum` | Wild 2012 three-domain exposome (PMID:22296988) |

### Three traps worth naming

**IARC groups are hazard identification, not risk assessment.** A group states
how strong the evidence is that the agent *can* cause cancer under some
circumstance. It says nothing about potency or exposure level — Group 1 contains
both plutonium and processed meat. Never paraphrase a group as a statement of
risk, and never treat a Group 1 listing as evidence that a particular entry's
exposure caused a particular cancer. **Group 3 is not a finding of safety**: it
means the evidence is inadequate. `GROUP_4` is retained only as a deprecated
value — it was withdrawn by the 2019 Preamble amendment and must not be used for
new curation.

**Exposure duration is about the exposure, not the disease course.** A single
acute exposure can cause a chronic disease. Use `temporality` / `clinical_course`
on the phenotype descriptor for the latter. The values carry the ATSDR ranges
(acute 1–14 days, intermediate 15–364 days, chronic 365 days and longer) as their
definitions; agencies disagree on bin boundaries, so when a source uses a
different convention pick the value whose *meaning* matches and note it, rather
than forcing the source's word onto a value with a different range.

**Not every axis applies to every agent.** Noise has no IARC group and no GHS
class — those instruments classify chemical agents. Route of exposure is a
toxicological concept for agents taken up into the body and does not apply to
acoustic energy at all; `Noise_Induced_Hearing_Loss` records `UNKNOWN` rather
than forcing an inapplicable value. Omitting an axis is correct and preferable to
inventing a value for it.

### GHS categories

Each GHS class is subdivided into numbered categories grading severity
(Carcinogenicity 1A/1B/2, acute toxicity 1–5). The category is deliberately
**not** a permissible value — the boundaries are defined per class in
class-specific terms, and flattening them into one enum would produce values that
only make sense in context. Put the category in `notes` (e.g. "Carc. 1A")
alongside the class.

## What was deliberately not encoded

Recording these keeps a future curator from assuming they were overlooked.

- **NTP *Report on Carcinogens*, EPA IRIS cancer descriptors, ACGIH TLV
  carcinogenicity notations (A1–A5).** Three national systems that re-rank
  largely the same evidence as IARC. Carrying four near-parallel carcinogen
  scales invites curators to assert a listing they have not checked. IARC is the
  WHO/international instrument and the one cited in the occupational literature
  dismech curates. If a national listing is the specific point, state it in
  `notes` with its source.
- **GBD (IHME) environmental and occupational risk-factor hierarchy.** A genuine
  sanctioned classification that would fit this module, but its exact Level 2 /
  Level 3 label set could not be verified against a primary source when the
  module was written. Transcribing an approximate hierarchy would defeat the
  purpose. Left for a follow-up working from the GBD capstone appendix.
- **ICD-10 Z57 / Z58 and ICD-11 external-cause codes.** These are *encounter and
  external-cause* codes rather than a disease nosology; the right home for them
  is `DiseaseMappings` alongside the existing `icd10cm_mappings` /
  `icd11f_mappings`, not a classification enum.
- **ISCO-08 occupations and NAICS/SIC industries.** These classify jobs and
  industries, not diseases or agents.

## How the Classifications card renders

The disorder page's Classifications card is **driven by the schema**, not by a
hardcoded list in the template: `_classification_display_spec()` reads
`DiseaseClassifications`, takes each slot's display label from its LinkML
`title`, and nests slots that declare a `slot_group` under that group. Adding a
new classification slot therefore renders with no template edit.

This replaced a hand-maintained list that had drifted — `icimd_category` (74
entries), `isds_skeletal_category` (168) and `nih_research_priority` (16) were
being curated but rendered nowhere. A test asserts every
`DiseaseClassifications` slot appears in the spec and carries a `title`, so the
gap cannot silently reopen.

It is also the one job LinkML slot groups are legitimately for: the three
occupational slots render as sub-rows under a single "Occupational Disease"
heading, with the sub-label suppressed for groups of one so a lone slot does not
repeat its own heading.

## Validation

```bash
uv run linkml-validate -s src/dismech/schema/dismech.yaml -C Disease kb/disorders/Silicosis.yaml
just validate kb/disorders/Silicosis.yaml
```

Schema validation rejects free-text values. The rendered enum pages, including
the full ILO and EU hierarchies with per-value disorder links, are generated
into `pages/classifications/` by `uv run python -m dismech.render --all`.

To list values:

```bash
uv run python -c "
from linkml_runtime.utils.schemaview import SchemaView
sv = SchemaView('src/dismech/schema/dismech.yaml')
for enum_name in ('ILOCausativeAgentEnum', 'ILODiseaseCategoryEnum'):
    e = sv.get_enum(enum_name)
    print(f'{enum_name}  (axis subset: {list(e.in_subset)}, source: {e.source})')
    for k, pv in e.permissible_values.items():
        print(('  ' if pv.is_a else '') + k)
"
```

Each value's own provenance, where it has one, is in its `source` metaslot
rather than its description — for the European schedule that is how you tell an
amendment addition from a 2003 base item:

```bash
uv run python -c "
from linkml_runtime.utils.schemaview import SchemaView
sv = SchemaView('src/dismech/schema/dismech.yaml')
for k, pv in sv.get_enum('EUOccupationalScheduleEnum').permissible_values.items():
    if pv.source:
        print(k, '->', pv.source)
"
```

## Sources

- ILO List of Occupational Diseases (revised 2010). Geneva: International Labour
  Office, 2010. ISBN 978-92-2-123795-2.
  <https://www.ilo.org/publications/ilo-list-occupational-diseases-revised-2010>
- Commission Recommendation 2003/670/EC of 19 September 2003 concerning the
  European schedule of occupational diseases (OJ L 238, 25.9.2003, p. 28).
  <http://data.europa.eu/eli/reco/2003/670/oj>
- Commission Recommendation (EU) 2022/2337 (OJ L 309, 30.11.2022) — COVID-19.
- Commission Recommendation (EU) 2025/2609 (OJ L, 2025/2609) — asbestos additions.
- IARC Monographs Preamble, amended January 2019.
  <https://monographs.iarc.who.int/iarc-monographs-preamble-preamble-to-the-iarc-monographs/>
- UN Globally Harmonized System of Classification and Labelling of Chemicals (GHS).
- ATSDR, About Minimal Risk Levels.
  <https://www.atsdr.cdc.gov/minimal-risk-levels/php/about/index.html>
- Wild CP. The exposome: from concept to utility. *Int J Epidemiol*
  2012;41(1):24–32. PMID:22296988.
