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
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





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
                  'CIVIC_ASSERTION': {'prefix_prefix': 'CIVIC_ASSERTION',
                                      'prefix_reference': 'https://civicdb.org/links/assertions/'},
                  'CIVIC_EID': {'prefix_prefix': 'CIVIC_EID',
                                'prefix_reference': 'https://civicdb.org/links/evidence_items/'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'ExO': {'prefix_prefix': 'ExO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ExO_'},
                  'FOODON': {'prefix_prefix': 'FOODON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/FOODON_'},
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
                  'LOINC': {'prefix_prefix': 'LOINC',
                            'prefix_reference': 'https://loinc.org/'},
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
                  'cellxgene': {'prefix_prefix': 'cellxgene',
                                'prefix_reference': 'https://cellxgene.cziscience.com/collections/'},
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
                  'morphic': {'prefix_prefix': 'morphic',
                              'prefix_reference': 'https://data.morphic.bio/'},
                  'namo': {'prefix_prefix': 'namo',
                           'prefix_reference': 'https://w3id.org/monarch-initiative/namo/'},
                  'osdr': {'prefix_prefix': 'osdr',
                           'prefix_reference': 'https://osdr.nasa.gov/bio/repo/data/studies/OSD-'},
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
    Diseases_of_the_ear_nose_and_throat = "otorhinolaryngologic disease"
    """
    Pathological processes of the ear, the nose, and the throat, also known as ENT diseases.
    """
    Diseases_of_the_ear_LEFT_PARENTHESISotitis_hearing_loss_cholesteatomaRIGHT_PARENTHESIS = "disorder of ear"
    """
    Diseases involving the external, middle, or inner ear, including infections, structural lesions, and hearing disorders.
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
    disorder_of_glycogen_metabolism = "disorder of glycogen metabolism"
    """
    Accumulation of glycogen in tissues (Pompe disease and related glycogen storage diseases)
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
    amyloidopathy = "amyloidopathy"
    """
    Amyloid protein aggregation disorders (Alzheimer's, CAA, hereditary cerebral amyloid angiopathy)
    """
    tauopathy = "tauopathy"
    """
    Tau protein aggregation disorders (Alzheimer's, PSP, CBD)
    """
    synucleinopathy = "synucleinopathy"
    """
    Alpha-synuclein aggregation disorders (Parkinson's, DLB, MSA)
    """
    intermediate_filament_disease = "intermediate filament disease"
    """
    Intermediate filament structure/aggregation disorders (Alexander disease/GFAP, epidermolysis bullosa simplex/keratins)
    """
    proteotoxic_disease = "proteotoxic disease"
    """
    Diseases driven by toxic protein misfolding/aggregation and proteostasis failure (Alexander disease, polyQ disorders)
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
    Wrong_statement = "WRONG_STATEMENT"
    """
    The annotated claim contains a demonstrable factual error (e.g., an incorrect statistic or assertion); the cited evidence documents the correct information. Use this when the claim is outright wrong, not merely contested. If the cited reference simply does not mention the claim, use NO_EVIDENCE instead. If the reference contradicts the claim but does not prove it factually wrong, use REFUTE.
    """
    Supports = "SUPPORT"
    """
    The cited evidence directly supports the claim
    """
    Refutes = "REFUTE"
    """
    The cited evidence directly contradicts the claim
    """
    No_evidence = "NO_EVIDENCE"
    """
    The cited reference does not contain evidence relevant to the claim
    """
    Partially_supports = "PARTIAL"
    """
    The cited evidence partially or indirectly supports the claim
    """


class EvidenceSourceEnum(str, Enum):
    """
    The provenance/source of the evidence item
    """
    Human_clinical = "HUMAN_CLINICAL"
    """
    Human clinical observations (patients, cohorts, case reports, clinical trials, epidemiology)
    """
    Model_organism = "MODEL_ORGANISM"
    """
    In vivo animal evidence (mouse, zebrafish, primate, veterinary case series including dog/cat/horse, other non-human animal models etc.)
    """
    In_vitro_SOLIDUS_ex_vivo = "IN_VITRO"
    """
    In vitro or ex vivo assays (cell culture, organoids, tissue slices, biochemical assays)
    """
    Computational = "COMPUTATIONAL"
    """
    In silico/modeling studies (simulation, docking, ML predictions, network inference) even when using clinical data inputs
    """
    Other = "OTHER"
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
    Obligate_LEFT_PARENTHESIS100PERCENT_SIGNRIGHT_PARENTHESIS = "OBLIGATE"
    """
    Present in all cases (100% of patients)
    """
    Very_frequent_LEFT_PARENTHESIS80_99PERCENT_SIGNRIGHT_PARENTHESIS = "VERY_FREQUENT"
    """
    Present in most cases (80-99% of patients)
    """
    Frequent_LEFT_PARENTHESIS30_79PERCENT_SIGNRIGHT_PARENTHESIS = "FREQUENT"
    """
    Present in many cases (30-79% of patients)
    """
    Occasional_LEFT_PARENTHESIS5_29PERCENT_SIGNRIGHT_PARENTHESIS = "OCCASIONAL"
    """
    Present in some cases (5-29% of patients)
    """
    Very_rare_LEFT_PARENTHESISLESS_THAN_SIGN5PERCENT_SIGNRIGHT_PARENTHESIS = "VERY_RARE"
    """
    Present in rare cases (<5% of patients)
    """


class ClinicalSignificanceEnum(str, Enum):
    """
    The clinical significance of a variant for a condition (ACMG guidelines)
    """
    Pathogenic = "PATHOGENIC"
    """
    Variant is pathogenic for the condition (ACMG class 5)
    """
    Likely_pathogenic = "LIKELY_PATHOGENIC"
    """
    Variant is likely pathogenic for the condition (ACMG class 4)
    """
    Benign = "BENIGN"
    """
    Variant is benign for the condition (ACMG class 1)
    """
    Likely_benign = "LIKELY_BENIGN"
    """
    Variant is likely benign for the condition (ACMG class 2)
    """
    Uncertain_significance = "UNCERTAIN_SIGNIFICANCE"
    """
    Clinical significance of the variant is uncertain (ACMG class 3)
    """


class RegulatoryVariantCategoryEnum(str, Enum):
    """
    Functional classification of non-coding gene regulatory variants based on their impact on gene expression patterns. Adapted from Cheng et al. 2024 (PMID:38436667). Includes traditional coding variant categories for completeness.
    """
    Loss_of_expression = "LOE"
    """
    Non-modular loss-of-expression. Diminishes or abolishes gene expression across all cell types that intrinsically express the gene. Analogous to coding amorphic or hypomorphic loss-of-function.
    """
    Modular_loss_of_expression = "mLOE"
    """
    Modular loss-of-expression. Diminishes or abolishes gene expression in only a subset of cell types or developmental windows. Represents a disease mechanism largely unique to non-coding regulatory variants.
    """
    Gain_of_ectopic_expression = "GOE"
    """
    Gain-of-ectopic-expression. Results in ectopic spatial and/or temporal expression of a gene. Can arise from enhancer adoption, novel TFBS creation, promoter switching, or repressor site disruption.
    """
    Loss_of_function = "LOF"
    """
    Coding loss-of-function. Loss of normal biological function via complete (amorphic) or partial (hypomorphic) loss of protein activity.
    """
    Gain_of_function = "GOF"
    """
    Coding gain-of-function. Creates a protein with increased activity (hypermorphic) or entirely new function (neomorphic).
    """
    Dominant_negative = "DN"
    """
    Dominant-negative. Creates a protein that blocks the normal function of the remaining wild-type protein (antimorphic).
    """


class RegulatoryElementTypeEnum(str, Enum):
    """
    Type of gene regulatory element disrupted by a non-coding variant.
    """
    Promoter = "PROMOTER"
    """
    Promoter-proximal element overlapping the transcription start site, containing core TF binding elements (TATA, CAAT, GC, CACCC boxes).
    """
    Enhancer = "ENHANCER"
    """
    Distal regulatory element that upregulates transcriptional activity. May be cell-type-specific or shared across cell types.
    """
    Silencer = "SILENCER"
    """
    Regulatory element that represses or silences gene transcription.
    """
    Insulator = "INSULATOR"
    """
    Boundary element (often CTCF-bound) that compartmentalizes adjacent gene regulatory domains and limits enhancer-promoter interactions.
    """
    TAD_boundary = "TAD_BOUNDARY"
    """
    Topologically associating domain boundary. Structural element maintaining chromatin loop domains; disruption can cause enhancer adoption or ectopic regulatory interactions.
    """
    Locus_control_region = "LOCUS_CONTROL_REGION"
    """
    A cluster of regulatory elements that controls expression of a gene cluster (e.g., the beta-globin LCR).
    """


class GeneDiseaseRelationshipEnum(str, Enum):
    """
    The qualitative relationship between a gene (or locus) and a disease. Use to constrain the free-text `association` slot to a controlled vocabulary aligned with ClinGen gene-disease validity concepts and common cancer/somatic driver classifications. The free-text `association` slot may still be used for narrative detail.
    """
    Causative = "CAUSATIVE"
    """
    Variants in the gene are sufficient to cause the disease in a mendelian or near-mendelian sense (corresponds to ClinGen "Definitive" or "Strong" gene-disease validity).
    """
    Risk_factor = "RISK_FACTOR"
    """
    Variants in the gene increase risk of disease but are neither necessary nor sufficient to cause it. Includes common-variant associations and HLA risk alleles.
    """
    Protective = "PROTECTIVE"
    """
    Variants in the gene reduce the risk or severity of disease.
    """
    Modifier = "MODIFIER"
    """
    Variants in the gene modify the severity, age of onset, or expressivity of disease without being a primary driver.
    """
    Susceptibility = "SUSCEPTIBILITY"
    """
    Variants in the gene confer susceptibility to disease in combination with other genetic or environmental factors. Used for polygenic susceptibility loci such as GWAS hits.
    """
    Somatic_driver = "SOMATIC_DRIVER"
    """
    Somatic alterations in the gene drive tumor initiation or progression (e.g., recurrent oncogenic drivers in cancer).
    """
    Cooperating_alteration = "COOPERATING"
    """
    Co-occurring somatic or germline alterations that cooperate with a primary driver to shape disease behavior or therapy response.
    """
    Biomarker = "BIOMARKER"
    """
    Gene whose expression, mutation, or amplification status serves as a diagnostic, prognostic, or predictive biomarker without a required causal role.
    """
    Disputed = "DISPUTED"
    """
    Reported gene-disease association whose validity is contested (corresponds to ClinGen "Disputed" or "Refuted").
    """
    Unknown = "UNKNOWN"
    """
    The relationship between the gene and the disease is unclear or not yet classified.
    """


class VariantOriginEnum(str, Enum):
    """
    The origin of variation in a gene with respect to a disease entry. Bound to GENO allele origin terms.
    """
    Germline = "GERMLINE"
    """
    germline allele origin
    """
    Somatic = "SOMATIC"
    """
    somatic allele origin
    """
    De_novo = "DE_NOVO"
    """
    de novo allele origin
    """
    Germline_and_somatic = "GERMLINE_AND_SOMATIC"
    """
    The gene is implicated by both germline and somatic variants in the disease (e.g., tumor suppressors with two-hit mechanisms).
    """
    Unknown = "UNKNOWN"
    """
    unknown allele origin
    """


class ModifierEnum(str, Enum):
    """
    Qualifiers for direction, intensity, or pathological state of a descriptor
    """
    Increased = "INCREASED"
    """
    Upregulated, hyperactive, elevated, or excessive
    """
    Decreased = "DECREASED"
    """
    Downregulated, hypoactive, reduced, or deficient
    """
    Abnormal = "ABNORMAL"
    """
    Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
    """
    Dysregulated = "DYSREGULATED"
    """
    Regulation is impaired (may be increased or decreased)
    """
    Absent = "ABSENT"
    """
    Not occurring or not present
    """


class DietaryModificationActionEnum(str, Enum):
    """
    Action applied to a food or beverage as part of a dietary treatment
    """
    Add = "ADD"
    """
    Increase intake or deliberately include the specified food or beverage
    """
    Restrict = "RESTRICT"
    """
    Limit intake of the specified food or beverage without full elimination
    """
    Avoid = "AVOID"
    """
    Eliminate or strictly avoid the specified food or beverage
    """
    Substitute = "SUBSTITUTE"
    """
    Use the specified food or beverage as a replacement within a dietary regimen
    """


class PenetranceEnum(str, Enum):
    """
    Penetrance classification for inheritance
    """
    Complete = "COMPLETE"
    """
    All individuals with the variant express the phenotype
    """
    Incomplete = "INCOMPLETE"
    """
    Not all individuals with the variant express the phenotype
    """
    Unknown = "UNKNOWN"
    """
    Penetrance has not been determined
    """


class ExpressivityEnum(str, Enum):
    """
    Expressivity classification for inheritance
    """
    Variable = "VARIABLE"
    """
    Phenotype severity or features vary among individuals with the same variant
    """
    Consistent = "CONSISTENT"
    """
    Phenotype is uniform among individuals with the same variant
    """
    Unknown = "UNKNOWN"
    """
    Expressivity has not been determined
    """


class LateralityEnum(str, Enum):
    """
    Laterality qualifier for anatomical structures or procedures
    """
    Left = "LEFT"
    """
    Left side of the body
    """
    Right = "RIGHT"
    """
    Right side of the body
    """
    Bilateral = "BILATERAL"
    """
    Both sides of the body
    """


class SpatialExtentEnum(str, Enum):
    """
    Qualifiers for the spatial extent or distribution of a phenotype or process
    """
    Focal = "FOCAL"
    """
    Confined to a single location or region
    """
    Multifocal = "MULTIFOCAL"
    """
    Affecting multiple discrete locations
    """
    Diffuse = "DIFFUSE"
    """
    Widespread, continuous distribution
    """
    Extensive = "EXTENSIVE"
    """
    Large extent, typically involving multiple segments or regions
    """
    Patchy = "PATCHY"
    """
    Irregular, discontinuous distribution
    """
    Segmental = "SEGMENTAL"
    """
    Affecting a specific segment or dermatome
    """


class TemporalityEnum(str, Enum):
    """
    Temporal qualifiers for descriptor post-composition
    """
    Acute = "ACUTE"
    """
    Acute manifestation or episode
    """
    Transient = "TRANSIENT"
    """
    Transient manifestation
    """
    Subacute = "SUBACUTE"
    """
    Subacute manifestation or episode
    """
    Chronic = "CHRONIC"
    """
    Chronic or persistent over time
    """
    Recurrent = "RECURRENT"
    """
    Repeated episodes separated by symptom-free intervals
    """
    Diurnal = "DIURNAL"
    """
    Manifestation occurring during the day
    """
    Nocturnal = "NOCTURNAL"
    """
    Manifestation occurring at night
    """
    Prolonged = "PROLONGED"
    """
    Manifestation lasting longer than typical
    """


class ClinicalCourseEnum(str, Enum):
    """
    Clinical course qualifiers for descriptor post-composition
    """
    Progressive = "PROGRESSIVE"
    """
    Worsening over time
    """
    Stable = "STABLE"
    """
    Not varying in severity or amount over time
    """


class SeverityQualifierEnum(str, Enum):
    """
    Severity qualifiers for descriptor post-composition
    """
    Mild = "MILD"
    """
    Mild severity
    """
    Moderate = "MODERATE"
    """
    Moderate severity
    """
    Severe = "SEVERE"
    """
    Severe severity
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


class MolecularFunctionTerm(str):
    """
    A term representing a molecular function
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
    A term representing a medical action or treatment (from MAXO or NCIT)
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


class BiomarkerReadoutRelationshipEnum(str, Enum):
    """
    Relationship between a biomarker and the pathograph node it reports on
    """
    Readout_of = "READOUT_OF"
    """
    The biomarker directly or indirectly measures the linked event or mechanism
    """
    Correlates_with = "CORRELATES_WITH"
    """
    The biomarker is statistically or clinically associated with the linked event or endpoint
    """
    Predicts = "PREDICTS"
    """
    The biomarker predicts a later event, endpoint, or clinical outcome
    """
    Pharmacodynamic_marker_of = "PHARMACODYNAMIC_MARKER_OF"
    """
    The biomarker reports biological response to a treatment or intervention at the linked node
    """


class BiomarkerReadoutDirectionEnum(str, Enum):
    """
    Direction of association between biomarker value/presence and the linked event or endpoint
    """
    Positive = "POSITIVE"
    """
    Higher biomarker value or stronger presence tracks with more of the linked event
    """
    Negative = "NEGATIVE"
    """
    Higher biomarker value or stronger presence tracks with less of the linked event
    """
    PresentSOLIDUSabsent = "PRESENT_ABSENT"
    """
    Biomarker presence or absence, rather than monotonic level, is the interpretable signal
    """
    Threshold_dependent = "THRESHOLD_DEPENDENT"
    """
    Interpretation depends on threshold, range, genotype, assay, or clinical context
    """


class BiomarkerEndpointContextEnum(str, Enum):
    """
    Endpoint or use context for a biomarker readout link
    """
    Diagnostic = "DIAGNOSTIC"
    """
    Used to support diagnosis or disease classification
    """
    Prognostic = "PROGNOSTIC"
    """
    Associated with future risk, disease severity, or clinical outcome
    """
    Monitoring = "MONITORING"
    """
    Used to track disease state or progression over time
    """
    Pharmacodynamic = "PHARMACODYNAMIC"
    """
    Used to track biological response to treatment or perturbation
    """
    Candidate_surrogate = "CANDIDATE_SURROGATE"
    """
    Potential surrogate endpoint candidate requiring explicit outcome-link evidence
    """


class SurrogateEndpointTableEnum(str, Enum):
    """
    FDA surrogate endpoint table section from which a row was curated
    """
    Adult_non_cancer_related = "ADULT_NONCANCER"
    """
    Adult Surrogate Endpoints - Non-cancer Related
    """
    Adult_cancer_related = "ADULT_CANCER"
    """
    Adult Surrogate Endpoints - Cancer Related
    """
    Pediatric_non_cancer_related = "PEDIATRIC_NONCANCER"
    """
    Pediatric Surrogate Endpoints - Non-cancer Related
    """
    Pediatric_cancer_related = "PEDIATRIC_CANCER"
    """
    Pediatric Surrogate Endpoints - Cancer Related
    """


class SurrogateEndpointApprovalTypeEnum(str, Enum):
    """
    Regulatory approval pathway context represented in the FDA surrogate endpoint table
    """
    Accelerated = "ACCELERATED"
    """
    Endpoint may support accelerated approval in the curated context
    """
    Traditional = "TRADITIONAL"
    """
    Endpoint may support traditional approval in the curated context
    """
    Accelerated_or_traditional = "ACCELERATED_OR_TRADITIONAL"
    """
    Endpoint may support accelerated or traditional approval depending on context of use
    """
    Traditional_and_monograph = "TRADITIONAL_AND_MONOGRAPH"
    """
    Endpoint appears in FDA table as traditional and monograph
    """


class SurrogateEndpointValidationLevelEnum(str, Enum):
    """
    BEST-aligned regulatory validation level inferred or curated for a surrogate endpoint
    """
    Validated_surrogate_endpoint = "VALIDATED_SURROGATE_ENDPOINT"
    """
    Supported by clinical data providing strong evidence that the endpoint predicts clinical benefit
    """
    Reasonably_likely_surrogate_endpoint = "REASONABLY_LIKELY_SURROGATE_ENDPOINT"
    """
    Supported by strong mechanistic and/or epidemiologic rationale, but without sufficient clinical validation for full surrogate validation
    """
    Context_dependent_surrogate_endpoint = "CONTEXT_DEPENDENT_SURROGATE_ENDPOINT"
    """
    Validation and approval pathway depend on context of use, disease setting, effect size, duration, residual uncertainty, and available therapy
    """


class ClinicalBenefitLinkageEnum(str, Enum):
    """
    How a surrogate endpoint is linked to clinical benefit in the regulatory context
    """
    Known_to_predict_clinical_benefit = "KNOWN_TO_PREDICT_CLINICAL_BENEFIT"
    """
    FDA table approval context indicates the endpoint is known to predict clinical benefit for the curated context
    """
    Reasonably_likely_to_predict_clinical_benefit = "REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT"
    """
    FDA table approval context indicates the endpoint is reasonably likely to predict clinical benefit
    """
    Context_dependent = "CONTEXT_DEPENDENT"
    """
    Clinical-benefit linkage depends on context of use and approval pathway
    """


class SurrogateEndpointFootnoteEnum(str, Enum):
    """
    Footnotes and symbols used in the FDA surrogate endpoint workbook
    """
    Composite_biomarker_surrogate = "COMPOSITE_BIOMARKER_SURROGATE"
    """
    Surrogate endpoint is part of a composite of biomarker surrogate endpoints
    """
    Mechanism_agnostic = "MECHANISM_AGNOSTIC"
    """
    Many mechanisms of action are associated with the surrogate endpoint, so it is not directly related to a particular causal pathway
    """
    Tumor_burden_context_dependent = "TUMOR_BURDEN_CONTEXT_DEPENDENT"
    """
    Tumor-burden endpoints may support accelerated or traditional approval depending on context of use
    """
    Anticipated_primary_efficacy_use = "ANTICIPATED_PRIMARY_EFFICACY_USE"
    """
    FDA anticipates the endpoint could be appropriate as a primary efficacy endpoint although it has not yet supported an approved NDA or BLA
    """
    Bone_mineral_density_context = "BONE_MINERAL_DENSITY_CONTEXT"
    """
    Bone mineral density footnote for male or glucocorticoid-induced osteoporosis contexts
    """
    Clinical_endpoints_required = "CLINICAL_ENDPOINTS_REQUIRED"
    """
    Clinical endpoints were required for the approvals
    """
    Arrhythmia_response_definition = "ARRHYTHMIA_RESPONSE_DEFINITION"
    """
    Specialized response definition footnote for supraventricular tachycardia endpoint
    """


class SurrogateEndpointMappingStatusEnum(str, Enum):
    """
    Status of mapping an FDA disease/use row to dismech disease entries
    """
    Exact_dismech_match = "EXACT_DISMECH_MATCH"
    """
    FDA disease/use maps directly to an existing dismech disease entry
    """
    Curated_dismech_mapping = "CURATED_DISMECH_MAPPING"
    """
    Mapping was manually curated despite non-identical labels
    """
    Candidate_dismech_mapping = "CANDIDATE_DISMECH_MAPPING"
    """
    Row mentions a disease represented in dismech but the FDA disease/use row is broader, multi-condition, or otherwise requires review
    """
    Needs_curation = "NEEDS_CURATION"
    """
    No dismech disease mapping has been assigned yet
    """
    Not_disease_specific = "NOT_DISEASE_SPECIFIC"
    """
    FDA row is a use, vaccine, or broad product context rather than a directly mappable disease entry
    """


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
    A MONDO disease, inherited disease susceptibility, or related medical condition term used to anchor a curated disorder entry
    """
    pass


class NCITDiseaseOrFindingTerm(str):
    """
    An NCIT disease-oriented oncology term used for disease-level cancer mappings and subtype grounding, including neoplasm-by-morphology, special-category neoplasm, and clinically used disease/finding boundary concepts.
    """
    pass


class DiseaseOrSubtypeTerm(str):
    """
    A MONDO disease term or NCIT cancer disease/subtype term used to ground a disease subtype or cancer facet value.
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


class FoodTerm(str):
    """
    A term representing a food, beverage, nutrient, mineral, or supplement source (from FOODON or CHEBI)
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
    MULTI_OMICS = "MULTI_OMICS"
    """
    Integrated multi-omics profiling (e.g., combined transcriptomics, proteomics, metabolomics)
    """
    MULTI_OMICS_PERTURBATION = "MULTI_OMICS_PERTURBATION"
    """
    Multi-omics profiling of genetic perturbations (e.g., CRISPR knockout combined with transcriptomic, chromatin accessibility, and cellular phenotyping)
    """


class ExperimentalModelTypeEnum(str, Enum):
    """
    Broad disease-centric categories for experimental model systems, primarily non-animal systems curated in this section
    """
    ORGANOID = "ORGANOID"
    """
    Self-organizing three-dimensional tissue model, often stem-cell-derived
    """
    ORGAN_ON_CHIP = "ORGAN_ON_CHIP"
    """
    Microfluidic organ- or tissue-on-chip model
    """
    CELL_LINE = "CELL_LINE"
    """
    Immortalized cell line-based disease model
    """
    IPSC_DERIVED_MODEL = "IPSC_DERIVED_MODEL"
    """
    Differentiated model derived from induced pluripotent stem cells
    """
    PRIMARY_CELL_CULTURE = "PRIMARY_CELL_CULTURE"
    """
    Primary-cell or biopsy-derived culture system, including monolayers
    """
    CO_CULTURE = "CO_CULTURE"
    """
    Host-microbe or multi-cell-type coculture system
    """
    OTHER = "OTHER"
    """
    Other experimental model type not covered above
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
    STRUCTURAL_PREDICTION = "STRUCTURAL_PREDICTION"
    """
    Protein structure prediction (AlphaFold, RoseTTAFold) or experimental structure (PDB X-ray, cryo-EM) used to understand disease mechanisms
    """
    MOLECULAR_DOCKING = "MOLECULAR_DOCKING"
    """
    Computational docking or molecular dynamics simulation of drug candidates to protein targets, typically informed by PDB/AlphaFold structures
    """


class ThresholdDirectionEnum(str, Enum):
    """
    Whether a threshold activates when the variable goes above or below the value
    """
    above = "above"
    """
    Activates when the variable exceeds the threshold
    """
    below = "below"
    """
    Activates when the variable falls below the threshold
    """


class CausalLinkTypeEnum(str, Enum):
    """
    Degree of mechanistic directness represented by a causal edge
    """
    DIRECT = "DIRECT"
    """
    Direct causal influence at the current graph granularity
    """
    INDIRECT_KNOWN_INTERMEDIATES = "INDIRECT_KNOWN_INTERMEDIATES"
    """
    Indirect relationship where one or more intermediates are known but omitted from the graph
    """
    INDIRECT_UNKNOWN_INTERMEDIATES = "INDIRECT_UNKNOWN_INTERMEDIATES"
    """
    Indirect relationship where at least one required intermediate mechanism is currently unknown
    """
    UNKNOWN = "UNKNOWN"
    """
    Directness has not yet been determined
    """


class TreatmentEffectEnum(str, Enum):
    """
    How a treatment affects a pathophysiology mechanism node
    """
    INHIBITS = "INHIBITS"
    """
    Blocks or decreases the mechanism (e.g., TKI inhibiting constitutive kinase activity)
    """
    ACTIVATES = "ACTIVATES"
    """
    Promotes or increases the mechanism (e.g., enzyme replacement restoring a deficient pathway)
    """
    MODULATES = "MODULATES"
    """
    Alters the mechanism without clear unidirectional effect
    """
    BYPASSES = "BYPASSES"
    """
    Works around the disrupted mechanism via an alternative pathway
    """
    RESTORES = "RESTORES"
    """
    Restores normal function of a disrupted mechanism (e.g., gene therapy, enzyme replacement)
    """


class MedicalActionCategoryEnum(str, Enum):
    """
    High-level category for a clinical action currently represented in the treatments section
    """
    THERAPEUTIC = "THERAPEUTIC"
    """
    An action intended to treat, prevent, mitigate, or manage disease processes, complications, or symptoms. These actions may link to pathophysiology nodes or phenotypes through target_mechanisms or target_phenotypes.
    """
    DIAGNOSTIC = "DIAGNOSTIC"
    """
    A diagnostic procedure or testing action used to establish or refine a diagnosis. These actions should not use target_mechanisms or target_phenotypes because they do not treat pathophysiology nodes or phenotypes.
    """
    SCREENING = "SCREENING"
    """
    Screening or surveillance intended to detect disease, risk, or early manifestations. These actions should not use target_mechanisms or target_phenotypes.
    """
    MONITORING = "MONITORING"
    """
    Clinical, laboratory, imaging, or longitudinal follow-up used to observe disease status or complications. These actions should not use target_mechanisms or target_phenotypes.
    """
    GENETIC_COUNSELING = "GENETIC_COUNSELING"
    """
    Counseling, carrier testing, recurrence-risk counseling, cascade testing, or reproductive planning. These actions should not use target_mechanisms or target_phenotypes because they do not directly modify disease pathophysiology or phenotypes.
    """


class MechanisticHypothesisStatusEnum(str, Enum):
    """
    Curation/maturity status for a disease-level mechanistic hypothesis
    """
    CANONICAL = "CANONICAL"
    """
    Widely accepted explanatory model used as the default disease mechanism
    """
    ALTERNATIVE = "ALTERNATIVE"
    """
    Plausible competing or superimposed hypothesis with supporting evidence
    """
    EMERGING = "EMERGING"
    """
    Early-stage hypothesis with limited or recently reported evidence
    """
    DEPRECATED = "DEPRECATED"
    """
    Historical hypothesis no longer supported as the current model
    """


class DiscussionKindEnum(str, Enum):
    """
    Kind of unresolved/in-progress item captured by a Discussion. Discussions are thread-like objects that record open questions, controversies, curation todos, emerging hypotheses, or interpretation debates attached to a disease entry or sub-object. Knowledge gaps are represented as a discussion kind so they can reuse the existing pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved.
    """
    OPEN_QUESTION = "OPEN_QUESTION"
    """
    An unresolved scientific question posed by curators or experts
    """
    KNOWLEDGE_GAP = "KNOWLEDGE_GAP"
    """
    A missing causal, evidentiary, model-system, or translational assertion whose resolution would materially improve the disease mechanism model
    """
    CONTROVERSY = "CONTROVERSY"
    """
    A live disagreement or competing interpretation between published positions
    """
    CURATION_TODO = "CURATION_TODO"
    """
    A curation task captured inline (e.g., "phenotype needs HPO term refinement")
    """
    EMERGING_HYPOTHESIS = "EMERGING_HYPOTHESIS"
    """
    A recently reported hypothesis under active discussion in the community
    """
    INTERPRETATION = "INTERPRETATION"
    """
    A discussion about how to interpret existing evidence or model an edge
    """


class DiscussionStatusEnum(str, Enum):
    """
    Lifecycle status for a Discussion
    """
    OPEN = "OPEN"
    """
    Posed but not yet under active discussion
    """
    UNDER_DISCUSSION = "UNDER_DISCUSSION"
    """
    Actively being discussed in one or more linked venues
    """
    RESOLVED = "RESOLVED"
    """
    Closed with a documented resolution; kept for provenance
    """
    ARCHIVED = "ARCHIVED"
    """
    No longer active and not resolved (deferred, stale, or superseded)
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
    CHI_SQUARE = "CHI_SQUARE"
    """
    Chi-square association statistic
    """
    LOG_OBS_EXP_RATIO = "LOG_OBS_EXP_RATIO"
    """
    Natural-log observed-to-expected co-occurrence ratio
    """
    OTHER = "OTHER"
    """
    Other or unspecified metric
    """


class MechanismConfidenceEnum(str, Enum):
    """
    Level of confidence in a pathophysiology mechanism
    """
    Established = "ESTABLISHED"
    """
    Well-established mechanism with strong evidence from multiple independent studies
    """
    Hypothetical = "HYPOTHETICAL"
    """
    Hypothetical mechanism with limited or indirect evidence; plausible but not yet validated
    """
    Provisional = "PROVISIONAL"
    """
    Provisional mechanism under active investigation with emerging but incomplete evidence
    """


class ReferenceTagEnum(str, Enum):
    """
    Controlled vocabulary for tagging top-level references by authoritative source type. Enables queries like "which disorders lack a GeneReviews citation?"
    """
    GeneReviews = "GeneReviews"
    """
    Reference is a GeneReviews article published in the NCBI Bookshelf (https://www.ncbi.nlm.nih.gov/books/NBK1116/). GeneReviews are expert-authored, peer-reviewed summaries updated on a rolling basis; they are the gold-standard narrative resource for rare Mendelian disease phenotyping and management.
    """



class CurationEvent(ConfiguredBaseModel):
    """
    A single curation event in the audit trail
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'curation_timestamp': {'name': 'curation_timestamp',
                                               'required': True}}})

    curation_timestamp: datetime  = Field(default=..., description="""ISO 8601 timestamp of the curation event""", json_schema_extra = { "linkml_meta": {'domain_of': ['CurationEvent']} })
    curation_model: Optional[str] = Field(default=None, description="""Model identifier used for curation (e.g., claude-opus-4-5-20251101)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CurationEvent']} })
    curation_action: Optional[CurationActionEnum] = Field(default=None, description="""Type of curation action performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['CurationEvent']} })
    curation_description: Optional[str] = Field(default=None, description="""Human-readable description of changes made""", json_schema_extra = { "linkml_meta": {'domain_of': ['CurationEvent']} })


class Term(ConfiguredBaseModel):
    """
    A structured reference to an ontology term
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    id: str = Field(default=..., description="""Ontology term identifier (CURIE)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label for the ontology term""", json_schema_extra = { "linkml_meta": {'comments': ['This is automatically validated by the linkml-term-validator '
                      'tool.'],
         'domain_of': ['Term']} })


class Descriptor(ConfiguredBaseModel):
    """
    Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, laterality, spatial_extent, onset, temporality, clinical_course, and severity slots.
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    predicate: Optional[Descriptor] = Field(default=None, description="""The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')""", json_schema_extra = { "linkml_meta": {'domain_of': ['Qualifier']} })
    value: Optional[Descriptor] = Field(default=None, description="""The value/filler in a qualifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Qualifier']} })


class DietaryModification(ConfiguredBaseModel):
    """
    A structured dietary addition, restriction, avoidance, or substitution used to post-compose a treatment descriptor with FOODON foods or beverages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use for bona fide dietary or nutritional treatments, not to '
                      'restate harmful exposures outside treatment context',
                      'Represent substitutions as paired AVOID and ADD entries when a '
                      'single replacement target is insufficient'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    action: Optional[DietaryModificationActionEnum] = Field(default=None, description="""The dietary action being applied""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryModification']} })
    food: Optional[FoodDescriptor] = Field(default=None, description="""The FOODON-bound food or beverage targeted by a dietary modification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryModification']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })


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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional Cell Ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for biological processes, bindable to Gene Ontology (GO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'BiologicalProcessTerm'}],
                                 'description': 'Optional GO biological process term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO biological process term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'BiologicalProcessTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class MolecularFunctionDescriptor(Descriptor):
    """
    A descriptor for molecular functions, bindable to Gene Ontology (GO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'MolecularFunctionTerm'}],
                                 'description': 'Optional GO molecular function term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO molecular function term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'MolecularFunctionTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for anatomical locations, bindable to UBERON
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'AnatomicalEntityTerm'}],
                                 'description': 'Optional UBERON anatomical entity '
                                                'term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional UBERON anatomical entity term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomicalEntityTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for chemical entities, bindable to CHEBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ChemicalEntityTerm'}],
                                 'description': 'Optional CHEBI chemical entity term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional CHEBI chemical entity term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ChemicalEntityTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional gene database term reference (e.g., HGNC)""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GeneTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for cellular components, bindable to GO cellular component
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'CellularComponentTerm'}],
                                 'description': 'Optional GO cellular component term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO cellular component term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellularComponentTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ProteinComplexDescriptor(Descriptor):
    """
    A descriptor for protein complexes that gene products participate in, bindable to GO protein complex terms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ProteinComplexTerm'}],
                                 'description': 'Optional GO protein complex term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO protein complex term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ProteinComplexTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class AssayDescriptor(Descriptor):
    """
    A descriptor for assays, bindable to OBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'AssayTerm'}],
                                 'description': 'Optional OBI assay term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional OBI assay term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AssayTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class TriggerDescriptor(Descriptor):
    """
    A descriptor for triggers/causes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'TriggerTerm'}],
                                 'description': 'Optional ontology term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'TriggerTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MONDO disease term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class SubtypeDescriptor(Descriptor):
    """
    A descriptor for disease subtypes, bindable to MONDO disease terms or NCIT oncology subtype terms.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'DiseaseOrSubtypeTerm'}],
                                 'description': 'MONDO or NCIT term reference for a '
                                                'subtype/facet value',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""MONDO or NCIT term reference for a subtype/facet value""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseOrSubtypeTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT biomarker term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'BiomarkerTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT gene product term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GeneProductTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCIT or HP histopathology finding term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'HistopathologyFindingTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""OPL life cycle stage term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'LifeCycleStageTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional HP phenotype term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'PhenotypeTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional HPO mode of inheritance term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'InheritanceTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class TreatmentDescriptor(Descriptor):
    """
    A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinical interventions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'dietary_modifications': {'comments': ['Best used when '
                                                               'treatment_term is a '
                                                               'dietary or nutritional '
                                                               'intervention (for '
                                                               'example MAXO:0000088 '
                                                               'dietary intervention)',
                                                               'Use FOODON-backed '
                                                               'foods or beverages '
                                                               'rather than abstract '
                                                               'nutrients where '
                                                               'possible'],
                                                  'description': 'The food or beverage '
                                                                 'additions, '
                                                                 'restrictions, '
                                                                 'avoidances, or '
                                                                 'substitutions that '
                                                                 'define a dietary '
                                                                 'intervention.',
                                                  'name': 'dietary_modifications'},
                        'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'TreatmentActionTerm'}],
                                 'description': 'Optional MAXO or NCIT treatment term '
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

    therapeutic_agent: Optional[list[ChemicalEntityDescriptor]] = Field(default=None, description="""The drug(s) or chemical agent(s) used in this treatment. Use when the MAXO term is generic (e.g., pharmacotherapy MAXO:0000058) but specific drugs are involved.""", json_schema_extra = { "linkml_meta": {'comments': ['Prefer CHEBI terms for specific drugs (e.g., CHEBI:15365 for '
                      'aspirin)',
                      'Use NCIT for drug classes when specific CHEBI term unavailable'],
         'domain_of': ['TreatmentDescriptor']} })
    dietary_modifications: Optional[list[DietaryModification]] = Field(default=None, description="""The food or beverage additions, restrictions, avoidances, or substitutions that define a dietary intervention.""", json_schema_extra = { "linkml_meta": {'comments': ['Best used when treatment_term is a dietary or nutritional '
                      'intervention (for example MAXO:0000088 dietary intervention)',
                      'Use FOODON-backed foods or beverages rather than abstract '
                      'nutrients where possible'],
         'domain_of': ['TreatmentDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MAXO or NCIT treatment term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'TreatmentActionTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional NCIT regimen term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'RegimenTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ECTO/XCO exposure term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ExposureTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ENVO environment term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'EnvironmentTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class FoodDescriptor(Descriptor):
    """
    A descriptor for foods, beverages, nutrients, minerals, and supplements, bindable to FOODON or CHEBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use FOODON for specific foods, beverages, food products, and '
                      'dietary sources',
                      'Use CHEBI when the dietary target is an exact nutrient, '
                      'mineral, vitamin, or supplement'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'FoodTerm'}],
                                 'description': 'Optional FOODON or CHEBI dietary '
                                                'entity term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional FOODON or CHEBI dietary entity term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'FoodTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCBITaxon term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class HostDescriptor(OrganismDescriptor):
    """
    A descriptor for hosts in an infectious agent life cycle
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use role for definitive, intermediate, reservoir, accidental, '
                      'or paratenic host'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCBITaxon term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class SampleTypeDescriptor(Descriptor):
    """
    A descriptor for biological sample types (tissue and/or cell type)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    tissue_term: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""UBERON term for the tissue""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleTypeDescriptor', 'ExperimentalModel']} })
    cell_type_term: Optional[CellTypeDescriptor] = Field(default=None, description="""CL term for the cell type""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleTypeDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class GeneticContext(ConfiguredBaseModel):
    """
    A structured description of a genetic context that modifies phenotype frequency, severity, or presentation. Flexible enough to capture single genes, multiple genes, mutation types, zygosity, complementation groups, and complex genotypes. The description slot accommodates contexts that don't fit neatly into the structured fields (e.g., structural variants, complex rearrangements).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'ExperimentalPerturbation',
                       'Pathophysiology',
                       'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    allele_type: Optional[str] = Field(default=None, description="""Type of allele or mutation (e.g., null, missense, splice_site, deletion, frameshift, nonsense, hypomorphic, structural_variant). Free text to accommodate the diversity of mutation nomenclature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext']} })
    zygosity: Optional[ZygosityEnum] = Field(default=None, description="""Zygosity context""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext']} })
    functional_impact: Optional[str] = Field(default=None, description="""Functional consequence of the genetic variant (e.g., loss_of_function, gain_of_function, dominant_negative).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext']} })
    complementation_group: Optional[str] = Field(default=None, description="""Complementation group designation (e.g., FA-A, FA-D1, BBS1). Used for genetically heterogeneous diseases where subtypes are historically named by complementation analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class OnsetDescriptor(ConfiguredBaseModel):
    """
    Structured description of age of onset. Combines an HPO onset category with optional quantitative age data and notes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    onset_category: Optional[OnsetEnum] = Field(default=None, description="""HPO onset category (e.g., CHILDHOOD, NEONATAL). Use when an approximate developmental stage is known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OnsetDescriptor']} })
    mean_age_years: Optional[float] = Field(default=None, description="""Mean age of onset in years, as reported in a cohort study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OnsetDescriptor']} })
    min_age_years: Optional[float] = Field(default=None, description="""Minimum (earliest) age of onset in years.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OnsetDescriptor']} })
    max_age_years: Optional[float] = Field(default=None, description="""Maximum (latest) age of onset in years.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OnsetDescriptor']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence supporting the frequency, severity, or onset claims made in this specific context. Distinct from the D2P evidence on the parent Phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    genetic_context: Optional[GeneticContext] = Field(default=None, description="""The genetic context under which this qualification applies. May specify genes, mutation types, zygosity, complementation groups, or complex genotypes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Pathophysiology']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Sex-specific stratum, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Demographics']} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'SurrogateEndpoint',
                       'ProgressionInfo',
                       'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Supports GEO, ArrayExpress, SRA, dbGaP, GTEx, ENCODE, MorPhiC, '
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

    accession: str = Field(default=..., description="""Dataset accession identifier as a CURIE (e.g., geo:GSE67472)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'implements': ['linkml:authoritative_reference']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'PublicationReference', 'TrackedIssue'],
         'implements': ['linkml:title']} })
    description: Optional[str] = Field(default=None, description="""A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': True} })
    organism: Optional[OrganismDescriptor] = Field(default=None, description="""The organism from which samples were derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ExperimentalModel']} })
    data_type: Optional[DatasetTypeEnum] = Field(default=None, description="""The type of omics or other data in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    sample_types: Optional[list[SampleTypeDescriptor]] = Field(default=None, description="""Types of biological samples in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    sample_count: Optional[int] = Field(default=None, description="""Total number of samples in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    conditions: Optional[list[str]] = Field(default=None, description="""Experimental conditions or disease states represented""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ExperimentalModel']} })
    exposures: Optional[list[ExposureDescriptor]] = Field(default=None, description="""Environmental exposures studied in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    platform: Optional[str] = Field(default=None, description="""Sequencing or array platform used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'ProteinStructure']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'PublicationReference']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ExperimentalModel(ConfiguredBaseModel):
    """
    A disease-relevant non-animal experimental model system. This is a disease-centric bridge class inspired by NAMO, intended to capture the model itself while keeping dismech focused on disease mechanisms rather than study-level model registries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use `namo_type` to map to a corresponding NAMO class when '
                      'applicable',
                      'Prefer `experimental_model_type` for broad local categorization '
                      'and `description` or `notes` for disease-specific nuance',
                      'Use `cell_source` to record whether the system is '
                      'patient-derived, iPSC-derived, primary, immortalized, or mixed'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    experimental_model_type: Optional[ExperimentalModelTypeEnum] = Field(default=None, description="""Broad category for an experimental model system""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel']} })
    namo_type: Optional[str] = Field(default=None, description="""Optional mapping to the corresponding NAMO class, such as `namo:Organoid` or `namo:OrganOnChip`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel']} })
    organism: Optional[OrganismDescriptor] = Field(default=None, description="""The organism from which samples were derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ExperimentalModel']} })
    tissue_term: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""UBERON term for the tissue""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleTypeDescriptor', 'ExperimentalModel']} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel', 'Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    conditions: Optional[list[str]] = Field(default=None, description="""Experimental conditions or disease states represented""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ExperimentalModel']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells used in the experimental model""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel']} })
    culture_system: Optional[str] = Field(default=None, description="""Culture format or device context used by the experimental model""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'ProteinStructure']} })
    modeled_mechanisms: Optional[list[ModelMechanismLink]] = Field(default=None, description="""Pathophysiology mechanism nodes/assertions that this experimental model is intended to recapitulate, perturb, or measure within the disease pathograph.""", json_schema_extra = { "linkml_meta": {'comments': ['Target names should match pathophysiology entry names in the '
                      'same disease file',
                      'Use description to capture the specific assayable or modeled '
                      'assertion, not just the node label',
                      'Kept intentionally lightweight so it can later align more '
                      'explicitly with NAMO relations'],
         'domain_of': ['ExperimentalModel', 'ComputationalModel']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'PublicationReference']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Experiment(ConfiguredBaseModel):
    """
    A structured experiment or protocol-level study design that can be proposed to resolve a knowledge gap, or later reused to represent experiments that have been carried out. The object itself is intentionally status-neutral: proposal, execution, and evidentiary status are expressed by the containing slot or future evidence context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['In `Discussion.proposed_experiments`, the containing slot means '
                      'the experiment is proposed as a response to an open question or '
                      'knowledge gap.',
                      'Use `model_systems` for NAMO-aligned models, `perturbations` '
                      'for pathograph/gene/chemical/exposure manipulations, and '
                      '`readouts` for ontology-backed outcome or mechanism '
                      'measurements.'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'assays': {'description': 'Ontology-backed assays used by the '
                                                  'experiment; prefer OBI terms when '
                                                  'available.',
                                   'name': 'assays'},
                        'evidence': {'description': 'Literature, protocol papers, or '
                                                    'dataset evidence supporting the '
                                                    'feasibility, precedent, or design '
                                                    'rationale for this experiment.',
                                     'name': 'evidence',
                                     'recommended': False},
                        'experiment_id': {'name': 'experiment_id', 'required': True},
                        'perturbations': {'description': 'Interventions or '
                                                         'manipulations applied in the '
                                                         'experiment. These may target '
                                                         'disease pathograph nodes, '
                                                         'genes, chemical entities, '
                                                         'treatments, exposures, '
                                                         'triggers, or biological '
                                                         'processes.',
                                          'inlined_as_list': True,
                                          'name': 'perturbations',
                                          'range': 'ExperimentalPerturbation'},
                        'readouts': {'description': 'Measurements or outcomes '
                                                    'interpreted against disease '
                                                    'pathograph nodes, phenotypes, '
                                                    'biomarkers, or biological '
                                                    'processes.',
                                     'inlined_as_list': True,
                                     'name': 'readouts',
                                     'range': 'ExperimentalReadout'}}})

    experiment_id: str = Field(default=..., description="""Stable identifier for an Experiment within a disease entry""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    experiment_type: Optional[Descriptor] = Field(default=None, description="""Ontology-backed descriptor for the overall experiment or study design. Prefer OBI terms when available; assay-level details should go in the `assays` slot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    model_systems: Optional[list[ExperimentalModel]] = Field(default=None, description="""Experimental model systems used or proposed for an experiment, using the ExperimentalModel pattern and optional NAMO alignment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'ExperimentalControl']} })
    perturbations: Optional[list[ExperimentalPerturbation]] = Field(default=None, description="""Interventions or manipulations applied in the experiment. These may target disease pathograph nodes, genes, chemical entities, treatments, exposures, triggers, or biological processes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'ExperimentalControl', 'ComputationalModel']} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, description="""Ontology-backed assays used by the experiment; prefer OBI terms when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment',
                       'ExperimentalReadout',
                       'Pathophysiology',
                       'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    readouts: Optional[list[ExperimentalReadout]] = Field(default=None, description="""Measurements or outcomes interpreted against disease pathograph nodes, phenotypes, biomarkers, or biological processes.""", json_schema_extra = { "linkml_meta": {'comments': ['Target names should match pathophysiology or phenotype entry '
                      'names in the same disease file',
                      'Readout links are observational/associative, not causal '
                      'disease-progression edges',
                      'Use evidence on the readout link when the '
                      "biomarker-to-mechanism mapping is distinct from the biomarker's "
                      'own evidence'],
         'domain_of': ['Experiment', 'Biochemical']} })
    controls: Optional[list[ExperimentalControl]] = Field(default=None, description="""Experimental controls, comparators, or counterfactual arms""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    decision_criterion: Optional[str] = Field(default=None, description="""Pre-specified qualitative or quantitative criterion for interpreting the experiment relative to the attached discussion or knowledge gap.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    would_support: Optional[list[str]] = Field(default=None, description="""Entity references that would be supported if the experiment meets its decision criterion. Uses the same hash-anchor grammar as `attaches_to`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    would_refute: Optional[list[str]] = Field(default=None, description="""Entity references that would be weakened or refuted if the experiment meets a contrary result. Uses the same hash-anchor grammar as `attaches_to`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    protocol_reference: Optional[str] = Field(default=None, description="""Optional protocol, methods paper, or registry reference for the experimental workflow. May be a PMID, DOI, protocols.io DOI, URL, or other stable identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    datasets: Optional[list[Dataset]] = Field(default=None, description="""Publicly available datasets relevant to disease research""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'Disease'], 'recommended': True} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Literature, protocol papers, or dataset evidence supporting the feasibility, precedent, or design rationale for this experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': False} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ExperimentalPerturbation(ConfiguredBaseModel):
    """
    A structured perturbation, intervention, or exposure used in an experiment. Prefer ontology-backed descriptors for genes, chemicals, treatments, exposures, triggers, and biological processes rather than plain string lists.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'target': {'description': 'Entity reference for the pathograph '
                                                  'node, phenotype, gene, or other '
                                                  'modeled object being perturbed. '
                                                  'Uses the same hash-anchor grammar '
                                                  'as `attaches_to` when pointing into '
                                                  'a disease entry.',
                                   'name': 'target'}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    target: str = Field(default=..., description="""Entity reference for the pathograph node, phenotype, gene, or other modeled object being perturbed. Uses the same hash-anchor grammar as `attaches_to` when pointing into a disease entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'ExperimentalPerturbation',
                       'Pathophysiology',
                       'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    chemical_entities: Optional[list[ChemicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Plasmalogen}]'}]} })
    treatment_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this treatment/medical action""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Treatment']} })
    exposure_term: Optional[ExposureDescriptor] = Field(default=None, description="""The ECTO/XCO term for this exposure event""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Environmental']} })
    triggers: Optional[list[TriggerDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Viral Infections}]'}]} })
    biological_processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: TNF-alpha Production}]'}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ExperimentalReadout(ConfiguredBaseModel):
    """
    A structured readout or outcome measured in an experiment. Use descriptor slots to ground readouts to phenotypes, biomarkers, biological processes, and assays.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'interpretation': {'description': 'Curator-facing explanation '
                                                          'of how this readout would '
                                                          'be interpreted relative to '
                                                          "the experiment's decision "
                                                          'criterion.',
                                           'name': 'interpretation'},
                        'target': {'description': 'Entity reference for the pathograph '
                                                  'node, phenotype, or other modeled '
                                                  'object that this readout measures '
                                                  'or adjudicates.',
                                   'name': 'target'}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    target: str = Field(default=..., description="""Entity reference for the pathograph node, phenotype, or other modeled object that this readout measures or adjudicates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    phenotype_term: Optional[PhenotypeDescriptor] = Field(default=None, description="""The HP term for this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'Phenotype']} })
    biomarker_term: Optional[BiomarkerDescriptor] = Field(default=None, description="""Ontology term for a biomarker (from NCIT)""", json_schema_extra = { "linkml_meta": {'comments': ['Use NCIT terms for biomarkers (proteins, genes, fusion '
                      'products)',
                      'NCIT:C16342 (Biomarker) is the root class for validation'],
         'domain_of': ['ExperimentalReadout', 'Biochemical']} })
    biological_processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: TNF-alpha Production}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment',
                       'ExperimentalReadout',
                       'Pathophysiology',
                       'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    direction: Optional[BiomarkerReadoutDirectionEnum] = Field(default=None, description="""Direction of association between the biomarker value/presence and the linked pathograph node""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'BiomarkerReadout']} })
    interpretation: Optional[str] = Field(default=None, description="""Curator-facing explanation of how this readout would be interpreted relative to the experiment's decision criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'BiomarkerReadout']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ExperimentalControl(ConfiguredBaseModel):
    """
    A comparator or control condition for an experiment, such as an isogenic wild-type line, mock perturbation, vehicle control, rescue arm, or untreated disease model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'perturbations': {'inlined_as_list': True,
                                          'name': 'perturbations',
                                          'range': 'ExperimentalPerturbation'}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    model_systems: Optional[list[ExperimentalModel]] = Field(default=None, description="""Experimental model systems used or proposed for an experiment, using the ExperimentalModel pattern and optional NAMO alignment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'ExperimentalControl']} })
    perturbations: Optional[list[ExperimentalPerturbation]] = Field(default=None, description="""Gene knockouts, reaction deletions, or parameter changes modeling the disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'ExperimentalControl', 'ComputationalModel']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    name: str = Field(default=..., description="""NCT identifier (e.g., NCT00000001) or trial name""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, description="""Brief summary or key details of the clinical trial""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': True} })
    phase: Optional[ClinicalTrialPhaseEnum] = Field(default=None, description="""Trial phase (Phase I, Phase II, Phase III, Phase IV, or Not Applicable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial', 'ProgressionInfo'],
         'examples': [{'value': 'Active TB'}],
         'recommended': True} })
    status: Optional[ClinicalTrialStatusEnum] = Field(default=None, description="""Recruitment or trial status (e.g., Recruiting, Completed, Terminated, Active not recruiting)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial', 'MechanisticHypothesis', 'Discussion'],
         'examples': [{'value': 'Recruiting'},
                      {'value': 'Completed'},
                      {'value': 'Terminated'}],
         'recommended': True} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Supporting evidence with snippets from trial documentation""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': False} })
    target_phenotypes: Optional[list[PhenotypeDescriptor]] = Field(default=None, description="""Phenotypes that this treatment or trial addresses or targets""", json_schema_extra = { "linkml_meta": {'comments': ["Should reference phenotype names defined in the same disease's "
                      'phenotypes list',
                      'Enables linking treatments/trials to the '
                      'symptoms/manifestations they aim to manage',
                      'Each phenotype can include ontology term references (HP)'],
         'domain_of': ['ClinicalTrial', 'Treatment']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    model_type: Optional[ComputationalModelTypeEnum] = Field(default=None, description="""Type of computational model""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    repository_url: Optional[str] = Field(default=None, description="""URL to model repository (GitHub, BiGG, VMH, BioModels)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    model_id: Optional[str] = Field(default=None, description="""Identifier within the repository (e.g., Recon3D, BIOMD0000000123)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    base_model: Optional[str] = Field(default=None, description="""Parent/base model this is derived from (e.g., Recon3D, Harvey 1.0)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    perturbations: Optional[list[GeneDescriptor]] = Field(default=None, description="""Gene knockouts, reaction deletions, or parameter changes modeling the disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'ExperimentalControl', 'ComputationalModel']} })
    variables: Optional[list[ModelVariable]] = Field(default=None, description="""Variables/outputs of a computational model with ontology mappings""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    modeled_mechanisms: Optional[list[ModelMechanismLink]] = Field(default=None, description="""Pathophysiology mechanism nodes/assertions that this experimental model is intended to recapitulate, perturb, or measure within the disease pathograph.""", json_schema_extra = { "linkml_meta": {'comments': ['Target names should match pathophysiology entry names in the '
                      'same disease file',
                      'Use description to capture the specific assayable or modeled '
                      'assertion, not just the node label',
                      'Kept intentionally lightweight so it can later align more '
                      'explicitly with NAMO relations'],
         'domain_of': ['ExperimentalModel', 'ComputationalModel']} })
    model_software: Optional[str] = Field(default=None, description="""Software/toolbox for running the model (e.g., COBRApy, COBRA Toolbox)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    model_format: Optional[str] = Field(default=None, description="""File format (e.g., SBML, MATLAB, JSON, ONNX)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputationalModel']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'ProteinStructure']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'PublicationReference']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ModelVariable(ConfiguredBaseModel):
    """
    A variable in a computational model, identified by a human-readable name, with an optional dataset_identifier for the native name in the model file and ontology term mappings (e.g., LOINC for clinical observables, CHEBI for metabolites, HP for phenotypic readouts).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use \'name\' for human-readable display (e.g., "Plasma '
                      'Calcium")',
                      "Use 'dataset_identifier' for the native model name (e.g., SBML "
                      'species "P", COBRA reaction "R_0001")',
                      'Map to LOINC codes for clinical lab measurements to link model '
                      'outputs to CDEs',
                      'Map to CHEBI for metabolite variables, HP for phenotypic '
                      'readouts'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    dataset_identifier: Optional[str] = Field(default=None, description="""Native identifier for this variable in the source dataset or model (e.g., SBML species ID, database column name, COBRA reaction ID). When the parent context already specifies the dataset (e.g., a ComputationalModel with model_id), this field gives the local name within that dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariable'],
         'examples': [{'value': 'ECCPhos'}, {'value': 'Qbone'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariable', 'EpidemiologyInfo'],
         'examples': [{'value': 'cm'}]} })
    mappings_list: Optional[list[ModelVariableDescriptor]] = Field(default=None, description="""Ontology term mappings for a model variable (LOINC, CHEBI, HP, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariable', 'Biochemical']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class SeverityTier(ConfiguredBaseModel):
    """
    A threshold-severity pair defining one tier in a severity scale
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'name': {'description': 'Severity label (e.g., "mild", '
                                                '"moderate", "severe")',
                                 'name': 'name',
                                 'required': True},
                        'threshold': {'description': 'The variable value at which this '
                                                     'severity tier activates',
                                      'name': 'threshold',
                                      'required': True}}})

    threshold: float = Field(default=..., description="""The variable value at which this severity tier activates""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeverityTier', 'ModelVariableDescriptor']} })
    name: str = Field(default=..., description="""Severity label (e.g., \"mild\", \"moderate\", \"severe\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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


class ModelVariableDescriptor(Descriptor):
    """
    A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, etc.). When the mapped term is an HP phenotype, optional threshold fields specify when the variable value activates that phenotype and at what severity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'severity_scale': {'description': 'Ordered severity tiers for '
                                                          'graded phenotype activation',
                                           'name': 'severity_scale'},
                        'term': {'description': 'Ontology term reference (LOINC code, '
                                                'CHEBI term, HP term, etc.)',
                                 'name': 'term'},
                        'threshold': {'description': 'Value at which the mapped '
                                                     'phenotype activates',
                                      'name': 'threshold'},
                        'threshold_direction': {'description': 'Whether the phenotype '
                                                               'activates above or '
                                                               'below the threshold',
                                                'name': 'threshold_direction'}}})

    threshold: Optional[float] = Field(default=None, description="""Value at which the mapped phenotype activates""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeverityTier', 'ModelVariableDescriptor']} })
    threshold_direction: Optional[ThresholdDirectionEnum] = Field(default=None, description="""Whether the phenotype activates above or below the threshold""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariableDescriptor']} })
    severity_scale: Optional[list[SeverityTier]] = Field(default=None, description="""Ordered severity tiers for graded phenotype activation""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariableDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Ontology term reference (LOINC code, CHEBI term, HP term, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


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

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, description="""Clinical or mechanistic overlaps, shared presentations, and diagnostic considerations with the focal disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    distinguishing_features: Optional[list[str]] = Field(default=None, description="""Key clinical, laboratory, imaging, or epidemiological features that help differentiate this condition from the focal disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, description="""Additional clinical notes or management considerations""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    disease_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO disease term for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis', 'Disease']} })


class Subtype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    display_name: Optional[str] = Field(default=None, description="""Human-readable display name for a subtype, used when the name (which serves as the FK target) is too terse for comfortable display. Optional; when absent, renderers should fall back to name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype']} })
    subtype_term: Optional[SubtypeDescriptor] = Field(default=None, description="""The ontology term grounding this subtype or cancer facet value. Prefer MONDO when available; use NCIT for oncology-specific subtype refinement when needed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype']} })
    mappings: Optional[DiseaseMappings] = Field(default=None, description="""External identifier mappings for this disease or subtype (SSSOM-inspired)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Disease']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Pathophysiology']} })
    geography: Optional[list[GeographyTerm]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype'], 'examples': [{'value': "['Philippines']"}]} })
    classification: Optional[str] = Field(default=None, description="""Classification scheme this subtype belongs to (e.g., 'complementation_group', 'pathway_tier', 'histological', 'molecular', 'clinical_phenotype').""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype']} })
    children: Optional[list[str]] = Field(default=None, description="""Names of other subtypes in this list that are members/children of this grouping subtype. Used to express cross-scheme relationships (e.g., a pathway_tier subtype grouping complementation_group subtypes).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    subtype_frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, description="""Frequency of this subtype among all cases of the parent disease (e.g., '60-70%', '~15%'). Distinct from phenotype frequency.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['Subtype']} })
    inheritance: Optional[list[Inheritance]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })


class EvidenceItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    reference: Optional[str] = Field(default=None, description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    reference_title: Optional[str] = Field(default=None, description="""The title of the referenced publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'], 'recommended': True} })
    supports: Optional[EvidenceItemSupportEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'], 'examples': [{'value': 'SUPPORT'}]} })
    evidence_source: Optional[EvidenceSourceEnum] = Field(default=None, description="""Origin of the evidence item (human clinical, model organism, in vitro, or computational)""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'], 'recommended': False} })
    snippet: Optional[str] = Field(default=None, description="""An exact excerpt/quote from the referenced publication that supports or refutes the claim""", json_schema_extra = { "linkml_meta": {'comments': ['This is automatically validated by the '
                      'linkml-reference-validator tool.'],
         'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'At the moment there is no healing therapy, so early '
                                'kidney transplant is a fundamental tool to improve '
                                'prognosis.'}],
         'implements': ['linkml:excerpt']} })
    explanation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'There is no curative treatment for nephronophthisis, '
                                'indicating that supportive care, including '
                                'symptomatic treatment and monitoring, is currently '
                                'applied to manage associated complications.'}]} })
    images: Optional[list[str]] = Field(default=None, description="""Relative paths to image files (figures, charts, micrographs) sourced from deep-research artifacts that directly support this specific evidence claim. Paths are relative to the research/ directory and must correspond to an artifact file committed to the repository. Only include images that are directly relevant to the claim being evidenced — do not include images for general illustrative purposes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'Feingold_Syndrome-deep-research-falcon_artifacts/image-1.png'}]} })


class CausalEdge(ConfiguredBaseModel):
    """
    A reference to a downstream effect or consequence in a causal relationship
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'causal_link_type': {'description': 'Encodes directness and '
                                                            'whether omitted '
                                                            'intermediates are known '
                                                            'versus unknown',
                                             'name': 'causal_link_type'},
                        'evidence': {'description': 'Evidence that supports this '
                                                    'specific edge (not just the '
                                                    'parent node-level claim)',
                                     'name': 'evidence'},
                        'hypothesis_groups': {'description': 'One or more hypothesis '
                                                             'IDs used to group edges '
                                                             'within alternative or '
                                                             'superimposed models',
                                              'name': 'hypothesis_groups'},
                        'intermediate_mechanisms': {'description': 'Free-text '
                                                                   'intermediates '
                                                                   'bridging source '
                                                                   'and target when '
                                                                   'using an indirect '
                                                                   'edge',
                                                    'name': 'intermediate_mechanisms'}}})

    target: str = Field(default=..., description="""The name of the target element in a causal relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence that supports this specific edge (not just the parent node-level claim)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    hypothesis_groups: Optional[list[str]] = Field(default=None, description="""One or more hypothesis IDs used to group edges within alternative or superimposed models""", json_schema_extra = { "linkml_meta": {'domain_of': ['CausalEdge']} })
    causal_link_type: Optional[CausalLinkTypeEnum] = Field(default=None, description="""Encodes directness and whether omitted intermediates are known versus unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['CausalEdge']} })
    intermediate_mechanisms: Optional[list[str]] = Field(default=None, description="""Free-text intermediates bridging source and target when using an indirect edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['CausalEdge']} })


class TreatmentMechanismTarget(ConfiguredBaseModel):
    """
    Links a treatment to a specific pathophysiology mechanism node it targets. Enables reasoning about which downstream phenotypes should respond to therapy and why resistance may emerge when the causal chain shifts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'evidence': {'description': 'Evidence that this treatment '
                                                    'targets this specific mechanism',
                                     'name': 'evidence'},
                        'target': {'description': 'Name of the pathophysiology entry '
                                                  'this treatment targets. Must match '
                                                  'a pathophysiology name in the same '
                                                  'disease file.',
                                   'name': 'target'}}})

    target: str = Field(default=..., description="""Name of the pathophysiology entry this treatment targets. Must match a pathophysiology name in the same disease file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    treatment_effect: Optional[TreatmentEffectEnum] = Field(default=None, description="""How the treatment affects the targeted mechanism""", json_schema_extra = { "linkml_meta": {'domain_of': ['TreatmentMechanismTarget']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence that this treatment targets this specific mechanism""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class ModelMechanismLink(ConfiguredBaseModel):
    """
    Links an experimental model to a specific pathophysiology mechanism node, with optional assertion text describing the aspect of the mechanism that the model recapitulates, perturbs, or reads out.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'Brief assertion-level note '
                                                       'describing what facet of the '
                                                       'linked mechanism the model '
                                                       'captures or assays.',
                                        'name': 'description'},
                        'evidence': {'description': 'Evidence that this model is '
                                                    'informative for the linked '
                                                    'mechanism',
                                     'name': 'evidence'},
                        'target': {'description': 'Name of the pathophysiology entry '
                                                  'this model is linked to. Must match '
                                                  'a pathophysiology name in the same '
                                                  'disease file.',
                                   'name': 'target'}}})

    target: str = Field(default=..., description="""Name of the pathophysiology entry this model is linked to. Must match a pathophysiology name in the same disease file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    description: Optional[str] = Field(default=None, description="""Brief assertion-level note describing what facet of the linked mechanism the model captures or assays.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence that this model is informative for the linked mechanism""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class BiomarkerReadout(ConfiguredBaseModel):
    """
    Links a biochemical biomarker to a pathograph node that it measures, reflects, predicts, or pharmacodynamically reports on. This is an observational readout link, not a causal claim that the biomarker causes the target mechanism or phenotype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'direction': {'description': 'Direction of association between '
                                                     'biomarker level/presence and the '
                                                     'linked event or endpoint.',
                                      'name': 'direction'},
                        'endpoint_context': {'description': 'Diagnostic, prognostic, '
                                                            'monitoring, '
                                                            'pharmacodynamic, or '
                                                            'candidate-surrogate use '
                                                            'context.',
                                             'name': 'endpoint_context'},
                        'evidence': {'description': 'Evidence supporting this '
                                                    'biomarker-to-pathograph-node '
                                                    'readout link',
                                     'name': 'evidence'},
                        'interpretation': {'description': 'Human-readable '
                                                          'interpretation of the link '
                                                          'for display and curation '
                                                          'review.',
                                           'name': 'interpretation'},
                        'regulatory_endpoint_refs': {'description': 'Source-table '
                                                                    'regulatory '
                                                                    'endpoint row IDs '
                                                                    'linked to this '
                                                                    'readout. Keep '
                                                                    'regulatory '
                                                                    'details in the '
                                                                    'source table; use '
                                                                    'this field only '
                                                                    'as a local bridge '
                                                                    'from disease '
                                                                    'biology to '
                                                                    'regulatory '
                                                                    'context.',
                                                     'name': 'regulatory_endpoint_refs'},
                        'relationship': {'description': 'How the biomarker relates to '
                                                        'the linked pathograph node.',
                                         'name': 'relationship',
                                         'required': True},
                        'target': {'description': 'Name of the pathograph node this '
                                                  'biomarker reports on. Prefer a '
                                                  'pathophysiology entry; phenotype '
                                                  'targets are also allowed when the '
                                                  'biomarker is explicitly tied to a '
                                                  'clinical manifestation.',
                                   'name': 'target',
                                   'required': True}}})

    target: str = Field(default=..., description="""Name of the pathograph node this biomarker reports on. Prefer a pathophysiology entry; phenotype targets are also allowed when the biomarker is explicitly tied to a clinical manifestation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout']} })
    relationship: BiomarkerReadoutRelationshipEnum = Field(default=..., description="""How the biomarker relates to the linked pathograph node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerReadout']} })
    direction: Optional[BiomarkerReadoutDirectionEnum] = Field(default=None, description="""Direction of association between biomarker level/presence and the linked event or endpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'BiomarkerReadout']} })
    endpoint_context: Optional[BiomarkerEndpointContextEnum] = Field(default=None, description="""Diagnostic, prognostic, monitoring, pharmacodynamic, or candidate-surrogate use context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerReadout']} })
    regulatory_endpoint_refs: Optional[list[str]] = Field(default=None, description="""Source-table regulatory endpoint row IDs linked to this readout. Keep regulatory details in the source table; use this field only as a local bridge from disease biology to regulatory context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerReadout']} })
    interpretation: Optional[str] = Field(default=None, description="""Human-readable interpretation of the link for display and curation review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'BiomarkerReadout']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Evidence supporting this biomarker-to-pathograph-node readout link""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class SurrogateEndpoint(ConfiguredBaseModel):
    """
    A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoint table or a similar authoritative source. This captures an endpoint used as a substitute for direct clinical benefit in a specified disease/use, patient population, approval-pathway, and therapeutic mechanism context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'approval_type': {'name': 'approval_type', 'required': True},
                        'clinical_benefit': {'description': 'Specific clinical benefit '
                                                            'or clinical outcome '
                                                            'predicted by the '
                                                            'surrogate endpoint, when '
                                                            'curated. FDA table rows '
                                                            'may leave this blank.',
                                             'name': 'clinical_benefit'},
                        'clinical_benefit_linkage': {'description': 'BEST-aligned '
                                                                    'relationship to '
                                                                    'clinical benefit. '
                                                                    'FDA table rows '
                                                                    'usually imply '
                                                                    'this via the '
                                                                    'approval pathway '
                                                                    'rather than '
                                                                    'naming a specific '
                                                                    'clinical outcome.',
                                                     'name': 'clinical_benefit_linkage',
                                                     'required': True},
                        'disease_or_use': {'name': 'disease_or_use', 'required': True},
                        'endpoint_validation_level': {'description': 'BEST-aligned '
                                                                     'level. For '
                                                                     'FDA-table rows '
                                                                     'this is derived '
                                                                     'from approval '
                                                                     'type unless a '
                                                                     'curator '
                                                                     'overrides it '
                                                                     'with more '
                                                                     'specific '
                                                                     'evidence.',
                                                      'name': 'endpoint_validation_level',
                                                      'required': True},
                        'mapping_status': {'name': 'mapping_status', 'required': True},
                        'patient_population': {'name': 'patient_population',
                                               'required': True},
                        'row_id': {'name': 'row_id', 'required': True},
                        'source_row_number': {'name': 'source_row_number',
                                              'required': True},
                        'source_sheet': {'name': 'source_sheet', 'required': True},
                        'source_table': {'name': 'source_table', 'required': True},
                        'surrogate_endpoint': {'name': 'surrogate_endpoint',
                                               'required': True}}})

    row_id: str = Field(default=..., description="""Stable row identifier assigned during source-table curation""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    source_table: SurrogateEndpointTableEnum = Field(default=..., description="""FDA surrogate endpoint table section from which the row was curated""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    source_sheet: str = Field(default=..., description="""Spreadsheet worksheet name or source table label""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    source_row_number: int = Field(default=..., description="""Row number in the source spreadsheet worksheet""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    disease_or_use: str = Field(default=..., description="""FDA disease or use text for a surrogate endpoint row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    patient_population: str = Field(default=..., description="""FDA patient population text for a surrogate endpoint row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    surrogate_endpoint: str = Field(default=..., description="""Surrogate endpoint text from the FDA surrogate endpoint table""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    approval_type: SurrogateEndpointApprovalTypeEnum = Field(default=..., description="""FDA approval pathway context for the surrogate endpoint row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    drug_mechanism_of_action: Optional[str] = Field(default=None, description="""FDA drug mechanism-of-action context for the surrogate endpoint row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'SurrogateEndpoint',
                       'ProgressionInfo',
                       'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    endpoint_validation_level: SurrogateEndpointValidationLevelEnum = Field(default=..., description="""BEST-aligned level. For FDA-table rows this is derived from approval type unless a curator overrides it with more specific evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    clinical_benefit_linkage: ClinicalBenefitLinkageEnum = Field(default=..., description="""BEST-aligned relationship to clinical benefit. FDA table rows usually imply this via the approval pathway rather than naming a specific clinical outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    clinical_benefit: Optional[str] = Field(default=None, description="""Specific clinical benefit or clinical outcome predicted by the surrogate endpoint, when curated. FDA table rows may leave this blank.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    clinical_benefit_linkage_basis: Optional[str] = Field(default=None, description="""Explanation of how the clinical-benefit linkage was inferred or curated""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    footnotes: Optional[list[SurrogateEndpointFootnoteEnum]] = Field(default=None, description="""FDA workbook footnote semantics attached to the source row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    context_of_use: Optional[str] = Field(default=None, description="""Concise context-of-use statement combining disease/use, population, endpoint, approval type, and therapeutic mechanism""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    mapping_status: SurrogateEndpointMappingStatusEnum = Field(default=..., description="""Status of mapping the FDA disease/use row to dismech disease entries""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    mapped_diseases: Optional[list[str]] = Field(default=None, description="""Names of dismech disease entries mapped or candidate-mapped to this FDA row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    mapped_disease_files: Optional[list[str]] = Field(default=None, description="""Relative paths of dismech disease YAML files mapped or candidate-mapped to this FDA row""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint']} })
    mapping_notes: Optional[str] = Field(default=None, description="""Notes on code-to-concept mapping decisions for this signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'AssociationSignal']} })
    source_url: Optional[str] = Field(default=None, description="""URL of the source page for a curated assertion or source collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_url: Optional[str] = Field(default=None, description="""URL of the source workbook or downloadable data file""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_sha256: Optional[str] = Field(default=None, description="""SHA-256 checksum of the downloaded source workbook used for import""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_content_current_as_of: Optional[date] = Field(default=None, description="""Date shown by the source as the content-current-as-of date""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    retrieved_date: Optional[date] = Field(default=None, description="""Date on which the source was retrieved for curation""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class SurrogateEndpointCollection(ConfiguredBaseModel):
    """
    A source-level collection of curated regulatory surrogate endpoint assertions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'surrogate_endpoints': {'name': 'surrogate_endpoints',
                                                'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    source_url: Optional[str] = Field(default=None, description="""URL of the source page for a curated assertion or source collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_url: Optional[str] = Field(default=None, description="""URL of the source workbook or downloadable data file""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_sha256: Optional[str] = Field(default=None, description="""SHA-256 checksum of the downloaded source workbook used for import""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_content_current_as_of: Optional[date] = Field(default=None, description="""Date shown by the source as the content-current-as-of date""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    retrieved_date: Optional[date] = Field(default=None, description="""Date on which the source was retrieved for curation""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    surrogate_endpoints: list[SurrogateEndpoint] = Field(default=..., description="""Curated surrogate endpoint assertions""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ProteinStructure(ConfiguredBaseModel):
    """
    A 3D protein structure from PDB or AlphaFold relevant to understanding a treatment's mechanism of action. Enables embedded 3D visualization of drug-target interactions via Mol* viewer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    pdb_id: str = Field(default=..., description="""PDB accession code (e.g., 3TCT) or AlphaFold identifier (e.g., AF-P02766-F1). Used to construct viewer URLs and fetch structure data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure']} })
    description: Optional[str] = Field(default=None, description="""Brief description of what the structure shows (e.g., drug-target co-crystal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    resolution_angstrom: Optional[float] = Field(default=None, description="""Structure resolution in angstroms (for experimental structures)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure']} })
    method: Optional[str] = Field(default=None, description="""Experimental method (X-ray, cryo-EM, NMR) or prediction method (AlphaFold)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure', 'AssociationSignal', 'GOEnrichment']} })
    ligand: Optional[str] = Field(default=None, description="""Name of bound drug/ligand if this is a co-crystal structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure']} })
    target_protein: Optional[str] = Field(default=None, description="""Name of the protein target in the structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure']} })
    publication: Optional[str] = Field(default=None, description="""Reference for the structure deposition or associated paper (e.g., PMID:12345678)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'ProteinStructure']} })


class PublicationReference(ConfiguredBaseModel):
    """
    A reference to a publication with associated findings
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'reference': {'identifier': True,
                                      'name': 'reference',
                                      'required': True}}})

    reference: str = Field(default=..., description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'PublicationReference', 'TrackedIssue'],
         'implements': ['linkml:title']} })
    found_in: Optional[list[str]] = Field(default=None, description="""Deep-research output files where this reference was cited""", json_schema_extra = { "linkml_meta": {'domain_of': ['PublicationReference']} })
    tags: Optional[list[ReferenceTagEnum]] = Field(default=None, description="""Authoritative-source tags for a reference (e.g. GeneReviews). Populated programmatically by scripts/tag_references.py; use `just tag-references` to refresh.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PublicationReference']} })
    findings: Optional[list[Finding]] = Field(default=None, description="""Key findings or claims extracted from this source (publication or dataset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'ExperimentalModel',
                       'ComputationalModel',
                       'PublicationReference']} })


class ExternalAssertion(ConfiguredBaseModel):
    """
    An externally curated assertion or registry record relevant to a disease or variant, such as a ClinGen gene-disease validity assertion or a ClinGen Allele Registry record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'external_id': {'name': 'external_id', 'required': True},
                        'source': {'name': 'source', 'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    source: str = Field(default=..., description="""Source dataset or provenance label""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion', 'AssociationSignal']} })
    assertion_type: Optional[str] = Field(default=None, description="""Type/category of the external assertion or registry record""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion']} })
    external_id: str = Field(default=..., description="""Identifier used by the external resource (e.g., CCID:009009, CA2573049045)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion']} })
    url: Optional[str] = Field(default=None, description="""URL for the external assertion or registry record""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion', 'TrackedIssue']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class TrackedIssue(ConfiguredBaseModel):
    """
    Structured pointer to an external tracker issue (typically a GitHub issue) used to record curation provenance. Use this for things like upstream ontology term requests, ontology coverage gaps, schema follow-ups, or any external ticket tied to a dismech object, instead of stashing raw URLs in free-text `notes` fields. Attachable at multiple levels of the model (disease entries, mappings, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'title': {'description': 'Short human-readable title of the '
                                                 'tracked issue.',
                                  'name': 'title'},
                        'url': {'description': 'Canonical URL of the tracked issue.',
                                'name': 'url',
                                'required': True}}})

    url: str = Field(default=..., description="""Canonical URL of the tracked issue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion', 'TrackedIssue']} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title of the tracked issue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'PublicationReference', 'TrackedIssue'],
         'implements': ['linkml:title']} })
    tracked_issue_role: Optional[str] = Field(default=None, description="""Role this tracked issue plays relative to the dismech content it is attached to. Free-text but common values include \"ontology_term_request\", \"ontology_coverage_gap\", \"schema_followup\", \"curation_followup\", and \"external_tracker_link\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackedIssue'],
         'examples': [{'value': 'ontology_term_request'}, {'value': 'schema_followup'}]} })
    tracked_issue_status: Optional[str] = Field(default=None, description="""Last known status of the tracked issue (e.g., \"OPEN\", \"CLOSED\", \"MERGED\"). This is a curator-recorded snapshot and may drift from the live tracker state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackedIssue'],
         'examples': [{'value': 'OPEN'}, {'value': 'CLOSED'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Finding(ConfiguredBaseModel):
    """
    A key finding or claim extracted from a source (publication or dataset)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    statement: str = Field(default=..., description="""A key finding or claim from the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    supporting_text: Optional[str] = Field(default=None, description="""Exact excerpt/quote from the publication supporting the statement""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class Prevalence(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    percentage: Optional[Union[float, int, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'float'},
                    {'range': 'integer'},
                    {'description': 'for ranges', 'range': 'string'}],
         'domain_of': ['Prevalence'],
         'examples': [{'value': '0.1'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ProgressionInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    phase: Optional[PhaseTerm] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial', 'ProgressionInfo'],
         'examples': [{'value': 'Active TB'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'SurrogateEndpoint',
                       'ProgressionInfo',
                       'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    incubation_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '3-14'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    incubation_years: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '2-15'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    duration_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '2-5'}]} })
    duration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': 'Variable'}]} })


class EpidemiologyInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    minimum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    maximum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    mean_range: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    factors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo'],
         'examples': [{'value': "['Genetic', 'Environmental', 'Infectious', "
                                "'Autoimmune', 'Metabolic', 'Neoplastic', 'Traumatic', "
                                "'Iatrogenic', 'Idiopathic']"}]} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariable', 'EpidemiologyInfo'],
         'examples': [{'value': 'cm'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class Pathophysiology(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel', 'Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    biological_processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: TNF-alpha Production}]'}]} })
    molecular_functions: Optional[list[MolecularFunctionDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Kinase Activity}]'}]} })
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Pathophysiology']} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    conforms_to: Optional[str] = Field(default=None, description="""Reference to a mechanism module that this pathophysiology node is an organ-specific instance of. Value is a path relative to kb/modules/ (e.g., \"fibrotic_response\") plus an optional node name after a hash (e.g., \"fibrotic_response#Mesenchymal Cell Activation\"). Used for cross-disorder consistency checking: if a node declares conformance, it should include the expected cell types, biological processes, and causal edges defined in the referenced module node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology']} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    consequence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': 'Leads to abnormal sexual development and bone '
                                'maturation.'}]} })
    consequences: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'todos': ['unify consequences and consequence']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'ExperimentalPerturbation',
                       'Pathophysiology',
                       'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    pathways: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Wnt Pathway}]'}]} })
    downstream: Optional[list[CausalEdge]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{target: Tissue Damage, causal_link_type: '
                                'INDIRECT_UNKNOWN_INTERMEDIATES, hypothesis_groups: '
                                '[canonical_model]}]'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    subtypes: Optional[list[str]] = Field(default=None, description="""Names of subtypes (foreign keys to this disease's `has_subtypes[].name`) associated with a phenotype, biochemical finding, pathophysiology node, or other subtyped entry. Use this multivalued form when an item is characteristic of more than one subtype with overlapping features. For single-subtype associations, the scalar `subtype` slot may still be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical'],
         'examples': [{'value': "['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4']"},
                      {'value': "['Type 1', 'Type 2']"}]} })
    cellular_components: Optional[list[CellularComponentDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Peroxisome}]'}]} })
    protein_complexes: Optional[list[ProteinComplexDescriptor]] = Field(default=None, description="""Protein complexes that gene products participate in""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: FA nuclear complex, term: {id: '
                                '"GO:0043240", label: "Fanconi anaemia nuclear '
                                'complex"}}]'}]} })
    chemical_entities: Optional[list[ChemicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Plasmalogen}]'}]} })
    gene_products: Optional[list[GeneProductDescriptor]] = Field(default=None, description="""Gene products (proteins, fusion proteins, oncoproteins) involved in this pathophysiology mechanism. Use NCIT terms for specific proteins.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: BCR-ABL1 fusion protein, term: {id: '
                                'NCIT:C16325, label: BCR/ABL1 Fusion Protein}}]'}]} })
    triggers: Optional[list[TriggerDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Viral Infections}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment',
                       'ExperimentalReadout',
                       'Pathophysiology',
                       'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    mechanisms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': "['Thrombocytopenia', 'Platelet Dysfunction', "
                                "'Disseminated Intravascular Coagulation (DIC)']"}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    genetic_context: Optional[GeneticContext] = Field(default=None, description="""The genetic context under which this qualification applies. May specify genes, mutation types, zygosity, complementation groups, or complex genotypes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Pathophysiology']} })
    pdb_structures: Optional[list[ProteinStructure]] = Field(default=None, description="""Experimental or predicted 3D protein structures relevant to this treatment's mechanism of action. Typically co-crystal structures of the drug bound to its target protein, or AlphaFold predictions of the drug target.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Treatment']} })
    mechanism_confidence: Optional[MechanismConfidenceEnum] = Field(default=None, description="""Level of confidence in this pathophysiology mechanism. If not specified, the mechanism is assumed to be established.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology']} })


class Phenotype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    phenotype_term: Optional[PhenotypeDescriptor] = Field(default=None, description="""The HP term for this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalReadout', 'Phenotype']} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    diagnostic: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'HistopathologyFinding']} })
    sequelae: Optional[list[CausalEdge]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype'],
         'examples': [{'value': '[{target: Diabetic Ketoacidosis}, {target: Chronic '
                                'Complications}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    subtypes: Optional[list[str]] = Field(default=None, description="""Names of subtypes (foreign keys to this disease's `has_subtypes[].name`) associated with a phenotype, biochemical finding, pathophysiology node, or other subtyped entry. Use this multivalued form when an item is characteristic of more than one subtype with overlapping features. For single-subtype associations, the scalar `subtype` slot may still be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical'],
         'examples': [{'value': "['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4']"},
                      {'value': "['Type 1', 'Type 2']"}]} })
    phenotype_contexts: Optional[list[PhenotypeContext]] = Field(default=None, description="""Context-specific qualifications of this phenotype's frequency, severity, or onset. Each context can optionally specify a genetic context, demographic stratum, or disease subtype. When no context qualifiers are set, provides evidence for the base frequency/severity claim (addressing the frequency-evidence separation problem).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })


class Biochemical(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    biomarker_term: Optional[BiomarkerDescriptor] = Field(default=None, description="""Ontology term for a biomarker (from NCIT)""", json_schema_extra = { "linkml_meta": {'comments': ['Use NCIT terms for biomarkers (proteins, genes, fusion '
                      'products)',
                      'NCIT:C16342 (Biomarker) is the root class for validation'],
         'domain_of': ['ExperimentalReadout', 'Biochemical']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    readouts: Optional[list[BiomarkerReadout]] = Field(default=None, description="""Links this biomarker to disease pathograph nodes that it measures, reflects, predicts, or pharmacodynamically reports on. The target should be a named pathograph node, typically a pathophysiology mechanism.""", json_schema_extra = { "linkml_meta": {'comments': ['Target names should match pathophysiology or phenotype entry '
                      'names in the same disease file',
                      'Readout links are observational/associative, not causal '
                      'disease-progression edges',
                      'Use evidence on the readout link when the '
                      "biomarker-to-mechanism mapping is distinct from the biomarker's "
                      'own evidence'],
         'domain_of': ['Experiment', 'Biochemical']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    specificity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical'], 'examples': [{'value': 'High'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    subtypes: Optional[list[str]] = Field(default=None, description="""Names of subtypes (foreign keys to this disease's `has_subtypes[].name`) associated with a phenotype, biochemical finding, pathophysiology node, or other subtyped entry. Use this multivalued form when an item is characteristic of more than one subtype with overlapping features. For single-subtype associations, the scalar `subtype` slot may still be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical'],
         'examples': [{'value': "['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4']"},
                      {'value': "['Type 1', 'Type 2']"}]} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel', 'Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment',
                       'ExperimentalReadout',
                       'Pathophysiology',
                       'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    mappings_list: Optional[list[ModelVariableDescriptor]] = Field(default=None, description="""Ontology term mappings for a model variable (LOINC, CHEBI, HP, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelVariable', 'Biochemical']} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
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

    name: str = Field(default=..., description="""Name of the histopathologic finding""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    finding_term: Optional[HistopathologyFindingDescriptor] = Field(default=None, description="""Ontology term for a histopathologic finding (from NCIT or HP)""", json_schema_extra = { "linkml_meta": {'comments': ['Use NCIT terms from Morphologic Finding (C35867) or Histologic '
                      'Grade (C18000)',
                      'Use HP terms for rosettes and cell morphology abnormalities '
                      '(HP:0025461 descendants)'],
         'domain_of': ['HistopathologyFinding']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the finding and its clinical significance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, description="""How frequently this finding is observed in the disease""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    diagnostic: Optional[bool] = Field(default=None, description="""Whether this finding is pathognomonic or highly diagnostic""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'HistopathologyFinding']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, description="""Context in which this finding is observed (e.g., specific subtype)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })


class Genetic(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    gene_term: Optional[GeneDescriptor] = Field(default=None, description="""The HGNC term for this gene""", json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    association: Optional[str] = Field(default=None, description="""Free-text descriptor of how the gene is associated with the disease. For a controlled vocabulary, also set `relationship_type`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'], 'examples': [{'value': 'Susceptibility'}]} })
    relationship_type: Optional[GeneDiseaseRelationshipEnum] = Field(default=None, description="""Controlled-vocabulary classification of the gene-disease relationship (e.g., causative, risk factor, modifier, somatic driver). Use this in addition to the free-text `association` slot when possible.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'], 'examples': [{'value': 'RISK_FACTOR'}]} })
    variant_origin: Optional[VariantOriginEnum] = Field(default=None, description="""The origin of disease-associated variation in this gene (germline, somatic, de novo, or both). Bound to GENO allele origin terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'], 'examples': [{'value': 'SOMATIC'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['PhenotypeContext',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    variants: Optional[list[Variant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    features: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'],
         'examples': [{'value': 'DNA virus from the Orthopoxvirus genus'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
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

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    chemicals: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental'], 'examples': [{'value': "['Phenol']"}]} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    exposure_term: Optional[ExposureDescriptor] = Field(default=None, description="""The ECTO/XCO term for this exposure event""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Environmental']} })
    environment_context: Optional[EnvironmentDescriptor] = Field(default=None, description="""The ENVO term for the environmental context/setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental']} })
    food_source: Optional[FoodDescriptor] = Field(default=None, description="""The FOODON or CHEBI term for a specific food, beverage, nutrient, mineral, or supplement source or vehicle relevant to an exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental', 'InfectiousAgent']} })


class Disease(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'creation_date': {'description': 'Timestamp for initial '
                                                         'creation of this disease '
                                                         'entry. Keep this stable '
                                                         'after first set.',
                                          'name': 'creation_date'},
                        'name': {'description': 'Preferred name for the disease',
                                 'name': 'name',
                                 'required': True},
                        'updated_date': {'description': 'Timestamp for the latest '
                                                        'substantive update to this '
                                                        'disease entry. Update this '
                                                        'whenever curated content '
                                                        'changes.',
                                         'name': 'updated_date'}}})

    name: str = Field(default=..., description="""Preferred name for the disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    disease_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO disease term for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis', 'Disease']} })
    creation_date: Optional[str] = Field(default=None, description="""Timestamp for initial creation of this disease entry. Keep this stable after first set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'ComorbidityAssociation'], 'recommended': True} })
    updated_date: Optional[str] = Field(default=None, description="""Timestamp for the latest substantive update to this disease entry. Update this whenever curated content changes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'ComorbidityAssociation'], 'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    references: Optional[list[PublicationReference]] = Field(default=None, description="""Top-level list of references with their key findings for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    parents: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'examples': [{'value': "['Bacterial Infection']"}]} })
    has_subtypes: Optional[list[Subtype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'InfectiousAgent']} })
    prevalence: Optional[list[Prevalence]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    progression: Optional[list[ProgressionInfo]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })
    mechanistic_hypotheses: Optional[list[MechanisticHypothesis]] = Field(default=None, description="""Disease-level mechanistic hypotheses that group and annotate causal edges""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    histopathology: Optional[list[HistopathologyFinding]] = Field(default=None, description="""Histopathologic findings including microscopic morphology, architectural patterns, cellular features, growth patterns, and histologic grading.""", json_schema_extra = { "linkml_meta": {'comments': ['Separate from phenotypes as these are tissue-level microscopic '
                      'observations',
                      'Use NCIT Morphologic Finding (C35867) or Histologic Grade '
                      '(C18000) terms',
                      "{'For cancer': 'includes grade, differentiation, growth "
                      "patterns, necrosis'}",
                      "{'For other diseases': 'may include architectural changes, "
                      "cellular infiltrates'}"],
         'domain_of': ['Disease']} })
    biochemical: Optional[list[Biochemical]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    stages: Optional[list[Stage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    genetic: Optional[list[Genetic]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    variants: Optional[list[Variant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    environmental: Optional[list[Environmental]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    treatments: Optional[list[Treatment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    categories: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    infectious_agent: Optional[list[InfectiousAgent]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    agent_life_cycle: Optional[AgentLifeCycle] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    transmission: Optional[list[Transmission]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    modeling_considerations: Optional[list[ModelingConsideration]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    epidemiology: Optional[list[EpidemiologyInfo]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'examples': [{'value': "['Global']"}]} })
    diagnosis: Optional[list[Diagnosis]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    differential_diagnoses: Optional[list[DifferentialDiagnosis]] = Field(default=None, description="""Differential diagnoses - similar diseases that must be ruled out""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'recommended': False} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    animal_models: Optional[list[AnimalModel]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    experimental_models: Optional[list[ExperimentalModel]] = Field(default=None, description="""Disease-relevant organoids, cell lines, chip systems, cocultures, and related experimental models curated as mechanism or translational resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'recommended': False} })
    datasets: Optional[list[Dataset]] = Field(default=None, description="""Publicly available datasets relevant to disease research""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment', 'Disease'], 'recommended': True} })
    clinical_trials: Optional[list[ClinicalTrial]] = Field(default=None, description="""Clinical trials relevant to disease treatment and research""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'recommended': False} })
    surrogate_endpoints: Optional[list[SurrogateEndpoint]] = Field(default=None, description="""Curated surrogate endpoint assertions""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease']} })
    computational_models: Optional[list[ComputationalModel]] = Field(default=None, description="""Computational models (metabolic, mechanistic, ML, digital twins) for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    classifications: Optional[DiseaseClassifications] = Field(default=None, description="""Classification assignments for this disease from various nosologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    definitions: Optional[list[Definition]] = Field(default=None, description="""Definitions or diagnostic criteria for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    mappings: Optional[DiseaseMappings] = Field(default=None, description="""External identifier mappings for this disease or subtype (SSSOM-inspired)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Disease']} })
    external_assertions: Optional[list[ExternalAssertion]] = Field(default=None, description="""External curated assertions or registry records relevant to this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Variant']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    discussions: Optional[list[Discussion]] = Field(default=None, description="""Open or recently-resolved discussion items attached to this entry. Each Discussion is a thread-like object with a `prompt`, a `kind` (OPEN_QUESTION, KNOWLEDGE_GAP, CONTROVERSY, etc.), a `status`, optional `attaches_to` pointers to specific nodes/gaps, an optional `proposed_experiments` block, and an `evidence` block reusing the standard EvidenceItem shape for citing primary literature, community commentary (e.g., Alzforum), and forum/issue threads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    curation_history: Optional[list[CurationEvent]] = Field(default=None, description="""Audit trail of AI-assisted curation events""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })

    @field_validator('creation_date')
    def pattern_creation_date(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid creation_date format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid creation_date format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('updated_date')
    def pattern_updated_date(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid updated_date format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid updated_date format: {v}"
            raise ValueError(err_msg)
        return v


class Stage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })
    substages: Optional[list[Stage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Stage']} })


class AgentLifeCycle(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    life_cycle_stages: Optional[list[AgentLifeCycleStage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AgentLifeCycle']} })
    hosts: Optional[list[HostDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Use NCBITaxon terms for host organisms',
                      'Use the role slot to indicate definitive, intermediate, '
                      'reservoir, or accidental host'],
         'domain_of': ['AgentLifeCycle']} })
    vectors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AgentLifeCycle']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    life_cycle_stage_term: Optional[LifeCycleStageDescriptor] = Field(default=None, description="""The OPL term for this agent life cycle stage""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgentLifeCycleStage']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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

    species: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'], 'examples': [{'value': 'Human'}]} })
    genotype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'], 'examples': [{'value': 'HLA-DQ2'}]} })
    background: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'Dataset',
                       'ExperimentalPerturbation',
                       'Subtype',
                       'Pathophysiology',
                       'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    alleles: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    associated_phenotypes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'],
         'examples': [{'value': "['Celiac Disease', 'Type 1 Diabetes', 'Autoimmune "
                                "Thyroid Disease']"}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class Treatment(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    action_category: Optional[MedicalActionCategoryEnum] = Field(default=None, description="""Optional high-level category for a clinical action in the treatments section. Use THERAPEUTIC for actions that treat, prevent, mitigate, or manage disease mechanisms or symptoms; use non-therapeutic categories for screening, diagnosis, monitoring, and genetic counseling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Treatment']} })
    treatment_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this treatment/medical action""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Treatment']} })
    regimen_term: Optional[RegimenDescriptor] = Field(default=None, description="""The NCIT term for this treatment regimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Treatment']} })
    target_phenotypes: Optional[list[PhenotypeDescriptor]] = Field(default=None, description="""Phenotypes that this treatment or trial addresses or targets""", json_schema_extra = { "linkml_meta": {'comments': ["Should reference phenotype names defined in the same disease's "
                      'phenotypes list',
                      'Enables linking treatments/trials to the '
                      'symptoms/manifestations they aim to manage',
                      'Each phenotype can include ontology term references (HP)'],
         'domain_of': ['ClinicalTrial', 'Treatment']} })
    target_mechanisms: Optional[list[TreatmentMechanismTarget]] = Field(default=None, description="""Pathophysiology mechanism nodes that this treatment targets or modulates. Links a treatment to specific steps in the disease's causal graph, enabling inference about which downstream phenotypes should respond to therapy.""", json_schema_extra = { "linkml_meta": {'comments': ['Target names should match pathophysiology entry names in the '
                      'same disease file',
                      'Complements target_phenotypes by explaining WHERE in the causal '
                      'chain the drug acts',
                      'Analogous to DrugMechDB paths but anchored to dismech '
                      'pathophysiology nodes'],
         'domain_of': ['Treatment']} })
    pdb_structures: Optional[list[ProteinStructure]] = Field(default=None, description="""Experimental or predicted 3D protein structures relevant to this treatment's mechanism of action. Typically co-crystal structures of the drug bound to its target protein, or AlphaFold predictions of the drug target.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Treatment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'Biochemical',
                       'HistopathologyFinding',
                       'Stage',
                       'AgentLifeCycle',
                       'AgentLifeCycleStage',
                       'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial',
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
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['HostDescriptor', 'Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    mechanism: Optional[list[Mechanism]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Treatment']} })
    examples: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })


class InfectiousAgent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    infectious_agent_term: Optional[OrganismDescriptor] = Field(default=None, description="""The NCBITaxon term for this infectious agent""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfectiousAgent']} })
    food_source: Optional[FoodDescriptor] = Field(default=None, description="""The FOODON or CHEBI term for a specific food, beverage, nutrient, mineral, or supplement source or vehicle relevant to an exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental', 'InfectiousAgent']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    has_subtypes: Optional[list[Subtype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'InfectiousAgent']} })


class Transmission(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalPerturbation', 'Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })


class Assay(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })


class Diagnosis(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    diagnosis_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this diagnostic procedure""", json_schema_extra = { "linkml_meta": {'comments': ['MAXO includes diagnostic procedures under medical actions',
                      'Use qualifiers with UBERON terms to specify anatomical location '
                      '(e.g., right heart catheterization)'],
         'domain_of': ['Diagnosis']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    results: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Diagnosis'],
         'examples': [{'value': 'Identifies MEFV mutations'}]} })
    markers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Diagnosis'], 'examples': [{'value': 'CRP, ESR, SAA'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })


class Inheritance(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    inheritance_term: Optional[InheritanceDescriptor] = Field(default=None, description="""The HPO mode of inheritance term for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    penetrance: Optional[PenetranceEnum] = Field(default=None, description="""Penetrance classification for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    penetrance_percentage: Optional[str] = Field(default=None, description="""Estimated penetrance percentage or range (e.g., 80-90)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    expressivity: Optional[ExpressivityEnum] = Field(default=None, description="""Expressivity classification for this inheritance pattern""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    de_novo_rate: Optional[str] = Field(default=None, description="""Estimated percentage of de novo cases (e.g., 80)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    parent_of_origin_effect: Optional[str] = Field(default=None, description="""Parent-of-origin effect or bias (e.g., paternal age effect)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inheritance']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })


class Variant(ConfiguredBaseModel):
    """
    A genetic variant associated with a disease, including coding and non-coding regulatory variants. For regulatory variants, use regulatory_category to classify the variant's impact on gene expression (LOE/mLOE/GOE per Cheng et al. 2024).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'ExperimentalPerturbation',
                       'Pathophysiology',
                       'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    functional_effects: Optional[list[FunctionalEffect]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    synonyms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    identifiers: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    external_assertions: Optional[list[ExternalAssertion]] = Field(default=None, description="""External curated assertions or registry records relevant to this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Variant']} })
    sequence_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    clinical_significance: Optional[ClinicalSignificanceEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })
    regulatory_category: Optional[RegulatoryVariantCategoryEnum] = Field(default=None, description="""Functional classification of a variant's impact on gene expression, using the LOE/mLOE/GOE framework (Cheng et al. 2024, PMID:38436667) or traditional coding categories (LOF/GOF/DN).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })


class FunctionalEffect(ConfiguredBaseModel):
    """
    Describes the functional consequence of a genetic variant, including regulatory impact classification (LOE/mLOE/GOE) for non-coding variants and the type of regulatory element affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    function: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })
    regulatory_category: Optional[RegulatoryVariantCategoryEnum] = Field(default=None, description="""Functional classification of a variant's impact on gene expression, using the LOE/mLOE/GOE framework (Cheng et al. 2024, PMID:38436667) or traditional coding categories (LOF/GOF/DN).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })
    regulatory_element_type: Optional[RegulatoryElementTypeEnum] = Field(default=None, description="""Type of gene regulatory element disrupted by a non-coding variant (e.g., promoter, enhancer, silencer, insulator, TAD boundary).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })
    affected_cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, description="""Cell types in which gene expression is specifically gained or lost. Particularly relevant for mLOE variants (modular loss in specific cell types) and GOE variants (ectopic gain in new cell types).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })
    affected_developmental_stage: Optional[str] = Field(default=None, description="""Developmental stage or temporal window in which expression is modularly lost or ectopically gained. Relevant for variants with temporal modularity (e.g., Hemophilia B Leyden).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })
    regulatory_mechanism: Optional[str] = Field(default=None, description="""The specific molecular mechanism by which the regulatory variant exerts its effect (e.g., TFBS disruption, enhancer adoption, promoter switching, repressor site loss, novel TFBS creation, heterochromatin spreading).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })


class Mechanism(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })


class ModelingConsideration(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class ClassificationAssignment(ConfiguredBaseModel):
    """
    Base class for classification assignments with evidence
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: ICDOMorphologyEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: HarrisonsChapterEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: LysosomalStorageEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: MechanisticNosologyEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: IUISCategoryEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    classification_value: ChannelopathyOrganSystemEnum = Field(default=..., description="""The classification value assigned""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICDOMorphologyAssignment',
                       'HarrisonsChapterAssignment',
                       'LysosomalStorageAssignment',
                       'MechanisticNosologyAssignment',
                       'IUISAssignment',
                       'ChannelopathyAssignment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DiseaseClassifications(ConfiguredBaseModel):
    """
    Container for all classification assignments for a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    icdo_morphology: Optional[ICDOMorphologyAssignment] = Field(default=None, description="""ICD-O morphology classification (for neoplastic diseases)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })
    harrisons_chapter: Optional[list[HarrisonsChapterAssignment]] = Field(default=None, description="""Harrison's internal medicine chapter classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })
    lysosomal_storage_category: Optional[LysosomalStorageAssignment] = Field(default=None, description="""Lysosomal storage disease biochemical classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })
    mechanistic_category: Optional[list[MechanisticNosologyAssignment]] = Field(default=None, description="""Mechanistic/pathway-based disease classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })
    iuis_category: Optional[IUISAssignment] = Field(default=None, description="""IUIS primary immunodeficiency classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })
    channelopathy_category: Optional[ChannelopathyAssignment] = Field(default=None, description="""Channelopathy organ system classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseClassifications']} })


class Definition(ConfiguredBaseModel):
    """
    A diagnostic or phenotype definition for the disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'definition_type': {'name': 'definition_type',
                                            'required': True},
                        'name': {'name': 'name', 'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    definition_type: DefinitionTypeEnum = Field(default=..., description="""The type of definition or criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    scope: Optional[str] = Field(default=None, description="""Scope or population for which the definition applies (e.g., adults, pediatrics)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    criteria_sets: Optional[list[CriteriaSet]] = Field(default=None, description="""Named criteria groupings within a definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition']} })
    inclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Inclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    exclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Exclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class CriteriaSet(ConfiguredBaseModel):
    """
    A named criteria grouping within a definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    scope: Optional[str] = Field(default=None, description="""Scope or population for which the definition applies (e.g., adults, pediatrics)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    minimum_required: Optional[int] = Field(default=None, description="""Minimum number of criteria required in this criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['CriteriaSet']} })
    core_clinical_characteristics: Optional[list[CriteriaItem]] = Field(default=None, description="""Core clinical characteristics used in a criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['CriteriaSet']} })
    inclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Inclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    exclusion_criteria: Optional[list[CriteriaItem]] = Field(default=None, description="""Exclusion criteria for a definition or criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['Definition', 'CriteriaSet']} })
    imaging_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Imaging requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['CriteriaSet']} })
    laboratory_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Laboratory or serologic requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['CriteriaSet']} })
    additional_requirements: Optional[list[CriteriaItem]] = Field(default=None, description="""Additional requirements used in a criteria set""", json_schema_extra = { "linkml_meta": {'domain_of': ['CriteriaSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class CriteriaItem(Descriptor):
    """
    A criterion element (clinical feature, test result, imaging requirement)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
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

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ICD10CMTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ICD11FTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class NCITMapping(TermMapping):
    """
    NCIT disease, subtype, or disease/finding ontology mapping for cancer entries
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'NCITDiseaseOrFindingTerm'}],
                                 'name': 'term'}}})

    term: Term = Field(default=..., description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'NCITDiseaseOrFindingTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    mapping_predicate: str = Field(default=..., description="""Relationship between this disease and the mapped term (e.g., skos:exactMatch)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_source: Optional[str] = Field(default=None, description="""Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    mapping_justification: Optional[str] = Field(default=None, description="""Brief rationale or justification for the mapping""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    consistency: Optional[list[MappingConsistency]] = Field(default=None, description="""Consistency assertions for this mapping against other sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermMapping']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
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

    reference: str = Field(default=..., description="""Reference source used to assess consistency (e.g., MONDO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'PublicationReference', 'MappingConsistency'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    consistent: MappingConsistencyEnum = Field(default=..., description="""Consistency status for a mapping relative to a reference source""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingConsistency']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DiseaseMappings(ConfiguredBaseModel):
    """
    Container for external identifier mappings for a disease or subtype
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    icd10cm_mappings: Optional[list[ICD10CMMapping]] = Field(default=None, description="""ICD-10-CM code mappings for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseMappings']} })
    icd11f_mappings: Optional[list[ICD11FMapping]] = Field(default=None, description="""ICD-11 Foundation code mappings for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseMappings']} })
    mondo_mappings: Optional[list[MondoMapping]] = Field(default=None, description="""MONDO disease ontology mappings for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseMappings']} })
    ncit_mappings: Optional[list[NCITMapping]] = Field(default=None, description="""NCIT disease, subtype, or disease/finding mappings""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseMappings']} })


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

    slug: Optional[str] = Field(default=None, description="""Use for leaf conditions; omit when using composition/components""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionDescriptor']} })
    preferred_term: Optional[str] = Field(default=None, description="""The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'ConditionDescriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MONDO disease term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'OPTIONAL',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    composition: Optional[ConditionCompositionEnum] = Field(default=None, description="""Composition type for a composite condition descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionDescriptor']} })
    components: Optional[list[ConditionDescriptor]] = Field(default=None, description="""Component conditions that make up a composite descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionDescriptor']} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    located_in: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""Anatomical location where this entity/process occurs or procedure is performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    laterality: Optional[LateralityEnum] = Field(default=None, description="""Laterality qualifier (left, right, or bilateral)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    spatial_extent: Optional[SpatialExtentEnum] = Field(default=None, description="""The spatial extent or distribution pattern applicable to this descriptor (e.g., focal, diffuse, extensive)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    onset: Optional[OnsetDescriptor] = Field(default=None, description="""Structured age of onset descriptor. Combines an HPO onset category with optional quantitative age data (mean, min, max in years) and free-text notes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor', 'PhenotypeContext']} })
    temporality: Optional[TemporalityEnum] = Field(default=None, description="""Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    clinical_course: Optional[ClinicalCourseEnum] = Field(default=None, description="""Clinical course qualifier for this descriptor (e.g., progressive, stable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    severity: Optional[Union[SeverityQualifierEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SeverityQualifierEnum'}, {'range': 'string'}],
         'domain_of': ['Descriptor', 'PhenotypeContext', 'Phenotype'],
         'examples': [{'value': 'Severe'}]} })
    qualifiers: Optional[list[Qualifier]] = Field(default=None, description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Prefer explicit slots like located_in and laterality instead '
                       'of generic qualifiers',
         'domain_of': ['Descriptor']} })


class ComorbidityAssociation(ConfiguredBaseModel):
    """
    An association between two conditions, including directionality, evidence, and computational characterizations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'creation_date': {'description': 'Timestamp for initial '
                                                         'creation of this comorbidity '
                                                         'entry. Keep this stable '
                                                         'after first set.',
                                          'name': 'creation_date'},
                        'updated_date': {'description': 'Timestamp for the latest '
                                                        'substantive update to this '
                                                        'comorbidity entry. Update '
                                                        'this whenever curated content '
                                                        'changes.',
                                         'name': 'updated_date'}}})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    creation_date: Optional[str] = Field(default=None, description="""Timestamp for initial creation of this comorbidity entry. Keep this stable after first set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'ComorbidityAssociation'], 'recommended': True} })
    updated_date: Optional[str] = Field(default=None, description="""Timestamp for the latest substantive update to this comorbidity entry. Update this whenever curated content changes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'ComorbidityAssociation'], 'recommended': True} })
    disease_a: Optional[ConditionDescriptor] = Field(default=None, description="""First disease in a comorbidity pair""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    disease_b: Optional[ConditionDescriptor] = Field(default=None, description="""Second disease in a comorbidity pair""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    directionality: Optional[ComorbidityDirectionEnum] = Field(default=None, description="""Direction of a comorbidity/trajectory association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation', 'AssociationSignal']} })
    association_signals: Optional[list[AssociationSignal]] = Field(default=None, description="""Association signals from EHR, registry, or computational sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    literature_evidence: Optional[list[EvidenceItem]] = Field(default=None, description="""Literature-based evidence items for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    hypotheses: Optional[list[ComorbidityHypothesis]] = Field(default=None, description="""Mechanistic or causal hypotheses about the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    shared_upstream_hypotheses: Optional[list[UpstreamConditionHypothesis]] = Field(default=None, description="""Suspected upstream conditions that may explain both A and B""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialDiagnosis', 'Disease', 'ComorbidityAssociation']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    curation_status: Optional[CurationStatusEnum] = Field(default=None, description="""Curation workflow status""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation']} })

    @field_validator('creation_date')
    def pattern_creation_date(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid creation_date format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid creation_date format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('updated_date')
    def pattern_updated_date(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid updated_date format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid updated_date format: {v}"
            raise ValueError(err_msg)
        return v


class AssociationSignal(ConfiguredBaseModel):
    """
    An association signal from EHR, registry, or computational sources, optionally stratified by sex, age, or cohort.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'method': {'name': 'method',
                                   'range': 'AssociationSignalMethodEnum'},
                        'source': {'name': 'source',
                                   'range': 'AssociationSignalSourceEnum'}}})

    source: Optional[AssociationSignalSourceEnum] = Field(default=None, description="""Source dataset or provenance label""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalAssertion', 'AssociationSignal']} })
    method: Optional[AssociationSignalMethodEnum] = Field(default=None, description="""Method or pipeline name""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure', 'AssociationSignal', 'GOEnrichment']} })
    signal_disorder_a_id: Optional[str] = Field(default=None, description="""Original identifier for disorder A in this signal (CURIE, e.g., ICD10:E12)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    signal_disorder_b_id: Optional[str] = Field(default=None, description="""Original identifier for disorder B in this signal (CURIE, e.g., ICD10:L28)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    population: Optional[str] = Field(default=None, description="""Population or cohort description (e.g., for prevalence or association signals)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Prevalence', 'AssociationSignal'],
         'examples': [{'value': 'Global'}]} })
    demographics: Optional[Demographics] = Field(default=None, description="""Demographic stratification for an association signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    mapping_notes: Optional[str] = Field(default=None, description="""Notes on code-to-concept mapping decisions for this signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'AssociationSignal']} })
    disorder_a_count: Optional[int] = Field(default=None, description="""Number of records/patients carrying disorder A in the source dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    disorder_b_count: Optional[int] = Field(default=None, description="""Number of records/patients carrying disorder B in the source dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    pair_count: Optional[int] = Field(default=None, description="""Number of records/patients with co-occurrence of disorder A and disorder B in the source dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    limited_precision: Optional[bool] = Field(default=None, description="""Whether the signal has limited statistical precision due to small co-occurrence count""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    precision_count_threshold: Optional[int] = Field(default=None, description="""Co-occurrence count threshold used to flag limited precision""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    directionality: Optional[ComorbidityDirectionEnum] = Field(default=None, description="""Direction of a comorbidity/trajectory association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComorbidityAssociation', 'AssociationSignal']} })
    a_before_b: Optional[float] = Field(default=None, description="""Probability or fraction of A before B in an EHR signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    b_before_a: Optional[float] = Field(default=None, description="""Probability or fraction of B before A in an EHR signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    same_time: Optional[float] = Field(default=None, description="""Probability or fraction of A and B occurring in the same time window""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    metrics: Optional[list[AssociationMetric]] = Field(default=None, description="""Quantitative association metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal', 'AssociationStatistics']} })
    statistics: Optional[AssociationStatistics] = Field(default=None, description="""Statistical summary for an association signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    go_enrichment: Optional[GOEnrichment] = Field(default=None, description="""GO enrichment results associated with a signal""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Demographics(ConfiguredBaseModel):
    """
    Demographic stratification for an association signal
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'sex': {'name': 'sex', 'range': 'SexEnum'}}})

    sex: Optional[SexEnum] = Field(default=None, description="""Sex-specific stratum, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext', 'Demographics']} })
    age_range: Optional[str] = Field(default=None, description="""Age range or stratification, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'SurrogateEndpoint',
                       'ProgressionInfo',
                       'Demographics'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })


class AssociationMetric(ConfiguredBaseModel):
    """
    Quantitative association metric and its uncertainty.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    metric_type: Optional[AssociationMetricTypeEnum] = Field(default=None, description="""Metric type (e.g., OR, RR, HR)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric']} })
    metric_value: Optional[float] = Field(default=None, description="""Metric value""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric']} })
    metric_ci_lower: Optional[float] = Field(default=None, description="""Lower confidence interval bound""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric']} })
    metric_ci_upper: Optional[float] = Field(default=None, description="""Upper confidence interval bound""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric']} })
    p_value: Optional[float] = Field(default=None, description="""P-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    fdr: Optional[float] = Field(default=None, description="""FDR-adjusted p-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class AssociationStatistics(ConfiguredBaseModel):
    """
    Statistical summary with evidence for an association signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    metrics: Optional[list[AssociationMetric]] = Field(default=None, description="""Quantitative association metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationSignal', 'AssociationStatistics']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class GOEnrichment(ConfiguredBaseModel):
    """
    GO enrichment results for an association signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    method: Optional[str] = Field(default=None, description="""Method or pipeline name""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinStructure', 'AssociationSignal', 'GOEnrichment']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    go_terms: Optional[list[GOEnrichmentTerm]] = Field(default=None, description="""GO term enrichment results""", json_schema_extra = { "linkml_meta": {'domain_of': ['GOEnrichment']} })


class GOEnrichmentTerm(ConfiguredBaseModel):
    """
    GO term enrichment result with statistical metrics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'TermMapping',
                       'ConditionDescriptor',
                       'GOEnrichmentTerm'],
         'recommended': True} })
    p_value: Optional[float] = Field(default=None, description="""P-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    fdr: Optional[float] = Field(default=None, description="""FDR-adjusted p-value for an association or enrichment""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociationMetric', 'GOEnrichmentTerm']} })
    overlap: Optional[float] = Field(default=None, description="""Overlap fraction for an enrichment term""", json_schema_extra = { "linkml_meta": {'domain_of': ['GOEnrichmentTerm']} })
    combined_score: Optional[float] = Field(default=None, description="""Combined score used by an enrichment method""", json_schema_extra = { "linkml_meta": {'domain_of': ['GOEnrichmentTerm']} })


class ComorbidityHypothesis(ConfiguredBaseModel):
    """
    Mechanistic hypothesis for a comorbidity association, with rich text and embedded evidence plus atomic pathophysiology elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Stage', 'ComorbidityHypothesis']} })


class UpstreamConditionHypothesis(ConfiguredBaseModel):
    """
    Hypothesized upstream condition that may explain both A and B.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    upstream_disorder: Optional[ConditionDescriptor] = Field(default=None, description="""Upstream disorder referenced in a hypothesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['UpstreamConditionHypothesis']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })


class MechanisticHypothesis(ConfiguredBaseModel):
    """
    Disease-level hypothesis metadata used to organize downstream causal edges into canonical or alternative explanatory models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'hypothesis_group_id': {'name': 'hypothesis_group_id',
                                                'required': True},
                        'status': {'name': 'status',
                                   'range': 'MechanisticHypothesisStatusEnum'}}})

    hypothesis_group_id: str = Field(default=..., description="""Stable identifier for a disease-level mechanistic hypothesis grouping""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanisticHypothesis']} })
    hypothesis_label: Optional[str] = Field(default=None, description="""Human-readable label/title for a mechanistic hypothesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanisticHypothesis']} })
    status: Optional[MechanisticHypothesisStatusEnum] = Field(default=None, description="""Status or state of a clinical trial or other process""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial', 'MechanisticHypothesis', 'Discussion'],
         'examples': [{'value': 'Recruiting'},
                      {'value': 'Completed'},
                      {'value': 'Terminated'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    applies_to_subtypes: Optional[list[str]] = Field(default=None, description="""Disease subtypes for which this hypothesis is intended to apply""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanisticHypothesis']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Discussion(ConfiguredBaseModel):
    """
    A thread-like record of an open question, controversy, curation todo, emerging hypothesis, or interpretation debate attached to a disease entry or sub-object. Discussions capture the *discourse* layer of curation (what is being argued or asked), complementing the structural knowledge-gap layer proposed in monarch-initiative/dismech#2617 (what is missing from the model). External thread links (e.g., Alzforum commentaries, GitHub issues) are not modelled as a separate slot; instead they are cited via the standard `evidence` block using the same EvidenceItem shape as primary literature.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'discussion_id': {'name': 'discussion_id', 'required': True},
                        'kind': {'name': 'kind', 'range': 'DiscussionKindEnum'},
                        'prompt': {'name': 'prompt', 'required': True},
                        'status': {'name': 'status', 'range': 'DiscussionStatusEnum'}}})

    discussion_id: str = Field(default=..., description="""Stable identifier for a Discussion, used as the target of cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    prompt: str = Field(default=..., description="""The unresolved question, controversy, or todo articulated by a Discussion""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    kind: Optional[DiscussionKindEnum] = Field(default=None, description="""Categorical type of a Discussion (narrowed via slot_usage to DiscussionKindEnum)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    status: Optional[DiscussionStatusEnum] = Field(default=None, description="""Status or state of a clinical trial or other process""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial', 'MechanisticHypothesis', 'Discussion'],
         'examples': [{'value': 'Recruiting'},
                      {'value': 'Completed'},
                      {'value': 'Terminated'}]} })
    attaches_to: Optional[list[str]] = Field(default=None, description="""Multivalued list of entity references pointing at the disease nodes, gaps, phenotypes, or other objects this item is about. Uses a hash-anchor grammar consistent with `conforms_to`: `[<file>:]<kind>#<name>`. Examples: `pathophysiology#Amyloid Plaque Formation`, `phenotype#Memory Loss`, `Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation`. Range is `string` for now; a custom EntityRef type with parser support can be introduced later without breaking existing data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    rationale: Optional[str] = Field(default=None, description="""Why this Discussion matters / what hangs on its resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    proposed_experiments: Optional[list[Experiment]] = Field(default=None, description="""Experiments proposed as ways to resolve this Discussion. The Experiment object is intentionally neutral: whether it is proposed, planned, in progress, or reported is determined by its containing context. Here, nesting under a Discussion means the experiment is proposed as a response to an open item or knowledge gap.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpoint',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis',
                       'Discussion'],
         'recommended': True} })
    posed_by: Optional[str] = Field(default=None, description="""Optional attribution for who posed a Discussion. ORCID is preferred when available (e.g., `ORCID:0000-0002-1825-0097`); a github handle or email is acceptable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    posed_date: Optional[datetime ] = Field(default=None, description="""Date the Discussion was first posed (ISO 8601)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    resolved_date: Optional[datetime ] = Field(default=None, description="""Date the Discussion's status moved to RESOLVED (ISO 8601)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    resolution_note: Optional[str] = Field(default=None, description="""Short summary written when a Discussion is marked RESOLVED""", json_schema_extra = { "linkml_meta": {'domain_of': ['Discussion']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class DiseaseCollection(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'tree_root': True})

    diseases: Optional[list[Disease]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseCollection']} })


class FDASurrogateEndpointCollection(SurrogateEndpointCollection):
    """
    FDA surrogate endpoint table import preserving row-level source provenance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'SeverityTier',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
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
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'DietaryModification',
                       'GeneticContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'Subtype',
                       'CausalEdge',
                       'TreatmentMechanismTarget',
                       'ModelMechanismLink',
                       'BiomarkerReadout',
                       'SurrogateEndpointCollection',
                       'ProteinStructure',
                       'ExternalAssertion',
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
                       'UpstreamConditionHypothesis',
                       'MechanisticHypothesis']} })
    source_url: Optional[str] = Field(default=None, description="""URL of the source page for a curated assertion or source collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_url: Optional[str] = Field(default=None, description="""URL of the source workbook or downloadable data file""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_workbook_sha256: Optional[str] = Field(default=None, description="""SHA-256 checksum of the downloaded source workbook used for import""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    source_content_current_as_of: Optional[date] = Field(default=None, description="""Date shown by the source as the content-current-as-of date""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    retrieved_date: Optional[date] = Field(default=None, description="""Date on which the source was retrieved for curation""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpoint', 'SurrogateEndpointCollection']} })
    surrogate_endpoints: list[SurrogateEndpoint] = Field(default=..., description="""Curated surrogate endpoint assertions""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease']} })
    tracked_issues: Optional[list[TrackedIssue]] = Field(default=None, description="""Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SurrogateEndpointCollection', 'Disease', 'TermMapping']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticContext',
                       'OnsetDescriptor',
                       'PhenotypeContext',
                       'Dataset',
                       'ExperimentalModel',
                       'Experiment',
                       'ExperimentalPerturbation',
                       'ExperimentalReadout',
                       'ExperimentalControl',
                       'ClinicalTrial',
                       'ComputationalModel',
                       'ModelVariable',
                       'DifferentialDiagnosis',
                       'SurrogateEndpoint',
                       'SurrogateEndpointCollection',
                       'ExternalAssertion',
                       'TrackedIssue',
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
                       'AssociationStatistics',
                       'MechanisticHypothesis',
                       'Discussion'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CurationEvent.model_rebuild()
Term.model_rebuild()
Descriptor.model_rebuild()
Qualifier.model_rebuild()
DietaryModification.model_rebuild()
CellTypeDescriptor.model_rebuild()
BiologicalProcessDescriptor.model_rebuild()
MolecularFunctionDescriptor.model_rebuild()
AnatomicalEntityDescriptor.model_rebuild()
ChemicalEntityDescriptor.model_rebuild()
GeneDescriptor.model_rebuild()
CellularComponentDescriptor.model_rebuild()
ProteinComplexDescriptor.model_rebuild()
AssayDescriptor.model_rebuild()
TriggerDescriptor.model_rebuild()
DiseaseDescriptor.model_rebuild()
SubtypeDescriptor.model_rebuild()
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
FoodDescriptor.model_rebuild()
OrganismDescriptor.model_rebuild()
HostDescriptor.model_rebuild()
SampleTypeDescriptor.model_rebuild()
GeneticContext.model_rebuild()
OnsetDescriptor.model_rebuild()
PhenotypeContext.model_rebuild()
Dataset.model_rebuild()
ExperimentalModel.model_rebuild()
Experiment.model_rebuild()
ExperimentalPerturbation.model_rebuild()
ExperimentalReadout.model_rebuild()
ExperimentalControl.model_rebuild()
ClinicalTrial.model_rebuild()
ComputationalModel.model_rebuild()
ModelVariable.model_rebuild()
SeverityTier.model_rebuild()
ModelVariableDescriptor.model_rebuild()
DifferentialDiagnosis.model_rebuild()
Subtype.model_rebuild()
EvidenceItem.model_rebuild()
CausalEdge.model_rebuild()
TreatmentMechanismTarget.model_rebuild()
ModelMechanismLink.model_rebuild()
BiomarkerReadout.model_rebuild()
SurrogateEndpoint.model_rebuild()
SurrogateEndpointCollection.model_rebuild()
ProteinStructure.model_rebuild()
PublicationReference.model_rebuild()
ExternalAssertion.model_rebuild()
TrackedIssue.model_rebuild()
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
NCITMapping.model_rebuild()
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
MechanisticHypothesis.model_rebuild()
Discussion.model_rebuild()
DiseaseCollection.model_rebuild()
FDASurrogateEndpointCollection.model_rebuild()
