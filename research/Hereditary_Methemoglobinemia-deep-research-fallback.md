# Hereditary Methemoglobinemia Deep Research Fallback

## Provider Attempts

- 2026-05-09T13:04Z: `timeout 240s just research-disorder falcon Hereditary_Methemoglobinemia`
  started successfully but produced no usable research artifact during the
  bounded wait. The timeout terminated the provider process with SIGTERM.
- 2026-05-09T13:08Z: `timeout 240s just research-disorder openai Hereditary_Methemoglobinemia`
  also started successfully but produced no usable research artifact during the
  bounded wait. The timeout terminated the provider process with SIGTERM.

No provider-generated deep-research narrative was available within the bounded
runtime. Curation therefore proceeded from generated structured Orphanet
evidence and fetched PubMed caches, without hand-editing any
`references_cache/*.md` files.

## Evidence Scope Used For Curation

- ORPHA:621 provides the direct disease mapping to MONDO:0018963, ICD-10:D74.0
  and OMIM cross-references, autosomal recessive inheritance, neonatal/infancy
  onset, unknown worldwide point prevalence, CYB5R3 disease-causing gene row,
  CYB5A candidate-tested gene row, and the structured HPO phenotype table.
- PMID:18318771 supports recessive congenital methemoglobinemia as
  NADH-cytochrome b5 reductase deficiency, distinguishes type I and type II,
  identifies CYB5R3 as the encoding gene, and links type II to neurologic
  impairment and reduced life expectancy.
- PMID:31898843 supports global CYB5R3 allelic heterogeneity, autosomal
  recessive inheritance, molecular pathology, and the association of FAD-domain
  variants with the severe neurologic type II form.
- PMID:3752898 supports the biochemical redox mechanism: ferric methemoglobin is
  normally reduced back to ferrous hemoglobin, but congenital reductase
  deficiency prevents efficient reduction and produces chronically elevated
  oxidized hemoglobin, cyanosis, and impaired oxygen binding.
- PMID:27879543 supports pediatric registry evidence for type I congenital
  methemoglobinemia in Yakutia, including median methemoglobin levels, cyanosis
  on examination, hypoxic-response laboratory correlations, and regional
  prevalence estimates.
- PMID:30614390 supports type II clinical progression with neonatal cyanosis,
  severe progressive developmental delay, movement disorders, progressive
  microcephaly, CYB5R3 variants, small lentiform/caudate nuclei, reduced
  frontotemporal volume, and basal ganglia hypoplasia as a diagnostic clue.
- PMID:19480335 supports the type I erythrocyte-restricted versus type II
  generalized tissue-deficiency distinction, type II neurologic features,
  prenatal diagnosis, and symptomatic ascorbic acid treatment of cyanosis.
- PMID:22024786 supports clinical diagnostic clues and management framing for
  methemoglobinemia, including cyanosis, hypoxia, saturation gap,
  chocolate-brown blood, symptom correlation with methemoglobin level, and
  methylene blue for significantly elevated methemoglobin.
- PMID:26574897 supports case-level type II congenital methemoglobinemia
  treatment with methylene blue, including CYB5R3 compound heterozygosity,
  cytochrome-b5 reductase deficiency, lowered methemoglobin level, and modest
  behavioral improvement.

## Curation Conclusions

The curated YAML represents the CYB5R3-related autosomal recessive mechanism:
germline CYB5R3 variants reduce NADH-cytochrome b5 reductase activity in
erythrocytes and, in type II, more broadly across tissues. The enzyme defect
impairs reduction of ferric methemoglobin back to ferrous oxygen-binding
hemoglobin, causing chronic methemoglobin accumulation, reduced oxygen
transport, cyanosis, lip and nail discoloration, and exertional dyspnea. Type II
adds generalized neurologic involvement, with developmental delay, severe
intellectual disability, movement disorder, progressive microcephaly, small
basal ganglia, and frontotemporal brain volume loss. Treatment evidence is
symptomatic: methylene blue can lower methemoglobin, while ascorbic acid is
reported for cyanosis; neither provides established correction of progressive
type II neurologic disease.
