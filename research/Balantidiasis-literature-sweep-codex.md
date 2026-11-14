# Balantidiasis literature sweep

This curation sweep checked recent and classic Balantidiasis reviews, a human
systematic review, open full-text environmental/life-cycle material, and human
clinical reports before creating `kb/disorders/Balantidiasis.yaml`.

## Sources used

- **PMID:18854484** — open full-text Clinical Microbiology Reviews synthesis
  of *Balantidium coli* biology, epidemiology, pathogenesis, diagnosis, and
  treatment. Used for the direct cyst-trophozoite life cycle, pig fecal cyst
  contamination of water, cecum/colon habitat, flask-shaped submucosal lesions,
  uncertain hyaluronidase contribution to ulceration, the chronic clinical
  presentation with nonbloody diarrhea and abdominal pain, stool microscopy, and
  tetracycline/metronidazole treatment.
- **PMID:35146143** — open full-text review on *Balantioides coli* cyst
  detection and viability assessment in environmental samples. Used for the
  current Balantioides/Balantidium synonymy, trophozoite and cyst stages,
  faecal-oral food/water transmission, infective cyst framing, and the statement
  that infected hosts range from asymptomatic infection to life-threatening
  colitis.
- **PMID:34339668** — systematic review and meta-analysis of human
  balantidiasis through 2020. Used for the association between pig proximity and
  B. coli positivity, the `CASES_IN_LITERATURE` prevalence record, and the
  predominant dysentery symptom in the reviewed human literature.
- **PMID:33183780** — recent Research in Veterinary Science review using the
  current genus name *Balantioides*. Used for the infectious-agent identity,
  main pig reservoir, epidemiologic risk factors, asymptomatic/chronic/acute
  symptomatic progression spectrum, and iodoquinol treatment row.
- **PMID:31688855** — human fatal colonic balantidiasis case report and review.
  Used for colonoscopy/fresh-sample/biopsy diagnosis and the rare intestinal
  perforation phenotype.
- **PMID:35734242** — open full-text human stool-microscopy case report. Used
  for stool wet mount diagnosis, abdominal pain, tenesmus, and a contemporary
  metronidazole-treated human case.
- **PMID:1190365** — human metronidazole treatment series. Used as primary
  support for metronidazole-associated parasitologic clearance in 20 human
  balantidiasis cases.

## Lump/split decision

`stubs/Balantidiasis.yaml` carries no MONDO descendants and lists `Ciliophora
infectious disease`, `parasitic intestinal disorder`, and `protozoa infectious
disease` as parents, so it was curated as a leaf infectious disorder.

The entry binds the agent to `NCBITaxon:71585` *Balantioides coli* rather than
to a broad ciliate or legacy-only label. Modern reviews treat *B. coli* as
*Balantioides coli* while retaining *Balantidium coli* as a synonym, and the
2021 review identifies it as the only confirmed human-parasitizing ciliate.

## Exclusions

- **Environmental food, water, and soil detection rates** were left out of
  `prevalence`. The open 2022 review reports many cyst-detection methods across
  environmental matrices, but it warns that protocols are not standardized and
  that microscopy-only cyst identification can be ambiguous.
- **Other proposed reservoirs**, including camels, cattle, donkeys, sheep, and
  goats, were mentioned in the life-cycle evidence but not modeled as host
  descriptors. The same review describes pigs as the main reservoir, and adding
  lower-confidence host records would have overstated their role in human
  transmission.
- **Extraintestinal balantidiasis** was left out of the mechanism graph. The
  systematic review found 27 extraintestinal infections and genitourinary
  colonization was common among those reports, but the graph here focuses on
  the conserved intestinal pathograph and avoids giving rare ectopic cases
  equal weight.

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
