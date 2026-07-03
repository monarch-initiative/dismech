# Heart Defect-Tongue Hamartoma-Polysyndactyly Syndrome (CHDTHP) Deep Research Fallback

## Provider Attempts

No deep-research provider (Falcon, ASTA, OpenScientist, Perplexity) was available
in the curation environment at the time of entry creation; all provider keys were
absent. Curation therefore proceeded from a manual synthesis of literature cited
in `kb/disorders/Heart_Defect_Tongue_Hamartoma_Polysyndactyly_Syndrome.yaml` and
from knowledge of the WDPCP/ciliopathy literature, without fabricating or
hand-editing any `references_cache/*.md` file.

Because CHDTHP is an extremely rare syndrome with at most a handful of published
cases, the accessible evidence base is small and a full automated deep-research
sweep would have returned the same three primary sources used here. The manual
synthesis is therefore not a limitation of the entry.

## Evidence Scope Used For Curation

Three primary sources anchor the entry:

- **PMID:25427950** (Saari J, Lovell MA, Yu HC, Bellus GA; *Am J Med Genet A*
  2015) — the only published case with molecularly confirmed biallelic WDPCP
  variants. Describes a young girl with polysyndactyly, coarctation of the aorta,
  and tongue hamartomas who is compound heterozygous for a WDPCP frameshift
  mutation and a likely pathogenic missense variant. Whole-exome sequencing
  confirms the diagnosis. Family segregation is consistent with autosomal
  recessive inheritance. This paper also cites the original case reports by
  Örstavik et al. (1992) and Digilio et al. (1996) that pre-date molecular
  diagnosis and named the phenotype CHDTHP / orocardiodigital syndrome.

- **PMID:20671153** (Kim SK, Shindo A, Park TJ, Oh EC et al.; *Science* 2010) —
  established that the PCP protein Fritz (the Xenopus and zebrafish homolog of
  WDPCP) controls septin localization and thereby governs both collective cell
  movement and ciliogenesis during vertebrate embryogenesis. Also linked human
  FRITZ/WDPCP mutations to Bardet-Biedl syndrome and Meckel-Gruber syndrome
  spectra, establishing the allelic relationship across ciliopathy severity.

- **PMID:24302887** (Cui C, Chatterjee B, Lozito TP, Zhang Z et al.; *PLoS Biol*
  2013) — characterized the Wdpcp-mutant mouse. Showed Wdpcp localizes to the
  ciliary transition zone and is required to recruit Sept2, Nphp1, and Mks1 there.
  Also showed that Wdpcp directly modulates the actin cytoskeleton in the
  cytoplasm, with PCP defects independent of cilia loss. Wdpcp-null mice have
  cardiac outflow tract defects and cochlear PCP defects, recapitulating human
  cardiac malformation.

Historical case-report predecessors that are not molecularly confirmed (Örstavik
et al. 1992, *Am J Med Genet*; Digilio et al. 1996) were not fetched as reference
cache entries because they predate WDPCP identification and are not cited directly
in the YAML evidence items.

## NEC Preflight

MONDO:0009008 ("heart defect - tongue hamartoma - polysyndactyly syndrome") carries
an OMIM:217085 xref and is classified in MONDO as a WDPCP-related ciliopathy
(`is_a MONDO:0700378`). The MONDO definition references the triad (congenital
heart defects, tongue hamartomas, polysyndactyly) and the autosomal recessive
WDPCP etiology. This exactly matches the disease entity curated here.

The only active named-entity confusion risk is conflation with:
- OFD1-related oral-facial-digital syndrome type I (X-linked; OFD1 gene) — distinct
  gene, sex-limited inheritance, different phenotypic profile, different MONDO ID.
- INTU-related OFD17 — distinct transition-zone gene.
- Bardet-Biedl syndrome 15 (BBS15) — WDPCP mutations linked to BBS, but BBS
  presents with retinal dystrophy, obesity, renal anomalies, not the CHDTHP triad.
- Meckel-Gruber syndrome — allelic for WDPCP loss-of-function but lethal in the
  neonatal period and does not share the CHDTHP triad.

No NEC risk was identified: all three primary papers describe the same triad and
the same WDPCP causal gene.

## Curation Conclusions

Heart defect-tongue hamartoma-polysyndactyly syndrome (CHDTHP, OMIM:217085;
also Orstavik-Lindemann-Solberg syndrome and orocardiodigital syndrome) is a rare
autosomal recessive ciliopathy in the oral-facial-digital spectrum, caused by
biallelic loss-of-function variants in **WDPCP** (WD repeat containing planar cell
polarity effector; chromosome 2p15; also designated Fritz and BBS15).

### Molecular basis

WDPCP encodes a planar cell polarity (PCP) effector with two separable disease-
relevant functions:

1. **Transition-zone ciliogenesis**: WDPCP localizes to the ciliary transition
   zone, where it recruits Sept2, Nphp1, and Mks1 — proteins that gate access to
   the cilium. Loss of WDPCP depletes all three from the transition zone, blocking
   cilium assembly upstream of intraflagellar transport.

2. **Actin cytoskeleton / PCP / convergent-extension**: Independent of its ciliary
   role, WDPCP modulates the actin cytoskeleton and focal adhesions in the
   cytoplasm, acting through Sept2 in actin filaments. Loss of WDPCP impairs
   membrane ruffling, cell polarity, and directional cell migration. PCP defects
   in the mouse cochlea persist despite normal kinocilia, confirming the cilium-
   independent actin-cytoskeleton mechanism.

### Pathophysiology

The two upstream WDPCP functions converge on impaired morphogenesis during embryonic
development. Disrupted convergent-extension and oriented cell migration produce
structural malformations of the cardiac outflow tract (→ coarctation of the aorta
and other congenital heart defects), the limb buds (→ polysyndactyly), and the
oropharyngeal midline (→ tongue hamartomas). Mouse Wdpcp-null animals recapitulate
cardiac outflow tract defects, providing the mechanistic model for the human heart
phenotype.

Ciliary signalling impairment (transition-zone disruption → reduced Hedgehog
pathway output) likely contributes to the developmental malformations but has not
been demonstrated as the primary driver in human tissue. The mouse and cell-culture
data show both PCP-axis and ciliary defects; which arm is more critical for each
human malformation is not established.

### Clinical phenotype (molecularly confirmed)

Defined by the cardinal triad:
- **Tongue hamartomas** (benign fibrovascular nodules of the tongue)
- **Polysyndactyly** (pre- or post-axial polydactyly combined with cutaneous syndactyly)
- **Congenital heart defects** (coarctation of the aorta in the index case; broader
  heart defects in pre-molecular reports)

The phenotype is within the oral-facial-digital syndrome spectrum but distinguished
from OFD type I by the WDPCP/PCP-actin basis, autosomal recessive inheritance, and
the unique cardiac + tongue hamartoma + polysyndactyly triad without midline clefting.

### Allelic spectrum and ciliopathy broadening

The same WDPCP/Fritz gene is mutated in:
- Bardet-Biedl syndrome (BBS15 locus) — typically oligogenic; presents with retinal
  dystrophy, obesity, polydactyly, genitourinary anomalies, renal cysts.
- Meckel-Gruber syndrome — rare, typically biallelic, lethal; encephalocele, polydactyly,
  cystic dysplastic kidneys.

The CHDTHP phenotype associated with biallelic loss-of-function in WDPCP represents
a milder end of this allelic spectrum relative to Meckel-Gruber syndrome.

### Evidence gaps and uncertainty

Given the extreme rarity of CHDTHP (fewer than 10 published cases recognized as this
syndrome, with only Saari 2015 having biallelic WDPCP molecular confirmation), several
clinically important questions remain open:

1. **Prevalence and incidence**: Unknown; likely in the range of <1:1,000,000.

2. **Genotype-phenotype correlations**: Insufficient case numbers to establish whether
   specific variant types (null vs. hypomorphic) predict the cardiac or limb phenotype.

3. **Long-term outcomes**: Not reported for the WDPCP-confirmed cohort. Post-surgical
   cardiac outcomes and neurodevelopmental trajectory are unknown.

4. **Ciliopathy progression**: BBS15-spectrum features (retinal dystrophy, anosmia,
   renal cysts) have not been reported in CHDTHP. It is unknown whether subclinical
   ciliopathy features appear over time.

5. **Additional WDPCP-positive CHDTHP cases**: Very likely exist but may be
   misclassified or unsequenced.

### Entry scope assessment

The curated entry correctly captures:
- The primary molecular lesion (WDPCP transition-zone defect → ciliogenesis failure)
- The orthogonal PCP/actin axis (not cilium-dependent)
- Convergent downstream developmental malformation
- The three cardinal phenotypes with HP terms
- Autosomal recessive inheritance
- Molecular diagnosis pathway
- Supportive treatments

The entry appropriately omits speculative ciliopathy-broadening features (retinal
dystrophy, anosmia, renal cysts) not documented in the molecularly confirmed human
case. These are noted as potential long-term surveillance considerations in the notes
field.
