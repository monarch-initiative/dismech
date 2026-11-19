---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:15.729632'
end_time: '2026-11-18T23:41:11.201151'
duration_seconds: 655.47
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Mitochondrial Iron-Sulfur Cluster Assembly Failure
  module_slug: mitochondrial_iron_sulfur_cluster_assembly_failure
  category: Module
  module_description: 'A conserved mechanism module for inherited failure of mitochondrial
    iron-sulfur (Fe-S) cluster biogenesis. A lesion in the core ISC machinery (NFS1-ISD11-ACP
    cysteine desulfurase, ISCU scaffold, frataxin, FDX2/FDXR electron supply, HSPA9/HSCB
    chaperones, GLRX5), in the late [4Fe-4S] assembly and targeting factors (ISCA1,
    ISCA2, IBA57, NFU1, BOLA3), or in export to the cytosolic CIA pathway (ABCB7)
    reduces cluster delivery to client apoproteins. Loss of cluster-dependent enzyme
    activity follows: lipoyl synthase (LIAS), so the lipoylated E2 subunits of pyruvate
    dehydrogenase, 2-oxoglutarate dehydrogenase and the glycine cleavage H-protein
    fail; respiratory complexes I, II and III; aconitase; and, via IRP1 activation,
    cellular iron regulation, producing mitochondrial iron accumulation and ring sideroblasts.'
  pathophysiology_summary: '- Iron-Sulfur Cluster Assembly Lesion: Initiating defect
    in a mitochondrial Fe-S cluster biogenesis factor.

    - Reduced Fe-S Cluster Delivery to Client Apoproteins: Central effector.

    - Lipoyl Synthase Failure: Loss of LIAS activity and protein lipoylation.

    - Respiratory Chain Complex Deficiency: Loss of complexes I, II and III.

    - Mitochondrial Iron Accumulation: IRP1 activation and iron overload.'
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-fable-5-2
  - claude-haiku-5-5
  - claude-opus-5-5
  num_turns: 56
  total_cost_usd: 1.963222000000001
  session_id: cf418dc9-38ba-4334-9c49-adc04898a0e3
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  - Write
  tool_calls: 55
  retrieval_calls: 49
  assistant_text_blocks: 5
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 0
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 1
  off_topic: 1
  off_topic_references:
  - PMID:11050011
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Mitochondrial Iron-Sulfur Cluster Assembly Failure
- **Module Slug:** mitochondrial_iron_sulfur_cluster_assembly_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module for inherited failure of mitochondrial iron-sulfur (Fe-S) cluster biogenesis. A lesion in the core ISC machinery (NFS1-ISD11-ACP cysteine desulfurase, ISCU scaffold, frataxin, FDX2/FDXR electron supply, HSPA9/HSCB chaperones, GLRX5), in the late [4Fe-4S] assembly and targeting factors (ISCA1, ISCA2, IBA57, NFU1, BOLA3), or in export to the cytosolic CIA pathway (ABCB7) reduces cluster delivery to client apoproteins. Loss of cluster-dependent enzyme activity follows: lipoyl synthase (LIAS), so the lipoylated E2 subunits of pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase and the glycine cleavage H-protein fail; respiratory complexes I, II and III; aconitase; and, via IRP1 activation, cellular iron regulation, producing mitochondrial iron accumulation and ring sideroblasts.

## Current Provisional Nodes

- Iron-Sulfur Cluster Assembly Lesion: Initiating defect in a mitochondrial Fe-S cluster biogenesis factor.
- Reduced Fe-S Cluster Delivery to Client Apoproteins: Central effector.
- Lipoyl Synthase Failure: Loss of LIAS activity and protein lipoylation.
- Respiratory Chain Complex Deficiency: Loss of complexes I, II and III.
- Mitochondrial Iron Accumulation: IRP1 activation and iron overload.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology described in the module description and
provisional nodes above. Prioritize evidence for:

- The conserved causal chain represented by the proposed nodes.
- The biological distinctions between node subgroups, especially if the module
  defines branching pathways.
- Any optional or gene-specific branches described in the node list, while
  distinguishing them from core module requirements.
- Explicit exclusions or boundary conditions stated in the module description.

## Questions To Answer

1. What is the best-supported shared mechanism for this module?
2. Is the current module name and scope appropriate, or is a clearer name or
   narrower boundary supported by the literature?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes, variants, exposures, cell types, tissues, or molecular
   processes support each branch or node?
5. What evidence supports the causal edges between upstream drivers, central
   effectors, and downstream consequences?
6. What direct human evidence links the same causal factor or variant class to
   multiple clinical or pathological manifestations?
7. What model organism, in vitro, or other experimental evidence clarifies the
   causal path from molecular perturbation to phenotype?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Output

Bash and file writes are blocked here, so I'm switching to the web fetch and search tools to get at PubMed.

Still gathering PubMed records. I'm now pulling the titles for the founding gene-discovery papers.

I'm now checking model-organism papers (zebrafish, rat, mouse) and the IRP1 evidence.

I have enough sourced evidence, so I'm checking the plan with the advisor before I write the report.

# Mechanism Module Report: Mitochondrial Iron-Sulfur Cluster Assembly Failure

**How this was done.** Every PMID, title and quote below was pulled from NCBI E-utilities (esearch, esummary, efetch) during this session. Quotes are short verbatim excerpts, each under 120 characters, taken from PubMed abstracts by an automated fetch tool. Some start or stop mid-sentence, and line breaks were joined. **Check every quote against the PubMed abstract before curation.** Where an excerpt is really an article title, it is labeled as one. The OLS ontology service refused connections (ECONNREFUSED), so ontology terms are given **by label only**, with no IDs. I did not retrieve full texts.

**How I read the request.** This report is about the shared, gene-independent causal chain from a lesion in the mitochondrial Fe-S assembly machinery to failure of its client enzymes. Diseases of the client enzymes themselves (LIAS, LIPT1/2, SDHx) and complex-specific assembly factors are treated as boundary cases.

---

## 1. Executive recommendation

**Keep the module, but change its structure and tighten its wording.**

1. **Name.** Keep "Mitochondrial Iron-Sulfur Cluster Assembly Failure". A more exact alternative is "Mitochondrial ISC Biogenesis Deficiency". Either way, the description should say the module covers the *mitochondrial ISC machinery* and its late [4Fe-4S] branch. It does not cover the client apoenzymes.
2. **Core chain.** Only three steps are shared by all genes:
   - an ISC factor lesion
   - reduced Fe-S cluster delivery to mitochondrial client apoproteins
   - loss of activity in Fe-S-dependent mitochondrial enzymes (respiratory complexes and/or aconitase and/or lipoyl synthase)

   Every human gene report I retrieved shows some deficit in an Fe-S enzyme. Which enzymes are affected differs by gene.
3. **Split the downstream nodes into two branches.**
   - **Late [4Fe-4S] / lipoylation branch** (NFU1, BOLA3, ISCA1, ISCA2, IBA57, GLRX5): lipoyl synthase fails, followed by PDH, 2-OGDH and glycine cleavage deficits, giving high lactate, pyruvate and glycine and a leukoencephalopathy pattern (the MMDS types 1–5). Lipoylation loss was **not** shown for the early-acting genes in the abstracts I retrieved.
   - **Iron-regulatory / erythroid branch** (GLRX5, HSPA9, HSCB, ABCB7; also FXN and ISCU in tissue): IRP1 is activated, ALAS2 is repressed and heme synthesis falls, mitochondrial iron overloads, and ring sideroblasts form.
4. **Downgrade the current description in three places:**
   - "Complexes I, II and III": the pattern varies by gene. NFS1 gives II/III, IBA57 gives I+II, ISCA2 mainly I, and the NFU1 signature is mainly II.
   - "Via IRP1 activation… mitochondrial iron accumulation": IRP1 activation was directly shown only for GLRX5 (human and zebrafish). Iron accumulation is **absent** in FDX2 patient muscle (PMID 35079622), so this node must be optional.
   - "Ring sideroblasts": this is a gene-specific erythroid outcome, not part of the core.
5. **ABCB7 is a boundary case.** Its main defect is in the *cytosolic* Fe-S maturation (CIA) step (PMID 11050011). It sits outside the "mitochondrial client apoprotein" effector node. I recommend keeping it only as an optional export branch, or moving it to a sister module (see open questions).

---

## 2. Proposed DAG nodes and causal edges

### Nodes

| # | Node | Status | Notes |
|---|---|---|---|
| N1 | Iron-sulfur cluster assembly lesion | **Core (required)** | Subtyped as early ISC (NFS1–ISD11–ACP, ISCU, FXN, FDX2/FDXR, HSPA9/HSCB, GLRX5) versus late [4Fe-4S] (ISCA1, ISCA2, IBA57, NFU1, BOLA3). |
| N2 | Reduced Fe-S cluster delivery to client apoproteins | **Core (required)** | Central effector. |
| N3 | Fe-S-dependent mitochondrial enzyme deficiency (umbrella) | **Core (required)** | Conformance needs at least one of N3a–N3c. |
| N3a | Respiratory chain complex deficiency (I, II and/or III) | Core-satisfying child | Pattern depends on the gene. |
| N3b | Mitochondrial aconitase deficiency | Core-satisfying child | FXN, ISCU, FDX2, LYRM4, ISCA/IBA57. |
| N3c | Lipoyl synthase failure, then loss of protein lipoylation | **Optional, branch-defining** (late [4Fe-4S] and GLRX5) | Leads to N4. |
| N4 | 2-oxoacid dehydrogenase (PDH, 2-OGDH) and glycine cleavage system deficiency | Optional, downstream of N3c | Lactate, pyruvate and glycine rise. "Variant NKH." |
| N5 | IRP1 activation (cytosolic aconitase loses its cluster) | Optional, gene-specific | Direct evidence for GLRX5 only. |
| N6 | Impaired erythroid heme synthesis (ALAS2 repression, ferrochelatase loss) | Optional, gene-specific (new node) | GLRX5, ABCB7, HSPA9, HSCB. |
| N7 | Mitochondrial iron accumulation | Optional, gene-specific | FXN, ISCU, GLRX5. Indirect evidence for FDXR. **Absent for FDX2.** |
| N8 | Ring sideroblast formation / congenital sideroblastic anemia | Optional, erythroid | GLRX5, ABCB7, HSPA9, HSCB. |
| N9 | Cytosolic Fe-S protein maturation defect (export to CIA) | Optional / boundary | ABCB7 (and secondarily any upstream ISC lesion). |

### Edges

| Edge | Strength | Key PMIDs |
|---|---|---|
| N1 → N2 | Strong (human and in vitro) | 22323289, 32817474, 22077971, 21944046, 23814038, 24498631 |
| N2 → N3a | Strong | 24281368, 23814038, 24498631, 27785568, 25539947, 31461310 |
| N2 → N3b | Strong | 9326946, 18304497, 24281368, 23814038, 22323289 |
| N2 → N3c | Strong for the late branch | 22077971, 22323289, 27532772, 29767723, 24334290 |
| N3c → N4 | Strong | 21944046, 24334290, 22152680 (LIAS primary deficiency, used as the positive control) |
| N2 → N5 (cytosolic aconitase/IRP1 loses its cluster) | Moderate: shown for GLRX5 only | 20364084, 16110529 |
| N5 → N6 | Moderate: IRP-mediated ALAS2 repression; zebrafish IRP1 knockdown rescues | 20364084, 16110529 |
| N2 → N6 (direct, IRP-independent) | Plausible: Fe-S needed for ferrochelatase stability | 19965627 (title only), 30660387 |
| N5 → N7 | Weak and indirect. The order is supported in mouse: iron accumulates *after* Fe-S enzymes fail. | 11175786, 20364084 |
| N6/N7 → N8 | Moderate | 20364084, 17192398, 26491070, 32634119 |
| N1 (ABCB7) → N9 | Moderate | 11050011, 25006243 (yeast/Arabidopsis transporter substrate) |

---

## 3. Gene-to-node mapping

"✓" means the finding appears in a retrieved abstract. "nr" means it was not retrieved in this session, which does not mean it is absent. "✗" means a retrieved finding contradicts the node.

| Gene | Role | N3a complexes | N3b aconitase | N3c/N4 lipoylation | N5 IRP1 | N6/N8 heme / sideroblasts | N7 Mt iron | Key PMIDs |
|---|---|---|---|---|---|---|---|---|
| NFS1 | Cysteine desulfurase | ✓ II/III | nr | nr | nr | nr | nr | 24498631; 35026043 (title only) |
| LYRM4 (ISD11) | NFS1 partner | ✓ I, II, III | ✓ ("aconitases", plus ferrochelatase) | nr | nr | nr | nr | 23814038; 31497476 (title only) |
| ACP (NDUFAB1) | NFS1 complex | nr: no human patients found (esearch returned 0) | | | | | | Gap |
| ISCU | Scaffold | nr | ✓ (SDH and aconitase in muscle) | nr | ✗ for "activation": IRP1 *gene* down in muscle | nr | ✓ muscle | 18304497, 23035118, 35079622 |
| FXN | Iron/sulfur donor, NFS1 activator | ✓ I–III | ✓ | nr | nr | nr | ✓ (mouse) | 9326946, 11175786 |
| FDX2 (FDX1L) | Electron supply | ✓ I, II, III | ✓ | nr | nr | nr | **✗ absent** | 24281368, 35079622, 32817474 |
| FDXR | FDX reductase | nr | nr | nr | nr | nr | ✓ indirect ("indirect evidence of mitochondrial iron overload") | 28965846 |
| HSPA9 | Chaperone | nr | nr | nr | nr | ✓ CSA | nr | 26491070 |
| HSCB | Co-chaperone | nr | nr | nr | nr | ✓ CSA, "siderocytes" | nr | 32634119, 24606901 |
| GLRX5 | [2Fe-2S] transfer | nr | nr | ✓ (variant NKH, lipoylation loss) | ✓ | ✓ | ✓ | 20364084, 16110529, 24334290, 30660387 |
| ISCA1 | Late [4Fe-4S] | ✓ "multiple defects" | nr | ✓ | nr | nr | nr | 29767723, 37140997, 22323289 |
| ISCA2 | Late [4Fe-4S] | ✓ I | nr | nr (listed in the LA differential, 27586888) | nr | nr | nr | 25539947 |
| IBA57 | Late [4Fe-4S] | ✓ I + II | nr | nr (listed in the LA differential) | nr | nr | nr | 27785568, 30269484 |
| NFU1 | Late targeting | ✓ II (SDHA/SDHB decreased) | nr | ✓ | nr | nr | nr | 21944046, 22077971, 23179554, 31461310 |
| BOLA3 | Late targeting | ✓ (combined RC) | nr | ✓ | nr | nr | nr | 21944046, 24334290, 27532772 |
| ABCB7 | Export to CIA | nr | nr | nr | nr | ✓ XLSA/A | nr | 10196363, 11050011, 17192398 |

---

## 4. Evidence table

### 4a. Human clinical and patient-cell evidence

| PMID | Gene | Type | Exact excerpt (verify) | Claim supported |
|---|---|---|---|---|
| 21944046 | NFU1, BOLA3 | Human, patient cells plus rescue | "Severe combined deficiency of the 2-oxoacid dehydrogenases, associated with a defect in lipoate synthesis"; "essential roles in the production of [Fe-S] centers for the normal maturation of" | N1→N2→N3c→N4 |
| 22077971 | NFU1 | Human | "impaired activity of the Fe-S enzyme lipoic acid synthase (LAS)"; "We conclude that NFU1 functions as a late-acting maturation factor for a subset" | Late branch; N3c |
| 23179554 | NFU1 | Human, patient tissue | "showed complete absence of protein-bound lipoic acid and decreased SDHA and SDHB subunits of complex II"; "defects in lipoic acid biosynthesis and complex II are the main molecular signature of this disease" | N3a (II) and N3c signature |
| 24334290 | LIAS, BOLA3, GLRX5 | Human | "Patients were deficient in lipoylation of mitochondrial proteins."; "neurodegeneration after a period of normal development." | N3c→N4 (variant NKH); GLRX5 enters the lipoylation branch |
| 29767723 | ISCA1 | Human plus cells | "severe impairment of lipoic acid synthesis."; "severe early onset leukodystrophy, multiple defects of respiratory complexes and a" | N3a, N3c; leukodystrophy |
| 25539947 | ISCA2 | Human | "to mitochondrial depletion and reduced complex I activity as well as decreased"; "MRI indicated similar white matter abnormalities in the patients." | N3a (I); white matter |
| 27785568 | IBA57 | Human | "All patients presented with combined or isolated defect of complex I and II."; "Brain MRI was characterized by cavitating leukodystrophy." | N3a (I+II) |
| 28803783 | NFU1, BOLA3, ISCA2, IBA57 vs LIPT1/2 | Human fibroblasts | "We confirm that NFU1, BOLA3, ISCA2 and IBA57 operate in the maturation of [4Fe-4S]" | Late branch grouping |
| 23814038 | LYRM4 | Human | "in a patient with deficiency of complexes I, II and III in muscle and liver."; "Several other Fe-S proteins were also affected in both patients, including the aconitases and ferrochelatase."; "consistent with a defect in the early step of ISC assembly affecting a broad" | Early lesion causes broad N3; ferrochelatase links to N6 |
| 24498631 | NFS1 | Human | "lactic acidemia, hypotonia, respiratory chain complex II and III deficiency"; "We describe the first disease in man likely caused by deficiency in NFS1" | N3a (II/III) |
| 18304497 | ISCU | Human muscle | "with associated deficiencies of succinate dehydrogenase and aconitase in skeletal muscle."; "consistent with a muscle-specific alteration of iron homeostasis in this disease." | N3a/N3b; tissue-restricted N7 |
| 23035118 | ISCU | Patient cells | "ISCU myopathy is a disease caused by an intronic mutation that leads to abnormally spliced ISCU mRNA."; "Oxidative stress negatively influences the mammalian Fe-S cluster assembly machinery by destabilization of ISCU." | Tissue specificity of N1 |
| 35079622 | ISCU, FDX2 | Human muscle | "Iron was excessively accumulated in ISCU-deficient skeletal muscle"; "This excessive iron accumulation was absent from FDX2 affected muscle"; "a downregulation of IRP1 and mitoferrin2 genes and an upregulation of frataxin (FXN) gene expression"; "ISCU and FDX2 are not involved in mitochondrial iron influx contrary to frataxin." | **N7 is not core**; IRP1 finding is at the transcript level |
| 24281368 | FDX2 (FDX1L) | Human | "severely impaired activities of iron sulfur (Fe-S)-dependent complexes I, II and III mitochondrial aconitase"; "presented with adolescent onset autosomal recessive mitochondrial myopathy" | N3a, N3b |
| 28965846 | FDXR | Human plus yeast | "eight subjects from four independent families affected by auditory neuropathy and optic atrophy"; "deregulated iron homeostasis in FDXR mutant fibroblasts and indirect evidence of mitochondrial iron overload" | N7 (indirect); neuro-sensory phenotype |
| 20364084 | GLRX5 | Human erythroblasts | "the iron-responsive element-binding (IRE-binding) activity of iron regulatory protein 1 (IRP1) was activated"; "Decreased aminolevulinate delta, synthase 2 (ALAS2) levels attributable to IRP-mediated translational repression were"; "were observed together with mitochondrial iron overload" | N5→N6→N7/N8 |
| 30660387 | GLRX5 | Human | "The protein-level of ferrochelatase, the terminal-enzyme of heme process, was increased"; "its activity was drastically decreased" | N6 (ferrochelatase activity, direct Fe-S dependence) |
| 26491070 | HSPA9 | Human | "involved in mitochondrial Fe-S biogenesis, result in CSA inherited as an autosomal recessive trait"; "a common coding single nucleotide polymorphism in trans that correlates with reduced messenger RNA expression" | N8 (CSA); hypomorphic allele mechanism |
| 32634119 | HSCB | Human plus models | "loss of HSCB results in impaired Fe-S cluster biogenesis"; "in a female patient with non-syndromic CSA"; "the development of siderocytes" | N8 |
| 10196363 | ABCB7 | Human genetics | "is an ortholog of the yeast ATM1 gene whose product localizes to the mitochondrial inner membrane"; "characterized by an infantile to early childhood onset of non-progressive cerebellar ataxia" | ABCB7 in XLSA/A |
| 11050011 | ABCB7 | Human plus yeast | "ABC7 is a functional orthologue of Atm1p"; title: "…disruption of cytosolic iron-sulfur protein maturation" | N9 (cytosolic, not mitochondrial client) |
| 9326946 | FXN | Human tissue | "Mutated frataxin triggers aconitase and mitochondrial Fe-S respiratory"; "Hypertrophic cardiomyopathy is observed in most FRDA patients." | N3a/N3b; heart |
| 22152680 | LIAS (client, boundary) | Human | "A pronounced reduction of the prosthetic group lipoamide was found in lipoylated proteins."; "neonatal-onset epilepsy, muscular hypotonia, lactic acidosis, and elevated glycine concentration" | Positive control for N3c→N4 |

### 4b. Model organism evidence

| PMID | System | Exact excerpt (verify) | Claim supported |
|---|---|---|---|
| 16110529 | Zebrafish *shiraz* (grx5) | "loss of Fe-S cluster assembly in sir animals activated IRP1"; "antisense knockdown of IRP1 restored sir embryo haemoglobin synthesis." | **Causal** N5→N6 (rescue) |
| 11175786 | Mouse FXN conditional KO | "motor neurons, and deficient activities of complexes I-III of the respiratory"; "intramitochondrial iron accumulation in a frataxin-deficient mammal, which"; "occurs after onset of the pathology and after inactivation of the Fe-S-dependent" | Order N3 → N7 (iron is a late consequence) |
| 17192398 | Mouse Abcb7 | "partial loss of function mutations in Abcb7 that directly or indirectly inhibit heme biosynthesis"; "formally demonstrate that XLSA/A is due to partial loss of function mutations in Abcb7" | ABCB7→N6/N8 |
| 31461310 | Rat Nfu1 G206C (human G208C) knock-in | "exhibited decreased expression and activity of mitochondrial Complex II"; "NFU1G206C rats showed increased right ventricular pressure, right ventricular hypertrophy" | N3a (II) → pulmonary hypertension |
| 37140997 | Rat neuron-specific Isca1 KO | "reduced content of respiratory chain complex protein"; "the rats suffered from developmental retardation, epilepsy, memory impairment, massive neuronal death" | N3a → neurodegeneration |

### 4c. In vitro and cell-biology evidence

| PMID | System | Exact excerpt (verify) | Claim supported |
|---|---|---|---|
| 22323289 | HeLa knockdown | "ISCA1, ISCA2, and IBA57 are specifically involved in the maturation of mitochondrial [4Fe-4S] proteins"; "including aconitase, respiratory complex I, and lipoic acid synthase" | Late branch → N3a/N3b/N3c |
| 32817474 | Reconstitution | "Electrons from FDX2 catalyze the reductive [2Fe-2S] cluster fusion on ISCA1-ISCA2 in an IBA57-dependent fashion." | FDX2/FDXR feed the late branch |
| 30269484 | Biochemistry | "IBA57 forms a heterodimeric complex with ISCA2 by bridging a [2Fe-2S] cluster" | Late branch mechanism |
| 27532772 | Yeast | "facilitate [4Fe-4S] cluster insertion into a subset of mitochondrial proteins such as lipoate synthase"; "Bol1 and Bol3 form dimeric complexes with both monothiol glutaredoxin Grx5 and Nfu1." | BOLA3/NFU1/GLRX5 as targeting factors for LIAS |
| 24606901 | Human cells | "two LYR motifs engage the ISCU-HSC20-HSPA9 complex"; "key to the assembly and function of complexes I, II, and III" | HSCB/HSPA9 deliver clusters to RC subunits |
| 25006243 | Yeast/Arabidopsis transporters | "We propose that mitochondria export glutathione polysulfide, containing glutathione and persulfide" | What ABCB7-family transporters export (orthologs; human not shown) |

### 4d. Reviews (for context, not primary evidence)

| PMID | Exact excerpt (verify) |
|---|---|
| 31935115 (Lill & Freibert 2020) | "catalytic conversion of the [2Fe-2S] into a [4Fe-4S] cluster and subsequent insertion into recipient apoproteins" |
| 32311335 (Maio & Rouault 2020) | "focus on human diseases caused by failures of the biogenesis pathway" |
| 35883565 (Camponeschi 2022) | "involved in the assembly and insertion of [4Fe-4S] clusters in mitochondrial proteins" |
| 34440194 (Lebigot 2021) | "Diagnosis could be suggested by high lactate, pyruvate, and glycine levels in body fluids."; "nearly all of the patients with MMDS presented with severe and early onset leukoencephalopathy." |
| 24777537 (Mayr 2014) | "LIPT1 deficiency spares the GCS, and resulted in a combined 2-oxoacid dehydrogenase deficiency" |
| 27586888 (Tort 2016) | "NFU1, BOLA3, IBA57, LIAS, GLRX5, LIPT1, ISCA2, and LIPT2" (differential list) |
| 34687937 (Selvanathan 2021) | "such as Friedreich ataxia and ISCU myopathy" |

### Abstract not retrieved or insufficient: full-text check needed

- **Titles only:** 31497476 (LYRM4, 3-MGA-uria), 35026043 (NFS1 spectrum), 30250212 and 37046037 (FDXR), 42829511 (FDXR genotype–phenotype systematic review, 2026), 30010796, 38444577, 41372147 (FDX2), 37511493 (BOLA3 His96Arg), 19965627 (ferrochelatase depends on ISC), 23943793 (FGF21 in ISC depletion), 33711344 (ISCA1 orchestrates ISCA2/NFU1).
- **GeneReviews chapters:** 29470032 (ISCA2) and 20301496 (XLSA/A, a retired chapter). "1993" is the series date, not the publication date.
- **Missing data to look for in full text:** ring sideroblasts and IRP status for HSPA9 and HSCB; lipoylation status for ISCU, FDX2, NFS1, LYRM4 and FXN.

---

## 5. Ontology suggestions (labels only; IDs not verified because OLS was unreachable)

**GO biological process**
- iron-sulfur cluster assembly
- [4Fe-4S] cluster assembly
- [2Fe-2S] cluster assembly
- protein lipoylation
- lipoate biosynthetic process
- mitochondrial electron transport, NADH to ubiquinone
- mitochondrial electron transport, succinate to ubiquinone
- tricarboxylic acid cycle (aconitase)
- glycine catabolic process (glycine cleavage system)
- intracellular iron ion homeostasis
- heme biosynthetic process
- erythrocyte differentiation / hemoglobin biosynthetic process

**GO cellular component (optional):** mitochondrial matrix; mitochondrial inner membrane (ABCB7).

**CL**
- erythroblast (or the more specific "polychromatophilic erythroblast" / "sideroblast", if available)
- skeletal muscle fiber
- cardiac muscle cell
- oligodendrocyte (white-matter disease)
- neuron
- retinal ganglion cell (FDXR optic atrophy)
- pulmonary artery endothelial and smooth muscle cells (NFU1 pulmonary hypertension; check the right terms)

**UBERON**
- bone marrow
- skeletal muscle tissue
- heart / cardiac ventricle
- brain white matter
- cerebellum (ABCB7 ataxia)
- optic nerve
- liver
- lung / pulmonary artery

---

## 6. Out-of-scope boundary notes

- **Defects in the client enzymes themselves are out of scope.** This covers LIAS, LIPT1, LIPT2, SDHx, and aconitase (ACO2). They reproduce N3/N4 without an ISC lesion and are the right positive controls. Note that LIPT1 deficiency spares the glycine cleavage system (24777537).
- **Complex-specific Fe-S insertion factors** (e.g. NUBPL, LYRM7, SDHAF1) were not retrieved here. I recommend excluding them, or treating them as a separate "targeted delivery" module.
- **The CIA pathway beyond ABCB7** (cytosolic and nuclear Fe-S maturation: NUBP1/2, CIAO1, MMS19) is out of scope. ABCB7 itself is a boundary case (11050011).
- **Acquired sideroblastic anemia** (SF3B1-MDS, which reduces ABCB7 expression, e.g. 36028755 and 18398482 by title) is out of scope for an inherited-mechanism module. It could be cross-referenced.
- **Ferroptosis and cancer roles of NFS1/FDXR** (29168506, 39954867 by title) are speculative for the inherited disease and should stay out.
- **Treatment and rescue** (antisense oligonucleotides for ISCU, 28007899) should be noted but kept out of the causal DAG.

---

## 7. Open questions for curator review

1. **ABCB7:** keep it as an optional N9 branch, or move it to a "mitochondrial-to-cytosolic Fe-S export" module? The evidence points to the cytosolic defect.
2. **FXN and Friedreich ataxia:** frataxin is a core ISC component, but FRDA is a repeat-expansion disease with its own large literature. Should FRDA conform here, or get its own module that cross-references this one? Its iron-accumulation evidence (11175786) is the strongest support for N7.
3. **GLRX5** satisfies both branches (lipoylation/variant NKH in 24334290, and IRP1/sideroblastic anemia in 20364084). Should it be tagged as a dual-branch gene, with allele-dependent phenotype?
4. **IRP1 measures disagree.** "IRP1 activation" (IRE-binding activity, GLRX5) is a different measurement from "IRP1 gene downregulation" (ISCU muscle, 35079622). Model N5 strictly as IRE-binding activity.
5. **Is the lipoylation defect confined to the late branch,** or is it simply untested in the early-ISC disorders? Full-text checks are needed for NFS1, LYRM4, ISCU and FDX2.
6. **Tissue specificity** (ISCU muscle mis-splicing, 23035118; erythroid-restricted HSPA9/HSCB; neuro-sensory FDXR): add a "tissue-restricted hypomorph" modifier node?
7. **ACP (NDUFAB1):** a PubMed search found no patient reports. Keep it in the description as machinery only, with no gene-axis disease.
8. **Founding reports I did not retrieve** need to be added before curation: first IBA57 patients, first GLRX5 sideroblastic anemia report, first HSPA9 and LYRM4 functional studies beyond those above, and the original BOLA3 isoform papers.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11050011` (1 mention) - Human ABC7 transporter: gene structure and mutation causing X-linked sideroblastic anemia with ataxia with disruption of cytosolic iron-sulfur protein maturation.
  - shared terms: human

Weighed against this report's own most characteristic terms: `mitochondrial`, `abcb7`, `cluster`, `nfu1`, `fe-s`, `glrx5`, `irp1`, `iscu`, `human`, `aconitase`, `assembly`, `bola3`, `fdxr`, `iron`, `fdx2`, `fe-4`, `iba57`, `isca2`, `nfs1`, `lipoylation`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

No ontology term identifiers were found in this report.