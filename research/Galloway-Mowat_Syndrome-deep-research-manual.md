---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-14T06:30:00Z'
end_time: '2026-04-14T08:01:21Z'
duration_seconds: 5481.0
citation_count: 13
notes: >
  Manual deep research was performed from PubMed primary papers, case series,
  and recent review abstracts plus local OAK ontology lookup. Reference caches
  were created with `just fetch-reference` and the disorder was scoped as the
  syndrome-level parent/root with explicit MONDO subtype coverage.
---

## Question

Curate a disease-level dismech entry for Galloway-Mowat syndrome as a broad parent/root, with subtype and gene heterogeneity documented, using PMID-backed exact quotes only and ontology-grounded disease, mechanism, phenotype, and treatment terms.

## Output

# Galloway-Mowat Syndrome Manual Deep-Research Note

## Scope

- Parent disease term: `MONDO:0009627` `Galloway-Mowat syndrome`
- Curation frame: syndrome-level parent/root, not a single-gene disorder
- Primary convergent outcomes: early-onset nephrotic syndrome/proteinuria plus microcephaly and brain malformation
- Key subtype families supported in the literature:
  - `WDR73`
  - KEOPS / t6A biogenesis: `LAGE3`, `OSGEP`, `TP53RK`, `TPRKB`, `GON7`, `YRDC`
  - nucleoporins: `NUP107`, `NUP133`
  - additional broadened genes: `WDR4`, `PRDM15`

## Exact Quoted Support

### Core syndrome definition

- PMID:40533795
  > Galloway-Mowat syndrome (GAMOS) is a rare autosomal recessive genetic disorder that is underrecognized.
- PMID:40533795
  > The phenotype is heterogeneous, but it is now widely accepted that early-onset nephrotic syndrome (SRNS) and microcephaly with brain malformation are characteristic features of Galloway-Mowat syndrome.
- PMID:36755238
  > Galloway-Mowat syndrome (GAMOS) is a group of rare hereditary diseases by the combination of early onset steroid-resistant nephrotic syndrome (SRNS) and microcephaly with brain anomalies caused by WDR73, LAGE3, OSGEP, TP53RK, TPRKB, GON7, WDR4 or NUP133 mutations.

### WDR73 subtype

- PMID:25466283
  > Galloway-Mowat syndrome is a rare autosomal-recessive condition characterized by nephrotic syndrome associated with microcephaly and neurological impairment.
- PMID:25466283
  > These data suggest that WDR73 plays a crucial role in the maintenance of cell architecture and cell survival.
- PMID:25466283
  > Altogether, WDR73 mutations cause Galloway-Mowat syndrome in a particular subset of individuals presenting with late-onset nephrotic syndrome, postnatal microcephaly, severe intellectual disability, and homogenous brain MRI features.

### KEOPS / t6A pathway

- PMID:31481669
  > We recently identified mutations in genes encoding four out of the five KEOPS subunits in children with Galloway-Mowat syndrome (GAMOS), a clinically heterogeneous autosomal recessive disease characterized by early-onset steroid-resistant nephrotic syndrome and microcephaly.
- PMID:31481669
  > Here we show that mutations in YRDC cause an extremely severe form of GAMOS whereas mutations in GON7, encoding the fifth KEOPS subunit, lead to a milder form of the disease.
- PMID:31481669
  > mutations which alter t6A biosynthesis in human cells have an impact on cell survival through decreased proliferation and protein synthesis, ultimately leading to apoptosis.

### OSGEP clinical severity

- PMID:30558655
  > Overall, 6 patients from 5 different Taiwanese families were included in our study; the patients had an identical OSGEP gene mutation (c.740G > A transition) and all exhibited a uniform clinical phenotype with early-onset nephrotic syndrome, craniofacial and skeletal dysmorphism, primary microcephaly with pachygyria, and death before 2 years of age.
- PMID:30558655
  > Neurological findings consisted of microcephaly, hypotonia, developmental delay, and seizures.
- PMID:30558655
  > Brain imaging studies all showed pachygyria and hypomyelination.
- PMID:30558655
  > All patients developed early-onset nephrotic syndrome. The proteinuria was steroid-resistant and eventually resulted in renal function impairment.
- PMID:30975089
  > These two cases, in conjunction with the findings of a literature review, indicate that OSGEP pathogenic variants are associated with an earlier onset of nephrotic syndrome and shorter life expectancy than WDR73 pathogenic variants.

### LAGE3 subtype and inheritance nuance

- PMID:36755238
  > Seven male members died prematurely, and three of them suffered from nephrotic syndrome, which is consistent with the x-linked gene map of the disease.
- PMID:36755238
  > The overall symptoms of the disease due to the LAGE3 mutation were mild compared to other pathogenic genes.
- PMID:36755238
  > Due to the heterogeneity of the renal phenotype, regular proteinuria screening is recommended for all patients diagnosed with GAMOS.

### Nucleoporin subtypes

- PMID:28280135
  > The founder mutation was associated with concomitant reduction in NUP107 protein and in the obligate binding partner NUP133 protein, as well as density of nuclear pores in patient cells.
- PMID:28280135
  > With the addition of these individuals, we implicate an allele-specific critical role for NUP107 in the regulation of brain growth and a GAMOS-like presentation.
- PMID:30427554
  > NUP107 and NUP133 (nucleoporin 133kDa) are interacting subunits of the nuclear pore complex in the nuclear envelope during interphase, and these proteins are also involved in centrosome positioning and spindle assembly during mitosis.
- PMID:30427554
  > A nup133-knockdown zebrafish model exhibited microcephaly, fewer neuronal cells, underdeveloped glomeruli, and fusion of the foot processes of the podocytes, which mimicked human GAMOS features.
- PMID:30427554
  > These data indicate that the biallelic NUP133 loss-of-function mutation causes GAMOS.

### Podocyte pathology

- PMID:11793093
  > Synaptopodin, GLEPP1, and nephrin expression was present, although reduced in Galloway-Mowat syndrome.
- PMID:36290302
  > our study indicated that nephrotic syndrome in GAMOS1 is associated with disruption of FA caused by WDR73 deficiency.

### Expanded gene space

- PMID:40533795
  > Although the five subunits that encode the KEOPS complex, OSGEP/TP53RK/TPRKB/LAGE3/GON7, are known to cause Galloway-Mowat syndrome, the mutation of the WDR73, WDR4, NUP107, NUP133, and PRDM15 genes can lead to Galloway-Mowat syndrome, which makes the diagnosis more challenging.
- PMID:33593823
  > Variants in PRDM15 can cause either isolated nephrotic syndrome or a GAMOS-type syndrome on an allelic basis.
- PMID:36681682
  > Patients with mutations of WDR4, a substrate adaptor of the CUL4 E3 ligase complex, develop cerebellar atrophy and gait phenotypes.

### Management evidence

- PMID:30558655
  > Prenatal ultrasound findings, fetal MRI, genetic counseling, and mutation analysis may be useful for an early prenatal diagnosis.
- PMID:31481669
  > most of the individuals carrying GON7 mutations were alive at last follow-up, with either a functioning graft or with normal renal function despite a mild to heavy proteinuria

## Curation Decisions

- Parent/root framing:
  The parent MONDO term already has explicit subtype children (`GAMOS1` through `GAMOS10`) and recent review evidence confirms broader genetic heterogeneity. The disorder YAML should therefore represent the syndrome as the root disease and keep gene-defined subtypes inside `has_subtypes`.

- Inheritance modeling:
  The literature still commonly describes GAMOS as autosomal recessive, but `LAGE3` creates a real X-linked branch. The YAML should therefore keep both `Autosomal recessive` and `X-linked recessive` inheritance entries, with a note explaining the spectrum.

- Mechanism modeling:
  The most defensible disease graph is convergent:
  - KEOPS / YRDC / GON7 defects -> impaired `tRNA modification`
  - `WDR73` defects -> disrupted focal adhesion, RNA processing, and cell-cycle control
  - `NUP107` / `NUP133` defects -> nuclear pore and spindle dysfunction
  - all of the above -> podocyte failure + impaired brain growth

- Phenotype selection:
  The safest high-signal phenotype set for the initial disease-level entry is:
  - `HP:0000252` Microcephaly
  - `HP:0012588` Steroid-resistant nephrotic syndrome
  - `HP:0001263` Global developmental delay
  - `HP:0008936` Axial hypotonia
  - `HP:0001250` Seizure
  - `HP:0001302` Pachygyria
  - `HP:0012444` Brain atrophy

- Treatment selection:
  The literature supports conservative treatment assertions only:
  - `MAXO:0000079` genetic counseling
  - `MAXO:0010039` organ transplantation, localized to kidney, only as subtype-limited renal rescue after ESRD

## Ontology Anchors Used

- Disease:
  - `MONDO:0009627` Galloway-Mowat syndrome
  - `MONDO:0033005` Galloway-Mowat syndrome 1
  - `MONDO:0033006` Galloway-Mowat syndrome 2, X-linked
  - `MONDO:0033007` Galloway-Mowat syndrome 3
  - `MONDO:0033008` Galloway-Mowat syndrome 4
  - `MONDO:0033009` Galloway-Mowat syndrome 5
  - `MONDO:0032691` Galloway-Mowat syndrome 6
  - `MONDO:0032692` Galloway-Mowat syndrome 7
  - `MONDO:0032693` Galloway-Mowat syndrome 8
  - `MONDO:0030471` Galloway-Mowat syndrome 9
  - `MONDO:0030476` Galloway-Mowat syndrome 10

- Cell and anatomy terms:
  - `CL:0000653` podocyte
  - `CL:0000540` neuron
  - `UBERON:0002113` kidney
  - `UBERON:0000955` brain

- Biological process and component terms:
  - `GO:0006400` tRNA modification
  - `GO:0006396` RNA processing
  - `GO:0048041` focal adhesion assembly
  - `GO:0044843` cell cycle G1/S phase transition
  - `GO:0051225` spindle assembly
  - `GO:0005643` nuclear pore

- Treatment terms:
  - `MAXO:0000079` genetic counseling
  - `MAXO:0010039` organ transplantation

## PMID Set Used

- PMID:11793093
- PMID:25466283
- PMID:28280135
- PMID:30427554
- PMID:30558655
- PMID:30975089
- PMID:31481669
- PMID:33593823
- PMID:33686175
- PMID:36290302
- PMID:36681682
- PMID:36755238
- PMID:40533795
