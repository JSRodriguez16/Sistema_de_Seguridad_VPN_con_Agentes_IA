IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025 2225
VPN-Encrypted Network Traffic Classification
Using a Time-Series Approach
Jaidip Kotak , Idan Yankelev , Idan Bibi, Yuval Elovici , and Asaf Shabtai
Abstract—Networktrafficclassificationprovidesvaluetoorga- applications or the type of applications, by analyzing the
nizationsandInternetserviceproviders(ISPs).Theidentification packets. This capability is extremely important for organi-
of applications or services from network traffic enables orga-
zations and network service providers, since it (1) provides
nizations to better manage their business, and ISPs to offer
effective security (e.g., detecting anomalous traffic or applica-
services to their users. Given the vast quantity of traffic flowing
in and out of organizations, it is impractical to write manual tion behavior), and (2) guarantees network quality-of-service
signatures for traffic identification. The effectiveness of machine (QoS) for specific applications (e.g., video streaming).
learning (ML) in the identification of applications or services The main challenges faced when performing NTC are:
fromnetworktraffichasbeendemonstrated.Evenwhennetwork
(1)thelargevolumeofnetworktraffic,(2)theevolvingnature
trafficisencrypted,MLalgorithmsachievehighaccuracyinthe
of network traffic patterns due to user behavior and changes
task of traffic identification based on statistical information and
thepackets’headersandpayloads.However,existingapproaches in applications’ functionality, and (3) the use of technologies
were shown to be ineffective for VPN-encrypted network traffic. like network address translation (NAT), internal proxies, and
Inthisstudy,weproposeanoveltime-seriesbasedapproachfor VPNs.
theidentificationoftraffic/sourceapplicationsonVPN-encrypted
Thetwoexistingnetworktrafficclassificationapproaches—
traffic. We also demonstrate the broad applicability of our
feature-based and rule-based methods (statistical and
proposed approach by evaluating its effectiveness on non-VPN
traffic that is encrypted, and on IoT traffic. behavioral)—are not directly applicable to VPN-encrypted
traffic. The limitation of the feature-based approach is based
Index Terms—Network traffic classification, virtual private
on the network flow, from which it identifies the right
networks (VPN), machine learning, encrypted traffic and cyber-
security. features and preprocesses them for the machine learning
(ML) model [11], [12]; it is not possible to segregate
different network flows in VPN-encrypted traffic, as all of
I. INTRODUCTION the traffic is within a single VPN-encrypted tunnel and is
thereforeasinglenetworkflow.Therule-basedapproachrelies
AMONG other changes in the past decade, today’s work-
mainly on the port number and the header fields of network
from-home culture has played a role in shifting people
communication [13], [14]. However, as mentioned, in VPN-
to online platforms, which has led to a dramatic increase in
encrypted traffic there is a single network flow and the header
the amount of Internet traffic. The number of Internet users
informationisnotvisibleduetotheencryptionprovidedbythe
worldwide is currently around 4.9 billion; this means that
VPN. Therefore, these approaches are not directly applicable
almost two-thirds of the world’s population is connected to
to VPN-encrypted network traffic classification (V-NTC).
the Internet [1].
Our Method: We propose a method for V-NTC, which is
Duetoonlineprivacycampaignsandgrowingconcernfrom
based on the sliding window of a time series. In this method,
advertisers,Internetserviceproviders(ISPs),andgovernments
features from the packets are derived every second, and the
regarding the disruption, manipulation, and monitoring of
features of m seconds are appended to form a single training
Internet traffic, users’ awareness of privacy issues associated
or testing instance, where m is the window length. Then, to
with Internet use has grown [2], [3], [4], [5], [6], [7]. To
form the next data instance, we slide by one second (i.e., 2
preserve privacy, circumvent censorship, and access geo-
to m+1 seconds) and construct a second data instance. The
filteredcontent,manyusersusevirtualprivatenetwork(VPN)
InceptionTimemodel[15]wasusedtoclassifythetime-series
technology [8], [9], [10].
based instances.
Given the increased volume of network traffic, there is
Evaluation: Initially, we planned to use the publicly
a need for service providers and organizations to perform
available VPN traffic dataset – ISCXVPN2016 [16] –
automatic network traffic classification (NTC) to infer the
to evaluate the proposed method for VPN-encrypted traf-
Received 25 December 2023; revised 12 August 2024 and 22 November fic classification. However, since we found a discrepancy
2024; accepted 23 January 2025. Date of publication 20 February 2025; in this dataset (described in detail in Section II-B),
date of current version 22 April 2025. The associate editor coordinating
we formed our own dataset that includes traffic from
the review of this article and approving it for publication was Y. Diao.
(Correspondingauthor:JaidipKotak.) three geographical locations. This dataset is available
TheauthorsarewiththeDepartmentofSoftwareandInformationSystems at https://zenodo.org/records/13301379. We evaluated our
Engineering,Ben-GurionUniversityoftheNegev,Be’erSheva84105,Israel
approachontheentiredatasetandforeachgeographicalloca-
(e-mail:jaidip@post.bgu.ac.il).
DigitalObjectIdentifier10.1109/TNSM.2025.3543903 tion, on both the classification task at the category level (e.g.,
1932-4537(cid:2)c 2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligence
andsimilartechnologies. Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

2226 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
streaming, chat), and the application level (e.g., YouTube, for their application’s communication. Even DPI tools are
Vimeo). An accuracy of 93-95% was obtained for category- irrelevant,asmostofthetrafficisencryptedorVPN-encrypted
level classification for each location and for the combined these days.
traffic from all three locations. Accuracy ranging from 84% Due to the lack of privacy, technologies such as NAT,
to 91% was obtained for application-level classification for internal proxies, and VPNs were established to allow compa-
each location and when combining the traffic from all three nies, organizations, and individuals to use a network without
locations.Todemonstrateourmethod’sgenericnatureonnon- revealing any identifying data; as a result, new methods
VPNtraffic,weevaluateditontheISCXVPN2016datasetand capable of performing encrypted NTC with high accuracy
a subset of the IoTTrace [17] dataset. withoutcompromisingusers’privacyareneeded.Advancesin
Contribution: The contributions of our research are as the field led to the development of novel approaches based
follows: on network traffic flow features, well suited to the data’s
(cid:129) To the best of our knowledge, we are the first to classify encrypted nature, as well as the use of deep neural network
and identify VPN-encrypted traffic using a time-series methods which allow the computer to find its own weights in
approach. order to correctly classify the traffic classes.
(cid:129) The proposed approach is generic in nature, i.e., it is In [28], the authors proposed a framework that employs a
applicabletoVPN-encryptedtraffic,non-VPNtraffic,and stacked autoencoder (SAE) and convolution neural network
IoT device type classification, as demonstrated in our (CNN)toclassifynetworktraffic.Totraintheneuralnetworks,
evaluation on different datasets. they performed a preprocessing phase in which the Ethernet
(cid:129) The proposed approach can be used on network traffic header and uniformed protocol header length were removed,
originating from different geographical locations (using and the packets’ bits were transformed to bytes; afterward,
a VPN). they filtered out all non-application data-related packets, such
(cid:129) We created a dataset of VPN-encrypted and non-VPN as packets with ACK/SYN/FIN flags or DNS queries. The
traffic from three different geographical locations which framework achieved 98% accuracy in the application identifi-
contains more unique applications than existing datasets cation task and 93% in the traffic categorization task by using
and will make this dataset available to the research theCNNnetworkastheclassificationmodel.Similarworkhas
community. been performed by [30], [31], [34], [39], [41] and [40] who
The remainder of this paper is organized as follows. utilized payload and other header information, applying deep
Section II reviews the related work on VPN traffic clas- learning models like a CNN, 1D-CNN & bidirectional gated
sification and the existing public VPN dataset. Section III recurrent unit (BiGRU), bidirectional encoder representation
describes the characteristics of the VPN-encrypted traffic Transformer (BERT) & CNN, three-layer multilayer percep-
dataset, the network setup during data generation, and the tion (MLP), CNN, and ensemble long short-term memory
data generation process. Section IV outlines the methods (LSTM),respectively,andachievingresultsinasimilarrange.
used, including data preprocessing, feature construction, and However,themajorlimitationoftheseapproaches isthatthey
the classification model. Section V presents the experiments rely on the presence of clear text information in encrypted
conducted and their results. Section VI discusses the findings, traffic, particularly with the TLS protocol, where initial nego-
limitations, and potential areas for future research. Finally, tiationhappensincleartext.InrealVPNtraffic,however,this
Section VII concludes the paper by summarizing our findings information is encrypted and hidden within the VPN tunnel,
and contributions. making these methods bound to fail.
In addition to deep learning models, several studies have
leveraged machine learning algorithms for classifying VPN
II. RELATEDWORK
and non-VPN network traffic. For instance, [32] proposed a
A. Network Traffic Classification
method that utilized time-related statistical features generated
In the past, network traffic detection was performed based by ISCXFlowMeter/CICFlowMeter, such as flow duration,
on the port numbers used in network communication. The flow bytes per second, max active time, max biat (backward
same port numbers were used by all the applications that inter-arrival time), max flowiat (flow inter-arrival time), mean
were communicating on the same protocol [18]. Therefore, biat, min active time, min biat, and std active time (standard
it was easy to identify the network traffic, as mentioned deviation of active time). These features were then used to
in [19], [20], [21]. Later, payload-based deep packet inspec- train a RF model, achieving over 95% accuracy for category-
tion (DPI) tools such as PACE, OpenDPI, L7-filter, nDPI and level VPN traffic classification.
Cisco’s NBAR were used to extract features from packets’ ISCXFlowMeter/CICFlowMeter is a network traffic flow
payloads; and then, simple ML models (such as decision tree generator and analyzer that processes packet capture (PCAP)
(DT), random forest (RF), and k-nearest neighbors (KNN)) files to generate bidirectional flows. Each flow is identified
capable of bifurcating between the different traffic groups and basedonthedirectionofthefirstpacket(sourcetodestination
classifying the packets based on the features were used, as or destination to source) and enriched with over 80 statistical
mentioned in [22], [23], [24], [25], [26], [27]. features, including flow duration, packet counts, byte counts,
However, as the Internet evolved, the above-mentioned and packet lengths for both forward and backward directions.
methods have become obsolete, since most developers today These features are frequently used in network traffic classi-
do not follow a specific standard in selecting the port number fication tasks, enabling the detection and differentiation of
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2227
TABLEI
SUMMARYOFENCRYPTEDTRAFFICCLASSIFICATIONAPPROACHES
varioustraffictypes.However,itisimportanttonotethatthese flows, which limits their applicability to real-world VPN
features rely on the ability to aggregate the packets by flows. scenarios where this assumption does not hold true.
Thisdependencymakessuchmethodsunsuitablewithdatasets In contrast, Vu et al., [29] developed a time-series feature
where multiple flows are encapsulated within a VPN tunnel, extraction method consisting of a feature engineering method,
appearing as a single flow. which is used to extract significant attributes of the encrypted
Similarly,studieslike[35]and[37]haveemployedfeatures network traffic behavior by analyzing the time series of
derived from ISCXFlowMeter with machine learning mod- receiving packets, and a deep learning-based method which
els such as neural networks (NN), support vector machines is used to exploit the correlation of time-series data samples
(SVM), and boosting algorithms (e.g., XGBoost, LightGBM, of the encrypted network applications. The authors used the
AdaBoost), achieving comparable results. newlygeneratedtime-seriesfeaturestotrainamodelbasedon
The limitation of such studies is that ISCXFlowMeter/ theLSTMrecurrentneuralnetworktolearnthefeaturesinthe
CICFlowmeter assume that traffic can be segmented into flow time-seriessamples.Themethod’sperformancesurpassedthat
records using 5-tuple values (source IP, destination IP, source of methods proposed in prior studies, obtaining an accuracy
port,destinationport,andprotocol).However,thisassumption of 98.17% while reducing the number of features used to
does not hold truefor realVPN traffic, where traffic flows are 55; in contrast, 1,500 features were required in the model
often merged and encrypted in the VPN tunnel. As a result, proposedin[28].Themethodwasprimarilytestedoncategory
these methods are not directly applicable to real VPN traffic classification instead of application classification.
scenarios. Table I summarizes recent work on encrypted network
Additionally, studies such as [33] and [36] utilized only traffic classification. It highlights that most studies utilize the
the packet sizes and inter-arrival times for classification, ISCXVPN2016 dataset, which contains known discrepancies.
employing LSTM & ordinary differential equation networks Additionally, many approaches either assume that traffic can
(ODENet)andadversarialauto-encoder(AAE)&deepsupport be segmented into multiple flows or rely on application
vectordatadescription(DSVDD),respectively.However,these payload content, neither of which is applicable to real VPN
approaches assume that traffic can be neatly segmented into traffic scenarios.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

2228 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
TABLEII
CHARACTERISTICSOFOURDATASET
B. Publicly Available Network Traffic Dataset was collected using one VPN client, which was configured
In most prior works, the ISCXVPN2016 dataset (VPN- forthreegeographicallocations(Canada,England,andJapan).
|                 |          |     |           |                |     |                   |             | The characteristics |     | of        | our dataset | are   | presented | in        | Table II. |
| --------------- | -------- | --- | --------- | -------------- | --- | ----------------- | ----------- | ------------------- | --- | --------- | ----------- | ----- | --------- | --------- | --------- |
| nonVPN          | dataset) | was | used      | to demonstrate |     | the effectiveness |             |                     |     |           |             |       |           |           |           |
|                 |          |     |           |                |     |                   |             | The categories      |     | are based | on          | those | used in   | [16] with | some      |
| of the proposed |          | NTC | and V-NTC | approaches     |     | [42],             | [43], [44], |                     |     |           |             |       |           |           |           |
[45], [46], [47]. However, on taking a more in-depth look exceptions (like P2P, Web browsing).
| at the content |     | of the | dataset’s | files, | we made | the | following |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | --------- | ------ | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
observations:
|     |     |     |     |     |     |     |     | A. Dataset | Characteristics |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- |
(cid:129) InsomePCAPfiles,thecontentofthepacketsisinclear
|     |     |     |     |     |     |     |     | The three | geographical |     | locations | (Europe, |     | North America, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --------- | -------- | --- | -------------- | --- |
text.
andAsia)wereusedtoobservetheimpactthatlocationhason
| (cid:129) The | port | numbers | used | are well-known |     | port numbers | for |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------- | ---- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theperformanceofourapproach.Trafficfromeachapplication
| different    |           | services. |            |           |     |            |      |              |     |         |        |          |          |      |       |
| ------------ | --------- | --------- | ---------- | --------- | --- | ---------- | ---- | ------------ | --- | ------- | ------ | -------- | -------- | ---- | ----- |
|              |           |           |            |           |     |            |      | was captured |     | for 1.5 | hours, | thus the | recorded | PCAP | files |
| (cid:129) In | some PCAP |           | files, the | protocols | are | TLS, HTTP, | etc. |              |     |         |        |          |          |      |       |
(+/-
|                   |            |           |        |          |        |             |           | in the dataset   |            | are nearly | uniform |          | 5-10     | minutes).       | The     |
| ----------------- | ---------- | --------- | ------ | -------- | ------ | ----------- | --------- | ---------------- | ---------- | ---------- | ------- | -------- | -------- | --------------- | ------- |
| (cid:129) Certain | structures |           | of the | protocol | (like  | HTML        | pages for |                  |            |            |         |          |          |                 |         |
|                   |            |           |        |          |        |             |           | first difference |            | observed   | in the  | data     | from the | three locations |         |
| the               | HTTP       | protocol) | are    | present  | in the | clear text. |           |                  |            |            |         |          |          |                 |         |
|                   |            |           |        |          |        |             |           | was in           | the amount | of         | traffic | recorded | (in      | GB) for         | a fixed |
(cid:129) OnresolvingtheDNSnamefortheIPaddress,wefound
|      |        |         |         |     |            |               |     | period           | of time | (1.5     | hours). When |         | using a | VPN client | for |
| ---- | ------ | ------- | ------- | --- | ---------- | ------------- | --- | ---------------- | ------- | -------- | ------------ | ------- | ------- | ---------- | --- |
| that | the IP | address | belongs | to  | the server | of well-known |     |                  |         |          |              |         |         |            |     |
|      |        |         |         |     |            |               |     | the geographical |         | location | of           | Canada, | 10 GB   | of traffic | was |
applications.
(cid:129) There are multiple flow records. captured, whereas 7 GB was captured for England, and 8 GB
|               |              |               |           |          |              |                  |         | was captured | for            | Japan. |          |          |            |         |          |
| ------------- | ------------ | ------------- | --------- | -------- | ------------ | ---------------- | ------- | ------------ | -------------- | ------ | -------- | -------- | ---------- | ------- | -------- |
| The above     | observations |               | derived   |          | from the     | VPN-encrypted    |         |              |                |        |          |          |            |         |          |
|               |              |               |           |          |              |                  |         | After        | capturing      | the    | traffic, | the PCAP | files      | were    | cleaned, |
| traffic PCAP  |              | files suggest |           | that the | dataset      | does not         | contain |              |                |        |          |          |            |         |          |
|               |              |               |           |          |              |                  |         | removing     | the background |        | noise,   | and      | segregated | so they | only     |
| VPN-encrypted |              | data          | (see also | A).      | Ideally,     | in VPN-encrypted |         |              |                |        |          |          |            |         |          |
|               |              |               |           |          |              |                  |         | contained    | the traffic    | flow   | from     | the VPN  | tunnel;    | this    | way, the |
| data, we      | would        | see one       | (or       | a few)   | flow records | for              | the VPN |              |                |        |          |          |            |         |          |
datasetcanbeusedinfutureresearchwithouttheneedtoclean
tunnel(s),whichmightnotusewell-knownports.Also,dueto
|                                                          |         |         |             |     |                      |     |          | the files  | again. |     |     |     |     |     |     |
| -------------------------------------------------------- | ------- | ------- | ----------- | --- | -------------------- | --- | -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| the presence                                             | of      | the VPN | tunnel      | in  | real VPN-encrypted   |     | traffic, |            |        |     |     |     |     |     |     |
| network                                                  | traffic | should  | not contain |     | the structure/header |     | of any   |            |        |     |     |     |     |     |     |
| protocol;however,inthisdataset,protocolsaredetectedbased |         |         |             |     |                      |     |          | B. Network | Setup  |     |     |     |     |     |     |
on the structure/header.
|     |     |     |     |     |     |     |     | To produce |     | the dataset, | we  | used | VirtualBox | to  | create a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | ---- | ---------- | --- | -------- |
SincethereisaneedforaVPN-encrypteddatasetonwhich
|            |          |            |             |            |            |             |          | virtual machine |                | on top      | of the        | host computer. |          | Wireshark     | was     |
| ---------- | -------- | ---------- | ----------- | ---------- | ---------- | ----------- | -------- | --------------- | -------------- | ----------- | ------------- | -------------- | -------- | ------------- | ------- |
| NTC and    | V-NTC    | approaches |             | can        | be tested, | to evaluate | the      |                 |                |             |               |                |          |               |         |
|            |          |            |             |            |            |             |          | used on         | both           | the virtual | machine       | and            | the      | host computer | to      |
| method     | proposed | in         | this study, | we         | created    | our own     | dataset, |                 |                |             |               |                |          |               |         |
|            |          |            |             |            |            |             |          | capture         | non-VPN        | and         | VPN-encrypted |                | network  | traffic,      | respec- |
| details of | which    | are        | provided    | in Section | III.       |             |          |                 |                |             |               |                |          |               |         |
|            |          |            |             |            |            |             |          | tively. OpenVPN |                | was         | used on       | the host       | computer | as the        | VPN     |
|            |          |            |             |            |            |             |          | client with     | configurations |             | for three     | different      |          | countries:    | Japan,  |
III. ENCRYPTEDTRAFFICDATASET Canada, and England, i.e., the VPN servers were located in
Inthissection,wedescribethecharacteristicsofourdataset those locations (while the VPN client was located in Israel).
and provide an overview of how it was created. We collected Firefox was used for all of the applications requiring a Web
25GBoflabelednetworktrafficandapproximately76.5hours browser. VPN-encrypted traffic was captured between the
of packet capture from our four categories of traffic (chat, VPN client (host computer) and the VPN server. In addition,
video, file transfer, and video conferencing), containing both non-VPN-encrypted traffic was captured between the virtual
VPN-encrypted and non-VPN-encrypted traffic flows. Data machine and the application layer.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2229
Fig.1. ComparisonofgenericmachinelearningsystemsandVPN-encryptedtrafficclassificationframework.
C. Data Generation
| The dataset    | was       | made           | up of      | traffic      | from each       | application |        |     |     |     |     |     |     |
| -------------- | --------- | -------------- | ---------- | ------------ | --------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| mentioned      | in Table  | II. Wireshark  |            | was          | used to create  | a           | single |     |     |     |     |     |     |
| 1.5 hour       | PCAP      | file for       | each       | application. | The             | traffic     | in     |     |     |     |     |     |     |
| the video      | category, | which          | consists   | of           | Vimeo,          | Netflix,    | and    |     |     |     |     |     |     |
| YouTube,       | was       | produced       | by members |              | of the research |             | team   |     |     |     |     |     |     |
| as they        | watched   | videos         | on each    | platform.    | The             | traffic     | in the |     |     |     |     |     |     |
| chat category, |           | which consists | of         | Skype,       | Facebook,       | Google      |        |     |     |     |     |     |     |
Hangouts, WhatsApp, and Telegram, was created by team Fig.2. Datainstancesconstructionusingslidingwindow.
| members     | as they | chatted            | with one | another   | on each | platform. |            |             |             |     |        |                 |      |
| ----------- | ------- | ------------------ | -------- | --------- | ------- | --------- | ---------- | ----------- | ----------- | --- | ------ | --------------- | ---- |
|             |         |                    |          |           |         |           | source and | destination | IP address, |     | source | and destination | port |
| The traffic | in the  | video conferencing |          | category, | which   | consists  |            |             |             |     |        |                 |      |
of Skype, Google Meet, Zoom, and Microsoft Teams, was number, and packet size of each packet. This process results
generatedbyteammembersastheyparticipatedinconference in a raw feature file for each application.
| calls on | each platform. |     | For the | file transfer | category, |     | which |     |     |     |     |     |     |
| -------- | -------------- | --- | ------- | ------------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- |
consists of WhatsApp, Dropbox, Google Drive, Skype, and B. Feature Construction
Telegram, we uploaded and downloaded files of various sizes Within each feature file, the packets are grouped, per
| on the different |     | applications | and | captured | the traffic. |     |             |              |          |           |        |         |             |
| ---------------- | --- | ------------ | --- | -------- | ------------ | --- | ----------- | ------------ | -------- | --------- | ------ | ------- | ----------- |
|                  |     |              |     |          |              |     | second;     | then the     | features | listed in | Table  | III are | created for |
|                  |     |              |     |          |              |     | each group. | A one-second |          | sliding   | window | is used | to provide  |
IV. METHODS
|     |     |     |     |     |     |     | high granularity | and | capture | real-time | variations |     | in traffic, |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --------- | ---------- | --- | ----------- |
A comparison between a generic machine learning system whichisessentialfortimelydetectionandresponse.Statistical
and our VPN-encrypted traffic classification approach is pro- featureswerealsoincluded,astheywereshowntobeeffective
vided in Fig. 1, which highlights the process flow from data for online network intrusion detection in the paper presenting
capture to output analysis; shows how network traffic is Kitsune [48]. We focus on three primary series of features:
captured, preprocessed, modeled, and analyzed to determine time delta, packet sizes, and accumulated directional packet
application or category probabilities; and aids in network sizes, in addition to some other features. The time delta
device management. The subsections that follow provide series involves the generation of statistical features based on
detailedexplanationsofeachstage:datapreprocessing,feature the time difference ratios between consecutive packets. For
construction, and classification model. the packet sizes series, we create statistical features related
|     |     |     |     |     |     |     | to the size | ratios | between | consecutive | packets. |     | In contrast, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | ----------- | -------- | --- | ------------ |
A. Data Preprocessing the accumulated directional packet sizes series involves the
|      |          |      |         |              |     |                | construction | of statistical | features |     | that account | for | the ratio of |
| ---- | -------- | ---- | ------- | ------------ | --- | -------------- | ------------ | -------------- | -------- | --- | ------------ | --- | ------------ |
| From | the PCAP | file | of each | application, | we  | first filtered |              |                |          |     |              |     |              |
out the single largest flow (by size) which contains the cumulativepacketsizebetweenconsecutivepackets,consider-
ingthedirectionofeachpacket.Thiscomprehensiveapproach
| application’s | VPN-encrypted |          | traffic. | By      | performing | this | step      |                 |              |               |     |           |            |
| ------------- | ------------- | -------- | -------- | ------- | ---------- | ---- | --------- | --------------- | ------------ | ------------- | --- | --------- | ---------- |
|               |               |          |          |         |            |      | ensures   | that we capture | both         | instantaneous |     | and       | cumulative |
| we eliminated | any           | unwanted | traffic  | (noise) | generated  | by   | other     |                 |              |               |     |           |            |
|               |               |          |          |         |            |      | behaviors | in packet       | transmission | (refer        | to  | Algorithm | 1 in the   |
applicationsrunninginthebackground.Thepublisheddataset
|              |     |               |      |     |              |           | Appendix | for the pseudocode). |     |     |     |     |     |
| ------------ | --- | ------------- | ---- | --- | ------------ | --------- | -------- | -------------------- | --- | --- | --- | --- | --- |
| will consist | of  | these cleaned | PCAP |     | files. After | obtaining |          |                      |     |     |     |     |     |
the single VPN-encrypted flow for each application, it was Thenweappliedtheconceptoftheslidingwindow,wherein
Tshark1 a single instance is created by appending n features of m
| processed | using |     | to extract | fields | like the | timestamp, |         |            |        |         |       |         |             |
| --------- | ----- | --- | ---------- | ------ | -------- | ---------- | ------- | ---------- | ------ | ------- | ----- | ------- | ----------- |
|           |       |     |            |        |          |            | seconds | (i.e., the | window | length) | which | results | in a single |
1https://tshark.dev instance with the shape of 1 x n x m (refer Fig. 2 where
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

2230 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
TABLEIII
DETAILEDDESCRIPTIONSOFFEATURES,INCLUDINGTHEIRSERIES,SUB-SERIES,ANDRELEVANCETOVPNTRAFFIC
the window length is five). Table II contains the number Z-score normalization) on the entire dataset, transforming the
of data instances (column Total Instances) after the features data so that it has a mean of zero and a standard deviation
were constructed. We also performed standardization (i.e., of one. Our aim in performing this feature construction
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2231
TABLEIV
SUMMARYOFTHEEXPERIMENTSPERFORMED
| process | was to | convert | the network |     | traffic | data to | time-series |     |     |     |     |     |     |     |     |
| ------- | ------ | ------- | ----------- | --- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
data.
| C. Classification |                | Model     |         |                   |        |                    |            |     |     |     |     |     |     |     |     |
| ----------------- | -------------- | --------- | ------- | ----------------- | ------ | ------------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| For the           | classification |           | of      | the VPN-encrypted |        | network            | traf-      |     |     |     |     |     |     |     |     |
| fic (that         | was            | converted | to      | time-series       | data), | we                 | used the   |     |     |     |     |     |     |     |     |
| InceptionTime     |                | model     | [15].   | This model        | is     | an inception-based |            |     |     |     |     |     |     |     |     |
| network           | [49] that      | applies   | several | convolutions      |        | with               | filters of |     |     |     |     |     |     |     |     |
various lengths. It consists of an ensemble of five different Fig.3. Inceptionnetworkfortime-seriesclassification[49].
| inception    | networks  | that       | are         | initialized | randomly.        |           |              |     |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | ----------- | ----------- | ---------------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Inception    | network   |            | classifiers | contain     | two              | different | residual     |     |     |     |     |     |     |     |     |
| blocks.      | For the   | inception  | network,    |             | each block       | is        | comprised    |     |     |     |     |     |     |     |     |
| of three     | inception | modules    |             | rather      | than traditional |           | fully con-   |     |     |     |     |     |     |     |     |
| volutional   | layers.   | Each       | inception   | module      | applies          |           | convolutions |     |     |     |     |     |     |     |     |
| with lengths | of        | 10, 20,    | and         | 40, with    | a max            | pooling   | operation    |     |     |     |     |     |     |     |     |
| followed     | by a      | bottleneck | layer,      | and         | concatenates     |           | the outputs. |     |     |     |     |     |     |     |     |
Fig.4. Datasplitfor5-foldcross-validationintime-seriesanalysis.
| Each residual | block’s |        | input    | is transferred | via  | a shortcut | linear      |     |     |     |     |     |     |     |     |
| ------------- | ------- | ------ | -------- | -------------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| connection    | so      | it can | be added | to the         | next | block’s    | input, thus |     |     |     |     |     |     |     |     |
mitigatingthevanishinggradientproblembyallowingadirect application, as shown in Fig. 4, for five folds, where 80%
flowofthegradient[50].Thepaddingchosenaimstomaintain
|     |     |     |     |     |     |     |     | of the dataset | was | used | for training, |     | and 20% | was | used for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------------- | --- | ------- | --- | -------- |
the dimensionality of the time series after the convolutions. testing. We divided the training and test set in a sequential
| After the | residual | blocks, |          | a global | average    | pooling | (GAP)    |           |              |            |                 |            |           |      |          |
| --------- | -------- | ------- | -------- | -------- | ---------- | ------- | -------- | --------- | ------------ | ---------- | --------------- | ---------- | --------- | ---- | -------- |
|           |          |         |          |          |            |         |          | manner    | to avoid     | leaking    | any information |            | resulting | from | the      |
| layer is  | employed | which   | averages |          | the output | (in     | the form |           |              |            |                 |            |           |      |          |
|           |          |         |          |          |            |         |          | features’ | construction | (described |                 | in Section | IV-B)     | to   | the test |
of multivariate time series) over the whole time dimension. set. We used a batch size of 64, and training was performed
| The network | is  | comprised | of  | six inception |     | modules | stacked |                |     |         |      |        |            |     |         |
| ----------- | --- | --------- | --- | ------------- | --- | ------- | ------- | -------------- | --- | ------- | ---- | ------ | ---------- | --- | ------- |
|             |     |           |     |               |     |         |         | for 10 epochs. | The | metrics | used | in our | evaluation | are | the F1- |
sequentiallywithineachresidualblock.Eachmoduleincludes score and accuracy. Note that as shown in Table III, feature
abottlenecklayertoreducedimensionality,whichisfollowed
|             |               |     |        |      |           |        |          | numbers | 44-47 will      | not | have any   | impact | in experiments |             | 1-4, |
| ----------- | ------------- | --- | ------ | ---- | --------- | ------ | -------- | ------- | --------------- | --- | ---------- | ------ | -------------- | ----------- | ---- |
| by multiple | convolutional |     | layers | with | different | filter | lengths. |         |                 |     |            |        |                |             |      |
|             |               |     |        |      |           |        |          | because | in VPN traffic, |     | the unique | source | and            | destination | IP   |
Then,afinaltraditionalfullyconnectedsoftmaxlayerisused, and the unique source and destination port will remain the
| with the | number | of  | neurons | equal | to the | number | of classes |             |                   |     |        |     |           |          |      |
| -------- | ------ | --- | ------- | ----- | ------ | ------ | ---------- | ----------- | ----------------- | --- | ------ | --- | --------- | -------- | ---- |
|          |        |     |         |       |        |        |            | same across | all applications. |     | Values |     | for these | features | will |
in the dataset. Fig. 3 depicts the architecture of an inception differinexperiments5-6andthereforewillhaveanimpacton
| network | in which | six | inception | modules | are | stacked | one after |                 |     |       |        |     |     |     |     |
| ------- | -------- | --- | --------- | ------- | --- | ------- | --------- | --------------- | --- | ----- | ------ | --- | --- | --- | --- |
|         |          |     |           |         |     |         |           | the performance | in  | those | cases. |     |     |     |     |
theother.Theinceptionmodulesusemultiplefiltersofvarying
| lengths, | specifically | three    | sets    | of filters | each       | with | lengths of   |             |                       |                |     |            |         |         |     |
| -------- | ------------ | -------- | ------- | ---------- | ---------- | ---- | ------------ | ----------- | --------------------- | -------------- | --- | ---------- | ------- | ------- | --- |
|          |              |          |         |            |            |      |              | Experiments | 1-2:                  | Classification |     | of Network | Traffic | at      | the |
| 10, 20,  | and 40.      | For more | details | about      | the model, |      | please refer |             |                       |                |     |            |         |         |     |
|          |              |          |         |            |            |      |              | Category-   | and Application-Level |                |     | for the    | Entire  | Dataset |     |
to [15].
Inthesetwoexperiments,trafficfromallthreegeographical
|     |     |     |     |     |     |     |     | locations | was combined. |     | In the | first | experiment, | there | were |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------ | ----- | ----------- | ----- | ---- |
V. EXPERIMENTSANDRESULTS
|     |     |     |     |     |     |     |     | four labels, | i.e., four | application |     | categories. | The | classification |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ----------- | --- | ----------- | --- | -------------- | --- |
Table IVprovidesasummaryoftheexperimentsperformed. accuracy and F1-score results are presented in Table V; as
We divided the data into training and test sets for each can be seen, when the length of the sliding window was
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

2232 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
TABLEV
EXPERIMENT1-PERFORMANCEOFDIFFERENTAPPLICATIONSFORCATEGORY-LEVELCLASSIFICATION
WITHASLIDINGWINDOWLENGTHOF60SECONDS
TABLEVI
EXPERIMENT2-PERFORMANCEOFDIFFERENTAPPLICATIONSFORAPPLICATION-LEVELCLASSIFICATION
WITHASLIDINGWINDOWLENGTHOF60SECONDS
Fig.5. Performanceofthemodelstrainedontheentiredatasetforvariousslidingwindowlengths(Y-axis).
60 seconds, the overall accuracy obtained was 93.80%. In the againstthemodel;theresultscanbefoundinTables VandVI.
second experiment, there were 17 labels, i.e., one for each The results for smaller sized sliding windows are presented in
application. The classification accuracy and F1-score results Fig. 5; results for longer sized sliding windows are presented
are presented in Table VI; as can be seen, when the length in Fig. 8 in the Appendix. As can be seen, larger sliding
of the sliding window was 60 seconds, the overall accuracy windows,suchas120seconds,resultinminimalimprovement
obtained was 86.50%. Note that to obtain a granular view in accuracy while significantly increasing latency. Based on
of the performance, we examined each application’s test data this analysis, a 60-second sliding window was chosen as it
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2233
TABLEVII
EXPERIMENT3-PERFORMANCEOFDIFFERENTAPPLICATIONSFOREACHCOUNTRYFORCATEGORY-LEVELCLASSIFICATION
WITHASLIDINGWINDOWLENGTHOF60SECONDS
TABLEVIII
EXPERIMENT4-PERFORMANCEOFDIFFERENTAPPLICATIONSFOREACHCOUNTRYFORAPPLICATION-LEVELCLASSIFICATIONFORA
SLIDINGWINDOWLENGTHOF60SECONDS
strikesabalancebetweencapturingsufficientdataforaccurate
classification and maintaining low latency for practical real-
world application. It can be seen that poorer accuracy was
obtained for the Whatsapp_files application at the category
level (see Table V) with the combined data from all three
countries; this could stem from the different sizes of the
files that were used when capturing the network traffic.
AfterremovingtheWhatsapp_filesapplication’sdatafromthe
training and test samples, the overall category-level accuracy
results improved from 93.80% to 96.20%, and the overall
application-level accuracy results improved from 86.50% to
88.60%.
The experiments were conducted on a system with the
Fig.6. Comparativeanalysisofvariousmodelsforexperiment1-2.
following configuration: a single NVIDIA TITAN X (Pascal)
GPU,6CPUcores,125.21GBofRAM,and12.0GBofGPU average RAM utilization was 11.56%. The average prediction
memory. The average CPU utilization during the experiments time for 1,000 instances was 0.0639 seconds, and the training
was 8.37%, the average GPU utilization was 4.69%, and the time per epoch was approximately 38 seconds.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

2234 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
TABLEIX
CHARACTERISTICSOFTHEISCXVPN2016DATASETSUBSET
TABLEX
EXPERIMENTS5&6-PERFORMANCEOFDIFFERENTAPPLICATIONSFORCATEGORY-ANDAPPLICATION-LEVELCLASSIFICATION
The bar chart in Fig. 6 compares our proposed method’s The baseline LSTM model (denoted as LSTM 80 40 20)
performance with that of the method of Vu et al. [29] and used for comparison consists of a sequential architecture with
a method with baseline LSTM model. As can be seen, an 80-neuron LSTM layer, followed by a 40-neuron LSTM
our proposed method outperforms the others on all metrics. layer, and a 20-neuron dense layer. This architecture also
The significant difference in application-level performance includes three dropout layers, each with a dropout rate of
indicates that our method captures granular patterns more 0.5, and uses the features proposed in this paper. The worst
effectively than the other two method, reflecting its superior performance of the three was obtained by the model of
capability in detailed pattern recognition. Vu et al. [29], as depicted in the graph.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2235
Fig.7. Performanceofthemodelstrainedoncountry-specificdataforvariousslidingwindowlengths(Y-axis).
TABLEXI
EXPERIMENT7-PERFORMANCEONIOTDATAFORSLIDINGWINDOWSOFVARIOUSLENGTHS(OCTOBER23)
TABLEXII
EXPERIMENT7-PERFORMANCEONIOTDATAFORSLIDINGWINDOWSOFVARIOUSLENGTHS(OCTOBER24)
Fig.8. Performanceofthemodelstrainedontheentiredatasetforprolongedslidingwindowlengths(Y-axis).
Experiments 3-4: Classification of Network Traffic at the categories. The classification accuracy and F1-score results
Category- and Application-Level for Each Country for the three models trained respectively on traffic from
|          |                  |             |                    | Japan, Canada, | and England | are presented | in Table VII. | In  |
| -------- | ---------------- | ----------- | ------------------ | -------------- | ----------- | ------------- | ------------- | --- |
| In these | two experiments, | models were | trained separately |                |             |               |               |     |
foreachcountry,i.e.,trainedandtestedononecountry.Inthe the fourth experiment, there were 17 labels, i.e., one for each
|                   |            |              |                        | application. | The classification | accuracy | and F1-score | results |
| ----------------- | ---------- | ------------ | ---------------------- | ------------ | ------------------ | -------- | ------------ | ------- |
| third experiment, | there were | four labels, | i.e., four application |              |                    |          |              |         |
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

2236 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
Fig.9. HTTPprotocoltagsarevisibleinthepayloadofdata.
forthethreemodelstrainedontrafficfromJapan,Canada,and In the fifth experiment, there were six labels, i.e., six
England respectively are presented in Table VIII. The results application categories. The classification accuracy and F1-
forsmallerslidingwindowsarepresentedinFig. 7.Ascanbe score results are presented in Table X; as can be seen, the
seen, in most cases the accuracy and F1-score results improve overall accuracy was 97.30% when the length of the sliding
as the size of the sliding window increases. window was 60 seconds. As seen in the table, the accuracy
|     |     |     |     | of our approach | at the | category level | was lower for Spotify; |
| --- | --- | --- | --- | --------------- | ------ | -------------- | ---------------------- |
Experiments 5-6: Classification of Network Traffic at the this could be due to Spotify’s streaming format (audio) which
| Category- | and Application-Level | for Non-VPN-Encrypted |     |              |         |                    |                    |
| --------- | --------------------- | --------------------- | --- | ------------ | ------- | ------------------ | ------------------ |
|           |                       |                       |     | differs from | that of | the other recorded | streaming services |
| Traffic   |                       |                       |     | (video).     |         |                    |                    |
In these two experiments, a subset of non-VPN traffic from In the sixth experiment, there were 21 labels, i.e., one
the ISCXVPN2016 datset was used; the characteristics of for each application. The classification accuracy and F1-score
the subset are presented in Table IX. In both experiments, results are presented in Table X; as can be seen, the overall
we considered files in which the traffic was present for at accuracy was 93.40% when the length of the sliding window
| least 300 | seconds, i.e., at least | five minutes | of recording. | was 60 seconds. |     |     |     |
| --------- | ----------------------- | ------------ | ------------- | --------------- | --- | --- | --- |
Please note: In these two experiments, as there were multiple To see the impact of the last four features (i.e., feature
files per application, we calculated weighted accuracy. Also, numbers 44 to 47), we reran these two experiments with-
as mentioned earlier, we use all the features mentioned in out those four features and obtained 95.5% (compared to
Table III in these experiments. 97.30%) accuracy in category classification (experiment five)
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2237
Fig.10. SyntaxoftheFTPprotocolisvisibleinthepayloadofdata.
and 83.60% (compared to 93.40%) accuracy in application data from a larger number of applications and from different
classification (experiment six). This shows that application- geographical locations,which isbettersuitedtotoday’s appli-
level accuracy drops significantly after removing the last four cations, and used it to demonstrate the effectiveness of our
features,whichshowsthemajorcontributionofthosefeatures. proposed approach. To demonstrate the generic and universal
Note that to obtain a granular view of the performance, we natureofourapproach,wealsoassessedourapproach’sability
examined each application’s test data against the model; the to identify applications in non-VPN-encrypted network traffic
results can be found in Table X. (experiments 5 & 6) as well as IoT devices; the results of
We also represent the top 10 features for each experiment thisexperiment(experiment7)arepresentedattheendofthis
in the Appendix. section).
We used a sliding window time-series approach which
VI. DISCUSSION enablesourmethodtoidentityanytypeoftrafficwithlessdata
Prior research [16], [29], [31] only demonstrated the thanthatneededbyothermethods,i.e.,thenumberofseconds
proposedmethod’seffectivenessontheexistingdataset,which of traffic needed is equal to the length of the sliding window.
haslimitations.Hereweproducedanewbalanceddatasetwith In other approaches one might need to wait for the flow’s
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

2238 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
Fig.11. PCAPshowsmultipleflowswithwell-knowndomainnamesandports.
TABLEXIII TABLEXIV
MOSTIMPORTANTFEATURESINEXPERIMENT1 MOSTIMPORTANTFEATURESINEXPERIMENT2
completionorforacertainnumberofpacketstobeexchanged,
whichcanoftenbetimeconsuming.Ouraiminproposingthis
approach was to provide a time-series-based approach which in existing flow-based approaches if there are 10 flows in the
is generic in nature and can be applied to different network traffictherewillbe10datainstances,whereasinourapproach,
scenarios, irrespective of the domain (e.g., IoT and computer the number of data instances can vary based on the time;
network), protocol (e.g., TCP and UDP), and the type of therefore, we were unable to compare the performance of our
encryption (e.g., VPN-encrypted, TLS-encrypted, and non- approach directly with the performance of existing methods.
encrypted). As our approach differs from existing approaches However,theaccuracy reportedinthispaperiscomparable or
in that it is based on time series, we could not directly betterthantheaccuracy obtained byother methods inmostof
comparethemethods’accuracyinourperformanceevaluation; the examined scenarios.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2239
TABLEXV TABLEXVII
MOSTIMPORTANTFEATURESINEXPERIMENT3(JAPAN) MOSTIMPORTANTFEATURESINEXPERIMENT3(CANADA)
TABLEXVIII
MOSTIMPORTANTFEATURESINEXPERIMENT4(JAPAN)
TABLEXVI
MOSTIMPORTANTFEATURESINEXPERIMENT3(ENGLAND)
| from October  | 23 and 24          | are presented | in Tables  | XI and XII   |
| ------------- | ------------------ | ------------- | ---------- | ------------ |
| respectively. | In this experiment | we            | removed    | the features |
| (for example, | fw_1250_packets)   | that had      | a standard | deviation    |
| value of      | zero, since they   | had no impact | on the     | performance  |
| and created   | an error (division | by zero)      | when       | performing   |
Experiment 7: Classification of IoT Device Type standardization. Also, as mentioned earlier we included the
In this experiment, we used a subset of the IoTTrace [17] last four features mentioned in Table III in this experiment.
dataset (specifically, traffic fromOctober 23 and 24). We took WenotethatalthoughweusedtwodifferentNetatmodevices,
intoaccountIoTdeviceswhosenetworktrafficlastedformore the model was able to bifurcate their traffic correctly despite
than3000seconds(i.e.,50minutes)totraintwomodels(each both devices coming from the same manufacturer.
modelwastrainedforaday).Weused8000secondsoftraffic To see the impact of the last four features (i.e., feature
from each IoT device in the experiment. We were unable to numbers 44 to 47), we reran this experiment for a sliding
use the entire dataset, because the data was not continuous, windowof60secondswithoutthosefourfeaturesandobtained
as is needed for training in our approach. However, our aim 97.80% (compared to 97.80%) and 98.90% (compared to
was only to perform a proof of concept demonstrating the 99.80%) accuracy for the October 23 and October 24 datasets
applicability of our approach on a different type of dataset. respectively. This shows that removing the last four features
The results of the two models trained and tested on traffic had no, or very minimal, impact on performance in this case.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore.  Restrictions apply.

2240 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
TABLEXIX TABLEXXII
MOSTIMPORTANTFEATURESINEXPERIMENT4(ENGLAND) MOSTIMPORTANTFEATURESINEXPERIMENT6
TABLEXXIII
MOSTIMPORTANTFEATURESINEXPERIMENT7(OCTOBER23)
TABLEXX
MOSTIMPORTANTFEATURESINEXPERIMENT4(CANADA)
TABLEXXI
MOSTIMPORTANTFEATURESINEXPERIMENT5 TABLEXXIV
MOSTIMPORTANTFEATURESINEXPERIMENT7(OCTOBER24)
VII. CONCLUSION
application- and category-levels. To evaluate our approach we
In this paper, we proposed a time-series-based approach created a new dataset that consists of the traffic of differ-
for the classification of VPN-encrypted network traffic at the ent applications captured from three different geographical
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

KOTAKetal.:VPN-ENCRYPTEDNETWORKTRAFFICCLASSIFICATIONUSINGATIME-SERIESAPPROACH 2241
Algorithm 1 Feature Extraction fromaparticularcountryandtestitagainstdatafromdifferent
1: Input: countries.
(cid:129) TSV_file: TSV file containing parsed packet data
(cid:129) window_length: List of time window lengths in
APPENDIX
seconds(e.g.30,40,50,60etc.)forfeatureextraction
2: Output: The tables below present the 10 most important features
(cid:129) features_df: Dataframe containing extracted features for each experiment. The “Difference (%)” column in each
3: Algorithm: table represents the difference between the baseline validation
4: Load parsed packet data from TSV file into dataframe accuracy (with all features) and the new validation accuracy
5: Determine packet direction based on source port (without the feature mentioned).
6: Initialize an empty list for statistics
7: for each time sample in window_length do REFERENCES
8: Extract data sample within the specified time window
[1] Statista.“Topic:Internetusageworldwide.”[Online].Available:https://
from dataframe
www.statista.com/topics/1145/internet-usage-worldwide/#topicHeader_
9: Compute time delta features: _wrapper
(cid:129) Bidirectional delta ratios between consecutive pack- [2] R.Subramanian,“ThegrowthofglobalInternetcensorshipandcircum-
ets: (r Δ bi t ) i = Δ Δ t t in,i v p e . n 6 t , io 2 n 0 : 11 A . survey,” Commun. Int. Inf. Manag. Assoc., vol. 11, no. 2,
out,i+1
(cid:129) Ingoing delta ratios between consecutive packets: [3] F. Li, A. A. Niaki, D. Choffnes, P. Gill, and A. Mislove, “A large-
(r Δ in t ) i = Δ Δ t in t i , n i , + i 1 s S c p a e l c e ia a l na In ly te si r s es o t f G de ro p u lo p ye D d a t t r a af C fi o c m d m iff u e n re ., n 2 ti 0 a 1 ti 9 o , n p p p r . ac 1 t 3 ic 0 e – s 1 ,” 44 in . Proc.ACM
(cid:129) Outgoing delta ratios between consecutive packets: [4] N. Weaver, C. Kreibich, and V. Paxson, “Redirecting DNS for Ads
(r Δ ou t t) i = Δ Δ t o t u o t u ,i t, + i 1 a (F nd OC p I r ) o , fi 2 t, 0 ” 1 i 1 n ,p P . ro 1 c 2 . . USENIX Workshop Free Open Commun. Internet
10: Compute packet size features: [5] A. M. Kakhki et al., “Identifying traffic differentiation in mobile
(cid:129) Bidirectionalsizeratiosbetweenconsecutivepackets: networks,”inProc.InternetMeas.Conf.,2015,pp.239–251.
(r s b i i ze ) i = siz s e iz o e ut i , n i , + i 1 [6] T “M .G o a n r i r to et r t i , n L g . n E e . t S w e o t r e k nar n e e s u k t i r , a L li . ty M : . A Per s e u s r , v L ey .C o . n Bo tr n a a f , fi a c nd di E ff . e P r . en D ti u a a t r io te n ,
(cid:129) Ingoing size ratios between consecutive packets: detection,”IEEECommun.SurveysTuts.,vol.20,no.3,pp.2486–2517,
(r s i i n ze ) i = si s z i e z i e n i , n i , + i 1 [7] R 3r . d S Q . ua R r a t. m , a 2 n 0 , 18 L . . Evdokimov, E. Wurstrow, J. A. Halderman, and
(cid:129) Outgoing size ratios between consecutive packets: R.Ensafi,“InvestigatinglargescaleHTTPSinterceptioninKazakhstan,”
(r s o i u ze t) i = si s z i e z o e u o t u ,i t, + i 1 [8] M in . P T r . o K c. h A an C , M J. I D nt e e B rn la e s t io M , e G a . s. M C . o V n o f. e , lk 2 e 0 r 2 , 0 A , . p C p. .S 12 n 5 o – er 1 e 3 n 2 , . C.Kanich,and
11: Compute accumulated packet size features: N. Vallina-Rodriguez, “An empirical analysis of the commercial VPN
(cid:129) Accumulated (cid:2) bidirectional size ratios: ecosystem,”inProc.InternetMeas.Conf.,2018,pp.443–456.
i
(r(cid:2)bi size ) i = (cid:2) i j j + = = 1 1 1 s s i i z z e e o i u n t , , j j [9] M V. . P I a k x r s a o m n , , N “A . n Va a l n l a in ly a s -R is o o d f rig th u e ez p , r S iv . ac S y en a e n v d ira s t e n c e u , ri M ty . r A isk . s K o a f af a a n r, dr a o n id d
(cid:129) Accumulated ingoing size ratios: VPN permission-enabled APPs,” in Proc. Internet Meas. Conf., 2016,
(cid:2)
i pp.349–364.
(r(cid:2)in size ) i = (cid:2)j i+ = 1 1sizein,j [10] T.SharmaandM.Bashir,“Privacyappsforsmartphones:Anassessment
j=1sizein,j of users’ preferences and limitations,” in Proc. Int. Conf. Human–
(cid:129) Accumulated (cid:2) outgoing size ratios: Comput.Interact.,2020,pp.533–546.
i
(r(cid:2)ou
s
t
ize
)
i
= (cid:2)j
i j +
=
= 1
1
1
s
s
i
i
z
z
e
e
o
o
u
u
t
t
,
,
j
j
[11] J
n
.
etw
Z
o
h
r
a
k
ng
tr
,
af
X
fic
.
c
C
la
h
s
e
s
n
ifi
,
ca
Y
ti
.
on
X
,”
ia
I
n
E
g
E
,
E/
W
AC
.
M
Zh
T
o
r
u
a
,
ns.
an
N
d
etw
J
.
.
, v
W
ol
u
.
,
23
“
,
R
n
o
o
b
.
u
4
st
,
12: Compute additional features pp.1257–1270,Aug.2015.
[12] T. T. Nguyen and G. Armitage, “A survey of techniques for Internet
13: Append all computed features to the statistics list traffic classification using machine learning,” IEEE Commun. Surveys
14: end for Tuts.,vol.10,no.4,pp.56–76,4thQuart.,2008.
15: Convert the statistics list into a new dataframe (fea- [13] A. Callado et al., “A survey on Internet traffic identification,” IEEE
Commun.SurveysTuts.,vol.11,no.3,pp.37–52,3rdQuart.,2009.
tures_df)
[14] N.AlKhaterandR.E.Overill,“Networktrafficclassificationtechniques
16: Return features_df and challenges,” in Proc. IEEE 10th Int. Conf. Digit. Inf. Manag.
(ICDIM),2015,pp.43–48.
[15] H. I. Fawaz et al., “InceptionTime: Finding AlexNet for time series
classification,”DataMin.Knowl.Disc.,vol.34,no.6,pp.1936–1962,
2020.
[16] G. Draper-Gil, A. H. Lashkari, M. S. I. Mamun, and A. A. Ghorbani,
locations.Suchadatasetisneededbytheresearchcommunity,
“Characterization of encrypted and VPN traffic using time-related,”
sincewefoundthattheexistingdatasethasseverallimitations. in Proc. 2nd Int. Conf. Inf. Syst. Security Privacy (ICISSP), 2016,
We also demonstrated the generic nature of the proposed pp.407–414.
[17] A. Sivanathan et al., “Classifying IoT devices in smart environments
approach by evaluating it in several other scenarios, such as
using network traffic characteristics,” IEEE Trans. Mobile Comput.,
classification of non-VPN-encrypted traffic and IoT device vol.18,no.8,pp.1745–1759,Aug.2018.
type.Itshouldalsobenotedthatalongwithorganizationsand [18] “Service name and transport protocol port number registry.” 2019.
[Online]. Available: https://www.iana.org/assignments/service-names-
ISPs,methods ofthistype canalsobeused byadversaries for
port-numbers/service-names-port-numbers.xhtml?&amp;page=1
reconnaissance of their targets. In future research, we plan to [19] P. Schneider, TCP/IP Traffic Classification Based on Port Numbers,
apply our approach in scenarios where there is network traffic HarvardUniv.,Cambridge,MA,USA,1997.
[20] G.ChengandS.Wang,“Trafficclassificationbasedonportconnection
flowing simultaneously from different applications within the
pattern,” in Proc. Int. Conf. Comput. Sci. Service Syst. (CSSS), 2011,
same VPN tunnel. We also plan to train our approach on data pp.914–917.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.

2242 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.2,APRIL2025
[21] Q.Zhang,Y.Ma,J.Wang,andX.Li,“UDPtrafficclassificationusing [36] S. Lv, C. Wang, Z. Wang, S. Wang, B. Wang, and Y. Zhang, “AAE-
most distinguished port,” in Proc. 16th Asia–Pac. Netw. Oper. Manag. DSVDD:Aone-classclassificationmodelforVPNtrafficidentification,”
Symp.,2014,pp.1–4. Comput.Netw.,vol.236,Nov.2023,Art.no.109990.
[22] M.Finsterbusch,C.Richter,E.Rocha,J.-A.Muller,andK.Hanssgen, [37] G. Abbas, U. Farooq, P. Singh, S. S. Khurana, and P. Singh, “Feature
“A survey of payload-based traffic classification approaches,” IEEE engineeringandensemblelearning-basedclassificationofVPNandnon-
Commun. Surveys Tuts., vol. 16, no. 2, pp.1135–1156, 2nd Quart., VPN-based network traffic over temporal features,” SN Comput. Sci.,
2013. vol.4,no.5,p.546,2023.
[23] H.-K.Lim,J.-B.Kim,K.Kim,Y.-G.Hong,andY.-H.Han,“Payload- [38] Z. Wang et al. “An effective real-time traffic classification method
basedtrafficclassificationusingmulti-layerLSTMinsoftwaredefined using convolutional neural network.” 2023. [Online]. Available:
networks,”Appl.Sci.,vol.9,no.12,p.2550,2019.[Online].Available: https://ouci.dntb.gov.ua/en/works/4ggEk2B4/
https://www.mdpi.com/2076-3417/9/12/2550 [39] Y. Xu, J. Cao, K. Song, Q. Xiang, and G. Cheng, “FastTraffic: A
[24] F. Risso, M. Baldi, O. Morandi, A. Baldini, and P. Monclus, lightweight method for encrypted traffic fast classification,” Comput.
“Lightweight,payload-basedtrafficclassification:Anexperimentaleval- Netw.,vol.235,Nov.2023,Art.no.109965.
uation,”inProc.IEEEInt.Conf.Commun.,2008,pp.5869–5875. [40] R.T.Elmaghraby,N.M.A.Aziem,M.A.Sobh,andA.M.Bahaa-Eldin,
[25] Z. Fan and R. Liu, “Investigation of machine learning based network “Encrypted network traffic classification based on machine learning,”
traffic classification,” in Proc. Int. Symp. Wireless Commun. Syst. AinShamsEng.J.,vol.15,no.2,2024,Art.no.102361.
(ISWCS),2017,pp.1–6. [41] S.Soleymanpour,H.Sadr,andH.Beheshti,“Anefficientdeeplearning
[26] S. Özdel, Ç. Ates¸, P. D. Ates¸, M. Koca, and E. Anarım, “Payload- methodforencrypted traffic classification onthe Web,” inProc. IEEE
basednetworktrafficanalysisforapplicationclassificationandintrusion 6thInt.Conf.WebRes.(ICWR),2020,pp.209–216.
detection,”inProc.30thEur.SignalProcess.Conf.(EUSIPCO),2022, [42] A.IliyasuandH.Deng,“Semi-supervisedencryptedtrafficclassification
pp.638–642. withdeepconvolutionalgenerativeadversarialnetworks,”IEEEAccess,
[27] J.KotakandY.Elovici,“IoTdeviceidentificationusingdeeplearning,” vol.8,pp.118–126,2019.
inProc.Comput.Intell.SecurityInf.Syst.Conf.,2019,pp.76–86. [43] R. Nigmatullin, A. Ivchenko, and S. Dorokhin, “Differentiation of
[28] M.Lotfollahi,M.J.Siavoshani,R.S.H.Zade,andM.Saberian,“Deep sliding rescaled ranges: New approach to encrypted and VPN traffic
packet:Anovelapproachforencryptedtrafficclassificationusingdeep detection,”inProc.Int.Conf.Eng.Telecommun.(En&T),2020,pp.1–5.
learning,”SoftComput.,vol.24,no.3,pp.1999–2012,2020. [44] B. Appiah, A. Sackey, O.-A. Kwabena, J. B. Ansuura, and P. Buah,
[29] L.Vuetal.,“Timeseriesanalysisforencryptedtrafficclassification:A “Fusion dilated CNN for encrypted Web traffic classification,” Int. J.
deep learning approach,” in Proc. IEEE 18th Int. Symp. Commun. Inf. Netw.Security,vol.24,pp.733–740,Jul.2022.
Technol.(ISCIT),2018,pp.121–126. [45] D. Wei, F. Shi, and S. Dhelim, “A self-supervised learning model for
[30] S. Soleymanpour, H. Sadr, and M. N. Soleimandarabi, “CSCNN: unknown internet traffic identification based on surge period,” Future
Cost-sensitiveconvolutionalneuralnetworkforencryptedtrafficclassi- Internet,vol.14,p.289,Oct.2022.
fication,”NeuralProcess.Lett.,vol.53,no.5,pp.3497–3523,2021. [46] M.Pathmaperuma,Y.Rahulamathavn,S.Dogan,andA.Kondoz,“Deep
[31] G. Aceto, D. Ciuonzo, A. Montieri, and A. Pescapé, “DISTILLER: learningforencryptedtrafficclassificationandunknowndatadetection,”
Encryptedtrafficclassificationviamultimodalmultitaskdeeplearning,” Sensors,vol.22,p.7643,Oct.2022.
J.Netw.Comput.Appl.,vols.183–184,Jun.2021,Art.no.102985. [47] Y. Li, F. Wang, and S. Chen, “VPN traffic identification based on
[32] M. Al-Fayoumi, M. Al-Fawa’reh, and S. Nashwan, “VPN and non- tunneling protocol characteristics,” in Proc. IEEE CCET, Aug. 2022,
VPNnetworktrafficclassificationusingtime-relatedfeatures,”Comput. pp.150–156.
MaterialsContinua,vol.72,no.2,p.12,2022. [48] Y. Mirsky, T. Doitshman, Y. Elovici, and A. Shabtai, “KitSune: An
[33] S.Roy,T.Shapira,andY.Shavitt,“FastandleanencryptedInternettraf- ensemble of autoencoders for online network intrusion detection,” in
ficclassification,”Comput.Commun.,vol.186,pp.166–173,Mar.2022. Proc.Netw.Distrib.Syst.SecuritySymp.,2018,pp.1–8.
[34] Z.Shi,N.Luktarhan,Y.Song,andG.Tian,“BFCN:Anovelclassifica- [49] C. Szegedy, S. Ioffe, V. Vanhoucke, and A. A. Alemi, “Inception-v4,
tionmethodofencryptedtrafficbasedonBERTandCNN,”Electronics, inception-ResNet and the impact of residual connections on learning,”
vol.12,no.3,p.516,2023. inProc.31stAAAIConf.Artif.Intell.,2017,pp.4278–4284.
[35] S. Ramraj and G. Usha, “Hybrid feature learning framework for the [50] K.He,X.Zhang,S.Ren,andJ.Sun,“Deepresiduallearningforimage
classification of encrypted network traffic,” Connection Sci., vol. 35, recognition,”inProc.IEEEConf.Comput.Vis.PatternRecognit.,2016,
no.1,2023,Art.no.2197172. pp.770–778.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:33:31 UTC from IEEE Xplore. Restrictions apply.