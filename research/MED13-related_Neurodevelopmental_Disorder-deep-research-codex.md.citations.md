# Citations for MED13-related neurodevelopmental disorder

Date: 2026-04-12
Issue: https://github.com/monarch-initiative/dismech/issues/1140

## Repo context

1. G2P row triage in this repo:
   - [docs/research/g2p_all_genes_row_triage_2026_03_28.tsv](../docs/research/g2p_all_genes_row_triage_2026_03_28.tsv)
   - `MED13	G2P02649	MED13-related neurodevelopmental disorder	MONDO:0032485	strong	loss of function	...	NO_DISMECH_MATCH	CRITICAL`

2. G2P gene summary in this repo:
   - [docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv](../docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv)
   - marks `MED13` as `CRITICAL` and recommends `ADD_FIRST_GENE_DISEASE_ANCHOR`

3. Local ClinGen cache in this repo:
   - [cache/clingen/gene_validity.csv](../cache/clingen/gene_validity.csv)
   - MED13 -> "complex neurodevelopmental disorder" -> `Definitive`

4. Issue requesting this reassessment:
   - https://github.com/monarch-initiative/dismech/issues/1140
   - "Research MED13-related neurodevelopmental disorder"

## Official / authoritative sources

5. NCBI Gene: MED13 mediator complex subunit 13
   - https://www.ncbi.nlm.nih.gov/gene/9969
   - Useful for official symbol, synonyms, gene function, associated condition `Intellectual developmental disorder 61`, and the key publication list.

6. ClinGen gene validity assertion URL from the local cache
   - https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_e82f63b1-ed0f-4dd0-8168-3aa4e0a4c2a9-2022-05-17T180000.000Z
   - Local cache records this as MED13 -> complex neurodevelopmental disorder -> `Definitive`, AD, dated 2022-05-17.

## Primary literature

7. Snijders Blok L, et al. De novo mutations in MED13, a component of the Mediator complex, are associated with a novel neurodevelopmental disorder.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/29740699/
   - PMID: 29740699
   - Why it matters: syndrome-defining cohort and best single paper for a first disease anchor.

8. Trivisano M, et al. MED13 mutation: A novel cause of developmental and epileptic encephalopathy with infantile spasms.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/36087421/
   - PMID: 36087421
   - Why it matters: establishes that severe epilepsy / infantile spasms can occur in the MED13 spectrum.

9. Tolmacheva E, et al. Expanding phenotype of MED13-associated syndrome presenting novel de novo missense variant in a patient with multiple congenital anomalies.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/38745205/
   - Full text: https://bmcmedgenomics.biomedcentral.com/articles/10.1186/s12920-024-01857-z
   - PMID: 38745205
   - DOI: 10.1186/s12920-024-01857-z
   - Why it matters: expands the severe congenital-anomaly end of the phenotype.

10. Intellectual Developmental Disorder of Autosomal Dominant 61 Caused by a MED13 Variant Presenting With Congenital Unilateral Sensorineural Hearing Loss: A Case Report.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/41561257/
   - PMID: 41561257
   - Why it matters: supports haploinsufficiency for truncating variants and expands the sensory phenotype to congenital unilateral SNHL.

11. Harada M, et al. Mitochondrial dysfunction in MED13 variant-associated disease: a case of infantile spasms, cardiomyopathy and hepatomegaly.
    - PubMed: https://pubmed.ncbi.nlm.nih.gov/41130977/
    - PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12549833/
    - PMID: 41130977
    - PMCID: PMC12549833
    - DOI: 10.1038/s41439-025-00327-x
    - Why it matters: important severe case report, but likely not yet sufficient to define the core mechanism of the disorder.

12. Li Z-X, et al. Med13 is involved in the radial migration and contralateral projection of cortical neurons via PlxnA4.
    - Nature / Communications Biology: https://www.nature.com/articles/s42003-026-09704-w
    - DOI: 10.1038/s42003-026-09704-w
    - Published: 2026-02-09
    - Why it matters: first direct mechanistic study tying Med13 loss to cortical neuron migration / callosal projection defects and implicating `PLXNA4`.

## Notes on use

- For a first dismech disease anchor, prioritize citations 5 through 9 plus the local repo-context items above.
- Citation 11 is best treated as phenotype-expanding rather than syndrome-defining.
- Citation 12 is currently the strongest mechanistic bridge from MED13 to cortical developmental defects and is particularly useful for pathophysiology nodes.
- The main terminology decision to preserve is that the first entry should use the MED13-specific disease concept from G2P (`MONDO:0032485`) while still acknowledging that ClinGen validity was curated against the broader umbrella `MONDO:0100038`.
