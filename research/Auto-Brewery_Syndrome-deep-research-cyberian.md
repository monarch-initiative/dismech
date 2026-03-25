---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-16T20:06:26.686680'
end_time: '2026-01-16T20:22:21.662193'
duration_seconds: 954.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Auto-Brewery Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Auto-Brewery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Auto-Brewery Syndrome**.
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

# Auto-Brewery Syndrome: A Comprehensive Review of Pathophysiology and Molecular Mechanisms

## Introduction

Auto-brewery syndrome (ABS), also known as gut fermentation syndrome or endogenous ethanol fermentation, represents a rare and often underdiagnosed medical condition in which intoxicating quantities of ethanol are produced through endogenous fermentation of carbohydrates within the gastrointestinal tract, oral cavity, or urinary system[paramsothy-2023-abs-review-abstract]. Patients with this condition present with signs and symptoms of alcohol intoxication despite denying alcohol consumption, creating significant clinical, social, and legal challenges[dinis-oliveira-2021-metabolic-storm-abstract]. The syndrome was first documented in 1948 with a case describing fatal gastric rupture in a five-year-old African child, and Japanese literature documented instances under the term "Meitei-sho" during the 1970s[dinis-oliveira-2021-metabolic-storm-abstract].

The pathophysiology of ABS involves a "perfect metabolic storm" whereby gut dysbiosis—particularly fungal or bacterial overgrowth—combined with high carbohydrate intake and potentially impaired hepatic ethanol metabolism results in accumulation of endogenous ethanol to levels that produce clinical intoxication[dinis-oliveira-2021-metabolic-storm-summary]. While historically attributed primarily to fungal organisms, particularly Candida and Saccharomyces species, recent research has identified bacterial causes including high-alcohol-producing Klebsiella pneumoniae strains, expanding our understanding of this complex syndrome[zhu-2023-klebsiella-abs-abstract]. This review synthesizes current knowledge on the molecular mechanisms, genetic factors, clinical manifestations, and therapeutic approaches relevant to ABS.

## Etiology and Causative Organisms

The causative organisms in auto-brewery syndrome span both fungal and bacterial kingdoms, reflecting the diverse microorganisms capable of fermenting carbohydrates to ethanol within the human gastrointestinal tract. A systematic review by Bayoumy and colleagues analyzing 17 case reports covering 20 patients found that the microorganisms identified were usually from the Saccharomyces and Candida genera[bayoumy-2021-gfs-systematic-review-abstract]. The complete spectrum of identified causative organisms includes the yeasts Saccharomyces cerevisiae (brewer's yeast, the most commonly implicated organism), Saccharomyces boulardii (notably a probiotic yeast), Candida albicans, Candida tropicalis, Candida krusei, Candida glabrata, Candida kefyr, Candida parapsilosis, and Kluyveromyces marxianus[paramsothy-2023-abs-review-abstract][dinis-oliveira-2021-metabolic-storm-abstract].

The bacterial causes of ABS have gained increasing recognition following landmark work by Yuan and colleagues demonstrating that high-alcohol-producing Klebsiella pneumoniae (HiAlc Kpn) is associated with up to 60% of individuals with non-alcoholic fatty liver disease (NAFLD) in Chinese cohorts[yuan-2019-klebsiella-nafld-abstract]. Subsequent research by Zhu and colleagues identified three Klebsiella species—K. pneumoniae, K. quasipneumoniae, and K. variicola—as potential pathobionts capable of generating endogenous ethanol in ABS patients, with alcohol concentrations reaching 300-400 mg/dL during episodes, equivalent to approximately 15 shots of 40% whisky[zhu-2023-klebsiella-abs-abstract]. Additional bacterial organisms implicated in individual cases include Enterococcus faecium, Enterococcus faecalis, and Citrobacter freundii[dinis-oliveira-2021-metabolic-storm-abstract].

Most yeasts possess the capability to ferment sugars anaerobically, but species such as Candida glabrata and Saccharomyces cerevisiae exhibit an additional adaptation known as the Crabtree effect, enabling them to ferment sugars even in the presence of oxygen[dinis-oliveira-2021-metabolic-storm-summary]. This evolutionary adaptation allows these organisms to suppress the growth of competing microorganisms and may explain why pathological fermentation can occur even in the relatively aerobic environment of the upper gastrointestinal tract.

## Molecular Mechanisms of Ethanol Production

### Fungal Fermentation Pathway

The primary mechanism of ethanol production in fungal ABS involves the classical alcoholic fermentation pathway. Glucose is transported into microbial cells via hexose transporters, then metabolized through glycolysis to pyruvate[dinis-oliveira-2021-metabolic-storm-abstract]. Under anaerobic or microaerobic conditions, pyruvate undergoes decarboxylation to acetaldehyde, a reaction catalyzed by pyruvate decarboxylase (PDC), a thiamine pyrophosphate-dependent enzyme. In Saccharomyces cerevisiae, this enzyme is encoded by three genes—PDC1, PDC5, and PDC6—with Pdc1p and Pdc5p being the primary active isoforms during fermentation. The acetaldehyde is then reduced to ethanol by alcohol dehydrogenase (ADH), regenerating NAD+ in the process to sustain continued glycolysis.

In Candida albicans, alcohol dehydrogenase I encoded by the ADH1 gene serves as a key enzyme catalyzing the conversion of acetaldehyde to ethanol. Research has demonstrated that ADH1 promotes C. albicans pathogenicity through effects on oxidative phosphorylation, and deletion of ADH1 significantly affects mitochondrial membrane potential and intracellular ATP content. Interestingly, transcriptional regulators Gal4p and Tye7p have been shown to bind to and activate genes involved in fermenting pyruvate to ethanol, including PDC11, ADH1, and NDE1, indicating coordinated regulation of the entire fermentation pathway from glucose to ethanol.

### Bacterial Fermentation Pathway: The 2,3-Butanediol Route

Bacterial ABS, particularly that caused by Klebsiella species, employs a distinct metabolic pathway centered on the 2,3-butanediol fermentation system. Research by Li and colleagues demonstrated that carbohydrate substances are catabolized to produce both alcohol and 2,3-butanediol via this pathway, with ethanol arising as a byproduct[li-2021-klebsiella-23butanediol-abstract]. The pathway involves three critical enzymatic steps: first, alpha-acetolactate synthase (encoded by budB) catalyzes the condensation of two pyruvate molecules to form alpha-acetolactate with CO2 release; second, alpha-acetolactate decarboxylase (encoded by budA) converts alpha-acetolactate to acetoin; and third, 2,3-butanediol dehydrogenase (encoded by budC), also known as acetoin reductase, reduces acetoin to 2,3-butanediol.

Genomic analysis of HiAlc Kpn strains W14 and TH1 revealed that these organisms possess 12 copies of alcohol dehydrogenase (ADH) genes, significantly exceeding standard strains, enabling ethanol production up to 83.7 mmol/L under aerobic conditions[li-2021-klebsiella-23butanediol-abstract]. Proteomic analysis demonstrated that 10 proteins and six major metabolites involved in the 2,3-butanediol fermentation pathway exhibited at least a three-fold change in HiAlc strains. Importantly, this pathway operates under both aerobic and anaerobic conditions, though aerobic conditions yield higher alcohol production, explaining why gut fermentation can occur throughout the gastrointestinal tract.

Validation of this pathway was achieved through experiments with triazolopyrimidine, an inhibitor of alpha-acetolactate synthetase, which reduced alcohol production to below 10 mg/mL with IC50 values of 42.6-43.7 µM[li-2021-klebsiella-23butanediol-abstract]. Additionally, construction of ADH gene knockout mutants (W14-Δadh) demonstrated minimal pathological changes compared to wild-type strains, confirming the essential role of alcohol dehydrogenase in the disease process.

## Host Genetic Factors in Ethanol Metabolism

The severity and clinical presentation of ABS may be significantly influenced by host genetic factors affecting ethanol metabolism. The primary pathway of ethanol clearance involves two enzymatic steps: oxidation of ethanol to acetaldehyde by alcohol dehydrogenase (ADH), followed by oxidation of acetaldehyde to acetate by aldehyde dehydrogenase (ALDH)[edenberg-2007-adh-aldh-genetics-abstract]. Polymorphisms in genes encoding these enzymes can substantially alter the kinetics of ethanol and acetaldehyde metabolism.

Humans possess seven ADH genes (ADH1A, ADH1B, ADH1C, ADH4, ADH5, ADH6, ADH7) clustered on chromosome 4, with Class I enzymes (encoded by ADH1A, ADH1B, and ADH1C) accounting for approximately 70% of hepatic ethanol-oxidizing capacity[edenberg-2007-adh-aldh-genetics-abstract]. The ADH1B*2 allele, common in East Asian populations, encodes an enzyme with 70-80 fold higher turnover compared to the reference allele, resulting in more rapid conversion of ethanol to acetaldehyde. The ADH1B*3 allele, found primarily in African populations, also demonstrates enhanced activity.

The mitochondrial aldehyde dehydrogenase ALDH2, encoded on chromosome 12, plays the predominant role in acetaldehyde clearance. The ALDH2*2 variant, resulting from a lysine substitution at position 504, produces an essentially inactive enzyme with nearly dominant inheritance in heterozygotes[edenberg-2007-adh-aldh-genetics-abstract]. This variant is essentially only found in Asian populations, with approximately 50% of East Asians lacking functional ALDH2 activity. Individuals with ALDH2*2 accumulate acetaldehyde, leading to the characteristic "Asian flush" reaction characterized by facial flushing, nausea, and tachycardia—effects that parallel disulfiram (Antabuse) administration.

In the context of ABS, individuals with genetic polymorphisms of ADH and ALDH may find it more difficult to metabolize endogenous ethanol, potentially worsening intoxication symptoms[paramsothy-2023-abs-review-abstract]. Those with highly active ADH variants may rapidly generate acetaldehyde but, if they also carry ALDH2*2, cannot efficiently clear this toxic intermediate. Conversely, individuals with less active ADH variants may have prolonged ethanol half-life, allowing greater accumulation from even modest endogenous production rates. These genetic considerations underscore the importance of personalized assessment in ABS management.

## Predisposing Conditions and Risk Factors

Auto-brewery syndrome develops through a confluence of factors that create the "perfect metabolic storm"—intestinal dysbiosis, substrate availability, and impaired clearance mechanisms[dinis-oliveira-2021-metabolic-storm-summary]. The condition is more prevalent in patients with comorbidities including diabetes mellitus, obesity, liver cirrhosis, Crohn's disease, and short bowel syndrome, though it can occur in otherwise healthy individuals[paramsothy-2023-abs-review-abstract].

Antibiotic exposure represents a critical precipitating factor, with five of 17 case reports in the systematic review by Bayoumy describing recent antibiotic use before or at onset of symptoms[bayoumy-2021-gfs-systematic-review-abstract]. Antibiotics disrupt the protective commensal microbiota, potentially allowing colonization and overgrowth of alcohol-producing species. The case reported by Spinucci and colleagues elegantly demonstrated this mechanism: a patient with chronic intestinal pseudo-obstruction developed ABS specifically following amoxicillin-clavulanic acid treatment combined with a simple sugar-rich diet, with blood ethanol disappearing within 24 hours of discontinuing both factors and reappearing upon rechallenge[spinucci-2006-pseudoobstruction-abstract].

Gastrointestinal anatomical abnormalities predispose to ABS by creating conditions favoring microbial stagnation and overgrowth. These include short bowel syndrome resulting from surgical resection, chronic intestinal pseudo-obstruction, gastric bypass and other bariatric procedures, and any condition causing intestinal dysmotility. In short bowel syndrome, the reduced absorptive capacity means that undigested carbohydrates reach the colon in excessive quantities, providing abundant substrate for fermentation. A case of a 3-year-old girl with short bowel syndrome documented by Jansson-Nettelbladt demonstrated blood ethanol concentrations of 15 mmol/L associated with introduction of a carbohydrate-rich fruit drink, leading the authors to recommend adding ABS to the differential diagnosis for D-lactic acidosis in SBS patients[jansson-nettelbladt-2006-sbs-child-abstract].

Hepatic dysfunction impairs the first-pass metabolism that normally clears endogenous ethanol before it reaches systemic circulation. The liver efficiently clears ethanol through ADH-mediated oxidation following Michaelis-Menten kinetics with a Km of 0.05-0.10 g/L, but this protective mechanism fails when ethanol production exceeds hepatic clearance capacity or when hepatic function is compromised[dinis-oliveira-2021-metabolic-storm-summary]. Studies by Hafez and colleagues confirmed that blood ethanol levels were significantly higher in patients with liver cirrhosis and diabetes mellitus compared to healthy controls after 12-hour fasting, suggesting differential susceptibility to endogenous ethanol accumulation[hafez-2017-endogenous-ethanol-abstract].

## Disease Progression: From Initial Trigger to Clinical Manifestation

The development of auto-brewery syndrome follows a characteristic sequence of pathophysiological events that can be conceptualized as distinct phases progressing from predisposition to full clinical manifestation. Recent literature from Stamation (2025) identifies multiple interconnected mechanisms including gut dysbiosis, impaired intestinal barrier function, and dysregulation of the hypothalamic-pituitary-adrenal axis that collectively contribute to disease development[stamation-2025-alimentary-tract-ethanol-abstract].

The initial phase involves disruption of the normal gut microbiome, most commonly triggered by antibiotic exposure, which eliminates protective commensal bacteria and creates ecological niches for opportunistic colonization by fermentative organisms. This antibiotic-induced dysbiosis reduces colonization resistance, the phenomenon whereby resident microbiota prevent establishment of pathogenic organisms through nutrient competition, production of antimicrobial metabolites, and maintenance of intestinal immune homeostasis. Short-chain fatty acids (SCFAs) produced by gut bacterial fermentation have been found to inhibit the growth of Candida albicans through stimulation of intestinal mucosal immunity, and their depletion following antibiotic exposure facilitates fungal overgrowth.

The second phase involves establishment and proliferation of ethanol-producing microorganisms. Yeasts such as Saccharomyces cerevisiae and Candida species, or bacteria such as Klebsiella pneumoniae, colonize the intestinal lumen and begin metabolizing available carbohydrates. The Crabtree effect exhibited by certain yeasts allows them to perform alcoholic fermentation even in the presence of oxygen, conferring competitive advantage by producing ethanol that suppresses growth of competing microorganisms[tamama-2024-bladder-gut-fermentation-abstract]. This phase may be asymptomatic if ethanol production remains below hepatic clearance capacity.

The third phase represents the transition to clinical disease, occurring when endogenous ethanol production exceeds the liver's first-pass metabolic capacity. This tipping point may be reached through increased microbial burden, consumption of carbohydrate-rich meals providing abundant fermentation substrate, or compromise of hepatic function due to underlying liver disease. Once ethanol enters systemic circulation in quantities sufficient to produce detectable blood alcohol concentrations, the characteristic neurological, gastrointestinal, and behavioral symptoms manifest.

The fourth phase involves chronic exposure consequences if the condition remains undiagnosed or inadequately treated. Persistent endogenous ethanol production can lead to hepatic steatosis progressing to steatohepatitis, particularly when ethanol reaches the liver directly through the portal circulation[yuan-2019-klebsiella-nafld-abstract]. Furthermore, coupled with microbiota dysbiosis and oxidative stress, endogenous alcohol may contribute to lipid oxidation and fibrosis in liver disease. As hepatic function decreases, the liver's ability to metabolize ethanol also decreases, potentially creating a positive feedback loop that exacerbates the condition. Long-term exposure may also result in cravings for and addiction to alcohol, with subsequent development of alcohol use disorder.

A novel trigger recently identified in the literature is viral infection, specifically COVID-19. A 2024 case report documented development of ABS approximately one month following recovery from SARS-CoV-2 infection, with the authors hypothesizing that the virus altered gut microbiome composition to favor fermentation-capable organisms[COVID19-abs-2024-abstract]. This represents an emerging area requiring further investigation as post-viral dysbiosis becomes increasingly recognized.

## Clinical Manifestations and Phenotypic Spectrum

The clinical presentation of auto-brewery syndrome encompasses neurological, gastrointestinal, psychological, and systemic manifestations that can profoundly impact patients' quality of life and social functioning. The neurological symptoms dominate the clinical picture and directly mirror those of exogenous alcohol intoxication: memory loss, mental status changes, recurrent seizures, slurred speech, incoherent speech, blurred vision, dizziness, disorientation, and ataxia with poor coordination leading to falls[paramsothy-2023-abs-review-abstract][dinis-oliveira-2021-metabolic-storm-abstract].

In the systematic review by Bayoumy and colleagues, the most common presenting symptoms included slurred speech (5 of 20 patients, 25%), walking difficulties (5 patients, 25%), intoxication without alcohol consumption (7 patients, 35%), fruity breath odor (3 patients, 15%), and seizures (2 patients, 10%)[bayoumy-2021-gfs-systematic-review-abstract]. The gastrointestinal manifestations include bloating, belching, nausea, vomiting, diarrhea, generalized abdominal discomfort, and symptoms consistent with irritable bowel syndrome[dinis-oliveira-2021-metabolic-storm-abstract]. Psychological and behavioral symptoms encompass depression, bizarre behavior, somnolence, disorientation, fatigue, and aggression.

The blood alcohol concentrations achieved in ABS can be remarkably high. One documented case registered an ethanol concentration greater than 400 mg/dL following carbohydrate consumption, and the Klebsiella-associated cases described by Zhu reached 300-400 mg/dL during episodes[zhu-2023-klebsiella-abs-abstract]. These levels contrast sharply with normal endogenous ethanol production, which ranges from 0 to 0.0008 g/L with median levels of approximately 0.00113 g/L in healthy individuals[dinis-oliveira-2021-metabolic-storm-abstract]. Mouse model experiments confirmed that portal vein blood ethanol concentrations in animals colonized with HiAlc Klebsiella were two times higher than peripheral blood, confirming gut microbial production[li-2021-klebsiella-23butanediol-abstract].

Long-term consequences of untreated ABS can include hepatic steatosis progressing to steatohepatitis, particularly in cases caused by HiAlc Klebsiella where the endogenous ethanol directly reaches the liver through the portal circulation[yuan-2019-klebsiella-nafld-abstract]. Furthermore, chronic exposure to endogenous ethanol may result in cravings for and addiction to alcohol, with subsequent development of alcohol use disorder during or after treatment[dinis-oliveira-2021-metabolic-storm-abstract].

## Diagnostic Approach

Diagnosis of auto-brewery syndrome requires a high index of clinical suspicion combined with systematic evaluation to confirm endogenous ethanol production and exclude alternative explanations. The diagnostic workup begins with comprehensive history-taking, including detailed dietary habits, alcohol consumption patterns (with corroboration from family members), gastrointestinal symptoms, antibiotic exposure, and episodes of unexplained intoxication[paramsothy-2023-abs-review-abstract]. Physical examination assesses for signs of intoxication including alcohol-scented breath, glassy eyes, ataxia, and altered mental status.

Laboratory evaluation includes complete blood count, comprehensive metabolic panel, blood alcohol concentration, drug screening, and stool cultures for both bacterial and fungal organisms. Upper and lower endoscopy with collection of intestinal secretions from the stomach, small intestine, and cecum for culture helps identify the causative organism and guide antifungal or antibiotic therapy selection[malik-2019-abs-case-report-abstract].

The carbohydrate challenge test represents the definitive diagnostic procedure. The protocol involves patient preparation with 48-hour alcohol abstinence and 8-hour fasting, followed by baseline blood alcohol measurement[paramsothy-2023-abs-review-abstract]. The patient then receives 100-200 grams of oral glucose, with blood alcohol concentration and breath alcohol concentration measured at intervals of 0, 0.5, 1, 2, 4, 8, 16, and 24 hours[dinis-oliveira-2021-metabolic-storm-abstract]. Significant elevation of blood alcohol in the absence of exogenous alcohol consumption confirms the diagnosis. This testing should be conducted under observation to exclude covert alcohol consumption.

Differential diagnoses that must be excluded include irritable bowel syndrome, small intestinal bacterial overgrowth, hepatic encephalopathy, alcohol use disorder, psychiatric disorders, and importantly in short bowel syndrome patients, D-lactic acidosis[paramsothy-2023-abs-review-abstract][kowlgi-2015-dlactic-acidosis-abstract]. D-lactic acidosis shares the clinical presentation of encephalopathy, slurred speech, and ataxia with ABS, but is distinguished by the presence of metabolic acidosis and elevated D-lactate levels rather than elevated ethanol.

## Therapeutic Management

Treatment of auto-brewery syndrome requires a multifaceted approach combining dietary modification, antimicrobial therapy, microbiome restoration, and long-term maintenance strategies. Dietary modification forms the foundation of management: low-carbohydrate and sugar-restricted diets are essential for reducing fermentable substrates available to pathogenic microorganisms[paramsothy-2023-abs-review-abstract]. Recommendations include high-protein diets emphasizing quality meats, eggs, almonds, oats, cheese, Greek yogurt, and low-starch vegetables, with initial complete carbohydrate elimination for approximately 6 weeks before gradual reintroduction under nutritionist guidance[dinis-oliveira-2021-metabolic-storm-abstract].

Pharmacological management targets eradication of the causative organisms. For fungal ABS, fluconazole 100-150 mg daily for 14 days represents first-line therapy[paramsothy-2023-abs-review-abstract]. Second-line options include nystatin 500,000 IU three times daily for 10 days, which can be combined with fluconazole when resistance is suspected. For refractory cases, intravenous micafungin 150 mg for 6 weeks has been used successfully. Selection among antifungal classes—azoles, polyenes, and echinocandins—should be guided by culture and sensitivity results from endoscopic specimens[malik-2019-abs-case-report-abstract].

For bacterial ABS, particularly that caused by Klebsiella species, appropriate antibiotic therapy guided by sensitivity testing is indicated. Zhu and colleagues successfully treated a patient with HiAlc Klebsiella-associated ABS using levofloxacin combined with amino acid and vitamin C supplementation, achieving symptom-free status maintained during one-year follow-up[zhu-2023-klebsiella-abs-abstract].

Probiotic therapy aims to restore healthy gut microbiome composition and provide competitive inhibition of pathogenic organisms. Lactobacillus acidophilus (3 billion colony-forming units) used concurrently with antifungals has shown benefit, with multi-strain probiotic supplements recommended for long-term maintenance, sometimes continued for up to 1.5 years[paramsothy-2023-abs-review-abstract]. For bacterial ABS, complex probiotic preparations containing Lactobacillus species and Clostridium butyricum have demonstrated efficacy[zhu-2023-klebsiella-abs-abstract].

Fecal microbiota transplantation (FMT) has emerged as a promising option for refractory cases. One documented case demonstrated that a 47-year-old man treated with FMT for ABS remained symptom-free for 36 months[paramsothy-2023-abs-review-abstract]. The procedure aims to restore normal gut microbiome composition and diversity, displacing pathogenic fermentative organisms, though more research is needed to establish standardized protocols and long-term safety profiles.

## Bladder Fermentation Syndrome: A Related But Distinct Entity

Bladder fermentation syndrome (BFS), also termed urinary auto-brewery syndrome, represents a recently recognized related condition in which ethanol is produced within the urinary bladder rather than the gastrointestinal tract. The first experimentally-proven case was reported in 2020 by Kruckenberg and colleagues, describing a patient with poorly controlled diabetes who failed alcohol abstinence monitoring during liver transplant evaluation despite consistent denial of alcohol consumption[tamama-2024-bladder-gut-fermentation-abstract].

The pathophysiology of BFS differs fundamentally from gut fermentation syndrome in several respects. BFS requires three prerequisite conditions: hyperglycosuria providing glucose substrate, colonization by Crabtree-positive yeast (predominantly Candida glabrata), and the presence of oxygen in the bladder lumen (typically 4-40 mmHg). Notably, C. glabrata is phylogenetically closer to Saccharomyces cerevisiae than to Candida albicans, and like brewer's yeast, it exhibits the Crabtree effect—the ability to perform alcoholic fermentation even in the presence of adequate oxygen[tamama-2024-bladder-gut-fermentation-abstract]. This distinguishes it from other common urinary Candida species (C. albicans, C. tropicalis), which are Crabtree-negative and therefore unlikely to cause bladder fermentation.

A crucial distinguishing feature of BFS is the absence of systemic intoxication. The transitional epithelium lining the urinary bladder provides an effective barrier to ethanol absorption, in contrast to the highly permeable columnar epithelium of the intestine. Thus, while patients with BFS produce ethanol detectable in urine, they do not experience the neurological or behavioral symptoms characteristic of gut fermentation syndrome. This has profound implications for alcohol abstinence monitoring, as patients may repeatedly test positive for urinary ethanol without any clinical intoxication, leading to misdiagnosis as alcohol use disorder and potential disqualification from organ transplantation.

Diagnosis of BFS involves demonstrating positive urinary glucose and ethanol, negative serum ethanol metabolites (ethyl glucuronide, ethyl sulfate), and presence of yeast in urinalysis. A simplified diagnostic approach involves incubating a fresh urine sample at 37°C and demonstrating additional ethanol production over time. Treatment requires a two-pronged approach: optimizing glycemic control to reduce hyperglycosuria, and antifungal therapy. Importantly, SGLT2 inhibitors, increasingly used in diabetes management, may paradoxically worsen BFS by increasing urinary glucose excretion[tamama-2024-bladder-gut-fermentation-abstract].

Beyond diagnostic implications, BFS carries potential health consequences. Acetaldehyde, produced as an intermediate in the fermentation pathway, is a known carcinogen, raising concerns about increased bladder cancer risk in patients with chronic BFS. This represents an important area for future epidemiological investigation.

## Ontology-Based Disease Annotation

### Gene/Protein Annotations (HGNC)

The following genes are relevant to auto-brewery syndrome pathophysiology:

**Host Genes:**
- ADH1A, ADH1B, ADH1C, ADH4, ADH5, ADH6, ADH7 (HGNC:249-255) - Alcohol dehydrogenase family encoding enzymes catalyzing ethanol to acetaldehyde conversion
- ALDH2 (HGNC:404) - Aldehyde dehydrogenase 2, mitochondrial; catalyzes acetaldehyde to acetate conversion
- ALDH1A1 (HGNC:402) - Aldehyde dehydrogenase 1A1, cytosolic; secondary acetaldehyde metabolism

**Microbial Genes (Saccharomyces cerevisiae):**
- PDC1, PDC5, PDC6 - Pyruvate decarboxylase isoforms
- ADH1-ADH5 - Yeast alcohol dehydrogenase genes

**Microbial Genes (Klebsiella pneumoniae):**
- budB - Alpha-acetolactate synthase
- budA - Alpha-acetolactate decarboxylase
- budC - 2,3-butanediol dehydrogenase (acetoin reductase)
- ADH genes (multiple copies in HiAlc strains)

### Biological Processes (GO Terms)

- GO:0006066 - Alcohol metabolic process
- GO:0006067 - Ethanol metabolic process
- GO:0006069 - Ethanol oxidation
- GO:0006113 - Fermentation
- GO:0019655 - Glucose fermentation to ethanol
- GO:0046165 - Alcohol biosynthetic process
- GO:0006006 - Glucose metabolic process
- GO:0006096 - Glycolytic process
- GO:0006090 - Pyruvate metabolic process
- GO:0009408 - Response to ethanol
- GO:0010035 - Response to inorganic substance (response to acetaldehyde)
- GO:0006805 - Xenobiotic metabolic process

### Cellular Components (GO Terms)

- GO:0005829 - Cytosol (location of glycolysis and fermentation enzymes)
- GO:0005739 - Mitochondrion (location of ALDH2)
- GO:0005783 - Endoplasmic reticulum (CYP2E1 ethanol oxidation)
- GO:0005886 - Plasma membrane (hexose transporters)

### Phenotype Associations (HP Terms)

**Neurological Phenotypes:**
- HP:0001250 - Seizures
- HP:0001260 - Dysarthria (slurred speech)
- HP:0002066 - Gait ataxia
- HP:0001288 - Gait disturbance
- HP:0000738 - Hallucinations
- HP:0001289 - Confusion
- HP:0002354 - Memory impairment
- HP:0000739 - Anxiety
- HP:0000716 - Depression
- HP:0001259 - Coma

**Gastrointestinal Phenotypes:**
- HP:0002013 - Vomiting
- HP:0002014 - Diarrhea
- HP:0002017 - Nausea
- HP:0003270 - Abdominal distension (bloating)
- HP:0002020 - Gastroesophageal reflux
- HP:0012378 - Fatigue

**Metabolic Phenotypes:**
- HP:0003076 - Glycosuria (in diabetic comorbidity)
- HP:0001397 - Hepatic steatosis

### Cell Type Involvement (CL Terms)

- CL:0000182 - Hepatocyte (ethanol first-pass metabolism)
- CL:0000066 - Epithelial cell (intestinal epithelium)
- CL:0002503 - Enterocyte of small intestine
- CL:0002505 - Enterocyte of large intestine (colonocyte)
- CL:0000763 - Myeloid cell (immune response to dysbiosis)

### Anatomical Locations (UBERON Terms)

- UBERON:0000160 - Intestine
- UBERON:0002108 - Small intestine
- UBERON:0001155 - Colon
- UBERON:0001153 - Cecum
- UBERON:0000945 - Stomach
- UBERON:0002107 - Liver
- UBERON:0001264 - Pancreas (diabetes association)
- UBERON:0002048 - Lung (respiratory symptoms)
- UBERON:0000955 - Brain (neurological manifestations)
- UBERON:0002037 - Cerebellum (ataxia)
- UBERON:0001255 - Urinary bladder (bladder fermentation syndrome)

### Chemical Entities (CHEBI Terms)

**Primary Metabolites:**
- CHEBI:16236 - Ethanol
- CHEBI:15343 - Acetaldehyde
- CHEBI:30089 - Acetate

**Pathway Intermediates:**
- CHEBI:15361 - Pyruvate
- CHEBI:17234 - Glucose
- CHEBI:16108 - 2,3-Butanediol
- CHEBI:15688 - Acetoin
- CHEBI:16015 - Alpha-acetolactate

**Cofactors:**
- CHEBI:15846 - NAD+
- CHEBI:16908 - NADH
- CHEBI:9532 - Thiamine pyrophosphate (TPP)
- CHEBI:18420 - Mg2+

**Therapeutic Agents:**
- CHEBI:46081 - Fluconazole
- CHEBI:7660 - Nystatin
- CHEBI:600636 - Micafungin
- CHEBI:4911 - Itraconazole

## Open Questions

Several significant gaps remain in our understanding of auto-brewery syndrome that warrant further investigation:

1. **True Prevalence:** The actual prevalence of ABS remains unknown due to absence of standardized diagnostic criteria and likely significant underdiagnosis. Population-based studies using validated diagnostic protocols are needed to establish the true burden of this condition.

2. **Microbiome Determinants:** What specific microbiome configurations predispose to pathological fermentation? Research is needed to identify microbial signatures predictive of ABS risk and to understand why only some individuals with dysbiosis develop symptomatic ethanol production.

3. **Genetic Susceptibility:** While ADH and ALDH polymorphisms affect ethanol metabolism, their specific contribution to ABS susceptibility and severity has not been systematically studied. Genome-wide association studies in ABS cohorts could identify additional genetic risk factors.

4. **Fermentation Site Localization:** Current understanding suggests fermentation occurs primarily in the small intestine and cecum, but the precise anatomical localization may vary by causative organism. Non-invasive imaging or biomarker approaches to localize fermentation would improve therapeutic targeting.

5. **Bacterial vs. Fungal Pathophysiology:** The relative contributions of bacterial and fungal organisms to the overall ABS burden remain unclear. The discovery of HiAlc Klebsiella species raises questions about whether bacterial causes have been historically underrecognized.

6. **Long-term Hepatic Consequences:** The connection between ABS and NAFLD/NASH progression requires longitudinal study. Does chronic subclinical endogenous ethanol production contribute to metabolic liver disease in the broader population?

7. **Optimal Treatment Duration:** Current treatment protocols are empirically derived from case reports. Randomized controlled trials are needed to establish optimal antifungal/antibiotic duration, dietary restriction duration, and probiotic supplementation regimens.

8. **FMT Standardization:** Fecal microbiota transplantation shows promise for refractory cases, but optimal donor selection, preparation methods, and delivery routes remain undefined for this indication.

9. **Pediatric Considerations:** ABS in children with predisposing conditions (short bowel syndrome, congenital intestinal abnormalities) may have distinct features requiring age-specific diagnostic and therapeutic approaches.

10. **Medicolegal Framework:** The forensic and legal implications of ABS require clearer guidelines for courts evaluating claims of endogenous intoxication in DUI and related cases.

## References

1. **paramsothy-2023-abs-review** - Paramsothy J, Gutlapalli SD, et al. Understanding Auto-Brewery Syndrome in 2023: A Clinical and Comprehensive Review of a Rare Medical Condition. Cureus. 2023;15(4):e37678. PMID: 37206535. PMCID: PMC10189828. DOI: 10.7759/cureus.37678. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10189828/

2. **bayoumy-2021-gfs-systematic-review** - Bayoumy AB, Mulder I, Nauta A, Touw DJ, Mulder CJJ. Gut Fermentation Syndrome: A Systematic Review of Case Reports. United European Gastroenterology Journal. 2021;9(3):332-342. PMID: 33887125. PMCID: PMC8259373. DOI: 10.1002/ueg2.12062. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8259373/

3. **dinis-oliveira-2021-metabolic-storm** - Dinis-Oliveira RJ. The Auto-Brewery Syndrome: A Perfect Metabolic "Storm" with Clinical and Forensic Implications. Journal of Clinical Medicine. 2021;10(20):4637. PMID: 34682761. PMCID: PMC8537665. DOI: 10.3390/jcm10204637. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8537665/

4. **malik-2019-abs-case-report** - Malik F, Wickremesinghe P, Saverimuttu J. Case Report and Literature Review of Auto-Brewery Syndrome: Probably an Underdiagnosed Medical Condition. BMJ Open Gastroenterology. 2019;6(1):e000325. PMID: 31423320. PMCID: PMC6688699. DOI: 10.1136/bmjgast-2019-000325. URL: https://pubmed.ncbi.nlm.nih.gov/31423320/

5. **yuan-2019-klebsiella-nafld** - Yuan J, Chen C, Cui J, et al. Fatty Liver Disease Caused by High-Alcohol-Producing Klebsiella pneumoniae. Cell Metabolism. 2019;30(4):675-688.e7. PMID: 31543403. DOI: 10.1016/j.cmet.2019.08.018. URL: https://pubmed.ncbi.nlm.nih.gov/31543403/

6. **zhu-2023-klebsiella-abs** - Zhu F, Yuan J, Chen C, et al. Three Klebsiella Species as Potential Pathobionts Generating Endogenous Ethanol in a Clinical Cohort of Patients with Auto-Brewery Syndrome: A Case Control Study. eBioMedicine. 2023;91:104560. PMID: 37060744. PMCID: PMC10139882. DOI: 10.1016/j.ebiom.2023.104560. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10139882/

7. **li-2021-klebsiella-23butanediol** - Li NN, Bai HL, Gao J, et al. High Alcohol-Producing Klebsiella pneumoniae Causes Fatty Liver Disease Through 2,3-Butanediol Fermentation Pathway In Vivo. Gut Microbes. 2021;13(1):1979883. PMID: 34632939. PMCID: PMC8510565. DOI: 10.1080/19490976.2021.1979883. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8510565/

8. **edenberg-2007-adh-aldh-genetics** - Edenberg HJ. The Genetics of Alcohol Metabolism: Role of Alcohol Dehydrogenase and Aldehyde Dehydrogenase Variants. Alcohol Research & Health. 2007;30(1):5-13. PMID: 17718394. PMCID: PMC3860432. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3860432/

9. **spinucci-2006-pseudoobstruction** - Spinucci G, Guidetti M, Lanzoni E, Pironi L. Endogenous Ethanol Production in a Patient with Chronic Intestinal Pseudo-Obstruction and Small Intestinal Bacterial Overgrowth. European Journal of Gastroenterology & Hepatology. 2006;18(7):799-802. PMID: 16772842. DOI: 10.1097/01.meg.0000223906.55245.61. URL: https://pubmed.ncbi.nlm.nih.gov/16772842/

10. **jansson-nettelbladt-2006-sbs-child** - Jansson-Nettelbladt E, Meurling S, Petrini B, Sjölin J. Endogenous Ethanol Fermentation in a Child with Short Bowel Syndrome. Acta Paediatrica. 2006;95(4):502-504. PMID: 16720504. DOI: 10.1080/08035250500469427. URL: https://pubmed.ncbi.nlm.nih.gov/16720504/

11. **hafez-2017-endogenous-ethanol** - Hafez EM, Hamad ME, Fouad M, Abdel-Lateff A. Auto-Brewery Syndrome: Ethanol Pseudo-Toxicity in Diabetic and Hepatic Patients. Human & Experimental Toxicology. 2017;36(5):445-450. PMID: 27492480. DOI: 10.1177/0960327116661400. URL: https://pubmed.ncbi.nlm.nih.gov/27492480/

12. **kowlgi-2015-dlactic-acidosis** - Kowlgi NG, Chhabra L. D-Lactic Acidosis: An Underrecognized Complication of Short Bowel Syndrome. Gastroenterology Research and Practice. 2015;2015:476215. PMID: 25977687. PMCID: PMC4421027. DOI: 10.1155/2015/476215. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4421027/

13. **tamama-2024-bladder-gut-fermentation** - Tamama K. Gut and Bladder Fermentation Syndromes: A Narrative Review. BMC Medicine. 2024;22:24. PMID: 38246992. PMCID: PMC10801939. DOI: 10.1186/s12916-023-03241-7. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10801939/

14. **stamation-2025-alimentary-tract-ethanol** - Stamation R. Endogenous Ethanol Production in the Human Alimentary Tract: A Literature Review. Journal of Gastroenterology and Hepatology. 2025;40(4):783-790. PMID: 39853762. DOI: 10.1111/jgh.16869. URL: https://pubmed.ncbi.nlm.nih.gov/39853762/

15. **COVID19-abs-2024** - Auto-Brewery Syndrome After COVID-19 Infection. ACG Case Reports Journal. 2024;11(2):e01248. PMCID: PMC10852359. DOI: 10.14309/crj.0000000000001248. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10852359/

16. **kruckenberg-2020-urinary-abs** - Kruckenberg KM, DiMartini AF, Rymer JA, Pasculle AW, Tamama K. Urinary Auto-Brewery Syndrome: A Case Report. Annals of Internal Medicine. 2020;172(10):702-704. PMID: 32092761. DOI: 10.7326/L19-0661. URL: https://pubmed.ncbi.nlm.nih.gov/32092761/
