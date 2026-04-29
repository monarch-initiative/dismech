# dismech Use Cases

This document outlines use cases for the Disorder Mechanisms Knowledge Base (dismech),
organized by audience and application domain.

## Clinical & Research

### Differential Diagnosis Support

Given a set of phenotypes (HP terms), query dismech to find disorders sharing those
phenotypes and rank by overlap. The structured phenotype descriptors with ontology
bindings make this computationally tractable.

### Mechanism-Based Drug Repurposing

Two diseases that share pathophysiology (e.g., same biological processes, same cell
types affected) but have different treatments could be candidates for cross-disease
drug repurposing. The structured `pathophysiology`, `cell_types`, and `treatments`
fields enable systematic comparison.

### Comorbidity Prediction

The `comorbidities` and disease trajectory data can be mined to identify unexpected
disease co-occurrences and their shared mechanistic basis, going beyond epidemiological
correlation to mechanistic explanation.

### Clinical Trial Matching

With `clinical_trials`, `phenotypes`, and `genetic_basis` structured and ontology-linked,
patients could be matched to relevant trials based on their genotype-phenotype profile.

## Education

### Interactive Pathophysiology Browser

The HTML rendering already provides a browsable view of each disorder. This could be
expanded into a teaching tool where students explore how genetic variants lead to
molecular dysfunction, cellular changes, and clinical phenotypes — the full
"mechanism chain."

### Evidence Literacy Training

The evidence model (SUPPORT/REFUTE/PARTIAL, with required PMID snippets) teaches
trainees to evaluate claims against primary literature rather than accepting
statements at face value.

## Bioinformatics & Data Integration

### Ontology-Grounded NLP Benchmark

dismech entries with their precise ontology mappings (HP, MONDO, GO, CL, MAXO) could
serve as gold-standard annotations for evaluating biomedical NLP systems that extract
disease mechanisms from text.

### Knowledge Graph Seeding

Each disorder file encodes a mini knowledge graph
(disease → genetic basis → pathophysiology → cell types → phenotypes → treatments).
These could be projected into a formal KG (e.g., Monarch Initiative's KG) to enrich
disease-gene-phenotype edges with mechanistic context.

### Cross-Ontology Bridging

dismech links MONDO diseases to HP phenotypes, GO processes, CL cell types, MAXO
treatments, and UBERON anatomy in a single curated record. This creates implicit
cross-ontology mappings that are otherwise hard to derive automatically.

### Microbiome Integration

Diseases with environmental or microbial components (e.g., infectious diseases,
gut-related conditions) could be enriched with microbiome data from resources like
NMDC biosamples, linking host disease mechanisms to microbial community profiles.

## AI & Curation

### LLM Hallucination Benchmarking

The reference validation pipeline (snippet matching against PubMed abstracts) is itself
a reusable pattern for measuring how accurately LLMs cite scientific literature. dismech
could publish a benchmark dataset of verified vs. hallucinated citations.

### Automated Curation Pipelines

The existing skill system demonstrates a pattern where AI agents curate structured
knowledge with human-in-the-loop validation. This pattern could generalize to other
biomedical knowledge bases.

### Compliance-Driven Prioritization

The weighted compliance scoring identifies which entries most need enrichment. This
drives a triage system where curator effort (human or AI) is directed to the
highest-impact gaps.

## Precision Medicine

### Genotype-to-Treatment Pathway Mapping

For entries with `genetic_basis` → `pathophysiology` → `treatments` chains (especially
cancer entries like BRAF V600E melanoma, ALK-rearranged NSCLC), dismech encodes the
logic of precision oncology: specific mutations → specific targeted therapies.

### Rare Disease Mechanism Cataloging

With disorders including rare conditions (Achondrogenesis Type II,
Beta-Mannosidosis, CHIME syndrome), dismech serves as a structured mechanism reference
for diseases that are often poorly documented in traditional resources.
