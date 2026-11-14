---
disease_name: Dicrocoeliasis
mondo_id: MONDO:0005729
provider: codex-local-cached-source-pass
source_set: cached PR references
external_provider_used: false
---

# Dicrocoeliasis: cached-source completeness pass

This is a local completeness pass produced from the PubMed references already
cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:27895270 | Open full-text Spanish reference-unit series. Used for true-versus-spurious egg passage, the Dicrocoelium life-cycle overview, human infection after infected-ant ingestion, usually asymptomatic true infection, chronic cholangitis with bile-duct dilatation causing weight loss and fatigue, stool microscopy with liver-free-diet confirmation, and praziquantel/triclabendazole treatment of true infection. |
| PMID:33720847 | True Dicrocoelium spp. infection in a traveler visiting friends and relatives in Ghana. Used for Dicrocoelium hospes scope, snail/ant intermediate-host background, diarrhea and right-hypochondrial pain in a confirmed true case, eosinophilia with normal ultrasound and chemistry, praziquantel therapy, symptom and eosinophilia resolution, and the broader reported phenotype spectrum including abdominal distension, constipation, vomiting, transaminase elevation, and hepatomegaly. |
| PMID:20220269 | Open full-text true D. dendriticum infection in Turkey. Used for adult biliary residence, right-upper-quadrant pain, weight loss, chronic watery diarrhea, elevated alkaline phosphatase and IgE, persistent egg shedding after liver-free diet, and clearance after single-dose triclabendazole. |
| PMID:2260188 | Saudi 208-patient stool-positive clinical series. Used for the mixture of true and spurious infections, liver-function disturbance, eosinophilia, biliary disease, and the 4/9 praziquantel response. |
| PMID:19602926 | Confirmed true D. dendriticum infection. Used for eosinophilia and hyperbilirubinemia before albendazole therapy, and normalization of blood parameters after albendazole. |

## Completeness cross-check

- The genus-level `Dicrocoelium` agent remains scoped to both D. dendriticum
  and likely West African D. hospes cases.
- True ant-acquired infection and spurious egg passage after raw liver ingestion
  remain separated in the disease description, epidemiology, diagnosis, and
  treatment notes.
- The lifecycle evidence now uses `evidence_source: OTHER` for parasite and
  animal-host biology sentences rather than treating those background
  statements as direct human-clinical observations.
- The former "Biliary Irritation and Obstruction" node is renamed to
  `Bile-Duct Inflammation and Dilatation`, making its edges to cholangitis and
  biliary obstruction downstream manifestations rather than synonyms.
- Weight loss and fatigue are wired downstream of bile-duct inflammation and
  dilatation using the direct PMID:27895270 cause sentence.
- Elevated transaminases, hepatomegaly, fatigue, abdominal distension,
  constipation, and vomiting were all rechecked against PMID:33720847 and added
  as phenotype rows.
- Eosinophilia now has a dedicated host-response node and additional support
  from the 208-patient Saudi series.
- Praziquantel, triclabendazole, and albendazole now have structured NCIT
  pharmacotherapy rows with CHEBI agent bindings; the triclabendazole binding
  follows `runoak -i ols:chebi search triclabendazole`, which returned
  `CHEBI:94759`.

## Deferred or bounded items

- The CDC DPDx lifecycle detail remains out of the pathograph because the cached
  clinical sources already establish the required snail and ant intermediate
  hosts and metacercarial ingestion route.
- Spurious egg passage remains a diagnostic confounder and not a transmission
  route because eaten eggs or adult worms passing through the intestine do not
  establish adult biliary infection.
- The right-upper-quadrant/hypochondrial abdominal-pain wording remains bound
  to generic HPO `HP:0002027` Abdominal pain because OLS HPO searches for
  `right upper quadrant pain` and `hypochondriac pain` returned no specific
  right-hypochondrial abdominal-pain class.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
