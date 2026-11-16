# Dicrocoeliasis literature sweep

This curation sweep checked true human case reports and egg-positive case
series before creating `kb/disorders/Dicrocoeliasis.yaml`.

## Sources used

- **PMID:27895270** — open full-text 2016 Spanish reference-unit series.
  Used for the distinction between true ant-acquired infection and spurious
  raw-liver egg transit, the egg morphology, liver-free-diet confirmation, and
  treatment recommendations for true versus spurious infection.
- **PMID:33720847** — 2021 true *Dicrocoelium* spp. infection in a visiting
  friends-and-relatives traveler from Ghana. Used for the snail/ant life cycle,
  West African *D. hospes* scope, eosinophilia and symptom resolution after
  praziquantel, and the rare cholangitis or biliary-obstruction spectrum.
- **PMID:20220269** — open full-text true *D. dendriticum* infection in Turkey.
  Used for adult flukes in the gallbladder and bile ducts, right-upper-quadrant
  pain, weight loss, chronic watery diarrhea, persistent egg shedding after
  liver-free diet, and single-dose triclabendazole response.
- **PMID:2260188** — 1990 Saudi series of 208 patients with *D. dendriticum*
  ova in stool. Used for the mixture of true and spurious infections in a large
  stool-positive clinical series and the frequency of symptoms, liver-function
  disturbance, eosinophilia, biliary disease, and praziquantel response in that
  series.
- **PMID:19602926** — 2009 true *D. dendriticum* infection. Used for
  eosinophilia, elevated bilirubin, and albendazole response in a confirmed
  human case.

## Lump/split decision

`stubs/Dicrocoeliasis.yaml` carried no MONDO descendants and listed only
`helminthiasis` as a parent, so `MONDO:0005729` was curated as a leaf infectious
disease entry rather than as a grouping.

## Exclusions and term decisions

- **Agent species** were kept in prose under a genus-level
  `infectious_agent`. OLS resolves *D. dendriticum* and *D. hospes*
  separately, but the MONDO disease scope is dicrocoeliasis rather than
  species-specific infection, and recent true West African infections are
  reported as *Dicrocoelium* spp.
- **The sporocyst, cercaria, and slime-ball snail phases** were left in the
  broader lifecycle prose. The human clinical papers document the required
  snail and ant intermediate hosts; the CDC DPDx lifecycle fills in the exact
  daughter-sporocyst/cercaria/snail-mucus detail, but that level was not needed
  to support the pathograph.
- **Spurious egg passage** was kept as a diagnostic confounder rather than a
  pathophysiology node or a transmission route because eggs traversing the human
  intestine after liver ingestion are evidence against true biliary infection.
- **Praziquantel, triclabendazole, and albendazole** were bound after review.
  Praziquantel and albendazole were already in the local ChEBI cache;
  `runoak -i ols:chebi search triclabendazole` returned `CHEBI:94759`
  6-chloro-5-(2,3-dichlorophenoxy)-2-(methylthio)-1H-benzimidazole.
- **Right-upper-quadrant pain** was left bound to generic `HP:0002027`
  Abdominal pain because OLS HPO searches for `right upper quadrant pain` and
  `hypochondriac pain` returned no right-hypochondrial abdominal-pain class.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
