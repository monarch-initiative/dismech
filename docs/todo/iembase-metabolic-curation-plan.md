# IEMbase Metabolic Disease Curation Plan

Generated 2026-07-05 from `data/iembase/disease_index.json` and `data/iembase/dismech_mapping.tsv`. The source disease records were pre-fetched from the IEMbase v2 disorder API into `data/iembase/diseases/`.

This plan assigns every cached IEMbase disease record to one curation work package. Work packages follow the IEMbase classification hierarchy: collection -> group -> subgroup. Medium subgroups are kept intact; large subgroups are split by nosology order; small adjacent subgroups are merged only within the same IEMbase group.

## Coverage Validation

- IEMbase disease records covered: 2044
- Unique IEMbase IDs covered: 2044
- Work packages: 100
- Collections: 9
- Groups: 26
- Subgroups: 132
- Current DisMech mapping status: MAPPED 379, AMBIGUOUS 48, CANDIDATE 238, UNMAPPED 1379

Status meanings: `MAPPED` is the current local DisMech identifier or exact alias match; `AMBIGUOUS` has multiple exact local matches; `CANDIDATE` is a fuzzy review candidate; `UNMAPPED` has no confident local target. Treat short abbreviation-only `MAPPED` rows as audit items before counting them as true coverage, since abbreviations can be homonymous across diseases.

Package sizing rule: split subgroups larger than 30 records into nosology-ordered chunks of about 22 records, and merge adjacent small subgroups within the same IEMbase group until the package has about 20 records.

## Collection Backlog

| Collection | Records | MAPPED | AMBIGUOUS | CANDIDATE | UNMAPPED |
|---|---:|---:|---:|---:|---:|
| Cofactor and Mineral Metabolism | 145 | 31 | 2 | 12 | 100 |
| Complex Molecule and Organelle Metabolism | 416 | 79 | 5 | 51 | 281 |
| Intermediary Metabolism: Energy | 372 | 44 | 4 | 74 | 250 |
| Intermediary Metabolism: Nutrients | 240 | 53 | 12 | 31 | 144 |
| Intermediary Metabolism: Others | 10 | 2 | 0 | 0 | 8 |
| Lipid Metabolism and Transport | 211 | 32 | 5 | 32 | 142 |
| Metabolic Cell Signalling | 165 | 38 | 4 | 14 | 109 |
| Metabolism of Heterocyclic Compounds | 196 | 32 | 14 | 9 | 141 |
| Unclassified | 289 | 68 | 2 | 15 | 204 |

## Work Package Index

| WP | Collection | Group | Subgroup scope | Records | Status mix |
|---|---|---|---|---:|---|
| WP-001 | Intermediary Metabolism: Nutrients | Disorders of amino acid metabolism | Urea cycle disorders and inherited hyperammonemias; Organic acidurias | 27 | MAPPED 13, AMBIGUOUS 5, CANDIDATE 4, UNMAPPED 5 |
| WP-002 | Intermediary Metabolism: Nutrients | Disorders of amino acid metabolism | Disorders of branched-chain amino acid metabolism; Disorders of phenylalanine and tyrosine metabolism; Disorders of the metabolism of sulfur-containing amino acids and hydrogen sulfide | 28 | MAPPED 9, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 17 |
| WP-003 | Intermediary Metabolism: Nutrients | Disorders of amino acid metabolism | Disorders of glycine and serine metabolism; Disorders of ornithine, proline and hydroxyproline metabolism; Disorders of lysine, hydroxylysine, and tryptophan metabolism | 29 | MAPPED 6, AMBIGUOUS 2, CANDIDATE 1, UNMAPPED 20 |
| WP-004 | Intermediary Metabolism: Nutrients | Disorders of amino acid metabolism | Disorders of glutamate/glutamine and aspartate/asparagine metabolism; Disorders of histidine metabolism; Disorders of amino acid transport | 31 | MAPPED 4, AMBIGUOUS 2, CANDIDATE 3, UNMAPPED 22 |
| WP-005 | Intermediary Metabolism: Nutrients | Disorders of amino acid metabolism | Other disorders of amino acid metabolism | 1 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 0 |
| WP-006 | Intermediary Metabolism: Nutrients | Disorders of peptide and amine metabolism | Disorders of glutathione metabolism; Other disorders of peptide metabolism; Disorders of methylamine metabolism; Disorders of polyamine metabolism | 24 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 20 |
| WP-007 | Intermediary Metabolism: Nutrients | Disorders of carbohydrate metabolism | Disorders of galactose and fructose metabolism; Disorders of gluconeogenesis; Disorders of glycolysis | 33 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 26 |
| WP-008 | Intermediary Metabolism: Nutrients | Disorders of carbohydrate metabolism | Disorders of glycogen metabolism; Disorders of pentose phosphate metabolism | 27 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 10, UNMAPPED 12 |
| WP-009 | Intermediary Metabolism: Nutrients | Disorders of carbohydrate metabolism | Disorders of carbohydrate transmembrane transport and absorption; Other disorders of carbohydrate metabolism | 12 | MAPPED 1, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 9 |
| WP-010 | Intermediary Metabolism: Nutrients | Disorders of fatty acid and ketone body metabolism | Disorders of carnitine metabolism ; Disorders of mitochondrial fatty acid oxidation | 21 | MAPPED 6, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 9 |
| WP-011 | Intermediary Metabolism: Nutrients | Disorders of fatty acid and ketone body metabolism | Disorders of ketone body metabolism | 7 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 4 |
| WP-012 | Intermediary Metabolism: Energy | Disorders of energy substrate metabolism | Disorders of pyruvate metabolism; Disorders of the Krebs cycle | 28 | MAPPED 10, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 14 |
| WP-013 | Intermediary Metabolism: Energy | Disorders of energy substrate metabolism | Disorders of creatine metabolism | 4 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 1 |
| WP-014 | Intermediary Metabolism: Energy | mtDNA-related disorders | Disorders of mtDNA-encoded oxidative phosphorylation proteins; Disorders of mtDNA-encoded tRNA and rRNA | 38 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 37 |
| WP-015 | Intermediary Metabolism: Energy | mtDNA-related disorders | Disorders associated with single large-scale mtDNA deletions | 2 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2 |
| WP-016 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex I subunits and assembly factors / part 1 of 2 | 22 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 16, UNMAPPED 6 |
| WP-017 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex I subunits and assembly factors / part 2 of 2 | 20 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 12, UNMAPPED 8 |
| WP-018 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex II subunits and assembly factors; Disorders of complex III subunits and assembly factors | 22 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 10, UNMAPPED 12 |
| WP-019 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex IV subunits and assembly factors / part 1 of 2 | 22 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 14 |
| WP-020 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex IV subunits and assembly factors / part 2 of 2 | 11 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 5 |
| WP-021 | Intermediary Metabolism: Energy | Nuclear-encoded disorders of oxidative phosphorylation | Disorders of complex V subunits and assembly factors | 9 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 6 |
| WP-022 | Intermediary Metabolism: Energy | Disorders of mitochondrial cofactor biosynthesis | Disorders of coenzyme Q10 biosynthesis; Disorders of lipoic acid and iron-sulfur metabolism | 30 | MAPPED 9, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 15 |
| WP-023 | Intermediary Metabolism: Energy | Disorders of mitochondrial cofactor biosynthesis | Disorders of mitochondrial cytochrome c biosynthesis | 1 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 1 |
| WP-024 | Intermediary Metabolism: Energy | Disorders of mitochondrial DNA maintenance and replication | Disorders of mitochondrial nucleotide pool maintenance; Disorders of mtDNA replication and maintenance | 21 | MAPPED 1, AMBIGUOUS 3, CANDIDATE 7, UNMAPPED 10 |
| WP-025 | Intermediary Metabolism: Energy | Disorders of mitochondrial gene expression | Disorders of mitochondrial transcript processing and modification | 21 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 17 |
| WP-026 | Intermediary Metabolism: Energy | Disorders of mitochondrial gene expression | Disorders of mitochondrial aminoacyl-tRNA synthetases | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 19 |
| WP-027 | Intermediary Metabolism: Energy | Disorders of mitochondrial gene expression | Disorders of the mitoribosome | 29 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 27 |
| WP-028 | Intermediary Metabolism: Energy | Other disorders of mitochondrial function | Disorders of mitochondrial shuttles and carriers; Disorders of mitochondrial protein import | 26 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 21 |
| WP-029 | Intermediary Metabolism: Energy | Other disorders of mitochondrial function | Disorders of mitochondrial protein quality control | 26 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 19 |
| WP-030 | Intermediary Metabolism: Energy | Other disorders of mitochondrial function | Miscellaneous disorders associated with mitochondrial dysfunction | 18 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 16 |
| WP-031 | Intermediary Metabolism: Others | Disorders of metabolite repair/proofreading | Disorders of mitochondrial metabolite repair; Disorders of non-mitochondrial metabolite repair | 4 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2 |
| WP-032 | Intermediary Metabolism: Others | Miscellaneous disorders of intermediary metabolism | Disorders of glyoxylate and oxalate metabolism; Unassigned disorders of intermediary metabolism | 6 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6 |
| WP-033 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of fatty acyl synthesis, elongation, and recycling; Disorders of peroxisomal fatty acid oxidation | 21 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 17 |
| WP-034 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of eicosanoid metabolism; Disorders of glycerolipid metabolism; Disorders of glycerophospholipid metabolism | 21 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 3, UNMAPPED 13 |
| WP-035 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of phosphatidylcholine, phosphatidylserine and phosphatidylethanolamine metabolism | 25 | MAPPED 2, AMBIGUOUS 1, CANDIDATE 5, UNMAPPED 17 |
| WP-036 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of phosphatidylinositol metabolism / part 1 of 2 | 22 | MAPPED 2, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 15 |
| WP-037 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of phosphatidylinositol metabolism / part 2 of 2 | 16 | MAPPED 1, AMBIGUOUS 1, CANDIDATE 2, UNMAPPED 12 |
| WP-038 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of ether lipid metabolism; Disorders of sphingolipid synthesis and recycling | 31 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 11, UNMAPPED 15 |
| WP-039 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of sterol biosynthesis | 20 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 15 |
| WP-040 | Lipid Metabolism and Transport | Disorders of lipid metabolism | Disorders of bile acid metabolism | 18 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 11 |
| WP-041 | Lipid Metabolism and Transport | Disorders of lipoprotein metabolism | Hypercholesterolemias; Hypertriglyceridemias; Mixed hyperlipidemias | 22 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 17 |
| WP-042 | Lipid Metabolism and Transport | Disorders of lipoprotein metabolism | Disorders of high-density lipoprotein (HDL) metabolism; Disorders with decreased low-density lipoprotein (LDL) and/or triglycerides; Other disorders of lipoprotein metabolism | 15 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 10 |
| WP-043 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of pyrimidine metabolism; Disorders of purine metabolism | 41 | MAPPED 6, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 32 |
| WP-044 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of ectonucleotide and nucleic acid metabolism | 29 | MAPPED 3, AMBIGUOUS 10, CANDIDATE 0, UNMAPPED 16 |
| WP-045 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases / part 1 of 3 | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 17 |
| WP-046 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases / part 2 of 3 | 22 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 19 |
| WP-047 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases / part 3 of 3 | 2 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2 |
| WP-048 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of ribosomal biogenesis / part 1 of 3 | 22 | MAPPED 9, AMBIGUOUS 2, CANDIDATE 1, UNMAPPED 10 |
| WP-049 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of ribosomal biogenesis / part 2 of 3 | 22 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 22 |
| WP-050 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of ribosomal biogenesis / part 3 of 3 | 15 | MAPPED 1, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 12 |
| WP-051 | Metabolism of Heterocyclic Compounds | Disorders of nucleobase, nucleotide and nucleic acid metabolism | Disorders of purine and pyrimidine matabolism | 2 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 0 |
| WP-052 | Metabolism of Heterocyclic Compounds | Disorders of tetrapyrrole metabolism | Disorders of heme synthesis and porphyrias; Disorders of heme degradation and bilirubin metabolism | 19 | MAPPED 7, AMBIGUOUS 1, CANDIDATE 0, UNMAPPED 11 |
| WP-053 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of N-linked protein glycosylation / part 1 of 2 | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 15 |
| WP-054 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of N-linked protein glycosylation / part 2 of 2 | 20 | MAPPED 1, AMBIGUOUS 2, CANDIDATE 6, UNMAPPED 11 |
| WP-055 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of O-linked protein glycosylation / part 1 of 2 | 22 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 20 |
| WP-056 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of O-linked protein glycosylation / part 2 of 2 | 16 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 13 |
| WP-057 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of O-fucosylation; Disorders of glycosaminoglycan synthesis and O-xylosylation; Other disorders of O-linked protein glycosylation | 23 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 21 |
| WP-058 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of lipid glycosylation; Disorders of glycosylphosphatidylinositol biosynthesis | 29 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 24 |
| WP-059 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of multiple glycosylation pathways / part 1 of 2 | 22 | MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 17 |
| WP-060 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Disorders of multiple glycosylation pathways / part 2 of 2 | 14 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 5, UNMAPPED 8 |
| WP-061 | Complex Molecule and Organelle Metabolism | Congenital disorders of glycosylation | Other disorders of multiple glycosylation pathways; Disorders of deglycosylation | 5 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 5 |
| WP-062 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of mitochondrial membrane biogenesis and remodeling; Disorders of mitochondrial and peroxisomal dynamics | 28 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 25 |
| WP-063 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Peroxisomal biogenesis disorders; Disorders of lysosome-related organelle biogenesis | 33 | MAPPED 3, AMBIGUOUS 1, CANDIDATE 5, UNMAPPED 24 |
| WP-064 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of organelle interplay | 9 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6 |
| WP-065 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of vesicular trafficking / part 1 of 4 | 22 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 12 |
| WP-066 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of vesicular trafficking / part 2 of 4 | 22 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 16 |
| WP-067 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of vesicular trafficking / part 3 of 4 | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 19 |
| WP-068 | Complex Molecule and Organelle Metabolism | Disorders of organelle biogenesis, dynamics and interactions | Disorders of vesicular trafficking / part 4 of 4 | 5 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 3 |
| WP-069 | Complex Molecule and Organelle Metabolism | Disorders of complex molecule degradation | Disorders of sphingolipid degradation; Disorders of glycosaminoglycan degradation | 30 | MAPPED 20, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 5 |
| WP-070 | Complex Molecule and Organelle Metabolism | Disorders of complex molecule degradation | Disorders of glycoprotein degradation; Neuronal ceroid lipofuscinosis | 24 | MAPPED 15, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 9 |
| WP-071 | Complex Molecule and Organelle Metabolism | Disorders of complex molecule degradation | Disorders of autophagy | 29 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 6, UNMAPPED 18 |
| WP-072 | Complex Molecule and Organelle Metabolism | Disorders of complex molecule degradation | Other disorders of complex molecule degradation | 19 | MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 10 |
| WP-073 | Cofactor and Mineral Metabolism | Disorders of vitamin and cofactor metabolism | Disorders of tetrahydrobiopterin metabolism; Disorders of thiamine metabolism; Disorders of riboflavin metabolism; Disorders of niacin and NAD metabolism | 24 | MAPPED 4, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 15 |
| WP-074 | Cofactor and Mineral Metabolism | Disorders of vitamin and cofactor metabolism | Disorders of pantothenate and CoA metabolism; Disorders of pyridoxine metabolism; Disorders of biotin metabolism; Disorders of folate metabolism | 24 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 18 |
| WP-075 | Cofactor and Mineral Metabolism | Disorders of vitamin and cofactor metabolism | Disorders of cobalamin metabolism; Disorders of molybdenum cofactor metabolism | 24 | MAPPED 8, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 14 |
| WP-076 | Cofactor and Mineral Metabolism | Disorders of vitamin and cofactor metabolism | Other disorders of vitamin metabolism | 23 | MAPPED 7, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 14 |
| WP-077 | Cofactor and Mineral Metabolism | Disorders of trace elements and metals | Disorders of copper metabolism; Disorders of iron metabolism | 27 | MAPPED 7, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 18 |
| WP-078 | Cofactor and Mineral Metabolism | Disorders of trace elements and metals | Disorders of manganese metabolism; Disorders of zinc metabolism | 20 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 18 |
| WP-079 | Cofactor and Mineral Metabolism | Disorders of trace elements and metals | Other disorders of trace element metabolism | 3 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 3 |
| WP-080 | Metabolic Cell Signalling | Neurotransmitter disorders | Monoamine neurotransmission; Gamma-aminobutyric acid neurotransmitter disorders | 21 | MAPPED 5, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 14 |
| WP-081 | Metabolic Cell Signalling | Neurotransmitter disorders | Glutamate neurotransmitter disorders; Glycine neurotransmitter disorders; Disorders of choline neurotransmission | 40 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 32 |
| WP-082 | Metabolic Cell Signalling | Neurotransmitter disorders | Disorders of the synaptic vesicle cycle / part 1 of 2 | 22 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 18 |
| WP-083 | Metabolic Cell Signalling | Neurotransmitter disorders | Disorders of the synaptic vesicle cycle / part 2 of 2 | 12 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 8 |
| WP-084 | Metabolic Cell Signalling | Endocrine metabolic disorders | Disorders of insulin metabolism / part 1 of 2 | 22 | MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 13 |
| WP-085 | Metabolic Cell Signalling | Endocrine metabolic disorders | Disorders of insulin metabolism / part 2 of 2 | 11 | MAPPED 3, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 6 |
| WP-086 | Metabolic Cell Signalling | Endocrine metabolic disorders | Disorders of steroid metabolism / part 1 of 2 | 22 | MAPPED 11, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 10 |
| WP-087 | Metabolic Cell Signalling | Endocrine metabolic disorders | Disorders of steroid metabolism / part 2 of 2 | 15 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 8 |
| WP-088 | Unclassified | Unclassified | Unclassified / part 1 of 2 | 22 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 17 |
| WP-089 | Unclassified | Unclassified | Unclassified / part 2 of 2 | 22 | MAPPED 5, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 15 |
| WP-090 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM glycoproteins / part 1 of 5 | 22 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 20 |
| WP-091 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM glycoproteins / part 2 of 5 | 22 | MAPPED 4, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 16 |
| WP-092 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM glycoproteins / part 3 of 5 | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 18 |
| WP-093 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM glycoproteins / part 4 of 5 | 22 | MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 18 |
| WP-094 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM glycoproteins / part 5 of 5 | 2 | MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2 |
| WP-095 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of fibrillar collagens / part 1 of 2 | 22 | MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 15 |
| WP-096 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of fibrillar collagens / part 2 of 2 | 18 | MAPPED 7, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 10 |
| WP-097 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of  fibrillar collagen processing and maturation | 24 | MAPPED 17, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 7 |
| WP-098 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of ECM proteoglycans; Disorders of non-fibrillar collagens | 48 | MAPPED 7, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 39 |
| WP-099 | Unclassified | Disorders of the extracellular matrix (under construction) | Other disorders of connective tissue | 28 | MAPPED 6, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 21 |
| WP-100 | Unclassified | Disorders of the extracellular matrix (under construction) | Disorders of proteins in TGF-g signaling pathway | 15 | MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6 |

## Work Packages

### WP-001: Urea cycle disorders and inherited hyperammonemias + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of amino acid metabolism
- Subgroup scope: Urea cycle disorders and inherited hyperammonemias; Organic acidurias
- Records: 27 (MAPPED 13, AMBIGUOUS 5, CANDIDATE 4, UNMAPPED 5)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 12 | 1.1.01.01 | NAGS-related N-Acetylglutamate synthase deficiency | NAGS | 237310 | - | AMBIGUOUS: 2 local entities (alias_exact:n acetylglutamate synthase deficiency) |
| [ ] | 567 | 1.1.01.02 | GLUD1-related Glutamate dehydrogenase superactivity | GLUD1 | 606762 | 35878 | MAPPED -> HI/HA Syndrome (alias_exact:hyperinsulinism hyperammonemia syndrome) |
| [ ] | 11 | 1.1.02.01 | CPS1-related Carbamoyl phosphate synthetase I deficiency | CPS1 | 237300 | - | AMBIGUOUS: 2 local entities (alias_exact:carbamoyl phosphate synthetase i deficiency) |
| [ ] | 13 | 1.1.03.01 | OTC-related Ornithine transcarbamylase deficiency | OTC | 311250 | 664 | AMBIGUOUS: 2 local entities (alias_exact:ornithine carbamoyltransferase deficiency) |
| [ ] | 14 | 1.1.04.01 | ASS1-related Argininosuccinate synthetase deficiency | ASS1 | 215700 | - | AMBIGUOUS: 2 local entities (alias_exact:argininosuccinate synthetase deficiency) |
| [ ] | 15 | 1.1.05.01 | ASL-related Argininosuccinate lyase deficiency | ASL | 207900 | - | AMBIGUOUS: 2 local entities (alias_exact:argininosuccinate lyase deficiency) |
| [ ] | 16 | 1.1.06.01 | ARG1-related Arginase 1 deficiency | ARG1 | 207800 | - | MAPPED -> Arginase Deficiency (alias_exact:arg1 deficiency) |
| [ ] | 17 | 1.1.07.01 | SLC25A15-related Mitochondrial ornithine transporter deficiency | SLC25A15 | 238970 | - | MAPPED -> Hyperornithinemia-hyperammonemia-homocitrullinuria syndrome (identifier:OMIM:238970) |
| [ ] | 18 | 1.1.08.01 | SLC25A13-related Citrin deficiency | SLC25A13 | 605814;603471 | - | MAPPED -> Citrin Deficiency (alias_exact:citrin deficiency) |
| [ ] | 656 | 1.1.09.01 | CA5A-related Carbonic anhydrase VA deficiency | CA5A | 615751 | 401948 | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.769) |
| [ ] | 57 | 1.2.1.01 | MCCC1-related 3-Methylcrotonyl-CoA carboxylase 1 deficiency | MCCC1 | 210200 | - | CANDIDATE -> 3-Methylcrotonyl-CoA Carboxylase Deficiency (0.977) |
| [ ] | 544 | 1.2.2.01 | MCEE-related Methylmalonic aciduria due to methylmalonyl-CoA epimerase deficiency | MCEE | 251120 | 308425 | CANDIDATE -> Methylmalonic Acidemia (0.957) |
| [ ] | 163 | 1.2.05.01 | GCDH-related Glutaryl-CoA dehydrogenase deficiency | GCDH | 231670 | 25 | MAPPED -> Glutaryl-CoA Dehydrogenase Deficiency (alias_exact:glutaric acidemia type 1) |
| [ ] | 537 | 1.2.06.01 | SUGCT-related Succinate-hydroxymethylglutarate-CoA transferase deficiency | SUGCT | 231690 | 35706 | CANDIDATE -> Glutaryl-CoA Dehydrogenase Deficiency (0.958) |
| [ ] | 56 | 1.2.07.01 | IVD-related Isovaleryl-CoA dehydrogenase deficiency | IVD | 243500 | - | MAPPED -> Isovaleric Acidemia (alias_exact:isovaleric acidemia) |
| [ ] | 135 | 1.2.08.01 | ACAD8-related Isobutyryl-CoA dehydrogenase deficiency | ACAD8 | 611283 | 79159 | MAPPED -> Isobutyryl-CoA Dehydrogenase Deficiency (alias_exact:isobutyryl coa dehydrogenase deficiency) |
| [ ] | 63 | 1.2.09.01 | ACADSB-related 2-Methylbutyryl-CoA dehydrogenase deficiency | ACADSB | 610006 | - | MAPPED -> 2-Methylbutyryl-CoA Dehydrogenase Deficiency (alias_exact:2 methylbutyryl coa dehydrogenase deficiency) |
| [ ] | 1284 | 1.2.11.01 | MCCC2-related 3-Methylcrotonyl-CoA carboxylase 2 deficiency | MCCC2 | 210200 | 6 | MAPPED -> 3-Methylcrotonyl-CoA Carboxylase Deficiency (identifier:ORPHA:6) |
| [ ] | 58 | 1.2.12.01 | AUH-related 3-Methylglutaconyl-CoA hydratase deficiency | AUH | 250950 | - | UNMAPPED; weak candidate Glutaryl-CoA Dehydrogenase Deficiency (0.793) |
| [ ] | 665 | 1.2.13.01 | ECHS1-related Mitochondrial short-chain enoyl-CoA hydratase 1 deficiency | ECHS1 | 616277 | 255241 | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.710) |
| [ ] | 66 | 1.2.14.01 | HIBCH-related 3-hydroxyisobutyryl-CoA hydrolase deficiency | HIBCH | 250620 | - | MAPPED -> 3-hydroxyisobutyryl-CoA hydrolase deficiency (alias_exact:3 hydroxyisobutyryl coa hydrolase deficiency) |
| [ ] | 136 | 1.2.17.01 | ALDH6A1-related Methylmalonate semialdehyde dehydrogenase deficiency | ALDH6A1 | 603178 | 289307 | UNMAPPED; weak candidate Succinic Semialdehyde Dehydrogenase Deficiency (0.796) |
| [ ] | 68 | 1.2.18.01 | PCCA-related Propionic acidemia | PCCA | 232000 | - | MAPPED -> Propionic Acidemia (alias_exact:propionic acidemia) |
| [ ] | 1253 | 1.2.19.01 | PCCB-related Propionic acidemia due to propionyl-CoA carboxylase subunit beta deficiency | PCCB | 232000 | 35 | UNMAPPED; weak candidate Propionic Acidemia (0.649) |
| [ ] | 69 | 1.2.21.01 | MMUT-related Methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency | MMUT | 251000 | - | MAPPED -> Methylmalonic Acidemia (alias_exact:mma) |
| [ ] | 177 | 1.2.23.01 | MLYCD-related Malonyl-CoA decarboxylase deficiency | MLYCD | 248360 | 943 | MAPPED -> Migraine with aura (alias_exact:ma) |
| [ ] | 67 | 1.2.25.01 | HIBADH-related 3-Hydroxyisobutyrate dehydrogenase deficiency | HIBADH | 608475 | - | CANDIDATE -> Succinic Semialdehyde Dehydrogenase Deficiency (0.906) |

### WP-002: Disorders of branched-chain amino acid metabolism + 2 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of amino acid metabolism
- Subgroup scope: Disorders of branched-chain amino acid metabolism; Disorders of phenylalanine and tyrosine metabolism; Disorders of the metabolism of sulfur-containing amino acids and hydrogen sulfide
- Records: 28 (MAPPED 9, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 134 | 1.3.01.01 | BCAT2-related Branched-chain aminotransferase 2 deficiency | BCAT2 | 238340;113530 | - | UNMAPPED; weak candidate ornithine aminotransferase deficiency (0.815) |
| [ ] | 55 | 1.3.02.01 | BCKDHA-related Branched-chain ketoacid dehydrogenase E1 alpha deficiency | BCKDHA | 248600 | - | UNMAPPED; weak candidate Maple Syrup Urine Disease (0.862) |
| [ ] | 1251 | 1.3.03.01 | BCKDHB-related Branched-chain ketoacid dehydrogenase E1 beta deficiency | BCKDHB | 248600 | 268173 | UNMAPPED; weak candidate Maple Syrup Urine Disease (0.862) |
| [ ] | 1252 | 1.3.04.01 | DBT-related Dihydrolipoyl transacylase deficiency | DBT | 248600 | 268173 | UNMAPPED; weak candidate Maple Syrup Urine Disease (0.877) |
| [ ] | 664 | 1.3.06.01 | BCKDK-related Branched-chain ketoacid dehydrogenase kinase deficiency | BCKDK | 614923 | 308410 | MAPPED -> BCKDK Deficiency (alias_exact:bckdkd) |
| [ ] | 663 | 1.3.24.01 | PPM1K-related Branched-chain ketoacid dehydrogenase phosphatase deficiency | PPM1K | 615135 | 268162 | UNMAPPED; weak candidate Maple Syrup Urine Disease (0.794) |
| [ ] | 1 | 1.4.01.01 | PAH-related Phenylalanine hydroxylase deficiency | PAH | 261600 | - | MAPPED -> Phenylketonuria (identifier:OMIM:261600) |
| [ ] | 802 | 1.4.01.02 | TYR-related Tyrosinase deficiency | TYR | 203100 | 352731 | MAPPED -> OCA1A (alias_exact:oca1a) |
| [ ] | 20 | 1.4.02.01 | TAT-related Tyrosine aminotransferase deficiency | TAT | 276600 | - | CANDIDATE -> Tyrosinemia Type I (0.944) |
| [ ] | 21 | 1.4.03.01 | HPD-related 4-hydroxyphenylpyruvate dioxygenase deficiency | HPD | 276710 | - | UNMAPPED; weak candidate Alkaptonuria (0.698) |
| [ ] | 22 | 1.4.04.01 | HPD-related Hawkinsinuria | HPD | 140350 | - | UNMAPPED; weak candidate Alkaptonuria (0.511) |
| [ ] | 23 | 1.4.05.01 | HGD-related Homogentisic acid oxidase deficiency | HGD | 203500 | - | MAPPED -> Alkaptonuria (alias_exact:aku) |
| [ ] | 803 | 1.4.06.01 | GSTZ1-related Maleylacetoacetate isomerase deficiency | GSTZ1 | 617596 | - | UNMAPPED; weak candidate Benign Prostatic Hyperplasia (0.552) |
| [ ] | 19 | 1.4.07.01 | FAH-related Fumarylacetoacetase deficiency | FAH | 276700 | - | MAPPED -> Tyrosinemia Type I (alias_exact:fumarylacetoacetase deficiency) |
| [ ] | 24 | 1.5.01.01 | MAT1A-related Methionine adenosyltransferase I-III deficiency | MAT1A | 250850 | - | MAPPED -> MAT I/III deficiency (alias_exact:methionine adenosyltransferase i iii deficiency) |
| [ ] | 172 | 1.5.1.01 | ETHE1-related Mitochondrial sulfur dioxygenase deficiency | ETHE1 | 602473 | 51188 | UNMAPPED; weak candidate Chronic Traumatic Encephalopathy (0.784) |
| [ ] | 1283 | 1.5.02.01 | MAT1A-related Methionine adenosyltransferase I/III deficiency (dominant) | MAT1A | 250850 | 168598 | CANDIDATE -> MAT I/III deficiency (0.913) |
| [ ] | 25 | 1.5.03.01 | GNMT-related Glycine N-methyltransferase deficiency | GNMT | 606664 | - | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.795) |
| [ ] | 26 | 1.5.04.01 | AHCY-related S-adenosylhomocysteine hydrolase deficiency | AHCY | 613752 | - | UNMAPPED; weak candidate Cholesteryl Ester Storage Disease (0.602) |
| [ ] | 549 | 1.5.05.01 | ADK-related Adenosine kinase deficiency | ADK | 614300 | 289290 | MAPPED -> Adenosine Kinase Deficiency (alias_exact:adenosine kinase deficiency) |
| [ ] | 27 | 1.5.06.01 | CBS-related Cystathionine beta-synthase deficiency | CBS | 236200 | - | MAPPED -> Homocystinuria (alias_exact:classical homocystinuria) |
| [ ] | 28 | 1.5.07.01 | CTH-related Cystathionine gamma-lyase deficiency | CTH | 219500 | - | UNMAPPED; weak candidate Homocystinuria (0.838) |
| [ ] | 804 | 1.5.08.01 | SELENBP1-related Methanethiol oxidase deficiency | SELENBP1 | 604188 | - | UNMAPPED; weak candidate Chronic Granulomatous Disease (0.727) |
| [ ] | 29 | 1.5.09.01 | SUOX-related Isolated sulfite oxidase deficiency | SUOX | 272300 | - | UNMAPPED; weak candidate SCO1-Related COX Deficiency (0.734) |
| [ ] | 1160 | 1.5.11.01 | MAT2A-related Methionine adenosyltransferase II deficiency | MAT2A | 601468 | - | UNMAPPED |
| [ ] | 1401 | 1.5.11.02 | SQOR-related Mitochondrial sulfide:quinone oxidoreductase deficiency | SQOR | 619221 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.646) |
| [ ] | 1347 | 1.5.12.01 | MPST-related Mercaptopyruvate sulfurtransferase deficiency | MPST | 602496 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.486) |
| [ ] | 30 | 1.5.13.01 | MTR-related Methionine synthase deficiency | MTR | 250940 | - | MAPPED -> cblG (alias_exact:cblg) |

### WP-003: Disorders of glycine and serine metabolism + 2 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of amino acid metabolism
- Subgroup scope: Disorders of glycine and serine metabolism; Disorders of ornithine, proline and hydroxyproline metabolism; Disorders of lysine, hydroxylysine, and tryptophan metabolism
- Records: 29 (MAPPED 6, AMBIGUOUS 2, CANDIDATE 1, UNMAPPED 20)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 32 | 1.6.01.01 | GLDC-related Nonketotic hyperglycinemia due to glycine decarboxylase deficiency | GLDC | 238300 | - | MAPPED -> Nonketotic Hyperglycinemia (alias_exact:glycine encephalopathy) |
| [ ] | 33 | 1.6.01.02 | PHGDH-related 3-phosphoglycerate dehydrogenase deficiency | PHGDH | 601815 | - | UNMAPPED |
| [ ] | 35 | 1.6.02.01 | PSAT1-related Phosphoserine aminotransferase deficiency | PSAT1 | 610992;610936 | - | UNMAPPED; weak candidate ornithine aminotransferase deficiency (0.821) |
| [ ] | 1254 | 1.6.02.02 | AMT-related Nonketotic hyperglycinemia due to aminomethyltransferase deficiency | AMT | 605899 | 407 | MAPPED -> Nonketotic Hyperglycinemia (alias_exact:glycine encephalopathy) |
| [ ] | 34 | 1.6.03.01 | PSPH-related Phosphoserine phosphatase deficiency | PSPH | 172480;614023 | - | UNMAPPED; weak candidate PDH phosphatase deficiency (0.806) |
| [ ] | 831 | 1.6.04.01 | SLC1A4-related ASCT1 transporter deficiency | SLC1A4 | 616657 | 447997 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.833) |
| [ ] | 1465 | 1.6.05.01 | SHMT2-related Mitochondrial serine hydroxymethyltransferase deficiency | SHMT2 | 138450 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.660) |
| [ ] | 1255 | 1.6.08.01 | GCSH-related Glycine encephalopathy due to H protein deficiency | GCSH | 620423 | 407 | MAPPED -> Nonketotic Hyperglycinemia (alias_exact:glycine encephalopathy) |
| [ ] | 2189 | 1.6.09.01 | GLYAT-related Glycine N-acyltransferase deficiency | GLYAT | 607424 | - | UNMAPPED; weak candidate AGAT Deficiency (0.756) |
| [ ] | 395 | 1.7.01.01 | ALDH18A1-related Delta-1-pyrroline-5-carboxylate synthase deficiency, cutis laxa phenotype | ALDH18A1 | 219150 | 90348 | MAPPED -> ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (alias_exact:autosomal recessive cutis laxa type 3a) |
| [ ] | 562 | 1.7.1.01 | OAT-related Ornithine aminotransferase deficiency | OAT | 258870 | 414 | MAPPED -> ornithine aminotransferase deficiency (alias_exact:gyrate atrophy of the choroid and retina) |
| [ ] | 1286 | 1.7.02.01 | ALDH18A1-related Delta-1-pyrroline-5-carboxylate synthase deficiency, spastic paraplegia phenotype | ALDH18A1 | 219150 | 90348 | AMBIGUOUS: 2 local entities (alias_exact:spg9b) |
| [ ] | 504 | 1.7.02.02 | HOGA1-related Mitochondrial 4-hydroxy-2-oxoglutarate aldolase 1 deficiency deficiency | HOGA1 | 613616 | 93600 | UNMAPPED; weak candidate Primary erythromelalgia (0.588) |
| [ ] | 807 | 1.7.03.01 | PYCR1-related Pyrroline-5-carboxylate reductase 1 deficiency | PYCR1 | 612940;614438 | 293633 | CANDIDATE -> ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (0.974) |
| [ ] | 808 | 1.7.04.01 | PYCR2-related Pyrroline-5-carboxylate reductase 2 deficiency | PYCR2 | 616420 | 481152 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.886) |
| [ ] | 40 | 1.7.05.01 | PRODH-related Proline dehydrogenase deficiency | PRODH | 239500 | - | UNMAPPED |
| [ ] | 38 | 1.7.06.01 | ALDH4A1-related Pyrroline-5-carboxylate dehydrogenase deficiency | ALDH4A1 | 239510 | - | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.765) |
| [ ] | 809 | 1.7.07.01 | PRODH2-related Hydroxyproline dehydrogenase deficiency | PRODH2 | 616377 | 419 | UNMAPPED; weak candidate 3B-HSD (0.824) |
| [ ] | 42 | 1.7.14.01 | ALDH18A1-related Pyrroline-5-carboxylate synthetase deficiency | ALDH18A1 | 138250;219150 | - | AMBIGUOUS: 2 local entities (alias_exact:spg9a) |
| [ ] | 43 | 1.8.01.01 | AASS-related Alpha-aminoadipic semialdehyde synthase deficiency | AASS | 268700 | - | UNMAPPED; weak candidate Succinic Semialdehyde Dehydrogenase Deficiency (0.708) |
| [ ] | 652 | 1.8.01.02 | KYNU-related 3-Hydroxykynureninase deficiency | KYNU | 605197 | 79155 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.686) |
| [ ] | 651 | 1.8.02.01 | HAAO-related 3-Hydroxyanthranilic acid 3,4-dioxygenase deficiency | HAAO | 604521 | - | UNMAPPED; weak candidate Alkaptonuria (0.652) |
| [ ] | 618 | 1.8.03.01 | TDO2-related Hypertryptophanemia | TDO2 | 600627 | 2224 | UNMAPPED; weak candidate Alkaptonuria (0.701) |
| [ ] | 655 | 1.8.03.02 | DHTKD1-related 2-Aminoadipic 2-oxoadipic aciduria | DHTKD1 | 204750 | 79154 | UNMAPPED; weak candidate D-2-Hydroxyglutaric Aciduria (0.581) |
| [ ] | 1165 | 1.8.04.01 | ACMSD-related Aminocarboxymuconate semialdehyde decarboxylase superactivity | ACMSD | 608889 | - | UNMAPPED; weak candidate PRPS1 Superactivity (0.618) |
| [ ] | 1285 | 1.8.04.02 | DHTKD1-related  Charcot-Marie-Tooth disease | DHTKD1 | 204750 | 79154 | MAPPED -> Charcot-Marie-Tooth Disease (alias_exact:charcot marie tooth disease) |
| [ ] | 1164 | 1.8.05.01 | KMO-related Kynurenine-3-hydroxylase deficiency | KMO | 603538 | - | UNMAPPED; weak candidate Autosomal Recessive Dopa-Responsive Dystonia (0.848) |
| [ ] | 806 | 1.8.07.01 | PHYKPL-related 5-phosphohydroxylysine phospholyase deficiency | PHYKPL | 615011 | - | UNMAPPED |
| [ ] | 1161 | 1.8.08.01 | HYKK-related Hydroxylysinuria | HYKK | 614681 | - | UNMAPPED |

### WP-004: Disorders of glutamate/glutamine and aspartate/asparagine metabolism + 2 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of amino acid metabolism
- Subgroup scope: Disorders of glutamate/glutamine and aspartate/asparagine metabolism; Disorders of histidine metabolism; Disorders of amino acid transport
- Records: 31 (MAPPED 4, AMBIGUOUS 2, CANDIDATE 3, UNMAPPED 22)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 41 | 1.9.01.01 | GLUL-related Glutamine synthetase deficiency | GLUL | 610015 | 71278 | UNMAPPED; weak candidate Lipoic Acid Synthetase Deficiency (0.781) |
| [ ] | 830 | 1.9.01.02 | ASNS-related Asparagine synthetase deficiency | ASNS | 615574 | 391376 | UNMAPPED; weak candidate Citrullinemia Type I (0.789) |
| [ ] | 164 | 1.9.01.03 | ASPA-related Aspartoacylase deficiency | ASPA | 271900 | 314911 | MAPPED -> Canavan disease (identifier:OMIM:271900) |
| [ ] | 1363 | 1.9.02.01 | GLS-related Glutaminase deficiency | GLS | 618328 | - | UNMAPPED |
| [ ] | 1167 | 1.9.03.01 | GLS-related Glutaminase 1 superactivity | GLS | 138280 | - | UNMAPPED |
| [ ] | 1324 | 1.9.15.01 | GPT2-related Glutamate pyruvate transaminase 2 deficiency | GPT2 | 616281 | - | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.775) |
| [ ] | 1166 | 1.9.16.01 | GAD1-related Glutamate decarboxylase 1 deficiency | GAD1 | 603513 | 210141 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.732) |
| [ ] | 1696 | 1.9.17.01 | NAT8L-related Aspartate N-acetyltransferase deficiency | NAT8L | 614063 | - | UNMAPPED |
| [ ] | 45 | 1.10.01.01 | HAL-related Histidine ammonia-lyase deficiency | HAL | 235800 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaric Aciduria (0.724) |
| [ ] | 46 | 1.10.02.01 | UROC1-related Urocanase deficiency | UROC1 | 276880 | - | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.812) |
| [ ] | 50 | 1.11.01.01 | SLC6A19-related Hartnup disorder | SLC6A19 | 234500 | - | MAPPED -> Hartnup Disease (alias_exact:hartnup disorder) |
| [ ] | 1337 | 1.11.1.01 | SLC6A17-related Vesicular neutral amino acid transporter 3 deficiency | SLC6A17 | 616269 | - | UNMAPPED; weak candidate Autosomal Recessive Osteopetrosis Type 2 (0.703) |
| [ ] | 525 | 1.11.01.02 | CTNS-related Nephropathic cystinosis | CTNS | 219800;219900;219750 | 411634 | AMBIGUOUS: 2 local entities (identifier:OMIM:219750) |
| [ ] | 39 | 1.11.02.01 | SLC36A2; SLC6A20; SLC6A19-related Iminoglycinuria | SLC36A2; SLC6A20; SLC6A19 | 242600 | - | UNMAPPED |
| [ ] | 521 | 1.11.03.01 | SLC1A3-related Glutamate aspartate transporter deficiency | SLC1A3 | 612656 | 209967 | CANDIDATE -> Episodic Ataxia Type 2 (0.955) |
| [ ] | 798 | 1.11.03.02 | SLC36A2-related Hyperglycinuria | SLC36A2 | 138500;242600 | 42062 | UNMAPPED |
| [ ] | 48 | 1.11.04.01 | SLC3A1-related Cystinuria type A | SLC3A1 | 220100 | - | MAPPED -> Cystinuria (identifier:OMIM:220100) |
| [ ] | 820 | 1.11.04.02 | SLC1A2-related Astroglial glutamate aspartate transporter deficiency | SLC1A2 | 617105 | 442835 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 1250 | 1.11.05.01 | SLC7A9-related Cystinuria type B | SLC7A9 | 220100 | 93613 | MAPPED -> Cystinuria (identifier:OMIM:220100) |
| [ ] | 51 | 1.11.06.01 | SLC7A7-related Lysinuric protein intolerance | SLC7A7 | 222700 | - | UNMAPPED; weak candidate Hartnup Disease (0.667) |
| [ ] | 49 | 1.11.07.01 | SLC1A1-related Dicarboxylic aminoaciduria | SLC1A1 | 222730 | - | UNMAPPED |
| [ ] | 812 | 1.11.07.02 | SLC6A1-related GABA transporter deficiency | SLC6A1 | 616421 | 1942 | AMBIGUOUS: 2 local entities (identifier:ORPHA:1942) |
| [ ] | 799 | 1.11.08.01 | SLC7A5-related Large neutral amino acid transporter deficiency | SLC7A5 | 600182 | - | UNMAPPED; weak candidate Infantile Parkinsonism-Dystonia (0.684) |
| [ ] | 800 | 1.11.09.01 | SLC38A8-related Neuronal system A amino acid transporter deficiency | SLC38A8 | 609218 | 397618 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.644) |
| [ ] | 1338 | 1.11.11.01 | SLC7A14-related Lysosomal cationic amino acid transporter deficiency | SLC7A14 | 615725 | - | CANDIDATE -> Retinitis pigmentosa 7 (0.933) |
| [ ] | 1159 | 1.11.12.01 | SLC7A2-related Cationic amino acid transporter 2 deficiency | SLC7A2 | 601872 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.737) |
| [ ] | 1354 | 1.11.13.01 | SLC7A3-related Cationic amino acid transporter 3 deficiency | SLC7A3 | 300443 | - | UNMAPPED; weak candidate Infantile Parkinsonism-Dystonia (0.737) |
| [ ] | 1697 | 1.11.13.01 | SLC6A6-related Taurine transporter deficiency | SLC6A6 | 186854 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.871) |
| [ ] | 1698 | 1.11.14.01 | NOGENE-related Blue diaper syndrome | - | 211000 | - | UNMAPPED; weak candidate Sea-Blue Histiocyte Syndrome (0.667) |
| [ ] | 1699 | 1.11.15.01 | NOGENE-related Histidinuria | - | 235830 | - | UNMAPPED |
| [ ] | 2033 | 1.11.16.01 | SLC38A3-related Developmental and epileptic encephalopathy 102 | SLC38A3 | 619881 | - | CANDIDATE -> CN-Related Developmental and Epileptic Encephalopathy (0.967) |

### WP-005: Other disorders of amino acid metabolism

- Classification: Intermediary Metabolism: Nutrients -> Disorders of amino acid metabolism
- Subgroup scope: Other disorders of amino acid metabolism
- Records: 1 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 0)
- Work: review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 801 | 1.12.02.01 | ACY1-related Aminoacylase 1 deficiency | ACY1 | 609924 | 137754 | CANDIDATE -> Canavan disease (0.960) |

### WP-006: Disorders of glutathione metabolism + 3 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of peptide and amine metabolism
- Subgroup scope: Disorders of glutathione metabolism; Other disorders of peptide metabolism; Disorders of methylamine metabolism; Disorders of polyamine metabolism
- Records: 24 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 20)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 216 | 2.1.01.01 | GCLC-related Gamma-glutamylcysteine synthetase deficiency | GCLC | 230450 | - | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.667) |
| [ ] | 217 | 2.1.02.01 | GSS-related Glutathione synthetase deficiency, mild | GSS | 266130 | - | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.778) |
| [ ] | 512 | 2.1.02.02 | GSS-related Glutathione synthetase deficiency, severe | GSS | 266130 | 32 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.778) |
| [ ] | 214 | 2.1.03.01 | GGT1-related Gamma-glutamyl transpeptidase deficiency | GGT1 | 231950 | 33573 | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.765) |
| [ ] | 215 | 2.1.04.01 | OPLAH-related 5-Oxoprolinase deficiency | OPLAH | 260005 | 33572 | MAPPED -> 5-Oxoprolinase Deficiency (identifier:ORPHA:33572) |
| [ ] | 795 | 2.1.05.01 | GSR-related Glutathione reductase deficiency | GSR | 138300 | 90030 | UNMAPPED; weak candidate Cortisone Reductase Deficiency (0.839) |
| [ ] | 796 | 2.1.06.01 | GPX4-related Glutathione peroxidase 4 deficiency | GPX4 | 250220 | 93317 | MAPPED -> Multisystemic smooth muscle dysfunction syndrome (alias_exact:smds) |
| [ ] | 797 | 2.1.07.01 | NFE2L2-related NRF2 superactivity | NFE2L2 | 617744 | - | UNMAPPED |
| [ ] | 139 | 2.1.09.01 | DPEP1-related Dipeptidase deficiency | DPEP1 | 179780 | - | UNMAPPED |
| [ ] | 52 | 2.2.08.01 | PEPD-related Prolidase deficiency | PEPD | 170100;613230 | - | UNMAPPED |
| [ ] | 810 | 2.2.09.01 | XPNPEP3-related X-Prolyl aminopeptidase 3 deficiency | XPNPEP3 | 613159 | 93589 | UNMAPPED; weak candidate NPHP1-related (0.719) |
| [ ] | 53 | 2.2.16.01 | CNDP1-related Carnosine dipeptidase 1 deficiency | CNDP1 | 212200 | - | UNMAPPED |
| [ ] | 211 | 2.3.01.01 | DMGDH-related Dimethylglycine dehydrogenase deficiency | DMGDH | 605849 | 243343 | MAPPED -> Dimethylglycine Dehydrogenase Deficiency (identifier:ORPHA:243343) |
| [ ] | 170 | 2.3.02.01 | SARDH-related Sarcosine dehydrogenase deficiency | SARDH | 268900 | 3129 | UNMAPPED; weak candidate Isovaleric Acidemia (0.822) |
| [ ] | 210 | 2.3.03.01 | FMO3-related Flavin-containing monooxygenase 3 deficiency | FMO3 | 602079 | 468726 | UNMAPPED; weak candidate Primary erythromelalgia (0.667) |
| [ ] | 2137 | 2.3.04.01 | SLC44A1-related Neurodegeneration, childhood-onset, with ataxia, tremor, optic atrophy, and cognitive decline | SLC44A1 | 618868 | - | UNMAPPED; weak candidate Bosch-Boonstra-Schaaf Optic Atrophy Syndrome (0.439) |
| [ ] | 2183 | 2.3.05.01 | FLVCR1-related Severe developmental disorder spectrum | FLVCR1 | 621060 | - | UNMAPPED; weak candidate MED13 (0.686) |
| [ ] | 2182 | 2.3.06.01 | FLVCR2-related Proliferative vasculopathy and hydranencephaly-hydrocephaly | FLVCR2 | 225790 | - | UNMAPPED; weak candidate Proliferative Diabetic Retinopathy (0.515) |
| [ ] | 1402 | 2.4.08.01 | MTAP-related Methylthioadenosine phosphorylase deficiency | MTAP | 156540 | 85182 | UNMAPPED; weak candidate Mitochondrial Neurogastrointestinal Encephalomyopathy (0.846) |
| [ ] | 584 | 2.4.11.01 | SMS-related Spermine synthase deficiency | SMS | 309583;300105 | 477817 | UNMAPPED; weak candidate GM3 synthase deficiency (0.824) |
| [ ] | 1300 | 2.4.12.01 | SAT1-related Spermidine-spermine N(1)-acetyltransferase overactivity | SAT1 | 313020 | 2340 | MAPPED -> Keratosis follicularis spinulosa decalvans (identifier:ORPHA:2340) |
| [ ] | 1332 | 2.4.13.01 | ODC1-related Ornithine decarboxylase 1 superactivity | ODC1 | 165640 | 544488 | UNMAPPED; weak candidate Ornithine Carbamoyltransferase Deficiency (0.632) |
| [ ] | 1754 | 2.4.14.01 | NOGENE-related Diaminopentanuria | - | 222350 | - | UNMAPPED; weak candidate Cystinuria (0.696) |
| [ ] | 1774 | 2.4.15.01 | ATP13A3-related ATPase deficiency | ATP13A3 | 610232 | - | UNMAPPED |

### WP-007: Disorders of galactose and fructose metabolism + 2 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of carbohydrate metabolism
- Subgroup scope: Disorders of galactose and fructose metabolism; Disorders of gluconeogenesis; Disorders of glycolysis
- Records: 33 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 26)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 476 | 3.1.01.01 | KHK-related Hepatic fructokinase deficiency | KHK | 229800 | 2056 | UNMAPPED; weak candidate Essential Thrombocythemia (0.652) |
| [ ] | 473 | 3.1.01.02 | GALT-related Galactose-1-phosphate uridyltransferase deficiency (CDG) | GALT | 230400 | 79239 | MAPPED -> Classic Galactosemia (alias_exact:classic galactosemia) |
| [ ] | 565 | 3.1.02.01 | GLYCTK-related D-glycerate kinase deficiency | GLYCTK | 610516 | 941 | UNMAPPED; weak candidate Mevalonate Kinase Deficiency (0.772) |
| [ ] | 475 | 3.1.02.02 | GALE-related Galactose epimerase deficiency (CDG) | GALE | 230350 | 308487;308473 | UNMAPPED; weak candidate Galactosemia (0.774) |
| [ ] | 477 | 3.1.02.03 | ALDOB-related Aldolase B deficiency (CDG) | ALDOB | 229600 | 469 | MAPPED -> Hereditary Fructose Intolerance (identifier:ORPHA:469) |
| [ ] | 474 | 3.1.03.01 | GALK1-related Galactokinase deficiency (CDG) | GALK1 | 230200 | 79237 | UNMAPPED; weak candidate Galactosemia (0.774) |
| [ ] | 1362 | 3.1.04.01 | GALM-related Galactose mutarotase deficiency (CDG) | GALM | 137030 | 570422 | UNMAPPED; weak candidate Epimerase Deficiency (0.800) |
| [ ] | 1180 | 3.1.07.01 | SORD-related Sorbitol dehydrogenase deficiency | SORD | 182500 | - | UNMAPPED |
| [ ] | 1700 | 3.1.08.01 | TKFC-related Triokinase/FMN cyclase deficiency | TKFC | 618805 | - | UNMAPPED |
| [ ] | 542 | 3.2.01.01 | GKD-related Glycerol kinase deficiency, isolated | GK | 307030 | 408 | UNMAPPED; weak candidate BCKDK Deficiency (0.667) |
| [ ] | 483 | 3.2.02.01 | FBP1-related Fructose-1,6-bisphosphatase deficiency | FBP1 | 229700 | 348 | UNMAPPED; weak candidate Hereditary Fructose Intolerance (0.439) |
| [ ] | 218 | 3.2.03.01 | PC-related Pyruvate carboxylase deficiency | PC | 266150 | - | UNMAPPED; weak candidate Pyruvate Carboxylase Deficiency Disease (0.886) |
| [ ] | 910 | 3.2.04.01 | PCK1-related Cytosolic phosphoenolpyruvate carboxykinase deficiency | PCK1 | 261680 | 2880 | UNMAPPED; weak candidate Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism (0.397) |
| [ ] | 2032 | 3.2.05.01 | FBP2-related Leukodystrophy, childhood-onset, remitting | FBP2 | 619864 | - | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.602) |
| [ ] | 1183 | 3.2.9.01 | PCK2-related Mitochondrial phosphoenolpyruvate carboxykinase deficiency | PCK2 | 261650 | 2880 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.687) |
| [ ] | 502 | 3.3.1.01 | PGK1-related Phosphoglycerate kinase deficiency | PGK1 | 300653 | 713 | UNMAPPED; weak candidate Glycogen Storage Disease Type VII (0.742) |
| [ ] | 911 | 3.3.01.01 | HK1-related Hemolytic anemia due to hexokinase 1 deficiency | HK1 | 235700 | 99953 | UNMAPPED |
| [ ] | 912 | 3.3.02.01 | HK1-related Hereditary motor and sensory neuropathy, Russe type | HK1 | 605285 | 99953 | UNMAPPED |
| [ ] | 913 | 3.3.03.01 | HK1-related Retinitis pigmentosa type 79 | HK1 | 617460 | 99953 | UNMAPPED |
| [ ] | 1289 | 3.3.04.01 | GCK-related Glucokinase deficiency | GCK | 602485 | 99885 | UNMAPPED; weak candidate Diabetes mellitus (0.523) |
| [ ] | 568 | 3.3.05.01 | GCK-related Glucokinase superactivity | GCK | 602485 | 99885 | UNMAPPED |
| [ ] | 914 | 3.3.06.01 | GPI-related Glucose-6-phosphate isomerase deficiency | GPI | 615802 | 712 | UNMAPPED; weak candidate Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (0.857) |
| [ ] | 491 | 3.3.07.01 | PFKM-related Muscle phosphofructokinase deficiency | PFKM | 232800 | 371 | MAPPED -> Glycogen Storage Disease Type VII (identifier:OMIM:232800) |
| [ ] | 500 | 3.3.08.01 | ALDOA-related Aldolase A deficiency | ALDOA | 611881 | 57 | CANDIDATE -> Glycogen Storage Disease Type I (0.984) |
| [ ] | 653 | 3.3.09.01 | TPI1-related Triosephosphate isomerase deficiency | TPI1 | 615512 | 868 | UNMAPPED; weak candidate Hereditary intrinsic factor deficiency (0.596) |
| [ ] | 493 | 3.3.11.01 | PGAM2-related Muscle phosphoglycerate mutase deficiency | PGAM2 | 261670 | 97234 | CANDIDATE -> Glycogen Storage Disease Type I (0.984) |
| [ ] | 501 | 3.3.12.01 | ENO3-related Enolase beta deficiency | ENO3 | 612932 | 99849 | CANDIDATE -> Glycogen Storage Disease Type I (0.984) |
| [ ] | 915 | 3.3.13.01 | PKLR-related Pyruvate kinase deficiency | PKLR | 266200 | 766 | UNMAPPED; weak candidate Mevalonate Kinase Deficiency (0.815) |
| [ ] | 499 | 3.3.14.01 | LDHA-related Lactate dehydrogenase A deficiency | LDHA | 612933 | 2088 | CANDIDATE -> Glycogen Storage Disease Type I (0.984) |
| [ ] | 916 | 3.3.15.01 | LDHB-related Lactate dehydrogenase B deficiency | LDHB | 614128 | 284435 | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.836) |
| [ ] | 1392 | 3.3.16.01 | LDHD-related D-lactate dehydrogenase deficiency | LDHD | 245450 | - | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.852) |
| [ ] | 1752 | 3.3.17.01 | BPGM- related Bisphosphoglycerate mutase deficiency | BPGM | 222800 | - | UNMAPPED; weak candidate Methylmalonic Acidemia (0.494) |
| [ ] | 2004 | 3.3.18.01 | HK1-related Neurodevelopmental disorder with visual defects and brain anomalies | HK1 | 618547 | 99953 | UNMAPPED |

### WP-008: Disorders of glycogen metabolism + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of carbohydrate metabolism
- Subgroup scope: Disorders of glycogen metabolism; Disorders of pentose phosphate metabolism
- Records: 27 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 10, UNMAPPED 12)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 492 | 3.4.1.01 | PHKA2-related Hepatic phosphorylase kinase α2 subunit deficiency | PHKA2 | 306000 | 264580 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 496 | 3.4.01.01 | GYG1-related Muscle glycogenin 1 deficiency | GYG1 | 613507 | 263297 | CANDIDATE -> Glycogen Storage Disease XV (0.918) |
| [ ] | 484 | 3.4.01.02 | G6PC-related Glucose-6-phosphatase deficiency | G6PC | 232200 | 364 | MAPPED -> GSD Ia (glucose-6-phosphatase deficiency) (alias_exact:gsd ia) |
| [ ] | 498 | 3.4.02.01 | GYS1-related Muscle glycogen synthase deficiency | GYS1 | 611556 | 137625 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 497 | 3.4.03.01 | GYS2-related Hepatic glycogen synthase deficiency | GYS2 | 240600 | 2089 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 485 | 3.4.04.01 | SLC37A4-related Glucose-6-phosphate transporter deficiency (CDG) | SLC37A4 | 232220 | 79259 | CANDIDATE -> Glycogen Storage Disease Type I (0.984) |
| [ ] | 487 | 3.4.06.01 | AGL-related Amylo-1,6-glucosidase (debrancher) deficiency | AGL | 232400 | 366 | UNMAPPED; weak candidate Cori Forbes Disease (0.847) |
| [ ] | 488 | 3.4.07.01 | GBE1-related Glycogen branching enzyme deficiency | GBE1 | 232500 | 308621 | MAPPED -> Glycogen Storage Disease Type IV (alias_exact:glycogen branching enzyme deficiency) |
| [ ] | 489 | 3.4.08.01 | PYGM-related Muscle glycogen phosphorylase deficiency | PYGM | 232600 | 368 | CANDIDATE -> Glycogen Storage Disease Type I (0.968) |
| [ ] | 490 | 3.4.09.01 | PYGL-related Liver glycogen phosphorylase deficiency | PYGL | 232700 | 369 | CANDIDATE -> Glycogen Storage Disease Type I (0.968) |
| [ ] | 1258 | 3.4.11.01 | PHKB-related Phosphorylase kinase β subunit deficiency | PHKB | 261750 | 79240 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 1259 | 3.4.12.01 | PHKG2-related Hepatic phosphorylase kinase γ2 subunit deficiency | PHKG2 | 613027 | 264580 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 563 | 3.4.13.01 | PHKA1-related Muscle phosphorylase kinase deficiency | PHKA1 | 300559 | 715 | CANDIDATE -> Glycogen Storage Disease Type I (0.952) |
| [ ] | 907 | 3.4.14.01 | RBCK1-related HOIL1 deficiency | RBCK1 | 615895 | 397937 | UNMAPPED; weak candidate Glycogen Storage Disease XV (0.885) |
| [ ] | 564 | 3.4.15.01 | PRKAG2-related Phosphorylase kinase deficiency, AMP-activated | PRKAG2 | 600858;261740;194200 | 439854 | UNMAPPED; weak candidate Mitochondrial Neurogastrointestinal Encephalomyopathy (0.608) |
| [ ] | 908 | 3.4.17.01 | EPM2A-related Laforin deficiency | EPM2A | 254780 | 501 | AMBIGUOUS: 4 local entities (alias_exact:lafora disease) |
| [ ] | 909 | 3.4.18.01 | NHLRC1-related Malin deficiency | NHLRC1 | 254780 | 501 | UNMAPPED; weak candidate Progressive Myoclonus Epilepsy (0.882) |
| [ ] | 1182 | 3.4.19.01 | RNF31-related HOIL1 interacting protein deficiency | RNF31 | 612487 | 329173 | UNMAPPED; weak candidate E3-binding protein deficiency (0.769) |
| [ ] | 1701 | 3.4.20.01 | GYG2-related Liver glycogenin 2 deficiency | GYG2 | 300198 | - | UNMAPPED; weak candidate PCLD2 (0.439) |
| [ ] | 892 | 3.5.01.01 | G6PD-related Glucose-6-phosphate dehydrogenase deficiency | G6PD | 300908 | 466026 | MAPPED -> Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (alias_exact:glucose 6 phosphate dehydrogenase deficiency) |
| [ ] | 190 | 3.5.02.01 | RPIA-related Ribose-5-phosphate isomerase deficiency | RPIA | 608611 | 440706 | UNMAPPED; weak candidate Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (0.747) |
| [ ] | 189 | 3.5.03.01 | TALDO1-related Transaldolase deficiency | TALDO1 | 606003 | 101028 | MAPPED -> Transaldolase Deficiency (identifier:OMIM:606003) |
| [ ] | 893 | 3.5.04.01 | TKT-related Transketolase deficiency | TKT | 617044 | 488618 | UNMAPPED; weak candidate CN-Related Developmental and Epileptic Encephalopathy (0.504) |
| [ ] | 894 | 3.5.05.01 | SHPK-related Sedoheptulose kinase deficiency | SHPK | 617213 | 440713 | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.759) |
| [ ] | 895 | 3.5.06.01 | DCXR-related L-Xylulose reductase deficiency | DCXR | 260800 | 2843 | UNMAPPED; weak candidate Dimethylglycine Dehydrogenase Deficiency (0.833) |
| [ ] | 1368 | 3.5.08.01 | NOGENE-related L-Arabinosuria | - | - | - | UNMAPPED |
| [ ] | 1349 | 3.5.14.01 | NOGENE-related β-xylosidase deficiency | - | 278900 | - | UNMAPPED; weak candidate Sly syndrome (0.836) |

### WP-009: Disorders of carbohydrate transmembrane transport and absorption + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of carbohydrate metabolism
- Subgroup scope: Disorders of carbohydrate transmembrane transport and absorption; Other disorders of carbohydrate metabolism
- Records: 12 (MAPPED 1, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 9)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 480 | 3.6.01.01 | SLC2A1-related Glucose transporter 1 deficiency | SLC2A1 | 606777;612126;601042;614847 | 98811 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.853) |
| [ ] | 267 | 3.6.02.01 | SLC17A5-related Sialin deficiency (severe) | SLC17A5 | 269920 | 309334 | AMBIGUOUS: 2 local entities (alias_exact:salla disease) |
| [ ] | 667 | 3.6.02.02 | SLC45A1-related Neuronal glucose transporter deficiency | SLC45A1 | 617532 | 88616 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.800) |
| [ ] | 1369 | 3.6.02.03 | SLC17A5-related Sialin deficiency (milder) | SLC17A5 | 604369 | 309334 | AMBIGUOUS: 2 local entities (alias_exact:salla disease) |
| [ ] | 481 | 3.6.03.01 | SLC2A2-related Glucose transporter 2 deficiency | SLC2A2 | 227810 | 2088 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.853) |
| [ ] | 482 | 3.6.04.01 | SLC5A1-related Intestinal sodium-glucose cotransporter 1 deficiency | SLC5A1 | 606824 | 35710 | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.653) |
| [ ] | 668 | 3.6.05.01 | SI-related Sucrase-isomaltase deficiency | SI | 222900 | 306486 | MAPPED -> Congenital Sucrase-Isomaltase Deficiency (alias_exact:csid) |
| [ ] | 669 | 3.6.06.01 | TREH-related Trehalase deficiency | TREH | 612119 | 103909 | UNMAPPED; weak candidate Galactosemia (0.810) |
| [ ] | 891 | 3.6.07.01 | LCT-related Lactase deficiency | LCT | 223000 | 53690 | UNMAPPED |
| [ ] | 479 | 3.6.08.01 | SLC5A2-related Sodium-glucose cotransporter 2 deficiency | SLC5A2 | 233100 | 69076 | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.778) |
| [ ] | 1179 | 3.6.09.01 | MAP17-related Familial renal glucosuria | PDZK1IP1 | 607178 | - | UNMAPPED; weak candidate Unilateral (0.593) |
| [ ] | 1751 | 3.7.01.01 | PGM2L1-related Phosphoglucomutase 2-like 1 deficiency | PGM2L1 | 611610 | - | UNMAPPED; weak candidate GDF2-related HHT-like disease (0.561) |

### WP-010: Disorders of carnitine metabolism  + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Nutrients -> Disorders of fatty acid and ketone body metabolism
- Subgroup scope: Disorders of carnitine metabolism ; Disorders of mitochondrial fatty acid oxidation
- Records: 21 (MAPPED 6, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 9)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 9 | 4.1.01.01 | SLC22A5-related Primary carnitine deficiency | SLC22A5 | 212140 | - | MAPPED -> Primary Carnitine Deficiency (alias_exact:primary carnitine deficiency) |
| [ ] | 228 | 4.1.02.01 | CPT1A-related Carnitine palmitoyltransferase 1A deficiency | CPT1A | 255120 | - | CANDIDATE -> Carnitine Palmitoyltransferase II Deficiency (0.955) |
| [ ] | 230 | 4.1.03.01 | CPT2-related Carnitine palmitoyltransferase 2 deficiency | CPT2 | 255110 | - | CANDIDATE -> Carnitine Palmitoyltransferase II Deficiency (0.989) |
| [ ] | 229 | 4.1.04.01 | SLC25A20-related Carnitine acylcarnitine translocase deficiency | SLC25A20 | 212138 | 159 | MAPPED -> Carnitine-acylcarnitine Translocase Deficiency (alias_exact:carnitine acylcarnitine translocase deficiency) |
| [ ] | 1041 | 4.1.05.01 | TMLHE-related ε-N-trimethyllysine hydroxylase deficiency | TMLHE | 300872 | - | UNMAPPED; weak candidate Autosomal Recessive Dopa-Responsive Dystonia (0.817) |
| [ ] | 1202 | 4.1.06.01 | BBOX1-r elated Gamma-Butyrobetaine hydroxylase deficiency | BBOX1 | 603312 | - | UNMAPPED; weak candidate Autosomal Recessive Dopa-Responsive Dystonia (0.682) |
| [ ] | 673 | 4.1.07.01 | CPT1C-related Carnitine palmitoyl-transferase 1C deficiency | CPT1C | 616282 | 444099 | CANDIDATE -> Carnitine Palmitoyltransferase II Deficiency (0.966) |
| [ ] | 671 | 4.1.08.01 | CRAT-related Carnitine acetyltransferase deficiency | CRAT | 606175 | - | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.878) |
| [ ] | 235 | 4.2.01.01 | ACADS-related Short-chain acyl CoA dehydrogenase deficiency | ACADS | 201470 | 26792 | MAPPED -> Idiopathic Spontaneous Coronary Artery Dissection (alias_exact:scad) |
| [ ] | 1203 | 4.2.1.01 | ACADL-related Long-chain acyl-CoA dehydrogenase deficiency | ACADL | 609576 | 99900 | CANDIDATE -> Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (0.946) |
| [ ] | 234 | 4.2.02.01 | ACADM-related Medium-chain acyl CoA dehydrogenase deficiency | ACADM | 201450 | - | MAPPED -> Medium Chain Acyl-CoA Dehydrogenase Deficiency (alias_exact:medium chain acyl coa dehydrogenase deficiency) |
| [ ] | 231 | 4.2.03.01 | ACADVL-related Very long-chain acyl CoA dehydrogenase deficiency | ACADVL | 201475 | - | MAPPED -> Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (alias_exact:very long chain acyl coa dehydrogenase deficiency) |
| [ ] | 236 | 4.2.04.01 | HADH-related Short-chain 3-hydroxyacyl-CoA dehydrogenase deficiency | HADH | 231530 | 71212 | UNMAPPED |
| [ ] | 232 | 4.2.05.02 | HADHA-related Trifunctional protein subunit αalpha deficiency | HADHA | 609015 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.762) |
| [ ] | 237 | 4.2.06.01 | ETFA-related Electron transfer flavoprotein α subunit deficiency | ETFA | 231680 | - | CANDIDATE -> Multiple Acyl-CoA Dehydrogenase Deficiency (0.980) |
| [ ] | 233 | 4.2.06.02 | HADHB-related Isolated deficiency of long-chain 3-ketoacyl CoA thiolase | HADHB | 143450 | - | UNMAPPED |
| [ ] | 1282 | 4.2.06.03 | HADHB-related Trifunctional protein subunit β deficiency | HADHB | 609015 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.831) |
| [ ] | 1257 | 4.2.07.01 | ETFB-related Electron transfer flavoprotein β subunit deficiency | ETFB | 231680 | 394529 | CANDIDATE -> Multiple Acyl-CoA Dehydrogenase Deficiency (0.980) |
| [ ] | 239 | 4.2.08.01 | ETFDH-related Multiple acyl-CoA dehydrogenase deficiency | ETFDH | 231675 | - | MAPPED -> Multiple Acyl-CoA Dehydrogenase Deficiency (alias_exact:multiple acyl coa dehydrogenase deficiency) |
| [ ] | 532 | 4.2.08.02 | ETFDH-related Myopathic form of CoQ10 deficiency | ETFDH | 231675 | 394529 | UNMAPPED |
| [ ] | 1702 | 4.2.11.01 | NOGENE-related Medium-chain 3-ketoacyl-CoA thiolase (MCKAT) deficiency | - | 602199 | - | UNMAPPED; weak candidate Medium Chain Acyl-CoA Dehydrogenase Deficiency (0.768) |

### WP-011: Disorders of ketone body metabolism

- Classification: Intermediary Metabolism: Nutrients -> Disorders of fatty acid and ketone body metabolism
- Subgroup scope: Disorders of ketone body metabolism
- Records: 7 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 4)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 176 | 4.3.01.01 | HMGCS2-related 3-Hydroxy-3-methylglutaryl-CoA synthase deficiency | HMGCS2 | 605911 | 35701 | MAPPED -> 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (identifier:OMIM:605911) |
| [ ] | 175 | 4.3.02.01 | OXCT1-related Succinyl-CoA:3-oxoacid CoA transferase deficiency | OXCT1 | 245050 | 832 | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.650) |
| [ ] | 619 | 4.3.04.01 | SLC16A1-related Monocarboxylate transporter-1 deficiency | SLC16A1 | 616095 | 438075 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.778) |
| [ ] | 571 | 4.3.05.01 | SLC16A1-related Monocarboxylate transporter 1 superactivity | SLC16A1 | 610021 | 438075 | UNMAPPED; weak candidate PRPS1 Superactivity (0.611) |
| [ ] | 270 | 4.3.9.01 | ACAT2-related Acetoacetyl-CoA thiolase deficiency (cytosolic) | ACAT2 | 100678 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.776) |
| [ ] | 269 | 4.3.13.01 | ACAT1-related Mitochondrial acetoacetyl-CoA thiolase deficiency | ACAT1 | 203750 | 134 | MAPPED -> Beta-Ketothiolase Deficiency (alias_exact:mitochondrial acetoacetyl coa thiolase deficiency) |
| [ ] | 62 | 4.3.16.01 | HMGCL-related 3-Hydroxy-3-methylglutaryl-CoA lyase deficiency | HMGCL | 246450 | - | MAPPED -> 3-Hydroxy-3-Methylglutaric Aciduria (alias_exact:hmgcld) |

### WP-012: Disorders of pyruvate metabolism + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> Disorders of energy substrate metabolism
- Subgroup scope: Disorders of pyruvate metabolism; Disorders of the Krebs cycle
- Records: 28 (MAPPED 10, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 14)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 220 | 5.1.01.01 | PDHA1-related Pyruvate dehydrogenase E1 alpha deficiency | PDHA1 | 312170 | - | MAPPED -> Pyruvate Dehydrogenase Deficiency (alias_exact:pdh) |
| [ ] | 221 | 5.1.02.01 | PDHB-related Pyruvate dehydrogenase E1 beta deficiency | PDHB | 179060 | - | MAPPED -> Pyruvate Dehydrogenase Deficiency (alias_exact:pdh) |
| [ ] | 222 | 5.1.03.01 | DLAT-related Dihydrolipoyl transacetylase deficiency | DLAT | 245348 | - | MAPPED -> E2 deficiency (alias_exact:pyruvate dehydrogenase e2 deficiency) |
| [ ] | 224 | 5.1.04.01 | PDHX-related Pyruvate dehydrogenase E3-binding protein deficiency | PDHX | 245349 | - | MAPPED -> E3-binding protein deficiency (alias_exact:pyruvate dehydrogenase e3 binding protein deficiency) |
| [ ] | 223 | 5.1.05.01 | DLD-related Dihydrolipoyl dehydrogenase deficiency | DLD | 248600 | - | MAPPED -> E3 deficiency (alias_exact:pyruvate dehydrogenase e3 deficiency) |
| [ ] | 225 | 5.1.05.02 | PDP1-related Pyruvate dehydrogenase phosphatase deficiency | PDP1 | 608782 | - | MAPPED -> PDH phosphatase deficiency (alias_exact:pyruvate dehydrogenase phosphatase deficiency) |
| [ ] | 917 | 5.1.06.01 | MPC1-related Mitochondrial pyruvate carrier deficiency | MPC1 | 614741 | 447784 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.707) |
| [ ] | 918 | 5.1.07.01 | PDK3-related Pyruvate dehydrogenase kinase isoenzyme 3 superactivity | PDK3 | 300905 | 352675 | UNMAPPED; weak candidate CMTX5 (0.871) |
| [ ] | 2030 | 5.1.08.01 | PDHA2-related Pyruvate dehydrogenase, alpha-2 deficiency | PDHA2 | 619828 | - | CANDIDATE -> E1-alpha deficiency (0.940) |
| [ ] | 1703 | 5.1.14.01 | PDPR-related Pyruvate dehydrogenase phosphatase regulatory subunit deficiency | PDPR | 617835 | - | UNMAPPED; weak candidate PDH phosphatase deficiency (0.826) |
| [ ] | 919 | 5.2.01.01 | ACO2-related Mitochondrial aconitase deficiency | ACO2 | 614559 | 313850 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.853) |
| [ ] | 167 | 5.2.02.01 | IDH2-related Mitochondrial NADP+-dependent isocitrate dehydrogenase 2 superactivity | IDH2 | 613657 | 79315 | MAPPED -> D-2-Hydroxyglutaric Aciduria (identifier:ORPHA:79315) |
| [ ] | 920 | 5.2.03.01 | IDH3B-related Mitochondrial NADPH-dependent isocitrate dehydrogenase 3 betta subunit deficiency | IDH3B | 612572 | 791 | MAPPED -> EYS-Related Retinitis Pigmentosa (identifier:ORPHA:791) |
| [ ] | 503 | 5.2.04.01 | SUCLA2-related ATP-specific succinyl-CoA synthetase ligase betta subunit deficiency | SUCLA2 | 612073 | 1933 | CANDIDATE -> Mitochondrial DNA Depletion Syndrome 7 (0.914) |
| [ ] | 574 | 5.2.05.01 | SUCLG1-related GTP-specific succinyl-CoA synthetase ligase alpha subunit deficiency | SUCLG1 | 245400 | 17 | CANDIDATE -> Mitochondrial (0.914) |
| [ ] | 174 | 5.2.06.01 | FH-related Fumarate hydratase deficiency | FH | 606812 | 24 | MAPPED -> Familial hyperaldosteronism type I (alias_exact:fh1) |
| [ ] | 1260 | 5.2.07.01 | FH-related Fumarate hydratase deficiency, tumoral phenotype | FH | 150800 | 24 | MAPPED -> Familial hyperaldosteronism type I (alias_exact:fh1) |
| [ ] | 921 | 5.2.08.01 | MDH2-related Mitochondrial malate dehydrogenase deficiency | MDH2 | 617339 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.755) |
| [ ] | 1403 | 5.2.08.02 | MDH2-related Mitochondrial malate dehydrogenase deficiency, tumoral phenotype | MDH2 | 617339 | 29072 | UNMAPPED; weak candidate COX10-Related COX Deficiency (0.655) |
| [ ] | 1317 | 5.2.09.01 | SLC13A3-related Sodium dicarboxylate cotransporter 3 deficiency | SLC13A3 | 606411 | - | UNMAPPED; weak candidate SCN1B-related (0.392) |
| [ ] | 1314 | 5.2.09.02 | SLC13A5-related Plasma membrane citrate transporter deficiency | SLC13A5 | 615905 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 1393 | 5.2.11.01 | DLST-related Dihydrolipoamide succinyltransferase deficiency | DLST | 126063 | - | UNMAPPED |
| [ ] | 1390 | 5.2.12.01 | IDH1-related Cytosolic NADP+-dependent isocitrate dehydrogenase 1 superactivity | IDH1 | 147700 | - | UNMAPPED |
| [ ] | 173 | 5.2.13.01 | OGDH-related Alpha-ketoglutarate dehydrogenase deficiency | OGDH | 203740 | 99742 | UNMAPPED; weak candidate D-2-Hydroxyglutaric Aciduria (0.840) |
| [ ] | 1704 | 5.2.14.01 | IDH3A-related Mitochondrial NAD+-dependent isocitrate dehydrogenase 3 subunit alpha deficiency | IDH3A | 619007 | - | CANDIDATE -> Retinitis pigmentosa 7 (0.933) |
| [ ] | 2016 | 5.2.15.01 | OGDHL-related Oxoglutarate dehydrogenase-like protein deficiency | OGDHL | 617513 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.765) |
| [ ] | 2181 | 5.2.15.01 | IDH3G-related Mitochondrial NAD+-depend mitochondrial isocitrate dehydrogenase 3 gamma | IDH3G | 300089 | - | UNMAPPED; weak candidate Mitochondrial Neurogastrointestinal Encephalomyopathy (0.533) |
| [ ] | 2148 | 5.2.16.01 | MRPS36-related Mitochondrial ribosomal protein S36 deficiency | KGD4 | 611996 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.826) |

### WP-013: Disorders of creatine metabolism

- Classification: Intermediary Metabolism: Energy -> Disorders of energy substrate metabolism
- Subgroup scope: Disorders of creatine metabolism
- Records: 4 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 1)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 105 | 5.3.01.01 | GATM-related Arginine:glycine amidinotransferase deficiency | GATM | 612718 | - | MAPPED -> AGAT Deficiency (alias_exact:arginine glycine amidinotransferase deficiency) |
| [ ] | 1220 | 5.3.02.01 | GATM-related Arginine:glycine amidinotransferase aggregation syndrome | GATM | 600666 | - | UNMAPPED; weak candidate Fanconi Renotubular Syndrome (0.889) |
| [ ] | 104 | 5.3.03.01 | GAMT-related Guanidinoacetate methyltransferase deficiency | GAMT | 612736 | - | MAPPED -> Guanidinoacetate Methyltransferase Deficiency (alias_exact:cerebral creatine deficiency syndrome type 2) |
| [ ] | 106 | 5.3.04.01 | SLC6A8-related Creatine transporter deficiency | SLC6A8 | 300352 | - | CANDIDATE -> AGAT Deficiency (0.977) |

### WP-014: Disorders of mtDNA-encoded oxidative phosphorylation proteins + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> mtDNA-related disorders
- Subgroup scope: Disorders of mtDNA-encoded oxidative phosphorylation proteins; Disorders of mtDNA-encoded tRNA and rRNA
- Records: 38 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 37)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 735 | 6.1.01.01 | MT-CO1-related Cytochrome c oxidase subunit 1 deficiency | MT-CO1 | 516030 | 99845 | UNMAPPED; weak candidate COX4I1-Related COX Deficiency (0.891) |
| [ ] | 744 | 6.1.01.02 | MT-CYB-related Mitochondrial cytochrome b deficiency | MT-CYB | 516020 | 1460 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.769) |
| [ ] | 707 | 6.1.2.01 | MT-ND3-related NADH dehydrogenase core subunit 3 deficiency | MT-ND3 | 252010 | 99718 | UNMAPPED; weak candidate E1-beta deficiency (0.729) |
| [ ] | 736 | 6.1.02.01 | MT-CO2-related Cytochrome c oxidase subunit 2 deficiency | MT-CO2 | 516040 | 254905 | UNMAPPED; weak candidate COX4I1-Related COX Deficiency (0.870) |
| [ ] | 737 | 6.1.03.01 | MT-CO3-related Cytochrome c oxidase subunit 3 deficiency | MT-CO3 | 516050 | 99845 | UNMAPPED; weak candidate COX4I1-Related COX Deficiency (0.870) |
| [ ] | 741 | 6.1.04.01 | MT-ATP6-related Mitochondrial ATP synthase F0 subunit 6 deficiency | MT-ATP6 | 516060 | 397750 | UNMAPPED; weak candidate Myopathy, Lactic Acidosis, and Sideroblastic Anemia (0.495) |
| [ ] | 742 | 6.1.05.01 | MT-ATP8-related Mitochondrial ATP synthase F0 subunit 8 deficiency | MT-ATP8 | 516070 | 397750 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.769) |
| [ ] | 705 | 6.1.18.01 | MT-ND1-related NADH dehydrogenase core subunit 1 deficiency | MT-ND1 | 252010 | 255210 | UNMAPPED; weak candidate E1-beta deficiency (0.729) |
| [ ] | 706 | 6.1.19.01 | MT-ND2-related NADH dehydrogenase core subunit 2 deficiency | MT-ND2 | 252010 | 255210 | UNMAPPED; weak candidate E1-beta deficiency (0.729) |
| [ ] | 708 | 6.1.21.01 | MT-ND4-relatedNADH dehydrogenase core subunit 4 deficiency | MT-ND4 | 252010 | 99718 | UNMAPPED; weak candidate E1-beta deficiency (0.687) |
| [ ] | 709 | 6.1.22.01 | MT-ND4L-related NADH dehydrogenase core subunit 4L deficiency | MT-ND4L | 252010 | 104 | UNMAPPED; weak candidate E1-beta deficiency (0.721) |
| [ ] | 710 | 6.1.23.01 | MT-ND5-related NADH dehydrogenase core subunit 5 deficiency | MT-ND5 | 252010 | 255210 | UNMAPPED |
| [ ] | 711 | 6.1.24.01 | MT-ND6-related NADH dehydrogenase core subunit 6 deficiency | MT-ND6 | 252010 | 99718 | UNMAPPED; weak candidate E1-beta deficiency (0.729) |
| [ ] | 966 | 6.2.01.01 | MT-TA-related Mitochondrial tRNA(Ala) deficiency | MT-TA | 590000 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.759) |
| [ ] | 975 | 6.2.1.01 | MT-TI-related Mitochondrial tRNA(Ile) deficiency | MT-TI | 590045 | - | UNMAPPED |
| [ ] | 967 | 6.2.02.01 | MT-TR-related Mitochondrial tRNA(Arg) deficiency | MT-TR | 590005 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 985 | 6.2.2.01 | MT-TW-related Mitochondrial tRNA(Trp) deficiency | MT-TW | 590095 | 255210 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 968 | 6.2.03.01 | MT-TN-related Mitochondrial tRNA(Asn) deficiency | MT-TN | 590010 | 663 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 969 | 6.2.04.01 | MT-TD-related Mitochondrial tRNA(Asp) deficiency | MT-TD | 590015 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 970 | 6.2.05.01 | MT-TC-related Mitochondrial tRNA(Cys) deficiency | MT-TC | 590020 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.784) |
| [ ] | 408 | 6.2.06.01 | MT-TE-related Mitochondrial tRNA(Glu) deficiency | MT-TE | 500009 | 254864 | UNMAPPED; weak candidate Reversible Infantile Cytochrome c Oxidase Deficiency (0.689) |
| [ ] | 471 | 6.2.07.01 | MT-RNR1-related Mitochondrial ribosomal RNA 12S deficiency | MT-RNR1 | 580000 | 90641 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.750) |
| [ ] | 972 | 6.2.07.02 | MT-TQ-related Mitochondrial tRNA(Gln) deficiency | MT-TQ | 590030 | 551 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 963 | 6.2.08.01 | MT-RNR2-related Mitochondrial ribosomal RNA 16S deficiency | MT-RNR2 | 561010 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.750) |
| [ ] | 973 | 6.2.08.02 | MT-TG-related Mitochondrial tRNA(Gly) deficiency | MT-TG | 590035 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.759) |
| [ ] | 974 | 6.2.09.01 | MT-TH-related Mitochondrial tRNA(His) deficiency | MT-TH | 590040 | 90641 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 976 | 6.2.11.01 | MT-TL1-related Mitochondrial tRNA(Leu) 1 deficiency | MT-TL1 | 590050 | 225 | UNMAPPED |
| [ ] | 977 | 6.2.12.01 | MT-TL2-related Mitochondrial tRNA(Leu) 2 deficiency | MT-TL2 | 590055 | 663 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.765) |
| [ ] | 978 | 6.2.13.01 | MT-TK-related Mitochondrial tRNA(Lys) deficiency | MT-TK | 590060 | 225 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.784) |
| [ ] | 979 | 6.2.14.01 | MT-TM-related Mitochondrial tRNA(Met) deficiency | MT-TM | 590065 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 980 | 6.2.15.01 | MT-TF-related Mitochondrial tRNA(Phe) deficiency | MT-TF | 590070 | 551 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.810) |
| [ ] | 982 | 6.2.17.01 | MT-TS1-related Mitochondrial tRNA(Ser) 1 deficiency | MT-TS1 | 590080 | 90641 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.765) |
| [ ] | 983 | 6.2.18.01 | MT-TS2-related Mitochondrial tRNA(Ser) 2 deficiency | MT-TS2 | 590085 | 231183 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.765) |
| [ ] | 406 | 6.2.19.01 | MT-TT-related Mitochondrial tRNA(Thr) deficiency | MT-TT | 551000 | 254857 | UNMAPPED; weak candidate Reversible Infantile Cytochrome c Oxidase Deficiency (0.872) |
| [ ] | 986 | 6.2.21.01 | MT-TY-related Mitochondrial tRNA(Tyr) deficiency | MT-TY | 590100 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.785) |
| [ ] | 987 | 6.2.22.01 | MT-TV-related Mitochondrial tRNA(Val) deficiency | MT-TV | 590105 | 255210 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.759) |
| [ ] | 407 | 6.2.23.01 | MT-TE-related Mitochondrial Myopathy with Diabetes Mellitus | MT-TE | 500002 | 2596 | UNMAPPED; weak candidate Reversible Infantile Cytochrome c Oxidase Deficiency (0.524) |
| [ ] | 981 | 6.2.24.01 | MT-TP-related Mitochondrial tRNA(Pro) deficiency | MT-TP | 590075 | 14 | MAPPED -> Abetalipoproteinemia (identifier:ORPHA:14) |

### WP-015: Disorders associated with single large-scale mtDNA deletions

- Classification: Intermediary Metabolism: Energy -> mtDNA-related disorders
- Subgroup scope: Disorders associated with single large-scale mtDNA deletions
- Records: 2 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 397 | 6.3.01.01 | NOGENE-related Pearson Syndrome | - | 557000 | 699 | UNMAPPED; weak candidate Pancreatic Agenesis (0.469) |
| [ ] | 398 | 6.3.02.01 | NOGENE-related Kearns Sayre Syndrome | - | 530000 | 480 | UNMAPPED |

### WP-016: Disorders of complex I subunits and assembly factors (part 1 of 2)

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex I subunits and assembly factors
- Records: 22 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 16, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 677 | 7.1.01.01 | NDUFAF1-related Complex I assembly factor 1 deficiency | NDUFAF1 | 618234 | 289527 | CANDIDATE -> COX20-Related COX Deficiency (0.990) |
| [ ] | 684 | 7.1.1.01 | TMEM126B-related Transmembrane protein 126B deficiency | TMEM126B | 618250 | 2609 | CANDIDATE -> COX11-Related COX Deficiency (0.970) |
| [ ] | 685 | 7.1.01.02 | NDUFV1-related NADH dehydrogenase flavoprotein 1 deficiency | NDUFV1 | 618225 | 255241 | UNMAPPED |
| [ ] | 694 | 7.1.1.02 | NDUFA1-related NADH dehydrogenase alpha subcomplex subunit 1 deficiency | NDUFA1 | 301020 | 2609 | CANDIDATE -> PET100-Related COX Deficiency (0.990) |
| [ ] | 678 | 7.1.02.01 | NDUFAF2-related Complex I assembly factor 2 deficiency | NDUFAF2 | 618233 | 255241 | CANDIDATE -> COX14-Related COX Deficiency (0.990) |
| [ ] | 686 | 7.1.02.02 | NDUFV2-related NADH dehydrogenase flavoprotein 2 deficiency | NDUFV2 | 618229 | 255241 | CANDIDATE -> COX6B1-Related COX Deficiency (0.990) |
| [ ] | 679 | 7.1.03.01 | NDUFAF3-related Complex I assembly factor 3 deficiency | NDUFAF3 | 618240 | 70474 | CANDIDATE -> COX6A2-Related COX Deficiency (0.990) |
| [ ] | 687 | 7.1.03.02 | NDUFS1-related NADH dehydrogenase iron-sulfur protein 1 deficiency | NDUFS1 | 618229 | 255241 | CANDIDATE -> COX8A-Related COX Deficiency (0.980) |
| [ ] | 680 | 7.1.04.01 | NDUFAF4-related Complex I assembly factor 4 deficiency | NDUFAF4 | 618237 | 2609 | CANDIDATE -> COX8A-Related COX Deficiency (0.990) |
| [ ] | 688 | 7.1.04.02 | NDUFS2-related NADH dehydrogenase iron-sulfur protein 2 deficiency | NDUFS2 | 618228 | 70474 | CANDIDATE -> COX4I1-Related COX Deficiency (0.980) |
| [ ] | 681 | 7.1.05.01 | NDUFAF5-related Complex I assembly factor 5 deficiency | NDUFAF5 | 618238 | 255241 | CANDIDATE -> COX4I1-Related COX Deficiency (0.990) |
| [ ] | 689 | 7.1.05.02 | NDUFS3-related NADH dehydrogenase iron-sulfur protein 3 deficiency | NDUFS3 | 256000;252010 | 255241 | CANDIDATE -> TACO1-Related COX Deficiency (0.990) |
| [ ] | 1033 | 7.1.05.03 | TMEM126A-related Transmembrane protein 126A deficiency | TMEM126A | 612989 | 227976 | UNMAPPED; weak candidate SMA Type 1 (Werdnig-Hoffmann) (0.680) |
| [ ] | 682 | 7.1.06.01 | NDUFAF6-related Complex I assembly factor 6 deficiency | NDUFAF6 | 618239 | 255241 | UNMAPPED; weak candidate FRTS5 (0.265) |
| [ ] | 692 | 7.1.06.02 | NDUFS7-related NADH dehydrogenase iron-sulfur protein 7 deficiency | NDUFS7 | 618224 | 255241 | CANDIDATE -> COX10-Related COX Deficiency (0.990) |
| [ ] | 683 | 7.1.07.01 | FOXRED1-related Mitochondrial complex I deficiency, nuclear type 19 | FOXRED1 | 618241 | 255241 | CANDIDATE -> PET117-Related COX Deficiency (0.990) |
| [ ] | 693 | 7.1.07.02 | NDUFS8-related NADH dehydrogenase iron-sulfur protein 8 deficiency | NDUFS8 | 618222 | 255241 | CANDIDATE -> COX11-Related COX Deficiency (0.980) |
| [ ] | 690 | 7.1.08.01 | NDUFS4-related NADH dehydrogenase iron-sulfur protein 4 deficiency | NDUFS4 | 252010 | 255241 | UNMAPPED |
| [ ] | 927 | 7.1.08.02 | NUBPL-related Mitochondrial complex I deficiency, nuclear type 21 deficiency | NUBPL | 618242 | 2609 | UNMAPPED; weak candidate COXFA4-Related COX Deficiency (0.893) |
| [ ] | 438 | 7.1.09.01 | ACAD9-related Acyl-CoA Dehydrogenase 9 deficiency | ACAD9 | 611126 | 99901 | UNMAPPED; weak candidate Glutaryl-CoA Dehydrogenase Deficiency (0.889) |
| [ ] | 691 | 7.1.09.02 | NDUFS6-related NADH dehydrogenase iron-sulfur protein 6 deficiency | NDUFS6 | 618232 | 2609 | CANDIDATE -> PET117-Related COX Deficiency (0.980) |
| [ ] | 695 | 7.1.11.01 | NDUFA2-related NADH dehydrogenase alpha subcomplex subunit 2 deficiency | NDUFA2 | 256000 | 85136 | CANDIDATE -> COX10-Related COX Deficiency (0.980) |

### WP-017: Disorders of complex I subunits and assembly factors (part 2 of 2)

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex I subunits and assembly factors
- Records: 20 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 12, UNMAPPED 8)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1341 | 7.1.11.02 | TIMMDC1-related Mitochondrial complex I deficiency, nuclear type | TIMMDC1 | 615534 | - | CANDIDATE -> COX10-Related COX Deficiency (0.969) |
| [ ] | 697 | 7.1.12.01 | NDUFA9-related NADH dehydrogenase alpha subcomplex subunit 9 deficiency | NDUFA9 | 256000 | 255241 | CANDIDATE -> COX11-Related COX Deficiency (0.970) |
| [ ] | 1358 | 7.1.12.02 | NDUFAF7-related Complex I assembly factor 7 deficiency | NDUFAF7 | 615898 | 2609 | UNMAPPED; weak candidate COX14-Related COX Deficiency (0.678) |
| [ ] | 698 | 7.1.13.01 | NDUFA10-related NADH dehydrogenase alpha subcomplex subunit 10 deficiency | NDUFA10 | 618243 | 255241 | CANDIDATE -> COX16-Related COX Deficiency (0.990) |
| [ ] | 700 | 7.1.14.01 | NDUFA12-related NADH dehydrogenase alpha subcomplex subunit 12 deficiency | NDUFA12 | 618244 | 255241 | CANDIDATE -> COX11-Related COX Deficiency (0.990) |
| [ ] | 702 | 7.1.15.01 | NDUFB3-related NADH dehydrogenase beta subcomplex subunit 3 deficiency | NDUFB3 | 252010 | 2609 | CANDIDATE -> COX18-Related COX Deficiency (0.980) |
| [ ] | 926 | 7.1.16.01 | NDUFB8-related NADH dehydrogenase beta subcomplex subunit 8 deficiency | NDUFB8 | 602140 | - | CANDIDATE -> COX10-Related COX Deficiency (0.980) |
| [ ] | 704 | 7.1.17.01 | NDUFB11-related NADH dehydrogenase beta subcomplex subunit 11 deficiency | NDUFB11 | 252010 | 2556 | CANDIDATE -> COX10-Related COX Deficiency (0.980) |
| [ ] | 1320 | 7.1.25.01 | NDUFA6-related NADH dehydrogenase alpha subcomplex subunit 6 deficiency | NDUFA6 | 252010 | 2609 | UNMAPPED; weak candidate COX10-Related COX Deficiency (0.810) |
| [ ] | 703 | 7.1.26.01 | NDUFB9-related NADH dehydrogenase beta subcomplex subunit 9 deficiency | NDUFB9 | 252010 | 2609 | CANDIDATE -> FASTKD5-Related COX Deficiency (0.990) |
| [ ] | 701 | 7.1.27.01 | NDUFA13-related NADH dehydrogenase alpha subcomplex subunit 13 deficiency | NDUFA13 | 618249 | 255241 | CANDIDATE -> TACO1-Related COX Deficiency (0.980) |
| [ ] | 699 | 7.1.28.01 | NDUFA11-related NADH dehydrogenase alpha subcomplex subunit 11 deficiency | NDUFA11 | 618236 | 2609 | CANDIDATE -> COA3-Related COX Deficiency (0.990) |
| [ ] | 1356 | 7.1.29.01 | NADH dehydrogenase betta subcomplex subunit 10 deficiency | NDUFB10 | 603843 | 2609 | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.694) |
| [ ] | 1705 | 7.1.30.01 | NDUFA8-related NADH dehydrogenase alpha subcomplex subunit 8 deficiency | NDUFA8 | 603359 | - | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.701) |
| [ ] | 1706 | 7.1.31.01 | NDUFC2-related NADH dehydrogenase subunit C2 deficiency | NDUFC2 | 619170 | - | CANDIDATE -> COX10-Related COX Deficiency (0.980) |
| [ ] | 1707 | 7.1.32.01 | NDUFAF8-related Complex I assembly factor 8 deficiency | NDUFAF8 | 618776 | 2609 | UNMAPPED; weak candidate COX14-Related COX Deficiency (0.678) |
| [ ] | 2059 | 7.1.32.01 | NDUFB7-related NADH dehydrogenase betta subcomplex subunit 8 deficiency | NDUFB7 | 620135 | - | CANDIDATE -> COX10-Related COX Deficiency (0.980) |
| [ ] | 2067 | 7.1.33.01 | PYURF-related  S-adenosylmethionine-dependent methyltransferase chaperone deficeincy | PYURF | 619956 | - | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.614) |
| [ ] | 1759 | 7.1.34.01 | DNAJC30-related Leber's hereditary optic neuropathy | DNAJC30 | 619382 | - | UNMAPPED; weak candidate Distal Hereditary Motor Neuronopathy, Autosomal Recessive (0.674) |
| [ ] | 2240 | 7.1.35.01 | NDUFA5-related NADH:ubiquinone oxidoreductase subunit A5 deficiency | NDUFA5 | 601677 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.628) |

### WP-018: Disorders of complex II subunits and assembly factors + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex II subunits and assembly factors; Disorders of complex III subunits and assembly factors
- Records: 22 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 10, UNMAPPED 12)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 451 | 7.2.01.01 | SDHA-related Succinate dehydrogenase subunit A deficiency | SDHA | 252011 | 44890 | UNMAPPED; weak candidate E1-beta deficiency (0.776) |
| [ ] | 1262 | 7.2.01.02 | SDHAF1-related Succinate dehydrogenase complex assembly factor 1 deficiency | SDHAF1 | 252011 | 3208 | UNMAPPED; weak candidate COX10-Related COX Deficiency (0.800) |
| [ ] | 933 | 7.2.02.01 | SDHAF2-related Succinate dehydrogenase complex assembly factor 2 deficiency, tumoral phenotype | SDHAF2 | 601650 | 29072 | UNMAPPED; weak candidate Carney-Stratakis syndrome (0.846) |
| [ ] | 1261 | 7.2.02.02 | SDHA-related Succinate dehydrogenase subunit A deficiency, tumoral phenotype | SDHA | 614165 | 44890 | UNMAPPED; weak candidate Carney-Stratakis syndrome (0.846) |
| [ ] | 928 | 7.2.03.01 | SDHB-related Succinate dehydrogenase subunit B deficiency, tumoral phenotype | SDHB | 185470 | 97286 | UNMAPPED |
| [ ] | 929 | 7.2.04.01 | SDHB-related Succinate dehydrogenase subunit B deficiency | SDHB | 619224 | 97286 | UNMAPPED |
| [ ] | 930 | 7.2.05.01 | SDHC-related Succinate dehydrogenase subunit C deficiency, tumoral phenotype | SDHC | 605373 | 97286 | UNMAPPED; weak candidate Carney-Stratakis syndrome (0.846) |
| [ ] | 931 | 7.2.06.01 | SDHD-related Succinate dehydrogenase subunit D deficiency | SDHD | 252011 | 100093 | UNMAPPED |
| [ ] | 932 | 7.2.07.01 | SDHD-related Succinate dehydrogenase subunit D deficiency, tumoral phenotype | SDHD | 168000;171300 | 100093 | UNMAPPED; weak candidate Carney-Stratakis syndrome (0.846) |
| [ ] | 716 | 7.3.01.01 | UQCRB-related Mitochondrial complex III deficiency, nuclear type 3 | UQCRB | 615158 | 1460 | CANDIDATE -> COX10-Related COX Deficiency (0.970) |
| [ ] | 208 | 7.3.01.02 | BCS1L-related GRACILE syndrome | BCS1L | 603358 | 53693 | UNMAPPED; weak candidate CALFAN Syndrome (0.492) |
| [ ] | 666 | 7.3.02.01 | UQCRC2-related Mitochondrial complex III deficiency, nuclear type 5 | UQCRC2 | 615160 | 1460 | CANDIDATE -> COX8A-Related COX Deficiency (0.961) |
| [ ] | 712 | 7.3.02.02 | TTC19-related Mitochondrial complex III deficiency, nuclear type 2 | TTC19 | 615157 | 1460 | CANDIDATE -> COX11-Related COX Deficiency (0.961) |
| [ ] | 745 | 7.3.02.03 | CYC1-related Mitochondrial cytochrome c1 deficiency | CYC1 | 615453 | 1460 | CANDIDATE -> COX4I1-Related COX Deficiency (0.961) |
| [ ] | 717 | 7.3.03.01 | UQCRQ-related Mitochondrial complex III deficiency, nuclear type 4 | UQCRQ | 615159 | 1460 | CANDIDATE -> SCO1-Related COX Deficiency (0.970) |
| [ ] | 715 | 7.3.04.01 | LYRM7-related Mitochondrial complex III deficiency, nuclear type 8 | LYRM7 | 615838 | 1460 | CANDIDATE -> TACO1-Related COX Deficiency (0.970) |
| [ ] | 747 | 7.3.04.02 | HCCS-related Holocytochrome c synthase deficiency | HCCS | 309801 | 2556 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.762) |
| [ ] | 1686 | 7.3.04.03 | UQCRFS1-related Mitochondrial complex III deficiency, nuclear type 10 | UQCRFS1 | 618775 | 1460 | CANDIDATE -> COX14-Related COX Deficiency (0.971) |
| [ ] | 1342 | 7.3.05.01 | UQCC2-related Mitochondrial complex III deficiency, nuclear type | UQCC2 | 615824 | - | CANDIDATE -> COX10-Related COX Deficiency (0.949) |
| [ ] | 714 | 7.3.06.01 | UQCC3-related Mitochondrial complex III deficiency, nuclear type 9 | UQCC3 | 616111 | 1460 | CANDIDATE -> PET117-Related COX Deficiency (0.961) |
| [ ] | 1744 | 7.3.07.01 | UQCRC1-related Parkinsonism with polyneuropathy | UQCRC1 | 619279 | - | UNMAPPED; weak candidate Neutral Lipid Storage Myopathy (0.590) |
| [ ] | 2072 | 7.3.08.01 | UQCRH-related Ubiquinol-cytochrome C reductase hinge protein deficiency | UQCRH | 620137 | - | CANDIDATE -> COX20-Related COX Deficiency (0.971) |

### WP-019: Disorders of complex IV subunits and assembly factors (part 1 of 2)

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex IV subunits and assembly factors
- Records: 22 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 14)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 721 | 7.4.01.01 | COA6-related Cytochrome c oxidase assembly factor 6 deficiency | COA6 | 616501 | 1561 | CANDIDATE -> COX15-Related COX Deficiency (0.988) |
| [ ] | 935 | 7.4.1.01 | PET100-related Mitochondrial complex IV deficiency, nuclear type 12 deficiency | PET100 | 619055 | 255241 | CANDIDATE -> PET100-Related COX Deficiency (0.903) |
| [ ] | 1360 | 7.4.1.02 | COX5A-related Cytochrome c oxidase subunit 5A deficiency | COX5A | 603773 | - | UNMAPPED; weak candidate COX5A-Related COX Deficiency (0.891) |
| [ ] | 723 | 7.4.02.01 | COX10-related Cytochrome c oxidase assembly factor 10 deficiency | COX10 | 220110;256000 | 254905 | UNMAPPED; weak candidate COX10-Related COX Deficiency (0.826) |
| [ ] | 1361 | 7.4.2.01 | PET117-rerlated Mitochondrial complex IV deficiency | PET117 | 614771 | - | UNMAPPED; weak candidate PET117-Related COX Deficiency (0.725) |
| [ ] | 725 | 7.4.03.01 | COX15-related Cytochrome c oxidase assembly factor 15 deficiency | COX15 | 615119;256000 | 1561 | MAPPED -> COX15-Related COX Deficiency (alias_exact:cardioencephalomyopathy fatal infantile due to cytochrome c oxidase deficiency 2) |
| [ ] | 726 | 7.4.04.01 | COX20-related Cytochrome c oxidase assembly factor 20 deficiency | COX20 | 220110 | 254905 | UNMAPPED; weak candidate COX20-Related COX Deficiency (0.826) |
| [ ] | 730 | 7.4.04.02 | COX4I2-related Cytochrome c oxidase subunit 4I2 deficiency | COX4I2 | 612714 | 199337 | MAPPED -> COX4I2-Related Pancreatic Insufficiency-Anemia-Hyperostosis Syndrome (identifier:OMIM:612714) |
| [ ] | 727 | 7.4.05.01 | SCO1-related Mitochondrial complex IV deficiency | SCO1 | 220110 | 1561 | MAPPED -> SCO1-Related COX Deficiency (alias_exact:mitochondrial complex iv deficiency nuclear type 4) |
| [ ] | 731 | 7.4.05.02 | COX6A1 related Cytochrome c oxidase subunit 6A1 deficiency | COX6A1 | 616039 | 435998 | UNMAPPED; weak candidate COX6A2-Related COX Deficiency (0.865) |
| [ ] | 728 | 7.4.06.01 | SCO2-related Myopia 6 | SCO2 | 604377;608908 | 98619 | MAPPED -> SCO2-Related Fatal Infantile Cardioencephalomyopathy (alias_exact:cardioencephalomyopathy fatal infantile due to cytochrome c oxidase deficiency 1) |
| [ ] | 732 | 7.4.06.02 | COX6B1-related Cytochrome c oxidase subunit 6B1 deficiency | COX6B1 | 220110 | 254905 | UNMAPPED; weak candidate COX6B1-Related COX Deficiency (0.885) |
| [ ] | 729 | 7.4.07.01 | SURF1-related COX IV deficiency | SURF1 | 256000;616684 | 391351 | UNMAPPED; weak candidate SURF1-Related Leigh Syndrome (0.763) |
| [ ] | 733 | 7.4.07.02 | COX7B-related Cytochrome c oxidase subunit 7B deficiency | COX7B | 300887 | 2556 | UNMAPPED; weak candidate COX6B1-Related COX Deficiency (0.863) |
| [ ] | 734 | 7.4.08.01 | COX8A-related Cytochrome c oxidase subunit 8A deficiency | COX8A | 619059 | 254905 | UNMAPPED; weak candidate COX8A-Related COX Deficiency (0.891) |
| [ ] | 425 | 7.4.08.02 | LRPPRC-related Leigh Syndrome with French-Canadian Ethnicity | LRPPRC | 220111 | 70472 | UNMAPPED; weak candidate Leigh Syndrome (0.475) |
| [ ] | 934 | 7.4.09.01 | TACO1-related Mitochondrial complex IV deficiency deficiency | TACO1 | 220110 | 255241 | UNMAPPED; weak candidate TACO1-Related COX Deficiency (0.792) |
| [ ] | 1359 | 7.4.09.02 | COX4I1-related Cytochrome c oxidase subunit 4I1 deficiency | COX4I1 | 123864 | - | CANDIDATE -> COX4I1-Related COX Deficiency (0.915) |
| [ ] | 936 | 7.4.11.01 | FASTKD2-related Fast kinase domain-containing protein 3 deficiency | FASTKD2 | 220110 | 166105 | UNMAPPED; weak candidate E3-binding protein deficiency (0.658) |
| [ ] | 937 | 7.4.12.01 | COA8-related APOT1 apoptogenic protein 1 deficiency | COA8 | 619061 | - | MAPPED -> COA8-Related COX Deficiency (alias_exact:mitochondrial complex iv deficiency nuclear type 17) |
| [ ] | 722 | 7.4.13.01 | COA7-related Cytochrome C oxidase assembly factor 7 deficiency | COA7 | 220110 | 254905 | UNMAPPED; weak candidate COA3-Related COX Deficiency (0.811) |
| [ ] | 1187 | 7.4.14.01 | CEP89-related Isolated complex IV deficiency | CEP89 | 615470 | - | UNMAPPED; weak candidate COX14-Related COX Deficiency (0.824) |

### WP-020: Disorders of complex IV subunits and assembly factors (part 2 of 2)

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex IV subunits and assembly factors
- Records: 11 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 5)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 724 | 7.4.15.01 | COX14-related Cytochrome c oxidase assembly factor 14 deficiency | COX14 | 220110 | 254905 | UNMAPPED; weak candidate COX14-Related COX Deficiency (0.826) |
| [ ] | 720 | 7.4.16.01 | COA5-related Cytochrome c oxidase assembly factor 5 deficiency | COA5 | 616500 | 1561 | CANDIDATE -> COX15-Related COX Deficiency (0.988) |
| [ ] | 719 | 7.4.17.01 | COA3-related Cytochrome c oxidase assembly factor 3 deficiency | COA3 | 619058 | 254905 | UNMAPPED; weak candidate COA3-Related COX Deficiency (0.830) |
| [ ] | 696 | 7.4.18.01 | NDUFA4-related Cytochrome c oxidase subunit NDUFA4 (COXFA4) deficiency | NDUFA4 | 619065 | 255241 | MAPPED -> COXFA4-Related COX Deficiency (identifier:OMIM:619065) |
| [ ] | 1351 | 7.4.19.01 | ALDH1B1-related Aldehyde dehydrogenase 1B1 deficiency | ALDH1B1 | 100670 | - | UNMAPPED; weak candidate Dimethylglycine Dehydrogenase Deficiency (0.800) |
| [ ] | 1690 | 7.4.21.01 | COX16-related Cytochrome c oxidase assembly factor 16 deficiency | COX16 | 618064 | - | MAPPED -> COX16-Related COX Deficiency (identifier:OMIM:618064) |
| [ ] | 1708 | 7.4.22.01 | COX6A2-related Cytochrome c oxidase subunit 6A2 deficiency | COX6A2 | 619062 | 254905 | MAPPED -> COX6A2-Related COX Deficiency (alias_exact:mc4dn18) |
| [ ] | 2038 | 7.4.23.01 | RAF5IF-related Skeletal anomalies and mental retardation syndrome | RAB5IF | 616994 | - | UNMAPPED; weak candidate CHIME_syndrome (0.636) |
| [ ] | 2047 | 7.4.24.01 | COX11-related Cytochrome c oxidase copper chaperone 11 deficiency | COX11 | 603648 | - | MAPPED -> COX11-Related COX Deficiency (alias_exact:infantile onset mitochondrial encephalopathy) |
| [ ] | 2188 | 7.4.25.01 | FASTKD5-related Leigh syndrome | FASTKD5 | 614272 | - | AMBIGUOUS: 3 local entities (alias_exact:leigh syndrome) |
| [ ] | 2238 | 7.4.26.01 | COX18-related Cytochrome c oxi­dase assembly factor 18 deficiency | COX18 | 621488 | - | UNMAPPED; weak candidate COX18-Related COX Deficiency (0.818) |

### WP-021: Disorders of complex V subunits and assembly factors

- Classification: Intermediary Metabolism: Energy -> Nuclear-encoded disorders of oxidative phosphorylation
- Subgroup scope: Disorders of complex V subunits and assembly factors
- Records: 9 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 576 | 7.5.01.01 | TMEM70-related Transmembrane protein 70 deficiency | TMEM70 | 614052 | - | UNMAPPED; weak candidate COX11-Related COX Deficiency (0.756) |
| [ ] | 739 | 7.5.01.02 | ATP5F1A-related Mitochondrial ATP synthase F1 subunit alpha deficiency | ATP5F1A | 616045;615228 | 254913 | CANDIDATE -> SCO1-Related COX Deficiency (0.969) |
| [ ] | 738 | 7.5.02.01 | ATPAF2-related Mitochondrial ATP synthase F1 assembly factor 2 deficiency | ATPAF2 | 604273 | 254913 | CANDIDATE -> SURF1-Related Leigh Syndrome (0.990) |
| [ ] | 939 | 7.5.02.02 | ATP5F1D-related Mitochondrial ATP synthase F1 subunit δ deficiency | ATP5F1D | 603150 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.787) |
| [ ] | 740 | 7.5.03.01 | ATP5F1E-related Mitochondrial ATP synthase F1 subunit epsilon deficiency | ATP5F1E | 614053 | - | CANDIDATE -> COX10-Related COX Deficiency (0.990) |
| [ ] | 1290 | 7.5.06.01 | ATP5MD-related DAPIT deficiency | ATP5MD | 615204 | - | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.714) |
| [ ] | 1709 | 7.5.07.01 | ATP5PO-related Mitochondrial ATP synthase F1 subunit O deficiency | ATP5PO | 620359 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.769) |
| [ ] | 2048 | 7.5.08.01 | ATP5F1B-related Mitochondrial ATP synthase betta-subunit deficiency | ATP5F1B | 102910 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.761) |
| [ ] | 2114 | 7.5.09.01 | ATP5MC3-related Dystonia, early-onset, and/or spastic paraplegia | ATP5MC3 | 619681 | - | UNMAPPED; weak candidate Hereditary Spastic Paraplegia 48 (0.686) |

### WP-022: Disorders of coenzyme Q10 biosynthesis + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial cofactor biosynthesis
- Subgroup scope: Disorders of coenzyme Q10 biosynthesis; Disorders of lipoic acid and iron-sulfur metabolism
- Records: 30 (MAPPED 9, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 252 | 8.1.01.01 | PDSS1-related Prenyl diphosphate synthase subunit 1 deficiency | PDSS1 | 607429;607426 | 254898 | MAPPED -> PDSS1 (alias_exact:pdss1) |
| [ ] | 1201 | 8.1.1.01 | COQ5-related Coenzyme Q5 methyltransferase deficiency | COQ5 | 616359 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.899) |
| [ ] | 253 | 8.1.02.01 | PDSS2-related Prenyl diphosphate synthase subunit 2 deficiency | PDSS2 | 614652 | 255249 | MAPPED -> PDSS2 (alias_exact:pdss2) |
| [ ] | 254 | 8.1.03.01 | COQ2-related Coenzyme Q2 polyprenyltranferase deficiency | COQ2 | 609825;607426 | 98933 | MAPPED -> COQ2 (alias_exact:coq2) |
| [ ] | 1038 | 8.1.04.01 | COQ4-related Coenzyme Q4 deficiency | COQ4 | 616276 | 457185 | CANDIDATE -> Primary Coenzyme Q10 Deficiency (0.933) |
| [ ] | 531 | 8.1.05.01 | COQ6-related Coenzyme Q6 monooxygenase deficiency | COQ6 | 614650 | 93921 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.899) |
| [ ] | 1039 | 8.1.06.01 | COQ7-related Coenzyme Q7 hydroxylase deficiency | COQ7 | 616733 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.899) |
| [ ] | 256 | 8.1.07.01 | COQ8A-related Coenzyme Q8A (ADCK3) deficiency | COQ8A | 612016 | 139485 | MAPPED -> Autosomal Recessive Ataxia Due to Ubiquinone Deficiency (identifier:ORPHA:139485) |
| [ ] | 1040 | 8.1.08.01 | COQ8B-related Coenzyme Q8B (ADCK4) deficiency | COQ8B | 615573 | 93213 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.808) |
| [ ] | 255 | 8.1.09.01 | COQ9-related Coenzyme 9 deficiency | COQ9 | 614654 | 319678 | MAPPED -> COQ9 (alias_exact:coq9) |
| [ ] | 257 | 8.1.13.01 | APTX-related Aprataxin deficiency | APTX | 606350 | 1168 | MAPPED -> AOA1 (alias_exact:aoa1) |
| [ ] | 1755 | 8.1.14.01 | ADCK2-related CoQ-dependend myopathy | ADCK2 | 621162 | - | UNMAPPED; weak candidate TTN-CNM (0.629) |
| [ ] | 1758 | 8.1.15.01 | HPDL-related 4-Hydroxyphenylpyruvate dioxygenase-like protein deficiency | HPDL | 619026 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.685) |
| [ ] | 426 | 8.2.1.01 | ISCU-related Hereditary Myopathy with Lactic Acidosis | ISCU | 255125 | 43115 | UNMAPPED; weak candidate HNPP (0.646) |
| [ ] | 835 | 8.2.01.01 | LIPT2-related Lipoyltransferase 2 deficiency | LIPT2 | 617668 | 447795 | MAPPED -> Neonatal Severe Encephalopathy with Lactic Acidosis and Brain Abnormalities (alias_exact:nelaba) |
| [ ] | 836 | 8.2.02.01 | LIAS-related Lipoic acid synthase deficiency | LIAS | 614462 | 401859 | CANDIDATE -> Lipoic Acid Synthetase Deficiency (0.969) |
| [ ] | 837 | 8.2.03.01 | LIPT1-related Lipoyltransferase 1 deficiency | LIPT1 | 616299 | 401862 | UNMAPPED |
| [ ] | 838 | 8.2.04.01 | NFU1-related Multiple mitochondrial dysfunctions syndrome type 1 | NFU1 | 605711 | 401869 | CANDIDATE -> Multiple Mitochondrial Dysfunctions Syndrome 9B (0.918) |
| [ ] | 839 | 8.2.05.01 | BOLA3-related Multiple mitochondrial dysfunctions syndrome type 2 with hyperglycinemia | BOLA3 | 614299 | 401874 | UNMAPPED; weak candidate Multiple Mitochondrial Dysfunctions Syndrome 9B (0.756) |
| [ ] | 1278 | 8.2.06.01 | GLRX5-related Glutaredoxin 5 deficiency | GLRX5 | 205950 | 401866 | UNMAPPED; weak candidate MLASA2 (0.600) |
| [ ] | 1236 | 8.2.07.01 | IBA57-related Multiple mitochondrial dysfunctions syndrome | IBA57 | 615330 | 363424 | CANDIDATE -> Multiple Mitochondrial Dysfunctions Syndrome 9B (0.967) |
| [ ] | 1237 | 8.2.08.01 | ISCA1-related Multiple mitochondrial dysfunctions syndrome | ISCA1 | 617613 | - | CANDIDATE -> Multiple Mitochondrial Dysfunctions Syndrome 9B (0.967) |
| [ ] | 1238 | 8.2.09.01 | ISCA2-related Multiple mitochondrial dysfunctions syndrome | ISCA2 | 616370 | 457406 | CANDIDATE -> Multiple Mitochondrial Dysfunctions Syndrome 9B (0.967) |
| [ ] | 1239 | 8.2.11.01 | ABCB7-related Sideroblastic anemia and spinocerebellar ataxia | ABCB7 | 301310 | 2802 | UNMAPPED; weak candidate IOSCA (0.706) |
| [ ] | 1240 | 8.2.12.01 | FDXR-related Ferredoxin reductase deficiency | FDXR | 617717 | - | MAPPED -> Multiple Mitochondrial Dysfunctions Syndrome 9B (alias_exact:ferredoxin reductase deficiency) |
| [ ] | 1241 | 8.2.13.01 | FXN-related Frataxin deficiency | FXN | 229300 | 95 | MAPPED -> Friedreich Ataxia (identifier:OMIM:229300) |
| [ ] | 1170 | 8.2.14.01 | NFS1-related Infantile mitochondrial complex II/III deficiency | NFS1 | 603485 | 397593 | UNMAPPED; weak candidate COX10-Related COX Deficiency (0.687) |
| [ ] | 1169 | 8.2.15.01 | ISD11-related Combined oxidative phosphorylation deficiency | LYRM4 | 615595 | 397593 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.722) |
| [ ] | 1168 | 8.2.16.01 | FDX2-related Ferredoxin 2 deficiency | FDX2 | 614585 | - | UNMAPPED; weak candidate Multiple Mitochondrial Dysfunctions Syndrome 9B (0.815) |
| [ ] | 2124 | 8.2.17.1 | HSCB-related Mitochondrial iron-sulfur cluster cochaperone  deficiency | HSCB | 619523 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.639) |

### WP-023: Disorders of mitochondrial cytochrome c biosynthesis

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial cofactor biosynthesis
- Subgroup scope: Disorders of mitochondrial cytochrome c biosynthesis
- Records: 1 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 1)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 746 | 8.3.03.01 | CYCS-related Mitochondrial cytochrome c deficiency | CYCS | 612004 | 168629 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.747) |

### WP-024: Disorders of mitochondrial nucleotide pool maintenance + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial DNA maintenance and replication
- Subgroup scope: Disorders of mitochondrial nucleotide pool maintenance; Disorders of mtDNA replication and maintenance
- Records: 21 (MAPPED 1, AMBIGUOUS 3, CANDIDATE 7, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 143 | 9.1.03.01 | DGUOK-related Mitochondrial deoxyguanosine kinase deficiency | DGUOK | 251880;601465 | 494348 | CANDIDATE -> Mitochondrial DNA Depletion Syndrome 7 (0.983) |
| [ ] | 943 | 9.1.04.01 | MPV17-related Mitochondrial DNA depletion syndrome 6 (hepatocerebral type) | MPV17 | 256810 | 255229 | CANDIDATE -> Mitochondrial DNA Depletion Syndrome 7 (0.983) |
| [ ] | 158 | 9.1.06.01 | TK2-related Mitochondrial thymidine kinase 2 deficiency | TK2 | 609560;188250 | 254875 | CANDIDATE -> Mitochondrial Neurogastrointestinal Encephalomyopathy (0.914) |
| [ ] | 774 | 9.1.06.02 | SAMHD1-related Stenosis, aneurysm, moyamoya and stroke (SAMS association) (AGS5) | SAMHD1 | 612952 | 481662 | AMBIGUOUS: 2 local entities (identifier:OMIM:612952) |
| [ ] | 1406 | 9.1.06.03 | SAMHD1-related Familial chilblain lupus type 2 | SAMHD1 | 612952 | 481662 | AMBIGUOUS: 2 local entities (identifier:OMIM:612952) |
| [ ] | 150 | 9.1.07.01 | RRM2B-related Mitochondrial ribonucelotide reductase subunit 2 deficiency | RRM2B | 604712 | 298 | UNMAPPED; weak candidate Mitochondrial Neurogastrointestinal Encephalomyopathy (0.881) |
| [ ] | 157 | 9.1.08.01 | TYMP-related Thymidine phosphorylase deficiency | TYMP | 131222;603041 | 298 | AMBIGUOUS: 2 local entities (alias_exact:mngie) |
| [ ] | 2098 | 9.1.9.01 | RRM1-related Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 6 | RRM1 | 620647 | - | UNMAPPED; weak candidate CRADD-Related Thin Lissencephaly (0.511) |
| [ ] | 2180 | 9.1.10.01 | GUK1-related Guanylate kinase 1 deficiency | GUK1 | 621071 | - | CANDIDATE -> Mitochondrial (0.987) |
| [ ] | 1188 | 9.1.14.01 | CMPK2-related Mitochondrial UMP-CMP kinase 2 deficiency | CMPK2 | 611787 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.805) |
| [ ] | 411 | 9.2.01.01 | POLG-related Mitochondrial DNA polymerase gamma catalytic subunit deficiency 4A | POLG | 203700 | 726 | CANDIDATE -> Mitochondrial Neurogastrointestinal Encephalomyopathy (0.904) |
| [ ] | 946 | 9.2.1.01 | RNASEH1-related Mitochondrial ribonuclease H1 deficiency | RNASEH1 | 615156 | 329336 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.741) |
| [ ] | 420 | 9.2.01.02 | POLG-related Spinocerebellar Ataxia with Epilepsy, included (SCAE, included) | POLG | 607459 | 402082;70595;254881 | MAPPED -> Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis (alias_exact:sando) |
| [ ] | 1428 | 9.2.01.04 | POLG-related Mitochondrial DNA polymerase gamma catalytic subunit deficiency | POLG | 607459 | 94125 | UNMAPPED; weak candidate Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis (0.529) |
| [ ] | 942 | 9.2.02.01 | POLG2-related Mitochondrial DNA polymerase gamma accessory subunit deficiency | POLG2 | 610131 | 254892 | UNMAPPED; weak candidate Mitochondrial DNA Depletion Syndrome 7 (0.714) |
| [ ] | 944 | 9.2.05.01 | TWNK-related Mitochondrial DNA helicase deficiency | TWNK | 271245;616138 | 70595 | UNMAPPED; weak candidate Mitochondrial DNA Depletion Syndrome 7 (0.794) |
| [ ] | 945 | 9.2.09.01 | DNA2-related Helicase deficiency | DNA2 | 615156 | 352470 | UNMAPPED; weak candidate HFM1-related gametogenic failure (0.731) |
| [ ] | 947 | 9.2.11.01 | MGME1-related Mitochondrial genome maintenance exonuclease 1 deficiency | MGME1 | 615084 | 352447 | CANDIDATE -> Mitochondrial (0.927) |
| [ ] | 1336 | 9.2.13.01 | TOP3A-related Topoisomerase 3α deficiency | TOP3A | 618098 | - | UNMAPPED; weak candidate E1-alpha deficiency (0.706) |
| [ ] | 1710 | 9.2.14.01 | SSBP1-related Single-stranded DNA-binding protein 1 deficiency | SSBP1 | 165510 | 90635 | UNMAPPED; weak candidate E3-binding protein deficiency (0.727) |
| [ ] | 2127 | 9.2.15.01 | LIG3-related Mitochondrial DNA depletion syndrome 20 (MNGIE type) | LIG3 | 619780 | - | CANDIDATE -> Mitochondrial Neurogastrointestinal Encephalomyopathy (0.970) |

### WP-025: Disorders of mitochondrial transcript processing and modification

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial gene expression
- Subgroup scope: Disorders of mitochondrial transcript processing and modification
- Records: 21 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 949 | 10.1.01.01 | PNPT1-related Mitochondrial RNA import protein deficiency | PNPT1 | 614932;614934 | 90636 | UNMAPPED; weak candidate Autosomal Dominant Cerebellar Ataxia Type III (0.432) |
| [ ] | 957 | 10.1.1.01 | TRIT1-related tRNA isopentenyl transferase deficiency | TRIT1 | 617873 | - | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.771) |
| [ ] | 950 | 10.1.02.01 | TRMT10C-related Ribonuclease P 5' tRNA processing enzyme deficiency | TRMT10C | 616974 | 478042 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 951 | 10.1.03.01 | ELAC2-related Ribonuclease Z 3' tRNA processing enzyme deficiency | ELAC2 | 615440 | 369913 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 952 | 10.1.04.01 | MTPAP-related Mitochondrial poly(A) polymerase deficiency | MTPAP | 613672 | 254343 | CANDIDATE -> Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity (0.933) |
| [ ] | 953 | 10.1.05.01 | TRNT1-related CCA-adding tRNA-nucleotidyltransferase deficiency | TRNT1 | 616959 | 369861 | UNMAPPED; weak candidate EYS-Related Retinitis Pigmentosa (0.667) |
| [ ] | 954 | 10.1.06.01 | MTFMT-related Mitochondrial methionyl-tRNA formyltransferase deficiency | MTFMT | 614947 | 319524 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.650) |
| [ ] | 955 | 10.1.07.01 | GTPBP3-related tRNA 5-taurinomethyluridine modifier deficiency | GTPBP3 | 616198 | 444013 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.650) |
| [ ] | 956 | 10.1.08.01 | MTO1-related tRNA 5-carboxymethylaminomethyl transferase deficiency | MTO1 | 614702 | 314637 | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.673) |
| [ ] | 444 | 10.1.09.01 | PUS1-related Pseudouridine synthase 1 deficiency | PUS1 | 600462 | 2598 | MAPPED -> Myopathy, Lactic Acidosis, and Sideroblastic Anemia (identifier:ORPHA:2598) |
| [ ] | 958 | 10.1.11.01 | TRMT5-related tRNA methyltransferase 5 deficiency | TRMT5 | 616539 | 477684 | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.775) |
| [ ] | 445 | 10.1.12.01 | TRMU-related tRNA 5-methylaminomethyl-2-thiouridylate-methyltransferase deficiency | TRMU | 613070 | 90641 | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.667) |
| [ ] | 1404 | 10.1.14.01 | NSUN3-related Mitochondrial methionyl-tRNA methyltransferase deficiency | NSUN3 | 617491 | - | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.686) |
| [ ] | 64 | 10.1.15.01 | HSD17B10-related 17-beta-hydroxysteroid dehydrogenase type 10 deficiency | HSD17B10 | 300438 | - | UNMAPPED; weak candidate HSD10 Mitochondrial Disease (0.312) |
| [ ] | 1190 | 10.1.15.02 | PDE12-related Mitochondrial poly(A) exoribonuclease deficiency | PDE12 | 616519 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.727) |
| [ ] | 1189 | 10.1.16.01 | TFAM-related Mitochondrial transcription factor A deficiency | TFAM | 617156 | - | CANDIDATE -> Mitochondrial (0.987) |
| [ ] | 1711 | 10.1.17.01 | POLRMT-related Mitochondrial RNA polymerase deficiency | POLRMT | 619743 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.775) |
| [ ] | 1712 | 10.1.18.01 | PRORP-related RNase P catalytic subunit deficiency | PRORP | 619737 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.636) |
| [ ] | 1713 | 10.1.19.01 | THG1L-related tRNA-His guanylyltransferase 1 like deficiency | THG1L | 618800 | - | CANDIDATE -> CALFAN Syndrome (0.978) |
| [ ] | 2138 | 10.1.21.01 | TEFM-related Combined oxidative phosphorylation deficiency | TEFM | 620451 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.722) |
| [ ] | 2207 | 10.1.22.01 | MTERF3-related Developmental delay, intermittent hypoglycemia and metabolic acidosis | MTERF3 | 616930 | - | UNMAPPED; weak candidate CN-Related Developmental and Epileptic Encephalopathy (0.500) |

### WP-026: Disorders of mitochondrial aminoacyl-tRNA synthetases

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial gene expression
- Subgroup scope: Disorders of mitochondrial aminoacyl-tRNA synthetases
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 19)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 988 | 10.2.01.01 | AARS2-related Mitochondrial alanyl-tRNA synthetase deficiency | AARS2 | 614096;615889 | 99853 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.818) |
| [ ] | 996 | 10.2.1.01 | MARS2-related Mitochondrial methionyl-tRNA synthetase deficiency | MARS2 | 611390 | 314603 | UNMAPPED; weak candidate ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (0.835) |
| [ ] | 989 | 10.2.02.01 | RARS2-related Mitochondrial arginyl-tRNA synthetase deficiency | RARS2 | 611523 | 166073 | MAPPED -> PCH6 (alias_exact:pch6) |
| [ ] | 990 | 10.2.03.01 | NARS2-related Mitochondrial asparaginyl-tRNA synthetase deficiency | NARS2 | 616239 | 444458 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.796) |
| [ ] | 446 | 10.2.04.01 | DARS2-related Mitochondrial aspartyl-tRNA synthetase deficiency | DARS2 | 611105 | 137898 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.800) |
| [ ] | 991 | 10.2.05.01 | CARS2-related Mitochondrial cysteinyl-tRNA synthetase deficiency | CARS2 | 616672 | 477774 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.791) |
| [ ] | 992 | 10.2.06.01 | EARS2-related Mitochondrial glutamyl-tRNA synthetase deficiency | EARS2 | 614924 | 314051 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.822) |
| [ ] | 993 | 10.2.07.01 | HARS2-related Mitochondrial histidyl-tRNA synthetase deficiency | HARS2 | 614926 | 2855 | UNMAPPED; weak candidate Perrault-spectrum (0.829) |
| [ ] | 994 | 10.2.08.01 | IARS2-related Mitochondrial isoleucyl-tRNA synthetase deficiency | IARS2 | 616007 | 436174 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.791) |
| [ ] | 995 | 10.2.09.01 | LARS2-related Mitochondrial leucyl-tRNA synthetase deficiency | LARS2 | 615300 | 2855 | UNMAPPED; weak candidate Perrault-spectrum (0.829) |
| [ ] | 997 | 10.2.11.01 | FARS2-related Mitochondrial phenylalanyl-tRNA synthetase deficiency | FARS2 | 614946 | 466722 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.787) |
| [ ] | 998 | 10.2.12.01 | SARS2-related Mitochondrial seryl-tRNA synthetase deficiency | SARS2 | 613845 | 363694 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.828) |
| [ ] | 1279 | 10.2.13.01 | YARS2-related Mitochondrial tyrosyl-tRNA synthetase deficiency | YARS2 | 613561 | 2598 | MAPPED -> Myopathy, Lactic Acidosis, and Sideroblastic Anemia (identifier:ORPHA:2598) |
| [ ] | 999 | 10.2.14.01 | VARS2-related Mitochondrial valyl-tRNA synthetase deficiency | VARS2 | 615917 | 420728 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.828) |
| [ ] | 1000 | 10.2.15.01 | WARS2-related Mitochondrial tryptophanyl-tRNA synthetase deficiency | WARS2 | 617710 | 88616 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.766) |
| [ ] | 1195 | 10.2.18.01 | QRSL1-related Mitochondrial glutamyl-tRNA(Gln) amidotransferase subunit A deficiency | QRSL1 | 617209 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.618) |
| [ ] | 1225 | 10.2.19.01 | GATC-related Mitochondrial glutamyl-tRNA(Gln) amidotransferase subunit C deficiency | GATC | 617210 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.618) |
| [ ] | 1343 | 10.2.21.01 | PARS2-related Mitochondrial prolyl-tRNA synthetase deficiency | PARS2 | 612036 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.818) |
| [ ] | 1224 | 10.2.22.01 | GATB-related Mitochondrial glutamyl-tRNA(Gln) amidotransferase subunit B deficiency | GATB | 603645 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.618) |
| [ ] | 1194 | 10.2.23.01 | TARS2-related Mitochondrial threonyl-tRNA synthetase deficiency | TARS2 | 615918 | 420733 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.822) |
| [ ] | 1514 | 10.2.32.01 | DFNB89-related Mitochondrial and cytoplasmic lysyl-tRNA synthetase deficiency | KARS1 | 613641;613916 | 254334;90636 | UNMAPPED; weak candidate Autosomal Recessive Osteopetrosis Type 2 (0.789) |
| [ ] | 1715 | 10.2.33.01 | GARS1-related Mitochondrial and cytoplasmic glycyl-tRNA synthetase deficiency | GARS1 | 601472;619042 | 99938;139536 | MAPPED -> Distal Hereditary Motor Neuronopathy, Autosomal Dominant (identifier:OMIM:601472) |

### WP-027: Disorders of the mitoribosome

- Classification: Intermediary Metabolism: Energy -> Disorders of mitochondrial gene expression
- Subgroup scope: Disorders of the mitoribosome
- Records: 29 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 27)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 960 | 10.3.01.01 | MRPL3-related Mitochondrial ribosomal large subunit 3 deficiency | MRPL3 | 614582 | 319509 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.708) |
| [ ] | 1193 | 10.3.1.01 | MRPS23-related Mitochondrial ribosomal small subunit 23 deficiency | MRPS23 | 611985 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 964 | 10.3.01.02 | RMND1-related Combined oxidative phosphorylation deficiency type 11 | RMND1 | 614922 | 324535 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.650) |
| [ ] | 436 | 10.3.02.01 | GFM1-related Mitochondrial elongation factor G1 deficiency | GFM1 | 609060 | 137681 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.703) |
| [ ] | 961 | 10.3.02.02 | MRPL44-related Mitochondrial ribosomal large subunit 44 deficiency | MRPL44 | 615395 | 352563 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 965 | 10.3.03.01 | GFM2-related Mitochondrial elongation factor G2 deficiency | GFM2 | 606544 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.703) |
| [ ] | 1223 | 10.3.03.02 | MRPS2-related Mitochondrial ribosomal small subunit 2 deficiency | MRPS2 | 617950 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 437 | 10.3.04.01 | MRPS16-related Mitochondrial ribosomal small subunit 16 deficiency | MRPS16 | 610498 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 439 | 10.3.04.02 | TSFM-related Mitochondrial elongation factor Ts deficiency | TSFM | 610505 | 168566 | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.723) |
| [ ] | 440 | 10.3.05.01 | TUFM-related Mitochondrial elongation factor Tu deficiency | TUFM | 610678 | 254925 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.703) |
| [ ] | 441 | 10.3.05.02 | MRPS22-related Mitochondrial ribosomal small subunit 22 deficiency | MRPS22 | 611719 | 137908 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 443 | 10.3.06.01 | C12ORF65-related Mitochondrial release factor deficiency | MTRFR | 613559 | 320375 | UNMAPPED; weak candidate ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (0.738) |
| [ ] | 962 | 10.3.06.02 | MRPS34-related Mitochondrial ribosomal small subunit 34 deficiency | MRPS34 | 617664 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 1345 | 10.3.07.01 | GUF1-related Epileptic encephalopathy, early infantile | GUF1 | 617065 | - | UNMAPPED; weak candidate SYNGAP1-related Disorder (0.631) |
| [ ] | 1344 | 10.3.09.01 | ERAL1-related Perrault syndrome | ERAL1 | 617565 | - | MAPPED -> Perrault-spectrum (alias_exact:perrault syndrome) |
| [ ] | 1192 | 10.3.11.01 | MRPS7-related Mitochondrial ribosomal small subunit 7 deficiency | MRPS7 | 617872 | 457223 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 1348 | 10.3.12.01 | MRPS14-related Mitochondrial ribosomal small subunit 14 deficiency | MRPS14 | 611978 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 1191 | 10.3.13.01 | MRPL12-related Mitochondrial ribosomal large subunit 12 deficiency | MRPL12 | 602375 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 1352 | 10.3.15.01 | MRPS28-Related Mitochondrial ribosomal small subunit 28 deficiency | MRPS28 | 611990 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 1365 | 10.3.16.01 | MRM2-related Mitochondrial rRNA methyltransferase 2 deficiency | MRM2 | 618567 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.711) |
| [ ] | 1716 | 10.3.17.01 | MRPL24-related Mitochondrial ribosomal large subunit 24 deficiency | MRPL24 | 611836 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 1717 | 10.3.18.01 | MRPS25-related Mitochondrial ribosomal small subunit 25 deficiency | MRPS25 | 619025 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.674) |
| [ ] | 1718 | 10.3.19.01 | PTCD3-related Mitochondrial ribosomal small subunit 39 deficiency | PTCD3 | 619057 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 2104 | 10.3.20.01 | MRPL39-related Mitochondrial ribosomal large subunit 39 deficiency | MRPL39 | 620646 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 2145 | 10.3.21.01 | DAP3-related Perrault syndrome | DAP3 | 602074 | - | MAPPED -> Perrault-spectrum (alias_exact:perrault syndrome) |
| [ ] | 2146 | 10.3.22.01 | MRPL49-related Mitochondrial ribosomal large subunit 49 deficiency | MRPL49 | 606866 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 2130 | 10.3.23.01 | MRPL50-related Mitochondrial ribosomal large subunit 50 deficiency | MRPL50 | 611854 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.701) |
| [ ] | 2014 | 10.3.24.01 | SLIRP-related SRA Stem-loop interacting RNA binding protein deficiency | SLIRP | 610211 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.667) |
| [ ] | 2242 | 10.3.25.01 | MRPL42-related Combined oxidative phosphorylation deficiency syndrome | MRPL42 | 611847 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.642) |

### WP-028: Disorders of mitochondrial shuttles and carriers + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Energy -> Other disorders of mitochondrial function
- Subgroup scope: Disorders of mitochondrial shuttles and carriers; Disorders of mitochondrial protein import
- Records: 26 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 21)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 922 | 11.1.01.01 | SLC25A4-related Adenine nucleotide translocator deficiency AR | SLC25A4 | 615418 | 254892 | CANDIDATE -> Mitochondrial (0.927) |
| [ ] | 1372 | 11.1.01.02 | SLC25A4-related Adenine nucleotide translocator-related disorder | SLC25A4 | 609283 | 254892 | CANDIDATE -> Mitochondrial (0.927) |
| [ ] | 463 | 11.1.02.01 | SLC25A3-related Mitochondrial phosphate carrier deficiency | SLC25A3 | 610773 | 91130 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.747) |
| [ ] | 524 | 11.1.02.02 | SLC25A22-related Mitochondrial glutamate transporter deficiency | SLC25A22 | 609304 | 293181 | UNMAPPED; weak candidate DEE13 (0.759) |
| [ ] | 523 | 11.1.03.01 | SLC25A12-related Mitochondrial aspartate-glutamate carrier isoform 1 deficiency | SLC25A12 | 612949 | 353217 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.755) |
| [ ] | 923 | 11.1.04.01 | GPD1-related Cytosolic glycerol-3-phosphate dehydrogenase deficiency | GPD1 | 614480 | 300293 | UNMAPPED; weak candidate Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (0.788) |
| [ ] | 596 | 11.1.05.01 | SLC25A26-related S-adenosylmethionine carrier deficiency | SLC25A26 | 616794 | 466784 | UNMAPPED; weak candidate Hyperornithinemia-hyperammonemia-homocitrullinuria syndrome (0.746) |
| [ ] | 924 | 11.1.06.01 | SLC25A1-related Mitochondrial citrate carrier deficiency | SLC25A1 | 615182 | 98914 | UNMAPPED; weak candidate D-2-Hydroxyglutaric Aciduria (0.767) |
| [ ] | 466 | 11.1.07.01 | SLC25A38-related Mitochondrial glycine transporter deficiency | SLC25A38 | 205950 | 260305 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.737) |
| [ ] | 925 | 11.1.07.02 | SLC25A24-related Mitochondrial ATP-Mg-phosphate transporter deficiency | SLC25A24 | 612289 | 2095 | MAPPED -> Fontaine Progeroid Syndrome (identifier:OMIM:612289) |
| [ ] | 1036 | 11.1.08.01 | MICU1-related Mitochondrial calcium uniporter 1 deficiency | MICU1 | 615673 | 401768 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.733) |
| [ ] | 1389 | 11.1.08.02 | SLC25A11-related Mitochondrial oxoglutarate/malate carrier deficiency | SLC25A11 | 604165 | 29072 | UNMAPPED; weak candidate Carney-Stratakis syndrome (0.846) |
| [ ] | 1186 | 11.1.09.01 | SLC25A10-related Mitochondrial dicarboxylate transporter deficiency | SLC25A10 | 606794 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.707) |
| [ ] | 1350 | 11.1.14.01 | SLC25A21-related Mitochondrial oxodicarboxylate carrier deficiency | SLC25A21 | 607571 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.694) |
| [ ] | 1367 | 11.1.15.01 | MICU2-related Mitochondrial calcium uniporter 2 deficiency | MICU2 | 610632 | - | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.733) |
| [ ] | 1719 | 11.1.16.01 | MDH1-related Cytosolic malate dehydrogenase deficiency | MDH1 | 618959 | 618959 | CANDIDATE -> CN-Related Developmental and Epileptic Encephalopathy (0.966) |
| [ ] | 2050 | 11.1.17.01 | SLC25A36-related Mitochondrial pyrimidine nucleotide carrier 2 deficiency | SLC25A36 | 616149 | - | UNMAPPED; weak candidate HI/HA Syndrome (0.822) |
| [ ] | 1185 | 11.1.91.01 | GOT2-related Mitochondrial aspartate aminotransferase deficiency | GOT2 | 138150 | - | UNMAPPED; weak candidate ornithine aminotransferase deficiency (0.750) |
| [ ] | 1012 | 11.2.01.01 | TIMM14-related 3-Methylglutaconic aciduria type 5 deficiency | DNAJC19 | 610198 | 66634 | UNMAPPED; weak candidate Dilated Cardiomyopathy (0.786) |
| [ ] | 1010 | 11.2.01.02 | AGK-related Acylglycerol kinase deficiency | AGK | 212350;614691 | 1369 | MAPPED -> Sengers syndrome (alias_exact:sengers syndrome) |
| [ ] | 467 | 11.2.02.01 | TIMM8A-related Mohr-Tranebjaerg syndrome | TIMM8A | 304700 | 52368 | UNMAPPED |
| [ ] | 650 | 11.2.04.01 | TIMM50-related 3-methylglutaconic aciduria type 9 | TIMM50 | 607381 | 505216 | UNMAPPED; weak candidate Glutaryl-CoA Dehydrogenase Deficiency (0.759) |
| [ ] | 1015 | 11.2.06.01 | PAM16-related MAGMAS deficiency | PAM16 | 613320 | 401979 | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.762) |
| [ ] | 1466 | 11.2.07.01 | TIMM22-related Combined oxidative phosphorylation deficiency 43 | TIMM22 | 607251 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 1720 | 11.2.08.01 | TOMM70-related Multi-OXPHOS deficiency | TOMM70 | 606081 | - | UNMAPPED |
| [ ] | 2139 | 11.2.09.01 | TOMM7-related translocase deficiency | TOMM7 | 620601 | - | UNMAPPED; weak candidate Hyperornithinemia-hyperammonemia-homocitrullinuria syndrome (0.815) |

### WP-029: Disorders of mitochondrial protein quality control

- Classification: Intermediary Metabolism: Energy -> Other disorders of mitochondrial function
- Subgroup scope: Disorders of mitochondrial protein quality control
- Records: 26 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 19)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1016 | 11.3.01.01 | PMPCA-related Mitochondrial processing peptidase alpha deficiency | PMPCA | 213200 | 1170 | CANDIDATE -> CALFAN Syndrome (0.990) |
| [ ] | 1024 | 11.3.1.01 | AFG3L2-related m-AAA protease subunit deficiency | AFG3L2 | 614487;610246 | 313772 | UNMAPPED; weak candidate Spasticity-Ataxia-Gait Anomalies Syndrome (0.439) |
| [ ] | 1226 | 11.3.02.01 | PMPCB-related Mitochondrial processing peptidase betta deficiency | PMPCB | 617954 | - | CANDIDATE -> Multiple Mitochondrial Dysfunctions Syndrome 9B (0.968) |
| [ ] | 1017 | 11.3.03.01 | MIPEP-related Mitochondrial intermediate peptidase deficiency | MIPEP | 617228 | 478049 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.682) |
| [ ] | 1018 | 11.3.04.01 | CLPB-related 3-Methylglutaconic aciduria type 7, with cataracts, neurologic involvement and neutropenia | CLPB | 616271 | 445038 | UNMAPPED; weak candidate MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.500) |
| [ ] | 1032 | 11.3.04.02 | ATAD3A-related Harel-Yoon syndrome | ATAD3A | 617183 | 496790 | UNMAPPED |
| [ ] | 1019 | 11.3.05.01 | CLPP-related Perrault syndrome type 3 | CLPP | 614129 | 2855 | UNMAPPED; weak candidate Perrault-spectrum (0.829) |
| [ ] | 1020 | 11.3.06.01 | LONP1-related Cerebral, ocular, dental, auricular, and skeletal (CODAS) syndrome | LONP1 | 600373 | 1458 | UNMAPPED |
| [ ] | 1021 | 11.3.07.01 | HSPA9-related Epiphyseal, vertebral, ear, nose, plus associated malformations (EVEN-plus) syndrome | HSPA9 | 182170 | 496751 | UNMAPPED; weak candidate Inherited Aplastic Anemia (0.615) |
| [ ] | 1371 | 11.3.08.01 | HSP60-related Spastic paraplegia | HSPD1 | 612233;605280 | 100994 | CANDIDATE -> SPG4 (0.947) |
| [ ] | 1022 | 11.3.08.02 | HSP60-related Hypomyelinating leukodystrophy type 4 | HSPD1 | 612233;605280 | 100994 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.899) |
| [ ] | 1023 | 11.3.09.01 | SACS-related Sacsin deficiency | SACS | 270550 | 98 | MAPPED -> Charlevoix-Saguenay spastic ataxia (alias_exact:autosomal recessive spastic ataxia of charlevoix saguenay) |
| [ ] | 1025 | 11.3.11.01 | SPG7-related Paraplegin deficiency | SPG7 | 607259 | 99013 | MAPPED -> SPG7 (alias_exact:spg7) |
| [ ] | 948 | 11.3.12.01 | FBXL4-related Mitochondrial DNA depletion syndrome type 13 | FBXL4 | 615471 | 369897 | CANDIDATE -> Mitochondrial (0.927) |
| [ ] | 1026 | 11.3.12.02 | HTRA2-related 3-Methylglutaconic aciduria type 8 | HTRA2 | 617248 | 505208 | UNMAPPED; weak candidate Glutaryl-CoA Dehydrogenase Deficiency (0.759) |
| [ ] | 1027 | 11.3.13.01 | PRKN-related Parkin deficiency | PRKN | 600116 | 2828 | UNMAPPED; weak candidate Parkinson's Disease (0.642) |
| [ ] | 1028 | 11.3.14.01 | PINK1-related Early-onset Parkinson disease type 6 | PINK1 | 605909 | 2828 | UNMAPPED; weak candidate Parkinson's Disease (0.642) |
| [ ] | 1029 | 11.3.15.01 | USP9X-related Mental retardation 99 | USP9X | 300919 | 480880 | UNMAPPED |
| [ ] | 1030 | 11.3.16.01 | VCP-related Valosin-containing protein superactivity | VCP | 167320 | 100070 | MAPPED -> Inclusion body myopathy with Paget disease of bone and frontotemporal dementia (identifier:OMIM:167320) |
| [ ] | 1198 | 11.3.17.01 | PITRM1-related Pitrilysin metallopeptidase 1 deficiency | PITRM1 | 618211 | - | UNMAPPED |
| [ ] | 1249 | 11.3.17.02 | CLPX-related Erythropoietic protoporphyria type 2 | CLPX | 618015 | - | UNMAPPED; weak candidate Erythropoietic Protoporphyria (0.892) |
| [ ] | 1197 | 11.3.18.01 | YME1L1-related Optic atrophy | YME1L1 | 617302 | - | UNMAPPED; weak candidate Spinal Muscular Atrophy (0.611) |
| [ ] | 1366 | 11.3.19.01 | HSPE1-rerlated Heat-shock protein 10KD | HSPE1 | 600141 | - | UNMAPPED; weak candidate RPA1 (0.533) |
| [ ] | 1721 | 11.3.20.01 | OXA1L-related Mitochondrial encephalopathy | OXA1L | 601066 | - | UNMAPPED; weak candidate COX11-Related COX Deficiency (0.800) |
| [ ] | 2177 | 11.3.21.01 | CRYAB-related Hereditary optic atrophy | CRYAB | 613869 | - | UNMAPPED; weak candidate Central Areolar Choroidal Dystrophy (0.561) |
| [ ] | 2237 | 11.3.22,01 | XRN1-related 5’-3’ Exoribonuclease deficiency | XRN1 | 607994 | - | UNMAPPED; weak candidate Reversible Infantile Cytochrome c Oxidase Deficiency (0.810) |

### WP-030: Miscellaneous disorders associated with mitochondrial dysfunction

- Classification: Intermediary Metabolism: Energy -> Other disorders of mitochondrial function
- Subgroup scope: Miscellaneous disorders associated with mitochondrial dysfunction
- Records: 18 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 16)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 590 | 11.4.01.01 | PPA2-related Mitochondrial inorganic pyrophosphatase 2 deficiency | PPA2 | 617222 | - | UNMAPPED |
| [ ] | 1003 | 11.4.2.01 | PTRH2-related Peptidyl-tRNA hydrolase 2 deficiency | PTRH2 | 616263 | - | UNMAPPED; weak candidate Cholesteryl Ester Storage Disease (0.651) |
| [ ] | 1031 | 11.4.02.01 | SFXN4-related Sideroflexin 4 deficiency | SFXN4 | 615578 | 391348 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.650) |
| [ ] | 442 | 11.4.03.01 | AIFM1-related X-Linked Mitochondrial Myopathy | AIFM1 | 300816 | 101078 | UNMAPPED; weak candidate DFNX5 (0.651) |
| [ ] | 1014 | 11.4.05.01 | GFER-related Myopathy, mitochondrial progressive, with congenital cataract, hearing loss, and developmental delay | GFER | 613076 | 330054 | UNMAPPED; weak candidate Lichtenstein-Knorr Syndrome (0.494) |
| [ ] | 1034 | 11.4.06.01 | C1QBP-related C1q binding protein deficiency | C1QBP | 617713 | - | CANDIDATE -> E3-binding protein deficiency (0.915) |
| [ ] | 402 | 11.4.09.01 | PRICKLE3-related Leber Hereditary Optic Neuropathy, LHON | PRICKLE3 | 535000 | - | UNMAPPED; weak candidate Congenital Insensitivity to Pain (0.642) |
| [ ] | 1037 | 11.4.09.02 | RTN4IP1-related Nogo-interacting mitochondrial protein deficiency | RTN4IP1 | 616732 | 98676 | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.691) |
| [ ] | 1467 | 11.4.12.01 | DIABLO-related Deafness, autosomal dominant 64 | DIABLO | 614152 | - | UNMAPPED; weak candidate DFNA13 (0.800) |
| [ ] | 1200 | 11.4.13.01 | TXNRD2-related Mitochondrial thioredoxin reductase 2 deficiency | TXNRD2 | 617825 | 361 | UNMAPPED; weak candidate Multiple Mitochondrial Dysfunctions Syndrome 9B (0.734) |
| [ ] | 1199 | 11.4.14.01 | TXN2-related Mitochondrial thioredoxin 2 deficiency | TXN2 | 616811 | 478029 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.762) |
| [ ] | 1722 | 11.4.21.1 | NME3-related Nucleoside diphosphate kinase 3 deficiency | NME3 | 601817 | - | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.667) |
| [ ] | 1769 | 11.4.22.01 | C2orf69-related Combined oxidative phosphorylation deficiency 53 | C2orf69 | 619423 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.693) |
| [ ] | 2044 | 11.4.23.01 | LETM1-related Leucine zipper/EF-hand-containing transmembrane protein 1  deficiency | LETM1 | 620089 | - | UNMAPPED |
| [ ] | 2132 | 11.4.24.01 | PRDX3-related Peroxiredoxin 3 deficiency | PRDX3 | 619871 | - | UNMAPPED; weak candidate CACD1 (0.521) |
| [ ] | 2133 | 11.4.25.01 | PYROXD2-related  Pyridine nucleotide-disulphide oxidoreductase domain-containing protein deficiency | PYROXD2 | 617889 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.582) |
| [ ] | 2140 | 11.4.26.01 | TRAP1-related TNF receptor deficiency | TRAP1 | 606219 | - | UNMAPPED; weak candidate TNF Receptor-Associated Periodic Syndrome (0.562) |
| [ ] | 2120 | 11.4.26701 | DMPK-related Dystrophia myotonica protein kinase deficiency | DMPK | 160900 | - | MAPPED -> Myotonic Dystrophy Type 1 (identifier:OMIM:160900) |

### WP-031: Disorders of mitochondrial metabolite repair + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Others -> Disorders of metabolite repair/proofreading
- Subgroup scope: Disorders of mitochondrial metabolite repair; Disorders of non-mitochondrial metabolite repair
- Records: 4 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 166 | 12.1.01.01 | D2HGDH-related D-2-Hydroxyglutarate dehydrogenase deficiency | D2HGDH | 600721 | 79315 | MAPPED -> D-2-Hydroxyglutaric Aciduria (identifier:ORPHA:79315) |
| [ ] | 165 | 12.1.02.01 | L2HGDH-related L-2-Hydroxyglutarate dehydrogenase deficiency | L2HGDH | 236792 | 79314 | MAPPED -> L-2-Hydroxyglutaric Aciduria (alias_exact:l 2 hydroxyglutaric aciduria) |
| [ ] | 577 | 12.1.22.01 | ACSF3-related Acyl-CoA-synthase 3 deficiency | ACSF3 | 614245 | 289504 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.847) |
| [ ] | 1154 | 12.2.07.01 | G6PC3-related Ubiquitous glucose-6-phosphatase deficiency (CDG) | G6PC3 | 612541 | 331176 | UNMAPPED; weak candidate GSD Ia (glucose-6-phosphatase deficiency) (0.791) |

### WP-032: Disorders of glyoxylate and oxalate metabolism + 1 adjacent subgroup(s)

- Classification: Intermediary Metabolism: Others -> Miscellaneous disorders of intermediary metabolism
- Subgroup scope: Disorders of glyoxylate and oxalate metabolism; Unassigned disorders of intermediary metabolism
- Records: 6 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 97 | 13.1.01.01 | GRHPR-related Glyoxylate reductase/hydroxypyruvate reductase deficiency | GRHPR | 260000 | - | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.853) |
| [ ] | 597 | 13.1.03.01 | HAO1-related Hydroxyacid oxidase 1 deficiency | HAO1 | 605023 | - | UNMAPPED; weak candidate TACO1-Related COX Deficiency (0.778) |
| [ ] | 1116 | 13.1.03.02 | SLC26A1-related Oxalate transporter deficiency | SLC26A1 | 167030 | - | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.848) |
| [ ] | 96 | 13.1.04.01 | AGXT-related Alanine-glyoxylate aminotransferase deficiency (peroxisomal) | AGXT | 259900 | - | UNMAPPED; weak candidate ornithine aminotransferase deficiency (0.688) |
| [ ] | 2020 | 13.1.05.01 | SLC26A6-related Hyperoxaluria and nephrolithiasis | SLC26A6 | 610068 | - | UNMAPPED; weak candidate Paratyphoid Fever (0.293) |
| [ ] | 1117 | 13.2.01.01 | CAT-related Catalase deficiency | CAT | 614097 | 926 | UNMAPPED |

### WP-033: Disorders of fatty acyl synthesis, elongation, and recycling + 1 adjacent subgroup(s)

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of fatty acyl synthesis, elongation, and recycling; Disorders of peroxisomal fatty acid oxidation
- Records: 21 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 657 | 14.1.01.01 | ALDH3A2-related Fatty aldehyde dehydrogenase deficiency | ALDH3A2 | 270200 | 816 | UNMAPPED; weak candidate Sjogren's Syndrome (0.857) |
| [ ] | 748 | 14.1.01.02 | ACSL4-related Long-chain fatty acid-CoA ligase 4 deficiency | ACSL4 | 300387 | 86818 | UNMAPPED; weak candidate Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (0.702) |
| [ ] | 1045 | 14.1.01.03 | MECR-related Mitochondrial enoyl-CoA reductase deficiency | MECR | 617282 | - | UNMAPPED; weak candidate MPAN (0.837) |
| [ ] | 1044 | 14.1.02.01 | ELOVL1-related Very long-chain fatty acid elongase 1 deficiency | ELOVL1 | 611813 | - | UNMAPPED; weak candidate Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (0.742) |
| [ ] | 1244 | 14.1.03.01 | ELOVL4-related Very long-chain fatty acid elongase 4 deficiency, neurologic recessive phenotype | ELOVL4 | 614457 | 352333 | UNMAPPED |
| [ ] | 1688 | 14.1.03.02 | ELOVL4-related Very long-chain fatty acid elongase 4 deficiency, neurologic dominant phenotype | ELOVL4 | 614457 | 133190 | UNMAPPED |
| [ ] | 1245 | 14.1.04.01 | ELOVL4-related Very long-chain fatty acid elongase 4 deficiency, retinal phenotype | ELOVL4 | 600110 | 352333 | UNMAPPED; weak candidate Stargardt Disease (0.829) |
| [ ] | 1246 | 14.1.05.01 | ELOVL5-related Very long-chain fatty acid elongase 5 deficiency | ELOVL5 | 615957 | 423296 | CANDIDATE -> SCA8 (0.983) |
| [ ] | 1207 | 14.1.06.01 | TECR-related Trans-2-enoyl-CoA reductase deficiency | TECR | 614020 | 88616 | UNMAPPED; weak candidate RCDP4 (0.773) |
| [ ] | 1206 | 14.1.07.01 | HACD1-related 3-Hydroxyacyl-CoA dehydratase 1 deficiency | HACD1 | 610467 | 2020 | UNMAPPED; weak candidate Long-chain 3-hydroxyacyl-CoA Dehydrogenase Deficiency (0.800) |
| [ ] | 1205 | 14.1.08.01 | ACACB-related Mitochondrial acetyl-CoA carboxylase 2 deficiency | ACACB | 601557 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.837) |
| [ ] | 1204 | 14.1.09.01 | ACACA-related Cytosolic acetyl-CoA carboxylase 1 deficiency | ACACA | 613933 | - | UNMAPPED; weak candidate Propionic Acidemia (0.765) |
| [ ] | 1723 | 14.1.10.01 | MCAT-related Mitochondrial malonyltransferase deficiency | MCAT | 620583 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.762) |
| [ ] | 2105 | 14.1.11.01 | ACSL5-related Long-chain fatty acid-CoA ligase 5 deficiency | ACSL5 | 620357 | - | UNMAPPED; weak candidate Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (0.702) |
| [ ] | 280 | 14.2.01.01 | ABCD1-related X-linked adrenoleukodystrophy and adrenomyeloneuropathy | ABCD1 | 300100 | 369942 | UNMAPPED; weak candidate adrenoleukodystrophy (0.690) |
| [ ] | 273 | 14.2.02.01 | ACOX1-related Peroxisomal straight-chain acyl-CoA oxidase deficiency | ACOX1 | 264470 | 2971 | UNMAPPED; weak candidate Peroxisomal Acyl-CoA Oxidase Deficiency (0.839) |
| [ ] | 274 | 14.2.03.01 | HSD17B4-related D-Bifunctional protein deficiency | HSD17B4 | 261515 | 300 | MAPPED -> D-Bifunctional Protein Deficiency (identifier:OMIM:261515) |
| [ ] | 1113 | 14.2.04.01 | EHHADH-related L-Bifunctional protein deficiency | EHHADH | 615605 | 3337 | MAPPED -> FRTS3 (alias_exact:frts3) |
| [ ] | 1114 | 14.2.05.01 | SCP2-related Sterol carrier protein-2 deficiency | SCP2 | 613724 | 163684 | UNMAPPED; weak candidate E3-binding protein deficiency (0.688) |
| [ ] | 281 | 14.2.06.01 | PHYH-related Phytanoyl-CoA hydroxylase deficiency | PHYH | 266500 | 773 | MAPPED -> Adult Refsum Disease (identifier:ORPHA:773) |
| [ ] | 2073 | 14.2.07.01 | ACOX1-related Peroxisomal straight-chain acyl-CoA superactivity deficiency | ACOX1 | 618960 | - | UNMAPPED; weak candidate Peroxisomal Acyl-CoA Oxidase Deficiency (0.687) |

### WP-034: Disorders of eicosanoid metabolism + 2 adjacent subgroup(s)

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of eicosanoid metabolism; Disorders of glycerolipid metabolism; Disorders of glycerophospholipid metabolism
- Records: 21 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 3, UNMAPPED 13)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 766 | 14.3.01.01 | TBXAS1-related Thromboxane synthase deficiency | TBXAS1 | 231095 | 1802 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.793) |
| [ ] | 767 | 14.3.02.01 | HPGD-related 15-Hydroxy-prostaglandin dehydrogenase deficiency | HPGD | 259100;119900;259100 | 217059 | CANDIDATE -> Primary Hypertrophic Osteoarthropathy (0.914) |
| [ ] | 768 | 14.3.03.01 | SLCO2A1-related Prostaglandin transporter deficiency | SLCO2A1 | 259100;119900;259100 | 468641 | CANDIDATE -> Primary Hypertrophic Osteoarthropathy (0.914) |
| [ ] | 1339 | 14.3.04.01 | PLA2G4A-related Cytosolic phospholipase A2α deficiency | PLA2G4A | 600522 | - | UNMAPPED; weak candidate Idiopathic Pulmonary Fibrosis (0.588) |
| [ ] | 137 | 14.3.05.01 | LTC4S-related Leukotriene C4 synthase deficiency | LTC4S | 246530 | 79507 | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.721) |
| [ ] | 1318 | 14.4.1.01 | BSCL2-related Seipin deficiency | BSCL2 | 615924;269700 | - | CANDIDATE -> Berardinelli-Seip Congenital Lipodystrophy (0.911) |
| [ ] | 749 | 14.4.02.01 | AGPAT2-related Lysophosphatidic acid acyltransferase deficiency | AGPAT2 | 608594 | 528 | MAPPED -> Berardinelli-Seip Congenital Lipodystrophy (identifier:ORPHA:528) |
| [ ] | 750 | 14.4.03.01 | LPIN1-related Lipin 1 deficiency | LPIN1 | 268200 | 99845 | UNMAPPED; weak candidate Autosomal Recessive Multiple Pterygium Syndrome (0.604) |
| [ ] | 1046 | 14.4.03.02 | AQP7-related Aquaporin 7 deficiency | AQP7 | 614411 | - | UNMAPPED; weak candidate Heart Failure with Mildly Reduced Ejection Fraction (HFmrEF) (0.577) |
| [ ] | 751 | 14.4.04.01 | LPIN2-related Lipin 2 deficiency | LPIN2 | 609628 | 77297 | UNMAPPED |
| [ ] | 2099 | 14.4.04.01 | DAGLA-related Diacylglycerol lipase-alpha deficiency | DAGLA | 168885 | - | UNMAPPED; weak candidate E1-alpha deficiency (0.632) |
| [ ] | 752 | 14.4.05.01 | DGAT1-related Diacylglycerol acyltransferase deficiency | DGAT1 | 615863 | 329242 | UNMAPPED; weak candidate Traveler's Diarrhea (0.500) |
| [ ] | 753 | 14.4.06.01 | ABHD5-related 1-Acylglycerol-3-phosphate O-acyltransferase deficiency | ABHD5 | 275630 | 98907 | AMBIGUOUS: 2 local entities (alias_exact:chanarin dorfman syndrome) |
| [ ] | 754 | 14.4.07.01 | PNPLA2-related Adipose triglyceride lipase deficiency | PNPLA2 | 610717 | 98908 | MAPPED -> Neutral Lipid Storage Myopathy (identifier:ORPHA:98908) |
| [ ] | 755 | 14.4.08.01 | PLIN1-related Perilipin 1 deficiency | PLIN1 | 613877 | 280356 | UNMAPPED; weak candidate Familial Partial Lipodystrophy (0.896) |
| [ ] | 756 | 14.4.09.01 | LIPE-related Hormone-sensitive lipase deficiency | LIPE | 615980 | 435660 | UNMAPPED; weak candidate Familial Partial Lipodystrophy (0.896) |
| [ ] | 1319 | 14.4.11.01 | BSCL2-related Seipin superactivity | BSCL2 | 600794;270685 | - | MAPPED -> Distal Hereditary Motor Neuronopathy, Autosomal Dominant (identifier:OMIM:270685) |
| [ ] | 1468 | 14.4.12.01 | PLIN5-related Perilipin 5 deficiency | PLIN5 | 613248 | - | UNMAPPED |
| [ ] | 2106 | 14.4.13.01 | PLIN4-rerlated Perilipin 4 deficiency | PLIN4 | 601846 | - | UNMAPPED; weak candidate Neurodegeneration With Brain Iron Accumulation (0.463) |
| [ ] | 1061 | 14.5.00.06 | OCRL-related Phosphatidylinositol 4,5-bisphosphate-5-phosphatase deficiency (Lowe syndrome) | OCRL | 309000 | 534 | MAPPED -> Lowe syndrome (alias_exact:lowe syndrome) |
| [ ] | 1436 | 14.5.00.07 | OCRL-related Phosphatidylinositol 4,5-bisphosphate-5-phosphatase deficiency (Dent disease type 2) | OCRL | 300555 | 534 | UNMAPPED |

### WP-035: Disorders of phosphatidylcholine, phosphatidylserine and phosphatidylethanolamine metabolism

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of phosphatidylcholine, phosphatidylserine and phosphatidylethanolamine metabolism
- Records: 25 (MAPPED 2, AMBIGUOUS 1, CANDIDATE 5, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2018 | 14.5.01.04 | ABHD16A-related Phosphatidylserine lipase deficiency ABHD16A | ABHD16A | 142620 | - | UNMAPPED; weak candidate Hereditary Spastic Paraplegia (0.879) |
| [ ] | 1291 | 14.5.01.05 | PCYT1A-related Phosphocholine cytidylyltransferase 1α deficiency, lipodystrophy phenotype | PCYT1A | 608940 | 85167 | UNMAPPED; weak candidate Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome (0.525) |
| [ ] | 622 | 14.5.01.06 | PCYT1A-related Phosphocholine cytidylyltransferase 1α deficiency, retinoskeletal phenotype | PCYT1A | 608940 | 85167 | UNMAPPED; weak candidate Spondyloepiphyseal Dysplasia Congenita (0.703) |
| [ ] | 1457 | 14.5.01.07 | PCYT2-related Phosphocholine cytidylyltransferase 2 deficiency | PCYT2 | 618770 | - | CANDIDATE -> Hereditary Spastic Paraplegia 48 (0.952) |
| [ ] | 759 | 14.5.01.08 | PTDSS1-related Phosphatidylserine synthase 1 superactivity | PTDSS1 | 151050 | 2658 | AMBIGUOUS: 2 local entities (alias_exact:lmhd) |
| [ ] | 1247 | 14.5.01.09 | ATP8A2-related Phosphatidylserine flippase deficiency | ATP8A2 | 615268 | 1766 | MAPPED -> CAMRQ4 (alias_exact:camrq4) |
| [ ] | 761 | 14.5.01.10 | DDHD1-related Phosphatidic acid-preferrin phospholipase 1 deficiency | DDHD1 | 609340 | 101008 | UNMAPPED; weak candidate CALFAN Syndrome (0.750) |
| [ ] | 762 | 14.5.01.11 | DDHD2-related Phosphatidic acid-preferrin phospholipase 2 deficiency | DDHD2 | 609340 | 320380 | UNMAPPED; weak candidate ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (0.738) |
| [ ] | 760 | 14.5.01.12 | PLA2G6-related Phospholipase A2 group 6 deficiency | PLA2G6 | 256600 | 35069 | MAPPED -> Neurodegeneration With Brain Iron Accumulation (alias_exact:neurodegeneration with brain iron accumulation) |
| [ ] | 763 | 14.5.01.13 | PNPLA6-related Spastic paraplegia type 39 | PNPLA6 | 215470;275400;612020 | 139480 | UNMAPPED; weak candidate Boucher-Neuhauser Syndrome (0.515) |
| [ ] | 764 | 14.5.01.14 | CYP2U1-related Spastic paraplegia 56 | CYP2U1 | 615030 | 320411 | CANDIDATE -> Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity (0.952) |
| [ ] | 1327 | 14.5.01.15 | LIPH-related Lipase H deficiency | LIPH | 604379 | - | UNMAPPED; weak candidate Isolated Woolly Hair (0.660) |
| [ ] | 1328 | 14.5.01.16 | LPAR6-related Lysophosphatidic acid receptor 6 deficiency | LPAR6 | 278150 | - | UNMAPPED; weak candidate Isolated Woolly Hair (0.559) |
| [ ] | 765 | 14.5.01.17 | ABHD12-related Polyneuropathy, hearing loss, ataxia, retinitis pigmentosa, and cataract (PHARC) syndrome | ABHD12 | 612674 | 171848 | UNMAPPED; weak candidate PHARC syndrome (0.526) |
| [ ] | 1048 | 14.5.01.18 | DGKE-related Diacylglycerol kinase ε deficiency | DGKE | 615008 | 357008 | CANDIDATE -> Atypical Hemolytic Uremic Syndrome (0.907) |
| [ ] | 1322 | 14.5.01.19 | MBOAT7-related Lysophosphatidylinositol acyltransferase 1 deficiency | MBOAT7 | 617188 | - | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.800) |
| [ ] | 1227 | 14.5.01.20 | SELENOI-related Ethanolaminephosphotransferase 1 deficiency | SELENOI | 607915 | 506353 | CANDIDATE -> SPG11 (0.952) |
| [ ] | 1335 | 14.5.01.21 | FAAH2-related Fatty acid amide hydrolase 2 deficiency | FAAH2 | 300654 | - | UNMAPPED; weak candidate RCDP4 (0.632) |
| [ ] | 2045 | 14.5.01.22 | CHKA-rerlated Choline kinase, alpha deficiency | CHKA | 620023 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.874) |
| [ ] | 2046 | 14.5.01.23 | ATP11A-related Phospholipid flippase deficiency | ATP11A | 619810 | - | UNMAPPED |
| [ ] | 2102 | 14.5.01.24 | ATP11C-related Flippase deficiency | ATP11C | 301015 | - | UNMAPPED; weak candidate Congenital Dyserythropoietic Anemia (0.820) |
| [ ] | 2103 | 14.5.01.25 | ANO6-related Anoctamin 6 deficiency | ANO6 | 262890 | - | UNMAPPED |
| [ ] | 1047 | 14.5.01.27 | CHKB-related Choline kinase β deficiency | CHKB | 602541 | 280671 | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.772) |
| [ ] | 1043 | 14.5.01.28 | MFSD2A-related Lysophosphatidylcholine-esterified long-chain fatty acid transporter deficiency | MFSD2A | 616486 | 2512 | CANDIDATE -> Autosomal Recessive Primary Microcephaly (0.909) |
| [ ] | 2232 | 14.5.01.29 | SPNS1-related Sphingolipid transporter 1 deficiency | SPNS1 | 612583 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.725) |

### WP-036: Disorders of phosphatidylinositol metabolism (part 1 of 2)

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of phosphatidylinositol metabolism
- Records: 22 (MAPPED 2, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1452 | 14.5.02.01 | FIG4-related Phosphatidylinositol 3,5-bisphosphate-5-phosphatase deficiency, neuroskeletal phenotype (CMT4J) | FIG4 | 611228 | 3472 | CANDIDATE -> CMT4 (0.986) |
| [ ] | 1451 | 14.5.02.02 | FIG4-related Phosphatidylinositol 3,5-bisphosphate-5-phosphatase deficiency, neuroskeletal phenotype (BTOP) | FIG4 | 612691 | 3472 | UNMAPPED; weak candidate TUBB2B (0.474) |
| [ ] | 1060 | 14.5.02.03 | FIG4-related Phosphatidylinositol 3,5-bisphosphate-5-phosphatase deficiency, neuroskeletal phenotype (YVS) | FIG4 | 216340 | 3472 | UNMAPPED; weak candidate Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome (0.448) |
| [ ] | 1059 | 14.5.02.04 | FIG4-related Phosphatidylinositol 3,5-bisphosphate-5-phosphatase deficiency, neurologic phenotype (ALS11) | FIG4 | 612577;611228 | 208441 | UNMAPPED; weak candidate Amyotrophic Lateral Sclerosis (0.879) |
| [ ] | 1062 | 14.5.02.05 | SYNJ1-related Synaptojanin 1 deficiency (EIEE53) | SYNJ1 | 617389 | 442835 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.755) |
| [ ] | 1437 | 14.5.02.06 | SYNJ1-related Synaptojanin 1 deficiency (EOPD20) | SYNJ1 | 615530 | 442835 | UNMAPPED; weak candidate Early-Onset Alzheimer's Disease (0.676) |
| [ ] | 1771 | 14.5.02.06 | PLCH1-related Holoprosencephaly | PLCH1 | 612835 | - | CANDIDATE -> SHH_Holoprosencephaly_Spectrum (0.944) |
| [ ] | 1063 | 14.5.02.07 | MTM1-related Myotubularin 1 deficiency | MTM1 | 310400 | 596 | MAPPED -> XLMTM (alias_exact:x linked myotubular myopathy) |
| [ ] | 2022 | 14.5.02.07 | PLCH1-related Phospholipase C, ETA-1 deficiency | PLCH1 | 612835 | - | UNMAPPED |
| [ ] | 1064 | 14.5.02.08 | MTMR2-related Myotubularin-related protein 2 deficiency | MTMR2 | 601382 | 99955 | CANDIDATE -> CMT1 (0.971) |
| [ ] | 1065 | 14.5.02.09 | SBF2-related Myotubularin-related protein 2 regulatory protein deficiency | SBF2 | 604563 | 99956 | CANDIDATE -> CMT2 (0.971) |
| [ ] | 1067 | 14.5.02.10 | PIK3CA-related Catalytic phosphatidylinositol 3-kinase α subunit superactivity | PIK3CA | 171834 | 99802 | UNMAPPED |
| [ ] | 1068 | 14.5.02.11 | PIK3CD-related Catalytic phosphatidylinositol 3-kinase δ subunit superactivity | PIK3CD | 615513 | 397596 | UNMAPPED; weak candidate Activated PI3K-delta syndrome (0.541) |
| [ ] | 1069 | 14.5.02.12 | PIK3R1-related Phosphatidylinositol 3-kinase regulatory subunit 1 deficiency | PIK3R1 | 269880;616005 | 3163 | UNMAPPED; weak candidate Activated PI3K-delta syndrome (0.571) |
| [ ] | 1070 | 14.5.02.13 | PIK3R2-related Phosphatidylinositol 3-kinase regulatory subunit 2 superactivity | PIK3R2 | 603387 | 83473 | UNMAPPED; weak candidate Brachyphalangy-Polydactyly-Tibial Aplasia Syndrome (0.545) |
| [ ] | 1456 | 14.5.02.14 | VAC14-related deficiency type 1, neonatal | VAC14 | 216340 | - | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.588) |
| [ ] | 1453 | 14.5.02.15 | VAC14-related Lenk-Ploski syndrome | VAC14 | 617054 | - | UNMAPPED; weak candidate Autosomal dominant striatal neurodegeneration (0.610) |
| [ ] | 1071 | 14.5.02.16 | PIKFYVE-related Phosphatidylinositol-3-phosphate 5-kinase deficiency | PIKFYVE | 121850 | 98970 | UNMAPPED; weak candidate Cone-Rod Dystrophy (0.732) |
| [ ] | 1072 | 14.5.02.17 | PIP5K1C-related Phosphatidylinositol 4-phosphate 5-kinase deficiency | PIP5K1C | 611369 | 137783 | UNMAPPED; weak candidate LCCS (0.884) |
| [ ] | 1073 | 14.5.02.18 | PTEN-related Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase deficiency | PTEN | 158350 | 306498 | AMBIGUOUS: 4 local entities (identifier:ORPHA:306498) |
| [ ] | 2029 | 14.5.02.19 | PIK3CG-related Immunodeficiency 97 with autoinflammation | PIK3CG | 619802 | - | UNMAPPED; weak candidate IKBKG ectodermal dysplasia with immunodeficiency (0.650) |
| [ ] | 1074 | 14.5.02.20 | INPPL1-related Phosphatidylinositol 3,4,5-trisphosphate 5-phosphatase deficiency | INPPL1 | 258480 | 2746 | MAPPED -> Opsismodysplasia (alias_exact:opsismodysplasia) |

### WP-037: Disorders of phosphatidylinositol metabolism (part 2 of 2)

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of phosphatidylinositol metabolism
- Records: 16 (MAPPED 1, AMBIGUOUS 1, CANDIDATE 2, UNMAPPED 12)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1075 | 14.5.02.21 | INPP5E-related Inositol polyphosphate 5-phosphatase deficiency | INPP5E | 213300;610156 | 75858 | UNMAPPED; weak candidate Joubert syndrome (0.821) |
| [ ] | 1076 | 14.5.02.22 | PLCB1-related Phosphatidylinositol 4,5-bisphosphate phospholipase C β1 deficiency | PLCB1 | 613722 | 293181 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 1077 | 14.5.02.23 | PLCB4-related Phosphatidylinositol 4,5-bisphosphate phospholipase C β4 deficiency | PLCB4 | 614669 | 137888 | AMBIGUOUS: 2 local entities (identifier:OMIM:614669) |
| [ ] | 1438 | 14.5.02.24 | PLCG2-related Phosphatidylinositol 4,5-bisphosphate phospholipase C γ2 deficiency (APLAID) | PLCG2 | 614878 | 300359 | UNMAPPED |
| [ ] | 1078 | 14.5.02.25 | PLCG2-related Phosphatidylinositol 4,5-bisphosphate phospholipase C γ2 deficiency (FCAS3) | PLCG2 | 614468 | 300359 | CANDIDATE -> Familial Cold Autoinflammatory Syndrome (0.918) |
| [ ] | 1079 | 14.5.02.26 | PLCD1-related Phosphatidylinositol 4,5-bisphosphate phospholipase C δ1 deficiency | PLCD1 | 151600 | 2387 | UNMAPPED; weak candidate Familial Thoracic Aortic Aneurysm and Aortic Dissection (0.600) |
| [ ] | 1080 | 14.5.02.27 | PLCE1-related Phosphatidylinositol 4,5-bisphosphate phospholipase C ε1 deficiency | PLCE1 | 610725 | 93213 | UNMAPPED; weak candidate Galloway-Mowat syndrome (0.514) |
| [ ] | 1461 | 14.5.02.28 | PI4K2A-related Phosphatidylinositol 4‐kinase type 2‐alpha deficiency | PI4K2A | 609763 | - | UNMAPPED; weak candidate E1-alpha deficiency (0.611) |
| [ ] | 1309 | 14.5.02.29 | INPP5K-related Inositol polyphosphate 5-phosphatase K deficiency | INPP5K | 617404 | - | UNMAPPED; weak candidate Type B (Congenital muscular dystrophy with intellectual disability) (0.847) |
| [ ] | 1469 | 14.5.02.30 | PIK3C2A-related Phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha deficiency | PIK3C2A | 618440 | 557003 | MAPPED -> Oculocerebrodental Syndrome (identifier:OMIM:618440) |
| [ ] | 1471 | 14.5.02.31 | PI4KA-related Phosphatidylinositol 4-kinase type 3 alpha deficiency | PI4KA | 616531 | 98889 | UNMAPPED; weak candidate E1-alpha deficiency (0.611) |
| [ ] | 1215 | 14.5.02.32 | ITPR2-related Inositol 1,4,5-triphosphate receptor type 2 deficiency | ITPR2 | 106190 | 468666 | UNMAPPED; weak candidate COQ6 (0.562) |
| [ ] | 1214 | 14.5.02.33 | PLCB3-related Phosphatidylinositol 4,5-bisphosphate phospholipase C β3 deficiency | PLCB3 | 600230 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.696) |
| [ ] | 1213 | 14.5.02.34 | PIK3R5-related Phosphatidylinositol 4,5-bisphosphate 3-kinase regulatory subunit deficiency | PIK3R5 | 615217 | 64753 | UNMAPPED; weak candidate AOA1 (0.899) |
| [ ] | 1066 | 14.5.02.35 | SBF1-related Myotubularin-related protein 2 activator deficiency | SBF1 | 615284 | 363981 | CANDIDATE -> CMT4 (0.971) |
| [ ] | 1081 | 14.5.02.36 | ITPR1-related Inositol 1,4,5-triphosphate receptor type 1 deficiency | ITPR1 | 606658 | 98769 | UNMAPPED; weak candidate Autosomal Dominant Cerebellar Ataxia Type III (0.712) |

### WP-038: Disorders of ether lipid metabolism + 1 adjacent subgroup(s)

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of ether lipid metabolism; Disorders of sphingolipid synthesis and recycling
- Records: 31 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 11, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 277 | 14.5.03.01 | PEX7-related Peroxisomal targeting signal 2 receptor deficiency | PEX7 | 215100 | 309789 | MAPPED -> Rhizomelic Chondrodysplasia Punctata Type 1 (alias_exact:rcdp1) |
| [ ] | 278 | 14.5.03.02 | GNPAT-related Glycerone 3-phosphate acyltransferase deficiency | GNPAT | 602744 | 309796 | MAPPED -> RCDP2 (alias_exact:rcdp2) |
| [ ] | 279 | 14.5.03.03 | AGPS-related Alkylglycerone 3-phosphate synthase deficiency | AGPS | 600121 | 309803 | MAPPED -> RCDP3 (alias_exact:rcdp3) |
| [ ] | 1111 | 14.5.03.04 | FAR1-related Fatty Acyl-CoA reductase 1deficiency | FAR1 | 616154 | 438178 | CANDIDATE -> RCDP4 (0.986) |
| [ ] | 1691 | 14.5.03.05 | FAR1-related Fatty Acyl-CoA reductase superactivity | FAR1 | 616107 | 438178 | UNMAPPED; weak candidate RCDP4 (0.773) |
| [ ] | 1472 | 14.5.03.06 | AGMO-related Alkylglycerol monooxygenase deficiency | AGMO | 613738 | - | UNMAPPED |
| [ ] | 1049 | 14.6.01.01 | SPTLC1-related Serine palmitoyltransferase subunit 1 deficiency | SPTLC1 | 162400 | 36386 | CANDIDATE -> HSAN IV (0.970) |
| [ ] | 1394 | 14.6.1.01 | SGMS2-related Sphingomyelin synthase 2 deficiency | SGMS2 | 611574 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.781) |
| [ ] | 1050 | 14.6.02.01 | SPTLC2-related Serine palmitoyltransferase subunit 2 deficiency | SPTLC2 | 613640 | 36386 | UNMAPPED |
| [ ] | 1208 | 14.6.2.01 | CERS1-related Ceramide synthase 1 deficiency | CERS1 | 616230 | 424027 | UNMAPPED; weak candidate Progressive Myoclonus Epilepsy (0.896) |
| [ ] | 1051 | 14.6.03.01 | CERS3-related Ceramide synthase 3 deficiency | CERS3 | 615023 | 79394 | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.921) |
| [ ] | 1052 | 14.6.04.01 | CYP4F22-related Omega hydroxylase deficiency | CYP4F22 | 604777 | 313 | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.921) |
| [ ] | 1212 | 14.6.04.02 | HHAT-related Hedgehog acyltransferase deficiency | HHAT | 608116 | - | UNMAPPED; weak candidate Hedgehog-high Subtype (0.393) |
| [ ] | 1434 | 14.6.04.03 | SDR9C7-related Short-chain dehydrogenase-reductase 9C deficiency | SDR9C7 | 617574 | - | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.965) |
| [ ] | 1053 | 14.6.05.01 | GBA2-related Nonlysosomal glucosylceramidase deficiency | GBA2 | 614409 | 320391 | MAPPED -> Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity (alias_exact:spg46) |
| [ ] | 1301 | 14.6.05.03 | PNPLA1-related Acylceramide transacylase deficiency | PNPLA1 | 615024 | - | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.911) |
| [ ] | 1054 | 14.6.06.01 | FA2H-related Fatty acid 2-hydroxylase deficiency | FA2H | 612319 | 171629 | UNMAPPED; weak candidate AR Complex HSP (0.738) |
| [ ] | 1042 | 14.6.07.01 | SLC27A4-related Fatty acid transport protein 4 deficiency | SLC27A4 | 608649 | 88621 | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.712) |
| [ ] | 1055 | 14.6.07.02 | SGPL1-related Sphingosine-1-phosphate lyase deficiency | SGPL1 | 617575 | 506334 | UNMAPPED; weak candidate Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (0.738) |
| [ ] | 1435 | 14.6.11.01 | ABCA12-related lipid transporter deficiency | ABCA12 | 601277 | - | UNMAPPED; weak candidate Inherited Ichthyosis (0.808) |
| [ ] | 1432 | 14.6.12.01 | ALOX12B-related Arachinodate 12R-lipoxygenase deficiency | ALOX12B | 242100 | - | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.976) |
| [ ] | 1433 | 14.6.13.01 | ALOXE3-related Arachidonate lipoxygenase 3 deficiency | ALOXE3 | 242100 | - | UNMAPPED |
| [ ] | 1687 | 14.6.13.02 | LIPN-related Lipase N deficiency | LIPN | 613943 | - | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.976) |
| [ ] | 1458 | 14.6.14.01 | DEGS1-related Sphingolipid-1-delta (4)-desaturase deficiency | DEGS1 | 618404 | - | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.596) |
| [ ] | 1431 | 14.6.15.01 | KDSR-related 3-Ketodihydrosphingosine reductase deficiency | KDSR | 617526 | 316;317 | CANDIDATE -> Erythrokeratodermia Variabilis (0.978) |
| [ ] | 1248 | 14.6.17.01 | UGCG-related UDP-glucose ceramide glucosyltransferase deficiency | UGCG | 602874 | 281097 | AMBIGUOUS: 2 local entities (alias_exact:autosomal recessive congenital ichthyosis) |
| [ ] | 1210 | 14.6.18.01 | ACER3-related Alkaline ceramidase 3 deficiency | ACER3 | 617762 | 502444 | UNMAPPED; weak candidate Farber Disease (0.828) |
| [ ] | 1209 | 14.6.19.01 | CERS2-related Ceramide synthase 2 deficiency | CERS2 | 606920 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.814) |
| [ ] | 1724 | 14.6.21.01 | SPNS2-related Sphingosine-1-phosphate transporter deficiency | SPNS2 | 618457 | - | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.842) |
| [ ] | 2054 | 14.6.22.01 | SPTSSA-related Serine palmitoyltransferase, small subunit A deficiency | SPTSSA | 613540 | - | CANDIDATE -> Complex Hereditary Spastic Paraplegia (0.914) |
| [ ] | 2060 | 14.6.23.01 | TLCD3B-related  Cone-rod dystrophy 22 | TLCD3B | 619531 | - | CANDIDATE -> Cone-Rod Dystrophy (0.923) |

### WP-039: Disorders of sterol biosynthesis

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of sterol biosynthesis
- Records: 20 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 191 | 14.7.01.01 | MVK-related Mevalonate kinase deficiency (mild) | MVK | 260920 | 343 | MAPPED -> HIDS (alias_exact:hids) |
| [ ] | 193 | 14.7.1.01 | EBP-related Chondrodysplasia punctata 2 | EBP | 302960 | 79255 | UNMAPPED; weak candidate Rhizomelic Chondrodysplasia Punctata Type 1 (0.795) |
| [ ] | 513 | 14.7.01.02 | MVK-related Mevalonate kinase deficiency, severe | MVK | 610377 | 309025 | MAPPED -> Mevalonic Aciduria (alias_exact:mevalonic aciduria) |
| [ ] | 674 | 14.7.03.01 | PMVK-related Phosphomevalonate kinase deficiency | PMVK | 175800 | 735 | UNMAPPED; weak candidate Mevalonate Kinase Deficiency (0.889) |
| [ ] | 675 | 14.7.04.01 | MVD-related Mevalonate pyrophosphate decarboxylase deficiency | MVD | 614714 | 79152 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.690) |
| [ ] | 676 | 14.7.05.01 | FDPS-related Farnesylpyrophosphate synthetase deficiency | FDPS | 616631 | 79152 | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.814) |
| [ ] | 197 | 14.7.06.01 | LBR-related Sterol C14 reductase deficiency | LBR | 215140 | 1426 | UNMAPPED; weak candidate Sepiapterin reductase deficiency (0.794) |
| [ ] | 317 | 14.7.07.01 | MSMO1-related Sterol C4-methyloxidase deficiency | MSMO1 | 607545 | 488168 | UNMAPPED; weak candidate Cerebrotendinous xanthomatosis (0.788) |
| [ ] | 194 | 14.7.08.01 | NSDHL-related CHILD syndrome | NSDHL | 308050 | 139 | UNMAPPED; weak candidate Congenital Ichthyosiform Erythroderma (0.673) |
| [ ] | 515 | 14.7.09.01 | NSDHL-related CK syndrome, recessive | NSDHL | 300831 | 251383 | UNMAPPED; weak candidate Wieacker-Wolff Syndrome (0.667) |
| [ ] | 514 | 14.7.11.01 | EBP-related Chondrodysplasia punctata 2, recessive | EBP | 302960 | 35173 | UNMAPPED; weak candidate Rhizomelic Chondrodysplasia Punctata Type 1 (0.741) |
| [ ] | 196 | 14.7.12.01 | SC5D-related Lathosterolosis | SC5D | 607330 | 46059 | UNMAPPED; weak candidate Cerebrotendinous xanthomatosis (0.762) |
| [ ] | 195 | 14.7.13.01 | DHCR24-related Desmosterolosis | DHCR24 | 602398 | 35107 | UNMAPPED; weak candidate 3B-HSD (0.800) |
| [ ] | 192 | 14.7.14.01 | DHCR7-related Smith-Lemli-Opitz syndrome | DHCR7 | 270400 | 818 | MAPPED -> Smith-Lemli-Opitz syndrome (alias_exact:slos) |
| [ ] | 1329 | 14.7.16.01 | LSS-related Lanostherol synthase deficiency | LSS | 616509 | - | UNMAPPED; weak candidate GM3 synthase deficiency (0.741) |
| [ ] | 1302 | 14.7.17.01 | FDFT1-related Squalene synthase deficiency | FDFT1 | 184420 | - | UNMAPPED; weak candidate GM3 synthase deficiency (0.784) |
| [ ] | 1216 | 14.7.18.01 | GGPS1-related Geranylgeranyl pyrophosphate synthase deficiency | GGPS1 | 606982 | - | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.764) |
| [ ] | 318 | 14.7.19.01 | CYP51A1-related Lanosterol demethylase deficiency | CYP51A1 | 601637 | - | UNMAPPED; weak candidate COA3-Related COX Deficiency (0.716) |
| [ ] | 2055 | 14.7.20.01 | HMGCR-related 3-Hydroxy-3-methylglutaryl-CoA reductase deficiency | HMGCR | 620375 | - | CANDIDATE -> 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.911) |
| [ ] | 2190 | 14.7.21.01 | HMGCS1-related Rigid spine syndrome | HMGCS1 | 142940 | - | CANDIDATE -> 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.935) |

### WP-040: Disorders of bile acid metabolism

- Classification: Lipid Metabolism and Transport -> Disorders of lipid metabolism
- Subgroup scope: Disorders of bile acid metabolism
- Records: 18 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 11)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 179 | 14.8.01.01 | HSD3B7-related 3β-Hydroxy-Δ5-C27-steroid dehydrogenase-isomerase deficiency | HSD3B7 | 607764 | 79301 | UNMAPPED; weak candidate BASD Type 1 (0.744) |
| [ ] | 182 | 14.8.1.01 | CYP7A1-related Cholesterol 7α-hydroxylase deficiency | CYP7A1 | 118455 | 209902 | CANDIDATE -> BASD Type 3 (0.914) |
| [ ] | 180 | 14.8.02.01 | AKR1D1-related Δ4-3-Oxosteroid-5β-reductase deficiency | AKR1D1 | 604741 | 79303 | CANDIDATE -> BASD Type 2 (0.932) |
| [ ] | 181 | 14.8.03.01 | CYP7B1-related Oxysterol 7α-hydroxylase deficiency | CYP7B1 | 603711 | 100986 | CANDIDATE -> BASD Type 3 (0.987) |
| [ ] | 185 | 14.8.04.01 | ATP8B1-related Progressive familial intrahepatic cholestasis type 1 | ATP8B1 | 211600 | 79306 | UNMAPPED; weak candidate Type 1A (0.717) |
| [ ] | 183 | 14.8.04.02 | CYP27A1-related Sterol 27-hydroxylase deficiency | CYP27A1 | 213700 | 909 | MAPPED -> Cerebrotendinous xanthomatosis (identifier:OMIM:213700) |
| [ ] | 186 | 14.8.05.01 | ABCB11-related Progressive familial intrahepatic cholestasis type 2 | ABCB11 | 603201 | 79304 | UNMAPPED; weak candidate Type 1A (0.696) |
| [ ] | 188 | 14.8.05.02 | AMACR-related Alpha-Methylacyl-CoA racemase deficiency | AMACR | 604489 | 79095 | MAPPED -> BASD Type 4 (alias_exact:alpha methylacyl coa racemase deficiency) |
| [ ] | 552 | 14.8.06.01 | ABCB4-related Progressive familial intrahepatic cholestasis type 3 | ABCB4 | 602347 | 79305 | UNMAPPED; weak candidate Type 1A (0.696) |
| [ ] | 660 | 14.8.06.02 | ACOX2-related Congenital bile acid synthesis defect | ACOX2 | 617308 | - | MAPPED -> Inborn Disorder of Bile Acid Synthesis (alias_exact:congenital bile acid synthesis defect) |
| [ ] | 187 | 14.8.07.01 | BAAT-related Bile acid-CoA:aminoacid N-acyl transferase deficiency | BAAT | 602938 | 238475 | UNMAPPED; weak candidate Bile acid conjugation defect 1 (0.812) |
| [ ] | 662 | 14.8.07.02 | NR1H4-related Progressive familial intrahepatic cholestasis 5 NR1H4 | NR1H4 | 617049 | 69665 | UNMAPPED; weak candidate Progressive Familial Heart Block (0.612) |
| [ ] | 659 | 14.8.08.01 | ABCD3-related Congenital bile acid synthesis defect | ABCD3 | 616278 | - | MAPPED -> Inborn Disorder of Bile Acid Synthesis (alias_exact:congenital bile acid synthesis defect) |
| [ ] | 1228 | 14.8.08.02 | SLC10A1-related Sodium-taurocholate cotransporting polypeptide (NTCP) deficiency | SLC10A1 | 182396 | - | UNMAPPED; weak candidate SCN1B-related (0.321) |
| [ ] | 184 | 14.8.09.01 | SLC27A5-related Bile acid-CoA ligase deficiency | SLC27A5 | 603314 | 276066 | UNMAPPED; weak candidate Bile acid conjugation defect 1 (0.623) |
| [ ] | 1099 | 14.8.09.02 | SLC10A2-related Apical bile salt transporter deficiency | SLC10A2 | 613291 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.761) |
| [ ] | 1772 | 14.8.11.01 | SLC51A-related  Cholestasis, progressive familial intrahepatic, 6 | SLC51A | 619484 | - | UNMAPPED; weak candidate Progressive Familial Heart Block (0.658) |
| [ ] | 1773 | 14.8.12.01 | SLC51B-related Bile acid malabsorption, primary, 2 | SLC51B | 619481 | - | UNMAPPED; weak candidate Bile acid conjugation defect 1 (0.540) |

### WP-041: Hypercholesterolemias + 2 adjacent subgroup(s)

- Classification: Lipid Metabolism and Transport -> Disorders of lipoprotein metabolism
- Subgroup scope: Hypercholesterolemias; Hypertriglyceridemias; Mixed hyperlipidemias
- Records: 22 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 367 | 15.1.01.01 | LDLR-related Familial hypercholesterolemia heterozygous (LDLR) | LDLR | 143890;606945 | 391665 | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.763) |
| [ ] | 527 | 15.1.01.02 | LDLR-related Familial hypercholesterolemia homozygous | LDLR | 143890;606945 | 391665 | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.841) |
| [ ] | 370 | 15.1.02.01 | LDLRAP1-related Autosomal recessive hypercholesterolemia (ARH) | LDLRAP1 | 603813;605747 | 391665 | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.685) |
| [ ] | 368 | 15.1.03.01 | APOB-related Familial defective apolipoprotein B | APOB | 144010 | 391665 | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.667) |
| [ ] | 372 | 15.1.04.01 | APOB-related Apolipoprotein B deficiency | APOB | 144010;605019 | 391665 | MAPPED -> Abetalipoproteinemia (identifier:OMIM:605019) |
| [ ] | 369 | 15.1.05.01 | PCSK9-related Proprotein convertase superactivity | PCSK9 | 603776;607786 | 391665 | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.667) |
| [ ] | 373 | 15.1.06.01 | PCSK9-related  Proprotein convertase deficiency with low LDL | PCSK9 | 607786;613589 | 391665 | UNMAPPED |
| [ ] | 1082 | 15.1.07.01 | STAP1-related Familial hypercholesterolemia type 4 | STAP1 | 604298 | - | UNMAPPED; weak candidate Familial Hypercholesterolemia (0.892) |
| [ ] | 508 | 15.1.08.01 | ABCG5-related Sitosterolemia | ABCG5 | 210250 | 2882 | UNMAPPED |
| [ ] | 1276 | 15.1.09.01 | ABCG8-related Sitosterolemia | ABCG8 | 210250;611465 | 2882 | UNMAPPED |
| [ ] | 1085 | 15.2.2.01 | LMF1-related Lipase maturation factor 1 deficiency | LMF1 | 246650 | 444490 | UNMAPPED |
| [ ] | 381 | 15.2.16.01 | LPL-related Lipoprotein lipase deficiency | LPL | 609708;238600 | 411 | UNMAPPED |
| [ ] | 1001 | 15.2.16.02 | GARS-related Mitochondrial and cytoplasmic glycil-tRNA synthetase deficiency | GARS | 601472;600794 | 99938 | MAPPED -> Distal Hereditary Motor Neuronopathy, Autosomal Dominant (identifier:OMIM:601472) |
| [ ] | 505 | 15.2.17.01 | APOC2-related Apolipoprotein C-II deficiency | APOC2 | 608083;207750 | 309020 | UNMAPPED |
| [ ] | 1084 | 15.2.18.01 | GPIHBP1-related  Hyperlipoproteinemia type 1D | GPIHBP1 | 615947 | 444490 | UNMAPPED |
| [ ] | 1086 | 15.2.21.01 | APOA5-related Apolipoprotein A5 deficiency | APOA5 | 144650 | 70470 | UNMAPPED |
| [ ] | 1762 | 15.2.22.01 | CREB3L3-related Hypertriglyceridemia 2 | CREB3L3 | 619324 | - | CANDIDATE -> Hypertriglyceridemia (0.952) |
| [ ] | 507 | 15.3.13.01 | APOE-related Apolipoprotein E deficiency | APOE | 617347 | 412 | UNMAPPED |
| [ ] | 1292 | 15.3.14.01 | APOE-related Apolipoprotein E superactivity | APOE | 269600 | 412 | MAPPED -> Sea-Blue Histiocyte Syndrome (alias_exact:inherited lipemic splenomegaly) |
| [ ] | 1293 | 15.3.15.01 | APOE-related Lipoprotein glomerulopathy | APOE | 611771 | 412 | UNMAPPED |
| [ ] | 376 | 15.3.19.01 | LIPC-related Hepatic lipase deficiency | LIPC | 612797;614025 | 140905 | UNMAPPED; weak candidate Hepatic veno-occlusive disease-immunodeficiency syndrome (0.623) |
| [ ] | 506 | 15.3.20.01 | USF1-related Familial combined hyperlipidemia | USF1 | 144250;602491 | - | MAPPED -> Familial Combined Hyperlipidemia (alias_exact:familial combined hyperlipidemia) |

### WP-042: Disorders of high-density lipoprotein (HDL) metabolism + 2 adjacent subgroup(s)

- Classification: Lipid Metabolism and Transport -> Disorders of lipoprotein metabolism
- Subgroup scope: Disorders of high-density lipoprotein (HDL) metabolism; Disorders with decreased low-density lipoprotein (LDL) and/or triglycerides; Other disorders of lipoprotein metabolism
- Records: 15 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 377 | 15.4.3.01 | SCARB1-related Scavenger receptor B1 deficiency | SCARB1 | 601040;610762 | - | UNMAPPED; weak candidate Luminal Androgen Receptor (LAR) TNBC (0.484) |
| [ ] | 380 | 15.4.22.01 | LCAT-related Familial lecithin cholesterol acyl transferase deficiency | LCAT | 606967;245900 | 79292 | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.709) |
| [ ] | 528 | 15.4.22.02 | LCAT-related Familial Lecithin cholesterol acyl transferase deficiency (partial) | LCAT | 136120;606967 | 79292 | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.596) |
| [ ] | 378 | 15.4.23.01 | ABCA1-related Tangier disease | ABCA1 | 600046;205400 | 31150 | MAPPED -> Tangier_Disease (identifier:OMIM:205400) |
| [ ] | 379 | 15.4.24.01 | APOA1-related Apolipoprotein A-I deficiency | APOA1 | 107680 | 93560 | UNMAPPED |
| [ ] | 1294 | 15.4.25.01 | APOA1-related Hereditary apolipoprotein A1-related amyloidosis | APOA1 | 105200 | 93560 | MAPPED -> Amyloidosis (alias_exact:amyloidosis) |
| [ ] | 375 | 15.4.26.01 | CETP-related Cholesteryl ester transfer protein deficiency | CETP | 607322;143470 | 79506 | UNMAPPED; weak candidate Cholesteryl Ester Storage Disease (0.674) |
| [ ] | 1087 | 15.4.27.01 | APOC3-related Apolipoprotein C3 deficiency | APOC3 | 614028 | 79506 | UNMAPPED |
| [ ] | 374 | 15.5.1.01 | ANGPTL3-related Angiopoietin-like 3 deficiency | ANGPTL3 | 605019;604774 | - | MAPPED -> Abetalipoproteinemia (identifier:OMIM:605019) |
| [ ] | 371 | 15.5.11.01 | MTTP-related Microsomal triglyceride transfer protein deficiency | MTTP | 200100;157147 | 14 | MAPPED -> Abetalipoproteinemia (identifier:OMIM:200100) |
| [ ] | 1083 | 15.5.12.01 | SAR1B-related Chylomicron retention disease | SAR1B | 246700 | 71 | UNMAPPED |
| [ ] | 2101 | 15.6.28.01 | LSR-related Lipolysis-stimulated lipoprotein receptor deficiency | LSR | 616582 | - | UNMAPPED; weak candidate Infantile hepatic form (0.679) |
| [ ] | 1474 | 15.6.29.01 | VLDLR-related Very low-density lipoprotein receptor deficiency | VLDLR | 224050 | 1766 | MAPPED -> CAMRQ1 (alias_exact:camrq1) |
| [ ] | 509 | 15.6.31.01 | LPA-related Elevated Lipoprotein(a) | LPA | 152200 | 250831 | UNMAPPED; weak candidate Tangier_Disease (0.536) |
| [ ] | 2227 | 15.6.32.01 | LRP4-related Myasthenic syndrome | LRP4 | 616304 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.776) |

### WP-043: Disorders of pyrimidine metabolism + 1 adjacent subgroup(s)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of pyrimidine metabolism; Disorders of purine metabolism
- Records: 41 (MAPPED 6, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 32)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 159 | 16.1.01.01 | DPYD-related Dihydropyrimidine dehydrogenase deficiency | DPYD | 274270;612779 | 1675 | UNMAPPED |
| [ ] | 1476 | 16.1.1.01 | CTPS1-related CTP synthase 1 deficiency | CTPS1 | 615897 | 420573 | UNMAPPED; weak candidate GM3 synthase deficiency (0.833) |
| [ ] | 623 | 16.1.01.02 | CAD-related Trifunctional protein deficiency (CDG) | CAD | 616457 | 448010 | CANDIDATE -> Mitochondrial Trifunctional Protein Deficiency (0.941) |
| [ ] | 155 | 16.1.02.01 | DHODH-related Dihydroorotate dehydrogenase deficiency | DHODH | 263750;126064 | 246 | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.833) |
| [ ] | 268 | 16.1.02.02 | DPYS-related Dihydropyrimidinase deficiency | DPYS | 222748;613326 | 38874 | UNMAPPED |
| [ ] | 152 | 16.1.03.01 | UMPS-related Uridine monophosphate synthase deficiency | UMPS | 258900 | 30 | MAPPED -> Hereditary Orotic Aciduria (identifier:OMIM:258900) |
| [ ] | 160 | 16.1.03.02 | UPB1-related Beta-Ureidopropionase deficiency | UPB1 | 613161;606673 | 65287 | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.767) |
| [ ] | 156 | 16.1.04.01 | NT5C3A-related Pyrimidine 5’-nucleotidase superactivity | NT5C3A | 266120;197720 | 35120 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.689) |
| [ ] | 154 | 16.1.04.02 | NT5C3A-related Pyrimidine-5'-nucleotidase I deficiency | NT5C3A | 266120;606224;191720 | 35120 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.831) |
| [ ] | 811 | 16.1.04.03 | AGXT2-related Hyper-β-aminoisobutyric aciduria | AGXT2 | 210100 | - | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.689) |
| [ ] | 1364 | 16.1.07.01 | DUT-related dUTP pyrophosphatase deficiency | DUT | 601266 | - | UNMAPPED |
| [ ] | 1391 | 16.1.08.01 | SLC28A1-related Pyrimidine nucleoside transporter deficiency | SLC28A1 | 606207 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.737) |
| [ ] | 1475 | 16.1.09.01 | DTYMK-related Deoxythymidylate kinase deficiency | DTYMK | 188345 | - | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.754) |
| [ ] | 1725 | 16.1.11.01 | NOGENE-related Hyper-beta-alaninemia | - | 237400 | 309147 | UNMAPPED; weak candidate Beta Thalassemia (0.649) |
| [ ] | 2043 | 16.1.13.01 | TYMS-related Thymidylate synthase deficiency | TYMS | 188350 | - | UNMAPPED; weak candidate Dyskeratosis Congenita (0.898) |
| [ ] | 2015 | 16.1.12.01 | IMPDH2-related IMP dehydrogenase 2 deficiency | IMPDH2 | 146691 | - | UNMAPPED |
| [ ] | 364 | 16.2.1.01 | XDH-related Xanthine oxidase deficiency | XDH | 278300;607633 | 93601 | UNMAPPED; weak candidate Chronic Granulomatous Disease (0.824) |
| [ ] | 1232 | 16.2.2.01 | AK7-related Adenylate kinase 7 deficiency | AK7 | 615364 | - | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.821) |
| [ ] | 140 | 16.2.03.01 | ADSL-related Adenylosuccinate lyase deficiency | ADSL | 103050;608222 | 46 | MAPPED -> Adenylosuccinate Lyase Deficiency (identifier:ORPHA:46) |
| [ ] | 144 | 16.2.04.01 | AMPD1-related Myoadenylate deaminase deficiency | AMPD1 | 102770 | 45 | UNMAPPED; weak candidate ADA deficiency (0.825) |
| [ ] | 788 | 16.2.05.01 | AMPD2-related Adenosine monophosphate deaminase 3 deficiency | AMPD2 | 615809;615686 | 401805 | CANDIDATE -> PCH2 (0.970) |
| [ ] | 789 | 16.2.06.01 | AMPD3-related Erythrocyte adenosine monophosphate deaminase 3 deficiency | AMPD3 | 612874 | 45 | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.693) |
| [ ] | 142 | 16.2.07.01 | ADA-related Adenosine deaminase deficiency | ADA | 102700 | 39041 | MAPPED -> ADA deficiency (alias_exact:adenosine deaminase deficiency) |
| [ ] | 790 | 16.2.08.01 | ADA2-related Adenosine deaminase 2 deficiency | ADA2 | 607575 | 404553 | UNMAPPED; weak candidate Deficiency of Adenosine Deaminase 2 (0.627) |
| [ ] | 149 | 16.2.09.01 | PNP-related Purine nucleoside phosphorylase deficiency | PNP | 613179;164050 | 760 | UNMAPPED; weak candidate IMD33 (0.762) |
| [ ] | 145 | 16.2.11.01 | HPRT1-related Hypoxanthine guanine phosphoribosyltransferase deficiency | HPRT1 | 300322;308000 | 206428 | MAPPED -> Lesch-Nyhan Syndrome (alias_exact:hypoxanthine guanine phosphoribosyltransferase deficiency) |
| [ ] | 146 | 16.2.12.01 | APRT-related Adenine phosphoribosyl transferase deficiency | APRT | 102600 | 976 | MAPPED -> Adenine Phosphoribosyltransferase Deficiency (identifier:ORPHA:976) |
| [ ] | 791 | 16.2.13.01 | AK1-related Adenylate kinase 1 deficiency | AK1 | 612631 | 86817 | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.821) |
| [ ] | 792 | 16.2.14.01 | AK2-related Adenylate kinase 2 deficiency | AK2 | 267500 | 33355 | UNMAPPED; weak candidate Adenosine Kinase Deficiency (0.821) |
| [ ] | 363 | 16.2.15.01 | IMPDH1-related Inosine-5'-monophosphate dehydrogenase deficiency | IMPDH1 | 146690 | 65 | CANDIDATE -> GUCY2D-Related Retinopathy (0.985) |
| [ ] | 151 | 16.2.16.01 | TPMT-related Thiopurine S-methyltransferase deficiency | TPMT | 610460;187680 | 413687 | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.767) |
| [ ] | 1384 | 16.2.17.01 | ITPA-related Inosine triphosphatase deficiency | ITPA | 147520 | 457375 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.602) |
| [ ] | 793 | 16.2.18.01 | SLC22A12-related Urate transporter 1 deficiency | SLC22A12 | 220150 | 94088 | UNMAPPED |
| [ ] | 794 | 16.2.19.01 | SLC2A9-related Urate voltage-driven efflux transporter 1 deficiency | SLC2A9 | 612076 | 94088 | UNMAPPED |
| [ ] | 141 | 16.2.21.01 | ATIC-related AICAR transformylase-IMP cyclohydrolase deficiency | ATIC | 608688;601731 | 250977 | UNMAPPED; weak candidate Autosomal recessive GTP cyclohydrolase I deficiency (0.691) |
| [ ] | 1477 | 16.2.22.01 | PAICS-related Phosphoribosylaminoimidazole carboxylase deficiency | PAICS | 172439 | - | UNMAPPED; weak candidate Propionic Acidemia (0.690) |
| [ ] | 1478 | 16.2.23.01 | ADA-related Adenosine deaminase superactivity | ADA | 608958 | 99138 | UNMAPPED; weak candidate ADA deficiency (0.762) |
| [ ] | 1479 | 16.2.24.01 | FAMIN-related Juvenile arthritis | LACC1 | 618795 | 85414 | MAPPED -> Juvenile Idiopathic Arthritis (identifier:ORPHA:85414) |
| [ ] | 1480 | 16.2.25.01 | ADSS1-related Adenylosuccinate synthase-like 1 deficiency | ADSS1 | 617030 | - | UNMAPPED; weak candidate Adenylosuccinate Lyase Deficiency (0.842) |
| [ ] | 1481 | 16.2.26.01 | NUDT15-related Poor metabolism of thiopurines | NUDT15 | 615792 | - | UNMAPPED |
| [ ] | 2187 | 16.2.27.01 | PFAS-related Phosphoribosylformylglycinamidine synthase deficiency | PFAS | 602133 | - | UNMAPPED; weak candidate N-Acetylglutamate Synthase Deficiency (0.600) |

### WP-044: Disorders of ectonucleotide and nucleic acid metabolism

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of ectonucleotide and nucleic acid metabolism
- Records: 29 (MAPPED 3, AMBIGUOUS 10, CANDIDATE 0, UNMAPPED 16)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 769 | 16.3.01.01 | TREX1-related 3’ Repair exonuclease 1 deficiency (AGS1) | TREX1 | 225750 | 481662 | AMBIGUOUS: 2 local entities (identifier:OMIM:225750) |
| [ ] | 778 | 16.3.1.01 | OAS1-related 2’,5’-Oligoadenylate synthetase 1 deficiency | OAS1 | 222100 | - | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.759) |
| [ ] | 1397 | 16.3.01.02 | TREX1-related Familial chilblain lupus type 1 | TREX1 | 610448 | 481662 | UNMAPPED; weak candidate Aicardi-Goutieres syndrome 1 (0.127) |
| [ ] | 1398 | 16.3.01.03 | TREX1-related 3’ Repair exonuclease 1 deficiency (CDG) | TREX1 | 192315 | 481662 | UNMAPPED; weak candidate Aicardi-Goutieres Syndrome (0.458) |
| [ ] | 770 | 16.3.02.01 | RNASEH2B-related Ribonuclease H2 subunit B deficiency (AGS2) | RNASEH2B | 610181 | 51 | AMBIGUOUS: 2 local entities (identifier:OMIM:610181) |
| [ ] | 1631 | 16.3.2.01 | PRUNE1-related Neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies | PRUNE1 | 617481 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.680) |
| [ ] | 1399 | 16.3.03.01 | RNASEH2C-related Ribonuclease H2 subunit C deficiency (AGS3) | RNASEH2C | 610329 | 51 | AMBIGUOUS: 2 local entities (identifier:OMIM:610329) |
| [ ] | 1400 | 16.3.04.01 | RNASEH2A-related Ribonuclease H2 subunit A deficiency (AGS4) | RNASEH2A | 610333 | 51 | AMBIGUOUS: 2 local entities (identifier:OMIM:610333) |
| [ ] | 785 | 16.3.05.01 | AICDA-related Activation-induced cytidine deaminase deficiency | AICDA | 605258 | 101089 | UNMAPPED; weak candidate ADA deficiency (0.667) |
| [ ] | 773 | 16.3.05.02 | RNASET2-related Ribonuclease T2 deficiency | RNASET2 | 612951 | 85136 | UNMAPPED; weak candidate COA8-Related COX Deficiency (0.707) |
| [ ] | 786 | 16.3.06.01 | UNG-related Uracil-DNA glycosylase deficiency | UNG | 608106 | 101092 | UNMAPPED; weak candidate IMD33 (0.596) |
| [ ] | 775 | 16.3.07.01 | ADAR-related RNA-specific adenosine deaminase deficiency (AGS6) | ADAR | 615010 | 41 | AMBIGUOUS: 2 local entities (identifier:OMIM:615010) |
| [ ] | 1407 | 16.3.07.02 | ADAR-related RNA-specific adenosine deaminase deficiency | ADAR | 127400 | 41 | UNMAPPED; weak candidate Aicardi-Goutieres syndrome 6 (0.090) |
| [ ] | 776 | 16.3.08.01 | IFIH1-related MDA5 superactivity (AGS7) | IFIH1 | 615846 | 85191 | AMBIGUOUS: 2 local entities (identifier:OMIM:615846) |
| [ ] | 1408 | 16.3.08.02 | IFIH1-related Singleton-Merten syndrome type 1 | IFIH1 | 182250 | 85191 | UNMAPPED; weak candidate Aicardi-Goutieres syndrome 7 (0.450) |
| [ ] | 777 | 16.3.09.01 | TMEM173-related STING superactivity | TMEM173 | 615934 | 481662 | MAPPED -> STING-Associated Vasculopathy with Onset in Infancy (alias_exact:sting associated vasculopathy with onset in infancy) |
| [ ] | 779 | 16.3.11.01 | ABCC6-related Generalized arterial calcification of infancy type 2 | ABCC6 | 614473 | 51608 | AMBIGUOUS: 2 local entities (identifier:OMIM:614473) |
| [ ] | 1410 | 16.3.11.02 | ABCC6-related Pseudoxanthoma elasticum | ABCC6 | 264800 | 51608 | MAPPED -> Pseudoxanthoma Elasticum (alias_exact:pseudoxanthoma elasticum) |
| [ ] | 780 | 16.3.12.01 | ENPP1-related Ectonucleotide pyrophosphatase-phosphodiesterase 1 deficiency (GACI1) | ENPP1 | 208000 | 51608 | AMBIGUOUS: 2 local entities (identifier:OMIM:208000) |
| [ ] | 1689 | 16.3.12.02 | ENPP1-related Ectonucleotide pyrophosphatase-phosphodiesterase 1 deficiency (ARHR2) | ENPP1 | 613312 | 51608 | UNMAPPED |
| [ ] | 781 | 16.3.13.01 | ENPP1-related Ectonucleotide pyrophosphatase-phosphodiesterase 1 dimerization deficiency | ENPP1 | 615522 | 324561 | UNMAPPED |
| [ ] | 782 | 16.3.14.01 | NT5E-related Ecto-5'-nucleotidase deficiency | NT5E | 211800 | 289601 | MAPPED -> Hereditary Arterial and Articular Multiple Calcification Syndrome (alias_exact:acdc) |
| [ ] | 783 | 16.3.15.01 | SLC29A1-related Equilibrative nucleoside transporter 1 deficiency | SLC29A1 | 602193 | - | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.706) |
| [ ] | 784 | 16.3.16.01 | SLC29A3-related Equilibrative nucleoside transporter 3 deficiency | SLC29A3 | 602782 | 254707 | UNMAPPED; weak candidate Rosai-Dorfman Disease (0.677) |
| [ ] | 1409 | 16.3.17.01 | DDX58-related  Singleton-Merten syndrome type 2 | DDX58 | 616298 | - | UNMAPPED |
| [ ] | 1482 | 16.3.18.01 | ADARB1-related RNA-specific adenosine deaminase 2 deficiency | ADARB1 | 618862 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.803) |
| [ ] | 1483 | 16.3.19.01 | ENTPD1-related Ectonucleoside triphosphate diphosphohydrolase 1 deficiency | ENTPD1 | 615683 | 401810 | UNMAPPED; weak candidate ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum (0.738) |
| [ ] | 2107 | 16.3.21.01 | LSM11-related Aicardi-Goutières syndrome type 8 | LSM11 | 619486 | - | AMBIGUOUS: 2 local entities (identifier:OMIM:619486) |
| [ ] | 2108 | 16.3.22.01 | RNU7-related Aicardi-Goutières syndrome (AGS9) | RNU7-1 | 619487 | - | AMBIGUOUS: 2 local entities (identifier:OMIM:619487) |

### WP-045: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases (part 1 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1484 | 16.4.01.01 | TSEN2-related tRNA splicing endonuclease subunit 2 deficiency | TSEN2 | 612389 | 2524 | UNMAPPED; weak candidate Pontocerebellar Hypoplasia (0.867) |
| [ ] | 1492 | 16.4.1.01 | NSUN2-related Intellectual disability type 5, ar | NSUN2 | 611091 | 235;88616 | UNMAPPED; weak candidate MED13 Syndrome (0.821) |
| [ ] | 1485 | 16.4.02.01 | TSEN15-related tRNA splicing endonuclease subunit 15 deficiency | TSEN15 | 617026 | 2524 | UNMAPPED; weak candidate Pontocerebellar Hypoplasia (0.867) |
| [ ] | 1502 | 16.4.2.01 | PUS3-related Pseudouridine synthase 3 deficiency | PUS3 | 617051 | 488627 | UNMAPPED; weak candidate Autosomal Recessive Osteopetrosis Type 2 (0.703) |
| [ ] | 1486 | 16.4.03.01 | TSEN34-related tRNA splicing endonuclease subunit 34 deficiency | TSEN34 | 612390 | 2524 | UNMAPPED; weak candidate Pontocerebellar Hypoplasia (0.867) |
| [ ] | 1512 | 16.4.3.01 | IARS1-related Isoleucyl-tRNA synthetase 1 deficiency | IARS1 | 617093 | 541423 | UNMAPPED; weak candidate Antisynthetase Syndrome (0.623) |
| [ ] | 1487 | 16.4.04.01 | TSEN54-related tRNA splicing endonuclease subunit 54 deficiency | TSEN54 | 608755 | 2524;2254;166063;166068 | UNMAPPED; weak candidate PCH2 (0.868) |
| [ ] | 1522 | 16.4.4.01 | VARS1-related Valyl-tRNA synthetase 1 deficiency | VARS1 | 617802 | 420728 | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.732) |
| [ ] | 1488 | 16.4.05.01 | CLP1-related Pontocerebellar hypoplasia type 10 | CLP1 | 615803 | 411493 | MAPPED -> PCH10 (alias_exact:pontocerebellar hypoplasia type 10) |
| [ ] | 1421 | 16.4.06.01 | TRMT10A-related Microcephaly, short stature, and impaired glucose metabolism 1 | TRMT10A | 616013 | 391408 | UNMAPPED; weak candidate Galloway-Mowat syndrome (0.495) |
| [ ] | 1489 | 16.4.07.01 | TRMT1-related tRNA methyltransferase 1 deficiency | TRMT1 | 618302 | 528084 | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.775) |
| [ ] | 1490 | 16.4.08.01 | DALRD3-related Early infantile epileptic encephalopathy type 86 | DALRD3 | 618910 | 442835 | UNMAPPED |
| [ ] | 1491 | 16.4.09.01 | FTSJ-related RNA 2’-O-methyltransferase 1 deficiency | FTSJ1 | 309549 | 777 | UNMAPPED; weak candidate Guanidinoacetate Methyltransferase Deficiency (0.747) |
| [ ] | 1493 | 16.4.11.01 | ADAT3-related tRNA-specific adenosine deaminase 3 deficiency | ADAT3 | 615286 | 363528 | UNMAPPED; weak candidate ADA deficiency (0.789) |
| [ ] | 1494 | 16.4.12.01 | ELP1-related Elongator complex protein 1 deficiency | ELP1 | 223900 | 1764 | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.686) |
| [ ] | 1495 | 16.4.13.01 | ELP2-related Elongator complex protein 2 deficiency | ELP2 | 617270 | - | UNMAPPED; weak candidate Autosomal Recessive Osteopetrosis Type 2 (0.703) |
| [ ] | 1496 | 16.4.14.01 | YRDC-related Galloway-Mowat syndrome, YRDC type | YRDC | 612276 | - | UNMAPPED; weak candidate GAMOS10 (0.861) |
| [ ] | 1497 | 16.4.15.01 | GON7-related Galloway-Mowat syndrome, GON7 type | GON7 | 617436 | - | UNMAPPED; weak candidate GAMOS9 (0.873) |
| [ ] | 1498 | 16.4.16.01 | LAGE3-related Galloway-Mowat syndrome type 2 | LAGE3 | 301006 | 2065 | MAPPED -> GAMOS2 (alias_exact:gamos2) |
| [ ] | 1499 | 16.4.17.01 | OSGEP-related Galloway-Mowat syndrome type 3 | OSGEP | 617729 | 2065 | CANDIDATE -> GAMOS3 (0.909) |
| [ ] | 1500 | 16.4.18.01 | TP53RK-related Galloway-Mowat syndrome type 4 | TP53RK | 617730 | - | CANDIDATE -> GAMOS4 (0.909) |
| [ ] | 1501 | 16.4.19.01 | TPRKB-related Galloway-Mowat syndrome type 5 | TPRKB | 617731 | 2065 | MAPPED -> GAMOS5 (alias_exact:gamos5) |

### WP-046: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases (part 2 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases
- Records: 22 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 19)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1503 | 16.4.21.01 | WDR4-related Galloway-Mowat syndrome type 6 | WDR4 | 605924 | 2065 | MAPPED -> GAMOS6 (alias_exact:gamos6) |
| [ ] | 1504 | 16.4.22.01 | AARS1-related Alanyl-tRNA synthetase 1 deficiency | AARS1 | 613287;616339 | 228174;442835 | UNMAPPED; weak candidate Antisynthetase Syndrome (0.622) |
| [ ] | 1505 | 16.4.23.01 | RARS1-related Arginyl-tRNA synthetase 1 deficiency | RARS1 | 616140 | 438114 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.899) |
| [ ] | 1506 | 16.4.24.01 | NARS1-related Asparaginyl-tRNA synthetase 1 deficiency | NARS1 | 619091 | - | UNMAPPED; weak candidate Antisynthetase Syndrome (0.633) |
| [ ] | 1507 | 16.4.25.01 | DARS1-related Aspartyl-tRNA synthetase 1 deficiency | DARS1 | 615281 | 363412 | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.725) |
| [ ] | 1508 | 16.4.26.01 | CARS1-related Cysteinyl-tRNA synthetase 1 deficiency | CARS1 | 618891 | - | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.693) |
| [ ] | 1509 | 16.4.27.01 | QARS1-related Glutaminyl-tRNA synthetase 1 deficiency | QARS1 | 615760 | 404437;423306 | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.711) |
| [ ] | 1510 | 16.4.28.01 | EPRS1-related Glutamyl-prolyl-tRNA synthetase 1 deficiency | EPRS1 | 617951 | - | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.886) |
| [ ] | 1511 | 16.4.29.01 | HARS1-related Histidyl-tRNA synthetase 1 deficiency | HARS1 | 614504 | 488333;231183 | UNMAPPED; weak candidate Antisynthetase Syndrome (0.605) |
| [ ] | 1513 | 16.4.31.01 | LARS1-related Leucyl-tRNA synthetase 1 deficiency | LARS1 | 615438 | 370088 | UNMAPPED; weak candidate Lipoic Acid Synthetase Deficiency (0.765) |
| [ ] | 1515 | 16.4.33.01 | MARS1-related Methionyl-tRNA synthetase 1 deficiency | MARS1 | 156560 | 397735;401835;440427 | UNMAPPED; weak candidate CMT2 (0.765) |
| [ ] | 1516 | 16.4.34.01 | FARSA-related Phenylalanyl-tRNA synthetase subunit alpha deficiency | FARSA | 619013 | - | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.625) |
| [ ] | 1517 | 16.4.35.01 | FARSB-related Phenylalanyl-tRNA synthetase subunit beta deficiency | FARSB | 613658 | 178506 | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.632) |
| [ ] | 1518 | 16.4.36.01 | SARS1-related Seryl-tRNA synthetase 1 deficiency | SARS1 | 617709 | 88616 | UNMAPPED; weak candidate Lipoic Acid Synthetase Deficiency (0.746) |
| [ ] | 1519 | 16.4.37.01 | TARS1-related Threonyl-tRNA synthetase 1 deficiency | TARS1 | 618546 | 33364 | UNMAPPED; weak candidate Antisynthetase Syndrome (0.605) |
| [ ] | 1520 | 16.4.38.01 | WARS1-related Tryptophanyl-tRNA synthetase 1 deficiency | WARS1 | 617721 | - | UNMAPPED; weak candidate Distal Hereditary Motor Neuronopathy, Autosomal Dominant (0.796) |
| [ ] | 1521 | 16.4.39.01 | YARS1-related Tyrosyl-tRNA synthetase 1 deficiency | YARS1 | 608323 | 100045 | UNMAPPED; weak candidate Holocarboxylase Synthetase Deficiency (0.740) |
| [ ] | 1523 | 16.4.41.01 | AIMP1-related Leukodystrophy, hypomyelinating, 3 | AIMP1 | 260600 | 280293 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.651) |
| [ ] | 1524 | 16.4.42.01 | AIMP2-related Hypomyelinating leukodystrophy type 17 | AIMP2 | 618006 | - | CANDIDATE -> Hypomyelinating Leukodystrophy 7 (0.914) |
| [ ] | 2012 | 16.4.43.01 | NUP133-related Nephrotic syndrome, type 18 | NUP133 | 618177 | - | UNMAPPED; weak candidate Galloway-Mowat syndrome (0.558) |
| [ ] | 2013 | 16.4.44.01 | NUP107-related Nephrotic syndrome, type 11 | NUP107 | 618177;618348 | - | MAPPED -> GAMOS7 (alias_exact:galloway mowat syndrome 7) |
| [ ] | 2028 | 16.4.45.01 | CTU2-related Microcephaly, facial dysmorphism, renal agenesis, and ambiguous genitalia syndrome | CTU2 | 618142 | - | UNMAPPED; weak candidate Orofaciodigital Syndrome 17 (0.571) |

### WP-047: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases (part 3 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of non-mitochondrial tRNA processing and aminoacyl-tRNA synthetases
- Records: 2 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2039 | 16.4.46.01 | NUP62-related Nucleoporin 62 deficiency | NUP62 | 271930 | - | UNMAPPED; weak candidate Autosomal dominant striatal neurodegeneration (0.711) |
| [ ] | 2024 | 16.4.47.01 | THUMPD1-related disorder | THUMPD1 | 616662 | - | UNMAPPED |

### WP-048: Disorders of ribosomal biogenesis (part 1 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of ribosomal biogenesis
- Records: 22 (MAPPED 9, AMBIGUOUS 2, CANDIDATE 1, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1525 | 16.5.01.01 | TCOF1-related Treacher Collins syndrome type 1 | TCOF1 | 154500 | 861 | MAPPED -> TCS1 (alias_exact:tcs1) |
| [ ] | 1534 | 16.5.1.01 | POLR3H-related primary ovarian insufficiency | POLR3H | 619801 | 243 | AMBIGUOUS: 2 local entities (alias_exact:primary ovarian insufficiency) |
| [ ] | 1526 | 16.5.02.01 | POLR1D-related Treacher Collins syndrome type 2 | POLR1D | 613717 | 861 | MAPPED -> TCS2 (alias_exact:tcs2) |
| [ ] | 1544 | 16.5.2.01 | EMG1-related Bowen-Conradi syndrome | EMG1 | 211180 | 1270 | UNMAPPED |
| [ ] | 1527 | 16.5.03.01 | POLR1C-related Treacher Collins syndrome type 3 | POLR1C | 248390 | 861 | MAPPED -> TCS3 (alias_exact:tcs3) |
| [ ] | 1555 | 16.5.3.01 | RPS26-related Diamond-Blackfan anemia type 10 | RPS26 | 613309 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1528 | 16.5.04.01 | POLR1B-related Treacher Collins syndrome type 4 | POLR1B | 618939 | - | MAPPED -> TCS4 (alias_exact:tcs4) |
| [ ] | 1565 | 16.5.4.01 | RPS15A-related Diamond-Blackfan anemia type 20 | RPS15A | 618313 | - | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1529 | 16.5.05.01 | POLR1A-related Acrofacial dysostosis, Cincinnati type | POLR1A | 616462 | 1200 | UNMAPPED; weak candidate Mandibulofacial dysostosis with microcephaly (0.593) |
| [ ] | 1575 | 16.5.5.01 | DNAJC21-related Shwachman-Diamond syndrome | DNAJC21 | 617052 | - | AMBIGUOUS: 2 local entities (alias_exact:shwachman diamond syndrome) |
| [ ] | 1530 | 16.5.06.01 | POLR1C-related Leukodystrophy | POLR1C | 248390;616494 | 88637 | MAPPED -> Hypomyelinating Leukodystrophy 7 (alias_exact:leukodystrophy) |
| [ ] | 1532 | 16.5.08.01 | POLR3A-related Wiedemann-Rautenstrauch syndrome | POLR3A | 264090 | 3455 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.529) |
| [ ] | 1533 | 16.5.09.01 | POLR3B-related leukodystrophy (hypomyelinating leukodystrophy type 8) | POLR3B | 614381 | 88637;85186 | CANDIDATE -> Hypomyelinating Leukodystrophy 7 (0.982) |
| [ ] | 1535 | 16.5.11.01 | TAF1A-related familial isolated dilated cardiomyopathy | TAF1A | 604903 | 500180 | UNMAPPED; weak candidate Familial Dilated Cardiomyopathy (0.873) |
| [ ] | 1536 | 16.5.12.01 | UBTF-related Childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder | UBTF | 617672 | 500180 | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.512) |
| [ ] | 959 | 16.5.13.01 | RMRP-related Cartilage-hair hypoplasia | RMRP | 607095;250250;250460 | 93347 | UNMAPPED; weak candidate Thanatophoric Dysplasia Type 1 (0.821) |
| [ ] | 1537 | 16.5.13.02 | DKC1-related X-linked dyskeratosis congenita | DKC1 | 305000 | 1775;3322 | MAPPED -> Dyskeratosis Congenita (identifier:ORPHA:1775) |
| [ ] | 1538 | 16.5.14.01 | NOP10-related Autosomal recessive dyskeratosis congenita type 1 | NOP10 | 224230 | 1775 | MAPPED -> Dyskeratosis Congenita (identifier:ORPHA:1775) |
| [ ] | 1539 | 16.5.15.01 | NHP2-related Autosomal recessive dyskeratosis congenita type 2 | NHP2 | 613987 | 1775 | MAPPED -> Dyskeratosis Congenita (identifier:ORPHA:1775) |
| [ ] | 1546 | 16.5.16.01 | NPM1-related Nucleophosmin 1 deficiency | NPM1 | 164040 | 1775 | MAPPED -> Dyskeratosis Congenita (identifier:ORPHA:1775) |
| [ ] | 1540 | 16.5.17.01 | SNORD118-related Leukoencephalopathy with brain calcifications and cysts | SNORD118 | 614561 | 542310 | UNMAPPED; weak candidate Aicardi-Goutieres Syndrome (0.725) |
| [ ] | 1542 | 16.5.18.01 | POP1-related Anauxetic dysplasia type 2 | POP1 | 617396 | 93347 | UNMAPPED; weak candidate Thanatophoric Dysplasia Type 2 (0.821) |

### WP-049: Disorders of ribosomal biogenesis (part 2 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of ribosomal biogenesis
- Records: 22 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 22)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1543 | 16.5.19.01 | NEPRO-related skeletal dysplasia | NEPRO | 618853 | - | UNMAPPED; weak candidate Thanatophoric Dysplasia Type 1 (0.786) |
| [ ] | 1545 | 16.5.21.01 | BMS1-related aplasia cutis congenita | BMS1 | 107600 | 1114 | UNMAPPED; weak candidate Dyskeratosis Congenita (0.622) |
| [ ] | 1547 | 16.5.22.01 | RPS19-related Diamond-Blackfan anemia type 1 | RPS19 | 105650 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1548 | 16.5.23.01 | RPS24-related Diamond-Blackfan anemia type 3 | RPS24 | 610629 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1549 | 16.5.24.01 | RPS17-related Diamond-Blackfan anemia type 4 | RPS17 | 612527 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1550 | 16.5.25.01 | RPL35A-related Diamond-Blackfan anemia type 5 | RPL35A | 612528 | - | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1551 | 16.5.26.01 | RPL5-related Diamond-Blackfan anemia type 6 | RPL5 | 612561 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1552 | 16.5.27.01 | RPL11-related Diamond-Blackfan anemia type 7 | RPL11 | 612562 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1553 | 16.5.28.01 | RPS7-related Diamond-Blackfan anemia type 8 | RPS7 | 612563 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1554 | 16.5.29.01 | RPS10-related Diamond-Blackfan anemia type 9 | RPS10 | 613308 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.868) |
| [ ] | 1556 | 16.5.31.01 | RPL26-related Diamond-Blackfan anemia type 11 | RPL26 | 614900 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1557 | 16.5.32.01 | RPL15-related Diamond-Blackfan anemia type 12 | RPL15 | 615550 | - | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1558 | 16.5.33.01 | RPS29-related Diamond-Blackfan anemia type 13 | RPS29 | 615909 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1559 | 16.5.34.01 | TSR2-related Diamond-Blackfan anemia type 14 | TSR2 | 300946 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1560 | 16.5.35.01 | RPS28-related Diamond-Blackfan anemia type 15 | RPS28 | 606164 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1561 | 16.5.36.01 | RPL27-related Diamond-Blackfan anemia type 16 | RPL27 | 617408 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1562 | 16.5.37.01 | RPS27-related Diamond-Blackfan anemia type 17 | RPS27 | 617409 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1563 | 16.5.38.01 | RPL18-related Diamond-Blackfan anemia type 18 | RPL18 | 618310 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1564 | 16.5.39.01 | RPL35-related Diamond-Blackfan anemia type 19 | RPL35 | 618312 | 124 | UNMAPPED; weak candidate Diamond-Blackfan Anemia (0.852) |
| [ ] | 1566 | 16.5.41.01 | RPL10-related Cytosolic large ribosomal subunit 10 deficiency | RPL10 | 300998 | - | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.686) |
| [ ] | 1567 | 16.5.42.01 | RPL13-related Cytosolic large ribosomal subunit 13 deficiency | RPL13 | 618728 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.828) |
| [ ] | 1568 | 16.5.43.01 | RPL21-related Cytosolic large ribosomal subunit 21 deficiency | RPL21 | 615885 | 55654 | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.686) |

### WP-050: Disorders of ribosomal biogenesis (part 3 of 3)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of ribosomal biogenesis
- Records: 15 (MAPPED 1, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 12)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1569 | 16.5.44.01 | RPS20-related Cytosolic small ribosomal subunit 20 deficiency | RPS20 | 603682 | 440437 | UNMAPPED |
| [ ] | 1570 | 16.5.45.01 | RPS23-related Cytosolic small ribosomal subunit 23 deficiency | RPS23 | 617412 | - | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.647) |
| [ ] | 1571 | 16.5.46.01 | RPSA-related Cytosolic ribosomal SA deficiency | RPSA | 271400 | 101351 | UNMAPPED; weak candidate Epispadias (0.596) |
| [ ] | 1572 | 16.5.47.01 | PARN-related Poly(A)-specific ribonuclease deficiency | PARN | 616353 | - | UNMAPPED; weak candidate PARN (0.833) |
| [ ] | 1573 | 16.5.48.01 | SBDS-related Shwachman-Diamond syndrome type 1 | SBDS | 260400 | 811 | UNMAPPED |
| [ ] | 1574 | 16.5.49.01 | EFL1-related Shwachman-Diamond syndrome type 2 | EFL1 | 617941 | 811 | MAPPED -> EFL1-related Shwachman-Diamond syndrome (alias_exact:sds2) |
| [ ] | 1576 | 16.5.51.01 | EIF6-related Shwachman-Diamond syndrome | EIF6 | 602912 | - | AMBIGUOUS: 2 local entities (alias_exact:shwachman diamond syndrome) |
| [ ] | 1748 | 16.5.52.01 | POLR3K-related Leukodystrophy, hypomyelinating, 21 | POLR3K | 619310 | - | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.737) |
| [ ] | 1745 | 16.5.53.01 | POLR3GL-related Short stature, oligodontia, dysmorphic facies, and motor delay | POLR3GL | 619234 | - | UNMAPPED; weak candidate Van Buchem Disease (0.541) |
| [ ] | 1763 | 16.5.54.01 | RPL3L-related Cardiomyopathy, dilated, 2D | RPL3L | 619371 | - | UNMAPPED; weak candidate Dilated Cardiomyopathy (0.656) |
| [ ] | 1770 | 16.5.55.01 | RBM28-related Alopecia, neurologic defects, and endocrinopathy syndrome | RBM28 | 612079 | - | UNMAPPED; weak candidate Paraneoplastic Neurological Syndromes (0.539) |
| [ ] | 2019 | 16.5.56.01 | LTV1-related Low temperature viability protein 1 deficiency | LTV1 | 620199 | - | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.615) |
| [ ] | 2035 | 16.5.57.01 | SHQ1-related  Neurodevelopmental disorder with dystonia and seizures | SHQ1 | 619922 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.764) |
| [ ] | 2049 | 16.5.58.01 | TAF8-related  Neurodevelopmental disorder | TAF8 | 619972 | - | CANDIDATE -> Bosch-Boonstra-Schaaf Optic Atrophy Syndrome (1.000) |
| [ ] | 2074 | 16.5.59.01 | ERI1-related Exoribonuclease 1 deficiency | ERI1 | 608739 | - | UNMAPPED |

### WP-051: Disorders of purine and pyrimidine matabolism

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of nucleobase, nucleotide and nucleic acid metabolism
- Subgroup scope: Disorders of purine and pyrimidine matabolism
- Records: 2 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 0)
- Work: review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 362 | 16.2.01.01 | PRPS1-related Phosphoribosyl pyrophosphate synthetase 1 superactivity | PRPS1 | 300661 | 99014 | CANDIDATE -> PRPS1 Superactivity (0.972) |
| [ ] | 147 | 16.2.02.01 | PRPS1-related Phosphoribosyl pyrophosphate synthetase 1 deficiency | PRPS1 | 311850 | 1187 | MAPPED -> Arts syndrome (identifier:ORPHA:1187) |

### WP-052: Disorders of heme synthesis and porphyrias + 1 adjacent subgroup(s)

- Classification: Metabolism of Heterocyclic Compounds -> Disorders of tetrapyrrole metabolism
- Subgroup scope: Disorders of heme synthesis and porphyrias; Disorders of heme degradation and bilirubin metabolism
- Records: 19 (MAPPED 7, AMBIGUOUS 1, CANDIDATE 0, UNMAPPED 11)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 107 | 17.1.1.01 | FECH-related Ferrochelatase deficiency | FECH | 177000 | - | MAPPED -> Erythropoietic Protoporphyria (alias_exact:erythropoietic protoporphyria) |
| [ ] | 110 | 17.1.01.01 | ALAS2-related Erythroid 5-aminolevulinate synthase deficiency | ALAS2 | 300751 | 75563 | UNMAPPED |
| [ ] | 108 | 17.1.02.01 | ALAS2-related Erythroid 5-aminolevulinate synthase superactivity | ALAS2 | 300752 | - | UNMAPPED |
| [ ] | 115 | 17.1.03.01 | ALAD-related Delta-aminolevulinate dehydratase deficiency | ALAD | 125270 | 100924 | MAPPED -> Porphyria due to ALA Dehydratase Deficiency (identifier:ORPHA:100924) |
| [ ] | 112 | 17.1.04.01 | HMBS-related Porphobilinogen deaminase deficiency | HMBS | 176000 | 79276 | MAPPED -> Acute Intermittent Porphyria (identifier:ORPHA:79276) |
| [ ] | 111 | 17.1.05.01 | UROS-related Uroporphyrinogen III synthase deficiency | UROS | 263700 | 79277 | MAPPED -> Congenital Erythropoietic Porphyria (alias_exact:congenital erythropoietic porphyria) |
| [ ] | 114 | 17.1.06.01 | UROD-related Hepatic uroporphyrinogen decarboxylase deficiency | UROD | 176100 | 95159 | UNMAPPED; weak candidate Inherited Porphyria (0.337) |
| [ ] | 113 | 17.1.07.01 | CPOX-related Coproporphyrinogen oxidase deficiency | CPOX | 121300 | 79273 | MAPPED -> Hereditary Coproporphyria (alias_exact:hereditary coproporphyria) |
| [ ] | 1296 | 17.1.08.01 | CPOX-related Hereditary coproporphyria | CPOX | 121300 | 79273 | MAPPED -> Hereditary Coproporphyria (alias_exact:hereditary coproporphyria) |
| [ ] | 109 | 17.1.09.01 | PPOX-related Protoporphyrinogen oxidase deficiency | PPOX | 176200 | - | UNMAPPED; weak candidate Inherited Porphyria (0.643) |
| [ ] | 1093 | 17.1.11.01 | GATA1-related Anemia, with/without neutropenia and/or platelet abnormalities | GATA1 | 300835 | 99887 | UNMAPPED; weak candidate Congenital Dyserythropoietic Anemia (0.396) |
| [ ] | 1094 | 17.1.12.01 | ABCB6-related Mitochondrial porphyrin transporter deficiency | ABCB6 | 609153;615402 | 98944 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.717) |
| [ ] | 661 | 17.2.01.01 | UGT1A1-related UDP-glucuronosyltransferase A1 deficiency | UGT1A1 | 218800;606785 | 205 | MAPPED -> Gilbert's Syndrome (alias_exact:gilbert syndrome) |
| [ ] | 554 | 17.2.02.01 | ABCC2-related Canalicular bilirubin glucuronide transporter deficiency | ABCC2 | 237500;601107 | 234 | UNMAPPED; weak candidate Stevens-Johnson Syndrome (0.783) |
| [ ] | 1095 | 17.2.13.01 | CYB5R3-related NADH-cytochrome b5 reductase deficiency | CYB5R3 | 250800 | 621 | AMBIGUOUS: 2 local entities (identifier:ORPHA:621) |
| [ ] | 1096 | 17.2.14.01 | CYB5A-related Cytochrome b5 deficiency | CYB5A | 250790 | 90796 | UNMAPPED; weak candidate COX5A-Related COX Deficiency (0.819) |
| [ ] | 1097 | 17.2.15.01 | HMOX1-related Heme oxygenase 1 deficiency | HMOX1 | 614034 | - | UNMAPPED; weak candidate Inherited Porphyria (0.293) |
| [ ] | 1098 | 17.2.16.01 | BLVRA-related Biliverdin reductase α deficiency | BLVRA | 614156 | 276405 | UNMAPPED; weak candidate Multiple Mitochondrial Dysfunctions Syndrome 9B (0.765) |
| [ ] | 553 | 17.2.17.01 | SLCO1B1;SLCO1B3-related Rotor syndrome | SLCO1B1;SLCO1B3 | 237450;604843;605495 | 3111 | UNMAPPED; weak candidate Type 4B (0.358) |

### WP-053: Disorders of N-linked protein glycosylation (part 1 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of N-linked protein glycosylation
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 321 | 18.1.01.01 | PMM2-related Phosphomannomutase 2 deficiency (CDG) | PMM2 | 601785 | 79318 | UNMAPPED |
| [ ] | 331 | 18.1.1.01 | RFT1-related Flippase of Man5GlcNAc2-PP-Dol deficiency (CDG) | RFT1 | 612015 | - | UNMAPPED; weak candidate X-linked SCID (0.588) |
| [ ] | 322 | 18.1.02.01 | MPI-related Phosphomannose isomerase deficiency (CDG) | MPI | 602579 | 79319 | UNMAPPED |
| [ ] | 333 | 18.1.2.01 | GCS1-related Glucosidase 1 deficiency (CDG) | MOGS | 606056 | - | UNMAPPED; weak candidate Gaucher Disease (0.783) |
| [ ] | 328 | 18.1.03.01 | DPAGT1-related UDP-GlcNAc:Dol-P-GlcNac-P transferase deficiency (CDG) | DPAGT1 | 608093 | 86309 | UNMAPPED |
| [ ] | 1692 | 18.1.3.01 | GFUS-related GDP-L-fucose synthase deficiency (CDG) | GFUS | 137020 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.762) |
| [ ] | 605 | 18.1.04.01 | ALG13-related UDP-N-acetylglucosamine transferase catalytic subunit deficiency (CDG) | ALG13 | 300884 | 324422 | UNMAPPED; weak candidate DEE13 (0.695) |
| [ ] | 1387 | 18.1.05.01 | ALG13-related UDP-N-acetylglucosamine transferase catalytic subunit deficiency, XLD (CDG) | ALG13 | 300884 | 324422 | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.524) |
| [ ] | 606 | 18.1.06.01 | ALG14-related Congenital myasthenic syndrome, without tubular aggregates (CDG) | ALG14 | 616227;612866 | 353327 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.659) |
| [ ] | 329 | 18.1.07.01 | ALG1-related Mannosyltransferase 1 deficiency (CDG) | ALG1 | 608540 | 79327 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.912) |
| [ ] | 327 | 18.1.08.01 | ALG2-related Mannosyltransferase 2 deficiency (CDG) | ALG2 | 607906 | 79326 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.912) |
| [ ] | 383 | 18.1.09.01 | ALG11-related Mannosyltransferase 4-5 deficiency (CDG) | ALG11 | 613661 | 280071 | UNMAPPED; weak candidate ALG12-congenital disorder of glycosylation (0.886) |
| [ ] | 324 | 18.1.11.01 | ALG3-related Mannosyltransferase 6 deficiency (CDG) | ALG3 | 601110 | 79321 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.912) |
| [ ] | 330 | 18.1.12.01 | ALG9-related Mannosyltransferase 7-9 deficiency (CDG) | ALG9 | 608776 | - | MAPPED -> ALG9-congenital disorder of glycosylation (alias_exact:alg9 cdg) |
| [ ] | 2095 | 18.1.12.02 | ALG9-related Mannosyltransferase 7-9 deficiency-CDG(ad) | ALG9 | 606941 | - | MAPPED -> ALG9-congenital disorder of glycosylation (alias_exact:alg9 cdg) |
| [ ] | 325 | 18.1.13.01 | ALG12-related Mannosyltransferase 8 deficiency (CDG) | ALG12 | 607143 | 79324 | MAPPED -> ALG12-congenital disorder of glycosylation (alias_exact:alg12 cdg) |
| [ ] | 323 | 18.1.14.01 | ALG6-related Glucosyltransferase 1 deficiency (CDG) | ALG6 | 603147 | 79320 | UNMAPPED |
| [ ] | 326 | 18.1.15.01 | ALG8-related Glucosyltransferase 2 deficiency (CDG) | ALG8 | 608104 | 79325 | UNMAPPED; weak candidate ALG8-related ADPLD (0.476) |
| [ ] | 2082 | 18.1.15.02 | ALG10-related Alpha-1,2-glucosyltransferase deficiency-CDG | ALG10 | 618355 | - | UNMAPPED; weak candidate Fucosidosis (0.685) |
| [ ] | 2094 | 18.1.15.02 | ALG8-related Glucosyltransferase 2 deficiency-CDG(ad) | ALG8 | 608104 | 79325 | UNMAPPED; weak candidate Autosomal dominant polycystic liver disease (0.873) |
| [ ] | 334 | 18.1.16.01 | TUSC3-related Oligosaccharyltransferase subunit tusc 3 deficiency (CDG) | TUSC3 | 611093 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.584) |
| [ ] | 608 | 18.1.17.01 | STT3A-related Congenital disorder of glycosylation (CDG) | STT3A | 615596;601134 | 370921 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |

### WP-054: Disorders of N-linked protein glycosylation (part 2 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of N-linked protein glycosylation
- Records: 20 (MAPPED 1, AMBIGUOUS 2, CANDIDATE 6, UNMAPPED 11)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2090 | 18.1.17.02 | STT3A-related Congenital disorder of glycosylation-CDG(ad) | STT3A | 615596;601134 | 370921 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.945) |
| [ ] | 384 | 18.1.18.01 | MAGT1-related Magnesium transporter 1 deficiency (CDG) | MAGT1 | 300716;300853 | 317476 | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.598) |
| [ ] | 610 | 18.1.19.01 | SSR4-related Congenital disorder of glycosylation (CDG) | SSR4 | 300934 | 370927 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 626 | 18.1.21.01 | GANAB-related Alpha glucosidase II deficiency (CDG) | GANAB | 600666 | 730 | AMBIGUOUS: 3 local entities (identifier:ORPHA:730) |
| [ ] | 1118 | 18.1.22.01 | PRKCSH-related Alpha-1,3-glucosidase II subunit beta deficiency (CDG) | PRKCSH | 174050 | 2924 | AMBIGUOUS: 5 local entities (identifier:ORPHA:2924) |
| [ ] | 2079 | 18.1.22.02 | SEC63-related CDG | SEC63 | 617004 | - | MAPPED -> PCLD2 (alias_exact:pcld2) |
| [ ] | 611 | 18.1.23.01 | MAN1B1-related Mannosyl-oligosaccharide alpha-1,2-mannosidase deficiency (CDG) | MAN1B1 | 614202;604346 | - | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.713) |
| [ ] | 332 | 18.1.24.01 | MGAT2-related N-acetylglucosaminyltransferase 2 deficiency (CDG) | MGAT2 | 212066 | - | UNMAPPED; weak candidate MGAT2-congenital disorder of glycosylation (0.353) |
| [ ] | 1119 | 18.1.25.01 | FUT8-related Alpha-1,6-fucosyltransferase deficiency (CDG) | FUT8 | 618005 | - | UNMAPPED; weak candidate Fucosidosis (0.722) |
| [ ] | 1331 | 18.1.26.01 | FCSK-related Fucokinase deficiency (CDG) | FCSK | 618324 | - | UNMAPPED |
| [ ] | 609 | 18.1.27.01 | STT3B-related Congenital disorder of glycosylation (CDG) | STT3B | 615597 | 370924 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 607 | 18.1.28.01 | DDOST-related Congenital disorder of glycosylation (CDG) | DDOST | 614507;602202 | 300536 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 338 | 18.1.29.01 | B4GALT1-related Beta-1,4-galactosyltransferase 1 deficiency (CDG) | B4GALT1 | 607091 | 79332 | UNMAPPED; weak candidate GM1 Gangliosidosis Type 1 (0.651) |
| [ ] | 1464 | 18.1.31.01 | OSTC-related Oligosaccharyltransferase complex deficiency (CDG) | OSTC | 619023 | - | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.612) |
| [ ] | 1726 | 18.1.32.01 | SSR3-related Intellectual and developmental disabilities and sensorineural deafness (CDG) | SSR3 | 606213 | - | UNMAPPED; weak candidate MED13 (0.667) |
| [ ] | 1727 | 18.1.33.01 | MAN2B2-related Congenital disorder of glycosylation (CDG) | MAN2B2 | 618899 | - | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 1832 | 18.1.34.01 | EDEM3-related Congenital disorder of glycosylation (CDG) | EDEM3 | 619493 | - | CANDIDATE -> COG1-congenital disorder of glycosylation (0.977) |
| [ ] | 2042 | 18.1.35.01 | ALG5-related Dolichyl-phosphate beta-glucosyltransferase deficiency-CDG | ALG5 | 604565 | - | UNMAPPED; weak candidate Autosomal Dominant Polycystic Kidney Disease (0.635) |
| [ ] | 2057 | 18.1.36.01 | MAN2A2-related Alpha-mannosidase IIA deficiency-CDG | MAN2A2 | 600988 | - | UNMAPPED; weak candidate Fucosidosis (0.738) |
| [ ] | 2243 | 18.1.37.01 | RPN1-related Ribophorin I deficiency (CDG) | RPN1 | 180470 | - | UNMAPPED |

### WP-055: Disorders of O-linked protein glycosylation (part 1 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of O-linked protein glycosylation
- Records: 22 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 20)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 640 | 18.2.1.01 | RXYLT1-related Muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A (CDG) | RXYLT1 | 615041 | 51577 | MAPPED -> Cobblestone (alias_exact:cobblestone lissencephaly) |
| [ ] | 1129 | 18.2.1.02 | CHST3-related Chondroitin 6-sulfotransferase deficiency (CDG) | CHST3 | 143095 | 93280 | UNMAPPED; weak candidate Spondylocostal Dysostosis (0.625) |
| [ ] | 1304 | 18.2.1.03 | NDST1-related Heparan sulfate N-deacetylase-N-sulfotransferase 1 deficiency (DG) | NDST1 | 616116 | - | UNMAPPED; weak candidate Autosomal Recessive Osteopetrosis Type 2 (0.721) |
| [ ] | 352 | 18.2.01.06 | POMT1-related O-Mannosyltransferase 1 deficiency (CDG) | POMT1 | 236670;613555;609308 | 86812 | UNMAPPED; weak candidate Dystroglycanopathy (0.755) |
| [ ] | 358 | 18.2.02.01 | LFNG-rerlated O-Fucose-specific beta-1,3-N-acetylglucosaminyltransferase deficiency (CDG) | LFNG | 609813 | 2311 | UNMAPPED; weak candidate Spondylocostal Dysostosis (0.877) |
| [ ] | 353 | 18.2.02.02 | POMT2-related O-Mannosyltransferase 2 deficiency (CDG) | POMT2 | 613150;613156;613158 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.755) |
| [ ] | 639 | 18.2.02.03 | XYLT2-related Spondyloocular syndrome (CDG) | XYLT2 | 605822 | 85194 | UNMAPPED |
| [ ] | 1137 | 18.2.02.04 | C1GALT1C-related Core 1 beta-1,3-galactosyltransferase chaperone deficiency (CDG) | C1GALT1C1 | 300622 | - | UNMAPPED; weak candidate GM1 Gangliosidosis Type 1 (0.554) |
| [ ] | 1139 | 18.2.02.05 | EOGT-related EGF domain-specific O-linked N-acetylglucosamine transferase deficiency (CDG) | EOGT | 615297 | 974 | MAPPED -> AOS4 (alias_exact:aos4) |
| [ ] | 349 | 18.2.03.01 | B4GALT7-related Beta-1,4-galactosyltransferase 7 deficiency (CDG) | B4GALT7 | 130070 | 75496 | UNMAPPED; weak candidate spEDS-B4GALT7 (0.583) |
| [ ] | 359 | 18.2.03.02 | B3GALTL-related O-Fucose-specific beta-1,3-N-glucosyltransferase deficiency (CDG) | B3GLCT | 261540 | 709 | UNMAPPED; weak candidate Gaucher Disease (0.589) |
| [ ] | 354 | 18.2.03.03 | POMGNT1-related O-Mannose beta-1,2-N-acetyglucosaminyltransferase deficiency (CDG) | POMGNT1 | 253280;613151;613157 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.755) |
| [ ] | 1577 | 18.2.03.04 | GALNT14-related Polypeptide N-acetylgalactosaminyltransferase 14 deficiency (CDG) | GALNT14 | 608225 | - | UNMAPPED |
| [ ] | 2078 | 18.2.03.05 | COLGALT1-related Collagen beta(1-O)galactosyltransferase 1 deficiency (CDG) | COLGALT1 | 618360 | - | UNMAPPED; weak candidate Gaucher Disease (0.591) |
| [ ] | 1126 | 18.2.04.01 | B3GALT6-related Beta-1,3-galactosyltransferase 6 deficiency (CDG) | B3GALT6 | 271640;615349 | 93359 | UNMAPPED; weak candidate spEDS-B3GALT6 (0.583) |
| [ ] | 1120 | 18.2.04.02 | POMGNT2-related O-Mannose beta-1,4-N-acetylglucosaminyltransferase deficiency (CDG) | POMGNT2 | 614830;618135 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.892) |
| [ ] | 1121 | 18.2.05.01 | B3GALNT2-related Beta-1,3-galactosaminyltransferase 2 deficiency (CDG) | B3GALNT2 | 615181 | 88616 | UNMAPPED; weak candidate Dystroglycanopathy (0.597) |
| [ ] | 1127 | 18.2.05.02 | B3GAT3-related Beta-1,3-glucuronyltransferase 3 deficiency (CDG) | B3GAT3 | 245600 | 284139 | UNMAPPED; weak candidate Larsen Syndrome (0.857) |
| [ ] | 347 | 18.2.06.01 | EXT1-related Exostosin 1 deficiency (CDG) | EXT1 | 133700 | 55880 | UNMAPPED; weak candidate Multiple Synostoses Syndrome (0.597) |
| [ ] | 1122 | 18.2.06.02 | POMK-related O-Mannose kinase deficiency (CDG) | POMK | 616094;615249 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.881) |
| [ ] | 348 | 18.2.07.01 | EXT2-related Exostosin 2 deficiency (CDG) | EXT2 | 133701 | 52022 | UNMAPPED; weak candidate Multiple Synostoses Syndrome (0.597) |
| [ ] | 641 | 18.2.07.02 | CRPPA-related Muscular dystrophy-dystroglycanopathy type A7 and C7 (CDG) | CRPPA | 614643;616052 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.796) |

### WP-056: Disorders of O-linked protein glycosylation (part 2 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of O-linked protein glycosylation
- Records: 16 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 13)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2089 | 18.2.07.02 | EXT2-related Exostosin glycosyltransferase 2 deficiency (CDG) | EXT2 | 616682 | - | UNMAPPED; weak candidate EAST Syndrome (0.482) |
| [ ] | 642 | 18.2.08.01 | FKTN-related Muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A (CDG) | FKTN | 253800 | 272 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 643 | 18.2.08.02 | FKTN-related Muscular dystrophy-dystroglycanopathy (congenital without mental retardation), type B (CDG) | FKTN | 613152 | 272 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 644 | 18.2.08.03 | FKTN-related Muscular dystrophy-dystroglycanopathy (limb-girdle), type C (CDG) | FKTN | 611588 | 272 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 1128 | 18.2.08.04 | EXTL3-related Exostosin-like glycosyltransferase 3 deficiency (CDG) | EXTL3 | 617425 | - | UNMAPPED; weak candidate You-Hoover-Fong Syndrome (0.655) |
| [ ] | 385 | 18.2.09.01 | CHSY1-related Chondroitin sulfate synthase 1 deficiency (CDG) | CHSY1 | 605282 | 363417 | MAPPED -> Temtamy Preaxial Brachydactyly Syndrome (identifier:ORPHA:363417) |
| [ ] | 645 | 18.2.09.02 | FKRP-related Muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A (CDG) | FKRP | 613153 | 899 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 646 | 18.2.09.03 | FKRP-related Muscular dystrophy-dystroglycanopathy (congenital with or without mental retardation), type B (CDG) | FKRP | 606612 | 34515 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 647 | 18.2.09.04 | FKRP-related Muscular dystrophy-dystroglycanopathy (limb-girdle), type C (CDG) | FKRP | 606596 | 34515 | UNMAPPED; weak candidate Dystroglycanopathy (0.787) |
| [ ] | 1124 | 18.2.11.01 | B4GAT1-related Beta-1,4-glucuronyltransferase 1 deficiency (CDG) | B4GAT1 | 615287 | 899 | UNMAPPED; weak candidate MDDG13 (B4GAT1) (0.522) |
| [ ] | 1230 | 18.2.11.02 | CHST11-related Chondroitin 4-sulfotransferase 1 deficiency (CDG) | CHST11 | 610128 | - | UNMAPPED |
| [ ] | 1305 | 18.2.11.03 | HS6ST1-related Heparan sulfate 6-O-sulfate transferase 1 deficiency (CDG) | HS6ST1 | 614880 | - | CANDIDATE -> FGFR1-Related Hypogonadotropic Hypogonadism (0.931) |
| [ ] | 1130 | 18.2.12.01 | CHST14-related Dermatan 4-sulfotransferase 1 deficiency (CDG) | CHST14 | 601776 | 2953 | UNMAPPED; weak candidate Vascular Ehlers-Danlos Syndrome (0.776) |
| [ ] | 1125 | 18.2.12.02 | LARGE1-related Beta-1,3-glucuronyltransferase-α-1,3-xylosytransferase deficiency (CDG) | LARGE1 | 613154;608840 | 899 | UNMAPPED; weak candidate MDDG6 (LARGE1) (0.545) |
| [ ] | 2080 | 18.2.12.03 | TMTC3-related Transmembrane and tetratricopeptide repeat domains-containing protein 3 deficiency (CDG) | TMTC3 | 617255 | - | CANDIDATE -> Reelin Pathway Lissencephaly (0.929) |
| [ ] | 2081 | 18.2.12.04 | TMEM260-related Transmembrane protein 260 deficiency (CDG) | TMEM260 | 617478 | - | UNMAPPED; weak candidate Tall Stature-Intellectual Disability-Renal Anomalies Syndrome (0.632) |

### WP-057: Disorders of O-fucosylation + 2 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of O-fucosylation; Disorders of glycosaminoglycan synthesis and O-xylosylation; Other disorders of O-linked protein glycosylation
- Records: 23 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 21)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1140 | 18.2.02.06 | POFUT1-related O-fucosyltransferase deficiency (CDG) | POFUT1 | 615327 | 79145 | UNMAPPED; weak candidate EBS Severe (formerly Dowling-Meara) (0.328) |
| [ ] | 2091 | 18.2.02.07 | POFUT1-related Protein O-fucosyltransferase 1 deficiency-CDG | POFUT1 | 615327 | 79145 | UNMAPPED; weak candidate Galactosialidosis (0.515) |
| [ ] | 1218 | 18.2.2.01 | CSGALNACT1-related Chondroitin sulfate N-acetylgalactosaminyltransferase 1 deficiency (CDG) | CSGALNACT1 | 616615 | - | UNMAPPED; weak candidate Frontonasal dysplasia with alopecia and genital anomaly (0.542) |
| [ ] | 2064 | 18.2.03.05 | HS2ST1-related Heparan sulfate 2-O-sulfotransferase 1 deficiency (CDG) | HS2ST1 | 619194 | - | UNMAPPED; weak candidate Nonsyndromic CL/P (0.587) |
| [ ] | 638 | 18.2.03.06 | XYLT1-related Desbuquois dysplasia 2 (CDG) | XYLT1 | 615777 | 370930 | UNMAPPED; weak candidate GD2 (0.612) |
| [ ] | 1131 | 18.2.13.01 | DSE-related Dermatan sulfate epimerase deficiency (CDG) | DSE | 615539 | 2953 | UNMAPPED; weak candidate Vascular Ehlers-Danlos Syndrome (0.776) |
| [ ] | 1132 | 18.2.14.01 | CHST6-related Corneal N-acetylglucosamine 6-O-sulfotransferase deficiency (CDG) | CHST6 | 217800 | 98969 | UNMAPPED; weak candidate Macular dystrophy (0.810) |
| [ ] | 1133 | 18.2.15.01 | CANT1-related UDP-galactose nucleotidase deficiency (CDG) | CANT1 | 617719 | 1425 | MAPPED -> EDM7 (alias_exact:edm7) |
| [ ] | 1449 | 18.2.15.02 | CANT1-related UDP-galactose nucleotidase deficiency (CDG) | CANT1 | 251450 | 1425 | UNMAPPED; weak candidate Multiple Epiphyseal Dysplasia (0.429) |
| [ ] | 1134 | 18.2.16.01 | SLC26A2-related Sulfate transporter deficiency (CDG) | SLC26A2 | 226900;222600;256050;600972 | 93307 | UNMAPPED; weak candidate Atelosteogenesis Type II (0.667) |
| [ ] | 2077 | 18.2.16.02 | SLC13A1-related Na-sulfate cotransporter deficiency | SLC13A1 | 606193 | - | UNMAPPED |
| [ ] | 1135 | 18.2.17.01 | PAPSS2-related Phosphoadenosine 5'-phosphosulfate synthetase 2 deficiency (CDG) | PAPSS2 | 612847 | 93282 | UNMAPPED |
| [ ] | 1395 | 18.2.21.01 | HS6ST2-related Heparan sulfate 6-O-sulfotransferase 2 deficiency (CDG) | HS6ST2 | 301025 | - | UNMAPPED |
| [ ] | 1430 | 18.2.22.01 | TGDS-related TDP-D-glucose 4,6-dehydrogenase deficiency (CDG) | TGDS | 616145 | - | UNMAPPED; weak candidate Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency (0.756) |
| [ ] | 1728 | 18.2.30.01 | FAM20B-related Glycosaminoglycan xylosylkinase deficiency (CDG) | FAM20B | 611063 | - | UNMAPPED; weak candidate Thanatophoric Dysplasia Type 2 (0.576) |
| [ ] | 1729 | 18.2.30.02 | BPNT2-related Golgi-resident phosphoadenosine phosphate phosphatase deficiency (CDG) | BPNT2 | 614078 | 280586 | UNMAPPED; weak candidate PDH phosphatase deficiency (0.602) |
| [ ] | 1730 | 18.2.30.03 | SLC10A7-related Short stature, amelogenesis imperfecta, and skeletal dysplasia with scoliosis (CDG) | SLC10A7 | 618363 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type XIII (0.500) |
| [ ] | 2053 | 18.2.30.04 | SLC35B2-related Phosphoadenosine 5'-phosphosulfate transporter deficiency-CDG | SLC35B2 | 620269 | - | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.705) |
| [ ] | 350 | 18.2.04.03 | GALTNT3-related Polypeptide N-acetylgalactosaminyltransferase 3 deficiency (CDG) | GALNT3 | 211900 | 306661 | UNMAPPED; weak candidate Bilateral Striopallidodentate Calcinosis (0.494) |
| [ ] | 2062 | 18.2.4.03 | GALNT2-related UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase 2 deficiency-CDG | GALNT2 | 618885 | - | CANDIDATE -> COG1-congenital disorder of glycosylation (0.977) |
| [ ] | 625 | 18.2.04.04 | POGLUT1-related Dowling-Degos disease 4 (CDG) | POGLUT1 | 615696 | 79145 | UNMAPPED; weak candidate EBS Severe (formerly Dowling-Meara) (0.417) |
| [ ] | 1138 | 18.2.04.05 | OGT-related O-linked N-acetylglucosamine transferase deficiency (CDG) | OGT | 300997 | - | UNMAPPED; weak candidate Lipoyl Transferase 1 Deficiency (0.628) |
| [ ] | 1742 | 18.2.40.05 | POGLUT1-related Muscular dystrophy, limb-girdle, type 2Z (CDG) | POGLUT1 | 615696 | 79145 | UNMAPPED; weak candidate Limb-Girdle Muscular Dystrophy, Autosomal Dominant (0.747) |

### WP-058: Disorders of lipid glycosylation + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of lipid glycosylation; Disorders of glycosylphosphatidylinositol biosynthesis
- Records: 29 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 24)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 360 | 18.3.00.01 | ST3GAL5-related Lactosylceramide alpha-2,3-sialyltransferase deficiency (CDG) | ST3GAL5 | 609056 | 370938 | MAPPED -> GM3 synthase deficiency (identifier:OMIM:609056) |
| [ ] | 1150 | 18.3.00.04 | B4GALNT1-related GM2-GD2 synthase deficiency (CDG) | B4GALNT1 | 609195 | 101006 | UNMAPPED; weak candidate GM3 synthase deficiency (0.815) |
| [ ] | 1151 | 18.3.00.06 | ST3GAL3-related GD1a-GT1b synthase deficiency (CDG) | ST3GAL3 | 611090 | 88616 | UNMAPPED; weak candidate GM3 synthase deficiency (0.750) |
| [ ] | 1152 | 18.3.00.07 | A4GALT-related GGB3 synthase deficiency (CDG) | A4GALT | 111400 | - | UNMAPPED; weak candidate GM3 synthase deficiency (0.863) |
| [ ] | 1141 | 18.3.00.02 | PIGA-related GPI biosynthesis defect (CDG) | PIGA | 300868;300818 | 300496 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 628 | 18.3.00.03 | PIGC-related Developmental disability, severe intellectual disability, and drug-responsive epilepsy (CDG) | PIGC | 615716 | 88616 | UNMAPPED; weak candidate IRX5-related craniofacial dysostosis with osteopenia, intellectual disability, and dental anomalies (0.577) |
| [ ] | 1142 | 18.3.00.05 | PIGQ-related GPI biosynthesis defect (CDG) | PIGQ | 605754 | 1934 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 1231 | 18.3.00.08 | PIGH-related Glycosylphosphatidylinositol biosynthesis defect (CDG) | PIGH | 618010 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.500) |
| [ ] | 1143 | 18.3.00.09 | PIGL-related GPI biosynthesis defect (CDG) | PIGL | 280000 | 3474 | MAPPED -> CHIME_syndrome (alias_exact:chime syndrome) |
| [ ] | 627 | 18.3.00.11 | PIGW-related Hyperphosphatasia with mental retardation syndrome 5 (CDG) | PIGW | 616025 | 83639 | UNMAPPED; weak candidate CHIME_syndrome (0.590) |
| [ ] | 361 | 18.3.00.12 | PIGM-related Phosphatidylinositolglycan, class M, deficiency (CDG) | PIGM | 610293 | 83639 | UNMAPPED; weak candidate MHC class II deficiency 1 (0.568) |
| [ ] | 1144 | 18.3.00.13 | PIGV-related GPI biosynthesis defect (CDG) | PIGV | 239300 | 247262 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 1145 | 18.3.00.14 | PIGN-related GPI biosynthesis defect (CDG) | PIGN | 614080 | 280633 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 1146 | 18.3.00.15 | PIGO-related GPI biosynthesis defect (CDG) | PIGO | 614749 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 629 | 18.3.00.16 | PIGG-related Glycosylphosphatidylinpsitol biosynthesis defect 13 (CDG) | PIGG | 616917 | 488635 | UNMAPPED |
| [ ] | 1147 | 18.3.00.17 | PIGT-related GPI biosynthesis defect (CDG) | PIGT | 615398 | 369837 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 1148 | 18.3.00.18 | GPAA1-related GPI biosynthesis defect (CDG) | GPAA1 | 617810 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 630 | 18.3.00.19 | PGAP1-related GPI deacylase deficiency (CDG) | PGAP1 | 615802 | 88616 | UNMAPPED |
| [ ] | 631 | 18.3.00.20 | PGAP3-related Hyperphosphatasia with mental retardation syndrome 4 (CDG) | PGAP3 | 615716 | 247262 | UNMAPPED; weak candidate CHIME_syndrome (0.584) |
| [ ] | 1149 | 18.3.00.21 | PGAP2-related GPI biosynthesis defect (CDG) | PGAP2 | 614207 | 247262 | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.603) |
| [ ] | 1306 | 18.3.00.22 | PIGS-related Glycosylphosphatidylinositol class S deficiency (CDG) | PIGS | 618143 | - | UNMAPPED; weak candidate MHC class II deficiency 1 (0.526) |
| [ ] | 1388 | 18.3.00.23 | PIGB-related Developmental and epileptic encephalopathy (CDG) | PIGB | 604122 | - | CANDIDATE -> CN-Related Developmental and Epileptic Encephalopathy (0.955) |
| [ ] | 1219 | 18.3.00.24 | PIGP-related GPI biosynthesis defect (CDG) | PIGP | 617599 | 1934 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.755) |
| [ ] | 386 | 18.3.00.25 | PIGY-related Phosphatidylinositolglycan, class V, deficiency (CDG) | PIGY | 239300 | 247262 | UNMAPPED; weak candidate CHIME_syndrome (0.635) |
| [ ] | 1731 | 18.3.01.01 | PIGU-related Neurodevelopmental disorder with brain anomalies, seizures, and scoliosis (CDG) | PIGU | 618590 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.728) |
| [ ] | 1732 | 18.3.01.02 | PIGK-related Neurodevelopmental disorder with hypotonia and cerebellar atrophy, with or without seizures (CDG) | PIGK | 618879 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.663) |
| [ ] | 1764 | 18.3.01.03 | PIGF-related Onychodystrophy, osteodystrophy, impaired intellectual development, and seizures syndrome (CDG) | PIGF | 619356 | - | UNMAPPED; weak candidate DOORS Syndrome (0.778) |
| [ ] | 2041 | 18.3.01.04 | C18ORF32-related Neurodevelopmental disorder-CDG | C18ORF32 | 619985 | - | CANDIDATE -> Bosch-Boonstra-Schaaf Optic Atrophy Syndrome (0.931) |
| [ ] | 2066 | 18.3.1.05 | ARV1-related Fatty acid homeostasis modulator deficiency | ARV1 | 617020 | - | CANDIDATE -> DEE13 (0.978) |

### WP-059: Disorders of multiple glycosylation pathways (part 1 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of multiple glycosylation pathways
- Records: 22 (MAPPED 2, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 340 | 18.4.01.01 | SLC35A1-related CMP-sialic acid transporter deficiency (CDG) | SLC35A1 | 603585 | 238459 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.744) |
| [ ] | 346 | 18.4.01.02 | ATP6VOA2-related Cutis laxa, type IIA (CDG) | ATP6V0A2 | 219200;278250 | 357074 | UNMAPPED; weak candidate Peeling Skin Syndrome (0.762) |
| [ ] | 598 | 18.4.01.03 | GMPPA-related GDP-mannose pyrophosphorylase B deficiency (CDG) | GMPPA | 615510 | 869 | UNMAPPED; weak candidate CHIME_syndrome (0.692) |
| [ ] | 602 | 18.4.01.04 | DHDDS-related Dehydrodolichyl diphosphate synthase deficiency (CDG) | DHDDS | 613861;608172 | 442835 | CANDIDATE -> EYS-Related Retinitis Pigmentosa (0.957) |
| [ ] | 339 | 18.4.01.05 | GNE-related UDP-GlcNAc epimerase-kinase deficiency (CDG) | GNE | 600737;605820 | 602 | UNMAPPED; weak candidate Epimerase Deficiency (0.694) |
| [ ] | 2092 | 18.4.01.05 | DHDDS-related Dehydrodolichyl diphosphate synthase deficiency-CDG | DHDDS | 613861;608172 | 442835 | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.739) |
| [ ] | 599 | 18.4.02.01 | GMPPB-related Muscular dystrophy-dystroglycanopathy (CDG) | GMPPB | 615350;615351;615352 | 588 | CANDIDATE -> Dystroglycanopathy (0.949) |
| [ ] | 603 | 18.4.02.02 | NUS1-related Nogo-B receptor deficiency (CDG) | NUS1 | 617082 | 442835 | UNMAPPED; weak candidate GABRD (0.535) |
| [ ] | 2093 | 18.4.02.02 | NUS1-related cis-PTase deficiency-CDG | NUS1 | 617082 | 442835 | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.866) |
| [ ] | 612 | 18.4.02.03 | SLC35A2-related Early infantile epileptic encephalopathy-22 (CDG) | SLC35A2 | 314375 | 356961 | MAPPED -> SLC35A2-congenital disorder of glycosylation (alias_exact:cdg iim) |
| [ ] | 636 | 18.4.02.04 | ATP6V1A-related Cutis laxa, autosomal recessive, type IID (CDG) | ATP6V1A | 617403 | 357074 | UNMAPPED; weak candidate AR (0.686) |
| [ ] | 1299 | 18.4.02.05 | GNE-related UDP-GlcNAc epimerase/kinase superactivity (CDG) | GNE | 600737;605820 | 602 | UNMAPPED; weak candidate French-Canadian (0.550) |
| [ ] | 335 | 18.4.03.01 | SRD5A3-related Steroid 5 alpha-reductase 3 deficiency (CDG) | SRD5A3 | 612379 | 324737 | CANDIDATE -> 46,XY disorder of sex development due to 5-alpha-reductase 2 deficiency (0.925) |
| [ ] | 592 | 18.4.03.02 | NANS-related N-acetylneuraminic acid synthase deficiency (CDG) | NANS | 610442 | 168454 | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.792) |
| [ ] | 637 | 18.4.03.03 | ATP6V1E1-related Cutis laxa, autosomal recessive, type IIC (CDG) | ATP6V1E1 | 617402 | 357074 | UNMAPPED; weak candidate AR p47phox NCF1 (0.677) |
| [ ] | 1155 | 18.4.03.04 | SLC35A3-related UDP-N-acetylglucosamine transporter deficiency (CDG) | SLC35A3 | 615553 | 370943 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.767) |
| [ ] | 341 | 18.4.04.01 | SLC35C1-related GDP-fucose transporter deficiency (CDG) | SLC35C1 | 266265 | - | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.822) |
| [ ] | 342 | 18.4.04.02 | DOLK-related Dolichol kinase deficiency (CDG) | DOLK | 610768 | - | UNMAPPED |
| [ ] | 635 | 18.4.04.03 | ATP6AP1-related Immunodeficiency 47 and hepatopathy with or without neurologic features (CDG) | ATP6AP1 | 300972 | - | UNMAPPED; weak candidate IKBKG ectodermal dysplasia with immunodeficiency (0.610) |
| [ ] | 1153 | 18.4.04.04 | GFPT1-related Glutamine:fructose-6-phosphate transaminase deficiency (CDG) | GFPT1 | 610542 | 353327 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.882) |
| [ ] | 336 | 18.4.05.01 | DPM1-related GDP-Man:Dol-P mannosyltransferase subunit 1 deficiency (CDG) | DPM1 | 608799 | 79322 | UNMAPPED; weak candidate DPM1-related dystroglycanopathy (0.408) |
| [ ] | 351 | 18.4.05.02 | SLC35D1-related UDP-glucuronic acid-UDP-N-acetylgalactosamine dual transporter deficiency (CDG) | SLC35D1 | 269250 | 3144 | MAPPED -> Schneckenbecken Dysplasia (alias_exact:schneckenbecken dysplasia) |

### WP-060: Disorders of multiple glycosylation pathways (part 2 of 2)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Disorders of multiple glycosylation pathways
- Records: 14 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 5, UNMAPPED 8)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 600 | 18.4.05.03 | PGM1-related Phosphoglucomutase 1 deficiency (CDG) | PGM1 | 614921 | 319646 | CANDIDATE -> Glycogen Storage Disease Type I (0.938) |
| [ ] | 1157 | 18.4.05.04 | ATP6AP2-related X-linked mental retardation, Hedera type (CDG) | ATP6AP2 | 300423 | 93952 | UNMAPPED; weak candidate XL Complex HSP (0.584) |
| [ ] | 601 | 18.4.06.01 | PGM3-related Phosphoglucomutase 3 deficiency (CDG) | PGM3 | 615816;172100 | 443811 | CANDIDATE -> IMD33 (0.947) |
| [ ] | 604 | 18.4.06.02 | DPM2-related Dolichol-P-mannose synthase-2 deficiency (CDG) | DPM2 | 615042 | 329178 | UNMAPPED; weak candidate DPM2-related dystroglycanopathy (0.548) |
| [ ] | 634 | 18.4.06.03 | TMEM199-related Congenital disorder of glycosylation (CDG) | TMEM199 | 616829 | 466703 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 387 | 18.4.07.01 | DPM3-related GDP-Man:Dol-P mannosyltransferase 3 deficiency (CDG) | DPM3 | 612937 | 263494 | UNMAPPED; weak candidate DPM3-related dystroglycanopathy (0.444) |
| [ ] | 593 | 18.4.07.02 | CCDC115-related Congenital disorder of glycosylation (CDG) | CCDC115 | 616828 | 468684 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 337 | 18.4.08.01 | MPDU1-related Dol-P-Man utilization 1 deficiency (CDG) | MPDU1 | 609180 | 79323 | MAPPED -> MPDU1-congenital disorder of glycosylation (alias_exact:cdg if) |
| [ ] | 613 | 18.4.08.02 | TMEM165-related Congenital disorder of glycosylation (CDG) | TMEM165 | 614727;614726 | 314667 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 1353 | 18.4.08.03 | NPL-related N-Acetylneuraminate pyruvate lyase deficiency (CDG) | NPL | 611412 | - | UNMAPPED; weak candidate Hereditary Fructose Intolerance (0.731) |
| [ ] | 1578 | 18.4.09.01 | GNPNAT1-related Rhizomelic skeletal dysplasia (CDG) | GNPNAT1 | 616510 | - | UNMAPPED; weak candidate EDAR-Related Hypohidrotic Ectodermal Dysplasia (0.659) |
| [ ] | 1326 | 18.4.09.02 | SLC9A7-related Nonsyndromic intellectual disability (CDG) | SLC9A7 | 300368 | - | UNMAPPED; weak candidate MED13 Syndrome (0.730) |
| [ ] | 1733 | 18.4.30.01 | VMA21-related Myopathy, X-linked, with excessive autophagy (CDG) | VMA21 | 310440 | 25980 | UNMAPPED; weak candidate NDP-FEVR (0.562) |
| [ ] | 1761 | 18.4.30.02 | SLC37A4-related Glucose-6-phosphate (G6P) transporter deficiency (CDG) | SLC37A4 | 619525 | - | UNMAPPED |

### WP-061: Other disorders of multiple glycosylation pathways + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Congenital disorders of glycosylation
- Subgroup scope: Other disorders of multiple glycosylation pathways; Disorders of deglycosylation
- Records: 5 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 5)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1734 | 18.4.50.01 | UGDH-related Early infantile epileptic encephalopathy type 84 (CDG) | UGDH | 618792 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.745) |
| [ ] | 1735 | 18.4.50.02 | UGP2-related Early infantile epileptic encephalopathy type 83 (CDG) | UGP2 | 618744 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.725) |
| [ ] | 2186 | 18.4.51.01 | UGGT1-related UDP-glucose:glycoprotein glucosyltransferase 1 deficiency | UGGT1 | 605897 | - | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.623) |
| [ ] | 1158 | 18.5.01.01 | NGLY1-related N-Glycanase 1 deficiency (CDG) | NGLY1 | 615273 | 404454 | UNMAPPED |
| [ ] | 2023 | 18.5.02.01 | MAN2C1-related Mannosidase, alpha, class 2C, member 1 deficiency | MAN2C1 | 619775 | - | UNMAPPED; weak candidate 46,XY disorder of sex development due to 5-alpha-reductase 2 deficiency (0.619) |

### WP-062: Disorders of mitochondrial membrane biogenesis and remodeling + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of mitochondrial membrane biogenesis and remodeling; Disorders of mitochondrial and peroxisomal dynamics
- Records: 28 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 25)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 575 | 19.1.02.01 | SERAC1-related MEGDEL Syndrome | SERAC1 | 614739 | 352328 | UNMAPPED; weak candidate COX8A-Related COX Deficiency (0.483) |
| [ ] | 59 | 19.1.03.01 | TAZ-related Barth syndrome | TAZ | 302060 | - | MAPPED -> Barth syndrome (alias_exact:barth syndrome) |
| [ ] | 1011 | 19.1.04.01 | PNPLA8-related Mitochondrial myopathy with lactic acidosis | PNPLA8 | 251950 | 2597 | UNMAPPED; weak candidate Myopathy, Lactic Acidosis, and Sideroblastic Anemia (0.711) |
| [ ] | 1459 | 19.1.05.01 | PISD-related Phosphatidylserine decarboxylase deficiency | PISD | 612770 | - | UNMAPPED |
| [ ] | 1196 | 19.1.06.01 | PNPLA4-related Respiratory failure syndrome | PNPLA4 | 300102 | - | UNMAPPED; weak candidate Middle East Respiratory Syndrome (0.667) |
| [ ] | 1234 | 19.1.07.01 | MICOS13-related QIL1 deficiency | MICOS13 | 616658 | 67047 | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.710) |
| [ ] | 1580 | 19.1.08.01 | APOO-related MICOS complex subunit MIC26 deficiency | APOO | 300753 | - | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.698) |
| [ ] | 1581 | 19.1.09.01 | CHCHD2-related Parkinson disease 22 | CHCHD2 | 616710 | - | CANDIDATE -> Parkinson's Disease (0.919) |
| [ ] | 1346 | 19.1.11.01 | CHCHD10-related Spinal muscular atrophy, Jokela type | CHCHD10 | 615911;615048 | - | UNMAPPED; weak candidate SMA Type 1 (Werdnig-Hoffmann) (0.862) |
| [ ] | 2021 | 19.1.12.01 | CRLS1-related Cardiolipin synthase 1 deficiency | CRLS1 | 608188 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.742) |
| [ ] | 2037 | 19.1.13.01 | TAMM41-related Mitochondrial cytidine diphosphate-diacylglycerol synthase deficiency | TAMM41 | 614948 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.673) |
| [ ] | 2147 | 19.1.14.01 | PTPMT1-related Mitochondrial Protein-Tyr Phosphatase 1 deficiency | PTPMT1 | 609538 | - | UNMAPPED; weak candidate Beta-Ketothiolase Deficiency (0.687) |
| [ ] | 2176 | 19.1.15.01 | MICOS10-related Hepatocerebral mitochondrial DNA depletion syndrome | MICOS10 | 616574 | - | UNMAPPED; weak candidate Mitochondrial (0.809) |
| [ ] | 282 | 19.2.01.01 | DNM1L-related Dynamin-like protein 1 deficiency | DNM1L | 614388 | 98673 | UNMAPPED; weak candidate E3-binding protein deficiency (0.710) |
| [ ] | 416 | 19.2.01.02 | OPA1-related Childhood-onset optic atrophy type 1 | OPA1 | 165500 | 98673 | UNMAPPED; weak candidate Autosomal Dominant Optic Atrophy Plus (0.542) |
| [ ] | 421 | 19.2.01.03 | OPA1-related Optic Atrophy 1 and Deafness | OPA1 | 125250 | 98673 | UNMAPPED; weak candidate Autosomal Dominant Optic Atrophy Plus (0.552) |
| [ ] | 60 | 19.2.02.01 | OPA3-related Methylglutaconic aciduria type 3 | OPA3 | 258501 | - | UNMAPPED; weak candidate Glutaryl-CoA Dehydrogenase Deficiency (0.786) |
| [ ] | 1004 | 19.2.02.02 | MFF-related Mitochondrial fission factor deficiency | MFF | 617086 | 485421 | UNMAPPED; weak candidate Mitochondrial Trifunctional Protein Deficiency (0.729) |
| [ ] | 1005 | 19.2.03.01 | GDAP1-related Axonal Charcot-Marie-Tooth type 2K | GDAP1 | 607831;214400 | 99944 | UNMAPPED; weak candidate Charcot-Marie-Tooth Disease Type 2 (0.795) |
| [ ] | 1008 | 19.2.03.02 | MFN2-related Mitofusin 2-related disorder | MFN2 | 609260;617087 | 99947 | UNMAPPED; weak candidate Charcot-Marie-Tooth Disease Type 2 (0.658) |
| [ ] | 1006 | 19.2.04.01 | STAT2-related Immunodeficiency type 44 | STAT2 | 616636 | 431166 | UNMAPPED; weak candidate STAT2 Deficiency (0.593) |
| [ ] | 1009 | 19.2.04.02 | MSTO1-related Mitochondrial myopathy and ataxia | MSTO1 | 617675 | 502423 | UNMAPPED; weak candidate Myopathy, Lactic Acidosis, and Sideroblastic Anemia (0.800) |
| [ ] | 1007 | 19.2.05.01 | SLC25A46-related UGO-1 like protein deficiency | SLC25A46 | 616505 | 90120 | CANDIDATE -> Adult Refsum Disease (0.968) |
| [ ] | 1582 | 19.2.05.02 | MIEF2-related Mitochondrial elongation factor 2 deficiency | MIEF2 | 619024 | - | UNMAPPED; weak candidate Myopathy, Lactic Acidosis, and Sideroblastic Anemia (0.800) |
| [ ] | 2128 | 19.2.05.03 | MIEF1-related Mitochondrial elongation factor 1 disorder | MIEF1 | 620550 | - | UNMAPPED; weak candidate Mitochondrial (0.600) |
| [ ] | 1583 | 19.2.06.01 | SPART-related Spartin deficiency | SPART | 275900 | 101000 | UNMAPPED |
| [ ] | 1035 | 19.2.07.01 | TRAK1-related Trafficking kinesin-binding protein 1 deficiency | TRAK1 | 608112 | 442835 | UNMAPPED; weak candidate E3-binding protein deficiency (0.727) |
| [ ] | 1584 | 19.2.07.02 | SPATA5-related Epilepsy, hearing loss, and mental retardation syndrome | AFG2A | 616577 | - | UNMAPPED; weak candidate CHIME_syndrome (0.691) |

### WP-063: Peroxisomal biogenesis disorders + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Peroxisomal biogenesis disorders; Disorders of lysosome-related organelle biogenesis
- Records: 33 (MAPPED 3, AMBIGUOUS 1, CANDIDATE 5, UNMAPPED 24)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 272 | 19.3.01.01 | PEX1-related Peroxin 1 deficiency | PEX1 | 234580;214100;601539 | 772 | CANDIDATE -> Peroxisome Biogenesis Disorder (0.952) |
| [ ] | 1272 | 19.3.1.01 | PEX14-related Peroxin 14 deficiency | PEX14 | 614887 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.811) |
| [ ] | 1264 | 19.3.02.01 | PEX2-related Peroxin 2 deficiency | PEX2 | 614866;614867 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.822) |
| [ ] | 1265 | 19.3.03.01 | PEX3-related Peroxin 3 deficiency | PEX3 | 617370;614882 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.811) |
| [ ] | 1267 | 19.3.05.01 | PEX6-related Peroxin 6 deficiency | PEX6 | 614862;614863;616617 | 95433 | UNMAPPED; weak candidate Zellweger Spectrum Disorders (0.714) |
| [ ] | 1268 | 19.3.06.01 | PEX10-related Peroxin 10 deficiency | PEX10 | 614870;614871 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.822) |
| [ ] | 1269 | 19.3.07.01 | PEX11B-related Peroxin 14B deficiency | PEX11B | 614920 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.811) |
| [ ] | 1270 | 19.3.08.01 | PEX12-related Peroxin 12 deficiency | PEX12 | 614859;266510 | 772 | UNMAPPED; weak candidate Zellweger Spectrum Disorders (0.889) |
| [ ] | 1271 | 19.3.09.01 | PEX13-related Peroxin 13 deficiency | PEX13 | 614883;614885 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.811) |
| [ ] | 1273 | 19.3.11.01 | PEX16-related Peroxin 16 deficiency | PEX16 | 614876;614877 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.822) |
| [ ] | 1274 | 19.3.12.01 | PEX19-rerlasted Peroxin 19 deficiency | PEX19 | 614886 | 772 | CANDIDATE -> Peroxisome Biogenesis Disorder (0.938) |
| [ ] | 1275 | 19.3.13.01 | PEX26-related Peroxin 26 deficiency | PEX26 | 614872;614873 | 772 | UNMAPPED; weak candidate Peroxisome Biogenesis Disorder (0.822) |
| [ ] | 1266 | 19.3.14.01 | PEX5-related Peroxin 5 deficiency | PEX5 | 214110 | 468717 | CANDIDATE -> Peroxisome Biogenesis Disorder (0.952) |
| [ ] | 1112 | 19.3.15.01 | PEX5-related Peroxin 5 long isoform deficiency | PEX5 | 616716 | 468717 | UNMAPPED |
| [ ] | 1602 | 19.4.01.01 | VPS33B-related Arthrogryposis-renal dysfunction-cholestasis syndrome type 1 | VPS33B | 208085 | 2697 | UNMAPPED; weak candidate Multisystemic smooth muscle dysfunction syndrome (0.532) |
| [ ] | 1611 | 19.4.1.01 | BLOC1S3-related Hermansky-Pudlak syndrome type 8 | BLOC1S3 | 614077 | 231537 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 587 | 19.4.02.01 | VPS11-related Hypomyelinating leukodystrophy type 12 | VPS11 | 616683 | 466934 | UNMAPPED; weak candidate Hypomyelinating Leukodystrophy 7 (0.886) |
| [ ] | 1604 | 19.4.03.01 | HPS1-related Hermansky-Pudlak syndrome type 1 | HPS1 | 203300 | 231500 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1605 | 19.4.04.01 | AP3B1-related Hermansky-Pudlak syndrome type 2 | AP3B1 | 608233 | - | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1606 | 19.4.05.01 | HPS3-related Hermansky-Pudlak syndrome type 3 | HPS3 | 614072 | 231512 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1607 | 19.4.06.01 | HPS4-related Hermansky-Pudlak syndrome type 4 | HPS4 | 614073 | 231500 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1608 | 19.4.07.01 | HPS5-related Hermansky-Pudlak syndrome type 5 | HPS5 | 614074 | 231512 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1609 | 19.4.08.01 | HPS6-related Hermansky-Pudlak syndrome type 6 | HPS6 | 614075 | 231512 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1610 | 19.4.09.01 | DTNBP1-related Hermansky-Pudlak syndrome type 7 | DTNBP1 | 614075 | 231531 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1612 | 19.4.11.01 | BLOC1S6-related Hermansky-Pudlak syndrome type 9 | BLOC1S6 | 614171 | 280663 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.877) |
| [ ] | 1613 | 19.4.12.01 | AP3D1-related Hermansky-Pudlak syndrome type 10 | AP3D1 | 617050 | 284804 | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.862) |
| [ ] | 648 | 19.4.12.02 | VPS33A-related Mucopolysaccharidosis-plus syndrome | VPS33A | 617303 | 505248 | UNMAPPED; weak candidate Hurler syndrome (0.835) |
| [ ] | 1614 | 19.4.13.01 | LYST-related Chediak-Higashi syndrome | LYST | 214500 | 167;352723 | AMBIGUOUS: 2 local entities (alias_exact:chediak higashi syndrome) |
| [ ] | 1615 | 19.4.14.01 | MYO5A-related Griscelli syndrome type 1 | MYO5A | 214450 | 79476 | CANDIDATE -> Griscelli Type 2 (0.960) |
| [ ] | 1616 | 19.4.15.01 | RAB27A-related Griscelli syndrome type 2 | RAB27A | 607624 | 79477 | MAPPED -> Griscelli Type 2 (alias_exact:griscelli syndrome type 2) |
| [ ] | 1617 | 19.4.16.01 | MLPH-related Griscelli syndrome type 3 | MLPH | 609227 | 79478 | CANDIDATE -> Griscelli Type 2 (0.960) |
| [ ] | 1753 | 19.4.17.01 | GFAP-related Alexander disease | GFAP | 203450 | - | MAPPED -> Alexander Disease (identifier:OMIM:203450) |
| [ ] | 2241 | 19.4.18.01 | BLOC1S1-related Hypomyelinating leukodystrophy with epileptic encephalopathy | BLOC1S1 | 601444 | - | MAPPED -> BLOC1S1-related Complex Neurodevelopmental Disorder with Leukodystrophy (alias_exact:bloc1s1 related hypomyelinating leukodystrophy with epileptic encephalopathy) |

### WP-064: Disorders of organelle interplay

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of organelle interplay
- Records: 9 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1618 | 19.5.01.01 | EMC1-related Cerebellar atrophy, visual impairment, and psychomotor retardation | EMC1 | 616875 | 480898 | UNMAPPED; weak candidate Cerebellar Ataxia, Intellectual Disability, and Dysequilibrium Syndrome (0.496) |
| [ ] | 1619 | 19.5.02.01 | BAP31-related Deafness, dystonia, and cerebral hypomyelination | BCAP31 | 300475 | 369939;369942 | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.667) |
| [ ] | 1620 | 19.5.03.01 | VAPB-related Amyotrophic lateral sclerosis 8 | VAPB | 608627 | 209335;803 | MAPPED -> Amyotrophic Lateral Sclerosis (identifier:ORPHA:803) |
| [ ] | 1621 | 19.5.04.01 | VPS13A-related Choreoacanthocytosis | VPS13A | 200150 | 2388 | MAPPED -> Chorea-acanthocytosis (identifier:OMIM:200150) |
| [ ] | 1622 | 19.5.05.01 | VPS13C-related Autosomal recessive Parkinson disease type 23 | VPS13C | 616840 | 2828 | UNMAPPED; weak candidate Adult-Onset Dystonia-Parkinsonism (0.894) |
| [ ] | 1623 | 19.5.06.01 | VPS13D-related Spinocerebellar ataxia type 4 | VPS13D | 607317 | - | MAPPED -> Autosomal Recessive Cerebellar Ataxia-Saccadic Intrusion Syndrome (alias_exact:scar4) |
| [ ] | 1229 | 19.5.07.01 | ACBD5-related Acyl-CoA-binding domain-containing protein 5 deficiency | ACBD5 | 616618 | - | UNMAPPED; weak candidate Metachromatic Leukodystrophy (0.646) |
| [ ] | 1056 | 19.5.08.01 | COL4A3BP-related Ceramide transfer protein superactivity | COL4A3BP | 616351 | - | UNMAPPED; weak candidate Autosomal Dominant Osteopetrosis Type II (0.714) |
| [ ] | 633 | 19.5.11.01 | VPS13B-related Pepper syndrome (CDG) | VPS13B | 216550 | 193 | UNMAPPED; weak candidate GM3 synthase deficiency (0.741) |

### WP-065: Disorders of vesicular trafficking (part 1 of 4)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of vesicular trafficking
- Records: 22 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 6, UNMAPPED 12)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 344 | 19.6.01.01 | COG1-related Conserved oligomeric Golgi complex subunit 1 deficiency (CDG) | COG1 | 611209 | 263508 | MAPPED -> COG1-congenital disorder of glycosylation (identifier:ORPHA:263508) |
| [ ] | 632 | 19.6.1.01 | TRAPPC11-related Muscular dystrophy, limb-girdle, type 2S (CDG) | TRAPPC11 | 615356 | 369847 | UNMAPPED; weak candidate Limb-Girdle Muscular Dystrophy, Autosomal Dominant (0.747) |
| [ ] | 615 | 19.6.02.01 | COG4-related Conserved oligomeric Golgi complex subunit 4 deficiency (CDG) | COG4 | 613489 | 263501 | CANDIDATE -> COG1-congenital disorder of glycosylation (0.947) |
| [ ] | 1590 | 19.6.2.01 | TRAPPC2L-related Encephalopathy, progressive, early-onset, with episodic rhabdomyolysis | TRAPPC2L | 618331 | - | UNMAPPED; weak candidate Progressive Encephalomyelitis with Rigidity and Myoclonus (0.548) |
| [ ] | 388 | 19.6.03.01 | COG5-related Conserved oligomeric Golgi complex subunit 5 deficiency (CDG) | COG5 | 613612 | 263487 | CANDIDATE -> COG1-congenital disorder of glycosylation (0.947) |
| [ ] | 1600 | 19.6.3.01 | SCYL1-related Geroderma osteodysplasticum | GORAB | 231070 | 2078 | UNMAPPED; weak candidate CALFAN Syndrome (0.548) |
| [ ] | 389 | 19.6.04.01 | COG6-related Component of COG complex 6 deficiency (CDG) | COG6 | 606977;614576 | 464443 | UNMAPPED; weak candidate COX14-Related COX Deficiency (0.705) |
| [ ] | 1376 | 19.6.4.01 | AP4M1-related Spastic paraplegia | AP4M1 | 602296 | - | CANDIDATE -> SPG4 (0.947) |
| [ ] | 343 | 19.6.05.01 | COG7-related Conserved oligomeric Golgi complex subunit 7 deficiency (CDG) | COG7 | 608779 | 79333 | MAPPED -> COG7-congenital disorder of glycosylation (identifier:ORPHA:79333) |
| [ ] | 1643 | 19.6.5.01 | RAB3GAP1-related  Warburg micro syndrome type 1 | RAB3GAP1 | 600118 | 2510;1387 | MAPPED -> Warburg micro syndrome (identifier:ORPHA:2510) |
| [ ] | 345 | 19.6.06.01 | COG8-related Conserved oligomeric Golgi complex subunit 8 deficiency (CDG) | COG8 | 611182 | 95428 | CANDIDATE -> COG1-congenital disorder of glycosylation (0.947) |
| [ ] | 1156 | 19.6.07.01 | JAGN1-related Jagunal 1 deficiency (CDG) | JAGN1 | 616022 | 423384 | UNMAPPED; weak candidate Severe Congenital Nemaline Myopathy (0.704) |
| [ ] | 391 | 19.6.08.01 | SEC23B-related Congenital dyserythropoietic anemia type 2 (CDG) | SEC23B | 224100 | 98873 | CANDIDATE -> CDA II (0.955) |
| [ ] | 390 | 19.6.09.01 | TRIP11-related Achondrogenesis type IA (CDG) | TRIP11 | 200600 | 93299 | UNMAPPED; weak candidate Achondrogenesis Type II (0.857) |
| [ ] | 594 | 19.6.09.02 | TANGO2-related Recurrent metabolic encephalomyopathic crises associated with rhabdomyolysis, cardiac arrhythmias, and neurodegeneration | TANGO2 | 616878 | 480864 | UNMAPPED; weak candidate pantothenate kinase-associated neurodegeneration (0.453) |
| [ ] | 1321 | 19.6.12.01 | COG4-related Saul-Wilson syndrome (CDG) | COG4 | 618150 | 263501 | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.850) |
| [ ] | 1325 | 19.6.13.01 | GOSR2-related Epilepsy, progressive myoclonic (CDG) | GOSR2 | 614018 | - | UNMAPPED; weak candidate Progressive Myoclonus Epilepsy (0.688) |
| [ ] | 614 | 19.6.14.01 | COG2-related Conserved oligomeric Golgi complex subunit 2 deficiency (CDG) | COG2 | 606974 | - | CANDIDATE -> COG1-congenital disorder of glycosylation (0.947) |
| [ ] | 1585 | 19.6.15.01 | COPA-related Autoimmune interstitial lung, joint, and kidney disease | COPA | 616414 | 444092 | MAPPED -> COPA Syndrome (alias_exact:ailjk) |
| [ ] | 1586 | 19.6.16.01 | COPB2-related Microcephaly 19 | COPB2 | 617800 | 2512 | UNMAPPED; weak candidate TUBB/TUBB5-related Microcephaly (0.889) |
| [ ] | 1587 | 19.6.17.01 | ARCN1-related Archain 1 deficiency | ARCN1 | 617164 | - | UNMAPPED; weak candidate Stromme Syndrome (0.526) |
| [ ] | 1588 | 19.6.18.01 | SEC23A-related Craniolenticulosutural dysplasia | SEC23A | 607812 | 50814 | UNMAPPED; weak candidate Cranioectodermal Dysplasia (0.759) |

### WP-066: Disorders of vesicular trafficking (part 2 of 4)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of vesicular trafficking
- Records: 22 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 16)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1589 | 19.6.19.01 | TRAPPC2-related Spondyloepiphyseal dysplasia tarda | TRAPPC2 | 313400 | 93284 | UNMAPPED; weak candidate Spondyloepiphyseal Dysplasia Congenita (0.861) |
| [ ] | 1591 | 19.6.21.01 | TRAPPC4-related Neurodevelopmental disorder with epilepsy, spasticity, and brain atrophy | TRAPPC4 | 618741 | 528084 | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.734) |
| [ ] | 1592 | 19.6.22.01 | TRAPPC6B-related Neurodevelopmental disorder with microcephaly, epilepsy, and brain atrophy | TRAPPC6B | 617862 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.766) |
| [ ] | 1593 | 19.6.23.01 | TRAPPC9-related Mental retardation, autosomal recessive 13 (CDG) | TRAPPC9 | 613192 | 88616;352530 | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.738) |
| [ ] | 1594 | 19.6.24.01 | TRAPPC12-related Encephalopathy, progressive, early-onset, with brain atrophy and spasticity | TRAPPC12 | 617669 | 500144 | UNMAPPED; weak candidate Hashimoto Encephalopathy (0.522) |
| [ ] | 1595 | 19.6.25.01 | VPS45-related Neutropenia, severe congenital, 5 | VPS45 | 615285 | 369852 | UNMAPPED; weak candidate Severe Congenital Nemaline Myopathy (0.545) |
| [ ] | 1596 | 19.6.26.01 | VIPAS39-related Arthrogryposis-renal dysfunction-cholestasis syndrome type 2 | VIPAS39 | 613404 | 2697 | UNMAPPED; weak candidate Biotin-Thiamine-Responsive Basal Ganglia Disease (0.549) |
| [ ] | 1597 | 19.6.27.01 | NBAS-related Infantile liver failure syndrome 2 | NBAS | 608025 | 616483 | UNMAPPED; weak candidate GM3 synthase deficiency (0.687) |
| [ ] | 1598 | 19.6.28.01 | SCYL1-related Spinocerebellar ataxia, autosomal recessive 21 | SCYL1 | 616719 | 466794 | MAPPED -> CALFAN Syndrome (identifier:OMIM:616719) |
| [ ] | 1599 | 19.6.29.01 | SCYL2-related Arthrogryposis multiplex congenita 4, neurogenic, with agenesis of the corpus callosum | SCYL2 | 618766 | - | UNMAPPED; weak candidate Agenesis of the Corpus Callosum with Peripheral Neuropathy (0.613) |
| [ ] | 1601 | 19.6.31.01 | UNC13D-related Famillial hemophagocytic lymphohistiocytosis type 3 | UNC13D | 608898 | 540 | MAPPED -> FHL3 (alias_exact:fhl3) |
| [ ] | 1624 | 19.6.32.01 | STX11-related Famillial hemophagocytic lymphohistiocytosis type 4 | STX11 | 603552 | 540 | MAPPED -> FHL4 (alias_exact:fhl4) |
| [ ] | 1625 | 19.6.33.01 | STXBP2-related Famillial hemophagocytic lymphohistiocytosis type 5 | STXBP2 | 613101 | 540 | MAPPED -> FHL5 (alias_exact:fhl5) |
| [ ] | 1626 | 19.6.34.01 | ARFGEF2 deficiency | ARFGEF2 | 608097 | 98892 | UNMAPPED; weak candidate Periventricular Nodular Heterotopia (0.675) |
| [ ] | 1627 | 19.6.35.01 | AP1S2-related Mental retardation, X-linked syndromic 5 | AP1S2 | 304340 | 85335;1568;85329 | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.641) |
| [ ] | 1628 | 19.6.36.01 | AP2S1-related Hypocalciuric hypercalcemia type 3 | AP2S1 | 600740 | 101050 | UNMAPPED; weak candidate Infantile Hypercalcemia (0.688) |
| [ ] | 1629 | 19.6.37.01 | AP3B2-related  Early infantile epileptic encephalopathy type 48 | AP3B2 | 617276 | 442835 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 1375 | 19.6.38.01 | AP4B1-related Spastic paraplegia | AP4B1 | 607245 | - | UNMAPPED; weak candidate Complex Hereditary Spastic Paraplegia (0.696) |
| [ ] | 1377 | 19.6.39.01 | AP4E1-rerlated Spastic paraplegia | AP4E1 | 607244 | - | UNMAPPED; weak candidate Hereditary Spastic Paraplegia 48 (0.789) |
| [ ] | 1374 | 19.6.41.01 | AP4S1-related Spastic paraplegia | AP4S1 | 607243 | - | CANDIDATE -> SPG4 (0.947) |
| [ ] | 1635 | 19.6.42.01 | AAGAB-related p34 deficiency | AAGAB | 148600 | 79501 | UNMAPPED; weak candidate Punctate Palmoplantar Keratoderma (0.667) |
| [ ] | 1636 | 19.6.43.01 | RUBCN-related Rubicon deficiency | RUBCN | 615705 | 404499 | CANDIDATE -> CALFAN Syndrome (0.980) |

### WP-067: Disorders of vesicular trafficking (part 3 of 4)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of vesicular trafficking
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 19)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1637 | 19.6.44.01 | NBEAL2-related Grey platelet syndrome | NBEAL2 | 139090 | 721 | UNMAPPED; weak candidate Platelet-Type von Willebrand Disease (0.448) |
| [ ] | 1638 | 19.6.45.01 | LMAN1-related Combined factor V and factor VIII deficiency type 1 | LMAN1 | 227300 | 35909 | UNMAPPED; weak candidate Combined Saposin Deficiency (0.610) |
| [ ] | 1639 | 19.6.46.01 | MCFD2-related Combined factor V and factor VIII deficiency type 2 | MCFD2 | 613625 | 35909 | UNMAPPED |
| [ ] | 1640 | 19.6.47.01 | DYM-related Dymeclin deficiency | DYM | 223800;607326 | - | UNMAPPED; weak candidate Amniotic Band Syndrome (0.700) |
| [ ] | 1641 | 19.6.48.01 | RAB23-related Carpenter syndrome | RAB23 | 201000 | 65759 | UNMAPPED; weak candidate Wieacker-Wolff Syndrome (0.857) |
| [ ] | 1642 | 19.6.49.01 | RAB18-related Warburg micro syndrome type 3 | RAB18 | 614222 | 2510 | MAPPED -> Warburg micro syndrome (identifier:ORPHA:2510) |
| [ ] | 1693 | 19.6.51.01 | YIF1B-related Kaya-Barakat-Masson syndrome | YIF1B | 619125 | - | UNMAPPED |
| [ ] | 1644 | 19.6.51.02 | RAB3GAP2-related Warburg micro syndrome type 2 | RAB3GAP2 | 614225;212720 | 2510;1387;401830 | MAPPED -> Warburg micro syndrome (identifier:ORPHA:2510) |
| [ ] | 1694 | 19.6.52.01 | VPS4A-related CIMDAG syndrome | VPS4A | 609982 | - | UNMAPPED |
| [ ] | 1747 | 19.6.53.01 | VPS41-related Early onset dystonia | VPS41 | 605485 | - | UNMAPPED; weak candidate Early-onset FECD (0.722) |
| [ ] | 1746 | 19.6.54.01 | VPS16-related Dystonia 30 | VPS16 | 619291 | - | UNMAPPED; weak candidate SGCE-related myoclonus-dystonia (0.643) |
| [ ] | 1765 | 19.6.55.01 | STX5-related Syntaxin-5 deficiency (CDG) | STX5 | 620454 | - | UNMAPPED; weak candidate STX1B (0.464) |
| [ ] | 1766 | 19.6.56.01 | RINT1-related Infantile liver failure syndrome 3 (CDG) | RINT1 | 618641 | - | UNMAPPED; weak candidate GM3 synthase deficiency (0.648) |
| [ ] | 1767 | 19.6.57.01 | ATP9A-rerlated Neurodevelopmental disorder with poor growth and behavioral abnormalities | ATP9A | 609126 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.651) |
| [ ] | 2008 | 19.6.58.01 | AP1G1-related Usmani-Riazuddin syndrome | AP1G1 | 619467 | - | UNMAPPED |
| [ ] | 2009 | 19.6.59.01 | VPS50-related Neurodevelopmental disorder with microcephaly, seizures, and neonatal cholestasis | VPS50 | 619685 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.718) |
| [ ] | 2025 | 19.6.60.01 | CAMLG-related CDG | CAMLG | 601118 | - | UNMAPPED |
| [ ] | 2026 | 19.6.61.01 | GET4-related CDG | GET4 | 612056 | - | UNMAPPED |
| [ ] | 2027 | 19.6.62.01 | GET3-related CDG | GET3 | 601913 | - | UNMAPPED |
| [ ] | 2058 | 19.6.64.01 | COG3-related CDG | COG3 | 606975 | - | UNMAPPED |
| [ ] | 2083 | 19.6.65.01 | GM130-related Golgin A2 deficiency-CDG | GM130 | 620240 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.647) |
| [ ] | 2085 | 19.6.66.01 | STX16-related Syntaxin 16 deficiency-CDG | STX16 | 603233 | - | MAPPED -> PHP1B (alias_exact:php1b) |

### WP-068: Disorders of vesicular trafficking (part 4 of 4)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of organelle biogenesis, dynamics and interactions
- Subgroup scope: Disorders of vesicular trafficking
- Records: 5 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 3)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2086 | 19.6.67.01 | VPS51-related Pontocerebellar hypoplasia-CDG | VPS51 | 618606 | - | CANDIDATE -> PCH1A (0.971) |
| [ ] | 2087 | 19.6.68.01 | VPS53-related Pontocerebellar hypoplasia-CDG | VPS53 | 615851 | - | CANDIDATE -> PCH2 (0.985) |
| [ ] | 2096 | 19.6.69.01 | RAB5C-related RAS-associated protein deficiency | RAB5C | 604037 | - | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.769) |
| [ ] | 2097 | 19.6.70.01 | RAB33B-related Smith-McCort dysplasia 2 | RAB33B | 615222 | - | UNMAPPED; weak candidate Amniotic Band Syndrome (0.667) |
| [ ] | 2109 | 19.6.71.01 | GOLGA2-related Golgin A2 deficiency | GOLGA2 | 620240 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.647) |

### WP-069: Disorders of sphingolipid degradation + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of complex molecule degradation
- Subgroup scope: Disorders of sphingolipid degradation; Disorders of glycosaminoglycan degradation
- Records: 30 (MAPPED 20, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 5)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 288 | 20.1.01.01 | GBA-related Glucocerebrosidase deficiency | GBA | 230800 | 355 | MAPPED -> Gaucher Disease (identifier:OMIM:230800) |
| [ ] | 290 | 20.1.1.01 | ARSA-related Arylsulfatase A deficiency | ARSA | 250100 | 512 | MAPPED -> Metachromatic Leukodystrophy (alias_exact:metachromatic leukodystrophy) |
| [ ] | 294 | 20.1.02.01 | PSAP-related Gaucher disease-like disorder due to saposin C deficiency | PSAP | 610539 | 309263 | MAPPED -> Gaucher Disease Due To Saposin C Deficiency (alias_exact:saposin c deficiency) |
| [ ] | 298 | 20.1.03.01 | SMPD1-related Acid sphingomyelinase deficiency | SMPD1 | 257200;607616 | 77292 | CANDIDATE -> Niemann-Pick Disease Type A (0.901) |
| [ ] | 286 | 20.1.05.01 | HEXA-related Beta-hexosaminidase subunit alpha deficiency | HEXA | 272800 | 309192 | MAPPED -> Tay-Sachs Disease (identifier:OMIM:272800) |
| [ ] | 285 | 20.1.06.01 | HEXB-related Beta-hexosaminidase subunit beta deficiency | HEXB | 268800 | 796 | UNMAPPED; weak candidate Sandhoff Disease (0.571) |
| [ ] | 287 | 20.1.07.01 | GM2A-related GM2 activator protein deficiency | GM2A | 272750 | 309246 | MAPPED -> Tay-Sachs Disease AB Variant (alias_exact:gm2 activator protein deficiency) |
| [ ] | 289 | 20.1.08.02 | GALC-related Beta-galactosylceramidase deficiency | GALC | 245200 | 206448 | UNMAPPED; weak candidate Krabbe Disease (0.500) |
| [ ] | 292 | 20.1.09.01 | PSAP-related Krabbe disease-like disorder due to saposin A deficiency | PSAP | 611722 | 309263 | MAPPED -> Krabbe Disease Due To Saposin A Deficiency (alias_exact:saposin a deficiency) |
| [ ] | 293 | 20.1.11.01 | PSAP-related Metachromatic leukodystrophy-like disorder due to saposin B deficiency | PSAP | 249900 | 309263 | CANDIDATE -> Gaucher Disease Due To Saposin C Deficiency (0.950) |
| [ ] | 301 | 20.1.12.01 | SUMF1-related Formyl-glycine generating enzyme deficiency | SUMF1 | 272200 | 585 | AMBIGUOUS: 4 local entities (identifier:ORPHA:585) |
| [ ] | 296 | 20.1.13.01 | GLA-related Alpha-galactosidase A deficiency | GLA | 301500 | 324 | MAPPED -> Fabry disease (identifier:ORPHA:324) |
| [ ] | 248 | 20.1.14.01 | GLB1-related Beta-galactosidase 1 deficiency, Morquio B | GLB1 | 253010 | 354 | UNMAPPED; weak candidate Morquio syndrome (0.862) |
| [ ] | 284 | 20.1.14.01 | GLB1-related Beta-galactosidase-1 deficiency, GM1 gangliosis | GLB1 | 253010 | 79255 | UNMAPPED; weak candidate GM1 Gangliosidosis Type 1 (0.776) |
| [ ] | 297 | 20.1.14.01 | ASAH1-related Acid ceramidase deficiency, inflammatory phenotype | ASAH1 | 228000 | 333 | MAPPED -> Farber Disease (identifier:OMIM:228000) |
| [ ] | 1297 | 20.1.15.01 | ASAH1-related Acid ceramidase deficiency, primary neurologic phenotype | ASAH1 | 228000 | 333 | MAPPED -> Farber Disease (identifier:OMIM:228000) |
| [ ] | 291 | 20.1.16.01 | PSAP-related Combined saposin deficiency | PSAP | 611721 | 309263 | MAPPED -> Combined Saposin Deficiency (alias_exact:prosaposin deficiency) |
| [ ] | 1736 | 20.1.17.01 | SMPD4-related Neutral sphingomyelinase 3 deficiency | SMPD4 | 618622 | - | UNMAPPED; weak candidate Niemann-Pick Disease Type A (0.763) |
| [ ] | 241 | 20.2.01.01 | IDUA-related Alpha-iduronidase deficiency | IDUA | 607014;607015;607016 | 93473 | MAPPED -> Hurler syndrome (identifier:ORPHA:93473) |
| [ ] | 250 | 20.2.1.01 | GUSB-related Beta-glucuronidase deficiency | GUSB | 253220 | 584 | MAPPED -> Sly syndrome (identifier:ORPHA:584) |
| [ ] | 242 | 20.2.02.01 | IDS-related Iduronate 2-sulfatase deficiency | IDS | 309900 | 580 | MAPPED -> Hunter syndrome (identifier:ORPHA:580) |
| [ ] | 243 | 20.2.03.01 | SGSH-related Heparan N-sulfatase deficiency | SGSH | 252900 | 79269 | MAPPED -> MPS IIIA (alias_exact:mps 3a) |
| [ ] | 244 | 20.2.04.01 | NAGLU-related N-acetylglucosaminidase deficiency | NAGLU | 252920 | - | MAPPED -> MPS IIIB (alias_exact:mps 3b) |
| [ ] | 245 | 20.2.05.01 | HGSNAT-related Heparan-alpha-glucosaminide N-acetyltransferase deficiency | HGSNAT | 252930 | 79271 | MAPPED -> MPS IIIC (alias_exact:mps 3c) |
| [ ] | 246 | 20.2.06.01 | GNS-related N-Acetylglucosamine 6-sulfatase deficiency | GNS | 252940 | 79272 | MAPPED -> MPS IIID (alias_exact:mps 3d) |
| [ ] | 247 | 20.2.07.01 | GALNS-related N-Acetylgalactosamine 6-sulfatase deficiency | GALNS | 253000 | 309297 | MAPPED -> Type A (alias_exact:mucopolysaccharidosis type 4a) |
| [ ] | 249 | 20.2.09.01 | ARSB-related N-Acetylgalactosamine 4-sulfatase deficiency | ARSB | 253200 | - | MAPPED -> Maroteaux-Lamy syndrome (alias_exact:mps 6) |
| [ ] | 251 | 20.2.11.01 | HYAL1-related Hyaluronidase deficiency | HYAL1 | 601492 | 67041 | MAPPED -> Mucopolysaccharidosis type IX (alias_exact:hyaluronidase deficiency) |
| [ ] | 1323 | 20.2.13.01 | ARSG-related Arylsulfatase G deficiency | ARSG | 618144 | - | CANDIDATE -> Maroteaux-Lamy syndrome (0.962) |
| [ ] | 2017 | 20.2.17.01 | ARSK-related Arylsulfatase K deficiency | ARSK | 610011 | - | CANDIDATE -> Maroteaux-Lamy syndrome (0.962) |

### WP-070: Disorders of glycoprotein degradation + 1 adjacent subgroup(s)

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of complex molecule degradation
- Subgroup scope: Disorders of glycoprotein degradation; Neuronal ceroid lipofuscinosis
- Records: 24 (MAPPED 15, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 9)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 265 | 20.3.01.01 | NEU1-related Alpha-neuraminidase deficiency (CDG) | NEU1 | 256550 | 309294 | MAPPED -> Sialidosis type 1 (identifier:OMIM:256550) |
| [ ] | 319 | 20.3.02.01 | CTSA-related Cathepsin A deficiency | CTSA | 256540 | 351 | MAPPED -> Galactosialidosis (identifier:OMIM:256540) |
| [ ] | 260 | 20.3.03.01 | MAN2B1-related Alpha-mannosidase B deficiency | MAN2B1 | 248500 | 309288 | MAPPED -> Alpha-mannosidosis (identifier:OMIM:248500) |
| [ ] | 261 | 20.3.04.01 | MANBA-related Beta-mannosidase deficiency | MANBA | 248510 | 118 | MAPPED -> Beta Mannosidosis (identifier:ORPHA:118) |
| [ ] | 262 | 20.3.05.01 | Alpha-N-acetylgalactosaminidase deficiency | NAGA | 609241 | 79281 | MAPPED -> NAGA Deficiency Type 3 (identifier:ORPHA:79281) |
| [ ] | 263 | 20.3.05.02 | NAGA-related Alpha-N-acetylgalactosaminidase deficiency | NAGA | 609242 | 79280 | MAPPED -> Kanzaki Disease (alias_exact:kanzaki disease) |
| [ ] | 264 | 20.3.05.03 | Alpha-N-acetylgalactosaminidase deficiency | NAGA | 609241 | 79281 | MAPPED -> NAGA Deficiency Type 3 (identifier:ORPHA:79281) |
| [ ] | 259 | 20.3.06.01 | FUCA1-related Alpha-L-fucosidase deficiency | FUCA1 | 230000 | 349 | MAPPED -> Fucosidosis (identifier:OMIM:230000) |
| [ ] | 258 | 20.3.07.01 | AGA-related Aspartylglucosaminidase deficiency | AGA | 208400 | 93 | MAPPED -> Aspartylglucosaminuria (identifier:OMIM:208400) |
| [ ] | 306 | 20.4.01.01 | TPP1-related Tripeptidyl-peptidase 1 deficiency | TPP1 | 204500 | 168491 | MAPPED -> Neuronal Ceroid Lipofuscinosis 2 (alias_exact:cln2) |
| [ ] | 558 | 20.4.1.01 | ATP13A2-related Lysosomal type 5 P‐type ATPase deficiency | ATP13A2 | 606693 | 306674 | UNMAPPED; weak candidate Kufor-Rakeb syndrome (0.667) |
| [ ] | 307 | 20.4.02.01 | CLN3-related Lysosomal transmembrane protein deficiency | CLN3 | 204200 | 228346 | MAPPED -> Neuronal Ceroid Lipofuscinosis 3 (alias_exact:cln3) |
| [ ] | 309 | 20.4.03.01 | DNAJC5-related Kufs disease | DNAJC5 | 162350 | 228343 | MAPPED -> Adult Neuronal Ceroid Lipofuscinosis (alias_exact:kufs disease) |
| [ ] | 305 | 20.4.03.02 | PPT1-related Palmitoyl-protein thioesterase 1 deficiency | PPT1 | 256730 | 79263 | MAPPED -> Neuronal Ceroid Lipofuscinosis 1 (alias_exact:cln1) |
| [ ] | 310 | 20.4.04.01 | CLN5-related Lysosomal protein deficiency | CLN5 | 256731 | 228360 | UNMAPPED |
| [ ] | 308 | 20.4.05.01 | CLN6-related Kufs disease | CLN6 | 204300 | 228340 | MAPPED -> Adult Neuronal Ceroid Lipofuscinosis (alias_exact:kufs disease) |
| [ ] | 311 | 20.4.05.02 | CLN6-related Lysosomal protein deficiency | CLN6 | 601780 | 228340 | UNMAPPED |
| [ ] | 312 | 20.4.06.01 | MFSD8-related CLN7 Turkish variant | MFSD8 | 610951 | 228366 | MAPPED -> Neuronal Ceroid Lipofuscinosis 7 (alias_exact:cln7) |
| [ ] | 313 | 20.4.07.01 | CLN8-related Lysosomal protein deficiency | CLN8 | 600143 | 228354 | UNMAPPED |
| [ ] | 382 | 20.4.07.02 | CLN8-related Northern epilepsy variant | CLN8 | 610003 | 228354 | UNMAPPED |
| [ ] | 315 | 20.4.08.01 | CTSD-related Cathepsin D deficiency | CTSD | 610127 | 228337 | UNMAPPED; weak candidate Neuronal Ceroid Lipofuscinosis (0.667) |
| [ ] | 557 | 20.4.09.01 | GRN-related Progranulin deficiency | GRN | 614706 | 100070 | UNMAPPED |
| [ ] | 559 | 20.4.11.01 | CTSF-related Cathepsin F deficiency | CTSF | 603539 | 352709 | UNMAPPED; weak candidate Adult Neuronal Ceroid Lipofuscinosis (0.827) |
| [ ] | 560 | 20.4.12.01 | KCTD7-related CLN14 disease | KCTD7 | 611726 | 263516 | UNMAPPED; weak candidate Progressive Myoclonus Epilepsy (0.896) |

### WP-071: Disorders of autophagy

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of complex molecule degradation
- Subgroup scope: Disorders of autophagy
- Records: 29 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 6, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1100 | 20.5.01.01 | EPG5-related Vici syndrome | EPG5 | 242840 | 1493 | UNMAPPED |
| [ ] | 1373 | 20.5.1.01 | SQSTM1-related Frontotemporal dementia and/or amyotrophic lateral sclerosis | SQSTM1 | 616437 | - | UNMAPPED; weak candidate Amyotrophic Lateral Sclerosis (0.652) |
| [ ] | 617 | 20.5.02.01 | WDR45-related Neurodegeneration with brain iron accumulation 5 | WDR45 | 300894 | 329284 | MAPPED -> BPAN (alias_exact:neurodegeneration with brain iron accumulation 5) |
| [ ] | 1444 | 20.5.2.01 | ALS2-related Amyotrophic lateral sclerosis 2, juvenile | ALS2 | 205100 | - | UNMAPPED; weak candidate Amyotrophic Lateral Sclerosis (0.841) |
| [ ] | 1101 | 20.5.03.01 | SNX14-related Spinocerebellar ataxia 20 | SNX14 | 616354 | 397709 | CANDIDATE -> Autosomal Recessive (1.000) |
| [ ] | 1102 | 20.5.04.01 | SPG11-related Spatacsin deficiency | SPG11 | 602099 | 466775 | UNMAPPED; weak candidate SPG11 (0.423) |
| [ ] | 1439 | 20.5.04.02 | SPG11-related Spatacsin Spastic paraplegia type 11 | SPG11 | 604360 | 466775 | UNMAPPED; weak candidate SPG11 (0.737) |
| [ ] | 1440 | 20.5.04.03 | SPG11-related Axonal Charcot-Marie-Tooth disease type 2X | SPG11 | 616668 | 466775 | UNMAPPED; weak candidate SPG11 (0.215) |
| [ ] | 1103 | 20.5.05.01 | ZFYVE26-related Spastizin deficiency | ZFYVE26 | 270700 | 100996 | UNMAPPED; weak candidate AR Complex HSP (0.738) |
| [ ] | 1104 | 20.5.06.01 | AP5Z1-related  Spastic paraplegia 48 | AP5Z1 | 613647 | 306511 | MAPPED -> Hereditary Spastic Paraplegia 48 (alias_exact:spastic paraplegia 48) |
| [ ] | 1105 | 20.5.07.01 | TECPR2-related Spastic paraplegia 49 | TECPR2 | 615031 | 320385 | CANDIDATE -> SPG4 (0.976) |
| [ ] | 1106 | 20.5.08.01 | TBK1-related Frontotemporal dementia and/or amyotrophic lateral sclerosis type 4 | TBK1 | 616439 | 1930 | UNMAPPED; weak candidate Amyotrophic Lateral Sclerosis (0.604) |
| [ ] | 1107 | 20.5.09.01 | RAB7A-related Charcot-Marie-Tooth disease type 2B | RAB7A | 600882 | 99936 | MAPPED -> CMT2B (alias_exact:cmt2b) |
| [ ] | 1443 | 20.5.11.01 | SQSTM1-related Myopathy, distal, with rimmed vacuoles | SQSTM1 | 617158 | - | UNMAPPED |
| [ ] | 1442 | 20.5.12.01 | SQSTM1-related Neurodegeneration with ataxia, dystonia, and gaze palsy, childhood-onset | SQSTM1 | 617145 | - | UNMAPPED |
| [ ] | 1441 | 20.5.13.01 | SQSTM1-related Paget disease of bone 3 | SQSTM1 | 167250 | - | UNMAPPED |
| [ ] | 1378 | 20.5.18.01 | TBCK-related Hypotonia, infantile, with psychomotor retardation and characteristic facies | TBCK | 616899 | - | UNMAPPED; weak candidate Heart Failure with Preserved Ejection Fraction (HFpEF) (0.483) |
| [ ] | 1445 | 20.5.19.01 | ALS2-related Primary lateral sclerosis, juvenile | ALS2 | 606353 | - | UNMAPPED; weak candidate Primary Lateral Sclerosis (0.847) |
| [ ] | 1379 | 20.5.21.01 | ALS2-related Spastic paralysis (IAHSP) | ALS2 | 607225 | - | UNMAPPED; weak candidate Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity (0.772) |
| [ ] | 1446 | 20.5.22.01 | DCTN1-related Neuropathy, distal hereditary motor, type VIIB | DCTN1 | 607641 | - | MAPPED -> Distal Hereditary Motor Neuronopathy, Autosomal Dominant (identifier:OMIM:607641) |
| [ ] | 1380 | 20.5.23.01 | DCTN1-related Perry syndrome | DCTN1 | 168605 | - | UNMAPPED |
| [ ] | 1382 | 20.5.24.01 | MTMR14-related Centronuclear myopathy | MTMR14 | 611089 | - | AMBIGUOUS: 4 local entities (alias_exact:centronuclear myopathy) |
| [ ] | 1217 | 20.5.25.01 | ATG5-related Spinocerebellar ataxia | ATG5 | 617584 | - | UNMAPPED; weak candidate COQ8A (0.872) |
| [ ] | 1447 | 20.5.26.01 | CHMP2B-related Amyotrophic lateral sclerosis 17 | CHMP2B | 614696 | - | CANDIDATE -> Amyotrophic Lateral Sclerosis (0.951) |
| [ ] | 1383 | 20.5.27.01 | CHMP2B-related Dementia, familial, nonspecific | CHMP2B | 600795 | - | UNMAPPED; weak candidate Dementia with Lewy Bodies (0.481) |
| [ ] | 1768 | 20.5.28.01 | ATG7-related Spinocerebellar ataxia, autosomal recessive 31 | ATG7 | 619422 | - | CANDIDATE -> CALFAN Syndrome (0.978) |
| [ ] | 2052 | 20.5.29.01 | CHMP3-related Hereditary spastic paraplegia CHMP3 | CHMP3 | 610052 | - | CANDIDATE -> Hereditary Spastic Paraplegia (0.906) |
| [ ] | 2075 | 20.5.30.01 | WIPI2-related Intellectual developmental disorder with short stature and variable skeletal anomalies | WIPI2 | 618453 | - | UNMAPPED; weak candidate Snijders Blok-Campeau Syndrome (0.621) |
| [ ] | 2206 | 20.5.31.01 | ATG12-related Neurodevelopmental disorder | ATG12 | 609608 | - | CANDIDATE -> Bosch-Boonstra-Schaaf Optic Atrophy Syndrome (1.000) |

### WP-072: Other disorders of complex molecule degradation

- Classification: Complex Molecule and Organelle Metabolism -> Disorders of complex molecule degradation
- Subgroup scope: Other disorders of complex molecule degradation
- Records: 19 (MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 303 | 20.6.01.01 | NPC1-related Niemann-Pick disease type C1 | NPC1 | 257220 | 216981 | MAPPED -> NPC1 (alias_exact:niemann pick disease type c1) |
| [ ] | 1109 | 20.6.01.02 | CTSK-related Cathepsin K deficiency | CTSK | 265800 | 763 | MAPPED -> Pycnodysostosis (alias_exact:pycnodysostosis) |
| [ ] | 299 | 20.6.01.03 | GNPTAB-related UDP-N-acetylglucosamine-1-phosphotransferase subunit alpha/beta deficiency | GNPTAB | 252500 | 576 | MAPPED -> Mucolipidosis Type II (alias_exact:i cell disease) |
| [ ] | 556 | 20.6.01.04 | GNPTAB-related UDP-N-acetylglucosamine-1-phosphotransferase subunit alpha/beta deficiency (CDG) | GNPTAB | 252600 | 577 | MAPPED -> Mucolipidosis Type III Alpha/Beta (identifier:OMIM:252600) |
| [ ] | 300 | 20.6.02.01 | GNPTG-related UDP-N-acetylglucosamine-1-phosphotransferase subunit gamma deficiency (CDG) | GNPTG | 252605 | 577 | UNMAPPED; weak candidate GNPTG-Mucolipidosis (0.643) |
| [ ] | 304 | 20.6.02.02 | NPC2-related Niemann-Pick disease type C2 | NPC2 | 607625 | 216981 | MAPPED -> NPC2 (alias_exact:niemann pick disease type c2) |
| [ ] | 1110 | 20.6.02.03 | CTSC-related Cathepsin C deficiency | CTSC | 245010 | 2342 | UNMAPPED; weak candidate Galactosialidosis (0.737) |
| [ ] | 1448 | 20.6.02.04 | CTSC-related Cathepsin C deficiency | CTSC | 245000 | 2342 | UNMAPPED; weak candidate Galactosialidosis (0.737) |
| [ ] | 302 | 20.6.03.01 | LIPA-related Lysosomal acid lipase deficiency | LIPA | 278000 | 275761 | MAPPED -> Cholesteryl Ester Storage Disease (alias_exact:cholesteryl ester storage disease) |
| [ ] | 320 | 20.6.03.02 | SCARB2-related Glucocerebrosidase receptor deficiency | SCARB2 | 254900 | 163696 | UNMAPPED; weak candidate Gaucher Disease (0.866) |
| [ ] | 1108 | 20.6.03.03 | MCOLN1-related Mucolipin 1 deficiency | MCOLN1 | 252650 | 578 | MAPPED -> Mucolipidosis Type IV (alias_exact:mucolipidosis type 4) |
| [ ] | 1311 | 20.6.03.04 | CTSB-related Cathepsin B superactivity | CTSB | 148370 | - | UNMAPPED; weak candidate PRPS1 Superactivity (0.727) |
| [ ] | 1645 | 20.6.04.01 | MBTPS1-related Site-1 protease deficiency | MBTPS1 | 618392 | - | UNMAPPED; weak candidate Spondylometaphyseal Dysplasia Kozlowski Type (0.814) |
| [ ] | 486 | 20.6.05.01 | GAA-related Alpha-glucosidase deficiency | GAA | 232300 | 420429 | MAPPED -> Pompe Disease (identifier:OMIM:232300) |
| [ ] | 2088 | 20.6.07.01 | LYSET-related TMEM251 deficiency-CDG | LYSET | 619345 | - | UNMAPPED; weak candidate Arthrogryposis Multiplex Congenita (0.507) |
| [ ] | 2179 | 20.6.08.01 | CLCN7-related Chloride channel 7 superactivity | CLCN7 | 618541 | - | UNMAPPED |
| [ ] | 2185 | 20.6.09.01 | CLCN7-related Osteopetrosis, dominant | CLCN7 | 166600 | - | UNMAPPED; weak candidate Osteopetrosis (0.743) |
| [ ] | 2184 | 20.6.10.01 | CLCN7-related Osteopetrosis, recessive | CLCN7 | 611490 | - | UNMAPPED; weak candidate Osteopetrosis (0.722) |
| [ ] | 478 | 20.6.16.01 | LAMP2-related Lysosome-associated membrane protein 2 deficiency | LAMP2 | 300257 | 34587 | MAPPED -> Danon disease (identifier:ORPHA:34587) |

### WP-073: Disorders of tetrahydrobiopterin metabolism + 3 adjacent subgroup(s)

- Classification: Cofactor and Mineral Metabolism -> Disorders of vitamin and cofactor metabolism
- Subgroup scope: Disorders of tetrahydrobiopterin metabolism; Disorders of thiamine metabolism; Disorders of riboflavin metabolism; Disorders of niacin and NAD metabolism
- Records: 24 (MAPPED 4, AMBIGUOUS 1, CANDIDATE 4, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 3 | 21.1.02.01 | GCH1-related GTP cyclohydrolase I deficiency (GTPCH;ar) | GCH1 | 233910 | - | UNMAPPED |
| [ ] | 7 | 21.1.03.01 | GCH1-related GTP cyclohydrolase I deficiency (GTPCH;ad) | GCH1 | 600225 | - | UNMAPPED; weak candidate Dopa-Responsive Dystonia (0.762) |
| [ ] | 4 | 21.1.04.01 | PTS-related 6-Pyruvoyl-tetrahydropterin synthase deficiency (PTPS) | PTS | 261640 | - | MAPPED -> PTPS Deficiency (alias_exact:6 pyruvoyl tetrahydropterin synthase deficiency) |
| [ ] | 8 | 21.1.05.01 | SPR-related Sepiapterin reductase deficiency (SR) | SPR | 182125 | - | AMBIGUOUS: 2 local entities (alias_exact:sepiapterin reductase deficiency) |
| [ ] | 5 | 21.1.06.01 | QDPR-related Dihydropteridine reductase deficiency (DHPR) | QDPR | 261630 | - | MAPPED -> DHPR Deficiency (alias_exact:dihydropteridine reductase deficiency) |
| [ ] | 6 | 21.1.07.01 | PCBD1-related Pterin carbinolamine-4a-dehydratase deficiency (PCD) | PCBD1 | 264070 | - | UNMAPPED |
| [ ] | 95 | 21.2.01.01 | SLC19A2-related Thiamine transporter 1 deficiency | SLC19A2 | 603941 | - | UNMAPPED |
| [ ] | 392 | 21.2.02.01 | SLC19A3-related Thiamine transporter 2 deficiency | SLC19A3 | 606152 | 65284 | MAPPED -> Biotin-Thiamine-Responsive Basal Ganglia Disease (identifier:ORPHA:65284) |
| [ ] | 621 | 21.2.03.01 | TPK1-related Thiamine pyrophosphokinase deficiency | TPK1 | 614458 | 293955 | CANDIDATE -> Biotin-Thiamine-Responsive Basal Ganglia Disease (0.976) |
| [ ] | 393 | 21.2.04.01 | SLC25A19-related Mitochondrial thiamine pyrophosphate transporter deficiency | SLC25A19 | 606521 | 99742 | UNMAPPED; weak candidate GSD Ib (glucose-6-phosphate transporter deficiency) (0.667) |
| [ ] | 841 | 21.3.01.01 | SLC52A1-related Riboflavin transporter 1 deficiency | SLC52A1 | 615026 | 411712 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.806) |
| [ ] | 529 | 21.3.02.01 | SLC52A3-related Riboflavin transporter 2 deficiency | SLC52A3 | 211530 | 97229 | CANDIDATE -> Brown-Vialetto-Van Laere Syndrome (0.933) |
| [ ] | 530 | 21.3.02.02 | SLC52A3-related Fazio-Londe syndrome | SLC52A3 | 211500 | 97229 | UNMAPPED |
| [ ] | 1256 | 21.3.03.01 | SLC52A2-related Riboflavin transporter 3 deficiency | SLC52A2 | 614707 | 95433 | CANDIDATE -> Brown-Vialetto-Van Laere Syndrome (0.907) |
| [ ] | 842 | 21.3.04.01 | FLAD1-related Flavin adenine dinucleotide synthetase deficiency (late onset) | FLAD1 | 255100 | 394529 | UNMAPPED |
| [ ] | 843 | 21.3.05.01 | SLC25A32-related Mitochondrial flavin adenine dinucleotide transporter deficiency | SLC25A32 | 616839 | 394532 | UNMAPPED; weak candidate Tangier_Disease (0.618) |
| [ ] | 1695 | 21.3.06.01 | FLAD1-related Flavin adenine dinucleotide synthetase deficiency (early onset) | FLAD1 | 255100 | 394529 | UNMAPPED |
| [ ] | 844 | 21.4.01.01 | NMNAT1-related Nicotinamide mononucleotide adenylyl transferase 1 deficiency | NMNAT1 | 608553 | 65 | CANDIDATE -> CRB1 Retinal Dystrophies (0.964) |
| [ ] | 845 | 21.4.02.01 | NADK2-related Mitochondrial NAD kinase 2 deficiency | NADK2 | 616034 | 431361 | MAPPED -> DECR Deficiency (identifier:OMIM:616034) |
| [ ] | 846 | 21.4.03.01 | NAXE-related NAD(P)HX epimerase deficiency | NAXE | 617186 | - | UNMAPPED; weak candidate Epimerase Deficiency (0.816) |
| [ ] | 847 | 21.4.04.01 | NAXD-related NAD(P)HX dehydratase deficiency | NAXD | 615910 | - | UNMAPPED; weak candidate Inherited Threoninemia (0.762) |
| [ ] | 848 | 21.4.05.01 | NNT-related Nicotinamide nucleotide transhydrogenase deficiency | NNT | 614736 | 361 | UNMAPPED; weak candidate Galactosialidosis (0.595) |
| [ ] | 1737 | 21.4.06.01 | NADSYN1-related NAD synthetase 1 deficiency | NADSYN1 | 618845 | 521438 | UNMAPPED; weak candidate Lipoic Acid Synthetase Deficiency (0.800) |
| [ ] | 2205 | 21.4.07.01 | NMNAT3-related Nicotinamide mononucleotide adenylyl transferase 3 deficiency | NMNAT3 | 608702 | - | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.667) |

### WP-074: Disorders of pantothenate and CoA metabolism + 3 adjacent subgroup(s)

- Classification: Cofactor and Mineral Metabolism -> Disorders of vitamin and cofactor metabolism
- Subgroup scope: Disorders of pantothenate and CoA metabolism; Disorders of pyridoxine metabolism; Disorders of biotin metabolism; Disorders of folate metabolism
- Records: 24 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 209 | 21.5.01.01 | PANK2-related Pantothenate kinase 2 deficiency | PANK2 | 234200 | 216873 | MAPPED -> pantothenate kinase-associated neurodegeneration (alias_exact:hallervorden spatz disease) |
| [ ] | 1242 | 21.5.02.01 | PPCS-related Phosphopantothenoylcysteine synthetase deficiency | PPCS | 609853 | - | UNMAPPED; weak candidate AR-CNM (0.762) |
| [ ] | 620 | 21.5.03.01 | COASY-related Coenzyme A synthase deficiency | COASY | 615643 | 397725 | CANDIDATE -> BPAN (0.979) |
| [ ] | 1173 | 21.5.04.01 | SLC25A42-related Mitochondrial coenzyme a transporter deficiency | SLC25A42 | 610823 | - | UNMAPPED; weak candidate 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (0.750) |
| [ ] | 2111 | 21.5.05.01 | PPCDC-related Phosphopantothenoylcysteine decarboxylase deficiency | PPCDC | 609854 | - | MAPPED -> Dilated Cardiomyopathy (alias_exact:dilated cardiomyopathy) |
| [ ] | 76 | 21.6.01.01 | PNPO-related Pyridoxamine 5-phosphate oxidase deficiency | PNPO | 610090 | - | UNMAPPED; weak candidate COA3-Related COX Deficiency (0.687) |
| [ ] | 616 | 21.6.02.01 | PLPBP-related Pyridoxal 5'-phosphate binding protein deficiency | PLPBP | 617290 | 3006 | UNMAPPED; weak candidate E3-binding protein deficiency (0.727) |
| [ ] | 75 | 21.6.02.02 | ALDH7A1-related Alpha-amino adipic semialdehyde dehydrogenase deficiency | ALDH7A1 | 266100 | - | UNMAPPED; weak candidate Succinic Semialdehyde Dehydrogenase Deficiency (0.824) |
| [ ] | 561 | 21.6.03.01 | ALPL-related Tissue-nonspecific alkaline phosphatase deficiency | ALPL | 241500 | 436 | MAPPED -> Hypophosphatasia (identifier:ORPHA:436) |
| [ ] | 1174 | 21.6.04.01 | ALPI-related Intestinal alkaline phosphatase anchoring deficiency | ALPI | 171740 | - | UNMAPPED; weak candidate Lysosomal Acid Phosphatase Deficiency (0.659) |
| [ ] | 1738 | 21.6.05.01 | PDXK-related Pyridoxal kinase deficiency | PDXK | 618511 | - | UNMAPPED; weak candidate BCKDK Deficiency (0.776) |
| [ ] | 93 | 21.7.01.01 | BTD-related Biotinidase deficiency | BTD | 253260 | - | MAPPED -> Biotinidase Deficiency (alias_exact:biotinidase deficiency) |
| [ ] | 94 | 21.7.02.01 | HLCS-related Holocarboxylase synthetase deficiency | HLCS | 253270 | - | MAPPED -> Holocarboxylase Synthetase Deficiency (alias_exact:holocarboxylase synthetase deficiency) |
| [ ] | 1172 | 21.7.17.01 | SLC5A6-related Sodium-dependent multivitamin transporter deficiency | SLC5A6 | 604024 | - | UNMAPPED; weak candidate Infantile Parkinsonism-Dystonia (0.689) |
| [ ] | 70 | 21.8.01.01 | SLC46A1-related Proton-coupled folate transporter deficiency | SLC46A1 | 229050 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.711) |
| [ ] | 1646 | 21.8.1.01 | ALDH1L2-related Mitochondrial 10-formyltetrahydrofolate dehydrogenase deficiency | ALDH1L2 | 613584 | - | UNMAPPED; weak candidate 3B-HSD (0.655) |
| [ ] | 71 | 21.8.02.01 | FOLR1-related Folate receptor alpha deficiency | FOLR1 | 613068 | - | UNMAPPED; weak candidate E1-alpha deficiency (0.706) |
| [ ] | 72 | 21.8.03.01 | MTHFR-related 5,10-methylenetetrahydrofolate reductase deficiency | MTHFR | 236250 | - | UNMAPPED; weak candidate MTHFR deficiency (0.800) |
| [ ] | 551 | 21.8.04.01 | MTHFD1-related 5,10-Methylene-tetrahydrofolate dehydrogenase deficiency | MTHFD1 | 172460 | 268377 | UNMAPPED; weak candidate 3B-HSD (0.706) |
| [ ] | 73 | 21.8.05.01 | DHFR-related Dihydrofolate reductase deficiency | DHFR | 126060 | - | UNMAPPED; weak candidate DHPR Deficiency (0.845) |
| [ ] | 47 | 21.8.06.01 | FTCD-related Formimidoyltransferase cyclodeaminase deficiency | FTCD | 229100 | - | UNMAPPED; weak candidate Hereditary Orotic Aciduria (0.769) |
| [ ] | 580 | 21.8.07.01 | MTHFS-related 5,10-Methenyltetrahydrofolate synthetase deficiency | MTHFS | 604197 | - | UNMAPPED; weak candidate Carbamoyl Phosphate Synthetase I Deficiency (0.638) |
| [ ] | 1462 | 21.8.09.01 | SLC19A1-related Folate transporter 1 deficiency | SLC19A1 | 600424 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.825) |
| [ ] | 2143 | 21.8.11.01 | CIC-related Capicua deficiency | CIC | 612082 | - | UNMAPPED |

### WP-075: Disorders of cobalamin metabolism + 1 adjacent subgroup(s)

- Classification: Cofactor and Mineral Metabolism -> Disorders of vitamin and cofactor metabolism
- Subgroup scope: Disorders of cobalamin metabolism; Disorders of molybdenum cofactor metabolism
- Records: 24 (MAPPED 8, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 14)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 80 | 21.9.01.01 | CBLIF-related Intrinsic factor deficiency | CBLIF | 261000 | - | MAPPED -> Hereditary intrinsic factor deficiency (alias_exact:congenital pernicious anemia) |
| [ ] | 1396 | 21.9.1.01 | MMACHC; PRDX1-related Epi-cblC deficiency | MMACHC; PRDX1 | 609831;176763 | - | CANDIDATE -> MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.927) |
| [ ] | 82 | 21.9.02.01 | CUBN-related Cubilin deficiency | CUBN | 261100 | - | UNMAPPED; weak candidate Type III (0.533) |
| [ ] | 83 | 21.9.03.01 | AMN-related Amnionless deficiency | AMN | 261100 | - | UNMAPPED; weak candidate Type III (0.519) |
| [ ] | 84 | 21.9.04.01 | TCN1-related Haptocorrin deficiency | TCN1 | 193090 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.727) |
| [ ] | 85 | 21.9.05.01 | TCN2-related Transcobalamin 2 deficiency | TCN2 | 275350 | - | MAPPED -> TCN2 deficiency (alias_exact:tcn2 deficiency) |
| [ ] | 92 | 21.9.06.01 | CD320-related Transcobalamin receptor defect | CD320 | 613646 | - | UNMAPPED; weak candidate Methylmalonic Acidemia (0.764) |
| [ ] | 91 | 21.9.07.01 | LMBRD1-relasted Methylmalonic aciduria and homocystinuria, cblF type | LMBRD1 | 277380 | - | MAPPED -> cblF (alias_exact:cblf) |
| [ ] | 548 | 21.9.08.01 | ABCD4-related Methylmalonic aciduria and homocystinuria, cblJ type | ABCD4 | 614857 | 369955 | MAPPED -> cblJ (alias_exact:cblj) |
| [ ] | 90 | 21.9.09.01 | MMACHC-related Methylmalonic aciduria and homocystinuria, cblC type | MMACHC | 277400 | - | MAPPED -> cblC (alias_exact:cblc) |
| [ ] | 88 | 21.9.11.01 | MMADHC-related Methylmalonic aciduria, cblDv2 type | MMADHC | 277410 | - | UNMAPPED; weak candidate Inborn Disorder of Cobalamin Metabolism and Transport (0.452) |
| [ ] | 89 | 21.9.11.02 | MMADHC-related Homocystinuria, cblDv1 type | MMADHC | 277410 | - | UNMAPPED |
| [ ] | 316 | 21.9.11.03 | MMADHC-related Methylmalonic aciduria and homocystinuria, cblD type | MMADHC | 277410 | 79283 | UNMAPPED |
| [ ] | 31 | 21.9.12.01 | MTRR-related Methionine synthase reductase deficiency-cblE | MTRR | 236270 | - | MAPPED -> cblE (alias_exact:cble) |
| [ ] | 86 | 21.9.14.01 | MMAA-related Methylmalonic aciduria, cblA type | MMAA | 251100 | - | MAPPED -> cblA (alias_exact:cbla) |
| [ ] | 87 | 21.9.15.01 | MMAB-related Methylmalonic aciduria, cblB type | MMAB | 251110 | - | MAPPED -> cblB (alias_exact:cblb) |
| [ ] | 840 | 21.9.16.01 | HCFC1-related Methylmalonic aciduria and homocystinuria, cblX type | HCFC1 | 309541 | 369962 | CANDIDATE -> MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.980) |
| [ ] | 1386 | 21.9.18.01 | THAP11-related Methylmalonic aciduria and homocystinuria | THAP11 | 609119 | - | UNMAPPED; weak candidate cblC disease (0.891) |
| [ ] | 1385 | 21.9.19.01 | ZNF143-related Methylmalonic aciduria and homocystinuria | ZNF143 | 603433 | - | UNMAPPED; weak candidate cblC disease (0.891) |
| [ ] | 77 | 21.10.01.01 | MOCS1-related Molybdenum cofactor deficiency A | MOCS1 | 603707 | - | UNMAPPED; weak candidate FA-A (0.753) |
| [ ] | 78 | 21.10.02.01 | MOCS2-related Molybdopterin synthase deficiency | MOCS2 | 603708 | - | UNMAPPED; weak candidate PTPS Deficiency (0.775) |
| [ ] | 79 | 21.10.03.01 | GPHN-related Molybdenum cofactor deficiency C | GPHN | 603930 | - | UNMAPPED |
| [ ] | 867 | 21.10.04.01 | MOCOS-related Molybdenum cofactor sulfurase deficiency | MOCOS | 603592 | 93602 | UNMAPPED |
| [ ] | 1739 | 21.10.08.01 | MOCS3-related Molybdopterin synthase sulfurase deficiency | MOCS3 | 609277 | - | UNMAPPED; weak candidate PTPS Deficiency (0.689) |

### WP-076: Other disorders of vitamin metabolism

- Classification: Cofactor and Mineral Metabolism -> Disorders of vitamin and cofactor metabolism
- Subgroup scope: Other disorders of vitamin metabolism
- Records: 23 (MAPPED 7, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 14)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 494 | 21.11.01.01 | SLC2A10-related L-Dehydroascorbate transporter deficiency | SLC2A10 | 208050 | 3342 | MAPPED -> Arterial Tortuosity Syndrome (alias_exact:arterial tortuosity syndrome) |
| [ ] | 857 | 21.11.1.01 | ALDH1A3-related Retinaldehyde dehydrogenase 3 deficiency | ALDH1A3 | 615113 | 2542 | UNMAPPED; weak candidate Microphthalmia with Coloboma (0.776) |
| [ ] | 658 | 21.11.01.02 | TTPA-related Alpha-tocopherol transfer protein deficiency | TTPA | 277460 | 96 | MAPPED -> Familial Isolated Vitamin E Deficiency (identifier:ORPHA:96) |
| [ ] | 863 | 21.11.01.03 | GGCX-related Gamma-Glutamyl carboxylase deficiency | GGCX | 277450 | 98434 | MAPPED -> Vitamin K-Dependent Coagulation Factor Deficiency (identifier:ORPHA:98434) |
| [ ] | 849 | 21.11.01.04 | BCO1-related Beta-carotene 15,15'-dioxygenase deficiency | BCO1 | 115300 | 199285 | UNMAPPED; weak candidate Alkaptonuria (0.732) |
| [ ] | 859 | 21.11.01.05 | CYP27B1-related Vitamin D 1-α-hydroxylase deficiency | CYP27B1 | 264700 | 289157 | UNMAPPED; weak candidate BASD Type 3 (0.759) |
| [ ] | 850 | 21.11.02.01 | RBP4-related Plasma retinol-binding protein deficiency (dominant) | RBP4 | 616428;615147 | 98938 | UNMAPPED; weak candidate Microphthalmia with Coloboma (0.786) |
| [ ] | 860 | 21.11.02.02 | CYP2R1-related Vitamin D 25-hydroxylase deficiency | CYP2R1 | 600081 | 289157 | UNMAPPED; weak candidate Autosomal Recessive Dopa-Responsive Dystonia (0.788) |
| [ ] | 864 | 21.11.02.03 | VKORC1-related Vitamin K epoxide reductase deficiency | VKORC1 | 607473 | 98434 | MAPPED -> Vitamin K-Dependent Coagulation Factor Deficiency (identifier:ORPHA:98434) |
| [ ] | 851 | 21.11.03.01 | STRA6-related Vitamin A receptor deficiency | STRA6 | 601186 | 2470 | MAPPED -> STRA6-related syndromic microphthalmia (alias_exact:matthew wood syndrome) |
| [ ] | 861 | 21.11.03.02 | VDR-related Vitamin D receptor deficiency | VDR | 277440 | 93160 | UNMAPPED; weak candidate Familial Isolated Vitamin E Deficiency (0.684) |
| [ ] | 865 | 21.11.03.03 | EPHX1-related Microsomal epoxide hydrolase deficiency | EPHX1 | 607748 | 238475 | UNMAPPED; weak candidate 3-hydroxyisobutyryl-CoA hydrolase deficiency (0.675) |
| [ ] | 852 | 21.11.04.01 | LRAT-related Lecithin retinol acyltransferase deficiency | LRAT | 613341 | 364055 | CANDIDATE -> GUCY2D-Related Retinopathy (0.985) |
| [ ] | 862 | 21.11.04.02 | CYP24A1-related Vitamin D 24-hydroxylase deficiency | CYP24A1 | 143880 | 300547 | MAPPED -> Infantile Hypercalcemia (identifier:ORPHA:300547) |
| [ ] | 866 | 21.11.04.03 | UBIAD1-related Menaquinone-4 synthetase deficiency | UBIAD1 | 121800 | 98967 | UNMAPPED; weak candidate RBCD (0.772) |
| [ ] | 854 | 21.11.06.01 | RDH5-related Retinol dehydrogenase 5 deficiency | RDH5 | 136880 | 227796 | UNMAPPED; weak candidate Dimethylglycine Dehydrogenase Deficiency (0.806) |
| [ ] | 855 | 21.11.07.01 | RDH12-related Retinol dehydrogenase 12 deficiency | RDH12 | 612712 | 65 | CANDIDATE -> GUCY2D-Related Retinopathy (0.985) |
| [ ] | 856 | 21.11.09.01 | RBP3-related Interphotoreceptor retinol-binding protein deficiency | RBP3 | 615233 | 791 | MAPPED -> EYS-Related Retinitis Pigmentosa (identifier:ORPHA:791) |
| [ ] | 858 | 21.11.11.01 | RLBP1-related Cellular retinaldehyde-binding protein deficiency | RLBP1 | 180090 | 52427 | UNMAPPED; weak candidate E3-binding protein deficiency (0.718) |
| [ ] | 1222 | 21.11.12.01 | CYP26B1-related Retinoic acid hydroxylase deficiency | CYP26B1 | 614416 | 293925 | UNMAPPED |
| [ ] | 1310 | 21.11.13.01 | CYP26C1-related 9-cis-retinoic acid-metabolizing cytochrome deficiency | CYP26C1 | 614974 | - | UNMAPPED; weak candidate Focal Dermal Hypoplasia (0.741) |
| [ ] | 1330 | 21.11.14.01 | RARB-related Retinoic acid receptor β deficiency | RARB | 615524 | - | UNMAPPED; weak candidate STRA6-related syndromic microphthalmia (0.862) |
| [ ] | 1175 | 21.11.15.01 | RDH11-related Retinol dehydrogenase 11 deficiency | RDH11 | 616108 | 436245 | UNMAPPED; weak candidate Pyruvate Dehydrogenase Deficiency (0.794) |

### WP-077: Disorders of copper metabolism + 1 adjacent subgroup(s)

- Classification: Cofactor and Mineral Metabolism -> Disorders of trace elements and metals
- Subgroup scope: Disorders of copper metabolism; Disorders of iron metabolism
- Records: 27 (MAPPED 7, AMBIGUOUS 1, CANDIDATE 1, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 201 | 22.1.01.01 | ATP7B-related Copper-transporting ATPase subunit beta deficiency | ATP7B | 277900 | 905 | MAPPED -> Wilson Disease (identifier:OMIM:277900) |
| [ ] | 199 | 22.1.02.01 | ATP7A-related Copper-transporting ATPase subunit alpha deficiency (Menkes) | ATP7A | 309400 | 565 | MAPPED -> Menkes Disease (alias_exact:kinky hair disease) |
| [ ] | 200 | 22.1.02.02 | ATP7A-related Copper-transporting ATPase subunit alpha deficiency (OHS) | ATP7A | 304150 | 198 | MAPPED -> Occipital horn syndrome (alias_exact:occipital horn syndrome) |
| [ ] | 533 | 22.1.03.01 | ATP7A-related Copper-transporting ATPase subunit alpha deficiency (SMAX3) | ATP7A | 300489 | 404538 | UNMAPPED; weak candidate Menkes Disease (0.635) |
| [ ] | 578 | 22.1.04.01 | AP1S1-related MEDNIK syndrome | AP1S1 | 609313 | 171851 | MAPPED -> MEDNIK syndrome (alias_exact:mednik syndrome) |
| [ ] | 550 | 22.1.05.01 | SLC33A1-related Acetyl-CoA transporter deficiency | SLC33A1 | 614482 | 300313 | MAPPED -> Huppke-Brendel syndrome (alias_exact:huppke brendel syndrome) |
| [ ] | 1647 | 22.1.06.01 | AP1B1-related MEDNIK-like syndrome | AP1B1 | 242150 | 171851 | UNMAPPED; weak candidate MEDNIK syndrome (0.857) |
| [ ] | 1648 | 22.1.07.01 | CCS-related Copper chaperone for superoxide dismutase deficiency | CCS | 603864 | - | UNMAPPED; weak candidate Menkes Disease (0.505) |
| [ ] | 2040 | 22.1.08.01 | SLC31A1-related High-affinity copper transporter (CTR1) deficiency | SLC31A1 | 603085 | - | UNMAPPED; weak candidate Infantile Parkinsonism-Dystonia (0.702) |
| [ ] | 203 | 22.2.01.01 | HFE-related Hereditary hemochromatosis type 1 | HFE | 235200 | 443062 | UNMAPPED; weak candidate Hemochromatosis (0.881) |
| [ ] | 873 | 22.2.1.01 | TMPRSS6-related Matriptrase 2 deficiency | TMPRSS6 | 206200 | 209981 | UNMAPPED; weak candidate Refractory (0.559) |
| [ ] | 204 | 22.2.02.01 | HJV-related Hemojuvelin deficiency | HJV | 602390 | 79230 | CANDIDATE -> Hemochromatosis (0.962) |
| [ ] | 581 | 22.2.03.01 | HAMP-related Hepcidin deficiency | HAMP | 602390 | 79230 | MAPPED -> Hemochromatosis (alias_exact:hereditary hemochromatosis) |
| [ ] | 582 | 22.2.04.01 | TFR2-related Transferrin receptor 2 deficiency | TFR2 | 604250 | 225123 | MAPPED -> Hemochromatosis (alias_exact:hereditary hemochromatosis) |
| [ ] | 868 | 22.2.05.01 | SLC40A1-related Ferroportin 1 deficiency | SLC40A1 | 606069 | 139491 | UNMAPPED; weak candidate Hemochromatosis (0.881) |
| [ ] | 869 | 22.2.06.01 | FTL-related Ferritin light chain deficiency | FTL | 615604 | 440731 | UNMAPPED |
| [ ] | 870 | 22.2.07.01 | FTL-related Ferritin light chain superactivity | FTL | 606159 | 440731 | UNMAPPED; weak candidate Neurodegeneration With Brain Iron Accumulation (0.807) |
| [ ] | 871 | 22.2.08.01 | FTL-related Ferritin light chain dysregulation | FTL | 600886 | 440731 | UNMAPPED |
| [ ] | 872 | 22.2.09.01 | CP-related Hereditary ceruloplasmin deficiency | CP | 604290 | 48818 | AMBIGUOUS: 2 local entities (alias_exact:aceruloplasminemia) |
| [ ] | 206 | 22.2.11.01 | TF-related Hereditary transferrin deficiency | TF | 209300 | 1195 | UNMAPPED |
| [ ] | 874 | 22.2.12.01 | TFRC-related Transferrin receptor deficiency | TFRC | 616740 | 476113 | UNMAPPED; weak candidate IMD33 (0.791) |
| [ ] | 875 | 22.2.13.01 | SLC11A2-related Divalent metal transporter 1 deficiency | SLC11A2 | 206100 | 83642 | UNMAPPED; weak candidate SLC35A2-congenital disorder of glycosylation (0.720) |
| [ ] | 1176 | 22.2.14.01 | FTH1-related Ferritin heavy chain dysregulation | FTH1 | 615517 | 247790 | UNMAPPED; weak candidate Hemochromatosis (0.881) |
| [ ] | 1649 | 22.2.15.01 | BMP6-relared Iron overload | BMP6 | 112266 | 447792 | UNMAPPED |
| [ ] | 1650 | 22.2.16.01 | STEAP3-related Endosomal ferrireductase deficiency | STEAP3 | 615234 | 300298 | UNMAPPED; weak candidate MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.486) |
| [ ] | 205 | 22.2.17.01 | NOGENE-related Neonatal hemochromatosis | - | 231100 | 446 | UNMAPPED; weak candidate Hemochromatosis (0.769) |
| [ ] | 1740 | 22.2.18.01 | HEPHL1-related Hephastin-like protein 1 deficiency | HEPHL1 | 261990 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.719) |

### WP-078: Disorders of manganese metabolism + 1 adjacent subgroup(s)

- Classification: Cofactor and Mineral Metabolism -> Disorders of trace elements and metals
- Subgroup scope: Disorders of manganese metabolism; Disorders of zinc metabolism
- Records: 20 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 879 | 22.3.01.01 | SLC30A10-related Hypermanganesemia with dystonia type 1 | SLC30A10 | 613280 | 309854 | UNMAPPED; weak candidate MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.600) |
| [ ] | 1178 | 22.3.1.01 | EGF-related Epidermal growth factor deficiency | EGF | 611718 | 34527 | UNMAPPED; weak candidate AR-PAPSS2 (0.703) |
| [ ] | 883 | 22.3.01.02 | TRPM6-related Epithelial magnesium transporter deficiency | TRPM6 | 602014 | 30924 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.747) |
| [ ] | 880 | 22.3.02.01 | SLC39A14-related Hypermanganesemia with dystonia type 2 | SLC39A14 | 617013 | - | UNMAPPED; weak candidate MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.600) |
| [ ] | 884 | 22.3.02.02 | FXYD2-related Sodium-potassium ATPase γ subunit deficiency | FXYD2 | 154020 | 34528 | UNMAPPED; weak candidate Gitelman syndrome (0.689) |
| [ ] | 885 | 22.3.03.02 | CLDN10-related Claudin 10 deficiency | CLDN10 | 617671 | - | UNMAPPED; weak candidate ADULT (0.503) |
| [ ] | 886 | 22.3.04.01 | CLDN16-related Claudin 16 deficiency | CLDN16 | 248250 | 31043 | UNMAPPED; weak candidate Renal Agenesis (0.585) |
| [ ] | 887 | 22.3.05.01 | CLDN19-related Claudin 19 deficiency | CLDN19 | 248190 | 2196 | UNMAPPED; weak candidate MS-RO-positive (0.553) |
| [ ] | 888 | 22.3.06.01 | CNNM2-related Cyclin M2 deficiency | CNNM2 | 616418;613882 | 34527 | UNMAPPED; weak candidate Renal Agenesis (0.585) |
| [ ] | 890 | 22.3.08.01 | KCNJ10-related Epilepsy, ataxia, sensorineural deafness, tubulopathy (EAST) syndrome | KCNJ10 | 600791;612780 | 199343 | UNMAPPED; weak candidate EAST Syndrome (0.840) |
| [ ] | 1340 | 22.3.09.01 | ATP1A1-related Renal hypomagnesemia, refractory seizures, and intellectual disability | ATP1A1 | 618314 | - | UNMAPPED; weak candidate MED13 Syndrome (0.610) |
| [ ] | 595 | 22.3.11.01 | SLC39A8-related Congenital disorder of glycosylation (CDG) | SLC39A8 | 616721 | 468699 | CANDIDATE -> ALG12-congenital disorder of glycosylation (0.905) |
| [ ] | 2065 | 22.3.12.01 | SLC39A7-related Zinc transporter deficiency | SLC39A7 | 619693 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.847) |
| [ ] | 202 | 22.4.01.01 | SLC39A4-related Acrodermatitis enteropathica | SLC39A4 | 201100 | 37 | UNMAPPED |
| [ ] | 876 | 22.4.02.01 | SLC30A2-related Zinc transporter 2 deficiency | SLC30A2 | 608118 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.820) |
| [ ] | 877 | 22.4.03.01 | SLC39A13-related Spondylocheirodysplastic Ehlers-Danlos syndrome | SLC39A13 | 612350 | 157965 | CANDIDATE -> Spondylodysplastic Ehlers-Danlos Syndrome (0.932) |
| [ ] | 878 | 22.4.04.01 | SLC30A9-related Birk-Landau-Perez syndrome | SLC30A9 | 617595 | 505242 | UNMAPPED; weak candidate Landau-Kleffner Syndrome (0.720) |
| [ ] | 1463 | 22.4.05.01 | PSTPIP1-related Hyperzincemia and hypercalprotectinemia | PSTPIP1 | 604416 | - | UNMAPPED; weak candidate COPA Syndrome (0.432) |
| [ ] | 1750 | 22.4.06.01 | SLC30A5-related Perinatal lethal cardiomyopathy | SLC30A5 | 607819 | - | UNMAPPED; weak candidate Peripartum Cardiomyopathy (0.750) |
| [ ] | 2051 | 22.4.07.01 | SLC30A7-related Zinc transporter 7 deficiency | SLC30A7 | 611149 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.820) |

### WP-079: Other disorders of trace element metabolism

- Classification: Cofactor and Mineral Metabolism -> Disorders of trace elements and metals
- Subgroup scope: Other disorders of trace element metabolism
- Records: 3 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 3)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 881 | 22.5.01.01 | SECISBP2-related Selenocysteine insertion sequence-binding protein 2 deficiency | SECISBP2 | 609698 | 171706 | UNMAPPED; weak candidate E3-binding protein deficiency (0.615) |
| [ ] | 882 | 22.5.02.01 | SEPSECS-related O-phosphoseryl-tRNA(Sec) selenium transferase deficiency | SEPSECS | 613811 | 2524 | UNMAPPED; weak candidate Homocystinuria (0.744) |
| [ ] | 2178 | 22.5.03.01 | EEFSEC-related Selenopathy with early-onset neurodegeneration | EEFSEC | 607695 | - | UNMAPPED; weak candidate LCH-ND (0.590) |

### WP-080: Monoamine neurotransmission + 1 adjacent subgroup(s)

- Classification: Metabolic Cell Signalling -> Neurotransmitter disorders
- Subgroup scope: Monoamine neurotransmission; Gamma-aminobutyric acid neurotransmitter disorders
- Records: 21 (MAPPED 5, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 14)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 99 | 23.1.01.01 | TH-related Tyrosine hydroxylase deficiency | TH | 191290 | - | AMBIGUOUS: 2 local entities (alias_exact:tyrosine hydroxylase deficiency) |
| [ ] | 1651 | 23.1.1.01 | MAOA;MAOB-related Combined monoamine oxidase A and B deficiency | MAOA;MAOB | 309850;309860 | - | UNMAPPED; weak candidate Combined Saposin Deficiency (0.711) |
| [ ] | 100 | 23.1.02.01 | DDC-related Aromatic L-amino acid decarboxylase deficiency | DDC | 608643 | - | AMBIGUOUS: 2 local entities (alias_exact:aromatic l amino acid decarboxylase deficiency) |
| [ ] | 101 | 23.1.03.01 | DBH-related Dopamine beta-hydroxylase deficiency | DBH | 223360 | - | UNMAPPED; weak candidate 11B-OHD (0.848) |
| [ ] | 102 | 23.1.04.01 | MAOA-related Monoamine oxidase A deficiency | MAOA | 309850 | - | UNMAPPED; weak candidate Chronic Granulomatous Disease (0.778) |
| [ ] | 103 | 23.1.05.01 | SLC6A3-related Dopamine transporter deficiency | SLC6A3 | 613135;126455 | - | MAPPED -> Infantile Parkinsonism-Dystonia (alias_exact:infantile parkinsonism dystonia) |
| [ ] | 579 | 23.1.06.01 | SLC18A2-related Vesicular monoamine transporter 2 deficiency | SLC18A2 | 193001 | 352649 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.789) |
| [ ] | 1316 | 23.1.08.01 | CYB561-related Cytochrome b561 deficiency | CYB561 | 618182 | - | UNMAPPED; weak candidate COX6B1-Related COX Deficiency (0.782) |
| [ ] | 588 | 23.1.08.02 | DNAJC12-related Hyperphenylalaninemia | DNAJC12 | 606060 | - | UNMAPPED |
| [ ] | 1355 | 23.1.09.01 | SLC6A2-related Norepinephrine transporter deficiency | SLC6A2 | 604715 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.812) |
| [ ] | 815 | 23.2.1.01 | GABRB2-related GABA type A receptor β2 subunit deficiency | GABRB2 | 617829 | 442835 | UNMAPPED; weak candidate Undetermined Early-Onset Epileptic Encephalopathy (0.661) |
| [ ] | 36 | 23.2.05.01 | ABAT-related GABA transaminase deficiency | ABAT | 137150;613163 | - | UNMAPPED; weak candidate GABRD (0.411) |
| [ ] | 37 | 23.2.06.01 | ALDH5A1-related Succinic semialdehyde dehydrogenase deficiency | ALDH5A1 | 271980;610045 | - | MAPPED -> Succinic Semialdehyde Dehydrogenase Deficiency (identifier:OMIM:271980) |
| [ ] | 813 | 23.2.08.01 | GABRA1-related GABA type A receptor α1 subunit deficiency | GABRA1 | 615744 | 33069 | MAPPED -> Dravet_syndrome (identifier:ORPHA:33069) |
| [ ] | 814 | 23.2.09.01 | GABRB1-related GABA type A receptor β1 subunit deficiency | GABRB1 | 617153 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 816 | 23.2.11.01 | GABRB3-related GABA type A receptor β3 subunit deficiency | GABRB3 | 617829 | 64280 | UNMAPPED |
| [ ] | 817 | 23.2.12.01 | GABRG2-related GABA type A receptor γ2 subunit deficiency | GABRG2 | 611277 | 33069 | MAPPED -> Dravet_syndrome (identifier:ORPHA:33069) |
| [ ] | 818 | 23.2.13.01 | GABBR2-related GABA type B receptor subunit 2 deficiency | GABBR2 | 617904 | 3095 | UNMAPPED; weak candidate IGFALS Deficiency (0.620) |
| [ ] | 1163 | 23.2.14.01 | GABRD-related GABA type A receptor δ subunit deficiency | GABRD | 137163 | 36387 | MAPPED -> Generalized Epilepsy with Febrile Seizures Plus (identifier:ORPHA:36387) |
| [ ] | 1162 | 23.2.15.01 | GABRA6-related GABA type A receptor α 6 subunit deficiency | GABRA6 | 137143 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.571) |
| [ ] | 2069 | 23.2.19.01 | GABRA3-related GABA type A receptor subunit alpha 3 deficiency | GABRA3 | 301091 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.617) |

### WP-081: Glutamate neurotransmitter disorders + 2 adjacent subgroup(s)

- Classification: Metabolic Cell Signalling -> Neurotransmitter disorders
- Subgroup scope: Glutamate neurotransmitter disorders; Glycine neurotransmitter disorders; Disorders of choline neurotransmission
- Records: 40 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 32)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 826 | 23.3.1.01 | GRIA4-related Ionotropic glutamate receptor AMPA type subunit 4 dysregulation | GRIA4 | 617864 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.739) |
| [ ] | 821 | 23.3.05.01 | GRIN1-related Ionotropic glutamate receptor NMDA type subunit 1 dysregulation | GRIN1 | 614254;617820 | 178469 | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.750) |
| [ ] | 822 | 23.3.06.01 | GRIN2A-related Ionotropic glutamate receptor NMDA type subunit 2A dysregulation | GRIN2A | 245570 | 98818 | UNMAPPED |
| [ ] | 823 | 23.3.07.01 | GRIN2B-related Ionotropic glutamate receptor NMDA type subunit 2B dysregulation | GRIN2B | 616139;613970 | 3451 | MAPPED -> Infantile Spasms (identifier:ORPHA:3451) |
| [ ] | 824 | 23.3.08.01 | GRIN2D-related Ionotropic glutamate receptor NMDA type subunit 2D superactivity | GRIN2D | 617162 | 442835 | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.776) |
| [ ] | 825 | 23.3.09.01 | GRIA3-related Ionotropic glutamate receptor AMPA type subunit 3 deficiency | GRIA3 | 300699 | 364028 | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.667) |
| [ ] | 1235 | 23.3.11.01 | ATAD1-related Thorase deficiency | ATAD1 | 618011 | - | UNMAPPED; weak candidate Hereditary Hyperekplexia (0.591) |
| [ ] | 827 | 23.3.12.01 | GRM1-related Metabotropic glutamate receptor 1 deficiency | GRM1 | 614831 | 324262 | CANDIDATE -> CALFAN Syndrome (0.980) |
| [ ] | 828 | 23.3.13.01 | GRM1-related Metabotropic glutamate receptor 1 superactivity | GRM1 | 617691 | 404507 | CANDIDATE -> SCA4 (0.983) |
| [ ] | 829 | 23.3.14.01 | GRM6-related Metabotropic glutamate receptor 6 deficiency | GRM6 | 257270 | 215 | UNMAPPED; weak candidate CSNBAD1 (0.796) |
| [ ] | 1652 | 23.3.17.01 | GRIA2-related Ionotropic glutamate receptor AMPA type subunit 2 deficiency | GRIA2 | 618917 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.686) |
| [ ] | 1653 | 23.3.18.01 | GRID2-related Ionotropic glutamate receptor delta type subunit 2 deficiency | GRID2 | 616204 | 363432 | UNMAPPED; weak candidate COG1-congenital disorder of glycosylation (0.534) |
| [ ] | 2010 | 23.3.19.01 | GRIK2-related Intellectual developmental disorder | GRIK2 | 611092 | - | CANDIDATE -> MED13 Syndrome (0.959) |
| [ ] | 2011 | 23.3.19.02 | GRIK2-related Neurodevelopmental disorder with impaired language and ataxia and with or without seizures | GRIK2 | 619580 | - | UNMAPPED; weak candidate UNC13A-Related NDD with Seizures and Movement Disorder (0.632) |
| [ ] | 832 | 23.4.03.01 | SLC6A9-related Glycine transporter 1 deficiency | SLC6A9 | 617301 | 289860 | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.844) |
| [ ] | 522 | 23.4.04.01 | SLC6A5-related Glycine transporter 2 deficiency | SLC6A5 | 149400 | 3197 | MAPPED -> Hereditary Hyperekplexia (identifier:ORPHA:3197) |
| [ ] | 833 | 23.4.05.01 | GLRA1-related Glycine receptor subunit alpha 1 deficiency | GLRA1 | 149400 | 3197 | MAPPED -> Hereditary Hyperekplexia (identifier:ORPHA:3197) |
| [ ] | 834 | 23.4.06.01 | GLRB-related Glycine receptor subunit beta deficiency | GLRB | 614619 | 3197 | MAPPED -> Hereditary Hyperekplexia (identifier:ORPHA:3197) |
| [ ] | 2031 | 23.4.07.01 | GLRA2-related Intellectual developmental disorder, X-linked, syndromic, Pilorge type | GLRA2 | 301076 | - | UNMAPPED; weak candidate MED13 Syndrome (0.686) |
| [ ] | 1654 | 23.5.01.01 | SLC5A7-related Myasthenic syndrome 20, presynaptic | SLC5A7 | 617143 | 139589;98914 | UNMAPPED |
| [ ] | 1655 | 23.5.02.01 | CHAT-related Choline acetyltransferase deficiency | CHAT | 254210 | 98914 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.514) |
| [ ] | 1656 | 23.5.03.01 | RIC3-related Acetylcholine receptor chaperone deficiency | RIC3 | 610509 | - | UNMAPPED; weak candidate TNF Receptor-Associated Periodic Syndrome (0.524) |
| [ ] | 1657 | 23.5.04.01 | CHRNE-related Myasthenic syndrome, congenital, 4A slow-channel | CHRNE | 605809 | 98913 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.533) |
| [ ] | 2208 | 23.5.05.01 | CHRNA1-related Myasthenic syndrome 1A, slow-channel | CHRNA1 | 601462 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.600) |
| [ ] | 2209 | 23.5.06.01 | CHRNA1-related Myasthenic syndrome 1B, fast-channel | CHRNA1 | 608930 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.600) |
| [ ] | 2210 | 23.5.07.01 | CHRNA1-related Multiple pterygium syndrome, lethal type | CHRNA1 | 253290 | - | UNMAPPED; weak candidate CHRNA1-Associated Fetal Hypo-akinesia Disorder of Prenatal Onset (0.740) |
| [ ] | 2211 | 23.5.08.01 | CHRNA2-related Epilepsy, nocturnal frontal lobe | CHRNA2 | 610353 | - | UNMAPPED; weak candidate Type 4 (0.625) |
| [ ] | 2212 | 23.5.09.01 | CHRNA3-related Bladder dysfunction, autonomic, with impaired pupillary reflex and secondary CAKUT | CHRNA3 | 191800 | - | UNMAPPED; weak candidate Ectodermal Dysplasia and Immunodeficiency 2 (0.461) |
| [ ] | 2213 | 23.5.10.01 | CHRNA4-related Epilepsy, nocturnal frontal lobe | CHRNA4 | 600513 | - | UNMAPPED; weak candidate Type 1 (0.625) |
| [ ] | 2214 | 23.5.11.01 | CHRNB1-related Myasthenic syndrome 2A, slow-channel | CHRNB1 | 616313 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.600) |
| [ ] | 2215 | 23.5.12.01 | CHRNB2-related Epilepsy, nocturnal frontal lobe | CHRNB2 | 605375 | - | UNMAPPED; weak candidate Type 3 (0.625) |
| [ ] | 2216 | 23.5.13.01 | CHRND-related Myasthenic syndrome, congenital 3B, fast-channel | CHRND | 616322 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.533) |
| [ ] | 2217 | 23.5.14.01 | CHRND-related Myasthenic syndrome 3A, slow-channel | CHRND | 616321 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.608) |
| [ ] | 2218 | 23.5.15.01 | CHRND-related Multiple pterygium syndrome, lethal type | CHRND | 253290 | - | UNMAPPED |
| [ ] | 2219 | 23.5.16.01 | CHRNE-related Myasthenic syndrome 4B, fast-channel | CHRNE | 616324 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.608) |
| [ ] | 2220 | 23.5.17.01 | CHRNE-related Myasthenic syndrome 4C, associated with acetylcholine receptor deficiency | CHRNE | 608931 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.414) |
| [ ] | 2221 | 23.5.18.01 | CHRNG-related Multiple pterygium syndrome, lethal type | CHRNG | 253290 | - | UNMAPPED; weak candidate Autosomal Recessive Multiple Pterygium Syndrome (0.767) |
| [ ] | 2222 | 23.5.19.01 | CHRNG-related Multiple pterygium syndrome, Escobar variant | CHRNG | 265000 | - | MAPPED -> Autosomal Recessive Multiple Pterygium Syndrome (alias_exact:evmps) |
| [ ] | 2223 | 23.5.20.01 | RAPSN-related Myasthenic syndrome 11, associated with acetylcholine receptor deficiency | RAPSN | 616326 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.379) |
| [ ] | 2224 | 23.5.21.01 | SLC18A3-related Myasthenic syndrome 21, presynaptic | SLC18A3 | 617239 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.594) |

### WP-082: Disorders of the synaptic vesicle cycle (part 1 of 2)

- Classification: Metabolic Cell Signalling -> Neurotransmitter disorders
- Subgroup scope: Disorders of the synaptic vesicle cycle
- Records: 22 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1658 | 23.6.01.01 | TBC1D24-related Deafness , autosomal recessive 86/65 | TBC1D24 | 614617;616044;615338;220500;608105;605021 | 79500;352582;352587;352596 | UNMAPPED; weak candidate DOORS Syndrome (0.404) |
| [ ] | 1667 | 23.6.1.01 | RBSN-related Rabenosyn 5 deficiency | RBSN | 609511 | 369852 | UNMAPPED |
| [ ] | 1659 | 23.6.02.01 | KIF1A-related Spastic paraplegia 30 | KIF1A | 614255;614213;610357 | 178469;101010;970 | CANDIDATE -> SPG3A (0.952) |
| [ ] | 1677 | 23.6.2.01 | PNKD-related Paroxysmal nonkinesigenic dyskinesia type 1 | PNKD | 118800 | 98810 | UNMAPPED; weak candidate Stromme Syndrome (0.545) |
| [ ] | 1660 | 23.6.03.01 | KIF5A-related Myoclonus, intractable, neonatal | KIF5A | 602821 | 324611;100991 | UNMAPPED; weak candidate Complex Hereditary Spastic Paraplegia (0.621) |
| [ ] | 1661 | 23.6.04.01 | KIF5C-related Cortical dysplasia, complex, with other brain malformations 2 | KIF5C | 615282 | - | UNMAPPED; weak candidate TP63-Related Ectodermal Dysplasia Spectrum (0.667) |
| [ ] | 1662 | 23.6.05.01 | DYNC1H1-related Charcot-Marie-Tooth disease, axonal, type 20 | DYNC1H1 | 614228;614563;158600 | - | UNMAPPED |
| [ ] | 1663 | 23.6.06.01 | DNM1-related Dynamin 1 deficiency | DNM1 | 616346 | - | UNMAPPED; weak candidate Developmental and Epileptic Encephalopathy Type 42 (0.755) |
| [ ] | 1664 | 23.6.07.01 | DNM2-related Dynamin 2 deficiency | DNM2 | 602378 | - | UNMAPPED |
| [ ] | 1665 | 23.6.08.01 | NAPB-related Developmental and epileptic encephalopathy 107 | NAPB | 611270 | - | CANDIDATE -> CN-Related Developmental and Epileptic Encephalopathy (0.967) |
| [ ] | 1666 | 23.6.09.01 | PRRT2-related Proline-rich transmembrane protein 2 deficiency | PRRT2 | 614386 | - | UNMAPPED; weak candidate Benign Familial Infantile Epilepsy (0.562) |
| [ ] | 1668 | 23.6.11.01 | SNAP25-related Myasthenic syndrome, congenital, 18 | SNAP25 | 616330 | 98914 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.603) |
| [ ] | 1669 | 23.6.12.01 | SNAP29-related CEDNIK syndrome (CDG) | SNAP29 | 609528 | - | UNMAPPED |
| [ ] | 1670 | 23.6.13.01 | STXBP1-related Syntaxin-binding protein 1 deficiency | STXBP1 | 612164 | 1934 | UNMAPPED; weak candidate Undetermined Early-Onset Epileptic Encephalopathy (0.688) |
| [ ] | 1671 | 23.6.14.01 | SV2A-related Synaptic vesicle glycoprotein 2A deficiency | SV2A | 185860 | - | UNMAPPED; weak candidate Synaptic (0.529) |
| [ ] | 1455 | 23.6.15.01 | DNM2-related Charcot-Marie-Tooth disease, axonal type 2M | DNM2 | 606482 | - | UNMAPPED |
| [ ] | 1672 | 23.6.15.02 | VAMP1-related Synaptobrevin 1 deficiency | VAMP1 | 618323 | 98914;251282 | UNMAPPED; weak candidate SPG9A (0.853) |
| [ ] | 1454 | 23.6.16.01 | DNM2-related Centronuclear myopathy 1 | DNM2 | 160150 | - | CANDIDATE -> Centronuclear Myopathy (0.957) |
| [ ] | 1673 | 23.6.16.02 | VAMP2-related Synaptobrevin 2 deficiency | VAMP2 | 618760 | - | UNMAPPED; weak candidate UNC13A-Related Congenital NDD with Epilepsy (0.616) |
| [ ] | 1674 | 23.6.17.01 | STX1B-related Syntaxin 1B deficiency | STX1B | 616172 | 36387 | MAPPED -> Generalized Epilepsy with Febrile Seizures Plus (identifier:ORPHA:36387) |
| [ ] | 1675 | 23.6.18.01 | SYN1-related Synapsin 1 deficiency | SYN1 | 300491 | - | UNMAPPED; weak candidate Wieacker-Wolff Syndrome (0.527) |
| [ ] | 1676 | 23.6.19.01 | IL1RAPL1-related Mental retardation, X-linked 21/34 | IL1RAPL1 | 300143 | 777 | UNMAPPED; weak candidate DYRK1A-related intellectual disability syndrome (0.639) |

### WP-083: Disorders of the synaptic vesicle cycle (part 2 of 2)

- Classification: Metabolic Cell Signalling -> Neurotransmitter disorders
- Subgroup scope: Disorders of the synaptic vesicle cycle
- Records: 12 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 8)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2056 | 23.6.20.01 | STX1A-related Syntaxin 1A deficiency | STX1A | 186590 | - | UNMAPPED; weak candidate STX1B (0.517) |
| [ ] | 1678 | 23.6.21.01 | SYT1-relasted Synaptotagmin 1 deficiency | SYT1 | 618218 | 522077 | UNMAPPED; weak candidate 46,XY complete gonadal dysgenesis (0.714) |
| [ ] | 1679 | 23.6.22.01 | SYT2-related Synaptotagmin 2 deficiency | SYT2 | 616040 | 98914 | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.514) |
| [ ] | 1680 | 23.6.23.01 | SYT14-related Synaptotagmin 14 deficiency | SYT14 | 614229 | - | CANDIDATE -> CALFAN Syndrome (0.980) |
| [ ] | 1681 | 23.6.24.01 | TOR1A-related Artrhogryposis multiplex congenita type 5 | TOR1A | 618947 | - | UNMAPPED; weak candidate Arthrogryposis Multiplex Congenita (0.880) |
| [ ] | 1682 | 23.6.25.01 | LRRK2-related Parkinson disease 8 | LRRK2 | 607060 | - | CANDIDATE -> Parkinson's Disease (0.944) |
| [ ] | 1683 | 23.6.26.01 | DNAJC6-related Parkinson disease 19a/b | DNAJC6 | 615528 | - | UNMAPPED; weak candidate Parkinson's Disease (0.850) |
| [ ] | 1684 | 23.6.27.01 | CLTC-related Clathrin heavy chain deficiency | CLTC | 617854 | - | CANDIDATE -> DYRK1A-related intellectual disability syndrome (0.962) |
| [ ] | 1685 | 23.6.28.01 | SORCS-related Receptor 3 deficiency | SORCS3 | 606285 | - | UNMAPPED; weak candidate GABRD (0.478) |
| [ ] | 2061 | 23.6.29.01 | DLG4-related  Intellectual developmental disorder | DLG4 | 618793 | - | CANDIDATE -> MED13 Syndrome (0.982) |
| [ ] | 2203 | 23.6.30.01 | SNAPIN-related Prenatal-onset neurodevelopmental disorder | SNAPIN | 607007 | - | UNMAPPED; weak candidate Houge-Janssens Syndrome (0.829) |
| [ ] | 2239 | 23.6.31.01 | BSN-related Pre-synaptic Basson deficiency | BSN | 604020 | - | UNMAPPED; weak candidate Synaptic (0.476) |

### WP-084: Disorders of insulin metabolism (part 1 of 2)

- Classification: Metabolic Cell Signalling -> Endocrine metabolic disorders
- Subgroup scope: Disorders of insulin metabolism
- Records: 22 (MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 13)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 566 | 24.1.01.01 | ABCC8-related ATP-sensitive potassium channel regulatory subunit deficiency | ABCC8 | 256450 | 99886 | UNMAPPED |
| [ ] | 898 | 24.1.1.01 | INS-related Proinsulin cleavage deficiency | INS | 616214 | 99885 | UNMAPPED |
| [ ] | 1181 | 24.1.2.01 | AKT2-related Hypoinsulinemic hypoglycemia with hemihypertrophy | AKT2 | 125853 | 79085 | UNMAPPED |
| [ ] | 1287 | 24.1.02.01 | ABCC8-related ATP-sensitive potassium channel regulatory subunit superactivity | ABCC8 | 600509 | 99886 | MAPPED -> maturity-onset diabetes of the young, type 12 (alias_exact:maturity onset diabetes of the young type 12) |
| [ ] | 213 | 24.1.03.01 | KCNJ11-related ATP-sensitive potassium channel pore-forming subunit deficiency | KCNJ11 | 601820 | 99886 | UNMAPPED; weak candidate Congenital Isolated Hyperinsulinism (0.476) |
| [ ] | 1423 | 24.1.3.01 | DIS3L2-related Perlmann syndrome | DIS3L2 | 267000 | - | UNMAPPED |
| [ ] | 1288 | 24.1.04.01 | KCNJ11-related ATP-sensitive potassium channel pore-forming subunit superactivity | KCNJ11 | 601820 | 99886 | MAPPED -> maturity-onset diabetes of the young type 13 (alias_exact:maturity onset diabetes of the young type 13) |
| [ ] | 570 | 24.1.05.01 | HNF4A-related Hepatocyte nuclear factor 4-alpha ldeficiency MODY1 | HNF4A | 600281 | 93111 | UNMAPPED; weak candidate FRTS4 (0.209) |
| [ ] | 573 | 24.1.06.01 | HNF1A-related MODY3 | HNF1A | 142410 | 552 | UNMAPPED |
| [ ] | 896 | 24.1.07.01 | HNF1B-related Hepatocyte nuclear factor-1beta deficiency | HNF1B | 125853 | 97364 | UNMAPPED; weak candidate Diabetes mellitus (0.618) |
| [ ] | 468 | 24.1.08.01 | UCP1-3-related Uncoupling protein deficiency | UCP1;UCP2;UCP3 | 601665;607447 | - | UNMAPPED; weak candidate E3-binding protein deficiency (0.793) |
| [ ] | 572 | 24.1.08.02 | UCP2-related Uncoupling protein 2 deficiency | UCP2 | 601693 | 276556 | UNMAPPED; weak candidate E3-binding protein deficiency (0.767) |
| [ ] | 897 | 24.1.09.01 | INS-related Maturity-onset diabetes of the young type 10 | INS | 613370 | 99885 | MAPPED -> maturity-onset diabetes of the young type 10 (alias_exact:maturity onset diabetes of the young type 10) |
| [ ] | 583 | 24.1.11.01 | INSR-related Insulin receptor dysregulation, Donohue syndrome | INSR | 609968 | 769 | UNMAPPED; weak candidate IPEX Syndrome (0.600) |
| [ ] | 899 | 24.1.12.01 | PDX1-related Maturity-onset diabetes of the young type 4 | PDX1 | 606392;260370 | 99885 | MAPPED -> maturity-onset diabetes of the young type 4 (alias_exact:maturity onset diabetes of the young type 4) |
| [ ] | 900 | 24.1.13.01 | NEUROD1-related Maturity-onset diabetes of the young type 6 | NEUROD1 | 606394 | 552 | MAPPED -> maturity-onset diabetes of the young type 6 (alias_exact:maturity onset diabetes of the young type 6) |
| [ ] | 901 | 24.1.14.01 | KLF11-related Maturity-onset diabetes of the young type 7 | KLF11 | 610508 | 552 | MAPPED -> maturity-onset diabetes of the young type 7 (alias_exact:maturity onset diabetes of the young type 7) |
| [ ] | 902 | 24.1.15.01 | PAX4-related Maturity-onset diabetes of the young type 9 | PAX4 | 612225 | 552 | MAPPED -> maturity-onset diabetes of the young type 9 (alias_exact:maturity onset diabetes of the young type 9) |
| [ ] | 903 | 24.1.16.01 | BLK-related Maturity-onset diabetes of the young type 11 | BLK | 613375 | 552 | MAPPED -> maturity-onset diabetes of the young type 11 (alias_exact:maturity onset diabetes of the young type 11) |
| [ ] | 904 | 24.1.17.01 | APPL1-related Maturity-onset diabetes of the young type 14 | APPL1 | 616511 | 552 | MAPPED -> maturity-onset diabetes of the young type 14 (alias_exact:maturity onset diabetes of the young type 14) |
| [ ] | 905 | 24.1.18.01 | AKT2-related Serine/threonine kinase superactivity | AKT2 | 240900 | 79085 | UNMAPPED |
| [ ] | 1417 | 24.1.18.02 | AKT3-related  Serine/threonine kinase superactivity | AKT3 | 611223 | - | UNMAPPED; weak candidate PRPS1 Superactivity (0.562) |

### WP-085: Disorders of insulin metabolism (part 2 of 2)

- Classification: Metabolic Cell Signalling -> Endocrine metabolic disorders
- Subgroup scope: Disorders of insulin metabolism
- Records: 11 (MAPPED 3, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 906 | 24.1.19.01 | RFX6-related Maturity-onset diabetes of the young | RFX6 | 615710 | 293864 | MAPPED -> maturity-onset diabetes of the young (alias_exact:maturity onset diabetes of the young) |
| [ ] | 1425 | 24.1.21.01 | FOXA2-related  Hyperinsulinemic syndrome | FOXA2 | 600288 | - | UNMAPPED |
| [ ] | 1424 | 24.1.22.01 | GPC3-related Simpson-Golabi-Behmel syndrome | GPC3 | 312870 | - | UNMAPPED |
| [ ] | 1414 | 24.1.23.01 | KDM6A-related Kabuki syndrome | KDM6A | 300867 | 116 | AMBIGUOUS: 3 local entities (alias_exact:kabuki syndrome) |
| [ ] | 1450 | 24.1.24.01 | KMT2D-related Kabuki syndrome | KMT2D | 147920 | 116 | AMBIGUOUS: 3 local entities (alias_exact:kabuki syndrome) |
| [ ] | 1418 | 24.1.25.01 | NSD1;NFIX-related Sotos syndrome | NSD1;NFIX | 117550;617169 | - | UNMAPPED; weak candidate Ischemic Stroke (0.703) |
| [ ] | 1426 | 24.1.26.01 | PHOX2B-related Ondine syndrome | PHOX2B | 209880 | - | UNMAPPED; weak candidate Central Congenital Hypothyroidism (0.737) |
| [ ] | 1415 | 24.1.27.01 | NOGENE-related Turner syndrome | - | - | - | UNMAPPED |
| [ ] | 1419 | 24.1.28.01 | CACNA1C-related Timothy syndrome | CACNA1C | 601005 | - | MAPPED -> Timothy Syndrome (alias_exact:cacna1c related timothy syndrome) |
| [ ] | 1420 | 24.1.29.01 | CACNA1D-related Primary aldosteronism, seizures, and neurologic abnormalities | CACNA1D | 615474 | - | UNMAPPED; weak candidate B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality (0.535) |
| [ ] | 1413 | 24.1.31.01 | IGF2;H19;CDKN1C;KCNQ1-related Beckwith Wiedemann syndrome | IGF2;H19;CDKN1C;KCNQ1 | 130650 | 116 | MAPPED -> Beckwith-Wiedemann Syndrome (alias_exact:beckwith wiedemann syndrome) |

### WP-086: Disorders of steroid metabolism (part 1 of 2)

- Classification: Metabolic Cell Signalling -> Endocrine metabolic disorders
- Subgroup scope: Disorders of steroid metabolism
- Records: 22 (MAPPED 11, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 119 | 24.2.01.01 | CYP21A2-related 21-Hydroxylase deficiency | CYP21A2 | 201910 | 418 | MAPPED -> Congenital Adrenal Hyperplasia (alias_exact:cah) |
| [ ] | 124 | 24.2.1.01 | H6PD-related Hexose-6-phosphate dehydrogenase deficiency | H6PD | 604931 | 168588 | MAPPED -> Cortisone Reductase Deficiency (identifier:ORPHA:168588) |
| [ ] | 120 | 24.2.02.01 | CYP11B1-related 11-beta-Hydroxylase type 1 deficiency | CYP11B1 | 202010 | 418 | MAPPED -> Congenital Adrenal Hyperplasia (alias_exact:cah) |
| [ ] | 555 | 24.2.2.01 | AKR1C2-related 3-alpha-hydroxysteroid dehydrogenase type 3 deficiency | AKR1C2 | 600450 | 443087 | UNMAPPED; weak candidate 3B-HSD (0.860) |
| [ ] | 1303 | 24.2.2.02 | ESR2-related Estrogen receptor 2 deficiency | ESR2 | 601663 | - | UNMAPPED; weak candidate Luminal Androgen Receptor (LAR) TNBC (0.533) |
| [ ] | 122 | 24.2.03.01 | CYP11B1-related 11-beta-Hydroxylase superactivity | CYP11B1 | 103900 | 90795 | MAPPED -> Familial hyperaldosteronism type I (identifier:OMIM:103900) |
| [ ] | 118 | 24.2.04.01 | HSD3B2-related 3-beta-Hydroxysteroid dehydrogenase deficiency | HSD3B2 | 201810 | 418 | MAPPED -> 3B-HSD (alias_exact:3 beta hydroxysteroid dehydrogenase deficiency) |
| [ ] | 117 | 24.2.05.01 | CYP17A1-related 17-alpha-Hydroxylase deficiency | CYP17A1 | 202110 | 418 | MAPPED -> Congenital Adrenal Hyperplasia (alias_exact:congenital adrenal hyperplasia) |
| [ ] | 125 | 24.2.05.02 | CYP17A1-related 17,20-Lyase deficiency | CYP17A1 | 202110 | 90796 | UNMAPPED |
| [ ] | 116 | 24.2.06.01 | STAR-related Steroidogenic acute regulatory protein deficiency | STAR | 201710 | 314376 | UNMAPPED; weak candidate Congenital Adrenal Hyperplasia (0.750) |
| [ ] | 198 | 24.2.07.01 | POR-related Cytochrome P450 oxidoreductase deficincy | POR | 201750 | 83 | MAPPED -> Amniotic Band Syndrome (alias_exact:abs) |
| [ ] | 1281 | 24.2.08.01 | CYP11B2-related Steroid 18-hydroxylase deficiency | CYP11B2 | 203400 | 99763 | CANDIDATE -> Familial hyperaldosteronism type I (0.979) |
| [ ] | 1088 | 24.2.09.01 | CYP11B2-related Steroid 18-oxidase deficiency | CYP11B2 | 610600 | 99763 | UNMAPPED |
| [ ] | 1280 | 24.2.11.01 | HSD11B1-related 11-β-hydroxysteroid dehydrogenase deficiency | HSD11B1 | 614662 | 168588 | MAPPED -> Cortisone Reductase Deficiency (identifier:ORPHA:168588) |
| [ ] | 132 | 24.2.12.01 | NR3C1-related Glucocorticoid receptor deficiency | NR3C1 | 138040 | 786 | UNMAPPED; weak candidate Type I (0.625) |
| [ ] | 1090 | 24.2.13.01 | MC2R-related ACTH receptor deficiency | MC2R | 202200 | 361 | UNMAPPED |
| [ ] | 1091 | 24.2.14.01 | MRAP-related Melanocortin-2 receptor accessory protein deficiency | MRAP | 607398 | 361 | UNMAPPED; weak candidate Tay-Sachs Disease AB Variant (0.643) |
| [ ] | 128 | 24.2.15.01 | CYP19A1-related Aromatase deficiency | CYP19A1 | 107910 | 91 | MAPPED -> Aromatase Deficiency (identifier:ORPHA:91) |
| [ ] | 1263 | 24.2.16.01 | CYP19A1-related Aromatase superactivity | CYP19A1 | 107910 | 91 | MAPPED -> Aromatase Deficiency (identifier:ORPHA:91) |
| [ ] | 130 | 24.2.17.01 | ESR1-related Estrogen receptor deficiency | ESR1 | 133430 | 785 | UNMAPPED |
| [ ] | 510 | 24.2.18.01 | CYP11A1-related Side-chain cleavage enzyme deficiency | CYP11A1 | 118485 | 289548 | UNMAPPED; weak candidate Nonketotic Hyperglycinemia (0.732) |
| [ ] | 126 | 24.2.19.01 | HSD17B3-related 17-beta-Hydroxysteroid dehydrogenase deficiency | HSD17B3 | 264300 | 752 | MAPPED -> 46,XY disorder of sex development due to 17-beta-hydroxysteroid dehydrogenase 3 deficiency (identifier:ORPHA:752) |

### WP-087: Disorders of steroid metabolism (part 2 of 2)

- Classification: Metabolic Cell Signalling -> Endocrine metabolic disorders
- Subgroup scope: Disorders of steroid metabolism
- Records: 15 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 8)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 123 | 24.2.21.01 | HSD11B2-related 11-beta-Hydroxysteroid dehydrogenase 2 deficiency | HSD11B2 | 218030 | 320 | CANDIDATE -> 46,XY disorder of sex development due to 17-beta-hydroxysteroid dehydrogenase 3 deficiency (0.959) |
| [ ] | 127 | 24.2.22.01 | SRD5A2-related Steroid 5-alpha-reductase type 2 deficiency | SRD5A2 | 264600 | 1331 | CANDIDATE -> 46,XY disorder of sex development due to 5-alpha-reductase 2 deficiency (0.987) |
| [ ] | 129 | 24.2.23.01 | AR-related Androgen receptor deficiency | AR | 300068 | 754 | MAPPED -> Complete androgen insensitivity syndrome (identifier:ORPHA:754) |
| [ ] | 1295 | 24.2.24.01 | AR-related X-linked spinal and bulbar muscular atrophy | AR | 313200 | 754 | MAPPED -> Complete androgen insensitivity syndrome (identifier:ORPHA:754) |
| [ ] | 1092 | 24.2.25.01 | STS-related Steroid sulfatase deficiency | STS | 308100 | 461 | MAPPED -> X-Linked Ichthyosis (alias_exact:x linked ichthyosis) |
| [ ] | 1312 | 24.2.26.01 | SULT2B1-related Hydroxysteroid sulfotransferase deficiency | SULT2B1 | 617571 | - | CANDIDATE -> Autosomal Recessive Congenital Ichthyosis (0.911) |
| [ ] | 1313 | 24.2.27.01 | CLCN2-related Chloride channel 2 superactivity | CLCN2 | 605635 | - | MAPPED -> Type II (alias_exact:familial hyperaldosteronism type 2) |
| [ ] | 133 | 24.2.28.01 | NR3C2-related Mineralocorticoid receptor deficiency | NR3C2 | 264350 | 444916 | UNMAPPED; weak candidate IGF1 Resistance (0.558) |
| [ ] | 131 | 24.2.29.01 | PGR-related Progesterone receptor deficiency | PGR | 264080 | - | UNMAPPED; weak candidate IGF1 Resistance (0.632) |
| [ ] | 1756 | 24.2.30.01 | NR3C2-related Mineralocorticoid receptor superactivity | NR3C2 | 600983 | - | UNMAPPED; weak candidate PRPS1 Superactivity (0.542) |
| [ ] | 2034 | 24.2.31.01 | NR4A2-related Intellectual developmental disorder with language impairment and early-onset DOPA-responsive dystonia-parkinsonism | NR4A2 | 619911 | - | UNMAPPED; weak candidate Autosomal Dominant Dopa-Responsive Dystonia (0.459) |
| [ ] | 2070 | 24.2.32.01 | SCNN1B-related Epithelial sodium channel 1 beta subunit deficiency | SCNN1B | 620125 | - | UNMAPPED |
| [ ] | 2071 | 24.2.33.01 | SCNN1G-related Epithelial sodium channel 1 gamma subunit deficiency | SCNN1G | 620126 | - | UNMAPPED |
| [ ] | 2112 | 24.2.34.01 | SCNN1A-related Epithelial sodium channel 1 alpha subunit deficiency | SCNN1A | 264350 | - | UNMAPPED |
| [ ] | 2113 | 24.2.35.01 | SCNN1G-related Epithelial sodium channel 1 gamma subunit deficiency | SCNN1G | 620126 | - | UNMAPPED |

### WP-088: Unclassified (part 1 of 2)

- Classification: Unclassified -> Unclassified
- Subgroup scope: Unclassified
- Records: 22 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 17)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1057 | 25.1.01.01 | ZDHHC9-related Palmitoyltransferase deficiency | ZDHHC9 | 300799 | 776 | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.827) |
| [ ] | 1307 | 25.1.01.02 | MECP2-related Rett syndrome | MECP2 | 312750 | - | MAPPED -> Rett Syndrome (identifier:OMIM:312750) |
| [ ] | 1058 | 25.1.02.01 | PORCN-related Porcupine palmitoyltransferase deficiency | PORCN | 305600 | 2092 | UNMAPPED; weak candidate Focal Dermal Hypoplasia (0.754) |
| [ ] | 1429 | 25.1.02.02 | RBP4-related Plasma retinol-binding protein deficiency | RBP4 | 616428;615147 | 98938 | UNMAPPED; weak candidate E3-binding protein deficiency (0.800) |
| [ ] | 1460 | 25.1.02.03 | TNR-related Tenascin-R deficiency | TNR | 601995 | - | UNMAPPED |
| [ ] | 591 | 25.1.3.01 | SAMD9-related MIRAGE syndrome | SAMD9 | 617053 | 494433 | UNMAPPED; weak candidate CHARGE syndrome (0.511) |
| [ ] | 589 | 25.1.05.01 | KCNA4-related Potassium channelopathy | KCNA4 | 176266 | - | UNMAPPED; weak candidate CACNA1A-Related Disorder (0.755) |
| [ ] | 853 | 25.1.05.02 | RPE65-related Retinal isomerase deficiency | RPE65 | 204100;613794 | 364055 | UNMAPPED; weak candidate Inherited Retinal Dystrophy (0.567) |
| [ ] | 585 | 25.1.06.01 | PHEX-related X-Linked hypophosphatemia | PHEX | 307800 | 89936 | MAPPED -> X-Linked Hypophosphatemia (alias_exact:x linked hypophosphatemia) |
| [ ] | 889 | 25.1.07.01 | SLC12A3-related Sodium-chloride cotransporter deficiency | SLC12A3 | 263800 | 358 | MAPPED -> Gitelman syndrome (identifier:OMIM:263800) |
| [ ] | 1177 | 25.1.11.01 | KCNA1-related Episodic ataxia-myokymia syndrome | KCNA1 | 160120 | 98809 | UNMAPPED; weak candidate Episodic Ataxia (0.625) |
| [ ] | 1411 | 25.1.12.01 | NOGENE-related Lysine malabsorption syndrome | - | 247950 | - | UNMAPPED; weak candidate Chronic giardiasis with malabsorption (0.494) |
| [ ] | 1422 | 25.1.29.01 | HRAS-related Costello syndrome | HRAS | 218040 | - | MAPPED -> Costello Syndrome (alias_exact:costello syndrome) |
| [ ] | 1757 | 25.1.31.01 | GIMAP6-related Primary immune deficiency | GIMAP6 | 616960 | - | UNMAPPED; weak candidate Primary Coenzyme Q10 Deficiency (0.852) |
| [ ] | 1760 | 25.1.33.01 | ZFYVE19-related Cholestasis, progressive familial intrahepatic, 9 | ZFYVE19 | 619849 | - | UNMAPPED; weak candidate Progressive Familial Heart Block (0.658) |
| [ ] | 2005 | 25.1.34.01 | SLC16A2-related Monocarboxylate transporter 8 deficiency | SLC16A2 | 300523 | - | UNMAPPED; weak candidate Primary Carnitine Deficiency (0.778) |
| [ ] | 2006 | 25.1.35.01 | RYR1-related King-Denborough syndrome | RYR1 | 619542 | - | UNMAPPED |
| [ ] | 2007 | 25.1.35.02 | RYR1-related Minicore myopathy with external ophthalmoplegia | RYR1 | 255320 | - | UNMAPPED; weak candidate Multiminicore Disease (0.493) |
| [ ] | 1211 | 25.1.36.01 | ZDHHC15 palmitoyltransferase deficiency | ZDHHC15 | 300577 | - | UNMAPPED; weak candidate Carnitine Palmitoyltransferase II Deficiency (0.795) |
| [ ] | 2115 | 25.99.99.02 | C19orf12-related Neurodegeneration with brain iron accumulation 4 | C19orf12 | 614298 | - | MAPPED -> MPAN (alias_exact:neurodegeneration with brain iron accumulation 4) |
| [ ] | 2116 | 25.99.99.03 | CISD2-related Wolfram syndrome | CISD2 | 604928 | - | UNMAPPED |
| [ ] | 2117 | 25.99.99.04 | CTBP1-related Hypotonia, ataxia, developmental delay, and tooth enamel defect syndrome | CTBP1 | 617915 | - | UNMAPPED |

### WP-089: Unclassified (part 2 of 2)

- Classification: Unclassified -> Unclassified
- Subgroup scope: Unclassified
- Records: 22 (MAPPED 5, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2118 | 25.99.99.05 | DCC-related Gaze palsy, familial horizontal, with progressive scoliosis, 2 | DCC | 617542 | - | UNMAPPED |
| [ ] | 2119 | 25.99.99.06 | DIAPH1-related Seizures, cortical blindness, microcephaly syndrome | DIAPH1 | 616632 | - | UNMAPPED; weak candidate Galloway-Mowat syndrome (0.650) |
| [ ] | 2121 | 25.99.99.08 | ERCC6L2-related Bone marrow failure syndrome 2 | ERCC6L2 | 160900 | - | MAPPED -> Myotonic Dystrophy Type 1 (identifier:OMIM:160900) |
| [ ] | 2122 | 25.99.99.09 | FGF12-related Developmental and epileptic encephalopathy 47 | FGF12 | 617166 | - | CANDIDATE -> DEE24 (0.978) |
| [ ] | 2123 | 25.99.99.10 | GMPR-related Late-onset progressive external ophthalmoplegia | GMPR | 139265 | - | UNMAPPED; weak candidate Type 2 (0.571) |
| [ ] | 2125 | 25.99.99.12 | HTT-related Huntington disease | HTT | 143100 | - | MAPPED -> Huntington Disease (identifier:OMIM:143100) |
| [ ] | 2126 | 25.99.99.13 | IER3IP1-related Microcephaly, epilepsy, and diabetes syndrome | IER3IP1 | 614231 | - | UNMAPPED; weak candidate renal cysts and diabetes syndrome (0.737) |
| [ ] | 2129 | 25.99.99.16 | MORC2-related Developmental delay, impaired growth, dysmorphic facies, and axonal neuropathy | MORC2 | 619090 | - | UNMAPPED |
| [ ] | 2131 | 25.99.99.18 | P4HTM-related Prolyl 4-hydroxylase deficiency | P4HTM | 618493 | - | MAPPED -> HIDEA_Syndrome (alias_exact:hypotonia hypoventilation impaired intellectual development dysautonomia epilepsy and eye abnormalities) |
| [ ] | 2134 | 25.99.99.21 | RANBP2-related Encephalopathy, acute, infection-induced | RANBP2 | 608033 | - | UNMAPPED; weak candidate Campylobacteriosis (0.590) |
| [ ] | 2135 | 25.99.99.22 | RNF213-related Moyamoya disease | RNF213 | 607151 | - | MAPPED -> Moyamoya Disease (alias_exact:moyamoya disease) |
| [ ] | 2136 | 25.99.99.23 | ROBO3-related Gaze palsy, familial horizontal, with progressive scoliosis | ROBO3 | 607313 | - | UNMAPPED; weak candidate Familial Focal Epilepsy With Variable Foci (0.606) |
| [ ] | 2141 | 25.99.99.28 | WFS1-related Wolfram syndrome | WFS1 | 222300 | - | UNMAPPED |
| [ ] | 2142 | 25.99.99.29 | XRCC4-related Short stature, microcephaly, and endocrine dysfunction | XRCC4 | 616541 | - | UNMAPPED; weak candidate Stromme Syndrome (0.547) |
| [ ] | 2228 | 25.99.99.30 | MUSK-related Fetal akinesia deformation sequence | MUSK | 208150 | - | UNMAPPED |
| [ ] | 2229 | 25.99.99.31 | MUSK-related Myasthenic syndrome, 9, associated with acetylcholine receptor deficiency | MUSK | 616325 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.386) |
| [ ] | 2230 | 25.99.99.32 | DOK7-related Fetal akinesia deformation sequence | DOK7 | 618389 | - | UNMAPPED |
| [ ] | 2231 | 25.99.99.33 | DOK7-related Myasthenic syndrome | DOK7 | 254300 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.776) |
| [ ] | 2233 | 25.99.99.34 | TERT-related Dyskeratosis congenita (ad, ar) | TERT | 613989 | - | UNMAPPED; weak candidate Dyskeratosis Congenita (0.880) |
| [ ] | 2234 | 25.99.99.35 | TERC-related Dyskeratosis congenita (ad) | TERC | 127550 | - | CANDIDATE -> Dyskeratosis Congenita (0.936) |
| [ ] | 2235 | 25.99.99.36 | RTEL1-related Dyskeratosis congenita (ad, ar) | RTEL1 | 615190 | - | UNMAPPED; weak candidate Dyskeratosis Congenita (0.880) |
| [ ] | 2236 | 25.99.99.37 | ALMS1-related Alstrom syndrome | ALMS1 | 203800 | - | MAPPED -> Alstrom Syndrome (alias_exact:alstrom syndrome) |

### WP-090: Disorders of ECM glycoproteins (part 1 of 5)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM glycoproteins
- Records: 22 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 20)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1883 | 26.01.01.01 | AGRN-related Myasthenic syndrome, congenital, 8 | AGRN | 615120 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.613) |
| [ ] | 1884 | 26.01.02.01 | AMBN- related Amelogenesis imperfecta, type 1F | AMBN | 616270 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type I (0.757) |
| [ ] | 1885 | 26.01.03.01 | AMELX-related Amelogenesis imperfecta, type 1E | AMELX | 301200 | - | UNMAPPED; weak candidate Amelogenesis Imperfecta (0.852) |
| [ ] | 1886 | 26.01.04.01 | BMPER-related Diaphanospondylodysostosis | BMPER | 608022 | - | UNMAPPED; weak candidate Arterial Dissection-Lentiginosis Syndrome (0.538) |
| [ ] | 1887 | 26.01.05.01 | CILP;THBS2-related Intervertebral disc disease (susceptibility) | CILP;THBS2 | 603932 | - | UNMAPPED; weak candidate Malignant hyperthermia of anesthesia (0.608) |
| [ ] | 1888 | 26.01.06.01 | COCH-related Deafness, autosomal dominant, 9 | COCH | 601369 | - | UNMAPPED; weak candidate DFNA13 (0.815) |
| [ ] | 1889 | 26.01.06.02 | COCH-related Deafness, autosomal recessive 110 | COCH | 618094 | - | UNMAPPED; weak candidate EBS Autosomal Recessive (KRT14 null) (0.800) |
| [ ] | 1890 | 26.01.07.01 | COLQ-related Myasthenic syndrome, congenital, 5 | COLQ | 603034 | - | CANDIDATE -> Congenital Myasthenic Syndrome (0.909) |
| [ ] | 1891 | 26.01.08.01 | COMP-related Carpal tunnel syndrome 2 | COMP | 619161 | - | UNMAPPED |
| [ ] | 1892 | 26.01.08.02 | COMP-related Epiphyseal dysplasia, multiple, 1 | COMP | 132400 | - | MAPPED -> EDM1 (alias_exact:edm1) |
| [ ] | 1893 | 26.01.08.03 | COMP-related Pseudoachondroplasia | COMP | 177170 | - | UNMAPPED; weak candidate Multiple Epiphyseal Dysplasia (0.557) |
| [ ] | 1894 | 26.01.09.01 | CRELD1-related Atrioventricular septal defect | CRELD1 | 606217 | - | UNMAPPED; weak candidate TGA-VSD (0.818) |
| [ ] | 1895 | 26.01.10.01 | CTHRC1-related Barrett esophagus | CTHRC1 | 606217 | - | UNMAPPED; weak candidate Esophageal Carcinoma (0.615) |
| [ ] | 1896 | 26.01.11.01 | DMP1-related Hypophosphatemic rickets, autosomal recessive | DMP1 | 241520 | - | UNMAPPED; weak candidate SPG9B (0.682) |
| [ ] | 1897 | 26.01.12.01 | DSPP-related Deafness, autosomal dominant 39, with dentinogenesis | DSPP | 605594 | - | UNMAPPED; weak candidate Autosomal Dominant Osteopetrosis Type II (0.619) |
| [ ] | 1898 | 26.01.12.02 | DSPP-related Dentin dysplasia, type II | DSPP | 125420 | - | UNMAPPED; weak candidate Frontonasal dysplasia with alopecia and genital anomaly (0.784) |
| [ ] | 1899 | 26.01.12.03 | DSPP-related Dentinogenesis imperfecta, Shields type II | DSPP | 125490 | - | UNMAPPED; weak candidate Amelogenesis Imperfecta (0.800) |
| [ ] | 1900 | 26.01.12.04 | DSPP-related Dentinogenesis imperfecta, Shields type III | DSPP | 125500 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type III (0.771) |
| [ ] | 1901 | 26.01.13.01 | ECM1-related Lipoid proteinosis of Urbach and Wiethe | ECM1 | 247100 | - | UNMAPPED; weak candidate Minimal Change Disease (0.473) |
| [ ] | 1902 | 26.01.14.01 | EFEMP1-related Doyne honeycomb retinal dystrophy | EFEMP1 | 126600 | - | UNMAPPED; weak candidate CRB1 Retinal Dystrophies (0.692) |
| [ ] | 2100 | 26.01.14.02 | EFEMP1-related Cutis laxa, autosomal recessive, type ID | EFEMP1 | 620780 | - | UNMAPPED; weak candidate AR (0.721) |
| [ ] | 1903 | 26.01.15.01 | EFEMP2-related Cutis laxa, autosomal recessive, type 1B | EFEMP2 | 614437 | - | UNMAPPED; weak candidate Autosomal Recessive PFBC (0.710) |

### WP-091: Disorders of ECM glycoproteins (part 2 of 5)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM glycoproteins
- Records: 22 (MAPPED 4, AMBIGUOUS 0, CANDIDATE 2, UNMAPPED 16)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1904 | 26.01.16.01 | ELN-related Supravalvular aortic stenosis | ELN | 185500 | - | UNMAPPED; weak candidate Congenital Renal Artery Stenosis (0.521) |
| [ ] | 1905 | 26.01.16.02 | ELN-related Cutis laxa, autosomal dominant 1 | ELN | 123700 | - | UNMAPPED |
| [ ] | 1906 | 26.01.17.01 | EYS-related Retinitis pigmentosa 25 | EYS | 602772 | - | MAPPED -> EYS-Related Retinitis Pigmentosa (alias_exact:retinitis pigmentosa 25) |
| [ ] | 1907 | 26.01.18.01 | FBLN1-related Synpolydactyly 2 | FBLN1 | 608180 | - | UNMAPPED; weak candidate ML-DS (0.471) |
| [ ] | 1908 | 26.01.19.02 | FBLN5-related Cutis laxa, autosomal dominant 2 | FBLN5 | 614434 | - | CANDIDATE -> ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3 (0.968) |
| [ ] | 1909 | 26.01.19.03 | FBLN5-related Neuropathy, hereditary, with or without age-related macular degeneration | FBLN5 | 608895 | - | MAPPED -> Age-Related Macular Degeneration (alias_exact:macular degeneration) |
| [ ] | 1910 | 26.01.20.01 | FBN1-related Acromicric dysplasia | FBN1 | 102370 | - | UNMAPPED; weak candidate Geleophysic Dysplasia (0.634) |
| [ ] | 1911 | 26.01.20.02 | FBN1-related Ectopia lentis, familial | FBN1 | 129600 | - | UNMAPPED |
| [ ] | 1912 | 26.01.20.03 | FBN1-related Geleophysic dysplasia 2 | FBN1 | 614185 | - | MAPPED -> GD2 (alias_exact:geleophysic dysplasia 2) |
| [ ] | 1913 | 26.01.20.04 | FBN1-related Marfan lipodystrophy syndrome | FBN1 | 616914 | - | UNMAPPED; weak candidate Marfan Syndrome (0.682) |
| [ ] | 1914 | 26.01.20.05 | FBN1-related Marfan syndrome | FBN1 | 154700 | - | MAPPED -> Marfan Syndrome (alias_exact:marfan syndrome) |
| [ ] | 1915 | 26.01.20.06 | FBN1-related MASS syndrome | FBN1 | 604308 | - | UNMAPPED |
| [ ] | 1916 | 26.01.20.07 | FBN1-related Stiff skin syndrome | FBN1 | 184900 | - | UNMAPPED |
| [ ] | 1917 | 26.01.20.08 | FBN1-related Weill-Marchesani syndrome 2, dominant | FBN1 | 608328 | - | UNMAPPED |
| [ ] | 1918 | 26.01.21.01 | FBN2-related Contractural arachnodactyly, congenital | FBN2 | 121050 | - | UNMAPPED; weak candidate Arthrogryposis Multiplex Congenita (0.667) |
| [ ] | 1919 | 26.01.21.02 | FBN2-related Macular degeneration, early-onset | FBN2 | 616118 | - | UNMAPPED; weak candidate Age-Related Macular Degeneration (0.769) |
| [ ] | 1920 | 26.01.22.01 | FGA;FGB;FGG-related Dysﬁbrinogenemia, congenital | FGA;FGB;FGG | 616004 | - | UNMAPPED |
| [ ] | 1921 | 26.01.23.01 | FN1-related Glomerulopathy with ﬁbronectin deposits 2 | FN1 | 601894 | - | UNMAPPED; weak candidate STING-Associated Vasculopathy with Onset in Infancy (0.552) |
| [ ] | 1922 | 26.01.23.02 | FN1-related Spondylometaphyseal dysplasia, corner fracture type | FN1 | 184255 | - | UNMAPPED; weak candidate Spondylometaphyseal Dysplasia Kozlowski Type (0.841) |
| [ ] | 1923 | 26.01.24.01 | FRAS1-related Fraser syndrome 1 | FRAS1 | 219000 | - | UNMAPPED; weak candidate Timothy Syndrome (0.448) |
| [ ] | 1924 | 26.01.25.01 | GLDN-related Lethal congenital contracture syndrome 11 | GLDN | 617194 | - | CANDIDATE -> LCCS (0.988) |
| [ ] | 1925 | 26.01.26.01 | HMCN1-related Macular degeneration, age-related, 1 | HMCN1 | 603075 | - | UNMAPPED; weak candidate Age-Related Macular Degeneration (0.741) |

### WP-092: Disorders of ECM glycoproteins (part 3 of 5)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM glycoproteins
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1926 | 26.01.27.01 | IGFALS- related Acid-labile subunit deﬁciency | IGFALS | 615961 | - | UNMAPPED; weak candidate IGFALS Deficiency (0.800) |
| [ ] | 1927 | 26.01.28.01 | IGFBP7-related Retinal arterial macroaneurysm with supravalvular pulmonic stenosis | IGFBP7 | 614224 | - | UNMAPPED; weak candidate Arterial Dissection-Lentiginosis Syndrome (0.514) |
| [ ] | 1928 | 26.01.29.01 | ANOS1-related Hypogonadotropic hypogonadism 1 with or without anosmia | ANOS1 | 308700 | - | MAPPED -> ANOS1 (alias_exact:kallmann syndrome 1) |
| [ ] | 1929 | 26.01.30.01 | LAMA1-related Poretti–Boltshauser syndrome | LAMA1 | 615960 | - | UNMAPPED |
| [ ] | 1930 | 26.01.31.01 | LAMA2-related Muscular dystrophy, congenital merosin-deﬁcient, 1A | LAMA2 | 607855 | - | UNMAPPED; weak candidate Limb-Girdle Muscular Dystrophy, Autosomal Dominant (0.602) |
| [ ] | 1931 | 26.01.32.01 | LAMA3-related Epidermolysis bullosa, junctional 2B, severe | LAMA3 | 619784 | - | UNMAPPED; weak candidate Epidermolysis Bullosa (0.667) |
| [ ] | 1932 | 26.01.33.01 | LAMA4-related Cardiomyopathy, dilated, 1 | LAMA4 | 615235 | - | UNMAPPED; weak candidate Dilated Cardiomyopathy (0.667) |
| [ ] | 1933 | 26.01.34.01 | LAMB1-related Lissencephaly 5 | LAMB1 | 615191 | - | CANDIDATE -> Reelin Pathway Lissencephaly (0.929) |
| [ ] | 1935 | 26.01.35.01 | LAMB2-related Nephrotic syndrome, type 5, with or without ocular abnormalities | LAMB2 | 614199 | - | UNMAPPED; weak candidate Temtamy Syndrome (0.639) |
| [ ] | 1934 | 26.01.35.02 | LAMB2-related Pierson syndrome | LAMB2 | 609049 | - | UNMAPPED; weak candidate Galloway-Mowat syndrome (0.753) |
| [ ] | 1936 | 26.01.36.01 | LAMB3-related Epidermolysis bullosa, junctional 1A, intermediate | LAMB3 | 226650 | - | UNMAPPED; weak candidate Epidermolysis Bullosa (0.609) |
| [ ] | 1937 | 26.01.37.01 | LAMC3-related Cortical malformations, occipital | LAMC3 | 614115 | - | UNMAPPED; weak candidate KATNB1-related Cortical Malformation (0.792) |
| [ ] | 1939 | 26.01.38.01 | LGI1-related Epilepsy, familial temporal lobe, 1 | LGI1 | 600512 | - | UNMAPPED; weak candidate Familial Focal Epilepsy With Variable Foci (0.667) |
| [ ] | 1938 | 26.01.39.01 | LGI4-related Arthrogryposis multiplex congenita, neurogenic, with myelin defect | LGI4 | 617468 | - | UNMAPPED; weak candidate Arthrogryposis Multiplex Congenita (0.694) |
| [ ] | 1940 | 26.01.40.01 | LTBP2-related Weill-Marchesani syndrome 3, recessive | LTBP2 | 614819 | - | UNMAPPED; weak candidate Wieacker-Wolff Syndrome (0.582) |
| [ ] | 1941 | 26.01.40.02 | LTBP2-related Glaucoma 3, primary congenital, D | LTBP2 | 613086 | - | UNMAPPED; weak candidate Permanent Primary (0.622) |
| [ ] | 1942 | 26.01.40.03 | LTBP2-related Microspherophakia and/or megalocornea, with ectopia lentis and with or without secondary glaucoma | LTBP2 | 251750 | - | UNMAPPED; weak candidate MCPH2 (0.508) |
| [ ] | 1943 | 26.01.41.01 | LTBP3-related Dental anomalies and short stature | LTBP3 | 601216 | - | UNMAPPED |
| [ ] | 1944 | 26.01.41.02 | LTBP3-related Geleophysic dysplasia 3 | LTBP3 | 617809 | - | MAPPED -> GD3 (alias_exact:geleophysic dysplasia 3) |
| [ ] | 2191 | 26.01.41.04 | LTBP3-related Thoracic aortic aneurysm and dissection | LTBP3 | 602090 | - | UNMAPPED |
| [ ] | 1945 | 26.01.42.01 | LTBP4-related Cutis laxa, autosomal recessive, type IC | LTBP4 | 613177 | - | UNMAPPED |
| [ ] | 1947 | 26.01.43.01 | MATN3-related Epiphyseal dysplasia, multiple, 5 | MATN3 | 607078 | - | MAPPED -> EDM5 (alias_exact:edm5) |

### WP-093: Disorders of ECM glycoproteins (part 4 of 5)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM glycoproteins
- Records: 22 (MAPPED 1, AMBIGUOUS 0, CANDIDATE 3, UNMAPPED 18)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1946 | 26.01.43.02 | MATN3-related Spondyloepimetaphyseal dysplasia, Borochowitz-Cormier-Daire type | MATN3 | 608728 | - | UNMAPPED; weak candidate Multiple Epiphyseal Dysplasia (0.550) |
| [ ] | 1948 | 26.01.44.01 | MFAP5-related Aortic aneurysm, familial thoracic 9 | MFAP5 | 616166 | - | MAPPED -> MFAP5-related (alias_exact:aortic aneurysm familial thoracic 9) |
| [ ] | 1949 | 26.01.45.01 | MGP-related Keutel syndrome | MGP | 245150 | - | UNMAPPED; weak candidate ENPP1-related (0.496) |
| [ ] | 1950 | 26.01.46.01 | OTOG-related Deafness, autosomal recessive 18B | OTOG | 614945 | - | UNMAPPED; weak candidate EBS Autosomal Recessive (KRT14 null) (0.800) |
| [ ] | 1951 | 26.01.47.01 | PXDN-related Anterior segment dysgenesis 7 | PXDN | 269400 | - | CANDIDATE -> FOXE3-Related Anterior Segment Dysgenesis (0.964) |
| [ ] | 1952 | 26.01.48.01 | RELN-related Lissencephaly 2 (Norman-Roberts type) | RELN | 257320 | - | CANDIDATE -> Reelin Pathway Lissencephaly (0.963) |
| [ ] | 1953 | 26.01.48.02 | RELN-related Epilepsy, familial temporal lobe, 7 | RELN | 616436 | - | UNMAPPED; weak candidate Reelin Pathway Lissencephaly (0.472) |
| [ ] | 1954 | 26.01.49.01 | RSPO1-related Palmoplantar hyperkeratosis with squamous cell carcinoma of skin and 46,XX sex reversal | RSPO1 | 610644 | - | UNMAPPED; weak candidate 46,XX testicular disorder of sex development (0.327) |
| [ ] | 1955 | 26.01.50.01 | TRSPO2-related Tetraamelia syndrome 2 | RSPO2 | 618021 | - | UNMAPPED; weak candidate Hermansky-Pudlak Syndrome (0.600) |
| [ ] | 1956 | 26.01.51.01 | RSPO4-related Nail disorder, nonsyndromic congenital, 4 | RSPO4 | 206800 | - | UNMAPPED; weak candidate Dyskeratosis Congenita (0.634) |
| [ ] | 1957 | 26.01.52.01 | SMOC1-related Microphthalmia with limb anomalies | SMOC1 | 206920 | - | UNMAPPED |
| [ ] | 1958 | 26.01.53.01 | SMOC2-related Dentin dysplasia, type I | SMOC2 | 125400 | - | UNMAPPED; weak candidate Thanatophoric Dysplasia Type 1 (0.755) |
| [ ] | 1959 | 26.01.54.01 | SRPX2-related Rolandic epilepsy, mental retardation, and speech dyspraxia | SRPX2 | 300643 | - | UNMAPPED; weak candidate SRPX2-related Speech-Epilepsy-Polymicrogyria (0.522) |
| [ ] | 1960 | 26.01.55.01 | TECTA-related Deafness, autosomal dominant 8/12 | TECTA | 601543 | - | UNMAPPED; weak candidate DFNA13 (0.772) |
| [ ] | 1961 | 26.01.55.02 | TECTA-related Deafness, autosomal recessive 21 | TECTA | 603629 | - | UNMAPPED; weak candidate EBS Autosomal Recessive (KRT14 null) (0.815) |
| [ ] | 1971 | 26.01.58.01 | TSPEAR-related Deafness, autosomal recessive 98 | TSPEAR | 614861 | - | UNMAPPED; weak candidate EBS Autosomal Recessive (KRT14 null) (0.815) |
| [ ] | 1972 | 26.01.58.02 | TSPEAR-related Ectodermal dysplasia 14, hair/tooth type with or without hypohidrosis | TSPEAR | 618180 | - | UNMAPPED; weak candidate KRT85-Related Pure Hair-Nail Ectodermal Dysplasia (0.629) |
| [ ] | 1973 | 26.01.59.01 | VWA3B-related Spinocerebellar ataxia, autosomal recessive 22 | VWA3B | 616948 | - | CANDIDATE -> CALFAN Syndrome (0.978) |
| [ ] | 1975 | 26.01.60.01 | VWF-related von Willebrand disease, type 1 | VWF | 193400 | - | UNMAPPED; weak candidate Hereditary von Willebrand Disease (0.863) |
| [ ] | 1974 | 26.01.60.02 | VWF-related von Willebrand disease, type 3 | VWF | 277480 | - | UNMAPPED; weak candidate Hereditary von Willebrand Disease (0.863) |
| [ ] | 1976 | 26.01.60.03 | VWF-related von Willebrand disease, types 2A, 2B, 2M, and 2N | VWF | 613554 | - | UNMAPPED; weak candidate Hereditary von Willebrand Disease (0.667) |
| [ ] | 1977 | 26.01.61.01 | CCN6-related Arthropathy, progressive pseudorheumatoid, of childhood | CCN6 | 208230 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Strudwick Type (0.673) |

### WP-094: Disorders of ECM glycoproteins (part 5 of 5)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM glycoproteins
- Records: 2 (MAPPED 0, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 2)
- Work: curate missing DisMech pages for UNMAPPED rows.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1978 | 26.01.62.01 | ZP1-related Oocyte maturation defect 1 | ZP1 | 615774 | - | UNMAPPED; weak candidate Hypomaturation (0.597) |
| [ ] | 1979 | 26.01.63.01 | ZP3-related Oocyte maturation defect 3 | ZP3 | 617712 | - | UNMAPPED; weak candidate Hypomaturation (0.597) |

### WP-095: Disorders of fibrillar collagens (part 1 of 2)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of fibrillar collagens
- Records: 22 (MAPPED 3, AMBIGUOUS 0, CANDIDATE 4, UNMAPPED 15)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1776 | 26.02.01.01 | COL1A1-related Caffey disease | COL1A1 | 114000 | - | UNMAPPED; weak candidate Arterial Calcification of Infancy (0.737) |
| [ ] | 1777 | 26.02.01.02 | COL1A1;COL1A2-related Ehlers-Danlos syndrome, arthrochalasia type 1 | COL1A1;COL1A2 | 130060 | - | UNMAPPED; weak candidate Arthrogryposis Multiplex Congenita (0.853) |
| [ ] | 1778 | 26.02.01.03 | COL1A1;COL1A2-related Osteogenesis imperfecta, autosomal dominant | COL1A1;COL1A2 | 166200 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type I (0.847) |
| [ ] | 1779 | 26.02.01.04 | COL1A1;COL1A2-related Osteogenesis imperfecta, types II | COL1A1;COL1A2 | 166210 | - | CANDIDATE -> Osteogenesis Imperfecta Type XII (0.969) |
| [ ] | 1780 | 26.02.01.05 | COL1A1;COL1A2-related Osteogenesis imperfecta, types III | COL1A1;COL1A2 | 259420 | - | CANDIDATE -> Osteogenesis Imperfecta Type XIII (0.970) |
| [ ] | 1782 | 26.02.01.06 | COL1A1;COL1A2-related Osteogenesis imperfecta, types IV | COL1A1;COL1A2 | 166220 | - | CANDIDATE -> Osteogenesis Imperfecta Type XIV (0.969) |
| [ ] | 1781 | 26.02.01.07 | COL1A1; COL1A2-related Combined osteogenesis imperfecta, and Ehlers–Danlos syndrome 1 | COL1A1; COL1A2 | 619115 | - | UNMAPPED; weak candidate Ehlers-Danlos Syndrome, COL5A1-related (0.615) |
| [ ] | 1784 | 26.02.02.01 | COL1A2-related Ehlers–Danlos syndrome, arthrochalasia type 2 | COL1A2 | 617821 | - | CANDIDATE -> Hypermobile Ehlers-Danlos Syndrome (0.949) |
| [ ] | 1783 | 26.02.02.02 | COL1A2-related Ehlers–Danlos syndrome, cardiac valvular type | COL1A2 | 225320 | - | UNMAPPED; weak candidate Vascular Ehlers-Danlos Syndrome (0.850) |
| [ ] | 1785 | 26.02.02.03 | COL1A2-related Combined osteogenesis imperfecta and Ehlers-Danlos syndrome 2 | COL1A2 | 619120 | - | UNMAPPED; weak candidate Ehlers-Danlos Syndrome, COL5A1-related (0.615) |
| [ ] | 1786 | 26.02.03.01 | COL2A1-related Achondrogenesis, type II or hypochondrogenesis | COL2A1 | 200610 | - | UNMAPPED; weak candidate Achondrogenesis Type II (0.702) |
| [ ] | 1787 | 26.02.03.02 | COL2A1-related Avascular necrosis of the femoral head | COL2A1 | 608805 | - | UNMAPPED |
| [ ] | 1789 | 26.02.03.03 | COL2A1-related Czech dysplasia | COL2A1 | 609162 | - | UNMAPPED; weak candidate Kniest Dysplasia (0.710) |
| [ ] | 1788 | 26.02.03.04 | COL2A1-related Kniest dysplasia | COL2A1 | 156550 | - | MAPPED -> Kniest Dysplasia (alias_exact:kniest dysplasia) |
| [ ] | 1790 | 26.02.03.05 | COL2A1-related Legg-Calve-Perthes disease | COL2A1 | 150600 | - | UNMAPPED |
| [ ] | 1792 | 26.02.03.06 | COL2A1-related Osteoarthritis with mild chondrodysplasia | COL2A1 | 604864 | - | UNMAPPED; weak candidate Kniest Dysplasia (0.585) |
| [ ] | 1791 | 26.02.03.07 | COL2A1-related Platyspondylic skeletal dysplasia, Torrance type | COL2A1 | 151210 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Strudwick Type (0.660) |
| [ ] | 1793 | 26.02.03.08 | COL2A1-related Spondyloepiphyseal dysplasia congenita | COL2A1 | 183900 | - | MAPPED -> Spondyloepiphyseal Dysplasia Congenita (alias_exact:spondyloepiphyseal dysplasia congenita) |
| [ ] | 1794 | 26.02.03.09 | COL2A1-related Spondyloepimetaphyseal dysplasia, Strudwick type | COL2A1 | 184250 | - | MAPPED -> Spondyloepimetaphyseal Dysplasia Strudwick Type (alias_exact:spondyloepimetaphyseal dysplasia strudwick type) |
| [ ] | 1795 | 26.02.03.10 | COL2A1-related Spondyloepiphyseal dysplasia, Stanescu type | COL2A1 | 616583 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Strudwick Type (0.831) |
| [ ] | 1796 | 26.02.03.11 | COL2A1-related Spondyloperipheral dysplasia | COL2A1 | 271700 | - | UNMAPPED; weak candidate Spondyloepiphyseal Dysplasia Congenita (0.758) |
| [ ] | 1797 | 26.02.03.12 | COL2A1-related Stickler sydrome, type I, nonsyndromic ocular | COL2A1 | 609508 | - | UNMAPPED; weak candidate Stickler Syndrome Type 1 (0.840) |

### WP-096: Disorders of fibrillar collagens (part 2 of 2)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of fibrillar collagens
- Records: 18 (MAPPED 7, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 10)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1798 | 26.02.03.13 | COL2A1-related Stickler sydrome, type I | COL2A1 | 108300 | - | MAPPED -> Stickler Syndrome Type 1 (identifier:OMIM:108300) |
| [ ] | 1775 | 26.02.04.01 | COL3A1-related Ehlers–Danlos syndrome, vascular type | COL3A1 | 130050 | - | MAPPED -> Vascular Ehlers-Danlos Syndrome (alias_exact:ehlers danlos syndrome type 4) |
| [ ] | 1799 | 26.02.04.02 | COL3A1-related Polymicrogyria with or without vascular-type EDS | COL3A1 | 618343 | - | UNMAPPED; weak candidate Vascular Ehlers-Danlos Syndrome (0.429) |
| [ ] | 1810 | 26.02.10.01 | COL5A1;COL5A2-related Ehlers–Danlos syndrome, classic | COL5A1;COL5A2 | 130000 | - | UNMAPPED; weak candidate Ehlers-Danlos Syndrome (0.846) |
| [ ] | 1811 | 26.02.10.02 | COL5A1- related Fibromuscular dysplasia, multifocal | COL5A1 | 619329 | - | UNMAPPED |
| [ ] | 1812 | 26.02.11.01 | COL5A2-related Ehlers–Danlos syndrome, classic type, 2 | COL5A2 | 130010 | - | CANDIDATE -> Classical EDS (0.972) |
| [ ] | 1823 | 26.02.16.02 | COL8A2-related Posterior polymorphous corneal dystrophy 2 | COL8A2 | 609140 | - | UNMAPPED; weak candidate Fuchs Endothelial Corneal Dystrophy (0.622) |
| [ ] | 1835 | 26.02.21.01 | COL11A1-related Deafness, autosomal dominant 37 | COL11A1 | 618533 | - | UNMAPPED |
| [ ] | 1836 | 26.02.21.02 | COL11A1-related Fibrochondrogenesis 1 | COL11A1 | 228520 | - | MAPPED -> Type 1 (alias_exact:fibrochondrogenesis 1) |
| [ ] | 1837 | 26.02.21.03 | COL11A1-related Marshall syndrome | COL11A1 | 154780 | - | UNMAPPED |
| [ ] | 1838 | 26.02.21.04 | COL11A1-related Stickler syndrome, type II | COL11A1 | 604841 | - | UNMAPPED |
| [ ] | 1839 | 26.02.22.01 | COL11A2-related Deafness, autosomal dominant 13 | COL11A2 | 601868 | - | MAPPED -> DFNA13 (alias_exact:dfna13) |
| [ ] | 1840 | 26.02.22.02 | COL11A2-related Deafness, autosomal recessive 53 | COL11A2 | 609706 | - | MAPPED -> DFNB53 (alias_exact:dfnb53) |
| [ ] | 1841 | 26.02.22.03 | COL11A2-related Fibrochondrogenesis 2 | COL11A2 | 614524 | - | MAPPED -> Type 2 (alias_exact:fibrochondrogenesis 2) |
| [ ] | 1842 | 26.02.22.04 | COL11A2-related Otospondylomegaepiphyseal dysplasia, autosomal dominant | COL11A2 | 184840 | - | MAPPED -> COL11A2-Related Skeletal Spectrum (alias_exact:otospondylomegaepiphyseal dysplasia autosomal dominant) |
| [ ] | 1844 | 26.02.22.05 | COL11A2-relatedOtospondylomegaepiphyseal dysplasia, autosomal recessive | COL11A2 | 215150 | - | UNMAPPED; weak candidate COL11A2-Related Skeletal Spectrum (0.758) |
| [ ] | 1851 | 26.02.27.01 | COL25A1-related Fibrosis of extraocular muscles, congenital, 5 | COL25A1 | 616219 | - | UNMAPPED; weak candidate Classic Cystic Fibrosis (0.313) |
| [ ] | 1852 | 26.02.28.01 | COL27A1-related Steel syndrome | COL27A1 | 615155 | - | UNMAPPED; weak candidate TBX6-Associated Congenital Scoliosis (0.372) |

### WP-097: Disorders of  fibrillar collagen processing and maturation

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of  fibrillar collagen processing and maturation
- Records: 24 (MAPPED 17, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 7)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2154 | 26.03.01.01 | IFITM5-related Osteogenesis imperfecta | IFITM5 | 610967 | - | MAPPED -> Osteogenesis Imperfecta Type V (alias_exact:osteogenesis imperfecta type 5) |
| [ ] | 2155 | 26.03.02.01 | CRTAP-related Osteogenesis imperfecta | CRTAP | 610682 | - | MAPPED -> Osteogenesis Imperfecta Type VII (alias_exact:osteogenesis imperfecta type 7) |
| [ ] | 2157 | 26.03.03.01 | P3H1-related Osteogenesis imperfecta | P3H1 | 610915 | - | MAPPED -> Osteogenesis Imperfecta Type VIII (alias_exact:osteogenesis imperfecta type 8) |
| [ ] | 2158 | 26.03.04.01 | PPIB-related Osteogenesis imperfecta | PPIB | 259440 | - | MAPPED -> Osteogenesis Imperfecta Type IX (alias_exact:osteogenesis imperfecta type 9) |
| [ ] | 2159 | 26.03.05.01 | SERPINH1-related Osteogenesis imperfecta | SERPINH1 | 613848 | - | MAPPED -> Osteogenesis Imperfecta Type X (alias_exact:osteogenesis imperfecta type 10) |
| [ ] | 2160 | 26.03.06.01 | KDELR2-related Osteogenesis imperfecta | KDELR2 | 619131 | - | MAPPED -> Osteogenesis Imperfecta Type XXI (alias_exact:osteogenesis imperfecta type xxi) |
| [ ] | 2161 | 26.03.07.01 | BMP1-related Osteogenesis imperfecta | BMP1 | 614856 | - | MAPPED -> Osteogenesis Imperfecta Type XIII (alias_exact:osteogenesis imperfecta type xiii) |
| [ ] | 2162 | 26.03.08.01 | SEC24D-related Osteogenesis imperfecta-like | SEC24D | 616294 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type I (0.862) |
| [ ] | 2163 | 26.03.09.01 | P4HB-related Osteogenesis imperfecta-like | P4HB | 112240 | - | UNMAPPED; weak candidate Osteogenesis Imperfecta Type I (0.862) |
| [ ] | 1997 | 26.03.10.01 | PLOD1;FKBP14-related Ehlers-Danlos, Kyphoscoliotic | PLOD1;FKBP14 | 225400;614557 | - | UNMAPPED; weak candidate Ehlers-Danlos Syndrome (0.640) |
| [ ] | 1984 | 26.03.11.01 | ADAMTS2-related Ehlers-Danlos syndrome, dermatosparaxis type | ADAMTS2 | 225410 | - | UNMAPPED; weak candidate Dermatosparaxis EDS (0.882) |
| [ ] | 2164 | 26.03.12.01 | MBTPS2-related Osteogenesis imperfecta | MBTPS2 | 301014 | - | MAPPED -> Osteogenesis Imperfecta Type XIX (alias_exact:osteogenesis imperfecta type xix) |
| [ ] | 2165 | 26.03.13.01 | PLS3-related Osteoporosis familial | PLS3 | 300910 | - | UNMAPPED; weak candidate Osteoporosis (0.727) |
| [ ] | 2166 | 26.03.14.01 | SERPINF1-related Osteogenesis imperfecta | SERPINF1 | 613982 | - | MAPPED -> Osteogenesis Imperfecta Type VI (alias_exact:osteogenesis imperfecta type 6) |
| [ ] | 2167 | 26.03.15.01 | WNT1-related Osteogenesis imperfecta | WNT1 | 615220 | - | MAPPED -> Osteogenesis Imperfecta Type XV (alias_exact:osteogenesis imperfecta type xv) |
| [ ] | 2168 | 26.03.16.01 | TMEM38B-related Osteogenesis imperfecta | TMEM38B | 615066 | - | MAPPED -> Osteogenesis Imperfecta Type XIV (alias_exact:osteogenesis imperfecta type xiv) |
| [ ] | 2169 | 26.03.17.01 | CREB3L1-related Osteogenesis imperfecta (OASIS) | CREB3L1 | 616229 | - | MAPPED -> Osteogenesis Imperfecta Type XVI (alias_exact:osteogenesis imperfecta type xvi) |
| [ ] | 2170 | 26.03.18.01 | SPARC-related Osteogenesis imperfecta | SPARC | 616507 | - | MAPPED -> Osteogenesis Imperfecta Type XVII (identifier:OMIM:616507) |
| [ ] | 2171 | 26.03.19.01 | MESD-related Osteogenesis imperfecta | MESD | 618644 | - | MAPPED -> Osteogenesis Imperfecta Type XX (alias_exact:osteogenesis imperfecta type xx) |
| [ ] | 2172 | 26.03.20.01 | TENT5A-related Osteogenesis imperfecta (FAM46A) | TENT5A | 617952 | - | MAPPED -> Osteogenesis Imperfecta Type XVIII (alias_exact:osteogenesis imperfecta type xviii) |
| [ ] | 2173 | 26.03.21.01 | FKBP10-related Osteogenesis imperfecta | FKBP10 | 610968;259450 | - | MAPPED -> Osteogenesis Imperfecta Type XI (alias_exact:osteogenesis imperfecta type xi) |
| [ ] | 2174 | 26.03.22.01 | PLOD2-related Osteogenesis imperfecta | PLOD2 | 609220 | - | UNMAPPED; weak candidate Amelogenesis Imperfecta (0.870) |
| [ ] | 2175 | 26.03.23.01 | CCDC134-related Osteogenesis imperfecta | CCDC134 | 619795 | - | MAPPED -> Osteogenesis Imperfecta Type XXII (alias_exact:osteogenesis imperfecta type xxii) |
| [ ] | 2192 | 26.3.24.01 | P4HA1-related combined kyphoscoliotic-musculocontractural EDS | P4HA1 | 176710 | - | UNMAPPED; weak candidate MMACHC-related Methylmalonic Aciduria and Homocystinuria, cblC Type (0.449) |

### WP-098: Disorders of ECM proteoglycans + 1 adjacent subgroup(s)

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of ECM proteoglycans; Disorders of non-fibrillar collagens
- Records: 48 (MAPPED 7, AMBIGUOUS 2, CANDIDATE 0, UNMAPPED 39)
- Work: curate missing DisMech pages for UNMAPPED rows; resolve ambiguous exact matches by tightening aliases/cross-references; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 1853 | 26.05.01.01 | ACAN-related Spondyloepiphyseal dysplasia, Kimberley type | ACAN | 608361 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.800) |
| [ ] | 1854 | 26.05.01.02 | ACAN-related Short stature and advanced bone age, with or without early-onset osteoarthritis and/or osteochondritis dissecans | ACAN | 165800 | - | UNMAPPED; weak candidate Secondary Osteoarthritis (0.511) |
| [ ] | 1855 | 26.05.01.03 | ACAN-related Spondyloepimetaphyseal dysplasia, aggrecan type | ACAN | 612813 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.882) |
| [ ] | 1856 | 26.05.02.01 | ASPN-related Lumbar disc degeneration | ASPN | 603932 | - | UNMAPPED; weak candidate Age-Related Macular Degeneration (0.754) |
| [ ] | 1857 | 26.05.02.02 | ASPN-related Osteoarthritis susceptibility 3 (susceptibility to) | ASPN | 607850 | - | UNMAPPED; weak candidate Osteoarthritis (0.700) |
| [ ] | 1858 | 26.05.03.01 | BGN-related Meester–Loeys syndrome | BGN | 300989 | - | UNMAPPED; weak candidate Loeys-Dietz Syndrome (0.667) |
| [ ] | 1859 | 26.05.03.02 | BGN-related Spondyloepimetaphyseal dysplasia, XL | BGN | 300106 | - | UNMAPPED; weak candidate Spondyloepimetaphyseal Dysplasia Bieganski Type (0.805) |
| [ ] | 1860 | 26.05.04.01 | DCN-related Corneal dystrophy, congenital stromal | DCN | 610048 | - | UNMAPPED; weak candidate CACD1 (0.712) |
| [ ] | 1861 | 26.05.05.01 | HSPG2-related Dyssegmental dysplasia, Silverman-Handmaker type | HSPG2 | 224410 | - | UNMAPPED; weak candidate KRT85-Related Pure Hair-Nail Ectodermal Dysplasia (0.619) |
| [ ] | 1862 | 26.05.05.02 | HSPG2-related Schwartz–Jampel syndrome, type 1 | HSPG2 | 255800 | - | UNMAPPED; weak candidate Temtamy Syndrome (0.504) |
| [ ] | 1863 | 26.05.06.01 | IMPG1-related Macular dystrophy, vitelliform, 4 | IMPG1 | 616151 | - | UNMAPPED; weak candidate IMPG1-related (0.695) |
| [ ] | 1864 | 26.05.06.02 | IMPG1-related Retinitis pigmentosa 91 | IMPG1 | 153870 | - | UNMAPPED; weak candidate IMPG1-related (0.595) |
| [ ] | 1865 | 26.05.07.01 | IMPG2-related Macular dystrophy, vitelliform, 5 | IMPG2 | 616152 | - | UNMAPPED; weak candidate IMPG2-related (0.695) |
| [ ] | 1866 | 26.05.07.02 | IMPG2-related Retinitis pigmentosa 56 | IMPG2 | 613581 | - | UNMAPPED; weak candidate IMPG2-related (0.545) |
| [ ] | 1867 | 26.05.08.01 | KERA-related Cornea plana 2, autosomal recessive | KERA | 217300 | - | UNMAPPED; weak candidate OSMED (0.746) |
| [ ] | 1868 | 26.05.09.01 | NYX-related Night blindness, congenital stationary (complete), type 1A | NYX | 310500 | - | UNMAPPED; weak candidate CSNBAD1 (0.500) |
| [ ] | 1869 | 26.05.10.01 | PRG4-related Camptodactyly-arthropathy-coxa vara-pericarditis syndrome | PRG4 | 208250 | - | UNMAPPED; weak candidate Camptodactyly (0.469) |
| [ ] | 1870 | 26.05.11.01 | VCAN-related Wagner vitreoretinopathy | VCAN | 143200 | - | UNMAPPED; weak candidate Familial Exudative Vitreoretinopathy (0.846) |
| [ ] | 1800 | 26.06.05.01 | COL4A1-related Angiopathy, hereditary, with nephropathy, aneurysms, and muscle cramps | COL4A1 | 611773 | - | UNMAPPED; weak candidate Retinal Arterial Tortuosity (0.349) |
| [ ] | 1801 | 26.06.05.02 | COL4A1-related Brain small vessel disease with or without ocular anomalies | COL4A1 | 175780 | - | UNMAPPED; weak candidate Retinal Arterial Tortuosity (0.451) |
| [ ] | 1802 | 26.06.05.03 | COL4A1-related Microangiopathy and leukoencephalopathy, pontine, autosomal dominant | COL4A1 | 618564 | - | UNMAPPED |
| [ ] | 1803 | 26.06.06.01 | COL4A2-related Brain small vessel disease 2 | COL4A2 | 614483 | - | UNMAPPED; weak candidate Allergic Cutaneous Vasculitis (0.590) |
| [ ] | 1804 | 26.06.07.01 | COL4A3;COL4A4-related Alport syndrome 2, autosomal recessive | COL4A3;COL4A4 | 203780 | - | UNMAPPED; weak candidate Alport Syndrome (0.577) |
| [ ] | 1805 | 26.06.07.02 | COL4A3-related Alport syndrome 3, autosomal dominant | COL4A3 | 104200 | - | UNMAPPED; weak candidate Alport Syndrome (0.588) |
| [ ] | 1806 | 26.06.07.03 | COL4A3;COL4A4-related Hematuria, benign familial | COL4A3;COL4A4 | 141200 | - | UNMAPPED; weak candidate Anti-Glomerular Basement Membrane Disease (0.658) |
| [ ] | 1807 | 26.06.08.01 | COL4A5-related Alport syndrome 1, X-linked | COL4A5 | 301050 | - | UNMAPPED; weak candidate Alport Syndrome (0.732) |
| [ ] | 1809 | 26.06.09.01 | COL4A6-related Deafness, X-linked 6 | COL4A6 | 300914 | - | MAPPED -> DFNX6 (alias_exact:dfnx6) |
| [ ] | 1808 | 26.06.09.02 | COL4A5;COL4A6-related Leiomyomatosis, diffuse, with Alport syndrome | COL4A5;COL4A6 | 308940 | - | UNMAPPED; weak candidate Alport Syndrome (0.517) |
| [ ] | 1813 | 26.06.12.01 | COL6A1;COL6A2;COL6A3-related Bethlem myopathy 1 | COL6A1;COL6A2;COL6A3 | 158810 | - | UNMAPPED |
| [ ] | 1815 | 26.06.12.02 | COL6A1;COL6A2;COL6A3-related Ullrich congenital muscular dystrophy 1 | COL6A1;COL6A2;COL6A3 | 254090 | - | AMBIGUOUS: 2 local entities (identifier:OMIM:254090) |
| [ ] | 1816 | 26.06.13.01 | COL6A2-related Myosclerosis, congenital | COL6A2 | 255600 | - | UNMAPPED |
| [ ] | 1818 | 26.06.14.01 | COL6A3-related Dystonia 27 | COL6A3 | 616411 | - | UNMAPPED |
| [ ] | 1819 | 26.06.15.01 | COL7A1-related Epidermolysis bullosa dystrophica, autosomal recessive | COL7A1 | 226600 | - | UNMAPPED; weak candidate Dystrophic Epidermolysis Bullosa (0.767) |
| [ ] | 1820 | 26.06.15.02 | COL7A1-related Epidermolysis bullosa dystrophica, autosomal dominant | COL7A1 | 131750 | - | MAPPED -> DDEB (alias_exact:ddeb) |
| [ ] | 1821 | 26.06.15.03 | COL7A1-related Nail disorder, nonsyndromic congenital, 8 | COL7A1 | 607523 | - | UNMAPPED |
| [ ] | 1822 | 26.06.16.01 | COL8A2-related Fuchs endothelial corneal dystrophy 1 | COL8A2 | 136800 | - | MAPPED -> Fuchs Endothelial Corneal Dystrophy (identifier:OMIM:136800) |
| [ ] | 1824 | 26.06.17.01 | COL9A1-related Stickler syndrome, type IV | COL9A1 | 614134 | - | UNMAPPED |
| [ ] | 1825 | 26.06.17.02 | COL9A1-related Epiphyseal dysplasia, multiple, 6 | COL9A1 | 614135 | - | MAPPED -> EDM6 (alias_exact:edm6) |
| [ ] | 1827 | 26.06.18.01 | COL9A2-related Stickler syndrome, type V | COL9A2 | 614284 | - | UNMAPPED |
| [ ] | 1828 | 26.06.18.02 | COL9A2-related Epiphyseal dysplasia, multiple, 2 | COL9A2 | 600204 | - | MAPPED -> EDM2 (alias_exact:edm2) |
| [ ] | 1830 | 26.06.19.01 | COL9A3-related Epiphyseal dysplasia, multiple, 3 | COL9A3 | 600969 | - | MAPPED -> EDM3 (alias_exact:edm3) |
| [ ] | 1831 | 26.06.20.01 | COL10A1-related Metaphyseal chondrodysplasia, Schmid type | COL10A1 | 156500 | - | MAPPED -> Metaphyseal Chondrodysplasia, Schmid Type (alias_exact:metaphyseal chondrodysplasia schmid type) |
| [ ] | 1845 | 26.06.23.01 | COL12A1-related Ullrich congenital muscular dystrophy 2 | COL12A1 | 616470 | - | AMBIGUOUS: 2 local entities (identifier:OMIM:616470) |
| [ ] | 1846 | 26.06.23.02 | COL12A1-related Bethlem myopathy 2 | COL12A1 | 616471 | - | UNMAPPED |
| [ ] | 1847 | 26.06.24.01 | COL13A1-related Myasthenic syndrome, congenital, 19 | COL13A1 | 616720 | - | UNMAPPED; weak candidate Congenital Myasthenic Syndrome (0.603) |
| [ ] | 1848 | 26.06.25.01 | COL18A1-related Knobloch syndrome 1 | COL18A1 | 267750 | - | UNMAPPED; weak candidate Stage 5 (0.439) |
| [ ] | 1849 | 26.06.26.01 | COL17A1-related Epidermolysis bullosa, junctional 4, non-Herlitz type | COL17A1 | 619787 | - | UNMAPPED; weak candidate Epidermolysis Bullosa (0.618) |
| [ ] | 1850 | 26.06.26.02 | COL17A1-related Epithelial recurrent erosion dystrophy | COL17A1 | 122400 | - | UNMAPPED |

### WP-099: Other disorders of connective tissue

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Other disorders of connective tissue
- Records: 28 (MAPPED 6, AMBIGUOUS 0, CANDIDATE 1, UNMAPPED 21)
- Work: curate missing DisMech pages for UNMAPPED rows; review fuzzy candidates and decide whether to merge, subtype, or curate separately; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2076 | 26.4.16.01 | BMP2-related skeletal dysplasia | BMP2 | 617877 | - | UNMAPPED; weak candidate Amniotic Band Syndrome (0.778) |
| [ ] | 1980 | 26.07.01.01 | ACTA2-related Aortic aneurysm, familial thoracic 6 | ACTA2 | 611788 | - | MAPPED -> ACTA2-related (alias_exact:aortic aneurysm familial thoracic 6) |
| [ ] | 1981 | 26.07.01.02 | ACTA2-related Moyamoya disease 5 | ACTA2 | 614042 | - | UNMAPPED; weak candidate Multisystemic smooth muscle dysfunction syndrome (0.489) |
| [ ] | 1982 | 26.07.01.03 | ACTA2-related Multisystemic smooth muscle dysfunction syndrome | ACTA2 | 613834 | - | MAPPED -> Multisystemic smooth muscle dysfunction syndrome (alias_exact:acta2 related multisystemic smooth muscle dysfunction syndrome) |
| [ ] | 1983 | 26.07.02.01 | ADAMTS10-related Weill-Marchesani Syndrome | ADAMTS10 | 277600 | - | UNMAPPED; weak candidate Autosomal Recessive Multiple Pterygium Syndrome (0.696) |
| [ ] | 1985 | 26.07.04.01 | ADAMTSL4-related Ectopia lentis et pupillae | ADAMTSL4 | 225200 | - | UNMAPPED; weak candidate Jeavons Syndrome (0.515) |
| [ ] | 1986 | 26.07.04.02 | ADAMTSL4-related Ectopia lentis, isolated, autosomal recessive | ADAMTSL4 | 225100 | - | UNMAPPED; weak candidate OSMED (0.706) |
| [ ] | 1987 | 26.07.05.01 | FGFR3-related CATSHL Syndrome | FGFR3 | 610474 | - | UNMAPPED |
| [ ] | 1988 | 26.07.06.01 | FMR1-related Fragile-X Syndrome | FMR1 | 300624 | - | MAPPED -> Fragile X Syndrome (alias_exact:fragile x syndrome) |
| [ ] | 1989 | 26.07.07.01 | MED12-related Lujan-Fryns syndrome | MED12 | 309520 | - | UNMAPPED; weak candidate MED12 (0.700) |
| [ ] | 1990 | 26.07.07.02 | MED12-related Ohdo syndrome, X-linked | MED12 | 300895 | - | UNMAPPED; weak candidate MED12 (0.585) |
| [ ] | 1991 | 26.07.07.03 | MED12-related Opitz-Kaveggia syndrome | MED12 | 305450 | - | UNMAPPED; weak candidate MED12 (0.602) |
| [ ] | 1992 | 26.07.08.01 | NOTCH1-related Aortic valve disease 1 | NOTCH1 | 109730 | - | UNMAPPED |
| [ ] | 1993 | 26.07.08.02 | NOTCH1-related Adams-Oliver syndrome 5 | NOTCH1 | 616028 | - | MAPPED -> AOS5 (alias_exact:aos5) |
| [ ] | 1994 | 26.07.09.01 | MYH11-related Aortic aneurysm, familial thoracic 4 | MYH11 | 132900 | - | MAPPED -> MYH11-related (alias_exact:aortic aneurysm familial thoracic 4) |
| [ ] | 1995 | 26.07.09.02 | MYH11-related Megacystis-microcolon-intestinal hypoperistalsis syndrome 2 | MYH11 | 619351 | - | UNMAPPED |
| [ ] | 1996 | 26.07.09.03 | MYH11-related Visceral myopathy 2 | MYH11 | 619350 | - | UNMAPPED |
| [ ] | 1998 | 26.07.11.01 | PLOD3-related Procollagen-lysine, 2-oxoglutarate 5-dioxygenase 3 deficiency | PLOD3 | 612394 | - | UNMAPPED; weak candidate Alkaptonuria (0.660) |
| [ ] | 2000 | 26.07.12.01 | TGFB1-related Camurati-Engelmann Disease | TGFB1 | 131300 | - | MAPPED -> Camurati-Engelmann Disease (alias_exact:camurati engelmann disease) |
| [ ] | 1999 | 26.07.12.02 | TGFB1-related Inflammatory bowel disease, immunodeficiency, and encephalopathy | TGFB1 | 618213 | - | UNMAPPED |
| [ ] | 2003 | 26.07.15.01 | UPF3B-related Intellectual developmental disorder, X-linked, syndromic 14 | UPF3B | 300676 | - | UNMAPPED; weak candidate MED13 Syndrome (0.779) |
| [ ] | 1969 | 26.07.17.01 | TNXB-related Ehlers-Danlos syndrome, classic-like, 1 | TNXB | 606408 | - | UNMAPPED; weak candidate Classical EDS (0.889) |
| [ ] | 1970 | 26.07.17.02 | TNXB-related Vesicoureteral reflux 8 | TNXB | 615963 | - | UNMAPPED; weak candidate Gastroesophageal Reflux Disease (0.519) |
| [ ] | 2150 | 26.07.18.01 | AEBP1-related Ehlers-Danlos Syndrome, Classical-like | AEBP1 | 618000 | - | UNMAPPED; weak candidate Classical EDS (0.889) |
| [ ] | 2151 | 26.07.19.01 | C1R;C1S-related Ehlers-Danlos Syndrome, Periodontal | C1R;C1S | 130080;617174 | - | UNMAPPED; weak candidate Hypermobile Ehlers-Danlos Syndrome (0.794) |
| [ ] | 2153 | 26.07.20.01 | ZNF469;PRDM5-related Brittle Cornea Syndrome | ZNF469;PRDM5 | 229200;614170 | - | UNMAPPED |
| [ ] | 2225 | 26.7.21.01 | NOTCH2-related Alagille syndrome 2 | NOTCH2 | 610205 | - | CANDIDATE -> Alagille syndrome (0.944) |
| [ ] | 2226 | 26.7.21.02 | NOTCH2-related Hajdu-Cheney syndrome | NOTCH2 | 102500 | - | UNMAPPED |

### WP-100: Disorders of proteins in TGF-g signaling pathway

- Classification: Unclassified -> Disorders of the extracellular matrix (under construction)
- Subgroup scope: Disorders of proteins in TGF-g signaling pathway
- Records: 15 (MAPPED 9, AMBIGUOUS 0, CANDIDATE 0, UNMAPPED 6)
- Work: curate missing DisMech pages for UNMAPPED rows; verify mapped rows only when they share mechanism or aliases with new work.

| Done | IEMbase ID | Nosology | Disease | Gene | OMIM | ORPHA | Current DisMech status |
|---|---:|---|---|---|---|---|---|
| [ ] | 2002 | 26.08.1.01 | TGFBR1-related Loeys-Dietz syndrome, type 1 | TGFBR1 | 609192 | - | MAPPED -> Loeys-Dietz Syndrome Type 1 (alias_exact:loeys dietz syndrome type 1) |
| [ ] | 2001 | 26.08.2.01 | TGFBR2-related Loeys-Dietz syndrome, type 2 | TGFBR2 | 610168 | - | MAPPED -> Loeys-Dietz Syndrome Type 2 (alias_exact:loeys dietz syndrome type 2) |
| [ ] | 2193 | 26.08.3.01 | SMAD3-related Loeys–Dietz Syndrome | SMAD3 | 613795 | - | MAPPED -> Loeys-Dietz Syndrome (alias_exact:loeys dietz syndrome) |
| [ ] | 1968 | 26.08.4.01 | TGFBI-related Corneal dystrophy, Thiel-Behnke type | TGFBI | 602082 | - | UNMAPPED; weak candidate TGFBI Corneal Dystrophies (0.649) |
| [ ] | 1967 | 26.08.5.01 | TGFBI-related Corneal dystrophy, Reis-Bucklers type | TGFBI | 608470 | - | UNMAPPED; weak candidate TGFBI Corneal Dystrophies (0.642) |
| [ ] | 1966 | 26.08.6.01 | TGFBI-related Corneal dystrophy, lattice type IIIA | TGFBI | 608471 | - | UNMAPPED; weak candidate TGFBI Corneal Dystrophies (0.690) |
| [ ] | 1965 | 26.08.7.01 | TGFBI-related Corneal dystrophy, lattice type I | TGFBI | 122200 | - | MAPPED -> LCD1 (alias_exact:lattice corneal dystrophy type 1) |
| [ ] | 1964 | 26.08.8.01 | TGFBI-related Corneal dystrophy, Groenouw type I | TGFBI | 121900 | - | MAPPED -> GCD1 (alias_exact:granular corneal dystrophy type 1) |
| [ ] | 1963 | 26.08.9.01 | TGFBI-related Corneal dystrophy, epithelial basement membrane | TGFBI | 121820 | - | UNMAPPED; weak candidate TGFBI Corneal Dystrophies (0.750) |
| [ ] | 1962 | 26.08.10.01 | TGFBI-related Corneal dystrophy, Avellino type | TGFBI | 607541 | - | MAPPED -> Congenital Dyserythropoietic Anemia (alias_exact:cda) |
| [ ] | 2194 | 26.8.11.01 | TGFB2-related Loeys–Dietz Syndrome | TGFB2 | 614816 | - | MAPPED -> Loeys-Dietz Syndrome (alias_exact:loeys dietz syndrome) |
| [ ] | 2195 | 26.8.12.01 | TGFB3-related Loeys–Dietz Syndrome | TGFB3 | 615582 | - | MAPPED -> Loeys-Dietz Syndrome (alias_exact:loeys dietz syndrome) |
| [ ] | 2196 | 26.8.13.01 | SMAD2-related Loeys–Dietz Syndrome | SMAD2 | 619656 | - | MAPPED -> Loeys-Dietz Syndrome (alias_exact:loeys dietz syndrome) |
| [ ] | 2197 | 26.8.14.01 | SMAD4-related Myhre Syndrome (gain of function) | SMAD4 | 139210 | - | UNMAPPED; weak candidate Myhre Syndrome (0.667) |
| [ ] | 2198 | 26.8.15.01 | SMAD4-related Juvenile Polyposis Syndrome – HHT overlap (loss of function) | SMAD4 | 175050 | - | UNMAPPED; weak candidate SMAD4-associated juvenile polyposis/HHT overlap (0.820) |
