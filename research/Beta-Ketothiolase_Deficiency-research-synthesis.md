# Beta-Ketothiolase Deficiency Research Synthesis

## Provider Coverage

- Falcon: `Beta-Ketothiolase_Deficiency-deep-research-falcon.md`
- OpenScientist: `Beta-Ketothiolase_Deficiency-deep-research-openscientist.md`

## Agreement

Both providers describe beta-ketothiolase deficiency as an autosomal recessive ACAT1 disorder affecting mitochondrial acetoacetyl-CoA thiolase. They agree that the enzyme participates in isoleucine catabolism and ketone body metabolism, and that deficiency causes accumulation of isoleucine-derived organic acids with episodic ketoacidosis under catabolic stress.

The reports converge on the major clinical pattern: infancy or early-childhood onset, recurrent metabolic crises triggered by infection or fasting, vomiting/lethargy/hypotonia/seizures/coma during crises, characteristic urine organic acids and acylcarnitines, generally favorable prognosis with management, and possible neurologic sequelae including extrapyramidal signs or basal ganglia lesions.

## Differences

Falcon focused narrowly on the pathophysiology template: ACAT1/T2 enzyme deficiency, blocked isoleucine catabolism, impaired ketone handling, and crisis phenotypes. OpenScientist provided broader disease-characterization content: newborn screening caveats, ACAT1 variant spectrum, genotype-phenotype uncertainty, C5:1/C5-OH biomarkers, management strategy, and model-system limitations.

## YAML Integration

Integrated into `kb/disorders/Beta-Ketothiolase_Deficiency.yaml`:

- Confirmed that the core ACAT1 molecular defect, impaired isoleucine catabolism, impaired ketone body metabolism, and episodic decompensation cascade were already represented.
- Confirmed phenotype coverage for ketoacidosis, metabolic acidosis, lethargy, vomiting, hypotonia, seizures, coma, basal ganglia lesions, and extrapyramidal signs.
- Confirmed biochemical marker coverage for 2M3HB, tiglylglycine, 2MAA, C5:1, and C5-OH.
- Confirmed treatment coverage for catabolic-trigger avoidance, dietary management, acute dextrose, carnitine, newborn screening, and genetic counseling.
- Backfilled top-level references with `found_in` provenance for Falcon and OpenScientist citations.

## Not Integrated

Detailed variant-by-variant ACAT1 structural interpretation, adult diabetic ketoacidosis edge cases, and broad model-system proposals were left in the research reports rather than expanded into YAML, because the existing entry already captures the clinically actionable mechanism and management model.
