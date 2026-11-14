# Dioctophymiasis literature sweep

This curation sweep checked a human-case retrospective review and renal,
ectopic, and fatal case reports before creating
`kb/disorders/Dioctophymiasis.yaml`.

## Sources used

- **PMID:30963996** — 2019 open full-text Parasite report and retrospective
  review of 37 human dioctophymiasis cases. Used for the cases-in-literature
  count, kidney predominance, raw or undercooked fish/frog and unboiled-water
  exposures, loin pain and hematuria frequencies, occasional urinary frequency,
  urgency, fever, and anemia, morphologic diagnosis, and the statement that
  surgical removal is the only known means while standardized anthelmintic
  therapy is not established.
- **PMID:40867017** — 2025 open full-text Emerging Infectious Diseases report
  of a gastric-wall D. renale larva confirmed by morphology and sequencing.
  Used for the oligochaete, fish/amphibian, and mammalian life cycle; raw
  freshwater-fish exposure; L3 larval migrans versus patent adult infection;
  ectopic gastric-wall disease; and PCR confirmation.
- **PMID:26952087** — 2016 open full-text BMJ Case Reports renal D. renale
  infection with renal-cell carcinoma. Used only for the renal-parenchyma
  destruction mechanism and not for a cancer-causality claim, because the paper
  and PMID:30963996 both treat the tumor association as unresolved.
- **PMID:28299768** — 2017 Iranian right-kidney case report. Used for a
  concrete ultrasound/CT-detected renal mass case with operative worm removal.
- **PMID:24095916** — 2014 molecularly confirmed larval D. renale infection in a
  human subcutaneous nodule. Used for the dermal ectopic-larval phenotype and
  sequencing diagnosis.
- **PMID:21158627** — 2010 fatal bilateral renal dioctophymatosis. Used for
  renal failure after untreated bilateral kidney invasion.

## Lump/split decision

`stubs/Dioctophymiasis.yaml` carried no MONDO descendants and listed only
`Enoplea infectious disease` as a parent, so `MONDO:0000298` was curated as a
leaf infectious disease entry rather than as a grouping.

## Exclusions and term decisions

- **PMID:35137204** was fetched while surveying ectopic adult infection, but the
  fetcher could retrieve only metadata because the open PDF endpoint returned
  403. The cache was not cited.
- **Renal cell carcinoma** was not curated as a comorbidity or pathophysiologic
  consequence. Two human reports described D. renale with renal-cell carcinoma,
  but PMID:26952087 states there is no association and PMID:30963996 says the
  relationship is unclear.
- **Anthelmintic therapy** was left out of structured `treatments`. PMID:30963996
  found scattered ivermectin and albendazole successes but states that no
  strictly defined therapeutic approach exists and that surgical removal of
  worms or damaged kidney tissue is the only known means.
- **Fever and anemia** were added as reported human manifestations but were not
  linked causally from the renal-injury node because the cached review reports
  them clinically without tying them to a specific renal mechanism.
- **The gastric submucosal mass** was left unbound after HPO search for “gastric
  submucosal tumor” returned no specific term. A generic neoplasm or stomach
  abnormality binding would be misleading because the cited Korean lesion was a
  larval inflammatory mass mimicking a tumor.
- **Fish and amphibian paratenic hosts** are represented with broad NCBITaxon
  terms (`Actinopterygii`, `Amphibia`) because the human transmission route is
  raw/undercooked freshwater fish or frogs across cases, not one established
  host species.

## Cached-source follow-up pass

After the first review, the cached references under `references_cache/` were
re-read locally to check for missed mechanistic nodes, phenotypes, prevalence
evidence, diagnosis records, treatments, and ontology bindings. No external
deep-research provider was used for this follow-up pass.

### Mechanistic and clinical findings

The cached review supports keeping the pathograph split between ingested L3
larvae, the mammalian gastric-wall to hepatic migration route, adult renal
residence with parenchymal destruction, and ectopic larval residence. The
life-cycle details in PMID:40867017 describe the conserved mammalian cycle, so
animal-host background is indirect support for the human migration node rather
than direct human clinical evidence.

PMID:30963996 remains the best compact source for human frequencies and the
case count. It reviewed 32 papers with 37 human cases through October 2018,
found that 31 of 37 involved kidneys, and reported loin pain and hematuria in
22 of 37 cases each. The same clinical section lists fever, anemia, abdominal
pain, weight loss, frequent urination, urgent urination, urinary retention,
pyuria, and proteinuria as less frequent renal-case manifestations.

The ectopic-tissue evidence supports replacing a generic tissue binding with
the named sites in the cached papers: liver, abdominal cavity, retroperitoneal
space, subcutaneous tissue, and the stomach wall. The South Korean case adds a
gastric-wall mass presentation, while PMID:24095916 supports the subcutaneous
nodule presentation.

### Diagnosis and treatment findings

Morphologic identification of eggs or worms in urine or histopathologic tissue
sections remains the core diagnostic method for renal disease and ectopic
nodules. PCR followed by ribosomal or mitochondrial DNA sequencing is useful
for unusual ectopic larvae, especially where morphology overlaps Gnathostoma or
Anisakis. Renal ultrasound and computed tomography detect mass-like renal
infection but still feed into morphologic confirmation when a worm or tissue is
recovered.

Surgical or endoscopic removal remains the only structured treatment in this
entry. The human-case review notes isolated ivermectin and albendazole
successes but also states that anthelmintic treatment had not been established
as the proper course of action, so those drugs are intentionally left out of
the treatment block until stronger evidence is available.

### Ontology checks

Local OAK lookups resolved the new exact bindings used in the review patch:

- `HP:0100515` Pollakisuria for urinary frequency.
- `UBERON:0001167` wall of stomach.
- `UBERON:0003684` abdominal cavity.
- `UBERON:0003693` retroperitoneal space.
- `UBERON:0002072` hypodermis, represented with `preferred_term:`
  `subcutaneous tissue`.
- `NCIT:C16853` Microscopy.
- `NCIT:C153598` DNA Sequencing.
- `NCIT:C16502` Diagnostic Imaging Testing.
- `NCIT:C15329` Surgical Procedure.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
