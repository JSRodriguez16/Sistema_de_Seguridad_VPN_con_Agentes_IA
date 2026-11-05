ReceivedAugust1,2021,acceptedAugust10,2021,dateofpublicationAugust16,2021,dateofcurrentversionAugust20,2021.
DigitalObjectIdentifier10.1109/ACCESS.2021.3105000
DarkDetect: Darknet Traffic Detection and
Categorization Using Modified Convolution-Long
Short-Term Memory
MUHAMMADBILALSARWAR ,MUHAMMADKASHIFHANIF ,RAMZANTALIB ,
MUHAMMADYOUNAS ,ANDMUHAMMADUMERSARWAR
DepartmentofComputerScience,GovernmentCollegeUniversity,Faisalabad38000,Pakistan
Correspondingauthor:MuhammadKashifHanif(mkashifhanif@gcuf.edu.pk)
ABSTRACT Darknetiscommonlyknownastheepicenterofillegalonlineactivities.Ananalysisofdarknet
traffic is essential to monitor real-time applications and activities running over the Darknet. Recognizing
network traffic bound to unused Internet addresses has become undeniably significant for identifying and
examining malicious activities on the internet. Since there are no authentic hosts or devices in an unused
addressblock,anyobservednetworktrafficmustbetheaftereffectofmisconfigurationfromspoofedsource
addressed and other frameworks that monitor unused address space. However, the recent advancements
in artificial intelligence allow digital systems to detect and identify darknet traffic autonomously. In this
paper, we propose a generalized approach for darknet traffic detection and categorization using Deep
Learning. We examine the state-of-the-art complex dataset, which provides excessive information about
the darknet traffic and perform data preprocessing. Next, we analyze diverse feature selection techniques
to select optimal features for darknet traffic detection and categorization. We apply fine-tuned machine
learning (ML) algorithms which include Decision Tree (DT), Gradient Boosting (GB), Random Forest
Regressor(RFR),andExtremeGradientBoosting(XGB)onselectedfeaturesandcomparetheperformance.
Next,weapplymodifiedConvolution-LongShort-TermMemory(CNN-LSTM)andConvolution-Gradient
Recurrent Unit (CNN-GRU) deep learning techniques to recognize the network traffic more accurately.
The results demonstrate that the proposed approach outperforms the existing approaches by yielding the
maximum accuracy of 96% of darknet traffic detection and 89% of darknet traffic categorization through
XGBasafeatureselectionapproachandCNN-LSTMarecognitionmodel.
INDEX TERMS Characterization, darknet traffic, deep learning, encrypted traffic, machine learning,
Tor,VPN.
I. INTRODUCTION network, allows users to gain access to hidden Darknet
Networktrafficmonitoringandanalysisarechallengingsince resources. This technique implements second-generation
it helps to improve network performance, minimize your onion routing. Basically, in this routing, a circuit is built
attack surface, enhance security, and improve the resources incrementally, one hop by one hop. Usually, the darknet
management[1]–[3].Networktraffictradeincrimessuchas traffic is treated as misconfiguration because the host is
viruses,contractkillers,poisons,anddrugshappensthrough acting as illegitimate. A deep analysis of darknet traffic is
theDarknet[4].Theaddressspacewhichisnotusedonthe significantlyessentialtomonitorreal-timeapplications.The
internet is called darknets or network telescopes. Darknet analysis of darknet traffic provides complete information to
trafficisnotspeculatedovertheinternettointeractwithother thecybersecurityspecialists,andotherIToperatorsaboutthe
computersandonlypassivelyacceptsincomingpacketswith- servicesexploitedbyattackersorvulnerabletosomeattack
outgeneratingoutgoingpackets[5].Torisavirtualcomputer [6]–[9]. Researchers now focus on analyzing the darknet
traffic, specifically detecting Tor applications to determine
The associate editor coordinating the review of this manuscript and the malicious activities [10]–[14]. To achieve the detection
approvingitforpublicationwasDianaGratielaBerbecaru . objective, authors used ML, and Deep Learning (DL)
VOLUME9,2021 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 113705

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
techniques [15]–[18]. Authors in [5], [19], [20] explored evaluationandresults.SectionVIsummarizesthepaperand
whether graph mining techniques can help to uncover such providesthefuturedirection.
macroscopiccoordinatedeventsindarknettraffic.Thedark-
net traffic is getting complex daily, and malicious activities II. RELATEDWORK
suchasphysicalthreats,salesdatatheft,fraudulentactivity, This section presents the detailed related work based on
phishingattacks,andscams,DDoSattacks,illicitlinks,Illicit darknet traffic and activities monitoring and exploration.
Drugs,andterrorismvarydaybyday[21]–[24]. The related work methods are composed of the latest arti-
LimitationsofExistingStudy:Thestate-of-the-artworkhas ficial intelligence techniques and other safety networking
beendoneby[15]onthedetectionandcategorizationofdark- frameworks.
nettrafficandtakenasthebasepaper.Thedatasetusedinthis The authors in [25] proposed a system that tracks port
workcontains alargenumber ofmissing valuesthatcannot scanningactionpatternsbetweenseveralexploredportsand
beignored.Theauthorsinthisstudy[15]havenotexplained classifybasicconfigurationsoftheexaminedclusterofports.
howtheyhandledthislimitation.Thereexistmultiplerecom- Thisapproachisclaimedtobecompletelyautomaticwiththe
mendedmethodstohandlemissingvaluestoproducemean- latesttechniquesofgraphmodelingandtextmining.Itpro-
ingful information. The other limitation in this work is that vides complete information to the cybersecurity specialists
the authors selected 22 features from 61 extracted features anddifferentinformationtechnology(IT)operatorsaboutthe
usingonlyonefeatureselectiontechnique.Thedeeplearning servicesexploitedbyattackersorvulnerabletosomeattack.
approachtestedon15bestfeaturesoutof22selectedfeatures Thistechniquestandsouttobemoreusefulsinceitbecomes
that seem biased. Furthermore, the overall f-score is 86%, easy to identify the targets of attacks. The proposed system
but the f-score of traffic categories Browsing, E-mail, File- is tested on the massive dataset of Darknet or an internet
Transfer, and VOIP are 51%, 67%, 75%, and 61% respec- telescope.
tively, which are significantly less, that affects the overall The researchers in [16] highlighted the difficulties that
performance of the recognition model. To the best of our security agencies face to track the criminal activities going
knowledge,thisistheonlyotherbaselineworkinthecurrent on the Darknet. Analyzing the images in a massive amount
literature. Also, we used the dataset of that study through a ontheDarknetisatime-consumingtaskandstillnotaneffi-
fair comparison with them to make sense. Other studies on cient method. To encounter this issue, the researchers study
Darknettrafficusedlimitedoroutdateddatasets. different automated image classification methods which are
Thispaperanswersthefollowingresearchquestions.RQ1: basedonSemanticAttentionKeypointFiltering(SAKF)and
Theinterpretationofmodelsdetectingnetworktrafficheavily proposedanapproachthatcanomitthenon-relevanttopogra-
dependuponallnetworkfeature.Howisafeatureselection phiesatthedeeppixel-levelsuchthatallthepixelsarebeing
technique affect the performance of the detection model? filteredoutwhicharenotrelevanttotheforensicprocess.This
RQ2:Howtoassesstheimpactsofdatavolumeanddataset system is achieved by compounding the salience maps with
balance in using a deep learning approach to detect darknet Bag of Visual Words (BoVW). The researchers tested out
traffic? RQ3: How to detect darknet traffic accurately at theirsystemonacustom-madedatasetthatcontainstheTor
multi-level classification as Tor, Non-Tor, VPN, Non-VPN image.TheirfindingconcludesthatMobileNetv1,Resnet50,
andtrafficcategories:Audio-Stream,chat,mail,p2p,VOIP, andBoVW,composedofdenseSIFTdescriptors,standoutto
Video-Stream, Transfer, and Browsing using custom-tuned bemoreproficientthanotherapproaches.Theauthorsin[10]
machinelearninganddeeplearningpredictivemodels? proposedamachinelearning-basedthreatidentificationsys-
Keeping in sight the above research questions, this paper teminwhichthemachinelearningclassifiersaretrainedon
makesthefollowingcontributions: darknettraffic.ThenetworktrafficflowovertheDarknetis
1) Propose a customized LSTM based CNN eitherconsideredtobemaliciousorwronglyconfigured.The
(CNN-LSTM) deep learning approach for detecting darknettrafficflowcomprisesmultipleintimidations,includ-
andidentifyingdarknetnetworktraffic. ing DDoS attacks, botnets, spoofing, probes, and scanning
2) Apply pre-processing data operations, including data attacks.Theresearchersexaminedthedarknetnetworktraffic
imputations,featureselection,anddatabalancing. flowconfiguredatSURFnetandminedothernetworkprop-
3) Provide a set of customized parameters for accu- ertiesofthetrafficflow.Theresearchersappliedasupervised
rately recognizing traffic type and application cate- machine learning algorithm Random Forest and a concept
gories using CNN-LSTM with promising Accuracy, driftdetectorthatshowsthesystemisefficientlycapableof
Precision,Recall,andF-score. detectingbenignandmaligntrafficandproficientlydetecting
4) Present comparative results using various machine hiddenthreatsoverthenetwork.
learning,deeplearningtechniques,andstate-of-the-art The researchers in [17] emphasized the difficulties faced
toshowtheeffectivenessoftheproposedapproach. by the security investigators and law enforcers while moni-
Thepaper’sremainderisstructuredasfollows:SectionII toringandexaminingthenetworktrafficflowattheDarknet.
demonstrates the relevant work to darknet traffic analysis Arenownedmethodforsemanticalanalysisofmarketlisting
anddetection.SectionIVprovidestheproposedapproachfor istopmodeling,butthistechniqueisshowslaginthecapa-
darknettrafficanalysisanddetection.SectionVprovidesthe bilitytorecordthevisualimagesfoundinthoselisting.The
113706 VOLUME9,2021

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
TABLE1. Comparativesummaryofstate-of-the-artmethodsforDarknettrafficrecognition.
researchers proposed a machine learning-based framework theDarknet,resultinginaidforthecybercrimeinvestigation
basedonsupervised(CNN)andunsupervised(LDA)learning agencies.
techniquestoinferthemassivedatasetcontainingimagesto The authors in [38] performed a Tor network in-depth
encounterthisissue.Thus,thismethodstandsouttobemore review.Theauthorsmentionallthedarknetprosandconsand
proficient in investigating the material being transmitted on thenatureofdarknetnetworktrafficflow.Theanonymization
darknetmarkets.Theauthorsin[18]proposedanaturallan- oftheDarknetisconsideredoneoftheessentialfeaturessince
guageprocessing(NLP)basedsystemfordetectingthelegal itallowsuserstoanonymouslyperformanyactivity,whether
andillegalcommunicationsbeingcarriedontheDarknet.The itislegalornot.Theauthorsalsoreviewtheissuesofanony-
researchers claim to fulfill the gaps that are present in the mous payments with cryptocurrency. The authors conclude
current NLP-based models. The model detects the legal or this extensive review by enlightening the future aspects and
illegaltextontheDarknetbycomparingwebsiteswithsimilar challengesoftheDarknet.Theresearchersin[26]proposed
content. The model takes a drug-relevant website as a test aSAKFsystemthatclassifiestheimagesbyanalyzingonly
case. The model compares text and linguistic used on both pertinentportionsoftheimagecompoundingsaliencemaps
websitesandthendistinguishesthembasedonPOStagsand such that it chooses only those areas of the image which
theavailabilityoftheirtermedobjectsinWikipedia. havemorenoticeableinformationwithBoVW.Thissystemis
Cybercrimes, illegal drugs dealing, and cryptocurrency testedonsevendifferentpubliclyavailabledatasetsonwhich
markets are top trending over the Darknet recently. The thesystemshowedanaccuracygainof1.64to15.73higher
authors study and identify the research done over darknet than baseline approaches which used BoVW using dense
technologies and specifications to highlight the gaps and SIFT(Scale-InvariantFeatureTransform)descriptors.
difficulties in exploiting the illegal activities going over the Theresearchersin[27]proposedaprogrammedmodelthat
Darknet. The researchers in [36] discussed the limitations recognizes the activities being done on the Tor network by
anddifficultiesfacedwhileidentifyingthecriminalactivities analyzing the activities’ snapshots. The researchers in [12]
overthecybernetworkastheDarknetisprotectedwithspe- combinedthreeproficientalgorithmswiththehelpofarecti-
cificnetworkencryptionsandconfigurationsarehiddenfrom ficationnetworktoenhancethealgorithm’stextrecognition
searchengines.Thisnotonlyhelpsgovernmentagenciespur- procedure. The authors evaluated this composition of algo-
suetheculprits,butitwillalsohelpkeeppeaceinsociety.The rithms on four text datasets and TOICO-1K image datasets
researchersalsofocusedontheinternetforcrimes,exploiting ofTorforanalyzingthetext.Theproposedmodelshowsthe
Tor-servicesusers’identityanddrugdealing,andproposeda highestproficiencyovertheICDAR2015dataset.
systemtoinspectandexploreunidentifiedonlineillegitimate The researchers in [11], [39], [40] proposed a framework
markets. The authors in [37] review the latest technologies based on network flow features for Tor traffic analysis and
and researches that encounter the vulgar activities going on multi-levelcataloging.Themodelcandetecttheanonymous
theDarknet,whichincludesmoneylaundry,childpornogra- trafficL1,L2,andL3onmultipleplatforms,includingmobile
phy, and illegitimate drug trafficking. However, cryptocur- andPC.Theauthorclaimthattheimpactoftime-relatedfea-
rency is required for transactions over the Darknet, which turesishigherthanthatofthenon-time-relatedfeaturesonthe
includesbitcoins.Theauthorsreviewandhighlightthelatest mobileplatform,whileitistheoppositeonthePCplatform.
studiesthatdeanonymizetheculpritsandtheiractivitiesover Theresearcherin[28]proposedamachinelearningapproach
VOLUME9,2021 113707

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
to text classification over the Russian language-based Tor the machine effectively, and deep learning classifier’s per-
sites.Theproposedmodelanalyzesthetextandcategorizeit formance [41]. Missing data refers to the data that is not
fortheforensicspurpose.Foraquickanalysis,weconclude available (Null) or inapplicable or infinite data or the data
state-of-the-artstudiesinTable1. collectioneventthatneverhappened.Sincethedatasetisvast,
weremovetherowsthatcontainmissinginformation.Itwill
III. DATASETSELECTION not have any effect on the learning process [42]. Table 4
Otherdatasetsexist,suchasAnon17andDarknetUsageText providesthesamplesofmissingdatahighlightedinboldtext.
Address (DUTA)-10K-GVIS Lab (2019). Anon17 dataset This data can lead to misleading results of the machine and
consists of three anonymity tools: Tor, I2P, and deeplearningclassifier.
| JonDonym       | [13].     | DUTA      | dataset     | contains  |             | 25 categories |       |         |                          |     |     |     |     |     |     |
| -------------- | --------- | --------- | ----------- | --------- | ----------- | ------------- | ----- | ------- | ------------------------ | --- | --- | --- | --- | --- | --- |
| of legal       | and       | illegal   | activities  | with      | over        | 10,367        | manu- |         |                          |     |     |     |     |     |     |
|                |           |           |             |           |             |               |       | TABLE4. | Missingdatainthedataset. |     |     |     |     |     |     |
| ally labeled   | onion     | domains.1 |             | We select | recently    | published     |       |         |                          |     |     |     |     |     |     |
| dataset        | [15] that | is an     | amalgamated | of        | previously  | two           | iden- |         |                          |     |     |     |     |     |     |
| tical datasets | [30],     | and       | [29]        | with the  | enhancement | of            | VPN   |         |                          |     |     |     |     |     |     |
andTor-trafficcategories.Thisdatasetcontains85features,
| including   | 2 labels,      | traffic_type: |               | Tor,       | Non-Tor,  | VPN,       | Non-    |     |     |     |     |     |     |     |     |
| ----------- | -------------- | ------------- | ------------- | ---------- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| VPN and     | app_category:  |               | Audio-Stream, |            | Browsing, |            | Chat,   |     |     |     |     |     |     |     |     |
| E-mail,     | P2P, Transfer, |               | Video-Stream, |            | VOIP.     | Table 2    | shows   |     |     |     |     |     |     |     |     |
| the traffic | categories     | and           | number        | of samples |           | of each    | traffic |     |     |     |     |     |     |     |     |
| type. Table | 3              | shows each    | app           | category   | with      | the number | of      |     |     |     |     |     |     |     |     |
samples.
|     |     |     |     |     |     |     |     | B. DATABALANCING |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Thedatasetbalancingisoneofthevitalpartsofdataprepos-
TABLE2. Trafficcategory.
sessing.Itoptimizesthedatasetsothateveryclasspresentin
thedatasetmaygetrecognizedtobeprocessedandpredicted
|     |     |     |     |     |     |     |     | accurately. | According |     | to the | dataset | structure | used | for this |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------ | ------- | --------- | ---- | -------- |
approach,thereishighunbalancingbetweenclassesinstance,
|     |     |     |     |     |     |     |     | leading        | to significantly |        | less          | F1-Score | but      | higher   | accuracy   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | ------ | ------------- | -------- | -------- | -------- | ---------- |
|     |     |     |     |     |     |     |     | and precision. |                  | We use | SMOTE         | [8],     | [43] for | data     | balancing. |
|     |     |     |     |     |     |     |     | SMOTE          | over-samples     |        | the instances |          | of the   | majority | class,     |
TABLE3. Applicationcategory. meanwhilekeepingtheoriginalrepresentationofthedataset.
WeincreasetheTorclassby20%sinceTorwastheonlyclass
withtheleastinstances.
|     |     |     |     |     |     |     |     | C. FEATURESELECTION |           |           |           |             |           |        |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --------- | --------- | --------- | ----------- | --------- | ------ | ---------- |
|     |     |     |     |     |     |     |     | We apply            | the       | Principle | Component |             | Analysis  | (PCA)  | [6],       |
|     |     |     |     |     |     |     |     | DT [6],             | [44], and | XGB       | [45]      | for feature | selection |        | to extract |
|     |     |     |     |     |     |     |     | 20 important        |           | features. | A DT      | consists    | of        | roots, | branches,  |
|     |     |     |     |     |     |     |     | nodes, and          | leaves.   | One       | branch    | consists    | of        | nodes  | and com-   |
prisesonefeature.Theoccurrenceofeachfeaturefromroot
|     |     |     |     |     |     |     |     | to leaves | depicts | the importance |     | of  | each | feature. | Similarly, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------------- | --- | --- | ---- | -------- | ---------- |
IV. DARKDETECT
theXGBclassifierselectstheoptimalfeaturesusingfeature
| Figure | 1 represents | the | proposed | approach, |     | starting | with |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | -------- | --------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
importancecriteria.Itselectsthefeaturebasedonathreshold
| feature   | extraction | from | the       | data lake,   | and | finding   | out the |               |     |               |     |        |         |         |         |
| --------- | ---------- | ---- | --------- | ------------ | --- | --------- | ------- | ------------- | --- | ------------- | --- | ------ | ------- | ------- | ------- |
|           |            |      |           |              |     |           |         | (i.e., 0.08). | If  | the threshold |     | is too | low, no | feature | will be |
| essential | features   | for  | detecting | each traffic |     | category. | From    |               |     |               |     |        |         |         |         |
selected.
| the table | 2 and | 3, we | came | to the | point | that data | is an |            |     |              |     |              |     |          |          |
| --------- | ----- | ----- | ---- | ------ | ----- | --------- | ----- | ---------- | --- | ------------ | --- | ------------ | --- | -------- | -------- |
|           |       |       |      |        |       |           |       | We compare |     | the selected |     | 20 essential |     | features | with the |
imbalanceineachtrafficcategoryandappcategory.Datais
|                    |         |           |              |            |       |                |        | performance  | of    | 22 selected | important |                | features  | of               | the state- |
| ------------------ | ------- | --------- | ------------ | ---------- | ----- | -------------- | ------ | ------------ | ----- | ----------- | --------- | -------------- | --------- | ---------------- | ---------- |
| balanced           | through | the       | oversampling | technique. |       | Next,          | at the |              |       |             |           |                |           |                  |            |
|                    |         |           |              |            |       |                |        | of-the-art   | study | as shown    | in        | Table          | 5. The    | state-of-the-art |            |
| classification     |         | level, we | detect       | traffic    | types | and categories |        |              |       |             |           |                |           |                  |            |
|                    |         |           |              |            |       |                |        | study uses   | 15    | features    | in the    | classification |           | step from        | these      |
| their applications |         | through   | different    | ML         | and   | DL techniques  |        |              |       |             |           |                |           |                  |            |
|                    |         |           |              |            |       |                |        | 22 features, | while | we          | use 20    | features       | extracted | through          | the        |
explainedinsectionIV-D.
belowfeatureselectiontechniques.
Principalcomponentanalysis(PCA)isanunsupervised
A. HANDLINGMISSINGDATA
|              |           |     |         |         |        |         |       | algorithm | that     | produced | linear   | combinations    |     | of    | the actual |
| ------------ | --------- | --- | ------- | ------- | ------ | ------- | ----- | --------- | -------- | -------- | -------- | --------------- | --- | ----- | ---------- |
| This section | describes |     | various | ways to | handle | missing | data. |           |          |          |          |                 |     |       |            |
|              |           |     |         |         |        |         |       | features  | [6]. The | new      | features | are orthogonal, |     | which | means      |
Missingdatahandlingisacriticallyessentialtasktoimprove
|     |     |     |     |     |     |     |     | that they | are not | correlated |     | with each | other. | Furthermore, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | --- | --------- | ------ | ------------ | --- |
1http://gvis.unileon.es/dataset/duta-darknet-usage-text-addresses-10k/
thosefeaturesarerankedinorderoftheirexplainedvariance.
| 113708 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
FIGURE1. Taxonomyoftheproposedapproach.
Below are the machine learning classifiers that we used optimization. The core XGB algorithm is parallelizable,
toselectthefeaturesbasedontheirimportanceaccordingto whichmeansitdoesparallelizationwithinasingleDT.XGB
accuracy. performstreepruning,thestoppingcriteriafortreesplitting
DecisionTreeClassifierworksforbothregressionaswell within the GB Machines framework, which is greedy and
as classification problems [6], [44], [46]. The decision is depends upon the negative loss criterion at the split point.
simpletounderstand,interpretandvisualizeandcanhandle XGBadmitssparsefeaturesforinputsbyautomaticallylearn-
un-prepared data. Nonlinear parameters do not affect the ingthebestmissingvaluedependingupontraininglossand
performanceoftheDT.Theperformanceofthedecisioncan efficientlyhandlingvarioussparsitypatternsinthedata.This
bemeasuredusingentropy(unpredictability)andinformation approachsupportsbothregressionandclassificationpredic-
gain.Thelesstheentropyandhighestinformation,theclas- tivemodelingproblems.
sifierismoreaccurate.
XGBClassifier is a decision-tree-based ensemble ML D. CLASSIFICATION
algorithmthatusesagradient-boostingframework[45].XGB The dataset contains traffic types such as Tor, Non-Tor,
improves upon the base Gradient Boosting Machines (GB) VPN,Non-VPN,andapp_categoriessuchasAudio-Stream,
framework through algorithmic enhancements and systems Browsing, Chat, E-mail, P2P, Transfer, Video-Stream,
VOLUME9,2021 113709

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
TABLE5. Importantfeatureselectedbytheproposedapproach. more mathematical-intensive cause of logarithmic function,
whichisusedtocalculatingit.
|     |     |     |     |     |     |     | CNN-LSTM          |      | performs | multiple |              | tasks | to deliver  | a pro-   |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- | -------- | -------- | ------------ | ----- | ----------- | -------- |
|     |     |     |     |     |     |     | ficient accuracy. |      | CNN      | layer    | extracts     | the   | features    | of input |
|     |     |     |     |     |     |     | data, and         | LSTM | supports |          | the sequence |       | prediction. | The      |
CNN-LSTMmodelismainlyutilizedfordatainputinseries,
justasincontinuousnetworktrafficflow.
|     |     |     |     |     |     |     |               | h      | = H(W | x            | +W      | h +b | )          | (1)       |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ----- | ------------ | ------- | ---- | ---------- | --------- |
|     |     |     |     |     |     |     |               |        | t     | hx           | t hh    | t−1  | h          |           |
|     |     |     |     |     |     |     |               | p      | = W   | y            | +b      |      |            | (2)       |
|     |     |     |     |     |     |     |               |        | t     | hy t−1       | y       |      |            |           |
|     |     |     |     |     |     |     | The Equations |        | 1 and | 2 represents |         | main | computing  | equa-     |
|     |     |     |     |     |     |     | tions where   | series | input | is           | denoted | by   | x , series | output is |
t
|     |     |     |     |     |     |     | denotedbyy | t ,hiddenmemorycellsaredenotedbyh |     |     |     |     |     | t ,weight |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------------------- | --- | --- | --- | --- | --- | --------- |
matricesaredenotedbyW,andbiasvectorsaredenotedbyb.
|     |     |     |     |     |     |     | Following | equations |     | computer | the | hidden | state | of memory |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | --- | ------ | ----- | --------- |
cells:
|     |     |     |     |     |     |     | i = σ(W | x     | +W   | h +W | c      | +b   | )   | (3)      |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---- | ---- | ------ | ---- | --- | -------- |
|     |     |     |     |     |     |     | t       | ix t  | hh   | t−1  | ic t−1 |      | i   |          |
|     |     |     |     |     |     |     | f = σ(W | x     | +W   | h +W | c      | +b   | )   | (4)      |
|     |     |     |     |     |     |     | t       | fx t  | hh   | t−1  | fc t−1 |      | f   |          |
|     |     |     |     |     |     |     | c = f   | ∗c +i | ∗g(W | x    | +W     | h +W | c   | +b ) (5) |
VOIP. We apply modified deep learning techniques: t t t−1 t cx t hh t−1 cc t−1 c
|     |     |     |     |     |     |     | o = σ(W | x   | +W  | h +W | c   | +b  | )   | (6) |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- | --- | --- | --- | --- |
Convolution-Long Short Term Memory (CNN-LSTM) and t ox t hh t−1 oc t−1 o
Convolution-GatedRecurrentUnit(CNN-GRU)torecognize h = o ∗h(c ) (7)
|                |     |              |     |             |     |             | t t | t   |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| traffic types. | We  | also analyze | the | recognition | of  | the traffic |     |     |     |     |     |     |     |     |
categories using the machine learning techniques: GB, DT, CNN layer extracts the features of input data, and GRU
RFR,andXGBclassifiers.Wetuneandselecttheparameters supportsthesequenceprediction.CNN-GRUisanimprove-
basedontheefficiencyofthemodel(i.e.,F1-score).Weselect mentinthebasicfunctionalityofthestandardrecurrentneu-
the combination that was providing us best results. In the ralnetwork.BasicRNNfacesavanishinggradientproblem
results,weshowthetablewithallcombinationsandconclude
thatGRUencountersbyupdatingandresettingthegate.GRU
thebestresults. also maintains the ability to maintain the information for a
GradientBoostingClassifier(GB)producesaprediction longtimeordiscardirrelevantinformationtomakeefficiently
model in the form of a set of weak classifier models, like accuratepredictions.
decisiontrees.Successivedecisiontreesaregeneratedduring
the learning/training process. The algorithm builds the 1st z =δ(W(t)x +Uzh
|          |         |           |               |     |           |          |     |     | t   |     | t   | t−1 ) |     | (8) |
| -------- | ------- | --------- | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | ----- | --- | --- |
| model to | predict | the value | and calculate |     | the loss, | the dif- |     |     |     |     |     |       |     |     |
ference between the 1st model’s result and the true value. The Equation 8 represents the gate updation process in
Moreover, after the first step, the second classifier model is whichx t isinsertedintothenetworkunit,W(z)representsit’s
then built to predict the loss. Until a satisfactory result is ownweight.h t−1)containstheinformationfortheprevious
(
achieved,thiswholeprocesscontinues.TheGBistofindnew unitandgetsmultipliedbyownweightU(z).
| trees that | minimize | the loss | iteratively. | The | loss function | is  |     |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
usedtomeasurehowmanyerrorsaremadebytheclassifier. r =δ(W(r)x +Urh ) (9)
|        |        |           |       |     |             |     |     |     | t   |     | t   | t−1 |     |     |
| ------ | ------ | --------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Random | Forest | Regressor | (RFR) | is  | an ensemble | ML  |     |     |     |     |     |     |     |     |
technique proficient in classification and regression tasks The Equation 9 represents the reset part functionality
| using multiple |     | DT and bagging, | which | is  | a statistical | tech- | ofGRU. |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | ----- | --- | ------------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
nique.Baggingandboostingalgorithm,these2arethemost
(cid:48)
well-known ensemble techniques that aim to tackle high h =z (cid:12)h h−1 +(1−z )(cid:12)h (10)
|          |      |           |          |     |                |     |     |     | t t |     |     | t   | t   |     |
| -------- | ---- | --------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bias and | high | variance. | An Rf is | not | just averaging | the |     |     |     |     |     |     |     |     |
prediction of decision trees; it uses two main vital con- TheEquation10representsthefinalmemoryataparticular
| cepts that | give | it title random: | (1) | while | building | decision | timestep. |     |     |     |     |     |     |     |
| ---------- | ---- | ---------------- | --- | ----- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
trees,randomsamplingoftrainingwasobserved,(2)random
subgroups features for splitting nodes. Rf builds multiple V. EVALUATIONANDRESULTS
decision trees and aggregates their predictions to get more We use Precision, Recall, F-score, and Accuracy evaluation
stable and accurate results rather than relying on individual metrics to compare the proposed approach’s performance.
decision trees. Entropy uses the probability of a particular Table6showstheparameterswithtunedvaluesofmodified
result to decide how the tree nodes should branch. En is a convolution-LSTMtoachievethebestaccuracyandloss.
| 113710 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
TABLE6. Tunedparameters.
A. HARDWAREENVIRONMENT
The experiment’s computing environment is set as Intel(R) FIGURE2. AccuracycurvesoftheproposedDarkDetectapproach.
Corei7,8thGenerationwith16GBRAM,Windows10OS,
| and Python | version 3.7.6. | For parameter | tuning, we used |     |     |     |     |
| ---------- | -------------- | ------------- | --------------- | --- | --- | --- | --- |
TABLE9. Performanceevaluationmetricsshowscomparisonof
| GPUs from | Google Colab | and Tesla | lab. Table 7 shows |     |     |     |     |
| --------- | ------------ | --------- | ------------------ | --- | --- | --- | --- |
classificationtechniques.ThePrecision,Recall,andF-scoreareinthe
the computing environment in which the experiment is rangeof[0-1]with1beingthehighest.Thehighestvaluesareinbold.
conducted.
TABLE7. Computingenvironment.
|     |     |     |     | learning classifiers. | The results | of ML classifiers | are based |
| --- | --- | --- | --- | --------------------- | ----------- | ----------------- | --------- |
on20best-selectedfeaturesandafterdatabalancingthrough
Resultsareextractedbasedonfeatureselectionapproaches
|     |     |     |     | SMOTE. Table | 9 shows | that RFR achieves | 71% F-score |
| --- | --- | --- | --- | ------------ | ------- | ----------------- | ----------- |
in combination with classification techniques. For feature while GB achieves 81% F-score, which is 10% higher than
| selection, | we use PCA, | DT, and XGB. | For classification, |     |     |     |     |
| ---------- | ----------- | ------------ | ------------------- | --- | --- | --- | --- |
RFR.TheDTachieves84%F-score,whichis3%and13%
wemodifytheCNNmodelwithahiddenlayerofLSTMand
higherthanGBandRFR.Incomparison,XGBachieves85%
theCNNmodelwithahiddenlayerofGRU. F-score,whichis1%,4%,and14%higherthanDT,GB,and
RFR.AlthoughMLmodelsshowsignificantperformanceon
TABLE8. Performanceevaluationmetricsshowscomparisonof darknettrafficcategorization,categorizationstillneedssome
classificationtechniques.ThePrecision,Recall,andF-scoreareinthe
| rangeof[0-1]with1beingthehighest.Thehighestvaluesareinbold. |     |     |     | improvement. |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- |
TABLE10. Performanceevaluationmetricsshowacomparisonoffeature
selectionandclassificationtechniquesasacombination.ThePrecision,
Recall,andF-scoreisintherangeof[0-1],with1beingthehighest.The
highestvaluesareinbold.
B. DARKNETTRAFFICDETECTION
| We extensively | analyze | traffic categorization | and conclude |     |     |     |     |
| -------------- | ------- | ---------------------- | ------------ | --- | --- | --- | --- |
thatthefeatureselectionapproachXGBselectsthebestfea-
turethanDTandPCAandimprovesaccuracywiththeCNN-
| LSTM classifier. | We apply        | the same        | hierarchy for traffic |     |     |     |     |
| ---------------- | --------------- | --------------- | --------------------- | --- | --- | --- | --- |
| detection        | and present the | best results in | Table 8. As shown     |     |     |     |     |
| in Table         | 8, we achieve   | 1%, 4%, and     | 3% better Precision,  |     |     |     |     |
recall,andF-scorethroughCNN-LSTMthanCNN-GRUon
trafficTor,Non-Tor,VPN,andNon-VPN.Figure2showsthe Table 10 shows that CNN-GRU performs 2% better than
resultsofourtechnique. CNN-LSTM on features selected by PCA. In comparison,
CNN-LSTMperforms4%betterthanCNN-GRUonfeatures
C. DARKNETTRAFFICCATEGORIZATION thatDTselects.Meanwhile,inconclusion,theCNN-LSTM
Table 10, 9 and table 11 represents results on layer2 with modelsignificantlyimproves9%thanCNN-GRUonfeatures
traffic categories Audio-Stream, Chat, Email, P2P, VOIP, selectedbyXGB.So,intable11wecompareourbestresults
Video-Stream,Transfer,andBrowsing.Indarknettrafficcat- extractedthroughCNN-LSTMonfeatureswhichareselected
egorization, we first analyze the performance of machine byXGBwiththestate-of-the-artstudy[15].
| VOLUME9,2021 |     |     |     |     |     |     | 113711 |
| ------------ | --- | --- | --- | --- | --- | --- | ------ |

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
FIGURE3. AccuracyandLosscurvesofDarkDetect.
Figure3showstheresultsofourtechnique.Itisconcluded training.SMOTEimprovestherepresentationofTorclassand
that we achieve overall 3% better accuracy, while with the classificationaccuracy.
lossof0.43,whichis0.07lowerthanthestudy[15].
VI. CONCLUSION
Inthispaper,anapproachisproposedtodetectandcategorize
TABLE11. Comparisonresultsonevaluationmetricsofproposed
approachandstate-of-the-artstudy[15].Key:Precision-p,F-score-F1, darknettraffic.Theproposedapproachconsistsofadvanced
Recall-R.
|     |     |     |     |     |     |     | fine-tuned           | machine | learning |      | algorithms |             | and a convolutional |         |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------- | -------- | ---- | ---------- | ----------- | ------------------- | ------- |
|     |     |     |     |     |     |     | neural network-based |         |          | deep | learning   | classifier. | These               | classi- |
fiersaretestedfortheclassificationoverstate-of-the-art[30]
dataset,whichcontains8categoriesofnetworktrafficpack-
ets.Amongthetestedmachinelearningclassifiers,theclas-
|     |     |     |     |     |     |     | sifier XGB | stands | out | to be | the most | proficient |     | than other |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----- | -------- | ---------- | --- | ---------- |
competitorsbyyieldingaproficientaverageF-scoreof85%.
Moreover,themodifiedclassifierCNN-LSTMandtheXGB
|     |     |     |     |     |     |     | feature selection |             | approach |           | outperform |           | the state-of-the-art |        |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | -------- | --------- | ---------- | --------- | -------------------- | ------ |
|     |     |     |     |     |     |     | study [15]        | with        | a gain   | of 3%     | accuracy   |           | on average.          | In the |
|     |     |     |     |     |     |     | future, it        | is intended |          | to extend |            | this work | by testing           | and    |
combiningtheclassifiersinanensembleapproachandfurther
| As shown | in  | Table | 11, we | achieve | 44%, 17%, | 10% 1%, |     |     |     |     |     |     |     |     |
| -------- | --- | ----- | ------ | ------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
creatingapersonalizedgenerateddatasetthatisbeingloaded
| 1%, and | 27% | better | F-score | on Browsing, | File-Transfer, |     |           |         |             |     |      |     |          |            |
| ------- | --- | ------ | ------- | ------------ | -------------- | --- | --------- | ------- | ----------- | --- | ---- | --- | -------- | ---------- |
|         |     |        |         |              |                |     | with more | precise | information |     | that | is  | required | to train a |
P2P,Video-Streaming,andVOIPtrafficcategoriesthanbase
classifierwithmoreproficiency.
| paper. This                                           | is  | because | of 20  | important | selected | features. |            |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | ------- | ------ | --------- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Meanwhile,                                            | we  | got     | 5% and | 10% fewer | F-score  | on Chat   |            |     |     |     |     |     |     |     |
| andAudio-Streamingtrafficcategoriesthanbasepaper.This |     |         |        |           |          |           | REFERENCES |     |     |     |     |     |     |     |
comparative analysis proves that the proposed approach [1] M.Mittal,C.Iwendi,S.Khan,andA.R.Javed,‘‘Analysisofsecurity
andenergyefficiencyforshortestroutediscoveryinlow-energyadaptive
| XGB-CNN-LSTM |     | increased | 73% | F-score | on 6 | traffic cate- |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | ------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
clusteringhierarchyprotocolusingLevenberg-Marquardtneuralnetwork
gorieswhiletheminimallossofonly15%thanthestate-of-
andgatedrecurrentunitforintrusiondetectionsystem,’’Trans.Emerg.
the-artstudy[15]. Telecommun.Technol.,vol.32,no.6,p.e3997,Jun.2021.
Finally, after a comprehensive analysis and experiment, [2] W.Ahmed,F.Shahzad,A.R.Javed,F.Iqbal,andL.Ali,‘‘WhatsApp
|            |         |     |                |          |           |     | network | forensics: | Discovering |     | the IP | addresses | of suspects,’’ | in Proc. |
| ---------- | ------- | --- | -------------- | -------- | --------- | --- | ------- | ---------- | ----------- | --- | ------ | --------- | -------------- | -------- |
| this paper | answers |     | the identified | research | question. | The |         |            |             |     |        |           |                |          |
11thIFIPInt.Conf.NewTechnol.,MobilitySecur.(NTMS),Apr.2021,
| answertoRQ1wouldbethatdarknettrafficcanbedetected |     |     |     |     |     |     | pp.1–7. |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
using the proposed deep detect pipeline, which consists of [3] C. Iwendi, S. U. Rehman, A. R. Javed, S. Khan, and G. Srivastava,
‘‘SustainablesecurityfortheInternetofThingsusingartificialintelligence
XGBbasedfeatureselection,databalancingusingSMOTE,
|                    |     |       |           |     |            |        | architectures,’’ |     | ACM Trans. | Internet | Technol., |     | vol. 21, no. | 3, pp.1–22, |
| ------------------ | --- | ----- | --------- | --- | ---------- | ------ | ---------------- | --- | ---------- | -------- | --------- | --- | ------------ | ----------- |
| and classification |     | using | CNN-LSTM. |     | The answer | to RQ2 | Jun.2021.        |     |            |          |           |     |              |             |
wouldbethatXGBfeatureselectionalongwithCNN-LSTM K.Misata,‘‘TheTorproject:Aninsideview,’’XRDS,Crossroads,ACM
[4]
Mag.Students,vol.20,no.1,pp.45–47,Sep.2013.
| affects positively |     | predicts | the | darknet | traffic. | RQ3 can be |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | ------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] F.Soro,M.Allegretta,M.Mellia,I.Drago,andL.M.Bertholdo,‘‘Sensing
answeredsincetheminorityclassinstancesofTortrafficare
thenoise:Uncoveringcommunitiesindarknettraffic,’’inProc.Medit.
being misclassified in the testing process due to inadequate Commun.Comput.Netw.Conf.(MedComNet),Jun.2020,pp.1–8.
| 113712 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

M.B.Sarwaretal.:DarkDetect:DarknetTrafficDetectionandCategorization
[6] A.R.Javed,Z.Jalil,S.A.Moqurrab,S.Abbas,andX.Liu,‘‘Ensem- [25] S.Lagraa,Y.Chen,andJ.François,‘‘Deepminingportscansfromdark-
bleAdaBoostclassifierforaccurateandfastdetectionofbotnetattacks net,’’Int.J.Netw.Manage.,vol.29,no.3,p.e2065,May2019.
inconnectedvehicles,’’Trans.Emerg.Telecommun.Technol.,p.e4088, [26] E. Fidalgo, E. Alegre, L. Fernández-Robles, and V.González-Castro,
Aug.2020. ‘‘ClassifyingsuspiciouscontentinTordarknetthroughsemanticattention
[7] C.Iwendi,Z.Jalil,A.R.Javed,T.ReddyG.,R.Kaluri,G.Srivastava,and keypointfiltering,’’Digit.Invest.,vol.30,pp.12–22,Sep.2019.
O.Jo,‘‘KeySplitWatermark:Zerowatermarkingalgorithmforsoftware [27] R. Biswas, V. González-Castro, E. Fidalgo, and E. Alegre, ‘‘Percep-
protectionagainstcyber-attacks,’’IEEEAccess,vol.8,pp.72650–72660, tual image hashing based on frequency dominant neighborhood struc-
2020. ture applied to Tor domains recognition,’’ Neurocomputing, vol. 383,
[8] S.U.Rehman,M.Khaliq,S.I.Imtiaz,A.Rasool,M.Shafiq,A.R.Javed, pp.24–38,Mar.2020.
Z. Jalil, and A. K. Bashir, ‘‘DIDDOS: An approach for detection and [28] I. D. Buldin and N. S. Ivanov, ‘‘Text classification of illegal activities
identificationofdistributeddenialofservice(DDoS)cyberattacksusing ononionsites,’’inProc.IEEEConf.RussianYoungResearchersElectr.
gated recurrent units (GRU),’’ Future Gener. Comput. Syst., vol. 118, Electron.Eng.(EIConRus),Jan.2020,pp.245–247.
pp.453–466,May2021. [29] G. Draper-Gil, A. H. Lashkari, M. S. I. Mamun, and A. A. Ghorbani,
[9] S. I. Imtiaz, S. U. Rehman, A. R. Javed, Z. Jalil, X. Liu, and ‘‘CharacterizationofencryptedandVPNtrafficusingtime-relatedfea-
W.S.Alnumay, ‘‘DeepAMD: Detection and identification of Android tures,’’inProc.2ndInt.Conf.Inf.Syst.Secur.Privacy,2016,pp.407–414.
malwareusinghigh-efficientdeepartificialneuralnetwork,’’FutureGener. [30] A. H. Lashkari, G. Draper-Gil, M. S. I. Mamun, and A. A. Ghorbani,
Comput.Syst.,vol.115,pp.844–856,Feb.2021. ‘‘Characterization of Tor traffic using time based features,’’ in Proc.
[10] S.Kumar,H.Vranken,J.V.Dijk,andT.Hamalainen,‘‘Deepinthedark: ICISSp,2017,pp.253–262.
Anovelthreatdetectionsystemusingdarknettraffic,’’inProc.IEEEInt. [31] T. Tsikrika, A. Popescu, and J. Kludas, ‘‘Overview of the Wikipedia
Conf.BigData(BigData),Dec.2019,pp.4273–4279. image retrieval task at ImageCLEF 2011,’’ in Proc. CLEF, Notebook
[11] L.Wang,H.Mei,andV.S.Sheng,‘‘Multilevelidentificationandclassi- Papers/Labs/Workshop,vol.4,2011,p.5.
ficationanalysisofToronmobileandPCplatforms,’’IEEETrans.Ind. [32] M. W. Al-Nabki, E. Fidalgo, E. Alegre, and L. Fernández-Robles,
Informat.,vol.17,no.2,pp.1079–1088,Feb.2021. ‘‘ToRank:IdentifyingthemostinfluentialsuspiciousdomainsintheTor
[12] P.Blanco-Medina,E.Fidalgo,E.Alegre,andF.Jánez-Martino,‘‘Improv- network,’’ExpertSyst.Appl.,vol.123,pp.212–226,Jun.2019.
ingtextrecognitioninTordarknetwithrectificationandsuper-resolution [33] E. Fidalgo, E. Alegre, V. González-Castro, and L.Fernández-Robles,
techniques,’’inProc.9thInt.Conf.Imag.CrimeDetectionPrevention, ‘‘Boostingimageclassificationthroughsemanticattentionfilteringstrate-
2019,pp.32–37. gies,’’PatternRecognit.Lett.,vol.112,pp.176–183,Sep.2018.
[13] A. Montieri, D. Ciuonzo, G. Aceto, and A. Pescapé, ‘‘Anonymity [34] A.G.Weber,‘‘TheUSC-SIPIimagedatabaseversion5,’’USC-SIPIRep.,
services Tor, I2P, JonDonym: Classifying in the dark (web),’’ IEEE vol.315,no.1,1997.
Trans. Dependable Secure Comput., vol. 17, no. 3, pp.662–675, [35] P. B. Medina, E. F. Fernández, E. A. Gutiérrez, and M.W.AlNabki,
May2020. ‘‘Detectingtextualinformationinimagesfromoniondomainsusingtext
[14] A. Montieri, D. Ciuonzo, G. Bovenzi, V. Persico, and A. Pescapé, ‘‘A spotting,’’inProc.39thJornadasdeAutomática,Actas,Badajoz,Spain,
dive into the dark web: Hierarchical traffic classification of anonymity 2018,pp.975–982.
tools,’’ IEEE Trans. Netw. Sci. Eng., vol. 7, no. 3, pp.1043–1054, [36] V.Adewopo,B.Gonen,S.Varlioglu,andM.Ozer,‘‘Plungeintotheunder-
Mar.2019. world:Asurveyonemergenceofdarknet,’’inProc.Int.Conf.Comput.Sci.
[15] A.H.Lashkari,G.Kaur,andA.Rahali,‘‘DIDarknet:Acontemporary Comput.Intell.(CSCI),Dec.2019,pp.155–159.
approachtodetectandcharacterizethedarknettrafficusingdeepimage [37] W.Han,V.Duong,L.Nguyen,andC.Mier,‘‘Darknetandbitcoinde-
learning,’’ in Proc. 10th Int. Conf. Commun. Netw. Secur., Nov. 2020, anonymization:Emergingdevelopment,’’inProc.ZoomingInnov.Con-
pp.1–13. sum.Technol.Conf.(ZINC),May2020,pp.222–226.
[16] E. F. Fernandez, R. A. V. Carofilis, F. J. Martino, and P. B. Medina, [38] A.Nastuła,‘‘DilemmasrelatedtothefunctioningandgrowthofDarknet
‘‘ClassifyingsuspiciouscontentinTorDarknet,’’2020,arXiv:2005.10086. andtheonionrouternetwork,’’J.Sci.PapersSocialDevelop.Security,
[Online].Available:http://arxiv.org/abs/2005.10086 vol.10,no.2,pp.3–10,Apr.2020.
[17] A.BermanandC.L.Paul,‘‘MakingsenseofDarknetmarkets:Automatic [39] K. Shahbar and A. N. Zincir-Heywood, ‘‘Traffic flow analysis of Tor
inference of semantic classifications from unconventional multimedia pluggable transports,’’ in Proc. 11th Int. Conf. Netw. Service Manage.
datasets,’’inProc.Int.Conf.Hum.-Comput.Interact.Cham,Switzerland: (CNSM),Nov.2015,pp.178–181.
Springer,2019,pp.230–248. [40] K.ShahbarandA.N.Zincir-Heywood,‘‘Benchmarkingtwotechniques
[18] L. Choshen, D. Eldad, D. Hershcovich, E. Sulem, and O. Abend, forTorclassification:Flowlevelandcircuitlevelclassification,’’inProc.
‘‘The language of legal and illegal activity on the Darknet,’’ 2019, IEEESymp.Comput.Intell.CyberSecur.(CICS),Dec.2014,pp.1–8.
arXiv:1905.05543.[Online].Available:http://arxiv.org/abs/1905.05543 [41] A.R.Javed,S.U.Rehman,M.U.Khan,M.Alazab,andH.U.Khan,
[19] A.Basit,M.Zafar,X.Liu,A.R.Javed,Z.Jalil,andK.Kifayat,‘‘Acom- ‘‘Betalogger:Smartphonesensor-basedside-channelattackdetectionand
prehensivesurveyofAI-enabledphishingattacksdetectiontechniques,’’ textinferenceusinglanguagemodelinganddenseMultiLayerneuralnet-
Telecommun.Syst.,vol.76,no.1,pp.1–16,2020. work,’’ACMTrans.AsianLow-ResourceLang.Inf.Process.,vol.20,no.5,
[20] A.Basit,M.Zafar,A.R.Javed,andZ.Jalil,‘‘Anovelensemblemachine pp.1–17,Jun.2021.
learningmethodtodetectphishingattack,’’inProc.IEEE23rdInt.Multi- [42] M. Asad, M. Asim, T. Javed, M. O. Beg, H. Mujtaba, and S. Abbas,
topicConf.(INMIC),Nov.2020,pp.1–5. ‘‘DeepDetect:Detectionofdistributeddenialofserviceattacksusingdeep
[21] C.Mo,W.Xiaojuan,H.Mingshu,J.Lei,K.Javeed,andX.Wang,‘‘Anet- learning,’’Comput.J.,vol.63,no.7,pp.983–994,Jul.2020.
work traffic classification model based on metric learning,’’ Comput., [43] R. Blagus and L. Lusa, ‘‘Class prediction for high-dimensional class-
Mater.Continua,vol.64,no.2,pp.941–959,2020. imbalanceddata,’’BMCBioinf.,vol.11,no.1,pp.1–17,Dec.2010.
[22] B.Xiong,K.Yang,J.Y.Zhao,andK.Q.Li,‘‘Robustdynamicnetwork [44] Y.P.P.A.F.PavelandB.C.Soares,‘‘Decisiontree-baseddatacharacter-
traffic partitioning against malicious attacks,’’ J. Netw. Comput. Appl., izationformeta-learning,’’inProc.IDDM-2002,vol.111,2002.
vol.87,pp.20–31,Jun.2017. [45] A. Abbasi, A. R. Javed, C. Chakraborty, J. Nebhen, W. Zehra, and
[23] C.Du,S.Liu,L.Si,Y.Guo,andT.Jin,‘‘Usingobjectdetectionnetworkfor Z.Jalil, ‘‘ElStream: An ensemble learning approach for concept drift
malwaredetectionandidentificationinnetworktrafficpackets,’’Comput., detectionindynamicsocialbigdatastreamlearning,’’IEEEAccess,vol.9,
Mater.Continua,vol.64,no.3,pp.1785–1796,2020. pp.66408–66419,2021.
[24] W.Tian,X.Ji,W.Liu,G.Liu,R.Lin,J.Zhai,andY.Dai,‘‘Defensestrate- [46] A. R. Javed, T. Baker, M. Asim, M. Beg, and A. H. Al-Bayatti,
giesagainstnetworkattacksincyber-physicalsystemswithanalysiscost ‘‘AlphaLogger:Detectingmotion-basedside-channelattackusingsmart-
constraintbasedonhoneypotgamemodel,’’Comput.,Mater.Continua, phonekeystrokes,’’Tech.Rep.,2020.
vol.60,no.1,pp.193–211,2019.
VOLUME9,2021 113713