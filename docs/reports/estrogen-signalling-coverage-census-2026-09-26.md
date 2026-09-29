# Estrogen signalling coverage census

Where estrogen signalling is curated in `kb/disorders/`, counted in six tiers from loosest to strictest. Regenerate with `just estrogen-census`; the counts move with every curation PR, so treat the numbers here as a dated snapshot and the script as the deliverable. Background: issue #12925.

Entries scanned: **3186**.

| Tier | Test | Entries | Share |
| --- | --- | ---: | ---: |
| `MENTIONS_ESTROGEN` | names estrogen/estradiol/estrone/estriol or ER-alpha/ER-beta anywhere | 115 | 3.6% |
| `NODE_INVOKES` | the same, restricted to `pathophysiology:` | 57 | 1.8% |
| `GO_BOUND` | binds `GO:0030520` estrogen receptor signaling pathway | 12 | 0.4% |
| `RECEPTOR_NAMED` | names `ESR1`/`ESR2` or the phrase “estrogen receptor” | 30 | 0.9% |
| `GENE_BOUND` | binds `hgnc:3467` (ESR1) or `hgnc:3468` (ESR2) anywhere | 6 | 0.2% |
| `GENE_ON_NODE` | binds either gene in a `genes:` descriptor on a pathophysiology node | 1 | 0.0% |

The tiers are not strictly nested. An entry can bind the pathway without naming the receptor, and can name the receptor without binding the pathway, so each row is counted independently.

### Drift since commit `94591e52d4`

The baseline column is the figure reported in issue #12925 when the gap was described. Any difference is ordinary curation drift, except as noted below the table.

| Tier | Baseline | Now | Change |
| --- | ---: | ---: | ---: |
| `MENTIONS_ESTROGEN` | 115 | 115 | +0 |
| `NODE_INVOKES` | 57 | 57 | +0 |
| `GO_BOUND` | 12 | 12 | +0 |
| `RECEPTOR_NAMED` | 29 | 30 | +1 |
| `GENE_BOUND` | 6 | 6 | +0 |
| `GENE_ON_NODE` | 1 | 1 | +0 |

One of those differences is not drift. `RECEPTOR_NAMED` was measured with a line-based search, which misses `CHEK2-related_Cancer_Predisposition`: it writes “oestrogen receptor” in a folded scalar, so the phrase is split across two source lines and only exists once the document is parsed. Re-measuring the baseline tree with this script gives 30, not 29.

## The gap this was written to measure

11 entries bind `GO:0030520` on a node while putting no receptor gene on any node. The pathway is annotated and the receptor driving it is not.

| Entry | Node(s) binding the pathway |
| --- | --- |
| `Aromatase_Deficiency` | Estrogen Deficiency and Androgen Excess |
| `Breast_Carcinoma` | ER and HER2 Receptor Heterogeneity |
| `Breast_Fibroadenoma` | Dysregulated Stromal Estrogen Signaling and ECM Organization |
| `ER_Positive_Breast_Cancer` | ESR1 Mutation-Driven Endocrine Resistance; Estrogen Receptor Activation |
| `Endometrial_Carcinoma` | Unopposed Estrogen Signaling |
| `Endometrial_Endometrioid_Adenocarcinoma` | Unopposed Estrogen Signaling |
| `Heart_Failure` | Loss of Myocardial Oestrogen Receptor Signalling |
| `Lymphangioleiomyomatosis` | Estrogen-Driven LAM Cell Survival and Dissemination |
| `PIK3CA_Mutant_Breast_Cancer` | Endocrine Resistance |
| `Testicular_Sex_Cord_Stromal_Neoplasm` | Estrogen-Mediated Clinical Manifestations |
| `Triple_Negative_Breast_Cancer` | Loss of Hormone Receptor Signaling |

Each row is a research task, not a mechanical backfill. A `genes:` descriptor asserts that this receptor drives this mechanism in this disease, and some of these nodes are loss-of-signalling or ligand-supply claims where an ESR1 binding would be wrong. Deciding not to bind, with the reason recorded in `notes`, is a closed task.

## Receptor bound, but off the pathograph

5 entries bind ESR1 or ESR2 somewhere without the gene reaching a pathophysiology node. These are typically susceptibility polymorphisms in `genetic:`, where a genotype-association paper may legitimately stop short of supporting a causal edge.

| Entry | Gene(s) bound |
| --- | --- |
| `Breast_Carcinoma` | ESR1 |
| `ER_Positive_Breast_Cancer` | ESR1 |
| `Osteoporosis` | ESR1 |
| `Premenstrual_Dysphoric_Disorder` | ESR1 |
| `Skeletal_Fluorosis` | ESR1 |

## Receptor on the pathograph

- `46_XX_Gonadal_Dysgenesis` — ESR2

## Modules

Modules that mention estrogen or the receptor, and whether they bind it. “In module prose” separates a module that models the receptor from one that merely cites a paper about it: a mention confined to `reference_title` or `snippet` is quoted source metadata, not a claim the module makes. No module binds either gene. A module node binding is a design decision rather than a backfill, because a generic receptor binding may belong only in the conforming entries.

| Module | In module prose | Binds `GO:0030520` | Binds ESR1/ESR2 |
| --- | --- | --- | --- |
| `cdk46_inhibitor_resistance` | yes | no | no |
| `cholestatic_liver_injury` | yes | no | no |
| `deep_placentation_defect` | quoted sources only | no | no |
| `deregulated_nutrient_sensing` | yes | no | no |
| `osteoporosis_bone_resorption` | yes | no | no |
| `sex_steroid_driven_proliferation` | yes | yes | no |

