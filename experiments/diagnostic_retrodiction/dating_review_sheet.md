# Dating review sheet

Cases whose discovery report the dating agents could not settle. For each, pick the
**first primary research report** of the test for this disease (eligibility rules
v3, rule 5) and record it in `dating_human_review.tsv`. The case's cutoff is 31
December of the year before that report's PubMed date (the earlier of issue and
e-publication date).

- **NOT_ACCEPTED:** agents A, B and C name three different PMIDs, or no PMID is
  named by two agents whose quotes both pass.
- **ACCEPTED_FLAGGED:** A and B agree, but an earlier paper may be the real report.

Each case lists its candidates first. The earlier written assessment comes last;
read the candidates before it.

Decisions in the TSV: `ACCEPT_PMID | NO_ADEQUATE_REPORT | EXCLUDE_CASE`.

## C007: Barth syndrome — monolysocardiolipin:cardiolipin ratio

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [15805542](https://pubmed.ncbi.nlm.nih.gov/15805542/) | earlier-candidate | Monolysocardiolipins accumulate in Barth syndrome but do not lead to enhanced apoptosis. | J Lipid Res | 2005 Jun | 2004-12-31 (from PubMed pubdate) |
| [16873891](https://pubmed.ncbi.nlm.nih.gov/16873891/) | A, B | Monolysocardiolipin in cultured fibroblasts is a sensitive and specific marker for Barth Syndrome. | J Lipid Res | 2006 Oct | 2005-12-31 |

- **Agent A, PMID 16873891** (quote matches the abstract):
  > We therefore conclude that elevations of MLCLs are specific for BTHS and that the MLCL/CL ratio in fibroblasts is a better diagnostic marker than CL alone.
- **Agent B, PMID 16873891** (quote matches the abstract):
  > We therefore conclude that elevations of MLCLs are specific for BTHS and that the MLCL/CL ratio in fibroblasts is a better diagnostic marker than CL alone.

<details><summary>Earlier assessment</summary>

Both agents chose 16873891 (Houtkooper 2006), which measured MLCL/CL in cultured skin fibroblasts, not an accessible specimen. 15805542 (Valianpour 2005) found MLCL accumulation in patients' lymphocytes, among other tissues: the earlier, blood-based report, though its abstract gives no ratio. Cutoff 2005-12-31 vs 2004-12-31.

</details>

## C009: Celiac Disease — anti-tissue transglutaminase IgA

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [9212111](https://pubmed.ncbi.nlm.nih.gov/9212111/) | earlier-candidate | Identification of tissue transglutaminase as the autoantigen of celiac disease. | Nat Med | 1997 Jul | 1996-12-31 (from PubMed pubdate) |
| [9836104](https://pubmed.ncbi.nlm.nih.gov/9836104/) | A, B | Tissue transglutaminase antibodies for coeliac disease screening. | Ital J Gastroenterol Hepatol | 1998 Oct | 1997-12-31 |

- **Agent A, PMID 9836104** (quote matches the abstract):
  > All the untreated coeliacs and one out of 21 disease controls turned out to be positive for the presence of these antibodies.
- **Agent B, PMID 9836104** (quote matches the abstract):
  > All the untreated coeliacs and one out of 21 disease controls turned out to be positive for the presence of these antibodies.

<details><summary>Earlier assessment</summary>

Both agents chose 9836104 (Ital J Gastroenterol, Oct 1998), a screening study. 9212111 (Dieterich, Nat Med Jul 1997) identified tTG as the endomysial autoantigen and, per the Gut commentary 9391261, already showed raised IgA by tTG ELISA in coeliac sera and not controls. That is the discovery report. Cutoff 1997-12-31 vs 1996-12-31.

</details>

## C010: Childhood Absence Epilepsy — CSF glucose (hypoglycorrhachia)

- **Status:** NOT_ACCEPTED (DISAGREE)
- **Subset:** GLUT1-deficiency absence epilepsy

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [10592074](https://pubmed.ncbi.nlm.nih.gov/10592074/) | B | Glucose transporter type 1 deficiency: a study of two cases with video-EEG. | Eur J Pediatr | 1999 Dec | 1998-12-31 |
| [18479384](https://pubmed.ncbi.nlm.nih.gov/18479384/) | C | Glut-1 deficiency syndrome masquerading as idiopathic generalized epilepsy. | Epilepsia | 2008 Nov | 2007-12-31 |
| [20621801](https://pubmed.ncbi.nlm.nih.gov/20621801/) | A | Paroxysmal exercise-induced dyskinesia, writer's cramp, migraine with aura and absence epilepsy in twin brothers with a novel SLC2A1 missense mutation. | J Neurol Sci | 2010 Aug 15 | 2009-12-31 |

- **Agent B, PMID 10592074** (quote matches the abstract):
  > Atypical absence seizures are common in glucose transporter type 1 deficiency and should alert the clinician to the possibility of this treatable disorder when present in a young child with developmental delay.
- **Agent C, PMID 18479384** (quote matches the abstract):
  > To report the case of a child with short absences and occasional myoclonias since infancy who was first diagnosed with an idiopathic generalized epilepsy, but was documented at follow-up to have a mild phenotype of glucose transporter type 1 deficiency syndrome.
- **Agent A, PMID 20621801** (quote matches the abstract):
  > CSF/serum glucose ratio was moderately decreased in both patients.

<details><summary>Earlier assessment</summary>

A's 20621801 (2010) is a twin case report with absence epilepsy and a moderately low CSF/serum glucose ratio; B's 10592074 (1999) is two GLUT1-deficiency children with atypical absences. Neither establishes the test in a childhood absence epilepsy cohort. Unresolved; needs a targeted search for the first cohort report.

</details>

## C018: Heparin-Induced Thrombocytopenia — anti-PF4/heparin IgG immunoassay

- **Status:** NOT_ACCEPTED (DISAGREE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [1514184](https://pubmed.ncbi.nlm.nih.gov/1514184/) | C, earlier-candidate | Platelet factor 4 complexed to heparin is the target for antibodies generated in heparin-induced thrombocytopenia. | Thromb Haemost | 1992 Jul 6 | 1991-12-31 |
| [8191560](https://pubmed.ncbi.nlm.nih.gov/8191560/) | B | Laboratory diagnosis of heparin-associated thrombocytopenia and comparison of platelet aggregation test, heparin-induced platelet activation test, and platelet factor 4/heparin enzyme-linked immunosorbent assay. | Transfusion | 1994 May | 1993-12-31 |
| [8282825](https://pubmed.ncbi.nlm.nih.gov/8282825/) | A | Antibodies from patients with heparin-induced thrombocytopenia/thrombosis are specific for platelet factor 4 complexed with heparin or bound to endothelial cells. | J Clin Invest | 1994 Jan | 1993-12-31 |

- **Agent C, PMID 1514184** (quote not checkable (no abstract in PubMed)):
  > [no abstract indexed in PubMed; two-page letter reporting original data] Platelet factor 4 complexed to heparin is the target for antibodies generated in heparin-induced thrombocytopenia.
- **Agent B, PMID 8191560** (quote matches the abstract):
  > Positive results were obtained with 33 percent of sera in the PF4/heparin ELISA, with 33.5 percent of sera in the HIPA test, and with 11.5 percent of sera in the PAT.
- **Agent A, PMID 8282825** (quote matches the abstract):
  > We found that plasma from each of 12 patients with HITP contained high titer (> or = 1:200) antibodies that reacted with immobilized complexes of heparin and platelet factor 4 (PF4), a heparin-binding protein contained in platelet alpha-granules.

<details><summary>Earlier assessment</summary>

A's 8282825 (JCI, Jan 1994) shows patient antibodies bind immobilised heparin/PF4 complexes; B's 8191560 (Transfusion, May 1994) compares the PF4/heparin ELISA with functional tests, and lists A's paper among its own earlier hits. A targeted search found 1514184 (Amiral, Thromb Haemost 1992, letter), 'Platelet factor 4 complexed to heparin is the target for antibodies generated in heparin-induced thrombocytopenia', which likely precedes both. It has no abstract, so its content is not verified here. Cutoff 1993-12-31 (agents) vs 1991-12-31.

</details>

## C040: Optic Neuritis — AQP4-IgG

- **Status:** NOT_ACCEPTED (DISAGREE)
- **Subset:** AQP4-IgG-positive optic neuritis

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [15589308](https://pubmed.ncbi.nlm.nih.gov/15589308/) | A, earlier-candidate | A serum autoantibody marker of neuromyelitis optica: distinction from multiple sclerosis. | Lancet | 2004 Dec 11-17 | 2003-12-31 |
| [18094334](https://pubmed.ncbi.nlm.nih.gov/18094334/) | C | Neuromyelitis optica-IgG in childhood inflammatory demyelinating CNS disorders. | Neurology | 2008 Jan 29 | 2006-12-31 |
| [18434643](https://pubmed.ncbi.nlm.nih.gov/18434643/) | B | NMO-IgG predicts the outcome of recurrent optic neuritis. | Neurology | 2008 Jun 3 | 2007-12-31 |

- **Agent A, PMID 15589308** (quote matches the abstract):
  > NMO-IgG was detected in half of patients with high-risk syndromes.
- **Agent C, PMID 18094334** (quote matches the abstract):
  > Two other children were seropositive: 1 of 5 with recurrent ON and one child with recurrent LETM.
- **Agent B, PMID 18434643** (quote matches the abstract):
  > Twenty percent of the patients with recurrent ON seen at Mayo Clinic were seropositive.

<details><summary>Earlier assessment</summary>

A's 15589308 (Lennon 2004) tested NMO and 'syndromes that suggest high risk', which include recurrent optic neuritis; it appears in B's own earlier_pmids. B's 18434643 (Matiello 2008) is a prognostic study in recurrent ON. A's is the real discovery report. Cutoff 2003 vs 2007.

</details>

## C047: Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect — erythrocyte plasmalogens

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [1955304](https://pubmed.ncbi.nlm.nih.gov/1955304/) | A, B | Rhizomelic chondrodysplasia punctata: 16-year follow-up of a child from birth. | Ital J Neurol Sci | 1991 Oct | 1990-12-31 |
| [4010717](https://pubmed.ncbi.nlm.nih.gov/4010717/) | earlier-candidate | Rhizomelic chondrodysplasia punctata: another peroxisomal disorder. | N Engl J Med | 1985 Jul 18 | 1984-12-31 (from PubMed pubdate) |

- **Agent A, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.
- **Agent B, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.

<details><summary>Earlier assessment</summary>

Both agents chose 1955304 (1991), a case report that cites erythrocyte plasmalogens as how the child was diagnosed: not a discovery report. A targeted search found 4010717 (Heymans, NEJM 1985, letter), 'Rhizomelic chondrodysplasia punctata: another peroxisomal disorder', and 2452243 (Hoefler 1988, 'Biochemical abnormalities in RCDP'). The earlier_pmids query missed both because it searched the entry's own name. Heymans has no abstract to verify. Cutoff 1990-12-31 vs 1984-12-31.

</details>

## C048: Rhizomelic Chondrodysplasia Punctata Type 1 — erythrocyte plasmalogens

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [1955304](https://pubmed.ncbi.nlm.nih.gov/1955304/) | A, B | Rhizomelic chondrodysplasia punctata: 16-year follow-up of a child from birth. | Ital J Neurol Sci | 1991 Oct | 1990-12-31 |
| [4010717](https://pubmed.ncbi.nlm.nih.gov/4010717/) | earlier-candidate | Rhizomelic chondrodysplasia punctata: another peroxisomal disorder. | N Engl J Med | 1985 Jul 18 | 1984-12-31 (from PubMed pubdate) |

- **Agent A, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.
- **Agent B, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.

<details><summary>Earlier assessment</summary>

Same as the plasmalogen-synthesis-defect row: agents' 1955304 is a 1991 case report; Heymans 1985 (4010717) is the likely discovery report.

</details>

## C049: Rhizomelic Chondrodysplasia Punctata Type 5 — erythrocyte plasmalogens

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [1955304](https://pubmed.ncbi.nlm.nih.gov/1955304/) | A, B | Rhizomelic chondrodysplasia punctata: 16-year follow-up of a child from birth. | Ital J Neurol Sci | 1991 Oct | 1990-12-31 |
| [4010717](https://pubmed.ncbi.nlm.nih.gov/4010717/) | earlier-candidate | Rhizomelic chondrodysplasia punctata: another peroxisomal disorder. | N Engl J Med | 1985 Jul 18 | 1984-12-31 (from PubMed pubdate) |

- **Agent A, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.
- **Agent B, PMID 1955304** (quote matches the abstract):
  > A boy with rhizomelic chondrodysplasia punctata, diagnosed on the laboratory evidence of a high plasma concentration of phytanic acid and a low erythrocyte concentration of plasmalogens, has been followed from birth to the age of 16 years.

<details><summary>Earlier assessment</summary>

Same as the plasmalogen-synthesis-defect row: agents' 1955304 is a 1991 case report; Heymans 1985 (4010717) is the likely discovery report.

</details>

## C051: Smith-Lemli-Opitz syndrome — serum 7-dehydrocholesterol

- **Status:** ACCEPTED_FLAGGED (EARLIER_DISCOVERY_CANDIDATE)
- **Subset:** ALL

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [7684480](https://pubmed.ncbi.nlm.nih.gov/7684480/) | earlier-candidate | Defective cholesterol biosynthesis in Smith-Lemli-Opitz syndrome. | Lancet | 1993 May 29 | 1992-12-31 (from PubMed pubdate) |
| [8259166](https://pubmed.ncbi.nlm.nih.gov/8259166/) | A, B | Defective cholesterol biosynthesis associated with the Smith-Lemli-Opitz syndrome. | N Engl J Med | 1994 Jan 13 | 1993-12-31 |

- **Agent A, PMID 8259166** (quote matches the abstract):
  > Concentrations of the cholesterol precursor 7-dehydrocholesterol (cholesta-5,7-dien-3 beta-ol), which was not detectable in most of our controls, were elevated (11 to 31 mg per deciliter) more than 2000-fold above normal and were similar to the levels of cholesterol in all tissues from all patients.
- **Agent B, PMID 8259166** (quote matches the abstract):
  > Concentrations of the cholesterol precursor 7-dehydrocholesterol (cholesta-5,7-dien-3 beta-ol), which was not detectable in most of our controls, were elevated (11 to 31 mg per deciliter) more than 2000-fold above normal and were similar to the levels of cholesterol in all tissues from all patients.

<details><summary>Earlier assessment</summary>

Both agents chose 8259166 (Tint, NEJM Jan 1994). earlier_pmids has 8256825 (Tint, Am J Med Genet letter, Sep 1993), and a targeted search found 7684480 (Irons, Lancet letter, May 1993), 'Defective cholesterol biosynthesis in Smith-Lemli-Opitz syndrome'. Both are letters without abstracts, so their content is not verified here, but by title both report the defect before the NEJM paper. Cutoff 1993-12-31 vs 1992-12-31.

</details>

## C055: Stiff Person Syndrome — anti-glycine receptor antibodies

- **Status:** NOT_ACCEPTED (DISAGREE)
- **Subset:** glycine-receptor-antibody PERM

| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |
|---|---|---|---|---|---|
| [18852446](https://pubmed.ncbi.nlm.nih.gov/18852446/) | C, earlier-candidate | Progressive encephalomyelitis, rigidity, and myoclonus: a novel glycine receptor antibody. | Neurology | 2008 Oct 14 | 2007-12-31 |
| [21148607](https://pubmed.ncbi.nlm.nih.gov/21148607/) | A | Antiglycine-receptor encephalomyelitis with rigidity. | J Neurol Neurosurg Psychiatry | 2011 Dec | 2009-12-31 |
| [23090334](https://pubmed.ncbi.nlm.nih.gov/23090334/) | B | Glycine receptor autoimmune spectrum with stiff-man syndrome phenotype. | JAMA Neurol | 2013 Jan | 2012-12-31 |

- **Agent C, PMID 18852446** (quote not checkable (no abstract in PubMed)):
  > [no abstract indexed in PubMed; two-page clinical/scientific note] Progressive encephalomyelitis, rigidity, and myoclonus: a novel glycine receptor antibody.
- **Agent A, PMID 21148607** (quote matches the abstract):
  > GlyR-ab was detected with a cell-based assay of HEK293 cells transfected with the α1 subunit of the GyR.
- **Agent B, PMID 23090334** (quote matches the abstract):
  > Seropositive cases (12% of cases) included 9 with stiff-man syndrome (4 classic; 5 variant; 66% were glutamic acid decarboxylase 65-IgG positive) and 1 with progressive encephalomyelitis with rigidity and myoclonus.

<details><summary>Earlier assessment</summary>

A's 21148607 (Mas 2011) opens by saying GlyR antibodies 'were reported in a patient with PERM'; B's 23090334 (McKeon 2013) is a later spectrum study. A targeted search found 18852446 (Hutchinson, Neurology 2008), 'Progressive encephalomyelitis, rigidity, and myoclonus: a novel glycine receptor antibody', which is that original report. Neither agent's paper is the discovery. Cutoff 2007-12-31 if Hutchinson is right.

</details>
