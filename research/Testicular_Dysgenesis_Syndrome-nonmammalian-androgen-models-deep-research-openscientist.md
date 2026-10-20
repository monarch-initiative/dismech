---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T23:55:57.951898'
end_time: '2026-10-20T00:13:07.438385'
duration_seconds: 1029.49
template_file: templates/disease_nonmammalian_models_research.md
template_sha: "13f64a54d8d53e7eabcee8336fb164856c6fea48"
template_variables:
  disease_name: Testicular Dysgenesis Syndrome
  mondo_id: MONDO:0005437
  category: Complex
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
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Testicular_Dysgenesis_Syndrome-nonmammalian-androgen-models-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Testicular_Dysgenesis_Syndrome-nonmammalian-androgen-models-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Non-Mammalian Model Discovery Template

## Target Disease
- **Disease Name:** Testicular Dysgenesis Syndrome
- **MONDO ID:** MONDO:0005437

## Scope — Read This First

This is **not** a request for a general account of this disease. The disease's
pathophysiology and clinical features are already curated. The single question
is narrow:

> **Which non-mammalian animal models of androgen signalling in male
> reproductive development exist, and which of this disease's mechanism nodes
> could any of them legitimately support?**

"Non-mammalian" means teleost fish, elasmobranchs, amphibians, reptiles, birds,
and invertebrates with an androgen-receptor-like system. Mammalian models
(rodent, lagomorph, ungulate, primate, marsupial) are **out of scope** and a
report that returns them has failed this brief.

## What Is Already Curated — Do Not Re-Derive Any Of It

The record already carries exactly three animal models, all mammalian:

1. **Gestational di(n-butyl) phthalate (DBP) rat** (Wistar; PMID:28352662) —
   window-specific suppression of fetal testicular testosterone; shortened
   anogenital distance, focal testicular dysgenesis, cryptorchidism,
   hypospadias, compensated adult Leydig cell failure.
2. **Gestational flutamide rat** (Sprague-Dawley and Wistar; PMID:15788718) —
   androgen receptor blockade, separating receptor-level action from
   steroidogenesis; hypospadias, vaginal pouch, cleft prepuce, missing prostate
   lobes, tissue-selective by gestational day.
3. **Rxfp2 D294G missense mouse** (PMID:20963592) — partial loss of INSL3
   receptor trafficking; cryptorchidism with spermatogenic failure.

Do not restate, re-justify, or re-report these. Do not report that the disease's
models are predominantly rodent — that is the premise of the question, not a
finding.

## The Mechanism Nodes To Map Against

The record's causal graph has these eleven nodes. Any model you propose must be
mapped to one or more of them **by name**, exactly as written here:

1. Common Early Disruption of Testis Lineage Specification *(cellular scale: an
   early disturbance of fetal testis set-up at the level of somatic cell lineage
   specification — Leydig and Sertoli — which independently produces Leydig
   failure, Sertoli dysfunction and the focal dysgenetic lesion)*
2. Focal Testicular Dysgenesis
3. Fetal Leydig Cell Dysfunction
4. Deficient Androgen Action in the Masculinization Programming Window
   *(molecular scale: insufficient androgen receptor signalling, GO:0030521, in
   reproductive tract target tissues during a discrete fetal window — rat
   embryonic day 15.5–18.5; postulated human equivalent 8–14 weeks gestation)*
5. Incomplete Reproductive Tract Masculinization *(organism scale:
   under-virilisation — hypospadias, altered penile length, reduced ventral
   prostate and seminal vesicle size)*
6. Impaired INSL3-RXFP2 Signalling at the Gubernaculum
7. Failure of Trans-abdominal Testicular Descent
8. Sertoli Cell Dysfunction
9. Arrested Gonocyte Differentiation
10. Germ Cell Neoplasia In Situ
11. Invasive Testicular Germ Cell Tumour

The three nodes of greatest interest are **1, 4 and 5**.

## The Homology Problem — Address It Directly, Do Not Evade It

Several of these nodes are defined in mammal-specific terms. The gubernaculum,
prostate, seminal vesicle, penile urethra, anogenital distance and
trans-abdominal descent have no counterpart outside mammals. Node 4 is pinned to
a fetal programming window that may have no analogue in a taxon with
indeterminate or environmentally labile gonadal sex.

Therefore, for **every** model you propose, state which of these it is:

- **(a) Recapitulates** the node: the same lesion in a homologous structure or a
  conserved molecular step.
- **(b) Perturbs** the node: the manipulation acts on the node's named molecular
  step (e.g. androgen receptor signalling) without reproducing the mammalian
  structural outcome.
- **(c) Informative by analogy only**: the model speaks to androgen biology but
  the node's defining feature is absent in that taxon. Say what is absent.
- **(d) Fails to recapitulate**: the model has been tested against this
  biology and does not reproduce it. A documented negative is a valuable
  result — report it.

A report that proposes a fish model for "Incomplete Reproductive Tract
Masculinization" without stating that fish have no prostate, seminal vesicle or
penile urethra has failed this brief.

## Systems To Cover

Cover each of the following. Say explicitly where a system has nothing to offer
— an empty system is a useful result, not a gap in the report.

- **Teleost androgen receptor genetics.** Zebrafish `ar` mutants; medaka `ar`
  mutants; tilapia. Critically: does loss of AR prevent testis formation at all,
  or only later androgen-dependent features? This distinction decides whether
  such a model touches node 1 or only node 4.
- **Teleost somatic gonad lineage specification.** `gsdf`, `dmrt1` (and medaka
  `dmy`/`dmrt1bY`), `amh`, `sox9`, `nr5a1`/`ff1`, `wt1`, `foxl2`, `cyp17a1`,
  `cyp11c1`. Which mutants produce a disorganised or mixed-lineage gonad rather
  than clean sex reversal? A mixed-lineage lesion is the closest non-mammalian
  analogue of focal dysgenesis and is of specific interest.
- **Androgen-dependent structures used as regulatory assays.** Three-spined
  stickleback spiggin; medaka anal-fin papillary processes; fathead minnow
  nuptial tubercles; poeciliid gonopodium (*Gambusia*, *Poecilia*). Give the
  OECD test guideline number where one exists.
- **Elasmobranch claspers.** Androgen dependence of clasper development, if
  primary literature exists.
- **Amphibian.** *Xenopus laevis* and *tropicalis* androgen receptor function;
  AR knockout or knockdown if any exists; nuptial pads and larynx; OECD LAGDA
  (TG 241) and what it detects about androgen-axis disruption.
- **Reptilian.** American alligator — the Lake Apopka and related work on
  phallus size, plasma testosterone and gonad morphology; controlled in-ovo
  exposure studies. Distinguish controlled models from correlational
  contaminated-population studies, which are a different grade of evidence.
- **Avian.** Androgen dependence, or independence, of phallus development,
  including the chicken-versus-duck phallus reduction work and BMP signalling;
  in-ovo exposure models in quail and chicken. Note that birds are
  female-heterogametic and that avian gonadal sex is not androgen-programmed in
  the mammalian way.
- **Endocrine-disrupting chemical exposure in non-mammals.** Where testis-ova or
  intersex gonads are reported in fish, state whether the mechanism was traced
  to somatic lineage specification or only to circulating steroid levels. Only
  the former is relevant to node 1.
- **Conserved developmental windows.** Does any non-mammalian taxon have a
  described discrete window of androgen-dependent or gonadal-sex lability, and
  how does it compare conceptually to the mammalian masculinization programming
  window? This is the crux of whether node 4 can take a non-mammalian model at
  all.

## Output Required Per Candidate Model

- Species (scientific and common name), and the line, allele or exposure
- Category: genetic model, controlled exposure model, or wild-population study
- A short description of what the model is and what it shows
- The mechanism node(s) it maps to, named exactly as listed above
- Its classification as (a), (b), (c) or (d) above, with the reason
- The primary publication as a **PMID**
- At least one **exact verbatim quote** from the abstract or text supporting the
  key claim, with the article's exact title. Quotes are machine-validated
  against the source after this report is returned: a paraphrase presented as a
  quote, or a PMID that does not resolve, is a hard failure.
- What the model does **not** show, and the species difference that limits it

## Evidence Discipline

- Every PMID must resolve and must be the paper you mean. Give its exact title.
- Never present a paraphrase as a quote.
- Do not claim a model or a finding does not exist on the strength of an
  unsuccessful search. Say what you searched and what you found.
- Where the androgen biology of a taxon is genuinely not conserved with the
  mammalian pathway, say so plainly. A short report that correctly rules most
  candidates out is more useful than a long one that stretches homology.


## Output

# Non-Mammalian Animal Models of Androgen Signalling in Male Reproductive Development: Mapping onto the Testicular Dysgenesis Syndrome Causal Graph

**Target disease:** Testicular Dysgenesis Syndrome (TDS) — MONDO:0005437
**Question:** Which non-mammalian animal models of androgen signalling in male reproductive development exist, and which of this disease's eleven mechanism nodes could any of them legitimately support?

---

## Summary

Non-mammalian models of androgen signalling in male reproductive development **do exist and are mechanistically informative, but they converge almost entirely on a single node of the TDS causal graph: Node 4, "Deficient Androgen Action in the Masculinization Programming Window."** Across teleost fish (zebrafish, medaka, fathead minnow, guppy, stickleback), one elasmobranch (little skate), one amphibian (*Xenopus*), one reptile (American alligator), birds, and decapod invertebrates, the recurring and defensible mapping is classification **(b): these models *perturb* the named molecular step of Node 4 — androgen-receptor (AR) signalling, GO:0030521 — without *recapitulating* the mammalian structural outcome.** No non-mammalian model recapitulates the disease. The reason is structural and developmental, not a gap in the literature: the fetal masculinization programming window itself (rat E15.5–18.5; human ~8–14 weeks) has **no non-mammalian analogue**, because the discrete developmental windows that do exist in fish and reptiles govern *gonadal sex determination* via temperature and estrogen/aromatase, not *androgen programming of reproductive-tract target tissues* after gonadal sex is already fixed.

The three nodes of greatest interest behave as follows. **Node 4** can take a non-mammalian model only as a *perturbation* (b), never a recapitulation — the molecular step (AR signalling) is deeply conserved, but the window that defines the node is absent. **Node 1** (Common Early Disruption of Testis Lineage Specification) has **no non-mammalian model**: teleost somatic-lineage mutants give *clean sex reversal* or *germ-cell* phenotypes, not the mixed-lineage focal dysgenesis that defines the mammalian lesion; and fish intersex from endocrine disruptors is *estrogen-driven tissue feminization*, not a Sertoli/Leydig specification defect. **Node 5** (Incomplete Reproductive Tract Masculinization) is reachable *only by analogy* (c), because no non-mammalian taxon possesses a prostate, seminal vesicle, or penile urethra; and the avian phallus provides a documented *androgen-independent* (Bmp4-driven) negative. Nodes 2, 3, 6, 7, 8, 9, 10 and 11 are either reachable only as distant teleost analogues (Node 3) or have no non-mammalian model at all (Nodes 2, 6, 7, 10, 11).

A separate, clean negative applies to **invertebrates**: the brief's category of "invertebrates with an androgen-receptor-like system" is essentially empty, because the crustacean "androgenic gland" masculinizer is an insulin-like peptide (IAG) acting through a receptor tyrosine kinase — a *nominal*, not *molecular*, homologue of the vertebrate nuclear androgen receptor. There is therefore no invertebrate AR model for Node 4.

---

## Key Findings

### Node 4 — Perturbation models (classification b)

#### F001. Teleost androgen receptor knockouts: AR perturbs androgen action but does not block testis lineage specification

Two independent zebrafish (*Danio rerio*) *ar*-null lines settle the single most decisive question in the brief: does loss of AR prevent testis *formation*, or only later androgen-dependent *features*? The answer is the latter, which places teleost AR models at Node 4 and explicitly **not** at Node 1.

In the Crowder/Gorelick line ([PMID: 29272351](https://pubmed.ncbi.nlm.nih.gov/29272351/)), the majority of *ar*−/− animals develop ovaries, and the minority that form testes show **structurally disorganized testes and impaired sperm release** — i.e., when a testis does form, its androgen-dependent somatic architecture and output fail, yet a testis *lineage* can still be specified. In the Tang et al. line ([PMID: 29228103](https://pubmed.ncbi.nlm.nih.gov/29228103/)), *ar*−/− males have smaller testes and are largely infertile, but **still produce some mature spermatozoa capable of IVF**, with elevated steroidogenic gene expression and reduced 11-ketotestosterone — the signature of lost androgen-dependent amplification rather than primary lineage failure.

> "The small percentage of mutants that developed testes displayed female secondary sexual characteristics, exhibited structurally disorganized testes, and were unable to release or produce normal levels of sperm, demonstrating that AR is necessary for zebrafish testis development and fertility." — *Nuclear Androgen Receptor Regulates Testes Organization and Oocyte Maturation in Zebrafish* ([PMID: 29272351](https://pubmed.ncbi.nlm.nih.gov/29272351/))

> "Homozygous ar mutant male fish with smaller testis size were found to be infertile when tested by natural mating. Intriguingly, a small amount of mature spermatozoa was observed in the ar mutant fish." — *Fertility impairment with defective spermatogenesis and steroidogenesis in male zebrafish lacking androgen receptor* ([PMID: 29228103](https://pubmed.ncbi.nlm.nih.gov/29228103/))

**Mapping:** Node 4 (Deficient Androgen Action), classification **(b)**. **What it does not show:** It does not reproduce the fetal masculinization *window*, nor any reproductive-tract structure (Node 5), because zebrafish lack a prostate, seminal vesicle and penile urethra, and sex determination here is polygenic/labile rather than driven by an androgen-programmed fetal window.

#### F010. Medaka *scl* (cyp17a1/P450c17) mutant: steroidogenic androgen deficiency with an intact receptor — teleost analogue of Nodes 3/4

The recessive medaka (*Oryzias latipes*) *scl* ("sex character-less") mutant ([PMID: 18393567](https://pubmed.ncbi.nlm.nih.gov/18393567/)) carries a loss-of-function mutation in P450c17 (*cyp17a1*), the steroidogenic enzyme required to synthesize androgen and estrogen. Both XX and XY mutants form gonads containing spermatozoa but develop **neither male nor female secondary sex characters**; critically, androgen administration *restores* male papillary processes, proving the AR is functional and the lesion lies upstream in steroid synthesis. This is the teleost parallel of the flutamide-vs-DBP distinction already curated in the rat models: it separates *steroidogenic* (Leydig-type) failure from *receptor-level* action.

> "Because papillary processes, a male secondary sex character, were induced in the XY mutants by androgen administration, it seems that the androgen receptor is functioning normally. We found a loss-of-function type mutation in the P450c17 gene of the mutant" — *The novel mutant scl of the medaka fish, Oryzias latipes, shows no secondary sex characters* ([PMID: 18393567](https://pubmed.ncbi.nlm.nih.gov/18393567/))

**Mapping:** Node 3 (Fetal Leydig Cell Dysfunction, by analogy to steroidogenic failure) and Node 4 (androgen action), classification **(b)**. **What it does not show:** No reproductive-tract masculinization lesion (Node 5) and no fetal programming window; the phenotype is read out on fish secondary sex characters.

#### F005 & F011. Androgen-dependent secondary-sex structures as validated AR-signalling readouts

Three teleost structures function as quantitative in-vivo assays of AR signalling, and each is a Node-4 perturbation by analogy:

- **Fathead minnow (*Pimephales promelas*) nuptial tubercles** ([PMID: 15597888](https://pubmed.ncbi.nlm.nih.gov/15597888/)): the AR agonist 17β-trenbolone induces male-type tubercles in females, and the AR antagonist flutamide blocks this, demonstrating an AR-receptor-mediated response in vivo. This endpoint is used in the **OECD Fish Short-Term Reproduction Assay (TG 229)** as the secondary sex characteristic measure.
- **Medaka anal-fin papillary processes** ([PMID: 24248458](https://pubmed.ncbi.nlm.nih.gov/24248458/)): androgen-dependent via Bmp7/Lef1 downstream of AR; induced by methyltestosterone and suppressed by flutamide.
- **Guppy (*Poecilia reticulata*) gonopodium** ([PMID: 37677862](https://pubmed.ncbi.nlm.nih.gov/37677862/)): 17β-trenbolone masculinizes female anal/caudal fins, docks to guppy AR, upregulates TGFβ/BMP and Wnt pathways, and the effect is blocked by flutamide. The gonopodium is the poeciliid intromittent organ, so this is AR-driven development of an *internal-fertilization* organ — mechanistically analogous to the skate clasper.

> "the anti-androgen effectively blocked trenbolone-induced masculinization (nuptial tubercle production) of female fathead minnows, indicating antagonism of an AR receptor-mediated response in vivo" — *Evaluation of the model anti-androgen flutamide for assessing the mechanistic basis of responses to an androgen in the fathead minnow (Pimephales promelas)* ([PMID: 15597888](https://pubmed.ncbi.nlm.nih.gov/15597888/))

> "Development of papillary processes concomitant with the induction of Bmp7 and Lef1 in the distal bone nodules by exposure to methyltestosterone was significantly suppressed by an antiandrogen, flutamide, in female medaka." — *Bmp7 and Lef1 are the downstream effectors of androgen signaling in androgen-induced sex characteristics development in medaka* ([PMID: 24248458](https://pubmed.ncbi.nlm.nih.gov/24248458/))

> "17β-trenbolone-induced masculinization of caudal and anal fins in female guppies, concomitant to the upregulated expression of differentially expressed genes involved in the above-mentioned two signaling pathways, was significantly inhibited by flutamide (androgen receptor antagonist)" — *17β-Trenbolone activates androgen receptor, upregulates transforming growth factor beta/bone morphogenetic protein and Wnt signaling pathways, and induces masculinization of caudal and anal fins in female guppies (Poecilia reticulata)* ([PMID: 37677862](https://pubmed.ncbi.nlm.nih.gov/37677862/))

**Mapping:** Node 4, classification **(b)**. **What they do not show:** None is a reproductive-tract structure homologous to human genitalia; they are fish-specific secondary sex characters. They index AR *activation/antagonism*, not a dysgenetic or window-specific programming lesion.

A fourth structure, the **three-spined stickleback (*Gasterosteus aculeatus*) spiggin**, is the only teleost androgen *and anti-androgen* biomarker with a quantifiable ELISA endpoint ([PMID: 17975538](https://pubmed.ncbi.nlm.nih.gov/17975538/); [PMID: 17627896](https://pubmed.ncbi.nlm.nih.gov/17627896/)), underpinning the stickleback androgenised-female / spiggin assay (OECD Guidance Document 148). It too is a Node-4 readout by analogy.

#### F002. Elasmobranch clasper: AR directly drives a male copulatory organ via Shh/Hand2

In the little skate (*Leucoraja erinacea*), O'Shaughnessy, Dahn & Cohn ([PMID: 25868783](https://pubmed.ncbi.nlm.nih.gov/25868783/)) showed that Shh signalling is necessary for male clasper development and sufficient to induce clasper cartilage in females, and that **AR controls the male-specific Shh pattern by regulating Hand2 through a directly-bound androgen response element (ARE).** This is a mechanistically resolved, AR-dependent masculinization of an external copulatory structure in a non-mammalian vertebrate — the deepest molecular dissection of AR-driven external-genital patterning outside mammals.

> "Androgen receptor (AR) controls the male-specific pattern of Shh in pelvic fins by regulation of Hand2. We identify an androgen response element (ARE) in the Hand2 locus and present biochemical evidence that AR can directly bind the Hand2 ARE." — *Molecular development of chondrichthyan claspers and the evolution of copulatory organs* ([PMID: 25868783](https://pubmed.ncbi.nlm.nih.gov/25868783/))

**Mapping:** Node 4, classification **(b)** (direct AR molecular action); informative toward Node 5 **only by analogy (c)**. **What it does not show:** The clasper is a cartilaginous pelvic-fin derivative, not a urethra-bearing phallus, prostate or seminal vesicle; there is no fetal androgen-programming window in the mammalian sense.

---

### Node 1 — No non-mammalian model (clean negatives)

#### F004. Teleost somatic-lineage mutants give sex reversal or germ-cell phenotypes, not focal dysgenesis

The brief flagged mixed-lineage gonads as the closest possible non-mammalian analogue of focal testicular dysgenesis. The genetics do not deliver one. In medaka, *dmrt1* loss ([PMID: 22187367](https://pubmed.ncbi.nlm.nih.gov/22187367/)) produces XY gonads that first form a **normal testis** and then **transdifferentiate wholesale into an ovary** — a clean, complete male-to-female reversal, not a disorganized mixed-lineage gonad. In *Oryzias hubbsi*, *gsdf* knockout ([PMID: 38870865](https://pubmed.ncbi.nlm.nih.gov/38870865/)) causes **no sex reversal at all**, instead producing germ-cell overproliferation and accelerated meiosis — a germ-cell, not somatic-lineage, phenotype. Neither reproduces the coexistence of mis-specified Sertoli/Leydig lineages with seminiferous-cord disorganization that defines mammalian focal dysgenesis.

> "the XY mutant gonads first developed into the normal testis type. However, the gonads transdifferentiated into the ovary type." — *Dmrt1 mutation causes a male-to-female sex reversal after the sex determination by Dmy in the medaka* ([PMID: 22187367](https://pubmed.ncbi.nlm.nih.gov/22187367/))

> "histological analyses revealed no male-to-female sex reversal in Gsdf-knockout fish, contrary to findings in other medaka species" — *Gsdf is not indispensable for male differentiation in the medaka species Oryzias hubbsi* ([PMID: 38870865](https://pubmed.ncbi.nlm.nih.gov/38870865/))

**Mapping:** Tested against Node 1/Node 2; classification **(d) fails to recapitulate.** **Species difference:** teleost sex determination is switch-like (master genes *dmy*/*dmrt1bY*, *gsdf*, *amhy*) and labile, producing binary fate flips rather than the partial, focal, mixed-lineage dysgenesis of the mammalian fetal testis.

#### F006. Fish intersex/testis-ova is estrogen-driven feminization, not a lineage-specification defect

Where intersex gonads are reported in wild fish, the mechanism traces to **estrogenic drive**, not to a somatic testis-lineage specification error. In wild roach (*Rutilus rutilus*), estrogenic wastewater activity is established as the main driver of feminized phenotypes, with elevated male plasma vitellogenin ([PMID: 37595157](https://pubmed.ncbi.nlm.nih.gov/37595157/)), and genetic-sex-marker work shows intersex arises from feminization of genetic *males* by oestrogen ([PMID: 32293100](https://pubmed.ncbi.nlm.nih.gov/32293100/)). The lesion is an estrogen-receptor / germ-cell feminization, not a Sertoli/Leydig set-up failure.

> "Estrogenic activity emanating from wastewater treatment works (WwTW) has been conclusively demonstrated to be the main driver of these feminized phenotypes." — *Endocrine Disruption Is Reduced but Still Widespread in Wild Roach* ([PMID: 37595157](https://pubmed.ncbi.nlm.nih.gov/37595157/))

**Mapping:** Tested against Node 1; classification **(d)/not relevant** — the mechanism is circulating estrogen, not somatic lineage specification. Only a lineage-specification mechanism would be relevant to Node 1, and none is demonstrated.

---

### Node 5 — Analogy only, plus a documented androgen-independent negative

#### F003. Avian phallus reduction is androgen-INDEPENDENT (Bmp4-driven apoptosis)

Birds provide an important negative control for Node 5. In galliform birds the genital tubercle begins to develop and then regresses by **Bmp4-induced apoptosis**; inhibiting Bmp signalling rescues the tubercle, and activating Bmp4 in duck induces galliform-like apoptosis ([PMID: 23746636](https://pubmed.ncbi.nlm.nih.gov/23746636/)). Phallus reduction here is driven by *de novo* programmed cell death, **not** by loss of androgen-dependent outgrowth. Combined with birds being female-heterogametic (ZZ/ZW) and avian gonadal sex not being androgen-programmed in the mammalian way, avian phallus biology does not model androgen-deficient under-virilisation.

> "evolutionary reduction of the intromittent phallus in galliform birds occurred not by disruption of outgrowth signals but by de novo activation of cell death by Bmp4 in the genital tubercle" — *Developmental basis of phallus reduction during bird evolution* ([PMID: 23746636](https://pubmed.ncbi.nlm.nih.gov/23746636/))

**Mapping:** Tested against Node 5; classification **(d) fails to recapitulate** — the mechanism is explicitly not androgen-dependent.

#### F007. American alligator: phallus is androgen-responsive by analogy, but gonadal sex is temperature/estrogen-determined, and controlled exposure did not reproduce the correlational phallus reduction

The American alligator (*Alligator mississippiensis*) illustrates the gulf between correlational wild-population evidence and controlled models. **Wild-population/correlational:** juvenile alligators from contaminated Lake Apopka have smaller phalluses and altered plasma steroids ([PMID: 10603274](https://pubmed.ncbi.nlm.nih.gov/10603274/)). **Controlled in-ovo exposure:** topical egg exposure to the antiandrogenic/estrogenic metabolite p,p′-DDE skewed sex ratio female but did **not** alter plasma testosterone, aromatase, oviduct epithelium or phallus morphology ([PMID: 16112671](https://pubmed.ncbi.nlm.nih.gov/16112671/)); and embryonic estradiol (not androgen deficiency) recapitulated Apopka ovarian transcriptomes ([PMID: 30010799](https://pubmed.ncbi.nlm.nih.gov/30010799/)). Alligator gonadal sex is temperature-dependent, not androgen-programmed.

> "Both p,p'-DDE and E(2) failed to influence plasma T, gonadal aromatase activity, oviductal ECH, and phallus morphology at the concentrations used." — *Developmental alterations as a result of in ovo exposure to the pesticide metabolite p,p'-DDE in Alligator mississippiensis* ([PMID: 16112671](https://pubmed.ncbi.nlm.nih.gov/16112671/))

> "Phallus size was significantly smaller in males from lakes Griffin and Apopka when compared to males from Lake Woodruff NWR." — *Plasma steroid concentrations and male phallus size in juvenile alligators from seven Florida lakes* ([PMID: 10603274](https://pubmed.ncbi.nlm.nih.gov/10603274/))

**Mapping:** Node 5 **by analogy only (c)** for the androgen-responsive phallus; the controlled model is a **(d)** negative for reproducing the correlational phallus endpoint. **Species difference:** temperature-dependent sex determination; no fetal androgen-programming window; the reproductive-abnormality signal in the contaminated population is estrogen-driven.

---

### Invertebrates — the category is empty

#### F008. Invertebrate "androgenic" masculinization uses a peptide (IAG)/insulin-receptor axis, not a nuclear androgen receptor

In decapod crustaceans the androgenic gland secretes the insulin-like androgenic gland hormone (IAG); IAG drives masculinization and its loss causes feminization, acting through an insulin-like receptor ([PMID: 33013714](https://pubmed.ncbi.nlm.nih.gov/33013714/); [PMID: 26677879](https://pubmed.ncbi.nlm.nih.gov/26677879/)). This is a peptide / receptor-tyrosine-kinase axis, mechanistically **unrelated** to the vertebrate nuclear androgen receptor (GO:0030521) that defines Node 4. The brief's category of "invertebrates with an androgen-receptor-like system" is therefore essentially unfilled: the crustacean "androgenic gland" is a *nominal*, not *molecular*, homologue.

> "IAG expression induces masculinization, while the absence of the AG or a deficiency in IAG expression results in feminization." — *The "IAG-Switch"-A Key Controlling Element in Decapod Crustacean Sex Differentiation* ([PMID: 33013714](https://pubmed.ncbi.nlm.nih.gov/33013714/))

**Mapping:** No mapping to any node; classification **(d)/not applicable** — wrong molecular pathway.

---

### The crux — conserved developmental windows

#### F009. Non-mammalian "windows" are gonadal-sex-determination windows, not androgen-programming windows

This finding decides whether Node 4 can take a non-mammalian model *as a recapitulation* — and the answer is no. Discrete developmental windows do exist in non-mammals, but they govern **gonadal fate**, not androgen programming of reproductive-tract targets. In medaka, thermal sex manipulation is effective only before embryonic stage 36, showing gonadal fate is fixed early ([PMID: 18391524](https://pubmed.ncbi.nlm.nih.gov/18391524/)). In three-spined stickleback, a defined critical period of sexual differentiation underlies the spiggin assay ([PMID: 17975538](https://pubmed.ncbi.nlm.nih.gov/17975538/)). Alligator gonadal sex is temperature-dependent ([PMID: 16112671](https://pubmed.ncbi.nlm.nih.gov/16112671/)). These windows are controlled by temperature and aromatase/estrogen and determine whether a gonad becomes testis or ovary — conceptually distinct from the mammalian masculinization programming window (rat E15.5–18.5), which is a window of *androgen action on tract target tissues after gonadal sex is already fixed*.

> "Thermal manipulation of sex was ineffective after stage 36, indicating that gonadal fate in medaka is determined considerably earlier than histological differentiation" — *Temperature-dependent sex determination in Hd-rR medaka Oryzias latipes: gender sensitivity, thermal threshold, critical period, and DMRT1 expression profile* ([PMID: 18391524](https://pubmed.ncbi.nlm.nih.gov/18391524/))

**Mapping:** The defining *window* feature of Node 4 has no clean non-mammalian analogue; classification **(c) informative by analogy only** at best — what is absent is the post-sex-determination androgen-programming window acting on tract tissues.

---

## Mechanistic Model / Interpretation

The TDS causal graph is vertical: an early somatic-lineage disturbance (Node 1) propagates down through Leydig/Sertoli dysfunction (Nodes 3, 8) and the focal dysgenetic lesion (Node 2) to deficient androgen action in a discrete fetal window (Node 4), producing under-virilisation of mammal-specific tract structures (Node 5), and in parallel a germ-cell axis (Nodes 9–11) and an INSL3–gubernaculum–descent axis (Nodes 6–7). Non-mammalian models attach to this graph at exactly one rung.

```
TDS CAUSAL GRAPH                       NON-MAMMALIAN MODEL COVERAGE
--------------------------------       -------------------------------------------
[1] Early lineage disruption   <----   NONE. dmrt1 = clean reversal; gsdf = germ-cell;
    (Leydig + Sertoli)                  fish intersex = estrogenic. (d)/not relevant
        |
[2] Focal testicular dysgenesis <---   NONE. No mixed-lineage teleost lesion. (d)
        |
[3] Fetal Leydig dysfunction   <----   medaka scl (cyp17a1): steroidogenic loss. (b), analogy
        |
[8] Sertoli dysfunction        <----   zebrafish ar-/- disorganized testis (indirect). (b)
        |
[4] DEFICIENT ANDROGEN ACTION  <====   **CONVERGENCE ZONE** — all AR models here:
    (AR signalling, fetal window)       zebrafish/teleost ar-null, fathead minnow
        |                               tubercles (TG 229), medaka papillary processes,
        |                               guppy gonopodium, stickleback spiggin (GD 148),
        |                               medaka scl, skate clasper, Xenopus larynx/LAGDA
        |                               (TG 241). ALL classification (b) — perturb, never
        |                               recapitulate. Window itself = no analogue (c).
        |
[5] Incomplete tract           <----   ANALOGY ONLY (c): no prostate/sem.vesicle/urethra.
    masculinization                     Alligator phallus (c, correlational); avian
        |                               phallus = androgen-INDEPENDENT, Bmp4 (d negative).
        |
[6] INSL3-RXFP2 gubernaculum   <----   NONE (no gubernaculum outside mammals).
[7] Trans-abdominal descent    <----   NONE (no trans-abdominal descent).
[9] Arrested gonocyte diff.    <----   NONE mapped.
[10] GCNIS                     <----   NONE.
[11] Invasive TGCT             <----   NONE.
```

The unifying principle is a **conserved molecule in a non-conserved anatomy and timeline.** The nuclear androgen receptor and its downstream effectors (Shh/Hand2 in skate; Bmp7/Lef1 in medaka; TGFβ/BMP/Wnt in guppy) are ancient and shared, so any assay that reads AR *activation* or *antagonism* legitimately perturbs Node 4's molecular step. But the node is not merely "AR signalling" — it is AR signalling *in reproductive-tract target tissues during a discrete fetal window after gonadal sex is fixed*. That compound definition fails outside mammals on two counts: the tract targets (prostate, seminal vesicle, penile urethra, gubernaculum) do not exist, and the fetal window does not exist because non-mammalian "windows" set gonadal sex itself, upstream, via temperature and estrogen.

### Classification summary table

| Model (species, line/exposure) | Category | Node(s) | Class | Primary PMID |
|---|---|---|---|---|
| Zebrafish *ar*−/− (Crowder/Gorelick) | genetic | 4 (8 indirect) | (b) | [29272351](https://pubmed.ncbi.nlm.nih.gov/29272351/) |
| Zebrafish *ar*−/− (Tang et al.) | genetic | 4 | (b) | [29228103](https://pubmed.ncbi.nlm.nih.gov/29228103/) |
| Medaka *scl* (*cyp17a1*) | genetic | 3, 4 | (b) | [18393567](https://pubmed.ncbi.nlm.nih.gov/18393567/) |
| Fathead minnow nuptial tubercles (trenbolone±flutamide) | exposure | 4 | (b) | [15597888](https://pubmed.ncbi.nlm.nih.gov/15597888/) |
| Medaka anal-fin papillary processes | exposure | 4 | (b) | [24248458](https://pubmed.ncbi.nlm.nih.gov/24248458/) |
| Guppy gonopodium (trenbolone±flutamide) | exposure | 4 | (b) | [37677862](https://pubmed.ncbi.nlm.nih.gov/37677862/) |
| Stickleback spiggin assay | exposure | 4 | (b) | [17975538](https://pubmed.ncbi.nlm.nih.gov/17975538/) |
| Little skate clasper (Shh/Hand2/AR) | genetic/molecular | 4; 5 (analogy) | (b)/(c) | [25868783](https://pubmed.ncbi.nlm.nih.gov/25868783/) |
| Medaka *dmrt1* | genetic | 1/2 tested | (d) | [22187367](https://pubmed.ncbi.nlm.nih.gov/22187367/) |
| *O. hubbsi gsdf* KO | genetic | 1/2 tested | (d) | [38870865](https://pubmed.ncbi.nlm.nih.gov/38870865/) |
| Wild roach intersex | wild-population | 1 tested | (d)/n.r. | [37595157](https://pubmed.ncbi.nlm.nih.gov/37595157/); [32293100](https://pubmed.ncbi.nlm.nih.gov/32293100/) |
| Galliform phallus (Bmp4) | genetic/developmental | 5 tested | (d) | [23746636](https://pubmed.ncbi.nlm.nih.gov/23746636/) |
| Alligator phallus (Lake Apopka) | wild-population | 5 | (c) | [10603274](https://pubmed.ncbi.nlm.nih.gov/10603274/) |
| Alligator in-ovo p,p′-DDE | controlled exposure | 5 tested | (d) | [16112671](https://pubmed.ncbi.nlm.nih.gov/16112671/) |
| Crustacean androgenic gland (IAG) | genetic/physiological | none | (d)/n.a. | [33013714](https://pubmed.ncbi.nlm.nih.gov/33013714/) |

---

## Evidence Base

**Teleost AR genetics (Node 4 vs Node 1 distinction).** The two zebrafish *ar*-null papers ([PMID: 29272351](https://pubmed.ncbi.nlm.nih.gov/29272351/); [PMID: 29228103](https://pubmed.ncbi.nlm.nih.gov/29228103/)) are the load-bearing evidence that AR loss disorganizes a testis and abolishes fertility *without preventing testis specification* — precisely the Node-4-not-Node-1 boundary the brief asked us to decide. A companion paper ([PMID: 35225789](https://pubmed.ncbi.nlm.nih.gov/35225789/)) showing progestin rescue of testis organization in androgen-depleted zebrafish reinforces that the defect is one of androgen-dependent maintenance, not lineage set-up.

**Steroidogenesis vs receptor (Nodes 3/4).** The medaka *scl* mutant ([PMID: 18393567](https://pubmed.ncbi.nlm.nih.gov/18393567/)) provides the clean teleost separation of steroidogenic failure from receptor failure, with androgen rescue proving an intact AR — the mirror image of the curated flutamide-vs-DBP rat contrast.

**Regulatory bioassays (Node 4 readouts).** Fathead minnow ([PMID: 15597888](https://pubmed.ncbi.nlm.nih.gov/15597888/)), medaka ([PMID: 24248458](https://pubmed.ncbi.nlm.nih.gov/24248458/)), guppy ([PMID: 37677862](https://pubmed.ncbi.nlm.nih.gov/37677862/)) and stickleback ([PMID: 17975538](https://pubmed.ncbi.nlm.nih.gov/17975538/); [PMID: 17627896](https://pubmed.ncbi.nlm.nih.gov/17627896/)) collectively establish that teleost secondary-sex structures are flutamide-sensitive AR readouts embedded in OECD guidelines (TG 229; GD 148).

**Somatic-lineage negatives (Node 1).** Medaka *dmrt1* ([PMID: 22187367](https://pubmed.ncbi.nlm.nih.gov/22187367/)) and *O. hubbsi gsdf* ([PMID: 38870865](https://pubmed.ncbi.nlm.nih.gov/38870865/)) are the key negatives: switch-like reversal and germ-cell phenotypes, not dysgenesis. The roach intersex literature ([PMID: 37595157](https://pubmed.ncbi.nlm.nih.gov/37595157/); [PMID: 32293100](https://pubmed.ncbi.nlm.nih.gov/32293100/)) attributes fish intersex to estrogenic drive, excluding it from Node 1.

**Node 5 negatives/analogies.** The galliform phallus paper ([PMID: 23746636](https://pubmed.ncbi.nlm.nih.gov/23746636/)) is a decisive androgen-independent (Bmp4) negative. The alligator literature splits by evidence grade: correlational Lake Apopka phallus reduction ([PMID: 10603274](https://pubmed.ncbi.nlm.nih.gov/10603274/)) versus controlled in-ovo exposure that failed to reproduce it and implicated estrogen, not androgen deficiency ([PMID: 16112671](https://pubmed.ncbi.nlm.nih.gov/16112671/); [PMID: 30010799](https://pubmed.ncbi.nlm.nih.gov/30010799/)).

**Window biology (crux of Node 4).** Medaka thermal-window work ([PMID: 18391524](https://pubmed.ncbi.nlm.nih.gov/18391524/)) establishes that the non-mammalian discrete window is a *gonadal-fate* window, conceptually distinct from the mammalian androgen-programming window.

**Elasmobranch & invertebrate.** The skate clasper paper ([PMID: 25868783](https://pubmed.ncbi.nlm.nih.gov/25868783/)) is the strongest non-mammalian molecular model of AR-driven external-genital patterning. The crustacean IAG literature ([PMID: 33013714](https://pubmed.ncbi.nlm.nih.gov/33013714/); [PMID: 26677879](https://pubmed.ncbi.nlm.nih.gov/26677879/)) establishes that the invertebrate masculinizer is not a nuclear AR.

---

## Limitations and Knowledge Gaps

1. **Amphibian AR loss-of-function is a genuine gap.** *Xenopus* AR biology is documented at the level of receptor expression and hormone regulation in the sexually dimorphic larynx ([PMID: 8844518](https://pubmed.ncbi.nlm.nih.gov/8844518/); [PMID: 2909399](https://pubmed.ncbi.nlm.nih.gov/2909399/)), and the OECD LAGDA (TG 241) detects antiandrogenic testis pathology via chemical exposure (e.g., prochloraz, [PMID: 29674245](https://pubmed.ncbi.nlm.nih.gov/29674245/)). But I did not locate a published *Xenopus* AR knockout/knockdown. The amphibian evidence therefore rests on pharmacology and expression, not a clean genetic null; this should be stated as "searched, not found" rather than "does not exist."

2. **Node 5 is unavoidably analogy-only.** No non-mammalian taxon possesses a prostate, seminal vesicle, or penile urethra, so no model can *recapitulate* incomplete reproductive-tract masculinization. Every claim toward Node 5 is classification (c) or a (d) negative.

3. **Nodes 2, 6, 7, 10, 11 have no non-mammalian model** — there is no non-mammalian gubernaculum, trans-abdominal descent, GCNIS, or invasive TGCT system mapped here. These are empty systems, reported as such.

4. **The window problem is conceptual, not merely empirical.** Even a perfect teleost AR model cannot recapitulate Node 4 as defined, because the fetal androgen-programming window has no non-mammalian analogue. This is the single most important limiting conclusion.

5. **Evidence grades differ sharply.** Genetic nulls (zebrafish *ar*, medaka *scl/dmrt1/gsdf*) and controlled exposures (OECD assays, alligator in-ovo) are strong; wild-population correlational studies (Lake Apopka phallus, roach intersex) are a weaker grade and were kept distinct throughout.

---

## Proposed Follow-up Experiments / Actions

1. **Resolve the amphibian AR gap directly.** Search for and, if absent, flag the need for a *Xenopus tropicalis* AR CRISPR knockout with gonadal and laryngeal phenotyping. This is the one vertebrate class where a clean AR-null is plausibly within reach but was not found in the current literature search.

2. **Mine teleost somatic mutants for partial/mosaic lesions.** Conditional or mosaic knockdown of *gsdf*, *amh*, *sox9b*, or *nr5a1/ff1* in zebrafish/medaka to ask whether *graded* (not binary) perturbation can produce a disorganized mixed-lineage gonad — the only conceivable route to a non-mammalian Node-1/Node-2 analogue. Current full nulls give switch-like outcomes; dose-sensitized backgrounds are untested here.

3. **Formally register the OECD assay mappings** (TG 229 fathead minnow; GD 148 stickleback; TG 241 LAGDA) as validated Node-4 *perturbation* readouts in the disease record, with explicit (b) classification, so downstream users do not mistake them for disease-recapitulating models.

4. **Use the skate clasper Shh/Hand2/AR module as a comparative-genomics anchor.** Test whether the Hand2 ARE and Shh regulatory logic are conserved in mammalian external-genital development — this would convert an analogy-only (c) relationship for Node 5 into a testable conserved-mechanism hypothesis.

5. **Do not pursue invertebrate AR models.** The IAG/insulin-receptor axis is confirmed as the crustacean masculinizer; effort here would not touch Node 4. Record the category as closed.

---

## Conclusion

Non-mammalian androgen-signalling models are real, mechanistically deep, and regulatorily validated — but they map to the TDS graph almost entirely at **Node 4 as classification (b)**: they *perturb* androgen-receptor signalling and never *recapitulate* the disease, because the fetal masculinization programming window and the mammal-specific tract targets that define Nodes 4 and 5 have no non-mammalian counterpart. Nodes 1–2 (focal dysgenesis) return clean negatives, Node 5 is analogy-only with a documented androgen-independent avian negative, and invertebrates are empty because their masculinizer is a peptide, not a nuclear receptor. A short, correctly-ruled-out answer is the honest one here.


## Artifacts

- [OpenScientist final report](Testicular_Dysgenesis_Syndrome-nonmammalian-androgen-models-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Testicular_Dysgenesis_Syndrome-nonmammalian-androgen-models-deep-research-openscientist_artifacts/final_report.pdf)