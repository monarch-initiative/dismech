# Hedgehog Signaling Pathway

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'htmlLabels': true}}}%%
flowchart TD

    classDef variant fill:#ffd6d6,stroke:#c0392b,color:#000
    classDef chemical fill:#fdebd0,stroke:#e67e22,color:#000
    classDef envfactor fill:#fde8e8,stroke:#922b21,color:#000
    classDef molEntity fill:#fef9e7,stroke:#d4ac0d,color:#000
    classDef molActivity fill:#d6eaf8,stroke:#2471a3,color:#000
    classDef cellProcess fill:#d5f5e3,stroke:#1e8449,color:#000
    classDef tissueProcess fill:#e8daef,stroke:#7d3c98,color:#000
    classDef phenotype fill:#fef5e7,stroke:#ca6f1e,color:#000
    classDef modulator fill:#eaf2ff,stroke:#2e4057,color:#000
    classDef module_node fill:#f2f3f4,stroke:#aab7b8,color:#666,stroke-dasharray:5 3

    ptch1_inhibition["PTCH1
Hedgehog receptor act…"]
    class ptch1_inhibition molActivity
    smo_activity["SMO
G protein-coupled rec…"]
    class smo_activity molActivity
    sufu_sequestering_gli1["SUFU
protein sequestering …"]
    class sufu_sequestering_gli1 molActivity
    gli1_activation["GLI1
DNA-binding transcrip…"]
    class gli1_activation molActivity

    %% Causal relations
    ptch1_inhibition -- inhibits --o smo_activity
    smo_activity -- inhibits --o sufu_sequestering_gli1
    sufu_sequestering_gli1 -- inhibits --o gli1_activation

```

## Legend

| Shape | Node kind |
|-------|-----------|
| `>rect]` | Variant / input |
| `([pill])` | Molecular entity (protein / chemical) |
| `[rect]` | Molecular activity |
| `((circle))` | Cellular process |
| `[[double-rect]]` | Tissue process |
| `{diamond}` | Phenotype |
| `[(cylinder)]` | Modulator (therapeutic / dietary) |
| dashed grey | Imported module node |
