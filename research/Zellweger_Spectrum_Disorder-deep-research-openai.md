# Zellweger Spectrum Disorder Deep Research Notes

Date: 2026-04-12

## Scope and disease framing

This curation treats Zellweger spectrum disorder (ZSD) as a single disease-level
continuum rather than splitting classical Zellweger syndrome, neonatal
adrenoleukodystrophy, infantile Refsum disease, or Heimler syndrome into
separate dismech entries.

Key framing evidence:

- `PMID:26750748`: "The extreme variability in disease manifestation ranging from onset of profound neurologic symptoms in newborns to progressive degenerative disease in adults presents practical challenges in disease diagnosis and medical management."
- `PMID:36293220`: "The vast majority of PBDs belong to Zellweger Spectrum Disordes (ZSDs) and represents a continuum of overlapping clinical symptoms, with Zellweger syndrome being the most severe and Heimler syndrome the less severe disease."
- `PMID:11389485`: "Zellweger syndrome (ZS), neonatal adrenoleukodystrophy (NALD), and infantile Refsum disease (IRD) are clinically overlapping syndromes, collectively called "peroxisome biogenesis disorders" (PBDs), with clinical features being most severe in ZS and least pronounced in IRD."

## Ontology choice

I anchored the YAML to `MONDO:0019234` with preferred term `Zellweger spectrum disorder`.

Reasoning:

- In current MONDO, `MONDO:0019234` is labeled `peroxisome biogenesis disorder`,
  but its definition corresponds to the Zellweger spectrum / PBD-ZSD continuum.
- `MONDO:0019609` is labeled `Zellweger spectrum disorders`, but its current
  definition is narrower and reads more like the classical severe syndrome.
- Using `MONDO:0019234` avoids over-narrowing the disease anchor while still
  representing the clinically used ZSD continuum.

This is why the YAML note explicitly documents the MONDO label/preferred-term
asymmetry instead of silently accepting it.

## Main mechanistic story

The disease story was curated as an atomic chain rather than a bundled
"peroxisomal dysfunction" block:

1. Biallelic pathogenic variants in 13 `PEX` genes impair peroxisome biogenesis
   and matrix protein import.
2. This creates a deficiency of functional peroxisomes.
3. Distinct downstream consequences then separate into:
   - reduced peroxisomal beta-oxidation
   - impaired ether lipid biosynthesis
   - C27 bile acid intermediate accumulation
   - abnormal neuronal migration
4. Those downstream lesions were then mapped to organ/tissue-level pathology:
   - cerebral/cerebellar white matter disease
   - retinal degeneration
   - progressive liver disease

This structure is closer to causal resolution than the previous file, which
collapsed nearly all disease biology into a few broad nodes.

## Key evidence selections

### Disease-gene set and major gene

- `PMID:40112482`: "Zellweger spectrum disorder (ZSD) results from biallelic variants in any one of 13 PEX genes involved in peroxisome biogenesis and function."
- `PMID:40112482`: "The majority of ZSD cases result from pathogenic variants in PEX1."
- `PMID:11389485`: "Approximately 65% of the patients with PBD harbor mutations in PEX1."
- `PMID:11389485`: "The majority of these latter patients carried at least one copy of the common G843D allele."

Why included:

- This supports one heterogeneous disease definition with `PEX1` highlighted as
  the dominant disease gene and `PEX1 p.Gly843Asp` captured as a clinically
  relevant attenuating allele.

### Organelle-level initiating lesion

- `PMID:33417206`: "Impaired peroxisome biogenesis, including defects of membrane assembly, import of peroxisomal matrix proteins, and division of peroxisome, causes peroxisome biogenesis disorders (PBDs)."
- `PMID:30793331`: "Currently, no therapies are available for Zellweger spectrum disorders (ZSDs), a group of genetic metabolic disorders characterised by a deficiency of functional peroxisomes."

Why included:

- These two quotes cleanly separate the initiating biogenesis/import defect from
  the next node, loss of functional peroxisomes.

### Lipid metabolic consequences

- `PMID:33417206`: "Peroxisomes are presented in all eukaryotic cells and play essential roles in many of lipid metabolic pathways, including β-oxidation of fatty acids and synthesis of ether-linked glycerophospholipids, such as plasmalogens."
- `PMID:24503136`: "we demonstrate that murine cells homozygous for the Pex1-G844D allele respond to chaperone-like compounds, which normalizes peroxisomal β-oxidation."
- `PMID:12473763`: "Multiple peroxisomal functions including de novo plasmalogen synthesis, dihydroxyacetonephosphate acyltransferase (DHAPAT) activity, C26:0/C22:0 ratio, C26:0 and pristanic acid beta-oxidation, and phytanic acid alpha-oxidation were analyzed in fibroblasts from a series of patients with defined clinical phenotypes."

Why included:

- These support keeping beta-oxidation and ether lipid/plasmalogen biology as
  separate downstream nodes rather than collapsing them into one metabolite node.

### Hepatic mechanism

- `PMID:28644367`: "Accumulation of these potentially hepatotoxic metabolites and the reduction in bile acid-dependent bile flow from the lack of primary bile acids may lead to liver injury"
- `PMID:28644367`: "ZSDs are characterized by progressive liver disease and extrahepatic manifestations such as central nervous system dysfunction"
- `PMID:30793331`: "Although CA treatment did lead to reduced levels of toxic C27 -bile acid intermediates in ZSD patients without severe liver fibrosis or cirrhosis, no improvement of clinically relevant parameters was observed after 21 months of treatment."

Why included:

- These support a specific hepatic mechanism node centered on C27 bile acid
  intermediates rather than a vague "liver involvement" statement, and they
  justify the nuanced treatment statement for cholic acid.

### Neurodevelopment and later progression

- `PMID:15868469`: "Peroxisome biogenesis disorders, of which Zellweger syndrome is the most severe, result in severe neurological dysfunction associated with abnormal CNS neuronal migrations due to the lack of functional peroxisomes."
- `PMID:26287655`: "Disease progression may occur and is mainly due to cerebral and cerebellar white matter abnormalities, and peripheral neuropathy."
- `PMID:26287655`: "Systematic MRI review revealed T2 hyperintense white matter abnormalities in the hilus of the dentate nucleus and/or peridentate region in nine out of 16 patients."

Why included:

- These distinguish an early developmental brain mechanism from later
  progressive white matter disease in attenuated survivors.

### Sensory phenotypes

- `PMID:38664000`: "Fundus examination revealed a variable retinitis pigmentosa (RP)-like phenotype with rounded hyperpigmentations as most prominent feature in six out of nine patients."
- `PMID:38664000`: "This study highlights the ophthalmological phenotype resembling RP with moderate to severe visual impairment in patients with mild ZSD."
- `PMID:34534157`: "The majority of PBD-ZSD patients in this study presented with moderately-severe to severe hearing loss and relatively slow rates of longitudinal changes in hearing sensitivity."

Why included:

- These support retinal degeneration and sensorineural hearing impairment as
  supported phenotype-level assertions rather than relying on older generic
  textbook descriptions alone.

### Endocrine modifier with management impact

- `PMID:25179809`: "Primary adrenal insufficiency was found in 7/24 patients examined, with 4/7 being asymptomatic."
- `PMID:25179809`: "Systematic evaluation of adrenal function, through a Synacthen test, should be included in the clinical management of these patients."

Why included:

- Adrenal insufficiency was included because it changes clinical surveillance and
  is not just a minor associated finding.

## Treatments included

Included:

- Supportive/surveillance-based care
- Cholic acid

Why:

- Both have direct disease-specific evidence.
- Cholic acid was phrased carefully: biochemical benefit is supported, but
  clinically meaningful disease modification is limited.

Not included:

- Experimental proteostasis/chaperone rescue strategies for `PEX1 p.Gly843Asp`
- Empiric bile acid statements without disease-specific ZSD evidence
- Generic supplements without direct support in retrieved evidence

## Histopathology and modifier choices

Included:

- Liver disease as an organ-level pathophysiology node, because liver injury and
  progressive liver disease are explicitly supported.
- `PEX1 p.Gly843Asp` as a modifier-like variant note, because residual protein
  and attenuated phenotype are directly supported.

Not added as standalone sections:

- Separate histopathology block for brain or retina. The strongest retrieved
  evidence was clinical imaging and phenotype-focused rather than lesion-rich
  pathology studies with clean disease-level generalizability.

## Curation exclusions and cleanup relative to the old file

The previous `Peroxisome_Biogenesis_Disorder.yaml` entry mixed:

- broad peroxisomal disease language outside the Zellweger spectrum
- weak or non-specific prevalence claims
- bundled mechanism nodes
- partially supported metabolite/treatment statements

Those were removed or tightened. The rewritten file focuses on the ZSD
continuum, preserves only directly supported mechanisms/phenotypes/treatments,
and uses ontology-grounded terms where the evidence was strong enough to justify
them.
