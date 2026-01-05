---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-16T19:09:37.023396'
end_time: '2025-12-16T19:12:05.942806'
duration_seconds: 148.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibrodysplasia Ossificans Progressiva
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 58
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Fibrodysplasia Ossificans Progressiva
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fibrodysplasia Ossificans Progressiva**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

<think>
This is a comprehensive request for a disease pathophysiology research report on Fibrodysplasia Ossificans Progressiva (FOP). I need to synthesize information from all the provided search results into a well-structured, comprehensive report that covers:

1. Core pathophysiology and molecular mechanisms
2. Key molecular players (genes, proteins, metabolites)
3. Biological processes affected
4. Cellular components involved
5. Disease progression stages
6. Phenotypic manifestations
7. Clinical relationships to mechanisms

The search results are extensive and include recent research from 2023-2024 as well as foundational studies. I need to organize this into a coherent narrative that exceeds 10,000 words.

Let me structure this as:
- Title with summary
- Introduction to FOP
- Genetic basis and molecular foundation
- ACVR1 mutation and BMP signaling dysfunction
- Heterotopic ossification mechanism
- Inflammatory mechanisms
- Cellular and progenitor cell involvement
- Molecular signaling cascades
- Disease progression and clinical manifestations
- Therapeutic targets and emerging treatments
- Conclusion

Let me start writing the comprehensive report.
</think>

# Pathophysiology of Fibrodysplasia Ossificans Progressiva: Molecular Mechanisms, Cellular Events, and Disease Progression

Fibrodysplasia ossificans progressiva (FOP) is an extraordinarily rare but profoundly disabling genetic disorder characterized by progressive heterotopic ossification—the formation of qualitatively normal bone in locations where bone does not normally develop, such as skeletal muscles, tendons, ligaments, and connective tissues[1][8]. This devastating disease exemplifies a failure of normal developmental and regenerative processes, wherein the body's own bone morphogenetic protein (BMP) signaling pathway becomes hyperactivated through gain-of-function mutations in the ACVR1/ALK2 gene, ultimately leading to the formation of a disabling second skeleton that progressively locks patients into immobility[1][3]. The median life expectancy for patients with FOP is approximately 40 years, with most individuals becoming wheelchair-bound by their third decade of life, primarily due to thoracic insufficiency syndrome and related respiratory complications[1][8]. Understanding the pathophysiology of FOP has proven illuminating not only for this rare condition but also for broader principles of heterotopic ossification, stem cell biology, and the intersection between developmental signaling pathways and inflammatory responses that can transform normal tissue regeneration into pathological bone formation.

## Genetic Basis and Molecular Foundation of FOP

The genetic foundation of FOP was discovered through identification of heterozygous gain-of-function mutations in the ACVR1 gene located on chromosome 2[1][2]. The ACVR1 gene encodes activin A receptor type I, also known as activin receptor-like kinase 2 (ALK2), a transmembrane serine/threonine kinase receptor that functions as a type I receptor in the bone morphogenetic protein (BMP) signaling pathway[1][3]. The vast majority of FOP cases—approximately 90 percent—are caused by a single, recurrent point mutation designated c.617G>A, which results in an arginine-to-histidine substitution at codon position 206 (R206H) within the glycine-serine (GS) rich activation domain of the ACVR1 protein[1][2][3]. This R206H mutation occurs in a CpG dinucleotide within a coding exon that lacks a high density of CpG islands, and the mutation arises through spontaneous deamination of methylated cytosine, representing the most common nucleotide substitution found in humans[2]. Remarkably, the identical R206H mutation has also been identified in at least two cats with FOP, confirming the general biological validity of this mutation across mammalian species[2].

While the R206H mutation accounts for the vast majority of classic FOP cases, patients presenting with atypical FOP phenotypes—termed FOP-plus or FOP variants—have been found to carry novel heterozygous ACVR1 missense mutations in conserved amino acids located within either the GS domain or the protein kinase domain of the receptor[2][57]. These atypical mutations include p.Q207E, p.G328R, p.G328E, p.G328W, p.R258S, p.R375P, p.L196P, and p.R202I, among others[60]. Protein structure homology modeling predicts that each of these amino acid substitutions activates the ACVR1 protein and enhances receptor signaling activity, and importantly, genotype-phenotype correlation studies reveal relationships between specific ACVR1 mutations and the age of onset of heterotopic ossification or effects on embryonic skeletal development[57]. The key observation that all FOP-causing mutations are heterozygous—with affected individuals carrying one normal and one mutant ACVR1 allele—demonstrates that a single mutant copy is sufficient to cause disease, establishing FOP as an autosomal dominant disorder[1][8].

## Pathophysiology of the ACVR1 R206H Mutation and BMP Signaling Dysregulation

The ACVR1 R206H gain-of-function mutation fundamentally alters the signaling properties of the type I receptor, inducing both ligand-independent constitutive activity and ligand-dependent hyperactivity through the bone morphogenetic protein signaling cascade[1][3][4][5]. To understand the pathophysiology of this mutation, it is essential first to appreciate the normal function of ACVR1 in canonical BMP signaling. In normal circumstances, ACVR1 functions as a type I BMP receptor that requires ligand binding and interaction with type II receptors to become activated[3]. The BMP ligands BMP2, BMP4, BMP6, and BMP7 bind to type II receptors, which then recruit and phosphorylate type I receptors such as ACVR1 at specific serine and threonine residues within the GS domain, thereby activating the kinase activity of the type I receptor[3]. The activated ACVR1 receptor then phosphorylates intracellular SMAD proteins—specifically SMAD1, SMAD5, and SMAD8/9—which subsequently complex with the common mediator SMAD4 and translocate to the nucleus to regulate the transcription of BMP-responsive target genes[1][3][5].

The R206H mutation disrupts normal regulatory mechanisms that keep ACVR1 in an inactive state in the absence of appropriate stimuli[2][24][39]. Structural analysis reveals that the FOP-ACVR1 mutant receptor exhibits mild constitutive (ligand-independent) kinase activity, meaning the receptor transmits signals even without exogenous BMP ligand stimulation[5][21]. More critically, the mutant receptor becomes hypersensitive to BMP ligands, particularly to BMP2, BMP4, BMP6, and BMP7, resulting in much higher levels of phosphorylation of downstream SMAD1/5/8 proteins compared to wild-type ACVR1 in response to the same BMP ligand concentration[3][5]. This aberrant signaling through the SMAD pathway leads to increased expression of BMP transcriptional target genes and enhanced osteogenic and chondrogenic gene expression[4][5]. The dysregulation of the canonical BMP pathway is further amplified by disruptions in the normal negative feedback mechanisms that typically limit BMP signaling. In cells expressing the FOP mutation, there is increased expression of BMP4 and decreased expression of BMP antagonists such as Noggin and Gremlin, meaning the pathway fails to appropriately regulate the concentration of BMP in the extracellular space[13]. Thus, ACVR1 R206H mutant cells cannot properly control the intensity and duration of BMP signaling, resulting in constitutive activation of the osteogenic program.

A particularly significant discovery in FOP pathophysiology emerged in 2015 when researchers demonstrated that the ACVR1 R206H mutant receptor acquires a novel molecular property: the capacity to respond to Activin A, a ligand that normally signals through ACVR1B (ALK4) rather than ACVR1 (ALK2)[24][41]. Wild-type ACVR1 does not respond to Activin A in the BMP signaling context; instead, Activin A typically functions through the TGF-β/SMAD2/3 signaling pathway via ACVR1B[24][41]. However, FOP-ACVR1 R206H has acquired the ability to transduce BMP signaling in response to Activin A, resulting in aberrant activation of BMP-specific SMAD1/5/8 phosphorylation in addition to the normal TGF-β/SMAD2/3 signaling[24]. This acquired responsiveness to Activin A has been implicated as a crucial trigger for heterotopic ossification in FOP patients, as neutralizing antibodies against Activin A suppress heterotopic ossification in FOP mouse models[38][41]. The discovery of this mechanism has led to ongoing clinical trials testing anti-Activin A monoclonal antibodies (REGN2477) as a therapeutic intervention for FOP[41].

## Non-Canonical BMP Signaling and Mechanotransduction Pathways in FOP

Beyond the canonical SMAD1/5/8 signaling pathway, FOP-ACVR1 mutations also aberrantly activate multiple non-canonical signaling pathways that contribute to the pathophysiology of heterotopic ossification[3][5][13]. The p38 mitogen-activated protein kinase (MAPK) pathway represents one critical non-canonical effector of BMP signaling[3][5][13]. In normal BMP signaling, ligand-bound type II receptors activate the type I receptor ALK2, which phosphorylates not only SMAD proteins but also recruits and activates transforming growth factor-beta-activated kinase 1 (TAK1)[37][40]. TAK1 then activates downstream MAPK kinases (MKK3/6), which phosphorylate and activate p38 MAPK[37][40]. Activated p38 MAPK phosphorylates and activates the master osteogenic transcription factors RUNX2, DLXL5, and Osterix (OSX), which are essential for osteoblast differentiation and bone formation[5][40]. In FOP patients and FOP cell models, p38 MAPK phosphorylation is significantly elevated in response to BMP stimulation, and pharmacological inhibition of p38 MAPK activity has been shown to reduce heterotopic ossification in mouse models[5][37].

Another important non-canonical pathway dysregulated in FOP involves the mechanotransduction pathway mediated by RhoA[3][23]. The canonical transducer of BMP signaling, phosphorylated SMAD1/5/8 (pSMAD1/5/8), is shared with the RhoA pathway, which is a mechanotransduction mechanism crucial for regulating cell movements and how cells sense their physical environment[3][23]. FOP mutations aberrantly phosphorylate SMAD1/5/8 in response to abnormal signals, and this crosstalk between BMP and RhoA signaling pathways means that FOP mutant cells lose their ability to correctly sense and respond to mechanical forces in the microenvironment[3]. This impaired mechanosensing has profound implications for tissue regeneration and may explain why muscle injury frequently triggers heterotopic ossification in FOP patients.

Additionally, emerging research has identified dysregulation of phosphoinositide 3-kinase (PI3K) and mammalian target of rapamycin (mTOR) signaling in FOP[5][22]. FOP-ACVR1 R206H has been shown to induce PI3K and mTOR signaling, and inhibitors of mTOR have demonstrated efficacy in reducing heterotopic ossification in FOP mouse models[5][22]. The mTOR pathway represents a particularly attractive therapeutic target because it functions upstream of hypoxia-inducible factor 1-alpha (HIF1-α), another critical regulator of heterotopic ossification in FOP that will be discussed in subsequent sections[22].

## Heterotopic Ossification Through Endochondral Ossification: Cellular and Tissue Events

Heterotopic ossification in FOP progresses through a characteristic sequence of histological stages that remarkably recapitulate embryonic skeletal development and postnatal fracture healing, yet occurs in abnormal anatomical locations and is associated with inflammation and immune cell infiltration that distinguishes it from normal bone formation[1][3][4][13]. The process of bone formation in FOP occurs through endochondral ossification (EO), the same mechanism by which most of the developing embryonic skeleton forms—through an intermediate cartilage template that is subsequently replaced by bone[1][3][4]. However, heterotopic endochondral ossification in FOP differs fundamentally from normal skeletal development in that it grows irregularly, is commonly associated with immune cell activity and inflammation, and occurs in response to tissue injury or infection in the postnatal period rather than being subject to the tight developmental regulation that governs embryonic skeletal formation[3].

The histopathological evolution of FOP lesions proceeds through a well-characterized sequence of overlapping phases[1][4]. In the earliest stage, termed the catabolic or inflammatory phase, there is rapid and destructive tissue damage characterized by intense mononuclear cell infiltration involving macrophages, mast cells, and lymphocytes, as well as perivascular infiltration of these immune cells[1][8][13]. During this phase, the inflammatory cellular infiltrate migrates into the affected skeletal muscle, causing death of muscle cells through mechanisms that remain incompletely understood but appear to involve both direct inflammatory damage and cytokine-mediated cell death[1][8]. This catabolic phase is clinically manifested as a "flare-up"—an episodic event characterized by swelling (edema), pain, decreased range of motion, stiffness, and sometimes warmth at the affected site[7][10].

Following the intense inflammatory phase, a robust anabolic phase supervenes within days to weeks, characterized by intensive fibroproliferation, angiogenesis, neovascularity, and a very high density of mast cells[1][4][8]. The early fibroproliferative lesions are histologically similar to aggressive juvenile fibromatosis and cannot be easily distinguished from this condition, which has important implications for diagnosis[1][8]. As these lesions mature, the fibroproliferative tissue undergoes a remarkable transformation through a process of avascular condensation into cartilage via chondrogenic differentiation[1][4]. This fibroproliferative-to-chondrogenic transition is a critical developmental step where mesenchymal progenitor cells differentiate into chondrocytes, accumulate cartilage matrix proteins such as collagen II and aggrecan, and organize into a cartilage structure that serves as a scaffold for subsequent bone formation[3][4][8]. The final phase involves revascularization accompanied by osteogenesis—the replacement of the cartilage template with mature bone through both osteoclast-mediated cartilage resorption and osteoblast-mediated bone matrix deposition[1][4][8]. The resulting heterotopic bone masses contain mature lamellar bone and often include marrow elements (fat cells, blood vessels, and hematopoietic elements), making them histologically identical to normal skeletal bone[1][4].

A crucial observation regarding FOP heterotopic ossification is that the fibroproliferative, chondrogenic, and osteogenic stages are characterized by multipotent stem-like cells of vascular origin, while the late osteogenic phase involves inflammatory cells of hematopoietic origin[1][4]. This mixed cellular composition, with contributions from both vascular-derived mesenchymal progenitors and hematopoietic immune cells, highlights the intimate connection between inflammatory responses and bone formation in FOP pathophysiology. Different regions of an active FOP lesion can be at different stages of maturation simultaneously, suggesting different rates of maturation across the lesion and indicating that the overall process involves multiple overlapping waves of cellular activity and differentiation.

## Cellular Progenitors and Their Role in Heterotopic Ossification

A critical advancement in understanding FOP pathophysiology came from studies employing Cre-lox lineage tracing methodologies to identify which cell populations contribute to heterotopic ossification[4][26]. These studies revealed that Tie2-expressing cells—markers of endothelial and endothelial precursor cells—contribute robustly to the fibroproliferative, chondrogenic, and osteogenic stages of heterotopic ossification and constitute a major cellular source of the bone-forming cells[4][26]. When researchers used Tie2-Cre transgenic mice in which endothelial and endothelial precursor cells are genetically marked, they found that these Tie2+ cells comprised approximately 40-50 percent of lesional cells at the fibroproliferative, chondrogenic, and osteogenic stages of heterotopic ossification maturation[4]. Importantly, in FOP models, Tie2+ cells appear responsible in part for the formation of the initial fibroproliferative lesion, suggesting that endothelial precursors respond to inflammatory signals and become the primary cell source for heterotopic bone formation[4][26]. Recent work has further demonstrated that Tie2-expressing endothelial progenitor cells can transform into multipotent mesenchymal stem cells through an ACVR1-dependent mechanism[29].

More recent research has identified fibro/adipogenic progenitors (FAPs) as another prominent heterotopic ossification progenitor population[5][15][18]. FAPs are skeletal muscle-resident progenitor cells defined by their anatomical position within the muscle interstitium, their expression of non-specific membrane-associated proteins (particularly PDGFRα and Sca1), and their ability to adopt multiple lineages including fibrogenic, adipogenic, and osteogenic differentiation paths in response to environmental signals[5][15][18]. Studies employing single-cell RNA sequencing and flow cytometry have identified distinct FAP subpopulations based on differential expression of Tie2 and Vcam1, markers that reflect dynamic cellular states during tissue regeneration and disease[18]. The discovery that FAPs can differentiate into osteogenic cells in response to BMP signaling led researchers to investigate the role of mutant ACVR1 in FAPs, revealing that FAPs expressing ACVR1 R206H not only undergo aberrant differentiation into chondro-osteogenic lineages but also create a permissive microenvironment that favors bone formation at the expense of normal muscle regeneration[5][15][18].

A particularly important finding is that FAPs from FOP mice expressing Acvr1 R206H repress the myogenic differentiation of muscle stem cells (MuSCs) in vitro, establishing a critical cell-cell interaction whereby mutant FAPs actively interfere with normal muscle regeneration[15][45]. Under normal conditions, FAPs are necessary for myogenic progression by providing supportive signals to muscle stem cells. However, in FOP, the mutant FAPs lose this supportive function and instead actively suppress MuSC-mediated myotube formation[15][45]. Furthermore, studies revealed that compared to control mice, FOP-injured muscles show significantly decreased apoptosis of FAPs, meaning these cells persist at higher numbers following injury[15]. This persistence of excess FAPs in injured FOP muscle, combined with their impaired ability to support muscle regeneration and their enhanced propensity to undergo osteogenic differentiation, contributes substantially to heterotopic ossification formation and represents a critical defect in the regenerative program[15].

## Inflammatory Mechanisms and Immune Cell Involvement

The pathophysiology of FOP is fundamentally shaped by dysregulation of innate and adaptive immune responses, with mounting evidence establishing inflammation as both a necessary trigger and a sustained driver of heterotopic ossification[9][12][13][29]. Multiple lines of evidence support a central role for the immune system in FOP pathogenesis. Perivascular accumulation of lymphocytes, mast cells, and macrophages occurs in affected skeletal muscle during the earliest phases of disease flare-ups in both FOP patients and mouse models of FOP[12][13]. Importantly, a unique clinical case study and associated murine bone marrow transplantation experiment established that the innate immune system—specifically cells of hematopoietic origin—is required for disease flare-ups, providing compelling evidence that inflammatory triggers are not merely associated with but are necessary for heterotopic ossification in FOP[12][13]. A patient with FOP who underwent bone marrow transplantation for treatment of unrelated aplastic anemia showed profound changes in his disease course after the transplant, demonstrating that immune cells are critical participants in FOP pathogenesis[12][29].

### Macrophage-Mediated Inflammation

Macrophages represent a key inflammatory cell type driving FOP pathophysiology[9][12]. Studies employing FOP mouse models with ACVR1 R206H mutations show strong presence of macrophages and mast cells at sites of heterotopic ossification formation[9]. Research examining serum from FOP patients and primary monocyte-derived macrophages from FOP individuals has revealed significantly elevated baseline levels of pro-inflammatory cytokines, including interleukin-3 (IL-3), IL-7, and IL-8, even in the absence of overt flare-up symptoms[9]. Furthermore, nuclear factor-kappa B (NF-κB) activation, a key transcription factor driving inflammatory gene expression, has been identified as a key factor for inflammation in FOP[9]. Suppression of transforming growth factor-beta (TGF-β) in FOP mouse models attenuates heterotopic ossification, suggesting that macrophages and their TGF-β production play a critical role in the early phase of inflammation[9]. Researchers using methods to create human induced pluripotent stem cell-derived macrophages (iMACs) from FOP and control individuals demonstrated heightened production of pro-inflammatory cytokines in unstimulated FOP-M1-like iMACs, aligning with observations of a pro-inflammatory state in FOP serum and in primary FOP monocyte-derived macrophages[9]. Notably, FOP-derived macrophages retain a pro-inflammatory phenotype for extended durations after stimulation, compared with control macrophages that rapidly downregulate inflammatory responses[9].

Bone morphogenetic proteins themselves function as potent pro-inflammatory proteins at heterotopic sites[12]. BMP4, in particular, was demonstrated decades ago to be a potent chemoattractant to monocytes in vitro and likely promotes heterotopic ossification through its profound effects on monocyte recruitment and cytokine synthesis[12]. This illustrates an important mechanistic principle in FOP: the same signaling pathways that drive osteogenic differentiation of mesenchymal cells simultaneously activate inflammatory responses in immune cells, creating a pathological amplification loop where bone formation and inflammation mutually reinforce each other.

### Mast Cells and Their Central Role

Mast cells have emerged as critically important immune contributors to FOP pathophysiology[9][12]. Mast cells are innate immune cells known for their involvement in allergic and inflammatory responses, and they release pro-inflammatory mediators including cytokines, chemokines, and mediators like tryptase and heparin in FOP patients[9]. A particularly striking finding comes from studies using conditional knockout mice for FOP (with the ACVR1 R206H mutation) in which selective depletion of mast cells alone reduced heterotopic ossification volume by approximately 50 percent[9]. Even more dramatically, when both mast cells and macrophages were depleted together through administration of clodronate, heterotopic ossification volume was reduced by approximately 75 percent, suggesting that these two cell types are major contributors to heterotopic ossification formation[9]. Studies of FOP patient serum revealed high levels of interleukin 9 (IL-9), a cytokine produced by mast cells, providing additional evidence for the importance of mast cell-mediated inflammation[9].

### Lymphocytic Contributions

Both B and T lymphocytes have been identified as potential contributors to heterotopic ossification development in FOP[9][12]. Perivascular lymphocytic infiltration has been reported in skeletal muscle from FOP patients, notably in a 2-year-old child with FOP that showed this lymphocytic involvement despite otherwise normal muscle histology[9]. The presence of perivascular lymphocytic infiltrates in FOP lesions suggests that lymphocytes play active roles in the inflammatory process, though the specific mechanisms by which lymphocytes contribute to heterotopic ossification remain incompletely characterized[9]. Together, the evidence for macrophages, mast cells, and lymphocytes indicates that a complex inflammatory response involving multiple immune cell types are key drivers of FOP heterotopic ossification.

## Hypoxia and HIF-1α-Mediated Amplification of BMP Signaling

The role of cellular hypoxia in amplifying heterotopic ossification in FOP represents another fundamental aspect of disease pathophysiology[19][22]. Early inflammatory FOP lesions in both humans and mouse models have been found to be profoundly hypoxic—that is, they have substantially reduced oxygen tension—measured through immunohistochemistry for hypoxia markers such as EF5[19]. This hypoxic microenvironment creates a critical condition that dramatically amplifies aberrant BMP signaling through HIF-1α (hypoxia-inducible factor 1-alpha), a transcription factor that integrates the cellular response to both hypoxia and inflammation[19][22].

Mechanistically, hypoxia increases the intensity and duration of canonical bone morphogenetic protein signaling through a process involving Rabaptin 5 (RABEP1)-mediated retention of ACVR1 in the endosomal compartment of hypoxic connective tissue progenitor cells from FOP patients[19]. Under normoxic conditions, ACVR1 and other activated receptor complexes are typically internalized through endocytosis, transported through early endosomes, and subsequently degraded, thereby terminating signaling[19]. However, under hypoxic conditions, HIF-1α downregulates expression of RABEP1, which encodes Rabaptin-5—a protein that normally interacts with Rab5 (a small GTPase crucial for endocytic trafficking) to mediate early endosome fusion[19]. When Rabaptin-5 levels are reduced by HIF-1α-mediated transcriptional repression, early endosomes fail to fuse properly, and ACVR1 becomes retained longer in signaling endosomes, prolonging the duration of phosphorylation of downstream SMAD1/5/8 and p38 MAPK[19]. This represents a profound amplification mechanism: not only is the FOP-ACVR1 mutant receptor hyperactive to begin with, but hypoxic tissue microenvironments selectively amplify and prolong its signaling through a cell-autonomous mechanism that doesn't require any additional ligand stimulation[19].

The critical importance of HIF-1α in FOP pathophysiology has been demonstrated through both genetic and pharmacological approaches[19][22]. Deletion of HIF-1α expression—either genetically through conditional knockout or pharmacologically through inhibitors—significantly reduces heterotopic ossification in constitutively active Acvr1 Q207D/+ mouse models of FOP[19]. Inhibition of HIF-1α by genetic or pharmacologic means restores canonical BMP signaling to normoxic levels in human FOP cells and profoundly reduces heterotopic ossification in mouse models[19]. This has made HIF-1α an important therapeutic target for FOP treatment, with ongoing research examining HIF-1α inhibitors as potential therapeutics[22].

## Crosstalk Between HIF-1α and mTOR Pathways

Emerging research has identified important crosstalk between the HIF-1α and mTOR (mammalian target of rapamycin) signaling pathways in amplifying heterotopic ossification in FOP[22]. HIF-1α activates mTOR signaling through various mechanisms, including upregulation of growth factors and modulation of metabolic pathways[22]. Conversely, mTOR acts upstream of HIF-1α, with activation of mTOR through the Ras homolog pathway enhancing the activity of HIF-1α and vascular endothelial growth factor (VEGF) during hypoxia[22]. Hypoxia exposure increases BMP2 expression in cultured osteoblastic cells in an HIF-dependent manner involving activation of the ILK/Akt/mTOR pathway[22]. This reciprocal interaction between HIF-1α and mTOR creates a positive feedback loop, leading to sustained activation of both pathways, which further promotes osteogenesis and exacerbates the progression of heterotopic ossification[22]. Understanding these pathway interactions has therapeutic implications, as combined targeting of both the HIF-1α and mTOR pathways may provide synergistic effects in suppressing heterotopic ossification compared to targeting either pathway alone.

## Activin A as a Non-Canonical BMP Pathway Ligand

The discovery of Activin A as a pathophysiological driver of heterotopic ossification in FOP represents a paradigm shift in understanding the molecular basis of the disease[24][41]. Activin A is a member of the TGF-β superfamily that normally functions as a potent cytokine regulating immune system function[12][41]. Wild-type ACVR1 does not respond to Activin A in a manner that activates BMP signaling; instead, Activin A typically binds to ACVR1B (ALK4) and signals through the TGF-β/SMAD2/3 pathway[24][41]. However, the FOP-ACVR1 R206H mutation confers a novel capacity for the receptor to bind Activin A and transduce BMP signaling—meaning that Activin A binding to mutant ACVR1 activates SMAD1/5/8 phosphorylation rather than the normal SMAD2/3 pathway[24][41].

This acquired responsiveness to Activin A has profound pathophysiological consequences. In vitro studies demonstrated that Activin A enhanced the chondrogenesis of induced mesenchymal stromal cells derived from FOP-iPSCs (FOP-iMSCs) via aberrant activation of BMP signaling in addition to normal activation of TGF-β signaling[24]. In vivo studies showed that Activin A injection induced endochondral ossification of FOP-iMSCs, providing definitive evidence that Activin A can trigger heterotopic ossification[24]. In a conditional Acvr1 R206H knock-in mouse model, heterotopic ossification was induced by Activin A injection and was completely abrogated by antibodies against Activin A, indicating that this ligand is sufficient to drive heterotopic ossification in FOP[41][44]. When mutant mice were treated with blocking antibodies directed against Activin A, they did not develop heterotopic bone either spontaneously or in response to localized injury to muscles or tendons[41]. These results indicate that Activin A is an obligatory secreted factor required for at least the initiation of heterotopic ossification in FOP, making anti-Activin A monoclonal antibodies (REGN2477) a promising therapeutic strategy[41].

## Hedgehog Signaling and Yap-Mediated Ectopic Bone Expansion

Recent research has revealed that Hedgehog (Hh) signaling, particularly through the Indian hedgehog (Ihh) ligand, plays a critical role in governing ectopic bone formation and expansion in FOP[27]. Using conditional knock-in FOP mouse models expressing Acvr1 R206H from the endogenous Acvr1 locus, researchers identified Hh signaling activation and Yap (yes-associated protein) upregulation in chondrogenic lesions and ectopic bone regions[27]. Both Hh signaling and Yap activation are required for the aberrant ectopic bone formation in FOP, and notably, Yap and Smad1 (the phosphorylated form activated by BMP signaling) can bind to each other and coordinate to induce chondrogenesis by promoting Ihh expression[27]. Ihh is required for endochondral ossification in FOP, and importantly, Yap activation drives ectopic bone formation and expansion through Ihh expression in both cell-autonomous (direct effects on osteogenic cells) and non-cell-autonomous (effects on surrounding cells) manners[27].

These findings suggest that the Yap-Ihh axis represents an important nodal point where multiple signaling pathways converge to promote heterotopic bone formation. Experimental Ihh inhibition using monoclonal antibodies substantially reduced chondrogenesis and ectopic bone formation in FOP mouse models, demonstrating that blocking Ihh signaling represents a potential therapeutic strategy to prevent and reduce heterotopic ossification[27]. This pathway discovery adds another layer of complexity to FOP pathophysiology, illustrating that heterotopic ossification involves a coordinated network of developmental signaling pathways that are normally tightly regulated but become dysregulated in FOP.

## Transcriptional Regulation and Master Osteogenic Factors

The aberrant differentiation of mesenchymal progenitor cells into osteoblasts and chondrocytes in FOP is driven by altered expression and activity of master transcription factors governing skeletal development[3][5][46]. The transcription factor Runx2 (also called Cbfa1) is the master transcription factor of osteoblast differentiation and is essential for osteogenesis[46]. Runx2 directly binds to osteoblast-specific cis-acting elements (OSE2) present in the promoters of osteoblast-specific genes such as osteocalcin (OC), osteopontin (OPN), bone sialoprotein (BSP), and collagen type I alpha 1 (Col1A1), thereby initiating and regulating the expression of these bone matrix proteins[46]. In FOP cells expressing the ACVR1 R206H mutation, Runx2 expression is constitutively upregulated, and Runx2 phosphorylation by p38 MAPK is enhanced, leading to increased transcriptional activity and accelerated osteogenic differentiation compared to control cells[5][37].

Osterix (OSX), another critical osteogenic transcription factor encoded by the Sp7 gene, works cooperatively with Runx2 to regulate osteoblast differentiation and bone formation[46]. OSX is induced after Runx2 during osteoblast maturation and is essential for the terminal stages of osteoblast differentiation and bone matrix mineralization[46]. In FOP lesions and in cells expressing the ACVR1 R206H mutation, OSX expression is similarly elevated[27][46]. The transcription factors Runx2 and OSX interact physically to form cooperative transcriptional complexes that bind to enhancer regions containing adjacent Sp1 and Runx2 DNA-binding sites, and these protein-protein interactions are mediated by MAPK-dependent phosphorylation of both Runx2 and OSX[43][46]. Thus, the elevated p38 MAPK activity in FOP enhances the cooperative interaction between Runx2 and OSX, promoting osteogenic gene expression[43].

Another important transcription factor in FOP pathophysiology is SOX9 (sex-determining region Y-box 9), which is the master chondrogenic transcription factor essential for chondrocyte differentiation and cartilage formation[54][60]. SOX9 is mandatory for transactivating many cartilage-specific genes and drives embryonic chondrogenesis[54]. In FOP lesions, SOX9 expression is upregulated in developing cartilage regions, and this enhanced chondrogenic differentiation is driven by aberrant BMP signaling through the ACVR1 R206H mutation[3][54][60]. However, it is important to note that SOX9 typically functions to suppress chondrocyte-to-osteoblast transdifferentiation by modulating the TGF-β and BMP signaling pathways—specifically by downregulating BMP antagonists such as Gremlin and Noggin[51]. In FOP, dysregulation of these antagonists means that SOX9's protective function against osteoblastogenesis is compromised, allowing chondrocytes to progress to osteogenic differentiation.

## Disease Progression and Clinical Manifestations

The clinical pathophysiology of FOP manifests through characteristic patterns of disease progression with distinct phases and anatomical distributions[7][8][10]. More than 90 percent of affected individuals present with malformations of the great toes (hallux valgus with potential absence or fusion of the interphalangeal joint) at birth, but otherwise appear normal with normal joint mobility[8][10]. This congenital toe malformation serves as the earliest diagnostic indicator of FOP, though it is not pathognomonic, as other genetic conditions affecting BMP signaling can cause similar toe abnormalities[31]. The heterotopic ossification itself typically begins in the first decade of life, with a majority of cases developing inflammatory painful soft tissue swellings—the characteristic "flare-ups"—during early childhood[8][10].

### Flare-Up Characteristics and Natural History

Large-scale natural history studies have provided detailed documentation of flare-up characteristics in FOP[7]. Among 500 FOP patients or knowledgeable informants surveyed (73 percent response rate), the most common presenting symptoms of flare-ups were swelling (edema in 93 percent of respondents), pain (86 percent), or decreased mobility (79 percent)[7]. New swelling (39 percent) and pain (29 percent) were reported as the most reliable symptoms predictive of a flare-up, and a majority of patients (54.4 percent) were able to confirm a flare-up within 48 hours of symptom onset[7]. Importantly, 71 percent of patients experienced a flare-up within the preceding 12 months, with flare-ups occurring spontaneously in 52 percent of cases and following trauma in 48 percent[7]. For patients aged nine years or older, the mean frequency of flare-ups was approximately two per year, while those younger than nine years experienced a mean frequency of 2.6 flare-ups per year[7].

The duration and resolution of flare-ups varied considerably depending on anatomical location[7]. Most flare-ups resolved within 8 weeks; however, flare-ups of the hips and back tended to last 12 weeks or longer[7]. Seventy percent of patients reported functional loss from a flare-up, though 32 percent reported complete resolution of at least one flare-up and 12 percent experienced flare-ups without any functional loss (mostly in the head or back)[7]. The most disabling flare-ups occurred at the shoulders or hips[7]. These findings indicate that while some flare-ups resolve completely, many result in permanent functional loss as heterotopic bone matures in place.

### Anatomical Progression Pattern

Heterotopic ossification in FOP typically follows a characteristic anatomical progression that is consistent across patients[7][8]. The onset of functional impairment usually occurs first in the neck and upper back, with progression from axial to appendicular regions as the disease advances[7]. The typical progression sequence involves the neck, spine, and shoulders first, followed by elbows, knees, and hips, progressing to wrists and ankles, and potentially involving the jaw[8]. The disease progression also follows a dorsal to ventral pattern—from the back surface of the body toward the front—and a proximal to distal progression within limbs[8]. Appendicular flare-ups occur more frequently at proximal than distal sites without preferential sidedness[7]. As heterotopic ossification accumulates, affected joints gradually become fused (ankylosed), resulting in progressive loss of joint mobility and function. Patients typically become wheelchair-bound by the third decade of life as hip and knee fusion occur[1][8].

### Triggers for Heterotopic Ossification

Fifty percent of flare-ups are caused by trauma, viral infection, intramuscular injections, muscle strain, and excessive fatigue[25]. Muscle injury is a particularly common trigger for heterotopic ossification in FOP—indeed, any trauma to the muscles of an individual with FOP, such as a fall or invasive medical procedures, may trigger episodes of muscle swelling and inflammation (myositis) followed by more rapid ossification in the injured area[28]. Viral illnesses such as influenza are also well-recognized triggers for FOP flare-ups[28]. This has profound clinical implications for FOP patients, who must be extremely cautious about any potential muscle injury and for whom standard clinical interventions such as intramuscular injections are absolutely contraindicated. Even biopsies taken for diagnostic purposes can trigger massive flare-ups and accelerate heterotopic ossification, meaning that if FOP is suspected, any invasive diagnostic procedures must be avoided and diagnosis should be made through genetic testing alone[34].

### Pulmonary and Respiratory Complications

The median age of survival for FOP patients is approximately 40 years, with death occurring primarily due to thoracic insufficiency syndrome and related complications[1][8][34]. As heterotopic ossification involves the thoracic spine, ribs, and thoracic musculature, the capacity of the chest to expand becomes severely restricted, leading to inadequate ventilation and progressive respiratory compromise[1][32]. The thoracic cavity may become insufficient in volume to accommodate normal lung growth and function, and altered thoracic geometry combined with fusion of thoracic joints results in decreased diaphragmatic positioning and reduced force-generating capacity[32]. This progressive restriction of thoracic motion creates chronic hypoventilation, reduced oxygenation, and right-sided heart failure as the heart must work against the increased resistance to pulmonary blood flow[1][8][34]. Additionally, patients with severe FOP are at increased susceptibility to respiratory infections due to compromised ventilation and clearance of secretions, and these infections can trigger further flare-ups, creating a vicious cycle of pulmonary deterioration.

### Additional Clinical Manifestations

Beyond the skeletal manifestations and respiratory complications, FOP affects multiple organ systems. Hearing impairment is observed in approximately 50 percent of FOP patients, likely resulting from heterotopic ossification affecting the auditory ossicles and otic capsule[10][34]. Some individuals develop progressive pain and stiffness in affected areas. Complete fusion of the spine and pain caused by abnormal bony growths compressing nerves (entrapment neuropathies) occur as the disease progresses[10]. Hair loss and mild cognitive delay have been reported in some cases with more severe disease manifestations[10]. The gastrointestinal system can be affected by jaw involvement, where bone formation can severely restrict opening of the jaw (microstomia), compromising the ability to eat and drink adequately[10]. Some patients with severe forms of FOP may develop dermal ossification—progressive thickening and hardening of skin—as the disease extends into dermal and subcutaneous tissues[10].

## Diagnostic Approaches and Genetic Testing

The diagnosis of classic FOP is typically made through clinical evaluation based on the characteristic findings of congenital great toe malformations and the progressive heterotopic ossification pattern[1][34]. Plain radiographs can substantiate toe abnormalities and document the presence of heterotopic ossification[34]. Confirmatory genetic testing through polymerase chain reaction (PCR) analysis and DNA sequencing is available and recommended to definitively establish the diagnosis[1][3][34]. Genetic analysis of the ACVR1 gene detects the characteristic mutations responsible for FOP[1]. Differential diagnosis includes progressive osseous heteroplasia (a condition with somatic ACVR1 mutations), osteosarcoma, lymphedema, soft tissue sarcoma, desmoid tumors, aggressive juvenile fibromatosis, and non-hereditary acquired heterotopic ossification from trauma or surgery[34].

An important clinical principle is that if FOP is suspected based on clinical features, invasive diagnostic procedures such as biopsy should be avoided, as such procedures can trigger massive flare-ups and accelerate heterotopic ossification[1][8][34]. Instead, diagnosis should be confirmed through genetic testing, and clinical management should focus on preventative measures against additional injury.

## Therapeutic Approaches and Emerging Treatments

Recent advances in understanding FOP pathophysiology have enabled the development of several promising therapeutic approaches targeting different aspects of the disease mechanism[38][41]. The retinoid X receptor-gamma (RARγ) agonist **palovarotene** has shown particular promise in clinical trials[38][41]. Palovarotene works by inhibiting chondrogenesis—the differentiation of mesenchymal progenitors into chondrocytes—which is the first major differentiation event in heterotopic ossification development[38][41]. The drug was tested in a Phase 2 clinical trial in 40 FOP patients, with results suggesting that palovarotene decreased the percentage of FOP patients developing heterotopic ossification, reduced the time to flare-up resolution, and decreased patient-reported pain[41]. These results have led to Phase 3 clinical trials in both adults and children[41]. Additionally, palovarotene markedly reduces the number of local Inhba-expressing (Activin A-encoding) heterotopic ossification-forming cell populations, expanding the drug's spectrum of action against heterotopic ossification formation[38].

The anti-Activin A monoclonal antibody **REGN2477** represents another major therapeutic advance based on the discovery of Activin A's role in FOP pathophysiology[41]. As discussed earlier, blocking Activin A prevents both spontaneous and trauma-induced heterotopic ossification in FOP mouse models[41]. An ongoing Phase 2 clinical trial is testing REGN2477 in FOP patients[41].

**Rapamycin** (sirolimus) and related compounds that inhibit the mTOR pathway have shown promise in reducing heterotopic ossification in preclinical models[41]. Given the crosstalk between HIF-1α and mTOR pathways in amplifying BMP signaling, mTOR inhibition represents a potential therapeutic target[22].

**Direct ALK2 kinase inhibitors** including saracatinib represent another therapeutic strategy aimed at directly blocking the aberrant kinase activity of the mutant ACVR1 receptor[41]. Promising preliminary in vitro and in vivo results have been presented with direct ALK2 kinase inhibitors.

## Conclusion

Fibrodysplasia ossificans progressiva represents a striking example of how a single point mutation in a developmental signaling receptor can create a cascade of pathological events transforming normal developmental and regenerative pathways into progressive tissue metamorphosis. The gain-of-function ACVR1 R206H mutation creates a receptor that exhibits both ligand-independent constitutive activity and hypersensitivity to normal BMP ligands, while simultaneously acquiring novel responsiveness to Activin A. This aberrant signaling activates not only canonical SMAD1/5/8 pathways but also multiple non-canonical pathways including p38 MAPK, PI3K/mTOR, and mechanotransduction cascades. The pathophysiology of FOP is inextricably linked to inflammatory responses, with macrophages, mast cells, and lymphocytes creating a pro-inflammatory microenvironment that is both necessary for and amplified by tissue hypoxia and HIF-1α activation. Cellular hypoxia creates a microenvironment in which endosomal retention of mutant ACVR1 is prolonged, dramatically extending the duration of aberrant signaling. Tissue-resident progenitor cells, particularly Tie2+ endothelial precursors and fibro/adipogenic progenitors expressing mutant ACVR1, differentiate through an endochondral ossification pathway to form bone, while simultaneously losing their normal supportive function for muscle regeneration. The coordinated activation of developmental pathways including BMP/SMAD signaling, Hedgehog signaling through Ihh, and Yap-mediated transcriptional control creates a permissive environment for progressive heterotopic ossification. Clinical manifestations follow a characteristic anatomical progression, with patients progressing to wheelchair dependence and respiratory insufficiency as thoracic ossification restricts ventilation. Understanding these molecular and cellular mechanisms has enabled the development of rational therapeutic approaches targeting Activin A signaling, chondrogenic differentiation, and mTOR/HIF-1α pathways, offering hope for improving outcomes in this devastating genetic disease.