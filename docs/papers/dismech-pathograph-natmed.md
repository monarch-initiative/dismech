---
title: "Pathographs: an integrative causal representation of disease mechanism for translational medicine"
target_journal: Nature Medicine (Perspective / Resource)
authors:
  - Christopher J. Mungall (LBNL, Monarch Initiative)
  - J. Harry Caufield (LBNL)
  - [co-authors TBD]
draft_status: working draft
revision_notes:
  - Tightened abstract to ~180 words, restructured as context-gap-approach-impact.
  - Removed numbered section headings; adopted short declarative headings in Nature style.
  - Reduced first-person opinion language ("we argue", "we believe", "we claim"); converted to evidence statements where possible.
  - Replaced vague claims with concrete numbers from the slide deck (Th17 cluster odds ratios, Fanconi 19 nodes, 6.1% validated GWAS rate, ~500 disorders).
  - Added four figure callouts with placeholders and in-text "(Fig. N)" references.
  - Boxed the mechanism-modules and validation-stack content as Box 1 and Box 2.
  - Inserted numeric reference markers [N] and a placeholder References section.
  - Cut meta-commentary and redundant sentences; tightened paragraph energy throughout.
  - Suggested alternative titles in a top-of-file HTML comment.
---

<!--
Alternative titles considered:
  - "Pathographs: a causal substrate for mechanism-aware medicine"
  - "An evidence-grounded causal model of disease for the new-approach-methodology era"
  - "Dismech: open pathographs for translational disease mechanism"
-->

## Abstract

Clinical decisions about a genetic variant, an exposure, or a candidate therapy still rest on an implicit, expert-held model of *why* a disease presents the way it does. That mechanistic model is rarely written down in a form a clinician, a regulator, or an artificial intelligence system can interrogate, and the new approach methodologies (NAMs) that now substitute for animal data — organoids, iPSC-derived multicellular systems, genome-scale perturbation screens — have no shared interpretive layer mapping their readouts to human disease. We present dismech, an open knowledge base that represents disease mechanism as a **pathograph**: a typed, directed, evidence-backed causal graph linking aetiology, pathophysiology, phenotype, treatment, and the assays that support each claim. The pathograph encodes competing mechanistic hypotheses and explicit knowledge gaps as first-class objects, and is built collaboratively by curators and autonomous research agents under deterministic validation. Dismech currently covers approximately 500 disorders with ten conserved mechanism modules and integrates NAM datasets, ClinGen gene–disease validity, Orphanet, and ClinicalTrials.gov. The resource provides a substrate for mechanism-aware differential diagnosis, drug repurposing, GWAS interpretation, NAM-based regulatory science, and auditable clinical AI.

## A missing causal substrate for translational medicine

Three trends are converging on the same gap. Large language models trained on clinical text now meet or exceed clinicians on benchmark tasks but cannot account for *why* an answer is correct in mechanistic terms, and their failure modes are difficult to predict because the substrate is statistical rather than causal [1]. The FDA Modernization Act 2.0 and analogous policies have opened the door to NAMs as primary evidence for human disease, but the interpretive layer that maps a NAM readout to a human phenotype, a target tissue, and a therapeutic decision remains ad hoc [2]. And the molecular and clinical data layers themselves are maturing: GWAS, rare-variant burden tests, Perturb-seq atlases, and clinical trial registries each describe a slice of disease, but the joins between them are weak [3,4].

The common shortfall is the absence of an explicit, machine-readable causal model of the disease itself. Existing resources solve adjacent problems well — OMIM and the Human Phenotype Ontology (HPO) capture phenotype associations [5]; KEGG and Reactome describe canonical pathways [6,7]; ClinVar and ClinGen describe variant pathogenicity [8]; DrugBank and OpenTargets describe drug–target relationships [9,10] — but none encode the directed chain *variant → molecular dysfunction → cellular phenotype → tissue effect → clinical phenotype → treatment* together with the evidence supporting each edge and the alternative chains that competing schools endorse. That chain is what a clinician implicitly reasons over, and what a regulatory reviewer expects when a NAM dossier substitutes for an animal study.

Dismech provides this substrate. It is an open knowledge base covering approximately 500 disorders, structured around a pathograph data model (Fig. 1), built collaboratively by domain experts and AI agents under deterministic validation, and designed to interoperate with both upstream evidence generators (NAMs, structured databases, autonomous research agents) and downstream applications (phenotype-driven differential diagnosis, mechanism-guided drug repurposing, GWAS interpretation, regulatory science).

**Figure 1 |** The pathograph data model: six node types (genetic, environmental, pathophysiology, biochemical, phenotype, treatment) bound to community ontologies, connected by typed causal edges carrying evidence items with primary identifiers and verbatim snippets. *[FIGURE PLACEHOLDER]*

## The pathograph

A pathograph is a typed, directed graph whose nodes are biological entities on the disease causation chain and whose edges are causal relations supported by evidence. Six node types are first-class (Table 1). Edges are directional and typed (causes, upregulates, ameliorates, is diagnostic of). Each edge carries an evidence list in which every item cites a primary identifier — a PMID, DOI, NCT trial number, Orphanet entry, ClinGen assertion ID, or NAM dataset accession — together with the verbatim snippet supporting the claim and a classification of whether the evidence supports, refutes, partially supports, or contradicts it.

**Table 1.** Pathograph node types and their ontology bindings.

| Node type | Examples | Community standards |
|---|---|---|
| Genetic factor | *FBN1* loss of function; gain-of-function *FGFR3* | HGNC; ClinGen validity assertions |
| Environmental factor | UV exposure, gluten ingestion, SARS-CoV-2 infection | ECTO, MeSH |
| Pathophysiology mechanism | Type 2 immune response; replication fork collapse | GO biological process, Cell Ontology, UBERON |
| Biochemical state | Elevated phenylalanine; cytotoxic glutamine | ChEBI |
| Phenotype | Aortic root aneurysm; pancytopenia; dyspnea | HPO |
| Treatment | Anti-TNF biologic therapy; PARP inhibition | MAXO, NCIT, ChEBI |

The downstream effects of this design are concrete. Because the same node type is reused across diseases, an "inflammatory bone marrow microenvironment" node in Fanconi anaemia and a similar node in myelodysplastic syndrome become directly comparable. Because treatments are nodes with explicit `target_mechanisms` edges to the pathophysiology they modify, the pathograph encodes the *rationale* for a therapy, not only an indication. Because environmental and genetic factors are sibling node types, complex diseases such as asthma, inflammatory bowel disease, and long COVID are modelled in the same idiom as Mendelian disease.

Even partial pathographs reshape the questions a knowledge base can answer. The dismech Fanconi anaemia entry encodes 19 mechanism nodes linking *FANCA/B/C/...* loss of function through replication fork instability to bone marrow failure, hyperpigmentation, and predisposition to specific cancers (Fig. 2). With this graph one can ask which phenotypes are explained by the bone-marrow-failure subgraph and which require the genome-instability subgraph, and flag patient phenotypes unexplained by either. The decomposition is currently performed implicitly by specialists; the pathograph makes it inspectable.

**Figure 2 |** Worked example pathograph for Fanconi anaemia, with 19 mechanism nodes and overlaid hypothesis groups for the bone-marrow-failure and genome-instability subgraphs. *[FIGURE PLACEHOLDER]*

> **Box 1 | Mechanism modules: encoding conserved pathological motifs**
>
> Many diseases share conserved mechanistic motifs. The fibrotic response — tissue injury, mesenchymal cell activation, myofibroblast differentiation, excessive ECM deposition, organ dysfunction — recurs across liver cirrhosis, idiopathic pulmonary fibrosis, systemic sclerosis, and chronic kidney disease. Adaptive immune resistance via checkpoint upregulation recurs across solid tumours. Synthetic lethality between homologous recombination repair deficiency and PARP inhibition recurs across *BRCA1/2*-driven cancers.
>
> Dismech captures these motifs as **mechanism modules**, structurally identical to disease entries. A disease pathograph node declares conformance to a module node via a `conforms_to` reference; this is checked for consistency (organ-specific specialisation of cell types, expected downstream edges) but not inherited — duplication is deliberate, because disease-specific specialisation matters clinically. Current modules cover the fibrotic response, immune checkpoint blockade, HRR/FA–BRCA synthetic lethality, RTK/GRB2 signalling adaptation, PARP/PARG/viral macrodomain antiviral countermeasures, intestinal barrier dysfunction, ER protein storage disease, meiotic prophase failure, neural-crest melanocyte deficiency, and pentanucleotide repeat RNA toxicity. Each module is itself an object of curation and revision and carries its own knowledge gaps and competing hypotheses.

## Integrating NAMs, genetics, drugs, and trials

NAM datasets enter the pathograph as evidence on existing edges, as new mechanism nodes when they reveal previously unrepresented biology, or as datasets attached to a hypothesis (Fig. 3). The MorPhiC Consortium produces null alleles of human genes in iPSC-derived multicellular systems and measures molecular and cellular phenotypes [11]; dismech ingests these as evidence with `evidence_source: IN_VITRO` attached to phenotype descriptors flagged as `category: Cellular`, with a dataset accession (`morphic:GENE`) pointing back to the primary data. Perturb-seq atlases fit the same way: a T-cell Perturb-seq study reporting that a regulator cluster (e.g., the IRF4/BATF/STAT3-centred Th17 cluster) is enriched in genes from an autoimmune GWAS becomes evidence on the relevant pathophysiology node [4]. Organoid drug-response studies plug into treatment nodes.

The dividend is that NAM data stop being orphan readouts. A cardiomyocyte differentiation phenotype in an *ISL1*-null iPSC system becomes an edge in the congenital heart disease pathograph, immediately adjacent to a human clinical phenotype and a gene–disease validity assertion. Regulatory uses of NAM data require this kind of mapping [2]; dismech provides the substrate.

**Figure 3 |** Mapping new approach methodologies onto pathographs. Iso-genic iPSC cellular phenotypes, organoid drug responses, and Perturb-seq regulator clusters attach as evidence to specific edges in the existing causal graph, anchored by gene, cell type, and biological process. *[FIGURE PLACEHOLDER]*

Genetic basis is encoded with HGNC-bound gene identifiers, allele-level detail where relevant, inheritance, and links to ClinGen gene–disease validity and dosage-sensitivity assertions [8]. Treatments distinguish the medical action (e.g., pharmacotherapy, bound to MAXO or NCIT) from the therapeutic agent (e.g., duloxetine, bound to ChEBI or NCIT), enabling drug-level queries across diseases. Clinical trials are first-class objects bound to ClinicalTrials.gov NCT identifiers with target phenotypes that connect a trial back to the phenotype nodes it addresses. Comorbidity edges between diseases are supported by EHR disease-trajectory data, literature, GO enrichment, and genetic correlation, with directionality preserved where the underlying study supports it. The power emerges from integration: a query for "diseases whose treatments target the same pathophysiology module" returns mechanism-justified repurposing candidates rather than surface-level similarity.

## Mechanistic uncertainty as a first-class object

The mechanistic literature is messy. Multiple schools of thought may co-exist for years — the amyloid cascade, tau-first, neuroinflammation, and vascular hypotheses in Alzheimer disease [12]; the viral persistence, autoimmune, microclot, mast-cell, and microbiome models in long COVID [13]. Some claims are well established but lack a quotable primary source. Some questions have no current answer. Collapsing the literature into a single confident narrative is a category error for a translational substrate; dismech instead encodes uncertainty explicitly through four mechanisms.

First, **mechanistic hypotheses** are objects on a disease or module, each with a stable `hypothesis_group_id`, a `hypothesis_label`, a status (CANONICAL, ALTERNATIVE, EMERGING, REFUTED), a description, and an evidence list. Causal edges opt into one or more hypothesis groups via `hypothesis_groups`; a disease can therefore carry multiple parallel causal subgraphs that share some nodes and diverge on others. The Alzheimer disease entry currently carries amyloid cascade, tau neurodegeneration, neuroimmune/glial amplification, synaptic failure, autophagy–lysosomal clearance, vascular/BBB clearance, and HSV-1 reactivation hypothesis groups. The long COVID entry carries persistence, autoimmune, microclot, mast-cell neuroimmune, and microbiome dysbiosis groups. The pathograph is therefore not a single tree but a set of overlapping causal narratives, each independently citable.

Second, **knowledge gaps** are first-class records (`kind: KNOWLEDGE_GAP`) with a status (OPEN, ADDRESSED), a rationale, an `attaches_to` reference anchoring the gap to specific pathograph nodes, and an optional list of `proposed_experiments` — including NAM-based experiments — that would resolve it. This treats "we do not yet know" as a positive assertion, making the resource a roadmap for *what to investigate next*.

Third, every evidence item carries a **support classification** (SUPPORT, REFUTE, PARTIAL, NO_EVIDENCE, WRONG_STATEMENT). Refuting citations are retained on the record rather than silently deleted.

Fourth, every evidence item carries an **evidence source** (HUMAN_CLINICAL, MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL, OTHER) recording the kind of study that supports the claim. This matters when interpreting NAM data: an iPSC-derived cardiomyocyte phenotype is IN_VITRO evidence and is the appropriate support for a cellular phenotype, but should not stand alone as support for a clinical phenotype.

A user can therefore ask which claims in a disease rest only on model-organism data, which hypothesis groups are competing for which phenotypes, and which open knowledge gaps could be addressed by which NAMs — and obtain answers.

## Closing the loop with autonomous research agents

A mechanistic knowledge base is most useful when it is continuously interrogated against the primary literature. Static curated reviews go stale within a year or two, and the volume of relevant mechanistic publications exceeds what any individual curator can track.

Dismech is designed to interoperate with autonomous research agents, foremost OpenScientist, which performs multi-hour deep investigations of a focused biomedical question with iterative search, hypothesis refinement, and explicit citation tracking [14]. The integration is direct: every mechanistic hypothesis on a disease can seed an OpenScientist run, configured with the existing hypothesis YAML as the seed claim and asked to support, refute, qualify, or compete with it against the current literature (Fig. 4). The output is captured as a structured report alongside a per-citation index, with provider, model, duration, and citation count recorded in the frontmatter for reproducibility.

To date, this loop has run across more than one hundred hypothesis groups spanning neurodegenerative disease (Alzheimer, Huntington, ALS, Parkinson), metabolic disease (porphyrias, ketogenesis disorders, transaldolase deficiency, Tangier, abetalipoproteinemia), oncology (high-grade serous ovarian cancer POLQ resistance), infectious and post-infectious disease (COVID-19 macrodomain biology, long COVID variants), and Mendelian disease (cystic fibrosis, sickle cell, haemophilia, Friedreich ataxia, Rett, Fragile X, adrenoleukodystrophy, Gaucher, Wilson, achondroplasia). Each run produces a citation-grounded narrative that human curators triage into the pathograph: confirmed claims become evidence on existing edges, new mechanism nodes capture previously unrepresented biology, and unresolved disputes become competing hypothesis groups or new knowledge gaps.

**Figure 4 |** Closed-loop interaction between dismech and OpenScientist. A knowledge gap or hypothesis on a pathograph node generates a focused agent prompt; the agent returns a citation-grounded report; deterministic validators check identifiers and verbatim snippets; a human curator triages findings back onto the pathograph. *[FIGURE PLACEHOLDER]*

This is a different relationship between an autonomous agent and a knowledge base than is usually proposed. The agent does not write to the knowledge base; it writes evidence for a curator to act on. The pathograph determines which questions are worth asking — a knowledge gap on a specific node generates a focused prompt — and the place where the agent's findings are made permanent and inspectable. Hallucinated citations and misquoted snippets, a documented failure mode of current deep-research systems [15], are caught by deterministic validators before reaching the knowledge base.

> **Box 2 | Construction under deterministic validation**
>
> Dismech is built collaboratively by domain experts and AI agents (Claude and Codex via the Claude Code and Claude Agent SDK harnesses). Agents propose new entries, enrich existing ones, and respond to compliance scoring that identifies the lowest-coverage files. Resource integrity does not depend on agent integrity. It depends on three deterministic validation layers: a schema validator, an ontology term validator that checks every identifier against the authoritative ontology, and a reference validator that requires every evidence snippet to be a verbatim substring of a cached primary source. The validators are mechanical and reproducible; reference caches and ontology snapshots are version-controlled. Every change passes through GitHub-based review and continuous integration, and an automated AI reviewer performs a second pass focused on curation guidelines.
>
> The encoding details — disease entries as YAML, validated against a LinkML schema, with ontology bindings to HPO, GO, CL, UBERON, MONDO, MAXO, ChEBI, NCIT, HGNC, and GENO — are deliberately invisible at the user level. What matters at the resource level is conformance to community standards: dismech reuses identifiers that the rest of biomedicine already uses, and exports to the Biolink Model KGX format so that the pathograph can be consumed by existing knowledge-graph infrastructure including the Monarch KG and the NCATS Biomedical Data Translator [16,17].

## Applications

### Mechanism-aware differential diagnosis

Phenotype-driven differential diagnosis against HPO-annotated disease databases is well established [5]. Pathograph-aware matching adds two capabilities. First, phenotype frequency on a per-genotype basis means that excluded phenotypes are honoured: pancytopenia is very frequent in Fanconi anaemia overall but explicitly excluded in *FANCD1/BRCA2* and FA-S/*BRCA1* subtypes, and a phenomatcher that respects this returns a different ranked list than one that does not. Second, when a patient phenotype is absent from the candidate disease's phenotype list, the pathograph allows a *mechanistic* answer to "is this consistent?" Fever is not a primary Fanconi anaemia phenotype, but the bone-marrow-failure → neutropenia → infection-susceptibility subgraph supports it. The dismech phenomatcher takes a GA4GH Phenopacket [18], performs ontology-aware matching, weights by curated frequency, and uses the pathograph to generate explanations for non-exact matches, returning a probability estimate with a per-phenotype explanation chain rather than a black-box score.

### Mechanism-guided drug repurposing

Pathograph treatments are bound to the mechanisms they target. Two diseases whose pathographs share a mechanism module are immediate repurposing candidates for therapies that target that module — and the shared module identifies *which* therapies. The fibrotic response module is the most developed example: it predicts that anti-fibrotic agents validated in idiopathic pulmonary fibrosis should be considered in hepatic, renal, and cutaneous fibrosis with the same mechanistic rationale, made explicit and citable rather than analogical. The immune checkpoint blockade module similarly explains why a checkpoint inhibitor active in one solid tumour is a candidate in another with the same adaptive-immune-resistance node, and why diseases lacking that node are not.

### GWAS and Perturb-seq interpretation

Pathographs serve as a validation layer for pipelines that propose gene → program → trait relationships from GWAS combined with Perturb-seq [4]. Each gene → program → trait triple is classified as CONFIRMED (all elements documented and connected in dismech), PARTIAL (some elements present, chain incomplete), NOVEL (absent from dismech, a candidate for curation), or CONTRADICTED (dismech documents an opposite effect). Applied to the recent T-cell Perturb-seq atlas of 22 million primary CD4+ T cells, validation against dismech rose from 2.7% (baseline) to 6.1% across twelve autoimmune diseases as targeted curation incorporated pipeline-flagged candidate genes (BACH2, TNFAIP3, STAT3, IL10, CD28, EGR2, ETS1, IRF4, IKZF1, SMAD3, SATB1). The standout signal was a six-gene regulator cluster (IRF4, BATF, STAT3, JUNB, IPMK, NUP188) centred on Th17 differentiation, with odds ratios of 58.2 in Crohn disease, 38.1 in atopic dermatitis, 26.9 in psoriasis, 24.0 in inflammatory bowel disease (merged), and 16.9 in multiple sclerosis. This finding drove dismech curation of an atopic dermatitis entry and strengthened Th17 pathophysiology (GO:0072538) across five autoimmune disorders. The loop is bidirectional: pipeline-flagged novel candidates prioritise curation; the resulting curation supports the next round of pipeline validation.

### NAMs and regulatory science

The pathograph is the bridge between a NAM readout and a regulatory or clinical decision. When an iPSC-derived disease model recapitulates a cellular phenotype, the pathograph identifies which clinical phenotype it is upstream of and via what mechanism — and which clinical phenotypes it does *not* address. When an organoid drug screen identifies a candidate, the pathograph identifies which mechanism node it targets and which other diseases share that node. When a NAM dataset diverges from a human clinical observation, the pathograph localises the divergence to a specific edge, generating a hypothesis-shaped follow-up rather than a diffuse failure. In our view, this is the most consequential medium-term application: the bottleneck in NAM adoption is not the assays themselves but the interpretive infrastructure, and an open, citable, integrative causal model is that infrastructure.

### Clinical AI grounding

LLM-based clinical assistants are being deployed in diagnostic and therapeutic decision support, but they fail in modes that are difficult to predict and audit [1]. A pathograph offers an explainable, ontology-grounded substrate: every assertion is bound to a primary identifier and an exact snippet, and the causal chain is traversable rather than implicit. When a clinical AI proposes that a patient symptom is explained by a particular mechanism, the pathograph either supports that chain end-to-end with citations or does not — and the failure mode is visible. Dismech is not ready for direct clinical deployment, but it is the kind of substrate that would make such deployment auditable.

## Limitations

Dismech is incomplete. Its current approximately 500 disorder entries are a small fraction of the Mondo disease space; depth of curation varies; mechanism modules are early. Some entries depend heavily on review-article evidence rather than primary studies because suitable quotable abstracts could not be located, and these are marked rather than silently filled. Knowledge gaps are themselves under-curated. The balance between hypothesis groupings and a single canonical narrative is an editorial choice that varies by disease. Snippets are limited to publication abstracts and structured-database fields, restricting mechanistic detail; full-text-aware evidence is on the roadmap. Coverage of NAM datasets is limited to a handful of consortium outputs (MorPhiC anchor genes, selected Perturb-seq atlases); systematic ingestion of NAM dataset catalogues is a priority. Coverage of paediatric and rare disease is stronger than coverage of common chronic disease, where the literature is broader and editorial choices harder. The reference cache layer has a measured ~1% hallucination rate that the validation stack catches but does not prevent at source.

## Outlook

The translational pipeline needs an explicit, evidence-backed, integrative causal representation of disease mechanism — one that brings together genetics, environmental exposures, pathophysiology, NAM readouts, drugs, trials, and the assays and datasets that support each claim, and that encodes mechanistic uncertainty honestly as competing hypotheses and open knowledge gaps. Dismech is our attempt at that representation. It is designed as the substrate that autonomous research agents investigate, that NAM dossiers map onto, that mechanism-aware repurposing draws from, and that clinical AI can be grounded against. The pathograph data model and the validation stack are mature; the content is growing. We will scale curation through agent-assisted pipelines, expand NAM dataset ingestion in collaboration with consortium producers, and integrate with the Monarch KG and NCATS Translator so that pathograph-derived edges flow into the broader translational graph. The pathograph is open and citable; we invite the community to interrogate, extend, and challenge it.

## Data and code availability

Knowledge base: <https://github.com/monarch-initiative/dismech>. Browsable resource: <https://monarch-initiative.github.io/dismech/>. All disorder entries, mechanism modules, schema, validation tooling, and reference caches are version-controlled and openly licensed.

## Acknowledgements

Monarch Initiative; LBNL Environmental Genomics & Systems Biology; the OBO Foundry, HPO, MONDO, MAXO, Cell Ontology, GO, and UBERON development teams; ClinGen; Orphanet/Orphadata; ClinicalTrials.gov; the MorPhiC Consortium; and the OpenScientist development team. Funded by [TBD].

## References

[1] [TBD: representative review of LLM clinical benchmark performance and failure-mode analysis]
[2] [TBD: FDA Modernization Act 2.0 and follow-on regulatory guidance on NAMs]
[3] [TBD: GWAS catalogue / large-scale common-variant survey]
[4] [TBD: Ota et al. 2025 — GWAS + Perturb-seq causal-graph paper used in the autoimmune validation]
[5] [TBD: HPO and OMIM resource citations]
[6] [TBD: KEGG]
[7] [TBD: Reactome]
[8] [TBD: ClinVar / ClinGen gene–disease validity framework]
[9] [TBD: DrugBank]
[10] [TBD: OpenTargets]
[11] [TBD: MorPhiC Consortium / Ota null-allele iPSC paper, PMID:39939790]
[12] [TBD: Alzheimer disease — representative review covering amyloid, tau, neuroinflammation, vascular hypotheses]
[13] [TBD: Long COVID — representative review covering persistence, autoimmune, microclot, mast-cell, microbiome models]
[14] [TBD: OpenScientist / autonomous deep-research agent reference]
[15] [TBD: Deep-research / LLM citation hallucination measurement study]
[16] [TBD: Monarch Initiative / Monarch KG]
[17] [TBD: NCATS Biomedical Data Translator]
[18] [TBD: GA4GH Phenopackets standard]
