---
provider: claude_managed
model: claude-opus-5-5
cached: false
start_time: '2026-11-09T12:19:24.682400'
end_time: '2026-11-09T12:31:42.830425'
duration_seconds: 738.15
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Chronic Traumatic Encephalopathy
  mondo_id: MONDO:0043512
  category: Neurological Disorder
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    retriever_model: claude-haiku-5-5
    max_iterations: 5
    max_cost_usd: 20.0
    allowed_hosts: []
    max_repair_rounds: 2
    poll_interval: 15.0
    timeout: 5400
    session_id: sesn_01Ro6cnPMgGsyHDb23pr1TQB
    delete_session: false
run_metadata:
  session_id: sesn_01Ro6cnPMgGsyHDb23pr1TQB
  agent_id: agent_01K5k8H6H4Uxic777boZvtbf
  agent_version: 1
  environment_id: env_01NDhAwC4BsT39w6UteFeYkq
  retriever_model: claude-haiku-5-5
  stop_reason: end_turn
  outcome_result: satisfied
  workflow_runs: 2
  tool_calls: 56
  outcome_iterations: 2
  grader_explanation: "An independent grader found all criteria met:\n\n- Research\
    \ report rubric (evidence, traceability, alignment, relevance, structure, coverage)\
    \ (met): I checked REPORT.md (110 KB), PLAN.md and 178 evidence files in citations/.\n\
    \nEvidence: Every evidence file has key, identifiers, title, source_url and content.\
    \ Each body is retrieved source text (abstracts or verbatim excerpts under '##\
    \ Text'), not an agent summary. My script found no PubMed source_url whose PMID\
    \ differs from the file's identifiers. One formatting flaw: in about 32 files\
    \ (e.g. mez-2017, katz-2021), all the IDs are packed into one comma-joined YAML\
    \ string rather than separate list items. The IDs are still present and match\
    \ the source_url.\n\nTraceability: Every PMID, DOI and NCT cited in the report\
    \ body appears in an evidence file's identifiers; the agent's check.py reported\
    \ 165 cited IDs with none missing. All 234 quoted strings matched the cited evidence\
    \ file word for word. Claims carry inline IDs throughout.\n\nAlignment: I spot-checked\
    \ the following against their sources and all were supported:\n- Daneshvar 2026:\
    \ onset at 63.4 and death at 73.1 years\n- Lehman 2012: neurodegenerative mortality\
    \ SMR 2.83, and AD/ALS about fourfold\n- Daneshvar 2021: ALS mortality SMR 3.94\n\
    - Rowson 2014: concussion relative risk 46.1%\n- Miner 2024: AUC 0.742\n- Corsellis\
    \ epilepsy collection (PMID:39528258): community-study range of 0\u20138%\n- Wiegand\
    \ 2026: FA associated with CTE certainty\n- PMID:41589584: stage I/II not associated\
    \ with symptoms, and low-stage manifestation uncertain\n- Female footballer letter\
    \ (PMID:37391669)\n\nThe report states disagreements openly: causality (Bradford\
    \ Hill vs 'premature' vs CDC), suicide, inexorable progression, TES accuracy estimates,\
    \ prevalence by sampling frame, and the year the term 'CTE' was coined.\n\nRelevance:\
    \ Nearly all sources are primary studies or authoritative reviews. Web pages (CDC,\
    \ ICD list, MedLink) are used only for policy and identifier points, and preprints\
    \ and conference abstracts are flagged as such. No section rests on a single source.\n\
    \nStructure: The report follows the 15 sections the task specifies. It opens with\
    \ an interpretation and a summary of main findings, names the causal gene ('none')\
    \ in the first paragraph, and flags the MONDO:0043512 vs MONDO:0019976 discrepancy.\
    \ It gives ontology CURIEs (HP, GO, CL, UBERON, CHEBI, NCIT, NCBITaxon, HGNC)\
    \ backed by OLS/HGNC evidence files. It includes an HPO phenotype table with frequencies,\
    \ a numbered and branched causal chain, an Open Questions section, and a References\
    \ section with one line per source giving its ID, citation and evidence file.\
    \ Some later sections (10\u201313, 15) lean on bullet lists, but the template's\
    \ required format takes precedence.\n\nCoverage: All 12 sub-questions in PLAN.md\
    \ are answered. Template items that do not apply (Mendelian inheritance, genetic\
    \ testing, immunization, OMIA) are set aside with reasons.\n\nThe only flaws are\
    \ minor (the identifier list formatting, and some citations of an HGNC MAPT URL\
    \ for other genes that are nonetheless covered in the same evidence file), so\
    \ this fully meets the criterion."
  input_tokens: 956
  output_tokens: 555735
  cache_read_input_tokens: 56541716
  web_search_requests: 74
  web_fetch_requests: 0
  list_cost_usd: 14.45
  active_seconds: 3887.548
  evidence_check:
    evidence_files: 178
    cited_identifiers: 135
    cited_without_evidence: []
    quotes_checked: 129
    quotes_anchored: 129
    unanchored_quotes: []
  repair_rounds: 1
  repair_history:
  - evidence_files: 178
    cited_identifiers: 135
    cited_without_evidence: []
    quotes_checked: 129
    quotes_anchored: 127
citation_count: 165
reference_validation:
  total_references: 135
  verified: 135
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 126
  quotes_valid: 100
  quotes_unsupported: 26
  unsupported_quote_references:
  - PMID:40239644
  - PMID:42341996
  - PMID:28742910
  - PMID:23966253
  - PMID:33826224
  - PMID:36759368
  - PMID:25904048
  - PMID:32774238
  - PMID:35862387
  - PMID:37456643
  - PMID:37803386
  - PMID:30285061
  - PMID:39728882
  - PMID:34255876
  quotes_not_checkable: 3
  relevance_assessed: 135
  on_topic: 109
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 146
  verified: 128
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 123
  labels_matching: 104
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0043512
    reported_labels:
    - if available
    - dementia due to head trauma; post-traumatic brain syndrome; post-traumatic dementia
    - traumatic encephalopathy
    ontology_label: traumatic encephalopathy
  - term_id: MONDO:0019976
    reported_labels:
    - A tauopathy characterized by progressive neurodegeneration secondary to repetitive
      mild traumatic brain injuries
    - chronic traumatic encephalopathy
    - Boxer's dementia; chronic traumatic encephalopathy; dementia pugilistica; punch-drunk
      syndrome
    ontology_label: chronic traumatic encephalopathy
  - term_id: HP:0001251
    reported_labels:
    - Ataxia; nearest term
    ontology_label: Ataxia
  - term_id: GO:0008017
    reported_labels:
    - microtubule binding; normal tau function lost on hyperphosphorylation, inferred
    ontology_label: microtubule binding
  - term_id: GO:0042552
    reported_labels:
    - myelination; white matter loss, inferred
    ontology_label: myelination
  - term_id: CL:0000598
    reported_labels:
    - pyramidal neuron; layer 2/3 sulcal neurons are lost
    ontology_label: pyramidal neuron
  - term_id: CL:0000669
    reported_labels:
    - pericyte; neurovascular unit, inferred
    ontology_label: pericyte
  labels_variant: 12
  not_configured: 7
  not_configured_terms:
  - MESH:D000070627
  - Orphanet:97353
  - DOID:0081291
  - UMLS:C0149843
  - SCTID:230283005
  - MEDGEN:508441
  - GARD:0019371
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 179
artifact_sources:
  claude_managed: 179
artifacts:
- filename: PLAN.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/PLAN.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PY3HbJ4WnNrRFAH1BK6jJG
  description: null
- filename: abdolmohammadi-2020-genetics-of-cte-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/abdolmohammadi-2020-genetics-of-cte-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01YLE5kuCX6JK6UR2TV6s7et
  description: null
- filename: abdolmohammadi-2024-ice-hockey-duration.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/abdolmohammadi-2024-ice-hockey-duration.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01FEpPoAr4xzarj25CrLUKeU
  description: null
- filename: ackermans-2021-unconventional-animal-models.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ackermans-2021-unconventional-animal-models.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016dVtZXQepm2mePfYgJx5cy
  description: null
- filename: ackermans-2022-headbutting-bovids.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ackermans-2022-headbutting-bovids.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011Lt4Titf1qqArTsH7ZKDXo
  description: null
- filename: acs-2017-cte-brief-historical-overview.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/acs-2017-cte-brief-historical-overview.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01G9tgZ2djquxZ1vP9NT1MkD
  description: null
- filename: adams-2024-substantia-nigra-contact-sports.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/adams-2024-substantia-nigra-contact-sports.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01WaYaD6yZKP9S3nZhfBUR6y
  description: null
- filename: alosco-2017-age-first-exposure-neuropsychiatric-outcomes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2017-age-first-exposure-neuropsychiatric-outcomes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01AL1g794DEfXrFCpr2k8ppS
  description: null
- filename: alosco-2018-age-first-exposure-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2018-age-first-exposure-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_015TGHULMACLW6ip3UZWKnhr
  description: null
- filename: alosco-2020-tau-deposition-mckee-staging.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2020-tau-deposition-mckee-staging.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01K3wNDmQZ1kve9ENpsbkRqu
  description: null
- filename: alosco-2021-diagnose-cte-design.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2021-diagnose-cte-design.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01DHUwNX7cEtE7bLF5PNg4qV
  description: null
- filename: alosco-2023-flortaucipir-postmortem.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2023-flortaucipir-postmortem.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PTyMLwxcDzDQb8kAFUi4oE
  description: null
- filename: alosco-2024-regional-tau-pathology-cte-correlates.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2024-regional-tau-pathology-cte-correlates.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01KXNJePv3S83hnQUoVWzvjK
  description: null
- filename: arciniega-2024-cavum-septum-diagnose.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/arciniega-2024-cavum-septum-diagnose.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01DrKKK84hgTb1LDpbe7YPAT
  description: null
- filename: arena-2026-performance-tes-criteria-cte-nc.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/arena-2026-performance-tes-criteria-cte-nc.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01DecCJwgagzVvoYuVcbmqNR
  description: null
- filename: asken-2022-biomarkers-rhi-tes-clinicopathological-series.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/asken-2022-biomarkers-rhi-tes-clinicopathological-series.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01W5jvpJ6P62A8PqCkqLCbwi
  description: null
- filename: atherton-2020-gwas-cte-abstract.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/atherton-2020-gwas-cte-abstract.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Y86hX8yG71EtKHgHDKcxXL
  description: null
- filename: atherton-2022-apoe-genotypes-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/atherton-2022-apoe-genotypes-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_014z2kzNbhXYjspVTpHwhMvL
  description: null
- filename: bieniek-2015-cte-pathology-neurodegenerative-brain-bank.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2015-cte-pathology-neurodegenerative-brain-bank.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01LmEuVHhsJYc5AX3PszAApZ
  description: null
- filename: bieniek-2020-contact-sports-mayo-cohort.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2020-contact-sports-mayo-cohort.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0198kKjUtK9Byko8UK5uUsoR
  description: null
- filename: bieniek-2021-second-ninds-nibib-consensus.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2021-second-ninds-nibib-consensus.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01P1TCYhMXsPKTry4gWnmCWg
  description: null
- filename: biorxiv-2025-injury-cte-like-multicellular-model.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/biorxiv-2025-injury-cte-like-multicellular-model.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0126w4JR6nhBRKGZFFrRNZLH
  description: null
- filename: braun-2020-mechanical-injury-neurons-tau.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/braun-2020-mechanical-injury-neurons-tau.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Kruo54aAeUoVmV2LhAUqyd
  description: null
- filename: breen-2020-preclinical-treatment-cte-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/breen-2020-preclinical-treatment-cte-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01AJMDmugkqmU9ZRVcSMn6fA
  description: null
- filename: breen-2026-contact-sports-dna-methylation-preprint.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/breen-2026-contact-sports-dna-methylation-preprint.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Kg16zFhvUr8Cgt57WWd7o4
  description: null
- filename: bruce-2023-football-parkinson-disease.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bruce-2023-football-parkinson-disease.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016XFWUDLhcf1Cs3Z4Gs6zeC
  description: null
- filename: butler-2022-tau-primarily-neuronal.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/butler-2022-tau-primarily-neuronal.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013vo1UTrBFLbcZVvomRCNdA
  description: null
- filename: butler-2025-repeated-head-trauma-neuron-loss.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/butler-2025-repeated-head-trauma-neuron-loss.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01W58DsPpHsKk6yY4RphZuKB
  description: null
- filename: cantu-2019-management-chronic-traumatic-encephalopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cantu-2019-management-chronic-traumatic-encephalopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Qj8dW9wh32ndwtiYxq8f1G
  description: null
- filename: castellani-2017-dementia-pugilistica-revisited.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/castellani-2017-dementia-pugilistica-revisited.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Cgjhp628hefXVVpfWWHqc3
  description: null
- filename: cdc-2024-about-repeated-head-impacts.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cdc-2024-about-repeated-head-impacts.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01GLHeKdCnvz8PqF4XDRGqcm
  description: null
- filename: chancellor-2021-oligodendroglia-astroglia.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/chancellor-2021-oligodendroglia-astroglia.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VJLBuJhVyQJJTUugx5NeoN
  description: null
- filename: cherry-2016-microglial-neuroinflammation-tau.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2016-microglial-neuroinflammation-tau.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PN1xUSkzqhj7Q6z8MD6bDN
  description: null
- filename: cherry-2017-ccl11-cns-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2017-ccl11-cns-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_017Zkbkij3eHWVY49DPKvb4z
  description: null
- filename: cherry-2018-tmem106b-variation-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2018-tmem106b-variation-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01DhD5Nrm4bk1ShMSvDuwkA8
  description: null
- filename: cherry-2020-ccl2-microglia-recruitment.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2020-ccl2-microglia-recruitment.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01AAdRJWwJPKzrY6kJcN1qeM
  description: null
- filename: clinicaltrials-nct02003183-fddnp-pet-cte-risk.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02003183-fddnp-pet-cte-risk.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XXhaQz9R3qGefeyQCMHk2K
  description: null
- filename: clinicaltrials-nct02266563-amyloid-tauopathy-pet-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02266563-amyloid-tauopathy-pet-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01WeKk358RtFM29p4nRgJXdZ
  description: null
- filename: clinicaltrials-nct02460094-biib092-mad-psp.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02460094-biib092-mad-psp.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011bVizfurFhkKtb5EkswMUP
  description: null
- filename: clinicaltrials-nct02959294-adipose-stromal-cells-withdrawn.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02959294-adipose-stromal-cells-withdrawn.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Pa2AM9UgUtotHsCcY5d6GX
  description: null
- filename: clinicaltrials-nct03068468-gosuranemab-psp-passport.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03068468-gosuranemab-psp-passport.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01UeYspWpVStwRGt3g1mfh6d
  description: null
- filename: clinicaltrials-nct03218332-post-concussion-athletes-cte-biomarkers.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03218332-post-concussion-athletes-cte-biomarkers.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011jVnHQ8TgUtH7wUkswwgx3
  description: null
- filename: clinicaltrials-nct03352557-gosuranemab-early-ad.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03352557-gosuranemab-early-ad.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VzLtnBLN9UgQQBn4yQTWbm
  description: null
- filename: clinicaltrials-nct04796207-fish-oil-football-subconcussion.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct04796207-fish-oil-football-subconcussion.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Lj17p1j3Cm7d4pxTqGnudQ
  description: null
- filename: clinicaltrials-nct04928534-blood-biomarkers-tes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct04928534-blood-biomarkers-tes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Kn8kYicyZbkm6h3Mqj3jpf
  description: null
- filename: clinicaltrials-nct05490576-tau-connectomics-tes-pet.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct05490576-tau-connectomics-tes-pet.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01FfvTBfoQzoCMoW5v777RAG
  description: null
- filename: crary-2014-primary-age-related-tauopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/crary-2014-primary-age-related-tauopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01La7prMMLNU1fcL4t7dkzZS
  description: null
- filename: cummings-2023-therapeutic-landscape-tauopathies.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cummings-2023-therapeutic-landscape-tauopathies.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01D6wSBYJ3U7p72zqKEjERk9
  description: null
- filename: dams-oconnor-2023-intimate-partner-violence-neuropathology.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dams-oconnor-2023-intimate-partner-violence-neuropathology.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01EfpBPqZ93th4RiffX2XYHy
  description: null
- filename: daneshvar-2021-als-incidence-mortality-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/daneshvar-2021-als-incidence-mortality-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01RXxiDVXdho1Wfhzaxvq8zm
  description: null
- filename: daneshvar-2026-cte-prevalence-at-death-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/daneshvar-2026-cte-prevalence-at-death-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01CgVLExmwUVDWqha6yfG2iw
  description: null
- filename: dickstein-2021-blast-rats-tau-biomarkers.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dickstein-2021-blast-rats-tau-biomarkers.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Moeg9NxZB2YG9BLfHdpb9g
  description: null
- filename: dong-2025-somatic-genomic-alterations-neurons.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dong-2025-somatic-genomic-alterations-neurons.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01GuRuPDUt7BnRRxwMT3TTK1
  description: null
- filename: eagle-2024-premortem-cte-diagnosis-football-exposures.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/eagle-2024-premortem-cte-diagnosis-football-exposures.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013HaDNFiyaGfMhLu2Ehn5Ea
  description: null
- filename: esin-2025-chronic-traumatic-encephalopathy-review-russian.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/esin-2025-chronic-traumatic-encephalopathy-review-russian.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016gzQWMcuhvaLKbLMAta28W
  description: null
- filename: falcon-2019-novel-tau-filament.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/falcon-2019-novel-tau-filament.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01JhFRyXG5CYvethpVQNVcUV
  description: null
- filename: farah-2018-woodpecker-tau.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/farah-2018-woodpecker-tau.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013vv437i2RzmddaEiYxwmFJ
  description: null
- filename: fortington-2025-epidemiological-principles-rhi-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/fortington-2025-epidemiological-principles-rhi-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_015ammhudM3LLtmtX1srBvYh
  description: null
- filename: frontiers-2024-non-mammalian-models-injury.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/frontiers-2024-non-mammalian-models-injury.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0139c5GEkWR7uENabXPYRHCD
  description: null
- filename: frontiers-2024-preclinical-tbi-models-overview.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/frontiers-2024-preclinical-tbi-models-overview.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_014zn96AvQ6227akb9m2cqT3
  description: null
- filename: gallini-2026-bias-adjusted-prevalence-cte-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/gallini-2026-bias-adjusted-prevalence-cte-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_018UadJFb6dbvMyBKEfm2DQP
  description: null
- filename: gardner-2015-evaluating-treating-neurobehavioral-symptoms-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/gardner-2015-evaluating-treating-neurobehavioral-symptoms-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01EkHvaGoBfHsiz7DCX5c9aJ
  description: null
- filename: goldstein-2012-blast-mouse-model.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/goldstein-2012-blast-mouse-model.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012Cp3PbfkyyWihuApLWEv6M
  description: null
- filename: grashow-2024-perceived-cte-suicidality-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/grashow-2024-perceived-cte-suicidality-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01R9hp53w7qwUwUvoXXibH2U
  description: null
- filename: han-2025-mapt-h1-haplotype-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/han-2025-mapt-h1-haplotype-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XHMea65r8tJBrJKBr77pKh
  description: null
- filename: hartman-2025-tmem106b-microglia-cytokines.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hartman-2025-tmem106b-microglia-cytokines.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01KUdxZz3hKwgb6NXB3QJr2e
  description: null
- filename: hearn-2022-active-rehabilitation-tauopathies-umbrella-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hearn-2022-active-rehabilitation-tauopathies-umbrella-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Rx2r6aJnaRsWskZmPMBVdu
  description: null
- filename: hearn-2024-person-centred-active-rehabilitation-suspected-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hearn-2024-person-centred-active-rehabilitation-suspected-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012NNfic7N7AVYKzVqDEheG4
  description: null
- filename: hgnc-genes-cte-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hgnc-genes-cte-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01JosLr16U5PVMK9Kf2NsbzS
  description: null
- filename: icdlist-2026-icd10cm-f07-81-postconcussional-syndrome.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/icdlist-2026-icd10cm-f07-81-postconcussional-syndrome.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01FNRvzJWpzdBqUXFsTZ8sik
  description: null
- filename: iverson-2019-cte-not-inexorably-progressive.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2019-cte-not-inexorably-progressive.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01NdwqrmqpS7BR6mDdZgtPUQ
  description: null
- filename: iverson-2019-mild-cte-no-contact-sports.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2019-mild-cte-no-contact-sports.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01KqwDzwG85xs2wGc6kx73aX
  description: null
- filename: iverson-2023-cte-nc-uncommon-amateur-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2023-cte-nc-uncommon-amateur-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01R3RYWB2x33P4NqaEHfM7MN
  description: null
- filename: jansson-2026-csf-biomarkers-diagnose.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/jansson-2026-csf-biomarkers-diagnose.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01LXZXSHV5An1ojf9yLhvYPZ
  description: null
- filename: jun-2026-cte-devastating-legacy-repetitive-concussion.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/jun-2026-cte-devastating-legacy-repetitive-concussion.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_014VFb6KGaPekRGCXXWJiK3R
  description: null
- filename: kamps-2025-enlarged-cavum-neuroimaging.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kamps-2025-enlarged-cavum-neuroimaging.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012QZcCBhJnA9UTkiJzyJVNW
  description: null
- filename: katz-2021-nindd-traumatic-encephalopathy-syndrome-criteria.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/katz-2021-nindd-traumatic-encephalopathy-syndrome-criteria.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Lmwae5bUzZPz7uJzcsftSp
  description: null
- filename: katzenberger-2013-drosophila-closed-head-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/katzenberger-2013-drosophila-closed-head-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012WyJm6yFyUfhs5CVWcpYKv
  description: null
- filename: kawamura-2023-pharmacological-treatment-suspected-cte-challenges.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kawamura-2023-pharmacological-treatment-suspected-cte-challenges.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0126xU28D6S594dBuwnxz3To
  description: null
- filename: kenney-2018-dementia-moderate-severe-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kenney-2018-dementia-moderate-severe-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01SvAoewLtPPJz3xGR3nkiQV
  description: null
- filename: kim-2023-legal-medicine-multidisciplinary-tes-management.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kim-2023-legal-medicine-multidisciplinary-tes-management.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01DpsAm9gU32FYXY4yVme1H3
  description: null
- filename: kimura-2026-chimera-tau-transgenic.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kimura-2026-chimera-tau-transgenic.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0198BRMAxgG1YNk1ykKztpeg
  description: null
- filename: kirsch-2023-vascular-injury-rhi-tau.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kirsch-2023-vascular-injury-rhi-tau.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011TWtHknLpyA7q7ZukJEnag
  description: null
- filename: kleven-2026-tes-multidomain-indices.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kleven-2026-tes-multidomain-indices.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01SMmhkmkZLp9v8AJ2ADXUbr
  description: null
- filename: koerte-2016-cavum-septi-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/koerte-2016-cavum-septi-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013FUh6jk5EBZpDwJoTvU95g
  description: null
- filename: kovacs-2016-artag-harmonized.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kovacs-2016-artag-harmonized.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01KzwXG3Lc4cyYHDwuV2td2V
  description: null
- filename: labadorf-2023-early-late-cte-gene-expression.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/labadorf-2023-early-late-cte-gene-expression.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_015XU6MAjThNfJk27A1CqUn6
  description: null
- filename: lai-2024-kcnj2-organoid-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lai-2024-kcnj2-organoid-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016H91ChCbknspR5f74LcM1v
  description: null
- filename: layden-2026-cte-neuropathology-dementia-symptoms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/layden-2026-cte-neuropathology-dementia-symptoms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016Bif2niBoLJqyWVxfYcL2F
  description: null
- filename: lehman-2012-neurodegenerative-causes-of-death-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lehman-2012-neurodegenerative-causes-of-death-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01QaBUyBs7An3xpbML3gPUuC
  description: null
- filename: liang-2023-qeeg-former-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/liang-2023-qeeg-former-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01V6jtkpuqyDN9wnDDqcHvoy
  description: null
- filename: ling-2017-mixed-pathologies-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ling-2017-mixed-pathologies-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01JCcMZ8zDXncyMv3tDf3c8t
  description: null
- filename: lobue-2025-cognitive-impairment-dementia-cte-meta-analysis.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lobue-2025-cognitive-impairment-dementia-cte-meta-analysis.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01MHj9mP21KRGVXGNGJW83Zp
  description: null
- filename: luster-2026-neurodegenerative-mortality-nfl.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/luster-2026-neurodegenerative-mortality-nfl.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01V1gnDrMBdPTgPnsg2rS1jp
  description: null
- filename: mackay-2019-neurodegenerative-disease-mortality-soccer.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mackay-2019-neurodegenerative-disease-mortality-soccer.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01HdHJNKXRsZtB2n2Yq84B93
  description: null
- filename: mccrory-2007-evidence-cte-boxing.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mccrory-2007-evidence-cte-boxing.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01USXRWNbTKf2TwNMWRyQQ35
  description: null
- filename: mckee-2009-cte-athletes-progressive-tauopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2009-cte-athletes-progressive-tauopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Vm5Jm4GvNXyGN6UEJAmSHA
  description: null
- filename: mckee-2010-tdp43-proteinopathy-mnd.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2010-tdp43-proteinopathy-mnd.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01SR9S8RZZNiX66HnFEVyKot
  description: null
- filename: mckee-2013-spectrum-disease-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2013-spectrum-disease-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Kr6HUNTW2qiDwq2gEP1BxE
  description: null
- filename: mckee-2015-neuropathology-cte-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2015-neuropathology-cte-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Cq23ubdVnRetuVRRL6Gjat
  description: null
- filename: mckee-2016-first-ninds-nibib-consensus.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2016-first-ninds-nibib-consensus.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VZTy3zt4AxK8LyVe14faSC
  description: null
- filename: mckee-2023-cte-criteria-repetitive-head-impacts.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2023-cte-criteria-repetitive-head-impacts.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012S6sZvbmvtuqzxcxeYcxjd
  description: null
- filename: mckee-2023-young-contact-sport-athletes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2023-young-contact-sport-athletes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01J8QDJ3t5LQ3PLZg7vWLCXF
  description: null
- filename: medlink-chronic-traumatic-encephalopathy-history-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/medlink-chronic-traumatic-encephalopathy-history-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01GDBhKnJgjzxsEZc9RxFXaB
  description: null
- filename: melchior-2026-dyrk1a-repetitive-head-injury.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/melchior-2026-dyrk1a-repetitive-head-injury.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Hwr3nHnb86WPoxzidrbmCD
  description: null
- filename: mesh-2017-d000070627-chronic-traumatic-encephalopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mesh-2017-d000070627-chronic-traumatic-encephalopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_019wk4pZZM9Pa8bwKTRgt83T
  description: null
- filename: mez-2017-clinicopathological-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2017-clinicopathological-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01UCAzY1ZLYRxgDuN5MsgT4r
  description: null
- filename: mez-2020-duration-football-play.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2020-duration-football-play.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01EVU9BeHgN9mLkUkNdsAM5T
  description: null
- filename: mez-2021-validity-2014-tes-criteria.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2021-validity-2014-tes-criteria.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_018FUqTZbATf12T4udqFL8ai
  description: null
- filename: mez-2026-validity-ninds-tes-criteria-preprint.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2026-validity-ninds-tes-criteria-preprint.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01TZpUCnzFwJxbDWuTrCKxxE
  description: null
- filename: miner-2024-plasma-biomarkers-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/miner-2024-plasma-biomarkers-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XkX8rkitDeTn8nSTeGF6kr
  description: null
- filename: miner-2026-plasma-ptau217-rhi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/miner-2026-plasma-ptau217-rhi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Tqk4ynpxZu3ACS7n2JdPyM
  description: null
- filename: montenigro-2014-clinical-subtypes-tes-criteria.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/montenigro-2014-clinical-subtypes-tes-criteria.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XUaxj2BPHZRV5L1iT9t39R
  description: null
- filename: moraga-amaro-2025-rat-rmtbi-florzolotau.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/moraga-amaro-2025-rat-rmtbi-florzolotau.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01A4kBVzSw3our8ixxwixqB6
  description: null
- filename: moszczynski-2018-pthr175-tau-phosphorylation.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/moszczynski-2018-pthr175-tau-phosphorylation.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Voz8tQ5b1szT9cRZUSFXDD
  description: null
- filename: mouzon-2019-no-tau-pathology-tg-model.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mouzon-2019-no-tau-pathology-tg-model.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016FRS1DvVwhSwkaVsijYHuv
  description: null
- filename: ncbi-clinvar-omim-gwas-catalog-check-2026.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ncbi-clinvar-omim-gwas-catalog-check-2026.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Vw8f3bGX9v4HLttUwYrQ6C
  description: null
- filename: nowinski-2022-bradford-hill-repetitive-head-impacts.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/nowinski-2022-bradford-hill-repetitive-head-impacts.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01AavZ5x3YCm6zQfRrMLz7X7
  description: null
- filename: ojo-2013-repetitive-mild-tbi-hTau-mice.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ojo-2013-repetitive-mild-tbi-hTau-mice.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01JkHWL4Q3sExngtcoLVnK5Z
  description: null
- filename: ojo-2016-repetitive-head-trauma-mice-to-men.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ojo-2016-repetitive-head-trauma-mice-to-men.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01BmD2Q13QhiHFeCMeej7dNj
  description: null
- filename: ols-2026-mondo-0019976-chronic-traumatic-encephalopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-2026-mondo-0019976-chronic-traumatic-encephalopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01D3FzG3y6HRqxbKaKCKJJNc
  description: null
- filename: ols-2026-mondo-0043512-traumatic-encephalopathy.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-2026-mondo-0043512-traumatic-encephalopathy.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01LBAdCFki2ZdjHDeaSHMpmN
  description: null
- filename: ols-chebi-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-chebi-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016mmcMs2ptaE2MksFJCEtMB
  description: null
- filename: ols-cl-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-cl-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XxPZVQroCNB7k353Dfbepm
  description: null
- filename: ols-go-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-go-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Gep6xYmSao4CkooTUzqfNH
  description: null
- filename: ols-hp-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-hp-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_016vfi7NNGpEV3Kmkf89xTri
  description: null
- filename: ols-mondo-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-mondo-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01BEN36S2cX5Ufzj4VrAreyg
  description: null
- filename: ols-ncbitaxon-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-ncbitaxon-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_019CiKagAv9RL5M2CaxSYtFj
  description: null
- filename: ols-ncit-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-ncit-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01WkbZfupQmhHPzNRbHpS2kd
  description: null
- filename: ols-spotcheck-2026-mondo-0019976-parents.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-spotcheck-2026-mondo-0019976-parents.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011czUFZSLwMcW6iB22hnuwH
  description: null
- filename: ols-uberon-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-uberon-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01JFuA2kfbyXzc2xLcztxvvU
  description: null
- filename: omalu-2005-cte-national-football-league-player.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/omalu-2005-cte-national-football-league-player.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01WoDTo2UaMqW9yNVLsGY1FA
  description: null
- filename: omalu-2011-histomorphologic-phenotypes-cte-athletes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/omalu-2011-histomorphologic-phenotypes-cte-athletes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01CuP9Aoc5jcktyy82LzYPZs
  description: null
- filename: ontology-supplement-chebi-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-chebi-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VfjxQWm6ikdWio6dQ4whUW
  description: null
- filename: ontology-supplement-cl-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-cl-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011W6fGRoSsL3XAA2T9YP8TC
  description: null
- filename: ontology-supplement-go-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-go-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VrypaCaDF4v1EEdRs5Kmrv
  description: null
- filename: ontology-supplement-hp-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-hp-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01CMtPqv6WzPmcLXi9qfN2A2
  description: null
- filename: ontology-supplement-mondo-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-mondo-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01UrCbzd3pAfbzET7ea22MgL
  description: null
- filename: ontology-supplement-ncit-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-ncit-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01CFErXUbKggQ8RrQwfpmEnj
  description: null
- filename: ontology-supplement-uberon-terms.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-uberon-terms.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01U8brChVZnquy2W3K8EiDwy
  description: null
- filename: oup-2018-martland-history-punch-drunk.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/oup-2018-martland-history-punch-drunk.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01BhQVpsQVstNL2NqS2RB4aC
  description: null
- filename: patricios-2023-amsterdam-2022-consensus-concussion-sport.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/patricios-2023-amsterdam-2022-consensus-concussion-sport.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Hn5H52woqi8Q6HsQXcHAK5
  description: null
- filename: pennington-2026-proteomic-proteasome-ribosome.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/pennington-2026-proteomic-proteasome-ribosome.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01MGPEkAtFtxAsPDHYqYyPaV
  description: null
- filename: perivascular-2025-glial-reactivity-ptau-lesions.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/perivascular-2025-glial-reactivity-ptau-lesions.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_0198Rcw1JvUv4iHP5FRAZGdY
  description: null
- filename: petraglia-2014-repetitive-mild-tbi-mouse-model.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/petraglia-2014-repetitive-mild-tbi-mouse-model.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01B2jjxmZPuFAErrfBEA7TKK
  description: null
- filename: pfaller-2019-rule-limiting-full-contact-practice.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/pfaller-2019-rule-limiting-full-contact-practice.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XimU6PRfnp22TSHgqK9FbL
  description: null
- filename: priemer-2022-military-personnel-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/priemer-2022-military-personnel-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01UVLWoS3GJgxqF6oqS1ZQ6T
  description: null
- filename: qi-2025-prevalence-athletes-meta-analysis.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/qi-2025-prevalence-athletes-meta-analysis.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01HJKC9yvsjKB6yB2i9cyjdA
  description: null
- filename: rodriguez-2026-population-based-sao-paulo-cohort.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rodriguez-2026-population-based-sao-paulo-cohort.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01P2e3iwdupEGEMiMmbHfSP1
  description: null
- filename: rossi-2023-emerging-symptomatic-treatment-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rossi-2023-emerging-symptomatic-treatment-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01MbzJ72unc1bGQBNNSapn63
  description: null
- filename: rowson-2014-helmet-design-concussion-football.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rowson-2014-helmet-design-concussion-football.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01FivfzfZpVrzPj3wRgFXvoF
  description: null
- filename: russell-2020-mental-health-suicide-soccer.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/russell-2020-mental-health-suicide-soccer.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013d4AfbeRQwMftWBeWCrsnw
  description: null
- filename: russell-2021-field-position-career-length-soccer.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/russell-2021-field-position-career-length-soccer.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Wp38QNydUEowqgaCNU81Xj
  description: null
- filename: ryniejska-2025-corsellis-epilepsy-collection.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ryniejska-2025-corsellis-epilepsy-collection.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01KeYZ3mZur2WuE3kSRLsugu
  description: null
- filename: sacramento-2020-anti-phospho-tau-gene-therapy-cte-mouse.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/sacramento-2020-anti-phospho-tau-gene-therapy-cte-mouse.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PmmUPH6ZbP5QV7LDPFJrrp
  description: null
- filename: schaffert-2021-tes-frequency-retired-athletes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/schaffert-2021-tes-frequency-retired-athletes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01XV6NjMQdWd6JiGXm95vAuJ
  description: null
- filename: selmanovic-2025-community-autopsy-late-effects-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/selmanovic-2025-community-autopsy-late-effects-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01LgViK5SoPCTogtScvY6hZb
  description: null
- filename: shatirishvili-2026-fluid-biomarkers-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/shatirishvili-2026-fluid-biomarkers-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01H1CPHF7snFhS4dNqsMjRtw
  description: null
- filename: shively-2017-localized-cortical-cte-axonal-injury.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/shively-2017-localized-cortical-cte-axonal-injury.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PXUuaYpc3sVs36McpZWNKY
  description: null
- filename: smoliga-2018-reconsidering-woodpecker-model.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/smoliga-2018-reconsidering-woodpecker-model.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_012qdJLRb3DWWDncJKSKHwkC
  description: null
- filename: smoliga-2026-beaks-to-brains-woodpecker.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/smoliga-2026-beaks-to-brains-woodpecker.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01S3ivxgAGzHgwBd3CEYfFHG
  description: null
- filename: stamm-2015-age-first-exposure-nfl-cognition.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stamm-2015-age-first-exposure-nfl-cognition.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01EUT9KBpVU2AbJep4aL85Ls
  description: null
- filename: stathas-2022-tau-ser202-ser396.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stathas-2022-tau-ser202-ser396.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01J2FtG4y7pRCSBjBwtAAs8g
  description: null
- filename: stern-2013-clinical-presentation-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stern-2013-clinical-presentation-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01C4CMTqc9DKZWmrv8Mr96XB
  description: null
- filename: su-2024-flortaucipir-diagnose.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/su-2024-flortaucipir-diagnose.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01HwPx768Upz1mJSPMvEQVmG
  description: null
- filename: suter-2022-australian-sports-brain-bank-first-three-years.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/suter-2022-australian-sports-brain-bank-first-three-years.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PB71QRnT7hKnJWKiUM7DN9
  description: null
- filename: suter-2023-chronic-traumatic-encephalopathy-female-afl-footballer.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/suter-2023-chronic-traumatic-encephalopathy-female-afl-footballer.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_017MmHrccajgDjC2xqRGYN4y
  description: null
- filename: tbicoe-2023-cte-research-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/tbicoe-2023-cte-research-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_013tL6SLDgA2Tnyn5yUEprwh
  description: null
- filename: va-dod-2021-post-acute-mtbi-guideline-landing.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/va-dod-2021-post-acute-mtbi-guideline-landing.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01YVJpGyc2Ugc7X27BmDtuu4
  description: null
- filename: varlow-2023-tau-radiotracers-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/varlow-2023-tau-radiotracers-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01AHHUXuUi631F8rzYLbjexN
  description: null
- filename: vrillon-2026-flortaucipir-ptau217-differential.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/vrillon-2026-flortaucipir-ptau217-differential.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VVsaaKcEaDjwbAyVSJYwxk
  description: null
- filename: wahlquist-2024-youth-soccer-heading-exposure-clinical-measures.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wahlquist-2024-youth-soccer-heading-exposure-clinical-measures.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01LRYZoZ3F18d9hc8WUDysav
  description: null
- filename: walsh-2024-substance-use-football-players.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/walsh-2024-substance-use-football-players.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01PJBY9AuUyKRaGnfHbjNRiK
  description: null
- filename: whelan-2023-ncaa-kickoff-rule-change.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/whelan-2023-ncaa-kickoff-rule-change.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01T4aMZC6s3P83rUNLW7Y6cG
  description: null
- filename: wiebe-2018-ivy-league-experimental-kickoff-rule.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wiebe-2018-ivy-league-experimental-kickoff-rule.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01Sq3fdEZayabEQHZnrNVrXC
  description: null
- filename: wiegand-2026-gm-wm-diffusion-tes.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wiegand-2026-gm-wm-diffusion-tes.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_011bqvoYwa9mA57TdWx629Ly
  description: null
- filename: wortzel-2013-cte-suicide-systematic-review.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wortzel-2013-cte-suicide-systematic-review.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01VM11mTxiu4eMHMmakDc9dL
  description: null
- filename: yu-2023-neuronal-tau-white-matter-tbi.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/yu-2023-neuronal-tau-white-matter-tbi.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01G7WMDeetH1uerxzBZVrtKy
  description: null
- filename: yun-2026-brain-microphysiological-ad-cte.md
  path: Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/yun-2026-brain-microphysiological-ad-cte.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01TkyHjhRK6V1RruTzpXTg2v
  description: null
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Traumatic Encephalopathy
- **MONDO ID:** MONDO:0043512 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Neurological Disorder

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Chronic Traumatic Encephalopathy** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Ontology terms

Where a concept you discuss belongs to one of these ontologies, give its term as a CURIE followed by the term's label in brackets, in the form `PREFIX:ID (term label)`: MONDO, HP, GO, CL, UBERON, CHEBI, NCIT, NCBITaxon, HGNC. Use no other ontologies for this. Give only identifiers you have looked up, not ones recalled from memory, and leave a concept without a term rather than guess one.

## Output

# Chronic Traumatic Encephalopathy (CTE): Disease Characteristics Review

## Interpretation and Scope

**Causal gene: none.** Chronic traumatic encephalopathy is an acquired, environmentally caused neurodegenerative tauopathy. It has no Mendelian causal gene and no OMIM disease entry. The disease protein is tau, encoded by HGNC:6893 (MAPT), which aggregates in a hyperphosphorylated form but is not mutated. Susceptibility is modified by common variants in HGNC:613 (APOE), HGNC:22407 (TMEM106B) and the MAPT 17q21.31 haplotype region. A database check found no ClinVar records for CTE, no OMIM entry titled for CTE (the only OMIM hits were the FTDP-17 entry 600274 and the MAPT entry 157140), and no GWAS Catalog results (https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy).

**Identifier discrepancy (important for the knowledge base).** The template gives MONDO:0043512. In the EBI Ontology Lookup Service that ID is labelled "traumatic encephalopathy", with the definition "Encephalopathy resulting from trauma." and synonyms "dementia due to head trauma; post-traumatic brain syndrome; post-traumatic dementia" (MONDO:0043512). The MONDO class that carries the CTE name, synonyms and the CTE-specific definition is MONDO:0019976 (chronic traumatic encephalopathy), defined as "A tauopathy characterized by progressive neurodegeneration secondary to repetitive mild traumatic brain injuries" (MONDO:0019976). In OLS, the parents of MONDO:0019976 are MONDO:0001627 (dementia) and MONDO:0005574 (tauopathy) (https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0019976/parents). I followed the disease **name** and category (Neurological Disorder) and researched CTE. MONDO:0043512 is best read as a broader, generic traumatic-encephalopathy concept. Curators should decide whether the entry should be keyed to MONDO:0019976.

**Evidence types.** Nearly all human evidence comes from aggregated research cohorts, mostly brain-bank autopsy series and clinicopathological case series, plus population cohort mortality studies and living-athlete biomarker cohorts. None of it comes from EHR-derived individual patient records. Each claim below is marked as human clinical, human post-mortem, model organism, in vitro or computational where relevant.

**Ontology terms.** All CURIEs were looked up in EBI OLS4 and HGNC REST by a retriever (evidence files `citations/ols-*-terms.md`, `citations/ontology-supplement-*-terms.md`, `citations/hgnc-genes-cte-terms.md`, `citations/ols-2026-mondo-*.md`). A concept with no exact match is left without a term.

## Summary of Main Findings

CTE is defined only neuropathologically. Its pathognomonic lesion is a perivascular accumulation of hyperphosphorylated tau in neurons, with or without astrocytes, at the depths of cortical sulci (PMID:26667418; PMID:33611507; PMID:36759368). It can be diagnosed definitively only at autopsy. Its proposed clinical counterpart is traumatic encephalopathy syndrome (TES) (PMID:33722990). The necessary exposure is repetitive head impacts (RHI), most often from contact sports and sometimes from military service. In American football, risk follows a dose–response pattern: "The odds of CTE double every 2.6 years of football played" (PMID:31589352). Ice hockey shows the same pattern (PMID:39630446).

Frequencies differ sharply between sources. CTE is very common in donated brains of elite contact-sport athletes, for example 110 of 111 NFL players (PMID:28742910) and a selection-bias-adjusted 74.5% of deceased NFL players (PMID:42949744). It is rare in unselected population autopsy cohorts, for example 0.6% in São Paulo (PMID:41627284). Tau filaments in CTE have a distinct cryo-EM fold (PMID:30894745). The pathology spreads in an ordered pattern described by McKee stages I–IV (PMID:23208308), with frequent TDP-43 co-pathology. Neuroinflammatory, vascular and white-matter changes, together with somatic DNA alterations, are documented in human tissue (PMID:27793189; PMID:36617181; PMID:34019156; PMID:41166474; PMID:40963024).

There is no validated in-life biomarker. There is no disease-modifying therapy and no CTE-specific therapeutic trial. Prevention rests on reducing RHI exposure. Whether RHI causes CTE, how specific the lesion is, whether it always progresses, and how far it explains clinical symptoms are all still debated (PMID:35937061; PMID:39277838; PMID:31670780; PMID:41589584).

---

## 1. Disease Information

**Overview.** MeSH defines CTE as "Degenerative brain disease linked to repetitive brain trauma. Progressive symptoms may include MEMORY LOSS; AGGRESSION; or DEPRESSION." (MESH:D000070627). The 2016 NINDS/NIBIB consensus panel "defined the pathognomonic lesion of CTE as an accumulation of abnormal hyperphosphorylated tau (p-tau) in neurons and astroglia distributed around small blood vessels at the depths of cortical sulci and in an irregular pattern" (PMID:26667418). The second consensus meeting kept this definition. It proposed "a minimum threshold for CTE diagnosis and an algorithm for the assessment of CTE severity as \"Low CTE\" or \"High CTE\"" (PMID:33611507). A later review states that the pathognomonic lesion consists of "a perivascular accumulation of neuronal phosphorylated tau (p-tau) variably alongside astrocytic aggregates at the depths of the cortical sulci" and that "CTE can be definitively diagnosed only by postmortem neuropathological examination; the corresponding clinical condition is known as traumatic encephalopathy syndrome (TES)" (PMID:36759368).

**Identifiers.**
- MONDO: MONDO:0019976 (chronic traumatic encephalopathy) is the CTE class. The template's MONDO:0043512 (traumatic encephalopathy) is a generic class (see Interpretation) (MONDO:0019976; MONDO:0043512).
- MeSH: D000070627 "Chronic Traumatic Encephalopathy", "dateIntroduced: 2017-01-01" (MESH:D000070627).
- Orphanet: Orphanet:97353, from the MONDO cross-reference. The Orphanet page itself could not be retrieved (MONDO:0019976).
- Other cross-references on MONDO:0019976: DOID:0081291, UMLS:C0149843, SCTID:230283005, MEDGEN:508441, GARD:0019371.
- NCIT: a second lookup confirmed that NCIT has no term labelled chronic traumatic encephalopathy. NCIT:C35542 (Traumatic Encephalopathy) is the nearest term and maps to MONDO:0043512 (MONDO:0043512).
- ICD-10-CM: there is no dedicated code. F07.81 "Postconcussional syndrome" is "Also documented as - Chronic traumatic encephalopathy" (https://icdlist.com/icd-10/F07.81).
- ICD-11: no CTE code was verified. MONDO:0043512 carries only an ICD-11 foundation ID, icd11.foundation:1673722101, for the generic "traumatic encephalopathy" (MONDO:0043512).
- OMIM: not applicable; there is no CTE entry.

**Synonyms and history.** MONDO lists the exact synonyms "Boxer's dementia; chronic traumatic encephalopathy; dementia pugilistica; punch-drunk syndrome" (MONDO:0019976). The syndrome was "formally recognized in the medical literature in 1928" as punch drunk syndrome, and the punch-drunk "terminology was replaced by the less derisive 'dementia pugilistica' in 1937" (PMID:29036831). Martland's 1928 paper "documented 23 examples of boxers" (https://academic.oup.com/brain/article/141/1/318/4774567). Secondary sources disagree on when the term "chronic traumatic encephalopathy" was established. One says it was "cemented as the medical diagnosis" by Critchley in 1949 (DOI:10.1021/acschemneuro.7b00291). Another says "Critchley is widely credited with popularizing the term “chronic traumatic encephalopathy” in 1957" (https://www.medlink.com/articles/chronic-traumatic-encephalopathy). The modern era of CTE in American football begins with the 2005 autopsy of a retired NFL player (PMID:15987548). The clinical counterpart, traumatic encephalopathy syndrome (TES), was formalised in 2014 research criteria (PMID:25580160) and in the 2021 NINDS consensus criteria (PMID:33722990).

**Source of information.** The data are aggregated and disease-level. They come from brain banks such as the VA-BU-CLF/UNITE bank (PMID:28742910), Mayo Clinic (PMID:26518018; PMID:31199537), the Australian Sports Brain Bank (DOI:10.5694/mja2.51420) and the University of São Paulo Biobank (PMID:41627284). Other sources are population mortality cohorts (PMID:31633894; PMID:42534468) and prospective living-athlete cohorts (PMID:34384490).

## 2. Etiology

### Disease causal factors

The primary cause is environmental and mechanical: repetitive head impacts (RHI). These include concussive and subconcussive impacts, mostly from contact and collision sports. "Over 97% of CTE cases published have been reported in individuals with known exposure to repetitive head impacts (RHI)" (PMID:36759368). In the Mayo neurodegenerative brain bank, "CTE pathology was not detected in 198 individuals without exposure to contact sports, including 33 individuals with documented single-incident TBI" (PMID:26518018). A Bradford Hill analysis "found convincing evidence of a causal relationship between RHI and CTE, as well as an absence of evidence-based alternative explanations" (PMID:35937061). A counterpoint argues that "assertions of causality having been established are premature" (PMID:39277838). The CDC's position is that "There is no strong evidence that shows that getting one or more concussions (or other mild traumatic brain injuries) or occasional hits to the head leads to CTE" (https://www.cdc.gov/traumatic-brain-injury/about/repeated-head-impacts.html). No infectious or genetic primary cause has been identified.

### Risk factors

**Exposure dose (strongest evidence; human post-mortem).** In 266 deceased American football players, "More years of football played were associated with having CTE (odds ratio [OR] = 1.30 per year played" and with CTE severity (OR = 1.14 per year). "Sensitivity and specificity were maximized at 11 years played", and simulations suggested the association was robust to brain-bank selection (PMID:31589352). In 77 ice hockey players, "CTE was found in 5 of 26 donors (19.2%) who played fewer than 13 years, 14 of 27 donors (51.9%) who played 13 to 23 years, and 23 of 24 donors (95.8%) who played more than 23 years of hockey" (OR per year 1.34) (PMID:39630446). Level of play also matters. Mez et al. reported CTE in "3 of 14 high school (21%), 48 of 53 college (91%), 9 of 14 semiprofessional (64%), 7 of 8 Canadian Football League (88%), and 110 of 111 National Football League (99%) players" (PMID:28742910). In under-30 donors, football careers were longer in those with CTE (mean difference 2.81 years) (PMID:37639244).

**Sport and setting.** CTE "has been reported in amateur and professional athletes, including a bull rider, boxers, wrestlers, and American, Canadian, and Australian rules football, rugby union, rugby league, soccer, and ice hockey players" (PMID:36759368). In a military brain bank, "All brains with CTE were from decedents who had participated in contact sports". Blast exposure was not significantly associated with CTE (relative risk 1.71; 95% CI 0.46 to 6.37), and the authors note that small numbers "preclude causal conclusions" (PMID:35675177). Among women with intimate partner violence, no CTE-NC was found in 14 prospective cases or in 70 archival cases (PMID:37897548). Boxing is the historical exposure. For modern boxing, "No current epidemiological evidence exists to determine the prevalence of this condition in modern day boxing" (PMID:17503873). Epilepsy with recurrent TBI is a further setting: CTE-NC was found in 15.7% of the Corsellis epilepsy collection (PMID:39528258).

**Single TBI.** Evidence that a single moderate or severe TBI causes CTE is weak. It rests on case reports of mixed proteinopathy after moderate-severe TBI (PMID:29155947) and on one community-cohort case with two severe isolated TBIs and no known RHI (PMID:41108192).

**Age at first exposure.** Age at first exposure "was not associated with CTE pathological severity". However, "every 1 year younger participants began to play tackle football predicted earlier reported cognitive symptom onset by 2.44 years" (PMID:29710395). Starting tackle football before age 12 was associated with worse later-life neuropsychiatric and executive measures (PMID:28926003; PMID:25632088).

**Sex.** Almost all reported cases are male. The landmark series was "all males" (PMID:23208308). The Mayo series was "largely observed in men (except for one woman)" (PMID:31199537). One woman with CTE was found among young donors (PMID:37639244). A 2023 letter reported "the first case of CTE in a former professional female footballer", whose findings "fulfill current diagnostic criteria for low-stage CTE". The authors note that "there have been only a handful of CTE cases reported in females" (PMID:37391669).

**Age.** CTE stage rises with age: "older age was associated with increased odds for having a higher CTE stage" (PMID:32778942).

**Lifestyle and confounders.** In 429 football players, "Substance use treatment had no associations with neuropathological endpoints" (PMID:39269838). In the Mayo registry, cases with CTE pathology had higher frequencies of antemortem "alcohol abuse" (PMID:31199537). Depression was the strongest correlate of a self-reported premortem "CTE diagnosis" (OR 9.5). This reflects clinical labelling rather than etiology (PMID:37798551).

### Genetic risk factors (modifiers; human post-mortem)

All genetic evidence comes from post-mortem association studies of RHI-exposed brain donors. The effects are modest and depend on age. The best-studied modifier is APOE. In 364 RHI-exposed donors, "Among donors older than 65 years, APOEε4 status was significantly associated with CTE stage (odds ratio [OR], 2.34 [95% CI, 1.30-4.20]". Yet "There was no significant association for CTE status" and "No associations were observed for APOEε2 status" (PMID:35759276). So ε4 appears to affect severity among people who already have CTE, not whether CTE occurs.

TMEM106B shows the same pattern, though the findings are framed differently across studies. In 86 CTE cases, the rs3173615 minor allele frequency was no different from controls (0.42 vs 0.43). Within cases, however, the minor allele was associated with less p-tau, less CD68 neuroinflammation and less dementia (PMID:30390709). A later study of 323 donors framed the common genotype as the risk genotype: "Among donors > 65 years old, the TMEM106B risk genotype was associated with increased CTE stage (OR = 2.748 [95% CI 1.183-6.383], p = 0.019)". In donors aged 65 or younger it was associated with dementia (OR 6.912) (PMID:41264095).

The MAPT region on chromosome 17q21.31 has also been studied. In 447 European-ancestry donors, "The H1β1γ1 haplotype was significantly associated with dementia and semi-quantitative tau burden in multiple cortical and medial temporal regions commonly affected in CTE" (PMID:40239644). An earlier Mayo study observed "a slight increase in MAPT H1 haplotype" (PMID:26518018).

Genome-wide evidence is minimal. A single conference abstract (n=175) reports that "Two loci achieved genome-wide significance", in PIP5K1B (rs63565460) and ABAT (rs12447028). No peer-reviewed paper or replication was found (https://alz-journals.onlinelibrary.wiley.com/doi/abs/10.1002/alz.046505; conference abstract).

### Protective factors

Genetic protection is supported only by case-only analyses. In these, the TMEM106B rs3173615 minor allele "may have a protective effect on CTE-related outcomes" (PMID:30390709). The APOE ε2 allele, which protects against Alzheimer disease, showed no association with CTE (PMID:35759276). The main modifiable protective factor is lower cumulative RHI exposure, meaning fewer years of play (PMID:31589352) and a lower level of play (PMID:28742910). Rule changes that limit full-contact practice reduce concussions, but no study has yet shown that they reduce CTE (Section 13). No dietary or lifestyle protective factor has been demonstrated.

### Gene–environment interactions

Genetic effects are reported as years-of-play equivalents. "Among football players, the APOEε4 association size for CTE stage was similar to playing more than 7 years of football" (PMID:35759276). The TMEM106B risk-genotype effect was "comparable to the effect of playing > 8 years of contact sports" (PMID:41264095). For MAPT, "having a copy of the H1β1γ1 allele conferred a similar risk of pathological tau accumulation to playing 9.6 years of football" (PMID:40239644). A 2026 review summarises that genetic contributions "are thought to act primarily as modifiers of disease susceptibility and progression rather than direct causal drivers" (PMID:42341996). Somatic genome sequencing suggests that disease involves more than exposure alone: "the absence of similar changes in RHI neurons without CTE suggests that CTE involves mechanisms beyond RHI alone" (PMID:41166474).

## 3. Phenotypes

The clinical phenotype has been reconstructed mainly from retrospective informant interviews with relatives of brain donors. These interviews were conducted blind to pathology (PMID:23966253; PMID:28742910). Symptoms are frequent, but whether low-stage CTE itself causes symptoms is disputed (PMID:41589584; PMID:37639244).

**Symptom domains and frequencies.** In 36 autopsy-confirmed athletes, "A triad of cognitive, behavioral, and mood impairments was common overall, with cognitive deficits reported for almost all subjects. Three subjects were asymptomatic at the time of death" (PMID:23966253). In the 2017 football series: "Among 27 participants with mild CTE pathology, 26 (96%) had behavioral or mood symptoms or both, 23 (85%) had cognitive symptoms, and 9 (33%) had signs of dementia. Among 84 participants with severe CTE pathology, 75 (89%) had behavioral or mood symptoms or both, 80 (95%) had cognitive symptoms, and 71 (85%) had signs of dementia" (PMID:28742910). A literature review of 202 cases lists "impairments in mood (for example, depression and hopelessness), behavior (for example, explosivity and violence), cognition (for example, impaired memory, executive functioning, attention, and dementia), and, less commonly, motor functioning (for example, parkinsonism, ataxia, and dysarthria)" (PMID:25580160). By stage, McKee et al. reported "Symptoms in stage I chronic traumatic encephalopathy included headache and loss of attention and concentration. Additional symptoms in stage II included depression, explosivity and short-term memory loss. In stage III, executive dysfunction and cognitive impairment were found, and in stage IV, dementia, word-finding difficulty and aggression were characteristic" (PMID:23208308).

**Phenotype table.** The main frequency source is Table 3 of the 2017 football series. It covers 111 American football players with CTE whose informants completed standardized reports, split into mild CTE (stages I–II, n = 27) and severe CTE (stages III–IV, n = 84). Each cell gives n (%) as printed in the source (PMID:28742910). The authors note that "Symptom frequencies remained similar when only pure CTE cases (ie, those with no neuropathological evidence of comorbid neurodegenerative disease) were considered" (PMID:28742910). These are retrospective informant reports from a convenience sample of brain donors. They are not population frequencies.

| Phenotype (type) | HPO term | Mild CTE | Severe CTE | Total (n=111) | Other data / source |
|---|---|---|---|---|---|
| Progressive course (course) | — | 23 (85) | 84 (100) | 107 (96) | Progressive in 68% of 202 published cases (PMID:25580160) |
| Memory symptoms (symptom) | HP:0002354 (Memory impairment) | 19 (73) | 76 (92) | 95 (86) | Short-term memory loss from stage II (PMID:23208308) |
| Executive dysfunction (sign) | HP:0033051 (Impaired executive functioning) | 19 (73) | 67 (81) | 86 (79) | TES core feature (PMID:33722990) |
| Attention symptoms (symptom) | HP:0000736 (Short attention span) | 18 (69) | 67 (81) | 85 (78) | Stage I symptom (PMID:23208308) |
| Language symptoms (sign) | — (word-finding difficulty: no HPO match) | 10 (39) | 54 (66) | 64 (59) | Word-finding difficulty in stage IV (PMID:23208308) |
| Dementia (sign) | HP:0000726 (Dementia) | 9 (33) | 71 (85) | 80 (72) | Pooled 62% of published cases (PMID:40749155); stage IV OR 4.48 (PMID:41589584) |
| Impulsivity (behavioral) | HP:0100710 (Impulsivity) | 23 (89) | 65 (80) | 88 (82) | — |
| Depressive symptoms (behavioral) | HP:0000716 (Depression) | 18 (67) | 46 (56) | 64 (59) | Predicts TES in living athletes (PMID:33708171) |
| Explosivity (behavioral) | HP:0000737 (Irritability; nearest term) | 18 (67) | 38 (45) | 56 (51) | Stage II (PMID:23208308) |
| Apathy (behavioral) | HP:0000741 (Apathy) | 13 (50) | 43 (52) | 56 (51) | — |
| Anxiety (behavioral) | HP:0000739 (Anxiety) | 14 (52) | 41 (50) | 55 (51) | — |
| Hopelessness (behavioral) | HP:5200271 (Hopelessness) | 18 (69) | 36 (46) | 54 (52) | — |
| Verbal or physical violence (behavioral) | HP:0000718 (Aggressive behavior) | verbal 17 (63); physical 14 (52) | verbal 28 (34); physical 23 (28) | verbal 45 (41); physical 37 (34) | Aggression characteristic of stage IV (PMID:23208308) |
| Paranoia (behavioral) | HP:0011999 (Paranoia) | 11 (41) | 26 (31) | 37 (34) | — |
| Suicidality: ideation, attempts or completions (behavioral) | HP:0031589 (Suicidal ideation) | 15 (56) | 21 (25) | 36 (33) | Contested; see below |
| Visual hallucinations (sign) | HP:0002367 (Visual hallucination) | 6 (23) | 22 (27) | 28 (26) | 37.8% of CTE donors with parkinsonism (PMID:39008284) |
| Substance use disorder (behavioral) | — | 18 (67) | 41 (49) | 59 (53) | Confounder/comorbidity |
| Gait instability (sign) | HP:0001288 (Gait disturbance) | 7 (26) | 55 (66) | 62 (56) | — |
| Coordination difficulties (sign) | HP:0001251 (Ataxia; nearest term) | 7 (26) | 38 (45) | 45 (41) | — |
| Tremor (sign) | HP:0001337 (Tremor) | 5 (19) | 33 (39) | 38 (34) | — |
| Dysarthria (sign) | HP:0001260 (Dysarthria) | 5 (19) | 10 (13) | 15 (14) | — |
| Parkinsonism (sign) | HP:0001300 (Parkinsonism) | — | — | — | 24.7% of 481 CTE donors (PMID:39008284) |
| Headache (symptom) | HP:0002315 (Headache) | 8 (30) | 11 (14) | 19 (18) | Stage I symptom (PMID:23208308) |
| REM sleep behavior disorder, diagnosis or symptoms (sign) | HP:5200291 (REM sleep behavior disorder) | 7 (27) | 23 (29) | 30 (29) | — |
| Cerebral atrophy (imaging/pathology) | HP:0002059 (Cerebral atrophy) | — | — | — | Hemispheres, MTL, thalamus, mammillary bodies, brainstem (PMID:19535999) |
| Ventricular dilatation (imaging/pathology) | HP:0002119 (Ventriculomegaly) | — | — | — | From stage I (PMID:36759368) |
| Cavum septum pellucidum (imaging/pathology) | HP:0002389 (Cavum septum pellucidum) | — | — | — | Enlarged CSP in 44.6% of RHI-exposed living people (PMID:40046332) |
| Neurofibrillary tangles (pathology) | HP:0002185 (Neurofibrillary tangles) | — | — | — | Defining lesion (PMID:26667418) |

**Clinical subtypes and onset.** Two presentations exist. One is a behavior/mood group "whose initial features developed at a younger age" (n = 22). The other "developed at an older age and involved cognitive impairment" (n = 11) (PMID:23966253). The 2014 TES criteria describe behavioral/mood, cognitive, mixed and dementia variants (PMID:25580160). In the larger 2017 series of 111 informant-reported cases, 47 (42.3%) "initially presented with cognitive symptoms", 48 (43.2%) "initially presented with behavior or mood symptoms", and 16 (14.4%) presented with both. Most people developed both domains by the time of death: "43 (90%) of those initially presenting with only behavior or mood symptoms were reported to have cognitive symptoms at the time of death" (PMID:28742910). In Stern's series, "None of the subjects had motor disturbance as their initial feature", and "motor features, including parkinsonism, were not common in our sample" (PMID:23966253). Three asymptomatic donors with stage I–II pathology "raise the possibility that cognitive reserve37 may have a role in protecting against the clinical manifestations of CTE" (PMID:23966253; the numeral 37 is a reference marker in the source). A 2026 review, citing earlier series, reports "a mean age of onset of 44.3 years (range 16–83, n = 119), with symptoms beginning on average 14.5 years after retirement" (PMID:42341996). In the dementia subgroup of Stern's series, "The mean age of symptom onset for the dementia group was 57.7 years (SD = 18.3; range 25–82)", and "The mean length of time between dementia diagnosis and death was 8.0 years" (PMID:23966253). Onset is adult, usually midlife, and delayed after exposure. "delayed onset" is a supportive feature in TES (PMID:33722990).

**Severity and progression.** Progression is a core TES criterion (PMID:33722990). Functional dependence "is graded on 5 levels, ranging from independent to severe dementia" (PMID:33722990). Severity tracks pathological stage for cognition and dementia but not for mood. In 614 donors, "Higher CTE stage was associated with greater informant-reported cognitive symptoms" and "There were no associations with mood/behavioral scales". The authors note "It is uncertain if low-stage CTE clinically manifests" (PMID:41589584). The 2014 TES criteria were sensitive but not specific: "Cognitive (odds ratio [OR] = 3.6; 95% confidence interval [CI]: 1.2-5.1), but not mood/behavior or motor symptoms, were significantly associated with CTE pathology" (PMID:33826224).

**Parkinsonism.** In 481 CTE donors, "parkinsonism occurred frequently in individuals with CTE (119 [24.7%]". Those with parkinsonism had more dementia (87.4% vs 29.0%), more visual hallucinations and more probable REM sleep behavior disorder (PMID:39008284).

**Suicidality.** This remains contested. In the 2017 series, "The most common cause of death for participants with mild CTE pathology was suicide (12 [27%]) and for those with severe CTE pathology was neurodegenerative (ie, dementia-related and parkinsonian-related causes of death) (62 [47%])" (PMID:28742910). A systematic review found that "Only two case series met inclusion criteria and included autopsies from 17 unique cases, 5 of whom died by suicide" and rated the evidence very low (PMID:24328030). In the Australian Sports Brain Bank, "Six of the 12 donors with CTE and one of nine without CTE had died by suicide (P = 0.042)" (DOI:10.5694/mja2.51420). In young donors, "Suicide was the most common cause of death, followed by unintentional overdose; there were no differences in cause of death or clinical symptoms based on CTE status" (PMID:37639244). In a community sample, CTE-NC was "very uncommon in men who played amateur American football, those with mood disorders during life, and those with suicide as a manner of death" (PMID:37404944). Scottish former soccer players showed "no significant difference in rate of death by suicide" compared with controls (PMID:32694163).

**Quality-of-life impact.** P-tau burden is linked to everyday function. In 364 donors, global p-tau severity was associated with worse cognitive and Functional Activities Questionnaire scores, and "P-tau explained 13-49% of variance in cognitive and functional scales and 6-14% of variance in neuropsychiatric scales" (PMID:38317248). In ice hockey players, p-tau burden was associated with FAQ score and dementia (PMID:39630446). No CTE-specific EQ-5D, SF-36 or PROMIS data were found.

## 4. Genetic/Molecular Information

CTE has no causal gene and is not a monogenic disorder (see Interpretation). ACMG/AMP variant classification therefore does not apply, and the database check found no ClinVar records for the disease (https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy).

The central molecule is tau, the protein product of HGNC:6893 (MAPT; "microtubule associated protein tau"; NCBI Gene 4137; UniProt P10636) (https://rest.genenames.org/fetch/symbol/MAPT). In CTE, tau is wild-type. It accumulates as hyperphosphorylated filaments containing all six isoforms (PMID:30894745; PMID:29298849). The functional consequence is therefore a gain of toxic aggregation, not a loss- or gain-of-function coding mutation.

Germline susceptibility is carried by common variants.
- HGNC:613 (APOE): ε4 is associated with CTE stage in donors older than 65 (PMID:35759276).
- HGNC:22407 (TMEM106B): rs3173615 is described as "a missense coding SNP in TMEM106B". Its minor allele frequency is 0.42 in CTE cases and 0.43 in controls (PMID:30390709; PMID:41264095).
- MAPT H1β1γ1: a structural haplotype in the 17q21.31 inversion/copy-number region (PMID:40239644).
- PIP5K1B and ABAT: candidate GWAS loci, both intronic, with minor allele frequencies of 0.08 and 0.07. They are reported in a conference abstract only (https://alz-journals.onlinelibrary.wiley.com/doi/abs/10.1002/alz.046505).

Somatic variation has been found in CTE neurons. Single-neuron whole-genome sequencing of 15 CTE brains revealed "increased somatic single-nucleotide variants in CTE, exhibiting a pattern previously reported in Alzheimer's disease (AD)". A subset of cases also carried high burdens of somatic indels resembling signature ID4 (PMID:41166474). No COSMIC-type somatic driver is implicated.

Several other genes matter through co-pathology and biomarkers:
- HGNC:11571 (TARDBP), which encodes the protein in TDP-43 co-pathology.
- HGNC:620 (APP) and HGNC:11138 (SNCA), which encode the proteins in amyloid and α-synuclein co-pathology.
- HGNC:10610 (CCL11), HGNC:4235 (GFAP), HGNC:7739 (NEFL), HGNC:17761 (TREM2) and HGNC:1693 (CD68), which serve as inflammatory and injury markers (https://rest.genenames.org/fetch/symbol/MAPT).

Epigenetic evidence is preliminary. A preprint epigenome-wide study of human dorsolateral frontal cortex "identified 461 genome-wide significant CpG sites associated with duration of contact sports play, spanning 13 genes of which the majority were hypomethylated". It also reported that "alterations of CAMK2B and B4GALT6 were observed in CTE cases" (PMID:41377989; Research Square preprint, not peer reviewed). No histone or chromatin study and no epigenetic-clock study of CTE was found.

No chromosomal abnormalities have been reported. Aneuploidy, translocations and pathogenic CNVs have no known role, apart from the germline 17q21.31 structural haplotypes noted above (PMID:40239644).

## 5. Environmental Information

**Environmental factors.** The defining exposure is mechanical. It consists of repetitive concussive and nonconcussive head impacts from contact sports (American football, ice hockey, soccer, rugby, Australian rules football, boxing, wrestling), military service, and other repetitive trauma (PMID:36759368; PMID:33722990). Biomechanical modelling links lesion location to strain: "Computational 3-D and finite element models predict the perivascular and sulcal location of p-tau pathology as these brain regions undergo the greatest mechanical deformation during head impact injury" (PMID:36759368). Head impact exposure can be quantified. "A CDC study found that youth tackle football athletes ages 6 to 14 sustained 15 times more head impacts than flag football athletes" (https://www.cdc.gov/traumatic-brain-injury/about/repeated-head-impacts.html). Blast exposure is plausible from animal work (PMID:22593173) but not significantly associated with CTE in a military human series (PMID:35675177). No toxin, radiation or pollutant exposure is implicated, and the Comparative Toxicogenomics Database was not searched.

**Lifestyle factors.** Substance-use treatment and alcohol appear as clinical correlates or confounders, not causes (PMID:39269838; PMID:31199537). Ethanol, CHEBI:16236 (ethanol), is a potential confounder only.

**Infectious agents:** not applicable; no infectious etiology has been reported.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Repetitive head impacts deliver mechanical strain to the brain, which concentrates at the depths of cortical sulci and around small vessels** (computational; human post-mortem correlation). Finite-element models predict that these regions "undergo the greatest mechanical deformation" (PMID:36759368). The early sites of NFT accumulation in CTE brains "are regions of high deformation during injury" (PMID:33139536). GO:0009612 (response to mechanical stimulus).
2. **Mechanical deformation leads to neuronal tau hyperphosphorylation and mislocalisation** (in vitro, demonstrated). In cultured rat neurons, "The mechanical energy associated with high-strain rate deformation alone can induce tau mislocalization to dendritic spines and synaptic deficits", and these changes "can be reversed through inhibition of GSK3β and CDK5 or genetic deletion of tau" (PMID:33139536). In humans, activation of GSK3β and phosphorylation at Thr175 and Thr231 are features of CTE tauopathy (PMID:29298849). This step in humans is inferred from in vitro and model data. GO:0006468 (protein phosphorylation); GO:0008017 (microtubule binding; normal tau function lost on hyperphosphorylation, inferred).
3. **In parallel (branch A), RHI results in axonal injury and white-matter damage** (human, demonstrated as association). "Multifocal axonal varicosities and axonal loss were found in deep cortex and subcortical white matter at all stages" (PMID:23208308). A single severe axotomy (prefrontal leucotomy) produced CTE-like perivascular sulcal p-tau in 4 of 5 cases. This suggests that "chronic axonal damage contributes to the unique pathology of CTE over time" (PMID:27885490). In white matter, "Oligodendrocytes were found to be most severely affected", with iron-metabolism and stress transcripts and "excessive iron accumulation" (PMID:34019156). GO:0048678 (response to axon injury); GO:0042552 (myelination; white matter loss, inferred); CL:0000128 (oligodendrocyte).
4. **In parallel (branch B), RHI leads to microvascular injury and blood–brain barrier leakage** (human, association). "Levels of vascular injury-associated markers ICAM1, VCAM1, and CRP were increased in CTE compared to RHI-exposed and -naïve controls", and "Multifocal perivascular immunoreactivity for serum albumin was present in all RHI-exposed individuals" (PMID:36617181). Single-nucleus RNA-seq shows "angiogenic and inflamed endothelial cells" after RHI (PMID:40963024). CL:0000115 (endothelial cell); CL:2000044 (brain microvascular endothelial cell); CL:0000881 (perivascular macrophage; perivascular pigment-laden macrophages are reported in young donors, PMID:37639244); GO:0035633 (maintenance of blood-brain barrier; disrupted, inferred).
5. **Vascular and axonal injury lead to chronic neuroinflammation, with microglial recruitment and activation and astrocyte reactivity** (human, association; ordering inferred). RHI exposure "had a significant direct effect on CD68 cell density", and "The effect of RHI on ptau pathology was partially mediated through increased CD68 positive cell density" (PMID:27793189). "An increase in Iba1+ cells was found around blood vessels with perivascular tau pathology", and CCL2 tracked years of play (PMID:33278887). CCL11 is raised in CTE cortex (PMID:28950005). Perivascular astrocyte reactivity, with NQO1/L-ferritin co-labelling, suggests "iron-induced oxidative stress" (PMID:39921702). In young RHI-exposed donors, "SPP1-expressing inflammatory microglia" appear "prior to the onset of CTE p-tau pathology", and TGFβ1 is proposed as the signal behind "microglia-endothelial cell cross talk" (PMID:40963024). GO:0001774 (microglial cell activation); GO:0048143 (astrocyte activation); GO:0150076 (neuroinflammatory response); GO:0070098 (chemokine-mediated signaling pathway; CCL2/CCL11); GO:0001816 (cytokine production); GO:0006979 (response to oxidative stress); GO:0006879 (intracellular iron ion homeostasis; closest match); CL:0000129 (microglial cell); CL:0000127 (astrocyte).
6. **Inflammation, vascular injury and mechanical stress converge to cause perivascular aggregation of hyperphosphorylated tau in a CTE-specific filament fold** (human, demonstrated structure; trigger inferred). "all six brain tau isoforms assemble into filaments in CTE". "a different conformation of the β-helix region creates a hydrophobic cavity that is absent in tau filaments from the brains of patients with Alzheimer's disease". The additional density inside it "suggests that the incorporation of cofactors may have a role in tau aggregation in CTE" (PMID:30894745). "p-tau202 is the most upregulated p-tau species in CTE" and tracks RHI exposure years (PMID:34854540). Neuronal rather than astrocytic p-tau drives the lesion: "Neuronal p-tau was significantly associated with age, years of RHI exposure, and CTE severity; astrocytic p-tau pathology was only significantly associated with age" (PMID:35903039). GO:0097418 (neurofibrillary tangle); GO:1990000 (amyloid fibril formation; process-level proxy for filament assembly).
7. **Tau pathology spreads in an ordered pattern from focal sulcal epicentres to widespread cortex, medial temporal lobe and brainstem (McKee stages I→IV)** (human post-mortem, cross-sectional). "There is an ordered and predictable progression of hyperphosphorylated tau abnormalities through the nervous system" (PMID:23208308). The earliest stage is "restricted to DLF and LC" (PMID:32778942). In mice, RHI "enhanced the spreading of tau pathology" from inoculated fibrils, which suggests RHI may accelerate propagation rather than initiate it (model; PMID:41508043).
8. **Ongoing injury leads to co-pathologies and neurodegeneration** (human, association). These include TDP-43 inclusions ("in 85% of cases"), Aβ, α-synuclein, and neuronal and synaptic loss. The authors propose that "repetitive brain trauma and hyperphosphorylated tau protein deposition promote the accumulation of other abnormally aggregated proteins" (PMID:23208308). There is "a significant loss of cortical sulcus layer 2/3 neurons independent of p-tau pathology" (PMID:40963024). Somatic SNV and indel accumulation also occurs in CTE neurons (PMID:41166474). GO:0006974 (DNA damage response); GO:0051402 (neuron apoptotic process; cell-death process, mode unproven).
9. **Regional neurodegeneration results in clinical manifestations** (human clinicopathological association). Frontal cortex p-tau is associated with cognitive, functional and behavioral-regulation scores (PMID:38317248). Substantia nigra tau and neuronal loss mediate parkinsonism (PMID:39008284). Stage III/IV disease is associated with dementia (PMID:41589584). Mood and behavioral symptoms are not consistently explained by tau stage and are likely multifactorial (PMID:41589584; PMID:37639244).

**Upstream vs downstream.** Mechanical strain (step 1) is upstream. Axonal, vascular and inflammatory responses (steps 3–5) occur early, and in young donors they precede p-tau (PMID:40963024). Tau aggregation and spread (steps 6–7) are the defining downstream lesion. Co-pathology, neuronal loss and symptoms (steps 8–9) are most downstream. Low- and high-stage disease may differ mechanistically: gene expression associated with tau pathology "showed a nearly perfect inverse relationship when compared between these two groups" (PMID:36895005).

### Molecular profiling and pathways

Molecular profiling of human CTE tissue is recent, and all of it is cross-sectional.

In bulk transcriptomics, the largest dataset covers 76 prefrontal cortices (66 CTE, 10 controls). Changes in severe disease mainly implicate "diverse, strongly involved neuroinflammatory and neuroimmune processes". Pathology-modifying risk variants appear to act "via distinct biological pathways" (PMID:36895005).

Single-nucleus RNA-seq has examined two tissue types. Cortex from 8 controls, 9 RHI-exposed donors and 11 low-stage CTE cases showed early microglial, endothelial and synaptic changes (PMID:40963024). White matter from 8 CTE cases and 8 controls showed oligodendrocyte loss and astrocytic inflammation (PMID:34019156).

In proteomics, SomaScan profiling of 204 dorsolateral prefrontal cortex samples found that "proteasome subunit proteins and related pathways were strongly associated with CTE severity". It also found that "Reduction in ribosomal proteins and pathways was closely associated with ptau burden", and that MAPK signalling was altered (PMID:42603909).

Among signalling pathways, the kinases GSK3β and CDK5 are implicated by in vitro work (PMID:33139536), and activated GSK3β is present in human tissue (PMID:29298849). At the genomic level, CTE neurons carry somatic SNV and indel signatures shared with Alzheimer disease (PMID:41166474).

Metabolic and oxidative changes include iron accumulation and iron-related oxidative stress (PMID:34019156; PMID:39921702). Mitochondrial dysfunction and metabolic stress are discussed only in reviews (PMID:42341996).

No spatial transcriptomics, metabolomics, lipidomics or CRISPR screen of human CTE tissue was located. A genome-wide CRISPRi screen in mechanically injured iPSC-derived organoids identified the mechanosensory channel KCNJ2 as a target whose inhibition reduced injury effects. That system models traumatic brain injury rather than CTE (PMID:38579683).

**Cell types (CL):** CL:0000540 (neuron), CL:0000598 (pyramidal neuron; layer 2/3 sulcal neurons are lost), CL:0000127 (astrocyte), CL:0000129 (microglial cell), CL:0000128 (oligodendrocyte), CL:0000115 (endothelial cell), CL:0000669 (pericyte; neurovascular unit, inferred); CL:0000100 (motor neuron; CTE with motor neuron disease, PMID:20720505).

## 7. Anatomical Structures Affected

**Organ and system level.** The primary organ is the brain, UBERON:0000955 (brain), within the nervous system. Spinal cord motor-neuron disease occurs in a subset: "Three athletes with CTE also developed a progressive motor neuron disease", with TDP-43 inclusions in the spinal cord (PMID:20720505). Secondary effects are behavioral and psychiatric, plus motor involvement (parkinsonism). No non-neural organ involvement is described.

**Macroscopic findings.** "Neuropathologically, CTE is characterized by atrophy of the cerebral hemispheres, medial temporal lobe, thalamus, mammillary bodies, and brainstem, with ventricular dilatation and a fenestrated cavum septum pellucidum" (PMID:19535999). Macroscopic changes progress with stage: "typically mild dilatation of the frontal horn of the lateral ventricles or third ventricle with cavum septum pellucidum in stages I and II, evolving to mild cerebral atrophy, depigmentation of the LC and substantia nigra in stage III". Stage IV adds severe frontal and temporal atrophy, "thalamic atrophy", a "thalamic notch", "atrophy of mammillary bodies" and "thinning of the posterior corpus callosum in stage IV" (PMID:36759368). Brainstem involvement is integral: "brainstem p-tau pathology is an essential aspect of CTE", "with the LC affected at all stages, including stage I" (PMID:36759368). Even young donors with CTE "had more ventricular dilatation, cavum septum pellucidum, thalamic notching, and perivascular pigment-laden macrophages in the frontal white matter" (PMID:37639244).

**Regional (UBERON) distribution by stage.**
Within the brain, tau pathology spreads in a recognisable regional sequence. In stage I, "p‐tau pathology is found in discrete foci in the cerebral cortex, most commonly in the superior or lateral frontal cortices, typically around small vessels at the depths of sulci" (PMID:25904048). In stage II, foci multiply, but "The medial temporal lobe is spared neurofibrillary p‐tau pathology" (PMID:25904048). In stage III, the amygdala, hippocampus and entorhinal cortex show substantial neurofibrillary pathology. By stage IV there is "marked neuronal loss in the cortex, amygdala and hippocampus" (PMID:25904048).

In 366 donors, p-tau showed a predilection for the "dorsolateral frontal cortex (DLF), superior temporal cortex, entorhinal cortex, amygdala, and locus coeruleus (LC)" (PMID:32778942). Substantia nigra involvement underlies parkinsonism (PMID:39008284). The NINDS-NIBIB "High CTE" designation depends "on whether NFTs are present in the thalamus, mammillary bodies, hippocampus, amygdala, and entorhinal cortex" (PMID:36759368).

Suggested anatomical terms: UBERON:0000956 (cerebral cortex); UBERON:0001870 (frontal cortex); UBERON:0009834 (dorsolateral prefrontal cortex); UBERON:0001871 (temporal lobe); UBERON:0001872 (parietal lobe); UBERON:0002022 (insula); UBERON:0001950 (neocortex); UBERON:0005391 (cortical layer II); UBERON:0005392 (cortical layer III); UBERON:0013118 (sulcus of brain); UBERON:0001876 (amygdala); UBERON:0002728 (entorhinal cortex); UBERON:0002421 (hippocampal formation); UBERON:0001954 (Ammon's horn); UBERON:0004703 (dorsal thalamus); UBERON:0002206 (mammillary body); UBERON:0002148 (locus ceruleus); UBERON:0002038 (substantia nigra); UBERON:0002298 (brainstem); UBERON:0002316 (white matter); UBERON:0002336 (corpus callosum); UBERON:0004714 (septum pellucidum); UBERON:0009857 (cavum septum pellucidum); UBERON:0001869 (cerebral hemisphere); UBERON:0001981 (blood vessel); UBERON:0002240 (spinal cord; motor neuron disease subset). No exact UBERON label was returned for the bare terms hippocampus or thalamus, so the closest whole-structure terms are used.

**Tissue and cell level.** Nervous tissue is affected: gray-matter sulcal depths, superficial cortical layers II–III (PMID:26667418), CA2/CA4 of the hippocampus (PMID:26667418) and subcortical white matter (PMID:23208308). The cell types are listed in Section 6.

**Subcellular level.** GO:0097418 (neurofibrillary tangle); GO:0043204 (perikaryon), where p-tau accumulates in neuronal perikarya in a rat blast model (PMID:32094584); GO:0030425 (dendrite), where tau mislocalises to dendritic spines in vitro (PMID:33139536); GO:0030424 (axon), with axonal varicosities (PMID:23208308); GO:0045202 (synapse), with altered synaptic gene expression (PMID:40963024); GO:0043005 (neuron projection), including neuritic threads (PMID:19535999); GO:0005856 (cytoskeleton), tau being a microtubule-associated protein. Iron-related oxidative stress in astrocytes and oligodendrocytes is also documented (PMID:39921702; PMID:34019156).

**Lateralization.** Pathology is described as patchy and "irregular" (PMID:26667418). No study of systematic left–right asymmetry was found, and the leucotomy model was bilateral by design (PMID:27885490). Lateralization should be recorded as irregular/multifocal, with asymmetry not characterised.

## 8. Temporal Development

**Onset.** Onset is in adulthood, typically midlife, and insidious. It is delayed, usually by years to decades, after the exposure period ends. The 2026 review reports a mean onset of 44.3 years and onset about 14.5 years after retirement (PMID:42341996). Pathology can be present in young people: in donors under 30, "CTE was diagnosed in 63 (41.4%; median [IQR] age, 26 [24-27] years)", and "60 (95.2%) were diagnosed with mild CTE (stages I or II)" (PMID:37639244).

**Stages.** The McKee stages are I–IV (PMID:23208308), with a simplified Low/High system (PMID:33611507). The stage correlates with "increased duration of football play, survival after football and age at death" (PMID:23208308). In a 364-donor series, "140 (38.5%) had low CTE and 224 (61.5%) had high CTE" (PMID:38317248).

**Progression pattern and rate.** The disease is described as progressive and "slowly progressive" (PMID:19535999). This is debated: "CTE pathology might not be inexorably progressive or specific to those who have experienced repetitive neurotrauma" (PMID:31670780). Historical boxing cases suggest "subclinical and possibly static tauopathy in some athletes" (PMID:29036831). Course duration in a soccer dementia series was "an average age at onset of 63.6 years and disease duration of 10 years" (PMID:28205009). Among NFL donors with dementia, mean onset was 63.4 years and death 73.1 years (PMID:42642105). No remission, spontaneous or treatment-induced, has been documented.

**Critical periods.** Youth exposure may be a window of vulnerability. Starting tackle football before age 12 "predicted earlier cognitive (p < 0.0001) and behavioral/mood (p < 0.0001) symptom onset by 13.39 and 13.28 years, respectively" (PMID:29710395). The cumulative exposure window (years of play) is the main modifiable period (PMID:31589352).

## 9. Inheritance and Population

**Inheritance:** not applicable. CTE is acquired; it is not Mendelian, mitochondrial or polygenic-dominant. Penetrance, expressivity, anticipation, germline mosaicism, founder effects, consanguinity and carrier frequency do not apply. Genetic modifiers (Section 2) shift risk and severity given exposure (PMID:42341996).

**Prevalence (all autopsy-based; no true incidence data exist):**
All prevalence figures come from autopsy series; no true incidence data exist. Estimates depend heavily on how the brains were selected.

In donor series of highly exposed athletes, frequencies are very high. CTE was found in 177 of 202 football players (87%) in a convenience sample (PMID:28742910). Among all NFL players who died in 2008–21, "the possible CTE prevalence at death ranged between 18.5% and 98.7%", with the bounds set by assuming that none or all of the non-donors had CTE (PMID:42642105). A selection-bias-adjusted estimate for deceased NFL players was "74.5% (95% CI, 69.6%-78.3%)" (PMID:42949744). A meta-analysis found that "the pooled prevalence of CTE in contact sport athletes was 53.7%", and "rugby players exhibited the highest prevalence at 64.7%" (PMID:40194947).

Less selected samples give much lower figures. In the Mayo Clinic tissue registry, 42 of 2566 screened autopsies had CTE pathology or features. American football carried the highest frequency (15% of cases; OR 2.62) (PMID:31199537). In the military brain bank, the frequency was 4.4% (PMID:35675177). In a TBI-enriched community autopsy cohort it was 14.9% (PMID:41108192). Among community-sourced men over 50, 5.4% had possible CTE-NC features (PMID:37404944). In the population-based São Paulo cohort, "Seven cases (0.6%) met criteria for CTE-NC" (PMID:41627284). Community studies summarised elsewhere report 0%–8% (PMID:39528258).

The CDC states that "Scientists do not currently know how many people have or will develop CTE in the United States" and that "Prior studies suggest that CTE is likely very rare" in groups without long-term exposure (https://www.cdc.gov/traumatic-brain-injury/about/repeated-head-impacts.html).

**Demographics.** The sex ratio is overwhelmingly male, reflecting exposure (PMID:23208308; PMID:31199537; PMID:41627284). Only a few female cases have been published, including one former professional Australian rules footballer (PMID:37391669). Age at death in CTE series is broad: "ranging in age from 17 to 98 years (mean 59.5 years)" (PMID:23208308). The median age at death in the football series was 67 years (PMID:28742910). In the Australian series, CTE donors died younger (mean 48 vs 75 years) (DOI:10.5694/mja2.51420). Geographically, CTE has been reported from the USA, Australia, the UK and Brazil (PMID:28742910; DOI:10.5694/mja2.51420; PMID:28205009; PMID:41627284). Distribution follows sport participation rather than ancestry. No geographic distribution of variants is relevant. MAPT haplotype data exist only for European-ancestry donors (PMID:40239644).

## 10. Diagnostics

**Definitive diagnosis.** Diagnosis is neuropathological, using the NINDS/NIBIB criteria with AT8 p-tau immunohistochemistry (PMID:26667418; PMID:33611507). The first panel reached "good agreement" between raters (Cohen's kappa 0.67) and 0.78 against the CTE diagnosis (PMID:26667418). Supportive but non-specific features include "pretangles and NFTs affecting superficial layers (layers II-III) of cerebral cortex", CA2/CA4 hippocampal pathology, subcortical aggregates and thorn-shaped astrocytes (PMID:26667418).

**Clinical criteria (research only).** The NINDS TES criteria require "(1) substantial exposure to repetitive head impacts (RHIs) from contact sports, military service, or other causes; (2) core clinical features of cognitive impairment (in episodic memory and/or executive functioning) and/or neurobehavioral dysregulation; (3) a progressive course;" plus exclusion of other causes. They assign a provisional level of certainty for CTE (PMID:33722990). Their accuracy is disputed:
- 2014 criteria: "TES criteria demonstrated sensitivity and specificity of 0.97 and 0.21, respectively" (PMID:33826224).
- NINDS criteria (preprint): sensitivity 0.77 and specificity 0.84 for stage II–IV, and 0.90/0.90 at age ≥50 (PMID:42282171; medRxiv preprint).
- In an independent brain bank of 1,038 cases, positive predictive value was 24.0%, and "The diagnostic accuracy of TES for CTE-NC was driven by exposure to repetitive head impacts rather than proposed clinical features" (PMID:42135530).
- In living retired athletes, "54% of those meeting criteria for TES were diagnosed as cognitively normal via consensus diagnosis" (PMID:33708171).

**Imaging.** Suggested terms: NCIT:C17007 (Positron Emission Tomography); NCIT:C16809 (Magnetic Resonance Imaging); NCIT:C15327 (Lumbar Puncture); NCIT:C25153 (Autopsy), the definitive diagnostic procedure.
- Tau PET with flortaucipir, CHEBI:755635 (flortaucipir): "Significantly elevated flortaucipir uptake was observed in former football players", but "Flortaucipir PET was not able to differentiate TES groups" (PMID:38134231). In autopsy correlation (n=6), "specificity to CTE p-tau is uncertain" because of off-target binding (PMID:36152064). In vitro, flortaucipir binds MAO-A off-target, and the tracers MK-6240, CHEBI:758582 (florquinitau), and PI-2620 bind weakly: "3H-MK-6240 and 3H-PI-2620 had negligible binding in all but 2 CTE IV cases" (PMID:36109185).
- MRI, cavum septum pellucidum: enlarged CSP in 44.6% of RHI-exposed people vs 13.3% in AD (PMID:40046332). However, "No significant associations were found between CSP measures and diagnosis of TES" (PMID:39161749). Earlier work found a higher rate of CSP in symptomatic former NFL players (PMID:26414478).
- Diffusion MRI: gray/white boundary FA was associated with CTE certainty (PMID:41218808).
- Medial temporal atrophy and fornix changes are common in RHI/TES but reflect mixed pathologies (PMID:35481808).

**Fluid biomarkers.**
- Plasma p-tau181/231 were higher in former players, with modest discrimination (AUC 0.742). GFAP was higher in TES possible/probable (PMID:39351900).
- Plasma p-tau217 "is unlikely to be useful for the detection of CTE" but rules out amyloid (PMID:42440317).
- In CSF, "tau pathology in CTE is not reliably reflected by currently available fluid biomarkers" (PMID:41612558).
- A review of p-tau, NfL, GFAP, S100B and sTREM2 concluded that "None currently provides CTE-specific discrimination" (PMID:42931149).
- Post-mortem CSF CCL11 distinguished CTE from controls and AD (AUC 0.839, preliminary) (PMID:28950005).
- Combining cognition, blood biomarkers and MRI improves TES classification (AUC 0.84–0.91) (PMID:42288852).

**Electrophysiology.** The qEEG algorithm separating former NFL players from controls "had a specificity = 80%, a sensitivity = 60%, and an area under curve (AUC) = 0.75". This distinguishes exposure, not CTE (PMID:36324216).

**Genetic and omics testing.** No genetic test (WGS, WES, panel, CMA, karyotype, FISH, mtDNA or repeat expansion) has a diagnostic role. APOE and TMEM106B genotypes are research modifiers only (PMID:35759276; PMID:32712945). Blood transcriptomic and proteomic biomarker studies are registered (NCT04928534). The DIAGNOSE CTE project states that "CTE cannot yet be diagnosed during life" (PMID:34384490).

**Differential diagnosis.** The main differentials are:
- Alzheimer disease, MONDO:0004975 (Alzheimer disease). Its tau fold differs, and p-tau396 predominates in AD (PMID:30894745; PMID:34854540).
- Frontotemporal lobar degeneration, MONDO:0017276 (frontotemporal dementia), including FTLD-TDP (PMID:35481808).
- Primary age-related tauopathy, in which NFTs are "mostly restricted to structures in the medial temporal lobe, basal forebrain, brainstem, and olfactory areas" (PMID:25348064).
- Aging-related tau astrogliopathy (ARTAG), which "can be distinguished from primary tauopathies, but may be concurrent with primary tauopathies or other disorders" (PMID:26659578). Sulcal astrocytic p-tau in CTE is mostly subpial thorn-shaped astrocytes, "a form of age-related tau astrogliopathy" (PMID:35903039). Under the consensus criteria, "Subpial TSA, or ARTAG, were considered only supportive, non-diagnostic, features of CTE" (PMID:36759368).
- Limbic TDP-43 and hippocampal sclerosis (PMID:35481808).
- Progressive supranuclear palsy, MONDO:0019037 (progressive supranuclear palsy), and other tauopathies used as comparators in the consensus panel (PMID:26667418).
- Lewy body disease, MONDO:0007488 (Lewy body dementia), and Parkinson disease, MONDO:0005180 (Parkinson disease). These often co-occur with CTE; parkinsonism in CTE is mostly not explained by nigral Lewy bodies (PMID:39008284; PMID:23208308).
- Amyotrophic lateral sclerosis, MONDO:0004976 (amyotrophic lateral sclerosis), as CTE with motor neuron disease (PMID:20720505).
- Treatable mimics: depression, anxiety and sleep apnea "should be distinguished from neurodegenerative disease" (PMID:37798551).

**Screening.** No screening programme exists for asymptomatic people, and none can exist without validated biomarkers.

## 11. Outcome/Prognosis

**Mortality in exposed populations (proxy for CTE burden).**
- NFL players had lower all-cause mortality (SMR 0.70) but "higher neurodegenerative mortality (SMR = 3.94; 95% CI: 3.38-4.56)". This remained threefold higher after accounting for competing risks (PMID:42534468).
- In an earlier pension cohort, neurodegenerative mortality SMR was 2.83–3.26, and ALS and AD were each about fourfold (PMID:22955124).
- ALS mortality SMR was 3.94 (PMID:34910152).
- Scottish soccer players: "Mortality with neurodegenerative disease listed as the primary cause was 1.7% among former soccer players and 0.5% among controls" (PMID:31633894). Neurodegenerative disease risk was highest for defenders and for careers over 15 years (HR 5.20) (PMID:34338724).
- None of these measures is CTE-specific mortality, because CTE is not coded on death certificates.

**Survival and life expectancy.** No 5-year or 10-year survival data exist. The disease course in clinicopathological series spans years to a decade or more (PMID:28205009; PMID:42642105). Among NFL brain donors, "63 (18.6%) had neurodegenerative disease listed as primary cause of death" (PMID:42642105).

**Morbidity and disability.** Dementia-related diagnoses were "prevalent (62%; 95% CI 48%-75%)" in published CTE cases (PMID:40749155). In donors, stage IV CTE was associated with clinician-diagnosed dementia (risk ratio 1.44) (PMID:42642105). Bias-adjusted dementia prevalence during life among deceased NFL players was 27.2% (PMID:42949744). Functional dependence is graded in TES (PMID:33722990).

**Complications.** These include dementia, parkinsonism (with hallucinations and REM sleep behavior disorder) (PMID:39008284), motor neuron disease (PMID:20720505), and possibly suicide, which is contested (Section 3). Co-pathologies (AD, Lewy body disease, FTLD) are common: "Chronic traumatic encephalopathy was the sole diagnosis in 43 cases (63%)" (PMID:23208308).

**Prognostic factors.**
- Higher stage and p-tau burden (PMID:41589584; PMID:38317248).
- Older age (PMID:32778942).
- Longer exposure (PMID:31589352).
- Genetic modifiers: APOE ε4 and TMEM106B (PMID:35759276; PMID:41264095).
- CD68 microglial density predicted dementia, an effect that disappeared when p-tau was included (PMID:27793189).
- No prognostic biomarker is validated in living people.

**Recovery potential.** No recovery has been documented. Whether low-stage disease ever becomes clinically manifest is uncertain (PMID:41589584).

## 12. Treatment

**Disease-modifying therapy: none.** Reviews agree that there are no "treatments for the underlying disease process" but that "There are non-pharmacologic and pharmacologic treatments for the symptoms of CTE that improve the quality of daily life" (PMID:31215252). "there are currently no ongoing clinical trials for the treatment of CTE" (2020) (PMID:32774238). Falcon et al. state that "No disease-modifying therapies currently exist, and diagnosis requires an autopsy" (PMID:30894745).

**Symptomatic pharmacotherapy.** Drug choice is extrapolated from other tauopathies. The lack of CTE-specific evidence "is one of the main reasons for the lack of specific pharmacological studies targeting symptoms or pathologic pathways of this disease" (PMID:37300418). Reviews describe treating depression and other symptoms, "Aside from supportive treatment designed to address specific symptoms (such as depression or comorbid seizures)" (PMID:32774238). "Guidelines for the evaluation and treatment of these patients are sparse" (PMID:26336629). In a memory-clinic case series of 14 former NFL players, the authors advise: "If parkinsonism is identified, a trial of dopaminergic therapy may be beneficial", and "If AD pathology is suspected, the patient may benefit from treatment with an acetylcholinesterase inhibitor". One patient showed "near-complete resolution of frequent explosive rage attacks" after lamotrigine, and another improved after migraine treatment with flunarizine and dihydroergotamine (PMID:26336629; case-level evidence). A 2025 review lists "symptomatic therapy for anxiety and depression, cognitive impairment, behavioral disorders, neuroprotectors, and non-drug intervention methods" (PMID:40879226). No randomized trial of any symptomatic drug in CTE or TES was found. Suggested NCIT terms: NCIT:C265 (Antidepressant Agent; closest match); NCIT:C94725 (Selective Serotonin Reuptake Inhibitor); NCIT:C29710 (Antipsychotic Agent); NCIT:C47792 (Acetylcholinesterase Inhibitor; closest match); NCIT:C73269 (Memantine); NCIT:C611 (Levodopa). Relevant ChEBI entities: CHEBI:53289 (donepezil); CHEBI:64312 (memantine). No CTE-specific pharmacogenomic data exist.

**Rehabilitation and supportive care.** A 12-month n-of-1 study of six people with suspected CTE "provided primary-level evidence to suggest active rehabilitation as a potential intervention", with mixed effects on mood and behaviour (PMID:38814891). Suggested terms: NCIT:C15302 (Physical Therapy); NCIT:C121351 (Occupational Therapy); NCIT:C15308 (Psychotherapy); NCIT:C64345 (Cognitive Behavior Therapy; closest match). An umbrella review of other tauopathies notes that "Currently, no treatment has been validated by clinical trials to be used for the management of CTE" and that "Evidence suggests that active rehabilitation has beneficial effects on vestibular/ocular symptoms" (PMID:35862387). A medico-legal analysis states that "The MDT is considered to be the appropriate or preferred model of care for the management of TES" (PMID:37456643). Further terms: NCIT:C15315 (Rehabilitation; closest match); NCIT:C159273 (Speech Language Therapy; closest match). Treating comorbid depression, anxiety and sleep apnea is recommended because these "are treatable conditions" (PMID:37798551).

**Experimental and advanced therapeutics (preclinical).**
- AAVrh.10 vectors encoding anti-pTau antibodies "significantly reduced pTau levels across the CNS" in a repeated-TBI mouse model (gene therapy; mouse) (PMID:31608704).
- The DYRK1A inhibitor SM07883 reduced RHI-induced pTau and glial activation in hTau mice (model) (PMID:41651695).
- Preclinical kinase inhibitor, antibody and anti-inflammatory approaches are reviewed in PMID:32774238.
- GSK3β/CDK5 inhibition reversed deformation-induced tau mislocalisation in vitro (PMID:33139536).
- The CCL2, TMEM106B/TREM2 and TGFβ1 pathways are proposed targets (PMID:33278887; PMID:41264095; PMID:40963024).
- Tau-directed antibodies have been tested in other tauopathies and failed. A 2023 review lists CTE among the tauopathies that drug-development programmes target. It reports that "Gosuranemab showed no efficacy in primary and secondary outcome measures compared to the placebo", and that "Tilavonemab’s development in PSP was halted after it failed to show efficacy over placebo even though target engagement had been established" (PMID:37803386). Registered gosuranemab (BIIB092) trials include NCT03068468 (PSP), NCT02460094 (PSP, multiple ascending dose) and NCT03352557 (early AD). None enrolled people with CTE. Suggested terms: NCIT:C20401 (Monoclonal Antibody); NCIT:C15238 (Gene Therapy).
- No RNA-based therapy, cell therapy or immunotherapy has reached a CTE-specific trial. The only cell-therapy record listing CTE as a condition was withdrawn (NCT02959294).

**Registered trials (all diagnostic or preventive; none tests a CTE therapy).**
- NCT05490576: [18F]PI-2620 tau PET in TES; status unknown.
- NCT04928534: blood multi-omics biomarkers for TES/CTE; completed.
- NCT02266563: [18F]AV-1451 and florbetapir PET in TBI/CTE; completed.
- NCT02003183: FDDNP-PET in persons at risk for CTE; completed.
- NCT03218332: post-concussion syndrome in professional athletes, with in vivo CTE biomarkers; recruiting.
- NCT04796207: DHA/EPA fish-oil supplementation and sub-concussion biomarkers in collegiate football; completed. Terms: NCIT:C497 (Fish Oil); CHEBI:36005 (docosahexaenoic acid).
- NCT02959294: adipose-derived stromal vascular fraction in concussion/TBI; withdrawn.

**Treatment strategy.** No algorithm or guideline specific to CTE exists. The VA/DoD post-acute mild TBI guideline addresses symptom management after mTBI, not CTE (https://www.healthquality.va.gov/guidelines/rehab/mtbi/). Management is symptom-directed, multidisciplinary and patient-tailored (PMID:37300418).

## 13. Prevention

**Primary prevention: reducing RHI exposure.** This is the only evidence-based approach. The exposure-based argument rests on dose–response data (PMID:31589352; PMID:39630446). A Brazilian population study concludes its findings "support prioritizing primary prevention by reducing exposure to repetitive head impacts in sport and other settings" (PMID:41627284). For soccer, its authors suggest "strategies directed toward reducing head impact exposure may be advisable in the meantime" (PMID:34338724). Interventions that reduce concussion or impact exposure, though not yet shown to reduce CTE:
- Practice contact limits: "The rate of SRC sustained in high school football practice decreased by 57% after a rule change limiting the amount and duration of full-contact activities, with no change in competition concussion rate" (PMID:31306587).
- Kickoff rules: "The kickoff rule change in Ivy League football was associated with a reduction in concussions" (PMID:30285061). After the 2018 NCAA rule, however, "there was not a corresponding decrease in concussions during kickoff plays as anticipated" (PMID:37538536).
- Youth heading limits: US Soccer guidelines "prohibit heading for children 10 years old and younger, while those aged 11–13 are restricted by weekly practice exposure limits, however in game heading is unrestricted" (PMID:39728882).
- Helmets: "helmet design may never prevent all concussions from occurring in football" but can reduce their incidence. Concussion relative risk was 46.1% for one helmet model vs another (PMID:24484225). No NCIT term for protective helmet was found.
- Delaying tackle football: retrospective data on starting before age 12 (PMID:25632088; PMID:28926003; PMID:29710395) motivate youth-exposure policy. The authors note that replication is needed.
- Consensus: the 6th International Consensus on Concussion in Sport "summarises evidence-informed principles of concussion prevention, assessment and management" (PMID:37316210).

**Secondary prevention and screening.** None is possible yet, because no in-life diagnostic exists (PMID:34384490). Living cohorts such as DIAGNOSE CTE aim to enable it (PMID:34384490).

**Tertiary prevention.** Diagnose and treat depression, anxiety and sleep apnea, and avoid misattribution to CTE. Perceived CTE "represents a novel risk factor for suicidality" and should prompt assessment of treatable conditions (PMID:39312218; PMID:37798551).

**Not applicable:** immunization, genetic screening (carrier, preimplantation, prenatal), genetic counseling for inheritance, and prophylactic medication.

**Risk stratification.** Years and level of play, age at first exposure, and research-level genotype (PMID:31589352; PMID:35759276). Predictive genetic testing has been discussed but is not recommended (PMID:32712945).

## 14. Other Species / Natural Disease

No naturally occurring CTE is recognised in veterinary medicine. There is no OMIA entry and no zoonotic potential. Head-impact-associated tau pathology has been explored in species that strike with their heads:
- **Muskox and bighorn sheep.** NCBITaxon:37176 (Ovibos moschatus) and NCBITaxon:37174 (Ovis canadensis). In muskoxen, phosphorylated tau-immunoreactive "neuritic thread clusters, neurites, and neurons were concentrated in the superficial layers of the neocortex, preferentially at the bottom of the sulci in the muskoxen and occasionally around blood vessels". "Tau-immunoreactive lesions were rare in the bighorn sheep" (n = 3 and 4; preliminary) (PMID:35579705). This sulcal-depth, superficial-layer distribution resembles human CTE, but the samples are tiny.
- **Woodpeckers.** Brains of 10 ethanol-preserved woodpeckers showed "perivascular and white matter tract silver-positive deposits in eight out of the 10 woodpecker brains", with none in 5 control birds (PMID:29394252). Critics note that "It remains unknown how closely woodpecker-specific tau pathology resembles chronic traumatic encephalopathy" (PMID:29778361). A 2026 review finds "a lack of direct applicability of these findings to human TBI prevention" (DOI:10.1002/ar.25567).
- **Orthologs.** MAPT is conserved across mammals, and the tau gene structure "was originally determined from cattle brains" (PMID:34255876). Orthologue NCBI Gene IDs were not retrieved.

## 15. Model Organisms

No model fully recapitulates human CTE. A 2026 review states that "no single model fully recapitulates the disease trajectory" (PMID:42341996). The defining sulcal-depth localisation "is difficult to model in lissencephalic rodent brains, which lack the cortical folding that concentrates strain at the depths of the sulci" (PMID:42341996).

**Mouse (NCBITaxon:10090, Mus musculus).**
- *Repetitive closed-head mTBI in wild-type mice.* Six impacts daily for 7 days produced "persistent and widespread astrogliosis and microglial activation, as well as significantly elevated phospho-tau immunoreactivity to 6-months" (PMID:25593768).
- *hTau mice (human tau on a null murine background; transgenic).* Aged hTau mice given repetitive mTBI showed increased phospho-tau, but "We did not observe the perivascular tau pathology, neuritic threads, or astrocytic tangles that are commonly found in human CTE" (PMID:23334597). In young hTau mice, white-matter degeneration and progressive learning deficits occurred, with "only transient, injury-dependent increases in phosphorylated tau" (PMID:29993324).
- *CHIMERA rmTBI.* Wild-type mice showed no hyperphosphorylated tau. P301S tau transgenic mice showed increased AT8-positive cells. RHI enhanced the spread of inoculated tau fibrils (PMID:41508043). Repeated CHIMERA is also described as producing chronic microgliosis, axonal injury and astrogliosis (review; DOI:10.3389/fncel.2024.1371213).
- *Single blast in C57BL/6.* This produced "phosphorylated tauopathy, myelinated axonopathy, microvasculopathy, chronic neuroinflammation, and neurodegeneration", together with learning and memory deficits (PMID:22593173).
- *hTau.P301S with repetitive mTBI.* Tau worsened chronic white-matter atrophy (PMID:37578550).

**Rat (NCBITaxon:10116, Rattus norvegicus).**
- Repetitive low-level blast: rats "accumulated abnormal hyperphosphorylated tau in neuronal perikarya and perivascular astroglial processes" (PMID:32094584).
- Three mTBIs: sex-dependent tau-PET autoradiography binding at 12 weeks (PMID:39943994).
- Moderate TBI: reproduced pThr175 tau and GSK3β activation (PMID:29298849).

**Large animals.** Pig, NCBITaxon:9823 (Sus scrofa), and sheep, NCBITaxon:9940 (Ovis aries), have gyrencephalic brains. In pigs, simulated diffuse axonal injury produces tau accumulation, but behavioural testing standards are lacking. "Domestic sheep have thus emerged as the preferred large animal model for tauopathies" (review; PMID:34255876). No CTE-specific repetitive-impact large-animal study with p-tau quantification was found.

**Drosophila (NCBITaxon:7227, Drosophila melanogaster).** A closed-head TBI device produces "temporary incapacitation, ataxia, activation of the innate immune response, neurodegeneration, and death" (PMID:24127584). Flies lack sulci and perivascular regions (DOI:10.3389/fneur.2024.1378620).

**In vitro and human cellular models.**
- Mechanically deformed rat hippocampal neurons (tau mislocalisation, reversible with GSK3β/CDK5 inhibition) (PMID:33139536).
- iPSC-derived cortical organoids injured by ultrasound (neuronal death, tau phosphorylation, TDP-43 nuclear egress) (PMID:38579683).
- A human tri- and penta-culture 3D platform showing "persistent tau phosphorylation, axonal degeneration, chronic inflammation, and metabolic dysfunction without widespread neuronal loss" (bioRxiv preprint; https://www.biorxiv.org/content/10.64898/2025.12.29.696879v1.full).
- Microphysiological systems are reviewed in PMID:42950990.

**Recapitulation summary.**
- Captured well: phospho-tau increases, gliosis, white-matter and axonal injury, and behavioural deficits.
- Captured poorly: the sulcal-depth perivascular neuronal lesion, the CTE-specific filament fold, decades-long latency and staged spread.
- Main applications: mechanism (mechanotransduction, kinase signalling, inflammation), biomarker discovery and preclinical testing of therapeutics (PMID:31608704).

**Resources.** MGI, RGD, ZFIN, FlyBase and IMSR were not searched in this review. No dedicated CTE genetic model exists, because the disease has no causal gene.

## Open Questions

1. **Causality and specificity.** Is the RHI–CTE relationship causal, as the Bradford Hill analysis argues (PMID:35937061), or premature to assert (PMID:39277838)? How specific is the lesion, given reports in people without known neurotrauma (PMID:31169877; PMID:31670780)?
2. **Clinical meaning of low-stage CTE.** Stage I/II disease shows no association with symptoms (PMID:41589584). Young symptomatic donors show the same symptoms regardless of CTE status (PMID:37639244). What actually causes the mood and behavioural syndrome in RHI-exposed people?
3. **In-life diagnosis.** Can a CTE-specific tau PET ligand be developed? Current tracers bind poorly or off-target (PMID:36109185). Can fluid or multimodal panels be validated against autopsy (PMID:42931149; PMID:42288852)? TES accuracy estimates conflict sharply (PMID:33826224; PMID:42282171; PMID:42135530).
4. **True population burden.** All estimates are autopsy-based and subject to selection bias. Estimates range from 0.6% in population cohorts (PMID:41627284) to 74.5% bias-adjusted in NFL decedents (PMID:42949744). No incidence data exist, and data on women are scarce (PMID:40194947).
5. **Mechanistic trigger.** What initiates neuronal tau aggregation in the CTE fold, and what is the non-tau cofactor density (PMID:30894745)? Does early inflammatory and vascular injury cause tau deposition or only precede it (PMID:40963024)?
6. **Genetics.** The APOE, TMEM106B and MAPT findings need replication in independent and ancestrally diverse cohorts (PMID:35759276; PMID:40239644). The GWAS abstract was never published (https://alz-journals.onlinelibrary.wiley.com/doi/abs/10.1002/alz.046505).
7. **Progression.** Is CTE inexorably progressive (PMID:31670780; PMID:29036831)? Longitudinal antemortem-to-autopsy cohorts are needed (PMID:42931149).
8. **Prevention efficacy.** Do rule changes, heading limits and delayed tackle age reduce CTE, rather than just concussions (PMID:31306587; PMID:37538536)?
9. **Therapeutics.** No CTE therapeutic trial exists (PMID:32774238). Tau-directed, anti-inflammatory and kinase approaches remain preclinical (PMID:31608704).

## References

- PMID:32712945 Abdolmohammadi B et al. 2020. Genetics of Chronic Traumatic Encephalopathy. evidence: citations/abdolmohammadi-2020-genetics-of-cte-review.md
- PMID:39630446 Abdolmohammadi B et al. 2024. Duration of Ice Hockey Play and Chronic Traumatic Encephalopathy. evidence: citations/abdolmohammadi-2024-ice-hockey-duration.md
- PMID:34255876 Ackermans NL et al. 2021. Unconventional animal models for traumatic brain injury and chronic traumatic encephalopathy. evidence: citations/ackermans-2021-unconventional-animal-models.md
- PMID:35579705 Ackermans NL et al. 2022. Evidence of traumatic brain injury in headbutting bovids. evidence: citations/ackermans-2022-headbutting-bovids.md
- DOI:10.1021/acschemneuro.7b00291 Authors not stated 2017. Chronic Traumatic Encephalopathy (CTE): A Brief Historical Overview and Recent Focus on NFL Players. evidence: citations/acs-2017-cte-brief-historical-overview.md
- PMID:39008284 Adams JW et al. 2024. Substantia Nigra Pathology, Contact Sports Play, and Parkinsonism in Chronic Traumatic Encephalopathy. evidence: citations/adams-2024-substantia-nigra-contact-sports.md
- PMID:28926003 Alosco ML et al. 2017. Age of first exposure to American football and long-term neuropsychiatric and cognitive outcomes. evidence: citations/alosco-2017-age-first-exposure-neuropsychiatric-outcomes.md
- PMID:29710395 Alosco ML et al. 2018. Age of first exposure to tackle football and chronic traumatic encephalopathy. evidence: citations/alosco-2018-age-first-exposure-football.md
- PMID:32778942 Alosco ML et al. 2020. Characterizing tau deposition in chronic traumatic encephalopathy (CTE): utility of the McKee CTE staging scheme. evidence: citations/alosco-2020-tau-deposition-mckee-staging.md
- PMID:34384490 Alosco ML et al. 2021. Developing methods to detect and diagnose chronic traumatic encephalopathy during life: rationale, design, and methodology for the DIAGNOSE CTE Research Project. evidence: citations/alosco-2021-diagnose-cte-design.md
- PMID:36152064 Alosco ML et al. 2023. Associations between near end-of-life flortaucipir PET and postmortem CTE-related tau neuropathology in six former American football players. evidence: citations/alosco-2023-flortaucipir-postmortem.md
- PMID:38317248 Alosco ML et al. 2024. Cognitive, functional, and neuropsychiatric correlates of regional tau pathology in autopsy-confirmed chronic traumatic encephalopathy. evidence: citations/alosco-2024-regional-tau-pathology-cte-correlates.md
- PMID:39161749 Arciniega H et al. 2024. Cavum Septum Pellucidum in Former American Football Players: Findings From the DIAGNOSE CTE Research Project. evidence: citations/arciniega-2024-cavum-septum-diagnose.md
- PMID:42135530 Arena JD et al. 2026. Performance of traumatic encephalopathy syndrome criteria in identifying individuals with chronic traumatic encephalopathy. evidence: citations/arena-2026-performance-tes-criteria-cte-nc.md
- PMID:35481808 Asken BM et al. 2022. Multi-Modal Biomarkers of Repetitive Head Impacts and Traumatic Encephalopathy Syndrome: A Clinicopathological Case Series. evidence: citations/asken-2022-biomarkers-rhi-tes-clinicopathological-series.md
- https://alz-journals.onlinelibrary.wiley.com/doi/abs/10.1002/alz.046505 Atherton K et al. 2020. Genome wide association study of chronic traumatic encephalopathy. evidence: citations/atherton-2020-gwas-cte-abstract.md
- PMID:35759276 Atherton K et al. 2022. Association of APOE Genotypes and Chronic Traumatic Encephalopathy. evidence: citations/atherton-2022-apoe-genotypes-cte.md
- PMID:26518018 Bieniek KF et al. 2015. Chronic traumatic encephalopathy pathology in a neurodegenerative disorders brain bank. evidence: citations/bieniek-2015-cte-pathology-neurodegenerative-brain-bank.md
- PMID:31199537 Bieniek KF et al. 2020. Association between contact sports participation and chronic traumatic encephalopathy: a retrospective cohort study. evidence: citations/bieniek-2020-contact-sports-mayo-cohort.md
- PMID:33611507 Bieniek KF et al. 2021. The Second NINDS/NIBIB Consensus Meeting to Define Neuropathological Criteria for the Diagnosis of Chronic Traumatic Encephalopathy. evidence: citations/bieniek-2021-second-ninds-nibib-consensus.md
- https://www.biorxiv.org/content/10.64898/2025.12.29.696879v1.full Authors not retrieved 2025. Injury-induced CTE-like pathology emerges in a human multicellular in vitro brain model and reveals mitochondrial and neurovascular regulation. evidence: citations/biorxiv-2025-injury-cte-like-multicellular-model.md
- PMID:33139536 Braun NJ et al. 2020. Mechanical injuries of neurons induce tau mislocalization to dendritic spines and tau-dependent synaptic dysfunction. evidence: citations/braun-2020-mechanical-injury-neurons-tau.md
- PMID:32774238 Breen PW et al. 2020. Recent Preclinical Insights Into the Treatment of Chronic Traumatic Encephalopathy. evidence: citations/breen-2020-preclinical-treatment-cte-review.md
- PMID:41377989 Breen KA et al. 2026. Duration of contact sports play associated with aberrant DNA methylation in human frontal cortex. evidence: citations/breen-2026-contact-sports-dna-methylation-preprint.md
- PMID:35903039 Butler MLMD et al. 2022. Tau Pathology in Chronic Traumatic Encephalopathy is Primarily Neuronal. evidence: citations/butler-2022-tau-primarily-neuronal.md
- PMID:40963024 Butler MLMD et al. 2025. Repeated head trauma causes neuron loss and inflammation in young athletes. evidence: citations/butler-2025-repeated-head-trauma-neuron-loss.md
- PMID:31215252 Cantu R et al. 2019. Management of chronic traumatic encephalopathy. evidence: citations/cantu-2019-management-chronic-traumatic-encephalopathy.md
- PMID:29036831 Castellani RJ et al. 2017. Dementia Pugilistica Revisited. evidence: citations/castellani-2017-dementia-pugilistica-revisited.md
- https://www.cdc.gov/traumatic-brain-injury/about/repeated-head-impacts.html Centers for Disease Control and Prevention 2024. About Repeated Head Impacts. evidence: citations/cdc-2024-about-repeated-head-impacts.md
- PMID:34019156 Chancellor KB et al. 2021. Altered oligodendroglia and astroglia in chronic traumatic encephalopathy. evidence: citations/chancellor-2021-oligodendroglia-astroglia.md
- PMID:27793189 Cherry JD et al. 2016. Microglial neuroinflammation contributes to tau accumulation in chronic traumatic encephalopathy. evidence: citations/cherry-2016-microglial-neuroinflammation-tau.md
- PMID:28950005 Cherry JD et al. 2017. CCL11 is increased in the CNS in chronic traumatic encephalopathy but not in Alzheimer's disease. evidence: citations/cherry-2017-ccl11-cns-cte.md
- PMID:30390709 Cherry JD et al. 2018. Variation in TMEM106B in chronic traumatic encephalopathy. evidence: citations/cherry-2018-tmem106b-variation-cte.md
- PMID:33278887 Cherry JD et al. 2020. CCL2 is associated with microglia and macrophage recruitment in chronic traumatic encephalopathy. evidence: citations/cherry-2020-ccl2-microglia-recruitment.md
- NCT02003183 University of California et al. 2013. Traumatic Brain Injury and Risk for Chronic Traumatic Encephalopathy. evidence: citations/clinicaltrials-nct02003183-fddnp-pet-cte-risk.md
- NCT02266563 Samuel Gandy 2015. Amyloid and Tauopathy PET Imaging in Acute and Chronic Traumatic Brain Injury. evidence: citations/clinicaltrials-nct02266563-amyloid-tauopathy-pet-tbi.md
- NCT02460094 ClinicalTrials.gov registry record 2015. A Randomized, Double-Blind, Placebo-Controlled, Multiple Ascending Dose Study of Intravenously Administered BMS-986168 in Patients With Progressive Supranuclear Palsy. evidence: citations/clinicaltrials-nct02460094-biib092-mad-psp.md
- NCT02959294 Robert W. Alexander et al. 2018. Use of Adipose-Derived Stem/Stromal Cells in Concussion and Traumatic Brain Injuries. evidence: citations/clinicaltrials-nct02959294-adipose-stromal-cells-withdrawn.md
- NCT03068468 ClinicalTrials.gov registry record 2017. A Randomized, Double-Blind, Placebo-Controlled, Parallel-Group Study to Evaluate the Efficacy and Safety of Intravenously Administered BIIB092 in Participants With Progressive Supranuclear Palsy. evidence: citations/clinicaltrials-nct03068468-gosuranemab-psp-passport.md
- NCT03218332 University Health Network et al. 2011. Post-Concussion Syndrome in Professional Athletes: A Multidisciplinary Study. evidence: citations/clinicaltrials-nct03218332-post-concussion-athletes-cte-biomarkers.md
- NCT03352557 ClinicalTrials.gov registry record 2018. Randomized, Double-Blind, Placebo-Controlled, Parallel-Group Study to Assess the Safety, Tolerability, and Efficacy of BIIB092 in Subjects With Mild Cognitive Impairment Due to Alzheimer's Disease or With Mild Alzheimer's Disease. evidence: citations/clinicaltrials-nct03352557-gosuranemab-early-ad.md
- NCT04796207 University of Arizona 2019. The Effects of Fish Oil Supplementation on the Brain Health of Collegiate Football Athletes. evidence: citations/clinicaltrials-nct04796207-fish-oil-football-subconcussion.md
- NCT04928534 Tianjin Medical University 2021. Cohort Study of Blood Biomarkers for TES. evidence: citations/clinicaltrials-nct04928534-blood-biomarkers-tes.md
- NCT05490576 Macquarie University et al. 2023. Tau And Connectomics In TES Study. evidence: citations/clinicaltrials-nct05490576-tau-connectomics-tes-pet.md
- PMID:25348064 Crary JF et al. 2014. Primary age-related tauopathy (PART): a common pathology associated with human aging. evidence: citations/crary-2014-primary-age-related-tauopathy.md
- PMID:37803386 Cummings JL et al. 2023. The therapeutic landscape of tauopathies: challenges and prospects. evidence: citations/cummings-2023-therapeutic-landscape-tauopathies.md
- PMID:37897548 Dams-O'Connor K et al. 2023. The neuropathology of intimate partner violence. evidence: citations/dams-oconnor-2023-intimate-partner-violence-neuropathology.md
- PMID:34910152 Daneshvar DH et al. 2021. Incidence of and Mortality From Amyotrophic Lateral Sclerosis in National Football League Athletes. evidence: citations/daneshvar-2021-als-incidence-mortality-nfl.md
- PMID:42642105 Daneshvar DH et al. 2026. Prevalence of chronic traumatic encephalopathy at death in National Football League players: retrospective population based cohort study, 2008-21. evidence: citations/daneshvar-2026-cte-prevalence-at-death-nfl.md
- PMID:32094584 Dickstein DL et al. 2021. Brain and blood biomarkers of tauopathy and neuronal injury in humans and rats with neurobehavioral syndromes following blast exposure. evidence: citations/dickstein-2021-blast-rats-tau-biomarkers.md
- PMID:41166474 Dong G et al. 2025. Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. evidence: citations/dong-2025-somatic-genomic-alterations-neurons.md
- PMID:37798551 Eagle SR et al. 2024. Interaction of Medical Conditions and Football Exposures Associated with Premortem Chronic Traumatic Encephalopathy Diagnosis in Former Professional American Football Players. evidence: citations/eagle-2024-premortem-cte-diagnosis-football-exposures.md
- PMID:40879226 Esin RG et al. 2025. [Chronic traumatic encephalopathy]. evidence: citations/esin-2025-chronic-traumatic-encephalopathy-review-russian.md
- PMID:30894745 Falcon B et al. 2019. Novel tau filament fold in chronic traumatic encephalopathy encloses hydrophobic molecules. evidence: citations/falcon-2019-novel-tau-filament.md
- PMID:29394252 Farah G et al. 2018. Tau accumulations in the brains of woodpeckers. evidence: citations/farah-2018-woodpecker-tau.md
- PMID:39277838 Fortington LV et al. 2025. Epidemiological Principles in Claims of Causality: An Enquiry into Repetitive Head Impacts (RHI) and Chronic Traumatic Encephalopathy (CTE). evidence: citations/fortington-2025-epidemiological-principles-rhi-cte.md
- DOI:10.3389/fneur.2024.1378620 Authors not retrieved 2024. Recent insights from non-mammalian models of brain injuries: an emerging literature. evidence: citations/frontiers-2024-non-mammalian-models-injury.md
- DOI:10.3389/fncel.2024.1371213 Authors not retrieved 2024. An overview of preclinical models of traumatic brain injury (TBI): relevance to pathophysiological mechanisms. evidence: citations/frontiers-2024-preclinical-tbi-models-overview.md
- PMID:42949744 Gallini J et al. 2026. Bias-Adjusted Prevalence of Chronic Traumatic Encephalopathy Among Deceased National Football League Players. evidence: citations/gallini-2026-bias-adjusted-prevalence-cte-nfl.md
- PMID:26336629 Gardner RC et al. 2015. Evaluating and treating neurobehavioral symptoms in professional American football players: Lessons from a case series. evidence: citations/gardner-2015-evaluating-treating-neurobehavioral-symptoms-nfl.md
- PMID:22593173 Goldstein LE et al. 2012. Chronic traumatic encephalopathy in blast-exposed military veterans and a blast neurotrauma mouse model. evidence: citations/goldstein-2012-blast-mouse-model.md
- PMID:39312218 Grashow R et al. 2024. Perceived Chronic Traumatic Encephalopathy and Suicidality in Former Professional Football Players. evidence: citations/grashow-2024-perceived-cte-suicidality-football.md
- PMID:40239644 Han X et al. 2025. A structural haplotype in the 17q21.31 MAPT region is associated with increased risk for chronic traumatic encephalopathy endophenotypes. evidence: citations/han-2025-mapt-h1-haplotype-cte.md
- PMID:41264095 Hartman S et al. 2025. Genetic variation in TMEM106B alters microglial activation and cytokine responses in chronic traumatic encephalopathy. evidence: citations/hartman-2025-tmem106b-microglia-cytokines.md
- PMID:35862387 Hearn R et al. 2022. The effects of active rehabilitation on symptoms associated with tau pathology: An umbrella review. Implications for chronic traumatic encephalopathy symptom management. evidence: citations/hearn-2022-active-rehabilitation-tauopathies-umbrella-review.md
- PMID:38814891 Hearn R et al. 2024. The effects of person-centred active rehabilitation on symptoms of suspected Chronic Traumatic Encephalopathy: A mixed-methods single case design. evidence: citations/hearn-2024-person-centred-active-rehabilitation-suspected-cte.md
- https://rest.genenames.org/fetch/symbol/MAPT HUGO Gene Nomenclature Committee 2026. HGNC gene symbol lookup for CTE report genes (MAPT, APOE, TMEM106B, GRN, TARDBP, APP, SNCA, CCL11, GFAP, NEFL, TREM2, CD68). evidence: citations/hgnc-genes-cte-terms.md
- https://icdlist.com/icd-10/F07.81 Authors not stated 2026. \"ICD-10-CM Diagnosis Code F07.81: Postconcussional syndrome\" (icdlist.com). evidence: citations/icdlist-2026-icd10cm-f07-81-postconcussional-syndrome.md
- PMID:31670780 Iverson GL et al. 2019. Chronic traumatic encephalopathy neuropathology might not be inexorably progressive or unique to repetitive neurotrauma. evidence: citations/iverson-2019-cte-not-inexorably-progressive.md
- PMID:31169877 Iverson GL et al. 2019. Mild Chronic Traumatic Encephalopathy Neuropathology in People With No Known Participation in Contact Sports or History of Repetitive Neurotrauma. evidence: citations/iverson-2019-mild-cte-no-contact-sports.md
- PMID:37404944 Iverson GL et al. 2023. Chronic traumatic encephalopathy neuropathologic change is uncommon in men who played amateur American football. evidence: citations/iverson-2023-cte-nc-uncommon-amateur-football.md
- PMID:41612558 Jansson D et al. 2026. Alterations in CSF Amyloid-β and Tau Biomarkers in Former College and Professional American Football Players: Findings from the DIAGNOSE CTE Research Project. evidence: citations/jansson-2026-csf-biomarkers-diagnose.md
- PMID:42341996 Jun S et al. 2026. Chronic traumatic encephalopathy: A devastating legacy of repetitive concussion. evidence: citations/jun-2026-cte-devastating-legacy-repetitive-concussion.md
- PMID:40046332 Kamps S et al. 2025. Enlarged cavum septum pellucidum as a neuroimaging signature of head impact exposure. evidence: citations/kamps-2025-enlarged-cavum-neuroimaging.md
- PMID:33722990 Katz DI et al. 2021. National Institute of Neurological Disorders and Stroke Consensus Diagnostic Criteria for Traumatic Encephalopathy Syndrome. evidence: citations/katz-2021-nindd-traumatic-encephalopathy-syndrome-criteria.md
- PMID:24127584 Katzenberger RJ et al. 2013. A Drosophila model of closed head traumatic brain injury. evidence: citations/katzenberger-2013-drosophila-closed-head-tbi.md
- PMID:29155947 Kenney K et al. 2018. Dementia After Moderate-Severe Traumatic Brain Injury: Coexistence of Multiple Proteinopathies. evidence: citations/kenney-2018-dementia-moderate-severe-tbi.md
- PMID:37456643 Kim PS et al. 2023. Legal medicine implications of a multidisciplinary approach to managing Traumatic Encephalopathy Syndrome in Australia. evidence: citations/kim-2023-legal-medicine-multidisciplinary-tes-management.md
- PMID:41508043 Kimura T et al. 2026. Repetitive mild traumatic brain injury with the closed-head impact model of engineered rotational acceleration (CHIMERA) promotes tau pathology in tau transgenic mice and its propagation in brains injected with tau fibrils. evidence: citations/kimura-2026-chimera-tau-transgenic.md
- PMID:36617181 Kirsch D et al. 2023. Vascular injury is associated with repetitive head impacts and tau pathology in chronic traumatic encephalopathy. evidence: citations/kirsch-2023-vascular-injury-rhi-tau.md
- PMID:42288852 Conway Kleven BD et al. 2026. Cognitive, biomarker, and neuroimaging indices associated with traumatic encephalopathy syndrome across two independent athlete cohorts. evidence: citations/kleven-2026-tes-multidomain-indices.md
- PMID:26414478 Koerte IK et al. 2016. Cavum Septi Pellucidi in Symptomatic Former Professional Football Players. evidence: citations/koerte-2016-cavum-septi-football.md
- PMID:26659578 Kovacs GG et al. 2016. Aging-related tau astrogliopathy (ARTAG): harmonized evaluation strategy. evidence: citations/kovacs-2016-artag-harmonized.md
- PMID:36895005 Labadorf A et al. 2023. Inflammation and neuronal gene expression changes differ in early versus late chronic traumatic encephalopathy brain. evidence: citations/labadorf-2023-early-late-cte-gene-expression.md
- PMID:38579683 Lai JD et al. 2024. KCNJ2 inhibition mitigates mechanical injury in a human brain organoid model of traumatic brain injury. evidence: citations/lai-2024-kcnj2-organoid-tbi.md
- PMID:41589584 Layden RM et al. 2026. CTE neuropathology alone is associated with dementia and cognitive symptoms. evidence: citations/layden-2026-cte-neuropathology-dementia-symptoms.md
- PMID:22955124 Lehman EJ et al. 2012. Neurodegenerative causes of death among retired National Football League players. evidence: citations/lehman-2012-neurodegenerative-causes-of-death-nfl.md
- PMID:36324216 Liang B et al. 2023. Long-Term Changes in Brain Connectivity Reflected in Quantitative Electrophysiology of Symptomatic Former National Football League Players. evidence: citations/liang-2023-qeeg-former-nfl.md
- PMID:28205009 Ling H et al. 2017. Mixed pathologies including chronic traumatic encephalopathy account for dementia in retired association football (soccer) players. evidence: citations/ling-2017-mixed-pathologies-football.md
- PMID:40749155 LoBue C et al. 2025. Cognitive Impairment and Dementia-Related Diagnoses in Chronic Traumatic Encephalopathy: A Systematic Review and Meta-Analysis. evidence: citations/lobue-2025-cognitive-impairment-dementia-cte-meta-analysis.md
- PMID:42534468 Luster CB et al. 2026. Neurodegenerative mortality among National Football League Players. evidence: citations/luster-2026-neurodegenerative-mortality-nfl.md
- PMID:31633894 Mackay DF et al. 2019. Neurodegenerative Disease Mortality among Former Professional Soccer Players. evidence: citations/mackay-2019-neurodegenerative-disease-mortality-soccer.md
- PMID:17503873 McCrory P et al. 2007. The evidence for chronic traumatic encephalopathy in boxing. evidence: citations/mccrory-2007-evidence-cte-boxing.md
- PMID:19535999 McKee AC et al. 2009. Chronic traumatic encephalopathy in athletes: progressive tauopathy after repetitive head injury. evidence: citations/mckee-2009-cte-athletes-progressive-tauopathy.md
- PMID:20720505 McKee AC et al. 2010. TDP-43 proteinopathy and motor neuron disease in chronic traumatic encephalopathy. evidence: citations/mckee-2010-tdp43-proteinopathy-mnd.md
- PMID:23208308 McKee AC et al. 2013. The spectrum of disease in chronic traumatic encephalopathy. evidence: citations/mckee-2013-spectrum-disease-cte.md
- PMID:25904048 McKee AC et al. 2015. The neuropathology of chronic traumatic encephalopathy. evidence: citations/mckee-2015-neuropathology-cte-review.md
- PMID:26667418 McKee AC et al. 2016. The first NINDS/NIBIB consensus meeting to define neuropathological criteria for the diagnosis of chronic traumatic encephalopathy. evidence: citations/mckee-2016-first-ninds-nibib-consensus.md
- PMID:36759368 McKee AC et al. 2023. Chronic traumatic encephalopathy (CTE): criteria for neuropathological diagnosis and relationship to repetitive head impacts. evidence: citations/mckee-2023-cte-criteria-repetitive-head-impacts.md
- PMID:37639244 McKee AC et al. 2023. Neuropathologic and Clinical Findings in Young Contact Sport Athletes Exposed to Repetitive Head Impacts. evidence: citations/mckee-2023-young-contact-sport-athletes.md
- https://www.medlink.com/articles/chronic-traumatic-encephalopathy Authors not stated not stated in retrieved text. \"Chronic traumatic encephalopathy\" (MedLink Neurology review). evidence: citations/medlink-chronic-traumatic-encephalopathy-history-review.md
- PMID:41651695 Melchior B et al. 2026. Targeting dual specificity tyrosine-phosphorylation-regulated kinase 1A mitigates tauopathy and enhances recovery after repetitive head injury. evidence: citations/melchior-2026-dyrk1a-repetitive-head-injury.md
- MESH:D000070627 National Library of Medicine 2017 (dateIntroduced; lastUpdated 2021-03-12). MeSH descriptor D000070627 Chronic Traumatic Encephalopathy. evidence: citations/mesh-2017-d000070627-chronic-traumatic-encephalopathy.md
- PMID:28742910 Mez J et al. 2017. Clinicopathological Evaluation of Chronic Traumatic Encephalopathy in Players of American Football. evidence: citations/mez-2017-clinicopathological-football.md
- PMID:31589352 Mez J et al. 2020. Duration of American Football Play and Chronic Traumatic Encephalopathy. evidence: citations/mez-2020-duration-football-play.md
- PMID:33826224 Mez J et al. 2021. Validity of the 2014 traumatic encephalopathy syndrome criteria for CTE pathology. evidence: citations/mez-2021-validity-2014-tes-criteria.md
- PMID:42282171 Mez J et al. 2026. Validity of the NINDS traumatic encephalopathy syndrome criteria for predicting chronic traumatic encephalopathy. evidence: citations/mez-2026-validity-ninds-tes-criteria-preprint.md
- PMID:39351900 Miner AE et al. 2024. Examination of plasma biomarkers of amyloid, tau, neurodegeneration, and neuroinflammation in former elite American football players. evidence: citations/miner-2024-plasma-biomarkers-football.md
- PMID:42440317 Miner AE et al. 2026. Plasma Phosphorylated Tau 217 in Participants at Risk for Chronic Traumatic Encephalopathy. evidence: citations/miner-2026-plasma-ptau217-rhi.md
- PMID:25580160 Montenigro PH et al. 2014. Clinical subtypes of chronic traumatic encephalopathy: literature review and proposed research diagnostic criteria for traumatic encephalopathy syndrome. evidence: citations/montenigro-2014-clinical-subtypes-tes-criteria.md
- PMID:39943994 Moraga-Amaro R et al. 2025. Short- and long-term changes in neurological, behavioural, and blood biomarkers following repeated mild traumatic brain injury in rats-potential biological sex-dependent effects. evidence: citations/moraga-amaro-2025-rat-rmtbi-florzolotau.md
- PMID:29298849 Moszczynski AJ et al. 2018. Pathologic Thr175 tau phosphorylation in CTE and CTE with ALS. evidence: citations/moszczynski-2018-pthr175-tau-phosphorylation.md
- PMID:29993324 Mouzon B et al. 2019. Chronic White Matter Degeneration, but No Tau Pathology at One-Year Post-Repetitive Mild Traumatic Brain Injury in a Tau Transgenic Model. evidence: citations/mouzon-2019-no-tau-pathology-tg-model.md
- https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy Retrieval log 2026. Database presence check: ClinVar, OMIM, GWAS Catalog and PubMed for chronic traumatic encephalopathy (queries run 2026-11-09). evidence: citations/ncbi-clinvar-omim-gwas-catalog-check-2026.md
- PMID:35937061 Nowinski CJ et al. 2022. Applying the Bradford Hill Criteria for Causation to Repetitive Head Impacts and Chronic Traumatic Encephalopathy. evidence: citations/nowinski-2022-bradford-hill-repetitive-head-impacts.md
- PMID:23334597 Ojo JO et al. 2013. Repetitive mild traumatic brain injury augments tau pathology and glial activation in aged hTau mice. evidence: citations/ojo-2013-repetitive-mild-tbi-hTau-mice.md
- MONDO:0019976 EBI Ontology Lookup Service 2026. EBI OLS4 / MONDO record MONDO:0019976 chronic traumatic encephalopathy. evidence: citations/ols-2026-mondo-0019976-chronic-traumatic-encephalopathy.md
- MONDO:0043512 EBI Ontology Lookup Service 2026. EBI OLS4 / MONDO record MONDO:0043512 traumatic encephalopathy. evidence: citations/ols-2026-mondo-0043512-traumatic-encephalopathy.md
- https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0019976/parents EBI Ontology Lookup Service 2026. EBI OLS4 spot-check - parents of MONDO:0019976 (chronic traumatic encephalopathy). evidence: citations/ols-spotcheck-2026-mondo-0019976-parents.md
- PMID:15987548 Omalu BI et al. 2005. Chronic traumatic encephalopathy in a National Football League player. evidence: citations/omalu-2005-cte-national-football-league-player.md
- MONDO:0043512 EMBL-EBI Ontology Lookup Service 2026. EBI OLS4 ontology term lookup: MONDO terms for CTE knowledge-base (ontology supplement). evidence: citations/ontology-supplement-mondo-terms.md
- https://academic.oup.com/brain/article/141/1/318/4774567 Authors not stated 2018. Dr Harrison Martland and the history of punch drunk syndrome. evidence: citations/oup-2018-martland-history-punch-drunk.md
- PMID:37316210 Patricios JS et al. 2023. Consensus statement on concussion in sport: the 6th International Conference on Concussion in Sport-Amsterdam, October 2022. evidence: citations/patricios-2023-amsterdam-2022-consensus-concussion-sport.md
- PMID:42603909 Pennington HE et al. 2026. Proteomic analysis of human chronic traumatic encephalopathy brain implicates proteasome and ribosome dysfunction in disease severity. evidence: citations/pennington-2026-proteomic-proteasome-ribosome.md
- PMID:39921702 Osterman C et al. 2025. Perivascular glial reactivity is a feature of phosphorylated tau lesions in chronic traumatic encephalopathy. evidence: citations/perivascular-2025-glial-reactivity-ptau-lesions.md
- PMID:25593768 Petraglia AL et al. 2014. The pathophysiology underlying repetitive mild traumatic brain injury in a novel mouse model of chronic traumatic encephalopathy. evidence: citations/petraglia-2014-repetitive-mild-tbi-mouse-model.md
- PMID:31306587 Pfaller AY et al. 2019. Effect of a New Rule Limiting Full Contact Practice on the Incidence of Sport-Related Concussion in High School Football Players. evidence: citations/pfaller-2019-rule-limiting-full-contact-practice.md
- PMID:35675177 Priemer DS et al. 2022. Chronic Traumatic Encephalopathy in the Brains of Military Personnel. evidence: citations/priemer-2022-military-personnel-cte.md
- PMID:40194947 Qi B et al. 2025. Prevalence of Chronic Traumatic Encephalopathy in Athletes With Repetitive Head Impacts: A Systematic Review and Meta-Analysis. evidence: citations/qi-2025-prevalence-athletes-meta-analysis.md
- PMID:41627284 Rodriguez RD et al. 2026. Clinicopathological study of chronic traumatic encephalopathy pathology in a population-based cohort. evidence: citations/rodriguez-2026-population-based-sao-paulo-cohort.md
- PMID:37300418 Rossi C et al. 2023. Emerging Symptomatic Treatment of Chronic Traumatic Encephalopathy (CTE): a narrative review. evidence: citations/rossi-2023-emerging-symptomatic-treatment-cte.md
- PMID:24484225 Rowson S et al. 2014. Can helmet design reduce the risk of concussion in football?. evidence: citations/rowson-2014-helmet-design-concussion-football.md
- PMID:32694163 Russell ER et al. 2020. Mental health and suicide in former professional soccer players. evidence: citations/russell-2020-mental-health-suicide-soccer.md
- PMID:34338724 Russell ER et al. 2021. Association of Field Position and Career Length With Risk of Neurodegenerative Disease in Male Former Professional Soccer Players. evidence: citations/russell-2021-field-position-career-length-soccer.md
- PMID:39528258 Ryniejska M et al. 2025. The prevalence of chronic traumatic encephalopathy in a historical epilepsy post-mortem collection. evidence: citations/ryniejska-2025-corsellis-epilepsy-collection.md
- PMID:31608704 Sacramento CB et al. 2020. Anti-Phospho-Tau Gene Therapy for Chronic Traumatic Encephalopathy. evidence: citations/sacramento-2020-anti-phospho-tau-gene-therapy-cte-mouse.md
- PMID:33708171 Schaffert J et al. 2021. Frequency and Predictors of Traumatic Encephalopathy Syndrome in a Prospective Cohort of Retired Professional Athletes. evidence: citations/schaffert-2021-tes-frequency-retired-athletes.md
- PMID:41108192 Selmanovic E et al. 2025. Chronic traumatic encephalopathy neuropathologic change in the Late Effects of Traumatic Brain Injury project: Findings in a community autopsy cohort. evidence: citations/selmanovic-2025-community-autopsy-late-effects-tbi.md
- PMID:42931149 Shatirishvili N 2026. Fluid Biomarkers for the Antemortem Detection of Chronic Traumatic Encephalopathy: A Critical Review. evidence: citations/shatirishvili-2026-fluid-biomarkers-review.md
- PMID:27885490 Shively SB et al. 2017. Localized cortical chronic traumatic encephalopathy pathology after single, severe axonal injury in human brain. evidence: citations/shively-2017-localized-cortical-cte-axonal-injury.md
- PMID:29778361 Smoliga JM 2018. Reconsidering the woodpecker model of traumatic brain injury. evidence: citations/smoliga-2018-reconsidering-woodpecker-model.md
- DOI:10.1002/ar.25567 Smoliga 2026. From beaks to brains—Challenges in translating woodpecker biology into traumatic brain injury innovation. evidence: citations/smoliga-2026-beaks-to-brains-woodpecker.md
- PMID:25632088 Stamm JM et al. 2015. Age of first exposure to football and later-life cognitive impairment in former NFL players. evidence: citations/stamm-2015-age-first-exposure-nfl-cognition.md
- PMID:34854540 Stathas S et al. 2022. Tau phosphorylation sites serine202 and serine396 are differently altered in chronic traumatic encephalopathy and Alzheimer's disease. evidence: citations/stathas-2022-tau-ser202-ser396.md
- PMID:23966253 Stern RA et al. 2013. Clinical presentation of chronic traumatic encephalopathy. evidence: citations/stern-2013-clinical-presentation-cte.md
- PMID:38134231 Su Y et al. 2024. Flortaucipir tau PET findings from former professional and college American football players in the DIAGNOSE CTE research project. evidence: citations/su-2024-flortaucipir-diagnose.md
- DOI:10.5694/mja2.51420 Suter CM et al. 2022. Chronic traumatic encephalopathy in Australia: the first three years of the Australian Sports Brain Bank. evidence: citations/suter-2022-australian-sports-brain-bank-first-three-years.md
- PMID:37391669 Suter CM et al. 2023. Chronic traumatic encephalopathy in a female ex-professional Australian rules footballer. evidence: citations/suter-2023-chronic-traumatic-encephalopathy-female-afl-footballer.md
- https://www.healthquality.va.gov/guidelines/rehab/mtbi/ VA/DoD Clinical Practice Guideline Work Group 2021. Management and Rehabilitation of Post-Acute Mild Traumatic Brain Injury (mTBI) (2021) - VA/DOD Clinical Practice Guidelines (landing page). evidence: citations/va-dod-2021-post-acute-mtbi-guideline-landing.md
- PMID:36109185 Varlow C et al. 2023. Evaluation of Tau Radiotracers in Chronic Traumatic Encephalopathy. evidence: citations/varlow-2023-tau-radiotracers-cte.md
- PMID:39728882 Wahlquist VE et al. 2024. Youth Soccer Heading Exposure and Its Effects on Clinical Outcome Measures. evidence: citations/wahlquist-2024-youth-soccer-heading-exposure-clinical-measures.md
- PMID:39269838 Walsh M et al. 2024. Clinical and Neuropathological Correlates of Substance Use in American Football Players. evidence: citations/walsh-2024-substance-use-football-players.md
- PMID:37538536 Whelan BM et al. 2023. Effect of the 2018 NCAA Kickoff Rule Change on Concussion Rates in Collegiate Football: Results From a Division 1 Conference. evidence: citations/whelan-2023-ncaa-kickoff-rule-change.md
- PMID:30285061 Wiebe DJ et al. 2018. Association Between the Experimental Kickoff Rule and Concussion Rates in Ivy League Football. evidence: citations/wiebe-2018-ivy-league-experimental-kickoff-rule.md
- PMID:41218808 Wiegand TLT et al. 2026. Diffusion Alterations at the Gray Matter/White Matter Boundary in Traumatic Encephalopathy Syndrome. evidence: citations/wiegand-2026-gm-wm-diffusion-tes.md
- PMID:24328030 Wortzel HS et al. 2013. Chronic traumatic encephalopathy and suicide: a systematic review. evidence: citations/wortzel-2013-cte-suicide-systematic-review.md
- PMID:37578550 Yu F et al. 2023. Neuronal tau pathology worsens late-phase white matter degeneration after traumatic brain injury in transgenic mice. evidence: citations/yu-2023-neuronal-tau-white-matter-tbi.md
- PMID:42950990 Yun Y et al. 2026. Engineering human brain microphysiological systems for alzheimer's disease (AD) and chronic traumatic encephalopathy (CTE) modeling and drug testing: translational promise, limitations, and future directions. evidence: citations/yun-2026-brain-microphysiological-ad-cte.md


## Artifacts

- [PLAN.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/PLAN.md)
- [abdolmohammadi-2020-genetics-of-cte-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/abdolmohammadi-2020-genetics-of-cte-review.md)
- [abdolmohammadi-2024-ice-hockey-duration.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/abdolmohammadi-2024-ice-hockey-duration.md)
- [ackermans-2021-unconventional-animal-models.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ackermans-2021-unconventional-animal-models.md)
- [ackermans-2022-headbutting-bovids.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ackermans-2022-headbutting-bovids.md)
- [acs-2017-cte-brief-historical-overview.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/acs-2017-cte-brief-historical-overview.md)
- [adams-2024-substantia-nigra-contact-sports.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/adams-2024-substantia-nigra-contact-sports.md)
- [alosco-2017-age-first-exposure-neuropsychiatric-outcomes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2017-age-first-exposure-neuropsychiatric-outcomes.md)
- [alosco-2018-age-first-exposure-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2018-age-first-exposure-football.md)
- [alosco-2020-tau-deposition-mckee-staging.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2020-tau-deposition-mckee-staging.md)
- [alosco-2021-diagnose-cte-design.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2021-diagnose-cte-design.md)
- [alosco-2023-flortaucipir-postmortem.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2023-flortaucipir-postmortem.md)
- [alosco-2024-regional-tau-pathology-cte-correlates.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/alosco-2024-regional-tau-pathology-cte-correlates.md)
- [arciniega-2024-cavum-septum-diagnose.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/arciniega-2024-cavum-septum-diagnose.md)
- [arena-2026-performance-tes-criteria-cte-nc.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/arena-2026-performance-tes-criteria-cte-nc.md)
- [asken-2022-biomarkers-rhi-tes-clinicopathological-series.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/asken-2022-biomarkers-rhi-tes-clinicopathological-series.md)
- [atherton-2020-gwas-cte-abstract.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/atherton-2020-gwas-cte-abstract.md)
- [atherton-2022-apoe-genotypes-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/atherton-2022-apoe-genotypes-cte.md)
- [bieniek-2015-cte-pathology-neurodegenerative-brain-bank.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2015-cte-pathology-neurodegenerative-brain-bank.md)
- [bieniek-2020-contact-sports-mayo-cohort.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2020-contact-sports-mayo-cohort.md)
- [bieniek-2021-second-ninds-nibib-consensus.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bieniek-2021-second-ninds-nibib-consensus.md)
- [biorxiv-2025-injury-cte-like-multicellular-model.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/biorxiv-2025-injury-cte-like-multicellular-model.md)
- [braun-2020-mechanical-injury-neurons-tau.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/braun-2020-mechanical-injury-neurons-tau.md)
- [breen-2020-preclinical-treatment-cte-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/breen-2020-preclinical-treatment-cte-review.md)
- [breen-2026-contact-sports-dna-methylation-preprint.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/breen-2026-contact-sports-dna-methylation-preprint.md)
- [bruce-2023-football-parkinson-disease.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/bruce-2023-football-parkinson-disease.md)
- [butler-2022-tau-primarily-neuronal.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/butler-2022-tau-primarily-neuronal.md)
- [butler-2025-repeated-head-trauma-neuron-loss.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/butler-2025-repeated-head-trauma-neuron-loss.md)
- [cantu-2019-management-chronic-traumatic-encephalopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cantu-2019-management-chronic-traumatic-encephalopathy.md)
- [castellani-2017-dementia-pugilistica-revisited.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/castellani-2017-dementia-pugilistica-revisited.md)
- [cdc-2024-about-repeated-head-impacts.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cdc-2024-about-repeated-head-impacts.md)
- [chancellor-2021-oligodendroglia-astroglia.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/chancellor-2021-oligodendroglia-astroglia.md)
- [cherry-2016-microglial-neuroinflammation-tau.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2016-microglial-neuroinflammation-tau.md)
- [cherry-2017-ccl11-cns-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2017-ccl11-cns-cte.md)
- [cherry-2018-tmem106b-variation-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2018-tmem106b-variation-cte.md)
- [cherry-2020-ccl2-microglia-recruitment.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cherry-2020-ccl2-microglia-recruitment.md)
- [clinicaltrials-nct02003183-fddnp-pet-cte-risk.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02003183-fddnp-pet-cte-risk.md)
- [clinicaltrials-nct02266563-amyloid-tauopathy-pet-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02266563-amyloid-tauopathy-pet-tbi.md)
- [clinicaltrials-nct02460094-biib092-mad-psp.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02460094-biib092-mad-psp.md)
- [clinicaltrials-nct02959294-adipose-stromal-cells-withdrawn.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct02959294-adipose-stromal-cells-withdrawn.md)
- [clinicaltrials-nct03068468-gosuranemab-psp-passport.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03068468-gosuranemab-psp-passport.md)
- [clinicaltrials-nct03218332-post-concussion-athletes-cte-biomarkers.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03218332-post-concussion-athletes-cte-biomarkers.md)
- [clinicaltrials-nct03352557-gosuranemab-early-ad.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct03352557-gosuranemab-early-ad.md)
- [clinicaltrials-nct04796207-fish-oil-football-subconcussion.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct04796207-fish-oil-football-subconcussion.md)
- [clinicaltrials-nct04928534-blood-biomarkers-tes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct04928534-blood-biomarkers-tes.md)
- [clinicaltrials-nct05490576-tau-connectomics-tes-pet.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/clinicaltrials-nct05490576-tau-connectomics-tes-pet.md)
- [crary-2014-primary-age-related-tauopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/crary-2014-primary-age-related-tauopathy.md)
- [cummings-2023-therapeutic-landscape-tauopathies.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/cummings-2023-therapeutic-landscape-tauopathies.md)
- [dams-oconnor-2023-intimate-partner-violence-neuropathology.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dams-oconnor-2023-intimate-partner-violence-neuropathology.md)
- [daneshvar-2021-als-incidence-mortality-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/daneshvar-2021-als-incidence-mortality-nfl.md)
- [daneshvar-2026-cte-prevalence-at-death-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/daneshvar-2026-cte-prevalence-at-death-nfl.md)
- [dickstein-2021-blast-rats-tau-biomarkers.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dickstein-2021-blast-rats-tau-biomarkers.md)
- [dong-2025-somatic-genomic-alterations-neurons.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/dong-2025-somatic-genomic-alterations-neurons.md)
- [eagle-2024-premortem-cte-diagnosis-football-exposures.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/eagle-2024-premortem-cte-diagnosis-football-exposures.md)
- [esin-2025-chronic-traumatic-encephalopathy-review-russian.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/esin-2025-chronic-traumatic-encephalopathy-review-russian.md)
- [falcon-2019-novel-tau-filament.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/falcon-2019-novel-tau-filament.md)
- [farah-2018-woodpecker-tau.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/farah-2018-woodpecker-tau.md)
- [fortington-2025-epidemiological-principles-rhi-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/fortington-2025-epidemiological-principles-rhi-cte.md)
- [frontiers-2024-non-mammalian-models-injury.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/frontiers-2024-non-mammalian-models-injury.md)
- [frontiers-2024-preclinical-tbi-models-overview.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/frontiers-2024-preclinical-tbi-models-overview.md)
- [gallini-2026-bias-adjusted-prevalence-cte-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/gallini-2026-bias-adjusted-prevalence-cte-nfl.md)
- [gardner-2015-evaluating-treating-neurobehavioral-symptoms-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/gardner-2015-evaluating-treating-neurobehavioral-symptoms-nfl.md)
- [goldstein-2012-blast-mouse-model.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/goldstein-2012-blast-mouse-model.md)
- [grashow-2024-perceived-cte-suicidality-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/grashow-2024-perceived-cte-suicidality-football.md)
- [han-2025-mapt-h1-haplotype-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/han-2025-mapt-h1-haplotype-cte.md)
- [hartman-2025-tmem106b-microglia-cytokines.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hartman-2025-tmem106b-microglia-cytokines.md)
- [hearn-2022-active-rehabilitation-tauopathies-umbrella-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hearn-2022-active-rehabilitation-tauopathies-umbrella-review.md)
- [hearn-2024-person-centred-active-rehabilitation-suspected-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hearn-2024-person-centred-active-rehabilitation-suspected-cte.md)
- [hgnc-genes-cte-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/hgnc-genes-cte-terms.md)
- [icdlist-2026-icd10cm-f07-81-postconcussional-syndrome.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/icdlist-2026-icd10cm-f07-81-postconcussional-syndrome.md)
- [iverson-2019-cte-not-inexorably-progressive.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2019-cte-not-inexorably-progressive.md)
- [iverson-2019-mild-cte-no-contact-sports.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2019-mild-cte-no-contact-sports.md)
- [iverson-2023-cte-nc-uncommon-amateur-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/iverson-2023-cte-nc-uncommon-amateur-football.md)
- [jansson-2026-csf-biomarkers-diagnose.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/jansson-2026-csf-biomarkers-diagnose.md)
- [jun-2026-cte-devastating-legacy-repetitive-concussion.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/jun-2026-cte-devastating-legacy-repetitive-concussion.md)
- [kamps-2025-enlarged-cavum-neuroimaging.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kamps-2025-enlarged-cavum-neuroimaging.md)
- [katz-2021-nindd-traumatic-encephalopathy-syndrome-criteria.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/katz-2021-nindd-traumatic-encephalopathy-syndrome-criteria.md)
- [katzenberger-2013-drosophila-closed-head-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/katzenberger-2013-drosophila-closed-head-tbi.md)
- [kawamura-2023-pharmacological-treatment-suspected-cte-challenges.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kawamura-2023-pharmacological-treatment-suspected-cte-challenges.md)
- [kenney-2018-dementia-moderate-severe-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kenney-2018-dementia-moderate-severe-tbi.md)
- [kim-2023-legal-medicine-multidisciplinary-tes-management.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kim-2023-legal-medicine-multidisciplinary-tes-management.md)
- [kimura-2026-chimera-tau-transgenic.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kimura-2026-chimera-tau-transgenic.md)
- [kirsch-2023-vascular-injury-rhi-tau.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kirsch-2023-vascular-injury-rhi-tau.md)
- [kleven-2026-tes-multidomain-indices.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kleven-2026-tes-multidomain-indices.md)
- [koerte-2016-cavum-septi-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/koerte-2016-cavum-septi-football.md)
- [kovacs-2016-artag-harmonized.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/kovacs-2016-artag-harmonized.md)
- [labadorf-2023-early-late-cte-gene-expression.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/labadorf-2023-early-late-cte-gene-expression.md)
- [lai-2024-kcnj2-organoid-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lai-2024-kcnj2-organoid-tbi.md)
- [layden-2026-cte-neuropathology-dementia-symptoms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/layden-2026-cte-neuropathology-dementia-symptoms.md)
- [lehman-2012-neurodegenerative-causes-of-death-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lehman-2012-neurodegenerative-causes-of-death-nfl.md)
- [liang-2023-qeeg-former-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/liang-2023-qeeg-former-nfl.md)
- [ling-2017-mixed-pathologies-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ling-2017-mixed-pathologies-football.md)
- [lobue-2025-cognitive-impairment-dementia-cte-meta-analysis.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/lobue-2025-cognitive-impairment-dementia-cte-meta-analysis.md)
- [luster-2026-neurodegenerative-mortality-nfl.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/luster-2026-neurodegenerative-mortality-nfl.md)
- [mackay-2019-neurodegenerative-disease-mortality-soccer.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mackay-2019-neurodegenerative-disease-mortality-soccer.md)
- [mccrory-2007-evidence-cte-boxing.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mccrory-2007-evidence-cte-boxing.md)
- [mckee-2009-cte-athletes-progressive-tauopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2009-cte-athletes-progressive-tauopathy.md)
- [mckee-2010-tdp43-proteinopathy-mnd.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2010-tdp43-proteinopathy-mnd.md)
- [mckee-2013-spectrum-disease-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2013-spectrum-disease-cte.md)
- [mckee-2015-neuropathology-cte-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2015-neuropathology-cte-review.md)
- [mckee-2016-first-ninds-nibib-consensus.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2016-first-ninds-nibib-consensus.md)
- [mckee-2023-cte-criteria-repetitive-head-impacts.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2023-cte-criteria-repetitive-head-impacts.md)
- [mckee-2023-young-contact-sport-athletes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mckee-2023-young-contact-sport-athletes.md)
- [medlink-chronic-traumatic-encephalopathy-history-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/medlink-chronic-traumatic-encephalopathy-history-review.md)
- [melchior-2026-dyrk1a-repetitive-head-injury.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/melchior-2026-dyrk1a-repetitive-head-injury.md)
- [mesh-2017-d000070627-chronic-traumatic-encephalopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mesh-2017-d000070627-chronic-traumatic-encephalopathy.md)
- [mez-2017-clinicopathological-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2017-clinicopathological-football.md)
- [mez-2020-duration-football-play.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2020-duration-football-play.md)
- [mez-2021-validity-2014-tes-criteria.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2021-validity-2014-tes-criteria.md)
- [mez-2026-validity-ninds-tes-criteria-preprint.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mez-2026-validity-ninds-tes-criteria-preprint.md)
- [miner-2024-plasma-biomarkers-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/miner-2024-plasma-biomarkers-football.md)
- [miner-2026-plasma-ptau217-rhi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/miner-2026-plasma-ptau217-rhi.md)
- [montenigro-2014-clinical-subtypes-tes-criteria.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/montenigro-2014-clinical-subtypes-tes-criteria.md)
- [moraga-amaro-2025-rat-rmtbi-florzolotau.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/moraga-amaro-2025-rat-rmtbi-florzolotau.md)
- [moszczynski-2018-pthr175-tau-phosphorylation.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/moszczynski-2018-pthr175-tau-phosphorylation.md)
- [mouzon-2019-no-tau-pathology-tg-model.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/mouzon-2019-no-tau-pathology-tg-model.md)
- [ncbi-clinvar-omim-gwas-catalog-check-2026.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ncbi-clinvar-omim-gwas-catalog-check-2026.md)
- [nowinski-2022-bradford-hill-repetitive-head-impacts.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/nowinski-2022-bradford-hill-repetitive-head-impacts.md)
- [ojo-2013-repetitive-mild-tbi-hTau-mice.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ojo-2013-repetitive-mild-tbi-hTau-mice.md)
- [ojo-2016-repetitive-head-trauma-mice-to-men.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ojo-2016-repetitive-head-trauma-mice-to-men.md)
- [ols-2026-mondo-0019976-chronic-traumatic-encephalopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-2026-mondo-0019976-chronic-traumatic-encephalopathy.md)
- [ols-2026-mondo-0043512-traumatic-encephalopathy.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-2026-mondo-0043512-traumatic-encephalopathy.md)
- [ols-chebi-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-chebi-terms.md)
- [ols-cl-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-cl-terms.md)
- [ols-go-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-go-terms.md)
- [ols-hp-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-hp-terms.md)
- [ols-mondo-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-mondo-terms.md)
- [ols-ncbitaxon-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-ncbitaxon-terms.md)
- [ols-ncit-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-ncit-terms.md)
- [ols-spotcheck-2026-mondo-0019976-parents.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-spotcheck-2026-mondo-0019976-parents.md)
- [ols-uberon-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ols-uberon-terms.md)
- [omalu-2005-cte-national-football-league-player.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/omalu-2005-cte-national-football-league-player.md)
- [omalu-2011-histomorphologic-phenotypes-cte-athletes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/omalu-2011-histomorphologic-phenotypes-cte-athletes.md)
- [ontology-supplement-chebi-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-chebi-terms.md)
- [ontology-supplement-cl-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-cl-terms.md)
- [ontology-supplement-go-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-go-terms.md)
- [ontology-supplement-hp-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-hp-terms.md)
- [ontology-supplement-mondo-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-mondo-terms.md)
- [ontology-supplement-ncit-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-ncit-terms.md)
- [ontology-supplement-uberon-terms.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ontology-supplement-uberon-terms.md)
- [oup-2018-martland-history-punch-drunk.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/oup-2018-martland-history-punch-drunk.md)
- [patricios-2023-amsterdam-2022-consensus-concussion-sport.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/patricios-2023-amsterdam-2022-consensus-concussion-sport.md)
- [pennington-2026-proteomic-proteasome-ribosome.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/pennington-2026-proteomic-proteasome-ribosome.md)
- [perivascular-2025-glial-reactivity-ptau-lesions.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/perivascular-2025-glial-reactivity-ptau-lesions.md)
- [petraglia-2014-repetitive-mild-tbi-mouse-model.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/petraglia-2014-repetitive-mild-tbi-mouse-model.md)
- [pfaller-2019-rule-limiting-full-contact-practice.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/pfaller-2019-rule-limiting-full-contact-practice.md)
- [priemer-2022-military-personnel-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/priemer-2022-military-personnel-cte.md)
- [qi-2025-prevalence-athletes-meta-analysis.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/qi-2025-prevalence-athletes-meta-analysis.md)
- [rodriguez-2026-population-based-sao-paulo-cohort.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rodriguez-2026-population-based-sao-paulo-cohort.md)
- [rossi-2023-emerging-symptomatic-treatment-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rossi-2023-emerging-symptomatic-treatment-cte.md)
- [rowson-2014-helmet-design-concussion-football.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/rowson-2014-helmet-design-concussion-football.md)
- [russell-2020-mental-health-suicide-soccer.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/russell-2020-mental-health-suicide-soccer.md)
- [russell-2021-field-position-career-length-soccer.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/russell-2021-field-position-career-length-soccer.md)
- [ryniejska-2025-corsellis-epilepsy-collection.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/ryniejska-2025-corsellis-epilepsy-collection.md)
- [sacramento-2020-anti-phospho-tau-gene-therapy-cte-mouse.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/sacramento-2020-anti-phospho-tau-gene-therapy-cte-mouse.md)
- [schaffert-2021-tes-frequency-retired-athletes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/schaffert-2021-tes-frequency-retired-athletes.md)
- [selmanovic-2025-community-autopsy-late-effects-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/selmanovic-2025-community-autopsy-late-effects-tbi.md)
- [shatirishvili-2026-fluid-biomarkers-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/shatirishvili-2026-fluid-biomarkers-review.md)
- [shively-2017-localized-cortical-cte-axonal-injury.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/shively-2017-localized-cortical-cte-axonal-injury.md)
- [smoliga-2018-reconsidering-woodpecker-model.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/smoliga-2018-reconsidering-woodpecker-model.md)
- [smoliga-2026-beaks-to-brains-woodpecker.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/smoliga-2026-beaks-to-brains-woodpecker.md)
- [stamm-2015-age-first-exposure-nfl-cognition.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stamm-2015-age-first-exposure-nfl-cognition.md)
- [stathas-2022-tau-ser202-ser396.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stathas-2022-tau-ser202-ser396.md)
- [stern-2013-clinical-presentation-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/stern-2013-clinical-presentation-cte.md)
- [su-2024-flortaucipir-diagnose.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/su-2024-flortaucipir-diagnose.md)
- [suter-2022-australian-sports-brain-bank-first-three-years.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/suter-2022-australian-sports-brain-bank-first-three-years.md)
- [suter-2023-chronic-traumatic-encephalopathy-female-afl-footballer.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/suter-2023-chronic-traumatic-encephalopathy-female-afl-footballer.md)
- [tbicoe-2023-cte-research-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/tbicoe-2023-cte-research-review.md)
- [va-dod-2021-post-acute-mtbi-guideline-landing.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/va-dod-2021-post-acute-mtbi-guideline-landing.md)
- [varlow-2023-tau-radiotracers-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/varlow-2023-tau-radiotracers-cte.md)
- [vrillon-2026-flortaucipir-ptau217-differential.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/vrillon-2026-flortaucipir-ptau217-differential.md)
- [wahlquist-2024-youth-soccer-heading-exposure-clinical-measures.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wahlquist-2024-youth-soccer-heading-exposure-clinical-measures.md)
- [walsh-2024-substance-use-football-players.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/walsh-2024-substance-use-football-players.md)
- [whelan-2023-ncaa-kickoff-rule-change.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/whelan-2023-ncaa-kickoff-rule-change.md)
- [wiebe-2018-ivy-league-experimental-kickoff-rule.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wiebe-2018-ivy-league-experimental-kickoff-rule.md)
- [wiegand-2026-gm-wm-diffusion-tes.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wiegand-2026-gm-wm-diffusion-tes.md)
- [wortzel-2013-cte-suicide-systematic-review.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/wortzel-2013-cte-suicide-systematic-review.md)
- [yu-2023-neuronal-tau-white-matter-tbi.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/yu-2023-neuronal-tau-white-matter-tbi.md)
- [yun-2026-brain-microphysiological-ad-cte.md](Chronic_Traumatic_Encephalopathy-deep-research-claude_managed_artifacts/yun-2026-brain-microphysiological-ad-cte.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 135 |
| Resolved | 135 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 126 |
| Quoted claims found in source | 100 |
| Quoted claims **not** found in source | 26 |
| Quoted claims with nothing to check against | 3 |
| References weighed for topical relevance | 135 |
| On topic | 109 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40239644` *(abstract only)*: "having a copy of the H1β1γ1 allele conferred a similar risk of pathological tau accumulation to playing 9.6 years of football"
  - closest text in source: "Genetic variation in the 17q21.31 region, containing microtubule-associated protein tau (MAPT), has been implicated in tauopathies but has not been investigated in CTE"
- `PMID:42341996` *(abstract only)*: "are thought to act primarily as modifiers of disease susceptibility and progression rather than direct causal drivers"
  - closest text in source: "CTE is defined by a distinct pattern of perivascular hyperphosphorylated tau accumulation at the depths of cortical sulci, linking injury-associated biomechanical strain and vascular vulnerability to spatially localized disease progression"
- `PMID:28742910` *(abstract only)*: "Symptom frequencies remained similar when only pure CTE cases (ie, those with no neuropathological evidence of comorbid neurodegenerative disease) were considered"
  - closest text in source: "MAIN OUTCOMES AND MEASURES: Neuropathological diagnoses of neurodegenerative diseases, including CTE, based on defined diagnostic criteria; CTE neuropathological severity (stages I to IV or dichotomized into mild [stages I and II] and severe [stages III and IV]); informant-reported athletic history and, for players who died in 2014 or later, clinical presentation, including behavior, mood, and cognitive symptoms and dementia"
- `PMID:28742910` *(abstract only)*: "43 (90%) of those initially presenting with only behavior or mood symptoms were reported to have cognitive symptoms at the time of death"
  - closest text in source: "MAIN OUTCOMES AND MEASURES: Neuropathological diagnoses of neurodegenerative diseases, including CTE, based on defined diagnostic criteria; CTE neuropathological severity (stages I to IV or dichotomized into mild [stages I and II] and severe [stages III and IV]); informant-reported athletic history and, for players who died in 2014 or later, clinical presentation, including behavior, mood, and cognitive symptoms and dementia"
- `PMID:23966253` *(abstract only)*: "motor features, including parkinsonism, were not common in our sample"
  - closest text in source: "Consistent with earlier case reports of boxers, 2 relatively distinct clinical presentations emerged, with one group whose initial features developed at a younger age and involved behavioral and/or mood disturbance (n = 22), and another group whose initial presentation developed at an older age and involved cognitive impairment (n = 11)"
- `PMID:23966253` *(abstract only)*: "raise the possibility that cognitive reserve37 may have a role in protecting against the clinical manifestations of CTE"
  - closest text in source: "CONCLUSIONS: This suggests there are 2 major clinical presentations of CTE, one a behavior/mood variant and the other a cognitive variant."
- `PMID:42341996` *(abstract only)*: "a mean age of onset of 44.3 years (range 16–83, n = 119), with symptoms beginning on average 14.5 years after retirement"
  - Text part not found as substring: 'a mean age of onset of 44.3 years (range 16–83, n = 119), with symptoms beginning on average 14.5 years after retirement' (note: only abstract available for PMID:42341996, full text may contain this excerpt)
- `PMID:23966253` *(abstract only)*: "The mean length of time between dementia diagnosis and death was 8.0 years"
  - closest text in source: "Three subjects were asymptomatic at the time of death"
- `PMID:33826224` *(abstract only)*: "Cognitive (odds ratio [OR] = 3.6; 95% confidence interval [CI]: 1.2-5.1), but not mood/behavior or motor symptoms, were significantly associated with CTE pathology"
  - closest text in source: "Cognitive (odds ratio [OR] = 3.6; 95% confidence interval [CI]: 1.2-5.1), but not mood/behavior or motor symptoms, were significantly associated with CTE pathology"
- `PMID:28742910` *(abstract only)*: "The most common cause of death for participants with mild CTE pathology was suicide (12 [27%]) and for those with severe CTE pathology was neurodegenerative (ie, dementia-related and parkinsonian-related causes of death) (62 [47%])"
  - closest text in source: "MAIN OUTCOMES AND MEASURES: Neuropathological diagnoses of neurodegenerative diseases, including CTE, based on defined diagnostic criteria; CTE neuropathological severity (stages I to IV or dichotomized into mild [stages I and II] and severe [stages III and IV]); informant-reported athletic history and, for players who died in 2014 or later, clinical presentation, including behavior, mood, and cognitive symptoms and dementia"
- `PMID:36759368` *(abstract only)*: "thinning of the posterior corpus callosum in stage IV"
  - Text part not found as substring: 'thinning of the posterior corpus callosum in stage IV' (note: only abstract available for PMID:36759368, full text may contain this excerpt)
- `PMID:36759368` *(abstract only)*: "with the LC affected at all stages, including stage I"
  - closest text in source: "CTE has been reported in amateur and professional athletes, including a bull rider, boxers, wrestlers, and American, Canadian, and Australian rules football, rugby union, rugby league, soccer, and ice hockey players"
- `PMID:25904048` *(abstract only)*: "p‐tau pathology is found in discrete foci in the cerebral cortex, most commonly in the superior or lateral frontal cortices, typically around small vessels at the depths of sulci"
  - closest text in source: "CTE is a tauopathy characterized by the deposition of hyperphosphorylated tau (p-tau) protein as neurofibrillary tangles, astrocytic tangles and neurites in striking clusters around small blood vessels of the cortex, typically at the sulcal depths"
- `PMID:25904048` *(abstract only)*: "The medial temporal lobe is spared neurofibrillary p‐tau pathology"
  - closest text in source: "CTE is a tauopathy characterized by the deposition of hyperphosphorylated tau (p-tau) protein as neurofibrillary tangles, astrocytic tangles and neurites in striking clusters around small blood vessels of the cortex, typically at the sulcal depths"
- `PMID:25904048` *(abstract only)*: "marked neuronal loss in the cortex, amygdala and hippocampus"
  - closest text in source: "CTE is a tauopathy characterized by the deposition of hyperphosphorylated tau (p-tau) protein as neurofibrillary tangles, astrocytic tangles and neurites in striking clusters around small blood vessels of the cortex, typically at the sulcal depths"
- `PMID:36759368` *(abstract only)*: "on whether NFTs are present in the thalamus, mammillary bodies, hippocampus, amygdala, and entorhinal cortex"
  - closest text in source: "Here, we present the advances in the neuropathological diagnosis of CTE culminating with the development of the NINDS-NIBIB criteria, the multiple international studies that have used these criteria to report CTE in hundreds of contact sports players and others, and the evidence for a robust dose-response relationship between RHI and CTE."
- `PMID:36759368` *(abstract only)*: "Subpial TSA, or ARTAG, were considered only supportive, non-diagnostic, features of CTE"
  - closest text in source: "Since the publication of NINDS-NIBIB criteria for the neuropathological diagnosis of CTE in 2016, and diagnostic refinements in 2021, hundreds of contact sport athletes and others have been diagnosed at postmortem examination with CTE"
- `PMID:32774238` *(abstract only)*: "Aside from supportive treatment designed to address specific symptoms (such as depression or comorbid seizures)"
  - closest text in source: "We discuss the overall translational potential of these approaches and provide recommendations for future bench-to-bedside treatment strategies."
- `PMID:35862387` *(abstract only)*: "Evidence suggests that active rehabilitation has beneficial effects on vestibular/ocular symptoms"
  - closest text in source: "ELIGIBILITY: Systematic review or meta-analyses that examine the effect active rehabilitation has on outcome measures of symptoms associated with CTE"
- `PMID:37456643` *(abstract only)*: "The MDT is considered to be the appropriate or preferred model of care for the management of TES"
  - closest text in source: "In the case of Traumatic Encephalopathy Syndrome (TES), where there are no universally accepted clinical diagnostic criteria, a clear clinical diagnosis can pose significant challenges for healthcare providers and for subsequent appropriate management"
- `PMID:37803386` *(abstract only)*: "Tilavonemab’s development in PSP was halted after it failed to show efficacy over placebo even though target engagement had been established"
  - closest text in source: "This review outlines the landscape of therapeutic drugs (indexed through February 28, 2023) that target tau pathology and describes drug candidates in clinical development as well as those in the discovery and preclinical phases"
- `PMID:30285061` *(abstract only)*: "The kickoff rule change in Ivy League football was associated with a reduction in concussions"
  - closest text in source: "This before-after study investigates changes in concussion among Ivy League football players after implementation of a 2016 rule change intended to land more kickoffs in the end zone and reduce player injury."
- `PMID:39728882` *(abstract only)*: "prohibit heading for children 10 years old and younger, while those aged 11–13 are restricted by weekly practice exposure limits, however in game heading is unrestricted"
  - closest text in source: "The effects of RHI in the youth population are still unknown, therefore, the purpose of this study was to examine if heading exposure is predictive of changes in self-reported symptoms, neurocognitive functioning, gait, and balance in female youth soccer players over the course of one soccer season"
- `PMID:34255876` *(abstract only)*: "was originally determined from cattle brains"
  - Text part not found as substring: 'was originally determined from cattle brains' (note: only abstract available for PMID:34255876, full text may contain this excerpt)
- `PMID:42341996` *(abstract only)*: "is difficult to model in lissencephalic rodent brains, which lack the cortical folding that concentrates strain at the depths of the sulci"
  - closest text in source: "CTE is defined by a distinct pattern of perivascular hyperphosphorylated tau accumulation at the depths of cortical sulci, linking injury-associated biomechanical strain and vascular vulnerability to spatially localized disease progression"
- `PMID:34255876` *(abstract only)*: "Domestic sheep have thus emerged as the preferred large animal model for tauopathies"
  - closest text in source: "While current animal models of TBI and CTE such as rodents, are useful to explore affected pathways, clinical findings therein have rarely translated into clinical applications, possibly because of the many morphofunctional differences between the model animals and humans"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:37391669`: "there have been only a handful of CTE cases reported in females"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.5694/mja2.51420`: "Six of the 12 donors with CTE and one of nine without CTE had died by suicide (P = 0.042)"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:29778361`: "It remains unknown how closely woodpecker-specific tau pathology resembles chronic traumatic encephalopathy"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 146 |
| Resolved | 128 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Not in the configured ontologies | 7 |
| Terms whose name was checked | 123 |
| Terms named correctly | 104 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0043512` (13 mentions) - the report calls it "if available", "dementia due to head trauma; post-traumatic brain syndrome; post-traumatic dementia", "traumatic encephalopathy"; MONDO calls it **traumatic encephalopathy**
- `MONDO:0019976` (12 mentions) - the report calls it "A tauopathy characterized by progressive neurodegeneration secondary to repetitive mild traumatic brain injuries", "chronic traumatic encephalopathy", "Boxer's dementia; chronic traumatic encephalopathy; dementia pugilistica; punch-drunk syndrome"; MONDO calls it **chronic traumatic encephalopathy**
- `HP:0001251` (1 mention) - the report calls it "Ataxia; nearest term"; HP calls it **Ataxia**
- `GO:0008017` (1 mention) - the report calls it "microtubule binding; normal tau function lost on hyperphosphorylation, inferred"; GO calls it **microtubule binding**
- `GO:0042552` (1 mention) - the report calls it "myelination; white matter loss, inferred"; GO calls it **myelination**
- `CL:0000598` (1 mention) - the report calls it "pyramidal neuron; layer 2/3 sulcal neurons are lost"; CL calls it **pyramidal neuron**
- `CL:0000669` (1 mention) - the report calls it "pericyte; neurovascular unit, inferred"; CL calls it **pericyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000737` (1 mention) - the report calls it "Irritability; nearest term"; HP calls it **Irritability**
- `GO:0035633` (1 mention) - the report calls it "maintenance of blood-brain barrier; disrupted, inferred"; GO calls it **maintenance of blood-brain barrier**
- `GO:0070098` (1 mention) - the report calls it "chemokine-mediated signaling pathway; CCL2/CCL11"; GO calls it **chemokine-mediated signaling pathway**
- `GO:0006879` (1 mention) - the report calls it "intracellular iron ion homeostasis; closest match"; GO calls it **intracellular iron ion homeostasis**
- `GO:1990000` (1 mention) - the report calls it "amyloid fibril formation; process-level proxy for filament assembly"; GO calls it **amyloid fibril formation**
- `GO:0051402` (1 mention) - the report calls it "neuron apoptotic process; cell-death process, mode unproven"; GO calls it **neuron apoptotic process**
- `UBERON:0002240` (1 mention) - the report calls it "spinal cord; motor neuron disease subset"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names
- `NCIT:C265` (1 mention) - the report calls it "Antidepressant Agent; closest match"; NCIT calls it **Antidepressant Agent**
- `NCIT:C47792` (1 mention) - the report calls it "Acetylcholinesterase Inhibitor; closest match"; NCIT calls it **Acetylcholinesterase Inhibitor**
- `NCIT:C64345` (1 mention) - the report calls it "Cognitive Behavior Therapy; closest match"; NCIT calls it **Cognitive Behavior Therapy**
- `NCIT:C15315` (1 mention) - the report calls it "Rehabilitation; closest match"; NCIT calls it **Rehabilitation**, and lists "Rehabilitation, Medical" among its other names
- `NCIT:C159273` (1 mention) - the report calls it "Speech Language Therapy; closest match"; NCIT calls it **Speech Language Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0043512` - called "if available", "dementia due to head trauma; post-traumatic brain syndrome; post-traumatic dementia", "traumatic encephalopathy"
- `HGNC:6893` - called "MAPT", "MAPT; "microtubule associated protein tau"; NCBI Gene 4137; UniProt P10636"
- `MONDO:0019976` - called "A tauopathy characterized by progressive neurodegeneration secondary to repetitive mild traumatic brain injuries", "chronic traumatic encephalopathy", "Boxer's dementia; chronic traumatic encephalopathy; dementia pugilistica; punch-drunk syndrome"
- `MESH:D000070627` - called "dateIntroduced: 2017-01-01", "MeSH: D000070627 "Chronic Traumatic Encephalopathy", "dateIntroduced: 2017-01-01"

### Terms from ontologies the report was not asked to use

The report was asked for terms from a fixed set of ontologies, and these come from others, so they were not looked up. Nothing here is evidence of fabrication; it does mean the report reached outside the ontologies it was given:

- `MESH:D000070627` (3 mentions), reported as "dateIntroduced: 2017-01-01", "MeSH: D000070627 "Chronic Traumatic Encephalopathy", "dateIntroduced: 2017-01-01"
- `Orphanet:97353` (1 mention)
- `DOID:0081291` (1 mention)
- `UMLS:C0149843` (1 mention)
- `SCTID:230283005` (1 mention)
- `MEDGEN:508441` (1 mention)
- `GARD:0019371` (1 mention)
