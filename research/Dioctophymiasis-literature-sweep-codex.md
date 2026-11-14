# Dioctophymiasis literature sweep

This curation sweep checked a human-case retrospective review and renal,
ectopic, and fatal case reports before creating
`kb/disorders/Dioctophymiasis.yaml`.

## Sources used

- **PMID:30963996** — 2019 open full-text Parasite report and retrospective
  review of 37 human dioctophymiasis cases. Used for the cases-in-literature
  count, kidney predominance, raw or undercooked fish/frog and unboiled-water
  exposures, loin pain and hematuria frequencies, morphologic diagnosis, and the
  statement that surgical removal is the only known means while standardized
  anthelmintic therapy is not established.
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
- **The gastric submucosal mass** was left unbound after HPO search for “gastric
  submucosal tumor” returned no specific term. A generic neoplasm or stomach
  abnormality binding would be misleading because the cited Korean lesion was a
  larval inflammatory mass mimicking a tumor.
- **Fish and amphibian paratenic hosts** are represented with broad NCBITaxon
  terms (`Actinopterygii`, `Amphibia`) because the human transmission route is
  raw/undercooked freshwater fish or frogs across cases, not one established
  host species.

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
