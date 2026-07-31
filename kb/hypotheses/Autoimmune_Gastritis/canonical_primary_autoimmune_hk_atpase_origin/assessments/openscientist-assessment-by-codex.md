# Assessment of the OpenScientist report

**Hypothesis:** Canonical primary autoimmunity against gastric H+/K+-ATPase
**Assessor:** Codex
**Verdict:** **PARTIALLY_SUPPORTED**

The report's central distinction is sound: the H+/K+-ATPase-specific CD4
effector mechanism is much better established than a single “primary” origin
for sporadic human AIG. The report then repeatedly weakens that distinction by
calling model pathways and case reports documented human initiators and by
treating clinical progression as proof of a self-sustaining immune mechanism.

## What survives review

Murine transgenic, neonatal-thymectomy, and transfer studies strongly support
H+/K+-ATPase-specific CD4 T cells as sufficient effectors. Small human
gastric-clone studies provide a concordant antigen-specific cellular signal.
The thymic result is also important but needs precise wording: ATP4A mRNA
expression alone did not delete pathogenic cells, whereas engineered ATP4B
coexpression enabled presentation and deletion
([PMID:16237067](https://pubmed.ncbi.nlm.nih.gov/16237067/)). Transgenic thymic
ATP4B prevented neonatal-thymectomy gastritis in mice
([PMID:8393475](https://pubmed.ncbi.nlm.nih.gov/8393475/)).

These experiments justify retaining the canonical effector mechanism and a
central-tolerance hypothesis. They do not prove that ATP4B-reactive T cells are
the dominant surviving repertoire in humans, or that one ATP4A-specific TCR is
necessary. TxA23 demonstrates sufficiency, not necessity
([PMID:11449363](https://pubmed.ncbi.nlm.nih.gov/11449363/)).

## Initiation and persistence are overgraded

The H. pylori studies establish cellular cross-reactivity and a few
post-eradication clinical histories, not infection-driven initiation or
self-perpetuation. The roseolovirus pathway is mechanistic in mice, not
established in humans
([PMID:35226043](https://pubmed.ncbi.nlm.nih.gov/35226043/)). Checkpoint
inhibitor gastritis provides an iatrogenic peripheral-tolerance model, but the
deeply phenotyped evidence cited is a single case and does not establish absence
of predisposition or identity with sporadic AIG
([PMID:34755133](https://pubmed.ncbi.nlm.nih.gov/34755133/)).

The prospective 498-patient cohort supports a progressive clinical course; it
does not mechanistically prove self-sustaining autoimmunity “regardless of the
initiating trigger,” and its abstract does not report a formal no-remission
endpoint ([PMID:38050966](https://pubmed.ncbi.nlm.nih.gov/38050966/)).

The genetic summary also merges unlike studies. The pernicious-anemia GWAS
identified PTPN22, PNPT1, HLA-DQB1, IL2RA, and AIRE; ABO and IFIH1 came from a
parietal-cell-antibody analysis in a type 1 diabetes cohort
([PMID:34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/),
[PMID:21829393](https://pubmed.ncbi.nlm.nih.gov/21829393/)).

Finally, the ontology candidates require correction. GO:0006968 is cellular
defense response, not central tolerance. GO:0002513 is specifically tolerance
induction to self antigen, not a generic peripheral-tolerance term.

## Disease-YAML follow-up

This assessment leaves `kb/disorders/Autoimmune_Gastritis.yaml` untouched. Its
current hypothesis description and notes nevertheless repeat report-derived
claims that need a separate evidence-curation pass:

- ATP4B is described as the thymus-absent dominant human autoantigen/repertoire;
- H. pylori mimicry, neonatal roseolovirus disruption, and checkpoint failure
  are presented together as parallel initiating pathways;
- all routes are said to converge on a self-sustaining cascade.

The safer disease-level representation is to retain the canonical
H+/K+-ATPase-specific effector mechanism, label each upstream route with its
actual species and evidence design, and keep initiation and post-trigger
persistence unresolved in sporadic humans.
