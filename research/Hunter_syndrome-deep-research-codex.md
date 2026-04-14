# Hunter syndrome manual research note

Date: 2026-04-14

## Scope

Manual curation note for a demo-ready disease-level dismech entry for Hunter syndrome
(mucopolysaccharidosis type 2, MPS II), with emphasis on a fully connected
mechanism graph, exact PMID-backed quotes, honest evidence-source tagging, and
conservative treatment claims.

## Naming and grounding checks

- Monarch / MONDO check:
  - `MONDO:0010674` resolves to primary label `mucopolysaccharidosis type 2`.
  - Monarch exact synonyms include `Hunter syndrome`, `Hunter's syndrome`,
    `MPS II`, and `iduronate 2-sulfatase deficiency`.
  - Curation choice: file name and display name use the familiar clinical name
    `Hunter syndrome`, while `disease_term.term.label` stays exactly on the
    MONDO primary label `mucopolysaccharidosis type 2`.

- ClinGen check:
  - ClinGen gene validity entry for `IDS` maps to
    `mucopolysaccharidosis type 2` / `MONDO:0010674`.
  - Local cache row:
    `"IDS","HGNC:5389","mucopolysaccharidosis type 2","MONDO:0010674","XL","SOP5","Definitive",...`
  - Direct ClinGen page grep confirms the key fields:
    `IDS`, `mucopolysaccharidosis type 2`, `MONDO:0010674`, `X-linked`,
    `Definitive`.
  - Curation choice: frame the proximal lesion explicitly as `IDS`
    / iduronate-2-sulfatase deficiency and keep the inheritance claim strictly
    X-linked recessive.

## Curation decisions

- Included one disease-modifying treatment entry:
  `Idursulfase enzyme replacement therapy`.
  Reason: standard of care with direct human clinical trial evidence.
  Structured therapeutic agent term verified locally against the repo OAK NCIT
  adapter as `NCIT:C65883` / `Idursulfase`.

- Included one downstream management entry:
  `Multidisciplinary supportive care`.
  Reason: conservative, clinically coherent, and supported by Hunter Outcome
  Survey adult-burden data.

- Did **not** include hematopoietic stem cell transplantation as a standard
  treatment entry.
  Reason: available abstract-level evidence is limited, mixed, and not strong
  enough for a clean conservative standard-of-care statement in Hunter syndrome.

- Did **not** use `dysostosis multiplex` as a Hunter-specific phenotype entry.
  Reason: the selected Hunter-specific abstract set gave strong support for
  short stature, joint stiffness, and connective-tissue/joint disease, but not
  a clean exact Hunter-specific abstract quote explicitly naming dysostosis
  multiplex.

## Mechanism graph used in YAML

1. `Iduronate-2-sulfatase deficiency`
2. `Heparan sulfate and dermatan sulfate lysosomal accumulation`
3. `Lysosomal dysfunction`
4. `Secondary neuronal injury`
5. `Neuronopathic central nervous system dysfunction`
6. `Connective tissue and skeletal-muscle dysfunction`
7. `Airway soft-tissue disease`
8. `Cardiac valvular thickening and dysfunction`

Graph logic:

- `IDS` deficiency directly causes `heparan sulfate and dermatan sulfate`
  storage.
- Storage burden progresses into broader `lysosomal dysfunction`.
- `Lysosomal dysfunction` feeds a separate `secondary neuronal injury` node
  before overt neuronopathic CNS dysfunction, while also branching into the
  major non-CNS tissue-level outcomes needed for a clinically coherent Hunter
  syndrome graph: connective tissue / skeletal disease, airway disease, and
  valve disease.
- `Idursulfase` targets the proximal enzyme deficiency and the substrate-storage
  node.
- `Supportive care` targets downstream phenotype burden rather than upstream
  biochemistry.

## Selected exact-quote evidence set

### Core disease framing

- PMID:25345092
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Hunter syndrome is caused by deficiency of the lysososmal enzyme iduronate-2-sulphatase that cleaves O-linked sulphate moieties from dermatan sulphate and heparan sulphate and leads to accumulation of GAGs.`
  - Use: proximal enzyme defect and substrate specificity.

- PMID:25345092
  - Source type: `HUMAN_CLINICAL`
  - Quote: `The disease is a X-linked condition affecting males and rarely females, clinically divided into severe (2/3) and attenuated types.`
  - Use: inheritance and severe/attenuated framing.

- PMID:21518713
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Mucopolysaccharidosis type II (MPS II) is a lysosomal storage disorder characterized by insufficiency of the iduronate-2-sulfatase enzyme, which results in excess heparan and dermatan sulfates within the lysosomes of various tissues and organs, including the central nervous system.`
  - Use: storage node.

### Lysosomal dysfunction and CNS disease

- PMID:24201805
  - Source type: `IN_VITRO`
  - Quote: `Experiments here reported show that NSCs derived from the subventricular zone (SVZ) of early symptomatic IDS-knockout (IDS-ko) mouse retained self-renewal capacity in vitro, but differentiated earlier than wild-type (wt) cells, displaying an evident lysosomal aggregation in oligodendroglial and astroglial cells.`
  - Use: secondary lysosomal dysfunction in glial lineages.

- PMID:32707880
  - Source type: `HUMAN_CLINICAL`
  - Quote: `In addition to the accumulation of CSF GAGs, nMPS II patients show elevated levels of lysosomal lipids, neurofilament light chain, and other biomarkers of neuronal damage and degeneration.`
  - Use: human evidence for downstream lysosome dysfunction and neuronal injury.

- PMID:21518713
  - Source type: `HUMAN_CLINICAL`
  - Quote: `One subset of patients had normal cognitive, speech and language, and adaptive functions whereas the other showed a dramatic decline in these areas.`
  - Use: neuronopathic CNS decline.

- PMID:19597960
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Patients with the severe form of the disease have cognitive impairment and typically die in the second decade of life.`
  - Use: severe-form cognitive impairment phenotype and clinical severity.

### Connective tissue, airway, and cardiac tissue-level dysfunction

- PMID:20354449
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Lysosomal accumulation of these GAG molecules results in cell, tissue, and organ dysfunction. The skeletal-muscle system involvement is because of essential accumulated GAGs in joints and connective tissue.`
  - Use: connective-tissue / skeletal-muscle node.

- PMID:38085235
  - Source type: `MODEL_ORGANISM`
  - Quote: `In contrast, tracheal, epiphyseal, and articular cartilage remained largely uncorrected by all vectors tested.`
  - Use: cartilage as a resistant downstream tissue compartment.

- PMID:25345092
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Recurrent and prolonged rhinitis with persistent nasal discharge are the first symptoms of airway disease that manifests itself as noisy breathing and later sleep apnea.`
  - Use: airway soft-tissue disease and sleep apnea phenotype.

- PMID:39440439
  - Source type: `HUMAN_CLINICAL`
  - Quote: `DS is a major component of the extracellular matrix of heart valves, which can be affected in MPS II.`
  - Use: cardiac valve mechanism node.

- PMID:25345092
  - Source type: `HUMAN_CLINICAL`
  - Quote: `valvular involvement, with progressive thickening and stiffening of the valve leaflets leading to mitral and aortic regurgitation and stenosis .`
  - Use: valvular phenotype.

### Phenotype support chosen for YAML

- PMID:25345092 supports:
  - coarse facial features
  - short stature
  - joint stiffness
  - hearing impairment
  - sleep apnea
  - hepatosplenomegaly
  - cardiac valve disease

- PMID:19597960 and PMID:21518713 support:
  - cognitive impairment / neuronopathic severe disease

### Treatment support chosen for YAML

- PMID:17185020
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Urinary glycosaminoglycans were reduced within 2 weeks of initiating idursulfase and were decreased 49% after 48 weeks of treatment (P<0.0001). Both liver and spleen volume were decreased at 24 weeks (P<0.01) and 48 weeks (P<0.001). The 6-minute walk test distance increased an average of 48 meters after 48 weeks (P=0.013).`
  - Use: direct human efficacy of idursulfase on somatic burden.

- PMID:25231261
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Although the present protocol of idursulfase administration may result efficacious in delaying the MPS II somatic disease progression at some extent, in this study we observed that several signs and symptoms did not improve during the therapy.`
  - Use: conservative limitation on idursulfase claims.

- PMID:25345092
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Current research is focused on pharmacological chaperones, gene therapy and substrate reduction therapy and therapies that, unlike Idursulfase, do cross the blood-brain barrier.`
  - Use: conservative statement that standard idursulfase does not address CNS disease.

- PMID:40598289
  - Source type: `HUMAN_CLINICAL`
  - Quote: `Overall, adult patients with neuronopathic and non-neuronopathic MPS II had a high disease burden and requirement for surgeries, emphasizing the need to continue multidisciplinary management and regular assessments in adulthood.`
  - Use: justify supportive multidisciplinary care without overstating disease modification.
