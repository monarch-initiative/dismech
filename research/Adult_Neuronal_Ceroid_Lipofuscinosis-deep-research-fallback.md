# Adult Neuronal Ceroid Lipofuscinosis Deep Research Fallback

Date: 2026-05-13

## Provider Attempts

- `falcon`: `just research-disorder falcon Adult_Neuronal_Ceroid_Lipofuscinosis`
  started and remained silent past the agent timeout window; terminated without
  producing a usable artifact.
- `openai`: `just research-disorder openai Adult_Neuronal_Ceroid_Lipofuscinosis`
  started and remained silent past the agent timeout window; terminated without
  producing a usable artifact.

Because no deep research provider returned a usable report, curation proceeded
from MONDO:0019260, a bounded set of cached primary literature, and the
existing group-level Neuronal Ceroid Lipofuscinosis research artifact.

## Integrated Literature Synthesis

Adult neuronal ceroid lipofuscinosis (Kufs disease) is a rare adult-onset
form of the NCL group of lysosomal storage neurodegenerative diseases.
Disease typically begins in the third or fourth decade and is clinically
divided into Type A (Kufs-A), a progressive myoclonus epilepsy with dementia,
ataxia, and pyramidal or extrapyramidal motor signs, and Type B (Kufs-B),
dominated by dementia with motor system dysfunction (cerebellar ataxia or
extrapyramidal signs) generally without prominent myoclonic epilepsy. In
contrast to the childhood NCL subtypes, retinopathy and visual loss are
characteristically absent.

Adult NCL is genetically heterogeneous. Arsov and colleagues established
that recessive pathogenic variants in CLN6 are the most common recessive
cause of Kufs disease, particularly the Type A progressive myoclonus
epilepsy phenotype, and provided systematic clinicopathologic and
ultrastructural characterization showing fingerprint and granular
lipopigment inclusions in CLN6-related cases (PMID:21549341). Subsequent
exome work by Smith and colleagues identified homozygous and compound
heterozygous CTSF mutations encoding cathepsin F as the major recessive
cause of Kufs Type B (designated CLN13), implicating impaired lysosomal
cysteine protease activity in the adult-onset disease group (PMID:23297359).
The autosomal dominant adult-onset form CLN4 is caused by heterozygous
mutations in DNAJC5 encoding cysteine-string protein alpha (CSPalpha), as
established by Noskova and colleagues using linkage and exome sequencing in
multiple unrelated families with autosomal dominant adult NCL
(PMID:21820099).

Mechanistically, the three molecular etiologies converge on lysosomal and
synaptic dysfunction. CLN6 encodes an ER-resident transmembrane protein
required for normal lysosomal proteolytic homeostasis; loss of function
leads to neuronal accumulation of autofluorescent ceroid lipopigment with
fingerprint and granular ultrastructure. CTSF encodes the lysosomal
cysteine protease cathepsin F; recessive loss-of-function impairs
intralysosomal protein catabolism and drives lipopigment storage in
neurons. Reviews emphasize that across NCL subtypes, including adult-onset
forms, lysosomal storage and progressive neuronal loss are the core
pathophysiologic features (PMID:30561534). DNAJC5/CSPalpha is a
synaptic-vesicle-associated co-chaperone whose dominant pathogenic variants
disrupt synaptic protein folding/quality control and SNARE-complex
assembly, producing presynaptic dysfunction in addition to lipopigment
storage; more recent work continues to characterize CLN4/DNAJC5 as a
distinct dominant adult-onset NCL with predominant dementia and
extrapyramidal features and to highlight palmitoylation/SNARE-related
biology in disease pathogenesis (PMID:39470529).

No curative therapy currently exists for adult NCL. Management is
supportive and primarily targets the clinical phenotype, including
antiseizure pharmacotherapy for myoclonic and other seizures in Kufs-A.
Genetic counseling is informed by the distinct recessive (CLN6, CTSF) and
dominant (DNAJC5) inheritance patterns.

## Key References

- PMID:21549341 - Arsov et al. Kufs disease, the major adult form of
  neuronal ceroid lipofuscinosis, caused by mutations in CLN6.
- PMID:21820099 - Noskova et al. Mutations in DNAJC5, encoding
  cysteine-string protein alpha, cause autosomal-dominant adult-onset
  neuronal ceroid lipofuscinosis (CLN4).
- PMID:23297359 - Smith et al. Cathepsin F mutations cause Type B Kufs
  disease, an adult-onset neuronal ceroid lipofuscinosis.
- PMID:30561534 - Review of neuronal ceroid lipofuscinoses summarizing
  lysosomal storage and progressive neurodegeneration across NCL subtypes,
  including adult-onset forms.
- PMID:39470529 - Recent work on CLN4/DNAJC5-related adult NCL and
  CSPalpha synaptic biology in disease pathogenesis.

## Notes on Scope

This fallback artifact is specific to adult-onset NCL (Kufs disease,
MONDO:0019260) and complements the broader
`Neuronal_Ceroid_Lipofuscinosis-deep-research-asta.md` group-level artifact.
Curation focused on the three adult-onset genetic etiologies (CLN6, CTSF,
DNAJC5/CLN4), the Type A vs Type B clinical distinction, and the absence
of retinopathy that distinguishes adult NCL from childhood NCL subtypes.
