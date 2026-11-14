# Rhinosporidiosis literature sweep

This curation sweep checked open reviews and recent surgical case reports before
creating `kb/disorders/Rhinosporidiosis.yaml`.

## Sources used

- **PMID:15814958** — open full-text 2005 review of unusual fungal and
  pseudofungal infections. Used for the placement of *Rhinosporidium seeberi*
  in the aquatic protistan Mesomycetozoea clade, its failure to grow in routine
  culture, trophocyte/sporangium tissue forms, the pathognomonic zonal
  sporangiospore arrangement, the historical concentration of cases in India
  and Sri Lanka, freshwater associations, non-contagiousness, localized
  nasopharyngeal and ocular conjunctival disease, histopathologic diagnosis,
  and surgical excision as the core treatment.
- **PMID:33269573** — 2020 taxonomy and epidemiology review. Used to cross-check
  the 18S rDNA placement in the aquatic-parasite DRIP/Mesomycetozoa clade, the
  hydrophilic uncultivated organism, common stagnant-water exposure history,
  and total excision with electro-cauterization as first-line therapy.
- **PMID:33289469** — 2020 clinical case report and literature review. Used for
  the pathophysiology, life-cycle, and transmission review; the probable free
  endospore inoculation of injured nasal epithelium; no documented family or
  animal-to-human cross-infection; the nasal, ocular, cutaneous, and
  disseminated forms; histopathologic confirmation; and recurrence after
  incomplete excision.
- **PMID:35180588** — 2022 nasal case report. Used for contemporary
  histopathology showing thick-walled sporangia and endospores in multiple
  developmental stages in a nasal mass removed by endoscopic excision.
- **PMID:38440563** — 2024 coblation case series. Used for the anatomic
  frequency of nasopharyngeal and oculosporidiosis presentations, epistaxis and
  nasal obstruction as common findings, and coblation-assisted excision with
  six months of dapsone as a recurrence-reduction strategy after
  histopathologic confirmation.

## Lump/split decision

`stubs/Rhinosporidiosis.yaml` carried no MONDO descendants and listed only
`parasitic Ichthyosporea infectious disease` as a parent, so it was curated as a
leaf infectious disease rather than a grouping.

## Exclusions and term decisions

- **Other named Mesomycetozoea or DRIP-clade organisms** were left out of the
  structured `infectious_agent`. The review literature names *R. seeberi* as the
  human rhinosporidiosis agent and mentions Dermocystidium, Ichthyophonus,
  Psorospermium, and the Rosette agent only to explain taxonomic placement.
- **A definitive aquatic host** was left unstructured because reviews frame
  fish or other aquatic animals as a plausible natural-host hypothesis that
  still needs investigation, while human infection is linked more directly to
  contaminated stagnant or freshwater exposure.
- **Sporangium and endospore stages** were modeled in prose rather than bound to
  OPL. The cached life-cycle terms cover reusable parasitic worm or protozoan
  stages, whereas these R. seeberi tissue forms are histopathologic morphology
  and are not required for cross-disease stage search.
- **Nasal polypoid mass** was left unbound after an OLS HPO search for
  `nasal polyp` returned only `HP:0100582` Nasal polyposis. That term would be
  too specific for the usual solitary unilateral polypoid mass described in
  rhinosporidiosis.
- **Nasal obstruction** was kept in the nasal-polypoid-mass phenotype
  description and not made a separate phenotype because epistaxis and the
  polypoid mass already capture the two best-supported nasal manifestations
  with exact or intentionally unbound local descriptors.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
