---
reference_id: DOI:10.1007/s00521-022-06940-z
title: Virtual reality and machine learning in the automatic photoparoxysmal response detection
authors:
- Fernando Moncada
- Sofía Martín
- Víctor M. González
- Víctor M. Álvarez
- Beatriz García-López
- Ana Isabel Gómez-Menéndez
- José R. Villar
journal: Neural Computing and Applications
year: '2023'
doi: 10.1007/s00521-022-06940-z
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://link.springer.com/content/pdf/10.1007/s00521-022-06940-z.pdf"
oa_status: hybrid
license: cc-by
local_pdf_path: files/DOI_10.1007_s00521-022-06940-z.pdf
---

# Virtual reality and machine learning in the automatic photoparoxysmal response detection
**Authors:** Fernando Moncada, Sofía Martín, Víctor M. González, Víctor M. Álvarez, Beatriz García-López, Ana Isabel Gómez-Menéndez, José R. Villar
**Journal:** Neural Computing and Applications (2023)
**DOI:** [10.1007/s00521-022-06940-z](https://doi.org/10.1007/s00521-022-06940-z)

## Content

AbstractPhotosensitivity, in relation to epilepsy, is a genetically determined condition in which patients have epileptic seizures of different severity provoked by visual stimuli. It can be diagnosed by detecting epileptiform discharges in their electroencephalogram (EEG), known as photoparoxysmal responses (PPR). The most accepted PPR detection method—a manual method—considered as the standard one, consists in submitting the subject to intermittent photic stimulation (IPS), i.e. a flashing light stimulation at increasing and decreasing flickering frequencies in a hospital room under controlled ambient conditions, while at the same time recording her/his brain response by means of EEG signals. This research focuses on introducing virtual reality (VR) in this context, adding, to the conventional infrastructure a more flexible one that can be programmed and that will allow developing a much wider and richer set of experiments in order to detect neurological illnesses, and to study subjects’ behaviours automatically. The loop includes the subject, the VR device, the EEG infrastructure and a computer to analyse and monitor the EEG signal and, in some cases, provide feedback to the VR. As will be shown, AI modelling will be needed in the automatic detection of PPR, but it would also be used in extending the functionality of this system with more advanced features. This system is currently in study with subjects at Burgos University Hospital, Spain.

S.I.: COMPUTATIONAL-BASED BIOMARKERS FOR MENTAL AND EMOTIONAL
HEALTH(CBMEH2021)
Virtual reality and machine learning in the automatic
photoparoxysmal response detection
Fernando Moncada 1 • Sofı´a Martı´n2 • Vı´ctor M. Gonza´ lez1 • Vı´ctor M. A´ lvarez2 • Beatriz Garcı´a-Lo´ pez3 •
Ana Isabel Go´ mez-Mene´ ndez3 • Jose´ R. Villar 2
Received: 9 November 2021 / Accepted: 4 January 2022 / Published online: 29 January 2022
/C211 The Author(s) 2022
Abstract
Photosensitivity, in relation to epilepsy, is a genetically determined condition in which patients have epileptic seizures of
different severity provoked by visual stimuli. It can be diagnosed by detecting epileptiform discharges in their elec-
troencephalogram (EEG), known as photoparoxysmal responses (PPR). The most accepted PPR detection method—a
manual method—considered as the standard one, consists in submitting the subject to intermittent photic stimulation (IPS),
i.e. a ﬂashing light stimulation at increasing and decreasing ﬂickering frequencies in a hospital room under controlled
ambient conditions, while at the same time recording her/his brain response by means of EEG signals. This research
focuses on introducing virtual reality (VR) in this context, adding, to the conventional infrastructure a more ﬂexible one
that can be programmed and that will allow developing a much wider and richer set of experiments in order to detect
neurological illnesses, and to study subjects’ behaviours automatically. The loop includes the subject, the VR device, the
EEG infrastructure and a computer to analyse and monitor the EEG signal and, in some cases, provide feedback to the VR.
As will be shown, AI modelling will be needed in the automatic detection of PPR, but it would also be used in extending
the functionality of this system with more advanced features. This system is currently in study with subjects at Burgos
University Hospital, Spain.
Keywords Electroencefalogram /C1 Virtual reality /C1 Photoparoxysmal response /C1 Machine learning
& Vı´ctor M. Gonza´lez
vmsuarez@uniovi.es
Fernando Moncada
UO245868@uniovi.es
Sofı´a Martı´n
UO258355@uniovi.es
Vı´ctor M. A´ lvarez
victoralvarez@uniovi.es
Beatriz Garcı´a-Lo´pez
bgarcialo@saludcastillayleon.es
Ana Isabel Go´mez-Mene´ndez
agomm@saludcastillayleon.es
Jose´ R. Villar
villarjose@uniovi.es
1 Electrical Engineering Department, University of Oviedo,
Asturias, Spain
2 Computer Science Department, University of Oviedo,
Asturias, Spain
3 Neurophysiology Department, Burgos University Hospital,
Burgos, Spain
123
Neural Computing and Applications (2023) 35:5643–5659
https://doi.org/10.1007/s00521-022-06940-z(0123456789().,-volV)(0123456789().,-volV)

1 Introduction
Virtual reality (VR) is increasingly becoming part of our
daily lives and its applicability is widening [ 29]: from
video games and entertaining, to education, medical
treatment and rehabilitation, military applications, archi-
tectural and urban design, digital marketing and activism,
engineering and robotics, ﬁne arts, heritage and archaeol-
ogy, occupational safety, social sciences, psychology and
many more. For this reason, it is not only important to
understand how this technology can affect our brains, but
also its potential to extend the current scope of neurological
diseases detection methods. Using VR in new speciﬁc
triggering scenarios will allow controlling and extending
the available functionalities of the visual stimulation sys-
tems used for the detection of such pathologies [ 4].
This reﬂection is not new. Back in the 1990s, research
performed to detect the risk of television and video games
exposure resulted in a set of recommendations for TV
manufacturers and video games developers. Simultane-
ously, the studies performed were the basis to many new
uses of these techniques in education [9] or in rehabilitation
[8], to name a few.
Photosensitivity is an abnormal visual sensitivity of the
brain resulting in a photoparoxysmal response (PPR), i.e. a
brain epileptic discharge consisting of a cortical spike or a
spike-and-wave provoked by a ﬂash or a visual stimuli
[26]. There are four different types of PPR resulting from
different brain responses to intermittent light stimulation
[31]. Even though PPR can be found in non-epileptic
electroencephalogram (EEG) recordings, it is strongly
associated with epilepsy [ 16]. The relevance of the PPR
relies on its association with speciﬁc epileptic syndromes
[34] and monitoring of treatment in a clinical context [ 20].
The photosensitivity range is related to the likelihood of
occurrence of reﬂex seizures in daily life; thus, it is of
crucial interest to early detect PPR. The most commonly
used procedure to detect PPR, known as intermittent photic
stimulation (IPS), is described in [ 23]. It proposes to sub-
mit the subject to a series of light ﬂashes while simulta-
neously monitoring the brain activity using EEG signals,
according to the European consensus group methodology
for visual stimulation deﬁned in 2012 [ 27]. The light ﬂa-
shes frequency is ﬁrst increased from a minimum to a
maximum or until a PPR is observed (whatever happen
ﬁrst). If no PPR is observed, the process ﬁnishes. Should a
PPR occur, the procedure is repeated in an inverse manner,
i.e. starting with a top ﬂickering frequency that is gradually
decreased until a minimum is reached or a PPR happen.
The aim is to detect the minimum and the maximum fre-
quencies at which the subject shows PPR, if any, with the
minimal exposure.
The detection of PPR is usually performed by physi-
cians, i.e. clinical neurophysiologists and nurses, who
manually review the EEG signals’ variability in search of
PPR [2, 14, 22], taking into account each subject’s clinical
context such as age, seizure and family history. To our best
knowledge, no automated method for the detection of PPR
has been developed so far. This research is mainly focused
on the design of a new and safe procedure for the automatic
detection of PPR within EEG signals using digital bio-
markers implemented using VR and AI techniques.
In this sense, [ 25] designed a PPR detection method by
analysing the potential and oscillation of the response
provoked by a ﬂashing stimulation, but following a dif-
ferent stimulation pattern from the standard one. There are
other recent studies that analyse the photosensitivity and
epilepsy based on other generalized discharges or seizures
than PPRs: in [ 18], a detection method based on the band
amplitude ﬂuctuation computed from a high-frequency and
a low-frequency components of the EEG windows in each
EEG channel is proposed; [ 30] applied the extreme gradi-
ent boost technique for the classiﬁcation of seizures in two
different ways (applying a standard partitioning of the data
and applying a leave-one-out cross-validation scheme),
while a channel-independent long short-term memory
network is used in [5]; the information extracted from EEG
and electrocardiogram (ECG) signals is used in [ 35]i na
multi-modal neural network which analyse the data in three
different ways (only EEG data with a convolutional LSTM
network; only ECG data with a residual convolutional
network; and a fused network which combines the outputs
of the individual networks to perform the ﬁnal classiﬁca-
tion); in [ 6], K-nearest neighbours and artiﬁcial neural
networks are used for the detection of ictal discharges and
inter-ictal states; [ 32] proposed an EEG single-channel
analysis applying three types of visibility graphs (basic,
horizontal and difference) to represent different EEG
patterns.
Other studies make use of additional and different bio-
metric measures for the same purpose, such us electro-
cardiograms (ECG) [ 10, 11, 28], electromyograms (EMG)
[3, 36] or magnetoencefalograms (MEG) [ 24].
This study proposes an alternative to the conventional
IPS procedure for PPR detection using VR and machine
learning (ML). This research is focused on the most fre-
quent PPR type; thus, the PPR detection still needs more
research work as it is not completely solved. However,
introducing VR would eventually allow to study and to
develop new and safer procedures for PPR detection. Since
the VR infrastructure is much more ﬂexible than the
standard one, it can be easily conﬁgured to carry out new
assays and stimulation paradigms, allowing for an
advanced IPS/Visual stimulation system. Our proposal
includes a VR device with a wireless connection to a
5644 Neural Computing and Applications (2023) 35:5643–5659
123

computer that has access to the data gathered by the EEG
sensors. The subject must wear at the same time both the
EEG cap and a head mounted display (HDM). Further-
more, a plausible solution for the automatic PPR detection
is proposed using some features extracted from the EEG
signals in an average montage, and classic ML techniques.
An average montage is used so that the electronegative
PPR discharge will express with an upward deﬂection of
the EEG signal in the affected channel.
The main contributions of this research are:
– To introduce VR in a close loop with AI and ML
models, so medical procedures could be revisited and
enhanced. This contribution can lead in the near future
to more advanced diagnose tests and procedures.
– To provide the neurophysiology department at Burgos
University Hospital with a novel instrument to analyse
the impact of VR in relation to photosensitivity by
integrating this solution in its daily work.
– To develop ML models to detect anomalies in the EEG
recordings when the patient is ﬂashed using either VR-
ML IPS or conventional IPS.
The structure of this study is as follows. The next section
focuses on the description of the proposal, detailing the
different elements in the loop. Section 3 gives details of the
experimentation set-up that has been carried out at the
proposal, while Sect. 4 includes all the obtained results and
the discussion on them. The ﬁnal section draws the con-
clusion of this research.
2 A prototype for VR-ML IPS procedure
The proposed solution complements the conventional set-
up by means of introducing a VR device that the subject
must wear along with an EEG cap (see Fig. 1). The signals
from the EEG sensors are analysed using well-known ML
techniques. The intelligent module will eventually control
the VR contents to gain increased capabilities and to per-
form more complex assays. This section gives details on
each of the main modules: the VR part (next subsection)
and the ML module (Sect. 2.2).
2.1 VR design for IPS and PPR detection
Flashing lights are one of the main triggers of photosen-
sitive responses. VR-Photosense [ 15] is a software
designed to detect photic-driving and PPR while using VR
and wearing a head-mounted display (HMD). VR-Photo-
sense offers a VR scenario with IPS in order to measure
brain responses to ﬂashing lights at various frequencies and
using different sequences. The main goal of this software is
to simulate conventional IPS tests in a virtual reality
environment.
Conventional IPS places the light stimulator at a very
short distance from the patient’s eyes, creating high
exposure to ﬂickering lights which are perceived with
intensity even when the patient’s eyes are closed. In order
to emulate the exposure and sensory effect caused by the
conventional IPS light stimulator, a virtual reality scene
has been designed as a 3D enclosing spherical dome
environment with the patient’s vision placed at its centre
(see Fig. 4). This design suppresses patient’s peripheral
vision and increases the focus on the visual stimuli even
with the eyes closed.
Fig. 1 To the left, the
conventional set for IPS
procedure. To the right, the new
VR-ML set for IPS procedure,
including automatic EEG
analysis and PPR detection
Neural Computing and Applications (2023) 35:5643–5659 5645
123

The VR-Photosense’s set-up is fairly simple. After
downloading and starting the app, the cardboard viewer,
into which a smartphone is inserted, is secured to the
subject’s head using the adaptable straps, leaving the upper
part of the head clear. Then, the EEG cap is easily set up on
the subject’s head covering all necessary points of contact
as shown in Fig. 2.
The software system is divided into two parts: the light
stimulation and the monitoring software. The VR-Photo-
sense’s default conﬁguration stimulates with white light
combined with dark black background, emulating the
conventional IPS. Introducing an innovation to conven-
tional IPS, VR-Photosene allows the colour of the ﬂicker-
ing light and background to be changed from the default
conﬁguration, so we designed two coloured settings in
addition to the white one: i) one with bright red ﬂashes and
deep blue background; ii) and another with deep blue ﬂa-
shes with dark black background. These tones may inﬂu-
ence the brain discharges, and combined may be more or
less provocative when compared to the default one,
allowing to study brain behaviour reacting to the stimula-
tion with both of these scenarios.
VR-Photosense has also been designed to resemble the
conventional stimulation set-up and to facilitate the work
of physicians, both clinical neurophysiologists and nurses,
while conducting photosensitivity tests at the hospital. This
system includes a monitoring feature that allows to observe
in real time what is happening on the VR stimulation via a
web server. This is thanks to the use of Websockets, a
communications protocol that offers full-duplex commu-
nication channels over a single TCP connection making it
faster and with low latency to update system.
This monitoring feature along with EEG recordings
translates into a full coverage IPS scenario that closely
resembles the conventional set-up, with the difference of
replacing the traditional stimulation device with a low cost
VR headset and the VR-Photosense software. The EEG set-
up to carry out VR-Photosense testing at the hospital
consists of using Natus Brain monitoring and Neuroworks
software for EEG recording. Furthermore, the different
hardware and software elements can be easily mixed and
replaced as they are completely independent from each
other. For example, the VR-Photosense can be conﬁgured
to work with higher end HDMs such as Oculus; or EEG
recording can be performed using a different device such
us OpenBCI 3D printed device and open source software,
which were used at the university EEG laboratory for
preliminary experiments.
All in all, VR-Photosense offers an innovative, low-cost
and cross-platform IPS scenario in virtual reality, with
more upcoming features to be included aimed to achieve a
more detailed diagnosis.
This light stimulation software has been implemented in
Unity 3D using the programming language C#. Unity is a
video game development engine that allows designing 3D
scenes by means of a visual editor and the programming of
gameplay events via scripting. These scripts are associated
with the game objects included in the scene so that they
behave in the desired way.
Within the scene, the assets included are structured in
software components as shown in Fig. 3.
– Controls: auto-generated script and input system. The
new InputSystem 1.0.2 of Unity has been used, which
allows to set up the desired inputs through an interface.
Different inputs can be entered from different devices
for the same action. This makes conﬁguration and
connectivity with different types of input hardware,
such as keyboards and game controllers, seamless.
Fig. 2 VR-Photosense set-up with a cardboard viewer and an
OpenBCI EEG headset
 Fig. 3 VR-Photosense software package diagram
5646 Neural Computing and Applications (2023) 35:5643–5659
123

– GoogleVR: an SDK for Android that allows the
creation of virtual reality applications to be used with
Google Cardboard HMD.
– Plugins: set of Android plugins needed to export
applications for devices using this operating system.
– Resources: all the scripts developed for lighting and
connection with the monitoring side. This package also
includes shaders and materials used in the scene.
– Scenes: the designed virtual reality scene (Fig. 4).
– XR: default Unity conﬁguration for extended (virtual
and augmented) reality apps.
The developed scene has four objects or GameObjects:
the camera, two point lights and a sphere (see Fig. 4). The
purpose of the sphere is to provide a black background,
placing the camera inside it and inverting the normals, thus
avoiding transparency. This inversion process is done by
adding a custom shader to a new material assigning it to the
sphere. As for the spotlights, one of them is the main white
light and the other provides a blue background for the
custom colour functionality.
All developed scripts use the MonoBehaviour built-in
class, since Unity uses a standard Mono run-time imple-
mentation. These classes are considered blueprints and
each time they are associated with a GameObject, a new
instance of the object deﬁned by that blueprint is created.
In them, two methods are predeﬁned: Start and Update. In
this case, only Start is used, which will be called by Unity
when loading the scene. It is also important to note the use
of corrutines. Corrutines are functions that allow pausing
and resuming the execution in the frame in which it was
paused. In this case they are used to implement the ﬂick-
ering effect in the lights and the stimulation sequences.
As for the input system, two options were considered:
remote control and keyboard. Considering the number of
conﬁgurable parameters and the controlled actions to be
performed by the person in charge of the stimulation, the
use of only a VR remote control was considered insufﬁ-
cient. Bearing in mind the end user and the technology they
use on a daily basis, the use of a Bluetooth keyboard was
chosen. As a result, more conﬁgurations are available and
the commands are set in the way these experts consider
more comfortable to perform the stimulation in the most
efﬁcient possible manner. However, in order to enable the
use of the stimulation with the Oculus Quest 2 glasses, this
conﬁguration has also been adapted for the two remote
controls associated with this HMD. Finally, the list of
commands available is shown in Table 1.
2.1.1 Monitoring
In addition to simulating the IPS environment, it is deemed
necessary to know what is happening inside the scene
during the tests. To address this problem, a monitoring
component—a web page ( https://vrphotosense.herokuapp.
com)—was added to the system. This solution allows the
physicists to see in real time what is happening in the VR
stimulation, e.g. the evolution of the sequences and the
commands entered by the user.
Another possibility was to implement a sound system to
communicate the situation through audio, but it was con-
sidered less efﬁcient as it was volatile and did not have a
visual record of the simulation.
To implement the monitoring system, a WebSokets
component was used, which allows real-time and fast
communication between the smartphone application and
the web page avoiding the use of a database. The desired
functionality is as shown in Fig. 5. Client 1, the smart-
phone application, sends information about the stimulation
to the server, and the server passes it to client 2, the web
page, which displays it on the screen along with a time
stamp.
WebSockets is a protocol that provides bidirectional,
full duplex communication over a single TCP socket. The
environment in which the VR-Photosense application is
used is a fairly sensitive one for medical testing, thus
imposing an as fast as possible exchange of information
exigence. WebSockets is probably the most popular pro-
tocol for this type of use cases where data needs to be sent
in real time. As we have seen before, Unity is based on the
Mono platform as scripting engine, which means that it
works in .NET (C#). This framework provides a default
support for this protocol that is also supported by Mono,
Fig. 4 Scene diagram implemented in Unity 3D
Neural Computing and Applications (2023) 35:5643–5659 5647
123

through the System.Net.WebSockets namespace. The
operation in this case would be as shown in Fig. 6.
The server has been developed using Node. It is a simple
server that receives information from the client and returns
it. In this case, nothing is done in Unity with the returned
Table 1 List of available
commands in VR-photosense
application
Available commands
Action Command (keyboard) Command (Quest 2)
Start Enter Right trigger
Pause Space bar Right grip
Reset Backspace Secondary touched (R)
Increment Hz Numpad ? Primary touched (R)
White light B Start (L)
Blue light A Left grip
Red-blue combination R Left trigger
Upward pattern Up arrow Primary touched (L)
Downward pattern Down arrow Secondary touched (L)
Exit Escape Start (R)
Fig. 5 Theoretical functionality
of the monitoring system
Fig. 6 Sequence diagram of the
system using WebSockets
5648 Neural Computing and Applications (2023) 35:5643–5659
123

information; it is the monitoring client that makes use of it.
This client is an HTML page that connects to the server,
opens a connection, gets the information coming from the
server that is part of a message and displays it on the
screen. This HTML client has been implemented in the
simplest possible way since it is an add-on to the main
work and its appearance in terms of design is not relevant
for the EEG laboratory staff.
2.2 ML-based PPR detection
PPR can be found in epileptic syndromes that present
seizures with or without visual stimulus trigger, and in
some subjects both types of seizures are observed. Waltz
classiﬁcation [ 31] is used to deﬁne the expression of the
PPR from an electroencephalographic point of view,
introducing up to four different types of PPR:
• Type-1: spikes within the occipital rhythm.
• Type-2: parieto-occipital spikes with a biphasic slow
wave.
• Type-3: parieto-occipital spikes with a biphasic slow
wave and spread to the frontal region.
• Type-4: generalized spikes and waves or polyspikes and
waves.
All of them are depicted in Fig. 7. Type-4 PPR is the most
frequently found in epileptic syndromes where photosen-
sitivity constitutes a clinical concern, as it seems to have a
strong association—higher than 90%—with epileptic sei-
zures; the detection of this type of PPR represents the
challenge focused on this research. Besides, in clinical
practice, it is frequent that expression of PPR is variable,
and in many times we obtain PPR that not necessarily ﬁt
within only one category of those initially deﬁned by
Waltz. Even more, the morphological characteristics of a
given subject’s PPR may vary because of clinical variables
as doses of anti-epileptic treatment, sleep quality, etc.
To identify Type-4 PPR we propose the use of sliding
windows—one second length and a tenth of a second
shift—followed by a pre-processing stages that subtracts
the window average and performs a feature extraction.
Well-known ML techniques consider these features to
propose a ﬁnal label to the window.
These ML techniques are applied in three parts that will
be described in this section. First, the set of transformations
that will be applied and their rationale are explained in
Sect. 2.2.1. Then, the design and deployment of the ML
models are detailed in Sect. 2.2.2 and, ﬁnally, the training
of the ML part is described in Sect. 2.2.3.
Fig. 7 The four types of PPR:
a type-1: spikes within the
occipital rhythm; b type-2:
parieto-occipital spikes with
biphasic slow wave; c type-3:
parieto-occipital spikes with
biphasic slow wave and spread
to the frontal region; d type-4:
generalized spikes and waves
Neural Computing and Applications (2023) 35:5643–5659 5649
123

2.2.1 Feature extraction
The selection of mathematical transformations for signals
representation is, per se, a problem that needs to be care-
fully addressed. The main point is to select features that, in
conjunction, include, as a whole, the information that the
experts use to make a decision. Therefore, all the possible
windows must be analysed and signiﬁcant differences must
be stated between the anomalies and the normal signal
state. Nowadays, the problem of feature transformation is
dealt with deep learning (DL) and, more speciﬁcally, with
auto-encoders; however, due to the lack of data to train the
networks, we left this issue for future research.
For this study, we focused on channels Fz and O2
because these are the channels were PPRs more frequently
appear regardless their type. We pay attention to their
normal and abnormal behaviour for the considered PPR
type. Some examples of the windows that might be faced
are depicted in Fig. 8. From the analysis of the signals, the
following features set has been selected to represent each
EEG data window, where w is the width of the window, t
refers the time stamp for which the feature is computed, c
is the channel—either Fz or O2—and d
c
t is the EEG
c channel’s signal with an average montage—the PPR
expresses with an upward deﬂection—at time stamp t:
• Cumulative First derivative , also known as the
intensity of the signal, computed as
CFDc
t ¼ 1
w
Pw/C0 1
i¼0 jdc
tþiþ1 /C0 dc
tþij=D. This feature has
been chosen because PPR present high rate of change in
the value of the channel. D represents the interval
between consecutive samples, which is kept constant.
• Cumulative Second derivative computed as
CSDc
t ¼ 1
w
Pw/C0 1
i¼0 jdc
tþiþ2 /C0 2 /C2 dc
tþiþ1 þ dc
tþij=D2.T h i s
feature has been selected because there is also a high
rate of change in the ﬁrst derivative, but not so high as
for artefacts.
• Number of relevant peaks using the S1 measurement
proposed in [ 19] and computed as follows. Equation 1
deﬁnes the calculation of S1, where k is the predeﬁned
number of samples and p is the current sample
timestamp for which we are determining whether it is
a peak or not. The S1 transformation represents a
scaling of the TS, which makes the peak detection
easier using a predeﬁned threshold a.
S1ðpÞ¼ 1
2 /C2 max
p/C0 1
i¼p/C0 k
ðdc
p /C0 dc
i Þþ max
pþk
i¼pþ1
ðdc
p /C0 dc
i Þ
/C26/C27
ð1Þ
So, for each point for which S1ðpÞ can be computed
within the EEG sliding window we compute S1ðpÞ;a
peak occurs in time p if the value Sp is higher than a and
is the highest in its 2 k neighbourhood. In the original
report, all the parameters ( k, a) where carefully deter-
mined for each problem in order to optimize the peak
detection. In this research, k is set to 10 and a is set to
three times the standard deviation of the EEG channel
values when no activity is shown (upper right corner in
Fig. 8).
• Sum of the absolute values , to measure the area under
the curve of the EEG signal.
Fig. 8 Three EEG fragments from different conditions: the left-most
and the centre recordings are considered normal conditions, while the
recording at the right shows a PPR. The recordings include, from top
to bottom, signals from the F3-AVG, Fz-AVG, F4-AVG, O1-AVG
and O2-AVG channels, respectively, where AVG stands for the
average of all recorded electrodes
5650 Neural Computing and Applications (2023) 35:5643–5659
123

• Maximum differences , also known in some ﬁelds as
amount of movement [ 1], which measures the differ-
ences between the highest and the smallest values—
expected to be a high value. It is calculated as
MDc
t ¼j maxi2½t;tþw/C138 ðdc
i Þ/C0 mini2½t;tþw/C138 ðdc
i Þj.
• Average Energy as proposed in [33], as the sum of the
squared discrete FFT components magnitudes of the
signal.
All the features are standardized; given a data set, the
average and the standard deviation are computed and used
to transform the values into a normal distribution with
mean 0.0 and standard deviation 1.0.
2.2.2 Designing and deploying the ML part
The goal in this stage is to obtain models able to label the
pre-processed EEG signal windows as normal or as PPR.
Due to the data imbalance, the most interesting approach is
to use unsupervised learning, so anomalies can be detected.
However, this might generate too many false positive, so it
could be interesting to also develop a complementary
supervised learning solution. Therefore, for this research
we proposed to use, ﬁrst, unsupervised learning to obtain a
model that signals those anomalous windows and then to
classify the anomalous windows as PPR or normal using a
supervised approach. The unsupervised learning is speciﬁc
for a given subject, while the supervised learning is a
generalised model.
For this stage, we will develop models following the
workﬂow proposed in Fig. 9. Data from the EEG sensors is
windowed as explained before. For each window, the
average is calculated and subtracted; the transformations
from the previous subsection are calculated afterwards. A
one-class classiﬁer, learned for the current subject data,
labels the window as normal or not. In case a window is
labelled as an anomaly, then the two-class classiﬁer,
learned from other subjects, labels the window as PPR or
not.
For the one-class classiﬁer, an unsupervised one-class
k-nearest neighbours model (1C-KNN) [ 12, 17] is tested:
this model has been selected for its fast training and
evaluation times while still performing sufﬁciently
accurate.
For the two-class classiﬁer we propose K-nearest
neighbour (2C-KNN) due to the small number of instances
in the available data set.
Both classiﬁers are from the scikit-learn library for
Phyton [21].
2.2.3 Training the ML part
Training the models has two main stages as can be seen in
Fig. 10: (i) training the one-class model and (ii) training
the two-class model. At this moment we have two collec-
tions of data: (a) a collection of windows from the current
subject (CPData), all labelled as normal, and (b) a collec-
tion of windows from the historical records (HRData), each
window with its corresponding normal or PPR label.
CPData is used in the one-class training, while HRData is
used in the two-class training. The ﬁrst part of the training
is the 2C-KNN learning using the HRData; in case of
highly imbalance of the data set, SMOTE will be used.
Different values of the parameter K are tested for both
classiﬁers to ﬁnd the best performing model.
When analysing the data recorded for the current sub-
ject, an incremental training is proposed. The idea is
repeating the one-class classiﬁer training until a real PPR
be detected at a certain ﬂashing frequency. That is, in case
the frequency to be tested is increased for example from 4
to 6 Hz, if no PPR is detected in this new stimulation
frequency, then the 1C-KNN is trained including the win-
dows gathered from the ﬁrst frequency range (1–6 Hz), and
then, the next ﬂashing frequency is evaluated (8 Hz) and
the process is repeated again until a PPR is detected. The
stimulation frequency at which the ﬁrst PPR is detected is
the cut frequency ( fc). The process is illustrated in Fig. 11.
This process has been described for the following
ﬂashing frequency increase sequence—standard
Fig. 9 The workﬂow of the designed approach. The data gathered
from the current subject are pre-processed. When a data window
comes from frequencies smaller or equal to fc (the cut frequency,
which is the stimulation frequency value at which the ﬁrst PPR
appears), the window is preserved for the training of the one-class
models; otherwise, the window is labelled as normal or as anomaly. In
this latter case, the two-class classiﬁer labels the window as PPR or
not. However, when no window is labelled as including a PPR for the
current frequency, the windows for this frequency are also considered
and the one class model is re-trained
Neural Computing and Applications (2023) 35:5643–5659 5651
123

frequencies used are 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25,
30, 40, and 50Hz.
Additionally, the PPR analysis also includes a decreas-
ing frequency study, starting at certain frequency (i.e. 50
Hz) and decreasing the frequency until a PPR be found.
The whole process should then be repeated but with fc set
to the corresponding limit; the same workﬂow shown at
Fig. 11 is mostly valid with minor changes: i) the com-
parison operation is /C21 , ii) the 2C-KNN is speciﬁc for the
decreasing ﬂashing frequencies.
3 Experimentation set-up
3.1 Evaluation of VR-ML IPS procedure
In the preliminary stage of the study, a series of intermit-
tent light stimulation tests were performed under the
supervision of physicians (clinical neurophysiologists) at
the hospital. The experimentation was divided into two
series of tests in order to determine whether the virtual
reality stimuli have a photosensitivity impact, both on
healthy subjects and on previously diagnosed photosensi-
tive subjects.
As a starting point, the simplest response to look for in
an EEG recording is a photic-driving response, that is, a
common physiological response to light stimuli during an
IPS, which is triggered by an intermittent photic retinal
stimulation that can be detected in the alpha rhythm [ 7]. It
consists of brain activity that matches the time and fre-
quency or harmonic frequency of intermittent light stimuli
[13]. It is usually greater when the light stimulation is close
to the subject’s alpha rhythm.
A second series of tests were carried out to determine
the ability of VR-Photosense to elicit photoparoxysmal
responses. These tests looked for PPR induced by photic
stimulation, as it has been previously described in this
paper, at existing EEG records corresponding to previously
diagnosed photosensitive subjects.
The study is ongoing. Although the low number of
subjects does not yet allow establishing generalizations, the
initial series of tests conﬁrmed very promising results
regarding the use of VR-IPS both for the detection of
photic-driving as well as PPR responses as described in the
Results and Discussion section.
3.2 Evaluation of the ML-based PPR detection
The data set gathered from Burgos University Hospital is
used to study the performance of the ML method for the
PPR detection. This data set includes ten anonymized EEG
recording sessions from different photosensitive subjects
Fig. 10 All the data are
windowed and the features are
computed. Although all the
training stages seem to be
simultaneous, they are
performed at different time
Fig. 11 Incremental learning of
the one class models once no
PPR has been found for a
certain ﬂashing frequency f. The
windows gathered for this f are
also used to train the one-class
models until the fc value is
found. The ﬁgure shows the
increasing ﬂashing frequency
case, a similar structure is
proposed when decreasing the
ﬂashing frequency
5652 Neural Computing and Applications (2023) 35:5643–5659
123

recorded with the hospital’s own equipment. Each session
consisted of two continuous recordings while the IPS (the
conventional IPS and the proposed VR-IPS) procedure was
performed: the frequency of the photic stimulation was
increased in the range 1–50 Hz for the detection of the
minimum frequency (fc) that causes a PPR in each subject.
The duration of each session varies in the range 3–5 min-
utes. The EEG signals were recorded at a sampling rate of
500Hz from 19 electrodes placed according the 10–20
standardized system, as shown in Fig. 12. Each recording
was then manually labelled by the expert clinical neuro-
physiologist by visual analysis, labelling every PPR with
their corresponding type: ﬁve subjects showed Type-4
PPR, while ﬁve other subjects showed other types of PPR.
Training the models follows a leave-one-participant-out
cross-validation scheme to train both one-class and two-
class classiﬁers. Therefore, EEG windows from the current
subject are not used in training the 2C-KNN model, while
the labelled windows from the remaining subjects con-
forms the HRData data set; conversely, the data from the
current subject conforms the CPData data set, which is
used by the 1C-KNN classiﬁer.
The HRData is used to train the 2C-KNN classiﬁer; to
do so, tenfold cross-validation is used to select the best
parameter value. On the other hand, the CPData is used to
train the 1C-KNN but also to evaluate the proposal.
Therefore, the CPData is split in two: i) the data for a
frequency f /C20 f
c, where fc is the current subject’s cut fre-
quency—used to train the 1C-KNN—and ii) the data for a
frequency f [ fc, used to evaluate both the 1C-KNN and
the 2C-KNN for those instances labelled as anomalies.
The accuracy (ACC), the sensitivity (SEN) and the
speciﬁcity (SPE) will be used to measure the quality of the
models. Furthermore, the average, median and standard
deviation among the tenfold of the cross-validation will
help in the evaluation of this model.
For the sake of simplicity, only increasing ﬂashing fre-
quencies training and analysing is shown. The comple-
mentary decreasing ﬂashing frequencies procedure would
be performed in a similar manner, so it is omitted to avoid
overload of ﬁgures and numbers.
The experimentation will be divided into two main
parts: training and evaluation of the 2C-KNN using the
HRData, and training and evaluation of the 1C-KNN using
the CPData. Due to the fact that this research is focused
only on Type-4 PPR, the experimentation will be per-
formed considering only these phenomena; however, we
also replicate the same experiments for the complete data
set considering all PPR types.
4 Results and discussion
4.1 Photic-driving response and PPR detection
using VR-Photosense
Our initial testing of VR-Photosense both on healthy sub-
jects and previously diagnosed subjects, conﬁrms the
expected correlation between the IPS and the EEG
recording. Moreover, we have identiﬁed photic-driving
responses (see Fig. 13) as well as PPR responses (see
Fig. 14) using the Natus Neuroworks monitor. In the for-
mer one, the expected photic-driving responses of a healthy
patient can be seen after the photic stimulation, more
strongly in the occipital and parietal channels, and at fre-
quencies of stimulation that are similar to the alpha rhythm
of the patient, that is their basal oscillating frequency when
awake and in quiet state. In this case, the frequency spec-
trum of the brain response after the stimulation at 10Hz
reveals a strong component around the same frequency
value as expected. In the last one, it is shown how a PPR
was triggered on an epilepsy diagnosed subject right after
the photic stimulation at a frequency rate of 30Hz started.
Each stimulation starting point is indicated by the purple
labels at the top of the plots. As artefacts, we can see the
blink electropositve deﬂexion in both frontopolar regions
and some muscular contraction activity, showed as fast
frequencies burst that appears darker in the recording.
Feedback from this stage of the study has been used to
reﬁne the software and accommodate it for clinical use at
the hospital.
In this research it is shown that no differences have been
found between the EEG responses recorded when using the
conventional IPS procedure or the proposed VR-IPS
Fig. 12 Position of the 19 scalp electrodes used to record EEG signals
according to the international 10–20 system of electrode placement as
deﬁned by the international federation of EEG societies
Neural Computing and Applications (2023) 35:5643–5659 5653
123

procedure, suggesting that they are completely comparable.
This assertion is based on the evidence that a clinical
neurophysiologist cannot tell the difference between two
EEG recordings, one registered while submitting the sub-
ject to the conventional IPS procedure, and the other one
obtained while submitting the same subject to the new VR-
IPS procedure.
At this point, testing VR-Photosense among diagnosed
subjects is crucial to advance on this study. At the time of
writing this paper, the research team has the approval of the
ethics committee from Burgos University Hospital to
conduct a trial on several subjects who suffer from pho-
tosensitivity, which will allow us to measure the
Fig. 13 Photic-driving response identiﬁed on a healthy subject using VR-Photosense at the ﬂash frequency 10 Hz
Fig. 14 PPR response identiﬁed on a previously diagnosed subject using VR-Photosense at the ﬂash frequency 30 Hz
5654 Neural Computing and Applications (2023) 35:5643–5659
123

performance of VR-Photosense to detect photoparoxysmal
responses.
4.2 Performance of the ML-based PPR detection
Two different stages conform the measurement of the
performance of the PPR detection: the evaluation of the
2C-KNN and the evaluation of the 1C-KNN. In this way, it
would be possible to determine whether any of the classi-
ﬁers needs improvements or if the whole system is able to
detect the PPR.
For the evaluation of the 2C-KNN, Table 3 includes the
mean (MN), median (MDN) and standard deviation (STD)
of the ACC, SEN and SPE for each case and for the best
parameter K found in the leave-one-participant-out tenfold
cross-validation of the corresponding HRData.
For the evaluation of the 1C-KNN, Table 2 includes the
mean (MN), median (MDN) and standard deviation (STD)
of the ACC, SEN and SPE for each subject and ﬂashing
frequency, and for the best parameter K found. In this case,
the cut frequency ( fc) started at 1 Hz to evaluate all pos-
sible ﬂashing stimulation frequencies. Then the 1C-KNN is
trained, and the next frequency data is labelled as anoma-
lies or not. Finally the fc is increased in order to repeat the
process with the next frequency data.
In both tables, two different sub-tables are shown: the
upper one corresponding to the performance of each clas-
siﬁer when taking into account all types of PPR; the lower
one corresponding to the case where only Type-4 PPR are
considered.
As can be seen, the detection results are better in the
case where only Type-4 PPR are considered by both
classiﬁers, as might be expected since our method was
Table 2 Results of the anomaly detection performance for all PPR
types (upper) and only for Type-4 PPR ( lower) in channel Fz of the
1C-KNN classiﬁer with K=15 neighbours. Mn = Mean. Mdn =
Median. StD = Standard Deviation. *Since subjects from P5 to P9 do
not have any Type-4 PPR, their results are not highlighted
Pi Acc Sens Spec F1
Mn Mdn StD Mn Mdn StD Mn Mdn StD Mn Mdn StD
P1 0.9549 0.9732 0.0552 0.4485 0.3158 0.4083 0.9843 0.9924 0.0195 0.2416 0.0000 0.3676
P2 0.9777 1.0000 0.0304 0.1506 0.0000 0.2471 0.9984 1.0000 0.0067 0.1845 0.0000 0.2920
P3 0.9448 0.9457 0.0312 0.3966 0.4182 0.3110 0.9928 0.9979 0.0101 0.4467 0.4933 0.3118
P4 0.9760 0.9882 0.0280 0.6722 0.7273 0.3420 0.9853 1.0000 0.0234 0.5009 0.5333 0.3169
P5 0.9938 1.0000 0.0152 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P6 0.9924 1.0000 0.0304 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P7 0.9902 1.0000 0.0205 0.0000 0.0000 0.0000 0.9989 1.0000 0.0044 0.0000 0.0000 0.0000
P8 0.9876 1.0000 0.0254 0.0278 0.0000 0.0481 0.9996 1.0000 0.0015 0.0455 0.0000 0.0787
P9 0.9733 0.9941 0.0306 0.0000 0.0000 0.0000 0.9982 1.0000 0.0040 0.0000 0.0000 0.0000
P10 0.9415 0.9532 0.0579 0.5859 0.7143 0.3368 0.9774 0.9773 0.0224 0.4794 0.6277 0.3868
Mn 0.9732 0.9854 0.0325 0.2282 0.2176 0.1693 0.9935 0.9968 0.0092 0.1899 0.1654 0.1754
Mdn 0.9768 0.9971 0.0304 0.0892 0.0000 0.1476 0.9983 1.0000 0.0055 0.1150 0.0000 0.1854
StD 0.0157 0.0168 0.0096 0.2381 0.2611 0.1597 0.0068 0.0048 0.0077 0.1818 0.2316 0.1596
P
1 0.9645 0.9728 0.0369 0.4357 0.4168 0.3238 0.9864 0.9936 0.0155 0.2340 0.0000 0.3469
P2 0.9947 1.0000 0.0108 0.7102 0.8295 0.3179 0.9974 1.0000 0.0061 0.5643 0.7619 0.3722
P3 0.9607 0.9628 0.0218 0.6582 0.6750 0.1604 0.9883 0.9892 0.0100 0.7071 0.7000 0.1075
P4 0.9871 1.0000 0.0193 0.5669 0.5694 0.0965 0.9941 1.0000 0.0098 0.4795 0.5455 0.2473
P5* 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P6* 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P7* 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P8* 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P9* 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000 1.0000 1.0000 0.0000 0.0000 0.0000 0.0000
P10 0.9375 0.9588 0.0750 0.5503 0.5417 0.2769 0.9753 0.9883 0.0310 0.3423 0.0000 0.3826
Mn 0.9844 0.9894 0.0164 0.2921 0.3032 0.1176 0.9942 0.9971 0.0072 0.2327 0.2007 0.1456
Mdn 0.9973 1.0000 0.0054 0.2178 0.2084 0.0483 0.9987 1.0000 0.0030 0.1170 0.0000 0.0538
StD 0.0181 0.0148 0.0175 0.2921 0.3032 0.1218 0.0065 0.0040 0.0075 0.2327 0.2810 0.1533
Neural Computing and Applications (2023) 35:5643–5659 5655
123

designed to focus only on the detection of this type of PPR.
However, there is still room for further improvements.
The results of the 1C-KNN classiﬁer, computed with the
best value found for the parameter K, i.e. K = 15 neigh-
bours, are shown in Table 2. The ﬁrst thing to note is that
the results for subjects 5 to 9 expose ACC and SPEC values
equal to or very close to 1 while SENS is equal to 0. The
reason for this is because those subjects did not show any
Type-4 PPR throughout their recordings. All other patients
presented at least one Type-4 PPR among all the PPR
triggered during their sessions.
Despite the fact that ﬁgures in Table 2 are not impres-
sive, the results obtained for the speciﬁc Type-4 PPR
detection are slightly better than those obtained if all the
PPR types are considered but only for some subjects; for
two of them the 1C-KNN decreased its performance. This
might be due to the fact that some PPR are not pure Type-4
PPR, making their detection even more challenging.
Besides, the behaviour of the 1C-KNN obtained only for
the Type-4 PPR performed perfectly for those patients that
did not include any Type-4 PPR; furthermore, the perfor-
mance considering the ACC and the SPEC are really high.
In terms of the results of the 2C-KNN classiﬁer shown
in Table 3, the same comments can be repeated. In this
case, one of the main reasons of the poor performance
could be the high HRData data imbalance, forcing to
introduce high rates of oversampling for the minority class
while severely undersampling the majority class when
using SMOTE. As a consequence, the outcome of the
SMOTE might not represent the variability of the initial
space, penalizing the overall results.
This study proposes several features to represent the
EEG TS; the obtained results may suggest these features
are not so representative and that a more complete study on
possible transformations is needed. Moreover, a feature
extraction stage would be required where introducing more
features to avoid the difﬁculties of ﬁnding an ideal feature
subset.
Additionally, the performance of KNN—either one class
or two classes—may suggest to introduce more complex
ML methods, such as random forests. However, due to the
limited size of the data set available for this study,
advanced ML methods were not used. Provided more data
is made available, these methods must be contemplated as
robust alternatives.
Undoubtedly, the experimentation and the results shown
in this study represent a very ﬁrst step in this research; it
must be considered as a proof of concept. This is due to
two main reasons: On the one hand, the fact that only ten
patients have been studied so far suggests that much more
patients must be analysed to conclude that the VR-IPS is
totally equivalent to the conventional IPS; however, if so,
the potential of VR will easily surpass the old procedures,
introducing new medical research lines. On the other hand,
the limited amount of data and its unbalanced nature rep-
resents a challenge for ML; obtaining accurate models
certainly requires a higher amount of data, so evaluation
methods using either leave-one-participant-out or K-par-
ticipants fold cross-validations schemes become feasible
and credible. Nonetheless, what it is clear from the
experiments and the obtained results is that VR-IPS rep-
resents very promising research that can potentially be
spread to many other different areas, such as Alzheimer
disease evaluation.
There are several improvements that can be introduced
to the ML model. First, a more in-depth analysis of a wider
set of transformations from different domains must be
done, such as temporal energy, statistical properties or
spectral measures. Afterwards, unsupervised learning could
show some relationships between these features and the
labels, showing some more promising transformation.
Furthermore, feature extraction—either principal compo-
nent analysis or locally linear embeddings—must be
applied to reduce the feature subset. With these new set of
features, different models can be studied, such as random
forests, support vector machines or perhaps the KNN can
proof good performance. In any case, the models must be
valid to deal with this type of one-class and two-class
problems in highly unbalanced problems. Besides, data
augmentation techniques can also be employed to increase
the number of available experiments. In case enough data
are gathered from the experiments currently being carried
out at Burgos University Hospital, deep learning—auto-
encoders plus dense layers or TS classiﬁcation using, for
instance, long short-term memory networks—and/or
XGBoost could also be applied in combination with dif-
ferent techniques such as High Frequency Oscillations.
5 Conclusions
For this study, our research team has developed a novel and
low-cost VR system that mimics and updates the conven-
tional intermittent photic stimulation (IPS) systems. It is
cross-platform and can be used with multiple types of VR
devices. It can also be used in any professional environ-
ment and with any type of EEG recording device, as VR-
Photosense is independent from the type of EEG headset
being used.
Our VR-IPS stimulation has proofed effectiveness to
identify photic-driving responses on healthy subjects as
well as PPR on photosensitive previously diagnosed sub-
jects during the initial testing. We are currently extending
this work to conduct a clinical trial on a large number of
patients.
5656 Neural Computing and Applications (2023) 35:5643–5659
123

We also proposed a ML-based PPR detection procedure
that extracts six standardized features ( Cumulative First
Derivative, Cumulative Second Derivative, Number of
Relevant Peaks, Sum of Absolute Values, Maximum Dif-
ferences, Average Energy ) from the EEG windows and
then sequentially applies two different versions of the
K-nearest neighbours algorithm: the ﬁrst one is an unsu-
pervised one-class KNN classiﬁer (1C-KNN) that detects
anomalous activity in the EEG window; the second one is a
supervised two-class KNN classiﬁer (2C-KNN) that deci-
des if the previously detected anomalous windows belong
to PPR activity or not. This technique is designed to target
only the detection of Type-4 PPR, as they represent a more
dangerous photosensitivity state than the other types.
Despite the ML results, which were not as high as
expected, the proposal can be considered a good proof of
concept in terms that, with more research, a robust and
resilience method for detecting PPR with VR ?ML would
be possible. However, due to the lack of large and good
EEG data sets this has not yet been possible, although at
Burgos University Hospital are working on gathering new
data from subjects.
From the operational point of view, the learning curve of
the new VR IPS is similar to the one of the conventional
IPS, according to the feedback comments provided by the
physicians of the neurophysiology department at Burgos
University Hospital who have been using the new system
so far, when compared to the conventional IPS they use
every day named Natus Nicolet V44.
Furthermore, more alternatives can be followed con-
cerning the ML solution. Introducing more complex ML
methods such as random forests, feature extraction tech-
niques such as principal component analysis or locally
linear embedding or deep learning solutions, when the
Table 3 Results of the leave-one-out cross-validation of PPR detection performance for all PPR types ( upper) and only for Type-4 PPR ( lower)
in channel Fz of the 2C-KNN classiﬁer with K=21 neighbours. Mn = Mean. Mdn = Median. StD = standard deviation
Acc Sens Spec F1
Foldi Mn Mdn StD Mn Mdn StD Mn Mdn StD Mn Mdn StD
F1 0.9660 0.9838 0.0342 0.4602 0.5385 0.3318 0.9768 0.9901 0.0295 0.3360 0.3963 0.2482
F2 0.9703 0.9746 0.0278 0.4826 0.6226 0.3562 0.9831 0.9921 0.0265 0.4193 0.4560 0.3197
F3 0.9687 0.9762 0.0311 0.4622 0.4848 0.3430 0.9805 0.9940 0.0319 0.3733 0.4237 0.2235
F4 0.9672 0.9833 0.0330 0.3937 0.5385 0.3365 0.9805 0.9942 0.0280 0.2886 0.3162 0.2594
F5 0.9560 0.9716 0.0373 0.3702 0.3927 0.3078 0.9722 0.9885 0.0298 0.2888 0.3207 0.2247
P6 0.9625 0.9781 0.0350 0.4121 0.4251 0.3506 0.9772 0.9915 0.0310 0.3279 0.3386 0.2661
F7 0.9650 0.9794 0.0313 0.5038 0.6216 0.3542 0.9802 0.9890 0.0259 0.3857 0.4118 0.2311
F8 0.9660 0.9786 0.0307 0.4748 0.5007 0.3577 0.9807 0.9936 0.0256 0.3924 0.4291 0.2487
F9 0.9685 0.9839 0.0306 0.4934 0.5423 0.2881 0.9815 0.9944 0.0240 0.3992 0.4314 0.1997
F10 0.9652 0.9757 0.0268 0.4073 0.3651 0.3121 0.9778 0.9862 0.0225 0.2554 0.2972 0.1737
Mn 0.9655 0.9785 0.0318 0.4460 0.5032 0.3338 0.9790 0.9914 0.0275 0.3467 0.3821 0.2395
Mdn 0.9660 0.9783 0.0312 0.4612 0.5196 0.3397 0.9803 0.9918 0.0273 0.3547 0.4041 0.2397
StD 0.0027 0.0033 0.0025 0.0401 0.0695 0.0191 0.0024 0.0023 0.0026 0.0473 0.0511 0.0289
Fold
i Mn Mdn StD Mn Mdn StD Mn Mdn StD Mn Mdn StD
F1 0.9575 0.9562 0.0203 0.6580 0.6250 0.2532 0.9675 0.9708 0.0186 0.1726 0.0000 0.2164
F2 0.9551 0.9587 0.0236 0.4866 0.4731 0.2763 0.9676 0.9718 0.0240 0.1816 0.0000 0.2293
F3 0.9567 0.9564 0.0167 0.6004 0.7188 0.3280 0.9675 0.9663 0.0150 0.1735 0.0658 0.1971
F4 0.9527 0.9551 0.0212 0.4786 0.4097 0.3080 0.9652 0.9619 0.0197 0.1445 0.0000 0.1952
F5 0.9535 0.9527 0.0188 0.5718 0.5396 0.3431 0.9678 0.9665 0.0156 0.1933 0.1175 0.1989
F6 0.9576 0.9577 0.0164 0.6385 0.6816 0.3282 0.9700 0.9663 0.0127 0.2250 0.2038 0.2146
F7 0.9541 0.9543 0.0207 0.6063 0.5932 0.3426 0.9674 0.9670 0.0173 0.2242 0.2165 0.2116
F8 0.9557 0.9549 0.0195 0.6118 0.6138 0.3337 0.9689 0.9709 0.0166 0.2197 0.2371 0.2028
F9 0.9529 0.9501 0.0180 0.6162 0.6217 0.3471 0.9659 0.9632 0.0157 0.2200 0.2105 0.2099
F10 0.9642 0.9654 0.0187 0.5662 0.5397 0.3570 0.9712 0.9731 0.0177 0.1494 0.0000 0.1883
Mn 0.9560 0.9561 0.0194 0.5834 0.5816 0.3217 0.9679 0.9678 0.0173 0.1904 0.1051 0.2064
Mdn 0.9554 0.9556 0.0191 0.6033 0.6035 0.3310 0.9676 0.9667 0.0170 0.1874 0.0916 0.2063
StD 0.0024 0.0027 0.0017 0.0461 0.0729 0.0255 0.0013 0.0031 0.0022 0.0261 0.0920 0.0100
Neural Computing and Applications (2023) 35:5643–5659 5657
123

amount of available data allows us to do so, such as auto-
encoders plus dense layers or long short-term memory
networks. All of these improvements represents future
research work.
Acknowledgements This research has been funded by the Spanish
Ministry of Science and Innovation under project MINECO-
TIN2017-84804-R, PID2020-112726RB-I00 and the State Research
Agency (AEI, Spain) under grant agreement No RED2018-102312-T
(IA-Biomed). Additionally, by the Council of Gijo ´n through the
University Institute of Industrial Technology of Asturias grant SV-21-
GIJON-1-19.
Funding Open Access funding provided thanks to the CRUE-CSIC
agreement with Springer Nature.
Conflict of interest The authors declare that they have no conflict of
interest.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit http://creativecommons.
org/licenses/by/4.0/.
References
1. A´ lvarez A, Trivin˜o G, Cordo´n O (2011) Body posture recognition
by means of a genetic fuzzy ﬁnite state machine. In: IEEE 5th
international workshop on genetic and evolutionary fuzzy sys-
tems (GEFs), pp 60–65
2. Beniczky S, Aurlien H, Franceschetti S, da Silva AM, Bisulli F,
Bentes C, Canafoglia L, Ferri L, Kry ´sl D, Peralta AR, Ra´cz A,
Cross JH, Arzimanoglou A (2020) Interrater agreement of clas-
siﬁcation of photoparoxysmal electroencephalographic response.
Epilepsia. https://doi.org/10.1111/epi.16655
3. Beniczky S, Conradsen I, Henning O, Fabricius M, Wolf P (2018)
Automated real-time detection of tonic-clonic seizures using a
wearable EMG device. Neurology. https://doi.org/10.1212/WNL.
0000000000004893
4. Brooks AL, Brahman S, Kapralos B, Nakajima A, Tyerman J,
Jain LC (2021) Recent advances in technologies for inclusive
well-being. Virtual patients, gamiﬁcation and simulation. Intel-
ligent systems reference library series, 196, 1 edn. Springer
5. Chakrabarti S, Swetapadma A, Pattnaik PK (2021) A channel
independent generalized seizure detection method for pediatric
epileptic seizures. Comput Methods Programs Biomed. https://
doi.org/10.1016/j.cmpb.2021.106335
6. Choubey H, Pandey A (2021) A combination of statistical
parameters for the detection of epilepsy and eeg classiﬁcation
using ann and knn classiﬁer. Signal Image Video Process. https://
doi.org/10.1007/s11760-020-01767-4
7. Cobb S (1947) Photic driving as a cause of clinical seizures in
epileptic patients. Arch Neurol Psych 58(1):70–71
8. Hall C, Vivanti A, Abbey K (2019) Impact of television on
nutritional intake in communal dining room settings among those
with acquired brain injury a pilot study. Nutrition and dietetics.
J Diet Australia 77(4):444–448. https://doi.org/10.1111/1747-
0080.12526
9. Hoffman BL, Hoffman R, Wessel CB, Shensa A, Woods MS,
Primack BA (2018) Use of ﬁctional medical television in health
sciences education: a systematic review. Adv Health Sci Educ
23(1):201–216. https://doi.org/10.1007/s10459-017-9754-5
10. Jahanbekam A, Baumann J, Nass RD, Bauckhage C, Hill H,
Elger CE, Surges R (2021) Performance of ecg-based seizure
detection algorithms strongly depends on training and test con-
ditions. Epilepsia Open. https://doi.org/10.1002/epi4.12520
11. Jeppesen J, Fuglsang-Frederiksen A, Johansen P, Christensen J,
Wu¨stenhagen S, Tankisi H, Qerama E, Hess A, Beniczky S
(2019) Seizure detection based on heart rate variability using a
wearable electrocardiography device. Epilepsia 60:2105–2113.
https://doi.org/10.1111/epi.16343
12. Khan SS, Ahmad A (2018) Relationship between variants of one-
class nearest neighbours and creating their accurate ensembles.
IEEE Trans Knowl Data Eng 30:1796–1809
13. Kiloh LG (2013) and McComas. Clinical electroencephalogra-
phy. Butterworth-Heinemann, A.J., Osselton, J.W
14. Larsen PM, Wu ¨stenhagen S, Terney D, Gardella E, Alving J,
Aurlien H, Beniczky S (2021) Photoparoxysmal response and its
characteristics in a large eeg database using the score system.
Clin Neurophysiol. https://doi.org/10.1016/j.clinph.2020.10.029
15. Martı´nS ,A´ lvarez V, Garcı´a-Lo´pez B, Gonza´lez VM, Vilar JR
(2021) Vr-photosense: a virtual reality photic stimulation inter-
face for the study of photosensitivity. In: Proceedings of 16th
international conference on soft computing models in industrial
and environmental applications (SOCO 2021) soft computing
models in industrial and environmental applications, pp 178–186.
Springer
16. Michelucci R, Pasini E, Riguzzi P, Andermann E, Ka ¨lvia¨inen R,
Genton P (2016) Myoclonus and seizures in progressive myo-
clonus epilepsies: pharmacology and therapeutic trials. Epilep
Disorder. https://doi.org/10.1684/epd.2016.0861
17. Munroe D, Madden MG (2005) Multi-class and single-class
classiﬁcation approaches to vehicle model recognition from
images. In: Proceedings of AICS-05: Irish conference on artiﬁcial
intelligence and cognitive science, pp 1–10
18. Omidvarnia A, Warren AE, Dalic LJ, Pedersen M, Jackson G
(2021) Automatic detection of generalized paroxysmal fast
activity in interictal eeg using time-frequency analysis. Comput
Biol Med. https://doi.org/10.1016/j.compbiomed.2021.104287
19. Palshikar GK (2009) Simple algorithms for peak detection in
time-series. Technical report, Tata Research Development and
Design Centre
20. Panayiotopoulos CP (2010). A clinical guide to epileptic syn-
dromes and their treatment. https://doi.org/10.1007/978-1-84628-
644-5
21. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B,
Grisel O, Blondel M, Prettenhofer P, Weiss R, Dubourg V,
Vanderplas J, Passos A, Cournapeau D, Brucher M, Perrot M,
Duchesnay E (2011) Scikit-learn: machine learning in Python.
J Mach Learn Res 12:2825–2830
22. Rathore C, Prakash S, Makwana P (2020) Prevalence of pho-
toparoxysmal response in patients with epilepsy: effect of the
underlying syndrome and treatment status. Seizure. https://doi.
org/10.1016/j.seizure.2020.09.006
23. Rubboli G, Parra J, Seri S, Takahashi T, Thomas P (2004) Eeg
diagnostic procedures and special investigations in the assess-
ment of photosensitivity. Epilepsia 45(5):35–39. https://doi.org/
10.1111/j.0013-9580.2004.451002.x
5658 Neural Computing and Applications (2023) 35:5643–5659
123

24. Soriano MC, Niso G, Clements J, Ortı´n S, Carrasco S, Gudı´nM ,
Mirasso CR, Pereda E (2017) Automated detection of epileptic
biomarkers in resting-state interictal meg data. Front Neuroin-
form. https://doi.org/10.3389/fninf.2017.00043
25. Strigaro G, Gori B, Varrasi C, Fleetwood T, Cantello G, Cantello
R (2021) Flash-evoked high-frequency eeg oscillations in pho-
tosensitive epilepsies. Epilep Res. https://doi.org/10.1016/j.eplep
syres.2021.106597
26. Trenite DKN (2019) Photosensitivity and epilepsy. In: Clinical
electroencephalography, pp 487–495. Springer
27. Trenite´ DKN, Rubboli G, Hirsch E, Martins Da Silva A, Seri S,
Wilkins A, Parra J, Covanis A, Elia M, Capovilla G, Stephani U,
Harding G (2012) Methodology of photic stimulation revisited:
updated European algorithm for visual stimulation in the eeg
laboratory. Epilepsia. https://doi.org/10.1111/j.1528-1167.2011.
03319.x
28. Ufongene C, Atrache RE, Loddenkemper T, Meisel C (2020)
Electrocardiographic changes associated with epilepsy beyond
heart rate and their utilization in future seizure detection and
forecasting methods. Clin Neurophysiol. https://doi.org/10.1016/
j.clinph.2020.01.007
29. Vailshery LS (2021) Ar/vr headset shipments worldwide
2020–2025. https://www.statista.com/statistics/653390/world
wide-virtual-and-augmented-reality-headset-shipments/
30. Vanabelle P, Handschutter PD, Tahry RE, Benjelloun M,
Boukhebouze M (2020) Epileptic seizure detection using eeg
signals and extreme gradient boosting. J Biomed Res. https://doi.
org/10.7555/JBR.33.20190016
31. Waltz S, Christen HJ, Doose H (1992) The different patterns of
the photoparoxysmal response—a genetic study. Electroen-
cephalogr Clin Neurophysiol 83(2):138–145. https://doi.org/10.
1016/0013-4694(92)90027-F. https://www.sciencedirect.com/sci
ence/article/pii/001346949290027F
32. Wang L, Long X, Arends JB, Aarts RM (2017) Eeg analysis of
seizure patterns using visibility graphs for detection of general-
ized seizures. J Neurosci Method. https://doi.org/10.1016/j.jneu
meth.2017.07.013
33. Wang S, Yang J, Chen N, Chen X, Zhang Q (2005) Human
activity recognition with user-free accelerometers in the sensor
networks. In: Proceedings of international conference on neural
networks and brain ICNN&B’05, pp 1212–1217
34. Wolf P, Goosses R (1986) Relation of photosensitivity to
epileptic syndromes. J Neurol Neurosurg Psych. https://doi.org/
10.1136/jnnp.49.12.1386
35. Yang Y, Truong N, Maher C, Kavehei O, Truong ND, Eshraghian
JK, Nikpour A (2021) A multimodal ai system for out-of-distri-
bution generalization of seizure detection. bioXRiv. https://doi.
org/10.1101/2021.07.02.450974
36. Zibrandtsen IC, Kidmose P, Kjaer TW (2018) Detection of
generalized tonic-clonic seizures from ear-eeg based on emg
analysis. Seizure. https://doi.org/10.1016/j.seizure.2018.05.001
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2023) 35:5643–5659 5659
123