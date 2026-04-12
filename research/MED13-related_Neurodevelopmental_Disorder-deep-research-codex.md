# MED13-related neurodevelopmental disorder

Date: 2026-04-12
Issue: https://github.com/monarch-initiative/dismech/issues/1140
Primary proposed disease anchor: `MONDO:0032485` `intellectual developmental disorder 61`
Related broader disease context: `MONDO:0100038` `complex neurodevelopmental disorder`
Category: Mendelian
Aliases used in the literature: intellectual developmental disorder, autosomal dominant 61; MRD61; MED13-associated syndrome

## Repo state

- The repo currently has no `kb/disorders/` entry for this disease.
- The current G2P release triage marks `MED13` as `CRITICAL`, `NO_DISMECH_MATCH`, `strong`, and `loss of function`, with the suggested action `ADD_FIRST_GENE_DISEASE_ANCHOR`.
- The local ClinGen cache records a definitive `MED13` gene-disease validity assertion, but it is attached to the broader label `complex neurodevelopmental disorder` rather than the more specific MED13 disease term used in the G2P row.

## Mechanism-centered assessment

MED13-related neurodevelopmental disorder is best framed as a dosage-sensitive transcriptional dysregulation disorder within the Mediator kinase module, not as a primary mitochondrial disease, channelopathy, or isolated malformation syndrome. The strongest disease trunk is:

1. heterozygous pathogenic `MED13` variation
2. altered MED13 dosage or function within the `MED12`-`MED13`-`CDK8`-`CCNC` kinase module
3. dysregulated RNA polymerase II-associated developmental transcription
4. impaired cortical neuronal migration, projection, and maturation programs
5. neurodevelopmental phenotypes dominated by developmental delay, intellectual disability, speech impairment, hypotonia, and behavioral or autism-spectrum features

That trunk is stronger than any alternative because it is supported at three separate levels:

- official gene-function annotation placing MED13 in the Mediator kinase module
- a syndrome-defining human cohort
- a direct cortical-development model connecting Med13 loss to neuronal migration and projection defects

## Why this mechanism is credible

NCBI Gene describes MED13 as a Mediator complex subunit that forms a sub-complex with MED12, cyclin C, and CDK8 and can negatively regulate Mediator-driven transactivation. That makes MED13 a plausible dosage-sensitive upstream controller of developmental transcription rather than a gene whose effects should be modeled through one narrow terminal pathway.

The strongest new mechanistic bridge is the 2026 Communications Biology study showing that Med13 knockdown in developing cortical neurons impaired radial migration, contralateral projection, and dendritic complexity, with partial rescue of migration and projection phenotypes by `PLXNA4` overexpression. This is the first localizable mechanistic link from MED13 dysfunction to a disease-relevant neurodevelopmental process and argues that cortical circuit formation should sit near the center of any first dismech pathophysiology model.

## Human disease evidence

### Syndrome-defining evidence

The anchoring paper is Snijders Blok et al. (Human Genetics, 2018; PMID: `29740699`), which established de novo `MED13` variants as the basis of a recognizable neurodevelopmental syndrome. This remains the single best paper for a first disease anchor because it defines the shared phenotype rather than a single outlier presentation.

### Phenotype expansion without changing the core mechanism

- Trivisano et al. (Seizure, 2022; PMID: `36087421`) shows that developmental and epileptic encephalopathy with infantile spasms can occur in the MED13 spectrum.
- Tolmacheva et al. (BMC Medical Genomics, 2024; PMID: `38745205`) extends the multisystem congenital-anomaly end of the phenotype.
- The 2025 hearing-loss case report (PMID: `41561257`) is useful because a truncating allele supports a loss-of-function or haploinsufficiency-skewed interpretation and expands the sensory phenotype.
- Harada et al. (Human Genome Variation, 2025; PMID: `41130977`) reports infantile spasms, cardiomyopathy, hepatomegaly, and mitochondrial abnormalities, but this should currently be treated as a severe or allele-specific presentation rather than the default mechanistic center of the disorder.

The implication is that epilepsy, heart disease, hearing loss, and possible metabolic stress are real spectrum extensions, but they should branch off the main transcriptional/cortical-development mechanism rather than define it.

## Anchor choice in this repo

The local data split in two directions:

- G2P points to the MED13-specific disease concept `MONDO:0032485` (`intellectual developmental disorder 61`).
- ClinGen validity is cached against the broader umbrella `MONDO:0100038` (`complex neurodevelopmental disorder`).

For dismech, the better first anchor is still the MED13-specific term. The human literature now supports a recognizable MED13-centered syndrome, and the G2P row explicitly asks for a first gene-disease anchor. The broader ClinGen label is still useful as supporting evidence that the gene-disease relationship is definitive, but it should not force the entry to collapse into an umbrella disorder that loses the MED13-specific mechanism and phenotype framing.

## Curation-ready entities

### Primary disease gene

- `MED13` (`hgnc:22474`)

### Mechanistically relevant partner genes

- `MED12`
- `CDK8`
- `CCNC`
- `PLXNA4`

These are useful for pathophysiology narrative and downstream edges, but they do not change the fact that the disorder should be rooted as a MED13 disease.

### Candidate cell types

- neural progenitor cell
- neuron
- cerebral cortex neuron

If a later YAML needs a narrower model, callosal or contralaterally projecting cortical neurons are attractive, but the current literature supports a broader cortical-neuron framing more safely.

### Candidate anatomical locations

- brain
- cerebral cortex
- corpus callosum

Secondary or variable sites:

- heart
- inner ear or auditory pathway
- eye or optic pathway

### Candidate biological processes

- regulation of transcription by RNA polymerase II
- cerebral cortex development
- neuron migration
- neuron projection development
- dendrite development

## Phenotypes that are safe for a first entry

### Core phenotypes

- developmental delay or global developmental delay
- intellectual disability
- speech and language impairment
- hypotonia
- autism-spectrum or behavioral abnormalities

### Secondary or spectrum-expanding phenotypes

- seizures, including infantile spasms
- congenital heart disease or cardiomyopathy
- hearing impairment
- ocular abnormalities
- corpus callosum abnormalities
- growth restriction or feeding difficulty
- mild dysmorphic facial features

The core list is strong enough for a first conservative YAML. The secondary list should be added only where there is direct disease-level evidence rather than extrapolation from isolated severe reports.

## What looks settled versus unsettled

### Settled enough

- `MED13` is a credible Mendelian neurodevelopmental disease gene.
- Autosomal-dominant, usually de novo disease is the default human pattern.
- Loss-of-function or haploinsufficiency is the best current default model, especially for truncating alleles.
- The most coherent mechanism framing is Mediator kinase-module dysfunction causing transcriptional dysregulation during cortical development.

### Still unsettled

- Whether all missense alleles operate through the same mechanism as truncating alleles
- Whether cardiomyopathy, hepatomegaly, and mitochondrial abnormalities are core-spectrum versus allele-specific
- The exact disease-level frequency of congenital heart disease, hearing loss, epilepsy, and corpus callosum anomalies

## Recommendation

This should become both:

- a conservative disorder entry rooted at `MONDO:0032485`
- a short project or curation note that records the anchor choice, the ClinGen versus G2P label split, and the decision to keep the first mechanism centered on Mediator/cortical-development biology rather than severe outlier phenotypes

The disorder entry is justified because the gene-disease relationship and core syndrome are already strong enough. The project note is still useful because the worktree currently needs a durable record of why the first entry should stay narrow and how to treat the more severe cardiac, auditory, and mitochondrial reports.

## Bottom line

`MED13` is no longer just a backlog candidate. In this repo it is a critical missing disease anchor, and the current local evidence supports a coherent first mechanism model: MED13 loss-of-function-skewed disruption of the Mediator kinase module leads to transcriptional dysregulation during cortical development, which then produces a recognizable neurodevelopmental syndrome. The right next step is not to wait for a perfect mechanism map, but to create a conservative MED13 disorder entry while preserving the unresolved anchor and phenotype-boundary decisions in a companion curation note linked to issue `#1140`.
