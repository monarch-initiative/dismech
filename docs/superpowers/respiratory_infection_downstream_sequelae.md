# Respiratory Infection → Downstream Disease Sequelae

**Source prompt:** Intercept ("Ending Respiratory Infections"),
https://blog.interceptfund.com/p/ending-respiratory-infections (accessed 2026-06-25).

The Intercept essay argues that common acute respiratory infections impose a large
hidden burden not only through the acute illness but through **downstream chronic and
acute disease sequelae**. It cites several striking epidemiological associations
between an index respiratory infection and a later (or acute-triggered) disease:

| Index infection | Downstream disease | Reported effect size (blog) | Primary source used here | Verified effect size |
|-----------------|--------------------|-----------------------------|--------------------------|----------------------|
| Early-life rhinovirus wheezing | Childhood asthma (by age 6) | ~9.8× | Jackson et al. 2008, AJRCCM (PMID:18565953) | OR 9.8 ✓ |
| Influenza | Acute myocardial infarction (first 7 days) | ~6.1× | Kwong et al. 2018, NEJM (PMID:29365305) | IRR 6.05 (3.86–9.50) ✓ |
| RSV | Heart failure | ~1.3× | Verschoor et al. 2025, JAGS (PMID:40696870) | **adj. HR 1.48–3.74** (blog figure not corroborated; real effect larger) |
| Severe influenza (w/ pneumonia) | Alzheimer's / dementia | ~4.5–5× (dem); ~2.6–4.1× (AD) | Levine 2023, Neuron (PMID:36669485); Sipilä 2021, Lancet ID (PMID:34166620) | qualitative only; numeric HRs in source tables, **unverified from abstract** → CANDIDATE |

## What was curated into dismech

Per the chosen scope ("enhance existing disorders"), the two best-evidenced links that
map onto **existing** dismech entries were added as pathophysiology nodes with verified
primary-literature evidence (exact-quote snippets validated against the cached
abstracts):

1. **`kb/disorders/Influenza.yaml`** — new node *"Triggering of Acute Myocardial
   Infarction"*, placed downstream of the existing *"Endothelial Dysfunction and
   Thromboinflammation"* node via an `INDIRECT_KNOWN_INTERMEDIATES` causal edge
   (inflammation → coronary plaque instability → platelet activation / atherothrombotic
   occlusion). Evidence: Kwong et al. NEJM 2018 self-controlled case series, incidence
   ratio 6.05 (95% CI 3.86–9.50) for acute MI in the 7-day risk interval, no excess
   after day 7 (PMID:29365305).

2. **`kb/disorders/Asthma.yaml`** — new node *"Early-Life Rhinovirus Wheezing Illness
   and Asthma Inception"*, with a downstream edge into the existing *"Type 2 Immune
   Response / Th2 Signaling"* node. Evidence: Jackson et al. AJRCCM 2008 COAST birth
   cohort, rhinovirus wheezing in the first 3 years associated with ~9.8× odds of asthma
   at age 6 (PMID:18565953).

## Endpoint disorders + directional trajectory entries (second pass)

To represent the directional disease-to-disease edges in the trajectory/comorbidity
layer (`kb/comorbidities/`, the home of dismech "trajectories"), three missing endpoint
`Disease` entries were created, then four `com_*.yaml` `A_BEFORE_B` trajectory entries:

**New endpoint disorders** (`kb/disorders/`), each validated (schema/term/reference):
- `Myocardial_Infarction.yaml` — generic type 1 (atherothrombotic) acute MI
  (MONDO:0005068). Evidence: Bentzon 2014 Circ Res (PMID:24902970, plaque rupture →
  coronary thrombosis), Reed 2017 Lancet (PMID:27502078).
- `Rhinovirus_Infection.yaml` — human rhinovirus infection (MONDO:0005709 common cold as
  closest term; rhinovirus-specific `preferred_term`). Evidence: Jacobs 2013 CMR
  (PMID:23297263).
- `Respiratory_Syncytial_Virus_Infection.yaml` — RSV infection (MONDO:0001577). Evidence:
  Griffiths 2017 CMR (PMID:27903593), Falsey 2005 NEJM (PMID:15858184), Verschoor 2025
  JAGS (PMID:40696870).

**New trajectory entries** (`kb/comorbidities/`, all `A_BEFORE_B`):
- `com_Influenza__Myocardial_Infarction.yaml` — IRR 6.05 (CI 3.86–9.50), Kwong 2018
  (PMID:29365305). `CURATED`.
- `com_Rhinovirus_Infection__Asthma.yaml` — OR 9.8, Jackson 2008 (PMID:18565953).
  `CURATED`.
- `com_Respiratory_Syncytial_Virus_Infection__Heart_Failure.yaml` — adjusted HR range
  1.48–3.74, Verschoor 2025 (PMID:40696870). `CURATED`. **Note:** the blog's "~1.3×" HF
  figure could not be corroborated; the verified primary source reports a *larger*
  effect, so the entry is curated to the verified HR range, not the blog number.
- `com_Influenza__Alzheimer_Disease.yaml` — `CANDIDATE`. The blog's 4.5–5× (dementia) /
  2.6–4.1× (Alzheimer's) magnitudes most plausibly trace to per-disease HRs in Levine
  2023 Neuron (PMID:36669485) but live in that paper's tables, **not verifiable from the
  abstract**, so they are NOT asserted as quantitative signals. Only the verifiable
  qualitative statement ("Influenza with pneumonia was significantly associated with five
  of the six neurodegenerative diseases studied") is curated, plus Sipilä 2021 Lancet ID
  (PMID:34166620) as adjacent (any-infection→dementia) context. Flagged for follow-up to
  extract the influenza-specific AD hazard ratio from full text.

The within-disease pathophysiology nodes (first pass) and these trajectory entries are
complementary: the nodes model *mechanism inside the index disease*; the `com_*` entries
model the *directional epidemiological edge* with quantitative `association_signals`.
