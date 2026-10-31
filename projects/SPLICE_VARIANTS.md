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
  - PRPF8-Related_Retinopathy
  - SNRNP200-Related_Dominant_Retinopathy
  - U2AF2-Related_Neurodevelopmental_Disorder
  - PRPF19-related_Neurodevelopmental_Disorder
  - CWC27-Related_Retinitis_Pigmentosa_With_or_Without_Skeletal_Anomalies
  - Hypotrichosis_11
  - LSM7-related_Leukodystrophy_And_Cerebellar_Atrophy
  - Lowry-Wood_Syndrome
  - Genetic_Developmental_and_Epileptic_Encephalopathy
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
  - spliceosome_component_dysfunction
  - antisense_oligonucleotide_therapy
groupings:
  - Spliceosomopathies
  - RNU4ATAC_Spectrum_Disorder
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
| PRPF8-Related_Retinopathy | PRPF8 |
| SNRNP200-Related_Dominant_Retinopathy | SNRNP200 |
| U2AF2-Related_Neurodevelopmental_Disorder | U2AF2 |
| PRPF19-related_Neurodevelopmental_Disorder | PRPF19 |
| CWC27-Related_Retinitis_Pigmentosa_With_or_Without_Skeletal_Anomalies | CWC27 |
| Hypotrichosis_11 | SNRPE |
| LSM7-related_Leukodystrophy_And_Cerebellar_Atrophy | LSM7 (in both the spliceosomal LSm2-8 and the mRNA-decay LSm1-7 rings) |
| Craniofacial_Microsomia | SF3B2 (one of several genes) |
| Orofaciodigital_Syndrome | ZRSR2 (one of several genes) |
| Mosaic_Variegated_Aneuploidy_Syndrome | CENATAC (minor-intron splicing; one of several genes) |
| Myelodysplastic_Syndrome | somatic SF3B1, SRSF2, U2AF1, ZRSR2 |

### Covered as subtypes, not entries

| Disorder | Gene | Where it is curated |
|---|---|---|
| Congenital cerebellar ataxia due to RNU12 mutation (MONDO:0033717) | RNU12 | The SCAR33 subtype of RNU12-related_Minor_Spliceopathy; Orphanet's term for the same disease as OMIM:620208 |
| Developmental and epileptic encephalopathy 119 (MONDO:1060177) | RNU2-2 | A subtype of Genetic_Developmental_and_Epileptic_Encephalopathy |
| Recessive RNU4-2-related neurodevelopmental disorder | RNU4-2 | A subtype of ReNU_Syndrome |
| RNU4-2- and RNU6-related retinitis pigmentosa | RNU4-2, RNU6 genes | A subtype of ReNU_Syndrome |
| RNU4ATAC spectrum disorder (MONDO:0100558) | RNU4ATAC | A grouping over Roifman, MOPD I and Lowry-Wood |

None of these has a stub. MONDO has no term yet for the recessive RNU4-2
disorder or for snRNA-gene retinitis pigmentosa: OLS searches of MONDO for
"RNU4-2", "RNU6" and "retinitis pigmentosa small nuclear RNA" returned no such
term, and retinitis pigmentosa 96 to 101 are caused by other genes (SAG, VWA8,
TMEM216, IDH3G, TBC1D32, CLN3). A stub can be added once MONDO has a term.

### Not yet curated

No spliceosome-component stubs remain in `stubs/`.

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
  (RNU4-2, RNU5B-1, RNU2-2). This is recorded as a `KNOWLEDGE_GAP` on
  `spliceosome_component_dysfunction`. The Eftud2 work shows the P53 branch
  contributes but is not sufficient: deleting Trp53 in neural crest did not
  rescue development.
- **Is RPE failure primary in the PRPF retinopathies?** Prpf8 knock-in mice
  show an RPE phagocytosis defect that patient-derived RPE did not reproduce,
  while retinal organoids degenerate without any RPE. Recorded as a
  `HUMAN_MODEL_MISMATCH` on PRPF8-Related_Retinopathy.

## Progress

- `spliceosome_component_dysfunction` module: component variant, then
  mis-splicing of a sensitive transcript subset (the key conformance target),
  an optional P53 branch, failure of splicing-sensitive cells, and
  tissue-restricted disease.
- `Spliceosomopathies` grouping: 22 members defined by a single
  `CONFORMS_TO_MODULE` criterion, three of them through the nested
  RNU4ATAC_Spectrum_Disorder grouping.
- Curated from stubs: PRPF8, SNRNP200, U2AF2, PRPF19, CWC27, SNRPE (Hypotrichosis
  11) and LSM7. RNU12 cerebellar ataxia was folded into the existing SCAR33
  subtype.
- Wired to the module: SNIP1, DHX16, WBP4 and SRRM2. Craniofacial_Microsomia
  is left out, because its SF3B2 node also carries FOXI3, GBX2 and SHROOM3.
- Not every member conforms at the mis-splicing node. Mis-splicing is not
  shown for Hypotrichosis 11 (the founding study found none in patient
  lymphocytes) or LSM7 (no splicing assay yet), and for PRPF19 it rests on fly
  ortholog knockdown only.

## Possible next steps

- Test which LSm ring LSM7 variants disrupt: the entry proposes a patient-cell
  experiment that separates splicing from mRNA decay.
- Add stubs for the recessive RNU4-2 and snRNA retinitis pigmentosa disorders
  once MONDO has terms for them.
- Audit how consistently Group 2 splice variants are recorded on gene entries.
