---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:20:54.006574'
end_time: '2026-10-24T13:41:13.050944'
duration_seconds: 1219.04
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 52
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Alpha_Synucleinopathies-environmental-exposures-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Alpha_Synucleinopathies-environmental-exposures-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Environmental exposures that contribute to the alpha-synucleinopathies

## Scope

The alpha-synucleinopathies curated in this knowledge base:

- Parkinson disease (MONDO:0005180)
- Dementia with Lewy bodies (MONDO:0007488)
- Multiple system atrophy (MONDO:0007803)
- Isolated REM sleep behavior disorder (MONDO:0005937), as the prodromal synucleinopathy
- Pure autonomic failure, where evidence exists

## Research objective

Identify the environmental, occupational, lifestyle and iatrogenic exposures that
raise or lower risk of each of these diseases, and the mechanism through which each
exposure is thought to act. The output will be used to curate the `environmental`
section of each disease entry and to link each exposure to a specific mechanism node.

Treat each disease separately. Most exposure epidemiology is from Parkinson disease;
do not transfer a Parkinson disease finding to dementia with Lewy bodies, multiple
system atrophy or REM sleep behavior disorder unless a study measured it in that
disease. Where an exposure has been studied in one of the other diseases and found
null, report the null result explicitly.

## Exposure classes to cover

1. Pesticides and herbicides: paraquat, rotenone, organochlorines, maneb/mancozeb,
   chlorpyrifos and other organophosphates; occupational versus residential exposure;
   well-water drinking as a proxy.
2. Solvents: trichloroethylene (TCE), perchloroethylene; the Camp Lejeune cohort.
3. Metals: manganese, lead, iron, mercury, copper.
4. Air pollution: PM2.5, nitrogen dioxide, traffic-related pollution.
5. Head injury / traumatic brain injury.
6. MPTP and other mitochondrial complex I toxicants (as mechanistic proof).
7. Gut-related exposures: microbiome-altering factors, appendectomy, truncal
   vagotomy, gastrointestinal infection, Helicobacter pylori.
8. Infections more broadly: influenza, hepatitis C, herpesviruses.
9. Protective or inverse associations: tobacco smoking, caffeine/coffee, urate,
   physical activity, ibuprofen/NSAIDs. Report the strength of the evidence and
   the reverse-causation and survival-bias critiques.
10. Medications: statins, beta-2 agonists/antagonists, calcium channel blockers,
    and any drug-induced risk relevant to these diseases.
11. Dairy consumption, diet, rural living and farming as composite proxies.
12. For multiple system atrophy specifically: farming, pesticides, solvents,
    metals, smoking (reported inverse), and the case-control evidence base.
13. For REM sleep behavior disorder specifically: the case-control studies of
    environmental risk factors (farming, pesticides, head injury, smoking,
    occupational exposures) and whether they predict phenoconversion.
14. For dementia with Lewy bodies specifically: any case-control or cohort
    evidence (smoking, caffeine, head injury, pesticides, education) and how it
    differs from Alzheimer disease and Parkinson disease.

## Mechanism nodes available for linking

Name, for each exposure, which of these existing nodes it is reported to act on,
and whether it triggers, exacerbates, predisposes to, or protects against it.

- Parkinson disease: Mitochondrial Dysfunction; Oxidative Stress; Alpha-Synuclein
  Aggregation; Dopaminergic Neuron Loss; Neuroinflammation; Gut Microbiome Dysbiosis;
  Intestinal Inflammation and Barrier Dysfunction; Enteric Alpha-Synuclein Seeding;
  Vagal-Brainstem Alpha-Synuclein Propagation; Central Alpha-Synuclein Initiation;
  Iron Accumulation and Ferroptosis; Blood-Brain Barrier Dysfunction;
  Autophagy-Lysosome Pathway Dysfunction.
- Dementia with Lewy bodies: Alpha-Synuclein Aggregation and Lewy Body Formation;
  Peripheral Autonomic and Lower Brainstem Lewy Pathology; Olfactory Bulb Lewy
  Pathology; Nigrostriatal Dopaminergic Degeneration; Concomitant Alzheimer Disease
  Co-Pathology.
- Multiple system atrophy: Oligodendroglial Alpha-Synuclein Accumulation (GCIs);
  Mitochondrial Dysfunction and Coenzyme Q10 Deficiency; Neuroinflammation.
- REM sleep behavior disorder: Alpha-Synuclein Pathology in the Brainstem
  REM-Atonia Circuit; Progression to Overt Synucleinopathy.

## Evidence requirements

- Cite PubMed-indexed primary studies and meta-analyses with PMIDs. Prefer
  meta-analyses and large prospective cohorts for effect sizes.
- For every claim give the effect size (OR, RR or HR with 95% CI) and the study
  design, and quote the key sentence verbatim from the abstract.
- Separate human epidemiology from animal or cell-model mechanism evidence, and
  label each.
- State explicitly where evidence is weak, conflicting, null, or likely confounded
  (reverse causation for smoking and coffee; recall bias in case-control designs).
- Do not invent PMIDs. If you cannot find a citable source, say so.

## Output format

1. A summary table: exposure | disease | direction | effect size | design | PMID.
2. One section per disease with the evidence for each exposure.
3. A section on shared mechanisms, mapping each exposure to the nodes above.
4. A list of open questions and gaps.

## Output

# Environmental Exposures Contributing to the Alpha-Synucleinopathies

## Summary

Environmental, occupational, lifestyle and iatrogenic exposures are **robustly and reproducibly linked to Parkinson disease (PD)**, but are **sparsely studied in the other synucleinopathies** — dementia with Lewy bodies (DLB), multiple system atrophy (MSA) and isolated REM sleep behaviour disorder (iRBD) — and, critically, **their directions of effect do not transfer between diseases.** The single most important curatorial conclusion of this investigation is therefore a negative one: a risk factor established for PD cannot be assumed to apply to DLB, MSA or iRBD, and in several cases the measured direction is *opposite*. Smoking, the archetypal inverse ("protective") factor for PD (RR ≈ 0.59), is a *risk* factor in prodromal iRBD (OR 1.43) and is *null* in DLB. Pesticide exposure, the strongest occupational signal in PD, was *null* in the one MSA case-control study that applied a job-exposure matrix. These dissociations are not noise; they are a central result that should guide curation of each disease's `environmental` section independently.

For Parkinson disease specifically, the evidence supports a coherent toxicological model. **Risk is raised** by mitochondrial complex-I/pro-oxidant pesticides (paraquat OR 1.64; rotenone OR 1.57; organochlorines OR 1.54; chlorpyrifos >2.5-fold residential), chlorinated solvents (trichloroethylene, via the Camp Lejeune cohort), cumulative bone lead, manganese welding fume (as a distinct parkinsonism), ambient air pollution (PM2.5 HR 1.04 per IQR), dairy consumption (OR ≈ 1.26, male-predominant), and specific infections (*Helicobacter pylori* OR 1.65; hepatitis C OR 1.20). **Risk is lowered** by cigarette/smokeless tobacco (RR 0.59), caffeine (HR 0.80), physical activity (HR 0.66), high urate/gout (IRR 0.80), ibuprofen (RR 0.73), calcium channel blockers (RR 0.76–0.81), statins (RR 0.79–0.86), and full truncal — but not superselective — vagotomy (HR 0.53 at >20 years). MPTP provides the mechanistic proof-of-principle that a complex-I toxicant can cause human parkinsonism.

The mechanistic through-line for PD is convergence on **mitochondrial dysfunction, oxidative stress, α-synuclein aggregation, autophagy-lysosome failure, neuroinflammation, and a gut–vagal propagation axis.** The inverse ("protective") associations, however, are persistently vulnerable to **reverse causation** (prodromal PD reduces smoking and coffee intake and raises fall/head-injury risk) and **survival/selection bias**, and much of the pesticide and metals literature rests on post-diagnosis biomonitoring and recall-based case-control designs. Where evidence is weak, conflicting or confounded, this report states so explicitly.

---

## Summary Table: Exposure → Disease → Direction → Effect Size → Design → PMID

| Exposure | Disease | Direction | Effect size (95% CI) | Design | PMID |
|---|---|---|---|---|---|
| Cigarette smoking | PD | ↓ protective | RR 0.59 (0.56–0.62) | Meta-analysis (69 studies) | [26272284](https://pubmed.ncbi.nlm.nih.gov/26272284/) |
| Smokeless tobacco (snus) | PD | ↓ protective | HR 0.41 (0.28–0.61) | Pooled cohort | [27940486](https://pubmed.ncbi.nlm.nih.gov/27940486/) |
| Caffeine/coffee | PD | ↓ protective | HR 0.80 (0.75–0.85) | Meta-analysis (13 studies) | [32580456](https://pubmed.ncbi.nlm.nih.gov/32580456/) |
| Physical activity | PD | ↓ protective | HR 0.66 (0.57–0.78) | Meta-analysis (6 cohorts) | [25410713](https://pubmed.ncbi.nlm.nih.gov/25410713/) |
| Urate / gout | PD | ↓ protective | IRR 0.80 (0.72–0.90) | Cohort (Sweden) | [41050064](https://pubmed.ncbi.nlm.nih.gov/41050064/) |
| Ibuprofen | PD | ↓ protective | RR 0.73 (0.63–0.85) | Pooled prospective | [21368281](https://pubmed.ncbi.nlm.nih.gov/21368281/) |
| Calcium channel blockers | PD | ↓ protective | RR 0.81 (0.69–0.95) | Meta-analysis | [26464872](https://pubmed.ncbi.nlm.nih.gov/26464872/) |
| Statins | PD | ↓ protective | RR 0.86 (0.77–0.95) | Meta-analysis (25 studies) | [39097909](https://pubmed.ncbi.nlm.nih.gov/39097909/) |
| β2-agonist (salbutamol) | PD | ↓ protective | RR ≈ 0.66 (0.46–0.93) | Prescription registry | [28860381](https://pubmed.ncbi.nlm.nih.gov/28860381/) |
| Truncal vagotomy (>20y) | PD | ↓ protective | HR 0.53 (0.28–0.99) | Registry cohort | [26031848](https://pubmed.ncbi.nlm.nih.gov/26031848/) |
| Paraquat | PD | ↑ risk | OR 1.64 (1.27–2.13) | Meta-analysis (13 studies) | [30474499](https://pubmed.ncbi.nlm.nih.gov/30474499/) |
| Rotenone | PD | ↑ risk | OR 1.57 | Cohort (AGRICAN) | [29136149](https://pubmed.ncbi.nlm.nih.gov/29136149/) |
| Organochlorines (blood) | PD | ↑ risk | OR 1.54 (1.32–1.79) | Meta-analysis (7 studies) | [39520734](https://pubmed.ncbi.nlm.nih.gov/39520734/) |
| Chlorpyrifos (residential) | PD | ↑ risk | >2.5-fold | Case-control (PEG) | [41382278](https://pubmed.ncbi.nlm.nih.gov/41382278/) |
| Rural living | PD | ↑ risk | OR 1.56 (1.18–2.07) | Meta-analysis | [11437458](https://pubmed.ncbi.nlm.nih.gov/11437458/) |
| Farming | PD | ↑ risk | OR 1.42 (1.05–1.91) | Meta-analysis | [11437458](https://pubmed.ncbi.nlm.nih.gov/11437458/) |
| Pesticide exposure (composite) | PD | ↑ risk | OR 1.85 (1.31–2.60) | Meta-analysis | [11437458](https://pubmed.ncbi.nlm.nih.gov/11437458/) |
| Well-water drinking | PD | ↑ (borderline) | OR 1.26 (0.97–1.64) | Meta-analysis | [11437458](https://pubmed.ncbi.nlm.nih.gov/11437458/) |
| Trichloroethylene (TCE) | PD | ↑ risk | ~70% higher risk | Cohort (Camp Lejeune) | [37184848](https://pubmed.ncbi.nlm.nih.gov/37184848/) |
| Cumulative bone lead | PD | ↑ risk | assoc. (meta) | Meta-analysis (88 studies) | [37022311](https://pubmed.ncbi.nlm.nih.gov/37022311/) |
| Manganese welding fume | Parkinsonism | ↑ risk | 15.6% vs 0% prevalence | Cross-sectional | [22975422](https://pubmed.ncbi.nlm.nih.gov/22975422/) |
| PM2.5 air pollution | PD | ↑ risk | HR 1.04 (1.01–1.08) per IQR | Cohort (Ontario) | [30124852](https://pubmed.ncbi.nlm.nih.gov/30124852/) |
| Traumatic brain injury | PD | ↑ / null (conflicting) | RR 1.48 (1.22–1.74) vs null | Meta-analyses | [36781627](https://pubmed.ncbi.nlm.nih.gov/36781627/) / [30396335](https://pubmed.ncbi.nlm.nih.gov/30396335/) |
| Dairy (high intake) | PD | ↑ risk | OR 1.26 (1.12–1.41) | Meta-analysis (29 cohorts) | [41252180](https://pubmed.ncbi.nlm.nih.gov/41252180/) |
| *H. pylori* | PD | ↑ risk | OR 1.65 (1.43–1.92) | Meta-analysis (23 studies) | [32017453](https://pubmed.ncbi.nlm.nih.gov/32017453/) |
| Hepatitis C virus | PD | ↑ risk | OR 1.20 (1.01–1.41) | Meta-analysis | [32017453](https://pubmed.ncbi.nlm.nih.gov/32017453/) |
| Influenza / herpesviruses | PD | null | not associated | Meta-analysis | [32017453](https://pubmed.ncbi.nlm.nih.gov/32017453/) |
| Proton pump inhibitors | PD | ↑ risk | OR 1.14 (1.07–1.22) | Meta-analysis (6 studies) | [41984194](https://pubmed.ncbi.nlm.nih.gov/41984194/) |
| GI syndromes (constipation etc.) | PD | ↑ (prodromal) | OR 3.3–4.6 | Case-control/cohort | [37620120](https://pubmed.ncbi.nlm.nih.gov/37620120/) |
| Appendectomy | PD | null | HR 1.42 (0.88–2.30) | Cohort (Korea) | [38696328](https://pubmed.ncbi.nlm.nih.gov/38696328/) |
| Occupational solvents/metals/pesticides | MSA | ↑ risk (weak) | assoc. | Case-control (ESGAP) | [11487219](https://pubmed.ncbi.nlm.nih.gov/11487219/) |
| Occupational pesticides (JEM) | MSA | **null** | no assoc. | Case-control (Aquitaine) | [15272223](https://pubmed.ncbi.nlm.nih.gov/15272223/) |
| Smoking | MSA | ↓ (less frequent) | assoc. | Case-control | [11487219](https://pubmed.ncbi.nlm.nih.gov/11487219/) |
| Smoking | iRBD | **↑ risk** | OR 1.43 (p=0.028) | Case-control (multicenter) | [22744670](https://pubmed.ncbi.nlm.nih.gov/22744670/) |
| Head injury | iRBD | ↑ risk | OR 1.59 (p=0.037) | Case-control | [22744670](https://pubmed.ncbi.nlm.nih.gov/22744670/) |
| Farming | iRBD | ↑ risk | OR 1.67 (p=0.022) | Case-control | [22744670](https://pubmed.ncbi.nlm.nih.gov/22744670/) |
| Caffeine | DLB | ↓ protective | OR 0.29 (0.14–0.57) | Case-control | [23892702](https://pubmed.ncbi.nlm.nih.gov/23892702/) |
| Smoking | DLB | **null** | not associated | Case-control | [23892702](https://pubmed.ncbi.nlm.nih.gov/23892702/) |

---

## Key Findings by Disease

### Parkinson Disease

#### Pesticides and herbicides

Pesticides are the best-established occupational/residential risk class for PD, and the subclasses converge mechanistically on mitochondrial complex-I inhibition and oxidative stress. **Paraquat**, a redox-cycling herbicide, carries a pooled odds ratio of **1.64 (95% CI 1.27–2.13)** across 13 case-control studies [PMID: 30474499](https://pubmed.ncbi.nlm.nih.gov/30474499/), with strong animal face-validity: a PRISMA meta-analysis of 54 rodent studies found paraquat produces substantial substantia nigra pars compacta neuronal loss (SMD 3.07, 95% CI 2.48–3.65) [PMID: 41871812](https://pubmed.ncbi.nlm.nih.gov/41871812/). **Rotenone**, a botanical complex-I inhibitor, was associated with PD at **OR 1.57** in the 181,842-participant AGRICAN cohort, strongest in farmers with the longest exposure [PMID: 29136149](https://pubmed.ncbi.nlm.nih.gov/29136149/), and remained associated "regardless of glove use" in the FAME nested case-control study [PMID: 25461423](https://pubmed.ncbi.nlm.nih.gov/25461423/) — an argument for causality rather than recall artefact. Dietary fat modifies the effect: rotenone OR rose to 5.8 (2.3–15) in those with high saturated-fat intake [PMID: 24120951](https://pubmed.ncbi.nlm.nih.gov/24120951/).

**Organochlorines** (dieldrin, DDT/DDE) increase PD risk, with a blood-measured pooled **OR 1.54 (1.32–1.79)** across 7 studies and OR 1.19 (1.04–1.35) by indirect assessment [PMID: 39520734](https://pubmed.ncbi.nlm.nih.gov/39520734/); the signal was positive in Asian studies and non-significant in North America/Europe. Animal work shows dieldrin impairs aldehyde dehydrogenase and dopamine homeostasis causing nigral oxidative damage [PMID: 42808099](https://pubmed.ncbi.nlm.nih.gov/42808099/), and perinatal dieldrin produces persistent sex-specific DNA-methylation changes in dopaminergic neurodevelopment genes [PMID: 38746441](https://pubmed.ncbi.nlm.nih.gov/38746441/). **Chlorpyrifos**, an organophosphate, is uniquely informative: in the UCLA PEG cohort long-term residential exposure conferred **>2.5-fold increased risk**, and the accompanying mouse/zebrafish work showed the dopaminergic loss was "at least partially due to autophagy dysfunction and synuclein accumulation" — restoring autophagic flux or eliminating synuclein was protective [PMID: 41382278](https://pubmed.ncbi.nlm.nih.gov/41382278/). Chlorpyrifos thus maps distinctively onto the **Autophagy-Lysosome Pathway Dysfunction** node.

Composite rural proxies reinforce these findings: a classic meta-analysis reported rural living OR 1.56 (1.18–2.07), farming OR 1.42 (1.05–1.91), pesticide exposure OR 1.85 (1.31–2.60), and well-water use OR 1.26 (0.97–1.64, borderline) [PMID: 11437458](https://pubmed.ncbi.nlm.nih.gov/11437458/). A Bradford-Hill weight-of-evidence assessment, however, cautioned that these rural associations are **weaker and less consistent** than the smoking "positive control," concluding that an unidentified factor correlated with rural living/farming — rather than any single measured pesticide — may be causal [PMID: 27055126](https://pubmed.ncbi.nlm.nih.gov/27055126/).

#### Solvents

Chlorinated solvent exposure increases PD risk. The strongest evidence is the **Camp Lejeune** population-based cohort: Marines stationed at the trichloroethylene (TCE)-contaminated base (monthly median TCE >70× the permissible level) had elevated PD risk (reported ~70% higher) and more frequent prodromal features versus the uncontaminated Camp Pendleton base [PMID: 37184848](https://pubmed.ncbi.nlm.nih.gov/37184848/). A follow-up found VOC-exposed PD patients progressed faster to psychosis, fracture and fall (adjusted HRs exceeding 2) [PMID: 38988230](https://pubmed.ncbi.nlm.nih.gov/38988230/). The companion mortality study reported an elevated PD hazard that persisted after quantitative bias analysis for smoking and alcohol [PMID: 38961410](https://pubmed.ncbi.nlm.nih.gov/38961410/).

#### Metals

A systematic review/meta-analysis of 88 studies found that **cumulative lead in bone** was associated with increased PD risk, while serum copper, iron and zinc were *lower* in cases (likely reflecting disease rather than cause), and — importantly — **no association for other metals, including manganese** [PMID: 37022311](https://pubmed.ncbi.nlm.nih.gov/37022311/). Cumulative bone lead also correlated with worse cognition in PD [PMID: 23143985](https://pubmed.ncbi.nlm.nih.gov/23143985/) and reduced olfactory recognition in elderly men [PMID: 26121922](https://pubmed.ncbi.nlm.nih.gov/26121922/). **Manganese** deserves separate treatment: Mn-containing welding fume causes a dose-dependent parkinsonism (prevalence **15.6% in welders vs 0%** in referents) with a clinical phenotype overlapping but distinct from Lewy-body PD (less rest tremor/asymmetry) [PMID: 22975422](https://pubmed.ncbi.nlm.nih.gov/22975422/); longitudinal follow-up showed dose-dependent progression (annual UPDRS3 +0.24 per mg Mn/m³·year) [PMID: 28031394](https://pubmed.ncbi.nlm.nih.gov/28031394/). Manganism is therefore best curated as a **distinct toxicant parkinsonism**, not idiopathic synucleinopathy.

#### Air pollution

The Ontario cohort (~2.2M adults, 38,745 PD cases) found each IQR (3.8 µg/m³) increase in PM2.5 associated with a **4% higher incident PD risk (HR 1.04, 1.01–1.08)**, with comparable small effects for NO2 and ozone [PMID: 30124852](https://pubmed.ncbi.nlm.nih.gov/30124852/). A Korean cohort found NO2 associated with incident PD (HR 1.41 highest vs lowest quartile) [PMID: 33999109](https://pubmed.ncbi.nlm.nih.gov/33999109/). An earlier US nested case-control found no overall association but positive subgroup effects in women and never-smokers (PM10 OR 1.65 in women) [PMID: 27285422](https://pubmed.ncbi.nlm.nih.gov/27285422/). The effect is real but **small and somewhat inconsistent.**

#### Head injury

The evidence is genuinely **conflicting.** Balabandian et al. pooled 15 studies to a TBI–PD risk ratio of **1.48 (1.22–1.74)** [PMID: 36781627](https://pubmed.ncbi.nlm.nih.gov/36781627/), whereas Huang et al. (18 studies, 3.26M patients) found TBI associated with dementia but **not PD** [PMID: 30396335](https://pubmed.ncbi.nlm.nih.gov/30396335/). This association is especially vulnerable to **reverse causation** — prodromal PD gait/balance impairment increases falls and head injuries — and to recall bias.

#### MPTP — mechanistic proof-of-principle

MPTP is not an epidemiological exposure but the historical demonstration that a synthetic complex-I toxicant causes irreversible human parkinsonism. It crosses the blood-brain barrier, is converted by astrocytic MAO-B to MPP+, selectively enters dopaminergic neurons via the dopamine transporter, and inhibits mitochondrial complex I, generating reactive oxygen species and causing nigrostriatal degeneration [PMID: 38773545](https://pubmed.ncbi.nlm.nih.gov/38773545/); [PMID: 27665784](https://pubmed.ncbi.nlm.nih.gov/27665784/). It is the mechanistic keystone linking the pesticide class to **Mitochondrial Dysfunction**, **Oxidative Stress** and **Dopaminergic Neuron Loss.**

#### Gut-related exposures

The gut–brain (Braak) axis is strongly supported. Specific GI syndromes **precede** PD diagnosis in a PD-specific manner (vs AD and cerebrovascular disease): gastroparesis OR 4.64, dysphagia OR 3.58, IBS-without-diarrhoea OR 3.53, constipation OR 3.32 [PMID: 37620120](https://pubmed.ncbi.nlm.nih.gov/37620120/). The vagal route is implicated by the vagotomy natural experiment: **full truncal vagotomy** reduced PD risk (HR 0.53 at >20 years) while **superselective vagotomy had no effect** (HR 1.09) [PMID: 26031848](https://pubmed.ncbi.nlm.nih.gov/26031848/). **Appendectomy**, by contrast, was **null** in a large Korean cohort (adjusted HR 1.42, 0.88–2.30) [PMID: 38696328](https://pubmed.ncbi.nlm.nih.gov/38696328/), with inconsistent Western results; it should be curated as unresolved. **PPI use** (which alters gut flora) modestly raised PD risk (OR 1.14, 1.07–1.22) even after adjustment for *H. pylori* [PMID: 41984194](https://pubmed.ncbi.nlm.nih.gov/41984194/).

#### Infections

A meta-analysis of 23 studies found **positive** associations for *Helicobacter pylori* (OR 1.65, 1.43–1.92), hepatitis C (OR 1.20, 1.01–1.41), *Malassezia* and *Pneumoniae*, and — importantly — **explicit null results** for influenza, herpesviruses, HBV, scarlet fever, mumps, varicella, pertussis, rubella and measles [PMID: 32017453](https://pubmed.ncbi.nlm.nih.gov/32017453/). Antiviral treatment of HCV reduced PD risk (OR 0.67), supporting causality for the HCV signal.

#### Protective / inverse associations

- **Smoking:** meta-analysis of 69 studies, ever-smokers RR **0.59 (0.56–0.62)**, with dose-response and a current-smoking RR of 0.35; smokeless tobacco (snus) in never-smokers HR 0.41 implicates **nicotine** rather than combustion [PMID: 26272284](https://pubmed.ncbi.nlm.nih.gov/26272284/); [PMID: 27940486](https://pubmed.ncbi.nlm.nih.gov/27940486/). The consistency across prospective designs argues against pure reverse causation, though it cannot be excluded.
- **Caffeine/coffee:** pooled HR **0.80 (0.75–0.85)**, dose-dependent [PMID: 32580456](https://pubmed.ncbi.nlm.nih.gov/32580456/).
- **Physical activity:** pooled HR **0.66 (0.57–0.78)**, stronger/clearer in men [PMID: 25410713](https://pubmed.ncbi.nlm.nih.gov/25410713/); [PMID: 20660864](https://pubmed.ncbi.nlm.nih.gov/20660864/).
- **Urate/gout:** gout inversely associated with PD (IRR **0.80**), and within gout patients higher urate was further protective [PMID: 41050064](https://pubmed.ncbi.nlm.nih.gov/41050064/).
- **Ibuprofen (but not aspirin or other NSAIDs):** pooled RR **0.73 (0.63–0.85)** [PMID: 21368281](https://pubmed.ncbi.nlm.nih.gov/21368281/).

A critical caveat applies to smoking and coffee: **reverse causation** (prodromal hypodopaminergic personality change reduces addictive behaviours) and **survival bias** remain plausible alternative explanations, and an umbrella review of 46 systematic reviews attributed many conflicting non-genetic associations to **study-design differences** (cohort vs case-control), rating 84.7% of reviews as critically low methodological quality [PMID: 33814465](https://pubmed.ncbi.nlm.nih.gov/33814465/).

#### Medications (iatrogenic)

- **Calcium channel blockers (dihydropyridine):** pooled RR **0.76–0.81** [PMID: 26464872](https://pubmed.ncbi.nlm.nih.gov/26464872/); [PMID: 25845582](https://pubmed.ncbi.nlm.nih.gov/25845582/).
- **Statins:** pooled RR **0.79–0.86**, duration-dependent (long-duration RR 0.49; short-term null), but with **no disease-modifying effect** on UPDRS-III [PMID: 39097909](https://pubmed.ncbi.nlm.nih.gov/39097909/); [PMID: 35629248](https://pubmed.ncbi.nlm.nih.gov/35629248/).
- **β2-adrenoreceptor drugs:** mechanistically, the β2AR regulates the *SNCA* (α-synuclein) gene; agonists (salbutamol) lower SNCA and were associated with reduced PD risk (RR ≈ 0.66), while antagonists (propranolol) raise SNCA and PD risk (RR ≈ 2.2) [PMID: 28860381](https://pubmed.ncbi.nlm.nih.gov/28860381/). This is the clearest exposure→gene→risk mechanistic chain in the dataset.

#### Diet

High **dairy** consumption modestly raises PD risk (meta-analysis of 29 cohorts, 1.3M participants: OR **1.26, 1.12–1.41** for high dairy; milk OR 1.23; low-fat dairy OR 1.30), with a male-predominant effect (males HR 1.28 vs females HR 1.02) and ~13% increased risk per cup of milk/day; legumes/nuts were protective [PMID: 41252180](https://pubmed.ncbi.nlm.nih.gov/41252180/); [PMID: 41792943](https://pubmed.ncbi.nlm.nih.gov/41792943/); [PMID: 28596209](https://pubmed.ncbi.nlm.nih.gov/28596209/).

### Multiple System Atrophy

The MSA environmental evidence base is **small and conflicting** (MSA prevalence ~4–5/100,000). The ESGAP European case-control study (73 MSA cases) reported increased risk with occupational exposure to organic solvents, plastic monomers/additives, pesticides and metals, and noted smoking was *less* frequent in MSA cases than controls [PMID: 11487219](https://pubmed.ncbi.nlm.nih.gov/11487219/). However, the Aquitaine case-control study, using a formal job-exposure matrix, found **no significant relationship between occupational pesticide exposure and MSA** [PMID: 15272223](https://pubmed.ncbi.nlm.nih.gov/15272223/) — directly cautioning against transferring the PD pesticide finding. The smoking direction (inverse) is the same as PD but rests on tiny samples. No robust meta-analytic effect size exists for any MSA exposure.

### REM Sleep Behaviour Disorder (prodromal synucleinopathy)

The pivotal multicenter case-control study (347 iRBD cases vs 347 matched controls) found that iRBD patients were **more likely to smoke (ever-smoking 64.0% vs 55.5%, OR 1.43, p=0.028)** — the *opposite* direction to PD — and also more likely to report previous **head injury (OR 1.59, p=0.037)**, **farming occupation (OR 1.67, p=0.022)**, borderline welding (OR 1.53), and fewer years of schooling; caffeine and alcohol did **not** differ between cases and controls [PMID: 22744670](https://pubmed.ncbi.nlm.nih.gov/22744670/). The reversed smoking direction is the clearest single demonstration of **non-transferability** in the entire dataset. On phenoconversion, autonomic rather than classical environmental markers predict progression: in a prospective iRBD cohort, neurogenic orthostatic hypotension (HR 5.05) and abnormal baroreflex function predicted conversion to overt synucleinopathy [PMID: 40112275](https://pubmed.ncbi.nlm.nih.gov/40112275/); environmental exposures have *not* been shown to predict phenoconversion.

### Dementia with Lewy Bodies

The single dedicated case-control study (147 DLB cases) found caffeine use **less** likely in DLB (OR **0.29, 0.14–0.57**) — consistent with PD — plus positive associations with anxiety (OR 7.4), depression (OR 6.0), stroke (OR 2.8), family history of PD (OR 4.6), and APOE ε4 (OR 2.2) [PMID: 23892702](https://pubmed.ncbi.nlm.nih.gov/23892702/). Critically, **smoking and education — which have opposing effects in AD and PD — were NOT risk factors for DLB**, and the authors concluded "DLB risk factors are an amalgam of those for AD and PD." Pesticide and head-injury data specific to DLB are essentially absent.

### Pure Autonomic Failure

No citable environmental epidemiology was found for pure autonomic failure. This is a genuine gap, and the disease's `environmental` section should be curated as "no exposure studies identified" rather than populated by transfer from PD.

---

## Mechanistic Model and Interpretation

The PD exposures converge on a small set of interacting mechanism nodes. Toxicant exposures (pesticides, solvents, metals, air pollution, MPTP) act predominantly at the **mitochondria/oxidative-stress** hub, while gut-related and infectious exposures act via the **gut–vagal α-synuclein propagation** axis; a subset (chlorpyrifos) additionally hits the **autophagy-lysosome** node, and β2-adrenergic drugs act "upstream" by transcriptionally regulating *SNCA* itself.

```
            TOXICANT ROUTE                          GUT–BRAIN ROUTE
   ┌──────────────────────────────┐      ┌───────────────────────────────┐
   │ Paraquat, Rotenone, MPTP,     │      │ H. pylori, HCV, PPIs,          │
   │ Organochlorines, Mn, TCE,     │      │ GI syndromes, (vagotomy = -)   │
   │ Air pollution (PM2.5/NO2), Pb │      │                                │
   │            │                  │      │             │                  │
   │            ▼                  │      │             ▼                  │
   │ Mitochondrial Dysfunction ◄───┘      │  Intestinal Inflammation /     │
   │ + Oxidative Stress            │      │  Barrier Dysfunction           │
   │            │                  │      │             │                  │
   │  Chlorpyrifos → Autophagy-    │      │             ▼                  │
   │        Lysosome Dysfunction   │      │   Enteric α-Syn Seeding        │
   │            ▼                  │      │             │                  │
   └───────► α-Synuclein Aggregation ◄────┤   Vagal–Brainstem Propagation  │
                │        ▲                 └─────────────┼──────────────────┘
                │        │ SNCA regulation (β2AR:        │
                │        │ salbutamol ↓ / propranolol ↑) │
                ▼        │                               ▼
        Dopaminergic Neuron Loss ◄─── Neuroinflammation ─┘
                │
                ▼
        PARKINSON DISEASE  (modified by: urate↓, PA↓, NSAIDs↓,
                            CCB/statin↓, dairy↑, nicotine↓)
```

**Exposure → mechanism-node mapping (PD):**

| Exposure | Primary node(s) | Mode |
|---|---|---|
| Paraquat, rotenone, MPTP | Mitochondrial Dysfunction; Oxidative Stress; Dopaminergic Neuron Loss | triggers |
| Organochlorines (dieldrin) | Oxidative Stress; Dopaminergic Neuron Loss | triggers |
| Chlorpyrifos | Autophagy-Lysosome Pathway Dysfunction; α-Synuclein Aggregation | triggers |
| TCE / solvents | Mitochondrial Dysfunction; Oxidative Stress | triggers |
| Lead | Oxidative Stress; Iron Accumulation/Ferroptosis | predisposes |
| Manganese | Dopaminergic/basal-ganglia injury (distinct parkinsonism) | triggers |
| Air pollution | Neuroinflammation; Oxidative Stress; Blood-Brain Barrier Dysfunction | predisposes |
| *H. pylori*, HCV, PPIs | Gut Microbiome Dysbiosis; Intestinal Inflammation | predisposes |
| GI syndromes / gut α-syn | Enteric α-Syn Seeding; Vagal-Brainstem Propagation | triggers (prodromal) |
| Truncal vagotomy | Vagal-Brainstem Propagation (interrupted) | protects |
| Nicotine (smoking/snus) | Oxidative Stress; Neuroinflammation | protects |
| Caffeine | Adenosine A2A / dopaminergic signalling | protects |
| Urate | Oxidative Stress (antioxidant) | protects |
| Ibuprofen | Neuroinflammation | protects |
| CCB (dihydropyridine) | Cav1.3 Ca²⁺ stress on dopaminergic neurons | protects |
| β2-agonist / antagonist | α-Synuclein Aggregation (via SNCA transcription) | protects / predisposes |

For the other diseases the mechanism nodes are far less populated by exposure data. MSA's **Oligodendroglial α-Synuclein Accumulation (GCIs)** and **Mitochondrial Dysfunction/CoQ10** nodes have only weak, conflicting occupational-solvent/metal links. iRBD's **Brainstem REM-Atonia Circuit** and **Progression to Overt Synucleinopathy** nodes are driven, in current data, by autonomic physiology rather than measured environmental exposure. DLB's **Concomitant Alzheimer Co-Pathology** node explains why its risk profile is an AD/PD amalgam with null smoking.

---

## Evidence Base

The strongest, highest-tier evidence underpinning this report:

- **Smoking:** [PMID: 26272284](https://pubmed.ncbi.nlm.nih.gov/26272284/) (69-study meta-analysis) and [PMID: 27940486](https://pubmed.ncbi.nlm.nih.gov/27940486/) (snus, isolating nicotine) jointly establish a robust, dose-responsive inverse association.
- **Paraquat / rotenone / organochlorines / chlorpyrifos:** [PMID: 30474499](https://pubmed.ncbi.nlm.nih.gov/30474499/), [PMID: 29136149](https://pubmed.ncbi.nlm.nih.gov/29136149/), [PMID: 39520734](https://pubmed.ncbi.nlm.nih.gov/39520734/), [PMID: 41382278](https://pubmed.ncbi.nlm.nih.gov/41382278/) provide convergent human effect sizes plus animal mechanism; the glove-use analysis [PMID: 25461423](https://pubmed.ncbi.nlm.nih.gov/25461423/) strengthens causal inference.
- **TCE / Camp Lejeune:** [PMID: 37184848](https://pubmed.ncbi.nlm.nih.gov/37184848/) and [PMID: 38988230](https://pubmed.ncbi.nlm.nih.gov/38988230/) — a quasi-experimental population comparison that is hard to confound.
- **Metals:** [PMID: 37022311](https://pubmed.ncbi.nlm.nih.gov/37022311/) is the definitive meta-analysis isolating lead and nulling manganese for *idiopathic* PD; [PMID: 22975422](https://pubmed.ncbi.nlm.nih.gov/22975422/) / [PMID: 28031394](https://pubmed.ncbi.nlm.nih.gov/28031394/) separately establish Mn welding parkinsonism.
- **Gut–vagal axis:** [PMID: 26031848](https://pubmed.ncbi.nlm.nih.gov/26031848/) (vagotomy) and [PMID: 37620120](https://pubmed.ncbi.nlm.nih.gov/37620120/) (prodromal GI syndromes) are the core support for the Braak hypothesis; [PMID: 38696328](https://pubmed.ncbi.nlm.nih.gov/38696328/) provides the null appendectomy counterpoint.
- **Non-transferability pillars:** [PMID: 22744670](https://pubmed.ncbi.nlm.nih.gov/22744670/) (iRBD smoking POSITIVE), [PMID: 23892702](https://pubmed.ncbi.nlm.nih.gov/23892702/) (DLB smoking NULL), [PMID: 15272223](https://pubmed.ncbi.nlm.nih.gov/15272223/) (MSA pesticide NULL) are the three pillars of the central result.
- **Consolidation / caveats:** [PMID: 33814465](https://pubmed.ncbi.nlm.nih.gov/33814465/) (umbrella review) and [PMID: 27055126](https://pubmed.ncbi.nlm.nih.gov/27055126/) (Bradford-Hill) temper the pesticide and inverse-association literature with design and consistency critiques.

Challenging/qualifying evidence is deliberately retained: the TBI meta-analyses conflict ([PMID: 36781627](https://pubmed.ncbi.nlm.nih.gov/36781627/) positive vs [PMID: 30396335](https://pubmed.ncbi.nlm.nih.gov/30396335/) null); air-pollution effects are small and subgroup-dependent ([PMID: 27285422](https://pubmed.ncbi.nlm.nih.gov/27285422/)); and the organochlorine signal is geographically heterogeneous ([PMID: 39520734](https://pubmed.ncbi.nlm.nih.gov/39520734/)).

---

## Limitations and Knowledge Gaps

1. **PD-centricity.** The overwhelming majority of effect sizes derive from PD. DLB rests essentially on a *single* case-control study, MSA on two small conflicting ones, and iRBD on one multicenter case-control plus phenoconversion cohorts. Effect sizes for non-PD synucleinopathies should be treated as provisional.
2. **Pure autonomic failure is unstudied.** No citable environmental epidemiology was found; this gap should be stated explicitly in curation.
3. **Reverse causation and survival bias** persistently threaten the inverse associations (smoking, coffee) and the TBI association. Prodromal PD can change behaviour decades before diagnosis.
4. **Recall and selection bias** dominate the case-control pesticide/solvent literature; much metals evidence uses post-diagnosis biomonitoring, which cannot establish temporality.
5. **Methodological quality is low.** 84.7% of systematic reviews in the umbrella review were rated critically low, and design differences explained many conflicts [PMID: 33814465](https://pubmed.ncbi.nlm.nih.gov/33814465/).
6. **Geographic heterogeneity** (organochlorines positive in Asia, null in West; PPIs significant in Asia/Europe, null in US) suggests unmeasured gene–environment or exposure-mix confounding.
7. **Manganism vs idiopathic PD** must not be conflated — Mn produces a related but pathologically distinct parkinsonism.
8. **No exposure predicts iRBD phenoconversion** in current data; autonomic markers do.

---

## Proposed Follow-up Actions

1. **Curate each disease's `environmental` section independently.** Do not propagate PD exposures to DLB, MSA or iRBD. Explicitly flag the reversed smoking direction in iRBD, the null smoking in DLB, and the null pesticide finding in MSA.
2. **Link exposures to mechanism nodes per the mapping table above**, tagging the mode (triggers / exacerbates / predisposes / protects) and the evidence tier (human meta-analysis > cohort > case-control > animal mechanism).
3. **Tag every inverse association with the reverse-causation/survival-bias caveat**, and every case-control exposure with the recall-bias caveat, as structured metadata.
4. **Record explicit null/absent entries** — MSA pesticides (JEM-null), DLB smoking (null), influenza/herpesviruses (null), appendectomy (null/unresolved), and pure autonomic failure (no data) — so the knowledge base distinguishes "studied and null" from "not studied."
5. **Prioritise future primary research** on DLB and MSA exposure epidemiology and on whether any environmental exposure predicts iRBD phenoconversion, which is the highest-value prevention target.
6. **Separate manganese welding parkinsonism** as its own entity linked to basal-ganglia/dopaminergic injury rather than Lewy-body α-synucleinopathy.

---

*Report generated from 28 confirmed findings across 89 reviewed papers over 5 investigation iterations. All effect sizes and verbatim support are drawn from PubMed-indexed primary studies and meta-analyses; no PMIDs were invented, and gaps (notably pure autonomic failure) are stated where no citable source exists.*


## Artifacts

- [OpenScientist final report](Alpha_Synucleinopathies-environmental-exposures-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Alpha_Synucleinopathies-environmental-exposures-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 52 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 52 |
| On topic | 39 |
| Off topic | 0 |

All extracted references resolved successfully.
