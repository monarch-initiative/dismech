---
reference_id: "HDRUK:PH236"
title: "Peripheral arterial disease"
database: "HDR UK Phenotype Library"
source_snapshot: "PH236 version 472"
content_type: "structured_record"
---

# HDRUK:PH236  Peripheral arterial disease

**PH236** version 472 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH236 |
| Version | 472 |
| Name | Peripheral arterial disease |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; OPCS4 codes; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/f06h-0c50 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Peripheral-arterial-disease---fe2fc8e0-17a2-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Peripheral-arterial-disease.cwl |
| Ontology | MONDO:0005386 peripheral arterial disease |

## Definition

Use MODIFIED CALIBER 'Peripheral arterial disease' (PAD) phenotyping algorithm:

At the specified date, a patient is considered to have 'Peripheral arterial disease' IF they meet any of the criteria below on or before the specified date.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

1. Primary care

1. Peripheral vascular disease diagnosis during a consultation. arterial_gprd: category 7

2. Record of history of PVD during a consultation. The following Read codes from CPRD:

1. Read:14F7.00 Medcode: 106762 Descr:H/O: arterial lower limb ulcer

2. Read:14NB.00 Medcode: 59534 Descr: H/O: Peripheral vascular disease procedure

3. Leg or aortic embolism or thrombosis diagnosis during a consultation. arterial_gprd: category 8

4. 'Peripheral arterial disease' procedures, excluding repair of AAA recording during a consultation. pad_opcs_gprd: category 3

5. Abnormal 'Peripheral arterial disease' (PAD) ultrasound or Doppler study results recorded during a consultation. As per implementation of pad_ud_gprd in CALIBER

6. Abnormal 'Peripheral arterial disease' angiography results recorded during a consultation. As per implementation of pad_angio_gprd in CALIBER

2. Secondary care

1. Primary or secondary diagnosis of Peripheral vascular disease during a hospitalization. arterial_hes: category 7

2. Primary or secondary diagnosis of leg or aortic embolism or thrombosis during a hospitalization. arterial_hes: category 8

3. Recording of 'Peripheral arterial disease' procedures, excluding repair of AAA. pad_procs_opcs: category 3

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:14F7.00 | H/O: arterial lower limb ulcer | Peripheral arterial disease - Primary care |
| READ2:14NB.00 | H/O: Peripheral vascular disease procedure | Peripheral arterial disease - Primary care |
| READ2:2G63.00 | Ischaemic toe | Peripheral arterial disease - Primary care |
| READ2:7A10000 | Emerg aortic bypass by anastomosis axillary to femoral art | Peripheral arterial disease - Primary care |
| READ2:7A10100 | Bypass aorta by anastomosis axillary to femoral artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A10200 | Axillo-bifemoral bypass graft | Peripheral arterial disease - Primary care |
| READ2:7A10300 | Axillo-unifemoral PTFE bypass graft | Peripheral arterial disease - Primary care |
| READ2:7A12.00 | Other bypass of bifurcation of aorta | Peripheral arterial disease - Primary care |
| READ2:7A12000 | Emerg bypass bifurc aorta by anast aorta to femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A12100 | Bypass bifurc aorta by anastom aorta to femoral artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A12111 | Aorto bifemoral graft | Peripheral arterial disease - Primary care |
| READ2:7A12112 | Dacron aortofemoral Y graft | Peripheral arterial disease - Primary care |
| READ2:7A12300 | Bypass bifurcation aorta by anastom aorta to iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A12311 | Aorto biiliac graft | Peripheral arterial disease - Primary care |
| READ2:7A12312 | Dacron aortoiliac Y graft | Peripheral arterial disease - Primary care |
| READ2:7A12y00 | Other specified other bypass of bifurcation of aorta | Peripheral arterial disease - Primary care |
| READ2:7A12z00 | Other bypass of bifurcation of aorta NOS | Peripheral arterial disease - Primary care |
| READ2:7A19200 | Open embolectomy of bifurcation of aorta | Peripheral arterial disease - Primary care |
| READ2:7A41.00 | Other bypass of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A41000 | Emerg bypass iliac art by iliac/femoral art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41100 | Bypass iliac artery by iliac/femoral artery anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41200 | Emerg bypass iliac artery by femoral/femoral art anast NEC | Peripheral arterial disease - Primary care |
| READ2:7A41211 | Emergency femoro-femoral prosthetic cross over graft | Peripheral arterial disease - Primary care |
| READ2:7A41300 | Bypass iliac artery by femoral/femoral art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41311 | Femoro-femoral prosthetic cross over graft | Peripheral arterial disease - Primary care |
| READ2:7A41400 | Emerg bypass comm iliac art by aorta/com iliac art anast NEC | Peripheral arterial disease - Primary care |
| READ2:7A41600 | Emerg bypass leg artery by aorta/com fem art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41900 | Bypass common iliac artery by aorta/com iliac art anast NEC | Peripheral arterial disease - Primary care |
| READ2:7A41B00 | Bypass leg artery by aorta/com femoral art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41C00 | Bypass leg artery by aorta/deep femoral art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A41F00 | Ilio-femoral prosthetic cross over graft | Peripheral arterial disease - Primary care |
| READ2:7A41y00 | Other specified other bypass of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A41z00 | Other bypass of iliac artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A42.00 | Reconstruction of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A42.11 | Reconstruction of common iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A42000 | Endarterectomy and patch repair of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A42011 | Endarterectomy and patch repair of common iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A42012 | Iliac endarterectomy and patch | Peripheral arterial disease - Primary care |
| READ2:7A42100 | Endarterectomy of iliac artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A42111 | Endarterectomy of common iliac artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A42y00 | Other specified reconstruction of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A42z00 | Reconstruction of iliac artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A43.00 | Other open operations on iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A43.11 | Other open operations on common iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A43000 | Repair of iliac artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A43011 | Repair of common iliac artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A43100 | Open embolectomy of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A43111 | Open embolectomy of common iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A43300 | Open insertion of iliac artery stent | Peripheral arterial disease - Primary care |
| READ2:7A44000 | Percutaneous transluminal angioplasty of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A44100 | Percutaneous transluminal embolectomy of iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A44300 | Insertion of iliac artery stent | Peripheral arterial disease - Primary care |
| READ2:7A44400 | Percutaneous transluminal insertion of iliac artery stent | Peripheral arterial disease - Primary care |
| READ2:7A44y00 | Other specified transluminal operation on iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A44z00 | Transluminal operation on iliac artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A47.00 | Other emergency bypass of femoral artery or popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A47.11 | Other emerg bypass femoral or popliteal art by anastomosis | Peripheral arterial disease - Primary care |
| READ2:7A47.13 | Other emergency bypass of deep femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A47.14 | Other emergency bypass of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A47.15 | Other emergency bypass of superficial femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A47.16 | Other emergency bypass of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A47000 | Emerg bypass femoral art by fem/pop art anast c prosth NEC | Peripheral arterial disease - Primary care |
| READ2:7A47100 | Emerg bypass popliteal art by pop/pop art anast c prosth NEC | Peripheral arterial disease - Primary care |
| READ2:7A47200 | Emerg bypass femoral art by fem/pop a anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A47300 | Emerg bypass pop art by pop/pop art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A47400 | Emerg bypass femoral art by fem/tib art anast c prosth NEC | Peripheral arterial disease - Primary care |
| READ2:7A47600 | Emerg bypass femoral art by fem/tib a anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A47700 | Emerg bypass pop art by pop/tib art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A47B00 | Emerg bypass pop art by pop/peron art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A47C00 | Emerg bypass femoral artery by fem/fem art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A47D00 | Emerg bypass popliteal artery by pop/fem art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A47y00 | Other emergency bypass of femoral or popliteal artery OS | Peripheral arterial disease - Primary care |
| READ2:7A47z00 | Other emergency bypass of femoral or popliteal artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A48.00 | Other bypass of femoral artery or popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A48.11 | Other bypass of femoral or popliteal artery by anastomosis | Peripheral arterial disease - Primary care |
| READ2:7A48.12 | Other bypass of common femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A48.14 | Other bypass of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A48.15 | Other bypass of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A48.16 | Other bypass of superficial femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A48000 | Bypass femoral artery by fem/pop art anast c prosthesis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48100 | Bypass popliteal artery by pop/pop a anast c prosthesis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48200 | Bypass femoral artery by fem/pop art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48300 | Bypass popliteal artery by pop/pop a anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48400 | Bypass femoral artery by fem/tib art anast c prosthesis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48500 | Bypass popliteal artery by pop/tib a anast c prosthesis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48600 | Bypass femoral artery by fem/tib art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48700 | Bypass popliteal artery by pop/tib a anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48800 | Bypass femoral artery by fem/peron a anast c prosthesis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48A00 | Bypass femoral artery by fem/peron a anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48B00 | Bypass popliteal art by pop/peron art anast c vein graft NEC | Peripheral arterial disease - Primary care |
| READ2:7A48C00 | Bypass femoral artery by femoral/femoral art anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48D00 | Bypass popliteal artery by pop/fem artery anastomosis NEC | Peripheral arterial disease - Primary care |
| READ2:7A48E00 | Femoro-femoral prosthetic cross over graft | Peripheral arterial disease - Primary care |
| READ2:7A48y00 | Other bypass of femoral artery or popliteal artery OS | Peripheral arterial disease - Primary care |
| READ2:7A48z00 | Other bypass of femoral artery or popliteal artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A49.00 | Reconstruction of femoral artery or popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A49.11 | Reconstruction of common femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A49.13 | Reconstruction of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A49.14 | Reconstruction of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A49.15 | Reconstruction of superficial femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A49000 | Endarterectomy and patch repair of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A49100 | Endarterectomy and patch repair of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A49200 | Endarterectomy of femoral artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A49300 | Endarterectomy of popliteal artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A49400 | Profundoplasty femoral artery & patch repair deep fem artery | Peripheral arterial disease - Primary care |
| READ2:7A49500 | Profundoplasty and patch repair of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A49600 | Profundoplasty of femoral artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A49700 | Profundoplasty of popliteal artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A49800 | Reconstruction of femoral artery with vein graft | Peripheral arterial disease - Primary care |
| READ2:7A49900 | Reconstruction of popliteal artery with vein graft | Peripheral arterial disease - Primary care |
| READ2:7A49y00 | Reconstruction of femoral or popliteal artery OS | Peripheral arterial disease - Primary care |
| READ2:7A49z00 | Reconstruction of femoral or popliteal artery NOS | Peripheral arterial disease - Primary care |
| READ2:7A4A.00 | Other open operations on femoral artery or popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4A.11 | Other open operations on common femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4A.13 | Other open operations on popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4A.14 | Other open operations on superficial femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4A000 | Repair of femoral artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A4A100 | Repair of popliteal artery NEC | Peripheral arterial disease - Primary care |
| READ2:7A4A200 | Open embolectomy of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4A211 | Open thrombectomy of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4A212 | Open femoral embolectomy | Peripheral arterial disease - Primary care |
| READ2:7A4A300 | Open embolectomy popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4A311 | Open thrombectomy of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4A700 | Repair of femoral artery with temporary silastic shunt | Peripheral arterial disease - Primary care |
| READ2:7A4A800 | Repair of popliteal artery with temporary silastic shunt | Peripheral arterial disease - Primary care |
| READ2:7A4Ay00 | Other open operation on femoral or popliteal artery OS | Peripheral arterial disease - Primary care |
| READ2:7A4B000 | Percutaneous transluminal angioplasty of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4B100 | Percutaneous transluminal angioplasty of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4B200 | Percutaneous transluminal embolectomy of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4B300 | Percutaneous transluminal embolectomy of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4B400 | Percutaneous transluminal embolisation of femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A4B500 | Percutaneous transluminal embolisation of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:7A4B800 | Percut translum thrombolysis femoral graft streptokinase | Peripheral arterial disease - Primary care |
| READ2:7A4B900 | Percutaneous transluminal insertion of stent femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A50.00 | Revision of reconstruction of artery | Peripheral arterial disease - Primary care |
| READ2:7A50000 | Revision of reconstruction involving aorta | Peripheral arterial disease - Primary care |
| READ2:7A50100 | Revision of reconstruction involving iliac artery | Peripheral arterial disease - Primary care |
| READ2:7A50200 | Revision of reconstruction involving femoral artery | Peripheral arterial disease - Primary care |
| READ2:7A50300 | Revision of reconstruction of popliteal artery | Peripheral arterial disease - Primary care |
| READ2:A3A0F00 | Gas gangrene-foot | Peripheral arterial disease - Primary care |
| READ2:C107.00 | Diabetes mellitus with peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C107000 | Diabetes mellitus, juvenile +peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C107100 | Diabetes mellitus, adult, + peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C107300 | IDDM with peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C107400 | NIDDM with peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C107z00 | Diabetes mellitus NOS with peripheral circulatory disorder | Peripheral arterial disease - Primary care |
| READ2:C108G00 | Insulin dependent diab mell with peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:C109F00 | Non-insulin-dependent d m with peripheral angiopath | Peripheral arterial disease - Primary care |
| READ2:C109F11 | Type II diabetes mellitus with peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:C109F12 | Type 2 diabetes mellitus with peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:C10EG00 | Type 1 diabetes mellitus with peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:C10FF00 | Type 2 diabetes mellitus with peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:G700.11 | Aorto-iliac disease | Peripheral arterial disease - Primary care |
| READ2:G702.00 | Extremity artery atheroma | Peripheral arterial disease - Primary care |
| READ2:G702z00 | Extremity artery atheroma NOS | Peripheral arterial disease - Primary care |
| READ2:G73..00 | Other peripheral vascular disease | Peripheral arterial disease - Primary care |
| READ2:G73..11 | Peripheral ischaemic vascular disease | Peripheral arterial disease - Primary care |
| READ2:G73..12 | Ischaemia of legs | Peripheral arterial disease - Primary care |
| READ2:G73..13 | Peripheral ischaemia | Peripheral arterial disease - Primary care |
| READ2:G731.00 | Thromboangiitis obliterans | Peripheral arterial disease - Primary care |
| READ2:G731000 | Buerger's disease | Peripheral arterial disease - Primary care |
| READ2:G731z00 | Thromboangiitis obliterans NOS | Peripheral arterial disease - Primary care |
| READ2:G732.00 | Peripheral gangrene | Peripheral arterial disease - Primary care |
| READ2:G732000 | Gangrene of toe | Peripheral arterial disease - Primary care |
| READ2:G732100 | Gangrene of foot | Peripheral arterial disease - Primary care |
| READ2:G733.00 | Ischaemic foot | Peripheral arterial disease - Primary care |
| READ2:G73y.00 | Other specified peripheral vascular disease | Peripheral arterial disease - Primary care |
| READ2:G73y000 | Diabetic peripheral angiopathy | Peripheral arterial disease - Primary care |
| READ2:G73y100 | Peripheral angiopathic disease EC NOS | Peripheral arterial disease - Primary care |
| READ2:G73y200 | Acrocyanosis | Peripheral arterial disease - Primary care |
| READ2:G73y400 | Acroparaesthesia - Schultze's type | Peripheral arterial disease - Primary care |
| READ2:G73y500 | Acroparaesthesia - Nothnagel's type | Peripheral arterial disease - Primary care |
| READ2:G73y511 | Nothnagel's vasomotor acroparaesthesia | Peripheral arterial disease - Primary care |
| READ2:G73y600 | Acroparaesthesia - unspecified | Peripheral arterial disease - Primary care |
| READ2:G73y700 | Erythrocyanosis | Peripheral arterial disease - Primary care |
| READ2:G73y800 | Erythromelalgia | Peripheral arterial disease - Primary care |
| READ2:G73yz00 | Other specified peripheral vascular disease NOS | Peripheral arterial disease - Primary care |
| READ2:G73z.00 | Peripheral vascular disease NOS | Peripheral arterial disease - Primary care |
| READ2:G73z000 | Intermittent claudication | Peripheral arterial disease - Primary care |
| READ2:G73z011 | Claudication | Peripheral arterial disease - Primary care |
| READ2:G73zz00 | Peripheral vascular disease NOS | Peripheral arterial disease - Primary care |
| READ2:G740.12 | Aortoiliac obstruction | Peripheral arterial disease - Primary care |
| READ2:G742400 | Embolism and thrombosis of the femoral artery | Peripheral arterial disease - Primary care |
| READ2:G742500 | Embolism and thrombosis of the popliteal artery | Peripheral arterial disease - Primary care |
| READ2:G742600 | Embolism and thrombosis of the anterior tibial artery | Peripheral arterial disease - Primary care |
| READ2:G742700 | Embolism and thrombosis of the dorsalis pedis artery | Peripheral arterial disease - Primary care |
| READ2:G742900 | Embolism and thrombosis of a leg artery NOS | Peripheral arterial disease - Primary care |
| READ2:G742z00 | Peripheral arterial embolism and thrombosis NOS | Peripheral arterial disease - Primary care |
| READ2:G74y000 | Embolism and/or thrombosis of the common iliac artery | Peripheral arterial disease - Primary care |
| READ2:G74y100 | Embolism and/or thrombosis of the internal iliac artery | Peripheral arterial disease - Primary care |
| READ2:G74y200 | Embolism and/or thrombosis of the external iliac artery | Peripheral arterial disease - Primary care |
| READ2:G74y300 | Embolism and thrombosis of the iliac artery unspecified | Peripheral arterial disease - Primary care |
| READ2:Gyu7400 | [X]Other specified peripheral vascular diseases | Peripheral arterial disease - Primary care |
| READ2:M271.12 | Ischaemic leg ulcer | Peripheral arterial disease - Primary care |
| READ2:M271000 | Ischaemic ulcer diabetic foot | Peripheral arterial disease - Primary care |
| READ2:M271300 | Arterial leg ulcer | Peripheral arterial disease - Primary care |
| READ2:M271400 | Mixed venous and arterial leg ulcer | Peripheral arterial disease - Primary care |
| READ2:R054200 | [D]Gangrene of toe in diabetic | Peripheral arterial disease - Primary care |
| READ2:R054300 | [D]Widespread diabetic foot gangrene | Peripheral arterial disease - Primary care |
| READ2:R055000 | [D]Failure of peripheral circulation | Peripheral arterial disease - Primary care |
| READ2:R055011 | [D]Peripheral circulatory failure | Peripheral arterial disease - Primary care |
| 10500 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 106762 (Med codes) | history of PVD during a consultation | Peripheral arterial disease - Primary care |
| 10827 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 11624 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 11766 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 12331 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 12735 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 14796 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 14797 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 14895 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 1517 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 15272 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 15302 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 15532 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 16260 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 16363 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 17336 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 18030 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 18038 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 18060 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 1826 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 18816 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 19155 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 2065 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 20657 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 2066 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 20892 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 21927 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 22016 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 22834 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 23352 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 23497 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 23871 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 24097 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 24229 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 24327 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 24677 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 24692 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 25954 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 27494 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 27580 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 2760 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 2761 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28030 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28119 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28125 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28166 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28616 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28777 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 28894 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 29112 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 30484 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 30989 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 31053 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 31338 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 32492 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 32634 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 33555 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 34037 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 34152 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 34153 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 34638 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 3530 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 35399 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 36065 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 36136 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 36443 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 36952 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 3715 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 3778 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 37787 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 37806 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 38907 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 38921 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 39039 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 39437 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 39776 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 39877 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 40302 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 40397 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 40619 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 40732 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 41768 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 41823 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 42115 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 42465 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 42640 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 42645 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 4317 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 4325 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 43648 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 43651 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 44250 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 44430 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 44835 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 4539 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 45428 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 47562 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 47835 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 48700 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 48755 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 48939 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 49273 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 49319 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 50894 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 51211 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 51331 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 52289 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 52342 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 52357 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 52695 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 52869 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 53580 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 53634 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 53675 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 54071 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 5414 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 54212 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 54865 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 54899 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 55402 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 55554 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 55825 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 55877 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 5650 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 56803 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 56919 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 5702 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 57793 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 5943 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 59534 (Med codes) | history of PVD during a consultation | Peripheral arterial disease - Primary care |
| 59602 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 60212 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 60465 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 60693 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 60699 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 61255 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 61256 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 61974 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6256 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 62775 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 62818 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 62866 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6308 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 63238 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 63280 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 63357 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 63368 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 63396 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6356 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 63605 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 64446 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 64555 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 64798 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 65025 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 65286 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 65669 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 65692 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6617 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66437 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66804 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66820 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66869 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66879 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66917 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 66930 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 67083 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 67401 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 67818 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 67982 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 68141 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6827 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 68320 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 68412 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 6853 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 68698 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 69124 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 69232 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 69519 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 70448 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 70922 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 71041 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 7111 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 71860 (Med codes) | Leg or aortic embolism or thrombosis (8) | Peripheral arterial disease - Primary care |
| 72448 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 72491 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 72632 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 73822 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 73961 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 81445 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 8801 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 9099 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 9119 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 9204 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 93468 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 95573 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 9561 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| 96255 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 96809 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 97606 (Med codes) | Other PAD procedures (3) | Peripheral arterial disease - Primary care |
| 98174 (Med codes) | Peripheral vascular disease (7) | Peripheral arterial disease - Primary care |
| ICD10:I731 | Thromboangiitis obliterans [Buerger] | Peripheral arterial disease - Secondary care - Diagnoses |
| ICD10:I738 | Other specified peripheral vascular diseases | Peripheral arterial disease - Secondary care - Diagnoses |
| ICD10:I739 | Peripheral vascular disease, unspecified | Peripheral arterial disease - Secondary care - Diagnoses |
| ICD10:I743 | Embolism and thrombosis of arteries of lower extremities | Peripheral arterial disease - Secondary care - Diagnoses |
| ICD10:I744 | Embolism and thrombosis of arteries of extremities, unspecified | Peripheral arterial disease - Secondary care - Diagnoses |
| ICD10:I745 | Embolism and thrombosis of iliac artery | Peripheral arterial disease - Secondary care - Diagnoses |
| OPCS4:L50 | Other emergency bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.1 | Emergency bypass of common iliac artery by anastomosis of aorta to common iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.2 | Emergency bypass of iliac artery by anastomosis of aorta to external iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.3 | Emergency bypass of artery of leg by anastomosis of aorta to common femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.4 | Emergency bypass of artery of leg by anastomosis of aorta to deep femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.5 | Emergency bypass of iliac artery by anastomosis of iliac artery to iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.6 | Emergency bypass of artery of leg by anastomosis of iliac artery to femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.8 | Other specified other emergency bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L50.9 | Unspecified other emergency bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51 | Other bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.1 | Bypass of common iliac artery by anastomosis of aorta to common iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.2 | Bypass of iliac artery by anastomosis of aorta to external iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.3 | Bypass of artery of leg by anastomosis of aorta to common femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.4 | Bypass of artery of leg by anastomosis of aorta to deep femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.5 | Bypass of iliac artery by anastomosis of iliac artery to iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.6 | Bypass of artery of leg by anastomosis of iliac artery to femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.8 | Other specified other bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L51.9 | Unspecified other bypass of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L52 | Reconstruction of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L52.1 | Endarterectomy of iliac artery and patch repair of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L52.2 | Endarterectomy of iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L52.8 | Other specified reconstruction of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L52.9 | Unspecified reconstruction of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L53 | Other open operations on iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L53.1 | Repair of iliac artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L53.2 | Open embolectomy of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L54.1 | Percutaneous transluminal angioplasty of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L54.2 | Percutaneous transluminal embolectomy of iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L54.4 | Percutaneous transluminal insertion of stent into iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L54.8 | Other specified transluminal operations on iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L54.9 | Unspecified transluminal operations on iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58 | Other emergency bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.1 | Emergency bypass of femoral artery by anastomosis of femoral artery to femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.2 | Emergency bypass of femoral artery by anastomosis of femoral artery to popliteal artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.3 | Emergency bypass of femoral artery by anastomosis of femoral artery to popliteal artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.4 | Emergency bypass of femoral artery by anastomosis of femoral artery to tibial artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.5 | Emergency bypass of femoral artery by anastomosis of femoral artery to tibial artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.6 | Emergency bypass of femoral artery by anastomosis of femoral artery to peroneal artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.7 | Emergency bypass of femoral artery by anastomosis of femoral artery to peroneal artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.8 | Other specified other emergency bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L58.9 | Unspecified other emergency bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59 | Other bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.1 | Bypass of femoral artery by anastomosis of femoral artery to femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.2 | Bypass of femoral artery by anastomosis of femoral artery to popliteal artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.3 | Bypass of femoral artery by anastomosis of femoral artery to popliteal artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.4 | Bypass of femoral artery by anastomosis of femoral artery to tibial artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.5 | Bypass of femoral artery by anastomosis of femoral artery to tibial artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.6 | Bypass of femoral artery by anastomosis of femoral artery to peroneal artery using prosthesis NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.7 | Bypass of femoral artery by anastomosis of femoral artery to peroneal artery using vein graft NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.8 | Other specified other bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L59.9 | Unspecified other bypass of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60 | Reconstruction of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.1 | Endarterectomy of femoral artery and patch repair of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.2 | Endarterectomy of femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.3 | Profundoplasty of femoral artery and patch repair of deep femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.4 | Profundoplasty of femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.8 | Other specified reconstruction of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L60.9 | Unspecified reconstruction of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L62 | Other open operations on femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L62.1 | Repair of femoral artery NEC | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L62.2 | Open embolectomy of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L62.8 | Other specified other open operations on femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L62.9 | Unspecified other open operations on femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L63.1 | Percutaneous transluminal angioplasty of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L63.2 | Percutaneous transluminal embolectomy of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L63.3 | Percutaneous transluminal embolisation of femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L63.5 | Percutaneous transluminal insertion of stent into femoral artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L65 | Revision of reconstruction of artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L65.1 | Revision of reconstruction involving aorta | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L65.2 | Revision of reconstruction involving iliac artery | Peripheral arterial disease - Secondary care - Procedures |
| OPCS4:L65.3 | Revision of reconstruction involving femoral artery | Peripheral arterial disease - Secondary care - Procedures |

## Source

HDR UK Phenotype Library record PH236 version 472, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH236/version/472/detail/)
