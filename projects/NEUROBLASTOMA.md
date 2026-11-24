---
title: Neuroblastoma Family Project
status: IN_PROGRESS
description: >-
  Curation of neuroblastoma and the entries around it: the peripheral
  neuroblastic tumours, the germline syndromes that predispose to them, the
  paraneoplastic syndrome they cause, and the tumours that share the name but
  not the lineage.
tags: [DISEASE_DOMAIN, ONCOLOGY, PEDIATRIC_CANCER]
nih_topics:
  - NIH_HT_42_rare_cancers_across_cancer_control_continuum
  - NIH_HT_68_childhood_adolescent_young_adult_aya_cancer
diseases:
  - Neuroblastoma
  - Ganglioneuroblastoma
  - Ganglioneuroma
  - ALK-Related_Neuroblastic_Tumor_Susceptibility
  - PHOX2B-Related_Neuroblastic_Tumor_Susceptibility
  - BARD1-related_Cancer_Predisposition
  - Beckwith-Wiedemann_Syndrome
  - Congenital_Central_Hypoventilation_Syndrome
  - Costello_Syndrome
  - Fanconi_Anemia
  - Intellectual_Disability_X-linked_102
  - Li-Fraumeni_Syndrome
  - Neurofibromatosis_Type_1
  - Noonan_Syndrome
  - Simpson-Golabi-Behmel_Syndrome_Type_1
  - Sotos_Syndrome
  - Weaver_Syndrome
  - Opsoclonus_Myoclonus_Syndrome
  - Paraneoplastic_Neurological_Syndromes
  - Olfactory_Neuroblastoma
  - CNS_Neuroblastoma_FOXR2-Activated
  - Pheochromocytoma_Paraganglioma
modules:
  - sustaining_proliferative_signaling
  - evading_growth_suppressors
  - enabling_replicative_immortality
  - invasion_and_metastasis
groupings:
  - Peripheral_Neuroblastic_Tumors
  - Neuroblastoma_Predisposition_Syndromes
drugs:
  - id: CHEBI:6067
    label: isotretinoin
  - id: CHEBI:41948
    label: eflornithine
  - id: CHEBI:135997
    label: iobenguane (131I)
  - id: CHEBI:125628
    label: alisertib
  - id: CHEBI:91414
    label: adavosertib
  - id: CHEBI:27899
    label: cisplatin
  - id: NCIT:C1570
    label: Dinutuximab
  - id: NCIT:C123428
    label: Naxitamab
phenotypes:
  - id: HP:0003006
    label: Neuroblastoma
  - id: HP:0004376
    label: Neuroblastic tumor
  - id: HP:0010543
    label: Opsoclonus
  - id: HP:0002277
    label: Horner syndrome
  - id: HP:0005208
    label: Secretory diarrhea
  - id: HP:0000520
    label: Proptosis
---

# Neuroblastoma Family Project

## Overview

This project tracks the curation of `Neuroblastoma` and the 21 entries around
it. It is the neuroblastoma part of the childhood-cancer work in
[`CHILDHOOD_CANCER.md`](CHILDHOOD_CANCER.md) and of the Tier 4 and Tier 13
rows of [`CANCER.md`](CANCER.md). Individual changes are tracked in
[dismech#14976](https://github.com/monarch-initiative/dismech/issues/14976).

## Scope: where each kind of thing is recorded

The family follows the cancer granularity ladder in design decisions §3a
([`docs/explanation/design-decisions.md`](../docs/explanation/design-decisions.md)).

| Rung | In this family | Where it is recorded |
|---|---|---|
| Histologic entity | Neuroblastoma (the Schwannian stroma-poor category of the International Neuroblastoma Pathology Classification), ganglioneuroblastoma, ganglioneuroma | Three entries, `Neuroblastoma` (`MONDO:0005072`), `Ganglioneuroblastoma` (`MONDO:0005035`) and `Ganglioneuroma` (`MONDO:0005033`), collected in `Peripheral_Neuroblastic_Tumors` |
| Biomarker or risk stratum | MYCN-amplified and high-risk neuroblastoma | `has_subtypes` on `Neuroblastoma`, beside the adrenal gland subclass (`MONDO:0006076`) |
| Stage | INRGSS L1, L2, M and MS | `stages:` on `Neuroblastoma`; relapsed or refractory disease is a `progression:` phase, not an entry |
| Germline predisposition | ALK- and PHOX2B-related susceptibility, and twelve syndromes with a raised neuroblastoma risk | Separate entries, collected in `Neuroblastoma_Predisposition_Syndromes` |
| Mechanism | Proliferative signalling, evasion of growth suppressors, replicative immortality, invasion and metastasis | `conforms_to` from `Neuroblastoma` nodes to the four hallmark modules of those names; no mechanism is an entry |

`Neuroblastoma`'s MONDO and NCIT classes also contain tumours the entry does not
cover. Olfactory neuroblastoma and CNS neuroblastoma with FOXR2 activation
have their own entries; retinal neuroblastoma has none. The entry's `notes`
carry the full scope statement.

## Family map

| Group | Entries | How the KB links them |
|---|---|---|
| Peripheral neuroblastic tumours | `Neuroblastoma`, `Ganglioneuroblastoma`, `Ganglioneuroma` | `Peripheral_Neuroblastic_Tumors` |
| Germline predisposition | `ALK-Related_Neuroblastic_Tumor_Susceptibility` (`MONDO:0013083`), `PHOX2B-Related_Neuroblastic_Tumor_Susceptibility` (`MONDO:0700041`), `BARD1-related_Cancer_Predisposition`, `Beckwith-Wiedemann_Syndrome`, `Congenital_Central_Hypoventilation_Syndrome`, `Costello_Syndrome`, `Fanconi_Anemia`, `Intellectual_Disability_X-linked_102`, `Li-Fraumeni_Syndrome`, `Neurofibromatosis_Type_1`, `Noonan_Syndrome`, `Simpson-Golabi-Behmel_Syndrome_Type_1`, `Sotos_Syndrome`, `Weaver_Syndrome` | `Neuroblastoma_Predisposition_Syndromes` |
| Paraneoplastic | `Opsoclonus_Myoclonus_Syndrome`, `Paraneoplastic_Neurological_Syndromes` | `Paraneoplastic_Neurological_Syndromes` carries a pointer subtype with `curated_in: Opsoclonus_Myoclonus_Syndrome`; `Neuroblastoma` has an opsoclonus-myoclonus phenotype |
| Same name, different tumour | `Olfactory_Neuroblastoma`, `CNS_Neuroblastoma_FOXR2-Activated` | Each carries a `Neuroblastoma` differential-diagnosis row, and `Neuroblastoma`'s scope note excludes both |
| Shared lineage | `Pheochromocytoma_Paraganglioma` | Composite pheochromocytoma and paraganglioma subtypes, whose second component is usually a ganglioneuroma, and a differential-diagnosis row in each direction with `Neuroblastoma` |

## Open questions

These are the questions recorded as `discussions` in the family that concern
neuroblastic tumours; none is marked resolved. Each is a record in its entry
and can be found by its id.

| Entry | Discussion | Kind | Question |
|---|---|---|---|
| `Neuroblastoma` | `mismatch_nb_aurora_a_mycn_amplified_benefit` | Human-model mismatch | Why do MYCN-amplified tumours respond worse to Aurora A inhibition than non-amplified ones, when the preclinical mechanism makes them the most Aurora A-dependent? |
| `Neuroblastoma` | `controversy_nb_mesenchymal_state_prognosis` | Controversy | Does a high mesenchymal cell-state signature predict worse outcome, better outcome, or neither? |
| `Neuroblastoma` | `controversy_nb_intermediate_adrenergic_mesenchymal_state` | Controversy | Which intermediate noradrenergic-mesenchymal population do patient tumours contain, and is it on a trajectory between the two states? |
| `Neuroblastoma` | `nb_myc_high_subset_proliferation_model_mismatch` | Human-model mismatch | Is there a proliferative difference between MYC-driven and MYCN-driven human tumours at all, as the zebrafish model implies? |
| `Neuroblastoma` | `gap_nb_consolidation_tandem_versus_busulfan_melphalan` | Knowledge gap | Which consolidation gives better event-free survival in high-risk disease: a carboplatin, etoposide and melphalan tandem transplant, or a single busulfan-melphalan transplant? |
| `Neuroblastoma` | `question_nb_alt_status_and_wee1_inhibitor_benefit` | Open question | Does alternative lengthening of telomeres mark the tumours that benefit from WEE1 inhibition? |
| `Ganglioneuroblastoma` | `gnb_schwannian_stroma_origin` | Controversy | Is the Schwannian stroma recruited from the host, or derived from the tumour? |
| `Ganglioneuroblastoma` | `gnb_nodule_clonality` | Controversy | Is the nodule of nodular ganglioneuroblastoma a genetically distinct clone? |
| `Ganglioneuroblastoma` | `gnb_tmm_prognostic_significance` | Knowledge gap | Does telomere maintenance status predict outcome, as it does in high-risk neuroblastoma? |
| `Ganglioneuroma` | `gn_origin` | Controversy | Does every ganglioneuroma arise by maturation of a neuroblastoma or ganglioneuroblastoma? |
| `ALK-Related_Neuroblastic_Tumor_Susceptibility` | `alk_nbts_surveillance_upper_age_bound` | Knowledge gap | Does a germline carrier's risk of a new tumour end in late childhood, as the surveillance protocol assumes, or continue into adult life? |
| `ALK-Related_Neuroblastic_Tumor_Susceptibility` | `alk_nbts_models_engineer_away_penetrance` | Human-model mismatch | Animal models reach far higher penetrance than the human carrier state: do they say anything about risk, as opposed to tumour formation after a second hit? |
| `BARD1-related_Cancer_Predisposition` | `bard1_neuroblastoma_common_vs_rare` | Knowledge gap | How large is a heterozygous carrier's neuroblastoma risk, and should carriers be surveilled? |
| `Weaver_Syndrome` | `weaver_neuroblastoma_mechanistic_bridge` | Knowledge gap | By what mechanism does a germline EZH2 variant raise neuroblastoma frequency? |
| `Opsoclonus_Myoclonus_Syndrome` | `oms_antigen_unknown` | Knowledge gap | What is the antigen of the intrathecal humoral response, and is the driving process humoral at all? |
| `Paraneoplastic_Neurological_Syndromes` | `pns_omas_humoral_versus_t_cell_effector` | Knowledge gap | In neuroblastoma-associated opsoclonus-myoclonus-ataxia, is the injuring arm humoral or T-cell mediated? |

## Stub decisions

- **Neuroblastoma, susceptibility to, 2 and 3** are curated, as
  `PHOX2B-Related_Neuroblastic_Tumor_Susceptibility` (`MONDO:0700041`) and
  `ALK-Related_Neuroblastic_Tumor_Susceptibility` (`MONDO:0013083`).
- **Neuroblastoma, susceptibility to, 1** (`MONDO:0009741`, KIF1B):
  `stubs/Neuroblastoma_Susceptibility_To_1.yaml` is BLOCKED at LOW priority,
  with its entry type left UNDECIDED. The germline KIF1B link rests on one
  family, and the follow-up study of that family (PMID:33112832) moved its
  pheochromocytoma predisposition onto a germline MAX variant. No
  gene-disease validity body has classified the pair. The stub's `notes`
  carry the full reasoning.
- **Myeloid sarcoma** (`MONDO:0006861`): `stubs/Myeloid_Sarcoma.yaml` is
  DEFERRED at LOW priority. It was nominated as a tumour that can be mistaken
  for neuroblastoma, but the fifth-edition WHO haematolymphoid classification
  (PMID:35732831) treats it as a tissue-based manifestation of acute myeloid
  leukaemia rather than an entity. The KB has no general acute myeloid
  leukaemia entry to hold it as a subtype.

## What the audits say

Measured on 2026-11-05 at `199eb7af890`. Re-run the commands below rather than
trusting these figures once the entries change.

- **Phenotypes wired to a mechanism.** 386 of the 503 phenotype nodes across
  the 22 entries have a causal in-edge, counted the way
  `just compliance-connectivity` counts them. `Neuroblastoma` has 14 of 16. Seven
  entries are fully connected. The lowest are
  `Congenital_Central_Hypoventilation_Syndrome` (1 of 5),
  `Paraneoplastic_Neurological_Syndromes` (2 of 10),
  `Intellectual_Disability_X-linked_102` (7 of 27),
  `Simpson-Golabi-Behmel_Syndrome_Type_1` (6 of 19) and `Sotos_Syndrome` (21
  of 53).
- **Cell of origin.** None of the five neoplasm entries assessed
  (`Neuroblastoma`, `Ganglioneuroblastoma`, `Ganglioneuroma`,
  `Olfactory_Neuroblastoma`, `CNS_Neuroblastoma_FOXR2-Activated`) marks an
  origin node yet, so `just check-cancer-origin` derives no cell of origin for
  any of them. `CNS_Neuroblastoma_FOXR2-Activated` binds no cell type at all.
- **Module conformance.** Thirteen entries carry at least one `conforms_to`.
  The nine that carry none are `Ganglioneuroma`,
  `ALK-Related_Neuroblastic_Tumor_Susceptibility`,
  `PHOX2B-Related_Neuroblastic_Tumor_Susceptibility`,
  `Beckwith-Wiedemann_Syndrome`, `Costello_Syndrome`,
  `Simpson-Golabi-Behmel_Syndrome_Type_1`, `Opsoclonus_Myoclonus_Syndrome`,
  `Paraneoplastic_Neurological_Syndromes` and
  `CNS_Neuroblastoma_FOXR2-Activated`.
- **GeneReviews baseline.** `Neurofibromatosis_Type_1` and `Noonan_Syndrome`
  cite GeneReviews chapters without tagging them (`CITED_UNTAGGED`, which
  `--strict` fails on). `Neuroblastoma`'s only match is the ALK-related
  chapter, which belongs to, and is tagged in,
  `ALK-Related_Neuroblastic_Tumor_Susceptibility`. Eight entries have no
  GeneReviews chapter, including `PHOX2B-Related_Neuroblastic_Tumor_Susceptibility`.

```bash
just list-disconnected-phenotypes kb/disorders/<Entry>.yaml
just check-cancer-origin --format list kb/disorders/<Entry>.yaml
just check-conformance-content kb/disorders/<Entry>.yaml
just check-genereviews --format tsv kb/disorders/<Entry>.yaml
```

## Related projects

- [`CHILDHOOD_CANCER.md`](CHILDHOOD_CANCER.md): the pediatric and AYA cancer
  landscape this family sits in.
- [`CANCER.md`](CANCER.md): the cancer curation tiers, where neuroblastoma is a
  Tier 4 and Tier 13 row.
