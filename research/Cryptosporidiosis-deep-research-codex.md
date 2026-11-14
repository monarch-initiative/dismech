# Cryptosporidiosis: cached-source completeness pass

This is a local literature sweep produced from the PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:37764167 | Full-text pediatric Cryptosporidium/Giardia review. Used for the genus-level agent, C. hominis/C. parvum predominance, environmental oocysts, mammalian small-intestinal infection, person-to-person and waterborne transmission, epithelial attachment/injury, TNF-alpha/IL-8 inflammation, barrier dysfunction with fluid-electrolyte imbalance, diarrhea/abdominal pain/vomiting/fever/respiratory manifestations, malnutrition and stunted growth, MBL2 susceptibility, diagnostic modalities, nitazoxanide positioning, and supportive care. |
| PMID:27219054 | Global Enteric Multicenter Study burden analysis. Used for the African-infant Cryptosporidium-attributable moderate-to-severe diarrhea incidence estimate with a person-years denominator. |
| PMID:23440042 | IL21R-deficiency human report. Used for biliary and duodenal Cryptosporidium infection, chronic cholangitis, liver fibrosis, and severe cellular-immunodeficiency host context. |
| PMID:11398117 | Randomized double-blind Egyptian nitazoxanide trial. Used for nitazoxanide clinical benefit in responsive cryptosporidial diarrhea. |
| PMID:12423984 | Zambian pediatric randomized trial. Used for nitazoxanide benefit in HIV-seronegative children and for the link between persistent pediatric cryptosporidiosis, malnutrition, and mortality. |
| PMID:11103042 | HIV-positive case series after highly active antiretroviral therapy. Used for antiretroviral immune restoration and organism eradication in AIDS-related intestinal cryptosporidiosis. |
| PMID:19212310 | AIDS-related cholangiopathy review. Used for advanced HIV/AIDS, active HIV replication plus C. parvum biliary epithelial injury, and the protective role of antiretroviral therapy against AIDS cholangiopathy. |
| PMID:22459705 | CD40 agonism study in X-linked hyper-IgM biliary cryptosporidiosis. Used for CD40LG deficiency as a susceptibility context and for refractory biliary C. hominis infection in XHM patients. |

## Completeness cross-check

- The entry stays deliberately lumped at the genus-level MONDO term and records C. hominis and C. parvum as the predominant human etiologic species rather than splitting by species.
- The life-cycle and transmission sections capture environmentally resistant oocysts, excystation in the mammalian small intestine, intracellular epithelial infection, person-to-person spread, contaminated water and food, and person-to-person or household exposure.
- The pathophysiology graph now separates ingestion/excystation, intracellular epithelial infection, epithelial injury, lamina-propria inflammation and cytokine signaling, barrier dysfunction with fluid-electrolyte imbalance, excess fluid loss, nutrient malabsorption, and severe-immunodeficiency biliary persistence.
- Prolonged diarrhea, malnutrition, and growth delay are now causally downstream of excess intestinal fluid loss or nutrient malabsorption; dehydration is downstream of fluid loss.
- Severe host susceptibility is represented from HIV/AIDS, CD40LG deficiency, IL21R deficiency, and MBL2 susceptibility evidence rather than as a generic “immunodeficiency” bucket.
- Nitazoxanide is kept as a small-molecule antiparasitic treatment with trial support and response-context caveats; antiretroviral therapy targets the HIV/AIDS host defect; supportive fluid/electrolyte care targets the dehydration branch.
- Diagnostics include stool microscopy, stool antigen detection, and nucleic-acid amplification, with the PCR row carrying the precise NCIT nucleic-acid amplification term.

## Deferred or bounded items

- Transplant and oncology host settings were not modeled because they are not supported by the cached pull-request source set at the same specificity as the HIV/AIDS, IL21R, CD40LG, and MBL2 rows.
- Calf or ruminant exposure was not forced into `agent_life_cycle.hosts`: the cached broad review says many non-human species occur in mammals and that C. parvum was described from mice and other mammals, but it also emphasizes that most human infection is now due to C. hominis or person-to-person C. parvum rather than classic zoonosis.
- High-income-country outbreaks such as Milwaukee were left out of `prevalence:` because the cached source uses them as waterborne-outbreak examples, not as stable incidence or prevalence estimates.
- Post-infectious sequelae such as reactive arthritis or persistent functional gastrointestinal symptoms were not modeled because the cached sources used here support acute/prolonged diarrhea, pediatric malnutrition and growth effects, and biliary disease in severe immune deficiency, but not a snippet-verified post-infectious mechanism.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
