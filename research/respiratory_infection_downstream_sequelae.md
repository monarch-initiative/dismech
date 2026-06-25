# Respiratory Infection → Downstream Disease Sequelae

**Source prompt:** Intercept ("Ending Respiratory Infections"),
https://blog.interceptfund.com/p/ending-respiratory-infections (accessed 2026-06-25).

The Intercept essay argues that common acute respiratory infections impose a large
hidden burden not only through the acute illness but through **downstream chronic and
acute disease sequelae**. It cites several striking epidemiological associations
between an index respiratory infection and a later (or acute-triggered) disease:

| Index infection | Downstream disease | Reported effect size (blog) | Primary source used here |
|-----------------|--------------------|-----------------------------|--------------------------|
| Early-life rhinovirus wheezing | Childhood asthma (by age 6) | ~9.8× | Jackson et al. 2008, AJRCCM (PMID:18565953) |
| Influenza | Acute myocardial infarction (first 7 days) | ~6.1× | Kwong et al. 2018, NEJM (PMID:29365305) |
| Severe influenza | Dementia | ~4.5–5× | *not yet curated — needs verified primary source* |
| Severe influenza / pneumonia | Alzheimer's disease | ~2.6–4.1× | *not yet curated — needs verified primary source* |
| RSV | Heart failure | ~1.3× | *not yet curated (no RSV entry); Kwong also reports RSV→MI IR 3.51* |

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

## Deferred / not curated

- **Influenza → dementia / Alzheimer's**: the blog's 4.5–5× (dementia) and 2.6–4.1×
  (Alzheimer's) figures were not added because verified primary sources with quotable
  abstracts were not located within scope. Candidate follow-up before curating.
- **RSV → heart failure** and **rhinovirus** as standalone links: dismech currently has
  no RSV or rhinovirus disorder entry, so these would require new disorder entries or a
  directional comorbidity/trajectory file rather than enhancement of an existing entry.
  Note Kwong et al. 2018 independently report an RSV→acute-MI incidence ratio of 3.51
  (95% CI 1.11–11.12), corroborating the broader respiratory-infection → acute
  cardiovascular event pattern.

These deferred links are good candidates for `kb/comorbidities/` A_BEFORE_B trajectory
entries once verified primary sources are in hand.
