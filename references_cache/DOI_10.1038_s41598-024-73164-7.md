---
reference_id: DOI:10.1038/s41598-024-73164-7
title: Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy against Trichuris trichiura
authors:
- Carla M. Grolimund
- Jürg Utzinger
- Jean T. Coulibaly
- Somphou Sayasone
- Said M. Ali
- Jennifer Keiser
- Penelope Vounatsou
journal: Scientific Reports
year: '2024'
doi: 10.1038/s41598-024-73164-7
content_type: full_text_html
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://doi.org/10.1038/s41598-024-73164-7"
oa_status: gold
license: cc-by-nc-nd
---

# Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy against Trichuris trichiura
**Authors:** Carla M. Grolimund, Jürg Utzinger, Jean T. Coulibaly, Somphou Sayasone, Said M. Ali, Jennifer Keiser, Penelope Vounatsou
**Journal:** Scientific Reports (2024)
**DOI:** [10.1038/s41598-024-73164-7](https://doi.org/10.1038/s41598-024-73164-7)

## Content

Scientific Reportsvolume14,  Article number:23543(2024)Cite this article

2958Accesses

1Citations

Metricsdetails

Trichuris trichiurais one of four soil-transmitted helminth species that, collectively, are responsible for a considerable public health burden. The World Health Organization recommends preventive chemotherapy as the main intervention to eliminate soil-transmitted helminthiasis as a public health problem. Clinical trials estimated the efficacy of different drugs and treatment regimen againstT. trichiuraand other soil-transmitted helminth species, whilst meta-analyses and modeling efforts were conducted to determine the most efficacious drugs and drug combinations. Of note, the diagnostic error was often neglected, and hence, cure rates (CRs) might be overestimated. We developed a Bayesian model, which estimates drug efficacy againstT. trichiura, taking into account the transmission mechanism and the diagnostic error. The model was fitted to individual-level egg count data from an ensemble of seven trials with 29 treatments. We estimated the ‘true’ CRs, which were consistently lower than those reported in the literature. In our analysis, the treatment with the highest CR was combination therapy of albendazole plus pyrantel pamoate plus oxantel pamoate with a CR of 79% and an egg reduction rate (ERR) of 91%. Albendazole plus oxantel pamoate showed the highest ERR of 97% and a CR of 69%. Additionally, we estimated the intensity-dependent sensitivity of the Kato-Katz technique. For 24 eggs per gram of stool, the sensitivity was around 50% for a single Kato-Katz thick smear and increased to almost 70% for duplicate Kato-Katz thick smears. Combination therapies against soil-transmitted helminthiasis should be considered and the evaluation of infection intensity in low transmission settings via multiple Kato-Katz thick smears is recommended.

Trichuris trichiura—also known as whipworm—is an intestinal nematode and one of four soil-transmitted helminth species infecting humans1,2.T. trichiurais responsible for a considerable public health burden, particularly in children in low- and middle-income countries (LMICs). For instance, severe anemia and inflammation of the colon are distinct consequences of aT. trichiurainfection3. An estimated 450 million people are infected withT. trichiura, leading to 337,000 years lost due to disability4. The World Health Organization (WHO) set the target to eliminate morbidity due to soil-transmitted helminthiasis in pre-school-age children and school-age children by 20305. To achieve this goal, WHO emphasizes preventive chemotherapy as the main intervention6. It recommends the use of albendazole (400 mg) and mebendazole (500 mg) in preventive chemotherapy programs because of simple administration, low cost, and community effectiveness. However, it is acknowledged that the efficacy of either treatment againstT. trichiurais low7,8,9,10. Hence, it is important to investigate treatment efficacy of alternative drugs and combination therapies11. Of note, Speich et al. found that combination therapy of oxantel pamoate (20 mg/kg) plus albendazole (400 mg) is more efficacious (higher cure rate (CR) and egg reduction rate (ERR)) againstT. trichiurathan single-dose albendazole (400 mg) or mebendazole (500 mg)12. Clarke et al. compared the efficacy of 21 treatment regimens againstT. trichiuraand showed that the combination therapy of albendazole plus ivermectin, albendazole plus oxantel pamoate, and multiple-dose mebendazole are more efficacious (regarding relative risk of CR and difference in ERR) than albendazole alone9. The sensitivity of diagnostics is an important and often discussed topic because of its implications on observed prevalence13. For instance, WHO highlights the need for more sensitive diagnostic tools for mapping and surveillance14. Knopp et al. showed that multiple Kato-Katz thick smears are required to accurately assess prevalences, particularly in low-infection settings15.

Meta-analyses and systematic reviews as well as analyses with latent class models have been done9,16,17. However, only the infection status of individuals was included in these analyses. Moreover, the diagnostic error of the Kato-Katz thick smear is not taken into account leading to overestimation of CRs. Bärenbold et al. and Moser et al. developed a model, which analyzed individual-level egg count data, taking into account the diagnostic error18,19. Grolimund et al. further developed the model to study efficacy of various drugs against hookworm, including the transmission mechanism of the infection20.

In this study, we further adapted the aforementioned model by Grolimund et al. toT. trichiuraand extended it to include the density-dependent fecundity of worms. Our aim was to estimate the CRs and ERRs of different treatment regimens againstT. trichiuraand to assess the sensitivity of the Kato-Katz technique.

The data used in this analysis have been published elsewhere10,12,21,22,23,24,25. Details on ethical approvals, trial registration, study design, informed consent procedures, drugs and regimens employed, diagnostic approach, potential risks and benefits are provided in the aforementioned studies.

The data used in this analysis consist of seven randomized trials carried out in Côte d’Ivoire, Lao People’s Democratic Republic, and Tanzania, which assessed the efficacy of different drugs and combination therapies against soil-transmitted helminth infection using the Kato-Katz thick smear technique as diagnostic assay10,12,21,22,23,24,25. All trials applied the same diagnostic approach, i.e., two stool specimens were collected from each individual on two consecutive days before and approximately 3 weeks after treatment, with duplicate Kato-Katz thick smears prepared per specimen, analyzed under a microscope by experienced laboratory technicians. Helminth eggs were counted and recorded per species. For the few trials which focused on hookworm, we only includedT. trichiura-positive individuals at baseline. An overview of the data, including treatment regimen, number of participants and mean infection intensities at baseline and treatment follow-up, is summarized in Table1.

At baseline, the data consist of egg counts (eggs per Kato-Katz slide)\(Y^{(0)}_{i_{jg}ds}\)for individuali, studyj, treatmentg, testing dayd, and samples. They are assumed to follow a negative binomial distribution with a daily individual mean\(\mu ^{(0)}_{i_{jg}d}\)for each treatment and study and an aggregation parameter\(k^{(0)}\):

The day-to-day variation\(\sigma _d^2\)in the excreted eggs was taken into account by random effects for each day and individuali, as follows:\(log\Big (\mu ^{(0)}_{i_{jg}d}\Big ) = log\Big (\mu ^{(0)}_{i_{jg}}\Big )+\epsilon ^{(0)}_{id}\), where\(\epsilon ^{(0)}_{id} \sim \mathcal {N}\Big (\frac{-\sigma _d^2}{2},\sigma _d^2\Big ).\)For the individual mean\(\mu ^{(0)}_{i_{jg}}\)we assumed a gamma distribution, that is\(\mu ^{(0)}_{i_{jg}}\sim \text {Gamma} \Big (\mu ^{(0)}_{jg}\cdot \sigma ^{(0)}_{jg}, \sigma ^{(0)}_{jg}\Big )\), where\(\mu ^{(0)}_{{jg}}\)and\(\sigma ^{(0)}_{jg}\)are hyperparameters.

At follow-up we have egg counts\(Y^{(1)}_{i_{jg}ds}\)which are fitted to a mixture distribution which separates the infected and non-infected individuals, that is

where\(\mu ^{(1)}_{i_{jg}d}\)is the daily individual mean and\(k^{(1)}\)is the variation from slide to slide of infected individuals, whilevis the mean andrthe aggregation of the non-infected individuals. The mixture component is the ’true’ prevalence\(\pi _{jg}\)for each treatment and study and is defined as the probability of harboring at least one fertilized female worm. We assumed that the male worms\(N_m\)and female worms\(N_f\)follow a common negative binomial distribution, that is

where\(w_{jg}\)is the mean worm burden,\(k_w\)the aggregation of the worms in the population,\(\alpha =\frac{w_{jg}}{w_{jg}+k_w}\), andpthe probability of a worm to be female. By assuming that the probability of a worm to be of either sex is 0.5 (i.e.,p= 0.5), that one male worm can fertilize all female worms and summing over the male worms, we derived the following distribution of fertilized female worms\(n_f\)(see Supplementary textS1):

The distribution of egg counts was computed by marginalizing over the joint distribution of egg counts and fertilized female worms, that is

where\(P(Y ^{(1)}_i|n_f)\equiv NB(cn_f,k^{(1)})\)andcthe number of eggs per fertilized female worm. Hence, we were able to compute the mean\(\mu ^{(1)}_{jg}\)and the variance\(\sigma ^2_{jg}\)of the marginal distribution of egg counts (see Supplementary textS2). Finally, from the latter two parameters a gamma distribution was derived for the individual mean infection intensity at follow-up, that is\(\mu ^{(1)}_{i_{jg}} \sim \text {Gamma}(\alpha _{jg}, \beta _{jg})\), where\(\alpha _{jg}=\frac{\mu ^{(1)}_{jg}}{\sigma ^2_{jg}}\)and\(\beta _{jg}=\frac{(\mu ^{(1)}_{jg})^2}{\sigma ^2_{jg}}\). The density-dependent fecundity of female worms was included in aforementioned parameters (see Supplementary textsS1andS2). Therefore, the whole transmission mechanism was taken into account20. The day-to-day variation\(\sigma _d^2\)in the excreted eggs at follow-up was taken into account in the same way as at baseline, that is\(log\Big (\mu ^{(1)}_{i_{jg}d}\Big ) = log\Big (\mu ^{(1)}_{i_{jg}}\Big )+\epsilon ^{(1)}_{id}\), where\(\epsilon ^{(1)}_{id} \sim \mathcal {N}\Big (\frac{-\sigma _d^2}{2},\sigma _d^2\Big )\). The ’true’ CR was computed as\(c_{jg}=1-\pi _{jg}\)and the ERR as\(\phi _{jg} = 1-\frac{{\mu }^{(1)}_{jg} \cdot \pi _{jg}}{{\mu }^{(0)}_{jg}}\). The sensitivity is estimated from the day-to-day variation\(\sigma _d\)and the aggregation calculated as weighted average from the aggregation at baseline\(k^{(0)}\)and follow-up\(k^{(1)}\)as follows:

with fixed mean infection intensities\(\mu _{ir}\)from 24 eggs per gram of stool (EPG, corresponds to 1 egg per Kato-Katz thick smear based on a stool volume of 41.7 mg) to 500 EPG. For the hyperparameters, the following priors were chosen: for\(\mu ^{(0)}_{jg}\)a gamma distribution with mean 50 and variance 1250; for\(\sigma ^{(0)}_{jg}\)an exponential distribution with mean 0.5 and variance 0.25, for\(\sigma _d^2\)a gamma distribution with mean 1 and variance 1; for\(1/k^{(0)}\)and\(1/k^{(1)}\)normal prior distributions with mean 0 and variance 1; for\(w_{jg}\)a gamma distribution with mean 2 and variance 50; for\(k_w\)a normal distribution with mean 0.3 and variance 0.5; forra normal distribution truncated at 0 with mean 0 and variance 1; forca normal with mean 1 and variance 1; and forda beta distribution with parameters 10 and 1. Semi-informative priors were used according to the biological literature26,27and weakly informative priors were chosen if prior knowledge was scarce or ambiguous. We compared prior and posterior distributions to confirm that inference is driven by the data. The model was run in Stan with 10 chains and 5000 iterations of which half of them were used for warm-up. Convergence was determined via Gelman and Rubin diagnostics28.

The number of participants and the mean infection intensities at baseline and treatment follow-up of the trials included in this analysis is summarized in Table1. The observed CRs for treatments againstT. trichiuraranged from 2 to 100%, and the ERRs from 0 to 100%. The largest difference in CRs between trials was observed for the combination treatment of albendazole (400 mg) plus oxantel pamoate (20 mg/kg). Estimated CRs in the different trials were 31, 69, and 100%, respectively. The corresponding ERRs were 68, 72, and 100%. For mebendazole (500 mg), the CRs were similar in the different studies ranging from 8 to 12%. There were larger differences in the ERRs ranging from 14 to 49%. The estimated CRs and ERRs for each treatment arm and trial are shown in Table2.

The estimates of the ‘true’ CRs ranged from\(1\)to\(79\%\)and the ‘true’ ERRs from\(-76\)to\(97\%\)(Table3). The most efficacious treatment againstT. trichiurain terms of CR was triple therapy (albendazole (400 mg) plus pyrantel pamoate (20 mg/kg) plus oxantel pamoate (20 mg/kg)) with a CR of 79% (95% Bayesian credible interval (BCI) 65–90%) and an ERR of 91% (95% BCI 67–99%). Albendazole (400 mg) plus oxantel pamoate (25 mg/kg) achieved the highest ERR of 97% (95% BCI 94–99%) and a CR of 63% (95% BCI 54–72%). Combination therapy with mebendazole (500 mg) plus pyrantel pamoate (20 mg/kg) plus oxantel pamoate (20 mg/kg) and albendazole (400 mg) plus oxantel pamoate (20 mg/kg) showed high efficacies with CRs of 69% (95% BCI 52–84%) and 63% (95% BCI 56–70%), respectively, and ERRs of 75% (95% BCI 11–97%) and 90% (95% BCI 84–95%), respectively.

The least efficiacious treatments againstT. trichiurawere single-dose albendazole (400 mg) with a CR of 1% (95% BCI 0–3%) and an ERR of 2% (95% BCI − 4 to 40%) and tribendimidine (400 mg) with a CR of 2% (95% BCI 0–4%) and an ERR of 40% (95% BCI 18–57%). Single-dose mebendazole (500 mg) had a similarly low CR of 4% (95% BCI 3–7%) and an even lower ERR than albendazole (31%, 95% BCI 16-45%).

Figure1shows the estimated ‘true’ CRs and ERRs with the corresponding 95% BCI. TableS2shows the estimates of the CRs, ERRs, and egg count variation at baseline and aggregation of the worm distribution at follow-up for each treatment arm from every trial. FigureS3shows the observed and ‘true’ CRs and ERRs with the corresponding 95% BCI graphically.

Estimated and observed cure rate (CR) and egg reduction rate (ERR) of drug therapies againstT. trichiura. Posterior mean and\(95\%\)Bayesian credible interval of the CR and the ERR (arithmetic mean) for the different treatment arms forT. trichiura. The black dots show the observed data. (Alb, albendazole; Iver, ivermectin; Meb, mebendazole; Oxan, oxantel pamoate; Pyr, pyrantel pamoate; Trib, tribendimidine).

The estimated day-to-day variation\((\sigma ^{(t)}_d)^2\)was 0.94 (95% BCI 0.91–0.97) and the variation in egg counts at baseline (\(k^{(0)}\)) was 0.08 (95% BCI 0.07–0.09) and 0.11 (95% BCI 0.1–0.12) at follow-up (\(k^{(1)}\)). Figure2shows the estimated sensitivity with 95% BCI of the Kato-Katz technique forT. trichiura. For a ‘true’ infection intensity of 24 EPG, which corresponds to the minimal infection intensity of one egg per slide using standard 41.7 mg templates, the sensitivity for a single Kato-Katz thick smear is between 44 and 53%; for duplicate Kato-Katz thick smears it is between 65 and 71%; and for quadruplicate Kato-Katz thick smears, obtained from two stool samples, it ranges from 88 to 92%. The sensitivity is above 90% for ‘true’ infection intensities above 300 EPG even for a single Kato-Katz thick smear.

Sensitivity of the Kato-Katz thick smear technique forT. trichiurafor single, duplicate or quadruplicate Kato-Katz thick smears. The lines show the posterior mean estimate and the shaded areas indicate the 95% Bayesian credible interval.

The Bayesian model used in this analysis takes into account diagnostic error, and hence, enabled us to infer on the ‘true’ efficacy of an ensemble of different drugs and treatment regimen againstT. trichiura. We not only estimated the ‘true’ CRs and ERRs of 29 different treatments separately, but also the weighted ‘true’ CRs and ERRs of those treatments where data were collected in several of the analyzed trials. Additionally, we provide the first intensity-dependent sensitivity estimation of the Kato-Katz technique for detection ofT. trichiurafor different sampling schemes.

The data analyzed in this study were collected by research groups using the same sampling protocols and adhering to the same diagnostic procedures, which enhances comparability between studies and treatments. Moreover, our estimates are infered from individual-level egg count data, which lead to better comparability to other studies and enabled us to estimate day-to-day variation. Since we took into account the diagnostic error, we accounted for individuals with low infection intensities, which are likely to be missed with the Kato-Katz thick smear technique, particularly if only a single or duplicate Kato-Katz thick smear(s) is analyzed. Hence, our estimates of the prevalence for the different treatments were higher than the observed ones, leading to lower CRs compared to those reported in the literature. These differences were also observed in studies which estimated CRs with the Kato-Katz technique and a quantitative real-time polymerase chain reaction (qPCR). For instance, Barda et al. observed CRs for combination therapy of albendazole plus oxantel pamoate of 82% for duplicate Kato-Katz thick smears from two days, compared to 79% with qPCR29. In our study, the observed CR was 78% compared to our model-based estimate of 63%. For albendazole plus ivermectin, Keller et al. reported CRs of 47% compared to 23% for the Kato-Katz technique and qPCR30, respectively, which is similar to our estimates.

Our results, which showed that combination therapy have a higher efficacy againstT. trichiurain terms of CR and ERR compared to single-drug treatments, are in line with earlier findings16. The triple combination treatment with albendazole (400 mg), pyrantel pamoate (20 mg/kg) and oxantel pamoate (20 mg/kg) showed the highest efficacy in terms of CR. In a systematic review and network meta-analysis put forth by Moser et al., the estimated CR and ERR of the aforementioned treatment were 84 and 92%16, respectively, which is similar to our results. The highest ERR was estimated for albendazole plus oxantel pamoate. The CR is comparable to the higher CR in the aforementioned meta-analysis, as the difference arises because of taking into account diagnostic error. The low efficacy of ivermectin might be due to a special strain in Côte d’Ivoire, which is closely related toTrichuris suis31. WHO recommends single-dose albendazole and single-dose mebendazole for the treatment of soil-transmitted helminth infection; yet, the low efficacy of those treatments reported by others was confirmed by our results7,8,9.

In comparison to the model developed by Grolimund et al., we include the density-dependent fecundity of egg production. Hence, all transmission mechanisms are taken into account and the model can be applied for high transmission settings. Although the distribution and administration of combination therapies is more difficult than single-drug therapies, their high efficacy could be crucial in the fight against soil-transmitted helminthiasis. Our study confirms that the sensitivity of the Kato-Katz technique increases substantially if multiple slides are read instead of a single one19,32. This insight is useful for control measures, as, at present, the recommended sampling scheme by WHO is to analyze only one Kato-Katz thick smear. If financial resources are not an issue and qPCR is not available, quadruplicate Kato-Katz thick smear should be employed for diagnosis. The intensity-dependent sensitivity curves developed in this analysis (for different numbers of Kato-Katz thick smears) can be consulted, particularly for low intensity settings, to decide how many thick smears should be analyzed per individual depending on how accurate the results should be.

Our study has several shortcomings that are offered for discussion. First, the estimates of the ERR have a rather large uncertainty. Second, the mean egg burden of the positives at follow-up is difficult to estimate for a treatment where no individual is positive. Nevertheless, the CR and ERR for such a treatment are estimated well, as they are also informed by the priors and the non-infected individuals. In the future our model could be extended to include factors such as age and sex. Large datasets would be required to undertake these analyses.

Our model can be adapted for other helminth species. For polygamous species only transmission priors would have to be changed, while for the monogamous case, also the mean and variance of the fertilized female worm distribution would have to be derived.

We developed a Bayesian model, which takes into account the transmission mechanism and the diagnostic error, which enabled us to directly compare the ‘true’ efficacy of 24 different treatment regimens againstT. trichiura. We found that combination therapy is more efficacious than single-drug treatment, which is in line with earlier findings. Furthermore, we estimated the infection intensity-dependent sensitivity of the Kato-Katz technique for different sampling schemes. Duplicate Kato-Katz thick smears increase the sensitivity considerably compared to a single Kato-Katz thick smear. The administration of combination therapies against soil-transmitted helminthiasis should be considered and the evaluation of infection intensity in low transmission settings via multiple Kato-Katz thick smears is recommended. These considerations should be further investigated by cost-benefit analysis for interventions in different settings.

Individual deidentified participant data that underlie the results reported in this article will be available upon request directly after publication for 1 year. Access will be granted to researchers who provide a scientifically sound proposal. The sponsor, investigator, and collaborators will approve the proposals on the basis of scientific merit. Requests should be directed to jennifer.keiser@swisstph.ch. Researchers who request data will need to sign a data access agreement before they are granted access.

World Health Organization. Soil-transmitted helminth infections.https://www.who.int/news-room/fact-sheets/detail/soil-transmitted-helminth-infections(2019). Accessed 10 Mar 2023.

Else, K. J.et al.Whipworm and roundworm infections.Nat. Rev. Dis. Prim.6, 44.https://doi.org/10.1038/s41572-020-0171-3(2020).

ArticlePubMedGoogle Scholar

Jourdan, P. M., Lamberton, P. H. L., Fenwick, A. & Addiss, D. G. Soil-transmitted helminth infections.Lancet391, 252–265.https://doi.org/10.1016/S0140-6736(17)31930-X(2018).

ArticlePubMedGoogle Scholar

Vos, T.et al.Global, regional, and national incidence, prevalence, and years lived with disability for 328 diseases and injuries for 195 countries, 1990–2016: A systematic analysis for the Global Burden of Disease Study 2016.Lancet390, 1211–1259 (2017).

ArticleGoogle Scholar

World Health Organization. 2030 targets for soil-transmitted helminthiases control programmes.http://www.who.int/intestinal_worms/resources/9789240000315/en/. Accessed 10 Mar 2023.

World Health Organization.Guideline: Preventive Chemotherapy to Control Soil-Transmitted Helminth Infections in At-risk Population Groups(World Health Organization, Geneva, 2017).

Google Scholar

Keiser, J. & Utzinger, J. Efficacy of current drugs against soil-transmitted helminth infections: Systematic review and meta-analysis.JAMA299, 1937–1948.https://doi.org/10.1001/jama.299.16.1937(2008).

ArticleCASPubMedGoogle Scholar

Moser, W., Schindler, C. & Keiser, J. Efficacy of recommended drugs against soil transmitted helminths: Systematic review and network meta-analysis.BMJ358, j4307.https://doi.org/10.1136/bmj.j4307(2017).

ArticlePubMedPubMed CentralGoogle Scholar

Clarke, N. E.et al.Efficacy of anthelminthic drugs and drug combinations against soil-transmitted helminths: A systematic review and network meta-analysis.Clin. Infect. Dis.68, 96–105.https://doi.org/10.1093/cid/ciy423(2019).

ArticleCASPubMedGoogle Scholar

Speich, B.et al.Efficacy and safety of albendazole plus ivermectin, albendazole plus mebendazole, albendazole plus oxantel pamoate, and mebendazole alone againstTrichuris trichiuraand concomitant soil-transmitted helminth infections: a four-arm, randomised controlled trial.Lancet Infect. Dis.15, 277–284.https://doi.org/10.1016/S1473-3099(14)71050-3(2015).

ArticleCASPubMedGoogle Scholar

Freeman, M. C.et al.Challenges and opportunities for control and elimination of soil-transmitted helminth infection beyond 2020.PLoS Negl. Trop. Dis.13, e0007201.https://doi.org/10.1371/journal.pntd.0007201(2019).

ArticlePubMedPubMed CentralGoogle Scholar

Speich, B.et al.Oxantel pamoate-albendazole forTrichuris trichiurainfection.N. Engl. J. Med.370, 610–620.https://doi.org/10.1056/NEJMoa1301956(2014).

ArticleCASPubMedGoogle Scholar

Dunn, J. C.et al.The increased sensitivity of qPCR in comparison to Kato-Katz is required for the accurate assessment of the prevalence of soil-transmitted helminth infection in settings that have received multiple rounds of mass drug administration.Parasit. Vectors13, 324 (2020).

ArticleCASPubMedPubMed CentralGoogle Scholar

World Health Organization. Ending the neglect to attain the Sustainable Development Goals: A road map for neglected tropical diseases 2021–2030.https://www.who.int/publications-detail-redirect/9789240010352. Accessed 10 Mar 2023.

Knopp, S.et al.Diagnosis of soil-transmitted helminths in the era of preventive chemotherapy: Effect of multiple stool sampling and use of different diagnostic techniques.PLoS Negl. Trop. Dis.2, e331.https://doi.org/10.1371/journal.pntd.0000331(2008).

ArticlePubMedPubMed CentralGoogle Scholar

Moser, W., Schindler, C. & Keiser, J. Drug combinations against soil-transmitted helminth infections.Adv. Parasitol.103, 91–115 (2019).

ArticlePubMedGoogle Scholar

Palmeirim, M. S.et al.Efficacy and safety of co-administered ivermectin plus albendazole for treating soil-transmitted helminths: A systematic review, meta-analysis and individual patient data analysis.PLoS Negl. Trop. Dis.12, e0006458 (2018).

ArticlePubMedPubMed CentralGoogle Scholar

Bärenbold, O.et al.Estimating sensitivity of the Kato-Katz technique for the diagnosis ofSchistosoma mansoniand hookworm in relation to infection intensity.PLoS Negl. Trop. Dis.11, e0005953 (2017).

ArticlePubMedPubMed CentralGoogle Scholar

Moser, W.et al.Diagnostic comparison between FECPAKG2 and the Kato-Katz method for analyzing soil-transmitted helminth eggs in stool.PLoS Negl. Trop. Dis.12, e0006562 (2018).

ArticlePubMedPubMed CentralGoogle Scholar

Grolimund, C. M., Bärenbold, O., Utzinger, J., Keiser, J. & Vounatsou, P. Modeling the effect of different drugs and treatment regimen for hookworm on cure and egg reduction rates taking into account diagnostic error.PLoS Negl. Trop. Dis.16, e0010810 (2022).

ArticlePubMedPubMed CentralGoogle Scholar

Wimmersberger, D.et al.Efficacy and safety of ivermectin againstTrichuris trichiurain preschool-aged and school-aged children: A randomized controlled dose-finding trial.Clin. Infect. Dis.67, 1247–1255.https://doi.org/10.1093/cid/ciy246(2018).

ArticleCASPubMedGoogle Scholar

Moser, W.et al.Efficacy and tolerability of triple drug therapy with albendazole, pyrantel pamoate, and oxantel pamoate compared with albendazole plus oxantel pamoate, pyrantel pamoate plus oxantel pamoate, and mebendazole plus pyrantel pamoate and oxantel pamoate against hookworm infections in school-aged children in Laos: A randomised, single-blind trial.Lancet Infect. Dis.18, 729–737.https://doi.org/10.1016/S1473-3099(18)30220-2(2018).

ArticleCASPubMedGoogle Scholar

Moser, W.et al.Efficacy and safety of tribendimidine, tribendimidine plus ivermectin, tribendimidine plus oxantel pamoate, and albendazole plus oxantel pamoate against hookworm and concomitant soil-transmitted helminth infections in Tanzania and Côte d’Ivoire: A randomised, controlled, single-blinded, non-inferiority trial.Lancet Infect. Dis.17, 1162–1171.https://doi.org/10.1016/S1473-3099(17)30487-5(2017).

ArticleCASPubMedGoogle Scholar

Moser, W.et al.Efficacy and safety of oxantel pamoate in school-aged children infected withTrichuris trichiuraon Pemba Island, Tanzania: A parallel, randomised, controlled, dose-ranging study.Lancet Infect. Dis.16, 53–60.https://doi.org/10.1016/S1473-3099(15)00271-6(2016).

ArticleCASPubMedGoogle Scholar

Palmeirim, M. S., Ame, S. M., Ali, S. M., Hattendorf, J. & Keiser, J. Efficacy and safety of a single dose versus a multiple dose regimen of mebendazole against hookworm infections in children: A randomised, double-blind trial.EClinicalMedicine1, 7–13 (2018).

ArticlePubMedPubMed CentralGoogle Scholar

Else, K. J.et al.Whipworm and roundworm infections.Nat. Rev. Dis. Prim.6, 44.https://doi.org/10.1038/s41572-020-0171-3(2020).

ArticlePubMedGoogle Scholar

Levecke, B.et al.Mathematical inference on helminth egg counts in stool and its applications in mass drug administration programmes to control soil-transmitted helminthiasis in public health.Adv. Parasitol.87, 193–247.https://doi.org/10.1016/bs.apar.2015.01.001(2015).

ArticlePubMedGoogle Scholar

Vats, D. & Knudson, C. Revisiting the Gelman-Rubin diagnostic.Stat. Sci.36, 518–529 (2021).

ArticleMathSciNetGoogle Scholar

Barda, B.et al.Comparison of real-time PCR and the Kato-Katz method for the diagnosis of soil-transmitted helminthiasis and assessment of cure in a randomized controlled trial.BMC Microbiol.20, 298 (2020).

ArticleCASPubMedPubMed CentralGoogle Scholar

Keller, L.et al.Performance of the Kato-Katz method and real time polymerase chain reaction for the diagnosis of soil-transmitted helminthiasis in the framework of a randomised controlled trial: Treatment efficacy and day-to-day variation.Parasit. Vectors13, 517 (2020).

ArticleCASPubMedPubMed CentralGoogle Scholar

Venkatesan, A.et al.Genetic differences among humanTrichurispopulations with differing responses to albendazole-ivermectin combination treatment.Am. J. Trop. Med. Hyg.105, 440–441 (2021).

Google Scholar

Liu, C.et al.More poop, more precision: Improving epidemiologic surveillance of soil-transmitted helminths with multiple fecal sampling using the Kato-Katz technique.Am. J. Trop. Med. Hyg.97, 870–875 (2017).

ArticlePubMedPubMed CentralGoogle Scholar

Download references

This study received financial support from the European Research Council (PV, grant number: ERC-2012-AdG-323180) and the Swiss National Science Foundation (JK, grant number: 320030_175585). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Swiss Tropical and Public Health Institute, Allschwil, Switzerland

Carla M. Grolimund, Jürg Utzinger, Somphou Sayasone, Jennifer Keiser & Penelope Vounatsou

University of Basel, Basel, Switzerland

Carla M. Grolimund, Jürg Utzinger, Somphou Sayasone, Jennifer Keiser & Penelope Vounatsou

Unit é de Formation et de Recherche Biosciences, Université Féélix Houphouët-Boigny, Abidjan, Côte d’Ivoire

Jean T. Coulibaly

Centre Suisse de Recherches Scientifiques en Côte d’Ivoire, Abidjan, Côte d’Ivoire

Jean T. Coulibaly

Lao Tropical and Public Health Institute, Vientiane, Lao People’s Democratic Republic

Somphou Sayasone

Public Health Laboratory Ivo de Carneri, Chake Chake, Pemba, Tanzania

Said M. Ali

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Conceptualization, C.M.G., J.K., and P.V.; Methodology, C.M.G., and P.V.; Acquisition of funding, J.K. and P.V.; Acquisition of data, J.T.C., S.S., S.M.A., and J.K.; Analysis, C.M.G. and P.V.; Interpretation of data, C.M.G., J.U., J.K., and P.V.; Writing original draft, C.M.G.; Review and editing, C.M.G., J.U., J.K., and P.V.

Correspondence toPenelope Vounatsou.

The authors declare no competing interests.

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Below is the link to the electronic supplementary material.

Open AccessThis article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visithttp://creativecommons.org/licenses/by-nc-nd/4.0/.

Reprints and permissions

Grolimund, C.M., Utzinger, J., Coulibaly, J.T.et al.Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy againstTrichuris trichiura.Sci Rep14, 23543 (2024). https://doi.org/10.1038/s41598-024-73164-7

Download citation

Received:02 April 2023

Accepted:16 September 2024

Published:09 October 2024

Version of record:09 October 2024

DOI:https://doi.org/10.1038/s41598-024-73164-7

Anyone you share the following link with will be able to read this content:

Sorry, a shareable link is not currently available for this article.

Provided by the Springer Nature SharedIt content-sharing initiative
