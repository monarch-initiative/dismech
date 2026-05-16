# Dopa-Responsive Dystonia Deep Research Fallback

## Provider Attempts

No deep-research provider was invoked for this root-level entry. The two
autosomal-form subtype entries (`Autosomal_Dominant_Dopa_Responsive_Dystonia`,
`Autosomal_Recessive_Dopa_Responsive_Dystonia`) already have their own
`-deep-research-fallback.md` artifacts from prior curation runs (`falcon` and
`openai` providers were attempted there and terminated on silence; curation
proceeded from Orphanet structured records plus a bounded set of fetched
PubMed/DOI references).

This root-level entry was curated **directly from the verified literature
already cached in `references_cache/`** and shared by both subtype files; no
provider was re-run because the root scope only synthesises cross-subtype
features that were already established at the subtype level.

## Integrated Literature Synthesis

Dopa-responsive dystonia is a group of rare neurometabolic disorders in
which inherited defects of dopamine biosynthesis cause childhood-onset
dystonia with a dramatic, sustained response to low-dose levodopa. The
group is mechanistically heterogeneous but converges on a shared striatal
dopamine-biosynthesis impairment in nigrostriatal dopaminergic neurons
(`CL:0000700`, `GO:0042416`).

**Autosomal dominant DRD** — most commonly caused by heterozygous GCH1
pathogenic variants (GTPCH1-deficient DRD / Segawa disease). Rarer
dominant causes include IMPDH2 and NR4A2 variants. The upstream defect
in the GCH1/IMPDH2 arm is reduced tetrahydrobiopterin biosynthesis
(`GO:0006729`, modelled here in a separate `BH4 Cofactor Limitation`
pathophysiology node), limiting cofactor availability for tyrosine
hydroxylase. NR4A2 haploinsufficiency produces dopaminergic denervation
on DAT imaging without a clear BH4 step. PMID:20301681, PMID:8852666,
PMID:33875303 and ORPHA:98808 are the principal supporting references;
all live in `references_cache/`.

**Autosomal recessive DRD** — most commonly caused by biallelic TH
(tyrosine hydroxylase) variants. The phenotypic spectrum spans
levodopa-responsive childhood dystonia, infantile parkinsonism with
motor delay, and progressive infantile encephalopathy. Rarer biallelic
TSPOAP1 variants also occur. In TH-deficient DRD the BH4 step is intact
— the defect is at tyrosine hydroxylase itself — which is why this
root entry isolates the BH4 limitation in its own pathophysiology node
rather than placing it on the unifying dopamine-biosynthesis endpoint
(see PR review on #2654). PMID:34834538, ORPHA:101150 supporting.

**Shared clinical syndrome.** Limb dystonia (`HP:0002451`, frequently
foot-onset, with diurnal fluctuation captured via
`temporality: DIURNAL`), focal dystonia (`HP:0004373`), parkinsonism
(`HP:0001300`), and gait disturbance (`HP:0001288`, also diurnal) are
shared across genotypes. PMID:33875303 reports gait disturbance in
92.7 % and diurnal fluctuation in 91.9 % of early-onset autosomal-
dominant GCH1-deficient DRD patients.

**Shared therapy.** Low-dose levodopa (`CHEBI:15765`) with a peripheral
aromatic L-amino-acid decarboxylase inhibitor (carbidopa or
benserazide) bypasses the dopamine-synthesis bottleneck and is the
defining therapeutic feature of the disease group. PMID:20301681
("characterized by ... a dramatic and sustained response to low doses
of oral administration of levodopa") is the canonical evidence.

## Out of scope for the root entry

- Subtype-specific molecular pathways (GCH1, IMPDH2, NR4A2, TH,
  TSPOAP1) — covered in the existing subtype dismech files.
- Severe AR-DRD phenotypes such as oculogyric crises, hypotonia, and
  the encephalopathic end of the TH-deficiency spectrum — these belong
  in `Autosomal_Recessive_Dopa_Responsive_Dystonia`.
- Differential diagnosis with juvenile parkinsonism, secondary
  dystonia syndromes, and BH4-deficiency metabolic disorders outside
  the DRD spectrum.
