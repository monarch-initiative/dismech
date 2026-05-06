# Autosomal Recessive Dopa-Responsive Dystonia Deep Research Fallback

## Provider Attempts

- `just research-disorder falcon Autosomal_Recessive_Dopa_Responsive_Dystonia`
  started and wrote only the startup line before remaining silent during the
  bounded wait; the process was terminated with signal 15 and produced no usable
  research artifact.
- `timeout 45s just research-disorder openai
  Autosomal_Recessive_Dopa_Responsive_Dystonia` wrote only the startup line and
  was terminated by the timeout with signal 15; it produced no usable research
  artifact.

## Literature Scope Used

Because both providers failed, the curation used structured Orphanet evidence
plus manually selected PubMed references focused on tyrosine hydroxylase
deficiency, dopa-responsive dystonia treatment, and the TSPOAP1/RIMBP1
recessive dystonia mechanism.

Key cached sources:

- ORPHA:101150 for disease definition, inheritance, European prevalence,
  TH/TSPOAP1 gene rows, MONDO/OMIM/xref rows, and Orphanet phenotype-frequency
  rows.
- PMID:20301610 for GeneReviews statements on TH-deficiency clinical spectrum,
  biallelic TH molecular diagnosis, autosomal recessive inheritance, and
  levodopa treatment response.
- PMID:34834538 for expert-review support that DRD reflects defective dopamine
  synthesis and that TH catalyzes the rate-limiting step in catecholamine
  biosynthesis.
- PMID:9703425 for human mutation evidence linking TH variants to autosomal
  recessive L-DOPA-responsive dystonia.
- PMID:34054692 for a genetically diagnosed DRD cohort including TH variants
  and long-term levodopa outcomes.
- PMID:30383639 for a human AR DRD case report with TH compound heterozygosity,
  clinical features, molecular diagnosis, and low-dose levodopa response.
- PMID:33539324 for TSPOAP1 biallelic variants, human recessive dystonia,
  mouse RIMBP1-loss motor findings, and in vitro synaptic release evidence.

## Curation Conclusions

- The core TH disease mechanism is biallelic TH pathogenic variation causing
  decreased tyrosine hydroxylase activity, decreased catecholamine biosynthesis,
  and impaired central dopamine synthesis.
- The phenotype spectrum is explicitly broad: mild TH-deficient
  dopa-responsive dystonia, infantile parkinsonism with motor delay, and
  progressive infantile encephalopathy.
- All Orphanet frequent phenotype rows in ORPHA:101150 were represented with
  exact structured-cache snippets; occasional and very rare Orphanet rows that
  capture the severe spectrum were also included.
- Molecular genetic testing, CSF neurotransmitter-metabolite findings, and
  levodopa responsiveness are the main diagnostic anchors available from the
  cached evidence.
- Levodopa with a decarboxylase inhibitor is the evidence-backed treatment
  anchor; the YAML binds the action to MAXO:0000058 pharmacotherapy and the
  therapeutic agent to CHEBI:15765 L-dopa.
- TSPOAP1 was included because ORPHA:101150 lists it as a disease-causing
  loss-of-function gene and PMID:33539324 provides human, mouse, and in vitro
  support for an autosomal recessive dystonia mechanism through presynaptic
  active-zone dysfunction.
