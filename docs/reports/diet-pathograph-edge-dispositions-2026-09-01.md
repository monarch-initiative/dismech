# Diet exposures and the pathograph: disposition of 42 candidates, 2026-09-01

The diet representation audit — `diet-representation-audit-2026-09-01.md`, added by
PR #10358 — found 42 `environmental[]` diet entries that carry a supporting,
snippet-backed citation but no `influences_mechanisms` link, so they never appear
in the mechanism graph. This records what was decided for each.

**20 got an edge (21 links). 8 are proposed but not added. 14 were left alone.**

## The rule applied

An `influences_mechanisms` edge asserts that the exposure acts on a *named
mechanism node*. So the test is not "is this a real risk factor" — it is:

> Does the cited snippet name something that maps to a node or phenotype in this
> file, or does it only say the exposure raises the risk of the disease?

A snippet that says only "X is associated with an increased risk of [the
disease]" identifies no node. Those were left alone. This is the distinction the
audit flagged and could not make itself: an association is not a mechanism.

Two schema slots were needed, and they are easy to conflate:

- **`causal_link_type`** is graph topology — does the edge jump over mechanism
  steps that are themselves nodes in this file? `DIRECT`, or
  `INDIRECT_KNOWN_INTERMEDIATES` when it does.
- **`directness`** on the evidence item is about the quote — does it assert the
  claim, or does the claim follow from it by an inference step?

They vary independently. Wilson Disease's dietary copper edge is topologically
`DIRECT` (intake feeds the hepatic copper pool with nothing in between) but its
evidence is `INDIRECT`, because the source says lowering intake prevents
re-accumulation and the forward claim is inferred from that removal design.

## Added (20 entries, 21 links)

| Entry | Exposure | Target node | Effect | Why |
|---|---|---|---|---|
| Celiac Disease | Gluten Exposure | Gluten-Triggered Immune Response | TRIGGERS | Snippet names gluten as required to *trigger* the enteropathy |
| Celiac Disease | Wheat / Barley / Rye | Gluten-Triggered Immune Response | TRIGGERS | One snippet names all three grains as triggering and maintaining it (3 links) |
| Gastroesophageal Reflux | Alcohol Consumption | Lower Esophageal Sphincter Dysfunction | EXACERBATES | Snippet states the sphincter-pressure reduction |
| Gastroesophageal Reflux | Dietary Factors | Lower Esophageal Sphincter Dysfunction | EXACERBATES | Physiologic evidence for chocolate and high-fat meals on the same node |
| Heart Failure | Alcohol Abuse | Myocardial Contractile Dysfunction | TRIGGERS | Snippet names chronic cardiac dysfunction and alcoholic dilated cardiomyopathy |
| Hyperlipidemia | High Saturated Fat Diet | Increased LDL Cholesterol | EXACERBATES | Snippet attributes the LDL-C rise to saturated fat substitution |
| Obesity | High-Calorie Diet | Energy Imbalance | TRIGGERS | Inpatient randomised crossover trial; excess intake attributable to processing itself |
| Obesity | Obesogenic Environment | Increased Body Mass Index | PREDISPOSES | Causal-inference systematic review linking outlet density to BMI |
| Osteoporosis | Vitamin D Deficiency | Bone Remodeling Imbalance | PREDISPOSES | Snippet gives the deficiency → hyperparathyroidism → bone loss route |
| Phenylketonuria | Dairy Intake | Hyperphenylalaninemia | EXACERBATES | Randomised crossover trial measuring phenylalanine tolerance from milk protein |
| Phenylketonuria | Mammalian Meat / Nut Intake | Hyperphenylalaninemia | EXACERBATES | Named among high-protein foods the diet avoids (2 links) |
| Wilson Disease | Dietary Copper | Hepatic Copper Accumulation | EXACERBATES | Snippet ties intake to copper re-accumulation |
| Irritable Bowel Syndrome | Dietary Triggers | Abdominal Pain, Bloating | EXACERBATES | Low-FODMAP meta-analysis reports both (2 links) |
| Migraine | Dietary Triggers | Headache | TRIGGERS | Provocation studies for caffeine withdrawal and MSG |
| Carotid Stenosis | Smoking and diet | Atherosclerotic carotid plaque formation | PREDISPOSES | Snippet names plaque development specifically |
| Marchiafava-Bignami | Chronic alcohol use and malnutrition | Alcohol-related thiamine depletion | PREDISPOSES | Review establishes this as the dominant clinical context |
| Lathyrism | Grass pea overconsumption | Beta-ODAP Receptor Agonism | TRIGGERS | Study attributes the disease to prolonged overconsumption |

Every edge carries its own evidence, copied byte-exact from the entry it sits on
so the snippet stays verified and `evidence_source` cannot drift.

Several edges are deliberately narrower than the entry they hang on. The GERD
dietary edge is scoped to the sphincter effect, because the same review found no
evidence that dietary avoidance improves outcomes. The IBS edge is scoped to
FODMAPs, because the gluten half of that annotation is uncited. The migraine edge
is scoped to caffeine withdrawal and MSG, because the entry's own `REFUTE` item
withdraws chocolate and aged cheese.

## Proposed, not added — these need a curator's ruling (8)

Each of these has good evidence for a *risk* claim and a plausible target node,
but the snippet does not reach the node. Adding them means accepting a
disease-level association as node-level support.

| Entry | Exposure | Proposed target | The problem |
|---|---|---|---|
| Gout | Red Meat and Organ Meat | Hyperuricemia | Cohort measures *incident gout*, not urate. Purine → urate is textbook, but this snippet does not say it |
| Gout | Shellfish Intake | Hyperuricemia | Same; the entry's own explanation already notes it measures incident gout rather than flares |
| Gout | Beer Intake | Hyperuricemia | UK Biobank per-drink association with incident gout |
| Gout | Fructose-Sweetened Soft Drink | Hyperuricemia | Meta-analysis of incident gout; note claims urate production |
| Liver Cirrhosis | Alcohol Consumption | Hepatocyte Injury and Death | Steep dose-response over 3M participants, but for cirrhosis risk, not hepatocyte injury |
| Coronary Artery Disease | High-Fat Diet | Coronary Endothelial Injury and Subendothelial LDL Retention | Cochrane RCT meta-analysis measures CVD events; the entry's own note says the LDL effect is small |
| Generalized Anxiety Disorder | Caffeine | (a phenotype) | Controlled trial shows GAD patients are abnormally caffeine-sensitive, but names no node or specific symptom |
| Tyrosinemia Type I | Catabolic and dietary stress | Toxic FAA/MAA accumulation | GeneReviews avoid-list; naming circumstances to avoid is not a mechanism measurement |

The four Gout entries are the cleanest illustration of the whole problem, and the
best fix is probably not a judgement call at all — it is a citation that measures
serum urate after a purine load, which would turn all four into ordinary
`EXACERBATES` edges on `Hyperuricemia`.

## Left alone (14)

All have solid evidence for a disease-level risk association and no node the
snippet reaches. This is the correct resting state, not a backlog.

Breast Carcinoma (alcohol), Colon Adenocarcinoma (alcohol), Essential
Hypertension (alcohol), Familial Hypercholesterolemia (alcohol), HPV-Negative
Head and Neck Cancer (ethanol), Laryngeal SCC (alcohol), Oral Cavity SCC
(ethanol), Postcricoid Region Cancer (tobacco and alcohol), Obstructive Sleep
Apnea (alcohol), Polycystic Kidney Disease (caffeine), Scurvy (vitamin C
deficiency), Thyroid Follicular Carcinoma (iodine deficiency), Type 2 Diabetes
Mellitus (high-calorie diet), Congestive Splenomegaly (alcohol).

Four are worth singling out:

- **Laryngeal SCC** and **Obstructive Sleep Apnea** already say so themselves.
  The laryngeal entry's `notes` record that it "makes a risk-association claim and
  describes no ethanol or acetaldehyde mechanism"; the OSA explanation says the
  meta-analysis "measures the association, not the airway-relaxation mechanism".
  Those entries were curated correctly and need nothing.
- **Congestive Splenomegaly** has a different problem: its description argues
  alcohol → cirrhosis → portal hypertension → splenomegaly, but the cited snippet
  is about anemia from direct bone-marrow toxicity. **The evidence does not
  support the claim the entry makes.** That is an evidence defect, not a missing
  edge, and it is not fixed here.
- **Scurvy** and **Polycystic Kidney Disease** rest on a case report and a
  GeneReviews avoid-list respectively, neither carrying an `evidence_source`.
  Vitamin C → collagen hydroxylation and caffeine → cAMP are both textbook, so
  both would become straightforward edges with a citation that states the
  mechanism.

## One thing fixed in passing

Wilson Disease graded `PMID:36010023` as `OTHER` on a treatment and left
`evidence_source` absent on the environmental entry, which counts as
`HUMAN_CLINICAL`. Copying the quote onto the new edge made
`check-snippet-grading` fail. The paper is a narrative review of dietary
recommendations with no primary data, so `OTHER` is right; the environmental item
was corrected to match rather than the new edge being graded to fit.
