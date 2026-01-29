---
name: microbiome-curation
description: >
  Skill for curating microbiome-related pathophysiology in the dismech knowledge base.
  Use this skill when adding dysbiosis mechanisms, ecological concepts (Anna Karenina,
  keystone taxa, colonization resistance), SCFA/metabolite pathways, and linking
  microbial ecology to disease pathophysiology. Covers IBD, C. diff, obesity, and
  other microbiome-associated conditions.
---

# Microbiome Curation Skill

## Overview

Curate microbiome-related pathophysiology entries with ecological depth beyond simple
taxa +/- lists. Focus on:
- Ecological concepts (diversity, stability, keystone taxa)
- Causal chains from dysbiosis to clinical manifestations
- Metabolic consequences (SCFA, bile acids)
- Integration with BugSigDB and primary literature

## When to Use

- Adding microbiome dysbiosis entries to disorders
- Curating pathophysiology for IBD, C. diff, obesity, metabolic diseases
- Decomposing "microbiome dysbiosis" into causal graph nodes
- Adding ecological concepts (Anna Karenina, colonization resistance)
- Linking microbial metabolites to host pathophysiology

## Key Principle: Graph Structure Over Monolithic Entries

**DO NOT** create single entries bundling all microbiome effects:

```yaml
# BAD - monolithic entry
- name: Microbiome Dysbiosis
  description: >
    Reduced diversity with depletion of Firmicutes and expansion of pathobionts,
    leading to decreased SCFA and barrier dysfunction.
```

**DO** decompose into atomic nodes with `downstream` edges:

```yaml
# GOOD - causal graph
- name: Loss of Microbial Diversity
  downstream:
  - target: Loss of Keystone SCFA Producers
  - target: Increased Microbial Community Instability

- name: Loss of Keystone SCFA Producers
  downstream:
  - target: Decreased Butyrate Production

- name: Decreased Butyrate Production
  downstream:
  - target: Impaired Colonocyte Energy Metabolism

- name: Impaired Colonocyte Energy Metabolism
  downstream:
  - target: Epithelial Barrier Dysfunction
```

This enables:
1. Shared nodes across disorders
2. Explicit feedback loops
3. Targeted therapeutic entry points
4. Evidence on specific causal steps

## Ecological Dimensions of Dysbiosis

### Beyond Taxa +/-

BugSigDB captures increased/decreased taxa, but ecology is richer:

| Dimension | What it captures | Example |
|-----------|------------------|---------|
| **Taxonomic** | Which species +/- | Faecalibacterium, E. coli |
| **α-Diversity** | Richness/evenness | Shannon index |
| **β-Diversity** | Inter-individual variability | Anna Karenina effect |
| **Functional** | Pathway capacity | Butyrate synthesis genes |
| **Metabolic** | Actual output | Fecal SCFA concentrations |
| **Network** | Community structure | Keystone taxa, modularity |
| **Stability** | Resilience | Alternative stable states |

### Anna Karenina Principle

> "All healthy microbiomes are alike; each dysbiotic microbiome is dysbiotic in its own way."

Dysbiosis often manifests as **increased stochasticity** rather than consistent shift to specific taxa.

```yaml
- name: Increased Microbial Community Instability
  description: >
    Anna Karenina effect - dysbiotic microbiomes show increased inter-individual
    variability and temporal instability. The community loses resilience and may
    occupy an alternative stable state that resists therapeutic intervention.
  notes: >
    This increased stochasticity complicates biomarker discovery and explains
    heterogeneous treatment responses.
  downstream:
  - target: Loss of Microbial Diversity
    description: Feedback loop - instability promotes further diversity loss
  evidence:
  - reference: PMID:28836573
    supports: SUPPORT
    snippet: "The result is an 'Anna Karenina principle' for animal microbiomes, in which dysbiotic individuals vary more in microbial community composition than healthy individuals."
```

### Keystone Taxa

Low-abundance species with high network connectivity:

| Taxon | Role | Loss Consequence |
|-------|------|------------------|
| *Faecalibacterium prausnitzii* | Butyrate producer, anti-inflammatory | ↓ SCFA, ↑ inflammation |
| *Akkermansia muciniphila* | Mucin degrader, cross-feeding hub | Barrier dysfunction |
| *Clostridium scindens* | 7α-dehydroxylation (bai operon) | Loss of colonization resistance |
| *Roseburia* spp. | Butyrate producer | ↓ SCFA |

### Colonization Resistance (C. diff model)

```yaml
- name: Loss of Colonization Resistance
  description: >
    The healthy microbiome prevents pathogen colonization through nutrient
    competition, niche exclusion, and antimicrobial production. Antibiotic
    disruption removes these barriers.
  notes: >
    Key taxa: Lachnospiraceae, Ruminococcaceae, Collinsella. C. scindens
    provides bile acid-mediated resistance via bai operon.
  downstream:
  - target: Pathogen Germination and Expansion

- name: Loss of Secondary Bile Acid Production
  description: >
    Depletion of 7α-dehydroxylating bacteria (C. scindens, C. hylemonae)
    prevents conversion of primary to secondary bile acids. Primary bile
    acids promote pathogen germination; secondary bile acids inhibit it.
  downstream:
  - target: Pathogen Germination and Expansion
```

## SCFA Pathway Template

Common pattern for butyrate-related mechanisms:

```yaml
- name: Loss of Keystone SCFA Producers
  description: >
    Depletion of butyrate-producing Firmicutes, particularly Faecalibacterium
    prausnitzii, Roseburia spp., and Eubacterium rectale. These keystone taxa
    support community structure through cross-feeding.
  notes: >
    F. prausnitzii is anti-inflammatory; its supernatant reduces colitis in
    animal models. Primary butyrate producers use the acetyl-CoA pathway.
  downstream:
  - target: Decreased Butyrate Production

- name: Decreased Butyrate Production
  description: >
    Reduced fecal SCFA concentrations, particularly butyrate. Butyrate is
    the primary energy source for colonocytes (~70% of energy) and exerts
    anti-inflammatory effects via HDAC inhibition and GPR109A signaling.
  biological_processes:
  - preferred_term: Short-chain Fatty Acid Metabolism
    term:
      id: GO:0046459
      label: short-chain fatty acid metabolic process
  downstream:
  - target: Impaired Colonocyte Energy Metabolism

- name: Impaired Colonocyte Energy Metabolism
  description: >
    Colonocytes deprived of butyrate shift from beta-oxidation to glycolysis,
    causing energy deficit. This impairs tight junction maintenance, mucus
    production, and epithelial renewal.
  cell_types:
  - preferred_term: Colonic Epithelial Cell
    term:
      id: CL:0011108
      label: colon epithelial cell
  downstream:
  - target: Epithelial Barrier Dysfunction
```

## Pathobiont Expansion Template

```yaml
- name: Pathobiont Expansion
  description: >
    Bloom of opportunistic pathobionts (adherent-invasive E. coli, Fusobacterium,
    Enterobacteriaceae) that exploit niches vacated by depleted commensals.
    Promote inflammation through LPS and epithelial invasion.
  downstream:
  - target: Mucosal Inflammation
    description: LPS and pro-inflammatory molecules
  - target: Epithelial Barrier Dysfunction
    description: Direct epithelial invasion and tight junction disruption
  evidence:
  - reference: PMID:26185088
    supports: SUPPORT
    snippet: "This is often characterized by an increased relative abundance of facultative anaerobic bacteria (e.g., Enterobacteriaeceae, Bacilli) and, at the same time, depletion of obligate anaerobic bacteria."
```

## BugSigDB Integration

### When to Reference BugSigDB

- Identifying which taxa are commonly reported +/- in a condition
- Validating that your keystone taxa match published signatures
- Finding PMIDs for evidence

### How to Search BugSigDB

```bash
# Web interface
open "https://bugsigdb.org/w/index.php?search=ulcerative+colitis"

# R/Bioconductor
# library(bugsigdbr)
# sigs <- getSignatures(condition = "ulcerative colitis")
```

### Adding BugSigDB Notes

```yaml
- name: Loss of Colonization Resistance
  notes: >
    Metagenomics studies consistently show CDI patients have depleted Lachnospiraceae,
    Ruminococcaceae, and Collinsella spp. compared to controls. BugSigDB signatures
    confirm depletion of these protective taxa.
```

## Key References

### Ecological Concepts
| Concept | PMID | Citation |
|---------|------|----------|
| Anna Karenina principle | 28836573 | Zaneveld et al. 2017, Nat Microbiol |
| Diversity/stability | 22972295 | Lozupone et al. 2012, Nature |
| Alternative stable states | [search for recent] | Microbiome journal |

### IBD Microbiome
| Topic | PMID | Citation |
|-------|------|----------|
| F. prausnitzii | 18936492 | Sokol et al. 2008, PNAS |
| IBD meta-analysis | 25307765 | Walters et al. 2014, FEBS Lett |
| Dysbiosis patterns | 26185088 | Stecher 2015, Microbiol Spectr |

### C. diff / Colonization Resistance
| Topic | PMID | Citation |
|-------|------|----------|
| bai operon | 32179626 | Reed et al. 2020, J Bacteriol |
| C. scindens | 28066726 | Studer et al. 2016, Front Cell Infect Microbiol |
| Toxin mechanism | 15831824 | Voth & Ballard 2005, Clin Microbiol Rev |

## Ontology Terms

### Biological Processes (GO)
```bash
uv run runoak -i sqlite:obo:go search "short-chain fatty acid"
uv run runoak -i sqlite:obo:go search "microbiome"
```

| Process | GO ID |
|---------|-------|
| SCFA metabolic process | GO:0046459 |
| Modification by symbiont | GO:0044003 |
| Inflammatory response | GO:0006954 |

### Cell Types (CL)
| Cell | CL ID |
|------|-------|
| Colon epithelial cell | CL:0011108 |
| Goblet cell | CL:0000160 |
| Neutrophil | CL:0000775 |

### Organisms (NCBITaxon)
```bash
uv run runoak -i sqlite:obo:ncbitaxon search "Faecalibacterium"
```

**Note:** Do NOT use NCBITaxon in `cell_types` - microbial taxa are not cell types.
Include taxa in `description` or `notes` fields instead.

## Validation

```bash
# Full validation
just validate kb/disorders/MyDisorder.yaml

# Check references
just validate-references kb/disorders/MyDisorder.yaml

# Generate HTML to visualize causal graph
uv run python -m dismech.render kb/disorders/MyDisorder.yaml
open pages/disorders/MyDisorder.html
```

## Common Patterns by Disorder Type

### IBD (UC, Crohn's)
1. Loss of Microbial Diversity
2. Loss of Keystone SCFA Producers (F. prausnitzii)
3. Pathobiont Expansion (AIEC, Fusobacterium)
4. Decreased Butyrate → Colonocyte Energy Deficit
5. Barrier Dysfunction
6. Anna Karenina instability (feedback)

### C. diff Infection
1. Antibiotic-Induced Microbial Depletion
2. Loss of Colonization Resistance
3. Loss of Secondary Bile Acid Production
4. C. difficile Germination and Expansion
5. Toxin Production → Epithelial Death + Neutrophil Recruitment
6. Pseudomembranous Colitis

### Obesity / Metabolic Syndrome
1. Firmicutes/Bacteroidetes ratio shift
2. Increased Energy Harvest
3. Altered Bile Acid Metabolism
4. Gut Barrier Permeability
5. Metabolic Endotoxemia (LPS)
6. Low-grade Inflammation

## Integration with Other Skills

- **dismech-terms**: For ontology lookups (GO, CL, UBERON)
- **dismech-references**: For validating PMID snippets
- **cancer-curator**: Some cancers have microbiome components (colorectal)
