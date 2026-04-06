# Epilepsy Mechanism Landscape

This note summarizes the main mechanistic lanes that appear repeatedly across
epilepsy disorders and explains how they should probably be represented in
dismech. The key modeling principle is that these lanes are often overlapping,
but they are not interchangeable.

## High-Level Map

| Mechanism lane | Representative disorders | Evidence signal | Modeling implication |
| --- | --- | --- | --- |
| Channelopathy / interneuron dysfunction | Dravet syndrome, KCNQ2-related DEE, SCN2A-related DEE, KCNT1-related DEE | Strong | Usually merits gene- or syndrome-level entries because treatment logic and cell-type vulnerability differ by channel and direction of effect. |
| Synaptic dysfunction | STXBP1 encephalopathy, SYNGAP1 encephalopathy, DNM1-related DEE | Strong | Keep separate from channelopathies; these are vesicle-release, receptor-complex, or synaptic-plasticity disorders rather than primarily ion-channel disorders. |
| mTOR / cortical malformation | TSC-associated epilepsy, DEPDC5-related focal epilepsy, focal cortical dysplasia | Strong | One of the clearest mechanistic families in epilepsy; should likely become a major dismech lane. |
| Neuroinflammation / immune / BBB | Drug-resistant focal epilepsy, autoimmune encephalitides, post-injury epilepsies | Moderate to strong, but heterogeneous | Often best modeled as either a focal epilepsy family or a reusable module rather than a universal explanation for all epilepsies. |
| Metabolic / mitochondrial | GLUT1 deficiency, lipoic-acid pathway defects, copper transport disorders | Strong for selected disorders | Worth explicit coverage because the mechanism directly changes treatment choices, especially ketogenic or metabolic therapy. |
| Transcriptional / developmental | CDKL5 disorder, CHD2-related epilepsy, PPP3CA-related DEE, RORB/NEXMIF-associated generalized epilepsies | Moderate to strong | Useful for DEE and generalized epilepsy families where altered neuronal differentiation or chromatin regulation is upstream of seizures. |
| Network excitability / homeostasis | TLE, Jeavons/EEM, many DEEs | Strong as a final common pathway | Important as a circuit-level layer, but not sufficient by itself to define disorder boundaries. |

## 1. Channelopathy and Interneuron Failure

This is the cleanest mechanistic story in the current KB. In Dravet syndrome,
loss of SCN1A function preferentially compromises inhibitory interneuron sodium
currents and firing, creating an excitation-inhibition imbalance that promotes
seizures. That is more specific than a generic "hyperexcitability" story: the
mechanistic lesion sits at a defined ion channel, in a defined cell class, with
direct precision-treatment implications.

The broader implication is that not all channelopathy epilepsies should be
lumped. KCNQ2-, SCN2A-, KCNT1-, and KCNB1-related epilepsies all involve altered
membrane excitability, but they differ in developmental timing, cell-type
expression, gain- versus loss-of-function logic, and sometimes in drug response.
For dismech, that argues for gene- or syndrome-level entries linked by a common
"channelopathy" framing rather than one monolithic page.

Primary literature anchors:

- [PMID:21463282](../../references_cache/PMID_21463282.md): SCN1A loss impairs
  GABAergic interneuron firing in Dravet models and supports an
  excitation-inhibition imbalance mechanism.
- [PMID:17675531](../../references_cache/PMID_17675531.md): KCNQ2 deletions and
  duplications causing benign familial neonatal seizures, supporting the broader
  point that discrete ion-channel lesions can define distinct epilepsy families.

## 2. Synaptic Dysfunction

A second strong lane is epilepsy caused by defects in synaptic vesicle release,
postsynaptic signaling complexes, or synaptic plasticity programs. STXBP1
encephalopathy is a core example: the syndrome is not best understood as a
classical channelopathy, but as a disorder of neurotransmitter release and
neurodevelopment. SYNGAP1-related epilepsy similarly points to dysfunctional
postsynaptic signaling and impaired synaptic homeostasis, often with generalized
DEE phenotypes and visually triggered or reflex seizure features.

This family matters because it explains why some generalized or DEE syndromes
cluster around cognitive impairment, reflex sensitivity, and mixed seizure
types, even when MRI is normal. In dismech terms, these disorders should carry
explicit synaptic mechanism nodes rather than being explained only at the level
of seizures or EEG pattern.

Primary literature anchors:

- [PMID:26865513](../../references_cache/PMID_26865513.md): large STXBP1
  encephalopathy cohort showing epilepsy as part of a broader
  neurodevelopmental-synaptic disorder.
- [PMID:30541864](../../references_cache/PMID_30541864.md): SYNGAP1
  encephalopathy as a distinctive generalized developmental and epileptic
  encephalopathy.
- [PMID:30685520](../../references_cache/PMID_30685520.md): SYNGAP1 mutations
  linked to reflex seizures and eye-closure sensitivity, connecting synaptic
  dysfunction to specific electroclinical phenotypes.

## 3. mTOR Pathway Hyperactivation and Cortical Malformation

The mTOR lane is one of the most actionable epilepsy mechanisms in the current
literature. DEPDC5 loss, TSC1/TSC2 loss, and somatic PI3K-AKT-mTOR pathway
variants converge on abnormal mTOR signaling, dysmorphic neurons, cortical
malformations, and focal epileptogenesis. This family is already partly visible
in the repo through [`kb/disorders/Tuberous_Sclerosis_Complex.yaml`](../../kb/disorders/Tuberous_Sclerosis_Complex.yaml)
and the mTOR nodes currently embedded in [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml).

This is not just a signaling story. The literature now supports a fuller chain:
mTOR hyperactivation, abnormal neuronal growth, dysmorphic/senescent lesional
cells, and focal seizure generation. That makes mTOR-related epilepsy a strong
candidate for a dedicated disorder family in dismech, with gene-level entries
below it and histopathology-aware entries such as focal cortical dysplasia type
II beside it.

Primary literature anchors:

- [PMID:31174205](../../references_cache/PMID_31174205.md): neuronal Depdc5
  loss causes mTORC1 hyperactivation and rapamycin-responsive epilepsy-relevant
  phenotypes.
- [PMID:38710875](../../references_cache/PMID_38710875.md): human FCDII tissue
  and a preclinical model linking dysmorphic/senescent pathological cells to
  epileptiform activity and seizure reduction after senolytics.
- [DOI:10.1002/ctm2.70072](../../references_cache/DOI_10.1002_ctm2.70072.md):
  single-nucleus multiomics in FCD IIIa showing excitatory-neuron, OPC,
  transcription-factor, and neuronal-immunity abnormalities in epileptogenic
  cortex.

## 4. Neuroinflammation, Immune Signaling, and Blood-Brain Barrier Dysfunction

This lane is real, but it needs careful scope discipline. The strongest case is
not that "all epilepsy is inflammatory." The strongest case is that specific
drug-resistant focal epilepsies and acquired epilepsies can be driven or
amplified by endothelial tight-junction loss, glial activation, albumin
extravasation, and immune-mediated synaptic disturbance.

For dismech, BBB dysfunction and glia-neuron signaling may be best represented
in two ways:

1. as a mechanism family for selected acquired or drug-resistant focal
   epilepsies, and
2. as reusable modules that can sit downstream of structural or immune insults.

Autoimmune encephalitis also belongs here, but it should be curated using
well-defined entities rather than a vague umbrella. Anti-NMDA receptor
encephalitis is a good proof that antibodies can directly alter synaptic
receptor abundance and produce frequent seizures, but that does not automatically
make it representative of all immune epilepsies.

Primary literature anchors:

- [PMID:35422069](../../references_cache/PMID_35422069.md): human and model
  evidence that claudin-5 loss and BBB breakdown are linked to seizures and are
  pharmacologically targetable.
- [PMID:31444362](../../references_cache/PMID_31444362.md): glia-neuron
  interactions contribute to state transitions into generalized seizures.
- [PMID:18851928](../../references_cache/PMID_18851928.md): anti-NMDA receptor
  antibodies reduce surface NMDA receptor clusters, with seizures present in a
  large immune-mediated encephalitis cohort.

## 5. Metabolic and Mitochondrial Mechanisms

A separate epilepsy lane is formed by disorders where seizures emerge from
energy failure, impaired substrate delivery, defective oxidative metabolism, or
cofactor deficiency. The pathophysiology is often biochemically concrete and
therapeutically meaningful. These disorders should not be treated as merely
"epilepsy plus metabolic findings."

The common logic across GLUT1 deficiency, lipoic-acid pathway defects, and some
mitochondrial disorders is that brain energy supply or oxidative flux is
insufficient for normal neuronal stability. This class is especially important
for dismech because treatment decisions often follow mechanism directly:
ketogenic diet or other metabolic interventions are not generic antiseizure
therapy, but partial mechanism replacement.

Primary literature anchors:

- [PMID:22152680](../../references_cache/PMID_22152680.md): LIAS deficiency
  connects neonatal-onset epilepsy to defective mitochondrial energy metabolism.
- [PMID:24341803](../../references_cache/PMID_24341803.md): LIPT1 mutations
  produce impaired lipoic-acid attachment with pyruvate and alpha-ketoglutarate
  dehydrogenase deficiency.
- [PMID:18456557](../../references_cache/PMID_18456557.md): randomized trial
  supporting ketogenic diet efficacy in childhood drug-resistant epilepsy,
  which is particularly relevant for metabolic epilepsy families.

Repo-relevant anchor:

- [`kb/disorders/Menkes_Disease.yaml`](../../kb/disorders/Menkes_Disease.yaml)
  already models a seizure-bearing metabolic disorder through copper transport,
  cuproenzyme deficiency, and mitochondrial/redox injury.

## 6. Transcriptional and Developmental Programs

Some epilepsies are best understood as disorders of neuronal development,
migration, chromatin regulation, or activity-dependent transcription, with
seizures emerging downstream of altered circuit assembly. These disorders often
sit in the DEE space and may overlap with photosensitive or generalized
epilepsies.

This lane is important because it prevents the KB from flattening all DEEs into
"severe seizures plus developmental delay." The developmental lesion often
explains why the epilepsy phenotype is broad, early, and accompanied by
persistent cognitive or behavioral impairment even when seizures later improve.
Some genes in this lane, such as ARID1B, are better treated as developmental
mechanism exemplars than as primary epilepsy anchors: seizures can occur, but
they are a feature of a broader neurodevelopmental syndrome rather than the
defining disease phenotype.

Primary literature anchors:

- [PMID:29184203](../../references_cache/PMID_29184203.md): ARID1B
  haploinsufficiency reduces cortical GABAergic interneurons and shifts
  excitatory-inhibitory balance during development, illustrating a
  development-first mechanism that can plausibly feed into epilepsy risk in a
  broader neurodevelopmental syndrome.
- [PMID:20493745](../../references_cache/PMID_20493745.md): CDKL5 mutations
  causing early-onset epileptic encephalopathy with staged epilepsy phenotypes.
- [PMID:30455226](../../references_cache/PMID_30455226.md): PPP3CA mutation in
  early-onset infant epileptic encephalopathy, explicitly tying neuronal
  development and circuit regulation to seizures.
- [PMID:26262932](../../references_cache/PMID_26262932.md): CHD2-associated
  generalized epilepsy with photosensitivity and overlap with recognized
  electroclinical syndromes.

## 7. Network Excitability and Homeostatic Failure

This is the cross-cutting circuit layer that many other mechanism families
converge on. It is indispensable, but it should usually be downstream of more
specific mechanisms. In temporal lobe epilepsy, altered E/I balance can be
measured noninvasively and linked to cognition and gene-expression signatures.
In Jeavons/electroclinical eyelid-myoclonia syndromes, the unresolved question
is whether the initiating circuitry is primarily occipital, generalized
thalamocortical, or both.

The practical rule for dismech is:

- use network excitability/homeostatic failure as a mechanistic layer, and
- avoid using it as the sole basis for lumping etiologically distinct epilepsies
  into one page.

Primary literature anchors:

- [PMID:39056027](../../references_cache/PMID_39056027.md): TLE study linking
  EEG-derived E/I imbalance to cognition and epilepsy-related gene expression.
- [PMID:21729035](../../references_cache/PMID_21729035.md): Jeavons syndrome
  data supporting an occipital-to-generalized network initiation model.
- [PMID:21463282](../../references_cache/PMID_21463282.md): Dravet model
  showing how a specific genetic lesion converges on circuit hyperexcitability.

## Bottom Line for dismech

The most useful epilepsy structure for dismech is likely:

1. an umbrella epilepsy entry kept intentionally high level,
2. several mechanistically coherent family entries below it, and
3. gene- or syndrome-specific entries where precision, prognosis, or treatment
   diverge enough to justify a separate graph.

That structure fits the current repo state better than either extreme:
neither one giant epilepsy page nor hundreds of disconnected gene pages.
