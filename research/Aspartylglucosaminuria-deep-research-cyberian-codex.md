---
provider: cyberian-codex
model: codex-local-synthesis
cached: true
start_time: '2026-05-03T16:14:23Z'
end_time: '2026-05-03T16:14:23Z'
duration_seconds: 0.0
template_file: codex_local_literature_synthesis_after_provider_timeouts
template_variables:
  disease_name: Aspartylglucosaminuria
  mondo_id: MONDO:0008830
  category: Mendelian
source_attempts:
- provider: falcon
  status: interrupted_after_no_output
- provider: openai
  status: interrupted_after_no_output
- provider: asta
  status: discarded_irrelevant_retrieval
citation_count: 7
---

## Question

Provide a concise mechanistic review of Aspartylglucosaminuria pathophysiology,
inheritance, causal gene, biochemical signature, cellular pathology, progression,
major clinical phenotypes, and treatment-relevant mechanisms.

## Output

Aspartylglucosaminuria (AGU) is an autosomal recessive lysosomal storage disease
caused by biallelic pathogenic variants in **AGA**, the gene encoding
aspartylglucosaminidase/glycosylasparaginase. AGA is required for hydrolysis of
the protein-oligosaccharide linkage in Asn-linked glycoproteins during lysosomal
turnover; loss of enzyme activity causes storage of glycoasparagines, including
GlcNAc-Asn/aspartylglucosamine, in tissues and body fluids (PMID:10571008;
PMID:27906067; https://pubmed.ncbi.nlm.nih.gov/27906067/).

The most direct molecular mechanism is loss of mature active AGA. Structural and
cell-biologic work shows that disease-causing AGA variants can disrupt folding,
dimerization in the endoplasmic reticulum, intracellular maturation/processing,
or active-site function, converging on reduced lysosomal enzyme activity
(PMID:11309371). The Finnish founder allele causes a C163S amino acid
substitution and is a common cause in Finland, while broader clinical reviews
describe more than 30 pathogenic AGA variants worldwide (PMID:27906067;
PMID:33439067).

The immediate biochemical consequence is accumulation and urinary excretion of
glycoasparagine substrate. Reviews describe accumulation of undegraded
glycoasparagines in tissues and body fluids, and translational studies identify
large amounts of urinary GlcNAc-Asn as a diagnostic biomarker for AGU
(PMID:27906067; PMID:33186692).

The nervous system is the most clinically important target. Biochemical reviews
emphasize severe effects on neuronal cells, and the AGU mouse model shows absent
AGA activity, urinary aspartylglucosamine excretion, lysosomal storage vacuoles
in neurons and glia, brain atrophy, and deep-gray-matter MRI abnormalities that
parallel human disease (PMID:10571008; PMID:9425233). This cellular storage
mechanism accounts for childhood onset with delayed speech and learning,
progressive intellectual disability, psychomotor decline, gait/motor
abnormalities, dyskinesia, and seizures (PMID:27906067; PMID:33439067).

AGU is also systemic. Clinical reviews describe coarse facial features, skeletal
abnormalities, connective-tissue overgrowth, hernias, recurrent respiratory and
ear infections, and progressive physical disability (PMID:27906067;
PMID:33439067). These features are consistent with non-neuronal lysosomal
storage and connective-tissue involvement, though the strongest mechanistic
evidence is for substrate accumulation and lysosomal storage rather than a
single downstream structural pathway.

There is no approved curative or disease-modifying therapy. Current management
is supportive and anticipatory. Reviews report that human enzyme replacement
trials have not been reported and allogeneic stem-cell transplantation has not
proved effective. Preclinical enzyme and gene-transfer studies show biological
correctability: adenovirus-mediated AGA reduced lysosomal storage in liver and
partly in periventricular brain, while systemic AAV9/AGA in Aga-deficient mice
produced sustained AGA activity, dose-dependent substrate clearance, reduced
gliosis, and preservation of cerebellar Purkinje neurons (PMID:27906067;
PMID:9930336; PMID:33186692).
