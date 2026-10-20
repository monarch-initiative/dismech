# Citations for Research Query

**Query:** # Non-Mammalian Model Discovery Template

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

**Provider:** openscientist
**Generated:** 2026-10-20T00:13:07.438385

1. PMID:29272351
2. PMID:29228103
3. PMID:18393567
4. PMID:15597888
5. PMID:24248458
6. PMID:37677862
7. PMID:17975538
8. PMID:17627896
9. PMID:25868783
10. PMID:22187367
11. PMID:38870865
12. PMID:37595157
13. PMID:32293100
14. PMID:23746636
15. PMID:10603274
16. PMID:16112671
17. PMID:30010799
18. PMID:33013714
19. PMID:26677879
20. PMID:18391524
21. PMID:35225789
22. PMID:8844518
23. PMID:2909399
24. PMID:29674245