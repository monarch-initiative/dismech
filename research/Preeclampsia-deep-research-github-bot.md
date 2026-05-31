## Research Summary: Preeclampsia (MONDO:0005081)

> This is assigned to @nlharris — skipping autonomous curation. This summary is intended as a research aid for the curator.

---

### Disease Overview

Preeclampsia is a multisystem pregnancy disorder affecting **2–8% of pregnancies worldwide**, accounting for >50,000 maternal and >500,000 fetal deaths annually. It is defined by new-onset hypertension (≥140/90 mmHg) developing after 20 weeks of gestation, typically accompanied by proteinuria or evidence of end-organ damage. It is the dominant clinical manifestation in a spectrum that includes gestational hypertension, HELLP syndrome (Hemolysis, Elevated Liver enzymes, Low Platelets), and eclampsia (seizures).

The condition is now understood as a vascular disorder unmasked by pregnancy rather than a hypertensive disorder per se — the placenta is the central driver, and delivery is the only definitive cure.

**Key ACOG diagnostic update (2019+):** Proteinuria is no longer required if severe hypertension coexists with end-organ damage (thrombocytopenia, renal insufficiency, impaired liver function, pulmonary edema, or new-onset headache/visual symptoms).

---

### Pathophysiology: The Two-Stage Model

The dominant framework is a **two-stage model** (Roberts/Hubel, extensively reviewed):

```
STAGE 1 (Silent, pre-clinical)         STAGE 2 (Clinical maternal syndrome)
─────────────────────────────           ─────────────────────────────────────
Defective trophoblast invasion   →  →   Anti-angiogenic factors released
+ Failed spiral artery remodeling       into maternal circulation
                                   →  →   Endothelial dysfunction (systemic)
                                         → Hypertension
                                         → Proteinuria (glomerular endotheliosis)
                                         → HELLP, eclampsia
```

This explains the early-onset/late-onset split: early-onset (< 34 wks) is dominated by placental failure (Stage 1); late-onset (≥ 34 wks) by maternal constitutional predisposition and endothelial vulnerability.

---

### Pathophysiology Nodes (Suggested Structure)

#### Node 1: Defective Trophoblast Invasion and Spiral Artery Remodeling
- Normally, extravillous trophoblasts (EVTs) invade the spiral arteries and replace vascular smooth muscle, transforming them from high-resistance to high-capacitance vessels
- In preeclampsia, this invasion is shallow; spiral arteries remain narrow, tortuous, and high-resistance
- Results in placental ischemia and hypoxia

**Key mechanisms:**
- Impaired uterine NK (uNK) cell tolerance and signaling (KIR/HLA-C interactions at the decidua-trophoblast interface)
- HLA-G expressed on EVTs normally dampens NK cytotoxicity; this axis is disrupted in PE
- Dysregulated TGF-β, VEGF, and HIF-1α signaling in the decidua

**Key cell types:**
- Extravillous trophoblast (EVT): `CL:0000351` (trophoblast) / extravillous subtype
- Uterine natural killer cell: `CL:0000623` (natural killer cell) — decidual NK cells are `CL:0002362`
- Decidual stromal cell

**Key biological processes:**
- Trophoblast cell migration / invasion: `GO:0001753` (trophoblast giant cell differentiation — verify specificity)
- `GO:0001570` (vasculogenesis)
- `GO:0035441` (cell migration involved in vasculogenesis)
- Response to hypoxia: `GO:0001666`

---

#### Node 2: Placental Oxidative Stress and sFlt-1 Overproduction
- Ischemic/hypoxic placenta upregulates HIF-1α, triggering massive production of **sFlt-1** (soluble VEGF receptor-1, a splice variant of FLT1)
- sFlt-1 is a potent decoy receptor that sequesters circulating **VEGF** and **PlGF** (placental growth factor)
- Result: markedly reduced free VEGF/PlGF → anti-angiogenic state in the mother
- **Soluble endoglin (sEng)**, also released by the hypoxic placenta, inhibits TGF-β signaling and amplifies endothelial damage
- The **sFlt-1:PlGF ratio** is now used clinically (ratio >38 predicts adverse outcomes within 4 weeks; EMA/FDA approved)

**Key genes (need OAK verification of HGNC IDs):**
- `FLT1` (hgnc:3738 — verify) — encodes Flt-1; alternative splicing generates sFlt-1
- `PGF` (hgnc:8982 — verify) — encodes PlGF
- `ENG` (hgnc:3349 — verify) — encodes endoglin; shed as sEng
- `VEGFA` (hgnc:12680 — verify) — primary target sequestered by sFlt-1

**Key biological processes:**
- `GO:0001525` — angiogenesis
- `GO:0048010` — VEGF receptor signaling pathway
- `GO:0001666` — cellular response to hypoxia
- HIF-1 signaling / hypoxia-inducible factor pathway

---

#### Node 3: Maternal Endothelial Dysfunction and Multi-Organ Injury
- Circulating sFlt-1, sEng, syncytiotrophoblast microparticles, and inflammatory mediators damage the systemic maternal endothelium
- Endothelial activation → reduced NO production, endothelin-1 upregulation → vasoconstriction → hypertension
- **Kidney:** Glomerular endotheliosis (pathognomonic lesion — swelling of glomerular endothelial cells, effacement of fenestrae) → proteinuria
- **Liver:** Hepatic sinusoidal obstruction, periportal necrosis → elevated transaminases; capsular distension → epigastric/RUQ pain; HELLP
- **Brain:** Posterior reversible encephalopathy syndrome (PRES), cerebral edema, seizures (eclampsia) — cerebrovascular autoregulation failure
- **Coagulation:** Endothelial activation triggers DIC-spectrum, thrombocytopenia (HELLP)
- **Placenta:** Decidual vasculopathy, infarcts → fetal growth restriction, placental abruption

**Key cell types:**
- Vascular endothelial cell: `CL:0000071` (blood vessel endothelial cell)
- Glomerular endothelial cell: `CL:1000850` (glomerular endothelial cell — verify)
- Syncytiotrophoblast: `CL:0000525` (syncytiotrophoblast — verify CL ID)
- Platelet: `CL:0000233`

**Key biological processes:**
- `GO:0008217` — regulation of blood pressure
- `GO:0045087` — innate immune response
- `GO:0042493` — response to drug (for treatment nodes)
- Nitric oxide signaling / endothelial NOS pathway
- `GO:0006954` — inflammatory response
- Complement activation: `GO:0006956`

---

### Clinical Phenotypes (Suggested HPO Terms)

| Phenotype | HP term | Notes |
|-----------|---------|-------|
| Hypertension | `HP:0000822` | Core diagnostic criterion |
| Proteinuria | `HP:0000093` | Common but not required |
| Edema | `HP:0000969` (peripheral) | Classic but removed from criteria |
| Thrombocytopenia | `HP:0001873` | HELLP; <100K/µL is threshold |
| Elevated hepatic transaminases | `HP:0002910` | HELLP component |
| Seizures | `HP:0001250` | Defines eclampsia |
| Headache | `HP:0002315` | New-onset, unresponsive to medication |
| Intrauterine growth retardation | `HP:0001511` | Fetal consequence |
| Renal insufficiency | `HP:0000083` | Cr >1.1 mg/dL |
| Visual impairment | `HP:0000505` | Scotomata, blurred vision |
| Hemolysis | `HP:0001878` | HELLP — microangiopathic |
| Pulmonary edema | `HP:0100598` | Severe feature |
| Abnormal platelet morphology | — | see thrombocytopenia |
| Placental abruption | `HP:0011410` — verify | Obstetric complication |

---

### Subtypes

The entry should have at least two main subtypes:
- **`Early-onset`** (< 34 weeks): Placenta-driven, more severe, higher sFlt-1, more associated with FGR; higher risk
- **`Late-onset`** (≥ 34 weeks): More maternal constitutional; less placental pathology; more common but generally less severe
- **`HELLP syndrome`**: Can be considered a severe variant with microangiopathic hemolysis, elevated LFTs, low platelets; may occur without classic hypertension/proteinuria
- **`Superimposed preeclampsia`**: On a background of chronic hypertension

---

### Treatments

| Treatment | Term | Notes |
|-----------|------|-------|
| Low-dose aspirin (prevention) | NCIT:C15986 + CHEBI:29177 (aspirin) | USPSTF Grade B; 81 mg/day from 12–28 wks |
| Magnesium sulfate (seizure prophylaxis) | NCIT:C15986 + CHEBI:32006 (verify) | Reduces eclampsia 58%; IV loading dose |
| Labetalol (BP control) | NCIT:C15986 + CHEBI:6522 (labetalol — verify) | First-line IV acute |
| Nifedipine (BP control) | NCIT:C15986 + CHEBI:7565 (nifedipine — verify) | Oral; first-line |
| Hydralazine | NCIT:C15986 + CHEBI:5757 (hydralazine — verify) | IV acute management |
| Delivery | MAXO:0000004 (surgical procedure) or MAXO:0001187 | Definitive treatment |
| Calcium supplementation (prevention) | MAXO:0000088 (dietary intervention) | Effective in low-calcium populations |
| Corticosteroids (fetal lung maturation) | MAXO:0000647 + CHEBI:16723 (betamethasone — verify) | If < 34 wks gestation |

---

### Key Evidence References (Verified PMIDs)

The following PMIDs were confirmed by direct abstract retrieval:

1. **PMID:30792480** — Phipps et al. 2019, *Nat Rev Nephrology* — "Pre-eclampsia: pathogenesis, novel diagnostics and therapies." Comprehensive mechanistic review covering sFlt-1/sEng/PlGF, endothelial dysfunction, renal glomerular endotheliosis, and emerging therapies. **Highly recommended as primary reference.**

2. **PMID:35177220** — Erez et al. 2022, *Am J Obstet Gynecol* — "Preeclampsia and eclampsia: the conceptual evolution of a syndrome." Covers the historical shift from neurological → vascular conceptualization; early vs. late onset subtypes; role of antiangiogenic factors.

3. **PMID:34033373** — Karrar et al. 2024, *StatPearls* — Comprehensive overview of diagnostic criteria, pathophysiology (uteroplacental ischemia), and management.

4. **PMID:32443079** — ACOG Practice Bulletin #222, 2020, *Obstet Gynecol* — Clinical guideline; the rate of preeclampsia increased 25% between 1987–2004; management thresholds and protocols.

**Additional high-priority references to fetch and verify (titles confirmed, PMIDs need `just fetch-reference` verification):**

- **Maynard et al. (2003)** *J Clin Invest* — "Excess placental soluble fms-like tyrosine kinase 1 (sFlt1) may contribute to endothelial dysfunction, hypertension, and proteinuria in preeclampsia" — The landmark animal model paper establishing sFlt-1 causality.
- **Levine et al. (2004)** *N Engl J Med* — "Circulating angiogenic factors and the risk of preeclampsia" — Prospective clinical cohort showing sFlt-1 rises and PlGF falls weeks before clinical PE onset.
- **Redman & Sargent (2005)** *Science* — "Latest advances in understanding preeclampsia" — Overview of immune and vascular mechanisms.
- **Verlohren et al. (2010/2012)** *Hypertension* — Established the sFlt-1:PlGF ratio clinical cutoff of 38.
- **Staff et al. (2019)** — Clinical use of angiogenic biomarkers in preeclampsia.

---

### Orphanet / Structured Sources

- Orphanet ORPHA code for pre-eclampsia: likely **ORPHA:275555** — run `just fetch-reference ORPHA:275555` to verify and check for definition, prevalence, and gene-disease associations that can be cited as `ORPHA:275555` evidence items.

---

### Suggested Module Conformance

Preeclampsia does not appear to conform to the existing `fibrotic_response` or `immune_checkpoint_blockade` modules. The disease may warrant a future **`placental_vascular_dysfunction`** module given the conserved sFlt-1/PlGF anti-angiogenic mechanism also seen in fetal growth restriction, spontaneous preterm birth, and HELLP syndrome.

The complement-driven endothelial damage node could potentially align with modules used in other thrombotic microangiopathy entries (e.g., aHUS) if those are curated.

---

### Long-term Consequences (for `progression` or `outcomes` section)

- Women with prior preeclampsia have **2× lifetime risk of cardiovascular disease**, 2–4× risk of hypertension, and 2× risk of stroke
- Preterm delivery and FGR are the primary fetal consequences
- Recurrence rate in subsequent pregnancies: 15–25% (higher if early-onset index pregnancy)

---

*Summary generated by Claude Code summarization agent from PubMed abstracts and authoritative review sources. All PMIDs must be verified with `just fetch-reference` before use as snippets.*
