# Alpha-mannosidosis Deep Research Fallback

## Provider Attempts

- Falcon: `just research-disorder falcon Alpha_Mannosidosis` started at this worktree and produced no output for several minutes; the provider process was terminated to avoid a silent deep-research wait.
- OpenAI: `just research-disorder openai Alpha_Mannosidosis` was attempted after Falcon and also produced no output during two bounded wait intervals; the provider process was terminated.

## Evidence Scope

The YAML curation integrates deterministic Orphanet structured records and fetched PubMed abstracts:

- ORPHA:61 provides the direct disease mapping to MONDO:0009561, OMIM:248500, the definition, autosomal recessive inheritance, natural-history onset terms, prevalence rows, and the complete disease-level HPO phenotype table.
- ORPHA:309282 and ORPHA:309288 provide infantile and adult subtype mappings to MONDO:0017732 and MONDO:0017733 plus MAN2B1 disease-causing gene rows.
- PMID:18651971 supports the clinical definition, progressive course, MAN2B1/lysosomal alpha-mannosidase disease mechanism, enzyme and urinary-oligosaccharide diagnostic approach, supportive care, and genetic counseling.
- PMID:26048034 supports the MAN2B1 genotype relationship, loss of lysosomal alpha-mannosidase activity, CSF oligosaccharide burden, and neurodevelopmental/motor/craniofacial phenotype links.
- PMID:15126988 supports allogeneic hematopoietic stem cell transplantation as a disease-modifying treatment that normalizes leukocyte enzyme activity and can stabilize progressive cognitive loss.
- PMID:29846843, PMID:36849760, and PMID:39381850 support velmanase alfa enzyme replacement therapy, including recombinant enzyme identity, clinical trial use, serum oligosaccharide clearance, immunologic effects, and long-term benefit.
- PMID:40276561 supports the contemporary cohort framing of alpha-mannosidosis as an ultrarare multisystemic disorder caused by alpha-mannosidase deficiency.

## Integration Notes

The curated YAML represents the canonical mechanism as MAN2B1-related lysosomal alpha-mannosidase deficiency leading to mannose-rich oligosaccharide lysosomal storage, with downstream neurodevelopmental, immune/infectious, skeletal, craniofacial, auditory, ocular, and visceral phenotypes. All ORPHA:61 disease-level phenotypes are included with exact Orphanet snippets and frequency bands. Frequent and very frequent phenotype rows from the ORPHA:309282 infantile and ORPHA:309288 adult subtype records are included as subtype-specific phenotype assertions. Treatment sections are limited to evidence-backed velmanase alfa enzyme replacement, hematopoietic stem cell transplantation, supportive care, and genetic counseling.
