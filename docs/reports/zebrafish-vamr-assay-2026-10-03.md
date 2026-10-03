# The zebrafish VAMR behaviour assay and where it meets the pathograph

The Visual and Acoustic Motor Response (VAMR) assay measures how zebrafish larvae move in response to light changes and tones. Spath et al. (2026) ran it on 17 reference chemicals for developmental neurotoxicity (DNT) and compared the results with the cell-based DNT in vitro battery (DNT IVB). This report records the assay's design, the per-chemical results, and the dismech nodes each tested chemical could attach to.

No dismech entry records this assay. Adding it is tracked in issue #13450.

Read on **2026-10-03**; `kb/` as of commit `093f725c24`.

## Sources

| Source | Identifier | What it gives |
| --- | --- | --- |
| Article | doi:10.1016/j.neuro.2026.103414, PMID:41780647, *NeuroToxicology* 114:103414, CC BY | PubMed holds the abstract only; not in PMC |
| Open full text | `url:https://zenodo.org/records/23035979/files/1-s2.0-S0161813X26000355-main.pdf` | Cached as full text by `just fetch-reference`; this is the citable form for anything beyond the abstract |
| Supplementary workbook | `https://ars.els-cdn.com/content/image/1-s2.0-S0161813X26000355-mmc3.xlsx` | Tables S1–S7. S3 and S4 hold every concentration-response fit |
| Dataset DOI printed in the article | 10.5281/zenodo.17937513 | Not registered; does not resolve |

[`data/vamr-endpoint-hit-calls-2026-10-03.tsv`](data/vamr-endpoint-hit-calls-2026-10-03.tsv) is Tables S3 and S4 reduced to one row per chemical, exposure arm and endpoint (884 rows), with a column saying whether the row passes the article's hit rule.

## Assay design

| | |
| --- | --- |
| Organism | Zebrafish (*Danio rerio*), in-house UFZ-OBI/WIK strain |
| Format | One larva per well, 96-square-well polystyrene plate, 400 µL 10% Hanks' balanced salt solution, 28 °C, 14:10 h light:dark |
| Acute arm | Larvae plated at 4 days post-fertilization (dpf), exposed at 5 dpf for 40 minutes, then tested. 36 larvae per concentration, 72 controls. Six concentrations, quarter-log spacing, 4.4–80 µM, extended downward for potent chemicals |
| Developmental arm | Embryos plated and exposed once at 1 dpf, tested at 5 dpf. 32 larvae per concentration, 96 controls. Nine concentrations, semi-log spacing, with the top concentration set below the level causing malformation |
| Vehicle | 0.4% DMSO |
| Stimuli | Light at 13.5 klux against dark at 0 lux; 300 Hz tones at 65 dB (low) and 75 dB (high) |
| Instrument | ViewPoint Zebrabox, ZebraLab software in quantization mode, 25 frames per second |
| Readout | Pixel change per second |
| Run time | 1 h 17 min |
| Exclusions | Malformed larvae and larvae without an inflated swim bladder are removed before analysis |

### The 26 endpoints

| Group | Endpoints | What is measured |
| --- | --- | --- |
| Visual startle | VSRB, VSR1, VSR2 | Movement in the 1 s after a light change |
| Baseline locomotion | BSL1–4 | Four 5-minute blocks in the dark |
| Visual motor response | VMR1; VMR2–5 | 10 minutes in the light; four 5-minute blocks back in the dark |
| Acoustic startle | ASR1, ASR2, ASR3 | Mean response to five low tones, five high tones, and five high tones after habituation training |
| Habituation learning | ASH1 | Decline in response within the first bout of 30 high tones at 1 s intervals |
| Potentiation of habituation | ASH1/5 | Fifth bout relative to the first and fifth together |
| Habituation total | ASHsum | Summed activity over the five bouts |
| Memory retention | ASR2/3 | ASR2 relative to ASR2 and ASR3 together |
| Rest-period activity | ISI1–3, IEI1–3, IBI | Movement between stimuli, between endpoints, and between habituation bouts |

### Analysis and hit rule

- Time-series endpoints (BSL1–4, VMR1–5) are fitted with generalized additive mixed models. The Fréchet distance between each exposed group's fitted curve and the control curve is the response.
- Single-value endpoints are fitted with Gaussian linear models. The absolute difference from the control mean is the response.
- Both feed the US EPA `tcplfit2` pipeline, which returns AC50, a point of departure and a benchmark concentration.
- An endpoint is a hit when its hit call is at least 0.9 and its curve fit carries fewer than two flags.

Because both response measures are absolute, **the tables carry no direction**. Whether a chemical raised or lowered movement is stated only in the article's text and figures.

## Results

Twelve chemicals with human or rodent evidence of DNT and five predicted negatives were tested. Three of the twelve (phenytoin, maneb, nicotine) are negative in the DNT IVB.

| | Acute | Developmental |
| --- | --- | --- |
| DNT-positive chemicals detected | 11 of 12 | 8 of 12 |
| The three DNT IVB false negatives | all detected | none detected |
| Predicted negatives called negative, as stated in the text | 5 of 5 | 4 of 5 (ibuprofen is a hit) |
| Potency against the DNT IVB | no significant difference | 1–4 orders of magnitude lower AC50 |

The authors state that acute hits "likely reflect short-term, receptor-mediated effects" and that it is not clear whether they predict developmental outcomes.

### Hits per chemical

Counts are endpoints passing the hit rule, out of 26, taken from the supplementary tables. AC50 in µM.

| Chemical | Class in the study | Acute hits | Most sensitive (acute) | Developmental hits | Most sensitive (developmental) |
| --- | --- | ---: | --- | ---: | --- |
| Chlorpyrifos | positive | 17 | BSL2, 0.53 | 14 | VMR5, 0.0010 |
| Trichlorfon | positive | 1 | BSL4, 3.1 | 15 | VMR3, 0.0023 |
| Triethyltin bromide | positive | 22 | VMR1, 0.13 | 11 | ASHsum, 0.0024 |
| Haloperidol | positive | 22 | ASHsum, 0.52 | 8 | BSL3, 0.022 |
| Tebuconazole | positive | 17 | BSL4, 6.3 | 4 | ASHsum, 0.19 |
| Hexachlorophene | positive | 7 | ASHsum, 0.060 | 2 | BSL1, 0.00026 |
| PFOA | positive | 1 | VMR1, 11.9 | 1 | VMR5, 0.011 |
| Ketamine hydrochloride | positive | 10 | BSL4, 15 | 2 (see below) | BSL3, 40 |
| BDE-99 | positive | 0 | – | 3 | BSL4, 0.0065 |
| Phenytoin (5,5-diphenylhydantoin) | positive, DNT IVB negative | 7 | BSL4, 0.084 | 0 | – |
| Maneb | positive, DNT IVB negative | 4 | ASR3, 0.76 | 0 | – |
| Nicotine | positive, DNT IVB negative | 2 | VMR2, 5.6 | 0 | – |
| Ibuprofen | predicted negative | 0 | – | 3 | VMR2, 0.15 |
| Saccharin | predicted negative | 0 | – | 6 (see below) | BSL3, 0.0013 |
| D-Mannitol | predicted negative | 0 | – | 1 (see below) | BSL4, 0.00052 |
| Sodium benzoate | predicted negative | 0 | – | 1 (see below) | VMR5, 0.099 |
| Acetaminophen | predicted negative | 0 | – | 0 | – |

### Learning and memory endpoints that pass the hit rule

| Endpoint | Hits (AC50, µM) |
| --- | --- |
| ASH1, habituation | Haloperidol, developmental, 1.25 |
| ASH1/5, potentiation of habituation | Phenytoin, acute, 18.3; haloperidol, acute, 10.4; hexachlorophene, acute, 0.13; trichlorfon, developmental, 1.65; triethyltin, developmental, 0.14 |
| ASR2/3, memory retention | Phenytoin, acute, 16.2; haloperidol, acute, 45.8; hexachlorophene, acute, 0.30; tebuconazole, acute, 59; triethyltin, acute, 4.8; ibuprofen, developmental, 4.5 |

### Where the article's text and its supplement disagree

- **Developmental negatives.** The text classifies saccharin, D-mannitol, sodium benzoate and acetaminophen as negative after developmental exposure. Table S4 has rows with a hit call of at least 0.9 for saccharin (6), D-mannitol (1) and sodium benzoate (1), and Table S6 lists a developmental AC50 for each. The flag column of Table S4 is empty for every row with a hit call of at least 0.9, so the flag half of the hit rule cannot be applied to the developmental arm from the published table.
- **Ketamine, developmental.** The text says ketamine was a hit only in the acute arm. Table S4 has two developmental rows at hit calls 0.907 and 0.947, both with an AC50 at 40 µM and no flags recorded.
- **Ketamine and habituation.** The discussion says acute ketamine "blocked habituation learning". The acute ASH1 fit has a hit call of 0.994 and three flags, so it is not a hit under the article's rule. The acute ketamine hits are BSL1–4, VMR2–5, ASHsum and IBI, between 15 and 43 µM.
- **Nicotine and habituation.** The discussion says acute nicotine impaired habituation, and Table S6 gives ASH1 at 0.22 µM as nicotine's most sensitive acute endpoint. That fit carries three flags. The two acute fits that pass are VMR2 (5.6 µM) and VSR2 (5.7 µM).
- **Trichlorfon and habituation.** The discussion says acute trichlorfon impaired habituation at the highest concentration. The acute ASH1 hit call is 0.008.
- **Count of positives detected in both arms.** One results paragraph says all nine DNT IVB-positive chemicals were hits in both arms; later paragraphs say seven. The tables give seven: chlorpyrifos, haloperidol, hexachlorophene, PFOA, tebuconazole, trichlorfon and triethyltin bromide.

## Attachment to dismech

The assay is a whole-organism animal model, so it belongs under `animal_models`, observing at `ORGANISM` scale. It is not specific to any chemical or disease; each tie below runs through one tested chemical.

### Chemicals with a node to attach to

| Chemical | Entry or module | Node | What the article supports |
| --- | --- | --- | --- |
| Chlorpyrifos | `Organophosphate_Poisoning` | `Central cholinergic overstimulation` | Acute exposure raised movement in normally quiet periods (AC50 2.46–9.01 µM on the endpoints shown); developmental exposure lowered movement on most endpoints (AC50 0.08–0.17 µM on the same endpoints) |
| Trichlorfon | `Organophosphate_Poisoning` | `Central cholinergic overstimulation` | Mostly developmental: 15 hits from 0.0023 µM |
| Ketamine | `nmda_receptor_hypofunction` | `NMDA Receptor Antagonism or Receptor Loss` | Ketamine is the perturbation; the hits are locomotor. A readout on `Learning and Memory Impairment` is not supported by a passing fit |
| Nicotine | `Organophosphate_Poisoning`; `Green_Tobacco_Sickness` | `Nicotinic receptor overstimulation`; `Nicotinic Acetylcholine Receptor Overstimulation` | Two acute hits on responses to light; none developmental |

The article measures behaviour only. It does not measure acetylcholinesterase activity, receptor occupancy or any molecular quantity, and it does not attribute the organophosphate results to cholinesterase inhibition. `Lead_Poisoning` conforms to three nodes of the NMDA module, but lead was not tested.

### Diseases the article names without data

The introduction cites attention deficit hyperactivity disorder and autism spectrum disorder as outcomes of developmental neurotoxicity. `Attention_Deficit-Hyperactivity_Disorder` has no `environmental` entries. The article cites Dalsager et al. 2019 (doi:10.1016/j.envres.2019.108533) for maternal chlorpyrifos and pyrethroid metabolites and ADHD symptoms in young children.

### Matching readouts with no tested chemical behind them

- `Exaggerated Startle Response` is a phenotype in `Hereditary_Hyperekplexia` and about ten other entries. ASR1–3 measure startle magnitude, but none of the 17 chemicals bears on those diseases.
- The introduction describes the assay as able to detect seizure-like activity. This article reports no seizure-like result, so it gives no tie to `epilepsy_excitation_inhibition_imbalance`.

### What dismech lacks

- No pathophysiology or phenotype node is named for habituation.
- No entry or module mentions maneb, PFOA, hexachlorophene, triethyltin, tebuconazole or trichlorfon.
- Chlorpyrifos is named once, in the description of `Organophosphate_Poisoning`. That entry has no animal, experimental or computational model.
- No entry is named for fetal hydantoin syndrome.
