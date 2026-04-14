---
provider: codex
model: gpt-5-codex
start_time: '2026-04-14T19:54:40Z'
end_time: '2026-04-14T19:54:40Z'
duration_seconds: 0.0
template_file: codex_manual_research_note
template_variables:
  disease_name: Morquio syndrome
  mondo_id: MONDO:0018938
  category: Mendelian
citation_count: 14
---

# Morquio syndrome curation note

## MONDO / Monarch anchor

- Root disease anchor: `MONDO:0018938` with canonical label `mucopolysaccharidosis type 4`.
- MONDO exact synonyms on the root term include `Morquio disease`, `Morquio syndrome`, `MPS IV`, `mucopolysaccharidosis IV`, and `mucopolysaccharidosis type IV`.
- Subtype anchors:
  - `MONDO:0009659` `mucopolysaccharidosis type 4A`
  - `MONDO:0009660` `mucopolysaccharidosis type 4B`
- Modeling consequence: use `Morquio syndrome` as the human-facing disease name, but anchor the disorder term to the MONDO root `mucopolysaccharidosis type 4`.

## ClinGen cross-check

- `cache/clingen/gene_validity.csv` line 3031: `GALNS` -> `mucopolysaccharidosis type 4A` (`MONDO:0009659`) is `Definitive`.
- `cache/clingen/gene_validity.csv` line 777: `GLB1` -> `mucopolysaccharidosis type 4B` (`MONDO:0009660`) is `Definitive`.
- There is no root-level ClinGen gene-disease assertion for `Morquio syndrome` as a single gene disease; the gene anchoring is subtype-specific.

## Lump / split decision

- Curate a Morquio root with explicit `Type A` and `Type B` subtypes.
- Reasoning:
  - The shared disease identity is clinically and mechanistically coherent at the MPS IV / Morquio level because both subtypes converge on keratan-sulfate-driven skeletal-connective-tissue pathology.
  - The proximal defect splits immediately at the lysosomal enzyme level, so the pathograph should open with separate `GALNS` and `GLB1` proximal nodes that converge on shared downstream storage and cartilage/connective-tissue dysfunction.
  - `GLB1` disease biology overlaps with GM1 gangliosidosis and some papers argue for a beta-galactosidase deficiency spectrum, but MONDO and ClinGen still retain `mucopolysaccharidosis type 4B` as a distinct disease subtype. That is strong enough to keep explicit Morquio B curation under the Morquio root rather than collapsing it into GM1 gangliosidosis.

## Exact PMID-backed quotes driving the YAML

- `PMID:32905071`
  - `"Mucopolysaccharidosis type IVA (MPS IVA) is an inborn error of glycosaminoglycan (GAG) catabolism characterized by a deficiency of the lysosomal enzyme, N-acetylgalactosamine 6-sulphatase (GALNS)."`
  - Use: subtype A proximal defect and `GALNS` genetic anchoring.
- `PMID:32905071`
  - `"Consequently, partially degraded GAG, chondroitin 6-sulfate (CS) and keratan sulfate (KS), accumulate in the lysosomes of affected cells, primarily in cartilage resulting in skeletal disease."`
  - Use: shared storage node, cartilage-first disease emphasis, biochemical section.
- `PMID:21497194`
  - `"GM1 gangliosidosis and Morquio B syndrome, both arising from beta-galactosidase (GLB1) deficiency, are very rare lysosomal storage diseases"`
  - Use: subtype B proximal gene/enzyme framing.
- `PMID:12559848`
  - `"These findings suggest that imbalanced substrate specificity of the mutant beta-Gals induces predominant accumulation of keratan sulfate and a rationale for performing differential diagnostic analysis for both disorders."`
  - Use: subtype B mechanism should be framed as a keratan-sulfate-biased beta-galactosidase defect, not generic GLB1 loss alone.
- `PMID:33558080`
  - `"Morquio B disease is an attenuated phenotype within the spectrum of beta galactosidase (GLB1) deficiencies."`
  - Use: subtype B description and root-level split note.
- `PMID:33558080`
  - `"It is characterised by dysostosis multiplex, ligament laxity, mildly coarse facies and heart valve defects due to keratan sulphate accumulation, predominantly in the cartilage."`
  - Use: subtype B skeletal/connective-tissue phenotype wording and extra-skeletal connective-tissue branch.
- `PMID:33977034`
  - `"In conclusion, we hypothesize that GMI gangliosidosis and MorB are part of one phenotypic spectrum of the same disease and that the classification of LSDs might need to be revised."`
  - Use: keep as a caveat in the research note and PR body, but do not let it override MONDO/ClinGen subtype modeling.
- `PMID:29326877`
  - `"Morquio A syndrome (mucopolysaccharidosis IVA, MPS IVA) is a lysosomal storage disease caused by a deficiency of N-acetylgalactosamine-6-sulfate sulfatase, resulting in systemic accumulation of the partially degraded glycosaminoglycans (GAGs), keratan sulfate and chondroitin-6-sulfate."`
  - Use: proximal Type A -> storage connection.
- `PMID:29326877`
  - `"The accumulation of these GAGs leads to distinguishing features as skeletal dysplasia with disproportionate dwarfism, short neck, kyphoscoliosis, pectus carinatum, tracheal obstruction, coxa valga, genu valgum, and joint laxity."`
  - Use: shared skeletal phenotype cluster and respiratory/airway consequence cluster.
- `PMID:29326877`
  - `"As a result, partially degraded GAGs accumulate in bone, ligaments, and cartilage, as well as the extracellular matrix (ECM) of these tissues, impeding endochondral ossification and chondrogenesis"`
  - Use: the key bridge from lysosomal storage to cartilage/connective-tissue dysfunction.
- `PMID:29326877`
  - `"Examination of the tissues demonstrated systemic storage materials in multiple tissues, as well as severely ballooned and vacuolated chondrocytes in the trachea, humerus, knee cartilage, and lung bronchus."`
  - Use: explicit chondrocyte pathology node; supports the airway branch as well as skeletal disease.
- `PMID:29326877`
  - `"Individuals with MPS IVA, particularly with the severe form, often do not survive past their twenties, as the most attributed causes of mortality and morbidity are spinal cord compression, instability of the C1-C2 joint, and airway compromise including tracheal obstruction"`
  - Use: craniovertebral instability and airway compromise should be explicit terminal mechanism nodes, not hidden inside phenotype text.
- `PMID:25346323`
  - `"Morquio A syndrome (mucopolysaccharidosis IVA) is a lysosomal storage disorder associated with skeletal and joint abnormalities and significant non-skeletal manifestations including respiratory disease, spinal cord compression, cardiac disease, impaired vision, hearing loss, and dental problems."`
  - Use: extra-skeletal connective-tissue branch and phenotype support.
- `PMID:25346323`
  - `"Because of the heterogeneous and progressive nature of the disease, the management of patients with Morquio A syndrome is challenging and requires a multidisciplinary approach, involving an array of specialists."`
  - Use: supportive-care / multidisciplinary management framing.
- `PMID:33256811`
  - `"Early recognition, diagnosis, and treatment of this progressive, multisystem disease by enzyme replacement therapy (ERT) can lead to improved outcomes and reduced mortality."`
  - Use: ERT justification in Type A.
- `PMID:33256811`
  - `"All three patients demonstrated improvements in growth, 6-min walk distance, joint range of motion, and respiratory function after 30 months of ERT."`
  - Use: disease-modifying impact of elosulfase alfa on somatic function.
- `PMID:26331768`
  - `"Early intervention with elosulfase alfa is well-tolerated and produces a decrease in uKS and a trend toward improvement in growth."`
  - Use: early-treatment argument and storage-burden reduction.
- `PMID:30442189`
  - `"While ERT is effective in reducing urinary glycosaminoglycans (GAGs) and liver and spleen volume, cartilaginous organs such as the trachea and bronchi, bones and eyes are poorly impacted by ERT probably due to limited penetration in the specific tissue."`
  - Use: honest limitation note on Type A ERT.
- `PMID:32071837`
  - `"Forty-one of 51 cases with informative clinical data had pure MBD including progressive growth impairment, kyphoscoliosis, coxa/genua valga, joint laxity, platyspondyly, odontoid hypoplasia."`
  - Use: subtype B skeletal phenotype cluster and odontoid/cervical risk.
- `PMID:32071837`
  - `"Corneal clouding, cardiac valve pathology, hepatosplenomegaly, spinal cord compression were infrequent"`
  - Use: keep severe extra-skeletal and cord-compression claims on Type B framed as infrequent, not core.
- `PMID:29054894`
  - `"MPS type IVA (Morquio A syndrome) has predominant musculoskeletal system involvement and corneal clouding with normal intelligence and can be misdiagnosed as primary skeletal disorders in clinical practice."`
  - Use: root description, corneal phenotype, and preserved cognition framing.
- `PMID:8233358`
  - `"In addition to the characteristic dwarfism with skeletal deformities, odontoid anomalies, hearing loss and corneal clouding, the authors found almost identical lens opacities in all three patients."`
  - Use: odontoid, hearing, and corneal phenotype support.

## Pathograph that follows from the evidence

- `Type A GALNS deficiency` -> `keratan sulfate-dominant lysosomal storage in cartilage and connective tissue`
- `Type B GLB1 deficiency with keratan sulfate-biased catalytic loss` -> `keratan sulfate-dominant lysosomal storage in cartilage and connective tissue`
- `keratan sulfate-dominant lysosomal storage in cartilage and connective tissue` -> `cartilage matrix dysfunction and impaired endochondral ossification`
- `cartilage matrix dysfunction and impaired endochondral ossification` -> `progressive skeletal dysplasia and joint laxity`
- `progressive skeletal dysplasia and joint laxity` -> `craniovertebral instability and cervical cord compression`
- `progressive skeletal dysplasia and joint laxity` -> `airway narrowing and respiratory compromise`
- `keratan sulfate-dominant lysosomal storage in cartilage and connective tissue` -> `corneal and valvular connective tissue involvement`

## Curation consequences

- Make the disorder root `Morquio syndrome` anchored to `MONDO:0018938`.
- Keep `Type A` and `Type B` explicit in `has_subtypes`, prevalence, genetics, and treatments where appropriate.
- Restrict disease-modifying ERT to `Type A`.
- Keep the airway and craniovertebral branches explicit rather than folding them into a generic skeletal node.
- Avoid implying that Type B routinely has neuronopathic disease; mention spectrum overlap only in notes/PR reasoning.
