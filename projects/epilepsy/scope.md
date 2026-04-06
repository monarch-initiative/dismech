# Initial Candidate Disorder Scope

This is a first-pass coverage list for epilepsy work in dismech. It is not an
attempt to enumerate every epilepsy-related MONDO term. The goal is to choose a
sequence of entries that maximizes mechanistic clarity and reuse.

## Scope Rules

| Rule | Practical meaning |
| --- | --- |
| Keep the umbrella | [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml) remains the index page. |
| Split on mechanism | If the causal chain, cell types, or lesion substrate differ materially, create separate entries. |
| Split on treatment logic | If a mechanism points to mTOR inhibition, ketogenic diet, immunotherapy, or syndrome-specific channel decisions, it probably deserves its own page. |
| Do not over-fragment too early | A family-level scaffold is often needed before dozens of very rare DEE pages become useful. |

## Current KB Anchors

| Entry | Status |
| --- | --- |
| [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml) | Umbrella/index entry; needs mechanism cleanup. |
| [`kb/disorders/Dravet_syndrome.yaml`](../../kb/disorders/Dravet_syndrome.yaml) | Existing high-value anchor for channelopathy/interneuron dysfunction. |
| [`kb/disorders/Jeavons_Syndrome.yaml`](../../kb/disorders/Jeavons_Syndrome.yaml) | Existing generalized/photosensitive anchor; needs evidence tightening. |
| [`kb/disorders/Tuberous_Sclerosis_Complex.yaml`](../../kb/disorders/Tuberous_Sclerosis_Complex.yaml) | Existing multisystem mTOR anchor. |
| [`kb/disorders/Menkes_Disease.yaml`](../../kb/disorders/Menkes_Disease.yaml) | Existing metabolic disorder with seizure mechanisms. |

## Wave 1: Highest-Value Next Entries

These should likely be curated before a large DEE expansion because they solve
current umbrella-page problems or establish reusable mechanism families.

| Candidate entry | Identifier / source | Mechanism lane | Why now |
| --- | --- | --- | --- |
| Temporal lobe epilepsy | MONDO:0005115 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Circuit / structural / inflammatory | TLE-specific content is already leaking into the umbrella page. |
| Mesial temporal lobe epilepsy with hippocampal sclerosis | MONDO:0020476 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Structural / hippocampal sclerosis | Likely deserves separation from generic TLE if curated around sclerosis, memory phenotype, and surgery relevance. |
| mTOR-related focal epilepsy | Mechanism family; exact disease term may need curation decision | mTOR / cortical malformation | Strong shared mechanism across TSC, DEPDC5, and focal cortical dysplasia. |
| Isolated focal cortical dysplasia type II | MONDO:0011818 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | mTOR / cortical malformation | High mechanistic coherence, strong histopathology signal, and direct relation to drug-resistant focal epilepsy. |
| DEPDC5-related familial focal epilepsy | MONDO:0024556 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | mTOR / focal epilepsy genetics | Clear bridge between gene-defined epilepsy and mTOR family logic. |
| BBB-disruption-associated drug-resistant focal epilepsy | Mechanism family entry | Neurovascular / inflammatory | Good candidate only if curated tightly around human focal/drug-resistant evidence rather than as a generic epilepsy claim. |

## Wave 2: Gene-Defined DEE Families Worth Adding Soon

These are strong candidates once the family-level scaffolding above is in
place.

| Candidate entry | Identifier / source | Mechanism lane | Notes |
| --- | --- | --- | --- |
| KCNQ2-related developmental and epileptic encephalopathy | MONDO:0013387 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Channelopathy | High clinical relevance and distinct neonatal presentation. |
| SCN2A-related developmental and epileptic encephalopathy | MONDO:0013388 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Channelopathy | Strong precision-treatment implications and broad phenotype spectrum. |
| KCNT1-related developmental and epileptic encephalopathy | MONDO:0013989 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Channelopathy | Distinct severe DEE lane with likely different treatment logic from SCN-family disorders. |
| STXBP1 encephalopathy | MONDO:0012812 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Synaptic dysfunction | Best first synaptic DEE after Dravet-style channelopathy anchors. |
| CDKL5 disorder | MONDO:0100039 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Transcriptional / developmental | Strong early-onset DEE and a useful developmental-mechanism exemplar. |
| Female-restricted epilepsy with intellectual disability (PCDH19-related spectrum) | MONDO:0010246 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Developmental / mosaic cellular interference | Important X-linked epilepsy mechanism family not captured by simple channelopathy logic. |
| SYNGAP1 encephalopathy | MONDO:0012960 from repo G2P triage (`intellectual disability, autosomal dominant 5`; exact synonym `SYNGAP1-related developmental and epileptic encephalopathy`) | Synaptic dysfunction | Strong candidate because of generalized DEE, reflex seizure features, and overlap with eyelid-myoclonia phenotypes. |
| CHD2-related photosensitive generalized epilepsy / DEE | MONDO:0014150 from repo G2P triage (`developmental and epileptic encephalopathy 94`; CHD2-linked) | Developmental / chromatin | Good bridge between DEE and photosensitive generalized epilepsy. |

## Wave 3: Metabolic and Multisystem Epilepsy Families

These are especially valuable because mechanism and therapy are tightly linked.

| Candidate entry | Identifier / source | Mechanism lane | Notes |
| --- | --- | --- | --- |
| GLUT1 deficiency syndrome | MONDO:0000188 from [`rare_without_any_icd.csv`](../RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv) | Metabolic / brain fuel transport | High-value ketogenic-diet-responsive epilepsy. |
| Menkes disease epilepsy refinement | Existing [`kb/disorders/Menkes_Disease.yaml`](../../kb/disorders/Menkes_Disease.yaml) | Copper / mitochondrial / metabolic | Likely better as refinement of existing disease page than as a separate epilepsy syndrome page. |
| LIAS/LIPT1-related neonatal epilepsies | MONDO term selection needed | Mitochondrial / cofactor metabolism | Good exemplars of neonatal epilepsy driven by concrete mitochondrial enzyme defects. |
| POLG-related epileptic disease spectrum | MONDO term selection needed | Mitochondrial DNA maintenance | Important but probably after a simpler metabolic anchor such as GLUT1. |

## Wave 4: Immune and Acquired Epilepsy Families

These should probably follow once the structural and gene-defined lanes are in
place.

| Candidate entry | Mechanism lane | Why deferred a bit |
| --- | --- | --- |
| Anti-NMDA receptor encephalitis with seizures | Immune / synaptic receptor autoimmunity | Better handled as a well-defined encephalitis entry rather than a vague "autoimmune epilepsy" page. |
| Rasmussen encephalitis | Immune / inflammatory focal epilepsy | Important, but needs a focused focal-inflammatory framework first. |
| FIRES / NORSE spectrum | Hyperinflammatory status epilepticus | High importance, but mechanistically complex and easy to overstate without careful source work. |

## Recommended First Curation Batch

If the next step is actual YAML creation/refactoring rather than more planning,
the most efficient first batch is:

1. Temporal lobe epilepsy
2. Mesial temporal lobe epilepsy with hippocampal sclerosis
3. mTOR-related focal epilepsy or focal cortical dysplasia type II
4. DEPDC5-related familial focal epilepsy
5. Cleanup/refactor of [`kb/disorders/Jeavons_Syndrome.yaml`](../../kb/disorders/Jeavons_Syndrome.yaml)

That batch would:

- remove subtype-specific leakage from the umbrella epilepsy page,
- establish two major mechanistic families outside Dravet,
- create a better home for existing TLE/mTOR/BBB content, and
- prepare the repo for a cleaner expansion into DEE and metabolic epilepsies.
