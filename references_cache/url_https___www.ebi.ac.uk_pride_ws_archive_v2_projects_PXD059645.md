---
reference_id: url:https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD059645
title: "https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD059645"
content_type: url
---

# https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD059645

## Content

{
  "accession" : "PXD059645",
  "title" : "Novel in vivo models of autosomal optic atrophy show conserved pathological changes in mitochondrial structure and function Dataset 2 Drosophila",
  "additionalAttributes" : [ ],
  "projectDescription" : "Autosomal optic atrophy (AOA) is a form of hereditary optic neuropathy characterized by the irreversible and progressive degermation of the retinal ganglion cells. Most cases of AOA are associated with a single dominant mutation in OPA1, which encodes a protein required for fusion of the inner mitochondrial membrane. It is unclear how loss of OPA1 leads to neuronal death, and despite ubiquitous expression appears to disproportionately affect the RGCs. This study introduces two novel in vivo models of OPA1-mediated AOA, including the first developmentally viable vertebrate Opa1 knockout (KO). These models allow for the study of Opa1 loss in neurons, specifically RGCs. Though survival is significantly reduced in Opa1 deficient zebrafish and Drosophila, both models permit the study of viable larvae. Moreover, zebrafish Opa1 KO larvae show impaired visual function but unchanged locomotor function, indicating that retinal neurons are particularly sensitive to Opa1 loss. Proteomic profiling of both models reveals marked disruption in protein expression associated with mitochondrial function, consistent with an observed decrease in mitochondrial respiratory function. Similarly, mitochondrial fragmentation and disordered cristae organization were observed in neuronal axons in both models highlighting Opa1’s highly conserved role in regulating mitochondrial morphology and function in neuronal axons. Importantly, in Opa1 deficient zebrafish, mitochondrial disruption and visual impairment precede degeneration of RGCs. These novel models mimic key features of AOA and provide valuable tools for therapeutic screening. Our findings suggest that therapies enhancing mitochondrial function may offer a potential treatment strategy for AOA.",
  "sampleProcessingProtocol" : "Fruit flies were maintained at 25°C on a 12-hour light dark cycle. Generally, animals were maintained on a standard fly food mixture (cornmeal, yeast, dextrose and agar, with tegosept and propionic acid as anti-fungal agents). To generate neuron-specific KO of Opa1, the following fly lines were obtained from the Bloomington Drosophila Stock Centre (BDSC, https://bdsc.indiana.edu/): Opa1 P{TKO.GS00657} (BDSC 76932) and elavG4;Cas9 (BDSC 67073). Other fly stocks used were UAS-mito::GFP (BDSC no. 42737 (Piling et al., 2006) and w1118 control (line number 60100, obtained from the Vienna Drosophila RNAi Centre, www.vdrc.at).  Either 30 adult fly heads were added to 100 μL of LYSE buffer (PreOmics, Germany) and 45 mg of protein extraction beads (Diagenode, Belgium) and homogenised in an ultrasonic bath for 35 minutes. The protein concentration of the solution was then determined using a BCA protein assay kit (Thermo Scientific, USA) according to manufacturer’s instructions. 100 μg of sample protein was made up to a final volume of 85 μL with LYSE buffer. These samples were washed and purified as per the protocol for the iST protein preparation kit (PreOmics, Germany). All samples were then centrifuged at 10,000 rpm for 5 minutes at 4°C, and 20μL of sample was taken from the upper fraction for analysis. Drosophila samples were analysed using a TimsTOF Pro mass spectrometer (Bruker, USA) with an Evosep One chromatography system. In both cases, peptides were separated using C18 reversed phase columns.",
  "dataProcessingProtocol" : "MaxQuant version 2.4.2.0(Cox and Mann 2008; Tyanova, Temu, and Cox 2016) was used to analyse the raw data, incorporating the Andromeda search engine (Cox et al. 2011). MS/MS spectra were matched against database DROSOPHILA_MELANOGASTER (22061 entries, 2023_03 release). All searches were performed using default MaxQuant settings. Trypsin was the specified enzyme allowing 2 missed cleavages and a false discovery rate (FDR) of 1% on the peptide and protein levels. Carbamidomethyl (C) was used as a fixed modification and acetylation (N terminus) a",
  "projectTags" : [ ],
  "keywords" : [ "Zebrafish; drosophila; mitochondria; optic atrophy; visual impairment." ],
  "doi" : "",
  "submissionType" : "PARTIAL",
  "license" : "Creative Commons Public Domain (CC0)",
  "submissionDate" : "2025-01-10",
  "publicationDate" : "2025-05-07",
  "submitters" : [ {
    "title" : "Dr",
    "firstName" : "Eugene",
    "lastName" : "Dillon",
    "identifier" : "58490151",
    "affiliation" : "UCD",
    "email" : "eugene.dillon@ucd.ie",
    "country" : "Ireland",
    "orcid" : "0000-0002-2845-3090",
    "name" : "Eugene Dillon",
    "id" : "58490151"
  } ],
  "labPIs" : [ {
    "title" : "Dr",
    "firstName" : "Niamh",
    "lastName" : "O'Sullivan",
    "identifier" : "3089154",
    "affiliation" : "Lecturer/Associate Professor,  School of Biomolecular and Biomedical Science, UCD Conway Institute, University College Dublin, Belfield, Dublin 4, Ireland",
    "email" : "niamh.osullivan@ucd.ie",
    "country" : "",
    "orcid" : "",
    "name" : "Niamh O'Sullivan",
    "id" : "3089154"
  } ],
  "instruments" : [ {
    "@type" : "CvParam",
    "cvLabel" : "MS",
    "accession" : "MS:1003005",
    "name" : "timsTOF Pro",
    "value" : ""
  } ],
  "softwares" : [ {
    "@type" : "CvParam",
    "cvLabel" : "MS",
    "accession" : "MS:1001583",
    "name" : "MaxQuant"
  } ],
  "experimentTypes" : [ {
    "@type" : "CvParam",
    "cvLabel" : "PRIDE",
    "accession" : "PRIDE:0000428",
    "name" : "Bottom-up proteomics"
  } ],
  "quantificationMethods" : [ {
    "@type" : "CvParam",
    "cvLabel" : "PRIDE",
    "accession" : "EFO:0030054",
    "name" : "label-free quantification"
  } ],
  "countries" : [ "Ireland" ],
  "sampleAttributes" : [ {
    "@type" : "Tuple",
    "key" : {
      "cvLabel" : "EFO",
      "accession" : "EFO:0000635",
      "name" : "organism part"
    },
    "value" : [ {
      "cvLabel" : "BTO",
      "accession" : "BTO:0000282",
      "name" : "head",
      "value" : ""
    } ]
  }, {
    "@type" : "Tuple",
    "key" : {
      "cvLabel" : "EFO",
      "accession" : "OBI:0100026",
      "name" : "organism"
    },
    "value" : [ {
      "cvLabel" : "NEWT",
      "accession" : "NEWT:7227",
      "name" : "Drosophila melanogaster (Fruit fly)",
      "value" : ""
    } ]
  }, {
    "@type" : "Tuple",
    "key" : {
      "cvLabel" : "EFO",
      "accession" : "EFO:0000408",
      "name" : "disease"
    },
    "value" : [ {
      "cvLabel" : "DOID",
      "accession" : "DOID:0111441",
      "name" : "optic atrophy 1",
      "value" : ""
    } ]
  } ],
  "organisms" : [ {
    "@type" : "CvParam",
    "cvLabel" : "NEWT",
    "accession" : "NEWT:7227",
    "name" : "Drosophila melanogaster (fruit fly)",
    "value" : ""
  } ],
  "organismParts" : [ {
    "@type" : "CvParam",
    "cvLabel" : "BTO",
    "accession" : "BTO:0000282",
    "name" : "Head",
    "value" : ""
  } ],
  "diseases" : [ {
    "@type" : "CvParam",
    "cvLabel" : "DOID",
    "accession" : "DOID:0111441",
    "name" : "Optic atrophy 1",
    "value" : ""
  } ],
  "references" : [ {
    "referenceLine" : "Strachan EL, Dillon ET, Sullivan M, Glennon JC, Peyrel A, Sarniguet J, Dubois K, Delprat B, Kennedy BN, O'Sullivan NC. Novel in vivo models of autosomal optic atrophy reveal conserved pathological changes in neuronal mitochondrial structure and function. FASEB J. 2025 39(7):e70497",
    "pubmedID" : 40202868,
    "doi" : "10.1096/fj.202403271r"
  } ],
  "identifiedPTMStrings" : [ {
    "@type" : "CvParam",
    "cvLabel" : "MOD",
    "accession" : "MOD:00425",
    "name" : "monohydroxylated residue",
    "value" : ""
  }, {
    "@type" : "CvParam",
    "cvLabel" : "MOD",
    "accession" : "MOD:00394",
    "name" : "acetylated residue",
    "value" : ""
  }, {
    "@type" : "CvParam",
    "cvLabel" : "MOD",
    "accession" : "MOD:00397",
    "name" : "iodoacetamide derivatized residue",
    "value" : ""
  } ],
  "totalFileDownloads" : 248,
  "otherOmicsLinks" : [ "px:PXD059584", "pride.project:PXD059584" ]
}
