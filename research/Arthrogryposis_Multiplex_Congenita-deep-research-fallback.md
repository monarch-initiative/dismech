# Arthrogryposis Multiplex Congenita Deep Research Fallback

## Provider Attempts

- 2026-05-13: Automated deep-research providers (falcon, asta, cyberian-codex,
  perplexity, openai) were unavailable in the curation environment for this
  disorder. No provider-generated research artifact was produced.

No provider-generated research artifact was available to integrate. Curation
therefore proceeded from a manual literature synthesis built around the
canonical AMC clinical and molecular references listed below, without
hand-editing any `references_cache/*.md` files.

## Evidence Scope Used For Curation

- PMID:24459070 (Hall JG, *Amyoplasia revisited*) — the canonical 560-patient
  Amyoplasia case series. Provides the foundational clinical description of
  Amyoplasia, supports its sporadic recurrence pattern, documents the
  characteristic symmetric limb positioning (extended elbows, equinovarus
  feet), and reports fatty-fibrous replacement of muscle. Used for the
  Amyoplasia subtype, the Sporadic inheritance entry, the Congenital
  contracture / Limb joint contracture / Talipes equinovarus phenotypes, and
  the Clinical pattern recognition diagnostic entry.
- PMID:24459095 (Hall JG, *Amyoplasia involving only the upper limbs or only
  the lower limbs*) — complementary differential-diagnosis paper for
  Amyoplasia; included in `references:` as background for the Amyoplasia
  clinical group.
- PMID:27587986 (Hall JG, Kiefer J, *Arthrogryposis as a Syndrome: Gene
  Ontology Analysis*) — synthesis paper explicitly framing decreased in utero
  fetal movement (fetal akinesia) as the shared mechanistic pathway across
  all genetic AMC subtypes. Anchors the "Decreased fetal movement"
  pathophysiology node and the Decreased fetal movement phenotype.
- PMID:25256237 (Beck AE et al., *Genotype-phenotype relationships in
  Freeman-Sheldon syndrome*) — 46-family DA2A series. Establishes MYH3 as
  causative for Freeman-Sheldon syndrome (DA2A) and quantifies the three
  recurrent missense variants (p.T178I, p.R672C, p.R672H) that account for
  the majority of DA2A cases. Used for the Heterozygous MYH3 variants
  genetic entry.
- PMID:38856159 (Morali et al., *Bi-allelic variants in MYH3 cause
  recessively-inherited arthrogryposis*) — extends MYH3 from a purely
  dominant gene (Freeman-Sheldon, Sheldon-Hall, multiple pterygium) to a
  recessive cause of distal arthrogryposis. Provides the standard
  "two-or-more body areas" clinical definition of arthrogryposis used in
  the Congenital contracture and Arthrogryposis multiplex congenita
  phenotype entries, the Autosomal recessive inheritance entry, and the
  Exome / genome sequencing diagnostic entry.
- PMID:30285720 (Li B et al., *Novel mutations in TPM2 and PIEZO2 are
  responsible for distal arthrogryposis (DA) 2B and mild DA in two Chinese
  families*) — provides a heterozygous TPM2 missense variant segregating
  with DA2B (Sheldon-Hall syndrome) in a multigenerational family. Used for
  the Heterozygous TPM2 variants genetic entry. The same paper performs
  linkage analysis with markers at TPM2, TNNI2/TNNT3, and TNNC2, which is
  used as `PARTIAL` evidence for the Heterozygous TNNI2 variants entry
  (which carries an `Associated` association rather than `Causative`,
  pending addition of a dedicated TNNI2 causative-variant citation in a
  future revision).
- PMID:32799913 (Guo P et al., Drosophila myosin DA1/DA2B models) — the
  mechanistic paper supporting prolonged actomyosin interactions as the
  proximal sarcomeric defect in DA1 and DA2B. Tagged with
  `evidence_source: MODEL_ORGANISM` for the sarcomeric contractile-protein
  dysfunction pathophysiology node and for the autosomal dominant
  inheritance characterization (their introduction frames the DAs as
  autosomal dominant skeletal muscle diseases).
- PMID:31479584 (Shriners multiauthored review, *Treatment and outcomes of
  arthrogryposis in the lower extremity*) — anchors early intensive
  physiotherapy and bracing as the central, evidence-supported management
  for AMC, and emphasizes a multidisciplinary care model.
- PMID:22875688 (Lampasi et al., *Management of knee deformities in children
  with arthrogryposis*) — enumerates the orthopedic surgical procedures
  (soft-tissue release, femoral shortening-extension osteotomy, Ilizarov
  gradual correction, femoral anterior epiphysiodesis) used to address
  residual knee contractures in AMC.

## Literature Synthesis

Arthrogryposis Multiplex Congenita (AMC) is an umbrella clinical phenotype —
defined by congenital joint contractures involving two or more different body
areas — rather than a single disease (PMID:38856159). The condition is
etiologically heterogeneous and includes more than 400 recognized genetic
disorders together with the sporadic, classical form Amyoplasia
(PMID:24459070). Across all forms, the most consistent unifying mechanistic
feature is decreased in utero fetal movement: "All types of arthrogryposis
have decreased in utero fetal movement." (PMID:27587986). Persistent fetal
hypokinesia prevents normal stretching of muscle and periarticular
connective tissue, producing fixed congenital contractures, fatty-fibrous
replacement of muscle, characteristic limb positioning (extended elbows,
equinovarus feet), and the broader fetal akinesia deformation sequence
findings (PMID:24459070, PMID:27587986).

Clinically, AMC is divided into four major groups. Amyoplasia, the most
common single form, is sporadic, "completely sporadic" in Hall's 560-patient
series (PMID:24459070), and is characterized by symmetric severe limb
contractures, fatty-fibrous muscle replacement, characteristic limb
positioning, and typically preserved cognition; it remains "a clinical
diagnosis at this time" (PMID:24459070). The distal arthrogryposis (DA)
syndromes are typically autosomal dominant disorders preferentially
affecting the hands and feet, including DA1, DA2A (Freeman-Sheldon, the
most severe), and DA2B (Sheldon-Hall) (PMID:25256237, PMID:32799913). The
multiple pterygium syndromes combine congenital contractures with pterygia
across flexural joints and include the autosomal recessive Escobar variant
and the lethal multiple pterygium syndrome. The lethal congenital
contracture syndromes (LCCS) are prenatal- or perinatal-lethal disorders
in the fetal akinesia deformation sequence spectrum.

Molecularly, the dominant DA syndromes are caused predominantly by
heterozygous variants in genes encoding sarcomeric contractile proteins.
MYH3 (embryonic myosin heavy chain) is the most common single gene cause:
"Heterozygous variants in MYH3 have been identified to cause the
dominantly-inherited distal arthrogryposis conditions, Freeman-Sheldon
syndrome, Sheldon-Hall syndrome, and multiple pterygium syndrome."
(PMID:38856159). In Beck et al.'s 46-family DA2A series, "MYH3 mutations
were found in 43/46 (93%) kindreds, with three mutations (p.T178I,
p.R672C, and p.R672H) explaining 39/43 (91%) of cases." (PMID:25256237).
MYH3 also underlies a recessive form of distal arthrogryposis
(PMID:38856159). Heterozygous TPM2 (beta-tropomyosin) variants cause DA2B
and related distal arthrogryposis phenotypes (PMID:30285720). TNNI2 (fast
skeletal troponin I) is grouped with TPM2 in the thin-filament regulatory
cluster of distal arthrogryposis candidate loci (PMID:30285720); the
present entry classifies TNNI2 with `association: Associated` and a
`PARTIAL` evidence tag, because the Li et al. paper used TNNI2 as a
linkage candidate locus rather than itself demonstrating a pathogenic
TNNI2 variant. Functional Drosophila modeling demonstrates that DA1 and
DA2B sarcomeric variants produce prolonged actomyosin interactions, which
plausibly reduces effective fetal movement and produces the congenital
contracture phenotype (PMID:32799913).

Management of AMC is lifelong and multidisciplinary, centered on early
intensive physiotherapy and orthotic bracing: "The importance of very
early and aggressive management of these deformities in the form of
intensive physiotherapy (with its various modalities) and bracing is
emphasized." (PMID:31479584). Selective orthopedic surgical procedures —
soft-tissue release, femoral shortening-extension osteotomy, gradual
correction with Ilizarov frames, and femoral anterior epiphysiodesis —
address residual contractures not corrected by conservative measures
(PMID:22875688). Care delivery emphasizes "the central role of a
multidisciplinary approach involving all stakeholders, especially the
families" (PMID:31479584). Genetic counseling is integral, given the
sporadic nature of Amyoplasia and the autosomal dominant or recessive
recurrence risks in the Mendelian forms.

## Curation Conclusions

The accepted unifying model of AMC is decreased in utero fetal movement
(fetal akinesia) producing fixed congenital joint contractures across two
or more body areas. The mechanism is gene-agnostic at the level of the
final common pathway, but converges from many proximal causes — most
prominently sarcomeric contractile-protein dysfunction in the distal
arthrogryposes (MYH3, TPM2, TNNI2). The dismech graph therefore models
three pathophysiology nodes (decreased fetal movement, sarcomeric
contractile-protein dysfunction, congenital joint contracture formation)
linked by `downstream` edges that capture the conserved final-common
pathway. Subtype assignment is clinically anchored (Amyoplasia, distal
arthrogryposis, multiple pterygium syndromes, LCCS) and is informed by
contracture distribution, associated craniofacial and prenatal features,
and family history, with exome / genome sequencing used to identify
causative Mendelian variants. Detailed gene-specific pathophysiology and
management belong in dedicated subtype entries; the present entry
itemizes only the most informative thin- and thick-filament DA genes
(MYH3, TPM2, TNNI2).
