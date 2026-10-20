---
title: Splice Variants and Spliceosome Disorders
status: IN_PROGRESS
description: >-
  Disorders caused by variants in spliceosome RNA and protein genes, and the
  splice-altering variants and splice-switching therapies that recur across
  the knowledge base.
tags: [MECHANISM, SPLICING, SPLICEOSOMOPATHY, NEURODEVELOPMENT, NONCODING]
diseases:
  - RNU5B-1_Related_Neurodevelopmental_Disorder_With_Seizures_And_Joint_Laxity
  - ReNU_Syndrome
  - RNU12-related_Minor_Spliceopathy
  - Roifman-syndrome
  - Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I
  - Neurodevelopmental_Disorder_with_Hypotonia_Feeding_Difficulties_Facial_Dysmorphism_and_Brain_Abnormalities
  - SNIP1-Related_Neurodevelopmental_Disorder
  - Neuromuscular_Disease_And_Ocular_Or_Auditory_Anomalies_With_Or_Without_Seizures
  - Mandibulofacial_Dysostosis_with_Microcephaly
  - Burn-McKeown_Syndrome
  - Cerebrocostomandibular_Syndrome
  - Nager_Acrofacial_Dysostosis
  - Intellectual_Developmental_Disorder_Autosomal_Dominant_72
  - PRPF31-Related_Retinopathy
  - Craniofacial_Microsomia
  - Orofaciodigital_Syndrome
  - Mosaic_Variegated_Aneuploidy_Syndrome
  - Myelodysplastic_Syndrome
  - Spinal_Muscular_Atrophy
  - Duchenne_Muscular_Dystrophy
  - Dravet_syndrome
  - Ataxia_Telangiectasia
  - Neuronal_Ceroid_Lipofuscinosis_7
  - Leber_Congenital_Amaurosis_10
  - Usher_Syndrome_Type_2
  - Stargardt_Disease
modules:
  - antisense_oligonucleotide_therapy
---

# Splice Variants and Spliceosome Disorders

## Scope

Splicing goes wrong in disease in three distinct ways, and this project keeps
them apart because they call for different pathographs:

1. **The machine is broken (trans).** A variant in a spliceosome component, an
   snRNA gene or a core protein, changes how many introns across the genome are
   handled. The disease mechanism is a pattern of mis-splicing, and the open
   question is usually which affected transcripts produce the phenotype.
2. **One transcript is broken (cis).** A variant in or near a splice site, or a
   deep-intronic variant that creates a pseudoexon, mis-splices a single gene.
   This is a variant-level fact on an ordinary gene entry, not a separate
   disease.
3. **Splicing is the treatment.** Splice-switching antisense oligonucleotides
   and small molecules correct or redirect splicing of a single transcript.

The first group is the core of the project. The other two are tracked so their
modelling stays consistent.

## Artifacts

| Artifact | What it is |
|---|---|
| [U5 Loop I and RNU5B-1](https://claude.ai/artifact/NdbjH4KmWzAomJVj6rrecK) | Illustrated explainer: the two steps of splicing, U5 loop I and where RNU5B-1 variants fall, the two 5′ splice-site classes, what patient RNA showed, and the missing link to the brain phenotype. Private until shared from its page. |
| [OpenScientist hypothesis search](https://github.com/monarch-initiative/dismech/blob/main/kb/hypotheses/RNU5B-1_Related_Neurodevelopmental_Disorder_With_Seizures_And_Joint_Laxity/rnu5b1_missplicing_drives_brain_phenotype/openscientist.md) | Report on whether variant-specific mis-splicing explains the RNU5B-1 phenotype; literature synthesis plus a GEO and SRA availability check. |
| [Assessment of that search](https://github.com/monarch-initiative/dismech/blob/main/kb/hypotheses/RNU5B-1_Related_Neurodevelopmental_Disorder_With_Seizures_And_Joint_Laxity/rnu5b1_missplicing_drives_brain_phenotype/assessments/openscientist-assessment-by-claude-code.yaml) | Verdict WEAKLY_SUPPORTED_UNRESOLVED, with claim-level dispositions and the data-access inventory. |

## Group 1: spliceosome component disorders

### snRNA genes

These genes are short, noncoding and multi-copy, so variants are missed by
standard exome capture and the copy that matters is often the one expressed in
brain. Dominant disease variants cluster in a few nucleotides of one
structural element.

| Entry | Gene | snRNA | Spliceosome |
|---|---|---|---|
| RNU5B-1_Related_Neurodevelopmental_Disorder_With_Seizures_And_Joint_Laxity | RNU5B-1 | U5 | major |
| ReNU_Syndrome | RNU4-2 | U4 | major |
| RNU12-related_Minor_Spliceopathy | RNU12 | U12 | minor |
| Roifman-syndrome | RNU4ATAC | U4atac | minor |
| Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I | RNU4ATAC | U4atac | minor |

### Spliceosome protein genes

| Entry | Gene |
|---|---|
| Neurodevelopmental_Disorder_with_Hypotonia_Feeding_Difficulties_Facial_Dysmorphism_and_Brain_Abnormalities | WBP4 |
| SNIP1-Related_Neurodevelopmental_Disorder | SNIP1 |
| Neuromuscular_Disease_And_Ocular_Or_Auditory_Anomalies_With_Or_Without_Seizures | DHX16 |
| Mandibulofacial_Dysostosis_with_Microcephaly | EFTUD2 |
| Burn-McKeown_Syndrome | TXNL4A |
| Cerebrocostomandibular_Syndrome | SNRPB |
| Nager_Acrofacial_Dysostosis | SF3B4 |
| Intellectual_Developmental_Disorder_Autosomal_Dominant_72 | SRRM2 |
| PRPF31-Related_Retinopathy | PRPF31 |
| Craniofacial_Microsomia | SF3B2 (one of several genes) |
| Orofaciodigital_Syndrome | ZRSR2 (one of several genes) |
| Mosaic_Variegated_Aneuploidy_Syndrome | CENATAC (minor-intron splicing; one of several genes) |
| Myelodysplastic_Syndrome | somatic SF3B1, SRSF2, U2AF1, ZRSR2 |

### Not yet curated

Each of these has a stub in `stubs/`.

| Stub | Gene | Note |
|---|---|---|
| RNU4ATAC_Spectrum_Disorder | RNU4ATAC | Lump/split decision against the Roifman and MOPD I entries |
| Congenital_Cerebellar_Ataxia_Due_To_RNU12_Mutation | RNU12 | Likely a `SUBTYPE` of the RNU12 entry |
| Developmental_Delay_Dysmorphic_Facies_And_Brain_Anomalies | U2AF2 | |
| PRPF19-related_Neurodevelopmental_Disorder | PRPF19 | |
| PRPF8-related_Retinopathy | PRPF8 | Tri-snRNP retinopathy, like PRPF31 |
| SNRNP200-related_Dominant_Retinopathy | SNRNP200 | Tri-snRNP retinopathy |
| Metaphyseal_Chondrodysplasia-retinitis_Pigmentosa_Syndrome | CWC27 | |
| Hypotrichosis_11 | SNRPE | |
| LSM7-related_Leukodystrophy_And_Cerebellar_Atrophy | LSM7 | LSM7 sits in both the U6-associated and the decay-associated LSm rings; check which the source implicates |

Recently described disorders with no stub yet: dominant and recessive RNU2-2
neurodevelopmental disorder, recessive RNU4-2 neurodevelopmental disorder, and
dominant U4/U6 retinitis pigmentosa (RNU4-2 three-way junction, RNU6 genes).
The ReNU_Syndrome entry already cites the papers for each.

## Group 2: cis splice-altering variants

These belong on the gene's own entry, as `genetic[].variants` with the
splicing consequence stated, and not as new disease entries. Use the
`noncoding-variant-impact` skill for deep-intronic and regulatory variants,
and keep the physical change, the splicing outcome and the evidence for that
outcome separate. No audit of how consistently the KB records these has been
done yet.

## Group 3: splice-switching therapy

Entries with an oligonucleotide treatment whose
`oligonucleotide_mechanism` is `SPLICE_MODULATION_EXON_SKIPPING` or
`SPLICE_MODULATION_EXON_INCLUSION`: Spinal_Muscular_Atrophy,
Duchenne_Muscular_Dystrophy, Dravet_syndrome, Ataxia_Telangiectasia,
Neuronal_Ceroid_Lipofuscinosis_7, Leber_Congenital_Amaurosis_10,
Usher_Syndrome_Type_2 and Stargardt_Disease, among others. Treatments that use
this mechanism should conform to `antisense_oligonucleotide_therapy`.

## Open questions

- **Which mis-spliced transcripts cause the phenotype?** Not answered for any
  major-spliceosome snRNA disorder. RNU5B-1 is recorded as a `KNOWLEDGE_GAP`
  with two proposed experiments: splicing in isogenic stem-cell-derived
  neurons, and the level and spliceosome incorporation of the mutant U5B-1.
- **Neomorphic or loss of function?** For dominant snRNA variants, the mutant
  RNA may redirect splice-site choice, or be degraded by snRNA quality control,
  or poison spliceosomes broadly. The RNU5B-1 entry carries both models as
  competing `mechanistic_hypotheses`, and ReNU_Syndrome has a matching gap.
- **Why are the phenotypes tissue-restricted?** Mutations in core, ubiquitous
  machinery give craniofacial dysostoses (EFTUD2, SF3B4, SNRPB, TXNL4A),
  isolated retinopathy (PRPF31, PRPF8, SNRNP200) or neurodevelopmental disease
  (RNU4-2, RNU5B-1, RNU2-2). No shared explanation is recorded.

## Possible next steps

- A mechanism module for spliceosome dysfunction, so these entries can
  `conform_to` a shared node chain instead of each restating it.
- A `Grouping` for the snRNA gene disorders, or for spliceosomopathies more
  broadly, with membership criteria on spliceosome components.
- Curate the stubs above, starting with the two tri-snRNP retinopathies, which
  extend the PRPF31 entry.
