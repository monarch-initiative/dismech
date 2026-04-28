## New Term Request: V5/MT (middle temporal visual area)

### Preferred term label
V5/MT (middle temporal visual area)

### Synonyms
- middle temporal visual area
- visual area V5
- visual area MT
- area V5
- area MT
- V5
- MT

### Definition
A functionally defined region of extrastriate visual cortex specialized for the perception of visual motion. Located on the lateral surface of the occipital lobe, typically within the ascending limb of the inferior temporal sulcus (ITS). This area is characterized by neurons selectively responsive to motion direction and speed.

### Parent term
`UBERON:0022232` (secondary visual cortex) or `UBERON:0000411` (visual cortex)

### Justification

**Clinical Need:**
We are curating akinetopsia (motion blindness, MONDO:0000660), a rare neurological disorder caused by damage to V5/MT. The current UBERON hierarchy lacks a term with appropriate specificity:

1. **UBERON:0000411 (visual cortex)** - Too broad; encompasses all visual processing areas
2. **UBERON:0022232 (secondary visual cortex)** - Still broad; includes V2, V3, V4, V5/MT, and other extrastriate areas
3. **UBERON:0013550 (Brodmann area 19)** - Architecturally defined but functionally heterogeneous; V5/MT occupies only a small portion of BA19

Using Brodmann area 19 to represent V5/MT is misleading because:
- BA19 is a large cytoarchitectonic region spanning much of the occipital cortex
- V5/MT is a small, functionally specialized area defined by motion-processing neurons
- The clinical literature consistently refers to "V5/MT" or "area MT," not "BA19"
- Damage to BA19 broadly does not necessarily cause akinetopsia; damage to V5/MT specifically does

**Anatomical Characteristics:**
- **Location:** Lateral occipital cortex, typically within the ascending limb of the inferior temporal sulcus (ALITS) or its dorsal/posterior continuation
- **Functional definition:** Motion-selective neurons with direction and speed tuning
- **Cross-species homology:** Well-established homology with macaque area MT
- **Retinotopic organization:** Contains a complete retinotopic map of the visual field

**Literature Support:**
V5/MT is one of the most extensively studied visual areas and is recognized as a distinct functional entity in human neuroimaging and clinical neurology:

- [The Retinotopic Organization of the Human Middle Temporal Area MT/V5 and Its Cortical Neighbors | Journal of Neuroscience](https://www.jneurosci.org/content/30/29/9801)
- [Area V5—a microcosm of the visual brain - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4381624/)
- [A new anatomical landmark for reliable identification of human area V5/MT: a quantitative analysis of sulcal patterning](https://pubmed.ncbi.nlm.nih.gov/10847595/)
- [Frontiers | Functional Segregation of the Middle Temporal Visual Motion Area](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.00427/full)

**Proposed Ontology Position:**
```
UBERON:0000411 visual cortex
  └─ UBERON:0022232 secondary visual cortex (extrastriate cortex)
      └─ UBERON:XXXXXXX V5/MT (middle temporal visual area) [NEW TERM]
```

**Database Cross-references:**
- NeuroNames: 1207 (area MT)
- Wikipedia: https://en.wikipedia.org/wiki/Middle_temporal_visual_area

### Use Case
This term is needed for precise annotation of:
1. Akinetopsia and other motion perception disorders
2. fMRI studies of visual motion processing
3. Computational models of the dorsal visual stream
4. Cross-species comparative neuroanatomy

### Additional Notes
The V5/MT designation reflects dual nomenclature traditions:
- **V5**: Human visual neuroscience convention (continuing from V1, V2, V3, V4)
- **MT (middle temporal)**: Primate neurophysiology convention based on macaque studies

Both designations refer to the same functionally defined area and are used interchangeably in the literature.

### Interim Recommendation for Akinetopsia Curation

Until a specific V5/MT term is added to UBERON, I recommend reverting to **UBERON:0022232 (secondary visual cortex)** for the Akinetopsia disorder file. This is "clearly non-specific" but accurately reflects that:
1. V5/MT is part of the secondary/extrastriate visual cortex
2. The term doesn't overpromise specificity we don't have
3. It avoids the misleading specificity of Brodmann area 19

The alternative of using only **UBERON:0000411 (visual cortex)** is even more general and may be too broad given that we know the disorder specifically affects extrastriate regions.

### Contact
Requested by: dismech knowledge base curation team (@dragon-ai-agent)
Context: https://github.com/monarch-initiative/dismech/issues/233
Authorized by: @cmungall
