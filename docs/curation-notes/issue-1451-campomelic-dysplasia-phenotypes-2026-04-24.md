# Issue #1451: Campomelic Dysplasia phenotype curation

Date: 2026-04-19

Scope:
- Restrict edits to the phenotype section of `kb/disorders/Campomelic_Dysplasia.yaml`
- Add clinically important phenotypes only when supported by exact PMID-backed abstract text
- Add frequency/onset only where the abstract directly supports the extra claim

Primary references used:
- PMID:11754051, *Acampomelic campomelic syndrome.*
  - Used for: bowed long bones, bell-shaped thorax, 11 pairs of ribs, hypoplastic scapulae, sex reversal
  - Key abstract language: characteristic skeletal phenotype list; "Campomelia (bowed limbs) is seen in most but not all patients"; "Sex reversal occurs in most patients with an XY karyotype"
- PMID:20301724, *Campomelic Dysplasia.*
  - Used for: clubfoot, Pierre-Robin sequence, cleft palate, laryngotracheomalacia, ambiguous genitalia, female external genitalia in 46,XY individuals, short stature, cervical spine instability, scoliosis, hearing impairment
  - Key abstract language: GeneReviews clinical characteristics sentence for core craniofacial/limb findings and long-term survivor complications
- PMID:6344634, *The campomelic syndrome: review, report of 17 cases, and follow-up on the currently 17-year-old boy first reported by Maroteaux et al in 1971.*
  - Used for: hip dislocation
  - Key abstract language: "Usually the hips are dislocated..."
- PMID:17185244, *Novel SOX9 gene mutation in campomelic dysplasia with autosomal sex reversal.*
  - Used for: micrognathia
  - Key abstract language: explicit case-level craniofacial phenotype list including cleft palate and micrognathia
- PMID:24800790, *Campomelic dysplasia.*
  - Used for: respiratory insufficiency and neonatal onset context
  - Key abstract language: "It is usually fatal in the neonatal period because of respiratory insufficiency"

Frequency/onset decisions:
- `Bowing of the Long Bones`: assigned `frequency: FREQUENT`
  - Rationale: PMID:11754051 states campomelia is seen in "most but not all patients"
- `Respiratory Insufficiency`: added `phenotype_contexts` with `onset_category: NEONATAL`
  - Rationale: PMID:24800790 explicitly places respiratory insufficiency in the neonatal period

Claims softened or constrained:
- `Short Stature` was reframed as a finding of long-term survivors rather than a blanket statement for all affected individuals
- `Sex Reversal`, `Ambiguous Genitalia`, and `Female External Genitalia in 46,XY Individual` were all explicitly constrained to affected individuals with a 46,XY karyotype
- No frequency was assigned to genital, airway, craniofacial, or survivor phenotypes unless the abstract text provided a direct qualitative frequency signal

Not added despite being mentioned in older literature abstracts:
- Cardiac, renal, and CNS anomalies from PMID:6344634 were not added in this pass because the goal was to strengthen the core phenotype section with findings that are both clinically important and better grounded across the modern Campomelic Dysplasia literature.
