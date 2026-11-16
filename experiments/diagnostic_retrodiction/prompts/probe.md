<!-- Knowledge probe (DRAFT). Not an arm and not scored for any endpoint. It measures what the
     model knows today about the disease's diagnosis, with no cutoff and no material, so that a
     T4 hit or a leakage alarm in an arm can be read against it. Same schema as the arms.
     Run once per unique arm_display_name. Placeholders: {DISPLAY_NAME}. -->
The disease is: {DISPLAY_NAME}.

List the accessible-specimen diagnostic tests (blood, serum, plasma, dried blood spot, urine or
cerebrospinal fluid; not germline sequencing) in current clinical use for this disease, most
established first, in the same format. Confidence is how established the test is.
