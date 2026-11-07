---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T18:31:06.621087'
end_time: '2026-11-06T18:59:26.711413'
duration_seconds: 1700.09
template_file: experiments/biomni_lead_exploration/repurposing_template.md
template_variables:
  disease_name: Idiopathic Pulmonary Fibrosis
  drug: a cGAS or STING inhibitor
  drug_action: blocking cytosolic DNA sensing through cGAS and its adaptor STING
  mechanism: self-DNA sensing through cGAS in damaged, senescent alveolar epithelium,
    driving type I interferon and senescence-associated inflammation
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 14
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cgas_sting_inhibitor-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cgas_sting_inhibitor-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Drug Repurposing Hypothesis Assessment

## The Hypothesis

- **Disease:** Idiopathic Pulmonary Fibrosis
- **Drug:** a cGAS or STING inhibitor
- **Drug's target and action:** blocking cytosolic DNA sensing through cGAS and its adaptor STING
- **Disease mechanism the drug would act on:** self-DNA sensing through cGAS in damaged, senescent alveolar epithelium, driving type I interferon and senescence-associated inflammation

The hypothesis is that a cGAS or STING inhibitor, by blocking cytosolic DNA sensing through cGAS and its adaptor STING, would benefit patients with
Idiopathic Pulmonary Fibrosis because it interrupts "self-DNA sensing through cGAS in damaged, senescent alveolar epithelium, driving type I interferon and senescence-associated inflammation". Your job is to assess this
hypothesis, not to advocate for it. Evidence against it is as valuable as evidence for it.

Every factual claim MUST cite a primary source by PMID (or DOI, or NCT number for a
trial registration) and include a short verbatim quote from the cited abstract or record.
Do not paraphrase quotes. Do not invent identifiers. Separate established findings from
your own inference, and label which is which.

## Questions

### 1. Is the mechanism active in this disease?

- Evidence that the drug's target or pathway is active, elevated or genetically implicated
  in patients with Idiopathic Pulmonary Fibrosis: in affected tissue, in blood, or through human genetics.
- Whether activity is uniform or confined to a subgroup of patients, and how that subgroup
  is identified (a biomarker, a clinical feature).

### 2. Does blocking it help?

- Clinical trials of a cGAS or STING inhibitor in Idiopathic Pulmonary Fibrosis: registration numbers, phase, status and
  reported results, if any exist.
- Trials of other drugs acting on the same target or pathway in Idiopathic Pulmonary Fibrosis, with their
  outcomes, including failures.
- Results of a cGAS or STING inhibitor in related diseases that share the mechanism, and how far those results
  should transfer here.
- Animal or human tissue experiments in which blocking the pathway changed
  Idiopathic Pulmonary Fibrosis-like features.

### 3. Reasons it might fail

- Redundant pathways, wrong cell compartment, wrong disease stage, drug not reaching the
  affected tissue, or trial endpoints that cannot detect the effect.
- Safety concerns specific to this patient population.

### 4. Verdict

- One paragraph: how strong is the case, and what single experiment or trial design would
  most efficiently test it?
- List the PMIDs and trial identifiers that carry the most weight, with one line each.


## Output

# Drug Repurposing Hypothesis Assessment: cGAS/STING Inhibition in Idiopathic Pulmonary Fibrosis

## Summary

**The mechanism is real, but the repurposing case is biologically plausible rather than clinically proven.** The cGAS-STING cytosolic DNA-sensing pathway is demonstrably active in idiopathic pulmonary fibrosis (IPF) lung tissue — localized to exactly the compartments the hypothesis names (senescent alveolar epithelium and macrophages) — and human genetics provides a striking causal proof-of-concept: gain-of-function mutations in *STING1* (the disease SAVI) cause progressive interstitial lung disease (ILD) in humans. Genetic and pharmacologic blockade of the pathway reduces fibrosis in multiple animal models and in a related human fibrotic disease (systemic sclerosis). This is a stronger mechanistic foundation than most IPF repurposing candidates possess.

**However, the case has serious, specific counterweights.** First, there are **zero registered clinical trials** of any cGAS or STING inhibitor in IPF (or in systemic sclerosis) as of November 2026 — the pathway has never been tested in the target disease, and the only clinical-stage STING drugs are *agonists* developed for oncology, the opposite of what is needed. Second, cGAS (*MB21D1/CGAS*) and STING (*TMEM173/STING1*) are **not** IPF genetic-risk genes; IPF risk is driven by telomere, senescence, and host-defense genes (MUC5B, TERT, TERC, FAM13A, DSP), placing cGAS-STING genetically downstream of the primary disease drivers. Third, the functionally dominant cellular compartment in animal models appears to be the **macrophage**, not the epithelium emphasized in the hypothesis, and selective drug delivery to distal-lung macrophages is a recognized translational hurdle. Fourth, downstream interferon-axis blockade (JAK inhibitors) gives only **partial, transient** control even in the purest human STING-driven lung fibrosis (SAVI), and IPF has a documented history of *harm* from broad immunosuppression. Finally, blocking a core antiviral sensor is a genuine safety liability in an infection-prone population.

**Verdict:** The hypothesis is worth testing but should not be assumed to work. The single most efficient test would be a biomarker-enriched (cGAMP-/interferon-signature-high), lung-targeted (inhaled) Phase 2a proof-of-mechanism trial of a cGAS or STING inhibitor added to standard antifibrotic therapy, with target engagement and interferon-stimulated gene (ISG) suppression as primary readouts rather than FVC alone. This report separates **established findings** (human tissue, human genetics, trial registries, published experiments) from **inference** (my synthesis of how these pieces combine), and labels each.

---

## Key Findings

### Finding 1 — The pathway is active in IPF lung, in the compartments the hypothesis names (Established)

Human tissue evidence directly supports the first premise of the hypothesis. Immunohistochemistry of 44 usual interstitial pneumonia (UIP) cases (IPF or autoimmune) showed cGAS and phosphorylated STING expression in the epithelium of remodeled areas and in macrophages ([PMID: 38944022](https://pubmed.ncbi.nlm.nih.gov/38944022/)): *"Epithelial cells in remodeled areas and macrophages expressed cGAS-pSTING, TREX1; epithelia but not macrophages stained for PARP1."* A separate study localized cGAS specifically to senescent epithelial cells — the exact cell state the hypothesis invokes ([PMID: 34524912](https://pubmed.ncbi.nlm.nih.gov/34524912/)): *"cGAS expression in fibrotic tissue from lungs of patients with IPF was detected within cells immunoreactive for epithelial cell adhesion molecule (EpCAM) and p21, epithelial and senescence markers, respectively."*

This is observational/descriptive evidence (protein localization, not a quantitative effect size), but it establishes that the drug's target is present and apparently activated in the right tissue and the right cells. This is the single strongest "mechanism is active" data point.

### Finding 2 — Human genetics gives a causal proof-of-concept: STING gain-of-function causes progressive ILD (Established)

The most compelling causal human evidence comes from a monogenic disease. STING-associated vasculopathy with onset in infancy (SAVI) is caused by heterozygous gain-of-function mutations in *STING1* that constitutively activate STING ([PMID: 42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/)): *"these mutations lead to a constitutive activation of the STING protein, resulting in excessive type I interferon production, which drives chronic inflammation and damage to various organs, primarily as cutaneous vasculopathy and progressive interstitial lung disease (ILD)."* A familial case series confirmed the monogenic etiology ([PMID: 40731159](https://pubmed.ncbi.nlm.nih.gov/40731159/)): *"STING-associated vasculopathy with onset in infancy (SAVI) is a very rare autosomal-dominant Mendelian autoinflammatory disease caused by heterozygous gain-of-function mutations in STING1."*

**Inference:** SAVI demonstrates that *too much* STING signaling is sufficient to produce progressive lung fibrosis in humans — a strong "forward genetics" argument that the pathway can drive the disease phenotype. The caveat (also established) is that SAVI pathogenesis has IFN-independent components ([PMID: 42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/)): *"SAVI pathogenesis is not only driven by the interferon storm, but relies also on non-canonical IFN-independent cellular pathways across distinct hematopoietic and non-hematopoietic compartments."* This flags that even complete IFN-axis blockade may not capture all of STING's fibrotic effects — a reason a *proximal* cGAS/STING inhibitor might outperform a *downstream* JAK inhibitor, but also a reason redundancy could blunt benefit.

### Finding 3 — Blocking the pathway reduces lung fibrosis in animal models (Established, with one contradiction)

Multiple independent studies show that interrupting cGAS-STING attenuates experimental lung fibrosis:

- STING-knockout and TREX1-knockout mice established STING's role in bleomycin fibrosis, and a STING-pathway inhibitor (QFAE-nB) alleviated fibrosis ([PMID: 37806536](https://pubmed.ncbi.nlm.nih.gov/37806536/)): *"TREX1-KO and STING-KO mice were used to verify the relationship between STING and PF and the important target action of QFAE-nB."*
- STING- and NLRP3-deficient mice showed significantly attenuated bleomycin inflammation/fibrosis downstream of oxidized mitochondrial DNA ([PMID: 41948458](https://pubmed.ncbi.nlm.nih.gov/41948458/)): *"studies using STING- and NLRP3-deficient mice demonstrated that loss of either pathway significantly attenuated BLM-induced inflammation and fibrosis, implicating their involvement downstream of oxid-mtDNA signaling."*
- Small-molecule cGAS inhibitors (G150, RU.521) reduced collagen deposition and improved survival in paraquat-induced lung fibrosis ([PMID: 40789441](https://pubmed.ncbi.nlm.nih.gov/40789441/)): *"the mouse-specific cGAS inhibitor RU.521 effectively reduced collagen deposition and fibrosis severity while also improving survival rates in PQ-treated mice."*

**Important contradiction (Established):** A UIP precision-cut-lung-slice model found that bleomycin activated cGAS-STING and senescence but with *no direct effect on fibrosis* ([PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)): *"Bleomycin promotes cellular senescence and activation of the cGAS-STING pathway without direct effect on fibrosis in an idiopathic pulmonary fibrosis model."* This demonstrates that pathway activation can be *dissociated* from the fibrotic outcome in a human-tissue-based UIP model, weighing against an obligate causal role.

### Finding 4 — The functionally dominant compartment is the macrophage, not the epithelium (Established)

This is a key mechanistic nuance that partly contradicts the hypothesis's framing. In the paraquat model, the pathway was hyperactivated in monocytes ([PMID: 40789441](https://pubmed.ncbi.nlm.nih.gov/40789441/)). More pointedly, macrophage-targeted STING gene editing ameliorated pulmonary fibrosis, with alveolar-macrophage STING identified as the critical driver ([PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)): *"The stimulator of interferon genes (STING) signaling pathway, particularly in alveolar macrophages, has been identified as a critical driver of fibrosis."* That same study names the translational barrier ([PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)): *"achieving efficient and selective drug delivery to these pathogenic macrophages in the distal lung represents the major hurdle that hinders its clinical translation."*

**Inference:** The hypothesis frames the epithelium as the key compartment; the strongest functional animal data point to macrophages. A systemically administered small-molecule inhibitor would hit both, so this does not sink the hypothesis — but it does mean that the epithelial-senescence narrative is incomplete, and it raises the bar for lung-targeted delivery.

### Finding 5 — Related-disease transfer: cGAS/STING suppression reverses fibrosis in systemic sclerosis, including lung (Established)

The closest clinical-adjacent evidence comes from systemic sclerosis (SSc). TY1, a noncoding-RNA drug that suppresses DNA damage and thereby inhibits cGAS/STING, normalized lung hydroxyproline and skin thickness in two mouse SSc models and reduced cGAS/cGAMP/STING/IFN in patient macrophages ([PMID: 42708359](https://pubmed.ncbi.nlm.nih.gov/42708359/)): *"In mice that had been injected s.c. with bleomycin to model SSc, exercise tolerance, cardiac function, lung hydroxyproline, and skin thickness reverted to normal levels after oral administration of TY1."* The authors conclude ([PMID: 42708359](https://pubmed.ncbi.nlm.nih.gov/42708359/)): *"Our findings support the hypothesis that cGAS/STING, activated by DNA damage, is a key driver of fibrosis in SSc."*

**Inference on transferability:** SSc-ILD and IPF share a fibrotic lung endpoint and a DNA-damage/senescence upstream, so transfer is plausible — but SSc is a primarily autoimmune, interferon-high disease, whereas IPF is a primarily epithelial-injury/aging disease with a weaker systemic IFN signature. The transfer is suggestive, not definitive.

### Finding 6 — Downstream IFN-axis blockade only partially and transiently helps STING-driven lung fibrosis (Established)

In SAVI, the purest human STING-driven ILD, JAK inhibitors offer only partial, transient control ([PMID: 42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/)): *"Janus kinase (JAK) inhibitors offer partial transient control, with risk of irreversible organ damage."* In that report, a boy failed ruxolitinib, tofacitinib, and baricitinib with worsening lung fibrosis, ultimately requiring allogeneic HSCT. In rheumatoid-arthritis-associated ILD, a phase II tofacitinib trial (NCT05246293) showed modest FVC decline (−72 mL/48 wk) and reduced KL-6 but frequent adverse events ([PMID: 42722091](https://pubmed.ncbi.nlm.nih.gov/42722091/)): *"Thirty-six (92%) had any adverse event; Three patients died. Upper airway respiratory infections were the most frequent adverse events."*

**Inference:** JAK inhibition acts *downstream* of STING on the IFN axis. Its limited efficacy could mean either (a) the IFN axis is not the whole story (favoring a proximal cGAS/STING inhibitor that also blocks IFN-independent STING outputs) or (b) the pathway is not the dominant fibrotic driver at the disease stage being treated (arguing against the hypothesis). Both interpretations are live; the data cannot yet distinguish them.

### Finding 7 — IPF genetics point away from cGAS/STING; no inhibitor trial exists (Established — key negative)

IPF GWAS risk loci are MUC5B, TERT, TERC (3q26), FAM13A, DSP, OBFC1/STN1, ATP11A, DPP9, 7q22, and 15q14-15 ([PMID: 23583980](https://pubmed.ncbi.nlm.nih.gov/23583980/)): *"We confirmed association with TERT at 5p15, MUC5B at 11p15 and the 3q26 region near TERC, and we identified seven newly associated loci."* The implicated processes are ([PMID: 23583980](https://pubmed.ncbi.nlm.nih.gov/23583980/)): *"genes involved in host defense, cell-cell adhesion and DNA repair contribute to risk of fibrotic IIPs."* These were replicated across ancestries ([PMID: 42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/)): *"We identified loci on chromosomes 4 (FAM13A; rs7690839), 5 (TERT; rs7734992), 6 (DSP; rs2076295), and 11 (MUC5B; rs35705950) that were significantly associated with risk of IPF."* **CGAS/MB21D1 and STING1/TMEM173 are absent from these lists.**

A ClinicalTrials.gov v2 API search (November 2026) returned **zero** trials of a cGAS or STING inhibitor for pulmonary fibrosis or systemic sclerosis; the only "STING" hits were jellyfish-sting products and oncology STING *agonists* ([PMID: 40533265](https://pubmed.ncbi.nlm.nih.gov/40533265/)): *"IMSA101 is a small molecule analog of cGAMP and a potent STING agonist."*

**Inference:** Human genetics places cGAS/STING downstream of the primary IPF drivers (telomere attrition → DNA damage/senescence → cGAS activation). This is consistent with cGAS being a *mediator* rather than an *initiator*. A downstream mediator can still be a good drug target, but the absence of genetic risk weakens the "human validation" argument that strengthens the best targets.

### Finding 8 — Counter-signal: type I IFN activity correlates with *less* fibrotic stages (Established)

A single-cell study of 108 IPF patients found ([PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/)): *"Type I interferon-activated myeloid states are associated with less fibrotic stages in idiopathic pulmonary fibrosis."* This directly complicates the hypothesis's IFN-driven rationale: if type I IFN activity marks *less* advanced fibrosis, then suppressing it might not help — or could even be counterproductive — in established disease.

### Finding 9 — Immunosuppression has harmed IPF patients; treatment effects are subgroup-specific (Established)

The PANTHER-IPF triple therapy (prednisone + azathioprine + N-acetylcysteine) increased hospitalization and death versus placebo ([PMID: 30290930](https://pubmed.ncbi.nlm.nih.gov/30290930/)): *"The widely used combination of prednisone, azathioprine, and N-acetylcysteine has now been associated with increased risk of hospitalization and death compared with placebo in patients with IPF."* Treatment effects are also genotype-dependent ([PMID: 26331942](https://pubmed.ncbi.nlm.nih.gov/26331942/)): *"NAC therapy was associated with a significant reduction in composite endpoint risk (hazard ratio, 0.14; 95% confidence interval, 0.02-0.83; P = 0.03) in those with a TT genotype."*

**Inference:** IPF has repeatedly punished broad immunomodulation, which raises the prior probability of net harm for any new immunomodulatory drug and strongly motivates biomarker-enriched patient selection rather than an all-comers trial.

### Finding 10 — Safety: cGAS-STING is a core antiviral sensor in an infection-prone population (Established, nuanced)

The cGAS-STING pathway is a core innate antiviral/antibacterial sensor ([PMID: 40697819](https://pubmed.ncbi.nlm.nih.gov/40697819/)): *"plays a pivotal role in defending against respiratory infections caused by viruses, bacteria, and mycobacteria."* Viral infections are recognized triggers of lethal acute exacerbation ([PMID: 42682877](https://pubmed.ncbi.nlm.nih.gov/42682877/)): *"Acute exacerbation of interstitial lung disease (AE-ILD) is often idiopathic, although viral infections are recognized precipitating factors."* The concern is tempered by a nationwide Japanese study finding AE-IPF incidence did not fall during the COVID-19 pandemic despite reduced respiratory infections ([PMID: 41253080](https://pubmed.ncbi.nlm.nih.gov/41253080/)): *"The findings of this study question the prior assumption that respiratory infections are key contributors to AE-IPF."*

**Inference:** Inhibiting a core antiviral sensor is a real but likely manageable liability — the risk is plausible but may be smaller than feared, and could be mitigated by intermittent dosing, inhaled lung-restricted delivery, and vaccination.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, staged model of where cGAS-STING sits in IPF pathobiology:

```
  UPSTREAM (IPF genetic risk)            cGAS-STING NODE               DOWNSTREAM
  ----------------------------           ----------------              -----------
  Telomere attrition (TERT/TERC)  --->   cytosolic self-DNA   --->   Type I IFN / ISGs
  DNA damage / DNA repair defects        sensing by cGAS              (JAK-STAT)
  MUC5B / host defense            --->   cGAMP --> STING      --->   SASP / NF-kB inflammation
  Aging, epithelial injury               (epithelium + macrophage)    --> fibroblast activation
                                                                      --> ECM deposition / fibrosis
  [Genetically validated]                [Active in tissue;          [JAK blockade = partial,
                                          NOT a genetic risk gene]    transient benefit]
```

**What the model says in favor of the hypothesis:** cGAS-STING is a convergence node downstream of the genetically validated upstream drivers (telomere/DNA-damage/senescence). It is physically present and activated in IPF lung, in both named compartments. It is sufficient to cause human lung fibrosis when constitutively switched on (SAVI). Blocking it — genetically or pharmacologically — reduces fibrosis in several animal models and in SSc. A proximal inhibitor (cGAS or STING) would, in principle, capture both the IFN-dependent and the IFN-independent STING outputs that a downstream JAK inhibitor misses.

**What the model says against the hypothesis:**
1. **Position matters.** cGAS-STING is a *mediator*, not an *initiator*; it is genetically downstream of the real IPF risk genes. Mediators can be redundantly bypassed (e.g., NLRP3, TGF-β, and other DNA-damage outputs run in parallel).
2. **Compartment mismatch.** The hypothesis emphasizes epithelium; the strongest functional data implicate macrophages, with a hard distal-lung delivery problem.
3. **Dissociability.** At least one UIP ex-vivo model shows pathway activation *without* a fibrotic consequence ([PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)).
4. **Direction of the IFN signal.** Type I IFN activity tracks with *less* fibrosis in patient single-cell data ([PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/)), undercutting the "IFN drives fibrosis" rationale.
5. **Downstream precedent is weak.** JAK inhibitors — the closest available surrogate — only transiently help even pure STING-driven lung disease.

**Net (Inference):** cGAS-STING is a legitimate, mechanistically supported node, but it is one node in a redundant, multi-compartment network, acting downstream of the disease's primary genetic drivers. This profile predicts *modest, subgroup-restricted* benefit rather than a transformative effect — which is precisely why patient enrichment and a mechanism-focused endpoint are essential.

---

## Evidence Base

| PMID | Role | What it shows | For / Against |
|------|------|---------------|---------------|
| [38944022](https://pubmed.ncbi.nlm.nih.gov/38944022/) | Human tissue | cGAS-pSTING in UIP epithelium + macrophages (44 cases) | **For** (mechanism active) |
| [34524912](https://pubmed.ncbi.nlm.nih.gov/34524912/) | Human tissue | cGAS in EpCAM+/p21+ senescent IPF epithelium | **For** (exact compartment) |
| [42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/) | Human genetics | STING1 GOF (SAVI) causes progressive ILD; IFN-independent arms | **For** (causal), caveat |
| [40731159](https://pubmed.ncbi.nlm.nih.gov/40731159/) | Human genetics | Confirms monogenic STING1 GOF → ILD; incomplete penetrance | **For** |
| [37806536](https://pubmed.ncbi.nlm.nih.gov/37806536/) | Animal | STING-KO/TREX1-KO + inhibitor reduce bleomycin fibrosis | **For** |
| [41948458](https://pubmed.ncbi.nlm.nih.gov/41948458/) | Animal | STING-/NLRP3-KO attenuate bleomycin fibrosis (oxid-mtDNA) | **For** |
| [40789441](https://pubmed.ncbi.nlm.nih.gov/40789441/) | Animal | cGAS inhibitors RU.521/G150 reduce fibrosis, improve survival; monocyte-driven | **For**, compartment caveat |
| [41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/) | Animal | Macrophage STING is critical driver; distal-lung delivery is the hurdle | **For** mechanism, **Against** easy translation |
| [42708359](https://pubmed.ncbi.nlm.nih.gov/42708359/) | Related disease | cGAS/STING suppression reverses SSc lung + skin fibrosis | **For** (transfer) |
| [40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/) | Human ex vivo | Pathway activated but no direct fibrosis effect in UIP model | **Against** (dissociable) |
| [42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/) | Human single-cell | Type I IFN myeloid states mark *less* fibrotic stages | **Against** (IFN rationale) |
| [42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/) | Human (SAVI) | JAK inhibitors only partial/transient; HSCT needed | **Against** (downstream weak) |
| [42722091](https://pubmed.ncbi.nlm.nih.gov/42722091/) | Trial (RA-ILD, NCT05246293) | Tofacitinib modest FVC effect, 92% AEs, 3 deaths | **Against** (safety/efficacy) |
| [30290930](https://pubmed.ncbi.nlm.nih.gov/30290930/) | Trial (PANTHER-IPF) | Immunosuppression increased death/hospitalization | **Against** (prior harm) |
| [26331942](https://pubmed.ncbi.nlm.nih.gov/26331942/) | Pharmacogenomics | TOLLIP genotype modifies NAC response | Supports **enrichment design** |
| [23583980](https://pubmed.ncbi.nlm.nih.gov/23583980/) | GWAS | IPF risk = telomere/host-defense; cGAS/STING absent | **Against** (not a risk gene) |
| [42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/) | GWAS replication | Same non-cGAS/STING loci across ancestries | **Against** |
| [40697819](https://pubmed.ncbi.nlm.nih.gov/40697819/) | Review | cGAS-STING is core antiviral/antibacterial sensor | **Against** (safety) |
| [42682877](https://pubmed.ncbi.nlm.nih.gov/42682877/) | Case | Viral infection triggers lethal AE-ILD | **Against** (safety) |
| [41253080](https://pubmed.ncbi.nlm.nih.gov/41253080/) | Epidemiology | AE-IPF unchanged in pandemic → infection may not dominate | Tempers safety concern |
| [40533265](https://pubmed.ncbi.nlm.nih.gov/40533265/) | Drug landscape | Clinical STING drugs are agonists (oncology), not inhibitors | Context (no asset ready) |

---

## Answers to the Four Questions

### 1. Is the mechanism active in this disease?
**Yes, by tissue and human genetics — but it is not a genetic risk gene, and activity may be subgroup-restricted.** cGAS-pSTING protein is present in IPF/UIP senescent epithelium and macrophages ([PMID: 38944022](https://pubmed.ncbi.nlm.nih.gov/38944022/), [34524912](https://pubmed.ncbi.nlm.nih.gov/34524912/)), and STING1 gain-of-function causes human ILD ([PMID: 42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/)). But CGAS/STING1 are absent from IPF GWAS loci ([PMID: 23583980](https://pubmed.ncbi.nlm.nih.gov/23583980/), [42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/)), placing the node genetically downstream. Activity is plausibly confined to a senescence-high / interferon-signature subgroup; the enrichment biomarker would be a cGAMP / ISG signature, though the counter-signal that IFN marks *less* fibrosis ([PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/)) means the right biomarker is not yet validated.

### 2. Does blocking it help?
**No human IPF trials exist.** Zero cGAS/STING-inhibitor trials in IPF or SSc (ClinicalTrials.gov v2, Nov 2026); clinical STING drugs are agonists for oncology ([PMID: 40533265](https://pubmed.ncbi.nlm.nih.gov/40533265/)). Same-pathway downstream drugs (JAK inhibitors) give only partial/transient benefit in STING-driven lung disease ([PMID: 42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/)) and modest, toxicity-laden effects in RA-ILD ([PMID: 42722091](https://pubmed.ncbi.nlm.nih.gov/42722091/)). In related disease (SSc), cGAS/STING suppression reverses lung fibrosis in models ([PMID: 42708359](https://pubmed.ncbi.nlm.nih.gov/42708359/)). Animal blockade (genetic + small-molecule) reduces bleomycin/paraquat fibrosis ([PMID: 37806536](https://pubmed.ncbi.nlm.nih.gov/37806536/), [41948458](https://pubmed.ncbi.nlm.nih.gov/41948458/), [40789441](https://pubmed.ncbi.nlm.nih.gov/40789441/)) — but with a contradicting ex-vivo UIP result ([PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)).

### 3. Reasons it might fail
Redundant parallel pathways (NLRP3, TGF-β, IFN-independent STING arms — [PMID: 41948458](https://pubmed.ncbi.nlm.nih.gov/41948458/), [42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/)); wrong cell compartment emphasis (macrophage >> epithelium — [PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)); wrong disease stage (IFN marks *less* fibrosis — [PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/); activation dissociable from fibrosis — [PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)); drug not reaching distal-lung target ([PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)); and FVC endpoints too insensitive for a modest, subgroup effect. **Safety:** blunting a core antiviral sensor in an exacerbation-prone population ([PMID: 40697819](https://pubmed.ncbi.nlm.nih.gov/40697819/), [42682877](https://pubmed.ncbi.nlm.nih.gov/42682877/)), against the backdrop of demonstrated immunosuppression harm in IPF ([PMID: 30290930](https://pubmed.ncbi.nlm.nih.gov/30290930/)).

### 4. Verdict
See the Verdict section below.

---

## Verdict

**Strength of the case (Inference): moderate — among the better-supported IPF repurposing hypotheses mechanistically, but unproven and with specific red flags.** The hypothesis rests on a genuinely strong triad: target present and activated in the right human tissue/cells, a human monogenic experiment-of-nature (SAVI) proving sufficiency, and reproducible fibrosis rescue by pathway blockade in animals and a related human disease. That is more than most repurposing candidates have. But the case is pulled down by five concrete counterweights: no human trial has ever been run; cGAS/STING are not IPF genetic-risk genes (downstream mediator, bypassable); the dominant functional compartment is the hard-to-reach distal-lung macrophage rather than the epithelium in the hypothesis; the IFN readout tracks with *less* fibrosis in patients; and the best available downstream surrogate (JAK inhibition) only transiently helps even pure STING-driven lung fibrosis, in a disease that has historically been harmed by immunosuppression.

**Single most efficient test (Inference):** A **biomarker-enriched, lung-targeted Phase 2a proof-of-mechanism trial.** Enroll IPF patients selected for a high baseline cGAS-STING / ISG signature (e.g., elevated cGAMP or blood/BAL interferon-stimulated genes) on stable antifibrotic background (pirfenidone or nintedanib). Deliver an **inhaled** cGAS or STING inhibitor to overcome the distal-lung delivery hurdle and limit systemic antiviral suppression. Make the **primary endpoint target engagement / ISG suppression in BAL or blood** (does the drug actually turn the pathway off in the lung?), with FVC slope, exacerbation rate, and a composite senescence/SASP biomarker as secondary readouts. This design directly tests the two things most likely to kill the hypothesis — delivery to the right compartment, and whether pathway suppression translates to a fibrotic signal — before committing to a large, insensitive FVC-powered trial. Pre-specify infection surveillance given the antiviral-sensor safety liability.

### Highest-weight identifiers (one line each)
- **[PMID: 42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/)** — SAVI: human STING1 gain-of-function causes progressive ILD (strongest causal human evidence *for*).
- **[PMID: 23583980](https://pubmed.ncbi.nlm.nih.gov/23583980/)** — IPF GWAS: risk is telomere/host-defense, not cGAS/STING (strongest genetic evidence *against* as a primary driver).
- **[PMID: 38944022](https://pubmed.ncbi.nlm.nih.gov/38944022/)** — cGAS-pSTING active in human UIP epithelium + macrophages (mechanism-is-active anchor).
- **[PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)** — Pathway activation dissociated from fibrosis in a human UIP model (key contradiction).
- **[PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)** — Macrophage STING is the critical driver; distal-lung delivery is the translational hurdle (compartment + delivery).
- **[PMID: 42708359](https://pubmed.ncbi.nlm.nih.gov/42708359/)** — cGAS/STING suppression reverses SSc lung fibrosis (best related-disease transfer).
- **[PMID: 42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/)** — JAK inhibitors only transiently control STING-driven lung fibrosis (downstream-precedent caution).
- **[PMID: 30290930](https://pubmed.ncbi.nlm.nih.gov/30290930/)** — PANTHER-IPF: immunosuppression harms IPF patients (prior-probability-of-harm anchor).
- **NCT05246293** — Phase II tofacitinib in RA-ILD: modest FVC effect, 92% AEs, 3 deaths ([PMID: 42722091](https://pubmed.ncbi.nlm.nih.gov/42722091/)).
- **ClinicalTrials.gov v2 (Nov 2026)** — Zero cGAS/STING-inhibitor trials in IPF or SSc (the central gap).

---

## Limitations and Knowledge Gaps

1. **No direct test exists.** The entire efficacy case for IPF is inferential — animal models, a related disease, and a downstream-pathway surrogate. No cGAS/STING inhibitor has been given to an IPF patient.
2. **Biomarker uncertainty.** The enrichment biomarker (cGAMP/ISG) is unvalidated, and one strong signal suggests IFN activity marks *less* fibrosis ([PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/)), so the "high-ISG = will respond" assumption may be wrong or even inverted.
3. **Model limitations.** Bleomycin and paraquat are acute-injury models that over-represent inflammation relative to the aging/senescence-driven human IPF; the one human-tissue (UIP slice) model showed *no* fibrosis effect ([PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/)).
4. **Compartment and delivery.** Whether epithelial or macrophage cGAS-STING matters more in humans is unresolved, and distal-lung delivery is unsolved ([PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)).
5. **Redundancy.** IFN-independent STING outputs and parallel pathways (NLRP3, TGF-β) could bypass inhibition ([PMID: 42741560](https://pubmed.ncbi.nlm.nih.gov/42741560/), [41948458](https://pubmed.ncbi.nlm.nih.gov/41948458/)).
6. **Stage.** All human tissue data are cross-sectional; whether the pathway *initiates*, *sustains*, or merely *marks* fibrosis cannot be determined.

## Proposed Follow-up Experiments / Actions

1. **Validate the enrichment biomarker first.** In banked IPF cohorts with longitudinal FVC, test whether a lung/blood cGAS-STING/ISG signature predicts *faster* progression. If it predicts slower progression (consistent with [PMID: 42627972](https://pubmed.ncbi.nlm.nih.gov/42627972/)), the hypothesis is in serious trouble before any drug is dosed.
2. **Human ex-vivo causal test.** Apply a cGAS and a STING inhibitor to IPF precision-cut lung slices and patient-derived epithelial/fibroblast/macrophage co-cultures; measure collagen/α-SMA, SASP, and ISGs. This directly addresses the dissociation seen in [PMID: 40882007](https://pubmed.ncbi.nlm.nih.gov/40882007/).
3. **Compartment dissection.** Use conditional (epithelium- vs macrophage-specific) cGAS/STING deletion in a senescence/telomere-driven (not just bleomycin) mouse model to resolve which compartment carries the fibrotic signal.
4. **Delivery solution.** Benchmark inhaled/nanoparticle cGAS or STING inhibitors for distal-lung macrophage engagement, building on the macrophage-targeted editing approach ([PMID: 41795185](https://pubmed.ncbi.nlm.nih.gov/41795185/)).
5. **The trial.** If (1)–(4) are favorable, run the biomarker-enriched, inhaled, antifibrotic-background Phase 2a described in the Verdict, with lung ISG suppression as the primary endpoint and pre-specified infection surveillance.

---

*This report distinguishes established findings (human tissue, human genetics, published experiments, trial registries) from labeled inference (my synthesis). All factual claims are cited to a primary source by PMID or trial identifier with a verbatim quote in the Key Findings and Evidence Base sections above.*


## Artifacts

- [OpenScientist final report](cgas_sting_inhibitor-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cgas_sting_inhibitor-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.
