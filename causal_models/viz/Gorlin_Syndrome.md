# Gorlin Syndrome — nevoid basal cell carcinoma syndrome

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

    subgraph mod["📦 hedgehog_signaling module"]
    ptch1_inhibition["PTCH1
Hedgehog receptor act…"]
    class ptch1_inhibition module_node
    smo_activity["SMO
G protein-coupled rec…"]
    class smo_activity module_node
    sufu_sequestering_gli1["SUFU
protein sequestering …"]
    class sufu_sequestering_gli1 module_node
    gli1_activation["GLI1
DNA-binding transcrip…"]
    class gli1_activation module_node
    end

    sonic_hedgehog(["sonic hedgehog protein"])
    class sonic_hedgehog molEntity
    gli1_upregulation["GLI1
DNA-binding transcrip… [GOF]"]
    class gli1_upregulation molActivity
    ccnd1_upregulation["CCND1 [↑]"]
    class ccnd1_upregulation molActivity
    basal_keratinocyte_proliferation(("keratinocyte
cell population pro… [↑]"))
    class basal_keratinocyte_proliferation cellProcess
    basal_cell_proliferation[["skin epidermis
cell population pro… [↑]"]]
    class basal_cell_proliferation tissueProcess
    bcc{"Basal cell carcinoma"}
    class bcc phenotype
    odontogenic_keratocysts{"Odontogenic keratocysts of …"}
    class odontogenic_keratocysts phenotype
    macrocephaly{"Macrocephaly"}
    class macrocephaly phenotype
    palmar_pits{"Palmar pits"}
    class palmar_pits phenotype
    falx_calcification{"Calcification of falx cereb…"}
    class falx_calcification phenotype
    vismodegib[("vismodegib")]
    class vismodegib modulator

    subgraph hyp_ptch1_driven["🧬 PTCH1-driven (~85%)"]
    ptch1_lof>"PTCH1 LOF"]
    class ptch1_lof variant
    end

    subgraph hyp_sufu_driven["🧬 SUFU-driven (~5%)"]
    sufu_lof>"SUFU LOF"]
    class sufu_lof variant
    cerebellar_granule_precursor_proliferation(("cerebellar granule cell precursor
cerebellar granule … [↑]"))
    class cerebellar_granule_precursor_proliferation cellProcess
    medulloblastoma{"Medulloblastoma"}
    class medulloblastoma phenotype
    end

    %% Causal relations
    ptch1_lof -- ptch1_driven --> ptch1_inhibition
    sufu_lof -- sufu_driven --> sufu_sequestering_gli1
    gli1_activation --> gli1_upregulation
    gli1_upregulation --> ccnd1_upregulation
    ccnd1_upregulation --> basal_keratinocyte_proliferation
    basal_keratinocyte_proliferation --> basal_cell_proliferation
    basal_cell_proliferation -.-> bcc
    gli1_activation -- sufu_driven --> cerebellar_granule_precursor_proliferation
    cerebellar_granule_precursor_proliferation -. sufu_driven .-> medulloblastoma
    sonic_hedgehog -- inhibits --o ptch1_inhibition
    vismodegib -- blocks_downstream --o smo_activity

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
