from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'dismech',
     'description': 'Disease Pathophysiology Knowledge Base Schema',
     'id': 'https://w3id.org/monarch-initiative/dismech',
     'imports': ['linkml:types',
                 'classifications/icdo_morphology',
                 'classifications/harrisons_chapters',
                 'classifications/lysosomal_storage',
                 'classifications/mechanistic_nosology',
                 'classifications/iuis_immunodeficiency',
                 'classifications/channelopathies',
                 'classifications/phenotype_category'],
     'license': 'BSD-3-Clause',
     'name': 'dismech',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'ExO': {'prefix_prefix': 'ExO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ExO_'},
                  'GENO': {'prefix_prefix': 'GENO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/GENO_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HGNC': {'prefix_prefix': 'HGNC',
                           'prefix_reference': 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'ICD10CM': {'prefix_prefix': 'ICD10CM',
                              'prefix_reference': 'http://purl.obolibrary.org/obo/ICD10CM_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'OPL': {'prefix_prefix': 'OPL',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OPL_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'http://www.ncbi.nlm.nih.gov/pubmed/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'XCO': {'prefix_prefix': 'XCO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/XCO_'},
                  'arrayexpress': {'prefix_prefix': 'arrayexpress',
                                   'prefix_reference': 'https://www.ebi.ac.uk/biostudies/arrayexpress/studies/'},
                  'bigg': {'prefix_prefix': 'bigg',
                           'prefix_reference': 'https://bigg.ucsd.edu/models/'},
                  'biomodels': {'prefix_prefix': 'biomodels',
                                'prefix_reference': 'https://www.ebi.ac.uk/biomodels/'},
                  'clinicaltrials': {'prefix_prefix': 'clinicaltrials',
                                     'prefix_reference': 'https://clinicaltrials.gov/study/'},
                  'clinvar': {'prefix_prefix': 'clinvar',
                              'prefix_reference': 'https://www.ncbi.nlm.nih.gov/clinvar/variation/'},
                  'dbgap': {'prefix_prefix': 'dbgap',
                            'prefix_reference': 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id='},
                  'dismech': {'prefix_prefix': 'dismech',
                              'prefix_reference': 'https://w3id.org/monarch-initiative/dismech/'},
                  'encode': {'prefix_prefix': 'encode',
                             'prefix_reference': 'https://www.encodeproject.org/experiments/'},
                  'geo': {'prefix_prefix': 'geo',
                          'prefix_reference': 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='},
                  'gtex': {'prefix_prefix': 'gtex',
                           'prefix_reference': 'https://gtexportal.org/home/datasets/'},
                  'hca': {'prefix_prefix': 'hca',
                          'prefix_reference': 'https://data.humancellatlas.org/explore/projects/'},
                  'icd11f': {'prefix_prefix': 'icd11f',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/icd11f_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'metabolights': {'prefix_prefix': 'metabolights',
                                   'prefix_reference': 'https://www.ebi.ac.uk/metabolights/'},
                  'phenopacket-store': {'prefix_prefix': 'phenopacket-store',
                                        'prefix_reference': 'https://github.com/monarch-initiative/phenopacket-store/tree/main/notebooks/'},
                  'pride': {'prefix_prefix': 'pride',
                            'prefix_reference': 'https://www.ebi.ac.uk/pride/archive/projects/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'sra': {'prefix_prefix': 'sra',
                          'prefix_reference': 'https://www.ncbi.nlm.nih.gov/sra/'},
                  'synapse': {'prefix_prefix': 'synapse',
                              'prefix_reference': 'https://www.synapse.org/#!Synapse:'},
                  'vmh': {'prefix_prefix': 'vmh',
                          'prefix_reference': 'https://www.vmh.life/#human/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://monarch-initiative.github.io/dismech'],
     'source_file': 'src/dismech/schema/dismech.yaml',
     'title': 'Disorder Mechanisms Knowledge Base Schema',
     'types': {'FrequencyQuantity': {'base': 'str',
                                     'from_schema': 'https://w3id.org/monarch-initiative/dismech',
                                     'name': 'FrequencyQuantity',
                                     'uri': 'xsd:string'},
               'PMID': {'base': 'str',
                        'from_schema': 'https://w3id.org/monarch-initiative/dismech',
                        'name': 'PMID',
                        'uri': 'xsd:string'}}} )

class ICDOMorphologyEnum(str, Enum):
    """
    ICD-O morphology axis classification for cancer subtypes. Values link to NCI Thesaurus for formal definitions.
    """
    Carcinoma = "Carcinoma"
    """
    Cancer arising from epithelial cells
    """
    Adenocarcinoma = "Adenocarcinoma"
    """
    Carcinoma arising from glandular epithelium
    """
    Squamous_Cell_Carcinoma = "Squamous Cell Carcinoma"
    """
    Carcinoma arising from squamous epithelium
    """
    Sarcoma = "Sarcoma"
    """
    Cancer arising from mesenchymal tissue
    """
    Leukemia = "Leukemia"
    """
    Cancer of blood-forming tissues
    """
    Lymphoma = "Lymphoma"
    """
    Cancer of the lymphatic system
    """
    Multiple_Myeloma = "Multiple Myeloma"
    """
    Cancer of plasma cells
    """
    Melanoma = "Melanoma"
    """
    Cancer arising from melanocytes
    """
    Glioma = "Glioma"
    """
    Cancer arising from glial cells
    """
    Embryonal_Neoplasm = "Embryonal Neoplasm"
    """
    Cancer arising from embryonic tissue
    """


class HarrisonsChapterEnum(str, Enum):
    """
    Traditional internal medicine chapter groupings for disease classification. Based on Harrison's Principles of Internal Medicine organization. Sub-chapters use is_a to indicate parent category.
    """
    Diseases_of_the_heart_and_blood_vessels = "cardiovascular disorder"
    """
    Heart and vascular diseases, including ischemic, structural, rhythm, and vascular conditions.
    """
    Ischemic_heart_disease_myocardial_infarction_angina = "coronary artery disorder"
    """
    Ischemic heart disease due to coronary artery pathology; includes myocardial infarction and angina.
    """
    Diseases_of_heart_muscle_LEFT_PARENTHESISdilated_hypertrophic_restrictiveRIGHT_PARENTHESIS = "cardiomyopathy"
    """
    Primary diseases of the myocardium affecting systolic or diastolic function.
    """
    Arrhythmias_conduction_disorders = "cardiac rhythm disease"
    """
    Electrical conduction or rhythm disorders causing arrhythmias or heart block.
    """
    Diseases_of_heart_valves_LEFT_PARENTHESISstenosis_regurgitationRIGHT_PARENTHESIS = "valvular heart disease"
    """
    Structural or functional valve disease (stenosis or regurgitation) affecting cardiac hemodynamics.
    """
    Diseases_of_arteries_and_veins_LEFT_PARENTHESISaneurysm_PAD_DVTRIGHT_PARENTHESIS = "vascular disease"
    """
    Arterial or venous disorders such as aneurysm, peripheral artery disease, or thrombosis.
    """
    Diseases_of_the_lungs_and_airways = "respiratory system disorder"
    """
    Diseases of airways, lung parenchyma, and pleura that impair ventilation or gas exchange.
    """
    COPD_asthma_bronchiectasis = "obstructive lung disease"
    """
    Airflow limitation from airway narrowing or collapse, including COPD and asthma.
    """
    Pulmonary_fibrosis_sarcoidosis = "interstitial lung disease"
    """
    Diffuse parenchymal lung disorders with inflammation or fibrosis that reduce gas exchange.
    """
    Pulmonary_hypertension_pulmonary_embolism = "pulmonary vascular disease"
    """
    Pulmonary arterial or venous vascular disorders, including hypertension and embolism.
    """
    Diseases_of_the_digestive_tract_and_accessory_organs = "digestive system disorder"
    """
    Diseases of the gastrointestinal tract and accessory organs affecting digestion or absorption.
    """
    CrohnAPOSTROPHEs_disease_ulcerative_colitis = "inflammatory bowel disease"
    """
    Chronic immune-mediated intestinal inflammation, typically Crohn disease or ulcerative colitis.
    """
    Peptic_ulcer_GERD_gastritis = "peptic disorder"
    """
    Acid-related disorders of the esophagus, stomach, or duodenum such as GERD and peptic ulcer disease.
    """
    Diseases_of_the_liver_gallbladder_and_biliary_system = "liver disorder"
    """
    Hepatobiliary diseases involving liver parenchyma, bile ducts, or gallbladder.
    """
    Diseases_of_the_kidneys_and_urinary_system = "kidney disorder"
    """
    Renal and urinary tract diseases affecting filtration, electrolyte balance, or urine flow.
    """
    Glomerulonephritis_nephrotic_syndrome = "glomerular disease"
    """
    Diseases of the glomerulus causing hematuria, proteinuria, or nephrotic/nephritic syndromes.
    """
    Diseases_of_blood_and_blood_forming_organs = "hematologic disorder"
    """
    Disorders of blood cells, bone marrow, and hemostasis.
    """
    Red_blood_cell_disorders = "anemia"
    """
    Reduced red cell mass or hemoglobin due to production defects, blood loss, or hemolysis.
    """
    Bleeding_and_thrombotic_disorders = "coagulation disorder"
    """
    Bleeding or thrombotic disorders from clotting factor, platelet, or regulatory defects.
    """
    Neoplastic_diseases_and_cancer = "cancer"
    """
    Neoplastic diseases characterized by uncontrolled cell proliferation and invasion.
    """
    Leukemia_lymphoma_myeloma = "hematologic malignancy"
    """
    Cancers of blood, bone marrow, and lymphoid tissues such as leukemia or lymphoma.
    """
    Carcinomas_sarcomas_other_solid_neoplasms = "solid tumor"
    """
    Non-hematologic neoplasms arising in organs or soft tissues.
    """
    Diseases_caused_by_pathogenic_microorganisms = "infectious disease"
    """
    Illness caused by pathogenic organisms with host invasion and immune response.
    """
    Infections_caused_by_bacteria = "bacterial infectious disease"
    """
    Infections caused by bacteria, including community and healthcare-associated pathogens.
    """
    Infections_caused_by_viruses = "viral infectious disease"
    """
    Infections caused by viruses affecting any organ system.
    """
    Infections_caused_by_fungi = "fungal infectious disease"
    """
    Mycoses ranging from superficial to invasive systemic infections.
    """
    Infections_caused_by_parasites_LEFT_PARENTHESISprotozoa_helminthsRIGHT_PARENTHESIS = "parasitic infectious disease"
    """
    Protozoal or helminth infections, often vector-borne or food/water transmitted.
    """
    Tuberculosis_NTM_leprosy = "mycobacterial infection"
    """
    Infections due to Mycobacterium species, including tuberculosis and non-tuberculous mycobacteria.
    """
    Diseases_of_the_immune_system_including_autoimmunity = "immune system disorder"
    """
    Immune dysregulation disorders including autoimmunity, immunodeficiency, or hypersensitivity.
    """
    Diseases_caused_by_immune_attack_on_self = "autoimmune disease"
    """
    Immune-mediated tissue damage due to loss of self-tolerance.
    """
    Hypersensitivity_disorders_anaphylaxis = "allergic disease"
    """
    Hypersensitivity disorders including atopy, allergic asthma, and anaphylaxis.
    """
    Diseases_of_hormonal_and_metabolic_systems = "endocrine system disorder"
    """
    Hormonal and metabolic gland disorders affecting systemic homeostasis.
    """
    Type_1_type_2_and_other_forms_of_diabetes = "diabetes mellitus"
    """
    Disorders of glucose regulation due to insulin deficiency and/or insulin resistance.
    """
    HyperSOLIDUShypothyroidism_thyroid_nodules_thyroid_cancer = "thyroid disorder"
    """
    Thyroid gland dysfunction or structural disease altering metabolic control.
    """
    CushingAPOSTROPHEs_AddisonAPOSTROPHEs_pheochromocytoma = "adrenal disorder"
    """
    Adrenal cortex or medulla disorders causing hormone excess or deficiency.
    """
    Diseases_of_the_central_and_peripheral_nervous_system = "nervous system disorder"
    """
    Central or peripheral nervous system diseases affecting cognition, sensation, or movement.
    """
    Stroke_TIA_vascular_dementia = "cerebrovascular disorder"
    """
    Brain ischemia or hemorrhage due to vascular disease, including stroke and TIA.
    """
    AlzheimerAPOSTROPHEs_ParkinsonAPOSTROPHEs_ALS_HuntingtonAPOSTROPHEs = "neurodegenerative disease"
    """
    Progressive neuronal loss leading to cognitive or motor decline.
    """
    Multiple_sclerosis_NMO_ADEM = "demyelinating disease"
    """
    Disorders with loss of myelin in the nervous system, often immune-mediated.
    """
    Myopathies_neuropathies_NMJ_disorders = "neuromuscular disease"
    """
    Diseases of peripheral nerve, neuromuscular junction, or muscle leading to weakness.
    """
    Seizure_disorders = "epilepsy"
    """
    Recurrent unprovoked seizures from abnormal neuronal activity.
    """
    Parkinsonism_dystonia_chorea_ataxia = "movement disorder"
    """
    Motor control disorders causing tremor, rigidity, dystonia, chorea, or ataxia.
    """
    Diseases_of_joints_connective_tissue_and_musculoskeletal_system = "musculoskeletal system disorder"
    """
    Diseases of joints, bones, muscles, or connective tissue.
    """
    Rheumatoid_arthritis_spondyloarthritis_gout = "inflammatory arthritis"
    """
    Inflammatory joint disorders with synovitis, such as RA or spondyloarthropathies.
    """
    SLE_scleroderma_SjogrenAPOSTROPHEs_vasculitis = "connective tissue disease"
    """
    Systemic autoimmune connective tissue disorders affecting skin, joints, vessels, and organs.
    """
    Diseases_of_the_skin_and_appendages = "skin disorder"
    """
    Diseases of the skin, hair, nails, and related appendages.
    """
    Mental_and_behavioral_disorders = "psychiatric disorder"
    """
    Mental and behavioral disorders affecting mood, thought, or behavior.
    """
    Inherited_diseases_and_birth_defects = "hereditary disease"
    """
    Genetic or congenital disorders due to inherited variants or developmental anomalies.
    """


class LysosomalStorageEnum(str, Enum):
    """
    Classification of lysosomal storage diseases by accumulated substrate type. Values link to MONDO disease grouping terms.
    """
    sphingolipidosis = "sphingolipidosis"
    """
    Accumulation of sphingolipids (Gaucher, Fabry, Niemann-Pick, Krabbe, etc.)
    """
    mucopolysaccharidosis = "mucopolysaccharidosis"
    """
    Accumulation of glycosaminoglycans (MPS I through IX)
    """
    mucolipidosis = "mucolipidosis"
    """
    Features of both sphingolipidoses and mucopolysaccharidoses
    """
    glycoproteinosis = "glycoproteinosis"
    """
    Accumulation of glycoproteins (fucosidosis, mannosidosis, sialidosis)
    """
    neuronal_ceroid_lipofuscinosis = "neuronal ceroid lipofuscinosis"
    """
    Accumulation of lipofuscin in neurons (Batten disease family)
    """


class MechanisticNosologyEnum(str, Enum):
    """
    Classification of diseases by molecular mechanism or affected cellular system. Tag diseases with their primary mechanistic category.
    """
    RASopathy = "RASopathy"
    """
    RAS/MAPK signaling pathway disorders (Noonan, Costello, CFC, NF1)
    """
    ciliopathy = "ciliopathy"
    """
    Primary cilia structure/function disorders (PKD, Bardet-Biedl, Joubert)
    """
    laminopathy = "laminopathy"
    """
    Nuclear lamina disorders (EDMD, progeria, lipodystrophy)
    """
    collagenopathy = "collagenopathy"
    """
    Collagen synthesis/structure disorders (OI, EDS, Alport)
    """
    mitochondrial_disease = "mitochondrial disease"
    """
    Mitochondrial function/genome disorders (MELAS, MERRF, Leigh)
    """
    tauopathy = "tauopathy"
    """
    Tau protein aggregation disorders (Alzheimer's, PSP, CBD)
    """
    synucleinopathy = "synucleinopathy"
    """
    Alpha-synuclein aggregation disorders (Parkinson's, DLB, MSA)
    """


class IUISCategoryEnum(str, Enum):
    """
    IUIS classification tables for inborn errors of immunity (IEI). Based on IUIS 2022 phenotypic classification.
    """
    combined_immunodeficiency = "combined immunodeficiency"
    """
    Table 1 - Immunodeficiencies affecting cellular and humoral immunity (SCID, CID, Omenn)
    """
    combined_immunodeficiency_with_syndromic_features = "combined immunodeficiency with syndromic features"
    """
    Table 2 - CID with associated or syndromic features (WAS, AT, DiGeorge, CHARGE)
    """
    predominantly_antibody_deficiency = "predominantly antibody deficiency"
    """
    Table 3 - Predominantly antibody deficiencies (XLA, CVID, selective Ig deficiency, hyper-IgM)
    """
    immune_dysregulation = "immune dysregulation"
    """
    Table 4 - Diseases of immune dysregulation (HLH, ALPS, IPEX, APECED)
    """
    phagocyte_defect = "phagocyte defect"
    """
    Table 5 - Congenital defects of phagocyte number or function (SCN, CGD, LAD)
    """
    innate_immunity_defect = "innate immunity defect"
    """
    Table 6 - Defects in intrinsic and innate immunity (MSMD, HSE susceptibility, CMC)
    """
    autoinflammatory_syndrome = "autoinflammatory syndrome"
    """
    Table 7 - Autoinflammatory disorders (FMF, CAPS, TRAPS, HIDS, interferonopathies)
    """
    complement_deficiency = "complement deficiency"
    """
    Table 8 - Complement deficiencies (C1-C9, MBL, factor H/I/B, properdin)
    """
    bone_marrow_failure = "bone marrow failure"
    """
    Table 9 - Bone marrow failure syndromes (Fanconi, DKC, SDS, DBA)
    """
    phenocopy_of_IEI = "phenocopy of IEI"
    """
    Table 10 - Phenocopies of IEI (somatic mutations, autoantibodies to cytokines)
    """


class ChannelopathyOrganSystemEnum(str, Enum):
    """
    Classification categories for channelopathies by affected organ system. Tag diseases like Long QT syndrome (cardiac), periodic paralysis (skeletal muscle), episodic ataxia (neurological), cystic fibrosis (epithelial).
    """
    cardiac_channelopathy = "cardiac channelopathy"
    """
    Ion channel disorders primarily affecting cardiac rhythm (Long QT, Brugada, CPVT)
    """
    skeletal_muscle_channelopathy = "skeletal muscle channelopathy"
    """
    Ion channel disorders causing episodic weakness or myotonia
    """
    neurological_channelopathy = "neurological channelopathy"
    """
    Ion channel disorders affecting CNS (episodic ataxia, epilepsy, migraine)
    """
    epithelial_channelopathy = "epithelial channelopathy"
    """
    Ion channel disorders affecting epithelial transport (cystic fibrosis)
    """


class PhenotypeCategoryEnum(str, Enum):
    """
    Broad phenotype categories from the Human Phenotype Ontology. Each value corresponds to a direct child of HP:0000118 (Phenotypic abnormality).
    """
    Abnormality_of_blood_and_blood_forming_tissues = "Blood"
    """
    Abnormalities of the hematopoietic system including anemias, coagulopathies, and leukocyte disorders
    """
    Abnormality_of_the_breast = "Breast"
    """
    Abnormalities of breast development, morphology, or function
    """
    Abnormality_of_the_cardiovascular_system = "Cardiovascular"
    """
    Abnormalities of the heart and vasculature
    """
    Abnormality_of_the_digestive_system = "Digestive"
    """
    Abnormalities of the gastrointestinal tract, liver, and pancreas
    """
    Abnormality_of_the_ear = "Ear"
    """
    Abnormalities of ear morphology or hearing
    """
    Abnormality_of_the_endocrine_system = "Endocrine"
    """
    Abnormalities of hormone-producing glands and endocrine regulation
    """
    Abnormality_of_the_eye = "Eye"
    """
    Abnormalities of the eye and visual system
    """
    Abnormality_of_the_genitourinary_system = "Genitourinary"
    """
    Abnormalities of the kidneys, urinary tract, and reproductive organs
    """
    Abnormality_of_head_or_neck = "Head and Neck"
    """
    Abnormalities of craniofacial structures and the neck
    """
    Abnormality_of_the_immune_system = "Immune"
    """
    Abnormalities of innate or adaptive immunity
    """
    Abnormality_of_the_integument = "Integument"
    """
    Abnormalities of skin, hair, nails, and sweat glands
    """
    Abnormality_of_limbs = "Limbs"
    """
    Abnormalities of upper or lower limb structure
    """
    Abnormality_of_metabolismSOLIDUShomeostasis = "Metabolism"
    """
    Abnormalities of metabolic processes and biochemical homeostasis
    """
    Abnormality_of_the_musculoskeletal_system = "Musculoskeletal"
    """
    Abnormalities of bones, joints, muscles, and connective tissue
    """
    Abnormality_of_the_nervous_system = "Nervous System"
    """
    Abnormalities of the central and peripheral nervous system
    """
    Abnormality_of_prenatal_development_or_birth = "Prenatal and Birth"
    """
    Abnormalities arising during prenatal development or at birth
    """
    Abnormality_of_the_respiratory_system = "Respiratory"
    """
    Abnormalities of the airways, lungs, and respiratory function
    """
    Abnormality_of_the_thoracic_cavity = "Thoracic Cavity"
    """
    Abnormalities of thoracic structures (pleura, mediastinum, diaphragm)
    """
    Abnormality_of_the_voice = "Voice"
    """
    Abnormalities of voice production and quality
    """
    Abnormal_cellular_phenotype = "Cellular"
    """
    Abnormalities at the cellular level including cell morphology and behavior
    """
    Constitutional_symptom = "Constitutional"
    """
    Systemic symptoms such as fever, fatigue, and weight loss
    """
    Growth_abnormality = "Growth"
    """
    Abnormalities of growth including short stature, tall stature, and growth delay
    """
    Neoplasm = "Neoplasm"
    """
    Benign or malignant neoplasms (tumors)
    """


class EvidenceItemSupportEnum(str, Enum):
    """
    The level of support for an evidence item
    """
    WRONG_STATEMENT = "WRONG_STATEMENT"
    """
    WRONG_STATEMENT
    """
    SUPPORT = "SUPPORT"
    """
    SUPPORT
    """
    REFUTE = "REFUTE"
    """
    REFUTE
    """
    NO_EVIDENCE = "NO_EVIDENCE"
    """
    NO_EVIDENCE
    """
    PARTIAL = "PARTIAL"
    """
    PARTIAL
    """


class EvidenceSourceEnum(str, Enum):
    """
    The provenance/source of the evidence item
    """
    HUMAN_CLINICAL = "HUMAN_CLINICAL"
    """
    Human clinical observations (patients, cohorts, case reports, clinical trials, epidemiology)
    """
    MODEL_ORGANISM = "MODEL_ORGANISM"
    """
    In vivo animal evidence (mouse, zebrafish, primate, veterinary case series including dog/cat/horse, other non-human animal models etc.)
    """
    IN_VITRO = "IN_VITRO"
    """
    In vitro or ex vivo assays (cell culture, organoids, tissue slices, biochemical assays)
    """
    COMPUTATIONAL = "COMPUTATIONAL"
    """
    In silico/modeling studies (simulation, docking, ML predictions, network inference) even when using clinical data inputs
    """
    OTHER = "OTHER"
    """
    Evidence not fitting the above (e.g., expert consensus without data, image atlases without cohort context)
    """


class DefinitionTypeEnum(str, Enum):
    """
    The type of definition or criteria set
    """
    DIAGNOSTIC_CRITERIA = "DIAGNOSTIC_CRITERIA"
    """
    Published diagnostic criteria (clinical/serologic/imaging)
    """
    PHENOTYPE_ALGORITHM = "PHENOTYPE_ALGORITHM"
    """
    Algorithmic phenotype definition (e.g., PheKB-style)
    """
    CASE_DEFINITION = "CASE_DEFINITION"
    """
    Case definition for surveillance or reporting
    """
    OTHER = "OTHER"
    """
    Other definition type
    """


class MappingConsistencyEnum(str, Enum):
    """
    Consistency of a mapping relative to another reference source
    """
    CONSISTENT = "CONSISTENT"
    """
    Mapping is consistent with the reference source
    """
    INCONSISTENT = "INCONSISTENT"
    """
    Mapping conflicts with the reference source
    """
    MISSING = "MISSING"
    """
    Mapping is missing from the reference source
    """
    UNKNOWN = "UNKNOWN"
    """
    Consistency not assessed or unclear
    """


class FrequencyEnum(str, Enum):
    """
    The frequency of an event or phenomenon
    """
    FREQUENT = "FREQUENT"
    """
    Frequent
    """
    OCCASIONAL = "OCCASIONAL"
    """
    Occasional
    """
    VERY_FREQUENT = "VERY_FREQUENT"
    """
    Very frequent
    """
    VERY_RARE = "VERY_RARE"
    """
    Very rare
    """
    OBLIGATE = "OBLIGATE"
    """
    Obligate
    """


class ClinicalSignificanceEnum(str, Enum):
    """
    The clinical significance of a variant for a condition (ACMG guidelines)
    """
    PATHOGENIC = "PATHOGENIC"
    """
    pathogenic_for_condition
    """
    LIKELY_PATHOGENIC = "LIKELY_PATHOGENIC"
    """
    likely_pathogenic_for_condition
    """
    BENIGN = "BENIGN"
    """
    benign_for_condition
    """
    LIKELY_BENIGN = "LIKELY_BENIGN"
    """
    likely_benign_for_condition
    """
    UNCERTAIN_SIGNIFICANCE = "UNCERTAIN_SIGNIFICANCE"
    """
    has_uncertain_significance_for_condition
    """


class ModifierEnum(str, Enum):
    """
    Qualifiers for direction, intensity, or pathological state of a descriptor
    """
    INCREASED = "INCREASED"
    """
    Upregulated, hyperactive, elevated, or excessive
    """
    DECREASED = "DECREASED"
    """
    Downregulated, hypoactive, reduced, or deficient
    """
    ABNORMAL = "ABNORMAL"
    """
    Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
    """
    DYSREGULATED = "DYSREGULATED"
    """
    Regulation is impaired (may be increased or decreased)
    """
    ABSENT = "ABSENT"
    """
    Not occurring or not present
    """


class PenetranceEnum(str, Enum):
    """
    Penetrance classification for inheritance
    """
    COMPLETE = "COMPLETE"
    """
    Complete penetrance
    """
    INCOMPLETE = "INCOMPLETE"
    """
    Incomplete or partial penetrance
    """
    UNKNOWN = "UNKNOWN"
    """
    Unknown or not specified
    """


class ExpressivityEnum(str, Enum):
    """
    Expressivity classification for inheritance
    """
    VARIABLE = "VARIABLE"
    """
    Variable expressivity
    """
    CONSISTENT = "CONSISTENT"
    """
    Consistent or uniform expressivity
    """
    UNKNOWN = "UNKNOWN"
    """
    Unknown or not specified
    """


class LateralityEnum(str, Enum):
    """
    Laterality qualifier for anatomical structures or procedures
    """
    LEFT = "LEFT"
    """
    Left side of the body
    """
    RIGHT = "RIGHT"
    """
    Right side of the body
    """
    BILATERAL = "BILATERAL"
    """
    Both sides of the body
    """


class AssayTerm(str):
    """
    A term representing an assay
    """
    pass


class CellularComponentTerm(str):
    """
    A term representing a cellular component
    """
    pass


class ProteinComplexTerm(str):
    """
    A term representing a protein complex
    """
    pass


class BiologicalProcessTerm(str):
    """
    A term representing a biological process or pathway
    """
    pass


class ChemicalEntityTerm(str):
    """
    A term representing a chemical entity
    """
    pass


class PhenotypeTerm(str):
    """
    A term representing a phenotype or disease manifestation
    """
    pass


class InheritanceTerm(str):
    """
    A term representing mode of inheritance
    """
    pass


class AnatomicalEntityTerm(str):
    """
    A term representing an anatomical entity
    """
    pass


class TreatmentActionTerm(str):
    """
    A term representing a medical action or treatment (from MAXO)
    """
    pass


class RegimenTerm(str):
    """
    A term representing a treatment regimen (from NCIT)
    """
    pass


class GeographyTerm(str):
    """
    A place or location
    """
    pass


class PhaseTerm(str):
    """
    A phase or stage
    """
    pass


class LifeCycleStageTerm(str):
    """
    A parasite life cycle stage term (from OPL)
    """
    pass


class TriggerTerm(str):
    """
    A trigger
    """
    pass


class GeneTerm(str):
    """
    A gene term from HGNC
    """
    pass


class CellTypeTerm(str):
    """
    A cell type
    """
    pass


class BiomarkerTerm(str):
    """
    A biomarker term from NCIT. Includes proteins, gene products, fusion products, and other molecular markers. No hierarchy constraint - validates term exists and label matches.
    """
    pass


class GeneProductTerm(str):
    """
    A gene product term from NCIT. Includes proteins, fusion proteins, oncoproteins, and other gene products involved in disease mechanisms.
    """
    pass


class HistopathologyFindingTerm(str):
    """
    A histopathologic finding term from NCIT. Includes morphologic findings, architectural patterns, growth patterns, cellular features, and grading. Rooted at NCIT:C35867 (Morphologic Finding) and NCIT:C18000 (Histologic Grade).
    """
    pass


class DiseaseTerm(str):
    """
    A disease or medical condition
    """
    pass


class ICD10CMTerm(str):
    """
    An ICD-10-CM diagnosis code
    """
    pass


class ICD11FTerm(str):
    """
    An ICD-11 Foundation diagnosis code
    """
    pass


class ExposureTerm(str):
    """
    A term representing an exposure event (from ECTO or XCO)
    """
    pass


class EnvironmentTerm(str):
    """
    A term representing an environmental context, material, or feature (from ENVO)
    """
    pass


class OrganismTerm(str):
    """
    A term representing an organism from NCBITaxon
    """
    pass


class OnsetEnum(str, Enum):
    """
    Age of onset categories from HPO
    """
    ANTENATAL = "ANTENATAL"
    """
    Antenatal onset
    """
    EMBRYONAL = "EMBRYONAL"
    """
    Embryonal onset
    """
    FETAL = "FETAL"
    """
    Fetal onset
    """
    CONGENITAL = "CONGENITAL"
    """
    Congenital onset
    """
    NEONATAL = "NEONATAL"
    """
    Neonatal onset
    """
    INFANTILE = "INFANTILE"
    """
    Infantile onset
    """
    CHILDHOOD = "CHILDHOOD"
    """
    Childhood onset
    """
    JUVENILE = "JUVENILE"
    """
    Juvenile onset
    """
    YOUNG_ADULT = "YOUNG_ADULT"
    """
    Young adult onset
    """
    MIDDLE_AGE = "MIDDLE_AGE"
    """
    Middle age onset
    """
    LATE = "LATE"
    """
    Late onset
    """
    PUERPERAL = "PUERPERAL"
    """
    Puerperal onset
    """


class ZygosityEnum(str, Enum):
    """
    Zygosity categories from GENO
    """
    HETEROZYGOUS = "HETEROZYGOUS"
    """
    Heterozygous
    """
    SIMPLE_HETEROZYGOUS = "SIMPLE_HETEROZYGOUS"
    """
    Simple heterozygous
    """
    COMPOUND_HETEROZYGOUS = "COMPOUND_HETEROZYGOUS"
    """
    Compound heterozygous
    """
    HOMOZYGOUS = "HOMOZYGOUS"
    """
    Homozygous
    """
    HEMIZYGOUS = "HEMIZYGOUS"
    """
    Hemizygous
    """


class DatasetTypeEnum(str, Enum):
    """
    Type of dataset or data resource
    """
    MICROARRAY = "MICROARRAY"
    """
    Gene expression microarray
    """
    BULK_RNA_SEQ = "BULK_RNA_SEQ"
    """
    Bulk RNA sequencing
    """
    SINGLE_CELL_RNA_SEQ = "SINGLE_CELL_RNA_SEQ"
    """
    Single-cell RNA sequencing
    """
    SPATIAL_TRANSCRIPTOMICS = "SPATIAL_TRANSCRIPTOMICS"
    """
    Spatially resolved transcriptomics
    """
    METHYLATION = "METHYLATION"
    """
    DNA methylation profiling
    """
    CHIP_SEQ = "CHIP_SEQ"
    """
    Chromatin immunoprecipitation sequencing
    """
    ATAC_SEQ = "ATAC_SEQ"
    """
    Assay for transposase-accessible chromatin sequencing
    """
    PROTEOMICS = "PROTEOMICS"
    """
    Protein expression profiling
    """
    METABOLOMICS = "METABOLOMICS"
    """
    Metabolite profiling
    """
    GWAS = "GWAS"
    """
    Genome-wide association study
    """
    WGS = "WGS"
    """
    Whole genome sequencing
    """
    WES = "WES"
    """
    Whole exome sequencing
    """
    PHENOPACKETS = "PHENOPACKETS"
    """
    GA4GH Phenopacket collection (case-level phenotype data)
    """
    VARIANT_DATABASE = "VARIANT_DATABASE"
    """
    Curated genetic variant collection
    """


class CurationActionEnum(str, Enum):
    """
    Simple action types for curation audit trail
    """
    CREATED = "CREATED"
    """
    Initial file creation
    """
    EDITED = "EDITED"
    """
    File modification
    """


class ClinicalTrialPhaseEnum(str, Enum):
    """
    Clinical trial phase categories per FDA/NIH standards
    """
    PHASE_I = "PHASE_I"
    """
    Phase I - Initial safety and dosage assessment in small group (20-100 participants)
    """
    PHASE_II = "PHASE_II"
    """
    Phase II - Efficacy and side effects assessment in larger group (100-500 participants)
    """
    PHASE_III = "PHASE_III"
    """
    Phase III - Efficacy confirmation and monitoring in large population (1000-5000 participants)
    """
    PHASE_IV = "PHASE_IV"
    """
    Phase IV - Post-market surveillance and additional benefits/risks studies
    """
    NOT_APPLICABLE = "NOT_APPLICABLE"
    """
    Trial does not follow standard FDA phase classification (e.g., observational, device studies)
    """


class ClinicalTrialStatusEnum(str, Enum):
    """
    Clinical trial recruitment and status categories per ClinicalTrials.gov
    """
    RECRUITING = "RECRUITING"
    """
    Currently enrolling participants
    """
    NOT_RECRUITING = "NOT_RECRUITING"
    """
    Not currently enrolling but may in the future
    """
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    """
    Actively recruiting previously enrolled participants (closed to new enrollment)
    """
    COMPLETED = "COMPLETED"
    """
    Trial data collection and analysis completed
    """
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    """
    Enrollment restricted to invited participants only
    """
    SUSPENDED = "SUSPENDED"
    """
    Temporarily halted pending review or administrative action
    """
    TERMINATED = "TERMINATED"
    """
    Stopped before completion, may include safety or efficacy concerns
    """
    WITHDRAWN = "WITHDRAWN"
    """
    Closed before enrollment began (never enrolled participants)
    """
    UNKNOWN = "UNKNOWN"
    """
    Status unknown or not provided
    """


class ComputationalModelTypeEnum(str, Enum):
    """
    Type of computational or in-silico model
    """
    GENOME_SCALE_METABOLIC = "GENOME_SCALE_METABOLIC"
    """
    Genome-scale metabolic reconstruction (e.g., Recon3D, Harvey)
    """
    FLUX_BALANCE_ANALYSIS = "FLUX_BALANCE_ANALYSIS"
    """
    Constraint-based FBA model
    """
    KINETIC = "KINETIC"
    """
    ODE-based kinetic model with rate equations
    """
    AGENT_BASED = "AGENT_BASED"
    """
    Agent-based simulation model
    """
    BOOLEAN_NETWORK = "BOOLEAN_NETWORK"
    """
    Boolean gene regulatory network
    """
    PHYSIOLOGICAL = "PHYSIOLOGICAL"
    """
    Physiologically-based pharmacokinetic (PBPK) or organ model
    """
    DIGITAL_TWIN = "DIGITAL_TWIN"
    """
    Patient-specific computational model
    """
    MACHINE_LEARNING = "MACHINE_LEARNING"
    """
    ML/AI predictive model trained on disease data
    """
    PERTURBATION_PREDICTION = "PERTURBATION_PREDICTION"
    """
    Cell-based perturbation models (CRISPR screens, chemical perturbations) with gene expression readouts
    """
    FOUNDATION_MODEL = "FOUNDATION_MODEL"
    """
    Pre-trained single-cell foundation models (scGPT, Geneformer, scGenePT) for perturbation response prediction
    """


class ComorbidityDirectionEnum(str, Enum):
    """
    Directionality of a comorbidity/trajectory association
    """
    A_BEFORE_B = "A_BEFORE_B"
    """
    A precedes B
    """
    B_BEFORE_A = "B_BEFORE_A"
    """
    B precedes A
    """
    BIDIRECTIONAL = "BIDIRECTIONAL"
    """
    Evidence supports both directions
    """
    SAME_TIME = "SAME_TIME"
    """
    Co-incident or same-time association
    """
    UNKNOWN = "UNKNOWN"
    """
    Directionality is unknown or not established
    """


class CurationStatusEnum(str, Enum):
    """
    Curation workflow status for an association
    """
    CANDIDATE = "CANDIDATE"
    """
    Prioritized for curation
    """
    IN_PROGRESS = "IN_PROGRESS"
    """
    Curation in progress
    """
    CURATED = "CURATED"
    """
    Curated with literature-backed evidence
    """
    DEFERRED = "DEFERRED"
    """
    Deferred or deprioritized
    """


class AssociationSignalSourceEnum(str, Enum):
    """
    Source of an association signal
    """
    DISEASE_TRAJECTORIES = "DISEASE_TRAJECTORIES"
    """
    Disease Trajectories (CSH/Austria)
    """
    COHD = "COHD"
    """
    Columbia Open Health Data (COHD)
    """
    LITERATURE = "LITERATURE"
    """
    Published literature source
    """
    OTHER = "OTHER"
    """
    Other or unspecified source
    """


class AssociationSignalMethodEnum(str, Enum):
    """
    Method used to derive an association signal
    """
    EHR_TEMPORAL_COMORBIDITY = "EHR_TEMPORAL_COMORBIDITY"
    """
    EHR-derived temporal comorbidity/trajectory signal
    """
    EHR_COHORT_ASSOCIATION = "EHR_COHORT_ASSOCIATION"
    """
    EHR-derived cohort association (non-temporal)
    """
    LITERATURE_ASSOCIATION = "LITERATURE_ASSOCIATION"
    """
    Association reported in the literature
    """
    COMPUTATIONAL_INFERENCE = "COMPUTATIONAL_INFERENCE"
    """
    Computational inference or enrichment
    """
    OTHER = "OTHER"
    """
    Other or unspecified method
    """


class SexEnum(str, Enum):
    """
    Sex-specific stratum
    """
    MALE = "MALE"
    """
    Male
    """
    FEMALE = "FEMALE"
    """
    Female
    """
    OTHER = "OTHER"
    """
    Other or nonbinary
    """
    UNKNOWN = "UNKNOWN"
    """
    Unknown or not specified
    """


class ConditionCompositionEnum(str, Enum):
    """
    Composition type for a composite condition descriptor
    """
    SINGLE = "SINGLE"
    """
    Single condition (default)
    """
    UNION = "UNION"
    """
    Union of multiple component conditions
    """
    CATEGORY = "CATEGORY"
    """
    Category code encompassing multiple conditions
    """
    OVERLAPS = "OVERLAPS"
    """
    Overlapping condition set (non-exhaustive)
    """
    SUBSET_OF = "SUBSET_OF"
    """
    Subset of a broader condition group
    """
    OTHER = "OTHER"
    """
    Other or unspecified composition
    """


class AssociationMetricTypeEnum(str, Enum):
    """
    Type of association metric
    """
    OR = "OR"
    """
    Odds ratio
    """
    AOR = "AOR"
    """
    Adjusted odds ratio
    """
    RR = "RR"
    """
    Relative risk
    """
    HR = "HR"
    """
    Hazard ratio
    """
    PREVALENCE = "PREVALENCE"
    """
    Prevalence proportion
    """
    INCIDENCE_RATE = "INCIDENCE_RATE"
    """
    Incidence rate
    """
    IRR = "IRR"
    """
    Incidence rate ratio
    """
    OTHER = "OTHER"
    """
    Other or unspecified metric
    """



class CurationEvent(ConfiguredBaseModel):
    """
    A single curation event in the audit trail
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'curation_timestamp': {'name': 'curation_timestamp',
                                               'required': True}}})

    curation_timestamp: datetime  = Field(default=..., description="""ISO 8601 timestamp of the curation event""", json_schema_extra = { "linkml_meta": {'alias': 'curation_timestamp', 'domain_of': ['CurationEvent']} })
    curation_model: Optional[str] = Field(default=None, description="""Model identifier used for curation (e.g., claude-opus-4-5-20251101)""", json_schema_extra = { "linkml_meta": {'alias': 'curation_model', 'domain_of': ['CurationEvent']} })
    curation_action: Optional[CurationActionEnum] = Field(default=None, description="""Type of curation action performed""", json_schema_extra = { "linkml_meta": {'alias': 'curation_action', 'domain_of': ['CurationEvent']} })
    curation_description: Optional[str] = Field(default=None, description="""Human-readable description of changes made""", json_schema_extra = { "linkml_meta": {'alias': 'curation_description', 'domain_of': ['CurationEvent']} })


class Term(ConfiguredBaseModel):
    """
    A structured reference to an ontology term
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    id: str = Field(default=..., description="""Ontology term identifier (CURIE)""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Term']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label for the ontology term""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'comments': ['This is automatically validated by the linkml-term-validator '
                      'tool.'],
         'domain_of': ['Term']} })


class Descriptor(ConfiguredBaseModel):
    """
    Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'A description of the '
                                                       'descriptor. This may typically '
                                                       'be redundant with the `term` '
                                                       'object, but the description is '
                                                       'more human-readable and may be '
                                                       'used to communicate nuances '
                                                       'not captured by the rigid '
                                                       'standardization of the term '
                                                       'object.',
                                        'name': 'description',
                                        'recommended': False}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class Qualifier(ConfiguredBaseModel):
    """
    A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['DEPRECATED - prefer explicit slots (located_in, laterality) for '
                      'better constraints',
                      'Use for formal semantic relationships like "has_input some X"',
                      'Both predicate and value are Descriptors, allowing recursive '
                      'composition',
                      'Predicate typically uses RO (Relation Ontology) terms'],
         'deprecated': 'Use explicit slots like located_in and laterality on '
                       'Descriptor instead',
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    predicate: Optional[Descriptor] = Field(default=None, description="""The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')""", json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Qualifier']} })
    value: Optional[Descriptor] = Field(default=None, description="""The value/filler in a qualifier""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Qualifier']} })


class CellTypeDescriptor(Descriptor):
    """
    A descriptor for cell types, bindable to Cell Ontology (CL)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'CellTypeTerm'}],
                                 'description': 'Optional Cell Ontology term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional Cell Ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for biological processes, bindable to Gene Ontology (GO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional GO biological process term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO biological process term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for anatomical locations, bindable to UBERON
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional UBERON anatomical entity '
                                                'term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional UBERON anatomical entity term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for chemical entities, bindable to CHEBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional CHEBI chemical entity term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional CHEBI chemical entity term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class GeneDescriptor(Descriptor):
    """
    A descriptor for genes, bindable to HGNC or other gene databases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'GeneTerm'}],
                                 'description': 'Optional gene database term reference '
                                                '(e.g., HGNC)',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional gene database term reference (e.g., HGNC)""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GeneTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for cellular components, bindable to GO cellular component
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional GO cellular component term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO cellular component term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ProteinComplexDescriptor(Descriptor):
    """
    A descriptor for protein complexes that gene products participate in, bindable to GO protein complex terms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional GO protein complex term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO protein complex term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class AssayDescriptor(Descriptor):
    """
    A descriptor for assays, bindable to OBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional OBI assay term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional OBI assay term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class TriggerDescriptor(Descriptor):
    """
    A descriptor for triggers/causes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional ontology term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class DiseaseDescriptor(Descriptor):
    """
    A descriptor for the focal disease, bindable to MONDO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'DiseaseTerm'}],
                                 'description': 'Optional MONDO disease term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MONDO disease term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class BiomarkerDescriptor(Descriptor):
    """
    A descriptor for biomarkers, bindable to NCIT
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'BiomarkerTerm'}],
                                 'description': 'NCIT biomarker term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT biomarker term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'BiomarkerTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class GeneProductDescriptor(Descriptor):
    """
    A descriptor for gene products (proteins, fusion proteins, oncoproteins), bindable to NCIT Gene Product hierarchy (NCIT:C26548)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'GeneProductTerm'}],
                                 'description': 'NCIT gene product term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT gene product term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GeneProductTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class HistopathologyFindingDescriptor(Descriptor):
    """
    A descriptor for histopathologic findings, bindable to NCIT Morphologic Finding (C35867), Histologic Grade (C18000), or HP Abnormal cell morphology (HP:0025461)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use for architectural patterns (spindle cell, epithelioid, '
                      'nested, etc.)',
                      'Use for differentiation status (well/poorly differentiated)',
                      'Use for specific findings (rosettes, necrosis, mitotic '
                      'activity)',
                      'Use for histologic grades when applicable'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'HistopathologyFindingTerm'}],
                                 'description': 'NCIT or HP histopathology finding '
                                                'term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT or HP histopathology finding term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'HistopathologyFindingTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class LifeCycleStageDescriptor(Descriptor):
    """
    A descriptor for parasite life cycle stages, bindable to OPL
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'LifeCycleStageTerm'}],
                                 'description': 'OPL life cycle stage term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""OPL life cycle stage term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'LifeCycleStageTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class PhenotypeDescriptor(Descriptor):
    """
    A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'PhenotypeTerm'}],
                                 'description': 'Optional HP phenotype term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional HP phenotype term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'PhenotypeTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class InheritanceDescriptor(Descriptor):
    """
    A descriptor for inheritance patterns, bindable to HPO mode of inheritance terms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'InheritanceTerm'}],
                                 'description': 'Optional HPO mode of inheritance term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional HPO mode of inheritance term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'InheritanceTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class TreatmentDescriptor(Descriptor):
    """
    A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'TreatmentActionTerm'}],
                                 'description': 'Optional MAXO treatment term '
                                                'reference',
                                 'name': 'term'},
                        'therapeutic_agent': {'comments': ['Prefer CHEBI terms for '
                                                           'specific drugs (e.g., '
                                                           'CHEBI:15365 for aspirin)',
                                                           'Use NCIT for drug classes '
                                                           'when specific CHEBI term '
                                                           'unavailable'],
                                              'description': 'The drug(s) or chemical '
                                                             'agent(s) used in this '
                                                             'treatment. Use when the '
                                                             'MAXO term is generic '
                                                             '(e.g., pharmacotherapy '
                                                             'MAXO:0000058) but '
                                                             'specific drugs are '
                                                             'involved.',
                                              'name': 'therapeutic_agent'}}})

    therapeutic_agent: Optional[list[ChemicalEntityDescriptor]] = Field(default=None, description="""The drug(s) or chemical agent(s) used in this treatment. Use when the MAXO term is generic (e.g., pharmacotherapy MAXO:0000058) but specific drugs are involved.""", json_schema_extra = { "linkml_meta": {'alias': 'therapeutic_agent',
         'comments': ['Prefer CHEBI terms for specific drugs (e.g., CHEBI:15365 for '
                      'aspirin)',
                      'Use NCIT for drug classes when specific CHEBI term unavailable'],
         'domain_of': ['TreatmentDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MAXO treatment term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'TreatmentActionTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class RegimenDescriptor(Descriptor):
    """
    A descriptor for treatment regimens, bindable to NCIT
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'RegimenTerm'}],
                                 'description': 'Optional NCIT regimen term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional NCIT regimen term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'RegimenTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ExposureDescriptor(Descriptor):
    """
    A descriptor for exposure events, bindable to ECTO or XCO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use ECTO (Environmental Conditions, Treatments, and Exposures '
                      'Ontology) for general exposures',
                      'Use XCO (Experimental Conditions Ontology) for experimental '
                      'exposure conditions'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ExposureTerm'}],
                                 'description': 'Optional ECTO/XCO exposure term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ECTO/XCO exposure term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ExposureTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class EnvironmentDescriptor(Descriptor):
    """
    A descriptor for environmental contexts/settings, bindable to ENVO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use ENVO (Environment Ontology) for habitats, biomes, and '
                      'environmental features'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'EnvironmentTerm'}],
                                 'description': 'Optional ENVO environment term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ENVO environment term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'EnvironmentTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class OrganismDescriptor(Descriptor):
    """
    A descriptor for organisms, bindable to NCBITaxon
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'OrganismTerm'}],
                                 'description': 'NCBITaxon term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCBITaxon term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class HostDescriptor(OrganismDescriptor):
    """
    A descriptor for hosts in an infectious agent life cycle
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use role for definitive, intermediate, reservoir, accidental, '
                      'or paratenic host'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role',
         'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCBITaxon term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class SampleTypeDescriptor(Descriptor):
    """
    A descriptor for biological sample types (tissue and/or cell type)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    tissue_term: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""UBERON term for the tissue""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_term', 'domain_of': ['SampleTypeDescriptor']} })
    cell_type_term: Optional[CellTypeDescriptor] = Field(default=None, description="""CL term for the cell type""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_term', 'domain_of': ['SampleTypeDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class GeneticContext(ConfiguredBaseModel):
    """
    A structured description of a genetic context that modifies phenotype frequency, severity, or presentation. Flexible enough to capture single genes, multiple genes, mutation types, zygosity, complementation groups, and complex genotypes. The description slot accommodates contexts that don't fit neatly into the structured fields (e.g., structural variants, complex rearrangements).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'domain_of': ['GeneticContext', 'Pathophysiology', 'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genes',
         'domain_of': ['GeneticContext', 'Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    allele_type: Optional[str] = Field(default=None, description="""Type of allele or mutation (e.g., null, missense, splice_site, deletion, frameshift, nonsense, hypomorphic, structural_variant). Free text to accommodate the diversity of mutation nomenclature.""", json_schema_extra = { "linkml_meta": {'alias': 'allele_type', 'domain_of': ['GeneticContext']} })
    zygosity: Optional[ZygosityEnum] = Field(default=None, description="""Zygosity context""", json_schema_extra = { "linkml_meta": {'alias': 'zygosity', 'domain_of': ['GeneticContext']} })
    functional_impact: Optional[str] = Field(default=None, description="""Functional consequence of the genetic variant (e.g., loss_of_function, gain_of_function, dominant_negative).""", json_schema_extra = { "linkml_meta": {'alias': 'functional_impact', 'domain_of': ['GeneticContext']} })
    complementation_group: Optional[str] = Field(default=None, description="""Complementation group designation (e.g., FA-A, FA-D1, BBS1). Used for genetically heterogeneous diseases where subtypes are historically named by complementation analysis.""", json_schema_extra = { "linkml_meta": {'alias': 'complementation_group', 'domain_of': ['GeneticContext']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class OnsetDescriptor(ConfiguredBaseModel):
    """
    Structured description of age of onset. Combines an HPO onset category with optional quantitative age data and notes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    onset_category: Optional[OnsetEnum] = Field(default=None, description="""HPO onset category (e.g., CHILDHOOD, NEONATAL). Use when an approximate developmental stage is known.""", json_schema_extra = { "linkml_meta": {'alias': 'onset_category', 'domain_of': ['OnsetDescriptor']} })
    mean_age_years: Optional[float] = Field(default=None, description="""Mean age of onset in years, as reported in a cohort study.""", json_schema_extra = { "linkml_meta": {'alias': 'mean_age_years', 'domain_of': ['OnsetDescriptor']} })
    min_age_years: Optional[float] = Field(default=None, description="""Minimum (earliest) age of onset in years.""", json_schema_extra = { "linkml_meta": {'alias': 'min_age_years', 'domain_of': ['OnsetDescriptor']} })
    max_age_years: Optional[float] = Field(default=None, description="""Maximum (latest) age of onset in years.""", json_schema_extra = { "linkml_meta": {'alias': 'max_age_years', 'domain_of': ['OnsetDescriptor']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class PhenotypeContext(ConfiguredBaseModel):
    """
    A context-specific annotation qualifying how a phenotype manifests under particular conditions. Each context can specify a genetic context, demographic stratum, or disease subtype, along with frequency, severity, onset, and supporting evidence specific to that context.
    When no context qualifier slots are set (no genetic_context, sex, population, age_range, or subtype), the context provides evidence for the overall/default frequency claim, addressing the evidence separation problem (issue #112).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'evidence': {'description': 'Evidence supporting the '
                                                    'frequency, severity, or onset '
                                                    'claims made in this specific '
                                                    'context. Distinct from the D2P '
                                                    'evidence on the parent Phenotype.',
                                     'name': 'evidence'},
                        'sex': {'name': 'sex', 'range': 'SexEnum'}}})

    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    severity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'severity',
         'domain_of': ['PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'alias': 'onset', 'domain_of': ['PhenotypeContext']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence supporting the frequency, severity, or onset claims made in this specific context. Distinct from the D2P evidence on the parent Phenotype.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    genetic_context: Optional[GeneticContext] = Field(default=None, description="""The genetic context under which this qualification applies. May specify genes, mutation types, zygosity, complementation groups, or complex genotypes.""", json_schema_extra = { "linkml_meta": {'alias': 'genetic_context', 'domain_of': ['PhenotypeContext']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Sex-specific stratum, if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'sex', 'domain_of': ['PhenotypeContext', 'Demographics']} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'alias': 'population',
         'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'age_range',
         'domain_of': ['PhenotypeContext', 'ProgressionInfo', 'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })


class Dataset(ConfiguredBaseModel):
    """
    A reference to a publicly available omics or phenotype dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Supports GEO, ArrayExpress, SRA, dbGaP, GTEx, ENCODE, '
                      'phenopacket-store, and other repositories'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'A description of the dataset. '
                                                       'This may typically be '
                                                       'redundant with the `title` '
                                                       'slot, but the description is '
                                                       'more human-readable and may be '
                                                       'used to communicate nuances '
                                                       'not captured by the rigid '
                                                       'standardization of the title '
                                                       'slot.',
                                        'name': 'description',
                                        'recommended': True}}})

    accession: str = Field(default=..., description="""Dataset accession identifier as a CURIE (e.g., geo:GSE67472)""", json_schema_extra = { "linkml_meta": {'alias': 'accession',
         'domain_of': ['Dataset'],
         'implements': ['linkml:authoritative_reference']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Dataset', 'PublicationReference'],
         'implements': ['linkml:title']} })
    description: Optional[str] = Field(default=None, description="""A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    organism: Optional[OrganismDescriptor] = Field(default=None, description="""The organism from which samples were derived""", json_schema_extra = { "linkml_meta": {'alias': 'organism', 'domain_of': ['Dataset']} })
    data_type: Optional[DatasetTypeEnum] = Field(default=None, description="""The type of omics or other data in the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'data_type', 'domain_of': ['Dataset']} })
    sample_types: Optional[list[SampleTypeDescriptor]] = Field(default=None, description="""Types of biological samples in the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'sample_types', 'domain_of': ['Dataset']} })
    sample_count: Optional[int] = Field(default=None, description="""Total number of samples in the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'sample_count', 'domain_of': ['Dataset']} })
    conditions: Optional[list[str]] = Field(default=None, description="""Experimental conditions or disease states represented""", json_schema_extra = { "linkml_meta": {'alias': 'conditions', 'domain_of': ['Dataset']} })
    exposures: Optional[list[ExposureDescriptor]] = Field(default=None, description="""Environmental exposures studied in the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'exposures', 'domain_of': ['Dataset']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genes',
         'domain_of': ['GeneticContext', 'Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    platform: Optional[str] = Field(default=None, description="""Sequencing or array platform used""", json_schema_extra = { "linkml_meta": {'alias': 'platform', 'domain_of': ['Dataset']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'alias': 'publication', 'domain_of': ['Dataset', 'ComputationalModel']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'alias': 'findings',
         'domain_of': ['Dataset', 'ComputationalModel', 'PublicationReference']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ClinicalTrial(ConfiguredBaseModel):
    """
    A clinical trial relevant to treatment or research of a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Uses NCT identifiers from ClinicalTrials.gov',
                      'Evidence and supporting text can be validated via '
                      'linkml-reference-validator against ClinicalTrials.gov API'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'Brief summary or key details '
                                                       'of the clinical trial',
                                        'name': 'description',
                                        'recommended': True},
                        'evidence': {'description': 'Supporting evidence with snippets '
                                                    'from trial documentation',
                                     'name': 'evidence',
                                     'recommended': False},
                        'name': {'description': 'NCT identifier (e.g., NCT00000001) or '
                                                'trial name',
                                 'identifier': False,
                                 'name': 'name'},
                        'phase': {'description': 'Trial phase (Phase I, Phase II, '
                                                 'Phase III, Phase IV, or Not '
                                                 'Applicable)',
                                  'name': 'phase',
                                  'range': 'ClinicalTrialPhaseEnum',
                                  'recommended': True},
                        'status': {'description': 'Recruitment or trial status (e.g., '
                                                  'Recruiting, Completed, Terminated, '
                                                  'Active not recruiting)',
                                   'name': 'status',
                                   'range': 'ClinicalTrialStatusEnum',
                                   'recommended': True}}})

    name: Optional[str] = Field(default=None, description="""NCT identifier (e.g., NCT00000001) or trial name""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, description="""Brief summary or key details of the clinical trial""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    phase: Optional[ClinicalTrialPhaseEnum] = Field(default=None, description="""Trial phase (Phase I, Phase II, Phase III, Phase IV, or Not Applicable)""", json_schema_extra = { "linkml_meta": {'alias': 'phase',
         'domain_of': ['ClinicalTrial', 'ProgressionInfo'],
         'examples': [{'value': 'Active TB'}],
         'recommended': True} })
    status: Optional[ClinicalTrialStatusEnum] = Field(default=None, description="""Recruitment or trial status (e.g., Recruiting, Completed, Terminated, Active not recruiting)""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['ClinicalTrial'],
         'examples': [{'value': 'Recruiting'},
                      {'value': 'Completed'},
                      {'value': 'Terminated'}],
         'recommended': True} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Supporting evidence with snippets from trial documentation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    target_phenotypes: Optional[list[PhenotypeDescriptor]] = Field(default=None, description="""Phenotypes that this treatment or trial addresses or targets""", json_schema_extra = { "linkml_meta": {'alias': 'target_phenotypes',
         'comments': ["Should reference phenotype names defined in the same disease's "
                      'phenotypes list',
                      'Enables linking treatments/trials to the '
                      'symptoms/manifestations they aim to manage',
                      'Each phenotype can include ontology term references (HP)'],
         'domain_of': ['ClinicalTrial', 'Treatment']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })


class ComputationalModel(ConfiguredBaseModel):
    """
    A computational or in-silico model relevant to understanding disease mechanisms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Covers genome-scale metabolic models, FBA, kinetic models, '
                      'digital twins, and ML models',
                      'Perturbations track gene knockouts or parameter changes used to '
                      'simulate the disease',
                      'Findings capture key predictions or insights the model can '
                      'generate'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    model_type: Optional[ComputationalModelTypeEnum] = Field(default=None, description="""Type of computational model""", json_schema_extra = { "linkml_meta": {'alias': 'model_type', 'domain_of': ['ComputationalModel']} })
    repository_url: Optional[str] = Field(default=None, description="""URL to model repository (GitHub, BiGG, VMH, BioModels)""", json_schema_extra = { "linkml_meta": {'alias': 'repository_url', 'domain_of': ['ComputationalModel']} })
    model_id: Optional[str] = Field(default=None, description="""Identifier within the repository (e.g., Recon3D, BIOMD0000000123)""", json_schema_extra = { "linkml_meta": {'alias': 'model_id', 'domain_of': ['ComputationalModel']} })
    base_model: Optional[str] = Field(default=None, description="""Parent/base model this is derived from (e.g., Recon3D, Harvey 1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'base_model', 'domain_of': ['ComputationalModel']} })
    perturbations: Optional[list[GeneDescriptor]] = Field(default=None, description="""Gene knockouts, reaction deletions, or parameter changes modeling the disease""", json_schema_extra = { "linkml_meta": {'alias': 'perturbations', 'domain_of': ['ComputationalModel']} })
    model_software: Optional[str] = Field(default=None, description="""Software/toolbox for running the model (e.g., COBRApy, COBRA Toolbox)""", json_schema_extra = { "linkml_meta": {'alias': 'model_software', 'domain_of': ['ComputationalModel']} })
    model_format: Optional[str] = Field(default=None, description="""File format (e.g., SBML, MATLAB, JSON, ONNX)""", json_schema_extra = { "linkml_meta": {'alias': 'model_format', 'domain_of': ['ComputationalModel']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'alias': 'publication', 'domain_of': ['Dataset', 'ComputationalModel']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'alias': 'findings',
         'domain_of': ['Dataset', 'ComputationalModel', 'PublicationReference']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DifferentialDiagnosis(ConfiguredBaseModel):
    """
    A disease or condition that presents similarly to the focal disease and must be differentiated
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Documents diseases/conditions with overlapping clinical '
                      'presentations',
                      'Includes distinguishing features to help differentiate from the '
                      'focal disease',
                      'Essential for clinical diagnostic accuracy'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'Clinical or mechanistic '
                                                       'overlaps, shared '
                                                       'presentations, and diagnostic '
                                                       'considerations with the focal '
                                                       'disease',
                                        'name': 'description'},
                        'distinguishing_features': {'description': 'Key clinical, '
                                                                   'laboratory, '
                                                                   'imaging, or '
                                                                   'epidemiological '
                                                                   'features that help '
                                                                   'differentiate this '
                                                                   'condition from the '
                                                                   'focal disease',
                                                    'name': 'distinguishing_features'},
                        'notes': {'description': 'Additional clinical notes or '
                                                 'management considerations',
                                  'name': 'notes'}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, description="""Clinical or mechanistic overlaps, shared presentations, and diagnostic considerations with the focal disease""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phenotypes',
         'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    distinguishing_features: Optional[list[str]] = Field(default=None, description="""Key clinical, laboratory, imaging, or epidemiological features that help differentiate this condition from the focal disease""", json_schema_extra = { "linkml_meta": {'alias': 'distinguishing_features', 'domain_of': ['DifferentialDiagnosis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, description="""Additional clinical notes or management considerations""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    disease_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO disease term for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'disease_term', 'domain_of': ['DifferentialDiagnosis', 'Disease']} })


class Subtype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    subtype_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO term for a disease subtype""", json_schema_extra = { "linkml_meta": {'alias': 'subtype_term', 'domain_of': ['Subtype']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locations', 'domain_of': ['Subtype', 'Pathophysiology']} })
    geography: Optional[list[GeographyTerm]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'geography',
         'domain_of': ['Subtype'],
         'examples': [{'value': "['Philippines']"}]} })


class EvidenceItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    reference: Optional[str] = Field(default=None, description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    supports: Optional[EvidenceItemSupportEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'supports',
         'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'SUPPORT'}]} })
    evidence_source: Optional[EvidenceSourceEnum] = Field(default=None, description="""Origin of the evidence item (human clinical, model organism, in vitro, or computational)""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_source',
         'domain_of': ['EvidenceItem'],
         'recommended': False} })
    snippet: Optional[str] = Field(default=None, description="""An exact excerpt/quote from the referenced publication that supports or refutes the claim""", json_schema_extra = { "linkml_meta": {'alias': 'snippet',
         'comments': ['This is automatically validated by the '
                      'linkml-reference-validator tool.'],
         'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'At the moment there is no healing therapy, so early '
                                'kidney transplant is a fundamental tool to improve '
                                'prognosis.'}],
         'implements': ['linkml:excerpt']} })
    explanation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'explanation',
         'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'There is no curative treatment for nephronophthisis, '
                                'indicating that supportive care, including '
                                'symptomatic treatment and monitoring, is currently '
                                'applied to manage associated complications.'}]} })


class CausalEdge(ConfiguredBaseModel):
    """
    A reference to a downstream effect or consequence in a causal relationship
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    target: str = Field(default=..., description="""The name of the target element in a causal relationship""", json_schema_extra = { "linkml_meta": {'alias': 'target', 'domain_of': ['CausalEdge']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class PublicationReference(ConfiguredBaseModel):
    """
    A reference to a publication with associated findings
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'reference': {'identifier': True,
                                      'name': 'reference',
                                      'required': True}}})

    reference: str = Field(default=..., description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Dataset', 'PublicationReference'],
         'implements': ['linkml:title']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'alias': 'findings',
         'domain_of': ['Dataset', 'ComputationalModel', 'PublicationReference']} })


class Finding(ConfiguredBaseModel):
    """
    A key finding or claim extracted from a source (publication or dataset)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    statement: str = Field(default=..., description="""A key finding or claim from the publication""", json_schema_extra = { "linkml_meta": {'alias': 'statement', 'domain_of': ['Finding']} })
    supporting_text: Optional[str] = Field(default=None, description="""Exact excerpt/quote from the publication supporting the statement""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text', 'domain_of': ['Finding']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class Prevalence(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'alias': 'population',
         'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    percentage: Optional[Union[float, int, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'percentage',
         'any_of': [{'range': 'float'},
                    {'range': 'integer'},
                    {'description': 'for ranges', 'range': 'string'}],
         'domain_of': ['Prevalence'],
         'examples': [{'value': '0.1'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ProgressionInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    phase: Optional[PhaseTerm] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phase',
         'domain_of': ['ClinicalTrial', 'ProgressionInfo'],
         'examples': [{'value': 'Active TB'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'age_range',
         'domain_of': ['PhenotypeContext', 'ProgressionInfo', 'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    incubation_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'incubation_days',
         'domain_of': ['ProgressionInfo'],
         'examples': [{'value': '3-14'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    incubation_years: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'incubation_years',
         'domain_of': ['ProgressionInfo'],
         'examples': [{'value': '2-15'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    duration_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'duration_days',
         'domain_of': ['ProgressionInfo'],
         'examples': [{'value': '2-5'}]} })
    duration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'duration',
         'domain_of': ['ProgressionInfo'],
         'examples': [{'value': 'Variable'}]} })


class EpidemiologyInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    minimum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'minimum_value', 'domain_of': ['EpidemiologyInfo']} })
    maximum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'maximum_value', 'domain_of': ['EpidemiologyInfo']} })
    mean_range: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mean_range', 'domain_of': ['EpidemiologyInfo']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    factors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'factors',
         'domain_of': ['EpidemiologyInfo'],
         'examples': [{'value': "['Genetic', 'Environmental', 'Infectious', "
                                "'Autoimmune', 'Metabolic', 'Neoplastic', 'Traumatic', "
                                "'Iatrogenic', 'Idiopathic']"}]} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'domain_of': ['EpidemiologyInfo'],
         'examples': [{'value': 'cm'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class Pathophysiology(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    biological_processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'biological_processes',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: TNF-alpha Production}]'}]} })
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locations', 'domain_of': ['Subtype', 'Pathophysiology']} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'examples',
         'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role',
         'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'synonyms',
         'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    consequence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'consequence',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': 'Leads to abnormal sexual development and bone '
                                'maturation.'}]} })
    consequences: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'consequences',
         'domain_of': ['Pathophysiology'],
         'todos': ['unify consequences and consequence']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'domain_of': ['GeneticContext', 'Pathophysiology', 'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    pathways: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pathways',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Wnt Pathway}]'}]} })
    downstream: Optional[list[CausalEdge]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'downstream',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{target: Tissue Damage}]'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genes',
         'domain_of': ['GeneticContext', 'Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    subtypes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtypes',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': "['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4']"}]} })
    cellular_components: Optional[list[CellularComponentDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cellular_components',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Peroxisome}]'}]} })
    protein_complexes: Optional[list[ProteinComplexDescriptor]] = Field(default=None, description="""Protein complexes that gene products participate in""", json_schema_extra = { "linkml_meta": {'alias': 'protein_complexes',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: FA nuclear complex, term: {id: '
                                '"GO:0043240", label: "Fanconi anaemia nuclear '
                                'complex"}}]'}]} })
    chemical_entities: Optional[list[ChemicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'chemical_entities',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Plasmalogen}]'}]} })
    gene_products: Optional[list[GeneProductDescriptor]] = Field(default=None, description="""Gene products (proteins, fusion proteins, oncoproteins) involved in this pathophysiology mechanism. Use NCIT terms for specific proteins.""", json_schema_extra = { "linkml_meta": {'alias': 'gene_products',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: BCR-ABL1 fusion protein, term: {id: '
                                'NCIT:C16325, label: BCR/ABL1 Fusion Protein}}]'}]} })
    triggers: Optional[list[TriggerDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'triggers',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Viral Infections}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'assays',
         'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    mechanisms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mechanisms',
         'domain_of': ['Pathophysiology'],
         'examples': [{'value': "['Thrombocytopenia', 'Platelet Dysfunction', "
                                "'Disseminated Intravascular Coagulation (DIC)']"}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })


class Phenotype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    phenotype_term: Optional[PhenotypeDescriptor] = Field(default=None, description="""The HP term for this phenotype""", json_schema_extra = { "linkml_meta": {'alias': 'phenotype_term', 'domain_of': ['Phenotype']} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    diagnostic: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'diagnostic', 'domain_of': ['Phenotype', 'HistopathologyFinding']} })
    sequelae: Optional[list[CausalEdge]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequelae',
         'domain_of': ['Phenotype'],
         'examples': [{'value': '[{target: Diabetic Ketoacidosis}, {target: Chronic '
                                'Complications}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    severity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'severity',
         'domain_of': ['PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    phenotype_contexts: Optional[list[PhenotypeContext]] = Field(default=None, description="""Context-specific qualifications of this phenotype's frequency, severity, or onset. Each context can optionally specify a genetic context, demographic stratum, or disease subtype. When no context qualifiers are set, provides evidence for the base frequency/severity claim (addressing the frequency-evidence separation problem).""", json_schema_extra = { "linkml_meta": {'alias': 'phenotype_contexts', 'domain_of': ['Phenotype']} })


class Biochemical(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    biomarker_term: Optional[BiomarkerDescriptor] = Field(default=None, description="""Ontology term for a biomarker (from NCIT)""", json_schema_extra = { "linkml_meta": {'alias': 'biomarker_term',
         'comments': ['Use NCIT terms for biomarkers (proteins, genes, fusion '
                      'products)',
                      'NCIT:C16342 (Biomarker) is the root class for validation'],
         'domain_of': ['Biochemical']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'presence',
         'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    specificity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'specificity',
         'domain_of': ['Biochemical'],
         'examples': [{'value': 'High'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'assays',
         'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'synonyms',
         'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })


class HistopathologyFinding(ConfiguredBaseModel):
    """
    A histopathologic finding from microscopic examination of tissue. Includes morphologic features, architectural patterns, cellular characteristics, growth patterns, and histologic grading.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["{'For cancers': 'tumor grade, differentiation, growth patterns, "
                      "necrosis, rosettes'}",
                      "{'For other diseases': 'inflammatory infiltrates, architectural "
                      "distortion, fibrosis'}",
                      'Separate from phenotypes as these are microscopic observations '
                      'requiring biopsy'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'context': {'description': 'Context in which this finding is '
                                                   'observed (e.g., specific subtype)',
                                    'name': 'context'},
                        'description': {'description': 'Detailed description of the '
                                                       'finding and its clinical '
                                                       'significance',
                                        'name': 'description'},
                        'diagnostic': {'description': 'Whether this finding is '
                                                      'pathognomonic or highly '
                                                      'diagnostic',
                                       'name': 'diagnostic'},
                        'frequency': {'description': 'How frequently this finding is '
                                                     'observed in the disease',
                                      'name': 'frequency'},
                        'name': {'description': 'Name of the histopathologic finding',
                                 'examples': [{'value': 'Flexner-Wintersteiner '
                                                        'Rosettes'},
                                              {'value': 'Spindle Cell Morphology'},
                                              {'value': 'High Grade (Fuhrman Grade '
                                                        '3-4)'}],
                                 'name': 'name'}}})

    name: str = Field(default=..., description="""Name of the histopathologic finding""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Flexner-Wintersteiner Rosettes'},
                      {'value': 'Spindle Cell Morphology'},
                      {'value': 'High Grade (Fuhrman Grade 3-4)'}]} })
    finding_term: Optional[HistopathologyFindingDescriptor] = Field(default=None, description="""Ontology term for a histopathologic finding (from NCIT or HP)""", json_schema_extra = { "linkml_meta": {'alias': 'finding_term',
         'comments': ['Use NCIT terms from Morphologic Finding (C35867) or Histologic '
                      'Grade (C18000)',
                      'Use HP terms for rosettes and cell morphology abnormalities '
                      '(HP:0025461 descendants)'],
         'domain_of': ['HistopathologyFinding']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the finding and its clinical significance""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, description="""How frequently this finding is observed in the disease""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    diagnostic: Optional[bool] = Field(default=None, description="""Whether this finding is pathognomonic or highly diagnostic""", json_schema_extra = { "linkml_meta": {'alias': 'diagnostic', 'domain_of': ['Phenotype', 'HistopathologyFinding']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, description="""Context in which this finding is observed (e.g., specific subtype)""", json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })


class Genetic(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    gene_term: Optional[GeneDescriptor] = Field(default=None, description="""The HGNC term for this gene""", json_schema_extra = { "linkml_meta": {'alias': 'gene_term', 'domain_of': ['Genetic']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'presence',
         'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    association: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'association',
         'domain_of': ['Genetic'],
         'examples': [{'value': 'Susceptibility'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subtype',
         'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'inheritance',
         'domain_of': ['Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    variants: Optional[list[Variant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'variants',
         'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    features: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'features',
         'domain_of': ['Genetic'],
         'examples': [{'value': 'DNA virus from the Orthopoxvirus genus'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'examples',
         'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })


class Environmental(ConfiguredBaseModel):
    """
    An environmental factor, exposure, or context relevant to disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'presence',
         'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    chemicals: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'chemicals',
         'domain_of': ['Environmental'],
         'examples': [{'value': "['Phenol']"}]} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'synonyms',
         'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'effect',
         'domain_of': ['Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'examples',
         'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    exposure_term: Optional[ExposureDescriptor] = Field(default=None, description="""The ECTO/XCO term for this exposure event""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_term', 'domain_of': ['Environmental']} })
    environment_context: Optional[EnvironmentDescriptor] = Field(default=None, description="""The ENVO term for the environmental context/setting""", json_schema_extra = { "linkml_meta": {'alias': 'environment_context', 'domain_of': ['Environmental']} })


class Disease(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'name': {'description': 'Preferred name for the disease',
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""Preferred name for the disease""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    disease_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO disease term for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'disease_term', 'domain_of': ['DifferentialDiagnosis', 'Disease']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    references: Optional[list[PublicationReference]] = Field(default=None, description="""Top-level list of references with their key findings for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['Disease']} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    parents: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'parents',
         'domain_of': ['Disease'],
         'examples': [{'value': "['Bacterial Infection']"}]} })
    has_subtypes: Optional[list[Subtype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_subtypes', 'domain_of': ['Disease', 'InfectiousAgent']} })
    prevalence: Optional[list[Prevalence]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'prevalence', 'domain_of': ['Disease']} })
    progression: Optional[list[ProgressionInfo]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'progression', 'domain_of': ['Disease']} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pathophysiology',
         'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phenotypes',
         'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    histopathology: Optional[list[HistopathologyFinding]] = Field(default=None, description="""Histopathologic findings including microscopic morphology, architectural patterns, cellular features, growth patterns, and histologic grading.""", json_schema_extra = { "linkml_meta": {'alias': 'histopathology',
         'comments': ['Separate from phenotypes as these are tissue-level microscopic '
                      'observations',
                      'Use NCIT Morphologic Finding (C35867) or Histologic Grade '
                      '(C18000) terms',
                      "{'For cancer': 'includes grade, differentiation, growth "
                      "patterns, necrosis'}",
                      "{'For other diseases': 'may include architectural changes, "
                      "cellular infiltrates'}"],
         'domain_of': ['Disease']} })
    biochemical: Optional[list[Biochemical]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'biochemical', 'domain_of': ['Disease']} })
    stages: Optional[list[Stage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'stages', 'domain_of': ['Disease']} })
    genetic: Optional[list[Genetic]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genetic', 'domain_of': ['Disease']} })
    variants: Optional[list[Variant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'variants',
         'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    environmental: Optional[list[Environmental]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'environmental', 'domain_of': ['Disease']} })
    treatments: Optional[list[Treatment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'treatments', 'domain_of': ['Disease']} })
    categories: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'categories', 'domain_of': ['Disease']} })
    infectious_agent: Optional[list[InfectiousAgent]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'infectious_agent', 'domain_of': ['Disease']} })
    agent_life_cycle: Optional[AgentLifeCycle] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'agent_life_cycle', 'domain_of': ['Disease']} })
    transmission: Optional[list[Transmission]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'transmission', 'domain_of': ['Disease']} })
    modeling_considerations: Optional[list[ModelingConsideration]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'modeling_considerations', 'domain_of': ['Disease']} })
    epidemiology: Optional[list[EpidemiologyInfo]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'epidemiology',
         'domain_of': ['Disease'],
         'examples': [{'value': "['Global']"}]} })
    diagnosis: Optional[list[Diagnosis]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'diagnosis', 'domain_of': ['Disease']} })
    differential_diagnoses: Optional[list[DifferentialDiagnosis]] = Field(default=None, description="""Differential diagnoses - similar diseases that must be ruled out""", json_schema_extra = { "linkml_meta": {'alias': 'differential_diagnoses',
         'domain_of': ['Disease'],
         'recommended': False} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'synonyms',
         'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'inheritance',
         'domain_of': ['Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    animal_models: Optional[list[AnimalModel]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'animal_models', 'domain_of': ['Disease']} })
    datasets: Optional[list[Dataset]] = Field(default=None, description="""Publicly available datasets relevant to disease research""", json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['Disease'], 'recommended': True} })
    clinical_trials: Optional[list[ClinicalTrial]] = Field(default=None, description="""Clinical trials relevant to disease treatment and research""", json_schema_extra = { "linkml_meta": {'alias': 'clinical_trials', 'domain_of': ['Disease'], 'recommended': False} })
    computational_models: Optional[list[ComputationalModel]] = Field(default=None, description="""Computational models (metabolic, mechanistic, ML, digital twins) for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'computational_models', 'domain_of': ['Disease']} })
    classifications: Optional[DiseaseClassifications] = Field(default=None, description="""Classification assignments for this disease from various nosologies""", json_schema_extra = { "linkml_meta": {'alias': 'classifications', 'domain_of': ['Disease']} })
    definitions: Optional[list[Definition]] = Field(default=None, description="""Definitions or diagnostic criteria for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'definitions', 'domain_of': ['Disease']} })
    mappings: Optional[DiseaseMappings] = Field(default=None, description="""External identifier mappings for this disease (SSSOM-inspired)""", json_schema_extra = { "linkml_meta": {'alias': 'mappings', 'domain_of': ['Disease']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    curation_history: Optional[list[CurationEvent]] = Field(default=None, description="""Audit trail of AI-assisted curation events""", json_schema_extra = { "linkml_meta": {'alias': 'curation_history', 'domain_of': ['Disease']} })


class Stage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role',
         'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'examples',
         'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pathophysiology',
         'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })
    substages: Optional[list[Stage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'substages', 'domain_of': ['Stage']} })


class AgentLifeCycle(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    life_cycle_stages: Optional[list[AgentLifeCycleStage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'life_cycle_stages', 'domain_of': ['AgentLifeCycle']} })
    hosts: Optional[list[HostDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hosts',
         'comments': ['Use NCBITaxon terms for host organisms',
                      'Use the role slot to indicate definitive, intermediate, '
                      'reservoir, or accidental host'],
         'domain_of': ['AgentLifeCycle']} })
    vectors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'vectors', 'domain_of': ['AgentLifeCycle']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })


class AgentLifeCycleStage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    life_cycle_stage_term: Optional[LifeCycleStageDescriptor] = Field(default=None, description="""The OPL term for this agent life cycle stage""", json_schema_extra = { "linkml_meta": {'alias': 'life_cycle_stage_term', 'domain_of': ['AgentLifeCycleStage']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })


class AnimalModel(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    species: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'species',
         'domain_of': ['AnimalModel'],
         'examples': [{'value': 'Human'}]} })
    genotype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genotype',
         'domain_of': ['AnimalModel'],
         'examples': [{'value': 'HLA-DQ2'}]} })
    background: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'background', 'domain_of': ['AnimalModel']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genes',
         'domain_of': ['GeneticContext', 'Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    alleles: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alleles', 'domain_of': ['AnimalModel']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    associated_phenotypes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'associated_phenotypes',
         'domain_of': ['AnimalModel'],
         'examples': [{'value': "['Celiac Disease', 'Type 1 Diabetes', 'Autoimmune "
                                "Thyroid Disease']"}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class Treatment(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    treatment_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this treatment/medical action""", json_schema_extra = { "linkml_meta": {'alias': 'treatment_term', 'domain_of': ['Treatment']} })
    regimen_term: Optional[RegimenDescriptor] = Field(default=None, description="""The NCIT term for this treatment regimen""", json_schema_extra = { "linkml_meta": {'alias': 'regimen_term', 'domain_of': ['Treatment']} })
    target_phenotypes: Optional[list[PhenotypeDescriptor]] = Field(default=None, description="""Phenotypes that this treatment or trial addresses or targets""", json_schema_extra = { "linkml_meta": {'alias': 'target_phenotypes',
         'comments': ["Should reference phenotype names defined in the same disease's "
                      'phenotypes list',
                      'Enables linking treatments/trials to the '
                      'symptoms/manifestations they aim to manage',
                      'Each phenotype can include ontology term references (HP)'],
         'domain_of': ['ClinicalTrial', 'Treatment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context',
         'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'review_notes',
         'domain_of': ['ClinicalTrial',
                       'Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role',
         'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    mechanism: Optional[list[Mechanism]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mechanism', 'domain_of': ['Treatment']} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'examples',
         'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })


class InfectiousAgent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    infectious_agent_term: Optional[OrganismDescriptor] = Field(default=None, description="""The NCBITaxon term for this infectious agent""", json_schema_extra = { "linkml_meta": {'alias': 'infectious_agent_term', 'domain_of': ['InfectiousAgent']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    has_subtypes: Optional[list[Subtype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_subtypes', 'domain_of': ['Disease', 'InfectiousAgent']} })


class Transmission(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'effect',
         'domain_of': ['Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })


class Assay(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })


class Diagnosis(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    diagnosis_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this diagnostic procedure""", json_schema_extra = { "linkml_meta": {'alias': 'diagnosis_term',
         'comments': ['MAXO includes diagnostic procedures under medical actions',
                      'Use qualifiers with UBERON terms to specify anatomical location '
                      '(e.g., right heart catheterization)'],
         'domain_of': ['Diagnosis']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'presence',
         'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    results: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'results',
         'domain_of': ['Diagnosis'],
         'examples': [{'value': 'Identifies MEFV mutations'}]} })
    markers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'markers',
         'domain_of': ['Diagnosis'],
         'examples': [{'value': 'CRP, ESR, SAA'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })


class Inheritance(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    inheritance_term: Optional[InheritanceDescriptor] = Field(default=None, description="""The HPO mode of inheritance term for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'alias': 'inheritance_term', 'domain_of': ['Inheritance']} })
    penetrance: Optional[PenetranceEnum] = Field(default=None, description="""Penetrance classification for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'alias': 'penetrance', 'domain_of': ['Inheritance']} })
    penetrance_percentage: Optional[str] = Field(default=None, description="""Estimated penetrance percentage or range (e.g., 80-90)""", json_schema_extra = { "linkml_meta": {'alias': 'penetrance_percentage', 'domain_of': ['Inheritance']} })
    expressivity: Optional[ExpressivityEnum] = Field(default=None, description="""Expressivity classification for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'alias': 'expressivity', 'domain_of': ['Inheritance']} })
    de_novo_rate: Optional[str] = Field(default=None, description="""Estimated percentage of de novo cases (e.g., 80)""", json_schema_extra = { "linkml_meta": {'alias': 'de_novo_rate', 'domain_of': ['Inheritance']} })
    parent_of_origin_effect: Optional[str] = Field(default=None, description="""Parent-of-origin effect or bias (e.g., paternal age effect)""", json_schema_extra = { "linkml_meta": {'alias': 'parent_of_origin_effect', 'domain_of': ['Inheritance']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })


class Variant(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'domain_of': ['GeneticContext', 'Pathophysiology', 'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    functional_effects: Optional[list[FunctionalEffect]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'functional_effects', 'domain_of': ['Variant']} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'synonyms',
         'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    identifiers: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'identifiers', 'domain_of': ['Variant']} })
    sequence_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_length', 'domain_of': ['Variant']} })
    clinical_significance: Optional[ClinicalSignificanceEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'clinical_significance', 'domain_of': ['Variant']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Variant', 'FunctionalEffect']} })


class FunctionalEffect(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    function: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'function', 'domain_of': ['FunctionalEffect']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Variant', 'FunctionalEffect']} })


class Mechanism(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })


class ModelingConsideration(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class ClassificationAssignment(ConfiguredBaseModel):
    """
    Base class for classification assignments with evidence
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ICDOMorphologyAssignment(ClassificationAssignment):
    """
    ICD-O morphology classification assignment for neoplastic diseases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'ICDOMorphologyEnum',
                                                 'required': True}}})

    classification_value: ICDOMorphologyEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class HarrisonsChapterAssignment(ClassificationAssignment):
    """
    Harrison's internal medicine chapter classification assignment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'HarrisonsChapterEnum',
                                                 'required': True}}})

    classification_value: HarrisonsChapterEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class LysosomalStorageAssignment(ClassificationAssignment):
    """
    Lysosomal storage disease biochemical classification assignment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'LysosomalStorageEnum',
                                                 'required': True}}})

    classification_value: LysosomalStorageEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class MechanisticNosologyAssignment(ClassificationAssignment):
    """
    Mechanistic/pathway-based disease classification assignment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'MechanisticNosologyEnum',
                                                 'required': True}}})

    classification_value: MechanisticNosologyEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class IUISAssignment(ClassificationAssignment):
    """
    IUIS primary immunodeficiency classification assignment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'IUISCategoryEnum',
                                                 'required': True}}})

    classification_value: IUISCategoryEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ChannelopathyAssignment(ClassificationAssignment):
    """
    Channelopathy organ system classification assignment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'classification_value': {'name': 'classification_value',
                                                 'range': 'ChannelopathyOrganSystemEnum',
                                                 'required': True}}})

    classification_value: ChannelopathyOrganSystemEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'alias': 'classification_value',
         'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DiseaseClassifications(ConfiguredBaseModel):
    """
    Container for all classification assignments for a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    icdo_morphology: Optional[ICDOMorphologyAssignment] = Field(default=None, description="""ICD-O morphology classification (for neoplastic diseases)""", json_schema_extra = { "linkml_meta": {'alias': 'icdo_morphology', 'domain_of': ['DiseaseClassifications']} })
    harrisons_chapter: Optional[list[HarrisonsChapterAssignment]] = Field(default=None, description="""Harrison's internal medicine chapter classification""", json_schema_extra = { "linkml_meta": {'alias': 'harrisons_chapter', 'domain_of': ['DiseaseClassifications']} })
    lysosomal_storage_category: Optional[LysosomalStorageAssignment] = Field(default=None, description="""Lysosomal storage disease biochemical classification""", json_schema_extra = { "linkml_meta": {'alias': 'lysosomal_storage_category', 'domain_of': ['DiseaseClassifications']} })
    mechanistic_category: Optional[list[MechanisticNosologyAssignment]] = Field(default=None, description="""Mechanistic/pathway-based disease classification""", json_schema_extra = { "linkml_meta": {'alias': 'mechanistic_category', 'domain_of': ['DiseaseClassifications']} })
    iuis_category: Optional[IUISAssignment] = Field(default=None, description="""IUIS primary immunodeficiency classification""", json_schema_extra = { "linkml_meta": {'alias': 'iuis_category', 'domain_of': ['DiseaseClassifications']} })
    channelopathy_category: Optional[ChannelopathyAssignment] = Field(default=None, description="""Channelopathy organ system classification""", json_schema_extra = { "linkml_meta": {'alias': 'channelopathy_category', 'domain_of': ['DiseaseClassifications']} })


class Definition(ConfiguredBaseModel):
    """
    A diagnostic or phenotype definition for the disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'definition_type': {'name': 'definition_type',
                                            'required': True},
                        'name': {'name': 'name', 'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    definition_type: DefinitionTypeEnum = Field(default=..., description="""The type of definition or criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'definition_type', 'domain_of': ['Definition']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    scope: Optional[str] = Field(default=None, description="""Scope or population for which the definition applies (e.g., adults, pediatrics)""", json_schema_extra = { "linkml_meta": {'alias': 'scope', 'domain_of': ['Definition', 'CriteriaSet']} })
    criteria_sets: Optional[list[CriteriaSet]] = Field(default=None, description="""Named criteria groupings within a definition""", json_schema_extra = { "linkml_meta": {'alias': 'criteria_sets', 'domain_of': ['Definition']} })
    inclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Inclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'inclusion_criteria', 'domain_of': ['Definition', 'CriteriaSet']} })
    exclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Exclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'exclusion_criteria', 'domain_of': ['Definition', 'CriteriaSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class CriteriaSet(ConfiguredBaseModel):
    """
    A named criteria grouping within a definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    scope: Optional[str] = Field(default=None, description="""Scope or population for which the definition applies (e.g., adults, pediatrics)""", json_schema_extra = { "linkml_meta": {'alias': 'scope', 'domain_of': ['Definition', 'CriteriaSet']} })
    minimum_required: Optional[int] = Field(default=None, description="""Minimum number of criteria required in this criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'minimum_required', 'domain_of': ['CriteriaSet']} })
    core_clinical_characteristics: Optional[list[CriteriaItem]] = Field(default=None, description="""Core clinical characteristics used in a criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'core_clinical_characteristics', 'domain_of': ['CriteriaSet']} })
    inclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Inclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'inclusion_criteria', 'domain_of': ['Definition', 'CriteriaSet']} })
    exclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Exclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'exclusion_criteria', 'domain_of': ['Definition', 'CriteriaSet']} })
    imaging_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Imaging requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'imaging_requirements', 'domain_of': ['CriteriaSet']} })
    laboratory_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Laboratory or serologic requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'laboratory_requirements', 'domain_of': ['CriteriaSet']} })
    additional_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Additional requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'alias': 'additional_requirements', 'domain_of': ['CriteriaSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class CriteriaItem(Descriptor):
    """
    A criterion element (clinical feature, test result, imaging requirement)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class TermMapping(ConfiguredBaseModel):
    """
    Mapping from this disease entry to an external term or code
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'mapping_predicate': {'name': 'mapping_predicate',
                                              'required': True},
                        'term': {'name': 'term', 'required': True}}})

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_predicate', 'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_source', 'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_justification', 'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'alias': 'consistency', 'domain_of': ['TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ICD10CMMapping(TermMapping):
    """
    ICD-10-CM diagnosis code mapping
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ICD10CMTerm'}],
                                 'name': 'term'}}})

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ICD10CMTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_predicate', 'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_source', 'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_justification', 'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'alias': 'consistency', 'domain_of': ['TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ICD11FMapping(TermMapping):
    """
    ICD-11 Foundation diagnosis code mapping
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ICD11FTerm'}],
                                 'name': 'term'}}})

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ICD11FTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_predicate', 'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_source', 'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_justification', 'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'alias': 'consistency', 'domain_of': ['TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class MondoMapping(TermMapping):
    """
    MONDO disease ontology mapping
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'DiseaseTerm'}],
                                 'name': 'term'}}})

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_predicate', 'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_source', 'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_justification', 'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'alias': 'consistency', 'domain_of': ['TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class MappingConsistency(ConfiguredBaseModel):
    """
    Consistency assertion for a mapping relative to another source
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'consistent': {'name': 'consistent', 'required': True},
                        'reference': {'description': 'Reference source used to assess '
                                                     'consistency (e.g., MONDO)',
                                      'name': 'reference',
                                      'range': 'string',
                                      'required': True}}})

    reference: str = Field(default=..., description="""Reference source used to assess consistency (e.g., MONDO)""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    consistent: MappingConsistencyEnum = Field(default=..., description="""Consistency status for a mapping relative to a reference source""", json_schema_extra = { "linkml_meta": {'alias': 'consistent', 'domain_of': ['MappingConsistency']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DiseaseMappings(ConfiguredBaseModel):
    """
    Container for external identifier mappings for a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    icd10cm_mappings: Optional[list[ICD10CMMapping]] = Field(default=None, description="""ICD-10-CM code mappings for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'icd10cm_mappings', 'domain_of': ['DiseaseMappings']} })
    icd11f_mappings: Optional[list[ICD11FMapping]] = Field(default=None, description="""ICD-11 Foundation code mappings for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'icd11f_mappings', 'domain_of': ['DiseaseMappings']} })
    mondo_mappings: Optional[list[MondoMapping]] = Field(default=None, description="""MONDO disease ontology mappings for this disease""", json_schema_extra = { "linkml_meta": {'alias': 'mondo_mappings', 'domain_of': ['DiseaseMappings']} })


class ConditionDescriptor(Descriptor):
    """
    A descriptor for a condition or disease, optionally bound to MONDO. External coding identifiers (ICD-10, OMOP, SNOMED, etc.) are captured on association signals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'preferred_term': {'name': 'preferred_term', 'required': False},
                        'slug': {'description': 'Use for leaf conditions; omit when '
                                                'using composition/components',
                                 'name': 'slug',
                                 'required': False},
                        'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'OPTIONAL',
                                               'range': 'DiseaseTerm'}],
                                 'description': 'Optional MONDO disease term reference',
                                 'name': 'term'}}})

    slug: Optional[str] = Field(default=None, description="""Use for leaf conditions; omit when using composition/components""", json_schema_extra = { "linkml_meta": {'alias': 'slug', 'domain_of': ['ConditionDescriptor']} })
    preferred_term: Optional[str] = Field(default=None, description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MONDO disease term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'OPTIONAL',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    composition: Optional[ConditionCompositionEnum] = Field(default=None, description="""Composition type for a composite condition descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'composition', 'domain_of': ['ConditionDescriptor']} })
    components: Optional[list[ConditionDescriptor]] = Field(default=None, description="""Component conditions that make up a composite descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'components', 'domain_of': ['ConditionDescriptor']} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'alias': 'modifier', 'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'alias': 'located_in', 'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality', 'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ComorbidityAssociation(ConfiguredBaseModel):
    """
    An association between two conditions, including directionality, evidence, and computational characterizations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ComorbidityAssociation'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    disease_a: Optional[ConditionDescriptor] = Field(default=None, description="""First disease in a comorbidity pair""", json_schema_extra = { "linkml_meta": {'alias': 'disease_a', 'domain_of': ['ComorbidityAssociation']} })
    disease_b: Optional[ConditionDescriptor] = Field(default=None, description="""Second disease in a comorbidity pair""", json_schema_extra = { "linkml_meta": {'alias': 'disease_b', 'domain_of': ['ComorbidityAssociation']} })
    directionality: Optional[ComorbidityDirectionEnum] = Field(default=None, description="""Direction of a comorbidity/trajectory association""", json_schema_extra = { "linkml_meta": {'alias': 'directionality',
         'domain_of': ['ComorbidityAssociation', 'AssociationSignal']} })
    association_signals: Optional[list[AssociationSignal]] = Field(default=None, description="""Association signals from EHR, registry, or computational sources""", json_schema_extra = { "linkml_meta": {'alias': 'association_signals', 'domain_of': ['ComorbidityAssociation']} })
    literature_evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Literature-based evidence items for this association""", json_schema_extra = { "linkml_meta": {'alias': 'literature_evidence', 'domain_of': ['ComorbidityAssociation']} })
    hypotheses: Optional[list[ComorbidityHypothesis]] = Field(default=None, description="""Mechanistic or causal hypotheses about the association""", json_schema_extra = { "linkml_meta": {'alias': 'hypotheses', 'domain_of': ['ComorbidityAssociation']} })
    shared_upstream_hypotheses: Optional[list[UpstreamConditionHypothesis]] = Field(default=None, description="""Suspected upstream conditions that may explain both A and B""", json_schema_extra = { "linkml_meta": {'alias': 'shared_upstream_hypotheses', 'domain_of': ['ComorbidityAssociation']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phenotypes',
         'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    curation_status: Optional[CurationStatusEnum] = Field(default=None, description="""Curation workflow status""", json_schema_extra = { "linkml_meta": {'alias': 'curation_status', 'domain_of': ['ComorbidityAssociation']} })


class AssociationSignal(ConfiguredBaseModel):
    """
    An association signal from EHR, registry, or computational sources, optionally stratified by sex, age, or cohort.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'method': {'name': 'method',
                                   'range': 'AssociationSignalMethodEnum'},
                        'source': {'name': 'source',
                                   'range': 'AssociationSignalSourceEnum'}}})

    source: Optional[AssociationSignalSourceEnum] = Field(default=None, description="""Source dataset or provenance label""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['AssociationSignal']} })
    method: Optional[AssociationSignalMethodEnum] = Field(default=None, description="""Method or pipeline name""", json_schema_extra = { "linkml_meta": {'alias': 'method', 'domain_of': ['AssociationSignal', 'GOEnrichment']} })
    signal_disorder_a_id: Optional[str] = Field(default=None, description="""Original identifier for disorder A in this signal (CURIE, e.g., ICD10:E12)""", json_schema_extra = { "linkml_meta": {'alias': 'signal_disorder_a_id', 'domain_of': ['AssociationSignal']} })
    signal_disorder_b_id: Optional[str] = Field(default=None, description="""Original identifier for disorder B in this signal (CURIE, e.g., ICD10:L28)""", json_schema_extra = { "linkml_meta": {'alias': 'signal_disorder_b_id', 'domain_of': ['AssociationSignal']} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'alias': 'population',
         'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    demographics: Optional[Demographics] = Field(default=None, description="""Demographic stratification for an association signal""", json_schema_extra = { "linkml_meta": {'alias': 'demographics', 'domain_of': ['AssociationSignal']} })
    mapping_notes: Optional[str] = Field(default=None, description="""Notes on code-to-concept mapping decisions for this signal""", json_schema_extra = { "linkml_meta": {'alias': 'mapping_notes', 'domain_of': ['AssociationSignal']} })
    directionality: Optional[ComorbidityDirectionEnum] = Field(default=None, description="""Direction of a comorbidity/trajectory association""", json_schema_extra = { "linkml_meta": {'alias': 'directionality',
         'domain_of': ['ComorbidityAssociation', 'AssociationSignal']} })
    a_before_b: Optional[float] = Field(default=None, description="""Probability or fraction of A before B in an EHR signal""", json_schema_extra = { "linkml_meta": {'alias': 'a_before_b', 'domain_of': ['AssociationSignal']} })
    b_before_a: Optional[float] = Field(default=None, description="""Probability or fraction of B before A in an EHR signal""", json_schema_extra = { "linkml_meta": {'alias': 'b_before_a', 'domain_of': ['AssociationSignal']} })
    same_time: Optional[float] = Field(default=None, description="""Probability or fraction of A and B occurring in the same time window""", json_schema_extra = { "linkml_meta": {'alias': 'same_time', 'domain_of': ['AssociationSignal']} })
    metrics: Optional[list[AssociationMetric]] = Field(default=None, description="""Quantitative association metrics""", json_schema_extra = { "linkml_meta": {'alias': 'metrics',
         'domain_of': ['AssociationSignal', 'AssociationStatistics']} })
    statistics: Optional[AssociationStatistics] = Field(default=None, description="""Statistical summary for an association signal""", json_schema_extra = { "linkml_meta": {'alias': 'statistics', 'domain_of': ['AssociationSignal']} })
    go_enrichment: Optional[GOEnrichment] = Field(default=None, description="""GO enrichment results associated with a signal""", json_schema_extra = { "linkml_meta": {'alias': 'go_enrichment', 'domain_of': ['AssociationSignal']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Demographics(ConfiguredBaseModel):
    """
    Demographic stratification for an association signal
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'sex': {'name': 'sex', 'range': 'SexEnum'}}})

    sex: Optional[SexEnum] = Field(default=None, description="""Sex-specific stratum, if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'sex', 'domain_of': ['PhenotypeContext', 'Demographics']} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'age_range',
         'domain_of': ['PhenotypeContext', 'ProgressionInfo', 'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })


class AssociationMetric(ConfiguredBaseModel):
    """
    Quantitative association metric and its uncertainty.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    metric_type: Optional[AssociationMetricTypeEnum] = Field(default=None, description="""Metric type (e.g., OR, RR, HR)""", json_schema_extra = { "linkml_meta": {'alias': 'metric_type', 'domain_of': ['AssociationMetric']} })
    metric_value: Optional[float] = Field(default=None, description="""Metric value""", json_schema_extra = { "linkml_meta": {'alias': 'metric_value', 'domain_of': ['AssociationMetric']} })
    metric_ci_lower: Optional[float] = Field(default=None, description="""Lower confidence interval bound""", json_schema_extra = { "linkml_meta": {'alias': 'metric_ci_lower', 'domain_of': ['AssociationMetric']} })
    metric_ci_upper: Optional[float] = Field(default=None, description="""Upper confidence interval bound""", json_schema_extra = { "linkml_meta": {'alias': 'metric_ci_upper', 'domain_of': ['AssociationMetric']} })
    p_value: Optional[float] = Field(default=None, description="""P-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'alias': 'p_value', 'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    fdr: Optional[float] = Field(default=None, description="""FDR-adjusted p-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'alias': 'fdr', 'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class AssociationStatistics(ConfiguredBaseModel):
    """
    Statistical summary with evidence for an association signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    metrics: Optional[list[AssociationMetric]] = Field(default=None, description="""Quantitative association metrics""", json_schema_extra = { "linkml_meta": {'alias': 'metrics',
         'domain_of': ['AssociationSignal', 'AssociationStatistics']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'TermMapping',
                       'MappingConsistency',
                       'ComorbidityAssociation',
                       'AssociationSignal',
                       'AssociationMetric',
                       'AssociationStatistics'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class GOEnrichment(ConfiguredBaseModel):
    """
    GO enrichment results for an association signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    method: Optional[str] = Field(default=None, description="""Method or pipeline name""", json_schema_extra = { "linkml_meta": {'alias': 'method', 'domain_of': ['AssociationSignal', 'GOEnrichment']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    go_terms: Optional[list[GOEnrichmentTerm]] = Field(default=None, description="""GO term enrichment results""", json_schema_extra = { "linkml_meta": {'alias': 'go_terms', 'domain_of': ['GOEnrichment']} })


class GOEnrichmentTerm(ConfiguredBaseModel):
    """
    GO term enrichment result with statistical metrics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    p_value: Optional[float] = Field(default=None, description="""P-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'alias': 'p_value', 'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    fdr: Optional[float] = Field(default=None, description="""FDR-adjusted p-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'alias': 'fdr', 'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    overlap: Optional[float] = Field(default=None, description="""Overlap fraction for an enrichment term""", json_schema_extra = { "linkml_meta": {'alias': 'overlap', 'domain_of': ['GOEnrichmentTerm']} })
    combined_score: Optional[float] = Field(default=None, description="""Combined score used by an enrichment method""", json_schema_extra = { "linkml_meta": {'alias': 'combined_score', 'domain_of': ['GOEnrichmentTerm']} })


class ComorbidityHypothesis(ConfiguredBaseModel):
    """
    Mechanistic hypothesis for a comorbidity association, with rich text and embedded evidence plus atomic pathophysiology elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pathophysiology',
         'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })


class UpstreamConditionHypothesis(ConfiguredBaseModel):
    """
    Hypothesized upstream condition that may explain both A and B.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    upstream_disorder: Optional[ConditionDescriptor] = Field(default=None, description="""Upstream disorder referenced in a hypothesis""", json_schema_extra = { "linkml_meta": {'alias': 'upstream_disorder', 'domain_of': ['UpstreamConditionHypothesis']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Descriptor',
                       'GeneticContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'HistopathologyFinding',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration',
                       'Definition',
                       'CriteriaSet',
                       'ConditionDescriptor',
                       'GOEnrichment',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'Finding',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration',
                       'ClassificationAssignment',
                       'Definition',
                       'CriteriaSet',
                       'AssociationSignal',
                       'AssociationStatistics',
                       'ComorbidityHypothesis',
                       'UpstreamConditionHypothesis'],
         'recommended': True} })


class DiseaseCollection(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'tree_root': True})

    diseases: Optional[list[Disease]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'diseases', 'domain_of': ['DiseaseCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CurationEvent.model_rebuild()
Term.model_rebuild()
Descriptor.model_rebuild()
Qualifier.model_rebuild()
CellTypeDescriptor.model_rebuild()
BiologicalProcessDescriptor.model_rebuild()
AnatomicalEntityDescriptor.model_rebuild()
ChemicalEntityDescriptor.model_rebuild()
GeneDescriptor.model_rebuild()
CellularComponentDescriptor.model_rebuild()
ProteinComplexDescriptor.model_rebuild()
AssayDescriptor.model_rebuild()
TriggerDescriptor.model_rebuild()
DiseaseDescriptor.model_rebuild()
BiomarkerDescriptor.model_rebuild()
GeneProductDescriptor.model_rebuild()
HistopathologyFindingDescriptor.model_rebuild()
LifeCycleStageDescriptor.model_rebuild()
PhenotypeDescriptor.model_rebuild()
InheritanceDescriptor.model_rebuild()
TreatmentDescriptor.model_rebuild()
RegimenDescriptor.model_rebuild()
ExposureDescriptor.model_rebuild()
EnvironmentDescriptor.model_rebuild()
OrganismDescriptor.model_rebuild()
HostDescriptor.model_rebuild()
SampleTypeDescriptor.model_rebuild()
GeneticContext.model_rebuild()
OnsetDescriptor.model_rebuild()
PhenotypeContext.model_rebuild()
Dataset.model_rebuild()
ClinicalTrial.model_rebuild()
ComputationalModel.model_rebuild()
DifferentialDiagnosis.model_rebuild()
Subtype.model_rebuild()
EvidenceItem.model_rebuild()
CausalEdge.model_rebuild()
PublicationReference.model_rebuild()
Finding.model_rebuild()
Prevalence.model_rebuild()
ProgressionInfo.model_rebuild()
EpidemiologyInfo.model_rebuild()
Pathophysiology.model_rebuild()
Phenotype.model_rebuild()
Biochemical.model_rebuild()
HistopathologyFinding.model_rebuild()
Genetic.model_rebuild()
Environmental.model_rebuild()
Disease.model_rebuild()
Stage.model_rebuild()
AgentLifeCycle.model_rebuild()
AgentLifeCycleStage.model_rebuild()
AnimalModel.model_rebuild()
Treatment.model_rebuild()
InfectiousAgent.model_rebuild()
Transmission.model_rebuild()
Assay.model_rebuild()
Diagnosis.model_rebuild()
Inheritance.model_rebuild()
Variant.model_rebuild()
FunctionalEffect.model_rebuild()
Mechanism.model_rebuild()
ModelingConsideration.model_rebuild()
ClassificationAssignment.model_rebuild()
ICDOMorphologyAssignment.model_rebuild()
HarrisonsChapterAssignment.model_rebuild()
LysosomalStorageAssignment.model_rebuild()
MechanisticNosologyAssignment.model_rebuild()
IUISAssignment.model_rebuild()
ChannelopathyAssignment.model_rebuild()
DiseaseClassifications.model_rebuild()
Definition.model_rebuild()
CriteriaSet.model_rebuild()
CriteriaItem.model_rebuild()
TermMapping.model_rebuild()
ICD10CMMapping.model_rebuild()
ICD11FMapping.model_rebuild()
MondoMapping.model_rebuild()
MappingConsistency.model_rebuild()
DiseaseMappings.model_rebuild()
ConditionDescriptor.model_rebuild()
ComorbidityAssociation.model_rebuild()
AssociationSignal.model_rebuild()
Demographics.model_rebuild()
AssociationMetric.model_rebuild()
AssociationStatistics.model_rebuild()
GOEnrichment.model_rebuild()
GOEnrichmentTerm.model_rebuild()
ComorbidityHypothesis.model_rebuild()
UpstreamConditionHypothesis.model_rebuild()
DiseaseCollection.model_rebuild()

