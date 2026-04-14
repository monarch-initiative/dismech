# Smith-Lemli-Opitz syndrome deep research notes

## Scope and disease framing

- Curated disease: `MONDO:0010035` Smith-Lemli-Opitz syndrome.
- Framing choice: treat SLOS as one disease-level DHCR7 deficiency spectrum rather than splitting historical "type I/type II" labels into separate disease entries. The literature consistently describes a continuous severity range from fetal-lethal multiple malformations to relatively mild neurodevelopmental disease.
- Do not lump with other sterol-biosynthesis disorders such as desmosterolosis or lathosterolosis. The mechanistic overlap is real, but the causal gene, sterol block, and downstream evidence base are disease-specific.
- Main encoded mechanistic story: `DHCR7 deficiency -> 7-DHC accumulation + relative cholesterol deficiency -> Smoothened/Hedgehog signaling impairment + oxysterol toxicity -> abnormal neurodevelopment`, with a separate fibroblast-supported oxidative-stress/autophagy branch.

## Why the pathophysiology graph was split this way

### 1. Core lesion

- `PMID:9653161`
  - Quote: "Here we identify the SLOS gene as a Delta7-sterol reductase (DHCR7, EC 1.3.1. 21) required for the de novo biosynthesis of cholesterol."
  - Use: anchors the disease to loss of DHCR7 activity, not just a descriptive sterol pattern.

### 2. Separate cholesterol deficiency from precursor accumulation

- `PMID:23059950`
  - Quote: "The enzymatic deficiency results in decreased cholesterol and increased 7DHC levels, both during embryonic development and after birth."
  - Use: justifies two sibling downstream nodes rather than a bundled "abnormal sterol metabolism" node.
- `PMID:7706951`
  - Quote: "It is characterized biochemically by low plasma cholesterol and greatly elevated levels of two dehydrocholesterols, one of which is the cholesterol precursor 7-dehydrocholesterol."
  - Use: strong human biochemical support for both branches.

### 3. Cholesterol deficiency branch

- `PMID:26685159`
  - Quote: "Our results indicate that a deficit in cholesterol, as opposed to an accumulation of 7DHC, impairs SMO activation and its localization to the primary cilium."
  - Use: this is the cleanest evidence that the sterol-deficiency arm should point specifically to impaired Smoothened activation, rather than vaguely to "abnormal Hedgehog signaling."
- Curation decision:
  - Encoded `Relative Cholesterol Deficiency -> Impaired Smoothened Activation`.
  - Did not overextend this paper into specific human malformations; the abstract supports the signaling defect, not a specific phenotype edge.

### 4. 7-DHC toxicity branch

- `PMID:22182693`
  - Quote: "The overall results suggest that 7-DHC oxidative metabolites are critical contributors to altered neural development in SLOS."
  - Use: supports a distinct oxysterol-toxicity node rather than treating 7-DHC excess as inert storage.
- `PMID:22182693`
  - Quote: "We also report that neurons are ten fold more susceptible to a 7-DHC-derived oxysterol mixture than glial cells, and that DHCEO accelerates differentiation and arborization of cortical neurons."
  - Use: supports a downstream `Premature Neurogenesis` node.
- `PMID:36111785`
  - Quote: "Here, we show that loss of DHCR7 causes accumulation of 7-DHC-derived oxysterol metabolites, premature neurogenesis from murine or human cortical neural precursors, and depletion of the cortical precursor pool, both in vitro and in vivo."
  - Use: reinforces the same causal branch and adds a modern mechanistic refinement through GR/TrkB signaling.
  - Curation decision: kept this paper in research notes but not as primary YAML evidence because its abstract mixes human precursor cultures and in vivo mouse work in one sentence, which complicates clean `evidence_source` tagging.

### 5. Oxidative stress / autophagy branch

- `PMID:25405082`
  - Quote: "We also show that the LC3B-II concentration in SLOS cells is directly proportional to the cellular concentration of 7DHC, suggesting that the increased autophagy is caused by 7DHC accumulation secondary to defective DHCR7."
  - Quote: "Further, the increased basal LC3B-II levels were decreased significantly by pretreating the cells with antioxidants implicating a role for oxidative stress in elevating autophagy in SLOS cells."
  - Use: strong patient-fibroblast evidence for a cellular-stress branch that is mechanistically distinct from the developmental signaling branch.
- Curation decision:
  - Encoded `Oxidative Stress-Linked Autophagy` as a separate node.
  - Did not claim this branch fully explains the congenital malformation phenotype.

## Phenotype selection

- Kept phenotype set focused on repeatedly cited, disease-defining human findings from `PMID:23059950`.
- Encoded:
  - Intellectual disability
  - Microcephaly
  - 2-3 toe syndactyly
  - Cleft palate
  - Postaxial polydactyly
  - Underdeveloped external genitalia in males
- Left out for now:
  - Autism spectrum disorder / behavioral phenotype as a standalone phenotype, because the strongest easily quotable support in the current source set comes from mechanistic papers or treatment trials rather than a clean phenotype-defining clinical abstract.
  - Organ-system-specific internal malformations beyond the general statement that they may affect every organ system, because I did not want to over-encode unspecific phenotype atoms without dedicated evidence.

## Genetics and modifier curation

### Causative gene

- `PMID:9653161`
  - Quote: "Our results strongly suggest that defects in the DHCR7 gene cause the SLOS."
- `PMID:17965227`
  - Quote: "In 263 SLOS patients 10 common alleles ... were found to constitute approximately 80% of disease-causing mutations."
- Curation decision:
  - Encoded `DHCR7` as causative.
  - Added the recurrent-allele note because it is clinically useful and cohort-backed.

### Modifier

- `PMID:22929031`
  - Quote: "Maternal ABCA1 genotypes show a highly significant correlation with clinical severity in SLOS patients (P=0.007)."
  - Quote: "ABCA1 is an additional genetic modifier in SLOS."
- Curation decision:
  - Encoded `ABCA1` as a modifier with an explicit note that the effect is maternal and plausibly mediated by placental cholesterol transfer.
  - Did not also encode maternal ApoE because I did not fetch a comparably clean primary abstract in this pass.

## Treatment curation choices

### Included

- `PMID:10951458`
  - Quote: "These results support the hypothesis that over time dietary cholesterol supplementation from egg yolk increases the plasma cholesterol levels and decreases levels of 7-DHC which may be toxic."
  - Encoded as dietary cholesterol supplementation.
- `PMID:27513191`
  - Quote: "Simvastatin seems to be relatively safe in patients with SLOS, improves the serum dehydrocholesterol-to-total sterol ratio, and significantly improves irritability symptoms in patients with mild to classic SLOS."
  - Encoded as adjunctive pharmacotherapy for mild-to-classic SLOS.
- `PMID:38077958`
  - Quote: "In this pilot study, cholic acid supplementation was well tolerated and safe and resulted in an increase in plasma cholesterol in most SLOS subjects."
  - Encoded cautiously as a preliminary pilot therapy with biochemical benefit.

### Not encoded

- Prenatal therapy concepts based on placental cholesterol transfer.
  - Reason: mechanistically interesting, but still not an established clinical treatment.
- Antioxidant therapy.
  - Reason: promising model-based rationale, but the current source set is still preclinical.

## Human biochemical anchors used in the YAML

- `PMID:23059950`
  - Quote: "The clinical diagnosis of SLOS is confirmed by demonstrating an abnormally elevated concentration of the cholesterol precursor, 7DHC, in serum or other tissues, or by the presence of two DHCR7 mutations."
- `PMID:7706951`
  - Quote: "These results suggest that a defect in 3 beta-hydroxysterol delta 7-reductase leads to both a profound lack of cholesterol and its replacement by dehydrocholesterols."

## Things intentionally left for a future pass

- Prenatal biomarkers and maternal serum/urine steroid signatures.
- Adrenal insufficiency and bile-acid physiology as complication-specific subgraphs.
- More granular internal-organ malformations with dedicated heart, renal, and genital-development mechanism edges.
- Explicit behavioral/psychiatric phenotype expansion once a clean human-clinical source set is assembled.

## Source set fetched into cache for this curation

- `PMID:9653161` DHCR7 causation
- `PMID:7706951` defining human sterol biochemistry
- `PMID:23059950` phenotype / natural history / diagnosis
- `PMID:17965227` prevalence and common allele spectrum
- `PMID:10951458` dietary cholesterol supplementation
- `PMID:27513191` simvastatin placebo-controlled trial
- `PMID:26685159` cholesterol deficiency impairs Smoothened activation
- `PMID:25405082` oxidative stress, autophagy, mitochondrial dysfunction
- `PMID:22182693` DHCEO / oxysterol neurodevelopmental toxicity
- `PMID:36111785` premature neurogenesis and antioxidant rescue
- `PMID:22929031` maternal ABCA1 modifier
- `PMID:38077958` cholic acid pilot study
