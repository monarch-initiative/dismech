# Cerebellar Ataxia, Intellectual Disability, and Dysequilibrium (CAMRQ) Deep Research Fallback

## Provider Attempts

No interactive deep-research provider artifact was generated for the initial
CAMRQ curation. This fallback document records the literature sources that
were used to construct the entry, along with the curation conclusions
surfaced when addressing claude-review feedback on PR #2696 (issue #2684).

No `references_cache/*.md` files were hand-edited; all PMIDs cited below were
fetched with `just fetch-reference` against the live PubMed E-utilities API.

## Evidence Scope Used For Curation

- **PMID:16080122** (Boycott et al., 2005) — original Hutterite VLDLR
  homozygous deletion paper. Source for VLDLR/CAMRQ1 identification,
  inferior cerebellar hypoplasia with cerebral gyral simplification, and
  the role of VLDLR in Reelin signaling and neuroblast migration.
- **PMID:21885617** (Gulsuner et al., 2011, *Genome Res*) — homozygosity
  mapping and targeted sequencing identification of *WDR81* p.P856L as the
  cause of cerebro-cerebellar hypoplasia with quadrupedal locomotion in a
  consanguineous Turkish kindred. Source for human CAMRQ2 genetic evidence,
  cerebellar peduncle atrophy, and Purkinje-cell-layer WDR81 expression.
- **PMID:27390838** (Doldur-Balli et al., 2015, *BMC Neurosci*) — zebrafish
  *wdr81* characterization confirming BEACH/WD40 domain architecture and
  developmental expression in Purkinje cells. Source for the conserved
  endolysosomal/autophagy role tagged `MODEL_ORGANISM`.
- **PMID:31612321** (Mikolajczak et al., 2019) — ATP8A2-related CAMRQ4
  phenotype spectrum and functional studies showing loss of
  phosphatidylserine-activated ATPase activity in missense alleles. Source
  for CAMRQ4 mechanism and the CAMRQ4-distinguishing global developmental
  delay / encephalopathy phenotype.
- **PMID:38581205** (Kaiyrzhanov et al., 2024, *Mov Disord*) — clinical and
  molecular spectrum of autosomal recessive CA8-related cerebellar ataxia
  (27 patients, 14 families). Source for the CAMRQ3 distinguishing
  progressive superior vermis atrophy, the CA8 / IP3R1 Purkinje-cell
  calcium-signaling mechanism, and ca8-knockout zebrafish recapitulation.
- **PMID:42051465** (Jawabri et al., 2026, *Hum Mutat*) — first African
  family with CAMRQ1, novel VLDLR p.P565Q variant retained in the ER.
  Source for the CAMRQ-wide clinical signature (cerebellar ataxia,
  hypotonia, intellectual disability, delayed ambulation, sometimes
  quadrupedal locomotion) and for the four-gene CAMRQ subtype list.

## Curation Conclusions

The accepted disease model is a clinically and genetically heterogeneous
group of four autosomal-recessive non-progressive cerebellar disorders
(CAMRQ1-4), unified by:

- A convergent neuroanatomical substrate of cerebellar hypoplasia or
  atrophy with prominent Purkinje cell involvement.
- A convergent clinical phenotype of ataxia, intellectual disability,
  hypotonia, delayed ambulation, and sometimes quadrupedal locomotion.
- Distinct molecular mechanisms per subtype:
  - **CAMRQ1 / VLDLR**: disrupted Reelin signaling → impaired neuronal
    migration → cerebellar lamination defect.
  - **CAMRQ2 / WDR81**: BEACH/WD40 endolysosomal-trafficking and selective
    autophagy defect in Purkinje cells.
  - **CAMRQ3 / CA8**: loss of IP3R1 inhibition by CA8 in Purkinje cells →
    dysregulated calcium signaling → progressive superior vermis atrophy.
  - **CAMRQ4 / ATP8A2**: loss of P4-type phosphatidylserine flippase
    activity → loss of neuronal membrane lipid asymmetry.

Mechanistic nodes for all four subtypes converge on a single
"Cerebellar Hypoplasia and Purkinje Cell Dysfunction" pathophysiology node
whose downstream output is the clinical motor/cognitive dysfunction node.

## Notes for Future Refresh

- A live deep-research provider run (e.g. `just research-disorder asta
  Cerebellar_Ataxia_Intellectual_Disability_and_Dysequilibrium`) would be
  valuable to expand frequency data, MorPhiC/iPSC cellular phenotype
  coverage, and rare/atypical features (e.g. epilepsy, pyramidal signs in
  CAMRQ3).
- Subtype names use short slug-style identifiers (`CAMRQ1`-`CAMRQ4`) as
  foreign-key targets per the subtype-naming convention in CLAUDE.md;
  `display_name` carries the verbose form.
