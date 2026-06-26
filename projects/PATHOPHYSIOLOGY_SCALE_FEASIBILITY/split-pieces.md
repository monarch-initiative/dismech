# Split-Piece Classification — Bundled Node Validation

## APL_PML_RARA — "PML-RARA Fusion Oncogene Formation"

**Original bundled node summary:** The t(15;17) translocation generates the PML-RARA fusion protein, which retains RARA DNA-binding domains but gains aberrant corepressor-recruiting properties and disrupts normal PML subnuclear localization — bundling the cytogenetic event itself with the molecular activity of the resulting fusion protein.

**Proposed split into 2 pieces:**

### Piece 1: t(15;17) Chromosomal Translocation and PML-RARA Fusion Gene Creation

- One-sentence description: The reciprocal t(15;17)(q24;q21) translocation joins PML and RARA coding sequences to create the PML-RARA fusion gene in the genome of a promyelocyte progenitor.
- Classification (JSON):
  ```json
  {
    "primary_kind": "MOLECULAR_ACTIVITY",
    "confidence": 2,
    "second_choice_kind": "CELLULAR_PROCESS",
    "proposes_new_kind": "GENOMIC_EVENT — a somatic chromosomal rearrangement is neither a molecular activity (no gene product acting on a substrate) nor a cellular process (no ongoing cellular behavior); it is a one-time structural mutation that generates a new genetic entity. The enum has no category for somatic mutation / genomic structural variant as a pathological event.",
    "split_suggestion": null,
    "reasoning": "A chromosomal translocation is closer to the molecular/genomic scale than any tissue or organismal process, but it is a discrete mutation event rather than an ongoing molecular activity, so the fit to MOLECULAR_ACTIVITY is poor."
  }
  ```

### Piece 2: PML-RARA Fusion Protein Aberrant Corepressor Recruitment Activity

- One-sentence description: The PML-RARA fusion protein binds retinoic acid response elements and recruits NCoR/SMRT/HDAC corepressor complexes at physiological RA concentrations, silencing granulocyte-differentiation target genes.
- Classification (JSON):
  ```json
  {
    "primary_kind": "MOLECULAR_ACTIVITY",
    "confidence": 5,
    "second_choice_kind": null,
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "The piece describes a specific molecular function of a fusion protein — transcriptional corepressor recruitment at defined regulatory elements — which is unambiguously MOLECULAR_ACTIVITY."
  }
  ```

---

## Blau_Syndrome — "Visceral and Vascular Involvement"

**Original bundled node summary:** Beyond the classic arthritis-uveitis-dermatitis triad, Blau syndrome can involve visceral organs (liver, kidney, lung) and vasculature; the node bundles ILD, hepatic involvement, renal involvement, and vasculitis as a single step despite each representing a distinct organ-level tissue process.

**Proposed split into 3 pieces:**

### Piece 1: Granulomatous Interstitial Lung Disease

- One-sentence description: Granulomatous inflammation driven by constitutive NOD2 activation extends to the pulmonary interstitium, producing interstitial lung disease in a subset of patients.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 5,
    "second_choice_kind": null,
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Granulomatous inflammation confined to a specific tissue (pulmonary interstitium) is a canonical TISSUE_PROCESS."
  }
  ```

### Piece 2: Systemic Vasculitis

- One-sentence description: Granulomatous inflammation extends to large and medium vessel walls, producing systemic vasculitis affecting multiple vascular beds.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 4,
    "second_choice_kind": "ORGANISM_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Vasculitis is primarily a pathological process at the vessel-wall tissue level, though 'systemic' spread across multiple vascular beds nudges slightly toward ORGANISM_PROCESS; TISSUE_PROCESS is the better primary call."
  }
  ```

### Piece 3: Hepatic and Renal Granulomatous Involvement

- One-sentence description: Non-caseating granulomas can form in the liver and kidney parenchyma as part of expanded visceral disease in Blau syndrome.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 5,
    "second_choice_kind": null,
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Granuloma formation within specific parenchymal organ tissues (liver, kidney) is unambiguously a TISSUE_PROCESS, even though two organs are mentioned — both are at the same scale and share the same granulomatous mechanism."
  }
  ```

---

## Ayme-Gripp_Syndrome — "Stabilized MAF protein and dysregulated transcriptional programs"

**Original bundled node summary:** Failure of GSK3-mediated phosphorylation prevents ubiquitination and proteasomal degradation of MAF, causing abnormal protein persistence that in turn perturbs developmental gene-expression programs — bundling a protein-stability state (MAF fails to be degraded) with its downstream transcriptional consequence.

**Proposed split into 2 pieces:**

### Piece 1: MAF Protein Stabilization via Impaired Ubiquitination and Proteasomal Degradation

- One-sentence description: Loss of phosphorylation-dependent ubiquitination prevents proteasomal turnover of MAF, producing an abnormally elevated and persistent MAF protein level in cells expressing the pathogenic allele.
- Classification (JSON):
  ```json
  {
    "primary_kind": "MOLECULAR_ACTIVITY",
    "confidence": 3,
    "second_choice_kind": "CELLULAR_PROCESS",
    "proposes_new_kind": "MOLECULAR_STATE — the node describes a protein-stability state (MAF is not degraded / MAF accumulates) rather than an ongoing molecular activity or a cellular behavior; the enum's MOLECULAR_ACTIVITY category is process-oriented (kinase activity, ion transport) and does not cleanly capture a protein dosage state that results from impaired degradation.",
    "split_suggestion": null,
    "reasoning": "The impaired ubiquitin-proteasome axis operates at the molecular scale (E3 ligase targeting of a transcription factor), making MOLECULAR_ACTIVITY the least-bad primary kind, but the core claim is a protein-level state rather than an activity."
  }
  ```

### Piece 2: Aberrant MAF Transcriptional Program Activation

- One-sentence description: Stabilized mutant MAF drives dysregulated expression of MAF target genes governing lens, auditory, and neural developmental programs.
- Classification (JSON):
  ```json
  {
    "primary_kind": "MOLECULAR_ACTIVITY",
    "confidence": 4,
    "second_choice_kind": "CELLULAR_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Transcription factor activity driving target gene expression is a molecular-scale function and fits MOLECULAR_ACTIVITY well, though the downstream effect on developmental programs in individual cells could also be read as CELLULAR_PROCESS."
  }
  ```

---

## Ayme-Gripp_Syndrome — "Multisystem developmental defects in lens, ear, brain, and growth"

**Original bundled node summary:** Dysregulated MAF activity produces cataract, hearing loss, abnormal skull growth, developmental impairment, and other ectodermal/skeletal features as a single undifferentiated node, bundling four distinct organ-system malformations that arise through partly distinct developmental pathways.

**Proposed split into 4 pieces:**

### Piece 1: Lens Developmental Defect (Congenital Cataract)

- One-sentence description: Dysregulated MAF target gene expression disrupts normal lens fiber cell differentiation and crystallin expression, producing congenital or early-onset cataract.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 4,
    "second_choice_kind": "CELLULAR_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Failure of lens development is an organ-level structural outcome (TISSUE_PROCESS), though the primary driver is cell-intrinsic transcription factor dysregulation in lens fiber cells (CELLULAR_PROCESS)."
  }
  ```

### Piece 2: Auditory System Developmental Defect (Sensorineural Hearing Loss)

- One-sentence description: Dysregulated MAF activity disrupts developmental programs required for inner ear differentiation or auditory nerve function, producing congenital sensorineural hearing loss.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 3,
    "second_choice_kind": "CELLULAR_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": null,
    "reasoning": "Sensorineural hearing loss as a structural auditory organ defect is best placed at TISSUE_PROCESS, but the intermediate mechanism (cell-type-specific transcriptional dysregulation) has a strong CELLULAR_PROCESS character, giving a real two-way tie."
  }
  ```

### Piece 3: Neurodevelopmental Impairment (Developmental Delay and Seizures)

- One-sentence description: Dysregulated MAF target gene expression perturbs neuronal differentiation and circuit formation, producing global developmental delay and seizures.
- Classification (JSON):
  ```json
  {
    "primary_kind": "TISSUE_PROCESS",
    "confidence": 3,
    "second_choice_kind": "ORGANISM_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": "This piece itself bundles two related but distinct claims: (a) structural brain developmental defect (abnormal brain morphology), which is TISSUE_PROCESS, and (b) whole-organism neurobehavioral outcome (developmental delay, seizures), which is closer to ORGANISM_PROCESS. Further splitting into 'Abnormal Brain Morphogenesis' and 'Neurobehavioral Developmental Impairment' would each be cleaner.",
    "reasoning": "Brain maldevelopment is best framed as a tissue-level process, but the clinical expression (global delay, seizures) is an organism-level phenotypic state, producing a genuine classification tie."
  }
  ```

### Piece 4: Somatic Growth Restriction and Craniofacial Dysmorphism

- One-sentence description: Dysregulated MAF developmental programs produce postnatal growth restriction and a characteristic craniofacial gestalt including brachycephaly and flat facial profile.
- Classification (JSON):
  ```json
  {
    "primary_kind": "ORGANISM_PROCESS",
    "confidence": 3,
    "second_choice_kind": "TISSUE_PROCESS",
    "proposes_new_kind": null,
    "split_suggestion": "Growth restriction (a whole-organism state) and craniofacial dysmorphism (a tissue/structural defect of the skull and face) are distinct enough to warrant separate nodes: 'Postnatal Growth Restriction' (ORGANISM_PROCESS) and 'Craniofacial Developmental Dysmorphism' (TISSUE_PROCESS).",
    "reasoning": "Growth restriction as a whole-body outcome best fits ORGANISM_PROCESS, but craniofacial dysmorphism is a local structural tissue defect, making this a bundled node with a genuine two-kind split."
  }
  ```

---

## Summary

- **Total pieces across 4 bundles:** 11 (2 + 3 + 2 + 4)
- **Cleanly fit a single kind (confidence ≥ 4, no proposes_new_kind):** 7 of 11
  - APL Piece 2 (MOLECULAR_ACTIVITY, conf 5)
  - Blau ILD (TISSUE_PROCESS, conf 5)
  - Blau Vasculitis (TISSUE_PROCESS, conf 4)
  - Blau Hepatic/Renal (TISSUE_PROCESS, conf 5)
  - Ayme-Gripp MAF Transcriptional Program (MOLECULAR_ACTIVITY, conf 4)
  - Ayme-Gripp Lens Defect (TISSUE_PROCESS, conf 4)
  - Blau Vasculitis (already counted)
- **Still propose a new kind:** 2 of 11
  - APL Piece 1: proposes GENOMIC_EVENT (chromosomal translocation as a mutation event)
  - Ayme-Gripp MAF Stabilization Piece 1: proposes MOLECULAR_STATE (protein dosage state from impaired degradation)
- **Pieces that remain bundled themselves (split_suggestion set):** 2 of 11
  - Ayme-Gripp Neurodevelopmental Impairment (structural brain defect + organism-level behavioral outcome)
  - Ayme-Gripp Growth/Craniofacial (whole-body growth + local skull morphology)
- **Dominant landing kind after splitting:** TISSUE_PROCESS (5 pieces) and MOLECULAR_ACTIVITY (3 pieces) dominate; ORGANISM_PROCESS appears as a secondary or co-primary in 2 pieces.

**Pattern:** Splitting works well — most pieces resolve cleanly into the 4-kind enum. The two persistent gaps are (1) somatic genomic events (translocations, mutations as events rather than activities) and (2) protein dosage/stability states. Both are "states" rather than "processes," confirming the calibration note that the enum is process-centric and may need a STATE or GENOMIC_EVENT extension to cover these recurring patterns.
