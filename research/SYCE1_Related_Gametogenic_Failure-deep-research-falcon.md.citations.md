# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder Mechanisms Knowledge Base. Use the seed claims below, then search for supporting, qualifying, or missing evidence. Prefer primary literature where available, but clearly label review-level support.

## Target Disease
- Disease name: SYCE1-related gametogenic failure
- Mondo: MONDO:1060214
- Category: Mendelian

## Seed Hypothesis
SYCE1-related gametogenic failure is caused by biallelic SYCE1 loss or damaging variants. SYCE1 is a synaptonemal-complex central element protein. Loss disrupts central element assembly and SYCE1 interactions with SYCP1 and C14ORF39/SIX6OS1, causing homologous chromosome synapsis failure during meiotic prophase I. Unsynapsed chromosomes lead to pachytene-stage meiotic arrest/checkpoint activation and germ-cell depletion. The same mechanism produces primary ovarian insufficiency or primary amenorrhea in 46,XX individuals and non-obstructive azoospermia or spermatogenic arrest in 46,XY individuals.

## Seed Evidence From Existing Curation

- PMID:25062452, human clinical: "A nonsense homozygous mutation (c.613C>T) was identified in the SYCE1 gene in both affected sisters. The parents and three brothers were heterozygous for the mutation, and an unaffected sister did not carry the mutation."
- PMID:25062452, human clinical: "These results highlight the importance of the synaptonemal complex and meiosis in ovarian function."
- PMID:32402064, model organism: "No SYCE1 protein was detected in homozygous mutants and Syce1 transcript level was highly diminished, suggesting transcript degradation as the basis of the infertility mechanism."
- PMID:32402064, model organism: "Our results strongly support a causative role of this mutation for the POI phenotype in human patients, and the mechanisms involved would relate to defects in homologous chromosome synapsis."
- PMID:32402064, model organism/context: "a familial mutation reported in two sisters with primary amenorrhea"
- PMID:34718620, in vitro/functional and human cohort: "the variations in SYCE1 disrupted its interaction with SYCP1 or C14ORF39, both of which affected SC assembly and meiosis."
- PMID:34718620, human clinical: "Our study identified novel pathogenic variations of C14ORF39 and SYCE1 in sporadic patients with POI or NOA, highlighting the essential role of SC genes in the maintenance of ovarian and testicular function."
- PMID:35718780, human clinical: "H&E and IF staining demonstrated that the spermatogenesis was arrested at pachytene stage in the two patients with NOA, suggesting these two novel CNVs within SYCE1 could lead to meiotic defect and NOA."

## Required Output

1. Executive judgment on whether the seed mechanism is supported, partially supported, or weakly supported.
2. Evidence matrix with citation, evidence type, claim tested, key finding, confidence, and limitations.
3. Clinical spectrum summary: 46,XX POI/primary amenorrhea; 46,XY non-obstructive azoospermia/spermatogenic arrest; any biochemical or histologic findings such as FSH/AMH, follicle depletion, pachytene arrest.
4. Variant and inheritance summary: variant classes, families/cohorts, biallelic inheritance, CNVs/deletions, loss of function.
5. Mechanistic causal chain from SYCE1 variant to synaptonemal complex assembly failure, homologous chromosome synapsis failure, pachytene arrest/checkpoint activation, germ-cell apoptosis/depletion, and sex-dimorphic reproductive phenotype.
6. Diagnostics and management implications: genetic testing, semen analysis, testicular biopsy, hormone replacement for POI, fertility preservation/oocyte cryopreservation, micro-TESE/ICSI context, genetic counseling.
7. Ontology suggestions by label only: HPO phenotypes, GO biological processes, CL cell types, treatment/action terms.
8. Knowledge gaps and weak claims: distinguish human direct evidence from mouse/model inference; identify claims needing full-text verification or additional cohorts.
9. Curation leads: specific updates that might be considered for the SYCE1 entry, but label them as leads requiring curator verification.

Do not fabricate PMIDs. If a source cannot be retrieved by the tool, state that clearly and use the seed evidence cautiously.
**Provider:** falcon
**Generated:** 2026-05-28T23:59:49.099085

1. https://pubmed.ncbi.nlm.nih.gov/25062452/
2. https://pubmed.ncbi.nlm.nih.gov/32402064/
3. https://pubmed.ncbi.nlm.nih.gov/34718620/
4. https://pubmed.ncbi.nlm.nih.gov/35718780/
