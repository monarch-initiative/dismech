# Human Microbiome Project (HMP)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

HMP provides the normal and disease-associated microbial context needed to
interpret host-microbe mechanisms. The Common Fund page describes HMP as
developing resources to study microbial communities living in and on the body
and their roles in health and disease, including reference bacterial genomes and
large metagenome datasets.

For dismech, the highest-value use is not "microbiome changed." It is
translation from microbial composition or function into host barrier, immune,
metabolic, epithelial, or neuroimmune mechanisms.

## Dismech Interpretation Pattern

Use HMP as a baseline and mechanistic contrast:

`microbial community or microbial gene function -> metabolite, pathogen
virulence, barrier interaction, immune stimulus, or epithelial stress ->
host biological process -> phenotype`

HMP is strongest when paired with disease-specific longitudinal or metabolomic
data, because healthy reference variation alone cannot prove disease causality.

## Concrete Implementation Plan

**Mode:** benchmark microbiome interpretation. HMP should be used as the
healthy/reference baseline that asks whether dismech microbiome mechanisms are
specific enough to name microbial function, body site, and host process.

**Required datasets and access path:**

- Use HMP DACC and HMP1 data model pages:
  https://www.hmpdacc.org/, https://www.hmpdacc.org/hmp/, and
  https://www.hmpdacc.org/hmp/overview/data-model/.
- Use the HMP Data Portal and NCBI BioProject `PRJNA43021` for HMP1 raw and
  value-added sequence data. HMP documentation states that microbial sequence
  data are open after host-read filtering, while filtered human sequence and
  protected metadata require qualified access through dbGaP.
- Use AWS/SRA paths for larger data. The HMPDACC resource publication describes
  raw or processed HMP data as accessible from SRA or the AWS bucket
  `s3://hmpdcc/`.
- Keep HMP1 healthy reference data separate from disease demonstration projects
  and from iHMP longitudinal disease cohorts.

**Tools and environment:**

- SRA Toolkit or AWS CLI for sequence access; QIIME2 for 16S, MetaPhlAn and
  HUMAnN for shotgun taxonomic and pathway profiles, KneadData for host-read
  filtering if reprocessing is needed.
- R `phyloseq`/`vegan` or Python `scikit-bio` for community comparisons.
- Functional interpretation should prioritize microbial pathways and
  metabolites over taxon names alone.

**Curation targets:**

- `Crohn_Disease`, `Ulcerative_Colitis`, `Pouchitis`, and
  `Small_Intestinal_Bacterial_Overgrowth`: gut microbial function linked to
  barrier injury, SCFA production, bile acids, LPS signaling, and inflammation.
- `Dental_Caries`: oral biofilm acid production and enamel demineralization.
- `Atopic_Dermatitis`: skin dysbiosis as barrier and itch-scratch amplifier,
  with causal confidence marked carefully.
- `Autism_Spectrum_Disorder`: use only as hypothesis context unless a study
  demonstrates a host neuroimmune or metabolic mechanism.

**Code to write:**

- Add `src/dismech/commonfund/hmp.py` to harvest HMP study/sample metadata into
  a manifest with body site, assay, BioProject/SRA accession, sequence type,
  open/protected status, and candidate disease mapping.
- Add `scripts/hmp_microbiome_mechanism_audit.py` to scan dismech files for
  vague "dysbiosis" claims and require a host process plus microbial function.
- Add schema-review notes for `MICROBIOME_16S`, `METAGENOMICS`,
  `METATRANSCRIPTOMICS`, and host-read-filtered sequence access.

**Graduate-student first pass:**

1. Choose one body site: gut, oral cavity, skin, or vagina.
2. Download only metadata and processed community profiles first.
3. Build a table with microbial feature, body site, host mechanism, disease
   file, and evidence strength. Convert only function-level claims into
   pathophysiology; leave pure taxonomic shifts as dataset findings.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How HMP helps |
|---------|--------------------------------|---------------|
| `Crohn_Disease` | Curated nodes: `Dysregulated Immune Response`, `Microbiome Imbalance`, `Paneth Cell Autophagy Impairment`, `Antimicrobial Defense Deficiency`, `Intestinal Barrier Dysfunction`, `IL-23/Th17 Axis Dysregulation` | HMP provides normal gut community and microbial gene-function reference for Crohn dysbiosis and antimicrobial-defense mechanisms. |
| `Ulcerative_Colitis` | Curated nodes: `Loss of Microbial Diversity`, `Loss of Keystone SCFA Producers`, `Pathobiont Expansion`, `Decreased Butyrate Production`, `Impaired Colonocyte Energy Metabolism`, `NLRP3 Inflammasome-Mediated Pyroptosis` | Directly supports a microbial function -> butyrate -> colonocyte metabolism -> inflammation mechanism pattern. |
| `Pouchitis` | Curated nodes: `Bacterial Dysbiosis`, `Mucosal Immune Dysregulation`, `Epithelial Barrier Dysfunction`, `NOD2 Genetic Susceptibility` | Use HMP/iHMP-like approaches to interpret pouch microbiota shifts after surgery. |
| `Small_Intestinal_Bacterial_Overgrowth` | Curated nodes: `Small-intestinal defense mechanism failure`, `Bacterial overgrowth in small intestine`, `Bacterial carbohydrate fermentation`, `Bile acid deconjugation and fat malabsorption`, `LPS-driven mucosal inflammation and barrier dysfunction` | Strong mechanistic microbiome example where microbial metabolism directly maps to symptoms. |
| `Dental_Caries` | Curated nodes: `Oral Microbiome Dysbiosis`, `Cariogenic Biofilm Virulence Factors`, `Disruption of Microbiome Resilience and Salivary Defense`, `Acid-Mediated Enamel Demineralization` | Use oral HMP references to contextualize cariogenic community shifts and acid production. |
| `Atopic_Dermatitis` | Curated nodes: `Epidermal Barrier Dysfunction`, `Type 2 Immune Response`, `Pruritogen-Induced Neuronal Activation`, `Scratching-Induced Barrier Injury`; trigger `Microbial Dysbiosis` | Candidate addition: skin microbiome dysbiosis -> barrier inflammation -> itch-scratch amplification. |
| `Autism_Spectrum_Disorder` | Curated nodes: `Gut Microbiota Dysbiosis`, `Enteric Nervous System Dysfunction`, `Neuroinflammation and Immune Dysregulation` | Use carefully as a mechanistic hypothesis space; avoid overclaiming causality from association studies. |

## High-Value Curation Work

- Add HMP-backed `datasets` to microbiome-heavy entries, starting with
  `Crohn_Disease`, `Ulcerative_Colitis`, `Pouchitis`,
  `Small_Intestinal_Bacterial_Overgrowth`, and `Dental_Caries`.
- Use functional microbial readouts, not only taxonomic shifts, when adding
  mechanisms: SCFA production, bile acid deconjugation, carbohydrate
  fermentation, LPS signaling, epithelial adhesion, or virulence factor delivery.
- Cross-link microbiome mechanisms to the existing
  `intestinal_barrier_dysfunction` module where diarrhea, permeability, or
  mucosal inflammation is central.
- Add confidence labels in notes when microbiome evidence is associative rather
  than causal.

## Fit for RFA-RM-26-017

Best partner datasets:

- HMP + iHMP: reference microbiome plus longitudinal host-microbiome dynamics.
- HMP + Metabolomics Workbench: microbial functional output through metabolites.
- HMP + HuBMAP: mucosal tissue and cell-neighborhood context.
- HMP + exRNA: host-microbe effects on biofluid RNA signatures.

## Sources

- NIH Common Fund HMP: https://commonfund.nih.gov/human-microbiome-project-hmp
- HMP DACC: https://www.hmpdacc.org/
- HMP data model/access: https://www.hmpdacc.org/hmp/overview/data-model/
- HMP Data Portal: https://portal.hmpdacc.org/
- NIH HMP/iHMP news release: https://www.nih.gov/news-events/news-releases/human-microbiome-project-expands-toolbox-studying-host-microbiome-interactions
