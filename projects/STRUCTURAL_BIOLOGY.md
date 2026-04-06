# Structural Biology & Disease Mechanisms Project

## Overview
Diseases where protein structure determination (PDB X-ray crystallography, cryo-EM) or computational structure prediction (AlphaFold) has been key to understanding pathophysiology, enabling drug design, or interpreting variant pathogenicity.

This is both a **curation guide** (which diseases to prioritize) and a **schema design exploration** (how structural biology insights fit into dismech's data model).

## How Structural Biology Data Fits Into dismech

### Where it already fits (no schema changes needed)

1. **Evidence items** — PDB/AlphaFold papers are citeable evidence for mechanism claims:
   ```yaml
   pathophysiology:
     - name: BCR-ABL constitutive kinase activation
       evidence:
         - reference: PMID:11423618   # imatinib-ABL crystal structure paper
           snippet: "Crystal structure of ABL in complex with STI571..."
           evidence_source: COMPUTATIONAL
   ```

2. **Treatment.mechanism** — Structure-based drug design narratives:
   ```yaml
   treatments:
     - name: Imatinib
       mechanism: >-
         Binds the inactive conformation of ABL kinase domain.
         Structure-based design informed by PDB:1IEP crystal structure.
   ```

3. **ComputationalModel** — AlphaFold or structural models as computational tools:
   ```yaml
   computational_models:
     - name: AlphaFold2 structure of CFTR ΔF508
       model_type: MACHINE_LEARNING   # or a new STRUCTURAL_PREDICTION type
       description: >-
         AlphaFold2 prediction of CFTR with ΔF508 deletion reveals
         destabilization of NBD1-ICL4 interface.
       repository_url: https://alphafold.ebi.ac.uk/entry/P13569
   ```

4. **GeneticContext.functional_impact** — Variant-level structural effects:
   ```yaml
   genetic_basis:
     - allele_type: missense
       functional_impact: >-
         T315I gatekeeper mutation blocks imatinib binding by
         introducing steric clash at the ATP-binding pocket.
   ```

### Where the schema could grow (potential new features)

#### Option A: Add `structural_insights` to ComputationalModelTypeEnum
Minimal change — just add a new enum value:
```yaml
ComputationalModelTypeEnum:
  permissible_values:
    STRUCTURAL_PREDICTION:
      description: >-
        Protein structure prediction (AlphaFold, RoseTTAFold) or
        molecular dynamics simulation of disease-relevant proteins
    MOLECULAR_DOCKING:
      description: >-
        Computational docking of drug candidates to protein targets,
        typically informed by PDB structures
```
This lets structural biology data live in the existing `computational_models` slot with proper typing. Least disruptive.

#### Option B: Add `structural_context` slot to GeneticContext
For variant-level structural mapping:
```yaml
structural_context:
  description: >-
    Structural biology context for how mutations affect protein
    structure or drug binding. References PDB/AlphaFold entries.
  range: StructuralContext
  inlined: true

# New class
StructuralContext:
  slots:
    - pdb_id
    - alphafold_id
    - affected_domain
    - structural_effect   # e.g., "disrupts salt bridge", "steric clash"
    - drug_binding_impact  # e.g., "blocks imatinib binding pocket"
    - evidence
```
More structured but heavier — only worth it if we plan to systematically capture variant-structure mappings.

#### Option C: Add `protein_structures` top-level slot on Disease
Like `computational_models` but specifically for structural biology:
```yaml
protein_structures:
  - name: ABL kinase domain with imatinib
    pdb_id: PDB:1IEP
    resolution: 2.1 A
    method: X-RAY_CRYSTALLOGRAPHY
    disease_relevance: >-
      Defines the imatinib binding mode and explains resistance mutations
    key_residues:
      - T315 (gatekeeper)
      - E286 (DFG motif)
    evidence: [...]
```
Most expressive but adds significant schema surface area.

### Recommendation
**Start with Option A** (add enum values to ComputationalModelTypeEnum) — it's zero-breaking-change and lets us capture structural biology in existing `computational_models` blocks immediately. As we curate, we'll learn whether Options B or C are needed. The `functional_impact` free-text field on GeneticContext already handles variant-structure narratives adequately for now.

## Diseases to Curate / Annotate with Structural Biology

### Tier 1: Structure Directly Enabled Targeted Therapy
These are paradigmatic — structure-based drug design changed patient outcomes.

| Disease | Key Protein(s) | PDB Landmark | Impact | Existing in KB? | Status |
|---------|----------------|-------------|--------|-----------------|--------|
| HIV/AIDS | HIV protease, RT, integrase | 1HHP, 1RT2, 3OYA | Protease inhibitors (saquinavir, ritonavir) | Yes (AIDS.yaml) | [ ] Annotate |
| Chronic Myeloid Leukemia | BCR-ABL kinase | 1IEP (imatinib complex) | Imatinib and successors | No | [ ] Create + annotate |
| COVID-19 | Spike protein, Mpro | 6VSB (spike cryo-EM), 6LU7 (Mpro) | Vaccines + Paxlovid | No | [ ] Create + annotate |
| Cystic Fibrosis | CFTR | 5UAK (cryo-EM) | Ivacaftor, lumacaftor correctors | No | [ ] Create + annotate |
| ALK-Rearranged NSCLC | ALK kinase | 2XP2, 5AA8 | Crizotinib, lorlatinib | Yes | [ ] Annotate |
| ATTR Amyloidosis | Transthyretin | 1F41 (TTR tetramer) | Tafamidis (kinetic stabilizer) | Yes | [ ] Annotate |
| HER2+ Breast Cancer | HER2/ERBB2 | 1N8Z | Trastuzumab (Herceptin) | No | [ ] Create + annotate |
| EGFR-mutant NSCLC | EGFR kinase | 1M17 | Gefitinib, osimertinib | No | [ ] Create + annotate |
| Influenza | Neuraminidase | 1NNC | Oseltamivir (Tamiflu) | No | [ ] Create + annotate |
| Gaucher Disease | GCase (GBA1) | 2NT0 | Pharmacological chaperones | No | [ ] Create + annotate |

### Tier 2: Structure Revealed Disease Mechanism
Understanding pathophysiology, even if therapy didn't follow directly from structure.

| Disease | Key Protein(s) | Structural Insight | Existing? | Status |
|---------|----------------|-------------------|-----------|--------|
| Alzheimer's Disease | Amyloid-beta, tau fibrils | Cryo-EM fibril polymorphs distinguish tauopathies (5OQV, 5O3L) | Yes | [ ] Annotate |
| Sickle Cell Disease | Hemoglobin S | First molecular disease; HbS polymerization (2HBS) | No | [ ] Create + annotate |
| Achondroplasia | FGFR3 | Constitutive kinase activation by G380R | Yes | [ ] Annotate |
| Phenylketonuria | PAH | Mutation mapping on PAH structure (1J8U) | Yes | [ ] Annotate |
| Fanconi Anemia | FA/BRCA complex | Cryo-EM of FA core complex | Yes | [ ] Annotate |
| Li-Fraumeni / p53 cancers | p53 DBD | Hotspot mutations mapped on crystal structure (2XWR) | No | [ ] Create + annotate |
| Marfan Syndrome | Fibrillin-1 | cbEGF domain structures explain Ca2+ binding defects | No | [ ] Create + annotate |
| Osteogenesis Imperfecta | Collagen I | Triple helix disruption by Gly substitutions | No | [ ] Create + annotate |
| Salla Disease | Sialin (SLC17A5) | Cryo-EM transport mechanism (2023) | Yes | [ ] Annotate |

### Tier 3: AlphaFold-Era Breakthroughs
Where AlphaFold specifically opened new doors.

| Area | Example Disease(s) | AlphaFold Contribution | Status |
|------|-------------------|----------------------|--------|
| Rare disease VUS interpretation | Many Mendelian diseases | Map VUS onto predicted structures to assess pathogenicity | [ ] Research |
| Neglected tropical diseases | Leishmaniasis, Chagas, malaria | First structures for parasitic protein drug targets | [ ] Research |
| Antimicrobial resistance | Drug-resistant TB, MRSA | Novel resistance enzyme structures | [ ] Research |
| Protein misfolding diseases | Parkinson's (alpha-synuclein), ALS (SOD1, TDP-43) | Disordered region predictions, aggregate interfaces | [ ] Research |
| Nuclear pore complex diseases | Nucleoporin-related leukemias | AlphaFold + cryo-EM joint modeling | [ ] Research |

## Implementation Plan

### Phase 1: Schema (minimal)
- [ ] Add `STRUCTURAL_PREDICTION` and `MOLECULAR_DOCKING` to `ComputationalModelTypeEnum`
- [ ] Validate enum additions pass `just qc`

### Phase 2: Annotate Existing Entries
- [ ] ATTR Amyloidosis — add TTR structure / tafamidis binding to computational_models
- [ ] ALK NSCLC — add ALK kinase structures to computational_models
- [ ] Alzheimer's — add cryo-EM fibril structures
- [ ] Achondroplasia — add FGFR3 structural context
- [ ] Phenylketonuria — add PAH structure mapping
- [ ] Fanconi Anemia — enrich cryo-EM references
- [ ] HIV/AIDS — add protease/RT/integrase structures

### Phase 3: New High-Impact Entries
- [ ] CML (BCR-ABL + imatinib — the poster child)
- [ ] Cystic Fibrosis (CFTR modulator story)
- [ ] Sickle Cell Disease (first molecular disease)
- [ ] HER2+ Breast Cancer (trastuzumab structural basis)

### Phase 4: Evaluate Schema Needs
After Phase 2-3 curation, assess whether:
- `functional_impact` free text is sufficient for variant-structure narratives
- A dedicated `StructuralContext` class (Option B) would add value
- A top-level `protein_structures` slot (Option C) is warranted

## References & Resources
- **PDB**: https://www.rcsb.org/
- **AlphaFold DB**: https://alphafold.ebi.ac.uk/
- **PDBe Knowledge Base**: https://www.ebi.ac.uk/pdbe/pdbe-kb/
- **SIFTS** (Structure Integration with Function, Taxonomy, Sequence): maps PDB to UniProt
- **Missense3D**: predicts structural impact of missense variants
- **AlphaMissense**: DeepMind pathogenicity classifier using AlphaFold
